
print("Merhaba! Sadece sana özel şifreleme yapmaya hazır mısın?")
key = input("Lütfen şifrelemede kullanmam için bir anahtar söyle: ")
plaintext= input("Şifrelemek istediğin metin nedir? ")


#plaintextin uzunluğunu py kendi algılayıp listeye dönüştürüor sonra diziye attım.

plaintext_dizi= list(plaintext) 
key_dizi= list(key)
cipher_text= []

key_mid_index= int(len(key_dizi)/2)   #anahtarın ortanca indisini tamsayı olarak buldum

alfabe = list("abcçdefgğhıijklmnoöprsştuüvyz") #alfabeyi tutan dizi oluşturdum

def alfabeden_indis_getir(x):
    for i in range (len(alfabe)) :
        if x==alfabe[i]:
            return i 
        
def guya():
    for i in range(len(plaintext_dizi)):
        m=((alfabe(key_mid_index)-alfabeden_indis_getir(plaintext_dizi[i]))+29)%29
        cipher_text.append(alfabe[m])

guya()

print("işte sana özel şifrelenmiş metnin:")
print(cipher_text)
