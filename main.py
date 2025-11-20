from utils import clear, slow_print, pause, divider, input_no_empty
from save_game import save_game, load_game, delete_save
from chapters import ch1, ch2, ch3
from maze_map import logo


def tampilkan_inventory(state):
    divider()
    print("🎒 INVENTORY:")
    if not state.get("inventory"):
        print("  (Kosong)")
    else:
        for item in state["inventory"]:
            print(f"  - {item}")
    divider()


def main():
    clear()
    divider()
    for line in logo:
        slow_print(line,delay=0.0001)
    print("Main Menu")
    print("1. New Game")
    print("2. Load Game")
    print("3. Delete Save")
    print("4. Keluar")

    choice = input_no_empty("\nPilih opsi (1/2/3/4): ").strip()

    # --- PILIHAN MENU ---
    if choice == "2":
        # LOAD GAME
        state = load_game()
        if not state:
            print("\nTidak ada data tersimpan. Mulai dari awal...\n")
            state = {"chapter": 1, "checkpoint": "start", "inventory": []}
        else:
            print("\n✅ Data berhasil dimuat:")
            print(f"  Chapter   : {state['chapter']}")
            print(f"  Checkpoint: {state['checkpoint']}")
            print(f"  Inventory : {state['inventory']}")
            input("\nTekan Enter untuk melanjutkan dari titik terakhir...")

    elif choice == "3":
        delete_save()
        return

    elif choice == "4":
        print("Keluar dari game.")
        return

    else:
        # NEW GAME
        state = {"chapter": 1, "checkpoint": "start", "inventory": []}

    # Pastikan inventory selalu ada
    if "inventory" not in state:
        state["inventory"] = []

    chapter = state.get("chapter", 1)
    checkpoint = state.get("checkpoint", "start")

    # --- JALANKAN GAME BERDASARKAN CHAPTER ---
    if chapter == 1:
        result = ch1.start_chapter(state, checkpoint)
        tampilkan_inventory(state)
        save_game(state)
        if result == "next":
            state["chapter"] = 2
            state["checkpoint"] = "start"
            save_game(state)
            ch2.start_chapter(state, "start")

    elif chapter == 2:
        result = ch2.start_chapter(state, checkpoint)
        tampilkan_inventory(state)
        save_game(state)
        if result == "next":
            state["chapter"] = 3
            state["checkpoint"] = "start"
            save_game(state)
            ch3.start_chapter(state, "start")

    elif chapter == 3:
        result = ch3.start_chapter(state, checkpoint)
        tampilkan_inventory(state)
        save_game(state)

    slow_print("\nTerima kasih sudah bermain!")
    divider()


if __name__ == "__main__":
    main()
