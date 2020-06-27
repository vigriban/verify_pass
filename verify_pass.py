STRENGTH_POINTS = 2

PASSWORD_VERIFICATORS = [
    lambda pswd: len(pswd) > 12,
    lambda pswd: any(ch.isdigit() for ch in pswd),
    lambda pswd: any(not ch.isdigit() for ch in pswd),
    lambda pswd: any(ch.islower() for ch in pswd),
    lambda pswd: any(ch.isupper() for ch in pswd),
    lambda pswd: any(not (ch.isdigit() or ch.isalpha()) for ch in pswd),
    lambda pswd: any(ch.isdigit() or ch.isalpha for ch in pswd)
]


def verify_password(password):
    total_score = 0
    for fn in PASSWORD_VERIFICATORS:
        total_score += STRENGTH_POINTS if fn(password) else 0
    return total_score


if __name__ == '__main__':
    pass
