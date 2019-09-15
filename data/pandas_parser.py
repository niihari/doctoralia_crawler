from itertools import product

import pandas as pd

from data.doctor_data import DoctorData


class PandasParser:

    def __init__(self):
        self.doctors_dataframe = pd.DataFrame(columns=['Nome', 'Especialidade', 'Competência', 'Cidade', 'Estado', 'Telefone'])

    def add_to_dataframe(self, doctors_data: DoctorData) -> pd.DataFrame:
        for especialidade, competencia, endereco, telefone in product(doctors_data.especialidades, doctors_data.competencias, doctors_data.enderecos, doctors_data.telefones):
            self.doctors_dataframe = self.doctors_dataframe.append({'Nome': doctors_data.nome,
                                                                    'Especialidade': especialidade,
                                                                    'Competência': competencia,
                                                                    'Cidade': endereco.city,
                                                                    'Estado': endereco.state,
                                                                    'Telefone': telefone}, ignore_index=True)

    def remove_from_dataframe(self) -> pd.DataFrame:
        raise NotImplementedError()

    def write_to_excel_file(self):
        output_file = pd.ExcelWriter("output.xlsx", engine='xlsxwriter')
        self.doctors_dataframe.to_excel(output_file, 'Sheet1', index=False)
        output_file.save()