print("İki nokta arasındaki en kısa uzaklığı bulan öklid programına hoşgeldiniz.")
print("Lütfen birinci noktanın x ve y kordinatlarını verilen sıra ile yazınız.")
x1 = int(input("X ="))
y1 = int(input("Y ="))
print("Lütfen ikinci noktanın x ve y kordinatlarını verilen sıra ile yazınız.")
x2 = int(input("X ="))
y2 = int(input("Y ="))

points = [(x1,y1),(x2,y2)]
print("Girilen noktalar:" , points)
apsis_fark = (x1-x2)**2 
ordinat_Fark = (y1-y2)**2
top_fark = apsis_fark + ordinat_Fark

def euclideanDistance(x) :
  min_mesafe = int(top_fark)**(0.5)
  return min_mesafe

sonuc = euclideanDistance(top_fark)
print("Noktalar arasındaki fark = " , sonuc)