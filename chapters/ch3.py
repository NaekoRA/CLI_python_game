from utils import (
    slow_print,
    pause,
    clear,
    divider,
    progress_bar,
    random_delay_text,
    input_no_empty,
)
from save_game import save_game
import random


def start_chapter(state=None, checkpoint=None):
    if state is None:
        state = {"chapter": 3, "checkpoint": "start", "inventory": []}
    if checkpoint:
        state["checkpoint"] = checkpoint
    else:
        checkpoint = state.get("checkpoint", "start")

    clear()
    divider()
    slow_print(".................")
    inventory = state.get("inventory", [])

    semua_sigil = {
        "pecahan_lathi",
        "pecahan_grana",
        "pecahan_pipi",
        "pecahan_makutha",
        "pecahan_paningal_kiwo",
        "pecahan_paningal_tengen",
    }

    total_sigil = len([i for i in inventory if i in semua_sigil])

    if total_sigil == len(semua_sigil):
        return good_ending(state)
    else:
        return bad_ending(state)


def good_ending(state):
    slow_print("kamu akhirnya mengalahkannya")
    slow_print("Dengan semua pecahan yang kamu kumpulkan sepanjang perjalanan")
    slow_print("kamu merangkainya kembali menjadi satu topeng malangan")
    progress_bar(2, "merangkai topeng")
    slow_print("tiba tiba ada angin dahsyat....")
    slow_print("bayanganmu kembali....")
    slow_print("dia berusaha untuk mendekatimu....")
    progress_bar(2, "bayanganmu mendekatimu")
    slow_print("namun dia tersedot kedalam topeng malangan yang sudah kamu perbaiki")
    slow_print("setelah bayanganmu tersedot kedalam topeng itu")
    slow_print("topeng itu menjadi debu menghapus semua gangguan yang ada")
    slow_print("kamu lompat dari aula keluar dari sekolahan itu dengan selamat")
    slow_print("KAMU MENANG")


def bad_ending(state):
    slow_print("kamu akhirnya mengalahkannya")
    slow_print("kamu mengambil pecahan yang di jatuhkan bayanganmu")
    slow_print("setelah mengambil pecahan itu")
    slow_print("kamu merangkainya dengan pecahan yang kamu punya")
    progress_bar(2, "merangkai topeng")
    slow_print(
        "kamu selesai merangkai topeng itu namun ada beberapa bagian topeng yang hilang"
    )
    progress_bar(1)
    slow_print("tiba tiba ada angin dahsyat....")
    slow_print("bayanganmu kembali....")
    slow_print("dia berusaha untuk mendekatimu....")
    progress_bar(2, "bayanganmu mendekatimu")
    slow_print("tubuhmu sangat kesakitan")
    slow_print("bayanganmu mendekat dan membawa pecahan-pecahan yang kurang")
    slow_print("bayangamu merebut topengmu dan menyatukan pecahan yang dia miliki")
    slow_print("dengan senyum yang mengerikan dia memakaikan topeng itu padamu")
    slow_print("dan kamu berubah menjadi golongan mereka")
    slow_print("GAME OVER")
