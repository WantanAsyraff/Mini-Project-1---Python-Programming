
import os 
import mysql.connector as sql_connect

mydb = sql_connect.connect(
    host="localhost",
    user="root",
    password="",
    database="kamsis_reports"
)

cursor = mydb.cursor()

# Masukkan ke dalam database baru
def insert_data(noBilik, saizBilik, namaPelapor, jenisKerosakan, cadanganPenerangan):
    cursor.execute(
        "INSERT INTO reports (noBilik, saizBilik, namaPelapor, jenisKerosakan, cadanganPenerangan) VALUES (%s, %s, %s, %s, %s)",
        (noBilik.capitalize(), saizBilik.capitalize(), namaPelapor.capitalize(), jenisKerosakan.capitalize(), cadanganPenerangan.capitalize())
    )
    mydb.commit()
    print("Data inserted sucessfully")

# Kita guna refNumber sebagai ID aduan pelapor puuurrr meow meow
def delete_data(refNumber):
    cursor.execute(
        "DELETE FROM reports WHERE refNumber= (%s)",
        (refNumber,)
    )
    mydb.commit()
    print("Data deleted sucessfully")

# Kita guna refNumber sebagai ID aduan pelapor puuurrr meow meow (kali 2)
def search_data(refNumber):
    cursor.execute(
        "SELECT  * FROM reports WHERE refnumber = %s",
        (refNumber,)
    )
    results = cursor.fetchone()
    return results

# Update data yg dah wujud
def update_data(refNumber, noBilik, saizBilik, namaPelapor, jenisKerosakan, cadanganPenerangan):
    cursor.execute(
        """
        UPDATE reports 
        SET noBilik = %s, saizBilik = %s, namaPelapor = %s, jenisKerosakan = %s, cadanganPenerangan = %s 
        WHERE refNumber = %s
        """,
        (noBilik.capitalize(), saizBilik.capitalize(), namaPelapor.capitalize(), jenisKerosakan.capitalize(), cadanganPenerangan.capitalize(),refNumber
        )
    )
    mydb.commit()
    print("Data updated successfully")
