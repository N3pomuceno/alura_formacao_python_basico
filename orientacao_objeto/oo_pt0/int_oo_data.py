

class Data():

    def __init__(self, dia_da_data, mes_da_data, ano_da_data):
        self.dia = dia_da_data
        self.mes = mes_da_data
        self.ano = ano_da_data

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))






