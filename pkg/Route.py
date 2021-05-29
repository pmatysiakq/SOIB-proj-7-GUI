from random import randint
import copy


class Route:
    def __init__(self, source, destination, topology):
        self.source_input = source
        self.destination_output = destination
        self.src_com, self.in_number = self.get_src_com_link(topology)
        self.dst_com, self.out_number = self.get_dst_com_link(topology)
        self.route = [self.src_com]
        self.inout = {
            "section": [1],
            "id": [self.src_com.id],
            "out_link": [],
        }

    def get_src_com_link(self, topology):
        """
        Trochę iksde. Bierze topologie i zwraca src komutator i aktualnie rozpatrywane wejście
        :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
        :return: źródłowy komutator i źródłowe wejście
        """
        for com in topology:
            if com.section == 1:
                if com.in_1.foreign_output == self.source_input:
                    return com, 1
                elif com.in_2.foreign_output == self.source_input:
                    return com, 2

    def get_dst_com_link(self, topology):
        """
        Trochę iksde. Bierze topologie i zwraca dst komutator i aktualnie rozpatrywane wyjście
        :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
        :return:
        """
        for com in topology:
            if com.section == topology[-1].section:
                if com.out_1.foreign_input == self.destination_output:
                    return com, 1
                elif com.out_2.foreign_input == self.destination_output:
                    return com, 2

    @staticmethod
    def next_output(com):
        """
        Ustala, przez które wyjście komutatora przejdzie trasa.

        Jeżeli oba wyjścia są dostępne to losuje jedno z nich, jeżeli jedno jest niedostępne to bierze
        to drugie. W innym przypadku zwraca -1
        :param com: komutator
        :return: wyjście komutatora com, przez które przejdzie trasa
        """
        output1 = com.out_1
        output2 = com.out_2

        if output1.is_busy == False and output2.is_busy == False:
            out_link = randint(1, 2)
        elif output1.is_busy == True and output2.is_busy == False:
            out_link = 2
        elif output1.is_busy == False and output2.is_busy == True:
            out_link = 1
        else:
            out_link = -1

            print(f"OUT1: {com.out_1.is_busy}, OUT2: {com.out_2.is_busy}, COM: sect- {com.section}, id- {com.id}")
        return out_link

    def get_next_com(self, topology, prev_com):
        """
        Na podstawie topologii ustala, jaki komutator będzie kolejny na trasie

        W dziki sposób sprawdza do którego komutatora podpięte jest wybrane wyjście
        poprzedniego komutatora na trasie.
        :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
        :param prev_com: poprzedni komutator na trasie
        :return:
        """
        section = prev_com.section + 1
        prev_output = Route.next_output(prev_com)
        self.inout["out_link"].append(prev_output)
        if prev_output == 1:
            next_com_id = prev_com.out_1.foreign_com_id
        elif prev_output == 2:
            next_com_id = prev_com.out_2.foreign_com_id
        else:
            return -1

        for com in topology:
            if com.section == section:
                if com.id == next_com_id:
                    self.route.append(com)
                    return com

    def change_status(self, topology):
        """
        Po ustaleniu trasy, ustawia odpowiednie wyjścia na zajęte.

        W następnych przejściach te wyjścia są oznaczone jako niedostępne dla nowych tras. A no i
        jeszcze ustawia użyte wyjście jako niedostępne.
        :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
        :return: zwraca zaktualizowaną topologię
        """

        # Pewnie niepotrzebne, wcześniej miałem inny pomysł
        topo = copy.deepcopy(topology)

        # Change status for input:
        for i in range(len(topo)):
            if topo[i].id == self.src_com.id and topo[i].in_1.id == self.in_number:
                topo[i].in_1.is_busy = True
                break
            elif topo[i].id == self.src_com.id and topo[i].in_2.id == self.in_number:
                topo[i].in_2.is_busy = True
                break

        # Change status for everything else
        for i in range(len(self.inout["section"])):
            for j in range(len(topo)):
                if topo[j].section == self.inout["section"][i] and topo[j].id == self.inout["id"][i] and topo[j].out_1.id == self.inout["out_link"][i]:
                    topo[j].out_1.is_busy = True
                    break
                if topo[j].section == self.inout["section"][i] and topo[j].id == self.inout["id"][i] and topo[j].out_2.id == self.inout["out_link"][i]:
                    topo[j].out_2.is_busy = True
                    break

        return topo

    def do_routing(self, sections, topology):
        """
        Ustala trasę od wejścia do wyjścia.

        Jeżeli nie uda sie ustalić komutatora - wywala AttributeError, dzięki któremu zlicza
        ile razy nie udało się ustalić trasy. Nie uwzględnia jak trasa dojdzie do ostatniej sekcji i
        nie znajdzie odpowiedniego wyjścia.
        :param sections: Ilość sekcji w polu komutacyjnym
        :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
        :return: Zwraca trasę, jeżeli uda się zestawić. -1 w innym przypadku.
        """
        com = self.route[-1]
        for i in range(sections - 1):
            com = self.get_next_com(topology, com)
            if com == -1:
                print(f"Can't establish route {self.source_input} - {self.destination_output}")
            self.inout["section"].append(com.section)
            self.inout["id"].append(com.id)
        if com.section == self.dst_com.section and com.id == self.dst_com.id:
            if com.out_1.id == self.out_number:
                if not com.out_1.is_busy:
                    self.inout["out_link"].append(self.out_number)
                    self.change_status(topology)
                    return self
                else:
                    return -1
            elif com.out_2.id == self.out_number:
                if not com.out_2.is_busy:
                    self.inout["out_link"].append(self.out_number)
                    self.change_status(topology)
                    return self
                else:
                    return -1
            else:
                return -1
        else:
            return -1
