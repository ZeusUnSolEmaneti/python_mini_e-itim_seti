"""
    Döngüler için direkt uygulama içinde bahsedersek daha iyi olacaktır
"""

for i in range(0, 5):  # range(0,5) yani i sayısı 0 dan 5'e(5 dahil değil)
    print(i)  # olan sayılardır
    # for i in range(0, 5) 'in anlamı i bu aralıkta olsun
    # ve sen onları birer birer arttırarak yazdır ekrana
i=0 #ilk olarak i diye bir değişken tanımlıyoruz
while i<10: #sonrasında while döngümüz içinde kodu yazıyoruz i değişkeni 10'a gelene kadar i artıcaktır.
  i+=1
  print(i)

"""
Output:
0
1
2
3
4
Process finished with exit code 0
"""
