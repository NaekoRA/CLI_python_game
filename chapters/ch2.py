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
import os
from maze_engine import MazeGame
from maze_map import (
    taman,
    gedung_sekolah_f2,
    gedung_sekolah_f3_no2,
    to_kantin,
    kantin,
    perpustakaan,
    perpustakaan2,
    masjid,
    masjid2,
    aula,
)


def start_chapter(state=None, checkpoint=None):
    if state is None:
        state = {"chapter": 2, "checkpoint": "start", "inventory": []}
    elif checkpoint == "taman":
        return roam_taman(state)
    elif checkpoint == "kelas":
        return kelas(state)
    elif checkpoint == "taman_selesai":
        return otw_kantin(state)
    elif checkpoint == "kantin":
        return area_kantin(state)
    elif checkpoint == "kantin_selesai":
        return otw_perpus(state)
    elif checkpoint == "perpustakaan":
        return perpus(state)
    elif checkpoint == "perpustakaan_selesai":
        return otw_masjid(state)
    elif checkpoint == "masjid":
        return area_masjid(state)
    elif checkpoint == "area_masjid":
        return otw_aula(state)
    elif checkpoint == "masjid_selesai":
        return akhir(state)
    elif checkpoint == "selesai":
        return "next"

    if checkpoint:
        state["checkpoint"] = checkpoint
    else:
        checkpoint = state.get("checkpoint", "start")
    clear()
    divider()
    slow_print("kamu berhasil melewati tantangan di ruangan itu")
    slow_print(
        "Setelah pintu terbuka, kamu keluar dan mencoba melakukan pemanggilan di tempat lain..."
    )
    input_no_empty("\nMasukkan '1' untuk melanjutkan...")
    game = MazeGame(gedung_sekolah_f2)
    results = game.start()
    if results == "F4":
        slow_print("kamu berjalan ke arah taman")
        slow_print("kamu ingin membuktikan mitos tentang siswi yang jadi hantu")
        state.update({"chapter": 2, "checkpoint": "taman"})
        save_game(state)
        return roam_taman(state)
    elif results == "F1":
        slow_print(
            "saat kamu membuka pintu tiba tiba ada mahluk hitam besar yang mencekik dan mematahan lehermu"
        )
        slow_print("keesokkan harinya kamudi temukan tewas di depan pintu F1 sekolahmu")
        return "game_over"
    elif results == "F3":
        clear()
        slow_print("ketika kamu mesuk ke dalam ruangan ")
        slow_print(
            "kamu melihat ada seoarnag gadis berambut hitam yang sedang duduk di pojok ruangan sembari memandang langit"
        )
        choice = (
            input_no_empty("\napakah kamu ingin mendekatinya? (1:ya/2:tidak): ")
            .strip()
            .lower()
        )
        if choice == "1":
            slow_print("kamu mendekatinya dan mencoba mengajak bicara")
            slow_print("tapi dia tidak meresponmu sama sekali")
            slow_print("tiba tiba secara perlahan dia berbalik menatapmu")
            slow_print("matanya merah menyala dan mulutnya robel sampai ke telinganya")
            slow_print("tiba tiba gadis itu bertanya padamu ")
            slow_print("'apakah menurutmu aku cantik??????????'")
            slow_print("1:iya")
            slow_print("2:tidak")
            slow_print("3:lari")
            choice2 = input_no_empty("\n(1/2/3): ").strip().lower()
            if choice2 == "1":
                slow_print("kamu menjawab iya")
                slow_print("tiba tiba gadis itu tersenyum lebar dan melompat ke arahmu")
                slow_print("dia mengeluarkan gunting dari sakunya dan merobek mulutmu")
                slow_print("kamu tewas di tempat")
                return "game_over"
            elif choice2 == "2":
                slow_print("kamu menjawab tidak")
                slow_print("tiba tiba gadis itu marah besar")
                slow_print("dengan cepat dia melompat ke arahmu")
                slow_print(
                    "menebas lehermu dengan guntingnya sebelum merobek mulutmu agar jadi seperti dirinya"
                )
                slow_print("kamu tewas di tempat")
                return "game_over"
            elif choice2 == "3":
                slow_print("kamu memilih untuk lari")
                progress_bar(2, "lari menjauh dari gadis itu")
                slow_print("tapi gadis itu kembali muncul di depanmu")
                slow_print(
                    "dengan cepat dia menebas lehermu dengan guntingnya sebelum merobek mulutmu agar jadi seperti dirinya"
                )
                slow_print("kamu tewas di tempat")
                return "game_over"
        elif choice == "2":
            slow_print("kamu memilih untuk tidak mendekatinya")
            progress_bar(2, "menjauh dari gadis itu")
            slow_print("kamu keluar dari ruangan itu")
            return roam5_f3(state)


