from pkg.Commutator import Commutator


def parse_file(file):
    """
    Reads file and creates topology of commutation field which is created
    connections of 2x2 commutators.
    :param file: path to topology file
    :return: topology as list of Commutators 2x2
    """
    topology = []
    with open(file, 'r') as file:
        sections = int(file.readline())
        com_in_sections = file.readline().split()
        inputs, outputs = 2 * int(com_in_sections[0]), 2 * int(com_in_sections[-1])

        file.readline()

        for i in range(sections):
            for j in range(int(com_in_sections[i])):
                line = file.readline().split()
                topology.append(Commutator(i+1, j+1, i, line[0], line[1], line[2], line[3], i+2, line[4], line[5], line[6], line[7]))
            file.readline()

    for elem in topology:
        if elem.section == 1:
            if elem.out_1.foreign_input == 0:
                elem.out_1.is_busy = True
            if elem.out_2.foreign_input == 0:
                elem.out_2.is_busy = True
        elif elem.section == topology[-1].section:
            if elem.in_1.foreign_output == 0:
                elem.in_1.is_busy = True
            if elem.in_2.foreign_output == 0:
                elem.in_2.is_busy = True
        else:
            if elem.in_1.foreign_output == 0:
                elem.in_1.is_busy = True
            if elem.in_2.foreign_output == 0:
                elem.in_2.is_busy = True
            if elem.out_1.foreign_input == 0:
                elem.out_1.is_busy = True
            if elem.out_2.foreign_input == 0:
                elem.out_2.is_busy = True

    return topology, inputs, outputs, sections
