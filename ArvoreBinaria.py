#Arvore binaria


class Node:
    def __init__(self,dado = None):
        self.dado = dado
        self.left = None
        self.right = None


class  tree:
    def __init__(self,Dado):
        self.root = Node(Dado)

    def AdicionarDado(self,Dado,root = None):

        if root is None:
            root = self.root


        if Dado < root.dado:
            if root.left is None:
                root.left = Node(Dado)

            else:
                self.AdicionarDado(Dado,root.left)    

        elif Dado > root.dado:
            if root.right is None:
                root.right = Node(Dado)
            else:
                self.AdicionarDado(Dado,root.right)    

    def RecuperarDados(self,root = None): # em ordem simetrica

        if root is None:
            root = self.root

        if root.left:
            self.RecuperarDados(root.left)

        print(" ",end="")    
        print(root.dado,end="")
        print(" ",end="")  

        if root.right:
            self.RecuperarDados(root.right)
               


    def RecuperarDados2(self,root = None): # pre-ordem

        if root is None:
            root = self.root 

        print(root.dado)

        if root.left:
            self.RecuperarDados2(root.left)

        if root.right:
            self.RecuperarDados2(root.right)          

    def RecuperarDados3(self,root = None):
        if root is None:
            root = self.root

        if root.left:
            self.RecuperarDados3(root.left)

        if root.right:
            self.RecuperarDados3(root.right)

        print(root.dado)

    def BuscarDados(self,root = None,date = None):
        if root is None:
            root = self.root
        
        if date is None:
            print("not found")

        if root.dado == date:
            print("True - key this tree")        

        elif date < root.dado:
            if root.left is None:
                print("not found")
            else:    
                self.BuscarDados(root.left,date)
        
        elif date > root.dado:
            if root.right is None:
                print("not found")
            else:
                self.BuscarDados(root.right,date)    
        
        else:
            print("Not found")


    def remocaoFolha(self,date = None,root = None,):

        if root is None:
            root = self.root
     
        if date < root.dado:
            root.left = self.remocaoFolha(date,root.left)
            
            

        elif date > root.dado:
            root.right = self.remocaoFolha(date,root.right,)
            
            
        else:
            if (root.left is None) and (root.right is None ):
                return None

            elif (root.left is None) or (root.right is None):
                if root.left:
                    return root.left

                elif root.right:
                    return root.right

            elif (root.left) and (root.right):

                sub = self.min(root.right)
                root.dado = sub.dado
                root.right = sub.right          

        return root


    #   descobrir o fator de balanceamento das subárvores (dado por Fator_balanc = A_dir - A_esq),
    # sendo o fator de balenceamento ideal deve estar entre -1 e 1, ou seja deve estar entre -1,0
    # e 1.
            
    def min(self,root):
        
        while root.left:
            root = root.left
            
        return root                

    def rotacaoDir(self,root = None):

        if root is None:
            root = self.root

        pai = root
        root = root.left
        pai.left = root.right
        root.right = pai        

        return root
        
    def rotacaoEsq(self,root = None):

        if root is None:
            root = self.root

        pai = root
        root = root.right
        pai.right = root.left
        root.left = pai

        return root



if __name__ == "__main__":

    teste = tree(3)

    teste.AdicionarDado(4)
    teste.AdicionarDado(5)

    #teste.AdicionarDado(25)
    #teste.AdicionarDado(20)
    #teste.AdicionarDado(15)
    #teste.AdicionarDado(35)
    #teste.AdicionarDado(80)
    #teste.AdicionarDado(200)
    #teste.AdicionarDado(300)
   
    
    #teste.RecuperarDados()
    '''
    print("")
    teste.RecuperarDados2()
    print("")
    teste.RecuperarDados3()
    '''
    #teste.BuscarDados(None,24)
    #teste.AdicionarDado(21)
    #teste.BuscarDados(None,21)
    #teste.BuscarDados(None,300)
    #teste.remocaoFolha(None,30)
    #teste.remocaoFolha(25)
    #teste.remocaoFolha(None,80)
    #teste.BuscarDados(None,300)
    #teste.RecuperarDados()
    
    teste.RecuperarDados2()
    teste.RecuperarDados2(teste.rotacaoEsq())
    
