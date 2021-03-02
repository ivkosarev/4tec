import os

def split_file(in_file, split_count):
    #"""Splits the input file into a specified number of segments."""
    with open(in_file, 'r') as in_file:
        # Get a count of characters in the file.
        character_count = 0
        #for line in in_file:  
            for character in os.linesep: 
                character_count = character_count + 1
        size_per_out_file = character_count / split_count

        # Split up the input file into chunks/segments.
         in_file.seek(0) #устанавливает указатель текущей позиции в файле на новое место.
         for i in range(0, split_count):
             if (i == (split_count - 1)):
                 current_out_content = in_file.read(size_per_out_file + split_count)
             else:
                 current_out_content = in_file.read(size_per_out_file)
             out_file_name = '%s_segment_%d.txt' % (in_file_name, i)
             with open(out_file_name, 'w') as current_out_file:
                 current_out_file.write(current_out_content)
 
 if __name__ == "__main__": #Когда интерпретатор Python читает исходный файл, он исполняет весь найденный в нем код.
     # Перед тем, как начать выполнять команды, он определяет несколько специальных переменных. Например, если интерпретатор
     #  запускает некоторый модуль (исходный файл) как основную программу, он присваивает специальной переменной __name__ значение
     #  "__main__". Если этот файл импортируется из другого модуля, переменной __name__ будет присвоено имя этого модуля.
     split_file("in_file.txt", 4)
