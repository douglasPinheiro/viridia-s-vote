# ============================================================
# VERÍDIA: PROTOCOLO ZERO
# FASE 01 - O ARQUIVO EMBARALHADO
# ============================================================


label phase_01_intro:

    $ phase01_restart()

    scene expression Transform(
        "images/backgrounds/central_investigacao.png",
        size=(config.screen_width, config.screen_height)
    )


    show dr_l serious at dr_l_right

    dr_l "Os registros foram recebidos fora de ordem."
    dr_l "Precisamos organizá-los por zona, seção e horário."
    dr_l "Você pode escolher entre diferentes algoritmos de ordenação."
    dr_l "Após a execução, valide se todos os registros foram preservados e se a sequência está correta."

    hide dr_l


    # ========================================================
    # DESAFIO
    # ========================================================

    call screen phase_01_challenge


    # ========================================================
    # VERIFICAÇÃO DO RESULTADO
    # ========================================================

    if phase01_completed:


        scene expression Transform(
            "images/backgrounds/central_investigacao.png",
            size=(config.screen_width, config.screen_height)
        )


        show dr_l happy at dr_l_right


        dr_l "Integridade dos registros restaurada."


        dr_l "O primeiro selo de verificação foi recuperado."


        dr_l "A sequência está consistente. Podemos prosseguir para a próxima etapa."


        hide dr_l


        # Marcar fase concluída
        # (Integraremos posteriormente ao sistema global de progresso.)


        return


    else:


        # Se a tela retornar sem concluir o desafio,
        # a fase retorna ao fluxo anterior.

        return