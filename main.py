from tkinter import *

window = Tk()
window.title("BMI Quiz")
window.minsize(300, 200)
window.resizable(width=False, height=False)

def bmi_result():
   if weight_entry.get() == "" or height_entry.get() == "":
       result_label.config(text="Lütfen Boş Bırakmayınız!")
   else:
       try:
            weight_result = float(weight_entry.get())
            height_result = float(height_entry.get())

            bmi_calc= float(weight_result / ((height_result /100 ) ** 2))
            result = round(bmi_calc, 2)

            if bmi_calc <= 18.0:
                result_label.config(text=f"BMI = {result} Zayıf")
            elif 18.0 < bmi_calc <= 25.0:
                result_label.config(text=f"BMI = {result} Normal")
            elif 25.0 < bmi_calc <= 30.0:
                result_label.config(text=f"BMI = {result} Şişman")
            elif 30.0 < bmi_calc <= 35.0:
                result_label.config(text=f"BMI = {result} Obez")
            else:
                result_label.config(text=f"BMI = {result} Aşırı Obez")
       except ValueError:
           result_label.config(text=f"Lütfen Geçerli bir sayı giriniz.")


weight_label = Label(text = "Weight(kg)")
weight_label.grid(row = 0, column = 0)
weight_entry = Entry()
weight_entry.grid(row = 0, column = 1,padx = 10, pady = 10)

height_label = Label(text = "Height(cm)")
height_label.grid(row = 1, column = 0)
height_entry = Entry()

height_entry.grid(row = 1, column = 1,padx = 10, pady = 10)

result_button = Button(text = "BMI Result", command =bmi_result,fg = "white", bg = "red")
result_button.grid(row = 2, column = 1,padx = 10, pady = 10)

result_label = Label()
result_label.grid(row = 3, column = 1)



window.mainloop()