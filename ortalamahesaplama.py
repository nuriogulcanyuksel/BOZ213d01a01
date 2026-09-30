while True:
    print("=== Not Ortalaması ve Durum Hesaplama Sistemi ===")

    vize = float(input("Vize notunuzu giriniz: "))
    final = float(input("Final notunuzu giriniz: "))

    ortalama = (vize * 0.40) + (final * 0.60)

    print(f"\nDönem Sonu Ortalamanız: {ortalama:.2f}")

    if final < 50:
        print("Sonuç: Kaldınız (Final barajı olan 50 geçilemedi - FF)")
    elif ortalama >= 85:
        print("Sonuç: AA ile Başarıyla Geçtiniz!")
    elif ortalama >= 70:
        print("Sonuç: BB ile Geçtiniz.")
    elif ortalama >=50:
        print("Sonuç: CC ile Geçtiniz.")
    else:
        print("Sonuç: Kaldınız (Ortalama 50'nin altında - FF)")

    devam = input("\nYeni bir not hesaplamak istiyor musunuz? (e/h): ")
    if devam.lower() != "e":
        print("Program sonlandırıldı.")
        break

