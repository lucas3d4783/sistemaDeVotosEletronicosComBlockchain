from django.shortcuts import render, redirect, get_object_or_404
from eleicoes.models import Eleicao, Eleicao_eleitor, Eleicao_candidato
from usuarios.models import Usuario
from blockchain.models import Block_eleicao, Chain_eleicao
import datetime
import Pyro4

def index(request): #quando for solicitado o url index, será encaminhado o index.html
    if not request.session.get('logado'): # se não estiver logado
        return redirect('login') # redireciona para a tela de login
    if request.session.get('user_tipo') != 'Eleitor': # se não for ELEITOR
        erro = "Apenas ELEITORES podem acessar esta parte do sistema!"
        context = {
            'erro': erro,
        }
        return render(request, 'eleitor/index.html', context) # mensagem de erro
    title = 'Eleitor' # Definir título da página
    context = {
        'title': title,
    }
    return render(request, 'eleitor/index.html', context)

def consulta(request): #quando for solicitado o url index, será encaminhado o index.html
    if not request.session.get('logado'): # se não estiver logado
        return redirect('login') # redireciona para a tela de login
    if request.session.get('user_tipo') != 'Eleitor': # se não for administrador
        erro = "Apenas ELEITORES podem acessar esta parte do sistema!"
        context = {
            'erro': erro,
        }
        return render(request, 'eleitor/index.html', context) # mensagem de erro
    title = 'Consulta' # Definir título da página
    pk = request.session.get('user_pk')
    #print(pk)
    usuario = get_object_or_404(Usuario, pk=pk) # realizar a instância do objeto que corresponde ao usuário logado
    #print(usuario.nome + " " + usuario.sobrenome)
    if usuario.tipo == "Eleitor": # testa se o usuário é eleitor ou não 
        eleicoes_eleitor = Eleicao_eleitor.objects.filter(eleitor__pk=pk) #
        context = {
            'title': title,
            'eleicoes_eleitor': eleicoes_eleitor,
        }
        return render(request, 'eleitor/consulta.html', context) 

    erro="Só eleitores tem permissão de acessar esta página!"
    context = {
        'title': title,
        'erro': erro
    } 

    return render(request, 'eleitor/consulta.html', context) #retorna mensagem de erro, pois o candidato não tem o direito de votar

def votacao(request, pk): # Realização do voto 
    if not request.session.get('logado'): # se não estiver logado
        return redirect('login') # redireciona para a tela de login
    if request.session.get('user_tipo') != 'Eleitor': # se não for ELEITOR
        erro = "Apenas ELEITORES podem acessar esta parte do sistema!"
        context = {
            'erro': erro,
        }
        return render(request, 'eleitor/votacao.html', context) # mensagem de erro
    if request.method == 'POST':
        return redirect('index')

    eleicao_pk = pk
    eleitor_pk = request.session.get('user_pk')

    ns = Pyro4.locateNS() # localizando o servidor de nomes
    uri = ns.lookup('blockchain') # obtendo a uri do objeto remoto
    o = Pyro4.Proxy(uri) #pegando o objeto remoto

    ja_votou = o.verificaSeJaVotou(eleicao_pk, eleitor_pk)
    print("QUANTIDADE de BLOCOS: ", o.get_chain_size())
    print(ja_votou, eleicao_pk, eleitor_pk)
    eleicao = get_object_or_404(Eleicao, pk=pk)
    candidatos = Eleicao_candidato.objects.filter(eleicao__pk=pk)
    eleitor = request.session.get('user_pk')

    if ja_votou:
        ja_votou = """Você já votou! Aguarde o término da eleição para conferir os resultados. 
        Em caso de dúvidas consulte a nossa equipe de suporte: lucas.reichert@redes.ufsm.br"""
        context = {
            'ja_votou': ja_votou,
            'candidatos': candidatos,
            'eleicao': eleicao,
            'eleitor': eleitor,
        }
        return render(request, 'eleitor/votacao.html', context)
    

    context = {
        'candidatos': candidatos,
        'eleicao': eleicao,
        'eleitor': eleitor,
    }

    return render(request, 'eleitor/votacao.html', context) 
    # deve ser direcionado para uma página para selecionar o respectivo candidato da respectiva eleição

def selecionar_candidato(request, eleicao_pk, eleitor_pk, candidato_pk): # Realização do voto 
    if not request.session.get('logado'): # se não estiver logado
        return redirect('login') # redireciona para a tela de login
    if request.session.get('user_tipo') != 'Eleitor': # se não for ELEITOR
        erro = "Apenas ELEITORES podem acessar esta parte do sistema!"
        context = {
            'erro': erro,
        }
        return render(request, 'eleitor/index.html', context) # mensagem de erro
    
    user_pk = request.session.get('user_pk') # foi substituido para garantir que o usuário não vai enviar a chave errada

    ns = Pyro4.locateNS() # localizando o servidor de nomes
    uri = ns.lookup('blockchain') # obtendo a uri do objeto remoto
    o = Pyro4.Proxy(uri) #pegando o objeto remoto
    print(eleicao_pk, user_pk)
    ja_votou = o.verificaSeJaVotou(eleicao_pk, user_pk)
    
    if ja_votou:
        print("Você já votou nesta Eleição")
    else:
        #geração de um bloco referente ao voto
        o.criarBloco(eleicao_pk, user_pk, candidato_pk) #criando bloco
        print(o.getChain())
        print("STATUS da Chain: ", o.isChainValid())
        print("QUANTIDADE de BLOCOS: ", o.get_chain_size())
   


    #dados = "{ 'eleicao': " +eleicao_pk+", 'eleitor': "+eleitor_pk+", 'candidato': "+candidato_pk+"}"

    #chain = Chain_eleicao()
    
    #gerando bloco genesis
    #bloco = chain.get_genesis_block()
    #print(bloco.index)
    #print(bloco.timestamp)
    #print(bloco.data)
    #print(bloco.previous_hash)
    #print(bloco.hash)

    #adicionando o bloco com os dados do voto
    #chain.add_block(dados)
    #chain.add_block(dados)
    #chain.add_block(dados)
    #chain.add_block(dados)

    #percorrendo os blocos da chain
    #for bloco in chain.blocks:
    #    print("------------------ BLOCO "+str(bloco.index)+" ------------------")
    #    print("INDEX: "+str(bloco.index))
    #    print("TIMESTAMP: "+str(bloco.timestamp))
    #    print("DADOS: "+str(bloco.data))
    #    print("HASH DO BLOCO ANTERIOR: "+str(bloco.previous_hash))
    #    print("HASH DO BLOCO: "+str(bloco.hash))
    #    print("---------------------------------------------\n")


    #criação do bloco referente ao voto
    #bloco = Block_eleicao(0, 
    #    datetime.datetime.utcnow(), 
    #    dados, 
    #    'arbitrary')

    #bloco.save() não funcionou o save

    #print(bloco.index)
    #print(bloco.timestamp)
    #print(bloco.data)
    #print(bloco.previous_hash)
    #print(bloco.hash)

    return redirect('index')


