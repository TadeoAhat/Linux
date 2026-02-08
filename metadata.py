import json

with open("example.cimg", "rb") as file: #rb je binarny mod na citanie a with zabezpeci ze sa subor VZDY zavrie po skonceni bloku
    magic = file.read(4) #citam prve styri bajty zo suboru
    assert magic == b"CIMG" #kontrolujeme ci su presne to co chceme, inak sa stane raise AssertionError
    meta_len = int.from_bytes(file.read(4), "big") #dalsie 4 bajty, ocakava sa 32bitove cislo, big znamena big-endian poradie bajtov (najvyznamnejsi 1.)
    meta = json.loads(file.read(meta_len).decode()) # json.loads zmeni na zoznam .decode prevedie bajty na str. 
    rest = file.read()
    print("metadata:", meta)
    print("data snippet:", rest[:200])