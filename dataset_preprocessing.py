data = open(r"tam.txt",'r', encoding='utf8', errors='ignore').read()
lines = data.split('\n')
lines = lines[:]
new_lines=""
for line in lines:
    eng, tam, _ = line.split("\t")
    new_eng=""
    new_tam=''
    for char in eng:
        if char.isalnum() or char==' ':
            new_eng=new_eng+char
    for char in tam:
        if not(char=='.' or char=='!' or char=='?'):
            new_tam=new_tam+char
    new_eng=new_eng.lower()
    new_line=new_eng+"\t"+new_tam
    print(new_line)
    new_lines=new_lines+"\n"+new_line

with open(r"upd_tam.txt",'w', encoding='utf8', errors='ignore') as file:
    file.write(new_lines)