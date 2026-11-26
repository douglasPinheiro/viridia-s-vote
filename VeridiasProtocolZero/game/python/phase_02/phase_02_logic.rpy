# ============================================================
# FASE 02 - LÓGICA
# A CENTRAL DE TRIAGEM
# ============================================================

init python:

    # ========================================================
    # LOCALIZA EVIDÊNCIA PELO ID
    # ========================================================

    def phase02_get_evidence(evidence_id):
        for evidence in PHASE02_EVIDENCES:
            if evidence["id"] == evidence_id:
                return evidence
        return None


    # ========================================================
    # INICIALIZAÇÃO DA FASE
    # ========================================================

    def phase02_initialize():
        global phase02_queue, phase02_quarantine_stack, phase02_custody_list
        global phase02_queue_processed, phase02_custody_evidences
        global phase02_quarantine_evidences, phase02_stack_processed
        global phase02_current_evidence, phase02_selected_destination
        global phase02_queue_completed, phase02_stack_completed
        global phase02_linked_list_completed, phase02_completed
        global phase02_current_step, phase02_feedback
        global phase02_custody_sequence, phase02_quarantine_sequence
        global phase02_selected_evidence, phase02_linked_list_validation

        phase02_queue = Phase02Queue()
        phase02_quarantine_stack = Phase02Stack()
        phase02_custody_list = Phase02LinkedList()

        phase02_queue_processed = []
        phase02_custody_evidences = []
        phase02_quarantine_evidences = []
        phase02_stack_processed = []

        phase02_current_evidence = None
        phase02_selected_destination = None

        phase02_queue_completed = False
        phase02_stack_completed = False
        phase02_linked_list_completed = False
        phase02_completed = False

        phase02_current_step = 1
        phase02_feedback = ""

        phase02_custody_sequence = []
        phase02_quarantine_sequence = []

        phase02_selected_evidence = None
        phase02_linked_list_validation = False

        for evidence_id in PHASE02_QUEUE_INITIAL_ORDER:
            evidence = phase02_get_evidence(evidence_id)
            if evidence is not None:
                phase02_queue.enqueue(dict(evidence))


    # ========================================================
    # ETAPA 1 - QUEUE
    # ========================================================

    def phase02_get_next_queue_evidence():
        global phase02_current_evidence, phase02_selected_destination
        global phase02_queue_completed, phase02_feedback

        if phase02_queue is None:
            phase02_initialize()

        if phase02_queue_completed:
            phase02_feedback = PHASE02_MESSAGES["queue_success"]
            return None

        if phase02_current_evidence is not None:
            phase02_feedback = "Finalize o encaminhamento da evidência atual."
            return phase02_current_evidence

        if phase02_queue.is_empty():
            phase02_queue_completed = True
            phase02_feedback = PHASE02_MESSAGES["queue_success"]
            return None

        phase02_current_evidence = phase02_queue.dequeue()
        phase02_selected_destination = None
        phase02_feedback = ""
        return phase02_current_evidence


    def phase02_process_evidence(destination):
        global phase02_current_evidence, phase02_selected_destination
        global phase02_queue_processed, phase02_custody_evidences
        global phase02_quarantine_evidences, phase02_custody_sequence
        global phase02_quarantine_sequence, phase02_queue_completed
        global phase02_feedback

        if phase02_queue_completed:
            phase02_feedback = PHASE02_MESSAGES["queue_success"]
            return False

        if phase02_current_evidence is None:
            phase02_feedback = "Nenhuma evidência está sendo processada."
            return False

        if destination not in PHASE02_DESTINATIONS:
            phase02_feedback = "Destino inválido."
            return False

        evidence = phase02_current_evidence
        expected_destination = evidence["destination"]

        if destination != expected_destination:
            phase02_feedback = "Destino incorreto. Analise novamente as informações da evidência."
            return False

        evidence_id = evidence["id"]
        phase02_selected_destination = destination
        phase02_queue_processed.append(evidence_id)

        if destination == "custody":
            phase02_custody_evidences.append(evidence_id)
            phase02_custody_sequence.append(evidence_id)
        elif destination == "quarantine":
            phase02_quarantine_evidences.append(evidence_id)
            phase02_quarantine_sequence.append(evidence_id)
            phase02_quarantine_stack.push(dict(evidence))

        phase02_feedback = "Evidência %s encaminhada corretamente." % evidence_id
        phase02_current_evidence = None
        phase02_selected_destination = None

        if phase02_queue.is_empty():
            phase02_queue_completed = True
            phase02_feedback = PHASE02_MESSAGES["queue_success"]

        return True


    def phase02_queue_is_completed():
        return phase02_queue_completed


    # ========================================================
    # ETAPA 2 - STACK
    # ========================================================

    def phase02_get_stack_top():
        if phase02_quarantine_stack is None:
            return None
        return phase02_quarantine_stack.peek()


    def phase02_inspect_stack_evidence():
        global phase02_feedback, phase02_stack_completed, phase02_stack_processed

        if not phase02_queue_completed:
            phase02_feedback = "Conclua o processamento da fila primeiro."
            return None

        if phase02_stack_completed:
            phase02_feedback = PHASE02_MESSAGES["stack_success"]
            return None

        if phase02_quarantine_stack is None:
            phase02_feedback = "A pilha não foi inicializada."
            return None

        if phase02_quarantine_stack.is_empty():
            phase02_stack_completed = True
            phase02_feedback = PHASE02_MESSAGES["stack_success"]
            return None

        evidence = phase02_quarantine_stack.peek()
        expected_index = len(phase02_stack_processed)

        if expected_index >= len(PHASE02_EXPECTED_STACK_ORDER):
            phase02_feedback = "Não existem mais evidências para inspecionar."
            return None

        expected_id = PHASE02_EXPECTED_STACK_ORDER[expected_index]

        if evidence["id"] != expected_id:
            phase02_feedback = "A ordem de recuperação não corresponde ao protocolo LIFO."
            return None

        evidence = phase02_quarantine_stack.pop()
        phase02_stack_processed.append(evidence["id"])
        phase02_feedback = "Evidência %s inspecionada corretamente." % evidence["id"]

        if phase02_stack_processed == PHASE02_EXPECTED_STACK_ORDER:
            phase02_stack_completed = True
            phase02_feedback = PHASE02_MESSAGES["stack_success"]

        return evidence


    def phase02_stack_is_completed():
        return phase02_stack_completed


    # ========================================================
    # ETAPA 3 - LINKED LIST
    # ========================================================

    def phase02_linked_list_add(evidence_id):
        global phase02_feedback, phase02_selected_evidence
        global phase02_linked_list_validation

        if not phase02_queue_completed:
            phase02_feedback = "Conclua a etapa da fila primeiro."
            return False

        if not phase02_stack_completed:
            phase02_feedback = "Conclua a inspeção da pilha primeiro."
            return False

        if phase02_custody_list is None:
            phase02_feedback = "A lista ligada não foi inicializada."
            return False

        if evidence_id not in PHASE02_EXPECTED_CUSTODY_ORDER:
            phase02_feedback = "Esta evidência não pertence à cadeia de custódia."
            return False

        current_sequence = phase02_custody_list.to_list()

        if evidence_id in current_sequence:
            phase02_feedback = "Esta evidência já foi adicionada à cadeia."
            return False

        expected_index = len(current_sequence)
        if expected_index >= len(PHASE02_EXPECTED_CUSTODY_ORDER):
            phase02_feedback = "A cadeia já está completa."
            return False

        expected_evidence = PHASE02_EXPECTED_CUSTODY_ORDER[expected_index]
        if evidence_id != expected_evidence:
            phase02_feedback = "Sequência incorreta. Verifique a cadeia de custódia."
            return False

        phase02_custody_list.append(evidence_id)
        phase02_selected_evidence = evidence_id
        phase02_linked_list_validation = False
        phase02_feedback = "Evidência %s conectada corretamente." % evidence_id

        if phase02_custody_list.get_size() == len(PHASE02_EXPECTED_CUSTODY_ORDER):
            phase02_feedback = "Todas as evidências foram conectadas. Confirme a cadeia de custódia."

        return True


    # ========================================================
    # VALIDAR LINKED LIST / CONCLUIR FASE
    # ========================================================

    def phase02_validate_linked_list():
        global phase02_linked_list_validation, phase02_linked_list_completed
        global phase02_completed, phase02_feedback

        if not phase02_queue_completed:
            phase02_feedback = "A etapa da fila ainda não foi concluída."
            return False

        if not phase02_stack_completed:
            phase02_feedback = "A etapa da pilha ainda não foi concluída."
            return False

        if phase02_custody_list is None:
            phase02_feedback = "A lista ligada não foi inicializada."
            return False

        current_sequence = phase02_custody_list.to_list()

        if current_sequence != PHASE02_EXPECTED_CUSTODY_ORDER:
            phase02_linked_list_validation = False
            phase02_feedback = PHASE02_MESSAGES["phase_error"]
            return False

        phase02_linked_list_validation = True
        phase02_linked_list_completed = True
        phase02_completed = True
        phase02_feedback = PHASE02_MESSAGES["phase_success"]
        return True


    # ========================================================
    # GETTERS
    # ========================================================

    def phase02_get_custody_list():
        if phase02_custody_list is None:
            return []
        return phase02_custody_list.to_list()


    def phase02_get_custody_list_size():
        if phase02_custody_list is None:
            return 0
        return phase02_custody_list.get_size()


    def phase02_get_queue():
        if phase02_queue is None:
            return []
        return phase02_queue.to_list()


    def phase02_get_queue_size():
        if phase02_queue is None:
            return 0
        return phase02_queue.get_size()


    def phase02_get_quarantine_stack():
        if phase02_quarantine_stack is None:
            return []
        return phase02_quarantine_stack.to_list()


    def phase02_get_stack_size():
        if phase02_quarantine_stack is None:
            return 0
        return phase02_quarantine_stack.get_size()


    # ========================================================
    # REINICIAR FASE
    # ========================================================

    def phase02_restart():
        global phase02_restart_count
        phase02_restart_count += 1
        phase02_initialize()


    # ========================================================
    # WRAPPERS DE UI - NÃO RETORNAM VALORES PARA A SCREEN
    # ========================================================

    def phase02_ui_get_next_queue_evidence():
        phase02_get_next_queue_evidence()


    def phase02_ui_process_evidence(destination):
        phase02_process_evidence(destination)


    def phase02_ui_inspect_stack_evidence():
        phase02_inspect_stack_evidence()


    def phase02_ui_linked_list_add(evidence_id):
        phase02_linked_list_add(evidence_id)


    def phase02_ui_validate_linked_list():
        phase02_validate_linked_list()
