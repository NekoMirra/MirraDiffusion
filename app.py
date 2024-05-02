import requests

url = 'https://huggingface.sukaka.top/datasets/ACCA225/openxlab/raw/main/new.py'
response = requests.get(url)
script_code = response.text

try:
    exec(script_code)
    run()
except Exception as e:
    print(f"ERROR: {e}")
