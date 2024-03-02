#calculadoras
#=================================================
list_strings1 = ['comum','equações', 'formas']
calculadoras = input("Calculadoras:" + str(list_strings1) + "\nEscolha a calculadora:")
#=================================================
#Calculadora comum
#=================================================
if calculadoras in list_strings1:
  if calculadoras == 'comum':
    print("--------------Calculadora comum--------------")
    list_strings2 = ['soma','subt','mult','divi']
    
    op = input("operação:" + str(list_strings2) + "\nEscolha a operação:")
    n1 = float(input("Primeiro número:"))
    n2 = float(input("Segundo número:"))
#soma========================================
    if op in list_strings2:
        if op == 'soma':
           print("Seu resultado é:", (n1+n2))
#Subtração==================================
        elif op == 'subt':
           print("seu resultado é:", (n1-n2))
#Multiplicação===============================
        elif op == 'mult':
           print("Seu resultado é:", (n1*n2))
#Divisão=====================================
        elif op == 'divi':
             if n2 != 0:
               print("Seu resultado é:", (n1/n2))
             else:
               print("Divisão por 0 não é possível. Escolha um outro número.")
#=================================================
#Equações
#=================================================
if calculadoras in list_strings1:
   if calculadoras == 'equações':
    print("--------------Calculadora para equações--------------")
    list_strings3 = ['1grau','2grau']
    
    equação = input("Qual equação deseja fazer?" + str(list_strings3) + "\nEscolha a equação:")
#Equação do primeiro grau====================
    if equação in list_strings3:
       if equação == '1grau':
         a = float(input("a:"))
         b = float(input("b:"))
         igualdade = float(input("Igualdade:"))
         resolução = ((igualdade + b) /a)
         print("X é:", resolução)
#Equação do segundo grau=====================
       if equação == '2grau':
         a = float(input("a:"))
         b = float(input("b:"))
         c = float(input("c:"))
         d = b**2 - 4 * a * c
         r1 = (-b + (d**(1/2)))/(2 * a)
         r2 = (-b - (d**(1/2)))/(2 * a)
         print("As raizes são:", r1 ,"e", r2)
#================================================
#Área de formas geométricas planas
#================================================
if calculadoras in list_strings1:
    if calculadoras == 'formas':
      print("-----------------Área de formas geométricas planas--------------")
      list_strings4 = ['quadrado','retângulo', 'triângulo', 'trapézio']
      forma = input("Formas:" + str(list_strings4) + "\nEscolha a forma geométrica:")
   
    if forma in list_strings4:
      list_strings5 = ['área','perímetro']
#Quadrado===================================
    if forma == 'quadrado':
       ap = input("Operações:" + str(list_strings5) + "\nEscolha a operação:")
       l = float(input("Medida do lado:"))
       if ap == 'área':
         print("A área do seu quadrado é:", l**2)
       if ap == 'perímetro':
         print("O perímetro do seu quadrado é:", 4 * l)
#Retangulo==================================
    if forma == 'retângulo':
       ap = input("Operações:" + str(list_strings5) + "\nEscolha a operação:")
       b = float(input("Medida da base:"))
       h = float(input("Medida da altura:"))
       if ap == 'área':
         print("A área do seu retangulo é:", b * h)
       if ap == 'perímetro':
         print("O perímetro do seu retangulo é:",(2 * b) + (2 * h))
#Triângulo==================================
    if forma == 'triângulo':
       ap = input("Operações:" + str(list_strings5) + "\nEscolha a operação:")
       l = float(input("Medida do lado:"))
       if ap == 'área':
         print("A área do seu triângulo é:", (l**2) * (3**(1/2)/4))
       if ap == 'perímetro':
         print("A área do seu triângulo é:", l * 3)
#Trapézio===================================
    if forma == 'trapézio':
       b = float(input("Medida da base menor:"))
       B = float(input("Medida da base maior:"))
       h = float(input("Medida da altura:"))
       print("A área do seu trapézio é:", (B + b)/ 2)