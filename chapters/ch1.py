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
from maze_engine import MazeGame
from maze_map import (
    Lapangan,
    depan_gedung,
    gedung_sekolah,
    gedung_sekolah_f3,
    gedung_sekolah_f2,
    lorong_satpam,
    ruang_kelas1,
    ruang_kelas2,
    taman,
)


def start_chapter(state=None, checkpoint="start"):
    if state is None:
        state = {"chapter": 1, "checkpoint": "start", "inventory": []}
    elif checkpoint == "roam1":
        return roam1(state)
    elif checkpoint == "roam2":
        return roam2(state)
    elif checkpoint == "roam3":
        return roam3(state)
    elif checkpoint == "ruang_kelas":
        return ruang_kelas(state)
    elif checkpoint == "roam4":
        return roam4(state)
    elif checkpoint == "roam5":
        return roam5(state)
    elif checkpoint == "ruang_kosong":
        return ruang_kosong(state)
    elif checkpoint == "ruang_kosong_selesai":
        return "next"

    clear()
    divider()
    slow_print(
        "Selamat datang di sekolahmu yang ingin kamu kunjungi di waktu malam", 0.04
    )
    slow_print("Kamu ingin membuktikan bahwa di dalam sekolahmu saat malam hari...")
    slow_print("...terdapat aktivitas tak kasat mata yang bisa kamu temui.")
    slow_print(
        "Kamu akan berperan sebagai Raka — siswa paling bandel soal hal-hal mistis."
    )
    slow_print("Kamu memiliki beberapa misi:")
    slow_print("1. Menemukan buku yang kamu tinggal")
    slow_print("2. Membakar foto yang memiliki mantra")
    slow_print("3. Mengambil semua foto entitas yang kamu temui")
    slow_print("4. Mengalahkan bayanganmu dalam mode iblis")
    slow_print("5. Menang dalam semua tantangan dan keluar tanpa bertemu satpam")

    pause()
    clear()
    divider()
    slow_print("Kamu sudah berada di depan sekolahanmu dan melihat Pak Satpam.")
    slow_print("Kamu memiliki 2 opsi untuk memasuki sekolahan:")

    while True:
        choice = input_no_empty("\n(ketik 1 untuk izin, 2 untuk diam-diam): ").strip()

        if choice == "1":
            slow_print(
                "\nKamu menghampiri satpam dan menjelaskan alasanmu datang malam-malam..."
            )
            slow_print("Satpam menatapmu curiga, dan mengusirmu.")
            return "game_over"

        elif choice == "2":
            slow_print("\nKamu memilih mengendap-endap melalui sisi pagar.")
            slow_print(
                "Namun kakimu tersandung ranting kering dan menimbulkan suara keras!"
            )
            slow_print("Satpam menyorotkan senter ke arahmu!")
            progress_bar(2, "Berlari menjauh dari satpam")
            slow_print(
                "Kamu berlari masuk ke lapangan gelap, jantung berdegup kencang..."
            )
            progress_bar(2, "Menyelinap menuju gedung utama")

            state.update({"chapter": 1, "checkpoint": "roam1"})
            save_game(state)
            return roam1(state)

        else:
            slow_print("\nKamu ragu-ragu... dan waktu terus berjalan...")
            slow_print("Satpam mendekat curiga. Kamu kehilangan kesempatan!")
            return "game_over"


def roam1(state):
    clear()
    slow_print("Kamu berhasil masuk ke dalam sekolah!")
    slow_print(
        "Tapi tunggu... Pak Satpam tampaknya menyadari kehadiranmu dan mulai mencarimu!"
    )
    slow_print("Kamu harus segera bersembunyi agar tidak ketahuan!")
    slow_print(
        "Gunakan tombol W A S D untuk bergerak dan capai titik 'F' untuk keluar."
    )
    input_no_empty('masukkan "1" untuk melanjutkan')

    game = MazeGame(Lapangan)
    results = game.start()

    if results == "WIN":
        slow_print("kamu berhasil sembunyi dari satpam!")

        state.update({"chapter": 1, "checkpoint": "roam2"})
        save_game(state)
        return roam2(state)
    else:
        slow_print("kamu tertangkap satpam!")
        return "game_over"


