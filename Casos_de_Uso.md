|<a href='http://code.google.com/p/aula/'>Home</a>|<a href='http://code.google.com/p/aula/wiki/Equipe_do_Sistema'>Equipe</a> |<a href='http://code.google.com/p/aula/wiki/Descricao_do_Sistema'>Descrição do Sistema</a>|<a href='http://code.google.com/p/aula/wiki/Especificacao_de_Requisitos'>Requisitos</a>| **Casos de Uso**|<a href='http://code.google.com/p/aula/wiki/Diagrama_UC'>Diagrama Caso de Uso</a>|<a href='http://code.google.com/p/aula/wiki/Database'>Database</a>|
|:------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:----------------|:--------------------------------------------------------------------------------|:-----------------------------------------------------------------|

# Especificação de Casos de Uso #

Um caso de uso representa uma parte discreta da interação entre um usuário (humano ou máquina) e o sistema. Cada caso de uso tem uma descrição a qual descreve sua funcionalidade.


---


## UC0001 - Gerenciamento de Departamento ##

| **Objetivo** | Cadastrar, editar e excluir os departamentos existentes na universidade. |
|:-------------|:-------------------------------------------------------------------------|
| **Descrição** | O administrador registra, edita e exclui informações do departamento como ID do departamento, nome do departamento, coordenador(es). |
| **Ator**     | Administrador.                                                           |
| **Prioridade** | Média.                                                                   |
| **Pré-condição** | O usuário estar logado como administrador.                               |
| **Pós-condições** | Os departamentos são cadastrados e já podem vincular-se aos cursos, são editados ou excluídos corretamente. |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - Ao regisrar, o Administrador informa ao sistema as informações necessárias sobre o departamento, como: Nome, Coordenador(es) e o ID do departamento. |
| 2 - Ao editar, o administrador acessa as informações já cadastradas do departamento e faz as alterações necessárias, ao final, o programa rearmazena os dados. |
| 3 - Ao excluir, o administrador informa o ID do departamento que deseja excluir, e o sistema exclui todas as informações relacionadas ao departamento. |

| **Fluxos alternativos** |
|:------------------------|
| 1.1 Se ao registrar, alguma informação digitada não estiver dentro dos padrões para registro, o sistema retorna a mensagem "[ERRO 006 ](.md) Erro no cadastro. Verifique se os itens foram inseridos corretamente.".|
| 1.2 Tentativa de registro de departamento e ele já existir. O existente não é sobrescrito. O sistema retorna uma mensagem de erro "[ERRO 005 ](.md)Departamento ja existente.". |
| 2.1 Se ao tentar editar as informações de um determinado departamento e for digitado alguma entrada fora dos padrões para edição, o sistema retorna uma mensagem "[ERRO 007 ](.md) Erro na edição."|
| 2.2 Se ao tentar editar as informações de um determinado departamento que não possui cadastro, o programa informa uma mensagem de erro "[ERRO 002 ](.md)Departamento nao existente." |
| 3.1 Se ao tentar excluir as informações de um departamento informando alguma entrada fora dos padrões de exclusão,o programa retorna uma mensagem "[ERRO 004 ](.md)Erro na exclusao." |
| 3.2 Se ao tentar excluir as informações de um departamento informando seu ID incorretamente, o sistema retorna uma mensagem "[ERRO 002 ](.md)Departamento nao existente."|


---


## UC0002 - Gerenciamento de Cursos ##

