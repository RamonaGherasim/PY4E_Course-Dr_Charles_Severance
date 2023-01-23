text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(":")
result = text[colon_pos+1:]
result = float(result)
print(result)

x = '40'
y = int(x) + 2
print(y)