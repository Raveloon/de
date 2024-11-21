print("Emlak Kayıt Programı Başarı ile çalıştırıldı... \n ")

list_idler = {}
list_adresler= {}
list_fiyatlar= {}
list_alan= {}
list_tip={}  
id_yaratıcı = -1
    
while True  :
    print("Yapılacak tercihi seçiniz")
    wanted = int(input("Yeni Kayıt İçin 1,  \nMevcut Kayıtları Görmek İçin 2 Yazınız \n "))   
    

    if wanted == 1 :
        id_yaratıcı += 1 
        id_value = id_yaratıcı
        list_idler.update({f"{id_yaratıcı}":f"{id_value}"}) 
        print("Öncelikle girilecek emlağın özelliklerini girmelisiniz : ")
        emlak_tipi=input("Emlak çeşidiniz nedir ? (ev,arsa,ofis,işyeri) ").capitalize()
                
        if True :
            if emlak_tipi == "Ev" :
               
               list_tip.update({f"{id_yaratıcı}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratıcı}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satılması veya kiralanmasını istediğiniz miktarı giriniz :")
               list_fiyatlar.update({f"{id_yaratıcı}":f"{fiyat}"})
               
               alan=input(f"Sahip olduğunuz {emlak_tipi}'in kaç metrekare olduğunu giriniz :")
               list_alan.update({f"{id_yaratıcı}":f"{alan}"})
               
               print("Emlağınız şu şekilde tanımlanıyor doğruluğunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratıcı}"))
               print(list_adresler.get(f"{id_yaratıcı}"))
               print(list_fiyatlar.get(f"{id_yaratıcı}"))          
               print(list_alan.get(f"{id_yaratıcı}"))
               
               
               eminlik_değeri = input("Eğer yanlış ise 'q' değilse herhangi bir girdi giriniz : ").capitalize()
               
               if eminlik_değeri == "Q" :
               
                   pass
               else : 
                   break
               
            elif emlak_tipi == "Arsa" :
               list_tip.update({f"{id_yaratıcı}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratıcı}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satılması veya kiralanmasını istediğiniz miktarı giriniz")
               list_fiyatlar.update({f"{id_yaratıcı}":f"{fiyat}"})
               
               alan=input(f"Sahip olduğunuz {emlak_tipi}'in kaç metrekare olduğunu giriniz :")
               list_alan.update({f"{id_yaratıcı}":f"{alan}"})
               
               print("Emlağınız şu şekilde tanımlanıyor doğruluğunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratıcı}"))
               print(list_adresler.get(f"{id_yaratıcı}"))
               print(list_fiyatlar.get(f"{id_yaratıcı}"))          
               print(list_alan.get(f"{id_yaratıcı}"))
               
               
               eminlik_değeri = input("Eğer yanlış ise 'q' değilse herhangi bir girdi giriniz : ").capitalize()
               
               if eminlik_değeri == "Q" :
               
                   pass
               else : 
                   break
                              
               
               
            elif emlak_tipi == "Ofis" :
               list_tip.update({f"{id_yaratıcı}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratıcı}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satılması veya kiralanmasını istediğiniz miktarı giriniz")
               list_fiyatlar.update({f"{id_yaratıcı}":f"{fiyat}"})
               
               alan=input(f"Sahip olduğunuz {emlak_tipi}'in kaç metrekare olduğunu giriniz :")
               list_alan.update({f"{id_yaratıcı}":f"{alan}"})
               
               print("Emlağınız şu şekilde tanımlanıyor doğruluğunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratıcı}"))
               print(list_adresler.get(f"{id_yaratıcı}"))
               print(list_fiyatlar.get(f"{id_yaratıcı}"))          
               print(list_alan.get(f"{id_yaratıcı}"))
               
               
               eminlik_değeri = input("Eğer yanlış ise 'q' değilse herhangi bir girdi giriniz : ").capitalize()
               
               if eminlik_değeri == "Q" :
               
                   pass
               else : 
                   break
               
               
               
               
            elif emlak_tipi == "İşyeri" :
               list_tip.update({f"{id_yaratıcı}":f"{emlak_tipi}"})
               
               adres=input(f"{emlak_tipi}inizin adresini giriniz :")
               list_adresler.update({f"{id_yaratıcı}":f"{adres}"})
               
               fiyat=input(f"{emlak_tipi}'nizin satılması veya kiralanmasını istediğiniz miktarı giriniz")
               list_fiyatlar.update({f"{id_yaratıcı}":f"{fiyat}"})
               
               alan=input(f"Sahip olduğunuz {emlak_tipi}'in kaç metrekare olduğunu giriniz :")
               list_alan.update({f"{id_yaratıcı}":f"{alan}"})
               
               print("Emlağınız şu şekilde tanımlanıyor doğruluğunu kontrol ediniz : " )
               
               print(list_tip.get(f"{id_yaratıcı}"))
               print(list_adresler.get(f"{id_yaratıcı}"))
               print(list_fiyatlar.get(f"{id_yaratıcı}"))          
               print(list_alan.get(f"{id_yaratıcı}"))
               
               
               eminlik_değeri = input("Eğer yanlış ise 'q' değilse herhangi bir girdi giriniz : ").capitalize()
               
               if eminlik_değeri == "Q" :
               
                   pass
               else : 
                   break
               
                            
              
            else :
                emlak_tipi = input("Yanlış girdi girdiniz emlak tipiniz nedir? (arsa,ev,ofis,işyeri)").capitalize()
            
                        
        
           
        
    elif wanted == 2 :
        class Emlak :
             def __init__(self,emlak_id,adres,fiyat,alan,emlak_tipi):
                 self.emlak_id=emlak_id
                 self.adres=adres
                 self.fiyat=fiyat
                 self.alan=alan
                 self.emlak_tipi=emlak_tipi
                
                 
             def emlak_id(self):
                 print("İstenen Emlağın İd numarası: ")
    elif wanted == 0 :
        pass
    else :
        print("İstediğiniz girdi sistemimizde bulunmamaktadır...")
   
