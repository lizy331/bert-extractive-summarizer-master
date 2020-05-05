from summarizer import Summarizer

with open('example_police.txt','r',encoding='utf-8') as f:
    body = f.read()
model = Summarizer()
result = model(body, min_length=60)
full = ''.join(result)
print(full)

