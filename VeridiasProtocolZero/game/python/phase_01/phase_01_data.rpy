# ============================================================
# VERÍDIA: PROTOCOLO ZERO
# FASE 01 - DADOS
# ============================================================

define PHASE01_INITIAL_RECORDS = [
    {"id": "R-04", "zone": "Norte", "section": 3, "timestamp": "10:42"},
    {"id": "R-01", "zone": "Sul", "section": 1, "timestamp": "09:15"},
    {"id": "R-05", "zone": "Norte", "section": 1, "timestamp": "11:20"},
    {"id": "R-02", "zone": "Norte", "section": 3, "timestamp": "08:30"},
    {"id": "R-03", "zone": "Sul", "section": 2, "timestamp": "10:05"},
]


# Estado atual da fase

default phase01_algorithm_results = {}
default phase01_algorithm_runs = []
default phase01_records = []
default phase01_steps = []
default phase01_step_index = 0
default phase01_algorithm = "bubble"
default phase01_sorted = False
default phase01_completed = False
default phase01_animation_running = False
default phase01_animation_completed = False
default phase01_comparisons = 0
default phase01_movements = 0
default phase01_validation_message = ""