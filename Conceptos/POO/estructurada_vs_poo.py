# FORMA ESTRUCTURADA I
estr_1_celular1_marca = "samsung"
estr_1_celular2_marca = "apple"
estr_1_celular3_marca = "huawei"

estr_1_celular1_modelo = "S23"
estr_1_celular2_modelo = "Iphone 15 pro"
estr_1_celular3_modelo = "P20 Pro"

estr_1_celular1_camaraT = "48MP"
estr_1_celular2_camaraT = "48MP"
estr_1_celular3_camaraT = "12MP"

estr_1_celular1_camaraF = "24MP"
estr_1_celular2_camaraF = "24MP"
estr_1_celular3_camaraF = "8MP"

print("FORMA ESTRUCTURADA I")
print(estr_1_celular1_camaraT)
print(estr_1_celular2_modelo)

# FORMA ESTRUCTURADA II
estr_2_celulares = {
    "estr_2_celular1": {
        "marca": "samsung",
        "modelo": "S23",
        "camaraT": "48MP",
        "camaraF": "24MP"
    },
    "estr_2_celular2": {
        "marca": "apple",
        "modelo": "Iphone 15 pro",
        "camaraT": "48MP",
        "camaraF": "24MP"
    },
    "estr_2_celular3": {
        "marca": "huawei",
        "modelo": "P20 Pro",
        "camaraT": "12MP",
        "camaraF": "8MP"
    }
}

print("FORMA ESTRUCTURADA II")
print(estr_2_celulares["estr_2_celular1"]["camaraT"])
print(estr_2_celulares["estr_2_celular2"]["modelo"])

# FORMA POO
class EstrPooCelular():
    def __init__(self, marca, modelo, camaraT, camaraF):
        self.marca = marca
        self.modelo = modelo
        self.camaraT = camaraT
        self.camaraF = camaraF

print("FORMA POO")
poo_celular1 = EstrPooCelular("samsung","S23","48MP","24MP")
poo_celular2 = EstrPooCelular("apple","Iphone 15 pro","48MP","24MP")
poo_celular3 = EstrPooCelular("huawei","P20 Pro","12MP","8MP")
print(poo_celular1.camaraT)
print(poo_celular2.modelo)