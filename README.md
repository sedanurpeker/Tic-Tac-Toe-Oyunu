# Tic-Tac-Toe-Oyunu
 Bu repository, yapay zeka destekli bir Tic Tac Toe oyununu içermektedir. Oyun, Q-learning algoritması kullanılarak bir ajan tarafından öğrenilmektedir. Kullanıcı, ajan ile veya bilgisayarın kendi kendine oynamasını sağlayarak eğitimi geliştirebilir.

## 📌 İçerik
### 1. Agent.py
- **Ajan sınıfını içerir** ve oyun tahtasını analiz ederek en iyi hamleyi belirler.
- **Q-learning algoritmasını uygular** ve eğitim sonucunda öğrendiği bilgileri saklar.

**Öğrenme ve oynama fonksiyonları içerir:**
-- x_rastgele_egit(): X oyuncusu olarak rastgele hamlelerle eğitim yapar.
-- o_rastgele_egit(): O oyuncusu olarak rastgele hamlelerle eğitim yapar.
-- insan_ile_oyna(): Ajanın insan oyuncuya karşı oynamasını sağlar.
-- bilgisayar_ile_oyna(): İki ajanın birbirine karşı oynamasını sağlar.

### 2. TicTacToe.py
**Tic Tac Toe oyununun mekaniklerini içerir.**
**Hamlelerin kontrolü ve kazananın belirlenmesi işlevlerini barındırır.**
**Tahtanın güncellenmesi ve görselleştirilmesini sağlar.**

 ### 3. run.py
**Oyunu başlatan dosyadır.**
İlgili ajanı çağırarak oyunun başlatılmasını sağlar.

### Oynama Seçenekleri

- **Ajanı eğitmek için:** ajan.x_rastgele_egit() veya ajan.o_rastgele_egit() çağrılabilir.
- **İnsan ile oynama:** ajan.insan_ile_oyna() çalıştırılarak kullanıcı ajana karşı oynayabilir.
- **Bilgisayarın kendi kendine oynaması:** ajan.bilgisayar_ile_oyna() fonksiyonu ile ajanların birbirine karşı oynaması sağlanabilir.
