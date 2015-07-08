|<a href='http://code.google.com/p/aula/'>Home</a>|<a href='http://code.google.com/p/aula/wiki/Equipe_do_Sistema'>Equipe</a> |<a href='http://code.google.com/p/aula/wiki/Descricao_do_Sistema'>Descrição do Sistema</a>| **Requisitos** |<a href='http://code.google.com/p/aula/wiki/Casos_de_Uso'>Casos de Uso</a>|<a href='http://code.google.com/p/aula/wiki/Diagrama_UC'>Diagrama Caso de Uso</a>|<a href='http://code.google.com/p/aula/wiki/Database'>Database</a>|
|:------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:---------------|:-------------------------------------------------------------------------|:--------------------------------------------------------------------------------|:-----------------------------------------------------------------|

# Requisitos #

Requisitos são definidos como funções ou capacidades que devem estar de acordo com o sistema. Nessa fase deveremos elucidar os requisitos do sistema, definindo de uma forma breve as funcionalidades e aplicações que o sistema pode oferecer, principalmente para os usuários finais, que são os professores, monitores e alunos. Estes serão acessados através de níveis diferenciados, desde consultas rápidas até a inserção de informação ao sistema.

## Requisitos Funcionais ##
Os requisitos funcionais expressam o comportamento de um software. As informações de entrada, o processamento e a saída emitida por uma funcionalidade são informações necessárias para especificar o requisito do referido grupo.

  * F001: Busca realizada através de filtros que centralizam as informações referentes a aulas, locais e horários;
  * F002: Horário de aulas já confirmadas;
  * F003: Informações referentes a salas, laboratórios e auditórios (quantidade total, funcionais e disponíveis);
  * F004: O aluno terá acesso às funções básicas, que são: procurar por salas, laboratórios e auditórios;
  * F005: Professores terão acesso às funções avançadas, que são:  funções básicas  + reserva de salas, laboratórios e auditórios;
  * F006: Administradores terão acesso total a todas as funções e dados + gerenciamento de locais + gerenciamento de professores, disciplinas, departamentos e locais;
  * F007: Os filtros serão distribuídos nas seguintes categorias: curso, disciplina, local e horário;


## Requisistos Não-funcionais ##
Os requisitos não funcionais mapeiam os aspectos qualitativos de um software .
  * NF001: Servidor local disponibilizado pela universidade. De preferência servidor Apache, banco de dados MySQL em um ambiente Linux;
  * NF002: Dados de entrada e saída armazenados em banco de dados;
  * NF003: Interface limpa, fácil e bastante intuitiva, além de prática;
  * NF004: Comunicação realizada através de terminal ligado à intranet da universidade;