import random
import tkinter as tk
# from tk import ttk

emoney={
     16726232:100000
    ,16726497:5000
    ,16726567:45000
    ,16726187:50000
}

stasiun=[
    [1,0,"Stasiun Lebak Bulus Bank Syariah Indonesia"]
    ,[2,1.8,"Stasiun Fatmawati Indomaret"]
    ,[3,2.4,"Cipete Raya Tuku"]
    ,[4,5.0,"Haji Nawi"]
    ,[5,6.8,"Blok A"]
    ,[6,8.0,"Blok M BCA"]
    ,[7,8.8,"Asean"]
    ,[8,10.3,"Senayan Mastercard"]
    ,[9,11.2,"IStora Mandiri"]
    ,[10,12.7,"Bendungan Hilir Astra"]
    ,[11,13.4,"Setiabudi"]
    ,[12,14.5,"Dukuh Atas BNI"]
    ,[13,15.7,"Bundaran HI Bank DKI"]
]

def End():
    return input("apakah anda ingin kembali ke menu utama?(y/n): ")=="y"


def Perhitungan(stasiunA,stasiunB):
    awal=stasiun[stasiunA-1]
    akhir=stasiun[stasiunB-1]
    print(f"Perjalanan Dari {awal[2]} ke {akhir[2]}")
    if(stasiunB==stasiunA):
        return 1
    tarif=1500+abs(awal[1]-akhir[1])*850
    return tarif
    
def Trippplan():
    print("--Trip Autogate MRT--")
    while True:
        user=int(input("Silahkan masukkan E-money ID anda : "))
        if user in emoney:
            break
        print("Akun tidak ditemukan")
    if(emoney[user]<10000):
        print("Mohon maaf, saldo anda kurang")
        while(not(input("Return to main menu (y/n) : ")=='y')):
            continue
        else:
            return Main()
    print(f"Welcome {user} Silahkan pilih stasiun keberangkatan dan tujuan")
    while(True):
        print("Kode | Nama Stasiun")
        for i in stasiun:
            if(i[0]<10):
                print(f"[{i[0]}]     {i[2]}")
            else:
                print(f"[{i[0]}]    {i[2]}")
        try:
            stawal=int(input("kode stasiun awal: "))
            stakhir=int(input("kode stasiun akhir: "))
        except ValueError:
            print("Masukkan angka yang sesuai dengan ketentuan stasiun!")
            continue
        if(1<=stawal<=13 and 1<=stakhir<=13):
            break
    tarif=Perhitungan(stawal,stakhir)
    print(f"Tarif perjalanan: {tarif}")
    if(emoney[user]>=tarif):
        emoney[user]-=tarif
        print("sisa saldo :",emoney[user])
    else:
        print("Mohon maaf, saldo anda kurang")
        while(not(input("Return to main menu (y/n) : ")=='y')):
            continue
        else:
            return Main()
    return

def topup():
    print("--Topup E-money--")
    while True:
            user=int(input("Silahkan masukkan E-money ID anda : "))
            if user in emoney:
                break
            print("Akun tidak ditemukan")
    while(True):
        nominal=int(input("masukkan nominal topup : "))
        if(nominal<0):
            continue
        else:
            break
    emoney[user]+=nominal
    print(f"Saldo Emoney : {emoney[user]}")

def Newacc():
    print("--Create New E-money Card--")
    nama=input("masukkan nama anda : ")
    saldo=int(input("Masukkan nominal saldo: "))
    if(input("Apakah Anda setuju dengan seluruh peraturan dan ketentuan pembuatan kartu?(y/n): ")=="y"):
        while True:
            newid=random.randint(10_000_000, 99_999_999)
            if(not(newid in emoney)):
                emoney[newid]=saldo
                break
                
        print(f"ID Kartu E-money anda : {newid}\nSaldo anda : {emoney[newid]}")

def Emoneymanagement():
    print("--E-money Management System--\nSilahkan pilih menu yang anda inginkan!")
    while True:
        menu=int(input("[1] Topup E-money\n[2] Buat Kartu E-money\nYour Answer : "))
        if(not(1<=menu<=2)):
            continue
        else:
            break
    if(menu==1):
        topup()
    else:
        Newacc()
    return

    
def Main():
    while True:
        print("#-------------------------------#\n--Selamat datang di mockup system autogate MRT Jakarta--\nSilahkan pilih menu aplikasi")
        while True:
            menu=int(input("[1] Trip Autogate MRT\n[2] E-money Management System\n(Please Input 1/2) : "))
            if(not(1<=menu<=2)):
                continue
            else:
                break
        if(not(menu-1)):
            Trippplan()
        else:
            Emoneymanagement()
        if not(End()):
            print("Terimakasih")
            break




Main()