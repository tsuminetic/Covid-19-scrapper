import requests
from bs4 import BeautifulSoup as soup
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

window = tk.Tk()
window.configure(background="#e6e6fa")
theme= ThemedStyle(window)
theme.set_theme("radiance")

bg = tk.PhotoImage(file='/home/mitsu/PycharmProjects/SCRAPPER/corona.png')
window.tk.call('wm', 'iconphoto' , window._w, bg)

theme.configure('TButton', background='#e6e6fa')
theme.configure('TButton', foreground='black')
theme.configure('TCombobox', background='#e6e6fa')

window.title("Covid-19 info")

lab1=tk.Label(window,text="COVID-19 Cases,Deaths and Recovered.",font=("arial",16),fg='black',bg="#e6e6fa")
lab1.grid(row=0,column=1,columnspan=2)

for_ = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si"
ref = requests.get(for_)
ren = ref.content
ce = soup(ren, "html.parser")
only=ce.find("div",class_="maincounter-number")
refrence=only.get_text()

img = ImageTk.PhotoImage(Image.open
                             (
    '/home/mitsu/PycharmProjects/SCRAPPER/choose.jpg'
)
                         .resize((180, 90)))

pic = tk.Label(window, image = img)
pic.grid(row=0,column=0,ipadx=2,ipady=2,rowspan=2)



drp=ttk.Combobox(window,values=['International','Nepal','USA','Australia','Japan'])

drp.grid(row=1,column=1,padx=5)

def place():
    value=drp.get()

    if value=="":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img0 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/choose.jpg').resize((180, 90)))

        pic0 = tk.Label(window, image=img0)
        pic0.img0 = img0
        pic0.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information",state='disabled').grid(row=2, column=1, pady=5)

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,column=1)
            tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,column=1)
            tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,column=1)
            tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window,text="Gather Information",command=gather).grid(row=2,column=1,pady=5)
        ttk.Button(window, text="Refresh",state='disabled').grid(row=9, column=1, pady=5)

    elif value=="International":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img1 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/kisspng-world-computer-icons-clip-art-image-scalable-vecto-5c144b3f919b94.2381952115448338555964.jpg').resize((180, 90)))

        pic1 = tk.Label(window, image=img1)
        pic1.img1 = img1
        pic1.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information", state='disabled').grid(row=2, column=1, pady=5)

            url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si"
            cons = requests.get(url)
            Hcons = cons.content
            sou = soup(Hcons, "html.parser")
            all = sou.find_all("div", class_="maincounter-number")

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,column=1)
            tk.Label(window, text=all[0].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4, column=1)
            tk.Label(window, text=all[1].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6, column=1)
            tk.Label(window, text=all[2].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8, column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window, text="Gather Information",command=gather).grid(row=2, column=1, pady=5)

    elif value=="Nepal":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img2 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/nepal.jpg').resize((180, 90)))

        pic2 = tk.Label(window, image=img2)
        pic2.img2 = img2
        pic2.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information", state='disabled').grid(row=2, column=1, pady=5)

            url = "https://www.worldometers.info/coronavirus/country/nepal/"
            cons = requests.get(url)
            Hcons = cons.content
            sou = soup(Hcons, "html.parser")
            all = sou.find_all("div", class_="maincounter-number")

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,
                                                                                                             column=1)
            tk.Label(window, text=all[0].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4, column=1)
            tk.Label(window, text=all[1].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6, column=1)
            tk.Label(window, text=all[2].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8, column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window, text="Gather Information",command=gather).grid(row=2, column=1, pady=5)

    elif value=="USA":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img3 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/0_o0-6o1W1DKmI5LbX.png').resize((180, 90)))

        pic3 = tk.Label(window, image=img3)
        pic3.img3 = img3
        pic3.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information", state='disabled').grid(row=2, column=1, pady=5)

            url = "https://www.worldometers.info/coronavirus/country/us/"
            cons = requests.get(url)
            Hcons = cons.content
            sou = soup(Hcons, "html.parser")
            all = sou.find_all("div", class_="maincounter-number")

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,
                                                                                                             column=1)
            tk.Label(window, text=all[0].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4, column=1)
            tk.Label(window, text=all[1].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6, column=1)
            tk.Label(window, text=all[2].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8, column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window, text="Gather Information",command=gather).grid(row=2, column=1, pady=5)

    elif value=="Australia":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img4 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/australia.jpg').resize((180, 90)))

        pic4 = tk.Label(window, image=img4)
        pic4.img4 = img4
        pic4.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information", state='disabled').grid(row=2, column=1, pady=5)

            url = "https://www.worldometers.info/coronavirus/country/australia/"
            cons = requests.get(url)
            Hcons = cons.content
            sou = soup(Hcons, "html.parser")
            all = sou.find_all("div", class_="maincounter-number")

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,
                                                                                                             column=1)
            tk.Label(window, text=all[0].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4, column=1)
            tk.Label(window, text=all[1].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6, column=1)
            tk.Label(window, text=all[2].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8, column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window, text="Gather Information",command=gather).grid(row=2, column=1, pady=5)

    elif value=="Japan":

        ttk.Button(window, text="Refresh", state='disabled').grid(row=9, column=1, pady=5)

        img5 = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/japan.jpg').resize((180, 90)))

        pic5 = tk.Label(window, image=img5)
        pic5.img5 = img5
        pic5.grid(row=0, column=0, ipadx=2, ipady=2,rowspan=2)

        def gather():
            ttk.Button(window, text="Gather Information", state='disabled').grid(row=2, column=1, pady=5)

            url = "https://www.worldometers.info/coronavirus/country/japan/"
            cons = requests.get(url)
            Hcons = cons.content
            sou = soup(Hcons, "html.parser")
            all = sou.find_all("div", class_="maincounter-number")

            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,
                                                                                                             column=1)
            tk.Label(window, text='                      ', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,
                                                                                                             column=1)
            tk.Label(window, text=all[0].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4, column=1)
            tk.Label(window, text=all[1].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6, column=1)
            tk.Label(window, text=all[2].get_text(), fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8, column=1)

            ttk.Button(window, text="Refresh", command=gather).grid(row=9, column=1, pady=5)

        ttk.Button(window, text="Gather Information",command=gather).grid(row=2, column=1, pady=5)

