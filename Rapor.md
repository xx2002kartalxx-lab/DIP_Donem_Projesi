# DIP Dönem Projesi: Otopark Doluluk Tespiti – Final Raporu

**Öğrenci:** Muhammet Furkan Kart  
**Proje Deposu:** `DIP_Donem_Projesi`  
**Proje Konusu:** Proje 08 – Otopark Doluluk Tespiti

---

## 1. Problem Tanımı
Açık hava otoparklarında park yerlerinin dolu veya boş olduğunu sabit kamera görüntülerinden otomatik olarak tespit etmek, dış ortam koşulları nedeniyle klasik görüntü işleme açısından zorlu bir problemdir. Gün içinde değişen güneş açısı, binaların ve ağaçların zemine düşürdüğü keskin yatay gölgeler, asfalttaki ışık parlamaları ve koyu renkli araçların düşük kontrastla zemine karışması standart parlaklık eşikleme yöntemlerini yanıltmaktadır.

Bu projenin amacı; derin öğrenme veya makine öğrenmesi sınıflandırıcıları kullanmadan, yalnızca **klasik sayısal görüntü işleme (DIP)** teknikleriyle dış ortam ışık ve gölge değişimlerine dayanıklı, sabit kamera altında 6 park yerinin doluluk durumunu güvenilir biçimde belirleyen tekrarlanabilir bir sistem geliştirmektir.

---

## 2. Veri Seti ve Hazırlık
Veri seti, farklı gün saatlerine ait güneş ışığı, keskin bina gölgeleri ve düşük kontrast koşullarını ile 8 farklı doluluk düzenini kapsamaktadır. Zorlaştırıcı koşul olarak günün farklı saatlerindeki ışık değişimi ve güneşli ile bulutlu hava durumu kullanılmıştır.

* **Geliştirme Seti (`data/gelistirme/`):** 42 fotoğraf (%70) – Algoritma tasarımı, yöntem karşılaştırması ve optimum eşik değerinin belirlenmesi için kullanılmıştır.
* **Test Seti (`data/test/`):** 18 fotoğraf (%30) – Geliştirme aşamasında sabitlenen parametrelerle nihai performans değerlendirmesi için ayrılmıştır.
* **ROI ve Görsel Etiketleme:** Sabit kamera açısındaki 6 park yerinin piksel koordinatları `(x1, y1, x2, y2)` kaynak kod içinde tanımlanmıştır. Çıktı görüntülerinde **yeşil kutular boş**, **mavi kutular dolu** park yerlerini göstermektedir. (Detaylı veri açıklaması için bkz. `data/README.md`.)

---

## 3. Yöntem ve Parametre Seçim Gerekçeleri
Proje, ders kapsamına uygun olarak yalnızca klasik görüntü işleme ve geometrik bölge analizi adımlarından oluşan aşağıdaki ardışık düzen (pipeline) ile kurulmuştur:

1. **Gri Tonlama (Grayscale):** Renk bilgisinden kaynaklanan gereksiz işlem yükünü ve aydınlatma renk sapmalarını azaltmak için uygulanmıştır.
2. **CLAHE (`clipLimit=2.0`, `tileGridSize=(8, 8)`):** Gölge altında kalan siyah ve koyu renkli araçların kenar detaylarını, aydınlık bölgeleri patlatmadan yerel kontrast artırımıyla ortaya çıkarmak için seçilmiştir.
3. **Gaussian Blur (`5×5`):** Asfalt yüzeyindeki küçük pürüzleri ve yüksek frekanslı çevresel gürültüleri bastırmak amacıyla uygulanmıştır.
4. **Yönlü Kenar Tespiti – Sobel X (`ksize=3`) ve İkili Eşikleme (`threshold=50`):** Otoparka düşen keskin bina gölgelerinin oluşturduğu baskın yatay çizgileri azaltmayı hedefleyerek, yalnızca araç gövdelerinin dikey hatlarını (kapı, sütun, tampon kenarları) yakalamak amacıyla standart Canny yerine X ekseni yönlü Sobel filtresi tercih edilmiştir.
5. **Morfolojik Genişletme (`dilate`, `3×3` çekirdek, `iterations=1`):** Sobel X ile elde edilen ince ve kopuk dikey kenar hatlarını bütünleştirmek için uygulanmıştır.
6. **ROI Piksel Yoğunluğu Eşiklemesi (`%12`):** Her bir sabit park alanı (ROI) içerisindeki beyaz kenar piksellerinin toplam ROI alanına oranı hesaplanmıştır. Yoğunluk `%12` üzerinde ise **Dolu (Mavi)**, `%12` ve altında ise **Boş (Yeşil)** kararı verilmiştir.

---

## 4. Karşılaştırmalı Deney (Canny vs. Sobel X)
Yöntem seçimini sayısal olarak doğrulamak amacıyla, **42 geliştirme fotoğrafı** (toplam **252 park yeri gözlemi**) üzerinde aynı ön işleme (Gri Tonlama + CLAHE + Gaussian Blur) ve son işleme (`3×3` Dilate) adımları sabit tutularak **Canny (50, 150)** ve **Sobel X (ksize=3, eşik=50)** yöntemleri karşılaştırılmıştır.

