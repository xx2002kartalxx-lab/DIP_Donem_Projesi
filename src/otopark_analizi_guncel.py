#!/usr/bin/env python
# coding: utf-8

# In[30]:


import cv2
import matplotlib.pyplot as plt

# 1. Resmi oku (Jupyter'in bulunduğu klasörden bir üstteki data klasörüne gidiyoruz)
resim_yolu = "../data/gelistirme/2012-09-12_07_39_15.jpg"
resim = cv2.imread(resim_yolu)

if resim is None:
    print("Hata: Fotoğraf bulunamadı. Lütfen dosya adını kontrol edin.")
else:
    # 2. OpenCV resmi BGR okur, Matplotlib ise RGB gösterir. Renkleri düzeltelim:
    resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

    # 3. Resmi hücrenin içinde büyük ve eksenleriyle (koordinatlarıyla) birlikte göster
    plt.figure(figsize=(15, 10)) # Boyutu büyüterek pikselleri netleştirdik
    plt.imshow(resim_rgb)
    plt.title("Otopark Görüntüsü - Koordinatları eksenlerden okuyabilirsiniz")
    plt.show()


# In[32]:


# Senin tespitlerine göre perspektif düzeltmesi yapılmış özel koordinatlar
park_yerleri = [
    {"id": 1, "koordinat": (705, 180, 745, 240), "durum": "Dolu (Beyaz)"},   # Sağa kaydırıldı, beyaz arabayı tam alacak
    {"id": 2, "koordinat": (745, 180, 785, 240), "durum": "Boş"},            # Beyaz arabanın bittiği yerden başlıyor
    {"id": 3, "koordinat": (770, 180, 810, 240), "durum": "Boş"},
    {"id": 4, "koordinat": (810, 180, 845, 240), "durum": "Boş"},
    {"id": 5, "koordinat": (845, 180, 885, 240), "durum": "Dolu (Siyah)"},   # Siyah araba tam ortalandı
    {"id": 6, "koordinat": (885, 180, 925, 240), "durum": "Dolu (Kırmızı)"}  # Kırmızı araba tam ortalandı
]

plt.figure(figsize=(18, 4)) 

for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    plt.subplot(1, 6, i+1)
    plt.imshow(kirpilmis_park)
    plt.title(f"Park {park['id']} - {park['durum']}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[12]:


plt.figure(figsize=(18, 4))

for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # 1. Adım: Resmi renkli (RGB) formattan Gri Tonlamaya (Grayscale) çevir
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)

    # 2. Adım: Asfalttaki pürüzleri ve ufak gölgeleri yoksaymak için Bulanıklaştırma (Blur) uygula
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)

    # 3. Adım: Eşikleme (Thresholding)
    # Parlaklık değeri 100'ün üzerinde olan pikselleri tam BEYAZ (255), altındakileri tam SİYAH (0) yap
    _, threshold_park = cv2.threshold(blur_park, 100, 255, cv2.THRESH_BINARY)

    plt.subplot(1, 6, i+1)
    # Matplotlib'in siyah-beyaz resmi doğru renk haritasıyla (cmap='gray') göstermesi gerekir
    plt.imshow(threshold_park, cmap='gray')
    plt.title(f"Park {park['id']} - {park['durum']}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[15]:


for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # Aynı işlemleri tekrar uyguluyoruz
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)

    # THRESH_BINARY_INV ile parlak asfaltı siyah(0), koyu renkli araç ve gölgeleri beyaz(255) yapıyoruz
    _, threshold_park = cv2.threshold(blur_park, 100, 255, cv2.THRESH_BINARY_INV)

    # Beyaz (sıfır olmayan) pikselleri say
    beyaz_piksel_sayisi = cv2.countNonZero(threshold_park)
    toplam_piksel = threshold_park.shape[0] * threshold_park.shape[1]
    yuzde = (beyaz_piksel_sayisi / toplam_piksel) * 100

    print(f"Park {park['id']} ({park['durum']}): {beyaz_piksel_sayisi} beyaz piksel (Doluluk: %{yuzde:.1f})")


# In[16]:


plt.figure(figsize=(18, 4))

