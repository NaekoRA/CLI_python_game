import os
import sys
import time
import random
import msvcrt


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.03, newline=True):
    i = 0
    while i < len(text):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"\r":
                sys.stdout.write(text[i:])
                sys.stdout.flush()
                break
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
        i += 1
    print()


def divider(symbol="=", length=50):
    print(symbol * length)


def pause(message="\nTekan Enter untuk melanjutkan..."):
    input(message)


def random_choice(options):
    return random.choice(options)


def coin_flip():
    return random.choice(["Head", "Tail"])


def dice_roll(sides=6):
    return random.randint(1, sides)


def hompimpa(players):
    slow_print("Hompimpa alaium gambreng!\n")
    time.sleep(0.5)
    hasil = {p: random.choice(["kiri", "kanan"]) for p in players}
    for p, h in hasil.items():
        print(f"{p}: {h}")
        time.sleep(0.3)
    same = all(h == list(hasil.values())[0] for h in hasil.values())
    if same:
        slow_print("\nSeri! Ulangi lagi...\n")
        time.sleep(1)
        return hompimpa(players)
    else:
        winner = random_choice(players)
        slow_print(f"\n🎉 Pemenang hompimpa adalah {winner}!\n")
        return winner


def rock_paper_scissors():
    choices = ["batu", "gunting", "kertas"]
    slow_print("Pilih: batu / gunting / kertas")
    player = input("> ").strip().lower()
    enemy = random_choice(choices)

    slow_print(f"Komputer memilih: {enemy}")
    if player == enemy:
        return "draw"
    elif (
        (player == "batu" and enemy == "gunting")
        or (player == "gunting" and enemy == "kertas")
        or (player == "kertas" and enemy == "batu")
    ):
        return "win"
    else:
        return "lose"


def type_effect_dialog(speaker, text, delay=0.03):
    slow_print(f"{speaker}: ", delay=0.02, newline=False)
    slow_print(text, delay=delay)


def progress_bar(duration=2, label="Memproses"):
    sys.stdout.write(f"{label}: [")
    sys.stdout.flush()
    for _ in range(30):
        time.sleep(duration / 30)
        sys.stdout.write("█")
        sys.stdout.flush()
    sys.stdout.write("]\n")


def random_delay_text(texts):
    for t in texts:
        slow_print(t)
        time.sleep(random.uniform(0.5, 1.5))


def input_no_empty(prompt):
    buffer = ""
    sys.stdout.write(prompt)
    sys.stdout.flush()

    while True:
        key = msvcrt.getch()

        if key == b"\r":
            if buffer.strip() == "":
                continue
            else:
                print()
                return buffer.strip()

        elif key == b"\x08":
            if len(buffer) > 0:
                buffer = buffer[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()

        elif key.isalnum() or key in b" ,.-_=+!?:":
            buffer += key.decode()
            sys.stdout.write(key.decode())
            sys.stdout.flush()

        else:
            continue
