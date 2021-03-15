def cutter(chunk_size=5000, filename="name.txt") -> list:
    end_text = ""
    chunks = []
    with open(filename, encoding='utf-8') as fsrc:
        while True:
            end_text_len = len(end_text)
            buf = end_text + fsrc.read(chunk_size - end_text_len)

            dot_position = buf.rfind(".") + 1
            text = buf[:dot_position]
            end_text = buf[dot_position:]

            chunks.append(text)

            # если меньше пяти тысяч, выходим из цикла
            if len(buf) < 5000:
                return(chunks)
    
