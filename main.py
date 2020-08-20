from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv
import json
from datetime import datetime
matplotlib.use('TkAgg')

global fig
startt = ""
endd = ""
global_date = ""
global_date2 = ""
file_name = ""
indication = ""
dates, temperature, humidity, pressure = [], [], [], []
datesTest, DS18B20_temp, BMP280_temp, BMP280_pressure, BME280_temp, BME280_pressure, BME280_humidity = [], [], [], [], [], [], []
AM2321_temp, AM2321_humidity = [], []
pribor = ""
TestPribor = ""

ticksallwith = ["0:00:00 ", "1:00:00 ", "2:00:00 ", "3:00:00 ", "4:00:00 ", "5:00:00 ", "6:00:00 ", "7:00:00 ",
                "8:00:00 ",
                "9:00:00 ", "10:00:00 ", "11:00:00 ", "12:00:00 ", "13:00:00 ", "14:00:00 ", "15:00:00 ", "16:00:00 ",
                "17:00:00 ", "18:00:00 ", "19:00:00 ", "20:00:00 ", "21:00:00 ", "22:00:00 ", "23:00:00 ", "24:00:00 "]

ticksallwithout = ["00 00 00 ", "01 00 00 ", "02 00 00 ", "03 00 00 ", "04 00 00 ", "05 00 00 ", "06 00 00 ",
                   "07 00 00 ",
                   "08 00 00 ",
                   "09 00 00 ", "10 00 00 ", "11 00 00 ", "12 00 00 ", "13 00 00 ", "14 00 00 ", "15 00 00 ",
                   "16 00 00 ",
                   "17 00 00 ", "18 00 00 ", "19 00 00 ", "20 00 00 ", "21 00 00 ", "22 00 00 ", "23 00 00 ",
                   "24 00 00 "]

ticks3hour = ["00:00:00", "3:00:00", "6:00:00", "9:00:00", "12:00:00", "15:00:00", "18:00:00", "21:00:00", "24:00:00"]

alldatesticks = ['28-10-2019 ', '29-10-2019 ', '30-10-2019 ', '31-10-2019 ', '01-11-2019 ', '02-11-2019 ',
                 '03-11-2019 ',
                 '04-11-2019 ', '05-11-2019 ', '06-11-2019 ', '07-11-2019 ', '08-11-2019 ', '09-11-2019 ',
                 '10-11-2019 ',
                 '11-11-2019 ', '12-11-2019 ', '13-11-2019 ', '14-11-2019 ', '15-11-2019 ', '16-11-2019 ',
                 '17-11-2019 ']

alldatesticks_no3_13 = ['28-10-2019 ', '29-10-2019 ', '30-10-2019 ', '31-10-2019 ', '01-11-2019 ', '02-11-2019 ',
                        '03-11-2019 ',
                        '05-11-2019 ', '06-11-2019 ', '07-11-2019 ', '08-11-2019 ', '09-11-2019 ', '10-11-2019 ',
                        '11-11-2019 ', '12-11-2019 ', '14-11-2019 ', '15-11-2019 ', '16-11-2019 ', '17-11-2019 ']

alldatestickswithout = ['2019 10 28 ', '2019 10 29 ', '2019 10 30 ', '2019 10 31 ', '2019 11 01 ', '2019 11 02 ',
                        '2019 11 03 ',
                        '2019 11 04 ', '2019 11 05 ', '2019 11 06 ', '2019 11 07 ', '2019 11 08 ', '2019 11 09 ',
                        '2019 11 10 ',
                        '2019 11 11 ', '2019 11 12 ', '2019 11 13 ', '2019 11 14 ', '2019 11 15 ', '2019 11 16 ',
                        '2019 11 17 ']

dates3ticks = ['28-10-2019 ', '31-10-2019 ', '03-11-2019 ',
               '06-11-2019 ', '09-11-2019 ',
               '12-11-2019 ', '15-11-2019 ', '18-11-2019 ']


def delete():
    root.quit()
    exit()


def Start():
    global fig, file_name
    fig = plt.figure(dpi=120, figsize=(16, 9))
    mb.showinfo("Выбор файла", "Выберите файл для работы (формат csv или json)")
    file_name = fd.askopenfilename(filetypes=[("CSV file", "*.csv"), ("JSON file", "*.json")])
    return file_name


def open_rosa_k2(reader_):
    global pribor
    pribor = "Rosa"
    header_row = next(reader_)
    header_row = next(reader_)
    for row in reader_:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            high = float(row[1])
            pressures = float(row[2])
            humidities = float(row[3])
        except ValueError:
            print('Ошибка данных')
        else:
            dates.append(current_date)
            temperature.append(high)
            pressure.append(pressures)
            humidity.append(humidities)


def open_test_studii(reader_):
    global pribor
    pribor = "Test"
    header_row = next(reader_)
    header_row = next(reader_)
    for row in reader_:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            tempDS18B20 = float(row[15])
            tempBMP280 = float(row[16])
            pressBMP280 = float(row[17])
            tempBME280 = float(row[18])
            pressBME280 = float(row[19])
            humidityBME280 = float(row[20])
            tempAM2321 = float(row[25])
            humidityAM2321 = float(row[26])
        except ValueError:
            print("Ошибка данных")
        else:
            datesTest.append(current_date)
            DS18B20_temp.append(tempDS18B20)
            BMP280_temp.append(tempBMP280)
            BMP280_pressure.append(pressBMP280)
            BME280_temp.append(tempBME280)
            BME280_pressure.append(pressBME280)
            BME280_humidity.append(humidityBME280)
            AM2321_temp.append(tempAM2321)
            AM2321_humidity.append(humidityAM2321)


def open_rosa_k2_json(json_data):
    global pribor
    pribor = "Rosa"
    dates.append(datetime.strptime(json_data[ii]['Date'], "%Y-%m-%d %H:%M:%S"))
    temperature.append(float(json_data[ii]['data']['weather_temp']))
    pressure.append(float(json_data[ii]['data']['weather_pressure']))
    humidity.append(float(json_data[ii]['data']['weather_humidity']))


def open_test_studii_json(json_data):
    global pribor
    pribor = "Test"
    datesTest.append(datetime.strptime(json_data[ii]['Date'], "%Y-%m-%d %H:%M:%S"))
    DS18B20_temp.append(float(json_data[ii]['data']['DS18B20_temp']))
    BMP280_temp.append(float(json_data[ii]['data']['BMP280_temp']))
    BMP280_pressure.append(float(json_data[ii]['data']['BMP280_pressure']))
    BME280_temp.append(float(json_data[ii]['data']['BME280_temp']))
    BME280_pressure.append(float(json_data[ii]['data']['BME280_pressure']))
    BME280_humidity.append(float(json_data[ii]['data']['BME280_humidity']))
    AM2321_temp.append(float(json_data[ii]['data']['AM2321_temp']))
    AM2321_humidity.append(float(json_data[ii]['data']['AM2321_humidity']))


