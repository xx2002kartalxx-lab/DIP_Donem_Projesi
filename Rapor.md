# DIP Dönem Projesi: Otopark Doluluk Tespiti - Final Raporu

**Öğrenci:** Muhammet Furkan Kart
**Proje Deposu:** DIP_Donem_Projesi

## 1. Yöntem ve Parametre Seçimleri (Deney Aşaması)
Proje geliştirme sürecinde (42 fotoğraflık veri seti) karşılaşılan en büyük zorluk, binaların otopark üzerine düşürdüğü keskin ve yatay gölgeler ile asfalttaki ışık parlamaları olmuştur. Bu zorlayıcı koşulları aşmak için aşağıdaki görüntü işleme boru hattı (pipeline) kurulmuştur:

1. **Grayscale Dönüşümü:** İşlem yükünü hafifletmek için.
2. **CLAHE (Contrast Limited Adaptive Histogram Equalization):** Gölge altında kalan siyah/koyu renkli araçların detaylarını, aydınlık bölgeleri patlatmadan bölgesel olarak ortaya çıkarmak için kullanıldı.
3. **Gaussian Blur (5x5):** Asfalt pürüzlerini ve çevresel gürültüleri yumuşatmak için uygulandı.
4. **Sobel X Filtresi:** Yatay bina gölgelerini eleyip, sadece araçların dikey hatlarını (kapı/sütun) yakalamak için Canny yerine Yönlü Sobel X (ksize=3) tercih edildi.
5. **Morfolojik Genişletme (Dilate):** Sobel ile elde edilen ince hatları birleştirmek için kullanıldı.
6. **ROI Eşikleme (Threshold):** 6 sabit park yeri için beyaz piksel/toplam piksel oranı hesaplandı. 42 fotoğraflık geliştirme setinde optimum doluluk sınırı **%12** olarak belirlendi.

## 2. Test Sonuçları ve Başarı Oranı (Final Aşaması)
Geliştirme aşamasında belirlenen parametreler (Sobel X ve %12 eşik değeri) değiştirilmeden, sistem daha önce görmediği farklı araç ve park düzenlerini içeren **18 fotoğraflık test setinde** çalıştırılmıştır.

* **Test Edilen Görüntü Sayısı:** 18
* **Tam Doğru Tahmin (6 park yerinin tamamı hatasız):** 17
* **Kısmi Hata Görülen Görüntü:** 1
* **Fotoğraf Bazında Başarı Oranı:** %94,44

Test setindeki toplam 108 park yeri (18 fotoğraf × 6 park yeri) tek tek doğrulanmıştır:
* **Doğru tespit edilen park yeri:** 106
* **Yanlış tespit edilen park yeri:** 2
* **Park Yeri Bazında Doğruluk:** %98,15

## 3. Hata Analizi
Sistemin yanıldığı tek test fotoğrafında 6 park yerinden 4'ü doğru, 2'si yanlış tespit edilmiştir. Hata, statik ROI yönteminin fiziksel limitlerinden (dinamik manevra engeli) kaynaklanmıştır. Hatalı tespit edilen görsel incelendiğinde; koyu renkli bir aracın park yerinden manevra yaparak çıkarken yatay bir pozisyonda kaldığı ve yandaki park yerlerinin ROI (İzleme Bölgesi) sınırlarını fiziksel olarak ihlal ettiği görülmüştür. Araç aslında o kutuya park etmiyor olmasına rağmen, gövde hatları Sobel X filtresi tarafından yakalanmış ve bölgedeki piksel yoğunluğu %12'lik eşik değerini aştığı için ilgili park yeri sistem tarafından anlık olarak "Dolu" (False Positive) olarak algılanmıştır. Bu durum, statik koordinat tabanlı sistemlerin, çizgiyi aşan veya manevra halindeki araçlara karşı doğal bir zafiyeti olduğunu göstermektedir.

## 4. Sonuç
Geliştirme aşamasında 42 fotoğraf kullanılmış, nihai değerlendirme 18 test fotoğrafı üzerinde yapılmıştır. Proje sonucunda fotoğraf bazında %94,44, park yeri bazında ise %98,15 doğruluk elde edilmiştir.