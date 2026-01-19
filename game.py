secret_number = 777
guess_number = int(input("masukkan tebak angka"))

while guess_number != secret_number:
    print("tebakan salah, silahkan coba lagi")
    guess_number = int(input("masukkan tebak angka"))

print("selamat..!! anda menebak angka dengan benar")