def plotfunc(first, second, third, type_of_graph, ind, trigger):
    global startt, endd
    if type_of_graph == 'single':
        if ind == "Температура":
            plt.plot(first, second, c='red')
            plt.xticks(first)
            plt.title("Temperature", fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Temperature', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])

            plt.xticks(xtick, number_of_ticks)
            fig.autofmt_xdate()
            plt.grid(True)
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Давление":
            plt.plot(first, second, c='grey')
            plt.xticks(first)
            plt.title("Pressure", fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Pressure', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])

            plt.xticks(xtick, number_of_ticks)
            fig.autofmt_xdate()
            plt.grid(True)
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Влажность":
            plt.plot(first, second, c='blue')
            plt.xticks(first)
            plt.title("Humidity", fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Humidity', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])
            plt.xticks(xtick, number_of_ticks)
            fig.autofmt_xdate()
            plt.grid(True)
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
    elif type_of_graph == "singlescatter":
        if ind == "Температура":
            plt.scatter(first, second)
            plt.plot(first, second, c='red')
            title = "Temperature"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Temperature', fontsize=16)
            plt.xticks(first)
            plt.yticks(
                [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40, 42.5, 45, 47.5,
                 50])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Давление":
            plt.scatter(first, second)
            plt.plot(first, second, c='grey')
            title = "Pressure"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Pressure', fontsize=16)
            plt.xticks(first)
            plt.yticks(
                [700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790,
                 795, 800])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Влажность":
            plt.scatter(first, second)
            plt.plot(first, second, c='blue')
            title = "Humidity"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Humidity', fontsize=16)
            plt.xticks(first)
            plt.yticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
    elif type_of_graph == 'double':
        if ind == "Температура":
            plt.plot(first, second, 'red', first, third, 'orange')
            title = "Temperature"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Temperature', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])

            plt.xticks(xtick, number_of_ticks)
            plt.yticks(
                [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40, 42.5, 45, 47.5,
                 50])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Давление":
            plt.plot(first, second, 'k', first, third, 'y')
            title = "Pressure"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Pressure', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])

            plt.xticks(xtick, number_of_ticks)
            plt.yticks(
                [700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790,
                 795, 800])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
        elif ind == "Влажность":
            plt.plot(first, second, 'm', first, third, 'b')
            title = "Humidity"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            plt.ylabel('Humidity', fontsize=16)
            number_of_ticks = ticksnumber(startt, endd)
            countt = int(float(len(first) / len(number_of_ticks) + 1))
            xtick = []
            for i in range(0, len(first), countt):
                xtick.append(first[i])
            plt.xticks(xtick, number_of_ticks)
            plt.yticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            plt.grid(True)
            fig.autofmt_xdate()
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.canvas.draw()
    elif type_of_graph == "allind":
        if trigger == "simple":
            if ind == "Температура":
                plt.plot(first, second, c='red')
                plt.title("Temperature", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Temperature', fontsize=16)
                xticks = []
                if filename.endswith('.csv'):
                    count = int(len(first) / 21) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks)
                elif filename.endswith('.json'):
                    count = int(len(first) / 19) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks_no3_13)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Давление":
                plt.plot(first, second, c='grey')
                plt.title("Pressure", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Pressure', fontsize=16)
                xticks = []
                if filename.endswith('.csv'):
                    count = int(len(first) / 21) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks)
                elif filename.endswith('.json'):
                    count = int(len(first) / 19) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks_no3_13)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Влажность":
                plt.plot(first, second, c='blue')
                plt.title("Humidity", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Humidity', fontsize=16)
                xticks = []
                if filename.endswith('.csv'):
                    count = int(len(first) / 21) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks)
                elif filename.endswith('.json'):
                    count = int(len(first) / 19) + 1
                    for i in range(0, len(first), count):
                        xticks.append(first[i])
                    plt.xticks(xticks, alldatesticks_no3_13)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
        elif trigger == "average":
            if ind == "Температура":
                plt.scatter(first, second)
                plt.plot(first, second, c='red')
                plt.title("Temperature", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Temperature', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Давление":
                plt.scatter(first, second)
                plt.plot(first, second, c='grey')
                plt.title("Pressure", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Pressure', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Влажность":
                plt.scatter(first, second)
                plt.plot(first, second, c='blue')
                plt.title("Humidity", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Humidity', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
        elif trigger == "minmax":
            if ind == "Температура":
                if filename.endswith('.csv'):
                    plt.scatter(alldatesticks, second)
                    plt.scatter(alldatesticks, first)
                    plt.plot(alldatesticks, second, c='red')
                    plt.plot(alldatesticks, first)
                    plt.fill_between(alldatesticks, second, first, facecolor='red', alpha=0.1)
                    plt.xticks(alldatesticks)
                elif filename.endswith('.json'):
                    plt.scatter(alldatesticks_no3_13, second)
                    plt.scatter(alldatesticks_no3_13, first)
                    plt.plot(alldatesticks_no3_13, second, c='red')
                    plt.plot(alldatesticks_no3_13, first)
                    plt.fill_between(alldatesticks_no3_13, second, first, facecolor='red', alpha=0.1)
                    plt.xticks(alldatesticks_no3_13)

                plt.title("Temperature", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Temperature', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Давление":
                if filename.endswith('.csv'):
                    plt.scatter(alldatesticks, second)
                    plt.scatter(alldatesticks, first)
                    plt.plot(alldatesticks, second, c='grey')
                    plt.plot(alldatesticks, first)
                    plt.fill_between(alldatesticks, second, first, facecolor='grey', alpha=0.1)
                    plt.xticks(alldatesticks)
                elif filename.endswith('.json'):
                    plt.scatter(alldatesticks_no3_13, second)
                    plt.scatter(alldatesticks_no3_13, first)
                    plt.plot(alldatesticks_no3_13, second, c='grey')
                    plt.plot(alldatesticks_no3_13, first)
                    plt.fill_between(alldatesticks_no3_13, second, first, facecolor='grey', alpha=0.1)
                    plt.xticks(alldatesticks_no3_13)
                plt.title("Pressure", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Pressure', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()
            elif ind == "Влажность":
                if filename.endswith('.csv'):
                    plt.scatter(alldatesticks, second)
                    plt.scatter(alldatesticks, first)
                    plt.plot(alldatesticks, second, c='blue')
                    plt.plot(alldatesticks, first)
                    plt.fill_between(alldatesticks, second, first, facecolor='m', alpha=0.1)
                    plt.xticks(alldatesticks)
                elif filename.endswith('.json'):
                    plt.scatter(alldatesticks_no3_13, second)
                    plt.scatter(alldatesticks_no3_13, first)
                    plt.plot(alldatesticks_no3_13, second, c='blue')
                    plt.plot(alldatesticks_no3_13, first)
                    plt.fill_between(alldatesticks_no3_13, second, first, facecolor='m', alpha=0.1)
                    plt.xticks(alldatesticks_no3_13)
                plt.title("Humidity", fontsize=24)
                plt.xlabel('', fontsize=16)
                plt.ylabel('Humidity', fontsize=16)
                fig.autofmt_xdate()
                plt.grid(True)
                plt.tick_params(axis='both', which='major', labelsize=16)
                fig.canvas.draw()


def DS18B20func():
    def DS():
        global TestPribor
        TestPribor = "DS18B20"
        DS_buttons()

    return DS


def BMP280func():
    def BMP280():
        global TestPribor
        TestPribor = "BMP280"
        BMP280_buttons()

    return BMP280


def BME280func():
    def BME280():
        global TestPribor
        TestPribor = "BME280"
        add_all_buttons()

    return BME280


def AM2321func():
    def AM():
        global TestPribor
        TestPribor = "AM2321"
        AM2321_buttons()

    return AM


def Draw():
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=0, column=0)


def DS_buttons():
    delete_buttons()
    DSbutt = Button(root, text="Температура", name='tempbutt', command=chooseuserindication("Температура")).place(
        x=1730, y=150)
    DSaverage_button = Button(root, text="Средняя температура за час", name='temp1butt',
                              command=averagetemp(1)).place(
        x=1730, y=200)

    DSaverage3_button = Button(root, text="Средняя температура за 3 часа", name='temp3butt',
                               command=averagetemp(3)).place(x=1730, y=250)

    DSaverage24_button = Button(root, text="Средняя температура за сутки", name='temp24butt',
                                command=averagetemp(24)).place(x=1730, y=300)


def BMP280_buttons():
    delete_buttons()
    BMP1 = Button(root, text="Температура", name='tempbutt', command=chooseuserindication("Температура")).place(
        x=1730, y=150)
    BMP5 = Button(root, text="Давление", name='pressbutt', command=chooseuserindication("Давление")).place(
        x=1730, y=200)
    BMP2 = Button(root, text="Средняя температура за час", name='temp1butt',
                  command=averagetemp(1)).place(
        x=1730, y=250)
    BMP6 = Button(root, text="Среднее давление за час", name='press1butt',
                  command=averagepress(1)).place(
        x=1730, y=300)
    BMP3 = Button(root, text="Средняя температура за 3 часа", name='temp3butt',
                  command=averagetemp(3)).place(x=1730, y=350)
    BMP7 = Button(root, text="Среднее давление за 3 часа", name='press3butt',
                  command=averagepress(3)).place(x=1730, y=400)
    BMP4 = Button(root, text="Средняя температура за сутки", name='temp24butt',
                  command=averagetemp(24)).place(x=1730, y=450)
    BMP8 = Button(root, text="Среднее давление за сутки", name='press24butt',
                  command=averagepress(24)).place(x=1730, y=500)


def AM2321_buttons():
    delete_buttons()
    AM1 = Button(root, text="Температура", name='tempbutt', command=chooseuserindication("Температура")).place(
        x=1730, y=150)
    AM2 = Button(root, text="Влажность", name='humiditybutt',
                 command=chooseuserindication("Влажность")).place(
        x=1730, y=200)
    AM3 = Button(root, text="Средняя температура за час", name='temp1butt',
                 command=averagetemp(1)).place(
        x=1730, y=250)
    AM4 = Button(root, text="Средняя влажность за час", name='humidity1butt',
                 command=averagehumidity(1)).place(x=1730, y=300)
    AM5 = Button(root, text="Средняя температура за 3 часа", name='temp3butt',
                 command=averagetemp(3)).place(x=1730, y=350)
    AM6 = Button(root, text="Средняя влажность за 3 часа", name='humidity3butt',
                 command=averagehumidity(3)).place(x=1730,
                                                   y=400)
    AM7 = Button(root, text="Средняя температура за сутки", name='temp24butt',
                 command=averagetemp(24)).place(x=1730, y=450)
    AM8 = Button(root, text="Средняя влажность за сутки", name='humidity24butt',
                 command=averagehumidity(24)).place(x=1730,
                                                    y=500)


def add_all_buttons():
    temp_button = Button(root, text="Температура", name='tempbutt', command=chooseuserindication("Температура")).place(
        x=1730, y=150)
    pressure_button = Button(root, text="Давление", name='pressbutt', command=chooseuserindication("Давление")).place(
        x=1730, y=200)
    humidity_button = Button(root, text="Влажность", name='humiditybutt',
                             command=chooseuserindication("Влажность")).place(
        x=1730, y=250)

    tempaverage_button = Button(root, text="Средняя температура за час", name='temp1butt',
                                command=averagetemp(1)).place(
        x=1730, y=300)
    pressaverage_button = Button(root, text="Среднее давление за час", name='press1butt',
                                 command=averagepress(1)).place(
        x=1730, y=350)
    humidityaverage_button = Button(root, text="Средняя влажность за час", name='humidity1butt',
                                    command=averagehumidity(1)).place(x=1730, y=400)

    tempaverage3_button = Button(root, text="Средняя температура за 3 часа", name='temp3butt',
                                 command=averagetemp(3)).place(x=1730, y=450)
    pressaverage3_button = Button(root, text="Среднее давление за 3 часа", name='press3butt',
                                  command=averagepress(3)).place(x=1730, y=500)
    humidityaverage3_button = Button(root, text="Средняя влажность за 3 часа", name='humidity3butt',
                                     command=averagehumidity(3)).place(x=1730,
                                                                       y=550)
    tempaverage24_button = Button(root, text="Средняя температура за сутки", name='temp24butt',
                                  command=averagetemp(24)).place(x=1730, y=600)
    pressaverage24_button = Button(root, text="Среднее давление за сутки", name='press24butt',
                                   command=averagepress(24)).place(x=1730, y=650)
    humidityaverage24_button = Button(root, text="Средняя влажность за сутки", name='humidity24butt',
                                      command=averagehumidity(24)).place(x=1730,
                                                                         y=700)


def add_three_buttons():
    temp_button = Button(root, text="Температура", name='tempbutt', command=chooseuserindication("Температура")).place(
        x=1730, y=150)
    pressure_button = Button(root, text="Давление", name='pressbutt', command=chooseuserindication("Давление")).place(
        x=1730, y=200)
    humidity_button = Button(root, text="Влажность", name='humiditybutt',
                             command=chooseuserindication("Влажность")).place(
        x=1730, y=250)


def delete_buttons():
    global global_date, global_date2
    lst = root.place_slaves()
    for l in lst:
        if (l.winfo_name() == 'tempbutt' or l.winfo_name() == 'pressbutt' or l.winfo_name() == 'humiditybutt' or
                l.winfo_name() == 'temp1butt' or l.winfo_name() == 'press1butt' or l.winfo_name() == 'humidity1butt' or
                l.winfo_name() == 'temp3butt' or l.winfo_name() == 'press3butt' or l.winfo_name() == 'humidity3butt' or
                l.winfo_name() == 'temp24butt' or l.winfo_name() == 'press24butt' or l.winfo_name() == 'humidity24butt'):
            l.destroy()


def onlyonedates():
    global pribor
    if pribor == 'Rosa':
        spisok = [dates[0]]
        for i in range(len(dates)):
            if dates[i] == spisok[i]:
                continue
            else:
                spisok.append(dates[i])

        return spisok
    elif pribor == 'Test':
        spisok = [datesTest[0]]
        for i in range(len(datesTest)):
            if datesTest[i] == spisok[i]:
                continue
            else:
                spisok.append(datesTest[i])
        return spisok
    else:
        mb.showerror(title='ОШИБКА!', message='Вы выбрали неправильный csv файл!')


def only_time():
    global pribor
    if pribor == 'Rosa':
        temp_time_spisok = []
        for test in dates:
            temp_time_spisok.append(test.strftime("%H"))
            temp_time_spisok.append(test.strftime("%M"))
            temp_time_spisok.append(test.strftime("%S"))

        temp_time = ''
        final_time = []
        temp_time_spisok.reverse()
        for x in range(1, len(temp_time_spisok)):
            temp_time += temp_time_spisok.pop()
            temp_time += ' '
            if (x % 3 == 0) and (x != 0):
                final_time.append(temp_time)
                temp_time = ''
        return final_time

    elif pribor == 'Test':
        temp_time_spisok = []
        for test in datesTest:
            temp_time_spisok.append(test.strftime("%H"))
            temp_time_spisok.append(test.strftime("%M"))
            temp_time_spisok.append(test.strftime("%S"))

        temp_time = ''
        final_time = []
        temp_time_spisok.reverse()
        for x in range(1, len(temp_time_spisok)):
            temp_time += temp_time_spisok.pop()
            temp_time += ' '
            if (x % 3 == 0) and (x != 0):
                final_time.append(temp_time)
                temp_time = ''
        return final_time


def only_date():
    global pribor
    if pribor == 'Rosa':
        temp_date = []
        for test in dates:
            temp_date.append(test.strftime("%Y"))
            temp_date.append(test.strftime("%m"))
            temp_date.append(test.strftime("%d"))
        temp = ''
        final_date = []
        temp_date.reverse()
        for x in range(1, len(temp_date)):
            temp += temp_date.pop()
            temp += ' '
            if (x % 3 == 0) and (x != 0):
                final_date.append(temp)
                temp = ''
        return final_date

    elif pribor == "Test":
        temp_date = []
        for test in datesTest:
            temp_date.append(test.strftime("%Y"))
            temp_date.append(test.strftime("%m"))
            temp_date.append(test.strftime("%d"))

        temp = ''
        final_date = []
        temp_date.reverse()
        for x in range(1, len(temp_date)):
            temp += temp_date.pop()
            temp += ' '
            if (x % 3 == 0) and (x != 0):
                final_date.append(temp)
                temp = ''
        return final_date


def minmaxind(trigger):
    def minmax():
        global pribor, TestPribor, global_date
        fig.clf()
        if pribor == "Rosa":
            if trigger == "Т":
                delete_buttons()
                temp = []
                mini = []
                maxi = []
                temps = int(len(temperature) / 25)
                save = temps
                jj = 0
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                            continue
                    for j in range(jj, temps):
                        temp.append(temperature[j])
                    mini.append(min(temp))
                    maxi.append(max(temp))
                    temp.clear()
                    jj = temps
                    temps += save
                plotfunc(mini, maxi, "", "allind", "Температура", "minmax")
            if trigger == "Д":
                delete_buttons()
                press = []
                mini = []
                maxi = []
                presss = int(len(pressure) / 25)
                save = presss
                jj = 0
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                            continue
                    for j in range(jj, presss):
                        press.append(pressure[j])
                    mini.append(min(press))
                    maxi.append(max(press))
                    press.clear()
                    jj = presss
                    presss += save
                plotfunc(mini, maxi, "", "allind", "Давление", "minmax")
            if trigger == "В":
                delete_buttons()
                humi = []
                mini = []
                maxi = []
                humii = int(len(humidity) / 25)
                save = humii
                jj = 0
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                            continue
                    for j in range(jj, humii):
                        humi.append(humidity[j])
                    mini.append(min(humi))
                    maxi.append(max(humi))
                    humi.clear()
                    jj = humii
                    humii += save
                plotfunc(mini, maxi, "", "allind", "Влажность", "minmax")
        elif pribor == "Test":
            if TestPribor == "DS18B20":
                if trigger == "Т":
                    delete_buttons()
                    temp = []
                    mini = []
                    maxi = []
                    temps = int(len(DS18B20_temp) / 25)
                    save = temps
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, temps):
                            temp.append(DS18B20_temp[j])
                        mini.append(min(temp))
                        maxi.append(max(temp))
                        temp.clear()
                        jj = temps
                        temps += save
                    plotfunc(mini, maxi, "", "allind", "Температура", "minmax")
                elif trigger == "Д":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                elif trigger == "В":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BMP280":
                if trigger == "Т":
                    delete_buttons()
                    temp = []
                    mini = []
                    maxi = []
                    temps = int(len(BMP280_temp) / 25)
                    save = temps
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, temps):
                            temp.append(BMP280_temp[j])
                        mini.append(min(temp))
                        maxi.append(max(temp))
                        temp.clear()
                        jj = temps
                        temps += save
                    plotfunc(mini, maxi, "", "allind", "Температура", "minmax")
                elif trigger == "Д":
                    delete_buttons()
                    press = []
                    mini = []
                    maxi = []
                    presss = int(len(BMP280_pressure) / 25)
                    save = presss
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, presss):
                            press.append(BMP280_pressure[j])
                        mini.append(min(press))
                        maxi.append(max(press))
                        press.clear()
                        jj = presss
                        presss += save
                    plotfunc(mini, maxi, "", "allind", "Давление", "minmax")
                elif trigger == "В":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BME280":
                if trigger == "Т":
                    delete_buttons()
                    temp = []
                    mini = []
                    maxi = []
                    temps = int(len(BME280_temp) / 25)
                    save = temps
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, temps):
                            temp.append(BME280_temp[j])
                        mini.append(min(temp))
                        maxi.append(max(temp))
                        temp.clear()
                        jj = temps
                        temps += save
                    plotfunc(mini, maxi, "", "allind", "Температура", "minmax")
                if trigger == "Д":
                    delete_buttons()
                    press = []
                    mini = []
                    maxi = []
                    presss = int(len(BME280_pressure) / 25)
                    save = presss
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, presss):
                            press.append(BME280_pressure[j])
                        mini.append(min(press))
                        maxi.append(max(press))
                        press.clear()
                        jj = presss
                        presss += save
                    plotfunc(mini, maxi, "", "allind", "Давление", "minmax")
                if trigger == "В":
                    delete_buttons()
                    humi = []
                    mini = []
                    maxi = []
                    humii = int(len(BME280_humidity) / 25)
                    save = humii
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, humii):
                            humi.append(BME280_humidity[j])
                        mini.append(min(humi))
                        maxi.append(max(humi))
                        humi.clear()
                        jj = humii
                        humii += save
                    plotfunc(mini, maxi, "", "allind", "Влажность", "minmax")
            elif TestPribor == "AM2321":
                if trigger == "Т":
                    delete_buttons()
                    temp = []
                    mini = []
                    maxi = []
                    temps = int(len(AM2321_temp) / 25)
                    save = temps
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, temps):
                            temp.append(AM2321_temp[j])
                        mini.append(min(temp))
                        maxi.append(max(temp))
                        temp.clear()
                        jj = temps
                        temps += save
                    plotfunc(mini, maxi, "", "allind", "Температура", "minmax")
                if trigger == "Д":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                if trigger == "В":
                    delete_buttons()
                    humi = []
                    mini = []
                    maxi = []
                    humii = int(len(AM2321_humidity) / 25)
                    save = humii
                    jj = 0
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04 " or alldatestickswithout[i] == "2019 11 13 ":
                                continue
                        for j in range(jj, humii):
                            humi.append(AM2321_humidity[j])
                        mini.append(min(humi))
                        maxi.append(max(humi))
                        humi.clear()
                        jj = humii
                        humii += save
                    plotfunc(mini, maxi, "", "allind", "Влажность", "minmax")

    return minmax


