from Data.user import User

def main():
    users = {}

    while True:
        print("\nMenu:")
        print("1. Mulai Parkir")
        print("2. Akhiri Parkir")
        print("3. Lihat Riwayat Parkir")
        print("4. Keluar")
        
        choice = input("Pilih opsi: ")

        if choice == "1":
            name = input("Masukkan nama pengguna: ")
            vehicle_type = input("Masukkan jenis kendaraan (mobil/sepeda motor/lainnya): ")

            if name not in users:
                users[name] = User(name)

            user = users[name]
            parking_session = user.start_parking(vehicle_type)
            print(f"Atas nama {parking_session.user_name} dengan kendaraan {parking_session.vehicle_type} pada {parking_session.start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        elif choice == "2":
            name = input("Masukkan nama pengguna: ")

            if name in users:
                user = users[name]
                end_session = user.end_parking()
                if isinstance(end_session, str):
                    print(end_session)
                else:
                    print(f"Diakhiri pada {end_session.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("Pengguna tidak ditemukan.")

        elif choice == "3":
            name = input("Masukkan nama pengguna: ")

            if name in users:
                user = users[name]
                history = user.get_parking_history()
                for session in history:
                    print(session)
            else:
                print("Pengguna tidak ditemukan")

        elif choice == "4":
            break

        else:
            print("Opsi tidak valid. Silakan coba lagi")

if __name__ == "__main__":
    main()
