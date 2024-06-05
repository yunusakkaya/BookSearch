   # BookSearch
   
   BookSearch, kullanıcıların kitapları arayabileceği, beğenebileceği ve beğendikleri kitaplara göre yeni öneriler alabilecekleri bir uygulamadır. Django ve React kullanılarak geliştirilmiştir.
   
   ## Özellikler
   
   - **Kitap Arama:** Kullanıcılar kitap başlığı, yazar, fiyat aralığı ve türe göre arama yapabilirler.
   - **Kitap Beğenme:** Kullanıcılar beğendikleri kitapları işaretleyebilir.
   - **Öneriler:** Beğenilen kitaplara göre kullanıcıya aynı sayfada yeni kitap önerileri sunulur.
   
   ## Kurulum
   
   ### Gereksinimler
   
   - Python 3.8+
   - Node.js 12+
   
   ### Adımlar
   
   #### Backend Kurulumu
   
   1. Proje dizininde bir Python sanal ortamı oluşturun ve etkinleştirin:
      ```bash
      python -m venv env
      source env/bin/activate  # MacOS/Linux
      .\env\Scripts\activate  # Windows    
      
   Gerekli kütüphaneleri yükleyin

       pip install -r requirements.txt

   Veritabanı migrasyonlarını yapın

        python manage.py makemigrations
        python manage.py migrate
                                 
   Veri setini içe aktarın

    python manage.py import_books path/to/your/csvfile.csv

   Frontend Kurulumu

    cd booksearch-frontend

    npm install

    npm start

## Kullanım
#### Web tarayıcınızı açın ve http://127.0.0.1:3000 adresine gidin.
#### Arama çubuğunu kullanarak kitap araması yapın.
#### Beğendiğiniz kitapları işaretlemek için beğeni butonuna tıklayın.
#### Sayfanın altında beğendiğiniz kitaplara göre önerilen kitapları görün.

### Katkıda Bulunanlar
#### Yunus Akkaya - Proje Sahibi

















