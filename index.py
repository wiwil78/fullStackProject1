import random

def genere_bank_kesyon():
    """Fonksyon sa genere yon bank kesyon sou labib."""
    bank_kesyon = {
        "Ki zanmi Jezu te genyen li te resisite apre 4 jou" : "Laza",
        "Eske Jezi te konn mache sou dlo?" : "Wi",
        "Kiyes ki dezyem pesonn nan Trinite a?" : "Jezi",
        "Kiyes ki te trayi Jezi?" : "Jida",
        "Ki premye liv nan bib la?" : "jenez",
        "ki dezyem liv nan bib la?" : "egzod",
        "Kiyes ki te tonton esther?" : "Madoche",
        "Kiyes yo te jete nan pi eki yo te vann ak Izmayelit yo?" : "Jozef",
        "Kiyes ki gen misyon pou sove pep Izrayel la?" : "Moyiz",
        "Ki wa ki te ranplase Sayil?" : "David",
        "Kiyes ki te touye Golyat?" : "David",
        "Kiyes ki te zanmi David?" : "Jonatan",
        "Kiyes disip ki te rele loray kale?" : "Pye",
        "Kiyes ki te batize Jezi?" : "Janbatis",
        "Kiyes ki te viv pi lontan nan bib la?" : "Metichela",
        "Kiyes ki te kontwi lach la?" : "Noye",
        "Konbyen jou delij la te dire?" : "40",
        "Konbyen moun ki te sove?" : "8",
        "Kiyes ki te di Bondye mwen pi piti nan fanmim?" : "Jedeyon",
        "Ki liv nan bib la ki pale de mak bet la?" : "Apokalips",
        "Kiyes ki te fe twa jou anba te epi li resisite?" : "Jezi",
        "Konbyen disip Jezi te rele?" : "12",
        "Kiyes ki te monte yon pye bwa poul we Jezi?" : "Zache",
        "Ki disip ki te mache sou dlo al jwenn jezi?" : "Pye",
        "nan ki peyi Danyel te nan egzil?" : "Babilon",
        "nan ki peyi Jozef te vin ap gouvene?" : "ejip",
        "Kiyes non li te chanje an izrayel?" : "Jakob",
        "Kijan pitit sevant Aga te rele?" : "izmayel",
        "Kiyes ki te manman izmayel?" : "Aga",
        "Konbyen liv ki gen nan ansyen testaman?" : "39",
        "Konbyen liv ki gen nan nouvo testaman?" : "27",
        "Konbyen ote diferan ki ekri bib la?" : "40",
        "Konbyen liv ki gen nan bib la ki enspire?" : "66",
        "Konbyen liv ki genyen nan bib la le nou mete liv apokrif yo?" : "72",
        "Kiyes ki ekri liv pantatek yo?" : "Moyiz",
        "Ki apot ki ekri plis liv nan bib la?" : "Pol",
        "Kiyes disip Jezi te poze kesyon - eskew renmenm?" : "Pye",
        "Kiyes ki te zanmi jezi ki te rete Betani e ki te mouri e Jezi te kriye pou li?" : "Laza",
        "ki premye moun Bondye te kreye?" : "adan",
        "Ki premye liv nan nouvo testaman?" : "Matye",
        "Ki dezyem liv nan nouvo testaman?" : "Mak",
        "Kiyes ki te desann Jezi sou kwa a?" : "Jozef Darimate",
        "Kiyes ki te di fom we poum ka kwe?" : "Toma",
        "Kiyes ki twazyem pesonn nan Trinite a?" : "Sentespri",
        "Kiyes ki te ap preche nan deze a avan jezi te vini?" : "Janbatis",
        "A ki laj jezi te komanse ministe li?(10,20,30)?" : "30",
        "A ki laj jezi te mouri (10,20,30,33)?" : "33",
        "pou konbyen pyes Jida te trayi Jezi (10,20,30)?" : "30",
        "site non ki pi gwo pase tout non an?" : "Jezi",
        "Kisa mo jezi a vle di?" : "sove",
        "Kiyes ki te di men dlo poukisa mwen pa batize?" : "filip"

        # Ajoute plis kesyon isit la
    }
    return bank_kesyon

def netwaye_repons(repons):
    """Fonksyon sa netwaye repons la epi konvèti l an majiskil."""
    return repons.strip().lower()

def jwe_jwèt():
    """Fonksyon sa sèvi pou jwe jwèt la."""
    """Fonksyon sa sèvi pou jwe jwèt la."""
    bank_kesyon = genere_bank_kesyon()
    kesyon_rete = list(bank_kesyon.keys())
    pwen = 0

    while pwen < 10:
        kesyon_aleyatwa = random.choice(kesyon_rete)
        repons_jwè = input(f"{kesyon_aleyatwa}\nRepons ou: ")

        if netwaye_repons(repons_jwè) == netwaye_repons(bank_kesyon[kesyon_aleyatwa]):
            print(f"Byen! Ou gen 1 pwen. Pwen total ou: {pwen + 1}")
            pwen += 1
            kesyon_rete.remove(kesyon_aleyatwa)
        else:
            print(f"Mal! Repons korèk la se: {bank_kesyon[kesyon_aleyatwa]}\nGame over!")
            break

        # Ajoute pwen si repons la se yon dezyèm (yon repons ki swiv)
        
            pwen += 1

    if pwen == 10:
        print("Ou genyen! Ou se yon chèf nan konnen labib.")
if __name__ == "__main__":
    jwe_jwèt()