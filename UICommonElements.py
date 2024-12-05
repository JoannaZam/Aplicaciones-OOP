from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz click', on_click=lambda: ui.notify('Click'))
with ui.row():
    ui.checkbox('Acepto los terminos', on_change=show)
    ui.switch('On/Off', on_change=show)
ui.radio(['Perro', 'Gato', 'Perico'], value='Perro', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')

ui.run()