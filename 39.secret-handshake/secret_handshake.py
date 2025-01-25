def commands(binary_str):
    num = int(binary_str, 2)
    moves = ['wink', 'double blink', 'close your eyes', 'jump']
    code = []
    for i in range(0, len(moves)):
        if num & 1 << i:
            code.append(moves[i])
    if num & 1 << 4:
        code.reverse()
    return code
