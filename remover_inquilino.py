def remove_item(lista_inquilinos,*args):
        deletar = list(args)
        for item in deletar:
            while item in lista_inquilinos:
                lista_inquilinos.remove(item)
            return lista_inquilinos