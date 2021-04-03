print('''
OYUNA HOŞ GELDİN DENİZ. 
1 İLE 100 ARASINDA BİR SAYI TUTABİLİR MİSİN?''')

a = 1
b = 100
sayac = 1

while (True):
    tahmin = int((a + b) // 2)
    print("\nBenim Tahminim {} . Doğru mu bildim?".format(tahmin))
    print(" 0 | Doğru Bildin\n 1 | {} den Daha Büyük Bir Sayı Tuttum\n 2 | Daha Küçük Bir Sayı Tuttum".format(tahmin))
    secim = int(input("\nCevabın: "))

    if secim == 0:
        print(50 * "\n")
        print("YUPPİ!\n{} adımda bildim! ".format(sayac))
        input("oyun bitti")
        break

    elif secim == 1:
        a = tahmin + 1
        sayac += 1
    elif secim == 2:
        b = tahmin - 1
        sayac += 1
    print(50 * "\n")