| **Objetivo** | Cadastrar, editar ou excluir todas os cursos da Universidade. |
|:-------------|:--------------------------------------------------------------|
| **Descrição** | Cadastrar todas os cursos da Universidade, afim de evitar que um curso possua dois ou mais nomes correspondentes a ele. |
| **Ator**     | Administrador                                                 |
| **Prioridade** | Média.                                                        |
| **Pré-condição** | O tipo de usuário "Administrador" é selecionado para ter acesso ao sistema. |
| **Pós-condições** | Todos os cursos poderão ser cadastrados, editados ou excluídos corretamente. |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - Os cursos são cadastrados com sucesso, possuindo apenas um nome correspondente a cada um deles e a Foreign Key da id do departamento deve estar relacionada. O administrador deve estar atento, evitando que um mesmo curso seja cadastrado mais de uma vez. São informadas entradas como ID do curso, nome e departamento. |
| 2 - Ao editar, o administrador acessa as informações já cadastradas do curso e faz as alterações necessárias, ao final, o programa rearmazena os dados. |
| 3 - Ao excluir, o administrador informa o ID do curso que deseja excluir, e o sistema exclui todas as informações relacionadas ao curso. |

| **Fluxos alternativos** |
|:------------------------|
| 1.1 - Ao tentar cadastro de curso já existente, retorna uma mensagem "[ERRO 005 ](.md)Curso ja existente.". |
| 1.2 Se ao registrar, alguma informação digitada não estiver dentro dos padrões para registro, o sistema retorna a mensagem "[ERRO 006](.md) Erro no cadastro. Verifique se os itens foram inseridos corretamente ou existe disciplinas e aulas relacionadas com esse curso.".|
| 2.1 Se ao tentar editar as informações de um determinado curso e for digitado alguma entrada fora dos padrões para edição, o sistema retorna uma mensagem "[ERRO 007 ](.md)Erro na edição."|
| 2.2 Se ao tentar editar as informações de um determinado curso que não possui cadastro, o programa informa uma mensagem de erro "[ERRO 002 ](.md)Curso nao existente." |
| 3.1 Se ao tentar excluir as informações de um curso informando alguma entrada fora dos padrões de exclusão,o programa retorna uma mensagem "[ERRO 004 ](.md)Erro na exclusao.Verifique se existe disciplinas e aulas relacionadas com esse curso." |
| 3.2 Se ao tentar excluir as informações de um curso informando seu ID incorretamente, o sistema retorna uma mensagem "[ERRO 002 ](.md)Curso nao existente."|



---


## UC0003 - Gerenciamento de Disciplina ##

| **Objetivo** | Cadastrar, editar e excluir todas as disciplinas da Universidade. |
|:-------------|:------------------------------------------------------------------|
| **Descrição** | Cadastrar todas as disciplinas da Universidade, afim de evitar que uma disciplina possua dois ou mais nomes correspondentes a ela. |
| **Ator**     | Administrador                                                     |
| **Prioridade** | Média.                                                            |
| **Pré-condição** | O tipo de usuário "Administrador" é selecionado para ter acesso ao sistema. |
| **Pós-condições** | Todas as disciplinas poderão ser cadastradas, editados ou excluídas corretamente. |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - As disciplinas são cadastradas com sucesso, possuindo apenas um nome correspondente a cada uma delas. O administrador deve estar atento, evitando que uma mesma disciplina seja cadastrada mais de uma vez.São informadas entradas como ID da disciplina, nome, curso e período no seu cadastro. |
| 2 - Ao editar, o administrador acessa as informações já cadastradas da disciplina e faz as alterações necessárias, ao final, o programa rearmazena os dados. |
| 3 - Ao excluir, o administrador informa o ID da disciplina que deseja excluir, e o sistema exclui todas as informações relacionadas a essa disciplina. |