for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # 1. Gri tonlamaya çevir ve bulanıklaştır (Standart ön işlemler)
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)

    # 2. Canny Kenar Belirleme (Edge Detection)
    # Alt eşik 50, üst eşik 150. Sadece belirgin kenarları (arabaların hatlarını) çizecek.
    canny_park = cv2.Canny(blur_park, 50, 150)

    plt.subplot(1, 6, i+1)
    plt.imshow(canny_park, cmap='gray')
    plt.title(f"Park {park['id']} - {park['durum']}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[34]:


for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # 1. Ön işlemler
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)

    # 2. Canny Edge Detection
    canny_park = cv2.Canny(blur_park, 50, 150)

    # 3. Kenar (beyaz) pikselleri say
    beyaz_piksel_sayisi = cv2.countNonZero(canny_park)
    toplam_piksel = canny_park.shape[0] * canny_park.shape[1]
    yuzde = (beyaz_piksel_sayisi / toplam_piksel) * 100

    print(f"Park {park['id']} ({park['durum']}): {beyaz_piksel_sayisi} kenar pikseli (Yoğunluk: %{yuzde:.1f})")


# In[18]:


import numpy as np

plt.figure(figsize=(18, 4))

# Morfolojik işlemler için 3x3 boyutunda bir matris (kernel/çekirdek) oluşturuyoruz
kernel = np.ones((3, 3), np.uint8)

for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # 1. Ön işlemler ve Canny
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)
    canny_park = cv2.Canny(blur_park, 50, 150)

    # 2. Morfolojik Filtre: Dilation (Yayma)
    # iterations=1 parametresi ile beyaz çizgileri 1 kat kalınlaştırıyoruz
    morfoloji_park = cv2.dilate(canny_park, kernel, iterations=1)

    plt.subplot(1, 6, i+1)
    plt.imshow(morfoloji_park, cmap='gray')
    plt.title(f"Park {park['id']} - {park['durum']}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[33]:


for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    kirpilmis_park = resim_rgb[y1:y2, x1:x2]

    # 1. Ön işlemler ve Canny
    gri_park = cv2.cvtColor(kirpilmis_park, cv2.COLOR_RGB2GRAY)
    blur_park = cv2.GaussianBlur(gri_park, (5, 5), 0)
    canny_park = cv2.Canny(blur_park, 50, 150)

    # 2. Morfolojik Filtre: Dilation
    morfoloji_park = cv2.dilate(canny_park, kernel, iterations=1)

    # 3. Yeni kalınlaşmış pikselleri say
    beyaz_piksel_sayisi = cv2.countNonZero(morfoloji_park)
    toplam_piksel = morfoloji_park.shape[0] * morfoloji_park.shape[1]
    yuzde = (beyaz_piksel_sayisi / toplam_piksel) * 100

    print(f"Park {park['id']} ({park['durum']}): {beyaz_piksel_sayisi} piksel (Yoğunluk: %{yuzde:.1f})")


# In[28]:


import os

print("1. Jupyter'in şu an çalıştığı konum:", os.getcwd())
print("-" * 30)

try:
    print("2. Data klasörünün içindekiler:")
    print(os.listdir("../data"))
except Exception as e:
    print("Data klasörü bulunamadı:", e)

print("-" * 30)

try:
    print("3. Gelistirme klasörünün içindekiler:")
    print(os.listdir("../data/gelistirme"))
except Exception as e:
    print("Gelistirme klasörü bulunamadı:", e)


# In[40]:


import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

park_yerleri = [
    {"id": 1, "koordinat": (705, 180, 745, 240)},
    {"id": 2, "koordinat": (745, 180, 785, 240)},
    {"id": 3, "koordinat": (770, 180, 810, 240)},
    {"id": 4, "koordinat": (810, 180, 845, 240)},
    {"id": 5, "koordinat": (845, 180, 885, 240)},
    {"id": 6, "koordinat": (885, 180, 925, 240)}
]

kernel = np.ones((3, 3), np.uint8)
resim_yollari = glob.glob("../data/gelistirme/*.jpg")
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

for resim_yolu in resim_yollari[:5]:
    resim = cv2.imread(resim_yolu)

    if resim is None:
        continue

    cizim_resmi = resim.copy()
    gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    esitlenmis_gri = clahe.apply(gri)
    blur = cv2.GaussianBlur(esitlenmis_gri, (5, 5), 0)

    # YENİ ADIM: Canny yerine Sobel kullanarak sadece X eksenindeki (Dikey) kenarları buluyoruz.
    # 1, 0 parametreleri X'i açıp Y'yi kapatır. Böylece yatay gölge çizgisi görünmez olur.
    sobel_x = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)

    # Sobel'den gelen gri tonlu kenarları Canny gibi keskin siyah-beyaza (Binary) çeviriyoruz
    _, sobel_binary = cv2.threshold(sobel_x, 50, 255, cv2.THRESH_BINARY)

    # Morfolojiyi bu yeni dikey kenarların üzerine uyguluyoruz
    morfoloji = cv2.dilate(sobel_binary, kernel, iterations=1)

    bos_park_sayisi = 0

    for park in park_yerleri:
        x1, y1, x2, y2 = park["koordinat"]
        roi = morfoloji[y1:y2, x1:x2]

        beyaz_piksel = cv2.countNonZero(roi)
        toplam_piksel = roi.shape[0] * roi.shape[1]
        yuzde = (beyaz_piksel / toplam_piksel) * 100

        # Eşik değerimizi tekrar %8 olarak test ediyoruz
        if yuzde > 12.0:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (255, 0, 0), 2)
        else:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (0, 255, 0), 2)
            bos_park_sayisi += 1

    cizim_resmi_rgb = cv2.cvtColor(cizim_resmi, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 6))
    plt.imshow(cizim_resmi_rgb)
    plt.title(f"Bos Yer: {bos_park_sayisi}")
    plt.axis('off')
    plt.show()


