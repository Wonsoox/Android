from periodic_table import periodic_table

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

#테스트 코드
if __name__ == "__main__":
    molecule = MoleculeProcessor("CCCCCHHHHHHHHHHOOOO")
    elements = molecule.get_elements()
    for elem in elements:
        print(elem)
