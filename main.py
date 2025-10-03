from flet import *

def main(page: Page):
    page.window.width=250
    page.window.height=500
    
    t1 = Text("wellcom")
    page.add(t1)

    t2 = ElevatedButton(text='press')
    page.add(t2)

    t3 = TextField()
    page.add(t3)

    t4 = Checkbox()
    page.add(t4)


if __name__ == "__main__":
    app(main)
