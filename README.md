# Sistema de Avaliação de Jogos

## O Que Foi Desenvolvido Até o Momento:
 - CRUD para inserção de jogos
 - Templates HTML e backend em Django
 - Controle de acesso por usuários
 - Sistema de avaliação de usuários em um jogo
 - Usuário pode ver avaliação de outros usuários e ver jogos que já avaliou

## Escopo do projeto
  - Sistema armazena uma biblioteca de jogos 
  - Usuários se cadastram e logam na plataforma 
  - Usuários podem avaliar um jogo e vê-los no mural
  - Usuários podem ver avaliações de outro e adicionar jogos no mural

## Manual do usuário

### Instalação do projeto

  Para baixar o projeto, em uma máquina com Docker instalado, no terminal faça:
  ```
docker pull arthurprioli/listador_jogos
  ```
  Depois que a imagem docker estiver na sua máquina, faça:
  ```
 docker run -d -p 8000:8000 arthurprioli/listador_jogos:latest
  ```

  Assim, execute em seu navegador colando na barra de URL:
  ```
localhost:8000
  ```
### Usando o projeto
**Testando criação de usuário e cadastro de jogo**
 - Para cadastrar um jogo no mural, primeiro você precisa ter um usuário cadastrado, vá na página de registro e crie seu usuário.
 - Após criado o usuário, faça login e vá para a página Home
 - Na página home, clique em Criar um novo jogo e insira o jogo desejado, como foto da capa, cole uma URL de imagem.
 - Ao cadastrar o jogo, abra o jogo e escreva sua avaliação.

**Testando diferentes visões para usuário e um usuário ver avaliações do outro**
 - Para testar a visualização de outros usuários, crie um novo usuário no registro, faça login com o mesmo e clique no jogo que o
primeiro usuário criado avaliou

**Para alterar um jogo, aperte em Atualizar e insira as informações novas/corrigidas**
**Para remover um jogo, clique em Excluir e confirme a exclusão do jogo**

