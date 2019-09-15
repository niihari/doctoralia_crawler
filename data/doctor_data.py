from typing import List, Set


class Address:

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    def __init__(self):
        self._city: str = ""
        self._state: str = ""

    # Overload
    def __string__(self) -> str:
        return 'Cidade:%s Estado:%s' % (self.city, self.state)

    # Overload
    def __eq__(self, other) -> bool:
        return self.city == other.city and self.state == other.state

    # Overload
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    # Overload
    def __repr__(self) -> str:
        return self.__string__()

    # Overload
    def __hash__(self):
        return hash((frozenset(self.city), frozenset(self.state)))


class DoctorData:

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def especialidades(self) -> List[str]:
        return self._especialidades

    @especialidades.setter
    def especialidades(self, especialidades: List[str]):
        self._especialidades = especialidades

    @property
    def competencias(self) -> List[str]:
        return self._competencias

    @competencias.setter
    def competencias(self, competencias: List[str]):
        self._competencias = competencias

    @property
    def enderecos(self) -> Set[Address]:
        return self._enderecos

    @enderecos.setter
    def enderecos(self, enderecos: Set[Address]):
        self._enderecos = enderecos

    @property
    def telefones(self) -> List[str]:
        return self._telefones

    @telefones.setter
    def telefones(self, telefones: List[str]):
        self._telefones = telefones

    def __init__(self):
        self._nome: str = ''
        self._especialidades: List[str] = []
        self._competencias: List[str] = ['']
        self._enderecos: Set[Address] = set()
        # TODO extract_telefones
        self._telefones: List[str] = ['']