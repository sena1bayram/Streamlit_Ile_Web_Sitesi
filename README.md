# 📚 Streamlit Veri Analizi ve Makine Öğrenimi Uygulaması

Bu proje, Streamlit kullanılarak geliştirilmiş kapsamlı bir veri analizi ve makine öğrenimi platformudur. Kullanıcıların kolayca veri görselleştirme, model eğitimi ve analiz yapmasına olanak tanır.

https://github.com/user-attachments/assets/80797450-977c-40e5-9b40-9da009fe41e5

## 🚀 Özellikler

- **Tasarım ve Sayfa Yapısı:**
  - Geniş ekran düzeni, özelleştirilmiş CSS ve üst barda şirket logosu ve tarih gösterimi.
- **Navigasyon ve Menü:**
  - Sol kenar çubuğu (sidebar) üzerinden "Ana Sayfa", "Hakkımızda" ve "İletişim" sayfalarına geçiş.
- **Ana Sayfa İçeriği:**
  - Şirket hakkında bilgiler ve müzik çalma özelliği.
- **Test Sayfası ve Model Seçimi:**
  - KNN, Random Forest, Decision Tree gibi sınıflandırma algoritmaları için seçim ve özelleştirme.
- **Veri Yükleme ve Görselleştirme:**
  - CSV formatında veri yükleme, pandas DataFrame ile görüntüleme ve Seaborn/Matplotlib ile grafik oluşturma.
- **Model Eğitimi ve Performans Analizi:**
  - Model eğitimi, test verisi oranı ayarı ve confusion matrix ile görselleştirme.
- **İletişim Formu:**
  - Kullanıcı mesaj ve fotoğraf yükleme özelliği.

## 🛠️ Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki araçların ve kütüphanelerin sisteminizde yüklü olması gerekmektedir:

- Python 3.7 veya üstü
- `streamlit`
- `pandas`
- `seaborn`
- `matplotlib`
- `scikit-learn`

## 📦 Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install streamlit pandas seaborn matplotlib scikit-learn
   ```

## 🖥️ Kullanım

1. `app.py` dosyasını çalıştırın:
   ```bash
   streamlit run app.py
   ```
2. Tarayıcınızda açılan sayfadan uygulamayı keşfedin.

## 📋 Örnek Sayfa Yapısı

- **Ana Sayfa:**
  - Markdown ile formatlanmış bilgiler ve müzik çalma butonları.
  - ![image](https://github.com/user-attachments/assets/96794dfa-9dfa-4815-81f3-2b40ede87e77)
  - ![image](https://github.com/user-attachments/assets/01b32f3c-c851-46e6-825e-af62bed3cb6b)

  - **Side Bar:**
  -  ![image](https://github.com/user-attachments/assets/dd21565a-68eb-4fe1-997d-855efca8dfee)
  - ![image](https://github.com/user-attachments/assets/4898ba7e-70fb-4d1c-954c-61874185dc85)

- **Model Seçimi:**
  - KNN, Random Forest, Decision Tree algoritmaları arasından seçim yapabilir ve parametreleri ayarlayabilirsiniz.
  - ![image](https://github.com/user-attachments/assets/0bcca6dd-0f72-46b4-93fc-68719548a91e)
  - ![image](https://github.com/user-attachments/assets/d32b4922-a9e5-43a4-9375-500a75b729f4)

- **Veri Görselleştirme:**
  - Yüklenen veri ile histogram, scatter plot gibi grafikler oluşturabilirsiniz.
  -![image](https://github.com/user-attachments/assets/df49dbc3-255a-486d-aea4-a362134a6f6f)






## 💡 Notlar

- Veri yüklemeden önce dosyanızın CSV formatında olduğundan emin olun.
- Uygulamada ayarladığınız model parametreleri doğru şekilde düzenlenmelidir.
- Çalıştırma sırasında oluşan hatalar için terminaldeki hata mesajlarını inceleyebilirsiniz.


Herhangi bir sorunuz veya katkınız için lütfen iletişime geçin! 😊
