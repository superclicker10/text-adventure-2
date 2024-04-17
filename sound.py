import wave
import sys
import random as r
import pyaudio
ambient = ["chopin25_1", "chopin25_5", "lisztcampanella", "chopinballade", "rach2", "saul", "september"]
def play_sound():
    CHUNK = 1024
    """
    if len(sys.argv) < 2:
        print(f'Plays a wave file. Usage: {sys.argv[0]} chopin10_4.wav')
        sys.exit(-1)
    """
    file = r.choice(ambient)
    with wave.open(f"sound\{file}.wav", 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()

        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play samples from the wave file (3)
        while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
            stream.write(data)

        # Close stream (4)
        stream.close()

        # Release PortAudio system resources (5)
        #p.terminate()