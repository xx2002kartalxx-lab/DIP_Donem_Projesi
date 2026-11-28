
# Otopark Doluluk Tespiti Veri Seti

## 1. Verinin Üretimi ve Koşullar
Bu projede kullanılan görüntüler, dış mekan otopark doluluk tespiti çalışmalarında standart kıyaslama (benchmark) olarak kullanılan **PKLot** veri setinin **PUCPR** kamerasına ait kayıtlarından seçilmiştir.

* **Resmi Veri Seti Sayfası (UFPR - VRI Lab):** https://web.inf.ufpr.br/vri/databases/parking-lot-database/
* **Kaggle Veri Seti Bağlantısı:** https://www.kaggle.com/datasets/ammarnassanalhajali/pklot-dataset
* **Kullanım Koşulu ve Lisans:** Veri seti **Creative Commons Attribution 4.0 International (CC BY 4.0)** lisansı ile sunulmaktadır. Kaynak makaleye atıf yapılması koşuluyla akademik ve eğitim amaçlı çalışmalarda serbestçe kullanılabilir.
* **Kaynak Makale Atfı:** Almeida, P. R. L., Oliveira, L. S., Britto Jr., A. S., Silva Jr., E. J., & Koerich, A. L. (2015). *PKLot – A robust dataset for parking lot classification*. Expert Systems with Applications, 42(11), 4937–4949.


## 2. Etiket Biçimi (Label Format)
Geleneksel sayısal görüntü işleme (DIP) yöntemleri kullanıldığı için harici bir etiketleme dosyası (XML, JSON, YOLO txt vb.) oluşturulmamıştır. Sistem "Sabit Koordinat (ROI)" mantığıyla çalıştığı için, incelenen 6 adet park yerinin piksel koordinatları (x1, y1, x2, y2) doğrudan Python kodunun içerisinde bir liste (`park_yerleri`) olarak tanımlanmıştır. Görsel çıktılarda **yeşil kutular boş, mavi kutular dolu park yerlerini** göstermektedir.

## 3. Geliştirme ve Test Dosyaları
Veri setindeki toplam 60 fotoğraf, algoritmanın Geliştirme aşaması ve nihai doğrulaması için %70 ve %30 oranlarında iki klasöre ayrılmıştır:
* **`data/gelistirme/` (42 Fotoğraf):** Görüntü işleme algoritmalarının (CLAHE, Sobel X) entegrasyonu ve piksel yoğunluğu eşik değerinin (Threshold: %12) optimum seviyesinin belirlenmesi için kullanılmıştır.
* **`data/test/` (18 Fotoğraf):** Sistemin geliştirme aşamasında hiç görmediği, parametreleri sabitlenmiş nihai algoritmanın test başarısını ölçmek amacıyla ayrılmış test görselleridir.

## 4. Veri Erişimi ve Boyutlar
Fotoğraflar optimize edilmiş formatta (JPG) olduğu ve GitHub'ın standart repo sınırlarını (100 MB) aşmadığı için doğrudan bu `data` klasörü altında barındırılmaktadır. Bu nedenle harici bir bulut indirme (Drive/Dropbox vb.) bağlantısına ihtiyaç duyulmamış olup, öğretim elemanı repoyu klonladığı an tüm verilere doğrudan erişebilecektir.
