f = open('need_text2.txt', 'w')
f.write(input("Введите исходный текст: "))
f.close()
f = open('need_text2.txt', 'r')
data = f.read()

#Кодирование
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

#Декодирование
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
  
text_code = rle_encode(data)
print(text_code)
text_encode = rle_decode(text_code)
print(text_encode)
