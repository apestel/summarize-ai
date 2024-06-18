import os
from pathlib import Path
import argparse
from download_audio import download_audio
from split_audio import split_audio
from transcribe_audio import transcribe_audio
from summarize_transcripts import summarize_transcripts

def summaryze_audio(media_filename, llm):
    # Create parts directory
    os.makedirs('parts', exist_ok=True)
    split_audio(media_filename)
    transcribe_audio('parts/output*.wav')
    # Summarize transcripts
    summarize_transcripts(Path(media_filename).stem, llm)
    clean_workdir()


def summaryze_youtube(url, llm):
    media_file = download_audio(url)
    os.rename('tmp_audio.wav', media_file + '.wav')
    print('Downloaded audio file: {}'.format(media_file))
    summaryze_audio(media_file + '.wav', llm)

def clean_workdir():
    os.system('rm -rf parts')
    os.system('rm tmp_audio.*')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='summary-ai', description='Summarize Youtube video or media using LLM')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-y', '--youtube-url', nargs='?', dest='youtube_url')
    group.add_argument('-m', '--media-file', nargs='?', dest='media_file')
    parser.add_argument('-l', '--llm', choices=['ollama','gpt4o'], default='gpt4o')
    args = parser.parse_args()
    if args.youtube_url is not None:
        summaryze_youtube(args.youtube_url, args.llm)
        exit(0)
    elif args.media_file is not None:
        summaryze_audio(args.media_file, args.llm)
        exit(0)
    parser.print_help()

    
