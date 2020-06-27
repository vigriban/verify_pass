import urwid

STRENGTH_POINTS = 2
REQUIRED_PASSWORD_LENGTH = 13

PASSWORD_VERIFICATORS = [
    lambda pswd: len(pswd) >= REQUIRED_PASSWORD_LENGTH,
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


def on_ask_change(edit, new_edit_text):
    password_rating = verify_password(new_edit_text)
    reply.set_text(f"Password rating: {password_rating}")


if __name__ == '__main__':
    ask = urwid.Edit("Enter password: ", mask="*")
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
