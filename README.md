# HelloCrewai Crew

Bem-vindo ao projeto HelloCrewai Crew, desenvolvido com [crewAI](https://crewai.com). Este template foi criado para ajudar você a configurar um sistema de IA multiagente de forma simples, aproveitando o framework poderoso e flexível fornecido pela crewAI. Nosso objetivo é permitir que seus agentes colaborem de maneira eficaz em tarefas complexas, maximizando sua inteligência coletiva e capacidades.

## Instalação

Certifique-se de ter o Python >=3.10 <3.14 instalado em seu sistema. Este projeto utiliza o [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências e pacotes, proporcionando uma experiência de configuração e execução simplificada.

Primeiro, caso ainda não tenha, instale o uv:

```bash
pip install uv
```

Em seguida, navegue até o diretório do seu projeto e instale as dependências:

(Opcional) Trave as dependências e instale-as usando o comando CLI:

```bash
crewai install
```

### Personalização

**Adicione sua `OPENAI_API_KEY` no arquivo `.env`**

- Modifique `src/hello_crewai/config/agents.yaml` para definir seus agentes
- Modifique `src/hello_crewai/config/tasks.yaml` para definir suas tarefas
- Modifique `src/hello_crewai/crew.py` para adicionar sua própria lógica, ferramentas e argumentos específicos
- Modifique `src/hello_crewai/main.py` para adicionar entradas personalizadas para seus agentes e tarefas

## Executando o Projeto

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute este comando a partir da pasta raiz do seu projeto:

```bash
crewai run
```

Este comando inicializa o HelloCrewai Crew, montando os agentes e atribuindo as tarefas conforme definido na sua configuração.

Este exemplo, sem modificações, irá criar um arquivo `report.md` com o resultado de uma pesquisa sobre LLMs na pasta raiz.

## Entendendo sua Equipe

O HelloCrewai Crew é composto por múltiplos agentes de IA, cada um com funções, objetivos e ferramentas únicas. Esses agentes colaboram em uma série de tarefas, definidas em `config/tasks.yaml`, aproveitando suas habilidades coletivas para alcançar objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente da sua equipe.

## Suporte

Para suporte, dúvidas ou feedback sobre o HelloCrewai Crew ou crewAI:

- Visite nossa [documentação](https://docs.crewai.com)
- Entre em contato pelo nosso [repositório no GitHub](https://github.com/joaomdmoura/crewai)
- [Junte-se ao nosso Discord](https://discord.com/invite/X4JWnZnxPb)
- [Converse com nossa documentação](https://chatg.pt/DWjSBZn)

Vamos criar maravilhas juntos com o poder e a simplicidade do crewAI.