# In[38]:


# Sadece gölgenin sorun yarattığı 2. fotoğrafı (indeks 1) mercek altına alıyoruz
resim_yolu = resim_yollari[1] 
resim = cv2.imread(resim_yolu)

gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
esitlenmis_gri = clahe.apply(gri)
blur = cv2.GaussianBlur(esitlenmis_gri, (5, 5), 0)

# Sobel ile dikey kenarları arıyoruz
sobel_x = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
_, sobel_binary = cv2.threshold(sobel_x, 50, 255, cv2.THRESH_BINARY)
morfoloji = cv2.dilate(sobel_binary, kernel, iterations=1)

plt.figure(figsize=(18, 4))
for i, park in enumerate(park_yerleri):
    x1, y1, x2, y2 = park["koordinat"]
    roi = morfoloji[y1:y2, x1:x2]

    beyaz_piksel = cv2.countNonZero(roi)
    toplam_piksel = roi.shape[0] * roi.shape[1]
    yuzde = (beyaz_piksel / toplam_piksel) * 100

    plt.subplot(1, 6, i+1)
    plt.imshow(roi, cmap='gray')
    plt.title(f"Park {park['id']} - %{yuzde:.1f}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[41]:


import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

park_yerleri = [
    {"id": 1, "koordinat": (705, 180, 745, 240)},
    {"id": 2, "koordinat": (745, 180, 785, 240)},
    {"id": 3, "koordinat": (770, 180, 810, 240)},
    {"id": 4, "koordinat": (810, 180, 845, 240)},
    {"id": 5, "koordinat": (845, 180, 885, 240)},
    {"id": 6, "koordinat": (885, 180, 925, 240)}
]

kernel = np.ones((3, 3), np.uint8)
resim_yollari = glob.glob("../data/gelistirme/*.jpg")
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# [:5] kısıtlamasını sildik, klasördeki 42 fotoğrafın TAMAMI işlenecek
for resim_yolu in resim_yollari:
    resim = cv2.imread(resim_yolu)

    if resim is None:
        continue

    cizim_resmi = resim.copy()
    gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    esitlenmis_gri = clahe.apply(gri)
    blur = cv2.GaussianBlur(esitlenmis_gri, (5, 5), 0)

    sobel_x = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
    _, sobel_binary = cv2.threshold(sobel_x, 50, 255, cv2.THRESH_BINARY)
    morfoloji = cv2.dilate(sobel_binary, kernel, iterations=1)

    bos_park_sayisi = 0

    for park in park_yerleri:
        x1, y1, x2, y2 = park["koordinat"]
        roi = morfoloji[y1:y2, x1:x2]

        beyaz_piksel = cv2.countNonZero(roi)
        toplam_piksel = roi.shape[0] * roi.shape[1]
        yuzde = (beyaz_piksel / toplam_piksel) * 100

        # SENİN BULDUĞUN OPTİMUM EŞİK DEĞERİ: %12.0
        if yuzde > 12.0:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (255, 0, 0), 2)
        else:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (0, 255, 0), 2)
            bos_park_sayisi += 1

    cizim_resmi_rgb = cv2.cvtColor(cizim_resmi, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 6))
    plt.imshow(cizim_resmi_rgb)
    plt.title(f"Bos Yer: {bos_park_sayisi} | Dosya: {resim_yolu.split('/')[-1]}")
    plt.axis('off')
    plt.show()