def roam2(state):
    clear()
    slow_print("Kamu melanjutkan perjalanan menuju gedung utama sekolah.")
    slow_print("Namun, ada 3 lorong di depanmu yang bisa kamu pilih")
    input_no_empty("\nMasukkan '1' untuk melanjutkan...")

    game = MazeGame(depan_gedung)
    results = game.start()
    if results == "F1":
        clear()
        game = MazeGame(lorong_satpam)
        results = game.start()
        if results == "WIN":
            slow_print("kamu berhasil melewati lorong satpam")
            state.update({"chapter": 1, "checkpoint": "roam3"})
            save_game(state)
            return roam3(state)

    elif results == "F2":
        clear()
        slow_print("kamu di hadapkan dengan pintu terkunci")
        slow_print("saat kamu menoleh ke kanan disana tertulis")
        slow_print('"Tahun kelahiran Bung Tomo"')
        answer = input_no_empty("\nMasukkan jawaban untuk membuka pintu: ").strip()
        if answer == "1920":
            slow_print("pintu terbuka kamu berhasil masuk ke lorong menuju ruang kelas")
            state.update({"chapter": 1, "checkpoint": "roam3"})
            save_game(state)
            return roam3(state)
        else:
            slow_print("jawaban salah pintu tetap terkunci")
            slow_print(
                "kamu menunggu di depan pintu tapi satpam datang dan menangkapmu"
            )
            return "game_over"
    elif results == "F3":
        clear()
        slow_print("kamu memasuki lorong gelap")
        slow_print(
            "tiba tiba ada sosok hitam besar dengan mata merah menyala menghadangmu"
        )
        slow_print("kamu berusaha lari tapi dia menangkap dan mencekik lehermu")
        slow_print("kamu tewas di tempat")
        return "game_over"


def roam3(state):
    clear()
    slow_print("kamu berada di sebuah lorong menuju ruang kelas")
    input_no_empty("\nMasukkan '1' untuk melanjutkan...")
    game = MazeGame(ruang_kelas1)
    results = game.start()
    if results == "WIN":
        slow_print("kamu berhasil masuk ke ruang kelas")
        state.update({"chapter": 1, "checkpoint": "ruang_kelas"})
        save_game(state)
        return ruang_kelas(state)


def ruang_kelas(state):
    clear()
    divider()
    slow_print(
        "Setibanya di kelas, kamu melihat sosok berdiri di pojok ruangan — tepat di bangkumu."
    )
    slow_print("Kamu memiliki dua pilihan untuk mengambil buku itu:")
    slow_print("1. Pura-pura tidak melihatnya.")
    slow_print("2. Memotretnya terlebih dahulu sebelum mengambil.")
    while True:
        choice = input_no_empty("\n(ketik 1/2): ").strip()
        if choice == "1":
            random_delay_text(
                [
                    "Kamu berpura-pura tidak melihat...",
                    "Langkahmu pelan mendekat ke bangku...",
                    "Tiba-tiba sosok itu bergerak cepat!",
                    "Dia merasukimu!",
                ]
            )
            return "game_over"

        elif choice == "2":
            progress_bar(2, "Menyiapkan kamera...")
            slow_print(
                "Kilatan cahaya dari handphone-mu membuatnya silau dan menghilang."
            )
            slow_print("Sosok hitam itu meninggalkan sebuah benda misterius di mejamu.")
            slow_print("1. Ambil benda itu.")
            slow_print("2. Biarkan saja dan ambil bukumu cepat-cepat.")
            choice2 = input_no_empty("\n(ketik 1/2): ").strip()
            if choice2 == "1":
                progress_bar(2, "Mengambil benda misterius")
                slow_print("Kamu mendapatkan *pecahan lathi* dan menyimpannya di tas.")
                state.setdefault("inventory", []).append("pecahan_lathi")
            else:
                slow_print("Kamu memutuskan untuk tidak mengambilnya.")
            slow_print("Kamu berhasil mengambil bukumu.")
            progress_bar(2, "Memasukkan buku ke tas")

            state.update({"chapter": 1, "checkpoint": "roam4"})
            save_game(state)
            return roam4(state)


def roam4(state):
    clear()
    game = MazeGame(ruang_kelas2)
    results = game.start()
    if results == "WIN":
        slow_print("kamu berhasil keluar dari ruang kelas")
        state.update({"chapter": 1, "checkpoint": "roam5"})
        save_game(state)
        return roam5(state)


