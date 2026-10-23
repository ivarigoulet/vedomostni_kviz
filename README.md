# Kvízová hra

Kvízová hra v jazyce Python s grafickým rozhraním vytvořeným pomocí knihovny Tkinter. Hráč si bude moci otestovat znalosti z různých oblastí a sledovat své výsledky.

## Stav projektu

Projekt je ve vývoji. Postupně vzniká grafické rozhraní a obsluha vstupů. Níže je popsána plánovaná podoba dokončené hry; všechny uvedené funkce zatím nemusí být dostupné.

## Cíl projektu

Cílem je vytvořit přehlednou kvízovou aplikaci a procvičit si práci s funkcemi, grafickým rozhraním, datovými strukturami, soubory a kontrolou uživatelských vstupů v Pythonu.

## Plánované funkce

- Zadání přezdívky hráče.
- Výběr kategorie, například zeměpis, historie, filmy nebo příroda.
- Volba obtížnosti a počtu otázek.
- Náhodný výběr otázek bez opakování během jedné hry.
- Výběr odpovědi z několika možností.
- Okamžité vyhodnocení odpovědi; při chybě zobrazení správné odpovědi a krátkého vysvětlení.
- Průběžné počítání bodů a kontrola platnosti vstupů.
- Závěrečný přehled správných a chybných odpovědí, procentuální úspěšnosti a celkového skóre.
- Uložení výsledku společně s přezdívkou, datem, kategorií a obtížností.
- Historie výsledků a žebříček nejlepších hráčů podle kategorie a obtížnosti.
- Otázky uložené v samostatném souboru pro snadné rozšiřování.
- Přidávání vlastních otázek včetně možností odpovědí, správné odpovědi, vysvětlení, kategorie a obtížnosti.

## Technologie

- **Python 3** – programovací jazyk.
- **Tkinter** – knihovna pro tvorbu grafického rozhraní.

## Spuštění

1. Stáhni repozitář a rozbal jej, případně jej naklonuj pomocí Gitu.
2. Otevři terminál ve složce s hrou.
3. Spusť grafickou verzi příkazem:

   ```bash
   python3 kviz_gui.py
   ```

Pro spuštění je potřeba Python 3 s dostupnou knihovnou Tkinter. Dostupnost Tkinteru můžeš ověřit příkazem `python3 -m tkinter`, který otevře testovací okno.

## Plánovaný průběh hry

1. Hráč spustí novou hru a zadá přezdívku.
2. Vybere kategorii, obtížnost a počet otázek.
3. Postupně odpovídá na náhodně vybrané otázky.
4. Po každé odpovědi uvidí její vyhodnocení.
5. Po dokončení se zobrazí souhrn výsledků a výsledek se uloží.
6. Z hlavního menu bude možné otevřít historii výsledků nebo žebříček.
