# ============================================================
# FASE 02 - SCREEN
# A CENTRAL DE TRIAGEM
# ============================================================

screen phase_02_challenge():

    modal True
    tag game

    $ queue_items = phase02_get_queue()
    $ stack_items = phase02_get_quarantine_stack()
    $ custody_items = phase02_get_custody_list()

    frame:
        background "#071018"
        xfill True
        yfill True
        padding (24, 18)

        vbox:
            spacing 10
            xfill True
            yfill True

            # HEADER
            hbox:
                xfill True
                spacing 20

                vbox:
                    spacing 2
                    text "CIV // CENTRAL DE TRIAGEM":
                        size 28
                        color "#00E5FF"
                        bold True
                    text "PROTOCOLO 02 // ESTRUTURAS DE DADOS":
                        size 13
                        color "#78909C"

                null

                vbox:
                    xalign 1.0
                    spacing 2
                    text "STATUS DO SISTEMA":
                        size 11
                        color "#78909C"
                    if phase02_completed:
                        text "CADEIA DE CUSTÓDIA VALIDADA":
                            size 15
                            color "#00FF99"
                            bold True
                    else:
                        text "PROCESSAMENTO EM ANDAMENTO":
                            size 15
                            color "#FFB000"
                            bold True

            frame:
                background "#16313D"
                xfill True
                ysize 2

            # NAVEGAÇÃO DE ETAPAS - TRÊS COLUNAS
            grid 3 1:
                xfill True
                spacing 8

                button:
                    xfill True
                    yminimum 75
                    background "#102630"
                    hover_background "#16404F"
                    action SetVariable("phase02_current_step", 1)
                    padding (10, 8)
                    vbox:
                        spacing 3
                        text "01 // QUEUE":
                            size 17
                            color "#00E5FF"
                            bold True
                        text "FIFO • Ordem de chegada":
                            size 11
                            color "#90A4AE"
                        if phase02_queue_completed:
                            text "STATUS: CONCLUÍDO":
                                size 11
                                color "#00FF99"
                        else:
                            text "STATUS: EM PROCESSAMENTO":
                                size 11
                                color "#FFB000"

                button:
                    xfill True
                    yminimum 75
                    background "#102630"
                    hover_background "#16404F"
                    sensitive phase02_queue_completed
                    action SetVariable("phase02_current_step", 2)
                    padding (10, 8)
                    vbox:
                        spacing 3
                        text "02 // STACK":
                            size 17
                            color "#FFB000"
                            bold True
                        text "LIFO • Último a entrar":
                            size 11
                            color "#90A4AE"
                        if phase02_stack_completed:
                            text "STATUS: CONCLUÍDO":
                                size 11
                                color "#00FF99"
                        elif phase02_queue_completed:
                            text "STATUS: DISPONÍVEL":
                                size 11
                                color "#FFB000"
                        else:
                            text "STATUS: BLOQUEADO":
                                size 11
                                color "#78909C"

                button:
                    xfill True
                    yminimum 75
                    background "#102630"
                    hover_background "#16404F"
                    sensitive phase02_stack_completed
                    action SetVariable("phase02_current_step", 3)
                    padding (10, 8)
                    vbox:
                        spacing 3
                        text "03 // LINKED LIST":
                            size 17
                            color "#00FF99"
                            bold True
                        text "Cadeia de custódia":
                            size 11
                            color "#90A4AE"
                        if phase02_linked_list_completed:
                            text "STATUS: CONCLUÍDO":
                                size 11
                                color "#00FF99"
                        elif phase02_stack_completed:
                            text "STATUS: DISPONÍVEL":
                                size 11
                                color "#FFB000"
                        else:
                            text "STATUS: BLOQUEADO":
                                size 11
                                color "#78909C"

            # ÁREA CENTRAL
            frame:
                background "#0C1922"
                xfill True
                padding (16, 12)

                vbox:
                    spacing 10
                    xfill True

                    # QUEUE
                    if phase02_current_step == 1:
                        text "ETAPA 01 // PROCESSAMENTO FIFO":
                            size 21
                            color "#00E5FF"
                            bold True
                        text "Os registros devem ser processados respeitando a ordem em que chegaram à central.":
                            size 14
                            color "#B0BEC5"

                        hbox:
                            spacing 14
                            xfill True

                            frame:
                                background "#102630"
                                xsize 320
                                padding (12, 8)
                                vbox:
                                    spacing 5
                                    text "FILA DE ENTRADA":
                                        size 15
                                        color "#00E5FF"
                                        bold True
                                    text "FRONT →":
                                        size 11
                                        color "#78909C"

                                    if queue_items:
                                        for index, item in enumerate(queue_items):
                                            if index == 0:
                                                button:
                                                    background "#205263"
                                                    hover_background "#00B8D4"
                                                    xfill True
                                                    padding (7, 5)
                                                    action Function(phase02_ui_get_next_queue_evidence)
                                                    text "[item['id']] // [item['name']]  < FRONT >":
                                                        size 12
                                                        color "#00E5FF"
                                                        bold True
                                            else:
                                                frame:
                                                    background "#173744"
                                                    xfill True
                                                    padding (7, 5)
                                                    text "[item['id']] // [item['name']]":
                                                        size 12
                                                        color "#E0F7FA"
                                    else:
                                        text "FILA VAZIA":
                                            size 13
                                            color "#00FF99"

                            frame:
                                background "#102630"
                                xfill True
                                padding (12, 8)
                                vbox:
                                    spacing 8
                                    text "REGISTRO EM ANÁLISE":
                                        size 15
                                        color "#00E5FF"
                                        bold True

                                    if phase02_current_evidence:
                                        text "[phase02_current_evidence['id']]":
                                            size 25
                                            color "#FFFFFF"
                                            bold True
                                        text "[phase02_current_evidence['name']]":
                                            size 17
                                            color "#E0F7FA"
                                        text "[phase02_current_evidence['description']]":
                                            size 13
                                            color "#B0BEC5"

                                        if phase02_current_evidence["status"] == "valid":
                                            text "ANÁLISE: REGISTRO VALIDADO":
                                                size 13
                                                color "#00FF99"
                                                bold True
                                        else:
                                            text "ANÁLISE: REGISTRO SUSPEITO":
                                                size 13
                                                color "#FF6B6B"
                                                bold True

                                        text "DESTINO DO REGISTRO":
                                            size 12
                                            color "#78909C"

                                        hbox:
                                            spacing 8
                                            button:
                                                background "#164C3C"
                                                hover_background "#1E6B50"
                                                action Function(phase02_ui_process_evidence, "custody")
                                                text "ENCAMINHAR À CUSTÓDIA":
                                                    size 13
                                                    color "#00FF99"
                                                    bold True
                                            button:
                                                background "#4A252B"
                                                hover_background "#70333B"
                                                action Function(phase02_ui_process_evidence, "quarantine")
                                                text "ENVIAR À QUARENTENA":
                                                    size 13
                                                    color "#FF6B6B"
                                                    bold True

                                    elif phase02_queue_completed:
                                        text "PROCESSAMENTO DA FILA CONCLUÍDO":
                                            size 17
                                            color "#00FF99"
                                            bold True
                                        text "Todos os registros foram processados. Avance para a etapa STACK.":
                                            size 13
                                            color "#B0BEC5"
                                    else:
                                        text "Nenhum registro selecionado.":
                                            size 13
                                            color "#78909C"
                                        text "Clique no registro FRONT da fila para retirá-lo e iniciar a análise.":
                                            size 13
                                            color "#B0BEC5"
                                        button:
                                            background "#16404F"
                                            hover_background "#1D586B"
                                            action Function(phase02_ui_get_next_queue_evidence)
                                            text "PROCESSAR PRÓXIMO REGISTRO":
                                                size 15
                                                color "#00E5FF"
                                                bold True

                    # STACK
                    elif phase02_current_step == 2:
                        text "ETAPA 02 // INSPEÇÃO LIFO":
                            size 21
                            color "#FFB000"
                            bold True
                        text "A quarentena utiliza uma pilha. A última evidência armazenada deve ser a primeira a ser inspecionada.":
                            size 14
                            color "#B0BEC5"

                        hbox:
                            spacing 14
                            xfill True

                            frame:
                                background "#102630"
                                xsize 320
                                padding (12, 8)
                                vbox:
                                    spacing 5
                                    text "PILHA DE QUARENTENA":
                                        size 15
                                        color "#FFB000"
                                        bold True
                                    text "TOP ↓":
                                        size 11
                                        color "#78909C"
                                    if stack_items:
                                        for item in stack_items:
                                            frame:
                                                background "#3A2B18"
                                                xfill True
                                                padding (7, 5)
                                                text "[item['id']] // [item['name']]":
                                                    size 12
                                                    color "#FFE0B2"
                                    else:
                                        text "PILHA VAZIA":
                                            size 13
                                            color "#00FF99"

                            frame:
                                background "#102630"
                                xfill True
                                padding (12, 8)
                                vbox:
                                    spacing 8
                                    text "INSPEÇÃO DA PILHA":
                                        size 15
                                        color "#FFB000"
                                        bold True
                                    if phase02_stack_completed:
                                        text "PILHA INSPECIONADA":
                                            size 20
                                            color "#00FF99"
                                            bold True
                                        text "Todas as evidências foram retiradas na sequência LIFO correta.":
                                            size 13
                                            color "#B0BEC5"
                                    elif phase02_queue_completed:
                                        $ stack_top = phase02_get_stack_top()
                                        if stack_top:
                                            text "EVIDÊNCIA NO TOPO":
                                                size 12
                                                color "#78909C"
                                            text "[stack_top['id']]":
                                                size 25
                                                color "#FFFFFF"
                                                bold True
                                            text "[stack_top['name']]":
                                                size 16
                                                color "#FFE0B2"
                                            text "[stack_top['description']]":
                                                size 13
                                                color "#B0BEC5"
                                            button:
                                                background "#5A4019"
                                                hover_background "#805C24"
                                                action Function(phase02_ui_inspect_stack_evidence)
                                                text "INSPECIONAR E RETIRAR TOPO":
                                                    size 14
                                                    color "#FFB000"
                                                    bold True
                                        else:
                                            text "PILHA VAZIA":
                                                size 18
                                                color "#00FF99"
                                    else:
                                        text "ETAPA BLOQUEADA":
                                            size 18
                                            color "#FF6B6B"
                                            bold True
                                        text "Conclua o processamento da Queue antes de iniciar a Stack.":
                                            size 13
                                            color "#B0BEC5"

                    # LINKED LIST
                    else:
                        text "ETAPA 03 // RECONSTRUÇÃO DA CADEIA":
                            size 21
                            color "#00FF99"
                            bold True
                        text "Reconstrua a cadeia de custódia conectando as evidências aprovadas na sequência correta.":
                            size 14
                            color "#B0BEC5"

                        hbox:
                            spacing 14
                            xfill True

                            frame:
                                background "#102630"
                                xsize 320
                                padding (12, 8)
                                vbox:
                                    spacing 6
                                    text "EVIDÊNCIAS APROVADAS":
                                        size 15
                                        color "#00FF99"
                                        bold True
                                    for evidence in PHASE02_EVIDENCES:
                                        if evidence["destination"] == "custody":
                                            button:
                                                background "#173744"
                                                hover_background "#205263"
                                                xfill True
                                                action Function(phase02_ui_linked_list_add, evidence["id"])
                                                text "[evidence['id']] // [evidence['name']]":
                                                    size 12
                                                    color "#E0F7FA"

                            frame:
                                background "#102630"
                                xfill True
                                padding (12, 8)
                                vbox:
                                    spacing 8
                                    text "CADEIA DE CUSTÓDIA":
                                        size 15
                                        color "#00FF99"
                                        bold True
                                    text "HEAD →":
                                        size 11
                                        color "#78909C"
                                    if custody_items:
                                        for item in custody_items:
                                            frame:
                                                background "#173D32"
                                                xfill True
                                                padding (7, 5)
                                                text "[item]":
                                                    size 15
                                                    color "#00FF99"
                                                    bold True
                                    else:
                                        text "LISTA VAZIA":
                                            size 13
                                            color "#78909C"

                                    if phase02_linked_list_completed:
                                        text "CADEIA VALIDADA":
                                            size 17
                                            color "#00FF99"
                                            bold True
                                    else:
                                        button:
                                            background "#164C3C"
                                            hover_background "#1E6B50"
                                            action Function(phase02_ui_validate_linked_list)
                                            text "VALIDAR CADEIA DE CUSTÓDIA":
                                                size 14
                                                color "#00FF99"
                                                bold True

            # FEEDBACK
            if phase02_feedback:
                frame:
                    background "#122A35"
                    xfill True
                    padding (8, 6)
                    text "[phase02_feedback]":
                        size 13
                        color "#00E5FF"

            # FOOTER
            hbox:
                xfill True
                spacing 12
                button:
                    background "#263238"
                    hover_background "#37474F"
                    action Function(phase02_restart)
                    text "REINICIAR FASE":
                        size 13
                        color "#B0BEC5"

                null

                if phase02_completed:
                    text "PROTOCOLO 02 CONCLUÍDO":
                        size 14
                        color "#00FF99"
                        bold True
                    button:
                        background "#164C3C"
                        hover_background "#1E6B50"
                        action Return()
                        text "AVANÇAR":
                            size 15
                            color "#00FF99"
                            bold True
                else:
                    text "PROTOCOLO DE TRIAGEM // CIV":
                        size 11
                        color "#546E7A"
