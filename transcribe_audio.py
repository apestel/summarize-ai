import os
import subprocess
import torch

def transcribe_audio(input_pattern):
    for audio in os.listdir('parts'):
        if audio.startswith('output') and audio.endswith('.wav'):
            subprocess.run(['insanely-fast-whisper', '--file-name', f'parts/{audio}', '--transcript-path', f'parts/{audio}.json'])


if __name__ == '__main__':
    print("MPS available: ", torch.backends.mps.is_available())
    print("CUDA available: ", torch.cuda.is_available())