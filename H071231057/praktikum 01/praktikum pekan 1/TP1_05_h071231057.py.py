#MERUBAH DETIK KE FORMAT JAM
DETIK      = int(input("MASUKKAN DETIK : "))
JAM        = DETIK // 3600
SISA_DETIK = DETIK % 3600
MENIT      = SISA_DETIK // 60
DETIK1     = SISA_DETIK % 60

print(JAM , "JAM" , MENIT , "MENIT" , DETIK1 , "DETIK" )
 
 







