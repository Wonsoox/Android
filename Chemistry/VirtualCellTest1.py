import ChemicalProcess
from collections import Counter  # Counter 클래스를 임포트

# 분자를 나타내는 클래스
class Molecule:
    def __init__(self, elements):
        self.elements = elements  # 원소 리스트
        self.formula = self.calculate_formula()  # 분자식 계산

    def calculate_formula(self):
        """원소의 수를 계산하여 분자식을 반환합니다."""
        element_count = Counter(elem.symbol for elem in self.elements)
        return ' + '.join(f"{count} {element}" for element, count in element_count.items())

# 가상의 세포 클래스
class Cell:
    def __init__(self):
        self.carbon_chain = []  # 탄소 결합을 저장할 리스트
        self.remaining_elements = []  # 결합하지 않은 잔여물 저장
        self.co2_produced = []  # 생성된 CO₂ 분자를 저장할 리스트

    def consume_elements(self, elements):
        """입력된 원소를 처리하고 이산화탄소 생성 및 잔여물 처리"""
        carbon_count = 0
        hydrogen_count = 0
        oxygen_count = 0
        
        for element in elements:
            if element.symbol == 'C':
                carbon_count += 1  # 탄소 수 증가
            elif element.symbol == 'H':
                hydrogen_count += 1  # 수소 수 증가
            elif element.symbol == 'O':
                oxygen_count += 1  # 산소 수 증가
            else:
                self.remaining_elements.append(element)  # 나머지는 잔여물로

        # 이산화탄소 생성: CO₂는 탄소 1개와 산소 2개 필요
        while carbon_count > 0 and oxygen_count >= 2:
            self.co2_produced.append(Molecule([Element('C'), Element('O'), Element('O')]))
            carbon_count -= 1
            oxygen_count -= 2

        # 수소는 나머지 원소에 포함되어 남는다
        self.remaining_elements.extend([Element('H')] * hydrogen_count)

    def display_cell_contents(self):
        """세포 내의 이산화탄소 생성량과 잔여물을 출력"""
        print("CO2 Produced:")
        for co2 in self.co2_produced:
            print(co2.formula)
        print("Remaining Elements:", [elem.symbol for elem in self.remaining_elements])

    def display_remaining_elements_count(self):
        """남은 원소의 종류와 개수를 출력"""
        element_counts = Counter(elem.symbol for elem in self.remaining_elements)
        print("Remaining Elements Count:")
        for element, count in element_counts.items():
            print(f"{element}: {count}")

# Element 클래스 가정 (추가 필요)
class Element:
    def __init__(self, symbol):
        self.symbol = symbol

# 테스트 코드
if __name__ == "__main__":
    molecule = ChemicalProcess.MoleculeProcessor("CCCCCHHHHHHHHHHOOOO")
    elements = molecule.get_elements()

    # 세포 생성 및 원소 처리
    cell = Cell()
    cell.consume_elements(elements)

    # 세포 내용 출력
    cell.display_cell_contents()

    # 남은 원소의 종류와 개수 출력
    cell.display_remaining_elements_count()
