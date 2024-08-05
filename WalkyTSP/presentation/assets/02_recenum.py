def rec_enum(xs, n):
    """Recursively enumerate xs"""
    if len(xs) == n:
        print(xs)
    for i in range(n):
        if i not in xs:
            rec_enum(xs + [i], n)
