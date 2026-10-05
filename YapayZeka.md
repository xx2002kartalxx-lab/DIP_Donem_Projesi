Oturum 1 — 05.10.2026
Oturum bilgileri
Katılan öğrenci veya öğrenciler: Muhammet Furkan Kart

Kullanılan araç ve biliniyorsa model: Google Gemini

Çalışmanın amacı: Proje 08 (Masaüstü Otopark Doluluk Tespiti) için uygun veri setinin seçilmesi, 60 fotoğraflık veri havuzunun proje dizinine entegre edilerek GitHub'a gönderilmesi ve OpenCV ile park yerlerinin koordinatlarının bulunması için temel çerçevenin kurulması.

İlgili uygulama commit’i veya pull request: [öğrenci sonradan ekleyecek]
İş,Katkı türü,İlgili dosya veya fonksiyon,Uygulama durumu
Veri seti ve koşul belirleme stratejisi,yöntem önerisi,data/ klasörü,dosyaya uygulandı
GitHub Desktop kullanım yönlendirmesi,kavram açıklama,"main branch, commit/push adımları",dosyaya uygulandı
Manuel fare tıklaması ile koordinat tespiti,kod üretimi,src/koordinat_bulucu.py,kodu verildi (çalıştırma doğrulanmadı)
Oturum kayıt dosyasının (YapayZeka.md) hazırlanması,dokümantasyon,YapayZeka.md,dosyaya uygulandı
Yöntem ve ders kapsamına uygunluk
Kullanılan veya önerilen görüntü işleme yöntemleri ve kısa gerekçeleri: Proje kapsamında tüm otoparkı otomatik taramak yerine "pilot park yerleri" belirlemek için cv2.setMouseCallback ile fare tıklama yöntemi önerilmiştir. Tespit algoritması için yalnızca piksel yoğunluk eşikleme (Thresholding) ve kenar belirleme (Canny Edge Detection) yöntemlerinin klasik OpenCV fonksiyonlarıyla kullanılması planlanmıştır.

Dersin sınırlarıyla çelişen öneri varsa ne olduğu ve düzeltilip düzeltilmediği: Derin öğrenme, makine öğrenmesi veya hazır sınıflandırıcılar içeren hiçbir yöntem önerilmemiş olup, tüm yaklaşım dersin sınırları olan klasik görüntü işleme teknikleriyle uyumlu tutulmuştur.

Kaynak veya arama konusu,Yapay zekânın yaptığı işlem,Erişim ve doğrulama durumu,Literatur.md dosyasına katkı
PKLot Dataset (PUCPR Otopark Verisi) - Kaggle,"Veri seti arama, kamera açısı analizi (PUCPR vs. UFPR) ve 3 ışık/hava koşulunun (Sunny, Cloudy, Rainy) tasnifi.",yalnızca önerildi,Bu oturumda literatür taramasına katkı sağlanmadı.
Doğrulama ve açık sorunlar
Gerçekten çalıştırılan test veya deneyler ve gözlenen sonuçlar: Toplam 60 adet fotoğraf (11, 12, 13, 14 Eylül tarihlerinden) data/ klasörüne kopyalanmış ve GitHub üzerinden "Yapay zeka kayıt belgesi eklendi" mesajıyla başarılı bir şekilde repository'e push edilmiştir (öğrencinin bildiriminden doğrulanmıştır).

Çalıştırılmayan kontroller, bilinen hatalar ve belirsizlikler: src/koordinat_bulucu.py içerisindeki OpenCV pencere açma ve koordinat okuma kodunun, öğrencinin yerel Anaconda/Spyder ortamında sorunsuz çalışıp çalışmadığı henüz test edilmemiş ve doğrulanmamıştır.

Önerilip kullanılmayan veya hatalı olduğu anlaşılan öneriler: Yönergedeki "ileri hedef" zorunluluğu, hoca ile yapılan görüşme sonucunda iptal edildiği için daha karmaşık segmentasyon ve nesne ayırma işlemleri stratejiden çıkarılmıştır.

Varsa doğrulanmayı bekleyen kaynak bilgileri ve literatür yorumları: Kaggle PKLot veri setine ait PDF veya makale referanslarının doğrulanması beklenmektedir.
Yapay zekâ çıktısında neyi değiştirdik veya reddettik, neden?
Yapay zeka başlangıçta PCB hata tespiti projesini (Proje 04) önerdi ancak ben Otopark Doluluk Tespiti (Proje 08) üzerinden ilerlemeyi seçtim. Ayrıca 15 fotoğraf kullanmayı düşündüğümde AI bunu onayladı ancak hocanın 60 fotoğraf kuralını hatırlatarak veri setini 60'a çıkarmasını sağladım.
Commit: "Yapay zeka kayıt belgesi eklendi" (61 dosya)
Hangi kodu ve sonucu kendimiz kontrol ettik?Kaggle PKLot veri setinden PUCPR kamerasının Sunny, Cloudy ve Rainy klasörlerindeki fotoğrafları bizzat inceledim. Toplam 60 fotoğrafın data klasörüne aktarılmasını ve GitHub'a başarıyla yüklenmesini kontrol ettim. Kod çalıştırma henüz yapılmadı.
Önerilen kaynaklardan hangilerini kendimiz okuyup doğruladık?Kaggle'daki PKLot veri setinin açıklamasını ve klasör yapısını inceleyip projeye uygunluğunu doğruladım.
Yapay zekânın kaynak bilgisi veya yorumunda hangi düzeltmeleri yaptık?Yapay zeka bir klasörde sadece 15 fotoğraf olduğunu varsaydı, ancak Kaggle web arayüzünün sadece 15 önizleme gösterdiğini, klasörün içinde aslında 34 fotoğraf olduğunu fark edip bu durumu ben düzelttim.
Bu oturumda ne öğrendik?Sabit koordinatlı görüntü işleme projelerinde (yapay zeka modeli kullanılmadığında) kamera açısının değişmemesinin ne kadar kritik olduğunu ve GitHub Desktop üzerinden branch (dal) kullanmadan doğrudan ana depoya (main) veri yüklemeyi öğrendim.
Kaydı kontrol eden öğrenciler:Muhammet Furkan Kart 221451016