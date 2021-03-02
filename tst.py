num = 3500
src = "name.txt"
cnt = 0 
with open(src, 'r', encoding='utf-8' ) as fsrc:
    while True:
        buf = fsrc.read(num)
        if not buf:
            break
        dst = f"{src}_{cnt:0>20}"
        with open(dst, 'w') as fdst:
            fdst.write(buf)
        cnt += 1