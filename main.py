from vstavki import *
from buble import *
from wiborka import *
from qsort import *
array = [12, 11, 13, 5, 6]
N=5
print(insertion_sort(N,array))#вставки
print(bubble(N,array))#пузырьком
print(sel_sort(N,array))#выборка
print(shaker_sort(N,array))#Шейкерная(быстрая)

import PySimpleGUI as sg
mda=[]
layout = [
          [sg.Text("Метод сортировки 1-Вставками, 2-Пузырьком, 3-Выборкой, 4-Шейкерная")],
          [sg.Input(key='-INPUT3-')],
          [sg.Text("Количество элементов массива")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("элемент массива")],
          [sg.Input(key='-INPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text("Отсортированный массив / затраченное время на сортировку")],
          
          [sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Button('Ok'), sg.Button('Quit')],]
window = sg.Window('Сортировочки', layout)
while True:
    event, values = window.read()
    type_of_sort=int(values['-INPUT3-'])
    N=int(values['-INPUT-'])
    print(values['-INPUT-'])
    mda.append(int(values['-INPUT2-']))
 
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Ваш массив ' + str(mda))
    if len(mda)==N:
        if type_of_sort==1:
            window['-OUTPUT2-'].update(insertion_sort(10,mda))
        if type_of_sort==2:
            window['-OUTPUT2-'].update(bubble(10,mda))
        if type_of_sort==3:
            window['-OUTPUT2-'].update(sel_sort(10,mda))
        if type_of_sort==4:
            window['-OUTPUT2-'].update(shaker_sort(10,mda))

window.close()