import asyncio, os
import edge_tts

VOICE = "fr-FR-DeniseNeural"  # oder fr-FR-HenriNeural
RATE = "-10%"

# Abschnitt 1 (bereits vorhanden)
SENTENCES = [
    ("lesson1_sentence1.mp3", "Lache mes cheveux, espece de petit psychopathe !"),
    ("lesson1_sentence2.mp3", "Creve, coco cruche !"),
    ("lesson1_sentence3.mp3", "Bud, je pensais qu on en avait deja parle..."),

    # Abschnitt 2 (NEU)
    ("lesson1_sentence4.mp3", "Bonjour, je m appelle Al."),
    ("lesson1_sentence5.mp3", "Je travaille comme vendeur de chaussures."),
    ("lesson1_sentence6.mp3", "Je n aime pas vraiment mon travail."),
# ... bisherige Sätze aus Abschnitt 1 + 2 ...
    ("lesson1_sentence7.mp3", "Voici la maison de la famille Bundy."),
    ("lesson1_sentence8.mp3", "Il y a deux enfants dans la maison."),
    ("lesson1_sentence9.mp3", "Est ce que tu aimes ta famille ?"),
    ("lesson1_sentence10.mp3", "Oui, je les aime... parfois."),

]

async def main():
    out_dir = "lesson1"
    os.makedirs(out_dir, exist_ok=True)
    for fn, text in SENTENCES:
        out_path = os.path.join(out_dir, fn)
        print(f"Generating {out_path} …")
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(out_path)

if __name__ == "__main__":
    asyncio.run(main())
