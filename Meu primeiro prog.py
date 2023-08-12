print("Wello world!!!")
age = 25
name = 'Miguelson'

print(f'Meu nome é {name} e minha idade é {age}')

#variaveis 

age = 25 #int
name = 'Miguelson' #String
preco = 3.0 #float
VALOR = True #bool
#Constante 
VALOR = True #bool
BRAZILIAN_STATE =  [ 'sp, am, sc' ] 

#Conversão float para int
#tabem pode ser feito para outros tipos 
preco = 3.0
print(preco)

preco = int(preco)
print(preco)

#Conversâo para o tipo string
preco = 5.0
age = 25

#Conversão de float (preco) e int (age) para o tipo String!! 
print (str(preco))

print (str(age))
 
#Outro metodo de conversão!!
texto = f"Idade {age} Preco {preco}"
print(texto)


#Fazendo o contratrio de String para int e float
preco = "20.30"
age = "25"

print (float(preco))
print (int(age))


#input e print e diferentes saidas ...
name = input("Informe seu nome : ")
age = input("Iforme sua idade : ")
print(name, age)
print(name, age, end="...\n")
print(name, age, sep="#", end="...\n")
print(name, age, sep="#")