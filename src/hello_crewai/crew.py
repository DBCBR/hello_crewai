from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import xml.sax.saxutils as saxutils

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class HelloCrewai():
    """HelloCrewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def exploratory_tester(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['exploratory_tester'],
            verbose=True
        )

    @agent
    def accessibility_analyst(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['accessibility_analyst'],
            verbose=True
        )

    @agent
    def performance_auditor(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['performance_auditor'],
            verbose=True
        )

    @agent
    def security_checker(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['security_checker'],
            verbose=True
        )

    @agent
    def documentation_specialist(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['documentation_specialist'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def testar_site(self) -> Task:
        return Task(
            config=self.tasks_config['testar_site'],  # type: ignore[index]
        )

    @task
    def avaliar_acessibilidade(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['avaliar_acessibilidade'],
        )

    @task
    def auditar_performance(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['auditar_performance'],
        )

    @task
    def verificar_seguranca(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['verificar_seguranca'],
        )

    @task
    def documentar_relatorio(self) -> Task:
        return Task(
            config=self.tasks_config['documentar_relatorio'],
            output_file='relatorio.md'
        )

    @task
    def documentar_relatorio_xml(self) -> Task:
        return Task(
            config=self.tasks_config['documentar_relatorio_xml'],
            output_file='relatorio.xml',
            # Adicione um template tabular para Excel:
            xml_template="""
<Relatorio>
  <Bugs>
    <Bug>
      <Area></Area>
      <Tipo></Tipo>
      <Descricao></Descricao>
      <Impacto></Impacto>
      <PassosReproducao></PassosReproducao>
      <ComportamentoEsperado></ComportamentoEsperado>
      <ComportamentoAtual></ComportamentoAtual>
      <Evidencia></Evidencia>
      <Recomendacao></Recomendacao>
    </Bug>
    <!-- Repita para cada bug -->
  </Bugs>
  <Sugestoes>
    <Sugestao>
      <Area></Area>
      <Descricao></Descricao>
      <Impacto></Impacto>
    </Sugestao>
    <!-- Repita para cada sugestão -->
  </Sugestoes>
</Relatorio>
"""
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HelloCrewai crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical,  # In case you wanna use that instead
            # https://docs.crewai.com/how-to/Hierarchical/
        )


def escape_xml(texto):
    return saxutils.escape(texto, {'"': "&quot;", "'": "&apos;"})


# Exemplo de uso:
campo = "<label>Nome</label>"
xml = f"<Descricao>{escape_xml(campo)}</Descricao>"
# Resultado: <Descricao>&lt;label&gt;Nome&lt;/label&gt;</Descricao>
