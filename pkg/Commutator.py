class Input:
    """
    Klasa reprezentująca pojedyncze wejście Komutatora.
    """
    def __init__(self, id, foreign_section, foreign_com_id, foreign_output):
        """
        Inicjalizacja wejścia.
        :param id: ID wejścia. Dozwolone 1/2 lub 0 - brak połączenia
        :param foreign_section: sekcja komutatora podłączonego do WE
        :param foreign_com_id: id komutatora podłączonego do WE
        :param foreign_output: Numer WY komutatora podłaczonego do WE
        """
        self.id = int(id)   # 1/2
        self.foreign_section = int(foreign_section)  # to which section connected
        self.foreign_com_id = int(foreign_com_id)   # to which commutator connected
        self.foreign_output = int(foreign_output)  # to which input connected
        self.is_busy = False


class Output:
    """
    Klasa reprezentująca pojedyncze wyjście Komutatora.
    """
    def __init__(self, id, foreign_section, foreign_com_id, foreign_input):
        """
        Inicjalizacja wyjścia
        :param id: ID wyjścia. Dozwolone 1/2 lub 0 - brak połączenia
        :param foreign_section: sekcja komutatora podłączonego do WY
        :param foreign_com_id: id komutatora podłączonego do WY
        :param foreign_input: Numer WE komutatora podłaczonego do WY
        """
        self.id = int(id)   # 1/2
        self.foreign_section = int(foreign_section)  # to which section connected
        self.foreign_com_id = int(foreign_com_id)   # to which commutator connected
        self.foreign_input = int(foreign_input)  # to which input connected
        self.is_busy = False


class Commutator:
    """
    Klasa reprezentująca pojedynczy komutator 2x2. 2 wejścia, 2 wyjścia
    """
    def __init__(self, section, id, left_section, left_id1, left_in1, left_id2, left_in2, right_section, right_id1,
                 right_out1, right_id2, right_out2):
        """

        :param section: Sekcja komutatora
        :param id: ID komutatora
        :param left_section: Sekcja komutatora podłączonego do WE
        :param left_id1: ID komutatora podłączonego do WE pierwszego
        :param left_in1: Numer WY podłączonego do WE komutatora pierwszego
        :param left_id2: ID komutatora podłączonego do WE drugiego
        :param left_in2: Numer WY podłączonego do WE komutatora drugiego
        :param right_section: Sekcja komutatora podłączonego do WY
        :param right_id1: ID komutatora podłączonego do WY pierwszego
        :param right_out1: Numer WE podłączonego do WY komutatora pierwszego
        :param right_id2: ID komutatora podłączonego do WY drugiego
        :param right_out2: Numer WE podłączonego do WY komutatora drugiego
        """
        self.section = int(section)
        self.id = int(id)
        self.in_1 = Input(id=1,
                          foreign_section=left_section,
                          foreign_com_id=left_id1,
                          foreign_output=left_in1,)
        self.in_2 = Input(id=2,
                          foreign_section=left_section,
                          foreign_com_id=left_id2,
                          foreign_output=left_in2,)
        self.out_1 = Output(id=1,
                            foreign_section=right_section,
                            foreign_com_id=right_id1,
                            foreign_input=right_out1,)
        self.out_2 = Output(id=2,
                            foreign_section=right_section,
                            foreign_com_id=right_id2,
                            foreign_input=right_out2,)
