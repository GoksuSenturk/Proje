# KOMPOZİT MALZEME ÜRETİMİNDE KULLANILAN PARALEL FIRINLARIN ÇİZELGELENMESİ PROBLEMİ 

Kod Phyton ortamında geliştirilmiştir. Geliştirilen kod temel olarak işleri batch'lere batch'leri de fırınlara atamaktadır. 

Kodun işleyişinin detayı şöyledir:

1-	Fırınların başlangıç zamanı 0 olarak atanmıştır. Problemde kullanılan ve bölüm.2’de belirtilen diğer parametreler tanıtılmıştır.

2-	9 adet boş batch array’i tanımlanmış ve iş-batch uyumluluğuna göre işler arasından  uyumluluk kısıtı çerçevesinde rastgele seçilenler işler batch’lere atanmıştır. Bir kez ataması yapılan iş işler grubundan çıkarılarak her işin sadece ve mutlaka bir batch’e atanması sağlanmıştır.

3-	Sonrasında her batch için o batch’e atanan işler arasından en erken due date’e sahip olan işin due date’inden batch’in işlem zamanını çıkarıyoruz. Bu sayede her batch’in işlerin gecikmemesi adına başlaması gereken maximum zamanı (t) bulmuş oluyoruz. Başka bir deyişle her batch’in başlaması gereken en geç zamanı elde etmiş oluyoruz.

4-	Daha sonra batch ve fırın ataması yapılması gereken kısma gelmiş oluyoruz. Bu aşamada elimizde tüm batch’lerin başlaması gereken en geç zaman bilgisi olmuş oluyor. Bu bilgiye göre tüm batch’i başlaması gereken zamana göre küçükten büyüğe sıralıyoruz ve en erken başlaması gerekeni ilk fırına bir sonrakini ikinci fırına sonrakini üçüncü fırına atıyoruz. Sonrasında atama yapılan fırınlardan minumum t’ye gelene sıradaki batch’i atıyoruz. Sonrasında tekrar minimum t’ye ulaşan fırın kontrol ediliyor ve sıradaki batch ona atanıyor. Aynı döngünün tüm batch’ler için tekrarlanması ile tüm batch’lerin fırınlara atanması tamamlanıyor.

Kodda kullanılan değişkenler ve açıklamaları:
t[t1,t2,t3] =fırınların kaçıncı dakikada olduğunu göstermektedir. 3 elemanlıdır çünkü problemimizde 3 fırın vardır.

tc= işerin kullanacağı termocouple sayısıdır. Bu problem örneğinde işlerin hepsi için aynı ve 1 olduğu için 1'e eşitlenmiştir. Projenin devamında bir array için de her iş için ayrı ayrı tanımlanabilir.

vp = işerin kullanacağı vakumport sayısıdır. Bu problem örneğinde işlerin hepsi için aynı ve 2 olduğu için 2'ye eşitlenmiştir. Projenin devamında bir array için de her iş için ayrı ayrı tanımlanabilir.

a= işerin kullanacağı alan miktarıdır. Bu problem örneğinde işlerin hepsi için aynı ve 3 olduğu için 3'e eşitlenmiştir. Projenin devamında bir array için de her iş için ayrı ayrı tanımlanabilir.

tcf= fırınların kullanacağı termocouple sayısıdır. Bu problem örneğinde fırınların hepsi için aynı ve 15 olduğu için 15'e eşitlenmiştir. Projenin devamında bir array için de her fırın için ayrı ayrı tanımlanabilir.

vpf= fırınların kullanacağı vakumport sayısıdır. Bu problem örneğinde fırınların hepsi için aynı ve 20 olduğu için 20'ye eşitlenmiştir. Projenin devamında bir array için de her fırın için ayrı ayrı tanımlanabilir.

af = fırınların sahip olduğu toplam alandır. Bu problem örneğinde fırınların hepsi için aynı ve 25 olduğu için 25'e eşitlenmiştir. Projenin devamında bir array için de her fırın için ayrı ayrı tanımlanabilir.

b[] = her batch için sonrasında işleri atamak üzere başta boş bir array tanımlanmıştır.

job_batch = iş ve batch'lerin uyumluluk matrisidir.

last start = batch'lerin başlaması gereken en geç zamandır.

minfirintime = fırınların hangisinin daha erken boş olduğunu anlamamızı sağlayan değişkendir.

pbatch= batch'lerin işlem süreleridir.
