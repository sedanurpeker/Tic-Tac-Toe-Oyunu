import numpy as np

class TicTacToe:
    def __init__(self):
        self.mevcut_durum = np.zeros(9, dtype=np.int8)
        self.kazanan = None
        self.oyuncu = 1

    def mevcut_oyunu_ciz(self):
        mevcut_durum = ['X' if x == 1 else 'O' if x == -1 else '--' for x in self.mevcut_durum]
        print(f'{mevcut_durum[0]:^5} {mevcut_durum[1]:^5} {mevcut_durum[2]:^5}')
        print(f'{mevcut_durum[3]:^5} {mevcut_durum[4]:^5} {mevcut_durum[5]:^5}')
        print(f'{mevcut_durum[6]:^5} {mevcut_durum[7]:^5} {mevcut_durum[8]:^5}')
        print('_' * 25)

    def mevcut_oyunu_al(self):
        return self.mevcut_durum

    def mevcut_tuple_al(self):
        return tuple(self.mevcut_durum)

    def mevcut_pozisyon_al(self):
        return (np.argwhere(self.mevcut_durum == 0).ravel())

    def oyunu_sifirla(self):
        self.mevcut_durum = np.zeros(9, dtype=np.int8)
        self.oyuncu = 1

    def oyuncu_al(self):
        return self.oyuncu

    def hareket_et(self, aksiyon):  # player is 1 for X, player is -1 for O
        if aksiyon in self.mevcut_pozisyon_al():
            self.mevcut_durum[aksiyon] = self.oyuncu
            # self.draw_current_game()
            self.oyuncu *= -1
        else:
            print('Mevcut degil.')

    def _hareket_et(self, _mevcut_durum, aksiyon):
        _mevcut_durum[aksiyon] = self.oyuncu
        return _mevcut_durum

    def sonraki_durum(self):
        durum = []
        _mevcut_durum = self.mevcut_durum
        _uygun_hareketler = self.mevcut_pozisyon_al()
        for move in _uygun_hareketler:
            durum.append(self._hareket_et(_mevcut_durum=_mevcut_durum, aksiyon=move))
        return durum

    def kazandi_mi(self, isgame=False):
        kazanan_koordinatlar = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                       [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                       [0, 4, 8], [2, 4, 6]])
        for koordinat in kazanan_koordinatlar:
            toplam = sum(self.mevcut_durum[koordinat])
            if toplam == 3:
                if isgame:
                    print('KAZANAN: X')
                self.kazanan = 1
                self.oyunu_sifirla()
                return 1
            elif toplam == -3:
                if isgame:
                    print('KAZANAN: O')
                self.kazanan = -1
                self.oyunu_sifirla()
                return -1
            elif sum(self.mevcut_durum == 1) == 5:
                if isgame:
                    print('BERABERE')
                self.kazanan = -2
                self.oyunu_sifirla()
                return -2
        return False