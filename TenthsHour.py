#Tenths of an Hour Calculator GUI
#Created by John Christian
import tkinter as tk
import tkinter.ttk as ttk

class TenthsOfHourApp:
    def __init__(self, parent):
        topLevel = ttk.Frame(parent, padding=10)
        topLevel.grid(column=0, row=0)

        headerLabel = ttk.Label(topLevel, text="Stuffy's Tenths of an Hour Calculator", font="{Arial} 16 {bold}")
        headerLabel.grid(column=0, row=0, sticky="nsew")

        inputFrame = ttk.Frame(topLevel, padding=10)
        inputFrame.grid(column=0, row=1, sticky="nsew")
        minutesLabel = ttk.Label(inputFrame, text="Minutes:")

        minutesEntry = ttk.Entry(inputFrame)

        minutesLabel.grid(column=0, row=0, sticky="e")

        minutesEntry.grid(column=1, row=0, pady=3)


        buttonFrame = ttk.Frame(topLevel)
        buttonFrame.grid(column=0, row=2, sticky='nsew')
        clearButton = ttk.Button(buttonFrame, text="Clear", command=self.clear)
        okayButton = ttk.Button(buttonFrame, text="Calculate", command=self.calculate)
        clearButton.grid(column=0, row=0, padx=3)
        okayButton.grid(column=1, row=0)

        self.mainWindow = topLevel
        self.minutesEntry = minutesEntry



    def clear(self):
        # print("Clear")
        self.minutesEntry.delete(0, tk.END)


    def showAnswer(self, parent, text):
        rootFrame = ttk.Frame(parent, padding=10)
        rootFrame.grid(column=0, row=0)

        headerLabel = ttk.Label(rootFrame, text="Tenths of an Hour", font="{Arial} 14 {bold}")
        headerLabel.grid(column=0, row=0)

        answerLabel = ttk.Label(rootFrame, text=text, justify=tk.CENTER)
        answerLabel.grid(column=0, row=1)


    def calculate(self):
        # print("Calculate Tenths of an Hour: ", self.minutesEntry.get())
        try:
            minutes = float(self.minutesEntry.get())
            tenthsHour = minutes/60 * 10
        except:
            top2 = tk.Toplevel(self.mainWindow)
            self.showAnswer(top2, "Nah Nah Nah...\n" + "Nice try. Enter a Valid Number for Minutes")
            # print("Please Enter a Valid Number for Meters.")
            return;
        print(minutes, "minutes is ", tenthsHour, "tenths of an hour. ")
        top2 = tk.Toplevel(self.mainWindow)

        self.showAnswer(top2, str(minutes) + " minutes is equal to " + "{:.2f} Tenths of an Hour.".format(tenthsHour))

        return float(tenthsHour)


    def run(self):
        self.mainWindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tenths of an Hour Calculator")
    app = TenthsOfHourApp(root)
    app.run()
