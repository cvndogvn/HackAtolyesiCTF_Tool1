import hashlib
# Coded by @cvndogvn
flag = 0
counter = 0

pHash = input("Lütfen MD5'i giriniz : ")
wordlist = input("Dosya ismini giriniz : ")

try:
    passFile = open(wordlist, "r")
except:
    print('Dosya bulunamadı!')
    quit()

for word in passFile:

    encWord = word.encode('utf-8')
    digest = hashlib.md5(encWord.strip()).hexdigest()
    counter += 1

    if digest == pHash:
        print('Şifre bulundu !!!')
        print("Şifreli " + pHash + " MD5'in çözülmüş hali : " + word)
        print("Dosyada " + str(counter) + " şifreyi analiz yaptık.")
        flag = 1
        break
if flag == 0:
    print('Dosyanın içinde şifreyi bulamadım :(')