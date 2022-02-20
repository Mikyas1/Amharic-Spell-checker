def is_unique(input_file):
    lines = []
    S = set()
    with open(input_file) as f:
        lines = f.readlines()

    for line in lines:
        try:
            S.add(line.strip())
        except Exception as e:
            pass

    if len(S) == len(lines):
        return True
    return False
