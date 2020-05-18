import PySimpleGUI as sg

operation_cases = ['+', '-', '*', '/']
pos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
end_cases = ['AC']
chess_pieces = ['♚', '♛']

nums_buttons = {'size': (10, 2), 'font': ('Fat Basic', 23), 'button_color': ("black", "#F8F8F8")}
symbols_buttons = {'size': (10, 2), 'font': ('Fat Basic', 23), 'button_color': ("black", "#CC0000")}
equals_button = {'size': (21, 2), 'font': ('Fat Basic', 23), 'button_color': ("black", "#660000")}
var = {'front': [], 'back': [], 'dec': False, 'x_val': 0.0, 'y_val': 0.0, 'result': 0.0, 'operator': ''}

layout = [
    [sg.Text('0.0000', size=(20, 1), justification='right', background_color='black', text_color='white', font=('Fat Basic', 60), relief='sunken', key="_DISPLAY_")],
    [sg.Button('♚', **symbols_buttons), sg.Button('♛', **symbols_buttons), sg.Button('AC', **symbols_buttons), sg.Button("/", **symbols_buttons)],
    [sg.Button('7', **nums_buttons), sg.Button('8', **nums_buttons), sg.Button('9', **nums_buttons), sg.Button("*", **symbols_buttons)],
    [sg.Button('4', **nums_buttons), sg.Button('5', **nums_buttons), sg.Button('6', **nums_buttons), sg.Button("-", **symbols_buttons)],
    [sg.Button('1', **nums_buttons), sg.Button('2', **nums_buttons), sg.Button('3', **nums_buttons), sg.Button("+", **symbols_buttons)],
    [sg.Button('0', **nums_buttons), sg.Button('.', **symbols_buttons), sg.Button('=', **equals_button, bind_return_key=True)]]

window = sg.Window(title = 'Calculator', layout = layout, background_color = "black", size = (790, 610))

def setup_nums():
    return float(''.join(var['front']) + '.' + ''.join(var['back']))

def click_nums(event):
    global var
    if var['dec']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(setup_nums())

def update_display(display_value):
    try:
        window['_DISPLAY_'].update(value = '{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value = display_value)

def click_operators(event):
    global var
    var['operator'] = event
    try:
        var['x_val'] = setup_nums()
    except:
        var['x_val'] = var['result']
    clear_cases()

def nums_calculation():
    global var
    var['y_val'] = setup_nums()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_cases()
    except:
        update_display("INVALID NUM/0  ")
        clear_cases()

def clear_cases():
    global var
    var['front'].clear()
    var['back'].clear()
    var['dec'] = False

while True:
    event, values = window.read()
    if event in pos:
        click_nums(event)
    if event == '=':
        nums_calculation()
    if event in operation_cases:
        click_operators(event)
    if event in end_cases:
        clear_cases()
        update_display(0.0)
        var['result'] = 0.0
    if event == '.':
        var['dec'] = True
    if event in chess_pieces:
        if event == chess_pieces[0]:
            update_display("KING KONG")
            clear_cases()
        else:
            update_display("QUEEN LATIFAH")
            clear_cases()
        var['result'] = 0.0
    if event is None:
        break