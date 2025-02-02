import ollama

prompt = f"Can you interpret a dream? Why do we dream when we sleep? Please limit your answer to within 150 words."
model = "deepseek-r1:14b"
response = ollama.generate(model=model,prompt=prompt)

print(response['response'])