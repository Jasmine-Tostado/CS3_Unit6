import tkinter as tk


class Calculator:
    ORIGINAL_NUM1 = 0
    ORIGINAL_NUM2 = 0

    def __init__(self):
        self._root = tk.Tk()

        # -------------- Display a header message  ---------------
        header = "Enter 2 numbers and click Add/Subtract"
        self._header = tk.Message(self._root, text=header)
        self._header.config(bg="lightblue", width=300)

        # define two numbers that can be overwritten by user
        self._num1 = self.ORIGINAL_NUM1
        self._num2 = self.ORIGINAL_NUM2

        # ----------------- label widgets ------------------
        self._label_num1 = tk.Label(self._root, text="First Number")
        self._label_num2 = tk.Label(self._root, text="Second Number")
        self._label_answer_text = tk.Label(self._root, text="Answer")
        self._label_answer_num = tk.Label(self._root, text=" - ")

        # ----------------- entry widgets ------------------
        self._entry_num1 = tk.Entry(self._root)
        self._entry_num1.insert(0, str(self._num1))
        self._entry_num2 = tk.Entry(self._root)
        self._entry_num2.insert(0, str(self._num2))

        # ----------------- button widgets ------------------
        self._button_add = tk.Button(self._root, text="Add",
                                     command=self._add)
        self._button_subtract = tk.Button(self._root, text="Subtract",
                                          command=self._subtract)

        # ------------ place all widgets using grid layout -------------
        self._header.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.EW)

        # sticky below refers to whether the widget should "stick" to its
        # left border (tk.W, where W stands for West) or right (tk.E)
        self._label_num1.grid(row=1, column=0, sticky=tk.E)
        self._entry_num1.grid(row=1, column=1, sticky=tk.W)

        self._label_num2.grid(row=2, column=0, sticky=tk.E)
        self._entry_num2.grid(row=2, column=1, sticky=tk.W)

        self._label_answer_text.grid(row=3, column=0, sticky=tk.E)
        self._label_answer_num.grid(row=3, column=1, sticky=tk.W)

        self._button_add.grid(row=4, column=0, pady=15)
        self._button_subtract.grid(row=4, column=1, pady=15)

        # ------ update the answer using starting values ---
        self._add()

    @property
    def root(self):
        return self._root

    # event handler for add
    def _add(self):
        self._num1 = float(self._entry_num1.get())
        self._num2 = float(self._entry_num2.get())
        answer = self._num1 + self._num2
        self._label_answer_num.config(text=str(f"{answer:.2f}"))

    # event handler for subtract
    def _subtract(self):
        self._num1 = float(self._entry_num1.get())
        self._num2 = float(self._entry_num2.get())
        answer = self._num1 - self._num2
        self._label_answer_num.config(text=str(f"{answer:.2f}"))


calc = Calculator()
calc.root.title("A Simple Calculator")
calc.root.mainloop()