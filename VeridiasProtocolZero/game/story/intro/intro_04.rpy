label intro_04:

    scene expression Transform(
        "images/backgrounds/central_investigacao.png",
        size=(config.screen_width, config.screen_height)
    )
    with dissolve

    pause 1.0

    show dr_l concerned at protagonist_left
    with dissolve

    dr_l "Você recebeu a convocação. Imagino que já tenha visto os alertas."

    show protagonist serious at protagonist_right
    with dissolve

    protagonist "Os sistemas de recuperação falharam?"

    show dr_l serious

    dr_l "Parcialmente. Os registros estão desordenados, evidências perderam suas relações e algumas estruturas não conseguem reconstruir seus estados."

    dr_l "Não temos tempo para confiar na recuperação automática. Vamos reconstruir tudo manualmente."

    protagonist "Por onde começamos?"

    show dr_l neutral

    dr_l "Pelos registros. Organize-os, valide a sequência e restaure a integridade do arquivo."

    hide dr_l
    hide protagonist
    with dissolve

    pause 1.0

    "PROTOCOLO ZERO"

    "FASE 01 // O ARQUIVO EMBARALHADO"

    jump phase_01_intro