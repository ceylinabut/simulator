print("_@uthor_=Ceylin Zeynep ABUT---------->9/A-135")
print("İVME HESAPLAYICI")

kütle = input("Kütle: ")

ksayı = input("Sürtünme Katsayısı: ")

yivme = input("Yerçekimi İvmesi: ")

aykuvvet = input("Aşağı Yönlü Kuvvet: ")

yykuvvet = input("Yatay Yönlü Kuvvet: ")

birinci = int(kütle)*int(yivme)+int(aykuvvet)

sürtünme = int(birinci*int(ksayı))

netk = int(int(yykuvvet)-int(sürtünme))

ivme = int(int(netk)*int(kütle))

print(int(ivme))
