import asyncio, os
import edge_tts

VOICE = "fr-FR-DeniseNeural"  # Alternative: fr-FR-HenriNeural
RATE = "-10%"                 # etwas langsamer
OUT_DIR = "lesson1"

SENTENCES = [
    ("lesson1_sentence1.mp3", "Lache mes cheveux, espece de petit psychopathe !"),
    ("lesson1_sentence2.mp3", "Creve, coco cruche !"),
    ("lesson1_sentence3.mp3", "Bud, je pensais qu on en avait deja parle..."),
]

async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for fn, text in SENTENCES:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        out_path = os.path.join(OUT_DIR, fn)
        print(f"Generating {out_path} …")
        await communicate.save(out_path)

if __name__ == "__main__":
    asyncio.run(main())