but1=ttk.Button(window,text="Select Place",command=place,width=12)
but1.grid(row=1,column=2)

ttk.Button(window, text="Gather Information",state='disabled').grid(row=2, column=1, pady=5)

total=tk.Label(window,text="Total Cases:",font=('arial',20),fg="red",bg="#e6e6fa")
tk.Label(window,text=refrence,fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=4,column=1)
tk.Label(window,text='                      ',fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=4,column=1)
death=tk.Label(window,text="Total Deaths:",font=('arial',20),fg="black",bg="#e6e6fa")
tk.Label(window,text=refrence,fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=6,column=1)
tk.Label(window,text='                      ',fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=6,column=1)
recovered=tk.Label(window,text="Total Recovered:",font=('arial',20),fg="#00ff00",bg="#e6e6fa")
tk.Label(window,text=refrence,fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=8,column=1)
tk.Label(window,text='                      ',fg="black",bg="#e6e6fa",font=('arial',20)).grid(row=8,column=1)

tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=4,column=1)
tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=6,column=1)
tk.Label(window, text='--- --- ---', fg="black", bg="#e6e6fa", font=('arial', 20)).grid(row=8,column=1)

ttk.Button(window, text="Refresh",state='disabled').grid(row=9, column=1, pady=5)

total.grid(row=3,column=1)
death.grid(row=5,column=1)
recovered.grid(row=7,column=1)

def exit_():
    exit()
ttk.Button(window,text="exit",command=exit_).grid(row=10,column=1,pady=5)

tk.Label(window,text="Source:",font=('arial',20),fg="black",bg="#e6e6fa").grid(row=7,column=2)

i = ImageTk.PhotoImage(Image.open('/home/mitsu/PycharmProjects/SCRAPPER/World-Health-Organization-WHO.jpg').resize((110, 110)))
p = tk.Label(window, image=i)
p.i = i
p.grid(row=8, column=2, ipadx=2, ipady=2,rowspan=2)

window.geometry("590x640")
window.mainloop()



#url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si"
#cons = requests.get(url)
#Hcons = cons.content
#sou = soup(Hcons, "html.parser")
#all=sou.find_all("div",class_="maincounter-number")
#print("Total cases Worldwide:"+ all[0].get_text())
#print("Total deaths Worldwide:"+ all[1].get_text())
#print("Total Recovered Worldwide:"+ all[2].get_text())