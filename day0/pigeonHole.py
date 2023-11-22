def pigeonhole_principle(items, containers):
    if items <= containers:
        print("No pigeonhole problem exists.")
        return

    pigeons_per_hole = items // containers
    extra_pigeons = items % containers

    print(f"Items: {items}")
    print(f"Containers: {containers}")
    print(f"Pigeons per hole: {pigeons_per_hole}")
    print(f"Extra pigeons: {extra_pigeons}")

    if extra_pigeons > 0:
        print(f"At least one container must have more than one item.")
    else:
        print("No pigeonhole problem exists.")

# Example usage
pigeonhole_principle(10, 5)

