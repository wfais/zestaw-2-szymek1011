def dodaj_element(wejscie):
    # --- 1. Znajdź maksymalną głębokość list ---
    def max_depth(obj, depth=0):
        if isinstance(obj, list):
            if not obj:
                return depth + 1
            return max(max_depth(x, depth + 1) for x in obj)
        elif isinstance(obj, tuple):
            if not obj:
                return depth
            return max(max_depth(x, depth + 1) for x in obj)
        elif isinstance(obj, dict):
            if not obj:
                return depth
            return max(max_depth(v, depth + 1) for v in obj.values())
        else:
            return depth

    deepest = max_depth(wejscie)

    # --- 2. Dodaj elementy w listach na najgłębszym poziomie ---
    def add_to_deepest(obj, depth=0):
        if isinstance(obj, list):
            if depth + 1 == deepest:
                if obj:
                    obj.append(obj[-1] + 1 if isinstance(obj[-1], (int, float)) else 1)
                else:
                    obj.append(1)
            else:
                for x in obj:
                    add_to_deepest(x, depth + 1)
        elif isinstance(obj, tuple):
            for x in obj:
                add_to_deepest(x, depth + 1)
        elif isinstance(obj, dict):
            for v in obj.values():
                add_to_deepest(v, depth + 1)
        return obj

    return add_to_deepest(wejscie)



if __name__ == '__main__':
    input_list = [1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5], "hello", 3, [4, 5], 5, (6, (1, [7, 8]))]
    print("Lista pierwotna:")
    print(input_list)

    output_list = dodaj_element(input_list)
    print("\nLista po przemianie:")
    print(output_list)
