import matplotlib.pyplot as plt


class Texto():
    '''
    Classe que serve para criar um objeto com o texto de uma notícia, que após processada gera um objeto da classe Palavra para cada palavra única na notícia.
    Para instanciar:
        Texto( str )
        onde str é uma string da notícia
    Atributos:
        original -> onde é guardado o texto original que foi submetido
        lista -> onde é guardada uma lista das palvras do texto (depois de limpo)
        objetosPalavras -> lista de apontadores para os objetos Palavra()
    Métodos:
        limparNoticia( str ):
            Processa a string com a notícia, passando tudo para carateres minúsculos e separando as palavras.
            Verifica se cada palavra é alfabética, tem uma dimensão maior que 1 (para excluir "a", "e", "o") e incluí as palavras com hífen.
            Devolve uma lista com as palavras que passaram as condições mencionadas.
        criarPalavra():
            Cria os objetos Palavra() com as palavras únicas e devolve uma lista com os apontadores para cada um dos objetos que criou.
            Exclui as Conjunções definidas.
            Passa para cada objeto Palavra, a própria palavra e a frequência com que esta aparece na notícia original.
        devolveObjetos():
            Devolve uma lista com os apontadores para os objetos Palavra.
        top():
            Devolve uma lista de apontadores para os dez objetos com maior frequência.
        hist():
            Gera um histograma com as 10 palavras mais utilizadas e respetiva frequência.
            É utilizada a libraria matplotlib para gerar o gráfico.
            As labels são rodadas para ficar na vertical.
    '''
    def __init__(self, noticia):
        self.__original = noticia
        self.__lista = self.limparNoticia(noticia)
        self.__objetosPalavras = self.criarPalavra()
        
    def limparNoticia(self, noticia):
        noticiaTemporario = noticia.replace('.', '')
        return [i for i in noticiaTemporario.lower().split() if (i.isalpha() and not len(i) == 1) or ('-' in i) ]

    def criarPalavra(self):
        palavrasUnicas = []
        conjuncoes = ['ao', 'um', 'mas', 'nem', 'já', 'ou', 'ora', 'que', 'quer', 'pois', 'por', 'de', 'da', 'do', 'se', 'para', 'as', 'os', 'até', 'em', 'no', 'na', 'nos', 'nas', 'às']
        apontadorPalavras =[]
        for i in self.__lista:
            if i not in palavrasUnicas:
                if i not in conjuncoes:
                    palavrasUnicas.append(i)
        for k in palavrasUnicas:
            freq = self.__lista.count(k)
            apontadorPalavras.append(Palavra(k, freq))
        return apontadorPalavras
    
    def devolveObjetos(self):
        return self.__objetosPalavras

    def top(self):
        self.__objetosPalavras.sort(key=lambda x: x.freq, reverse=True)
        palavrasTop = self.__objetosPalavras[:10]
        return palavrasTop

    def hist(self):
        labels = [i.palavra for i in self.top()]
        values = [i.freq for i in self.top()]
        plt.bar(labels, values)
        plt.xticks(labels, rotation='vertical')
        plt.yticks([i for i in range(1,max(values)+1,1)])
        plt.show()


class Palavra():
    '''
    Classe que serve para criar um objeto com uma palavra e com uma dada frequência.
     Para instanciar:
        Palavra( str, int )
        onde str é a string da palavra e int o valor da frequência
    Atributos:
        palavra -> palavra
        freq -> frequência
    '''
    def __init__(self, palavra, freq):
        self.palavra = palavra
        self.freq = freq


def main():
    '''
    Função que faz a gestão do menu.
    '''
    print('Bem-vindo ao Histograma de Palavras.')
    print('Programa desenvolvido por Bruno Araújo 80852 e Edgar Basto 93575.')
    op = 'continuar'
    noticia = 0
    while op == 'continuar':
        print('\nEscolha uma das seguintes opções:')
        print('\t1- Introduzir uma notícia.')
        print('\t2- Imprimir lista de todas as palavras únicas.')
        print('\t3- Obter Histograma com as 10 palavras mais utilizadas.')
        print('\t4- Sair do programa.')
        op = input('Introduza uma opção: ')
        if op == '1':
            texto = input('\nIntroduza a notícia: ')
            noticia = Texto(texto)
            op = 'continuar'
        elif op == '2':
            if noticia is not 0:
                print('\n')
                print([i.palavra for i in noticia.devolveObjetos()])
            else:
                print('\nTem de introduzir uma notícia primeiro.\n')
            op = 'continuar'
        elif op == '3':
            if noticia is not 0:
                noticia.hist()
            else:
                print('\nTem de introduzir uma notícia primeiro.\n')
            op = 'continuar'
        elif op == '4':
            print('\nObrigado por utilizar no nosso programa.')
        else:
            print('\nOpção não encontrada.\n')
            op = 'continuar'


main()


