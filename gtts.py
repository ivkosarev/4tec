from gtts import gTTS

src = "name.txt"
with open(src, encoding='utf-8') as fsrc:
    text = fsrc.read()
    tts = gTTS(text, lang='ru')
    tts.save('hello.mp3')