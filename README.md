# KOMPOZİT MALZEME ÜRETİMİNDE KULLANILAN PARALEL FIRINLARIN ÇİZELGELENMESİ PROBLEMİ 

Kod Phyton ortamında geliştirilmiştir. Geliştirilen kod temel olarak işleri batch'lere batch'leri de fırınlara atamaktadır. 

Kodun işleyişinin detayı şöyledir:

1-	Fırınların başlangıç zamanı 0 olarak atanmıştır. Problemde kullanılan ve bölüm.2’de belirtilen diğer parametreler tanıtılmıştır.

2-	9 adet boş batch array’i tanımlanmış ve iş-batch uyumluluğuna göre işler arasından  uyumluluk kısıtı çerçevesinde rastgele seçilenler işler batch’lere atanmıştır. Bir kez ataması yapılan iş işler grubundan çıkarılarak her işin sadece ve mutlaka bir batch’e atanması sağlanmıştır.
3-	Sonrasında her batch için o batch’e atanan işler arasından en erken due date’e sahip olan işin due date’inden batch’in işlem zamanını çıkarıyoruz. Bu sayede her batch’in işlerin gecikmemesi adına başlaması gereken maximum zamanı (t) bulmuş oluyoruz. Başka bir deyişle her batch’in başlaması gereken en geç zamanı elde etmiş oluyoruz.
4-	Daha sonra batch ve fırın ataması yapılması gereken kısma gelmiş oluyoruz. Bu aşamada elimizde tüm batch’lerin başlaması gereken en geç zaman bilgisi olmuş oluyor. Bu bilgiye göre tüm batch’i başlaması gereken zamana göre küçükten büyüğe sıralıyoruz ve en erken başlaması gerekeni ilk fırına bir sonrakini ikinci fırına sonrakini üçüncü fırına atıyoruz. Sonrasında atama yapılan fırınlardan minumum t’ye gelene sıradaki batch’i atıyoruz. Sonrasında tekrar minimum t’ye ulaşan fırın kontrol ediliyor ve sıradaki batch ona atanıyor. Aynı döngünün tüm batch’ler için tekrarlanması ile tüm batch’lerin fırınlara atanması tamamlanıyor.
