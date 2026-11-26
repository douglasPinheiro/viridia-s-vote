# ============================================================
# FASE 02 - DADOS
# A CENTRAL DE TRIAGEM
# ============================================================

init python:

    # ========================================================
    # EVIDÊNCIAS
    # ========================================================

    PHASE02_EVIDENCES = [
        {
            "id": "E1",
            "name": "Registro de autenticação",
            "description": "Assinatura digital validada.",
            "status": "valid",
            "destination": "custody",
            "arrival_order": 3
        },
        {
            "id": "E2",
            "name": "Registro de origem",
            "description": "Integridade e origem confirmadas.",
            "status": "valid",
            "destination": "custody",
            "arrival_order": 1
        },
        {
            "id": "E3",
            "name": "Registro de transmissão",
            "description": "Origem divergente da informação.",
            "status": "invalid",
            "destination": "quarantine",
            "arrival_order": 5
        },
        {
            "id": "E4",
            "name": "Registro de processamento",
            "description": "Origem autenticada.",
            "status": "valid",
            "destination": "custody",
            "arrival_order": 2
        },
        {
            "id": "E5",
            "name": "Registro de acesso",
            "description": "Assinatura digital inválida.",
            "status": "invalid",
            "destination": "quarantine",
            "arrival_order": 6
        },
        {
            "id": "E6",
            "name": "Registro de integridade",
            "description": "Hash íntegro e confirmado.",
            "status": "valid",
            "destination": "custody",
            "arrival_order": 4
        }
    ]


    # ========================================================
    # ORDEM INICIAL DA FILA
    # ========================================================

    PHASE02_QUEUE_INITIAL_ORDER = [
        "E2",
        "E4",
        "E1",
        "E6",
        "E3",
        "E5"
    ]


    # ========================================================
    # DESTINOS
    # ========================================================

    PHASE02_DESTINATIONS = {
        "custody": {
            "id": "custody",
            "name": "Custódia",
            "description": "Evidências aprovadas para a cadeia de custódia.",
            "color": "#00FF99"
        },
        "quarantine": {
            "id": "quarantine",
            "name": "Quarentena",
            "description": "Evidências que precisam ser isoladas.",
            "color": "#FF6B6B"
        }
    }


    # ========================================================
    # SEQUÊNCIA ESPERADA DA CADEIA DE CUSTÓDIA
    # ========================================================

    PHASE02_EXPECTED_CUSTODY_ORDER = [
        "E2",
        "E4",
        "E1",
        "E6"
    ]


    # ========================================================
    # ORDEM ESPERADA DE INSPEÇÃO DA PILHA
    # LIFO
    # ========================================================

    PHASE02_EXPECTED_STACK_ORDER = [
        "E5",
        "E3"
    ]


    # ========================================================
    # EVIDÊNCIAS ESPERADAS NA QUARENTENA
    # ========================================================

    PHASE02_EXPECTED_QUARANTINE = [
        "E3",
        "E5"
    ]


    # ========================================================
    # MENSAGENS
    # ========================================================

    PHASE02_MESSAGES = {
        "queue_intro": (
            "O fluxo de entrada foi interrompido. "
            "Processar os registros respeitando a ordem de chegada."
        ),

        "queue_success": (
            "Todas as evidências foram encaminhadas corretamente."
        ),

        "stack_intro": (
            "As evidências rejeitadas foram armazenadas na pilha "
            "de contenção. A recuperação segue a regra LIFO."
        ),

        "stack_success": (
            "A pilha de contenção foi inspecionada corretamente."
        ),

        "linked_list_intro": (
            "Reconstrua a cadeia de custódia conectando as evidências "
            "aprovadas na sequência correta."
        ),

        "phase_success": (
            "Cadeia de custódia reconstruída. "
            "Integridade dos registros confirmada."
        ),

        "phase_error": (
            "A sequência não corresponde ao protocolo de custódia."
        )
    }


# ============================================================
# ESTADO DA FASE 02
# ============================================================

default phase02_queue = None
default phase02_quarantine_stack = None
default phase02_custody_list = None

# Evidências retiradas da fila
default phase02_queue_processed = []

# Evidências encaminhadas para custódia
default phase02_custody_evidences = []

# Evidências encaminhadas para quarentena
default phase02_quarantine_evidences = []

# Evidências efetivamente retiradas da pilha
default phase02_stack_processed = []

# Evidência atualmente em processamento
default phase02_current_evidence = None

default phase02_selected_destination = None

# Controle de conclusão das etapas
default phase02_queue_completed = False
default phase02_stack_completed = False
default phase02_linked_list_completed = False
default phase02_completed = False

# Etapa atual
default phase02_current_step = 1

# Feedback da interface
default phase02_feedback = ""

# Sequências de processamento
default phase02_custody_sequence = []
default phase02_quarantine_sequence = []

# Controle da Linked List
default phase02_selected_evidence = None
default phase02_linked_list_validation = False

# Reinicializações
default phase02_restart_count = 0