# CHAT

### Um exemplo de chat

Este projeto simula salas de chat simples, permitindo que múltiplos usuários interajam em tempo real. A estrutura do código inclui dois componentes principais: o servidor e a interface de visualização do chat.

## Objetivo

Este repositório tem como objetivo demonstrar a implementação de um sistema básico de chat utilizando Python. O projeto simula a comunicação entre um servidor e vários clientes, onde cada cliente pode enviar e receber mensagens.

## Como Funciona

- **Servidor**: Gerencia as conexões e a comunicação entre os clientes. Ele escuta as mensagens enviadas e as transmite aos outros usuários.
- **Visualização (view.py)**: Interface onde os usuários podem enviar e receber mensagens.

## Tecnologias Utilizadas

- **Python 3.x** - Linguagem utilizada para implementar o servidor e a interface de chat.
- **Socket** - Biblioteca usada para criar a comunicação em rede entre o servidor e os clientes.

## Como Rodar o Projeto

### 1. Inicialize o servidor

Antes de qualquer coisa, é necessário rodar o servidor para gerenciar as conexões dos clientes. Para isso, no terminal, dentro da pasta do projeto, execute:

  ```bash
  python server.py
  ```

### 2. Inicie a simulação de chat

Após o servidor estar rodando, você pode iniciar a simulação de um cliente (usuário) em outro terminal, executando:

  ```bash
  python view.py
  ```

Isso abrirá a interface de chat onde você poderá enviar e receber mensagens.

## Estrutura de Pastas

  ```bash
  /chat
    server.py     # Código responsável pelo servidor de chat
    view.py       # Interface de visualização do chat
  ```

## Como Contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionando nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um pull request.
