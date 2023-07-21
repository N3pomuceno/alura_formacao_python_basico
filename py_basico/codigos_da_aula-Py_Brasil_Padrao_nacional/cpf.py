
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        fatia_um = self._cpf[:3]
        fatia_dois = self._cpf[3:6]
        fatia_tres = self._cpf[6:9]
        fatia_quatro = self._cpf[9:]
        # print(fatia_um, fatia_dois, fatia_tres, fatia_quatro)

        return "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)

    def __str__(self):
        return self.format_cpf()
        