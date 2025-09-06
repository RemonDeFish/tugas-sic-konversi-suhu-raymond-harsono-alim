def konversi_suhu(nilai, dari, ke):
    #biar g case sensitive
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Satuan suhu tidak valid"
    if dari == "k" and nilai < 0:
        return "Suhu tidak valid"
    if dari == ke:
        return nilai

    #konversi suhu
    if dari == "c" and ke == "f":
        hasil = (9/5) * nilai + 32
    elif dari == "c" and ke == "k":
        hasil = nilai + 273.15
    elif dari == "f" and ke == "c":
        hasil = (5/9) * (nilai - 32)
    elif dari == "f" and ke == "k":
        hasil = (5/9) * (nilai - 32) + 273.15
    elif dari == "k" and ke == "c":
        hasil = nilai - 273.15
    elif dari == "k" and ke == "f":
        hasil = (9/5) * (nilai - 273.15) + 32

    return hasil
