İlacTakipSistemi
Bu dosya Microsoft SQL ortamında yazılmıştır ve amacı bir kuruluşun veya veri analistinin ülke çapındaki eczaneler hakkında genel verilere erişip bunları kaydetmesini sağlamaktır.

İşlem adımları aşağıdaki gibi düzenlenmiştir:

1. **BACPAC Dosyasını İçe Aktarma**:
- Bir BACPAC dosyasını Microsoft SQL Server'a aktarmak için SQL Server Management Studio'yu (SSMS) açın.
- `Veritabanı` menüsünden `Veritabanına Bağlan` öğesini seçin.
- `Veritabanı` sekmesine gidin ve ardından `BACPAC Dosya Yedeklemesi` öğesini seçerek dosyayı içe aktarın.

2. **Python Dosyasını Çalıştırma**:
- Python dosyasını açın.
- Python dosyasında, `sunucu` bölümüne bağlandığınız sunucunun adını yazın. Bu genellikle `yerel` veya bilgisayarınızın adıdır. Örneğin:

server = '' ***** " # genellikle bilgisayar adı

3. **Veritabanına Bağlanma ve Sorgulama**:
- Python dosyasını çalıştırın ve bağlantı kurulduktan sonra tabloları sorgulayabilirsiniz.
- SQL komutları yazın ve SQL Server'da veritabanına erişerek verileri analiz edin.

Bu adımları izleyerek veritabanını içe aktarabilir, Python kullanarak bir bağlantı kurabilir ve sorgu işlemleri gerçekleştirebilirsiniz.
