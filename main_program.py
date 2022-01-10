import tkinter
from tkinter import *
import fls_main

root = Tk()
root.title("Pemeriksaan COVID-19")

line1 = Label(
    root, text="Jika Anda menderita berbagai gejala COVID-19").pack()
line2 = Label(
    root, text="Program ini akan mencoba menghitung peluang kemungkinan Covid-19.").pack()
line3 = Label(
    root, text="Oleh karena itu, mohon masukan gejala atau intensitasnya.").pack()
line4 = Label(root, text="(0 adalah paling sedikit)").pack()

cough, fever, breath = DoubleVar(), DoubleVar(), DoubleVar()

cough_label = Label(root, text="Intensitas tingkat batuk.").pack()
cough_slider = Scale(root, from_=0, to=9.9, orient=HORIZONTAL,
                     resolution=0.1, variable=cough)
cough_slider.pack()

fever_label = Label(root, text="Intensitas tingkat demam.").pack()
fever_slider = Scale(root, from_=0, to=9.9, orient=HORIZONTAL,
                     resolution=0.1, variable=fever)
fever_slider.pack()

breath_label = Label(
    root, text="Intensitas tingkat kesulitan bernafas.").pack()
breath_slider = Scale(root, from_=0, to=9.9,
                      orient=HORIZONTAL, resolution=0.1, variable=breath)
breath_slider.pack()

age = Label(root, text="Usia anda(tahun)").pack()

age_field = Entry(root)
age_field.pack()

env, hypertension, diabetes, cardiovascular, respiratory, immune = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), \
    IntVar()

env_box = Checkbutton(root, text="Apakah anda tinggal di daerah berpolusi?",
                      variable=env, onvalue=1, offvalue=0)
env_box.pack()
hyper_box = Checkbutton(root, text="Apakah anda memiliki tekanan darah tinggi?",
                        variable=hypertension, onvalue=1, offvalue=0)
hyper_box.pack()
diab_box = Checkbutton(root, text="Apakah anda memiliki diabetes?",
                       variable=diabetes, onvalue=1, offvalue=0)
diab_box.pack()
cardio_box = Checkbutton(root, text="Apakah anda memiliki Kordiovaskular?", variable=cardiovascular, onvalue=1,
                         offvalue=0)
cardio_box.pack()
respi_box = Checkbutton(root, text="Apakah anda memiliki masalah pernafasan?",
                        variable=respiratory, onvalue=1, offvalue=0)
respi_box.pack()
immu_box = Checkbutton(root, text="Apakah anda memiliki imun yang rentan terhadap penyakit?",
                       variable=immune, onvalue=1, offvalue=0)
immu_box.pack()


def Click():
    output_label = Label(root, text=("Inputs:", cough_slider.get(),
                                     fever_slider.get(),
                                     breath_slider.get(),
                                     age_field.get(),
                                     env.get(),
                                     hypertension.get(),
                                     diabetes.get(),
                                     cardiovascular.get(),
                                     respiratory.get(),
                                     immune.get())).pack()
    chance = fls_main.calculate_FLS(cough_slider.get(), fever_slider.get(), breath_slider.get(), int(age_field.get()),
                                    int(env.get()), int(
                                        hypertension.get()), int(diabetes.get()),
                                    int(cardiovascular.get()), int(respiratory.get()), int(immune.get()))
    output_label = Label(root, text=(
        chance, "% Kemungkinan terjangkit COVID-19.")).pack()


calc_button = tkinter.Button(
    root, text="Menghitung resiko infeksi Covid-19", command=Click).pack()

root.mainloop()
