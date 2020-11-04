

letra = ""
def  funcaoLetra ():
    letra = input ( "use os caracteres {[()]}:" )
    if  "{[()]}"  in  letra:
        print ( "Parâmetro true" )
        return  true
    else:
        print ( "Parâmetro falso" )
        return  false
funcaoLetra ()