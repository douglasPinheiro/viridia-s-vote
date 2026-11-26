# ==========================================
# VERÍDIA: PROTOCOLO ZERO
# DEFINIÇÃO DOS PERSONAGENS
# ==========================================


# ------------------------------------------
# PERSONAGENS DE DIÁLOGO
# ------------------------------------------

define protagonist = Character(
    "Analista",
    color="#00D9FF"
)

define dr_l = Character(
    "Dra. L",
    color="#B8C7D1"
)

define pedro = Character(
    "Pedro",
    color="#00D9FF"
)

define sistema_civ = Character(
    "SISTEMA CIV",
    color="#00FF99"
)


# ==========================================
# TRANSFORMS
# ==========================================


# ------------------------------------------
# PROTAGONISTA
# ------------------------------------------

transform protagonist_left:
    xalign 0.15
    yalign 1.0
    zoom 0.60

transform protagonist_center:
    xalign 0.5
    yalign 1.0
    zoom 0.60

transform protagonist_right:
    xalign 0.85
    yalign 1.0
    zoom 0.60


# ------------------------------------------
# DRA. L
# ------------------------------------------

transform dr_l_left:
    xalign 0.15
    yalign 1.0
    zoom 0.60

transform dr_l_center:
    xalign 0.5
    yalign 1.0
    zoom 0.60

transform dr_l_right:
    xalign 0.85
    yalign 1.0
    zoom 0.60


# ------------------------------------------
# PEDRO
# ------------------------------------------

transform pedro_left:
    xalign 0.15
    yalign 1.0
    zoom 0.60

transform pedro_center:
    xalign 0.5
    yalign 1.0
    zoom 0.60

transform pedro_right:
    xalign 0.85
    yalign 1.0
    zoom 0.60


# ==========================================
# SPRITES
# ==========================================


# ------------------------------------------
# PROTAGONISTA
# ------------------------------------------

image protagonist neutral = "images/characters/protagonist/protagonist_neutral.png"

image protagonist concerned = "images/characters/protagonist/protagonist_concerned.png"

image protagonist serious = "images/characters/protagonist/protagonist_serious.png"

image protagonist surprised = "images/characters/protagonist/protagonist_surprised.png"

image protagonist happy = "images/characters/protagonist/protagonist_happy.png"


# ------------------------------------------
# DRA. L
# ------------------------------------------

image dr_l neutral = "images/characters/dr_l/dr_l_neutral.png"

image dr_l concerned = "images/characters/dr_l/dr_l_concerned.png"

image dr_l serious = "images/characters/dr_l/dr_l_serious.png"

image dr_l surprised = "images/characters/dr_l/dr_l_surprised.png"

image dr_l happy = "images/characters/dr_l/dr_l_happy.png"


# ------------------------------------------
# PEDRO
# ------------------------------------------

image pedro neutral = "images/characters/pedro/pedro_neutral.png"

image pedro concerned = "images/characters/pedro/pedro_concerned.png"

image pedro happy = "images/characters/pedro/pedro_happy.png"