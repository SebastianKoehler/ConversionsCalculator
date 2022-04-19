from tkinter import Tk, Entry, Frame, Button, StringVar, END

calculation = ""
operator = ""

first_number = 0
second_number = 0
operator_count = 0
comma_count = 0

'''
17.04.22
Operationen noch nicht implementiert
Evaluierung noch nicht implementiert
0 wird beim klicken auf Komma gelöscht und , steht alleine
Wenn ich eine 0 stehen habe und auf clear_last klicke, wird auch die 0 entfernt
'''

if __name__ == "__main__":

    def check_for_comma():

        global calculation, comma_count

        inputDisplayField.config(state="normal")

        input_value = inputDisplayField.get()
        is_comma_inserted = ',' in input_value

        if is_comma_inserted is False:
            add_pressed_button_to_calculation(",")

        inputDisplayField.config(state="readonly")


    def absolute_input_value():

        global calculation
        inputDisplayField.config(state="normal")
        values = int(inputDisplayField.get())

        if values >= 0:
            absolute_value = values * -1
            inputDisplayField.delete(0, END)
            calculation = ""
            inputDisplayField.insert(END, str(absolute_value))
        if values < 0:
            absolute_value = values * -1
            inputDisplayField.delete(0, END)
            calculation = ""
            inputDisplayField.insert(END, str(absolute_value))

        inputDisplayField.config(state="readonly")


    def add_pressed_button_to_calculation(button):

        global calculation, comma_count

        inputDisplayField.config(state="normal")

        if len(inputDisplayField.get()) == 0:
            user_input.set("0")

        if button == 0:
            if inputDisplayField.get()[0] == '0':
                return
            elif inputDisplayField.get()[0] != '0':
                calculation += str(button)
                inputDisplayField.insert(END, calculation)
                calculation = ""
        elif button == ',':
            if inputDisplayField.get()[0] == '0' and comma_count == 0:
                comma_count = 1
                calculation += button
                inputDisplayField.insert(END, calculation)
                calculation = ""
            if inputDisplayField.get()[0] != '0' and comma_count == 0:
                comma_count = 1
                calculation += button
                inputDisplayField.insert(END, calculation)
                calculation = ""
        else:
            if inputDisplayField.get()[0] == '0' and comma_count == 1:
                calculation += str(button)
                inputDisplayField.insert(END, calculation)
                calculation = ""
            elif inputDisplayField.get()[0] == '0' and comma_count == 0:
                user_input.set("")
                calculation += str(button)
                inputDisplayField.insert(END, calculation)
                calculation = ""
            elif inputDisplayField.get()[0] != '0' and comma_count == 0:
                calculation += str(button)
                inputDisplayField.insert(END, calculation)
                calculation = ""
            else:
                calculation += str(button)
                inputDisplayField.insert(END, calculation)
                calculation = ""

        inputDisplayField.config(state="readonly")


    def evaluate_interim_result(operator_button):

        global calculation, operator_count, first_number, second_number

        inputDisplayField.config(state="normal")
        resultDisplayField.config(state="normal")

        operator_count += 1

        if operator_count == 1:
            eingabe1_string = inputDisplayField.get()

            is_first_number_float = ',' in eingabe1_string
            if is_first_number_float is False:
                first_number = int(eingabe1_string)
            else:
                change_comma_to_point = eingabe1_string.strip().replace(',', '.')
                first_number = float(change_comma_to_point)

            eingabe1_concatenate = eingabe1_string + " " + operator_button + " "
            resultDisplayField.insert(END, eingabe1_concatenate)
            inputDisplayField.delete(0, END)
        elif operator_count >= 2:
            eingabe2_string = inputDisplayField.get()

            is_second_number_float = ',' in eingabe2_string
            if is_second_number_float is False:
                second_number = int(eingabe2_string)
            else:
                change_comma_to_point = eingabe2_string.strip().replace(',', '.')
                first_number = float(change_comma_to_point)

            interim_result = evaluate_result()
            eingabe2_concatenate = str(interim_result) + " " + operator_button + " "
            inputDisplayField.delete(0, END)
            resultDisplayField.delete(0, END)
            resultDisplayField.insert(END, eingabe2_concatenate)
            inputDisplayField.insert(END, str(interim_result))
            inputDisplayField.delete(0, END)

        calculation = ""
        resultDisplayField.config(state="readonly")
        inputDisplayField.config(state="readonly")


    def evaluate_result():

        global calculation, operator_count, first_number, second_number, operator

        try:
            inputDisplayField.config(state="normal")
            resultDisplayField.config(state="normal")

            is_float_number_first = ',' in str(first_number)
            is_float_number_second = ',' in str(second_number)

            if is_float_number_first is True:
                change_comma_to_point = str(first_number).strip().replace(',', '.')
                first_number_converted_to_float = float(change_comma_to_point)
                first_number = first_number_converted_to_float
            else:
                remove_literals = str(first_number).strip().replace(',', '.').replace(' ', '')
                first_number_converted_to_int = int(float(remove_literals))
                first_number = first_number_converted_to_int

            if is_float_number_second is True:
                change_comma_to_point = str(second_number).strip().replace(',', '.')
                second_number_converted_to_float = float(change_comma_to_point)
                second_number = second_number_converted_to_float
            else:
                remove_literals = str(second_number).strip().replace(',', '.').replace(' ', '')
                second_number_converted_to_int = int(float(remove_literals))
                second_number = second_number_converted_to_int

            if operator == '+':
                return first_number + second_number
            elif operator == '-':
                return first_number - second_number
            elif operator == 'x':
                return first_number * second_number
            elif operator == '/':
                return first_number / second_number
            elif operator == '%':
                return first_number % second_number

        except ZeroDivisionError:
            zde_message = "ERROR, dividing with zero is not possible!"
            inputDisplayField.insert(END, zde_message)
        finally:
            calculation = ""
            operator_count = 0
            resultDisplayField.config(state="readonly")
            inputDisplayField.config(state="readonly")

    def clear_display():

        global calculation, comma_count

        inputDisplayField.config(state="normal")
        resultDisplayField.config(state="normal")

        resultDisplayField.delete(0, END)
        inputDisplayField.delete(0, END)

        inputDisplayField.insert(END, "0")

        calculation = ""
        comma_count = 0

        resultDisplayField.config(state="readonly")
        inputDisplayField.config(state="readonly")


    def clear_last():

        global calculation, comma_count

        inputDisplayField.config(state="normal")

        input_values = inputDisplayField.get()
        input_values_count = len(input_values)

        if input_values_count == 0:
            user_input.set("0")
        if input_values_count >= 1:
            if input_values_count == 1:
                last_value_index = input_values_count - 1
                inputDisplayField.delete(last_value_index, END)
                user_input.set("0")
            if input_values_count >= 2:
                second_last_value_index = input_values_count - 1
                inputDisplayField.delete(second_last_value_index, END)

        calculation = ""
        comma_count = 0
        inputDisplayField.config(state="readonly")


    # root window
    mainWindow = Tk()

    # mainWindow configuration
    mainWindow.title("Calculator & Conversions")
    mainWindow.iconbitmap('icons/monkey-icon.ico')
    mainWindow.geometry("300x350")
    mainWindow.resizable(False, False)
    mainWindow.configure(background="black")

    # String variable to get and show the pressed buttons
    user_input = StringVar()
    result_input = StringVar()

    user_input.set("0")

    # Frame:1 Display the result
    displayFrame = Frame(mainWindow, width=250, height=50, bg="grey")
    # Frame:2 Display the Input
    inputFrame = Frame(mainWindow, width=250, height=50, bg="grey")
    # Frame:3 Hold all the Buttons
    buttonFrame = Frame(mainWindow, width=250, height=50, bg="grey")

    # Result display definition
    resultDisplayField = Entry(displayFrame,
                               font=('arial', 14, 'bold'),
                               textvariable=result_input,
                               state="readonly",
                               width=19,
                               justify="right")

    # Input display definition
    inputDisplayField = Entry(inputFrame,
                              font=('arial', 14, 'bold'),
                              textvariable=user_input,
                              state="readonly",
                              width=19,
                              justify="right")

    # Buttons definition
    # 1. row
    modulo_btn = Button(buttonFrame, text="%", fg="black", bg="white", width=5, height=2,
                        command=lambda: evaluate_interim_result("%"))
    clear_btn = Button(buttonFrame, text="Clear", fg="black", bg="white", width=5, height=2,
                       command=clear_display)
    delete_btn = Button(buttonFrame, text="Del", fg="black", bg="white", width=5, height=2,
                        command=clear_last)
    division_btn = Button(buttonFrame, text="/", fg="black", bg="white", width=5, height=2,
                          command=lambda: evaluate_interim_result("/"))
    # 2. row
    seven_btn = Button(buttonFrame, text="7", fg="black", bg="white", width=5, height=2,
                       command=lambda: add_pressed_button_to_calculation(7))
    eight_btn = Button(buttonFrame, text="8", fg="black", bg="white", width=5, height=2,
                       command=lambda: add_pressed_button_to_calculation(8))
    nine_btn = Button(buttonFrame, text="9", fg="black", bg="white", width=5, height=2,
                      command=lambda: add_pressed_button_to_calculation(9))
    multiplication_btn = Button(buttonFrame, text="x", fg="black", bg="white", width=5, height=2,
                                command=lambda: evaluate_interim_result("x"))
    # 3. row
    four_btn = Button(buttonFrame, text="4", fg="black", bg="white", width=5, height=2,
                      command=lambda: add_pressed_button_to_calculation(4))
    five_btn = Button(buttonFrame, text="5", fg="black", bg="white", width=5, height=2,
                      command=lambda: add_pressed_button_to_calculation(5))
    six_btn = Button(buttonFrame, text="6", fg="black", bg="white", width=5, height=2,
                     command=lambda: add_pressed_button_to_calculation(6))
    subtraction_btn = Button(buttonFrame, text="-", fg="black", bg="white", width=5, height=2,
                             command=lambda: evaluate_interim_result("-"))
    # 4. row
    one_btn = Button(buttonFrame, text="1", fg="black", bg="white", width=5, height=2,
                     command=lambda: add_pressed_button_to_calculation(1))
    two_btn = Button(buttonFrame, text="2", fg="black", bg="white", width=5, height=2,
                     command=lambda: add_pressed_button_to_calculation(2))
    three_btn = Button(buttonFrame, text="3", fg="black", bg="white", width=5, height=2,
                       command=lambda: add_pressed_button_to_calculation(3))
    addition_btn = Button(buttonFrame, text="+", fg="black", bg="white", width=5, height=2,
                          command=lambda: evaluate_interim_result("+"))
    # 5. row
    absolute_btn = Button(buttonFrame, text="+/-", fg="black", bg="white", width=5, height=2,
                          command=absolute_input_value)
    zero_btn = Button(buttonFrame, text="0", fg="black", bg="white", width=5, height=2,
                      command=lambda: add_pressed_button_to_calculation(0))
    comma_btn = Button(buttonFrame, text=",", fg="black", bg="white", width=5, height=2,
                       command=check_for_comma)
    equals_btn = Button(buttonFrame, text="=", fg="black", bg="white", width=5, height=2,
                        command=evaluate_result)

    # Binding all widgets to the mainWindow
    # Frames
    displayFrame.pack()
    inputFrame.pack()
    buttonFrame.pack()
    # Display/Input Fields
    resultDisplayField.grid(row=0, column=0)
    inputDisplayField.grid(row=0, column=0)

    # Buttons
    # 1. row
    modulo_btn.grid(row=2, column=1, padx=1, pady=1)
    clear_btn.grid(row=2, column=2, padx=1, pady=1)
    delete_btn.grid(row=2, column=3, padx=1, pady=1)
    division_btn.grid(row=2, column=4, padx=1, pady=1)
    # 2. row
    seven_btn.grid(row=3, column=1, padx=1, pady=1)
    eight_btn.grid(row=3, column=2, padx=1, pady=1)
    nine_btn.grid(row=3, column=3, padx=1, pady=1)
    multiplication_btn.grid(row=3, column=4, padx=1, pady=1)
    # 3. row
    four_btn.grid(row=4, column=1, padx=1, pady=1)
    five_btn.grid(row=4, column=2, padx=1, pady=1)
    six_btn.grid(row=4, column=3, padx=1, pady=1)
    subtraction_btn.grid(row=4, column=4, padx=1, pady=1)
    # 4. row
    one_btn.grid(row=5, column=1, padx=1, pady=1)
    two_btn.grid(row=5, column=2, padx=1, pady=1)
    three_btn.grid(row=5, column=3, padx=1, pady=1)
    addition_btn.grid(row=5, column=4, padx=1, pady=1)
    # 5. row
    absolute_btn.grid(row=6, column=1, padx=1, pady=1)
    zero_btn.grid(row=6, column=2, padx=1, pady=1)
    comma_btn.grid(row=6, column=3, padx=1, pady=1)
    equals_btn.grid(row=6, column=4, padx=1, pady=1)

    # window event loop
    mainWindow.mainloop()
