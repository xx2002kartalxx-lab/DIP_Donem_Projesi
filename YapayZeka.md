Oturum 1 — 05.10.2026
Oturum bilgileri
Katılan öğrenci veya öğrenciler: Muhammet Furkan Kart

Kullanılan araç ve biliniyorsa model: Google Gemini

Bu dosyadaki oturum kayıtları yapay zekâ yardımıyla hazırlanır. Her kayıt, yalnızca belirtilen oturumun erişilebilir bağlamını kapsar. Öğrenciler kayıtları kontrol etmekten, kaynakları doğrulamaktan ve teslim edilen çalışmanın tamamını açıklayabilmekten sorumludur.

## Oturum 1 — 05.10.2026

### Oturum bilgileri
- Katılan öğrenci veya öğrenciler: Muhammet Furkan Kart
- Kullanılan araç ve biliniyorsa model: Google Gemini
- Çalışmanın amacı: Proje 08 (Masaüstü Otopark Doluluk Tespiti) için uygun veri setinin seçilmesi, 60 fotoğraflık veri havuzunun proje dizinine entegre edilerek GitHub'a gönderilmesi ve OpenCV ile park yerlerinin koordinatlarının bulunması için temel çerçevenin kurulması.
- İlgili uygulama commit’i veya pull request: [Commit: "Yapay zeka kayıt belgesi eklendi" (61 dosya)]

### Yapay zekâ katkısı
| İş | Katkı türü | İlgili dosya veya fonksiyon | Uygulama durumu |
|---|---|---|---|
| Veri seti ve koşul belirleme stratejisi | yöntem önerisi | `data/` klasörü | dosyaya uygulandı |
| GitHub Desktop kullanım yönlendirmesi | kavram açıklama | `main` branch, commit/push adımları | dosyaya uygulandı |
| Manuel fare tıklaması ile koordinat tespiti | kod üretimi | `src/koordinat_bulucu.py` | kodu verildi (çalıştırma doğrulanmadı) |
| Oturum kayıt dosyasının (YapayZeka.md) hazırlanması | dokümantasyon | `YapayZeka.md` | dosyaya uygulandı |

### Yöntem ve ders kapsamına uygunluk
- **Kullanılan veya önerilen görüntü işleme yöntemleri ve kısa gerekçeleri:** Proje kapsamında tüm otoparkı otomatik taramak yerine "pilot park yerleri" belirlemek için `cv2.setMouseCallback` ile fare tıklama yöntemi önerilmiştir. Tespit algoritması için yalnızca piksel yoğunluk eşikleme (Thresholding) ve kenar belirleme (Canny Edge Detection) yöntemlerinin klasik OpenCV fonksiyonlarıyla kullanılması planlanmıştır.
- **Dersin sınırlarıyla çelişen öneri varsa ne olduğu ve düzeltilip düzeltilmediği:** Derin öğrenme, makine öğrenmesi veya hazır sınıflandırıcılar içeren hiçbir yöntem önerilmemiş olup, tüm yaklaşım dersin sınırları olan klasik görüntü işleme teknikleriyle uyumlu tutulmuştur.

### Literatür taramasına yapay zekâ katkısı
| Kaynak veya arama konusu | Yapay zekânın yaptığı işlem | Erişim ve doğrulama durumu | Literatur.md dosyasına katkı |
|---|---|---|---|
| PKLot Dataset (PUCPR Otopark Verisi) - Kaggle | Veri seti arama, kamera açısı analizi (PUCPR vs. UFPR) ve 3 ışık/hava koşulunun (Sunny, Cloudy, Rainy) tasnifi. | yalnızca önerildi | Bu oturumda literatür taramasına katkı sağlanmadı. |

### Doğrulama ve açık sorunlar
- **Gerçekten çalıştırılan test veya deneyler ve gözlenen sonuçlar:** Toplam 60 adet fotoğraf (11, 12, 13, 14 Eylül tarihlerinden) `data/` klasörüne kopyalanmış ve GitHub üzerinden "Yapay zeka kayıt belgesi eklendi" mesajıyla başarılı bir şekilde repository'e push edilmiştir (öğrencinin bildiriminden doğrulanmıştır).
- **Çalıştırılmayan kontroller, bilinen hatalar ve belirsizlikler:** `src/koordinat_bulucu.py` içerisindeki OpenCV pencere açma ve koordinat okuma kodunun, öğrencinin yerel Anaconda/Spyder ortamında sorunsuz çalışıp çalışmadığı henüz test edilmemiş ve doğrulanmamıştır.
- **Önerilip kullanılmayan veya hatalı olduğu anlaşılan öneriler:** Yönergedeki "ileri hedef" zorunluluğu, hoca ile yapılan görüşme sonucunda iptal edildiği için daha karmaşık segmentasyon ve nesne ayırma işlemleri stratejiden çıkarılmıştır.
- **Varsa doğrulanmayı bekleyen kaynak bilgileri ve literatür yorumları:** Kaggle PKLot veri setine ait PDF veya makale referanslarının doğrulanması beklenmektedir.

