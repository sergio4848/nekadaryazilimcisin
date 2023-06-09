def puanlama_sorusu(soru, puan):
    cevap = input(soru)
    return puan if cevap.lower() == "evet" else 0

def yazilimci_puanlama():
    puan = 0
    puan += puanlama_sorusu("Python programlama dilini biliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("HTML ve CSS ile web sayfaları tasarlayabiliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("JavaScript programlama dilini kullanabiliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Bir veritabanı yönetim sistemiyle (Örneğin: MySQL) çalışabiliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Bir programlama dilinde (Python, Java, C++, vb.) en az bir proje geliştirdiniz mi? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Bir versiyon kontrol sistemi (Git, SVN, vb.) kullanabiliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("API'leri (Application Programming Interface) kullanabiliyor musunuz? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Bir web framework (Django, Flask, vb.) kullanarak web uygulamaları geliştirdiniz mi? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Bir veri analizi veya makine öğrenmesi projesi gerçekleştirdiniz mi? (Evet/Hayır): ", 10)
    puan += puanlama_sorusu("Yazılım geliştirme sürecinde test otomasyonu yapabiliyor musunuz? (Evet/Hayır): ", 10)

    print("Toplam puanınız:", puan)

yazilimci_puanlama()
