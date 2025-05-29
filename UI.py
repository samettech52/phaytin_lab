import VtIslem as vt
while True:
    secim=input("eklemek için e ye basınız,aramak için a ya basınız,silmek için s ye basınız ,listelemek için y ye basınız , güncellemek için g ye basınız, çıkmak için ç ye basınız")
    secim=str.upper(secim)
    match(secim):
        case "ç":
            break
        case "E":
            no=input("Adı giriniz:")
            adsa=input("Soyadı giriniz:")
            dt=input("dogum tarihini giriniz:")
            yas=int(input("Yaşını giriniz:"))
            giris=input("durumu giriniz aktif için a / pasif için p")
            if(giris=="A"):
                ak=True
            else:
                ak=False
            sql=f"insert into ogrenciler(OgrNo ,AdSoyad,DogTar,Yas,Aktif) VALUES('{no}','{adsa}','{dt}',{yas},{ak})"
            vt.EkleSilGuncelleme(sql,"ekleme")
        case "Y":
            sql="SELECT * FROM ogrenciler"
            ogrlist=vt.TamaminiGetir
            if ogrlist:
                print(f"{"ID":<15}{"Öğrenci No":<15}{"Ad soyad":<20} {"Doğum Tarihi":<15} {"Yaş":<10} {"Durum":<10}")
                for ogr in ogrlist:
                    if ogr:
                        if(ogr[5]=="1"):
                            ak="Aktif"
                        else:
                            ak="Pasif"
                        print(f"{ogr[0]:<15}{ogr[1]:<15}{ogr[2]:<20}{ogr[3]:<15}{str(ogr[4]):<10}{ak:<10}")
                    else:
                        print("listelencek kayıt bulunadı")
        case "A":
            giris=input("ogrenci numarası tada adını girin")
            sql=f"SELECT * FROM ogrenciler WHERE OgrNo like '%{giris}%' or AdSoyad like'%{giris}%'"
            ogr=vt.TamaminiGetir(sql=)
            if ogrlist:
                print(f"{"ID":<15}{"Öğrenci No":<15}{"Ad soyad":<20} {"Doğum Tarihi":<15} {"Yaş":<10} {"Durum":<10}")
                for ogr in ogrlist:      
                    if(ogr[5]=="1"):
                        ak="Aktif"
                    else:
                        ak="Pasif"
                    print(f"{ogr[0]:<15}{ogr[1]:<15}{ogr[2]:<20}{ogr[3]:<15}{str(ogr[4]):<10}{ak:<10}")
                else:
                    ("listelencek kayıt bulunmadı")
        case "S":
            giris=input("ogrenci numarası girin")
            sql=f"SELECT ID FROM ogrenciler WHERE OgrNo='{giris}'"
           
            ogr=vt.TekilGetir(sql)
            if ogr:
                 sql=f"DELETE FROM ogrenciler WHERE OgrNo='{giris}'"
                 vt.EkleSilGuncelleme(sql,"silme")
            else:
                print("ogrenci bulamadığında silinemedi ")
        case "G":
            giris=input("ogrenci numarası girin")
            sql=f"SELECT * FROM ogrenciler WHERE OgrNo='{giris}'"
            ogr=vt.TekilGetir(sql)
            if ogr:
                ogrSut=[]
                no=input("Öğrenci Numarsını Giriniz : ")
                if no:
                    ogrSut.append(no)
                else:
                    ogrSut.append(ogr[1])
                adsa=input("Adı Soyadı Giriniz : ")
                if adsa:
                    ogrSut.append(adsa)
                else:
                    ogrSut.append(ogr[2])
                dt=input("Doğum Tarihi Giriniz : ")
                if dt:
                    ogrSut.append(dt)
                else:
                    ogrSut.append(str(ogr[3]))
                giris=input("Yaş Giriniz : ")
                if len(giris)>0:
                    ogrSut.append(int(giris))
                 
                
                sql=f"UPDATE ogrenciler SET AdSoyad='{adsa}', DogTar='{dt}', Yas={yas}, Aktif={ak} WHERE OgrNo='{giris}'"          
            