# Digital Image Processing - Dönem Projesi Yapay Zeka Kullanım Kaydı

Bu belge, Digital Image Processing dersi kapsamında yürütülen dönem projesi (Proje 08 - Otopark Doluluk Tespiti) boyunca yapay zeka araçlarından alınan desteği şeffaf bir şekilde belgelemek amacıyla oluşturulmuştur. Proje tek kişilik bir grup tarafından yürütülmektedir.

## Oturum: 5 Ekim 2026

**Kullanılan Yapay Zeka Aracı:** Google Gemini (Büyük Dil Modeli)
**Proje Aşaması:** Proje seçimi, strateji belirleme, veri seti hazırlığı ve ilk kod altyapısının kurulması.

### Yapay Zeka Katkısının Detayları:

1. **Proje Stratejisi ve Analiz:** 
   * Proje yönergesi yapay zeka ile analiz edilerek, tek kişi çalışma şartlarına en uygun projenin (Proje 08) seçilmesi sağlandı.
   * Ders sorumlusunun verdiği "ileri hedef iptali" ve "hazır veri seti kullanımı" izinleri doğrultusunda en verimli yol haritası çıkarıldı.

2. **Veri Seti Seçimi ve Optimizasyonu:** 
   * Kaggle platformundaki "PKLot" veri setinin analizi yapıldı. Kamera açısı en dik ve sabit olan `PUCPR` alt klasörü tespit edildi.
   * Proje isterlerindeki "3 farklı ışık/hava koşulunda toplam 60 fotoğraf" kuralını eksiksiz sağlamak üzere güneşli, bulutlu ve yağmurlu (Sunny, Cloudy, Rainy) klasörlerinden veri seçimi stratejisi geliştirildi.

3. **Geliştirme Ortamı Kararları:** 
   * OpenCV (`cv2.imshow`) çakışmalarını önlemek için Jupyter Notebook yerine Spyder kullanılmasına karar verildi.
   * Ekip çalışması gerektiren Branch/Pull Request GitHub özellikleri yerine, tek kişilik çalışmaya uygun doğrudan "main" dalına commit/push yapma yöntemi planlandı.

4. **Kod Üretimi:** 
   * Otopark görsellerindeki pilot park yerlerinin koordinatlarını dinamik olarak belirlemek için OpenCV'nin fare tıklama olaylarını (`cv2.setMouseCallback`) kullanan `koordinat_bulucu.py` betiğinin ilk taslağı yapay zeka yardımıyla yazıldı.