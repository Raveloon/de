from Emlak import Emlak
# Ana program kısmı
while_tercih = True

# Başlangıç verileri (örnek olarak eklenmiş)
arr = [
    Emlak("Sarı Ev", "Ev", 800000, "11/28-117.Sokak"),
    Emlak("Yeşil Bina", "Ofis", 4200000, "11/28-117.Sokak"),
    Emlak("Büyük Arsa", "Arsa", 21000000, "11/28-117.Sokak"),
]

# Ana döngü
while while_tercih:
    ilk_secim = input(
        "\n\nAna ekrana Hoşgeldiniz...\n\nYeni Kayıt için: 1\nMevcut Kayıtları Görmek için: 2\nÇıkış yapmak için: 3\n\nSeçiminiz: "
    )

    if ilk_secim == "1":
        # Yeni bir emlak nesnesi oluştur ve listeye ekle
        yeni_emlak = Emlak("", "", 0, "").all_for_one()
        arr.append(yeni_emlak)
        print("\nYeni kayıt başarıyla eklendi!\n")

    elif ilk_secim == "2":
        # Mevcut kayıtları listele
        if arr:
            print("\nMevcut Kayıtlar:")
            kayit_no = 1  # Kayıt numarası için sayaç
            for emlak_nesnesi in arr:
                print(f"{kayit_no}. Kayıt:")
                emlak_nesnesi.liste_()
                kayit_no += 1
                print()
        else:
            print("\nHenüz kayıt bulunmuyor.")

    elif ilk_secim == "3":
        print("Programdan çıkılıyor...")
        while_tercih = False

    else:
        print("Hatalı tercih, lütfen 1, 2 veya 3 girin.")

        
        
        
        
        
        
        