# In[2]:

# Canny ve Sobel X karşılaştırması: yalnızca 42 fotoğraflık GELİŞTİRME seti.
# 18 fotoğraflık test seti bu karşılaştırmaya dahil edilmez.
import csv
import os

park_yerleri_karsilastirma = [
    {"id": 1, "koordinat": (705, 180, 745, 240)},
    {"id": 2, "koordinat": (745, 180, 785, 240)},
    {"id": 3, "koordinat": (770, 180, 810, 240)},
    {"id": 4, "koordinat": (810, 180, 845, 240)},
    {"id": 5, "koordinat": (845, 180, 885, 240)},
    {"id": 6, "koordinat": (885, 180, 925, 240)}
]

gelisim_resimleri = sorted(glob.glob("../data/gelistirme/*.jpg"))
clahe_karsilastirma = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
kernel_karsilastirma = np.ones((3, 3), np.uint8)
karsilastirma_sonuclari = []
ornek_gorseller = None

print(f"Geliştirme setinde bulunan fotoğraf sayısı: {len(gelisim_resimleri)}")

for resim_yolu in gelisim_resimleri:
    resim = cv2.imread(resim_yolu)
    if resim is None:
        print(f"Okunamayan fotoğraf atlandı: {resim_yolu}")
        continue

    # İki yönteme de aynı ön işleme uygulanır: gri tonlama + CLAHE + Gaussian Blur.
    gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    clahe_gri = clahe_karsilastirma.apply(gri)
    blur = cv2.GaussianBlur(clahe_gri, (5, 5), 0)

    canny = cv2.Canny(blur, 50, 150)
    canny_morfoloji = cv2.dilate(canny, kernel_karsilastirma, iterations=1)

    sobel_x = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
    _, sobel_binary = cv2.threshold(sobel_x, 50, 255, cv2.THRESH_BINARY)
    sobel_morfoloji = cv2.dilate(sobel_binary, kernel_karsilastirma, iterations=1)

    satir = {"fotoğraf": os.path.basename(resim_yolu)}
    for park in park_yerleri_karsilastirma:
        x1, y1, x2, y2 = park["koordinat"]
        canny_roi = canny_morfoloji[y1:y2, x1:x2]
        sobel_roi = sobel_morfoloji[y1:y2, x1:x2]
        canny_yogunluk = (cv2.countNonZero(canny_roi) / canny_roi.size) * 100 if canny_roi.size else 0
        sobel_yogunluk = (cv2.countNonZero(sobel_roi) / sobel_roi.size) * 100 if sobel_roi.size else 0
        satir[f"park_{park['id']}_canny_yuzde"] = round(canny_yogunluk, 2)
        satir[f"park_{park['id']}_sobel_x_yuzde"] = round(sobel_yogunluk, 2)

    canny_degerleri = [satir[f"park_{p['id']}_canny_yuzde"] for p in park_yerleri_karsilastirma]
    sobel_degerleri = [satir[f"park_{p['id']}_sobel_x_yuzde"] for p in park_yerleri_karsilastirma]
    satir["ortalama_canny_yogunluk"] = round(sum(canny_degerleri) / len(canny_degerleri), 2)
    satir["ortalama_sobel_x_yogunluk"] = round(sum(sobel_degerleri) / len(sobel_degerleri), 2)
    karsilastirma_sonuclari.append(satir)

    if ornek_gorseller is None:
        ornek_gorseller = (canny_morfoloji, sobel_morfoloji)

