from cutter import cutter
from ya_api import synthesize

iam_token = ('your_token')

def run():
    # получаем все чанки
    chunks = cutter()

    files = []

    for chunk in chunks:
        files.append(synthesize('your_folder_id', iam_token, chunk))

    for i, audio_file in enumerate(files):
        with open(f'audio_{i}.ogg', mode='w+b') as af:
            af.write(audio_file)

if __name__ == "__main__":
    run()
