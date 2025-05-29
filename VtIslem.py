#pip install mysql-connector-python
import  mysql.connector as mysqlcon
Baglanti=mysqlcon.connect(
    host="localhost",
    user="root",
    password="",
    database="pyvt"
)

def EkleSilGuncelleme(sql,tip):
    try:
        Isleyici=Baglanti.cursor()
        Isleyici.execute(sql)
        Baglanti.commit()
        Isleyici.Close()
        print (f"Kayıt başarıyla {tip} di.")
    except Exception as hata:
        print(f"Kayıt {tip} di. \n{hata} hatası oluştu.") 


def TekilGetir(sql):
    try:
        Isleyici=Baglanti.cursor()
        Isleyici.execute(sql)
        Sonuc=Isleyici.fetchone()
        Isleyici.Close()
        return Sonuc
    except Exception as hata:
        print(f"Kayıt getirilemedi. \n{hata} hatası oluştu.")
        return None
    
def TamaminiGetir(sql):
    try:
        Isleyici=Baglanti.cursor()    
        Isleyici.execute(sql)
        Sonuc=Isleyici.fetchall()
        Isleyici.close()
        return Sonuc
    except Exception as hata:
        print(f"Kayıtlar getirilemedi.\n{hata} hatası oluştu.")
        return None