| **Fluxos alternativos** |
|:------------------------|
| 1.1 - Ao tentar cadastro de disciplina já existente, retorna uma mensagem "[ERRO 005 ](.md)Disciplina ja existente. ". |
| 1.2 Se ao registrar, alguma informação digitada não estiver dentro dos padrões para registro, o sistema retorna a mensagem "[ERRO 006 ](.md) Erro no cadastro. Verifique se os itens foram inseridos corretamente.".|
| 2.1 Se ao tentar editar as informações de uma determinada disciplina e for digitado alguma entrada fora dos padrões para edição, o sistema retorna uma mensagem "[ERRO 007 ](.md) Erro na edição."|
| 2.2 Se ao tentar editar as informações de uma determinada disciplina que não possui cadastro, o programa informa uma mensagem de erro "[ERRO 002 ](.md)Disciplina nao existente." |
| 3.1 Se ao tentar excluir as informações de uma disciplina informando alguma entrada fora dos padrões de exclusão,o programa retorna uma mensagem "[ERRO 004 ](.md)Erro na exclusao." |
| 3.2 Se ao tentar excluir as informações de uma disciplina informando um ID não existente, o sistema retorna uma mensagem "[ERRO 002 ](.md)Disciplina nao existente."|



---



## UC0004 - Gerenciamento de professores ##

| **Objetivo** | Cadastrar os professores. |
|:-------------|:--------------------------|
| **Descrição** | O administrador registra, edita e exclui informação de um professor. |
| **Ator**     | Administrador e Professor |
| **Prioridade** | Média.                    |
| **Pré-condição** | O usuário ter logado como Administrador. |
| **Pós-condições** | O professor é cadastrado. |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - Ao registrar, o Administrador informa ao sistema as informações necessárias sobre o professor, como: Nome, ID do professor(CPF), Senha, e o departamento;O CPF deve ser digitado contendo 11 caracteres (somente números)|
| 2 - Ao editar, o Administrador acessa as informações já cadastradas do professor, e faz as alterações necessárias, ao final, o programa re-armazena as informações do professor; |
| 3 - Ao excluir, o Administrador informa o número de registro relacionado a um professor que deseja excluir, e o sistema exclui todas as informações relacionadas ao número de registro;|

| **Fluxos alternativos** |
|:------------------------|
| 1.1 Se o CPF  for digitado de forma incorreta, o sistema deve informar uma mensagem de erro "[ERRO 002 ](.md)Usuario nao existente. ".  |
| 2.1 Se ao tentar consultar as informações de um determinado professor que não possui cadastro, o programa informa uma mensagem de erro "[ERRO 002 ](.md)Usuario nao existente. " |
| 2.2 Se ao tentar editar as informações de um determinado professor e for digitado alguma entrada fora dos padrões para edição, o sistema retorna uma mensagem "[ERRO 007 ](.md) Erro na edição."|
| 3.1 Se ao tentar excluir as informações de um professor informando um número de CPF incorreto, o programa retorna uma mensagem de erro "[ERRO 002 ](.md)Usuario nao existente. ".|
| 3.2 Se ao tentar excluir as informações de uma disciplina informando alguma entrada fora dos padrões de exclusão,o programa retorna uma mensagem "[ERRO 004 ](.md)Erro na exclusao." |



---


## UC0005 - Gerenciamento de Prédio ##

| **Objetivo** | Cadastrar, editar e excluir prédio. |
|:-------------|:------------------------------------|
| **Descrição** | O prédio é responsável pelo armazenamento de salas, laboratórios e auditórios, logo, é preciso a especificação dos mesmos referentes ao prédio. |
| **Ator**     | Administrador                       |
| **Prioridade** | Média.                              |
| **Pré-condição** | O tipo de usuário "Administrador" é selecionado e ter acesso ao sistema. |
| **Pós-condições** | O prédio é registrado, tem suas informações editadas ou excluídas. |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - Ao cadastrar, o administrador insere informações como ID do prédio e nome do prédio.|
| 2 - Ao editar, o administrador acessa as informações já cadastradas do prédio e faz as alterações necessárias, ao final, o programa rearmazena os dados. |
| 3 - Ao excluir, o administrador informa o ID do prédio que deseja excluir, e o sistema exclui todas as informações relacionadas a esse prédio. |

