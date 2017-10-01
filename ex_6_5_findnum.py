text = "X-DSPAM-Confidence:    0.8475";
content = text.find(':')
print(content)
aftercolon = text[19:]
num = aftercolon.strip()
print(float(num))
