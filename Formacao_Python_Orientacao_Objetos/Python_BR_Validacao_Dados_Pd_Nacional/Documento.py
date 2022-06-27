from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento, tipo_documento):
        tipo_documento = tipo_documento.lower().strip()
        if tipo_documento == 'cpf':
            documento = str(documento).strip()
            return Cpf(documento)
        elif tipo_documento == 'cnpj':
            documento = str(documento).strip()
            return Cnpj(documento)
        else:
            raise ValueError(f"O tipo de documento {tipo_documento} é inválido!")

class Cpf:
    def __init__(self, documento):
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Inválido')

    def __str__(self):
        return CPF().mask(self.cpf)

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return CPF().validate(documento)
        else:
            raise ValueError('Número de dígitos inválido')

class Cnpj:
    def __init__(self, documento):
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido')

    def __str__(self):
        return CNPJ().mask(self.cnpj)

    def cnpj_eh_valido(self, documento):
        if len(documento) == 14:
            return CNPJ().validate(documento)
        else:
            raise ValueError('Número de dígitos inválido')