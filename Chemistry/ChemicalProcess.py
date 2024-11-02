# 원소 데이터베이스 (주기율표 일부)
periodic_table = {
    'H': {'name': 'Hydrogen', 'number': 1, 'metallic': False, 'group': 1, 'period': 1, 'valence': 1},
    'C': {'name': 'Carbon', 'number': 6, 'metallic': False, 'group': 14, 'period': 2, 'valence': 4},
    'O': {'name': 'Oxygen', 'number': 8, 'metallic': False, 'group': 16, 'period': 2, 'valence': 6},
    # 추가 원소는 여기에 계속 추가
}

# 원소 클래스
class Element:
    def __init__(self, symbol):
        if symbol in periodic_table:
            self.symbol = symbol
            self.properties = periodic_table[symbol]
        else:
            raise ValueError(f"Unknown element: {symbol}")

    def __repr__(self):
        return f"Element(symbol='{self.symbol}', properties={self.properties})"

    def valence_electrons(self):
        return self.properties['valence']

# 화합물 처리기
class MoleculeProcessor:
    def __init__(self, molecule_string):
        self.molecule_string = molecule_string
        self.element_list = self._parse_molecule()

    def _parse_molecule(self):
        """문자열을 개별 원자로 분해하여 저장"""
        return [Element(symbol) for symbol in self.molecule_string]

    def get_elements(self):
        """임시 저장소의 원자 리스트를 반환"""
        return self.element_list

# 테스트 코드
if __name__ == "__main__":
    molecule = MoleculeProcessor("CCCCCHHHHHHHHHHOOOO")
    elements = molecule.get_elements()
    for elem in elements:
        print(elem)