def roam5_f3(state):
    clear()
    game = MazeGame(gedung_sekolah_f3_no2)
    results = game.start()

    if results == "F4":
        clear()
        slow_print("kamu berjalan ke arah taman")
        slow_print("kamu ingin membuktikan mitos tentang siswi yang jadi hantu")
        state.update({"chapter": 2, "checkpoint": "taman"})
        save_game(state)
        return roam_taman(state)
    elif results == "F1":
        clear()
        slow_print(
            "saat kamu membuka pintu tiba tiba ada mahluk hitam besar yang mencekik dan mematahan lehermu"
        )
        slow_print("keesokkan harinya kamudi temukan tewas di depan pintu F1 sekolahmu")
        return "game_over"
    elif results == "F3":
        clear()
        slow_print("ketika kamu mesuk ke dalam ruangan ")
        slow_print(
            "kamu melihat ada seoarnag gadis berambut hitam yang sedang duduk di pojok ruangan sembari memandang langit"
        )
        choice = (
            input_no_empty("\napakah kamu ingin mendekatinya? (1:ya/2:tidak): ")
            .strip()
            .lower()
        )
        if choice == "1":
            slow_print("kamu mendekatinya dan mencoba mengajak bicara")
            slow_print("tapi dia tidak meresponmu sama sekali")
            slow_print("tiba tiba secara perlahan dia berbalik menatapmu")
            slow_print("matanya merah menyala dan mulutnya robel sampai ke telinganya")
            slow_print("tiba tiba gadis itu bertanya padamu ")
            slow_print("'apakah menurutmu aku cantik??????????'")
            slow_print("1:iya")
            slow_print("2:tidak")
            slow_print("3:lari")
            choice2 = input_no_empty("\n(1/2/3): ").strip().lower()
            clear()
            if choice2 == "1":
                slow_print("kamu menjawab iya")
                slow_print("tiba tiba gadis itu tersenyum lebar dan melompat ke arahmu")
                slow_print("dia mengeluarkan gunting dari sakunya dan merobek mulutmu")
                slow_print("kamu tewas di tempat")
                return "game_over"
            elif choice2 == "2":
                slow_print("kamu menjawab tidak")
                slow_print("tiba tiba gadis itu marah besar")
                slow_print("dengan cepat dia melompat ke arahmu")
                slow_print(
                    "menebas lehermu dengan guntingnya sebelum merobek mulutmu agar jadi seperti dirinya"
                )
                slow_print("kamu tewas di tempat")
                return "game_over"
            elif choice2 == "3":
                slow_print("kamu memilih untuk lari")
                progress_bar(2, "lari menjauh dari gadis itu")
                slow_print("tapi gadis itu kembali muncul di depanmu")
                slow_print(
                    "dengan cepat dia menebas lehermu dengan guntingnya sebelum merobek mulutmu agar jadi seperti dirinya"
                )
                slow_print("kamu tewas di tempat")
                return "game_over"
        elif choice == "2":
            slow_print("kamu memilih untuk tidak mendekatinya")
            progress_bar(2, "menjauh dari gadis itu")
            slow_print("kamu keluar dari ruangan itu")
            return roam5_f3(state)


