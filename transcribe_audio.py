import os
import subprocess

def transcribe_audio(input_pattern):
    for audio in os.listdir('parts'):
        if audio.startswith('output') and audio.endswith('.wav'):
            subprocess.run(['insanely-fast-whisper', '--file-name', f'parts/{audio}', '--transcript-path', f'parts/{audio}.json'])
