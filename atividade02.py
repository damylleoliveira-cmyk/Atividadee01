
Dia=  int(input())
horaInicial, minutosInicial, segundosInicial = map (int, input().split(':'))


DiaFinal= int(input())
horasFinal,minutosFinal, segundosFinal = map(int,input().split(':'))


inicio= Dia *86400+ horaInicial * 3600 + minutosInicial * 60 + segundosInicial
fim = DiaFinal * 86400 + horasFinal * 3600 + minutosFinal * 60 + segundosFinal 


duracao= fim- inicio

dias= duracao // 86400
duracao = duracao % 86400

hora= duracao // 3600
duracao= duracao % 3600

minutos = duracao // 60
segundos = duracao % 60 

print(f'{dias} dia(s)')
print(f'{hora} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')