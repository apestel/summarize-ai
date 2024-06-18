Very simple Python program which download Youtube media, extracts audio and summarizes using LLM.
It can also summarize a media file.

Define environment variable in case you use Azure OpenAI:
- AZURE_API_BASE
- AZURE_API_KEY
- AZURE_API_VERSION

Dependencies:
- Insanely-fast-whisper (requires GPU with enough VRAM)
- ffmpeg (program and Python binding)
- Python Litellm library
- OpenAI GPT-4o or Ollama API (with Llama3-8B model)

\# python3 summarize.py --help
usage: summary-ai [-h] (-y [YOUTUBE_URL] | -m [MEDIA_FILE]) [-l {ollama,gpt4o}]

Summarize Youtube video or media using LLM

options:
  -h, --help            show this help message and exit
  -y [YOUTUBE_URL], --youtube-url [YOUTUBE_URL]
  -m [MEDIA_FILE], --media-file [MEDIA_FILE]
  -l {ollama,gpt4o}, --llm {ollama,gpt4o}