### Öğrencinin dolduracağı bölüm
- Yapay zekâ çıktısında neyi değiştirdik veya reddettik, neden?
Yapay zeka başlangıçta PCB hata tespiti projesini (Proje 04) önerdi ancak ben Otopark Doluluk Tespiti (Proje 08) üzerinden ilerlemeyi seçtim. Ayrıca 15 fotoğraf kullanmayı düşündüğümde AI bunu onayladı ancak hocanın 60 fotoğraf kuralını hatırlatarak veri setini 60'a çıkarmasını sağladım.
- Hangi kodu ve sonucu kendimiz kontrol ettik?Kaggle PKLot veri setinden PUCPR kamerasının Sunny, Cloudy ve Rainy klasörlerindeki fotoğrafları bizzat inceledim. Toplam 60 fotoğrafın data klasörüne aktarılmasını ve GitHub'a başarıyla yüklenmesini kontrol ettim. Kod çalıştırma henüz yapılmadı.
- Önerilen kaynaklardan hangilerini kendimiz okuyup doğruladık?Kaggle'daki PKLot veri setinin açıklamasını ve klasör yapısını inceleyip projeye uygunluğunu doğruladım.
- Yapay zekânın kaynak bilgisi veya yorumunda hangi düzeltmeleri yaptık?Yapay zeka bir klasörde sadece 15 fotoğraf olduğunu varsaydı, ancak Kaggle web arayüzünün sadece 15 önizleme gösterdiğini, klasörün içinde aslında 34 fotoğraf olduğunu fark edip bu durumu ben düzelttim.
- Bu oturumda ne öğrendik?Sabit koordinatlı görüntü işleme projelerinde (yapay zeka modeli kullanılmadığında) kamera açısının değişmemesinin ne kadar kritik olduğunu ve GitHub Desktop üzerinden branch (dal) kullanmadan doğrudan ana depoya (main) veri yüklemeyi öğrendim.
- Kaydı kontrol eden öğrenciler:Muhammet Furkan Kart 221451016

## Oturum 2 — 05.10.2026

### Oturum bilgileri
- Katılan öğrenci veya öğrenciler: Muhammet Furkan Kart
- Kullanılan araç ve biliniyorsa model: Google Gemini
- Çalışmanın amacı: Projenin literatür taraması aşamasının gerçekleştirilmesi, akademik makalelerin bulunması ve klasik görüntü işleme kısıtlarına uygun literatür özetlerinin hazırlanarak Literatur.md dosyasına aktarılması.
- İlgili uygulama commit’i veya pull request: [Literatur.md dosyası eklendi]

### Yapay zekâ katkısı
| İş | Katkı türü | İlgili dosya veya fonksiyon | Uygulama durumu |
|---|---|---|---|
| Literatür araştırması ve makale bulma | literatür desteği | `Literatur.md` | önerildi |
| Literatürdeki yöntemlerin ders kısıtlarına göre filtrelenmesi | dokümantasyon | `Literatur.md` | dosyaya uygulandı |
| Karşılaştırma ve yöntem seçimi paragrafının taslağı | yöntem önerisi | `Literatur.md` | dosyaya uygulandı |

### Yöntem ve ders kapsamına uygunluk
- **Kullanılan veya önerilen görüntü işleme yöntemleri ve kısa gerekçeleri:** Literatür incelemesinde Canny Edge Detection, Thresholding ve Gaussian Blur gibi klasik yöntemlerin kullanım gerekçeleri makaleler üzerinden temellendirildi.
- **Dersin sınırlarıyla çelişen öneri varsa ne olduğu ve düzeltilip düzeltilmediği:** Bulunan kaynaklardan biri (Almeida 2015) SVM ve LBP gibi öğrenme temelli metotlar içeriyordu. Bu kaynağın yöntem kısmının kısıtlara aykırı olduğu metin içinde açıkça belirtildi ve kaynağın sadece "veri seti temini" amacıyla referans alındığı vurgulanarak kural ihlali önlendi.

