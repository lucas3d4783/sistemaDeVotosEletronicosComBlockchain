# BlockchainVoting
Sistema de votação utilizando o framework Django e a tecnologia de blockchain.
Neste projeto, foi desenvolvida uma blockchain genérica que funciona de forma distrbuída, visando disponibilizar ela para outras aplicações, via uma API REST. Será detalhada a implementação da aplicação em seus mínimos detalhes, visando ajudar futuros pesquisadores que desejarem estudar a tecnologia de blockchain, a motivação de detalhar a implementação do projeto, foi por notar que há muito conteúdo teórico em periódicos e online, porém há poucos conteúdos práticos que abordam o desenvolvimento de uma blockchain, ainda mais funcionando de forma distribuída. Para prova de conceito, foi desenvolvido uma aplicação web voltada para a votação eletrônica que vai acessar a API como uma aplicação cliente do web service, para armazenar informações sobre seus processos eleitorais.


## Intalação do Ambiente Virtual (opcional)

pip intall virtualenv

virtualenv venv

source venv/bin/activate

## Configuração do Ambiente

sudo apt install python3.x

apt install python3-pip

pip3  install django==2.2.6

pip3 install pillow (manipulação de imagens)

pip3 isntall Pyro4 (manipulação de objetos remotos objetos remotos)

Em um terminal deve ser executado o comando pyro-ns vai ser utilizado para acessar objetos remotos com nomes amigáveis, por exemplo:
PYRO:obj_dcf713ac20ce4fb2a6e72acaeba57dfd@localhost:51850
PYRO:custom_name@localhost:51851

Em outro terminal deve ser executado o comando ...... para a criação de uma blockchain remota.



# Algumas Telas do Sistema
## Desktop
<div align="center" style="padding='3%'">
  <img src="prints/1.png" class="img-fluid" style="" width="95%">
  <img src="prints/2.png" class="img-fluid" width="95%">
  <img src="prints/3.png" class="img-fluid" width="95%">
  <img src="prints/4.png" class="img-fluid" style="" width="95%">
  <img src="prints/5.png" class="img-fluid" width="95%">
  <img src="prints/6.png" class="img-fluid" width="95%">
  <img src="prints/7.png" class="img-fluid" style="" width="95%">
  <img src="prints/8.png" class="img-fluid" width="95%">
  <img src="prints/9.png" class="img-fluid" width="95%">
  <img src="prints/10.png" class="img-fluid" style="" width="95%">
  <img src="prints/11.png" class="img-fluid" width="95%">
  <img src="prints/12.png" class="img-fluid" width="95%">
  <img src="prints/13.png" class="img-fluid" style="" width="95%">
  <img src="prints/14.png" class="img-fluid" width="95%">
  <img src="prints/15.png" class="img-fluid" width="95%">
</div>

## Mobile
<div align="center">
  <img src="prints/6.jpg" class="img-fluid" style="" width="45%">
  <img src="prints/7.jpg" class="img-fluid" width="45%">
  <img src="prints/8.jpg" class="img-fluid" width="45%">
</div>

## Integração da Blockchain com a API REST
<div align="center" style="padding='3%'">
  <img src="prints/api.png" class="img-fluid" style="" width="95%">
</div>

