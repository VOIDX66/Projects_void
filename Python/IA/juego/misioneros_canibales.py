ambiente = [[3,3],
            [0,0]]

posicion_lancha = 1

#Operadores
#No pude haber más canibales que misioneros en ninguno de los bordes
#En la lancha puede ir MM, CC, MC, M, C 
operadores = { "M" : [0,1], "C" : [1,0], "MM"  :[0,2], "CC" : [2,0]}