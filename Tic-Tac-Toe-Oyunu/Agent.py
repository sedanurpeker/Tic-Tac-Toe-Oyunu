import numpy as np
import random
import pickle

class Ajan:
    def __init__(self, oyun, oyuncu='X', bolum=100000, epsilon=0.9, indirim_fak=0.6, eps_azaltma_fak=0.01):
        self.oyun = oyun
        self.oyuncu = oyuncu
        self.beyin = dict()
        self.bolum = bolum
        self.epsilon = epsilon
        self.indirim_fak = indirim_fak
        self.sonuclar = {'X': 0, 'O': 0, 'D': 0}
        self.eps_azaltma_fak = eps_azaltma_fak

    def beyni_kaydet(self, oyuncu):
        with open('beyin' + oyuncu, 'wb') as beyin_dosyasi:
            pickle.dump(self.beyin, beyin_dosyasi)

    def beyin_yukle(self, oyuncu):
        try:
            with open('beyin' + oyuncu, 'rb') as beyin_dosyasi:
                self.beyin = pickle.load(beyin_dosyasi)
        except:
            print('Kayitli gecmis bulunmamaktadir. Bu yuzden once ajani egitmelisiniz. Bundan dolayi ajan rastgele oynayacaktir.')

    def odul(self, oyuncu, move_history, sonuc):
        _odul = 0
        if oyuncu == 1:
            if sonuc == 1:
                _odul = 1
                self.sonuclar['X'] += 1
            elif sonuc == -1:
                _odul = -1
                self.sonuclar['O'] += 1
        elif oyuncu == -1:
            if sonuc == 1:
                _odul = -1
                self.sonuclar['X'] += 1
            elif sonuc == -1:
                _odul = 1
                self.sonuclar['O'] += 1

        if sonuc == -2:
            self.sonuclar['D'] += 1
        move_history.reverse()
        for durum, aksiyon in move_history:
            self.beyin[durum, aksiyon] = self.beyin.get((durum, aksiyon), 0.0) + _odul
            _odul *= self.indirim_fak

    def beyni_kullan(self):
        olasi_aksiyonlar = self.oyun.mevcut_pozisyon_al()
        max_qdegeri = -1000
        iyi_aksiyon = olasi_aksiyonlar[0]
        for aksiyon in olasi_aksiyonlar:
            qdegeri = self.beyin.get((self.oyun.mevcut_tuple_al(), aksiyon), 0.0)
            if qdegeri > max_qdegeri:
                iyi_aksiyon = aksiyon
                max_qdegeri = qdegeri
            elif qdegeri == max_qdegeri and random.random() < 0.5:
                iyi_aksiyon = aksiyon
                max_qdegeri = qdegeri
            elif len(olasi_aksiyonlar) == 9:
                iyi_aksiyon = random.choice(olasi_aksiyonlar)
                break
        return iyi_aksiyon

    def x_rastgele_egit(self):
        for _ in range(self.bolum):
            if _ % 1000 == 0:
                print('Bolum: ' + str(_))
                self.epsilon -= self.eps_azaltma_fak
            move_history = []
            while True:
                if sum(self.oyun.mevcut_oyunu_al() == 1) == 0 or random.random() < self.epsilon:
                    mevcut_aksiyonlar = self.oyun.mevcut_pozisyon_al()
                    eylem_x = random.choice(mevcut_aksiyonlar)
                    move_history.append([self.oyun.mevcut_tuple_al(), eylem_x])
                    self.oyun.hareket_et(eylem_x)
                else:
                    eylem_x = self.beyni_kullan()
                    move_history.append([self.oyun.mevcut_tuple_al(), eylem_x])
                    self.oyun.hareket_et(eylem_x)
                if self.oyun.kazandi_mi():
                    self.odul(1, move_history, self.oyun.kazanan)
                    break
                mevcut_aksiyonlar = self.oyun.mevcut_pozisyon_al()
                eylem_o = random.choice(mevcut_aksiyonlar)
                self.oyun.hareket_et(eylem_o)
                if self.oyun.kazandi_mi():
                    self.odul(1, move_history, self.oyun.kazanan)
                    break
        self.beyni_kaydet('X')
        print('Egitim Tamamlandi.')
        print('Sonuclar:')
        print(self.sonuclar)

    def o_rastgele_egit(self):
        for _ in range(self.bolum):
            if _ % 1000 == 0:
                print('Bolum: ' + str(_))
                self.epsilon -= self.eps_azaltma_fak
            move_history = []
            while True:
                mevcut_aksiyonlar = self.oyun.mevcut_pozisyon_al()
                eylem_x = random.choice(mevcut_aksiyonlar)
                self.oyun.hareket_et(eylem_x)
                if self.oyun.kazandi_mi():
                    self.odul(-1, move_history, self.oyun.kazanan)
                    break
                if random.random() < self.epsilon:
                    mevcut_aksiyonlar = self.oyun.mevcut_pozisyon_al()
                    eylem_o = random.choice(mevcut_aksiyonlar)
                    move_history.append([self.oyun.mevcut_tuple_al(), eylem_o])
                    self.oyun.hareket_et(eylem_o)
                else:
                    eylem_o = self.beyni_kullan()
                    move_history.append([self.oyun.mevcut_tuple_al(), eylem_o])
                    self.oyun.hareket_et(eylem_o)
                if self.oyun.kazandi_mi():
                    self.odul(-1, move_history, self.oyun.kazanan)
                    break
        self.beyni_kaydet('O')
        print('Egitim tamamlandi.')
        print('Sonuclar:')
        print(self.sonuclar)

    def insan_ile_oyna(self):
        self.beyin_yukle(self.oyuncu)
        emir = 1 if self.oyuncu == 'X' else -1
        while True:
            if emir == 1:
                self.oyun.hareket_et(self.beyni_kullan())
                self.oyun.mevcut_oyunu_ciz()
                emir *= -1
                if self.oyun.kazandi_mi(isgame=True):
                    break
            else:
                eylem_o = int(input('Hangi kareye oynayacaksiniz?'))
                self.oyun.hareket_et(eylem_o - 1)
                self.oyun.mevcut_oyunu_ciz()
                emir *= -1
                if self.oyun.kazandi_mi(isgame=True):
                    break
    def bilgisayar_ile_oyna(self):
        self.beyin_yukle('X')
        self.beyin_yukle('O')
        emir = 1
        while True:
            if emir == 1:
                self.oyun.hareket_et(self.beyni_kullan())
                self.oyun.mevcut_oyunu_ciz()
                if self.oyun.kazandi_mi(isgame=True):
                    break
            else:
                self.oyun.hareket_et(self.beyni_kullan())
                self.oyun.mevcut_oyunu_ciz()
                if self.oyun.kazandi_mi(isgame=True):
                    break
            emir *=-1