#######################################
#                                     #
#         Recipe Application          #
#                                     #
#######################################

class Yemekpisir:
    def yuksek_ates(self):
        print("Yüksek ateşte kaynayana kadar bekleyin")
    def kısık_ates(self):
        print("Kapağını kapatıp kısık ateşte yarım saat pişmesini bekleyin")
    def yag_ekle(self):
        print("Yemeğe yağ ekleyin")
    def baharat_ekle(self):
        print("Yemeğe baharatları ekleyin")
    def salca(self):
        print("Yemeğe salça ekleyin")
    def sebze_ekle(self):
        print("Domates ve soğanları küçük küçük dilimleyip tencereye ekleyin")

class Tazefasulye(Yemekpisir):
    def fasulye_ekle(self):
        print("Fasülyeleri tencereye koyun")

class Etsote(Yemekpisir):
    def et_ekle(self):
        print("Etleri tencereye koyun")
    def bekle(self):
        print("Etlerin rengi değişene kadar bekleyin")

class Patatesyemegi(Yemekpisir):
    def patetes_ekle(self):
        print("Patatesleri tencereye koyun")


print("1-Taze fasulye yemeği\n2-Et sote yemegi\n3-Patates yemeği")
secim=input("Tarifini istediğiniz yemegi seçin")

if secim == '1':
    print("1")
    yemek = Tazefasulye()
    yemek.sebze_ekle()
    yemek.salca()
    yemek.yag_ekle()
    yemek.fasulye_ekle()
    yemek.baharat_ekle()
    yemek.yuksek_ates()
    yemek.kısık_ates()

elif secim == '2':
    yemek = Etsote()
    yemek.yag_ekle()
    yemek.yuksek_ates()
    yemek.et_ekle()
    yemek.bekle()
    yemek.sebze_ekle()
    yemek.baharat_ekle()
    yemek.kısık_ates()

elif secim == '3':
    yemek = Patatesyemegi()
    yemek.sebze_ekle()
    yemek.salca()
    yemek.yag_ekle()
    yemek.patetes_ekle()
    yemek.baharat_ekle()
    yemek.yuksek_ates()
    yemek.kısık_ates()

else:
    print("Hatalı seçim yaptınız")



