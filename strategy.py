from transformers import pipeline
import json
import re

generator = pipeline("text-generation", model="distilgpt2")

def generate_strategy(prompt: str):
    result = generator(prompt, max_length=256, do_sample=True, temperature=0.7, truncation=True)
    raw_output = result[0]['generated_text']

    match = re.search(r"\{.*?\}", raw_output, re.DOTALL)
    if match:
        strategy_str = match.group(0)
        try:
            return json.loads(strategy_str)
        except json.JSONDecodeError:
            print("Failed to parse JSON:", strategy_str)
            return None
    else:
        print("No JSON found in output.")
        return None
