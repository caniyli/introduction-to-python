'''
Hw2: write a program that includes information about the grades of students in a school
-Keep these students' grades in a list
-Keep students' names in a list
-Create a dictionary named info and put all the information of students in a dictionary.
-Sort and list the students' grades here in descending order and congratulate the student with the highest score
'''

stNames = []
stGrades = []

#Ogrencilerin isim ve soyisimleri kullanıcıdan alındı
for i in range(5):
    name = input(f"{i+1}. ogrencının adını ve soyadını bir boşluk bırakarak giriniz")
    stNames.append(name)

#Ögrencilerin vize final  ve ödev notu kullanıcıdan alındı
for i in range(5):
    grade= input(f"{stNames[i]} isimli ogrencinin vize final ve ödev notlarını sırasıyla arasına virgül koyarak giriniz")
    stGrades.append(grade)

#Alınan bilgiler dictionary olarak düzenlendi ve ekrana yazdırıldı
info = {}
for i in range(5):
    info.update({stNames[i]:stGrades[i]})
print(info)

#Öğrencilerin not ortalaması alındı
for i in range(5):
    av = (int(info[stNames[i]].split(",")[0]) + int(info[stNames[i]].split(",")[1]) + int(info[stNames[i]].split(",")[2])) / 3
    info.update({stNames[i]:av})

#Büyükten küçüğe sıralanarak en yüksek alan öğrenci ekrana yazdırıldı
newinfo = sorted(info.items(), key=lambda x: x[1], reverse=True)
print(f"{newinfo[0][0]} İsimli öğrenci {newinfo[0][1]} ortalama ile en yuksek ortalamaya sahip")





