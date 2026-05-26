def shell_sort_names(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Membandingkan string secara abjad (case-insensitive)
            while j >= gap and arr[j - gap].lower() > temp.lower():
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    print("=== PROGRAM SHELL SORT NAMA ===")
    
    # List default sudah diganti sesuai permintaan
    my_data = ["kevin", "adam", "reno", "samudra"]
    
    print(f"List nama asli  : {my_data}")
    
    # Jalankan fungsi Shell Sort
    shell_sort_names(my_data)
    
    print(f"List setelah diurutkan: {my_data}")
    print("-" * 40)
    
    # Opsi tambahan jika ingin menerima input baru dari user di forum
    tanya = input("Mau coba input nama lain? (y/n): ")
    if tanya.lower() == 'y':
        input_user = input("Masukkan nama-nama (pisahkan dengan koma): ")
        list_nama = [nama.strip() for nama in input_user.split(",") if nama.strip()]
        print(f"List nama awal   : {list_nama}")
        shell_sort_names(list_nama)
        print(f"Hasil pengurutan : {list_nama}")