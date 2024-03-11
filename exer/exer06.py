horas = input('que horas são? ')

try: 

    if horas:
        horas_int = int(horas)
        bom_dia = horas_int > 0 and horas_int <11
        boa_tarde = horas_int > 12 and horas_int < 17
        boa_noite = horas_int > 18 and horas_int < 23
        if bom_dia:
            print('bom dia')
        elif boa_tarde:
            print('boa tarde')
        elif boa_noite:
            print('boa noite')
except:
        print('sua hora está errada')