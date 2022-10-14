from pickle import dump, load

def escribirObjeto(objeto):
    """
    recibe un objeto y lo guarda.
    """
    with open(f'{repr(objeto)}','wb') as archivo:
        dump(objeto,archivo)
        
def leerObjeto(objeto):
    """
    recibe nombre de archivo a leer y devuelve el objeto
    """
    with open(f'{objeto}','rb') as archivo:
        return load(archivo)
