import os
from mahasiswa import *

def main():
    os.system('cls')
    while True:
        read_mahasiswa()
        print("\nMenu:")
        print("1 - Add | 2 - Edit | 3 - Delete | 4 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system('cls')
            print("Create Mahasiswa")
            print("================\n")
            nim = input("Enter NIM: ")
            nama = input("Enter Nama: ")
            jk = input("Enter Jenis Kelamin: ")
            prodi = input("Enter Prodi: ")
            create_mahasiswa(nim, nama, jk, prodi)
            os.system('cls')
            
        elif choice == "2":
            os.system('cls')
            kode = input("Enter NIM of Mahasiswa to update: ")
            id, nim, nama, jk, prodi = get_mahasiswa(kode)
            print("Data Mahasiswa")
            print("================\n")
            print("ID:", id)
            print("NIM:", nim)
            print("Nama:", nama)
            print("Jenis Kelamin:", jk)
            print("Prodi:", prodi)
            print(" ")
            print("Edit Mahasiswa")
            print("================\n")
            new_nama = input("Enter new Nama: ")
            new_jk = input("Enter new Jenis Kelamin: ")
            new_prodi = input("Enter new Prodi: ")
            update_mahasiswa(nim, new_nama, new_jk, new_prodi)
            os.system('cls')

        elif choice == "3":
            nim = input("Enter NIM of Mahasiswa to delete: ")
            delete_mahasiswa(nim)
            os.system('cls')

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()