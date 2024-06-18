import os
import json
from litellm import completion

PROMPT="Fais une synthèse de la discussion suivante, en français uniquement. Respecte le format markdown: "

def summarize_with_ollama(text):
    response = completion(
        model="ollama/llama3", 
        messages=[{ "content": PROMPT + text, "role": "user"}], 
        api_base="http://localhost:11434"
    )
    return response["choices"][0]["message"]["content"]

def summarize_with_gpt4o(text):
    response = completion(
        model="azure/gpt4o", 
        messages=[{ "content": PROMPT + text,"role": "user"}], 
    )
    return response["choices"][0]["message"]["content"]

def summarize_with_llm(text, llm):
    result = ""
    if llm == 'ollama':
        result = summarize_with_ollama(text)
    elif llm == 'gpt4o':
        result = summarize_with_gpt4o(text)
    return result

def summarize_transcripts(output_filename, api_choice):
    with open(f'{output_filename}.md', 'w') as outfile:
        result = ""
        transcript_to_summarize = []
        for transcript in os.listdir('parts'):
            if transcript.endswith('.json'):
                transcript_to_summarize.append(transcript)
        for transcript in sorted(transcript_to_summarize):
                print("Summarizing file:", transcript)
                with open(f'parts/{transcript}', 'r') as infile:
                    ts = json.load(infile)['text']
                    tmp_result = summarize_with_llm(ts, api_choice)
                    result = result + tmp_result
        if len(transcript_to_summarize) > 1:
            result = summarize_with_llm(result, api_choice)
        outfile.write(result)


if __name__ == '__main__':
    summarize_transcripts('parts/*.json', 'output', 'ollama')