| **Fluxos alternativos** |
|:------------------------|
| 1.1 - Ao tentar cadastro de prédio já existente, retorna uma mensagem "[ERRO 005](.md)Predio ja existente.". |
| 1.2 Se ao registrar, alguma informação digitada não estiver dentro dos padrões para registro, o sistema retorna a mensagem "[ERRO 006 ](.md) Erro no cadastro. Verifique se os itens foram inseridos corretamente.".|
| 2.1 Se ao tentar editar as informações de um determinado prédio e for digitado alguma entrada fora dos padrões para edição, o sistema retorna uma mensagem "[ERRO 007 ](.md) Erro na edição."|
| 2.2 Se ao tentar editar as informações de um determinado prédio que não possui cadastro, o programa informa uma mensagem de erro "[ERRO 002 ](.md)Predio nao existente." |
| 3.1 Se ao tentar excluir as informações de um prédio informando alguma entrada fora dos padrões de exclusão,o programa retorna uma mensagem "[ERRO 004 ](.md)Erro na exclusao." |
| 3.2 Se ao tentar excluir as informações de um prédio informando um ID não existente, o sistema retorna uma mensagem "[ERRO 002 ](.md)Prédio nao existente."|


---


## UC0006 - Gerenciamento de Aulas ##

| **Objetivo** | Consiste em gerenciar o cadastro de aulas para locais, datas e horários. |
|:-------------|:-------------------------------------------------------------------------|
| **Descrição** | Poderá reservar e excluir reservas de aulas, informando entradas como ID do local, data, ID da disciplina e horário. |
| **Ator**     | Professor                                                                |
| **Prioridade** | Alta.                                                                    |
| **Pré-condição** | Todas os horários, aulas e salas já estão cadastradas e existir datas e horários livres para reservar aulas. |
| **Pós-condições** | A seleção é realizada.                                                   |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - Ao reservar, o professor informa entradas como ID do local, a data , o ID disciplina e a hora da reserva da aula.|
| 2 - Ao excluir, o professor informa o item a ser excluído.|

| **Fluxos alternativos** |
|:------------------------|
| 1.1 Se ao tentar reserva e a data estiver ocupada, o sistema retorna uma mensagem "[ERRO 005 ](.md) Reserva ja existente para determinada data."|
| 1.2 Se ao tentar reserva e o horário estiver ocupado, o sistema retorna uma mensagem "[ERRO 005 ](.md) Reserva ja existente para determinado horario."|
| 2.1 Se ao tentar deletar reserva que não possui horário cadastrado, o sistema informa a mensagem "[ERRO 004 ](.md)Erro na exclusao. Nao existe reserva nesse horario."|

---



## UC0007 - Busca ##

| **Objetivo** | Possibilitar ao usuário informações acerca de aulas, horários, cursos, disciplinas, professores, locais departamentos e prédios. |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------|
| **Descrição** | O usuário - que pode ser aluno, professor ou administrador - fará a busca da(s) aula(s) que deseja saber, informando ao sistema valores como o Departamento, o Curso, o Período e a Disciplina . |
| **Ator**     | Administrador, Professor e  Aluno                                                                                                |
| **Prioridade** | Alta.                                                                                                                            |
| **Pré-condição** | O sistema estar em pleno funcionamento e existirem aulas, horários, cursos, disciplinas, professores, locais, departamentos e prédios cadastrados. |
| **Pós-condições** |Após a busca é impresso na tela informação desejada.                                                                              |

## Cenários principais de sucesso ##

| **Usuário** |
|:------------|
| 1 - O usuário fará sua busca pela seleção na seguinte ordem: Departamento, Curso, Período e Disciplina . Após a  seleção o usuário clicará no botão "Buscar" e o sistema se encarregará da busca, e enfim imprimirá a informação desejada na tela. |


| **Fluxos alternativos** |
|:------------------------|
| 1. Campo selecionado não cadastrado: O sistema retorna a seguinte mensagem "Nao ha reserva para determinada busca." |



---



