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
İncelenen literatürde, makine öğrenmesi yaklaşımları (Örn. Almeida vd., 2015) yüksek doğruluk sunsa da, projemizin "klasik görüntü işleme" sınırları nedeniyle bu yöntemler kapsam dışı bırakılmıştır. Diğer çalışmalarda (Yusnita vd., Kumar vd.) sabit kameralı sistemlerde en yaygın ve başarılı yöntemin Gri Dönüşüm, Bulanıklaştırma (Blurring) ve Eşikleme (Thresholding/Edge Detection) algoritma zinciri olduğu görülmüştür. 
 akademik çalışmalar incelendiğinde, sabit kameralı dış mekan otoparklarında klasik görüntü işleme yaklaşımlarının temel olarak ön işleme (gri tonlama, kontrast dengeleme, bulanıklaştırma), kenar/gradyan çıkarımı, eşikleme ve morfolojik işlemler üzerine kurulduğu görülmektedir. Ancak dış mekan koşullarında gün ışığındaki ani değişimler ve keskin bina gölgeleri, yalnızca parlaklık tabanlı standart eşikleme (Thresholding) yöntemlerinin araç ve gölge ayrımında kararsız kalmasına yol açmaktadır.

Bu bulgular doğrultusunda projemizde ilk aşamada temel eşikleme (Thresholding) ve Canny kenar tespiti yaklaşımları incelenmiş; ardından dış mekan gölge problemini aşmak için yerel kontrast dengeleme (**CLAHE**), gürültü azaltma (**Gaussian Blur**) ve morfolojik genişletme (**Dilation**) adımlarıyla desteklenen iki kenar çıkarım yöntemi aynı geliştirme seti (42 fotoğraf) üzerinde karşılaştırılmıştır:
1. **Standart Canny Kenar Tespiti:** Çok yönlü kenar yakalama yapısı nedeniyle asfalt üzerindeki keskin yatay bina gölgelerini de araç kenarı olarak algılayabilmektedir.
2. **Yönlü Sobel X Filtresi:** Yalnızca dikey kenar bileşenlerine odaklanarak yatay gölge hatlarını bastırmakta ve araçların yapısal hatlarını daha kararlı biçimde ortaya çıkarmaktadır.

Bu nedenle projemizin nihai karşılaştırmalı deneyi **Canny** ve **Sobel X** yöntemleri arasında kurgulanmış, geliştirme setindeki sayısal ve görsel analizler sonucunda gölgeye karşı daha yüksek kararlılık sunan **CLAHE + Gaussian Blur + Sobel X + Eşikleme + Morfoloji** işlem zinciri nihai yöntem olarak seçilmiştir.