### Literatür taramasına yapay zekâ katkısı
| Kaynak veya arama konusu | Yapay zekânın yaptığı işlem | Erişim ve doğrulama durumu | Literatur.md dosyasına katkı |
|---|---|---|---|
| Almeida et al. (2015) - PKLot | Veri seti makalesinin bulunması ve ML kısıtının analizi | özet okundu (doğrulandı) | dosyaya eklendi |
| Yusnita et al. (2012) | Edge detection temelli makale araştırması | özet okundu (doğrulandı) | dosyaya eklendi |
| Ichihashi et al. (2009) | Gölge (shadow) problemlerini inceleyen akademik kaynak bulma | özet okundu (doğrulandı) | dosyaya eklendi |
| Kumar et al. (2025) | Güncel OpenCV pipeline mimarisini kullanan yayın bulma | özet okundu (doğrulandı) | dosyaya eklendi |
| True (2007) - UCSD | Statik imge (overhead) park yeri tespit raporu araştırması | özet okundu (doğrulandı) | dosyaya eklendi |

### Doğrulama ve açık sorunlar
- **Gerçekten çalıştırılan test veya deneyler ve gözlenen sonuçlar:** Literatür araştırması yapıldı, makalelerin DOI ve bağlantıları kontrol edilerek dosyaya eklendi.
- **Çalıştırılmayan kontroller, bilinen hatalar ve belirsizlikler:** Literatürde bahsedilen yöntemler (Thresholding vs Edge Detection) henüz kod üzerinde test edilmemiştir, sonraki adımda uygulanacaktır.
- **Önerilip kullanılmayan veya hatalı olduğu anlaşılan öneriler:** -
- **Varsa doğrulanmayı bekleyen kaynak bilgileri ve literatür yorumları:** -

### Öğrencinin dolduracağı bölüm
- Yapay zekâ çıktısında neyi değiştirdik veya reddettik, neden?Yapay zekanın bulduğu PKLot makalesindeki makine öğrenmesi (SVM) yöntemlerini dersin kurallarına aykırı olduğu için reddettim; bu makaleyi sadece kullandığımız veri setinin resmi dayanağı olarak literatüre ekledim.
- Hangi kodu ve sonucu kendimiz kontrol ettik?"Bu oturumda kod yazılmadı. Sadece Literatur.md ve YapayZeka.md dosyalarının proje dizinine doğru şekilde yerleştiği kontrol edildi.
- Önerilen kaynaklardan hangilerini kendimiz okuyup doğruladık?AI'nin önerdiği makalelerin (özellikle Kumar vd. ve Almeida vd.) DOI numaralarını ve bağlantılarını tarayıcıda açarak gerçekten var olduklarını, klasik görüntü işleme (OpenCV) anlattıklarını ve özet kısımlarını okuyup doğruladım.
- Yapay zekânın kaynak bilgisi veya yorumunda hangi düzeltmeleri yaptık?Yapay zekanın sunduğu kaynakların tam metinlerine erişim linklerini kontrol ettim, literatür değerlendirmesi paragrafını kendi proje kısıtlarıma (sadece Thresholding ve Edge Detection kullanma kararıma) göre netleştirdim."
- Bu oturumda ne öğrendik?Klasik görüntü işlemede otopark doluluğunu bulurken en büyük problemin asfaltın ıslaklığı ve araçların gölgeleri olduğunu, literatürün bu sorunu çözmek için kenar bulma (Edge Detection) ve bulanıklaştırma (Blur) yöntemlerine başvurduğunu öğrendim.
- Kaydı kontrol eden öğrenciler:Muhammet Furkan Kart 221451016
## Oturum 3 — 06.10.2026

### Oturum bilgileri
- Katılan öğrenci veya öğrenciler: Muhammet Furkan Kart
- Kullanılan araç ve biliniyorsa model: Gemini
- Çalışmanın amacı: Dış mekan otoparklarında dinamik ışık, bina gölgeleri ve kontrast değişimlerine dayanıklı Python ve OpenCV tabanlı otopark doluluk tespiti algoritmasının geliştirilmesi, test edilmesi ve eşik değerinin optimize edilmesi.
- İlgili uygulama commit’i veya pull request: [öğrenci sonradan ekleyecek]

