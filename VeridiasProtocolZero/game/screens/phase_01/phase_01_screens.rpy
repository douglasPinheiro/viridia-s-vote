# ============================================================
# VERÍDIA: PROTOCOLO ZERO
# FASE 01 - INTERFACE ANIMADA
# ============================================================

screen phase_01_challenge():
    modal True
    default screen_message = ""

    $ current_step = phase01_steps[phase01_step_index] if phase01_steps and phase01_step_index < len(phase01_steps) else None
    $ highlighted_indices = current_step["indices"] if current_step else []
    $ progress = (phase01_step_index / float(max(1, len(phase01_steps) - 1))) if phase01_steps else 0.0
    $ validation_color = "#00FF99" if phase01_completed else "#FF6B6B"
    $ choice_feedback_color = "#00FF99" if phase01_choice_confirmed else "#FFB347"

    add Solid("#07111C")

    # CABEÇALHO
    frame:
        xalign 0.5
        yalign 0.03
        xsize 1700
        ysize 100
        background Solid("#102333")
        padding (30, 20)

        vbox:
            spacing 8

            text "VERÍDIA // PROTOCOLO ZERO":
                size 30
                color "#00D9FF"
                bold True

            text "FASE 01 // O ARQUIVO EMBARALHADO":
                size 22
                color "#B8C7D1"

    # CONTEÚDO PRINCIPAL
    frame:
        xalign 0.5
        yalign 0.52
        xsize 1700
        ysize 790
        background Solid("#0C1B28")
        padding (35, 30)

        hbox:
            spacing 35

            # COLUNA DE REGISTROS
            vbox:
                xsize 850
                spacing 15

                text "Ordene os registros utilizando a chave composta":
                    size 20
                    color "#B8C7D1"

                text "Zona → Seção → Horário":
                    size 22
                    color "#FFFFFF"

                frame:
                    background Solid("#142838")
                    padding (20, 15)
                    xsize 830

                    vbox:
                        spacing 8

                        for index, record in enumerate(phase01_records):
                            $ is_highlighted = index in highlighted_indices
                            $ record_color = "#00D9FF" if is_highlighted else "#607D8B"
                            $ card_color = "#264B60" if is_highlighted else "#102333"

                            frame:
                                background Solid(card_color)
                                padding (10, 8)
                                xsize 790

                                hbox:
                                    spacing 20

                                    text record["id"]:
                                        size 22
                                        color record_color
                                        xsize 100

                                    text record["zone"]:
                                        size 22
                                        color "#FFFFFF"
                                        xsize 150

                                    text "Seção {}".format(record["section"]):
                                        size 22
                                        color "#B8C7D1"
                                        xsize 180

                                    text record["timestamp"]:
                                        size 22
                                        color "#FFFFFF"

                # ESTADO DA ANIMAÇÃO
                if current_step:
                    frame:
                        background Solid("#102333")
                        padding (15, 10)
                        xsize 830

                        vbox:
                            spacing 6

                            text "PASSO {} / {}".format(
                                phase01_step_index + 1,
                                len(phase01_steps)
                            ):
                                size 20
                                color "#00D9FF"
                                bold True

                            text current_step["description"]:
                                size 20
                                color "#FFFFFF"

                            if current_step["type"] == "compare":
                                text "AÇÃO: COMPARAÇÃO":
                                    size 18
                                    color "#FFCC66"

                            elif current_step["type"] == "swap":
                                text "AÇÃO: TROCA":
                                    size 18
                                    color "#00FF99"

                            elif current_step["type"] == "no_swap":
                                text "AÇÃO: SEM TROCA":
                                    size 18
                                    color "#B8C7D1"

                            elif current_step["type"] == "done":
                                text "AÇÃO: ORDENAÇÃO CONCLUÍDA":
                                    size 18
                                    color "#00FF99"

                # PROGRESSO
                if phase01_steps:
                    vbox:
                        spacing 5

                        text "PROGRESSO DA ANIMAÇÃO":
                            size 18
                            color "#B8C7D1"

                        bar:
                            value progress
                            xsize 800
                            ysize 15

                # MÉTRICAS
                text "MÉTRICAS DE EXECUÇÃO":
                    size 24
                    color "#00D9FF"
                    bold True

                hbox:
                    spacing 40

                    vbox:
                        spacing 5

                        text "COMPARAÇÕES":
                            size 18
                            color "#B8C7D1"

                        text str(phase01_comparisons):
                            size 30
                            color "#FFFFFF"

                    vbox:
                        spacing 5

                        text "MOVIMENTAÇÕES":
                            size 18
                            color "#B8C7D1"

                        text str(phase01_movements):
                            size 30
                            color "#FFFFFF"

            # COLUNA DE CONTROLES
            vbox:
                xsize 700
                spacing 15

                # CONTROLES SÓ APARECEM ANTES DA CONCLUSÃO
                if not phase01_completed:

                    text "Selecione um algoritmo":
                        size 20
                        color "#B8C7D1"

                    # SELEÇÃO DO ALGORITMO
                    vbox:
                        spacing 8

                        textbutton "BUBBLE SORT":
                            action SetVariable("phase01_algorithm", "bubble")
                            text_size 18
                            text_color "#FFFFFF"
                            text_hover_color "#00D9FF"

                        textbutton "MERGE SORT":
                            action SetVariable("phase01_algorithm", "merge")
                            text_size 18
                            text_color "#FFFFFF"
                            text_hover_color "#00D9FF"

                        textbutton "QUICK SORT":
                            action SetVariable("phase01_algorithm", "quick")
                            text_size 18
                            text_color "#FFFFFF"
                            text_hover_color "#00D9FF"

                    # ALGORITMO SELECIONADO
                    frame:
                        background Solid("#142838")
                        padding (15, 10)
                        xsize 620

                        vbox:
                            spacing 5

                            text "SELECIONADO":
                                size 15
                                color "#B8C7D1"

                            if phase01_algorithm == "bubble":
                                text "BUBBLE SORT":
                                    size 21
                                    color "#00D9FF"
                                    bold True

                            elif phase01_algorithm == "merge":
                                text "MERGE SORT":
                                    size 21
                                    color "#00D9FF"
                                    bold True

                            elif phase01_algorithm == "quick":
                                text "QUICK SORT":
                                    size 21
                                    color "#00D9FF"
                                    bold True

                    # COMPARATIVO DE DESEMPENHO
                    frame:
                        background Solid("#142838")
                        padding (12, 10)
                        xsize 620

                        vbox:
                            spacing 5

                            text "COMPARATIVO DE DESEMPENHO":
                                size 17
                                color "#00D9FF"
                                bold True

                            text "Algoritmos executados: [len(phase01_algorithm_runs)] / 3":
                                size 15
                                color "#FFFFFF"

                            hbox:
                                spacing 15

                                vbox:
                                    spacing 2

                                    text "BUBBLE":
                                        size 14
                                        color "#B8C7D1"

                                    if "bubble" in phase01_algorithm_results:
                                        text "[phase01_algorithm_results['bubble']['comparisons']] comparações":
                                            size 15
                                            color "#FFFFFF"
                                    else:
                                        text "--":
                                            size 15
                                            color "#607D8B"

                                vbox:
                                    spacing 2

                                    text "MERGE":
                                        size 14
                                        color "#B8C7D1"

                                    if "merge" in phase01_algorithm_results:
                                        text "[phase01_algorithm_results['merge']['comparisons']] comparações":
                                            size 15
                                            color "#FFFFFF"
                                    else:
                                        text "--":
                                            size 15
                                            color "#607D8B"

                                vbox:
                                    spacing 2

                                    text "QUICK":
                                        size 14
                                        color "#B8C7D1"

                                    if "quick" in phase01_algorithm_results:
                                        text "[phase01_algorithm_results['quick']['comparisons']] comparações":
                                            size 15
                                            color "#FFFFFF"
                                    else:
                                        text "--":
                                            size 15
                                            color "#607D8B"

                    # ESCOLHA INVESTIGATIVA
                    frame:
                        background Solid("#142838")
                        padding (12, 10)
                        xsize 620

                        vbox:
                            spacing 6

                            text "HIPÓTESE: MENOS COMPARAÇÕES":
                                size 17
                                color "#00D9FF"
                                bold True

                            text "Qual algoritmo teve o menor número de comparações?":
                                size 15
                                color "#FFFFFF"

                            hbox:
                                spacing 10

                                textbutton "BUBBLE":
                                    text_size 15
                                    action [
                                        SetVariable("phase01_best_algorithm_choice", "bubble"),
                                        SetVariable("phase01_choice_confirmed", False),
                                        SetVariable("phase01_completed", False),
                                        SetVariable("phase01_choice_feedback", "")
                                    ]

                                textbutton "MERGE":
                                    text_size 15
                                    action [
                                        SetVariable("phase01_best_algorithm_choice", "merge"),
                                        SetVariable("phase01_choice_confirmed", False),
                                        SetVariable("phase01_completed", False),
                                        SetVariable("phase01_choice_feedback", "")
                                    ]

                                textbutton "QUICK":
                                    text_size 15
                                    action [
                                        SetVariable("phase01_best_algorithm_choice", "quick"),
                                        SetVariable("phase01_choice_confirmed", False),
                                        SetVariable("phase01_completed", False),
                                        SetVariable("phase01_choice_feedback", "")
                                    ]

                            text "Selecionado: [phase01_best_algorithm_choice.upper() if phase01_best_algorithm_choice else 'Nenhum']":
                                size 15
                                color "#B8C7D1"

                            textbutton "CONFIRMAR HIPÓTESE":
                                action Function(phase01_confirm_best_algorithm)
                                text_size 17
                                text_color "#00D9FF"
                                text_hover_color "#FFFFFF"

                            if phase01_choice_feedback:
                                text phase01_choice_feedback:
                                    size 18
                                    color choice_feedback_color

                    # EXECUÇÃO TRADICIONAL
                    textbutton "EXECUTAR ORDENAÇÃO":
                        action Function(phase01_execute_sort)
                        text_size 19
                        text_color "#00D9FF"
                        text_hover_color "#FFFFFF"

                    # INICIAR ANIMAÇÃO
                    textbutton "INICIAR ANIMAÇÃO":
                        action Function(phase01_start_animation)
                        text_size 19
                        text_color "#00D9FF"
                        text_hover_color "#FFFFFF"

                    # CONTROLES DE ANIMAÇÃO
                    hbox:
                        spacing 15

                        textbutton "◀ ANTERIOR":
                            action Function(phase01_previous_step)
                            text_size 17
                            text_color "#FFFFFF"
                            text_hover_color "#00D9FF"

                        textbutton "PRÓXIMO ▶":
                            action Function(phase01_next_step)
                            text_size 17
                            text_color "#FFFFFF"
                            text_hover_color "#00D9FF"

                    # RESETAR REGISTROS
                    textbutton "RESETAR REGISTROS":
                        action Function(phase01_reset_records)
                        sensitive not phase01_records_are_original()
                        text_size 17
                        text_color "#B8C7D1"
                        text_hover_color "#FFFFFF"

                    # TIMER
                    if phase01_animation_running and not phase01_animation_completed:
                        timer 0.8 action Function(phase01_next_step) repeat True

                # MENSAGEM DE SUCESSO APÓS A HIPÓTESE CORRETA
                if phase01_completed:
                    frame:
                        background Solid("#12382F")
                        padding (15, 12)
                        xsize 620

                        vbox:
                            spacing 6

                            text "✓ REGISTROS REORDENADOS COM SUCESSO":
                                size 18
                                color "#00FF99"
                                bold True

                            text "Algoritmo de maior eficiência identificado: [phase01_best_algorithm_choice.upper()]":
                                size 16
                                color "#FFFFFF"

                # APÓS A HIPÓTESE CORRETA, SÓ ESTES BOTÕES
                textbutton "REINICIAR FASE":
                    action Function(phase01_restart)
                    text_size 18
                    text_color "#B8C7D1"
                    text_hover_color "#FFFFFF"

                if phase01_completed:
                    textbutton "CONTINUAR":
                        action Return()
                        text_size 20
                        text_color "#00FF99"
                        text_hover_color "#FFFFFF"

    # RODAPÉ
    frame:
        xalign 0.5
        yalign 0.98
        background Solid("#102333")
        padding (20, 10)

        text "CIV // COMISSÃO INDEPENDENTE DE VERIFICAÇÃO":
            size 16
            color "#607D8B"