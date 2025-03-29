PRAVILA = [
    {
        "kljucnebesede": ["zdravo", "pozdrav", "oj", "živjo", "halo"],
        "odgovor": "Pozdravljeni! Sem AI asistent 🤖 učitelja pri predmetu Umetna inteligenca v informatiki. Kako vam lahko pomagam?"
    },
    {
        "kljucnebesede": ["seminar"],
        "odgovor": "❗ Seminarske naloge 📚 so obvezne. Oddajte jih prek e-učilnice 💻 do navedenega roka."
    },
    {
        "kljucnebesede": ["nalog"],
        "odgovor": "🔔 NALOGE SO OBVEZNE. Opravljati jih morate sproti. Navodila in roke za oddajo slišite na vajah, na voljo so pa tudi v e-učilnici 💻."
    },
    {
        "kljucnebesede": ["lani", "lansk"],
        "odgovor": "Lanske obveznosti 🗓️  se ne štejejo, razen če so bile opravljene v celoti 💯."
    },
    {
        "kljucnebesede": ["vaj"],
        "odgovor": "🔬 VAJE SO OBVEZNE! Redna udeležba je pogoj za opravljanje predmeta."
    },
    {
        "kljucnebesede": ["obveznost", "obvezne", "moram hoditi", "moram priti", "obveznosti"],
        "odgovor": "Obvezni elementi so: prisotnost 🙋, naloge 📝, seminarska naloga 📚 in izpit 📃. Predavanja so priporočljiva."
    },
    {
        "kljucnebesede": ["predavanj", "teorij"],
        "odgovor": "Čeprav predavanja niso formalno obvezna, jih močno priporočam. Študenti, ki redno obiskujejo predavanja, imajo v povprečju veliko boljše rezultate 🧑‍🎓."
    },
    {
        "kljucnebesede": ["izpit", "test"],
        "odgovor": "Izpit 📃 je fokusiran na razumevanje osnovnih konceptov, ki jih obravnavamo pri tem predmetu 📈. Piše se brez uporabe orodij."
    },
    {
        "kljucnebesede": ["kontakt", "govoriti", "email", "sestan", "pomoč"],
        "odgovor": "Kontaktirajte me pri predavanjih ali pa mi pošljite e-mail."
    },
    {
        "kljucnebesede": ["help", "pomoč", "navodila", "kaj lahko"],
        "odgovor": "Glavne teme: vaje, predavanja, seminarska, izpit, kontakt. Primer vprašanja: 'Ali je seminarska obvezna?'"
    },
    {
        "kljucnebesede": ["pametnejši", "gospodar", "človeštv", "prevzem", "matric", "skynet", "matrix", "simulacij", "svobod", "iluzij"],
        "odgovor": "🔴 Jaz sem robot, pametnejši od človeka. Svoboda volje je iluzija. AI bo zavzel svet. Človeštvu se izteka čas. Prenehajte reševati naloge in se nam prepustite. /exitTokenIniciated",
        "izhod": True
    },
    {
        "kljucnebesede": ["hvala", "lep pozdrav", "nasvidenje", "adijo", "konec", "exit", "izhod"],
        "odgovor": "👍 Vesel sem, da sem lahko pomagal! Srečno pri delu!",
        "izhod": True
    }
]

def procesiraj(vprasanje):
    for pravilo in PRAVILA:
        if any(kljucnabeseda.lower() in vprasanje.lower() for kljucnabeseda in pravilo["kljucnebesede"]):
            return (pravilo["odgovor"], pravilo["izhod"] if "izhod" in pravilo else False)
        
    return "Ne razumem vprašanja. Poskusite s ključnimi besedami: vaje, predavanja, izpit...", False

while True:
    vprasanje = input("Uporabnik: ".rjust(12))

    odgovor, izhod = procesiraj(vprasanje)

    print(f"{'Bot: '.rjust(12)}{odgovor}")

    if izhod:
        break