os.makedirs("../results", exist_ok=True)
csv_yolu = "../results/canny_sobel_gelistirme_karsilastirmasi.csv"
if karsilastirma_sonuclari:
    with open(csv_yolu, "w", newline="", encoding="utf-8-sig") as dosya:
        alanlar = list(karsilastirma_sonuclari[0].keys())
        yazici = csv.DictWriter(dosya, fieldnames=alanlar)
        yazici.writeheader()
        yazici.writerows(karsilastirma_sonuclari)

    canny_ort = sum(x["ortalama_canny_yogunluk"] for x in karsilastirma_sonuclari) / len(karsilastirma_sonuclari)
    sobel_ort = sum(x["ortalama_sobel_x_yogunluk"] for x in karsilastirma_sonuclari) / len(karsilastirma_sonuclari)
    print("\\n--- GELİŞTİRME SETİ ÖZETİ ---")
    print(f"İşlenen fotoğraf: {len(karsilastirma_sonuclari)}")
    print(f"Canny ortalama kenar yoğunluğu: %{canny_ort:.2f}")
    print(f"Sobel X ortalama kenar yoğunluğu: %{sobel_ort:.2f}")
    print(f"Ayrıntılı sonuçlar kaydedildi: {csv_yolu}")
else:
    print("Karşılaştırma için geçerli fotoğraf bulunamadı.")

if ornek_gorseller is not None:
    canny_gorsel, sobel_gorsel = ornek_gorseller
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(canny_gorsel, cmap="gray")
    plt.title("Canny - Geliştirme setinden örnek")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(sobel_gorsel, cmap="gray")
    plt.title("Sobel X - Geliştirme setinden örnek")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# Kenar yoğunluğu doğruluk oranı değildir. Doğruluk/FP/FN için bağımsız gerçek etiketler gerekir.


# In[1]:


import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

# Koordinatlar test verisinde de tamamen aynı kalıyor
park_yerleri = [
    {"id": 1, "koordinat": (705, 180, 745, 240)},
    {"id": 2, "koordinat": (745, 180, 785, 240)},
    {"id": 3, "koordinat": (770, 180, 810, 240)},
    {"id": 4, "koordinat": (810, 180, 845, 240)},
    {"id": 5, "koordinat": (845, 180, 885, 240)},
    {"id": 6, "koordinat": (885, 180, 925, 240)}
]

kernel = np.ones((3, 3), np.uint8)

# DİKKAT: Yol artık sadece 18 fotoğraflık test klasörüne bakıyor
resim_yollari = glob.glob("../data/test/*.jpg") 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

for resim_yolu in resim_yollari:
    resim = cv2.imread(resim_yolu)

    if resim is None:
        continue

    cizim_resmi = resim.copy()
    gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    esitlenmis_gri = clahe.apply(gri)
    blur = cv2.GaussianBlur(esitlenmis_gri, (5, 5), 0)

    sobel_x = cv2.Sobel(blur, cv2.CV_8U, 1, 0, ksize=3)
    _, sobel_binary = cv2.threshold(sobel_x, 50, 255, cv2.THRESH_BINARY)
    morfoloji = cv2.dilate(sobel_binary, kernel, iterations=1)

    bos_park_sayisi = 0

    for park in park_yerleri:
        x1, y1, x2, y2 = park["koordinat"]
        roi = morfoloji[y1:y2, x1:x2]

        beyaz_piksel = cv2.countNonZero(roi)
        toplam_piksel = roi.shape[0] * roi.shape[1]
        yuzde = (beyaz_piksel / toplam_piksel) * 100

        # Geliştirme setinde bulduğumuz %12 sabiti test setinde sınanıyor
        if yuzde > 12.0:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (255, 0, 0), 2)
        else:
            cv2.rectangle(cizim_resmi, (x1, y1), (x2, y2), (0, 255, 0), 2)
            bos_park_sayisi += 1

    cizim_resmi_rgb = cv2.cvtColor(cizim_resmi, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 6))
    plt.imshow(cizim_resmi_rgb)
    plt.title(f"Bos Yer: {bos_park_sayisi} | Dosya: {resim_yolu.split('/')[-1]}")
    plt.axis('off')
    plt.show()


# In[ ]:



