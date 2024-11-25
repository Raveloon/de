class Emlak:
    def __init__(self, tanim, tip, fiyat, adres):
        self.tanim = tanim
        self.tip = tip
        self.fiyat = fiyat
        self.adres = adres

    def tanim_(self):
        self.tanim = input("Emlaginizi nasıl tanımlamak istersiniz: ")

    def tip_(self):
        while True:
            tip_input = input("Emlaginizin türü nedir (Ofis, Ev, Arsa, Bina): ").lower()
            if tip_input in ["ofis", "ev", "arsa", "bina"]:
                self.tip = tip_input.capitalize()
                break
            else:
                print("Lütfen geçerli bir tür giriniz: Ofis, Ev, Arsa, Bina.")

    def fiyat_(self):
        while True:
            try:
                self.fiyat = float(input(f"{self.tip}'nızı satmayı/kiralamayı düşündüğünüz miktar nedir (TL): "))
                break
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

    def adres_(self):
        self.adres = input(f"{self.tip}'nızın tam konumu nedir: ")

    def liste_(self):
        print("\nGirilen Değerler:")
        print(f"  Emlak Tanımı: {self.tanim}")
        print(f"  Türü:         {self.tip}")
        print(f"  Fiyatı:       {self.fiyat} TL")
        print(f"  Adresi:       {self.adres}")

    def all_for_one(self):
        self.tanim_()
        self.tip_()
        self.fiyat_()
        self.adres_()
        self.liste_()
        return self  # Kendisi döndürülerek nesne olarak saklanması sağlanır
    













    