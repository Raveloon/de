print("Emlak Kayıt Programı Başarı ile çalıştırıldı... \n ")

list_idler = {"199":"199","200":"200","201":"201"}
list_adresler= {"199":"Ankara","200":"İstanbul","201":"İzmir"}
list_fiyatlar= {"199":"1M", "200":"1.1M", "201":"2.5M"}
list_alan= {"199":"120 Metrekare", "200":"250 Metrekare", "201": "175 Metrekare"}
list_tip={"199":"Ev", "200":"Arsa", "201": "Ofis"}  
id_yaratici = -1

alpha= ""
    
while True  :
    print("Yapilacak tercihi seciniz")
    wanted = int(input("Yeni Kayit İcin 1,  \nMevcut Kayitlari Görmek İcin 2 Yaziniz \n "))   
    

    if wanted == 1 :
        id_yaratici += 1 
        id_value = id_yaratici
        list_idler.update({f"{id_yaratici}":f"{id_value}"}) 
        print("Oncelikle girilecek emlagın özelliklerini girmelisiniz : ")
        emlak_tipi1=input("Emlak cesidiniz nedir ? (ev,arsa,ofis,isyeri) ").lower()
        emlak_tipi = emlak_tipi1.capitalize()
        
                
        if True :
            if emlak_tipi == "Ev" :
               
               list_tip.update({f"{id_yaratici}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratici}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satilması veya kiralanmasini istediğiniz miktari giriniz :")
               list_fiyatlar.update({f"{id_yaratici}":f"{fiyat}"})
               
               alan=input(f"Sahip oldugunuz {emlak_tipi}'in kac metrekare oldugunu giriniz :")
               list_alan.update({f"{id_yaratici}":f"{alan}"})
               
               print("Emlaginiz su sekilde tanimlaniyor dogrulugunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratici}"))
               print(list_adresler.get(f"{id_yaratici}"))
               print(list_fiyatlar.get(f"{id_yaratici}"))          
               print(list_alan.get(f"{id_yaratici}"))
               
               
               eminlik_degeri = input(" Kayitinizdan eminseniz (k) yaziniz \n Eğer Kayidinizi hatali yaptiysaniz  (y)  yaziniz\n Eğer sistemi kapatmak istiyorsaniz (q) yazınız").capitalize()
               
               if eminlik_degeri == "K" :
                   
                   
               
                   pass
               elif eminlik_degeri == "Y":
                   list_adresler.popitem()
                   list_alan.popitem()
                   list_fiyatlar.popitem()
                   list_idler.popitem()
                   list_tip.popitem()
                   print("En son yaptiğiniz Kayıt silindi...\n\n\n")
                   
                   pass
               else : 
                   break
               
            elif emlak_tipi == "Arsa" :
               list_tip.update({f"{id_yaratici}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}nizin adresini giriniz :")
               list_adresler.update({f"{id_yaratici}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satilmasi veya kiralanmasini istediğiniz miktari giriniz")
               list_fiyatlar.update({f"{id_yaratici}":f"{fiyat}"})
               
               alan=input(f"Sahip oldugunuz {emlak_tipi}'in kaç metrekare oldugunu giriniz :")
               list_alan.update({f"{id_yaratici}":f"{alan}"})
               
               print("Emlagınız su sekilde tanimlaniyor dogrulugunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratici}"))
               print(list_adresler.get(f"{id_yaratici}"))
               print(list_fiyatlar.get(f"{id_yaratici}"))          
               print(list_alan.get(f"{id_yaratici}"))
               
               
               eminlik_degeri = input(" Kayitinizdan eminseniz (k) yaziniz \n Eğer Kayidinizi hatali yaptiysaniz  (y)  yaziniz\n Eğer sistemi kapatmak istiyorsaniz (q) yazınız").capitalize()
               
               if eminlik_degeri == "K" :
                   
                   
               
                   pass
               elif eminlik_degeri == "Y":
                   list_adresler.popitem()
                   list_alan.popitem()
                   list_fiyatlar.popitem()
                   list_idler.popitem()
                   list_tip.popitem()
                   print("En son yaptiğiniz Kayıt silindi...\n\n\n")
                   
                   pass
               else : 
                   break
                              
               
               
            elif emlak_tipi == "Ofis" :
               list_tip.update({f"{id_yaratici}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}nizin adresini giriniz :")
               list_adresler.update({f"{id_yaratici}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satilmasi veya kiralanmasini istediğiniz miktari giriniz")
               list_fiyatlar.update({f"{id_yaratici}":f"{fiyat}"})
               
               alan=input(f"Sahip oldugunuz {emlak_tipi}'in kaç metrekare oldugunu giriniz :")
               list_alan.update({f"{id_yaratici}":f"{alan}"})
               
               print("Emlagınız su sekilde tanimlaniyor dogrulugunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratici}"))
               print(list_adresler.get(f"{id_yaratici}"))
               print(list_fiyatlar.get(f"{id_yaratici}"))          
               print(list_alan.get(f"{id_yaratici}"))
               
               
               eminlik_degeri = input(" Kayitinizdan eminseniz (k) yaziniz \n Eğer Kayidinizi hatali yaptiysaniz  (y)  yaziniz\n Eğer sistemi kapatmak istiyorsaniz (q) yazınız").capitalize()
               
               if eminlik_degeri == "K" :
                   
                   
               
                   pass
               elif eminlik_degeri == "Y":
                   list_adresler.popitem()
                   list_alan.popitem()
                   list_fiyatlar.popitem()
                   list_idler.popitem()
                   list_tip.popitem()
                   print("En son yaptiğiniz Kayıt silindi...\n\n\n")
                   
                   pass
               else : 
                   break
               
               
               
               
            elif emlak_tipi == "İşyeri" :
               list_tip.update({f"{id_yaratici}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratici}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satilması veya kiralanmasini istediğiniz miktari giriniz :")
               list_fiyatlar.update({f"{id_yaratici}":f"{fiyat}"})
               
               alan=input(f"Sahip oldugunuz {emlak_tipi}'in kac metrekare oldugunu giriniz :")
               list_alan.update({f"{id_yaratici}":f"{alan}"})
               
               print("Emlagınız su sekilde tanimlaniyor dogrulugunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratici}"))
               print(list_adresler.get(f"{id_yaratici}"))
               print(list_fiyatlar.get(f"{id_yaratici}"))          
               print(list_alan.get(f"{id_yaratici}"))
               
               
               eminlik_degeri = input(" Kayitinizdan eminseniz (k) yaziniz \n Eğer Kayidinizi hatali yaptiysaniz  (y)  yaziniz\n Eğer sistemi kapatmak istiyorsaniz (q) yazınız").capitalize()
               
               if eminlik_degeri == "K" :
                   
                   
               
                   pass
               elif eminlik_degeri == "Y":
                   list_adresler.popitem()
                   list_alan.popitem()
                   list_fiyatlar.popitem()
                   list_idler.popitem()
                   list_tip.popitem()
                   print("En son yaptiğiniz Kayıt silindi...\n\n\n")
                   
                   pass
               else : 
                   break
               
                            
              
            else :
                emlak_tipi = input("Yanlış girdi girdiniz emlak tipiniz nedir? (arsa,ev,ofis,işyeri)").capitalize()
            
                        
        
           
     
    elif wanted == 2 :
        
        görüntüleme_degiskeni = 0
        
        for idler in list_idler:
            görüntüleme_degiskeni +=1
            gecici_kayıt=list_adresler.keys()
            print(f"{görüntüleme_degiskeni}'nci kayıt : \n")
            print(list_tip.get(f"{idler}"))
            print(list_adresler.get(f"{idler}"))
            print(list_fiyatlar.get(f"{idler}"))          
            print(list_alan.get(f"{idler}"))
            print("\n")
        
        emin_misin = input("Ana menüye geri dönmek içi 1'i \nSistemi kapatmak için 2'yi tuşlayınız")        
        if emin_misin == "1":
            pass
        elif emin_misin == "2":
            break
                     
        
    else :
        print("İstediğiniz girdi sistemimizde bulunmamaktadır...")
        
        
   
