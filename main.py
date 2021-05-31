from PyQt5 import QtCore, QtGui, QtWidgets
import copy
from pkg.Route import Route
from random import randint
from pkg.Parser import parse_file


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Funkcja wygenerowana przez PyQt5.

        Dodane zostały tylko eventy klikania przycisków.

        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 762)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-color: rgb(135, 135, 135);\n"
                                 "alternate-background-color: rgb(157, 157, 157);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.success_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.success_lcd.setGeometry(QtCore.QRect(690, 80, 131, 51))
        self.success_lcd.setAutoFillBackground(False)
        self.success_lcd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.success_lcd.setObjectName("success_lcd")
        self.fail_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fail_lcd.setGeometry(QtCore.QRect(890, 80, 131, 51))
        self.fail_lcd.setAutoFillBackground(True)
        self.fail_lcd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fail_lcd.setObjectName("fail_lcd")
        self.success_label = QtWidgets.QLabel(self.centralwidget)
        self.success_label.setGeometry(QtCore.QRect(620, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.success_label.setFont(font)
        self.success_label.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.success_label.setFrameShape(QtWidgets.QFrame.Box)
        self.success_label.setObjectName("success_label")
        self.fail_label = QtWidgets.QLabel(self.centralwidget)
        self.fail_label.setGeometry(QtCore.QRect(830, 80, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fail_label.setFont(font)
        self.fail_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.fail_label.setFrameShape(QtWidgets.QFrame.Box)
        self.fail_label.setObjectName("fail_label")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(20, 680, 571, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 660, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(20, 30, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 521, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(620, 570, 114, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 220, 551, 441))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 10, 551, 431))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.path_textEdit = QtWidgets.QLineEdit(self.widget)
        self.path_textEdit.setAutoFillBackground(False)
        self.path_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.path_textEdit.setObjectName("path_textEdit")
        self.horizontalLayout.addWidget(self.path_textEdit)
        self.topo_from_file_button = QtWidgets.QPushButton(self.widget)
        self.topo_from_file_button.setAutoFillBackground(False)
        self.topo_from_file_button.setStyleSheet("background-color: rgb(230, 224, 255);")
        self.topo_from_file_button.setObjectName("topo_from_file_button")

        self.topo_from_file_button.clicked.connect(self.load_topo_from_file)

        self.horizontalLayout.addWidget(self.topo_from_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.topology_textEdit = QtWidgets.QTextEdit(self.widget)
        self.topology_textEdit.setAutoFillBackground(True)
        self.topology_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.topology_textEdit.setObjectName("topology_textEdit")
        self.verticalLayout.addWidget(self.topology_textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setAutoFillBackground(False)
        self.start_button.setStyleSheet("background-color: rgb(243, 235, 255);")
        self.start_button.setObjectName("start_button")

        self.start_button.clicked.connect(self.start_pressed)

        self.horizontalLayout_2.addWidget(self.start_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.logs_text = QtWidgets.QTextEdit(self.centralwidget)
        self.logs_text.setGeometry(QtCore.QRect(620, 170, 411, 391))
        self.logs_text.setObjectName("logs_text")
        self.result_text = QtWidgets.QTextEdit(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(620, 601, 411, 41))
        self.result_text.setObjectName("result_text")
        self.how_to_button = QtWidgets.QPushButton(self.centralwidget)
        self.how_to_button.setGeometry(QtCore.QRect(880, 10, 141, 41))
        self.how_to_button.setAutoFillBackground(True)
        self.how_to_button.setStyleSheet("background-color: rgb(242, 233, 255);")
        self.how_to_button.setObjectName("how_to_button")

        self.how_to_button.clicked.connect(self.show_help)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(620, 670, 411, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tries_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tries_label.setFont(font)
        self.tries_label.setAutoFillBackground(False)
        self.tries_label.setStyleSheet("background-color: rgb(178, 196, 255);")
        self.tries_label.setObjectName("tries_label")
        self.horizontalLayout_3.addWidget(self.tries_label)
        self.tries_spinBox = QtWidgets.QSpinBox(self.widget)
        self.tries_spinBox.setMinimum(1)
        self.tries_spinBox.setMaximum(99999)
        self.tries_spinBox.setSingleStep(5)
        self.tries_spinBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.tries_spinBox.setProperty("value", 100)
        self.tries_spinBox.setDisplayIntegerBase(10)
        self.tries_spinBox.setObjectName("tries_spinBox")
        self.horizontalLayout_3.addWidget(self.tries_spinBox)
        self.tries_label.raise_()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(626, 142, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.fail_label.raise_()
        self.success_label.raise_()
        self.frame.raise_()
        self.success_lcd.raise_()
        self.fail_lcd.raise_()
        self.progress_bar.raise_()
        self.line.raise_()
        self.info_label.raise_()
        self.label.raise_()
        self.result_label.raise_()
        self.logs_text.raise_()
        self.result_text.raise_()
        self.how_to_button.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Funkcja wygenerowana przez PyQt5

        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.success_label.setText(_translate("MainWindow", "Success:"))
        self.fail_label.setText(_translate("MainWindow", "Fail:"))
        self.info_label.setText(_translate("MainWindow", "SOIB - Projekt nr. 7 - OPTYCZNE POLA KOMUTACYJNE"))
        self.label.setText(_translate("MainWindow",
                                      "Program sprawdza czy zadane pole komutacyjne, zbudowane z komutatorów 2x2 "
                                      "jest polem nieblokowalnym. W celu przeprowadzenia symulacji "
                                      "zdefiniuj topologię lub kliknij przycisk \"Load topology from file\""))
        self.result_label.setText(_translate("MainWindow", "Simulation Result"))
        self.label_2.setText(_translate("MainWindow", "File Name: "))
        self.topo_from_file_button.setText(_translate("MainWindow", "Load topology from file"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.how_to_button.setText(_translate("MainWindow", "How to define topology?"))
        self.label_3.setText(_translate("MainWindow", "Logi"))
        self.tries_label.setText(_translate("MainWindow", "Liczba prób:"))

    def load_topo_from_file(self):
        """
        ładuje topologię z pliku tekstowego i wyświetla w odpowiednim oknie.
        """
        file_name = QtWidgets.QFileDialog.getOpenFileName()
        print(file_name[0])
        self.path_textEdit.insert(file_name[0])
        with open(file=file_name[0], mode='r') as file:
            text = file.read()
            self.topology_textEdit.clear()
        self.topology_textEdit.setText(text)

    def start_pressed(self):
        """
        Funkcja wywoływana poprzez kliknięciu przycisku `START`.

        Uruchamia funkcję `run_algorithm`, czyli zasadniczą część programu.
        """
        with open(file="files/current_topo.txt", mode='w') as file:
            topology_file = self.topology_textEdit.toPlainText()
            file.write(topology_file)
        Ui_MainWindow.run_algorithm(self, "files/current_topo.txt")

    def log_route(self, route):
        """
        Wyświetla aktualnie obliczoną trase w polu logów.
        :param route: (Route) trasa do wyświetlenia
        """
        new_route = []
        for com in route.route:
            new_route.append(com.id)
        self.logs_text.append(f"Route: {new_route}")

    @staticmethod
    def get_in_out(inputs, outputs):
        """
        Na podstawie ilości wejść i wyjść losuje trasy (wejście, wyjście)

        :param inputs: (int) Ilość wejść w polu komutacyjnym
        :param outputs: (int) Ilość wyjść w polu komutacyjnym
        :return: Zwraca tablice krotek (wejście, wyjście)
        """
        routes = []
        number_of_routes = min(inputs, outputs)
        tmp_inputs = []
        tmp_outputs = []

        while len(tmp_inputs) < number_of_routes:
            random_in = randint(1, inputs)
            if random_in not in tmp_inputs:
                tmp_inputs.append(random_in)

        while len(tmp_outputs) < number_of_routes:
            random_out = randint(1, outputs)
            if random_out not in tmp_outputs:
                tmp_outputs.append(random_out)

        for i in range(number_of_routes):
            routes.append((tmp_inputs[i], tmp_outputs[i]))
        return routes

    def check_if_blocked(self, topology, sections, routes):
        """
        Sprawdza czy dane pole komutacyjne jest blokowalne.

        Jedno przejście ustala, czy pole jest blokowalne dla danego zbioru krotek
        (wejście, wyjście). Jeżeli da się zestawić wszystkie ścieżki, to pole jest nieblokowalne.
        :param topology: [*Commutator] Tablica zawierająca komutatory, reprezentujące topologie pola.
        :param sections: (int) Ilość sekcji w badanym polu komutacyjnym.
        :param routes: [(a, b)] Tablica tras do zestawienia w formacie (wejście, wyjście).
        :return: Zwraca `True` jeżeli pole jest blokowalne, `False` w przeciwnym razie.
        """
        topo = copy.deepcopy(topology)
        blocked = False
        for j in range(30):
            blocked = False
            # Dla każdej pary (wejście, wyjście) znajdź ścieżkę
            for route in routes:
                input, output = route
                # Aby mieć pewność, że ścieżka zostanie poprawnie zestawiona powtórz 10 razy
                for i in range(10):
                    one_route = Route(input, output, topo)
                    done_route = one_route.do_routing(sections, topo)
                    self.log_route(one_route)
                    # Jeżeli ścieżka została znaleziona dla danego (wejścia, wyjścia)
                    if done_route != -404:
                        blocked = False
                        topo = one_route.change_status(topo)
                        self.logs_text.append(f"A route has been found between input {input} and "
                                                              f"exit {output}!")
                        break
                # Jeżeli nie udalo się zestawić ścieżki między daną parą (wejście, wyjście) spróbuj od nowa
                else:
                    blocked = True
                    self.logs_text.append(f"The commutation field has been blocked!: {input} - {output}")

                if blocked:
                    topo = copy.deepcopy(topology)
                    break
            if not blocked:
                break
        return blocked

    def run_algorithm(self, file):
        """
        Główna funkcja uruchamiająca algorytm. Uruchamiana jest poprzez kliknięcie `START`

        Funkcja zajmuje się uruchomieniem algorytmu `algorithm_count` razy. Ponadto zajmuje się wyświetlaniem
        logów w odpowiednim polu. Jedna blokada powoduje przerwanie wykonywanie algorytmu.
        :param file: ścieżka do pliku z topologią.
        """
        topology, inputs, outputs, sections = parse_file(file)
        self.logs_text.setText("START!")
        ok_events = 0
        bad_events = 0
        self.fail_lcd.display(bad_events)
        self.success_lcd.display(ok_events)
        algorithm_count = self.tries_spinBox.value()
        bar_value = 1

        for i in range(algorithm_count):
            self.logs_text.append(f"\n-------------- Execution: {i} --------------")
            bar_value += Ui_MainWindow.normalize_bar(algorithm_count)
            self.progress_bar.setValue(round(bar_value))
            routes = Ui_MainWindow.get_in_out(inputs, outputs)
            field_blocked = self.check_if_blocked(topology, sections, routes)

            if field_blocked:
                bad_events += 1
                self.fail_lcd.display(bad_events)
                self.progress_bar.setValue(100)
                break
            else:
                ok_events += 1
                self.success_lcd.display(ok_events)

        self.logs_text.append(f"All routes established: {ok_events} times. Couldn't establish "
                                      f"route: {bad_events} times")

        if bad_events > 0:
            self.result_text.setText(f"Pole jest blokowalne.")
        else:
            self.result_text.setText(f"Dla danej próby pole jest nieblokowalne w szerokim sensie! "
                                     f"Aby sie upewnić, możesz zwiększyć ilość przejśc algorytmu!")

    @staticmethod
    def normalize_bar(value):
        """
        Zajmuje się normalizacją `progress baru` do 100.
        @param value: ilość przejść algorytmu
        @return: zwraca znormalizowaną liczbę
        """
        if value < 100:
            return 99
        elif value == 100:
            return 1
        else:
            return 100 / value

    def show_help(self):
        """
        Funkcja wywoływana poprzez kliknięcie przycisku `How to define topology?'

        Umożliwia wyświetlenie krótkiej instrukcji definiowania topologii.
        """
        with open("files/README.txt", 'r') as file:
            help_file = file.read()
        self.logs_text.setPlainText(help_file)
        self.logs_text.update()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
