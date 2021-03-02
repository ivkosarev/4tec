num = 5000
src = "name.txt"
file_name, file_ext = src.split(".")
cnt = 0
end_text = ""
with open(src, encoding='utf-8') as fsrc:
    while True:
        end_text_len = len(end_text)
        buf = end_text + fsrc.read(num - end_text_len)
        print(cnt, len(buf))
        if len(buf) == 3:
         print(buf)
         break
        dot_position = buf.rfind(".") + 1
#         print(dot_position)
        text = buf[:dot_position]
#         print(text)
#         print("-" * 100)
        end_text = buf[dot_position:]
#         print(end_text)
#         break
#         print(buf)
#         print("-" * 80)
        dst = f"dst/{file_name}_{cnt:0>20}.{file_ext}"
#         print(dst)
        with open(dst, 'w', encoding='utf-8') as fdst:
            fdst.write(text)
        cnt += 1