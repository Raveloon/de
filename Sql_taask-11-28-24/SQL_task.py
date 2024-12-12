import psycopg2

class Emlakcılık:
    def __init__(self,conn,tip,tanim,tamadres,fiyat):
        self.conn = conn
        self.tip = tip
        self.tanim = tanim
        self.tamadres = tamadres
        self.fiyat = fiyat
        
        
    def Tip_sorgu (self):
        while True:
            tip = input("Emlağınızın türü nedir? (Ev, Araba, Ofis, Malikane, Dükkan .vb").lower()
            if tip in ["ev","araba","ofis","malikane","dükkan"]:
                self.tip = tip.capitalize()
                break
            else :
                Tip_eminlik=input(f"{tip} Adında yeni bir tip türü kaydetmek istediğinizden emin misiniz ... (Evet/Hayır").capitalize()
                if Tip_eminlik == "Evet":
                    self.tip = tip
                    break
                else :
                    print("Tercihinizi tekrar yapınız \n⧴")
                    
                    
    def Tanim_sorgu (self):
        self.tanim = input("emlağınızı nasıl Tanımlarsınız ⧴")
        
        
    def Tam_adres_sorgu (self):
        tam_adres_onay = input("Tam adresini eklemek istiyorsanız (Y)").capitalize()
        if tam_adres_onay == "Y":
            self.tamadres = input(f"{self.tip}'nizin Tam adresini giriniz ⧴ ")
        else :
            print("Herhangi bir adres girilmedi...")
            self.tamadres = "None"
    
    
    def Max_Min_fiyat (self):
        max_min_ = input("Max/Min fiyat değeri girmek istiyorsanız (Y)").capitalize()
        if max_min_ == "Y":
            self.maxmin = input("Max/Min fiyat değeri giriniz ⧴")
        else :
            print("Herhangi bir fiyat girilmedi...")
            self.maxmin = "None"
    
    def Aciklama_sorgu (self):
        
        aciklama_onay = input("açıklama satırı da eklemek istiyorsanız (Y)").capitalize()
        if aciklama_onay == "Y":
            self.açıklama = input(f"{self.tip}'niz için Bir açıklama giriniz ⧴") 
        else :
            print("Herhangi bir açıklama girilmedi...")
            self.açıklama = "None"
            
            
    def ana_ekran_sorgu (self):
        self.Tanim_sorgu()
        self.Tip_sorgu()
        self.Tam_adres_sorgu()
        self.Max_Min_fiyat()
        self.Aciklama_sorgu()
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO emlak (id, tanim, tip, tamadres, maxmin, açıklama)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (id_value, self.tanim, self.tip,  self.tamadres, self.maxmin, self.açıklama))
            self.conn.commit()
        
        
    def get_all_homes(self):
        print("\n--- Kayıtlı Evler ---")
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM emlak order by id")
            homes = cursor.fetchall()
            if not homes:
                print("Kayıtlı ev bulunmamaktadır.\n")
            else:
                for home in homes:
                    print(f"""
------------------------------
ID: {home[0]}
Tanim: {home[1]}
Tip: {home[2]} TL
Tam Adres: {home[3]}
Max/Min fiyat: {home[4]}
Açıklama: {home[5]}
------------------------------
                    """)
        print()
    
    def ev_veri_giris (self):
        pass
 
conn = psycopg2.connect(
     dbname="postgres",
     user="postgres",
     password="x",
     host="localhost",
     port="5432"
 )
   
 
id_value = 5

while True :
    ana_ekran_tercihi = input("""Lütfen Tercih Yapınız:
⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁⦁
1 ⧴ Yeni Kayıt Girişi 
2 ⧴ Mevcut Kayıtları Göster
3 ⧴ Mevcut Kayıtlarda Değişiklikler
4 ⧴ Mevcut Kayıt silme 
5 ⧴ Çıkış Yap
                                                                
                                  """)
    if   ana_ekran_tercihi == "1" :
        id_value +=1
        yeni_emlak = Emlakcılık(conn,"","","","").ana_ekran_sorgu()
        
        
    elif ana_ekran_tercihi == "2":
        yeni_emlak = Emlakcılık(conn,"","","","").get_all_homes()
        
    elif ana_ekran_tercihi == "3":
        pass
    elif ana_ekran_tercihi == "4":
        pass
    elif ana_ekran_tercihi == "5":
        pass 
    else:
        print("Girilen girdi Tercihler arasında bulunmuyor...")                   
        
        
        
        
        
        
        