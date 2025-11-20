
print("Merhaba! Sadece sana özel şifreleme yapmaya hazır mısın?")
key = input("Lütfen şifrelemede kullanmam için bir anahtar söyle: ")
plaintext= input("Şifrelemek istediğin metin nedir? ")


#plaintextin uzunluğunu py kendi algılayıp listeye dönüştürüor sonra diziye attım.

plaintext_dizi= list(plaintext) 
key_dizi= list(key)
ciphertext= [] #ciphertext için içi boş dizi oluşturdum
alfabe = list("abcçdefgğhıijklmnoöprsştuüvyz") #alfabeyi tutan dizi oluşturdum

key_mid_index= int(len(key_dizi)/2)   #anahtarın ortanca indisini tamsayı olarak buldum


def alfabeden_indis_getir(x):         #x'in alfabedeki  yerini döndürüyor
    for i in range (len(alfabe)) :
        if x==alfabe[i]:
            return i 
        
def guya():
    mid_of_key= key_dizi[key_mid_index]    #ortanca harfi tutuyorum HARF
    for i in range(len(plaintext_dizi)):   #plain text boyutu kadar cipher text oluşturacak
        m=((alfabeden_indis_getir(mid_of_key)-alfabeden_indis_getir(plaintext_dizi[i]))+29)%29 #şifreleme için oluşturduğum kısım ana işlem burası
        ciphertext.append(alfabe[m])  #şifrelenmiş harfi bu listeye atıyorum 

guya()

print("işte sana özel şifrelenmiş metnin:")
print("".join(ciphertext))
