def palabraAgu(nombre_archivo):
    
    vocales_tildadas = "áéíóúÁÉÍÓÚ"
    
    
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        palabras = f.read().split()  
    
    
    with open("C:/Users/linit/Downloads/palabras/nancy.txt", 'w', encoding='utf-8') as nancy:
        
        for palabra in palabras:
            
            if len(palabra) >= 2:
                
                ultima_letra = palabra[-1]
                
                
                if len(palabra) > 1:
                    penultima_letra = palabra[-2]
                else:
                    penultima_letra = ''
                
                
                if ultima_letra in vocales_tildadas:
                    nancy.write(palabra + "\n")  

                
                elif (ultima_letra in "nsNS") and (penultima_letra in vocales_tildadas):
                    nancy.write(palabra + "\n")  


palabraAgu("jose.txt")
