label intro_01:
    # Para a música do menu
    stop music fadeout 2.0
    
    # Tela escura inicial
    scene black
    
    with fade
    pause 2.0
    
    # Inicia a trilha da introdução
    play music "audio/music/menu_ambient.ogg" fadein 4.0
    
    # Apresentação da cidade
    scene expression Transform(
        "images/backgrounds/central_investigacao.png",
        size=(config.screen_width, config.screen_height)
    )
    with dissolve
    pause 3.0
    
    # Narrativa
    "Verídia, 2042."
    pause 1.0
    "Uma cidade construída sobre sistemas inteligentes, redes interconectadas e infraestrutura digital."
    
    pause 1.0
    "Quase tudo funciona de forma automatizada."
    "Informações circulam em tempo real."
    "Sistemas municipais dependem de registros sincronizados para manter a cidade operando."
    
    pause 2.0
    "Até que, em uma madrugada, algo falha."
    
    pause 3.0
    # Próxima cena
    jump intro_02