def allindications(list):
    def allind():
        delete_buttons()
        global pribor, TestPribor, startt, endd
        if pribor == "Rosa":
            if list == "Температура":
                fig.clf()
                alltimes = only_time()
                temp = []
                timee = []
                while len(alltimes) != len(temperature):
                    if len(alltimes) > len(temperature):
                        alltimes.pop()
                    else:
                        temperature.pop()

                for j in range(0, len(alltimes), 25):
                    temp.append(temperature[j])
                    timee.append(alltimes[j])
                plotfunc(timee, temp, "", "allind", "Температура", "simple")
            elif list == "Давление":
                fig.clf()
                alltimes = only_time()
                press = []
                timee = []
                while len(alltimes) != len(pressure):
                    if len(alltimes) > len(pressure):
                        alltimes.pop()
                    else:
                        pressure.pop()

                for j in range(0, len(alltimes), 15):
                    press.append(pressure[j])
                    timee.append(alltimes[j])
                plotfunc(timee, press, "", "allind", "Давление", "simple")

            elif list == "Влажность":
                fig.clf()
                alltimes = only_time()
                humi = []
                timee = []
                while len(alltimes) != len(humidity):
                    if len(alltimes) > len(humidity):
                        alltimes.pop()
                    else:
                        humidity.pop()

                for j in range(0, len(alltimes), 15):
                    humi.append(humidity[j])
                    timee.append(alltimes[j])

                plotfunc(timee, humi, "", "allind", "Влажность", "simple")
        elif pribor == "Test":
            delete_buttons()
            if TestPribor == "DS18B20":
                if list == "Температура":
                    fig.clf()
                    alltimes = only_time()
                    temp = []
                    timee = []
                    while len(alltimes) != len(DS18B20_temp):
                        if len(alltimes) > len(DS18B20_temp):
                            alltimes.pop()
                        else:
                            DS18B20_temp.pop()

                    for j in range(0, len(alltimes), 50):
                        temp.append(DS18B20_temp[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, temp, "", "allind", "Температура", "simple")
                elif list == "Давление":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                elif list == "Влажность":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BMP280":
                if list == "Температура":
                    fig.clf()
                    alltimes = only_time()
                    temp = []
                    timee = []
                    while len(alltimes) != len(BMP280_temp):
                        if len(alltimes) > len(BMP280_temp):
                            alltimes.pop()
                        else:
                            BMP280_temp.pop()

                    for j in range(0, len(alltimes), 50):
                        temp.append(BMP280_temp[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, temp, "", "allind", "Температура", "simple")

                elif list == "Давление":
                    fig.clf()
                    alltimes = only_time()
                    press = []
                    timee = []
                    while len(alltimes) != len(BMP280_pressure):
                        if len(alltimes) > len(BMP280_pressure):
                            alltimes.pop()
                        else:
                            BMP280_pressure.pop()

                    for j in range(0, len(alltimes), 50):
                        press.append(BMP280_pressure[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, press, "", "allind", "Давление", "simple")
                elif list == "Влажность":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BME280":
                if list == "Температура":
                    fig.clf()
                    alltimes = only_time()
                    temp = []
                    timee = []
                    while len(alltimes) != len(BME280_temp):
                        if len(alltimes) > len(BME280_temp):
                            alltimes.pop()
                        else:
                            BME280_temp.pop()

                    for j in range(0, len(alltimes), 50):
                        temp.append(BME280_temp[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, temp, "", "allind", "Температура", "simple")
                elif list == "Давление":
                    fig.clf()
                    alltimes = only_time()
                    press = []
                    timee = []
                    while len(alltimes) != len(BME280_pressure):
                        if len(alltimes) > len(BME280_pressure):
                            alltimes.pop()
                        else:
                            BME280_pressure.pop()

                    for j in range(0, len(alltimes), 50):
                        press.append(BME280_pressure[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, press, "", "allind", "Давление", "simple")
                elif list == "Влажность":
                    fig.clf()
                    alltimes = only_time()
                    humi = []
                    timee = []
                    while len(alltimes) != len(BME280_humidity):
                        if len(alltimes) > len(BME280_humidity):
                            alltimes.pop()
                        else:
                            BME280_humidity.pop()

                    for j in range(0, len(alltimes), 50):
                        humi.append(BME280_humidity[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, humi, "", "allind", "Влажность", "simple")
            elif TestPribor == "AM2321":
                if list == "Температура":
                    fig.clf()
                    alltimes = only_time()
                    temp = []
                    timee = []
                    while len(alltimes) != len(AM2321_temp):
                        if len(alltimes) > len(AM2321_temp):
                            alltimes.pop()
                        else:
                            AM2321_temp.pop()

                    for j in range(0, len(alltimes), 50):
                        temp.append(AM2321_temp[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, temp, "", "allind", "Температура", "simple")
                elif list == "Давление":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                elif list == "Влажность":
                    fig.clf()
                    alltimes = only_time()
                    humi = []
                    timee = []
                    while len(alltimes) != len(AM2321_humidity):
                        if len(alltimes) > len(AM2321_humidity):
                            alltimes.pop()
                        else:
                            AM2321_humidity.pop()

                    for j in range(0, len(alltimes), 50):
                        humi.append(AM2321_humidity[j])
                        timee.append(alltimes[j])

                    plotfunc(timee, humi, "", "allind", "Влажность", "simple")

    return allind


def allindicationsaverage(list):
    def allind():
        delete_buttons()
        global pribor, TestPribor, global_date
        if pribor == "Rosa":
            if list == "Температура":
                fig.clf()
                temp = []
                dates = []
                j = 0
                rangerover = int(len(temperature) / len(alldatestickswithout))
                save = rangerover
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                            continue
                    count = 0
                    for j in range(rangerover):
                        count += temperature[j]
                    global_date = alldatestickswithout[i]
                    count = count / (j + 1)
                    temp.append(count)
                    dates.append(global_date)
                    j = rangerover
                    rangerover += save
                plotfunc(dates, temp, "", "allind", "Температура", "average")
            elif list == "Давление":
                fig.clf()
                press = []
                dates = []
                j = 0
                rangerover = int(len(pressure) / len(alldatestickswithout))
                save = rangerover
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                            continue
                    count = 0
                    for j in range(rangerover):
                        count += pressure[j]
                    global_date = alldatestickswithout[i]
                    count = count / (j + 1)
                    press.append(count)
                    dates.append(global_date)
                    j = rangerover
                    rangerover += save
                plotfunc(dates, press, "", "allind", "Давление", "average")
            elif list == "Влажность":
                fig.clf()
                humi = []
                dates = []
                j = 0
                rangerover = int(len(humidity) / len(alldatestickswithout))
                save = rangerover
                for i in range(len(alldatestickswithout)):
                    if filename.endswith('.json'):
                        if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                            continue
                    count = 0
                    for j in range(rangerover):
                        count += humidity[j]
                    global_date = alldatestickswithout[i]
                    count = count / (j + 1)
                    humi.append(count)
                    dates.append(global_date)
                    j = rangerover
                    rangerover += save
                plotfunc(dates, humi, "", "allind", "Влажность", "average")
        elif pribor == "Test":
            delete_buttons()
            if TestPribor == "DS18B20":
                if list == "Температура":
                    fig.clf()
                    temp = []
                    dates = []
                    j = 0

                    rangerover = int(len(DS18B20_temp) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += DS18B20_temp[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        temp.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, temp, "", "allind", "Температура", "average")
                elif list == "Давление":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                elif list == "Влажность":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BMP280":
                if list == "Температура":
                    fig.clf()
                    temp = []
                    dates = []
                    j = 0
                    rangerover = int(len(BMP280_temp) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += BMP280_temp[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        temp.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, temp, "", "allind", "Температура", "average")
                elif list == "Давление":
                    fig.clf()
                    press = []
                    dates = []
                    j = 0
                    rangerover = int(len(BMP280_pressure) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += BMP280_pressure[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        press.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, press, "", "allind", "Давление", "average")
                elif list == "Влажность":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний влажности")
            elif TestPribor == "BME280":
                if list == "Температура":
                    fig.clf()
                    temp = []
                    dates = []
                    j = 0
                    rangerover = int(len(BME280_temp) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += BME280_temp[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        temp.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, temp, "", "allind", "Температура", "average")
                elif list == "Давление":
                    fig.clf()
                    press = []
                    dates = []
                    j = 0
                    rangerover = int(len(BME280_pressure) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += BME280_pressure[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        press.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, press, "", "allind", "Давление", "average")
                elif list == "Влажность":
                    fig.clf()
                    humi = []
                    dates = []
                    j = 0
                    rangerover = int(len(BME280_humidity) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += BME280_humidity[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        humi.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, humi, "", "allind", "Влажность", "average")
            elif TestPribor == "AM2321":
                if list == "Температура":
                    fig.clf()
                    temp = []
                    dates = []
                    j = 0
                    rangerover = int(len(AM2321_temp) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += AM2321_temp[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        temp.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, temp, "", "allind", "Температура", "average")
                elif list == "Давление":
                    mb.showerror(title="Ошибка", message="У данного прибора нет показаний давления")
                elif list == "Влажность":
                    fig.clf()
                    humi = []
                    dates = []
                    j = 0
                    rangerover = int(len(AM2321_humidity) / len(alldatestickswithout))
                    save = rangerover
                    for i in range(len(alldatestickswithout)):
                        if filename.endswith('.json'):
                            if alldatestickswithout[i] == "2019 11 04" or alldatestickswithout[i] == "2019 11 13":
                                continue
                        count = 0
                        for j in range(rangerover):
                            count += AM2321_humidity[j]
                        global_date = alldatestickswithout[i]
                        count = count / (j + 1)
                        humi.append(count)
                        dates.append(global_date)
                        j = rangerover
                        rangerover += save
                    plotfunc(dates, humi, "", "allind", "Влажность", "average")

    return allind


def certaindateandtemp():
    global global_date, pribor, TestPribor
    alldates = only_date()
    alltimes = only_time()
    certaindatespisok = []
    certaintime = []
    for i in range(len(alldates)):
        if pribor == "Rosa":
            if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                certaindatespisok.append(temperature[i])
                certaintime.append(alltimes[i])
        elif pribor == "Test":
            if TestPribor == "DS18B20":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(DS18B20_temp[i])
                    certaintime.append(alltimes[i])
            elif TestPribor == "BMP280":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(BMP280_temp[i])
                    certaintime.append(alltimes[i])
            elif TestPribor == "BME280":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(BME280_temp[i])
                    certaintime.append(alltimes[i])
            elif TestPribor == "AM2321":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(AM2321_temp[i])
                    certaintime.append(alltimes[i])
    return certaindatespisok


def certaindateandpressure():
    global global_date, pribor, TestPribor
    alldates = only_date()
    alltimes = only_time()
    certaindatespisok = []
    for i in range(len(alldates)):
        if pribor == "Rosa":
            if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                certaindatespisok.append(pressure[i])

        elif pribor == "Test":

            if TestPribor == "BMP280":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(BMP280_pressure[i])

            elif TestPribor == "BME280":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(BME280_pressure[i])

    return certaindatespisok


def certaindateandhumidity():
    global global_date, pribor, TestPribor
    alldates = only_date()
    alltimes = only_time()
    certaindatespisok = []
    for i in range(len(alldates)):
        if pribor == "Rosa":
            if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                certaindatespisok.append(humidity[i])
        elif pribor == "Test":
            if TestPribor == "BME280":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(BME280_humidity[i])

            elif TestPribor == "AM2321":
                if (global_date == alldates[i]) and (alltimes[i] > '00 00 00') and (alltimes[i] < '24 00 00'):
                    certaindatespisok.append(AM2321_humidity[i])

    return certaindatespisok


def certain_date_temperatureuserdate(date, start, end, trigger):
    global global_date, pribor, TestPribor
    if trigger == 0:
        certaindatetemp = []
        certaintime = []
        alldates = only_date()
        alltimes = only_time()
        for i in range(len(alldates)):
            if pribor == "Rosa":
                if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                    certaindatetemp.append(temperature[i])
                    certaintime.append(alltimes[i])
            elif pribor == "Test":
                if TestPribor == "DS18B20":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatetemp.append(DS18B20_temp[i])
                        certaintime.append(alltimes[i])
                elif TestPribor == "BMP280":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatetemp.append(BMP280_temp[i])
                        certaintime.append(alltimes[i])
                elif TestPribor == "BME280":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatetemp.append(BME280_temp[i])
                        certaintime.append(alltimes[i])
                elif TestPribor == "AM2321":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatetemp.append(AM2321_temp[i])
                        certaintime.append(alltimes[i])
        return certaindatetemp, certaintime

    if trigger == 1:
        certaindatetemp = []
        daytemperature = certaindateandtemp()
        count = int(float(len(daytemperature) / 25))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(25):
            for j in range(itera, counter):
                alltemp += daytemperature[j]
            certaindatetemp.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatetemp

    if trigger == 3:
        certaindatetemp = []
        daytemperature = certaindateandtemp()
        count = int(float(len(daytemperature) / 9))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(int(9)):
            for j in range(itera, counter):
                alltemp += daytemperature[j]
            certaindatetemp.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatetemp

    if trigger == 24:
        certaindatetemp = []
        daytemperature = certaindateandtemp()
        alltemp = 0
        for i in range(len(daytemperature)):
            alltemp += daytemperature[i]

        certaindatetemp.append(alltemp / len(daytemperature))

        return certaindatetemp


def certain_date_pressureuserdate(date, start, end, trigger):
    global pribor, TestPribor
    if trigger == 0:
        certaindatepressure = []
        certaintime = []
        alldates = only_date()
        alltimes = only_time()
        for i in range(len(alldates)):
            if pribor == "Rosa":
                if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                    certaindatepressure.append(pressure[i])
                    certaintime.append(alltimes[i])
            elif pribor == "Test":
                if TestPribor == "BMP280":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatepressure.append(BMP280_pressure[i])
                        certaintime.append(alltimes[i])
                elif TestPribor == "BME280":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatepressure.append(BME280_pressure[i])
                        certaintime.append(alltimes[i])
        return certaindatepressure, certaintime

    if trigger == 1:
        certaindatepress = []
        daypress = certaindateandpressure()
        count = int(float(len(daypress) / 25))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(25):
            for j in range(itera, counter):
                alltemp += daypress[j]
            certaindatepress.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatepress

    if trigger == 3:
        certaindatepress = []
        daypress = certaindateandpressure()
        count = int(float(len(daypress) / 9))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(int(9)):
            for j in range(itera, counter):
                alltemp += daypress[j]
            certaindatepress.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatepress

    if trigger == 24:
        certaindatepress = []
        daypress = certaindateandpressure()
        alltemp = 0
        for i in range(len(daypress)):
            alltemp += daypress[i]

        certaindatepress.append(alltemp / len(daypress))

        return certaindatepress


def certain_date_humidityuserdate(date, start, end, trigger):
    global pribor, TestPribor
    if trigger == 0:
        certaindatehumidity = []
        certaintime = []
        alldates = only_date()
        alltimes = only_time()
        for i in range(len(alldates)):
            if pribor == "Rosa":
                if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                    certaindatehumidity.append(humidity[i])
                    certaintime.append(alltimes[i])
            elif pribor == "Test":

                if TestPribor == "BME280":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatehumidity.append(BME280_humidity[i])
                        certaintime.append(alltimes[i])
                if TestPribor == "AM2321":
                    if (date == alldates[i]) and (alltimes[i] > start) and (alltimes[i] < end):
                        certaindatehumidity.append(AM2321_humidity[i])
                        certaintime.append(alltimes[i])
        return certaindatehumidity, certaintime

    if trigger == 1:
        certaindatehumidity = []
        dayhumidity = certaindateandhumidity()
        count = int(float(len(dayhumidity) / 25))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(25):
            for j in range(itera, counter):
                alltemp += dayhumidity[j]
            certaindatehumidity.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatehumidity

    if trigger == 3:
        certaindatehumidity = []
        dayhumidity = certaindateandhumidity()
        count = int(float(len(dayhumidity) / 9))
        itera = 0
        alltemp = 0
        counter = count
        for i in range(int(9)):
            for j in range(itera, counter):
                alltemp += dayhumidity[j]
            certaindatehumidity.append(alltemp / count)
            alltemp = 0
            itera = counter
            counter += count

        return certaindatehumidity

    if trigger == 24:
        certaindatehumidity = []
        dayhumidity = certaindateandhumidity()
        alltemp = 0
        for i in range(len(dayhumidity)):
            alltemp += dayhumidity[i]

        certaindatehumidity.append(alltemp / len(dayhumidity))

        return certaindatehumidity


def checktime(value):
    if "00 00 00" in value:
        value = "00:00:00"
        return value
    if "01 00 00" in value:
        value = "01:00:00"
        return value
    if "02" in value:
        value = "02:00:00"
        return value
    if "03" in value:
        value = "03:00:00"
        return value
    if "04" in value:
        value = "04:00:00"
        return value
    if "05" in value:
        value = "05:00:00"
        return value
    if "06" in value:
        value = "06:00:00"
        return value
    if "07" in value:
        value = "07:00:00"
        return value
    if "08" in value:
        value = "08:00:00"
        return value
    if "09" in value:
        value = "09:00:00"
        return value
    if "10" in value:
        value = "10:00:00"
        return value
    if "11" in value:
        value = "11:00:00"
        return value
    if "12" in value:
        value = "12:00:00"
        return value
    if "13" in value:
        value = "13:00:00"
        return value
    if "14" in value:
        value = "14:00:00"
        return value
    if "15" in value:
        value = "15:00:00"
        return value
    if "16" in value:
        value = "16:00:00"
        return value
    if "17" in value:
        value = "17:00:00"
        return value
    if "18" in value:
        value = "18:00:00"
        return value
    if "19" in value:
        value = "19:00:00"
        return value
    if "20" in value:
        value = "20:00:00"
        return value
    if "21" in value:
        value = "21:00:00"
        return value
    if "22" in value:
        value = "22:00:00"
        return value
    if "23" in value:
        value = "23:00:00"
        return value
    if "24" in value:
        value = "24:00:00"
        return value


def ticksnumber(start, end):
    number = [checktime(start)]
    for i in ticksallwithout:
        if (i >= start) and (i <= end):
            number.append(checktime(i))
    return number


def chooseusertimestart(start):
    def chooseusertimestart_():
        global startt
        startt = start

    return chooseusertimestart_


def chooseusertimeend(end):
    def chooseusertimeend_():
        global pribor, endd
        if pribor == "Rosa":
            delete_buttons()
            add_three_buttons()
            endd = end
        elif pribor == "Test":
            delete_buttons()
            temp_button = Button(root, text="Температура", name='tempbutt',
                                 command=chooseuserindication("Температура")).place(x=1730, y=150)
            endd = end

    return chooseusertimeend_


def chooseuserdate(date):
    def chooseuserdate_():
        global startt, endd, global_date, global_date2, pribor
        if pribor == "Rosa":
            delete_buttons()
            add_three_buttons()
            global_date = date
        elif pribor == "Test":
            global_date = date

    return chooseuserdate_


def chooseuserdate2(date):
    def chooseuserdate2_():
        global startt, endd, global_date, global_date2, pribor
        if pribor == "Rosa":
            delete_buttons()
            add_three_buttons()
            global_date2 = date
        elif pribor == "Test":
            global_date2 = date

        if startt == "" or endd == "":
            mb.showerror(title="Ошибка",
                         message="Сначала выберите начальное и конечное время!")

    return chooseuserdate2_


def standard_for_one_day(date):
    def std():
        global startt, endd, global_date, global_date2, pribor, TestPribor
        if pribor == "Rosa":
            # winsound.Beep(freq, dur)
            add_all_buttons()
            global_date2 = ""
            global_date = date
            startt = "00 00 00"
            endd = "24 00 00"
        elif pribor == "Test":
            delete_buttons()
            # winsound.Beep(freq, dur)
            global_date2 = ""
            global_date = date
            startt = "00 00 00"
            endd = "24 00 00"
            if TestPribor == "DS18B20":
                DS_buttons()
            elif TestPribor == "BMP280":
                BMP280_buttons()
            elif TestPribor == "BME280":
                add_all_buttons()
            elif TestPribor == "AM2321":
                AM2321_buttons()

    return std


def reverse_to_pressure(start, end):
    global global_date
    fig.clf()
    finaldatestr = global_date
    finaltimestart = start
    finaltimeend = end
    daypressure, final_time = certain_date_pressureuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    plotfunc(final_time, daypressure, "", 'single', "Давление", "")


def reverse_to_humidity(start, end):
    global global_date
    fig.clf()
    finaldatestr = global_date
    finaltimestart = start
    finaltimeend = end
    dayhumidity, final_time = certain_date_humidityuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    plotfunc(final_time, dayhumidity, "", 'single', "Влажность", "")


def chooseuserindication(string):
    def viewparams():
        global global_date2
        if string == "Температура" and global_date2 == "":
            reverse_to_temperature(startt, endd)
        if string == "Давление" and global_date2 == "":
            reverse_to_pressure(startt, endd)
        if string == "Влажность" and global_date2 == "":
            reverse_to_humidity(startt, endd)

        if string == "Температура" and global_date2 != "":
            reverse_to_temperature2(startt, endd)
        if string == "Давление" and global_date2 != "":
            reverse_to_pressure2(startt, endd)
        if string == "Влажность" and global_date2 != "":
            reverse_to_humidity2(startt, endd)

    return viewparams


def reverse_to_temperature(usertimestart, usertimeend):
    global global_date
    fig.clf()
    finaldatestr = global_date
    finaltimestart = usertimestart
    finaltimeend = usertimeend
    daytemp, final_time = certain_date_temperatureuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    plotfunc(final_time, daytemp, "", 'single', "Температура", "")


def reverse_to_temperature2(usertimestart, usertimeend):
    global global_date, global_date2, startt, endd
    fig.clf()
    finaldatestr = global_date
    finaldatestr2 = global_date2
    finaltimestart = usertimestart
    finaltimeend = usertimeend
    daytemp, final_time = certain_date_temperatureuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    daytemp2, final_time2 = certain_date_temperatureuserdate(finaldatestr2, finaltimestart, finaltimeend, 0)

    while len(daytemp) != len(daytemp2):
        if len(daytemp) > len(daytemp2):
            daytemp.pop()
        else:
            daytemp2.pop()
    while len(final_time) != len(final_time2):
        if len(final_time) > len(final_time2):
            final_time.pop()
        else:
            final_time2.pop()
    plotfunc(final_time, daytemp, daytemp2, 'double', "Температура", "")


def reverse_to_pressure2(usertimestart, usertimeend):
    global global_date, global_date2
    fig.clf()
    finaldatestr = global_date
    finaldatestr2 = global_date2
    finaltimestart = usertimestart
    finaltimeend = usertimeend
    daypress, final_time = certain_date_pressureuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    daypress2, final_time2 = certain_date_pressureuserdate(finaldatestr2, finaltimestart, finaltimeend, 0)

    while len(daypress) != len(daypress2):
        if len(daypress) > len(daypress2):
            daypress.pop()
        else:
            daypress2.pop()
    while len(final_time) != len(final_time2):
        if len(final_time) > len(final_time2):
            final_time.pop()
        else:
            final_time2.pop()
    plotfunc(final_time, daypress, daypress2, 'double', "Давление", "")


def reverse_to_humidity2(usertimestart, usertimeend):
    global global_date, global_date2
    fig.clf()
    finaldatestr = global_date
    finaldatestr2 = global_date2
    finaltimestart = usertimestart
    finaltimeend = usertimeend
    dayhum, final_time = certain_date_humidityuserdate(finaldatestr, finaltimestart, finaltimeend, 0)
    dayhum2, final_time2 = certain_date_humidityuserdate(finaldatestr2, finaltimestart, finaltimeend, 0)

    while len(dayhum) != len(dayhum2):
        if len(dayhum) > len(dayhum2):
            dayhum.pop()
        else:
            dayhum2.pop()
    while len(final_time) != len(final_time2):
        if len(final_time) > len(final_time2):
            final_time.pop()
        else:
            final_time2.pop()
    plotfunc(final_time, dayhum, dayhum2, 'double', "Влажность", "")


def averagetemp(trigger1):
    def averagetemp_():
        global indication, global_date, fig
        if trigger1 == 1:
            fig.clf()
            indication = certain_date_temperatureuserdate(global_date, '0 00 00', '24 00 00', 1)
            plotfunc(ticksallwith, indication, "", "singlescatter", "Температура", "")

        if trigger1 == 3:
            fig.clf()
            indication = certain_date_temperatureuserdate(global_date, '0 00 00', '24 00 00', 3)
            plotfunc(ticks3hour, indication, "", "singlescatter", "Температура", "")
        if trigger1 == 24:
            fig.clf()
            indication = certain_date_temperatureuserdate(global_date, '0 00 00', '24 00 00', 24)
            plotfunc(global_date, indication, "", "singlescatter", "Температура", "")

    return averagetemp_


def averagepress(trigger):
    def averagepress_():
        global indication, global_date, fig
        if trigger == 1:
            fig.clf()
            indication = certain_date_pressureuserdate(global_date, '0 00 00', '24 00 00', 1)
            plotfunc(ticksallwith, indication, "", "singlescatter", "Давление", "")
        if trigger == 3:
            fig.clf()
            indication = certain_date_pressureuserdate(global_date, '0 00 00', '24 00 00', 3)
            plotfunc(ticks3hour, indication, "", "singlescatter", "Давление", "")
        if trigger == 24:
            fig.clf()
            indication = certain_date_pressureuserdate(global_date, '0 00 00', '24 00 00', 24)
            plotfunc(global_date, indication, "", "singlescatter", "Давление", "")

    return averagepress_


def averagehumidity(trigger):
    def averagehumidity_():
        global indication, global_date, fig
        if trigger == 1:
            fig.clf()
            indication = certain_date_humidityuserdate(global_date, '0 00 00', '24 00 00', 1)
            plotfunc(ticksallwith, indication, "", "singlescatter", "Влажность", "")
        if trigger == 3:
            fig.clf()
            indication = certain_date_humidityuserdate(global_date, '0 00 00', '24 00 00', 3)
            plotfunc(ticks3hour, indication, "", "singlescatter", "Влажность", "")
        if trigger == 24:
            fig.clf()
            indication = certain_date_humidityuserdate(global_date, '0 00 00', '24 00 00', 24)
            plotfunc(global_date, indication, "", "singlescatter", "Влажность", "")

    return averagehumidity_


filename = Start()

if filename.endswith('.csv'):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[1] == "РОСА К-2 (01)":
                open_rosa_k2(reader)
            if row[1] == "Тест Студии (schHome)":
                open_test_studii(reader)

elif filename.endswith('.json'):
    myfile = open(filename, mode='r', encoding='utf-8')
    json_data = json.load(myfile)
    for ii in json_data:
        if json_data[ii]['uName'] == "РОСА К-2":
            open_rosa_k2_json(json_data)
        elif json_data[ii]['uName'] == "Тест Студии":
            open_test_studii_json(json_data)

root = Tk()
root.overrideredirect(1)
mainmenu = Menu(root)
root.config(menu=mainmenu)
root.title("Практика Наумов")
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=delete)

choosemenu = Menu(mainmenu, tearoff=0)
choosemenu2 = Menu(choosemenu, tearoff=0)
for b in range(len(alldatesticks)):
    choosemenu2.add_command(label=alldatesticks[b], command=standard_for_one_day(alldatestickswithout[b]))

choosemenu3 = Menu(mainmenu, tearoff=0)

choosemenu4 = Menu(choosemenu3, tearoff=0)
for b in range(len(alldatesticks)):
    choosemenu4.add_command(label=alldatesticks[b], command=chooseuserdate(alldatestickswithout[b]))

choosemenu5 = Menu(choosemenu3, tearoff=0)
for b in range(len(ticksallwith)):
    choosemenu5.add_command(label=ticksallwith[b], command=chooseusertimestart(ticksallwithout[b]))

choosemenu6 = Menu(choosemenu3, tearoff=0)
for b in range(len(ticksallwith)):
    choosemenu6.add_command(label=ticksallwith[b], command=chooseusertimeend(ticksallwithout[b]))

choosemenu7 = Menu(mainmenu, tearoff=0)
choosemenu8 = Menu(choosemenu7, tearoff=0)
for b in range(len(alldatesticks)):
    choosemenu8.add_command(label=alldatesticks[b], command=chooseuserdate(alldatestickswithout[b]))

choosemenu9 = Menu(choosemenu7, tearoff=0)
for b in range(len(alldatesticks)):
    choosemenu9.add_command(label=alldatesticks[b], command=chooseuserdate2(alldatestickswithout[b]))

choosemenu10 = Menu(choosemenu7, tearoff=0)
for b in range(len(ticksallwith)):
    choosemenu10.add_command(label=ticksallwith[b], command=chooseusertimestart(ticksallwithout[b]))

choosemenu11 = Menu(choosemenu7, tearoff=0)
for b in range(len(ticksallwith)):
    choosemenu11.add_command(label=ticksallwith[b], command=chooseusertimeend(ticksallwithout[b]))

choosemenu13 = Menu(mainmenu, tearoff=0)
choosemenu13.add_command(label="Температура", command=allindications("Температура"))
choosemenu13.add_command(label="Давление", command=allindications("Давление"))
choosemenu13.add_command(label="Влажность", command=allindications("Влажность"))
choosemenu13.add_command(label="Осреднённая температура за сутки", command=allindicationsaverage("Температура"))
choosemenu13.add_command(label="Осреднённое давление за сутки", command=allindicationsaverage("Давление"))
choosemenu13.add_command(label="Осреднённая влажность за сутки", command=allindicationsaverage("Влажность"))
choosemenu13.add_command(label="Минимальная и максимальная температура", command=minmaxind("Т"))
choosemenu13.add_command(label="Минимальное и максимальное давление", command=minmaxind("Д"))
choosemenu13.add_command(label="Минимальная и максимальная влажность", command=minmaxind("В"))

mainmenu.add_cascade(label="Файл", menu=filemenu)
if AM2321_temp:
    choosemenu12 = Menu(mainmenu, tearoff=0)
    choosemenu12.add_command(label="DS18B20", command=DS18B20func())
    choosemenu12.add_command(label="BMP280", command=BMP280func())
    choosemenu12.add_command(label="BME280", command=BME280func())
    choosemenu12.add_command(label="AM2321", command=AM2321func())
    mainmenu.add_cascade(label="Выбор прибора", menu=choosemenu12)
mainmenu.add_cascade(label="Показать данные за весь день", menu=choosemenu)
choosemenu.add_cascade(label="Выбрать день", menu=choosemenu2)
mainmenu.add_cascade(label="Выбор временного промежутка", menu=choosemenu3)
mainmenu.add_cascade(label="Объединение графиков", menu=choosemenu7)
mainmenu.add_cascade(label="Показатели за всё время", menu=choosemenu13)
choosemenu3.add_cascade(label="Начальное время", menu=choosemenu5)
choosemenu3.add_cascade(label="Конечное время", menu=choosemenu6)
choosemenu3.add_cascade(label="Выбор дня для временного промежутка", menu=choosemenu4)
choosemenu7.add_cascade(label="Начальное время", menu=choosemenu10)
choosemenu7.add_cascade(label="Конечное время", menu=choosemenu11)
choosemenu7.add_cascade(label="Выбор первого дня для временного промежутка", menu=choosemenu8)
choosemenu7.add_cascade(label="Выбор второго дня для временного промежутка", menu=choosemenu9)

Draw()

root.mainloop()
