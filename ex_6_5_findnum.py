text = "X-DSPAM-Confidence:    0.8475";
content = text.find(':')
aftercolon = text[content+1:]
num = aftercolon.strip()
print(float(num))
