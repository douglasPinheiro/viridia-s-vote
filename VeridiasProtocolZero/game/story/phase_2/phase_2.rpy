# ============================================================
# VERÍDIA: PROTOCOLO ZERO
# FASE 02 - A CENTRAL DE TRIAGEM
# ============================================================


label phase_02_intro:

    $ phase02_initialize()
    
    scene expression Transform(
        "images/backgrounds/central_triagem.png",
        size=(config.screen_width, config.screen_height)
    )


    pause 1.0

    "A Central de Triagem da CIV está parcialmente operacional."

    "Alguns terminais exibem registros pendentes e alertas de processamento interrompido."

    show pedro neutral at pedro_right
    with dissolve

    # --------------------------------------------------------
    # APRESENTAÇÃO DE PEDRO
    # --------------------------------------------------------

    dr_l "Este é Pedro, responsável pela Central de Triagem. Ele estava acompanhando o processamento quando ocorreu a interrupção."

    show pedro concerned

    pedro "O processamento foi interrompido antes que todos os registros fossem tratados."

    protagonist "O que foi afetado?"

    pedro "A fila de entrada, os registros em quarentena e as referências que conectavam as evidências."

    dr_l "Precisamos reconstruir o processamento e verificar se todos os registros foram tratados corretamente."

    pedro "Os registros foram preservados. Porém, precisamos reorganizar o fluxo e reconstruir a cadeia de custódia."

    protagonist "Qual é o procedimento?"

    # --------------------------------------------------------
    # BRIEFING DA MISSÃO
    # --------------------------------------------------------

    dr_l "Primeiro, processar os registros pendentes respeitando a ordem de chegada."

    dr_l "Depois, inspecionar os registros em quarentena, preservando a ordem de recuperação."

    show pedro neutral

    pedro "Por último, reconstruir a cadeia de custódia, conectando os registros válidos na sequência correta."

    protagonist "Entendido. Vou reconstruir o processamento e validar a cadeia."

    # --------------------------------------------------------
    # INÍCIO DO PUZZLE
    # --------------------------------------------------------

    hide pedro
    with dissolve

    sistema_civ "PROTOCOLO 02 DISPONÍVEL"

    sistema_civ "CENTRAL DE TRIAGEM"

    sistema_civ "OBJETIVO: RECONSTRUIR O PROCESSAMENTO"

    pause 1.0

    call screen phase_02_challenge

    # --------------------------------------------------------
    # ENCERRAMENTO
    # --------------------------------------------------------

    if phase02_completed:

        scene expression Transform(
            "images/backgrounds/central_triagem.png",
            size=(config.screen_width, config.screen_height)
        )

        show pedro happy at pedro_right
        with dissolve

        sistema_civ "PROCESSAMENTO RECONSTRUÍDO"

        sistema_civ "FILA: VALIDADA"

        sistema_civ "QUARENTENA: INSPECIONADA"

        sistema_civ "CADEIA DE CUSTÓDIA: VALIDADA"

        pedro "A cadeia foi reconstruída. Todos os registros válidos estão conectados e as evidências em quarentena foram preservadas."

        protagonist "A interrupção comprometeu o processamento, mas conseguimos recuperar a sequência e a integridade dos registros."

        show pedro concerned

        dr_l "Ainda existem referências a setores externos à Central. Precisamos descobrir por quais caminhos os dados passaram."

        pedro "Os identificadores apontam para conexões entre diferentes setores. O mapa operacional pode ajudar a reconstruí-las."

        hide pedro
        with dissolve

        sistema_civ "PROTOCOLO 02 // CONCLUÍDO"

        sistema_civ "CADEIA DE CUSTÓDIA: VALIDADA"

        sistema_civ "PRÓXIMA ETAPA: O MAPA DAS SEÇÕES"

        pause 1.5

        jump phase_03_intro

    return