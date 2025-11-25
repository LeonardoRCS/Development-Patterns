# Trabalho de Engenharia de Software II - Padrões de Projeto (GoF)

**Alunos:** Leonardo R.C.S. e Tiago Hasse
**Padrões Escolhidos:** Command e Iterator
**Categoria:** Padrões Comportamentais

## 1. Introdução
Este repositório contém exemplos práticos e teóricos sobre dois padrões de projeto comportamentais do livro "Design Patterns" (GoF): Command e Iterator. O objetivo é demonstrar problemas de acoplamento e complexidade de código e como esses padrões resolvem tais questões.

## 2. Padrão Command
**O que é:** O Command é um padrão que encapsula uma solicitação como um objeto. Isso permite parametrizar clientes com diferentes solicitações, enfileirar ou registrar (log) solicitações e suportar operações que podem ser desfeitas (undo).

**Cenário do Exemplo:** Um controle remoto universal para automação residencial (Ligar luzes).
- **Sem o padrão:** O botão precisa saber exatamente qual classe e método chamar, criando alto acoplamento.
- **Com o padrão:** O botão apenas executa um comando genérico (`execute`), sem saber quem vai realizar a ação final.

## 3. Padrão Iterator
**O que é:** O Iterator permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore, etc.).

**Cenário do Exemplo:** Uma lista de canais de TV.
- **Sem o padrão:** O cliente precisa saber se a coleção é um Array ou uma Lista Encadeada para percorre-la (usando índices, por exemplo).
- **Com o padrão:** O cliente usa uma interface comum (`temProximo`, `proximo`) e consegue percorrer qualquer coleção sem saber como ela foi implementada internamente.