label intro_03:

    scene expression Transform(
        "images/backgrounds/central_investigacao.png",
        size=(config.screen_width, config.screen_height)
    )
    with dissolve

    pause 2.0

    "Uma mensagem de prioridade máxima é exibida no terminal secundário."

    pause 1.0

    "CIV // COMISSÃO INDEPENDENTE DE VERIFICAÇÃO"

    pause 2.0

    "O sistema identifica o destinatário."

    "ANALISTA DE INTEGRIDADE DE DADOS"

    pause 2.0

    show protagonist neutral at protagonist_right
    with dissolve

    "Você interrompe a análise dos alertas e abre a comunicação."

    pause 1.0

    "A mensagem contém apenas uma solicitação."

    "COMPAREÇA IMEDIATAMENTE À CENTRAL DE VERIFICAÇÃO."

    pause 2.0

    protagonist "Uma falha dessa magnitude... e estão solicitando intervenção manual?"

    pause 1.0

    protagonist "Isso significa que os mecanismos de recuperação não conseguiram reconstruir o estado anterior."

    pause 2.0

    "Você confirma o recebimento da convocação."

    pause 1.0

    "O protocolo de emergência é ativado."

    pause 2.0

    "DESTINO: CENTRAL DE VERIFICAÇÃO DA CIV"

    "STATUS: OPERAÇÃO DE RECONSTRUÇÃO AUTORIZADA"

    pause 3.0

    jump intro_04