def roam_taman(state):
    clear()
    slow_print(
        "Kamu berjalan menelusuri ujung lorong kelas angker itu dan berakhir di taman."
    )
    slow_print("Di taman, kamu mendengar seseorang menangis...")
    slow_print("Kamu melihat ke atas pohon — ternyata Mbak Kunti yang menangis.")
    slow_print("Dia melihatmu dan langsung mengejarmu dengan tawanya yang khas!")
    slow_print("Kamu mencoba lari secepat mungkin...")
    pause()
    clear()
    divider()
    slow_print(
        "Kamu terpojok di sudut taman dan Mbak Kunti menatapmu dengan senyuman mengerikan."
    )
    slow_print("Tak ada tempat untuk lari...")
    choice = input_no_empty("\n(1. Ambil foto / 2. Pasrah): ").strip()
    if choice == "1":
        progress_bar(2, "Menyiapkan kamera...")
        slow_print(
            "Kilatan cahaya dari handphone-mu membuatnya silau dan menghilang sementara."
        )
        slow_print("Namun sosok itu masih mengejarmu setelah itu...")
        slow_print(
            "Kamu tiba tiba teringat — ada foto siswi yang meninggal kecelakaan dan dikasih mantra oleh kekasihnya."
        )
        slow_print(
            "Kamu harus menemukan foto yang ada Mbak Kunti itu di dalamnya dan membakarnya."
        )
        slow_print("cepat lari ke kelas untuk mencari fotonya!")
        input_no_empty("\nmasuk '1' untuk melanjutkan...")
    else:
        random_delay_text(
            [
                "Mbak Kunti menerkammu dengan kecepatan luar biasa...",
                "Kamu kerasukan dan disadarkan oleh Pak Satpam di pagi hari...",
            ]
        )
        return "game_over"
    clear()
    game = MazeGame(taman)
    results = game.start()

    if results == "LOSE":
        slow_print("Mbak Kunti menangkapmu dengan tawa mengerikan...")
        slow_print("keesokan harinya, tubuhmu ditemukan di taman oleh Pak Satpam.")
        slow_print("pak satpam bilang kamu bergumam ingin membalas dendam pada andri")
        slow_print("pak satpam melaporkan kejadian itu ke pihak sekolah...")
        slow_print("kamu di skors dari sekolah")
        return "game_over"
    else:
        slow_print("Kamu berhasil masuk ke dalam kelas dengan selamat!")
        state.update({"chapter": 2, "checkpoint": "kelas"})
        save_game(state)
        return kelas(state)


