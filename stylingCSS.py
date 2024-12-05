from nicegui import ui


ui.icon('thumb_up', color='#ff0000').classes('text-9xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('JOANNA').style('color: #6c6ebd; font-weight: bold; font-family: Roboto; font-size: 20px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()