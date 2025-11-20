import json
import os

SAVE_FILE = "save_data.json"


def save_game(state):
    """Simpan progres game ke file JSON."""
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4, ensure_ascii=False)
        print("\n💾 Progress tersimpan.")
    except Exception as e:
        print(f"❌ Gagal menyimpan game: {e}")


def load_game():
    """Muat progres game dari file JSON."""
    if not os.path.exists(SAVE_FILE):
        return None
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state
    except Exception as e:
        print(f"❌ Gagal memuat save: {e}")
        return None


def delete_save():
    """Hapus file save."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("\n🗑️ Save data telah dihapus.")
    else:
        print("\nTidak ada file save yang ditemukan.")
