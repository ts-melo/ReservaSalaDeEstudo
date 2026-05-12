# Sistema de Reserva de Salas de Estudo

## Visão Geral
O sistema permite:
* Consultar a disponibilidade de salas em intervalos de tempo.
* Realizar reservas com diferentes politicas de colisão.
* Notificar usuários sobre alterações ou cancelamentos de reservas.

---

## Padrões de Projeto (Requisitos Obrigatórios)
| Padrão | Papel no Exercício | Pontos de Atenção |
| :--- | :--- | :--- |
| **Factory Method** | Instancia `SalaIndividual`, `SalaGrupo` e `SalaLaboratorio` sem acoplamento. | Criadas 3 subclasses de Sala. |
| **Strategy** | Define a `PoliticaDeReserva` para detectar colisões (Padrao vs. Prioridade Docente). | Troca de regras em tempo de execução. |
| **Observer** | Propaga notificações de alteração/cancelamento para usuários e serviços de relatório. | Implementação de push e pull de dados. |
| **Singleton** | Gerencia o `ReservaRepositorio` de forma única na memória. | Garantia de thread-safety com Lock. |
| **Decorator** |[BONUS] Adiciona serviços como `Equipamentos` e `Limpeza` às reservas existentes. | Wrappers para adicionar funcionalidades às reservas. |


---

## Estrutura do Repositório
* ``src/`` : codigo-fonte principal
* ``docs/`` : diagramas e documentação complementar

---

## Instruções de Uso

### Pré-Requisitos
* Python 3.10 ou superior

### Como usar
1. Clone o repositório
```bash
   git clone [https://github.com/ts-melo/ReservaSalaDeEstudo.git](https://github.com/ts-melo/ReservaSalaDeEstudo.git)
```
2. Acesse a pasta do código-fonte:
```bash
    cd ReservaSalaDeEstudo/src
```

3. Execute o arquivo principal:
```bash
    python main.py
```

4. Ou Utilize o menu interativo:
```bash
    python menu_interativo.py
```
## Navegação no Menu Interativo
1. **Fazer Reserva**:
Escolha o tipo de usuário (Docente/Estudante) para fazer as reservas e testar as diferentes Strategies de colisão.
2. **Adicionar**:
Teste o Decorator adicionando serviços de limpeaz ou equipamentos.
3. **Cancelar Reserva**:
Veja o observer em ação notificando o cancelamento.
4. **Relatório Diário**:
Consulta o singleton para listar todas as salas ocupadas.

## Autores
* Rafael Kenzo
* Thaís Souza de Melo