def kelas(state):
    clear()
    divider()
    slow_print("Kamu pun mulai mencari fotonya di setiap bangku.")
    slow_print("Tidak ada satupun... tapi kamu melihat tiga lemari di pojok ruangan.")
    slow_print("1. Lemari kayu yang sudah lapuk")
    slow_print("2. Lemari jati yang kokoh")
    slow_print("3. Lemari etalase dengan kunci unik")

    choice = input_no_empty("\n(ketik 1/2/3): ").strip()

    if choice == "1":
        clear()
        slow_print("Kamu membuka lemari itu perlahan...")
        pause()
        slow_print("*BRUKK!* Lemari itu runtuh karena sudah rapuh!")
        slow_print("Suara keras menarik perhatian Pak Satpam.")
        pause()
        slow_print("Kamu gagal dan diskors karena merusak fasilitas sekolah.")
        return "game_over"

    elif choice == "2":
        clear()
        slow_print(
            "Kamu membuka lemari jati itu... tapi tiba-tiba dorongan keras dari belakang membuat lemari menimpamu!"
        )
        slow_print("Mbak Kunti menatapmu dengan tawa seram.")
        slow_print("Kamu pun menjadi penghuni baru sekolah malam...")
        return "game_over"

    elif choice == "3":
        clear()
        slow_print("Kamu melihat kunci digital aneh di lemari etalase itu.")
        slow_print("Layar menampilkan tulisan samar:")
        slow_print("'Ketika jarum panjang di angka 12, jarum pendek di angka 3...'")
        slow_print("Clue: Waktu ketika lonceng sekolah berbunyi tiga kali.")
        slow_print('!!Gunakan format jam yang benar misal "00:00"!!')
        pause()

        correct_answers = ["15:00", "3:00", "03:00"]
        for attempt in range(3):
            answer = input_no_empty("\nMasukkan waktu yang benar: ").strip()
            if answer in correct_answers:
                clear()
                slow_print("\nJam digital itu menyala... lalu berbunyi *klik!*")
                slow_print(
                    "Lemari terbuka dan kamu menemukan foto Mbak Kunti di dalamnya."
                )
                progress_bar(2, "Menyobek dan membakar foto...")
                slow_print(
                    "Api membakar foto itu perlahan. Mbak Kunti tersenyum sebelum menghilang."
                )
                pause()
                slow_print("Sesuatu jatuh dari dalam lemari...")
                choice2 = input_no_empty(
                    "\n(1. Ambil benda itu / 2. Biarkan): "
                ).strip()
                if choice2 == "1":
                    clear()
                    slow_print(
                        "Kamu mendapatkan *pecahan pipi* dan menyimpannya ke dalam tas."
                    )
                    state.setdefault("inventory", []).append("pecahan_pipi")
                else:
                    clear()
                    slow_print("Kamu memutuskan untuk meninggalkannya.")

                state.update({"chapter": 2, "checkpoint": "taman_selesai"})
                save_game(state)
                return otw_kantin(state)
            else:
                clear()
                slow_print("Jam itu tetap mati...")
                if attempt < 2:
                    slow_print(
                        "Coba pikir lagi... lonceng sekolah biasanya berbunyi jam berapa?"
                    )
                else:
                    clear()
                    slow_print("Tiba-tiba jam itu menyala merah... *ERROR!*")
                    slow_print("Layar pecah dan asap hitam memenuhi ruangan.")
                    return "game_over"
    else:
        clear()
        slow_print(
            "Kamu kebingungan memilih... waktu habis, dan suara tawa Mbak Kunti menggema di belakangmu."
        )
        return "game_over"


def otw_kantin(state):
    clear()
    slow_print("kamu berhasil membakar foto mbak kunti,")
    slow_print("Dan keluar dengan tenang dari kelas itu")
    slow_print("kamupun berjalan menuju kantin")
    input_no_empty("\nmasuk '1' untuk melanjutkan...")
    clear()
    game = MazeGame(to_kantin)
    results = game.start()
    if results == "WIN":
        slow_print("kamu berhasil sampai di kantin dengan selamat")
        state.update({"chapter": 2, "checkpoint": "kantin"})
        save_game(state)
        return area_kantin(state)



def area_kantin(state):
    game = MazeGame(kantin)
    results = game.start()
    if results == "WIN":
        clear()
        slow_print(
            "Suasana hening... tiba-tiba kamu melihat bayanganmu sendiri menatap balik."
        )
        slow_print("Bayangan itu menantangmu bermain 'Gunting Batu Kertas'.")
        slow_print("Menang 3 kali — kamu bebas. Kalah — tubuhmu jadi miliknya.")

        pilihan = ["gunting", "batu", "kertas"]
        map_input = {"1": "gunting", "2": "batu", "3": "kertas"}
        skor_pemain = 0
        skor_bayangan = 0

        pause()
        while skor_pemain < 3 and skor_bayangan < 3:
            divider()
            print(f"(Kamu: {skor_pemain} | Bayangan: {skor_bayangan})")
            player_choice = input_no_empty(
                "\nPilih (1:gunting, 2:batu, 3:kertas): "
            ).strip()
            if player_choice not in map_input:
                slow_print(
                    "Bayangan itu tertawa... 'Kau bahkan tak tahu cara bermainnya?'"
                )
                pause()
                continue

            player_choice = map_input[player_choice]
            enemy_choice = random.choice(pilihan)
            slow_print(f"Bayangan itu memilih: {enemy_choice}")
            pause()

            if player_choice == enemy_choice:
                slow_print("Seri... Bayangan itu menatapmu tanpa ekspresi.")
                pause()
                clear()
            elif (
                (player_choice == "gunting" and enemy_choice == "kertas")
                or (player_choice == "batu" and enemy_choice == "gunting")
                or (player_choice == "kertas" and enemy_choice == "batu")
            ):
                skor_pemain += 1
                slow_print(
                    f"Kamu menang ronde ini! (Kamu: {skor_pemain} | Bayangan: {skor_bayangan})"
                )
                pause()
                clear()
            else:
                skor_bayangan += 1
                slow_print(
                    f"Kamu kalah ronde ini... (Kamu: {skor_pemain} | Bayangan: {skor_bayangan})"
                )
                pause()
                clear()

        divider()
        if skor_pemain == 3:
            slow_print("Bayangan itu perlahan memudar, berbisik pelan...")
            slow_print("'Kau menang kali ini...'")
            input_no_empty("masukkan '1' untuk melanjutkan")
            slow_print("Kamu berhasil lolos dari cengkeraman bayangan itu.")
            state.update({"chapter": 2, "checkpoint": "kantin_selesai"})
            save_game(state)
            return otw_perpus(state)
        else:
            slow_print("Bayangan itu tertawa keras...")
            slow_print("'Sekarang... tubuh ini milikku!'")
            return "game_over"


