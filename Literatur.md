# Otopark Doluluk Tespiti Literatür Taraması

Bu projede, otopark doluluk tespiti problemini klasik görüntü işleme teknikleriyle çözen 5 farklı literatür kaynağı incelenmiştir.

### 1. PKLot – A Robust Dataset for Parking Lot Classification
*   **Yazarlar ve Yıl:** Almeida, P. R. L., vd. (2015)
*   **Bağlantı/DOI:** 10.1016/j.eswa.2015.02.009
*   **Problem ve Yöntem:** Literatürdeki otopark veri seti eksikliğini çözmek amacıyla yazılmıştır. Yöntem olarak SVM makine öğrenmesi algoritması ve LBP (Local Binary Patterns) kullanılmıştır.
*   **Veri, Sonuç ve Sınırlılık:** PUCPR ve UFPR otoparklarından alınan 12.000+ görüntü ile %99 başarı raporlanmıştır. Makine öğrenmesi modeli gerektirmesi klasik yöntemler için bir sınırlılıktır.
*   **Projemizde Kullanımı:** Projemizdeki görüntü işleme kısıtlamaları nedeniyle makine öğrenmesi kısımları kullanılmayacaktır. Ancak projemizin temelini oluşturan 60 fotoğraflık PUCPR güneşli, yağmurlu ve bulutlu veri seti doğrudan bu makalenin çıktılarından elde edilmiştir.

### 2. Intelligent Parking Space Detection System Based on Image Processing
*   **Yazarlar ve Yıl:** Yusnita, R., Norbaya, F., & Basharuddin, N. (2012)
*   **Bağlantı/DOI:** 10.7763/IJIMT.2012.V3.242
*   **Problem ve Yöntem:** Boş park yerlerinin kamera ile tespiti. Gri seviyeye dönüştürme, Görüntü Eşikleme (Thresholding), Canny kenar belirleme (Edge Detection) ve morfolojik işlemler kullanılmıştır.
*   **Veri, Sonuç ve Sınırlılık:** Başarı oranı yüksektir ancak otopark zeminindeki boyaların eskimesine ve aşınmasına karşı hassasiyet gösterdiği (sınırlılık) belirtilmiştir.
*   **Projemizde Kullanımı:** Araçların dış hatlarını bulmak için kullandıkları Canny Kenar Belirleme (Edge Detection) fonksiyonunun uygulanış mantığı projemize referans olacaktır.

### 3. Vacant Parking Space Detector for Outdoors by Using Background Subtraction and Edge Detection
*   **Yazarlar ve Yıl:** Ichihashi, H., vd. (2009)
*   **Bağlantı/DOI:** 10.1109/ICMLC.2009.5212569
*   **Problem ve Yöntem:** Dış mekan otoparklarında ışık değişimlerine rağmen araç tespiti. Arka plan çıkarma (Background Subtraction) ve kenar özellikleri kullanılmıştır.
*   **Veri, Sonuç ve Sınırlılık:** Gündüz ve akşamüstü testlerinde araçların yola düşen yoğun gölgeleri nedeniyle algoritmanın bazı boş yerleri dolu zannettiği (yanlış pozitif) raporlanmıştır.
*   **Projemizde Kullanımı:** Güneşli hava klasörümüzdeki (Sunny) fotoğraflarda oluşacak keskin gölgelerin kodumuzu nasıl bozabileceğini öngörmemizi sağlamıştır. Bu yüzden kodumuza Bulanıklaştırma (Gaussian Blur) filtresi eklenecektir.

### 4. Automobile Parking Space Detection Using Open Cv
*   **Yazarlar ve Yıl:** Kumar, A., vd. (2025)
*   **Bağlantı/DOI:** https://www.ijfmr.com/papers/2025/1/34598.pdf (IJFMR)
*   **Problem ve Yöntem:** OpenCV kullanılarak araç park yeri doluluk sayacı yapımı. Görüntüyü griye çevirme, Gaussian Blur, Uyarlanabilir Eşikleme (Adaptive Thresholding) ve beyaz piksel sayma (CountNonZero) yöntemleri kullanılmıştır.
*   **Veri, Sonuç ve Sınırlılık:** Gerçek zamanlı olarak oldukça hızlı ve başarılı çalışır. Temel sınırlılığı kameranın sabit kalma zorunluluğudur (açı değişmemelidir).
*   **Projemizde Kullanımı:** Projemizdeki temel OpenCV işlem sırası (Gri -> Bulanıklaştır -> Eşikleme -> Piksel Say) doğrudan bu makaledeki işlem hattı (pipeline) baz alınarak kurgulanacaktır.

### 5. Vacant Parking Space Detection in Static Images
*   **Yazarlar ve Yıl:** True, N. (2007)
*   **Bağlantı/DOI:** UCSD Technical Report (https://cseweb.ucsd.edu/classes/wi07/cse252a/projects/NT_Parking.pdf)
*   **Problem ve Yöntem:** Sabit kuşbakışı (overhead) fotoğraflarda park yeri bulma. Kenar noktası tespiti ve renk histogramı.
*   **Veri, Sonuç ve Sınırlılık:** Sabit fotoğraflarda başarılıdır ancak hava kapandığında veya yağmur yağdığında renk histogramlarının bozulduğu görülmüştür.
*   **Projemizde Kullanımı:** Hava değişimlerinin etkisini ölçmek amacıyla, projemizdeki Yağmurlu (Rainy) ve Bulutlu (Cloudy) koşulları test ederken referans olarak kullanılacaktır.

---

### Literatür Değerlendirmesi ve Projede Uygulanacak Yöntemler
İncelenen literatürde, makine öğrenmesi yaklaşımları (Örn. Almeida vd., 2015) yüksek doğruluk sunsa da, projemizin "klasik görüntü işleme" sınırları nedeniyle bu yöntemler kapsam dışı bırakılmıştır. Diğer çalışmalarda (Yusnita vd., Kumar vd.) sabit kameralı sistemlerde en yaygın ve başarılı yöntemin Gri Dönüşüm, Bulanıklaştırma (Blurring) ve Eşikleme (Thresholding/Edge Detection) algoritma zinciri olduğu görülmüştür. Bu doğrultuda projemizde, Ichihashi ve True'nun çalışmalarında vurgulanan "gölgelerin ve hava durumunun tespiti bozması" sorununu çözmek ve analiz etmek için iki farklı yöntem denenecektir: 
Birinci yöntem olarak sadece piksellerin parlaklık yoğunluğuna dayanan **Görüntü Eşikleme (Thresholding)** uygulanacaktır. İkinci yöntem olarak ise gölge etkisinden daha az etkilenme potansiyeli olan ve araçların sadece dış kaporta sınırlarını tespit eden **Canny Kenar Belirleme (Edge Detection)** algoritması kodlanacaktır. Her iki yöntemin, belirlediğimiz 3 farklı hava/ışık koşulundaki başarı oranları karşılaştırılarak raporlanacaktır.