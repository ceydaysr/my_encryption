

alfabe = list("abcçdefgğhıijklmnoöprsştuüvyz") #alfabeyi tutan dizi oluşturdum

'''-----------------------FONKSİYONLAR-------------------------------------'''

def tum_bosluklari_kaldir_join(ayiklanacak_plaintext):
    return "".join(char for char in ayiklanacak_plaintext if not char.isspace())


def alfabeden_indis_getir(x):         #x'in alfabedeki  yerini döndürüyor
    for i in range (len(alfabe)) : 
        if x==alfabe[i]:
            return i 

def guya():
    mid_of_key= key_dizi[key_mid_index]    #ortanca harfi tutuyorum HARF SAYI DEĞİL!!!!!!
    for i in range(len(plaintext_dizi)):   #plain text boyutu kadar cipher text oluşturacak
        m=((alfabeden_indis_getir(mid_of_key)-alfabeden_indis_getir(plaintext_dizi[i]))+29)%29 #şifreleme için oluşturduğum kısım ana işlem burası
        ciphertext.append(alfabe[m])  #şifrelenmiş harfi bu listeye atıyorum 

'''-------------------------------------------------------------------------------'''

print("Merhaba! Sadece sana özel şifreleme yapmaya hazır mısın?")
print("Sayı ve özel karakter kullanma lütfen")
key = input("Lütfen şifrelemede kullanmam için bir anahtar söyle: ")
plaintext= input("Şifrelemek istediğin metin nedir? ")

plaintext_1= tum_bosluklari_kaldir_join(list(plaintext)) #boşluksuz plaintext aldım atadım

key_1= tum_bosluklari_kaldir_join(list(key))             #boşluksuz key aldım atadım

ciphertext= [] #ciphertext için içi boş dizi oluşturdum

plaintext_dizi=plaintext_1.lower()   #plaintexteki büyük harfleri küçülttüm.

key_dizi=key_1.lower()             #keydeki büyük harfleri küçülttüm.

key_mid_index= int(len(key_dizi)/2)   #anahtarın ortanca indisini tamsayı olarak buldum

guya()

print("işte sana özel şifrelenmiş metnin:")
print("".join(ciphertext))