| Yöntem | Ortalama Kenar Yoğunluğu (42 Görsel / 252 Gözlem) | Gözlem  |
| :--- | :---: | :--- |
| **Canny (50, 150)** | **%27,79** |Ortalama kenar yoğunluğu daha yüksektir. |
| **Sobel X (ksize=3)** | **%18,03** | 252 gözlemin 250'sinde (%99,2) Canny'den daha düşük kenar yoğunluğu üretmiştir. |

* Sobel X çıktılarında ortalama **9,76 puan** daha düşük kenar yoğunluğu elde edilmiştir.
* Geliştirme setindeki Sobel X dağılımı incelendiğinde **%11,33 ile %13,92** arasında hiçbir gözlem bulunmadığı, boş ve dolu kümelerinin doğal bir boşlukla net biçimde ayrıldığı görülmüştür. Bu bulgu, optimum eşik değeri olarak **%12** seçilmesini sayısal olarak desteklemiştir.
* Fotoğraf ve park yeri bazlı tüm karşılaştırma verileri `results/canny_sobel_gelistirme_karsilastirmasi.csv` dosyasında kayıtlıdır.

---

## 5. Sayısal Test Sonuçları
Geliştirme aşamasında belirlenen tüm parametreler (CLAHE, `5×5` Gaussian Blur, Sobel X ve `%12` eşik değeri) değiştirilmeden **18 fotoğraflık test setinde** çalıştırılmıştır. Her fotoğrafta 6 sabit park yeri bulunduğundan toplam **108 park yeri** tek tek doğrulanmıştır.

| Değerlendirme Ölçütü | Doğru | Yanlış | Toplam | Doğruluk Oranı |
| :--- | :---: | :---: | :---: | :---: |
| **Fotoğraf Bazlı (6/6 tam doğru kare)** | 17 | 1 | 18 | **%94,44** |
| **Park Yeri Bazlı (tekil ROI kararı)** | 106 | 2 | 108 | **%98,15** |
* **Orijinal Görüntü:** `results/orijinal_goruntu.png`
* **Ara İşlem Çıktıları:** `results/ara_islem_ciktilari.png`
* **Başarılı Tespit Örneği (Son Çıktı):** `results/basarili_ornek.png`
* **Hatalı Tespit Örneği:** `results/hata_analizi.png`

---

## 6. Hata Analizi ve Sınırlamalar
Sistemin yanıldığı tek test fotoğrafında (`results/hata_analizi.png`) 6 park yerinden 4'ü doğru, 2'si yanlış tespit edilmiştir. Hata, algoritmanın ışık veya gölgeye yenilmesinden değil, **statik koordinat (ROI)** yaklaşımının fiziksel sınırlarından kaynaklanmıştır:

* İlgili karede koyu renkli bir aracın park alanından manevra yaparak çıkarken yatay konumda kaldığı ve komşu boş park yerlerinin izleme bölgelerine (ROI) fiziksel olarak taştığı görülmüştür.
* Araç ilgili kutulara park etmiyor olmasına rağmen gövde hatları Sobel X filtresi tarafından yakalanmış, beyaz piksel yoğunluğu `%12` eşik değerini aştığı için 2 boş park yeri anlık olarak **Dolu (False Positive)** şeklinde işaretlenmiştir.
* **Kapsam Notu:** Ders görüşmesinde ileri hedef (çizgi ihlali/manevra ayrımı) zorunluluğu kaldırıldığı için manevra anındaki geçici taşmalar için ek takip/segmentasyon algoritması geliştirilmemiş; durum statik ROI yönteminin doğal bir sınırlaması olarak analiz edilmiştir. Ayrıca sistem, kamera açısının sabit kalmasını gerektirir.

---

## 7. Sonuç
Geliştirme aşamasında 42 fotoğraf üzerinde kurulan ve Canny'ye göre daha düşük kenar yoğunluğu veren **CLAHE + Gaussian Blur + Sobel X + Morfolojik Genişletme + %12 Eşikleme** işlem hattı, 18 fotoğraflık test setinde fotoğraf bazında **%94,44** (17/18), park yeri bazında ise **%98,15** (106/108) doğruluk sağlamıştır. Tüm adımlar klasik sayısal görüntü işleme sınırları içinde ve tekrarlanabilir biçimde tamamlanmıştır.

---

## 8. Ekip Üyesi Katkısı
Proje bireysel olarak yürütülmüştür.

* **Muhammet Furkan Kart:** Literatür taraması (`Literatur.md`), PKLot veri setinden geliştirme/test ayrımının oluşturulması (`data/`), 6 sabit ROI koordinatının belirlenmesi, klasik görüntü işleme işlem hattının kodlanması (`src/otopark_analizi_jupyter.ipynb`), Canny–Sobel X karşılaştırmalı deneyinin yürütülmesi (`results/`), test doğrulaması, hata analizi ve tüm dokümantasyonun (`README.md`, `Rapor.md`, `requirements.txt`, `YapayZeka.md`) hazırlanması.