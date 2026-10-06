# Otopark Doluluk Tespiti Veri Seti

## 1. Verinin Üretimi ve Koşullar
Bu veri seti, farklı gün saatlerinde (güneş ışığı, keskin bina gölgeleri ve düşük kontrast durumlarında) bir otopark alanının yüksek bir açıdan çekilmiş 60 adet dış mekan fotoğrafından oluşmaktadır. Proje yönergesinde belirtilen "20 farklı doluluk düzeni ve farklı ışık/açı koşulları" hedefine uygun olarak derlenmiştir. Kamera açısının yüksekliği ve mesafesi nedeniyle karelerde hiçbir yayanın veya kişinin yüzü seçilememekte olup, kişisel verilerin gizliliği korunmuştur.

**Dış Veri Kaynağı:** [  Açık kaynaklı PKLot veri setinden alınmıştır.https://www.kaggle.com/ ]
**Kullanım Koşulları:** Sadece akademik ve eğitim amaçlı dönem projesi kapsamında kullanılmıştır.

## 2. Etiket Biçimi (Label Format)
Geleneksel sayısal görüntü işleme (DIP) yöntemleri kullanıldığı için harici bir etiketleme dosyası (XML, JSON, YOLO txt vb.) oluşturulmamıştır. Sistem "Sabit Koordinat (ROI)" mantığıyla çalıştığı için, incelenen 6 adet park yerinin piksel koordinatları (x1, y1, x2, y2) doğrudan Python kodunun içerisinde bir liste (`park_yerleri`) olarak tanımlanmış ve donanımsal (hardcoded) etiketleme yapılmıştır.

## 3. Geliştirme ve Test Dosyaları
Veri setindeki toplam 60 fotoğraf, algoritmanın Ar-Ge aşaması ve nihai doğrulaması için %70 ve %30 oranlarında iki klasöre ayrılmıştır:
* **`data/gelistirme/` (42 Fotoğraf):** Görüntü işleme algoritmalarının (CLAHE, Sobel X) entegrasyonu ve piksel yoğunluğu eşik değerinin (Threshold: %12) optimum seviyesinin belirlenmesi için kullanılmıştır. 
* **`data/test/` (18 Fotoğraf):** Sistemin geliştirme aşamasında hiç görmediği, parametreleri sabitlenmiş nihai algoritmanın gerçek dünya başarısını (Accuracy) ölçmek amacıyla ayrılmış test görselleridir.

## 4. Veri Erişimi ve Boyutlar
Fotoğraflar optimize edilmiş formatta (JPG) olduğu ve GitHub'ın standart repo sınırlarını (100 MB) aşmadığı için doğrudan bu `data` klasörü altında barındırılmaktadır. Bu nedenle harici bir bulut indirme (Drive/Dropbox vb.) bağlantısına ihtiyaç duyulmamış olup, öğretim elemanı repoyu klonladığı an tüm verilere doğrudan erişebilecektir.
