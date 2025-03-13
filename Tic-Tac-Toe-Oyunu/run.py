from TicTacToe import TicTacToe
from Agent import Ajan

oyun = TicTacToe()
ajan = Ajan(oyun, 'X',indirim_fak = 0.6, bolum = 100000)

#ajan.x_rastgele_egit()
#ajan.bilgisayar_ile_oyna()
ajan.insan_ile_oyna()
