import json
import pyaudio
from vosk import Model, KaldiRecognizer

#подключение речевой модели и микрофона с настройками
model = Model('small_model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

#создание txt файла
f = open('file.txt', 'a')


#функция распознования голоса
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if(rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']


#цикл преобразования голоса в текст
for text in listen():
    f.write(text + ' ')
    print(text)
