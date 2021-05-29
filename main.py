from Parser import parse_file

from pkg.Route import Route
from random import randint


def get_random_in(topology, number_of_in):
    """
    Losuje randomowe wejścia.

    Nie uwzględnia, że niektóre są już zajęte. To jest uwzględnione
    w głównej funkcji.
    :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
    :param number_of_in: Ilośc wejść w polu komutacyjnym
    :return: Zwraca numer wejścia
    """
    random_input = randint(1, number_of_in)
    for com in topology:
        if com.section == 1:
            if com.in_1.foreign_output == random_input:
                if not com.in_1.is_busy:
                    return random_input
                else:
                    return -1
            elif com.in_2.foreign_output == random_input:
                if not com.in_2.is_busy:
                    return random_input
                else:
                    return -1


def display_routes(routes):
    """
    Wyświetla zestawione trasy.

    Raczej niepotrzebna funkcja
    :param routes: tablica tras
    """
    for r in routes:
        print("Route: ", end = '\t')
        for com in r.route:
            print(com.id, end = "\t")
        print()


def display_one_route(route):
    """
    Wyświetla wybraną trasę.
    :param route: trasa do wyświetlenia
    """
    print("Route: ", end='\t')
    for com in route.route:
        print(com.id, end="\t-\t")
    print()

def get_random_out(topology, number_of_out):
    """
    Losuje randomowe wyjście.

    Nie uwzględnia, że niektóre są już zajęte. To jest uwzględnione
    w głównej funkcji.
    :param topology: topologia pola komutacyjnego. Lista komutatorów 2x2
    :param number_of_out: Ilośc wyjść w polu komutacyjnym
    :return: Zwraca numer wyjścia
    """
    random_output = randint(1, number_of_out)
    for com in topology:
        if com.section == topology[-1].section:
            if int(com.out_1.foreign_input) == random_output:
                if not com.out_1.is_busy:
                    return random_output
                else:
                    return -1
            elif int(com.out_2.foreign_input) == random_output:
                if not com.out_2.is_busy:
                    return random_output
                else:
                    return -1

def start_algorithm(file, show_routes=False):
    """
    Wykonuje jedno przejście algorytmu.

    Algorytm kończy się, jeżeli wszystkie trasy zostaną zestawione lub
    gdy wystąpi jakiś wyjątek.
    :param file: ściężka do pliku z topologią pola komutacyjnego
    :param show_routes: parametr określający, czy chcemy, aby ścieżki
    były wyświetlane (True) lub nie (False) podczas wykonuwania algorytmu
    :return:
    """

    topology, inputs, outputs, sections = parse_file(file)

    routes_to_establish = min(inputs, outputs)
    established_routes = []

    while routes_to_establish > len(established_routes):
        random_in = get_random_in(topology, inputs)
        random_out = get_random_out(topology, outputs)
        count = 0
        while random_in == -1:
            random_in = get_random_in(topology, inputs)
            count += 1
            if count > 60:
                exit("Routing failed!")

        while random_out == -1:
            random_out = get_random_out(topology, outputs)
            count += 1
            if count > 120:
                exit("Routing failed!")

        route = Route(random_in, random_out, topology)
        new_route = route.do_routing(sections, topology)
        if new_route != -1:
            established_routes.append(new_route)
            topology = route.change_status(topology)
            if show_routes:
                print(f"Znaleziono trasę między wejściem {new_route.source_input}, a wyjściem {new_route.destination_output}!")
                display_one_route(new_route)
        else:
            return -1

    print("All connections have been established!")


if __name__ == "__main__":
    # start_algorithm("topology.txt", show_routes=True)
    ok_events = 0
    bad_events = 0

    for i in range(100):
        try:
            route = start_algorithm("topology5.txt", show_routes=False)
            if route == -1:
                bad_events += 1
            else:
                ok_events += 1
        except AttributeError:
            bad_events += 1
            print('-' * 80)
    print(f"All routes established: {ok_events} times. Couldn't establish route: {bad_events} times")



# display_routes(established_routes)
# print("Routes: " + str(established_routes))

# Tests
# for com in topology:
#     print(f"Commutator section: {com.section}, Comm id: {com.id}")
#     print(f"Input 1 - ID: {com.in_1.id}, Connected commutator: Section: {com.in_1.foreign_section}, "
#           f"ID: {com.in_1.foreign_com_id}, Comm IN: {com.in_1.foreign_output}, Busy: {com.in_1.is_busy}")
#     print(f"Input 2 - ID: {com.in_2.id}, Connected commutator: Section: {com.in_2.foreign_section}, "
#           f"ID: {com.in_2.foreign_com_id}, Comm IN: {com.in_2.foreign_output}, Busy: {com.in_2.is_busy}")
#     print(f"Output 1 - ID: {com.out_1.id}, Connected commutator: Section: {com.out_1.foreign_section}, "
#           f"ID: {com.out_1.foreign_com_id}, Comm IN: {com.out_1.foreign_input}, Busy: {com.out_1.is_busy}")
#     print(f"Output 2 - ID: {com.out_2.id}, Connected commutator: Section: {com.out_2.foreign_section}, "
#           f"ID: {com.out_2.foreign_com_id}, Comm IN: {com.out_2.foreign_input}, Busy: {com.out_2.is_busy}")
#     print()

