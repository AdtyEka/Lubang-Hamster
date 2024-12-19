import random  
from lib import pesan_sambutan 
from lib import exit_program 
pesan_sambutan()

nama_user = input("Masukkan Nama Anda = ")  

while nama_user == "":
    nama_user = input("Masukkan Nama Anda Terlebih Dahulu = ")  

while True:
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 
    goa_posisi = random.randint(1, 4)  
    goa = goa_kosong.copy() 
    goa [goa_posisi - 1] = "|Lewis Hamilton|"  
    goa_kosong = ' '.join(goa_kosong) 
    goa = ' '.join(goa)
    
    print("")
    print(f'''
      Haloo {nama_user}, coba perhatikan Goa di bawah ini
         {goa_kosong}
      Coba tebak Di manakah Posisi Lewis Berada
     ''')  

    pilihan_user = int(input("Menurut Kamu di Goa nomor berapa Lewis berada? [1 / 2 / 3 / 4] : ")) 

    print("")  
    print("Pilihan Anda Adalah =", pilihan_user)  
        
    konfirmasi_jawaban = input(f"Apakah Kamu Yakin dengan Jawaban ini = {pilihan_user} , jika yakin pilih [y] jika tidak pilih [n] = [y/n] ")

    if pilihan_user == "n":
        print("program akan berhenti")
        exit()
    elif konfirmasi_jawaban == "y":
        if pilihan_user == goa_posisi:
            print(f'''
                  Selamat {nama_user},
                  Kamu berhasil menebak posisi Lewis di GOA ke - 
                  {goa} 
                  sesuai dengan goa yang Anda pilih yaitu GOA ke- {pilihan_user}
                  dan lewis berada pada goa nomer {goa_posisi}
                  ''')
        else:
            print(f'''
                  yahhh {nama_user},
                  Kamu gagall menebak posisi Lewis di GOA ke - 
                  {goa} 
                  karena goa yang Anda pilih yaitu GOA ke-{pilihan_user}
                  dan lewis berada pada goa nomer {goa_posisi}
                  ''')
    else:
        print("Silahkan Ulangi Programnya")
        exit()    

    main_lagi = input("\nApakah Anda Ingin Bermain Lagi? [y/n] = ")
    if main_lagi == "n":
        print("===============================================================")
        print(f"program akan berhenti, terima kasih sudah bermain {nama_user} ")
        print("===============================================================")
        exit_program()
        break
    else:
        print("===============================")
        print(f"Baikk, Ayo Bermain Lagi {nama_user}")
        print("===============================")
        continue   
