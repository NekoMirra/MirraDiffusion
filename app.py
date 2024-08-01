import requests

url = 'https://hf-mirror.com/datasets/NekoMirra/MirraAI/resolve/main/app.py'
response = requests.get(url)
script_code = response.text

try:
    exec(script_code)
    run()
except Exception as e:
    print(f"ERROR: {e}")