def otw_perpus(state):
    game = MazeGame(perpustakaan)
    results = game.start()
    if results == "WIN":
        state.update({"chapter": 2, "checkpoint": "perpustakaan"})
        save_game(state)
        return perpus(state)


def perpus(state):
    divider()
    slow_print("Setelah bertemu bayangan tadi kamu sadar...")
    slow_print("Kamu masih diteror dan bingung bagaimana cara mengalahkannya.")
    pause()
    divider()
    slow_print("Di dalam, lampu berkedip-kedip. Kamu tetap masuk dan mencari buku itu.")
    slow_print("Tiba-tiba muncul *Hantu Guru Killer!*")
    slow_print(
        "Dia berkata dengan suara dingin: 'Kalau kau ingin selamat, jawab semua soalku tentang Jawa Timur!'"
    )
    pause()

    questions = [
        {
            "q": "1. Ibu kota provinsi Jawa Timur adalah...",
            "options": ["A. Malang", "B. Surabaya", "C. Kediri", "D. Banyuwangi"],
            "answer": "B",
        },
        {
            "q": "2. Gunung tertinggi di Jawa Timur adalah...",
            "options": ["A. Arjuno", "B. Kelud", "C. Semeru", "D. Raung"],
            "answer": "C",
        },
        {
            "q": "3. Kota penghasil kerajinan topeng Malangan adalah...",
            "options": ["A. Mojokerto", "B. Malang", "C. Blitar", "D. Bojonegoro"],
            "answer": "B",
        },
        {
            "q": "4. Tari tradisional khas Banyuwangi adalah...",
            "options": ["A. Reog", "B. Gandrung", "C. Remo", "D. Jaranan"],
            "answer": "B",
        },
        {
            "q": "5. Makanan khas Surabaya yang terkenal dengan kuah petis adalah...",
            "options": ["A. Soto", "B. Rawon", "C. Lontong Balap", "D. Pecel"],
            "answer": "C",
        },
        {
            "q": "6. Gunung Bromo terletak di wilayah...",
            "options": [
                "A. Pasuruan, Probolinggo, Lumajang",
                "B. Malang, Batu, Jember",
                "C. Jepang, Korea, China",
                "D. Sleman, Magelang, Boyolali",
            ],
            "answer": "A",
        },
    ]

    score = 0
    for q in questions:
        divider()
        slow_print(q["q"])
        for opt in q["options"]:
            print(opt)
        answer = input_no_empty("\nJawabanmu (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            slow_print("✅ Benar!")
            score += 1
            pause()
            clear()
        else:
            slow_print("❌ Salah!")
            pause()
            clear()

    divider()
    slow_print(f"Kamu menjawab benar {score} dari {len(questions)} soal.")
    pause()

    if score < 4:
        slow_print("😈 Hantu itu tertawa... 'Kau bodoh! Tempatmu di sini selamanya!'")
        return "game_over"

    slow_print("🔥 Hantu guru itu perlahan menghilang...")
    slow_print("sebelum dia menghilang, dia berbisik")
    slow_print('"kerja bagus nak"')
    slow_print('"pergilah ke aula nak"')
    slow_print('"kamu bisa ke aula dengan aman jika lewat area masjid')
    slow_print("kemudian hantu itu menghilang dengan senyuman di wajahnya")
    input_no_empty("\nmasukan '1' untuk melanjutkan...")
    state["inventory"].append("pecahan_makutha")
    state.update({"chapter": 2, "checkpoint": "perpustakaan_selesai"})
    save_game(state)
    return otw_masjid(state)


def otw_masjid(state):
    clear()
    game = MazeGame(perpustakaan2)
    results = game.start()
    if results == "WIN":
        slow_print("kamu berhasil sampai di masjid dengan selamat")
        state.update({"chapter": 2, "checkpoint": "masjid"})
        save_game(state)
        return area_masjid(state)


def area_masjid(state):
    clear()
    slow_print("di area masjid kamu melihat ada satpam yang sedang berjaga")
    slow_print("kamu harus bisa ke aula tanpa tertangkap satpam")
    input_no_empty("\nmasuk '1' untuk melanjutkan...")
    clear()
    game = MazeGame(masjid)
    results = game.start()
    if results == "F2":
        slow_print("kamu berhasil melewati para satpam tanpa ketauhan")
        state.update({"chapter": 2, "checkpoint": "area_masjid"})
        save_game(state)
        return otw_aula(state)
    elif results == "F1":
        slow_print("kamu menuju aula")
        state.update({"chapter": 2, "checkpoint": "masjid_selesai"})
        save_game
        return akhir(state)


def otw_aula(state):
    clear()
    slow_print(
        "Kamu mengecek dan melihat sosok yang sedang meringkuk di pinggir toilet."
    )
    slow_print("Kamu memotretnya dan mendapatkan *pecahan paningal kiwo*.")
    slow_print("kamupun menunggu para satpam pergi dari area masjid")
    progress_bar(2, "menunggu satpam pergi...")
    slow_print("para satpam sudah pergi dari area masjid")
    slow_print("pergilah ke aula")
    slow_print("sekarang saatnya menyelesaikan semuanya.....")
    input_no_empty("\nmasuk '1' untuk melanjutkan...")
    clear()
    game = MazeGame(masjid2)
    results = game.start()
    if results == "F1":
        slow_print("kamupun tiba di aula")
        state.update({"chapter": 2, "checkpoint": "masjid_selesai"})
        state["inventory"].append("pecahan_paningal_kiwo")
        save_game(state)
        return akhir(state)


def akhir(state):
    clear()
    divider()
    slow_print("dari jauh nampak bayangan")
    slow_print("bayangan itu sudah menunggumu — lebih BESAR, GELAP, dan MENAKUTKAN.")
    slow_print("kamu mencoba mendekat")
    progress_bar(2, "mendekati bayangan")
    slow_print("bayangan itu tiba tiba menatapmu")
    slow_print(
        "kamu terkejut bayangan itu memiliki wujud yang sama dengan mu(hanya sedikit lebih hitam)"
    )
    slow_print("bayangan itu menatapmu dengan senyum mengerikan")

    game = MazeGame(aula)
    results = game.start()
    if results == "WIN":
        slow_print("kamupun menghadapi bayanganmu sendiri...")
        slow_print("................")
        clear()
        slow_print("⚔️  PERTARUNGAN DIMULAI: DIRIMU VS BAYANGANMU ⚔️")
        pause()

        battle = BattleGame()
        battle.run()

        if battle.enemy_health <= 0 and battle.player_health > 0:
            divider()
            slow_print("🔥 Kau menatap tubuh bayanganmu yang mulai memudar.")
            progress_bar(2, "bayanganmu mulai memudar")
            slow_print("bayanganmu menghilang")
            slow_print("sepertinya kamu menang")
            state["inventory"].append("pecahan_paningal_tengen")
            state.update({"chapter": 2, "checkpoint": "selesai"})
            save_game(state)
            progress_bar(2, "Menyimpan progress dan menutup...")
            pause()
            return "next"
        else:
            divider()
            slow_print("💀 Bayanganmu menatapmu dingin...")
            slow_print("'Kau belum siap menghadapi dirimu sendiri,' katanya.")
            slow_print("Tubuhmu melemah, dan dunia mulai memudar dalam kegelapan...")
            return "game_over"


class BattleGame:
    def __init__(self):
        self.player_health = 100
        self.enemy_health = 100
        self.player_charging = 0
        self.enemy_charging = 0
        self.turn_count = 0
        self.game_over = False

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_ui(self):
        self.clear_screen()
        print("=" * 50)
        print("           PERTARUNGAN TURN-BASED")
        print("=" * 50)

        player_hp_percent = max(0, self.player_health) / 100
        enemy_hp_percent = max(0, self.enemy_health) / 100

        player_bar = "█" * int(player_hp_percent * 30) + " " * (
            30 - int(player_hp_percent * 30)
        )
        enemy_bar = "█" * int(enemy_hp_percent * 30) + " " * (
            30 - int(enemy_hp_percent * 30)
        )

        print(f"\nPLAYER:")
        print(f"HP: [{player_bar}] {self.player_health}/100")

        status_player = []
        if self.player_charging > 0:
            status_player.append(f"⚡ CHARGING ({self.player_charging}/2)")
        if status_player:
            print("Status: " + " ".join(status_player))

        print(f"\nMUSUH:")
        print(f"HP: [{enemy_bar}] {self.enemy_health}/100")

        status_enemy = []
        if self.enemy_charging > 0:
            status_enemy.append(f"⚡ CHARGING ({self.enemy_charging}/2)")
        if status_enemy:
            print("Status: " + " ".join(status_enemy))

        print(f"\nTurn: {self.turn_count}")
        print("-" * 50)

    def display_moves(self):
        print("\nPILIH AKSI:")
        if self.player_charging > 0:
            print("⚡ Anda sedang CHARGING serangan kuat!")
            if self.player_charging == 1:
                print("➤ CHARGING... (1/2) - Tekan Enter untuk melanjutkan")
            else:
                print("➤ CHARGING SELESAI! (2/2) - Tekan Enter untuk menyerang")
            print("\nTekan Enter untuk melanjutkan...", end="")
            return ["continue"]

        moves = []
        print("1. ⚔️  SERANG CEPAT (15-20 damage)")
        moves.append("1")

        print("2. ⚡ SERANG KUAT (10-80 damage, butuh 2 turn charging)")
        moves.append("2")

        print("3. 🛡️  BERTAHAN (kurangi damage 50% untuk 1 turn)")
        moves.append("3")

        print("4. 🏳️  MENYERAH (langsung kalah)")
        moves.append("4")

        return moves

    def player_attack_fast(self):
        damage = random.randint(15, 20)
        self.enemy_health -= damage
        return damage

    def player_start_charge(self):
        if self.player_charging == 0:
            self.player_charging = 1
            return "Anda mulai CHARGING serangan kuat! (1/2)"
        return ""

    def player_continue_charge(self):
        if self.player_charging == 1:
            self.player_charging = 2
            return "Anda melanjutkan CHARGING! (2/2) - Siap menyerang turn depan!"
        elif self.player_charging == 2:
            damage = random.randint(10, 80)
            self.enemy_health -= damage
            self.player_charging = 0
            return damage, "Serangan kuat TERLEPAS! ⚡"
        return 0, "Charging belum selesai!"

    def player_defend(self):
        return "Anda dalam mode BERTAHAN! Damage dikurangi 50%"

    def enemy_ai(self):
        if self.enemy_charging > 0:

            self.enemy_charging += 1

            if self.enemy_charging >= 3:
                damage = random.randint(30, 45)
                self.player_health -= damage
                self.enemy_charging = 0
                return (
                    damage,
                    f"Bayanganmu melepaskan serangan gelap! ⚡ {damage} damage!",
                )

            return (
                0,
                f"Bayanganmu masih mengumpulkan kekuatan... ({self.enemy_charging}/2)",
            )

        if random.random() < 0.3:
            self.enemy_charging = 1
            return 0, "Bayanganmu mulai mengisi energi kegelapan... (1/2)"

        damage = random.randint(10, 18)
        self.player_health -= damage
        return damage, f"Bayangan menyerang cepat! ⚔️ {damage} damage!"

    def process_turn(self, player_choice, available_moves):
        player_message = ""
        enemy_message = ""
        player_defending = False

        if self.player_charging > 0:
            if self.player_charging == 1:
                self.player_charging = 2
                player_message = (
                    "Anda melanjutkan CHARGING! (2/2) - Siap menyerang turn depan!"
                )
            else:
                damage = random.randint(40, 50)
                self.enemy_health -= damage
                self.player_charging = 0
                player_message = f"Serangan kuat TERLEPAS! ⚡ {damage} damage!"

        elif player_choice not in available_moves:
            player_message = "Pilihan tidak valid! Melewatkan turn."

        elif player_choice == "1":
            damage = self.player_attack_fast()
            player_message = f"Anda menyerang cepat! ⚔️ {damage} damage!"

        elif player_choice == "2":
            player_message = self.player_start_charge()

        elif player_choice == "3":
            player_defending = True
            player_message = self.player_defend()

        elif player_choice == "4":
            self.game_over = True
            return "MENYERAH", "Anda menyerah! Pertarungan berakhir."

        if not self.game_over:
            damage, enemy_msg = self.enemy_ai()

            if player_defending and damage > 0:
                damage = max(1, damage // 2)
                enemy_msg += f" (Dikurangi 50% karena bertahan → {damage} damage)"
                self.player_health += damage
                self.player_health -= damage // 2

            enemy_message = enemy_msg

        self.turn_count += 1

        return player_message, enemy_message

    def check_winner(self):
        if self.player_health <= 0 and self.enemy_health <= 0:
            return "DRAW"
        elif self.player_health <= 0:
            return "MUSUH"
        elif self.enemy_health <= 0:
            return "PLAYER"
        return None

    def show_battle_result(self, player_msg, enemy_msg):
        print(f"\n{'='*50}")
        print("HASIL TURN:")
        slow_print(f"➤ Player: {player_msg}")
        if enemy_msg:
            slow_print(f"➤ Musuh: {enemy_msg}")
        print(f"{'='*50}")
        print(f"\nUpdate Health:")
        print(f"Player HP: {max(0, self.player_health)}/100")
        print(f"Musuh HP: {max(0, self.enemy_health)}/100")

        input("\nTekan Enter untuk melanjutkan...")

    def run(self):
        slow_print("Kamu melawan Bayanganmu")
        print("Serangan kuat butuh 2 turn charging dan TIDAK BISA DIBATALKAN!")
        print("PERINGATAN: Once you go charging, you can't go back!")
        input_no_empty("masukkan '1' untuk mulai...")

        while not self.game_over:
            self.display_ui()
            available_moves = self.display_moves()
            try:
                if available_moves == ["continue"]:
                    choice = "continue"
                    input()
                else:
                    choice = input_no_empty("Pilih aksi (1-4): ").strip()
            except KeyboardInterrupt:
                print("\n\nGame dihentikan!")
                break
            player_msg, enemy_msg = self.process_turn(choice, available_moves)
            if choice != "4":
                self.show_battle_result(player_msg, enemy_msg)
            winner = self.check_winner()
            if winner:
                self.game_over = True
                self.display_ui()

                if winner == "PLAYER":
                    print(f"\n🎉 VICTORY! Anda menang dalam {self.turn_count} turn!")
                elif winner == "MUSUH":
                    print(f"\n💀 DEFEAT! Musuh menang dalam {self.turn_count} turn!")
                else:
                    print(f"\n🤝 DRAW! Keduanya kalah dalam {self.turn_count} turn!")

                print("=" * 50)
                break
            if choice == "4":
                self.display_ui()
                print(f"\n🏳️  Anda menyerah! Musuh menang!")
                print("=" * 50)
                break
