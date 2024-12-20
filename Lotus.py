import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Sayfa Konfigürasyonu
st.set_page_config(page_title="LotusAI", layout="wide")

# State: Sayfa Durumu
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

# CSS ile Tasarım
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f9f9f9;
            padding: 20px 10px;
        }
        .sidebar .logo {
            text-align: center;
            margin-bottom: 60px;
        }
        .sidebar .logo img {
            width: 80px;
            height: auto;
        }
        .sidebar .menu-item {
            font-size: 18px;
            padding: 12px 15px;
            color: #004a75;
            text-decoration: none;
            display: block;
            text-align: center;
            margin: 20px 0;
        }
        .sidebar .menu-item:hover {
            background-color: #d1e3f8;
            border-radius: 5px;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 20px;
            background-color: #004a75;
            color: white;
        }
        .header img {
            width: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Üst Bar
st.markdown(
    f"""
    <div class="header">
        <img src="https://lotusaibilisim.com/wp-content/uploads/2024/01/PNG-FORMAT.png" alt="Logo">
        <div>
            <label for="calendar" style="margin-right: 10px;">Bugün:</label>
            <span>{datetime.now().strftime('%Y-%m-%d')}</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.markdown(
    """
    <div class="logo">
        <img src="https://lotusaibilisim.com/wp-content/uploads/2024/01/PNG-FORMAT.png" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Butonları
if st.sidebar.button("Ana Sayfa"):
    st.session_state.current_page = "main"

if st.sidebar.button("Hakkımızda"):
    st.session_state.current_page = "about"

if st.sidebar.button("İletişim"):
    st.session_state.current_page = "contact"

# Sayfa İçerikleri
if st.session_state.current_page == "main":
       # "Müziği Başlat" butonunu ekleyerek müzik çalma
    if st.button('🎶 Müziği Başlat 🎶'):
        audio_file = "C:/Users/senao/OneDrive/Masaüstü/Stream_Ornek/chroma-dusk-269465.mp3"
        st.audio(audio_file, format='audio/mp3')
    st.title("Lotus AI: Veri Analitiği ve Modelleme Platformu 🤖📊")
    st.write(
        """

**Lotus AI**, veri analitiği ve makine öğrenimi süreçlerini bir arada sunarak, iş dünyası ve araştırma alanında en güçlü analiz ve modelleme çözümlerini sağlar. Kullanıcı dostu arayüzü ve güçlü altyapısı sayesinde, karmaşık veri setlerini hızlıca analiz edebilir, veriye dayalı kararlar alabilir ve etkili tahminler yapabilirsiniz. 🚀

**Lotus AI**'yi kullanarak, veri bilimi yolculuğunuzu daha verimli, daha etkili ve daha hızlı bir şekilde gerçekleştirebilirsiniz. Platform, sizi veri hazırlama aşamasından model sonuçlarının görselleştirilmesine kadar her adımda destekler. Süreç şu şekilde işler:

## 1. **Veri Yükleme ve Hazırlama** 📥
   - Kendi veri setinizi kolayca yükleyin ve analizler için hazırlayın. 📂
   - Verilerinizi hızlıca işleyin, eksik verileri tamamlayın ve gereksiz gürültüleri temizleyin. 🔄
   - **Lotus AI**, verilerinizi en uygun biçimde düzenleyerek analiz için hazır hale getirir.

## 2. **Model Seçimi ve Özelleştirme** 🔍
   - İhtiyacınıza uygun makine öğrenimi modelini seçmek hiç bu kadar kolay olmamıştı! 🎯
   - **Lotus AI**, farklı sektörlerden elde edilen verilerle eğitilmiş çok sayıda model sunar. Herhangi bir teknik bilgiye gerek kalmadan, istediğiniz modelle kolayca çalışmaya başlayabilirsiniz. 👩‍💻👨‍💻
   - İleri düzey kullanıcılar için model parametrelerini özelleştirebilir, optimizasyon işlemlerini daha derinlemesine yapabilirsiniz.

## 3. **Model Eğitimi ve Sonuçlar** 📈
   - Yüklediğiniz veri setiyle seçtiğiniz model üzerinde çalışarak, verinizin nasıl işlediğini ve hangi tahminleri yapabileceğini görün. 🤓
   - **Lotus AI**, verilerinizi hızlıca işler ve en iyi sonuçları alabilmeniz için gerekli eğitim süreçlerini otomatik olarak yürütür. 🔧
   - Eğitim sonuçlarıyla, modelinizin doğruluğunu ve güvenilirliğini analiz edebilirsiniz. ✅

## 4. **Sonuçların Görselleştirilmesi** 📊
   - **Lotus AI**, eğitilmiş modelin çıktısını sadece metin veya sayılarla sınırlı bırakmaz, aynı zamanda etkileyici görselleştirmelerle sunar. 🎨
   - Grafikler, tablolar ve interaktif araçlar ile modelinizin sonuçlarını daha anlaşılır ve etkili bir şekilde görselleştirin. 📉
   - Bu sayede, hem teknik hem de teknik olmayan kullanıcılar için veriye dayalı kararlar almak daha kolay hale gelir. 💡

---

**Lotus AI**, yalnızca teknik profesyonellerin değil, her seviyeden kullanıcıların veri analizini yapabileceği güçlü ve sezgisel bir platformdur. Şirketinizin veri bilimi ihtiyaçlarını karşılamak, en iyi makine öğrenimi çözümleriyle rekabet avantajı elde etmek ve karar alma süreçlerinizi hızlandırmak için ideal bir araçtır. 🌐✨

Veri analizi, modelleme ve görselleştirme süreçlerini **Lotus AI** ile hızlandırın, yenilikçi çözümlerle iş dünyasında fark yaratın! 🏆

        """
    )

    # Buton ile başka sayfaya geçiş
    if st.button("Test Sayfasına Git"):
        st.balloons()
        st.session_state.current_page = "test_page"

elif st.session_state.current_page == "about":
    st.info(
        """
        **Lotus AI**  
        Şirketimizin ana uzmanlık alanları arasında **Yapay Zeka (AI) algoritmaları**, **Veri İşleme (ETL)** ve **Kurumsal Yazılımlar** yer almaktadır.  
        AI alanında; makine öğrenmesi, optimizasyon teknikleri, esnek hesaplama yöntemleri, evrimsel hesaplama ve istatistiksel yöntemler ile ETL ve büyük veri operasyonları konuları yer almaktadır.  
        
        Kurucular **20 yıllık kurumsal yazılım geliştirme ve operasyon tecrübesine** sahiptir. Sahip olunan bu yetenekleri birleştirerek **AI çözümleri geliştirme sürecini kolaylaştırmak** amacıyla LotusAI ürünü geliştirme kanan alınmıştır.
        """
    )

elif st.session_state.current_page == "contact":
    st.header("Bize Ulaşın 📧")
    with st.form("contact_form"):
        user_message = st.text_area("Mesajınızı buraya yazın:", placeholder="Merhaba, size şunları sormak istiyorum...")
        uploaded_image = st.file_uploader("Fotoğraf yüklemek isterseniz buraya ekleyin:", type=["jpg", "png", "jpeg"])
        submitted = st.form_submit_button("Gönder")
        if submitted:
            if user_message:
                st.success("Mesajınız başarıyla iletilmiştir. En kısa zamanda size geri dönüş yapılacaktır. 🎉")
                st.info(f"Gönderilen Mesaj: {user_message}")
                if uploaded_image:
                    st.image(uploaded_image, caption="Yüklenen Fotoğraf", use_column_width=True)

elif st.session_state.current_page == "test_page":
    st.title("Uygulama Test Sayfası")
    
    # Model Seçimi - Unique key eklendi
    model_type = st.selectbox(
        "Problem Türünü Seçin",
        ["Sınıflandırma"],
        key="model_type_select"
    )
    
    # Sınıflandırma ise alt seçenekler - Unique key eklendi
    if model_type == "Sınıflandırma":
        classifier_type = st.selectbox(
            "Sınıflandırma Algoritmasını Seçin",
            ["KNN", "RandomForest", "DecisionTree"],
            key="classifier_type_select"
        )
        st.write(f"Seçilen Sınıflandırma Algoritması: {classifier_type}")

    # Veri Seti Yükleme
    uploaded_file = st.file_uploader("Veri Seti Yükle (CSV formatında):", type=["csv"], key="data_upload")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Veri seti başarıyla yüklendi!")
        st.subheader("Veri Setinin İlk 5 Satırı:")
        st.write(df.head())
        st.subheader("Veri Seti Özeti:")
        st.write(df.describe())
      
        # Veri Seti Görselleştirme - Unique key eklendi
        if st.checkbox("Veri Setini Görselleştir", key="visualize_checkbox"):
            selected_column = st.selectbox("Histogram için bir sütun seçin", df.columns, key="histogram_column_select")
            plt.figure(figsize=(10, 6))
            sns.histplot(df[selected_column], kde=True, bins=20)
            st.pyplot(plt)
        
        if model_type == "Sınıflandırma":
            if classifier_type == "KNN":
                # KNN için özellik seçimi - Unique key eklendi
                feature_columns = st.multiselect("Modelde kullanılacak özellik sütunlarını seçin", 
                                               options=df.columns, 
                                               key="knn_feature_select")
                target_column = st.selectbox("Hedef sütunu seçin", 
                                           options=df.columns, 
                                           key="knn_target_select")
                
                if feature_columns and target_column:
                    X = df[feature_columns]
                    y = df[target_column]
                    test_size = st.slider("Test Veri Oranı:", 0.1, 0.5, 0.2, key="knn_test_size")
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

                    k_value = st.slider("K Değerini Seçin:", 1, 20, 5, key="knn_k_value")
                    knn = KNeighborsClassifier(n_neighbors=k_value)
                    knn.fit(X_train, y_train)
                    y_pred = knn.predict(X_test)

                    st.subheader("Model Performansı")
                    cm = confusion_matrix(y_test, y_pred)
                    plt.figure(figsize=(8, 6))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
                    st.pyplot(plt)
                    st.write(f"Model Doğruluk Skoru: {knn.score(X_test, y_test):.2f}")

            elif classifier_type == "RandomForest":
                # Random Forest için özellik seçimi - Unique key eklendi
                feature_columns = st.multiselect("Modelde kullanılacak özellik sütunlarını seçin", 
                                               options=df.columns, 
                                               key="rf_feature_select")
                target_column = st.selectbox("Hedef sütunu seçin", 
                                           options=df.columns, 
                                           key="rf_target_select")
                
                if feature_columns and target_column:
                    X = df[feature_columns]
                    y = df[target_column]
                    
                    bins = st.slider("Sürekli hedefi sınıflandırmak için aralıkları belirleyin", 
                                   min_value=2, max_value=10, value=3, 
                                   key="rf_bins")
                    y = pd.cut(y, bins=bins, labels=[f"Class_{i}" for i in range(bins)])
                    
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                    
                    n_estimators = st.slider("n_estimators (Ağaç sayısı)", 
                                           min_value=10, max_value=200, value=100, step=10, 
                                           key="rf_n_estimators")
                    max_depth = st.slider("max_depth (Ağaç derinliği)", 
                                        min_value=1, max_value=50, value=10, step=1, 
                                        key="rf_max_depth")
                    
                    rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
                    rf.fit(X_train, y_train)
                    y_pred = rf.predict(X_test)
                    
                    cm = confusion_matrix(y_test, y_pred)
                    st.subheader("Confusion Matrix")
                    fig, ax = plt.subplots()
                    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
                    st.pyplot(fig)
                    
                    accuracy = rf.score(X_test, y_test)
                    st.write(f"Model Doğruluk Skoru: {accuracy:.2f}")

            elif classifier_type == "DecisionTree":
                # Decision Tree için özellik seçimi - Unique key eklendi
                feature_columns = st.multiselect("Modelde kullanılacak özellik sütunlarını seçin", 
                                               options=df.columns[:-1], 
                                               key="dt_feature_select")
                target_column = st.selectbox("Hedef sütunu seçin", 
                                           options=df.columns, 
                                           key="dt_target_select")

                if feature_columns and target_column:
                    X = df[feature_columns]
                    y = df[target_column]
                    
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                    
                    max_depth = st.slider("max_depth (Ağaç derinliği)", 
                                        min_value=1, max_value=50, value=10, step=1, 
                                        key="dt_max_depth")
                    
                    dt = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
                    dt.fit(X_train, y_train)
                    y_pred = dt.predict(X_test)
                    
                    cm = confusion_matrix(y_test, y_pred)
                    st.subheader("Confusion Matrix")
                    fig, ax = plt.subplots()
                    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
                    st.pyplot(fig)
                    
                    st.write(f"Model Doğruluk Skoru: {dt.score(X_test, y_test):.2f}")
    else:
        st.warning("Lütfen bir veri seti yükleyin!")

# Footer
st.markdown(
    """
    <footer style="text-align:center; padding: 20px 0; background-color:#f9f9f9;">
        <p>LotusAI - Tüm Hakları Saklıdır © 2024</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
