import random

def acakkata(): # list kata
    katakata = ['nyamuk','lalat','udang','kuda','ikan','kelinci','katak','ular','burung']
    i = random.choice(range(len(katakata)))
    return i,katakata[i]


skore = []
def startGame():
    answer=''
    randomWord = acakkata()[1]
    encryptWord = ''.join(random.sample(randomWord,len(randomWord)))
    limit = 5
    print('Kata acak:'+encryptWord)
    print('\n')
    while answer != randomWord:
        answer = input('Jawaban:')
        if answer == 'quit':
            quit()
        if answer == randomWord:
            skore.append(1)
            hasil = len(skore)
            print('JAWABAN ANDA BENAR, POINT ANDA = '+str(hasil))
        elif answer =='':
            print('ANDA BELUM MEMASUKKAN JAWABAN!')
        else:
            limit-=1
            print('JAWABAN ANDA SALAH!')
            if limit != 0:
                print('Kesempatan Anda Tinggal '+str(limit)+' kali lagi')
        if limit == 0:
            print('Game Berakhir')
            quit()
            
print('Anda Diberi Kesempatan sebanyak 5 kali')
print('Jika Kesempatan Habis game akan selesai')
print("Ketik 'quit' untuk keluar")
while True:
    startGame()


