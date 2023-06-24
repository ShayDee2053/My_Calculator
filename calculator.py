import customtkinter as ctk


class Calculator(ctk.CTk):

    def __init__(self):

        super().__init__()

        color = "yellow"

        ctk.set_appearance_mode("dark")
        self.title("Calculator")
        self.geometry("485x530+650+167")
        self.resizable(width=False, height=False)

        self.form = "0"
        self.field = ctk.CTkLabel(
            self,
            anchor="w",
            text=self.form,
            text_color=color,
            width=100,
            height=100,
            font=(
                "Times New Roman",
                30,
                "bold"
            )
        )

        self.field.grid(column=0, row=0, padx=20, pady=1)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 120

        for btn in btns:
            com = lambda x=btn: self.logic(x)
            ctk.CTkButton(
                self,
                text=btn,
                text_color="yellow",
                width=115,
                height=79,
                font=("Times New Roman", 30, "bold"),
                border_width=1,
                border_color="yellow",
                command=com
            ).place(x=x, y=y)

            x += 117
            if x > 400:
                x = 10
                y += 81

    def logic(self, operation):
        if operation == "C":
            self.form = ""
        elif operation == "DEL":
            self.form = self.form[0:-1]
        elif operation == "X^2":
            self.form = str((eval(self.form)) ** 2)
        elif operation == "=":
            try:
                self.form = str(eval(self.form))
            except ZeroDivisionError:
                self.form = "Error!"
        else:
            if self.form == "0":
                self.form = ""
            self.form += operation
        self.update()

    def update(self):
        if self.form == "":
            self.form = "0"
        self.field.configure(text=self.form)


if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
