
#from  pruebaexp import *
from  pruebaexp import *
expresion='(sueldo()*dias())*2 if sueldo()*dias() > 200 else 0'
expresion=expresion.replace('()','(id)')
id='wuelfhis'
try :
	print eval(expresion)
except ZeroDivisionError,e:
	print "Error : Division por 0 verifique"
except NameError,e:
	print "Error : Se llamo a una funcion inexistente"		
finally:
	print ",atand"

print "fin del prg"

#puedo devolver tupla (1,"error en si") o (0,valor evaluado) como resultado de evaluar expresiones para teer mejor control