### Yapay zekâ katkısı
| İş | Katkı türü | İlgili dosya veya fonksiyon | Uygulama durumu |
|---|---|---|---|
| Görüntü işleme ardışık düzeni (pipeline) tasarımı | yöntem önerisi | Jupyter Notebook / `main.py` | dosyaya uygulandı ve test edildi |
| Gölge ve kontrast sorunları için CLAHE ve Sobel X filtresi entegrasyonu | kod üretimi | Jupyter Notebook / `main.py` | dosyaya uygulandı ve test edildi |
| Piksel yoğunluğu eşik değerinin optimize edilmesi (%12) | hata ayıklama ve sonuç yorumlama | Jupyter Notebook / `main.py` | dosyaya uygulandı ve test edildi |

### Yöntem ve ders kapsamına uygunluk
- Kullanılan veya önerilen görüntü işleme yöntemleri ve kısa gerekçeleri: Gri tonlama, Gaussian Blur, CLAHE (Adaptif Histogram Eşitleme) ile karanlık gölgelerdeki detayların belirginleştirilmesi, Sobel X filtresi ile yatay bina gölgelerinin filtrelenip sadece dikey araç kenarlarının tespiti, morfolojik yayma (dilation) ve piksel yoğunluğu (thresholding) analizi kullanılmıştır. Bu yöntemler dış mekan koşullarındaki aydınlatma değişimlerinin etkisini en aza indirmek amacıyla seçilmiştir.
- Ders sınırıyla çelişen öneri varsa ne olduğu ve ders kapsamına uygunluğu: Ders kapsamıyla çelişen bir durum yoktur; geleneksel sayısal görüntü işleme temellerine (uzaysal filtreler, kenar tespiti ve eşikleme) dayanmaktadır.

### Doğrulama ve açık sorunlar
- Gerçekten çalıştırılan test veya deneyler ve gözlenen sonuçlar: Geliştirme veri setindeki 42 görüntü üzerinde 6 farklı ROI bölgesi test edilmiş, %95 başarı oranına ulaşılmıştır. Gölge altındaki araçların tespiti için eşik değeri %12 olarak doğrulanmıştır.
- Çalıştırılmayan kontroller, bilinen hatalar ve belirsizlikler: Araçların manevra yaptığı, çapraz durduğu veya park çizgilerini ihlal ettiği bazı uç durumlarda (edge cases) komşu piksellerden taşma nedeniyle yanlış pozitifler gözlemlenmiştir.
- Önerilip kullanılmayan veya hatalı olduğu anlaşılan öneriler: Standart Canny kenar tespiti filtresi dış mekan gölgelerinde aşırı gürültü ürettiği için yönlü Sobel X filtresi ile değiştirilmiştir.

### Öğrencinin dolduracağı bölüm
- Yapay zekâ çıktısında neyi değiştirdik veya reddettik, neden? Yapay zekâ ilk olarak standart Canny kenar tespiti algoritmasını önermişti; ancak bina gölgelerinin yatay çizgilerini araba kenarı sandığı için bu yaklaşımı reddettik ve sadece dikey kenarları tarayan yönlü Sobel X filtresine geçiş yaptık. Ayrıca önerilen %8 ve %15 eşik değerlerini veri setindeki gölge test sonuçlarına bakarak %12 olarak bizzat revize ettik.
- Hangi kodu ve sonucu kendimiz kontrol ettik? : Geliştirme veri setindeki 42 fotoğrafı Jupyter Lab üzerinde tek tek görselleştirerek inceledik. Özellikle gölgede kalan 5. fotoğrafın ve manevra yapan araçların sonuçlarını doğrudan gözümüzle kontrol edip hatalı piksellerin yüzdelik dilimlerini doğruladık.
- Bu oturumda ne öğrendik? Dış mekan görüntü işleme projelerinde aydınlatma değişimleri ve sert bina gölgelerinin klasik algoritmaları nasıl yanıltabileceğini ve bu sorunu çözmek için CLAHE ile kontrast eşitleme ve yönlü Sobel filtrelerinin nasıl birlikte kullanılması gerektiğini öğrendik. Ayrıca sabit koordinat (ROI) tabanlı sistemlerin manevra anlarındaki kısıtlamalarını analiz ettik.
- Kaydı kontrol eden öğrenciler:Muhammet Furkan Kart 221451016