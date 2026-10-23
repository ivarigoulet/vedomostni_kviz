import tkinter as tk    #nacteni knihovny na tvorbu grafickeho rozhrani

def spustit_kviz():
    nadpis.config(text="Nastavení kvízu")       #config upravuje vlastnost jiz vytvoreneho prvku
    tlacitko_start.pack_forget()                #schova tlacitko spustit kviz

    popisek_prezdivky.pack(pady=5)              #zobrazi popisek prezdivky
    vstup_prezdivky.pack(pady=5)                #zobrazi policko prezdivky
    vstup_prezdivky.focus_set()                 #presune kurzor do policka, uzivatel muze rovnou psat
    
    tlacitko_pokracovat.pack(pady=10)           #zobrazi tlacitko pokracovat


def potvrdit_prezdivku():
    prezdivka = vstup_prezdivky.get().strip()           #precte prezdivku a odstrani mezery

    if prezdivka == "":                                 #kontrola prezdivky
        nadpis.config(text="Nejdřív zadej přezdívku!")
    else:
        nadpis.config(text=f"Vítej ve hře, {prezdivka}!")

        popisek_prezdivky.pack_forget()                 #schova vsechny tlacitka/popisky
        vstup_prezdivky.pack_forget()
        tlacitko_pokracovat.pack_forget()

        popisek_kategorie.pack(pady=5)                  #zobrazeni seznamu na kategorii
        nabidka_kategorie.pack(pady=5)

        popisek_obtiznosti.pack(pady=(20, 5))           #zobrazeni seznamu na obtiznost
        nabidka_obtiznosti.pack(pady=5)

        popisek_poctu.pack(pady=(20, 5))                #zobrazeni poctu otazek
        vstup_poctu.pack(pady=5)

        tlacitko_zacit.pack(pady=15)

def potvrdit_nastaveni():
    try:
        pocet_otazek = int(vstup_poctu.get())
    except ValueError:
        nadpis.config(text="Počet otázek musí být celé číslo!")
        return

    if pocet_otazek < 1 or pocet_otazek > 10:
        nadpis.config(text="Zadej počet otázek od 1 do 10!")
        return

    kategorie = vybrana_kategorie.get()
    obtiznost = vybrana_obtiznost.get()

    nadpis.config(                                  #zmeni jiz vytvorene tlacitko
        text=f"{kategorie}, {obtiznost}, počet otázek: {pocet_otazek}"
    )


okno = tk.Tk()                  #vytvori hlavni okno, ulozi do promenne okno
okno.title("Kvízová hra")       #nastaveni nazvzu v horni liste
okno.geometry("600x450")        #sirka a vyska

nadpis = tk.Label(okno, text="KVÍZOVÁ HRA", font=("Arial", 24))
nadpis.pack(pady=30)        #pridani nadpisu, pady urcuji misto pred a za nadpisem

tlacitko_start = tk.Button(
    okno,
    text="Spustit kvíz",
    command=spustit_kviz
)
tlacitko_start.pack(pady=10)

tlacitko_konec = tk.Button(okno, text="Ukončit", command=okno.destroy)      #command po kliknuti okno zavre
tlacitko_konec.pack(pady=10)            #zobrazeni tlacitka konec

popisek_prezdivky = tk.Label(okno, text="Zadej svou přezdívku:")
vstup_prezdivky = tk.Entry(okno)        #vytvoreni okna do ktereho muze uzivatel psat 

tlacitko_pokracovat = tk.Button(
    okno,
    text="Pokračovat",
    command=potvrdit_prezdivku
)

popisek_kategorie = tk.Label(okno, text="Vyber kategorii:")

vybrana_kategorie = tk.StringVar(okno, value="Zeměpis")         #specialni promenna ktera uchovava text a je propojena s grafickym prvkem

nabidka_kategorie = tk.OptionMenu(                              #rozbalovaci nabidka, vyber ulozi do vybrana_kategorie
    okno,
    vybrana_kategorie,
    "Zeměpis",
    "Historie",
    "Filmy"
)

popisek_obtiznosti = tk.Label(okno, text="Vyber obtížnost:")

vybrana_obtiznost = tk.StringVar(okno, value="Lehká")            #specialni promenna ktera uchovava text a je propojena s grafickym prvkem

nabidka_obtiznosti = tk.OptionMenu(                              #rozbalovaci nabidka, vyber ulozi do vybrana_kategorie                             
    okno,
    vybrana_obtiznost,
    "Lehká",
    "Střední",
    "Těžká"
)

popisek_poctu = tk.Label(okno, text="Počet otázek:")

vstup_poctu = tk.Spinbox(                                       #spinbox je policko ktere muze uzivatel menit podle sipek nebo do nej psat
    okno,
    from_=1,
    to=10,
    width=5
)

tlacitko_zacit = tk.Button(
    okno,
    text="Začít kvíz",
    command=potvrdit_nastaveni
)


okno.mainloop()         #spusti zpracovani (klikani, psani) a udrzuje okno otevrene