def roam5(state):
    clear()
    slow_print("setelah keluar dari kelas kamupun melanjutkan perjalananmu")
    slow_print("kamu di hadapkan dengan 3 kelas pilih salah satu untuk di masuki")
    input_no_empty("\nMasukkan '1' untuk melanjutkan...")
    game = MazeGame(gedung_sekolah)
    results = game.start()

    if results == "F1":
        clear()
        slow_print(
            "saat kamu membuka pintu tiba tiba ada mahluk hitam besar yang mencekik dan mematahan lehermu"
        )
        slow_print("keesokkan harinya kamudi temukan tewas di depan pintu F1 sekolahmu")
        return "game_over"
    elif results == "F2":
        clear()
        slow_print("kamu menemukan kelas kosong")
        state.update({"chapter": 1, "checkpoint": "ruang_kosong"})
        save_game(state)
        return ruang_kosong(state)
    elif results == "F3":
        clear()
        slow_print("ketika kamu mesuk ke dalam ruangan ")
        slow_print(
            "kamu melihat ada seorang gadis berambut hitam yang sedang duduk di meja pojok belakang kelas sembari memandang langit"
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
            slow_print("matanya merah menyala dan mulutnya robek sampai ke telinganya")
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
    game = MazeGame(gedung_sekolah_f3)
    results = game.start()

    if results == "F1":
        slow_print(
            "saat kamu membuka pintu tiba tiba ada mahluk hitam besar yang mencekik dan mematahan lehermu"
        )
        slow_print("keesokkan harinya kamudi temukan tewas di depan pintu F1 sekolahmu")
        return "game_over"
    elif results == "F2":
        slow_print("kamu menemukan kelas kosong")
        state.update({"chapter": 1, "checkpoint": "ruang_kosong"})
        save_game(state)
        return ruang_kosong(state)
    elif results == "F3":
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


def ruang_kosong(state):
    clear()
    divider()
    random_delay_text(
        [
            "Kamu berjalan menuju ruang kosong di tengah koridor...",
            "Ruang itu dingin dan penuh debu...",
            "Tiba-tiba muncul ide gila — bagaimana jika melakukan pemanggilan arwah di sini?",
        ]
    )

    slow_print("Apakah kamu ingin memulai ritual?")
    slow_print("1. Ya, lakukan ritual.")
    slow_print("2. Tidak, tinggalkan ruangan.")
    while True:

        choice = input_no_empty("\n(ketik 1/2): ").strip()

        if choice == "1":
            clear()
            progress_bar(3, "Menyiapkan ritual...")
            slow_print(
                "Kamu menyalakan lilin dan membaca mantra dari buku catatan lama."
            )
            random_delay_text(
                [
                    "Udara di ruangan menjadi berat...",
                    "Bayanganmu di dinding mulai bergerak sendiri...",
                    "Sebuah suara berbisik: 'Kau memanggilku...?'",
                ]
            )
            slow_print("Kamu baru saja membangunkan sesuatu yang tidak seharusnya...")
            return "game_over"

        else:
            clear()
            slow_print(
                "Kamu memutuskan untuk tidak melanjutkan ritual dan keluar dari ruangan itu."
            )
            slow_print("Namun, pintu tiba-tiba terkunci!")
            slow_print("Di dalam ruangan itu terdapat tiga kaca besar...")
            slow_print(
                "Masing-masing memperlihatkan bayanganmu versi hitam dengan mata merah menyala."
            )
            pause()
            slow_print("Bayangan itu menantangmu untuk menebak mana yang asli.")
            divider()
            slow_print("1. Dengan mata merah menyala — berada di kanan.")
            slow_print("2. Dengan senyum lebar — berada di tengah.")
            slow_print("3. Dengan gigi runcing — berada di kiri.")
            divider()
            slow_print(
                "Clue: kanan memang seharusnya di kanan, kiri tidak di kiri, tengah tidak di tengah."
            )
            choice = input_no_empty("\n(ketik 1/2/3): ").strip()

            if choice == "1":
                clear()
                slow_print("\nKamu menebak dengan benar!")
                progress_bar(2, "Bayangan itu berteriak marah...")
                slow_print("Bayangan itu menghancurkan kaca lalu menghilang.")
                slow_print("Di sudut ruangan, kamu melihat sebuah benda jatuh.")
                slow_print("1. Ambil benda itu.")
                slow_print("2. Abaikan dan keluar dari ruangan.")
                item_choice = (
                    input_no_empty(
                        "\nApakah kamu ingin mengambil benda yang jatuh? (1/2): "
                    )
                    .strip()
                    .lower()
                )
                if item_choice == "1":
                    slow_print("Kamu memungut benda itu perlahan...")
                    progress_bar(2, "Memeriksa benda misterius")
                    slow_print("Itu adalah sebuah pecahan topeng.")
                    slow_print("Kamu menyimpannya ke dalam tas.")
                    state.setdefault("inventory", []).append("pecahan_grana")
                else:
                    pass
                progress_bar(2, "Melangkah keluar dari ruang kosong")
                state.update({"chapter": 1, "checkpoint": "ruang_kosong_selesai"})
                save_game(state)
                return "next"

            else:
                clear()
                random_delay_text(
                    [
                        "Ketiga bayanganmu menatap tajam...",
                        "Suara tawa menggelegar memenuhi ruangan...",
                        "Kaca pecah serentak dan mereka menyerangmu!",
                    ]
                )
                return "game_over"
