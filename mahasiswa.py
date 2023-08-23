from db import *

def create_mahasiswa(nim, nama, jk, prodi):
    query = "INSERT INTO mahasiswa (nim, nama, jk, prodi) VALUES (%s, %s, %s, %s)"
    values = (nim, nama, jk, prodi)
    cursor.execute(query, values)
    db.commit()
    read_mahasiswa()
    print("Mahasiswa created successfully!")

def read_mahasiswa():
    query = "SELECT * FROM mahasiswa"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

def get_mahasiswa(kode):
    query = "SELECT * FROM mahasiswa WHERE nim = %s"
    values = (kode,)
    cursor.execute(query, values)
    result = cursor.fetchone()  # Use fetchone() as you are fetching a single row
    if result:
        id, nim, nama, jk, prodi = result
        return id, nim, nama, jk, prodi
    else:
        return None

def update_mahasiswa(nim, new_nama, new_jk, new_prodi):
    query = "UPDATE mahasiswa SET nama = %s, jk = %s, prodi = %s WHERE nim = %s"
    values = (new_nama, new_jk, new_prodi, nim)
    cursor.execute(query, values)
    db.commit()
    read_mahasiswa()
    print("Mahasiswa updated successfully!")

def delete_mahasiswa(nim):
    query = "DELETE FROM mahasiswa WHERE nim = %s"
    value = (nim,)
    cursor.execute(query, value)
    db.commit()
    read_mahasiswa()
    print("Mahasiswa deleted successfully!")