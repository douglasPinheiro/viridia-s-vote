default phase01_best_algorithm_choice = None
default phase01_choice_feedback = ""
default phase01_choice_confirmed = False

init python:

    def phase01_key(record):
        return (
            record["zone"],
            record["section"],
            record["timestamp"]
        )

    def phase01_create_step(step_type, records, indices=None, description="", comparisons=0, movements=0):
        return {
            "type": step_type,
            "records": [record.copy() for record in records],
            "indices": indices or [],
            "description": description,
            "comparisons": comparisons,
            "movements": movements
        }

    # ========================================================
    # BUBBLE SORT - GERAÇÃO DOS PASSOS
    # ========================================================

    def phase01_generate_bubble_steps(records):
        working = [record.copy() for record in records]
        steps = []
        comparisons = 0
        movements = 0
        n = len(working)

        steps.append(
            phase01_create_step(
                "start",
                working,
                description="Estado inicial dos registros."
            )
        )

        for i in range(n):
            for j in range(n - i - 1):
                comparisons += 1

                steps.append(
                    phase01_create_step(
                        "compare",
                        working,
                        [j, j + 1],
                        "Comparando {} e {}.".format(
                            working[j]["id"],
                            working[j + 1]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

                if phase01_key(working[j]) > phase01_key(working[j + 1]):
                    working[j], working[j + 1] = (
                        working[j + 1],
                        working[j]
                    )
                    movements += 3

                    steps.append(
                        phase01_create_step(
                            "swap",
                            working,
                            [j, j + 1],
                            "Troca realizada entre os registros.",
                            comparisons,
                            movements
                        )
                    )
                else:
                    steps.append(
                        phase01_create_step(
                            "no_swap",
                            working,
                            [j, j + 1],
                            "Os registros já estão na ordem correta.",
                            comparisons,
                            movements
                        )
                    )

        steps.append(
            phase01_create_step(
                "done",
                working,
                description="Ordenação concluída.",
                comparisons=comparisons,
                movements=movements
            )
        )

        return steps, comparisons, movements

    # ========================================================
    # MERGE SORT - GERAÇÃO DOS PASSOS
    # ========================================================

    def phase01_generate_merge_steps(records):
        working = [record.copy() for record in records]
        steps = []
        comparisons = 0
        movements = 0

        steps.append(
            phase01_create_step(
                "start",
                working,
                description="Estado inicial dos registros."
            )
        )

        def merge_sort(items, start_index=0):
            nonlocal comparisons, movements

            if len(items) <= 1:
                return items

            middle = len(items) // 2

            steps.append(
                phase01_create_step(
                    "split",
                    working,
                    list(range(start_index, start_index + len(items))),
                    "Dividindo o conjunto em duas partes."
                )
            )

            left = merge_sort(items[:middle], start_index)
            right = merge_sort(items[middle:], start_index + middle)

            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                comparisons += 1

                steps.append(
                    phase01_create_step(
                        "compare",
                        working,
                        [start_index + i, start_index + middle + j],
                        "Comparando {} e {}.".format(
                            left[i]["id"],
                            right[j]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

                if phase01_key(left[i]) <= phase01_key(right[j]):
                    merged.append(left[i])
                    i += 1
                    description = "Selecionado {} da metade esquerda.".format(
                        merged[-1]["id"]
                    )
                    selected_type = "take_left"
                else:
                    merged.append(right[j])
                    j += 1
                    description = "Selecionado {} da metade direita.".format(
                        merged[-1]["id"]
                    )
                    selected_type = "take_right"

                movements += 1

                steps.append(
                    phase01_create_step(
                        selected_type,
                        working,
                        [start_index + len(merged) - 1],
                        description,
                        comparisons,
                        movements
                    )
                )

            while i < len(left):
                merged.append(left[i])
                i += 1
                movements += 1

                steps.append(
                    phase01_create_step(
                        "take_left",
                        working,
                        [start_index + len(merged) - 1],
                        "Restante da metade esquerda: {}.".format(
                            merged[-1]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

            while j < len(right):
                merged.append(right[j])
                j += 1
                movements += 1

                steps.append(
                    phase01_create_step(
                        "take_right",
                        working,
                        [start_index + len(merged) - 1],
                        "Restante da metade direita: {}.".format(
                            merged[-1]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

            working[start_index:start_index + len(merged)] = [
                item.copy() for item in merged
            ]

            steps.append(
                phase01_create_step(
                    "merge",
                    working,
                    list(range(start_index, start_index + len(merged))),
                    "Sublistas intercaladas nesta região.",
                    comparisons,
                    movements
                )
            )

            return merged

        merge_sort(working)

        steps.append(
            phase01_create_step(
                "done",
                working,
                description="Merge Sort concluído.",
                comparisons=comparisons,
                movements=movements
            )
        )

        return steps, comparisons, movements

    # ========================================================
    # QUICK SORT - GERAÇÃO DOS PASSOS
    # ========================================================

    def phase01_generate_quick_steps(records):
        working = [record.copy() for record in records]
        steps = []
        comparisons = 0
        movements = 0

        steps.append(
            phase01_create_step(
                "start",
                working,
                description="Estado inicial dos registros."
            )
        )

        def quick_sort(low, high):
            nonlocal comparisons, movements

            if low >= high:
                return

            pivot_record = working[high]
            pivot_key = phase01_key(pivot_record)

            steps.append(
                phase01_create_step(
                    "pivot",
                    working,
                    [high],
                    "Pivô escolhido: {}.".format(pivot_record["id"]),
                    comparisons,
                    movements
                )
            )

            i = low - 1

            for j in range(low, high):
                comparisons += 1

                steps.append(
                    phase01_create_step(
                        "compare",
                        working,
                        [j, high],
                        "Comparando {} com o pivô {}.".format(
                            working[j]["id"],
                            pivot_record["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

                if phase01_key(working[j]) <= pivot_key:
                    i += 1

                    if i != j:
                        working[i], working[j] = working[j], working[i]
                        movements += 3

                        steps.append(
                            phase01_create_step(
                                "swap",
                                working,
                                [i, j],
                                "Troca realizada para mover {} para a partição.".format(
                                    working[i]["id"]
                                ),
                                comparisons,
                                movements
                            )
                        )
                    else:
                        steps.append(
                            phase01_create_step(
                                "partition",
                                working,
                                [i, j],
                                "Registro já está na partição correta.",
                                comparisons,
                                movements
                            )
                        )

            pivot_index = i + 1

            if pivot_index != high:
                working[pivot_index], working[high] = (
                    working[high],
                    working[pivot_index]
                )
                movements += 3

                steps.append(
                    phase01_create_step(
                        "pivot_place",
                        working,
                        [pivot_index, high],
                        "Pivô {} colocado em sua posição.".format(
                            working[pivot_index]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )
            else:
                steps.append(
                    phase01_create_step(
                        "pivot_place",
                        working,
                        [pivot_index],
                        "Pivô {} já está em sua posição.".format(
                            working[pivot_index]["id"]
                        ),
                        comparisons,
                        movements
                    )
                )

            quick_sort(low, pivot_index - 1)
            quick_sort(pivot_index + 1, high)

        quick_sort(0, len(working) - 1)

        steps.append(
            phase01_create_step(
                "done",
                working,
                description="Quick Sort concluído.",
                comparisons=comparisons,
                movements=movements
            )
        )

        return steps, comparisons, movements
    
    # ========================================================
    # BUBBLE SORT TRADICIONAL
    # ========================================================

    def phase01_bubble_sort(records):
        comparisons = 0
        movements = 0
        n = len(records)

        for i in range(n):
            for j in range(n - i - 1):
                comparisons += 1

                if phase01_key(records[j]) > phase01_key(records[j + 1]):
                    records[j], records[j + 1] = (
                        records[j + 1],
                        records[j]
                    )
                    movements += 3

        return comparisons, movements

    # ========================================================
    # MERGE SORT TRADICIONAL
    # ========================================================

    def phase01_merge_sort(records):
        comparisons = 0
        movements = 0

        def merge_sort(items):
            nonlocal comparisons, movements

            if len(items) <= 1:
                return items

            middle = len(items) // 2
            left = merge_sort(items[:middle])
            right = merge_sort(items[middle:])

            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                comparisons += 1

                if phase01_key(left[i]) <= phase01_key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

                movements += 1

            while i < len(left):
                result.append(left[i])
                i += 1
                movements += 1

            while j < len(right):
                result.append(right[j])
                j += 1
                movements += 1

            return result

        sorted_records = merge_sort(records)
        records[:] = sorted_records

        return comparisons, movements

    # ========================================================
    # QUICK SORT TRADICIONAL
    # ========================================================

    def phase01_quick_sort(records):
        comparisons = 0
        movements = 0

        def quick_sort(low, high):
            nonlocal comparisons, movements

            if low >= high:
                return

            pivot = phase01_key(records[high])
            i = low - 1

            for j in range(low, high):
                comparisons += 1

                if phase01_key(records[j]) <= pivot:
                    i += 1

                    if i != j:
                        records[i], records[j] = (
                            records[j],
                            records[i]
                        )
                        movements += 3

            pivot_index = i + 1

            if pivot_index != high:
                records[pivot_index], records[high] = (
                    records[high],
                    records[pivot_index]
                )
                movements += 3

            quick_sort(low, pivot_index - 1)
            quick_sort(pivot_index + 1, high)

        quick_sort(0, len(records) - 1)

        return comparisons, movements

    # ========================================================
    # RESETAR REGISTROS PARA A ORDEM ORIGINAL
    # ========================================================

    def phase01_reset_records():
        global phase01_records
        global phase01_sorted
        global phase01_comparisons
        global phase01_movements
        global phase01_validation_message
        global phase01_steps
        global phase01_step_index
        global phase01_animation_running
        global phase01_animation_completed

        phase01_records = [record.copy() for record in PHASE01_INITIAL_RECORDS]
        phase01_sorted = False
        phase01_comparisons = 0
        phase01_movements = 0
        phase01_validation_message = ""
        phase01_steps = []
        phase01_step_index = 0
        phase01_animation_running = False
        phase01_animation_completed = False

    def phase01_records_are_original():
        return phase01_records == PHASE01_INITIAL_RECORDS

    # ========================================================
    # REGISTRAR RESULTADO
    # ========================================================

    def phase01_register_algorithm_result(algorithm, comparisons, movements):
        global phase01_algorithm_results
        global phase01_algorithm_runs

        phase01_algorithm_results[algorithm] = {
            "comparisons": comparisons,
            "movements": movements
        }

        if algorithm not in phase01_algorithm_runs:
            phase01_algorithm_runs.append(algorithm)

    # ========================================================
    # EXECUTAR ALGORITMO SELECIONADO
    # ========================================================

    def phase01_execute_sort():
        global phase01_records
        global phase01_sorted
        global phase01_comparisons
        global phase01_movements
        global phase01_completed
        global phase01_validation_message
        global phase01_steps
        global phase01_step_index
        global phase01_animation_running
        global phase01_animation_completed

        # Restaurar a entrada original a cada execução
        phase01_records = [
            record.copy()
            for record in PHASE01_INITIAL_RECORDS
        ]

        phase01_comparisons = 0
        phase01_movements = 0
        phase01_sorted = False
        phase01_completed = False
        phase01_validation_message = ""
        phase01_steps = []
        phase01_step_index = 0
        phase01_animation_running = False
        phase01_animation_completed = False

        if phase01_algorithm == "bubble":
            phase01_comparisons, phase01_movements = phase01_bubble_sort(
                phase01_records
            )
        elif phase01_algorithm == "merge":
            phase01_comparisons, phase01_movements = phase01_merge_sort(
                phase01_records
            )
        elif phase01_algorithm == "quick":
            phase01_comparisons, phase01_movements = phase01_quick_sort(
                phase01_records
            )

        phase01_register_algorithm_result(
            phase01_algorithm,
            phase01_comparisons,
            phase01_movements
        )

        phase01_sorted = True

    # ========================================================
    # INICIAR ANIMAÇÃO
    # ========================================================

    def phase01_start_animation():
        global phase01_records
        global phase01_steps
        global phase01_step_index
        global phase01_animation_running
        global phase01_animation_completed
        global phase01_comparisons
        global phase01_movements
        global phase01_sorted
        global phase01_completed
        global phase01_validation_message

        # Restaurar registros originais
        phase01_records = [
            record.copy()
            for record in PHASE01_INITIAL_RECORDS
        ]

        # Gerar passos conforme o algoritmo selecionado
        if phase01_algorithm == "bubble":
            phase01_steps, phase01_comparisons, phase01_movements = (
                phase01_generate_bubble_steps(phase01_records)
            )
        elif phase01_algorithm == "merge":
            phase01_steps, phase01_comparisons, phase01_movements = (
                phase01_generate_merge_steps(phase01_records)
            )
        elif phase01_algorithm == "quick":
            phase01_steps, phase01_comparisons, phase01_movements = (
                phase01_generate_quick_steps(phase01_records)
            )

        phase01_step_index = 0
        phase01_animation_running = False
        phase01_animation_completed = False
        phase01_sorted = False
        phase01_completed = False
        phase01_validation_message = ""

        if phase01_steps:
            phase01_records = [
                record.copy()
                for record in phase01_steps[0]["records"]
            ]

    # ========================================================
    # AVANÇAR ANIMAÇÃO
    # ========================================================

    def phase01_next_step():
        global phase01_records
        global phase01_step_index
        global phase01_animation_completed
        global phase01_animation_running
        global phase01_sorted
        global phase01_comparisons
        global phase01_movements

        if not phase01_steps:
            return

        if phase01_step_index < len(phase01_steps) - 1:
            phase01_step_index += 1

        current_step = phase01_steps[phase01_step_index]

        phase01_records = [
            record.copy()
            for record in current_step["records"]
        ]

        phase01_comparisons = current_step.get("comparisons", 0)
        phase01_movements = current_step.get("movements", 0)

        if current_step["type"] == "done":
            phase01_animation_running = False
            phase01_animation_completed = True
            phase01_sorted = True

            phase01_register_algorithm_result(
                phase01_algorithm,
                phase01_comparisons,
                phase01_movements
            )

    # ========================================================
    # VOLTAR ANIMAÇÃO
    # ========================================================

    def phase01_previous_step():
        global phase01_records
        global phase01_step_index
        global phase01_animation_completed
        global phase01_animation_running
        global phase01_sorted
        global phase01_comparisons
        global phase01_movements

        if not phase01_steps:
            return

        if phase01_step_index > 0:
            phase01_step_index -= 1

        current_step = phase01_steps[phase01_step_index]

        phase01_records = [
            record.copy()
            for record in current_step["records"]
        ]

        phase01_comparisons = current_step.get("comparisons", 0)
        phase01_movements = current_step.get("movements", 0)

        phase01_animation_completed = False
        phase01_animation_running = False
        phase01_sorted = False

    # ========================================================
    # EXECUÇÃO / PAUSA DA ANIMAÇÃO
    # ========================================================

    def phase01_toggle_animation():
        global phase01_animation_running

        phase01_animation_running = not phase01_animation_running

    # ========================================================
    # REINICIAR ANIMAÇÃO
    # ========================================================

    def phase01_restart_animation():
        global phase01_records
        global phase01_step_index
        global phase01_animation_running
        global phase01_animation_completed
        global phase01_sorted
        global phase01_completed
        global phase01_validation_message
        global phase01_comparisons
        global phase01_movements

        phase01_step_index = 0
        phase01_animation_running = False
        phase01_animation_completed = False
        phase01_sorted = False
        phase01_completed = False
        phase01_validation_message = ""

        if phase01_steps:
            phase01_records = [
                record.copy()
                for record in phase01_steps[0]["records"]
            ]

            phase01_comparisons = phase01_steps[0].get("comparisons", 0)
            phase01_movements = phase01_steps[0].get("movements", 0)

    # ========================================================
    # CONFIRMAR HIPÓTESE
    # ========================================================

    def phase01_confirm_best_algorithm():
        global phase01_choice_confirmed
        global phase01_choice_feedback
        global phase01_completed
        global phase01_validation_message

        phase01_completed = False
        phase01_validation_message = ""

        required = ["bubble", "merge", "quick"]

        # Exigir que os três algoritmos tenham sido executados
        if any(
            algorithm not in phase01_algorithm_results
            for algorithm in required
        ):
            phase01_choice_confirmed = False
            phase01_choice_feedback = (
                "Execute os três algoritmos antes de confirmar."
            )
            return

        if phase01_best_algorithm_choice is None:
            phase01_choice_confirmed = False
            phase01_choice_feedback = "Selecione uma hipótese."
            return

        # Encontrar algoritmo com menos comparações
        best = min(
            required,
            key=lambda algorithm: phase01_algorithm_results[algorithm]["comparisons"]
        )

        if phase01_best_algorithm_choice == best:
            phase01_choice_confirmed = True
            phase01_completed = True
            phase01_choice_feedback = (
                "CORRETO! Você identificou o algoritmo com menos comparações."
            )
            phase01_validation_message = (
                "PROTOCOLO CONCLUÍDO."
            )
        else:
            phase01_choice_confirmed = False
            phase01_completed = False
            phase01_choice_feedback = (
                "INCORRETO. Compare novamente os resultados."
            )

    # ========================================================
    # REINICIAR FASE
    # ========================================================

    def phase01_restart():
        global phase01_records
        global phase01_algorithm
        global phase01_sorted
        global phase01_completed
        global phase01_comparisons
        global phase01_movements
        global phase01_validation_message
        global phase01_steps
        global phase01_step_index
        global phase01_animation_running
        global phase01_animation_completed
        global phase01_best_algorithm_choice
        global phase01_choice_feedback
        global phase01_choice_confirmed
        global phase01_algorithm_results
        global phase01_algorithm_runs

        # Restaurar registros
        phase01_records = [
            record.copy()
            for record in PHASE01_INITIAL_RECORDS
        ]

        # Restaurar algoritmo
        phase01_algorithm = "bubble"

        # Restaurar estado
        phase01_sorted = False
        phase01_completed = False
        phase01_comparisons = 0
        phase01_movements = 0
        phase01_validation_message = ""

        # Limpar animação
        phase01_steps = []
        phase01_step_index = 0
        phase01_animation_running = False
        phase01_animation_completed = False

        # Limpar hipótese
        phase01_best_algorithm_choice = None
        phase01_choice_feedback = ""
        phase01_choice_confirmed = False

        # Limpar resultados
        phase01_algorithm_results = {}
        phase01_algorithm_runs = []