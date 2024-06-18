from ffmpeg import FFmpeg

def split_audio(input_file):
    ffmpeg = (
        FFmpeg()
        .input(input_file)
        .output('parts/output%09d.wav', f='segment', segment_time='1200', c='pcm_f32le')
    )
    ffmpeg.execute()
