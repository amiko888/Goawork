def vaporcode(s):
    up = s.upper()
    spaced = ''
    for i in up:
        if i != ' ':
            spaced += i + '  '
    return spaced.strip()