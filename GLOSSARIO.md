# 📘 Glossário Técnico — Laboratório 1: Prefect, Docker e CI/CD

Este glossário tem como objetivo servir de referência rápida para estudantes durante a execução do laboratório. Cada termo técnico utilizado na prática é descrito brevemente para reforçar a compreensão dos conceitos trabalhados.

---

### 🔧 Worker
O *worker* é o componente do Prefect que executa os fluxos (flows). Ele monitora uma fila de trabalho (work pool) e executa os deployments atribuídos a ele, localmente ou em ambiente gerenciado. É essencial manter o worker ativo para que as execuções ocorram.

---

### 🔗 Deployment
Um *deployment* é o processo de empacotamento de um flow para execução futura. Ele inclui definições como nome do flow, parâmetros, agendamentos e vínculo com um work pool. É a forma oficial de disponibilizar flows para serem executados por workers.

---

### 📦 Flow
Um *flow* é a unidade principal de orquestração no Prefect, definido como uma função Python com o decorator `@flow`. Ele encapsula a lógica completa de um processo automatizado, podendo conter múltiplas tasks e lógica condicional.

---

### ⚙️ Task
Uma *task* representa uma operação individual dentro de um flow, definida com o decorator `@task`. É ideal para modularização de passos como: cálculos, transformações, chamadas de API, leitura de arquivos, entre outros.

---

### 🧩 prefect.yaml
Arquivo de configuração base do projeto Prefect. Ele define os parâmetros do flow, o nome do deployment e o work pool que será utilizado. É gerado com `prefect init` e é utilizado pelo comando `prefect deploy`.

---

### 🛠️ Work Pool
O *work pool* conecta os deployments aos workers disponíveis. Ele organiza e distribui a carga de execução dos flows, podendo ser configurado localmente ou em ambientes gerenciados na nuvem.

---

### 🖥️ Dashboard
A interface visual para monitorar e gerenciar os flows e suas execuções. Pode ser local (`http://localhost:4200`) ou via Prefect Cloud. Permite observar logs, agendar execuções, acompanhar status e histórico de execuções.

---

### ☁️ Prefect Cloud
Serviço online da Prefect que centraliza a gestão de projetos, deployments, workers e agendamentos. Ideal para equipes e ambientes colaborativos. Necessita de autenticação via API Key e possibilita visualização remota dos flows.

---

### 🔒 Secrets (GitHub Actions)
Segredos são variáveis protegidas utilizadas no GitHub Actions para armazenar informações sensíveis como `PREFECT_API_KEY`. Elas garantem segurança durante execuções automatizadas, evitando exposição de dados privados.

---

### 🔄 GitHub Actions
Ferramenta de automação de fluxos no GitHub. Permite rodar scripts automaticamente após eventos como push ou pull request. Neste laboratório, é usada para automatizar o deploy de flows para a nuvem Prefect.

---

### 🔁 CI/CD (Integração Contínua / Entrega Contínua)
Conjunto de práticas de automação onde alterações no código são testadas, integradas e implantadas continuamente. Com Prefect e GitHub Actions, é possível implantar pipelines de dados com qualidade e agilidade.

---

### 🧪 ETL (Extract, Transform, Load)
Fluxo comum em engenharia de dados: **Extrair** dados de uma fonte (ex: CSV, API), **Transformar** (ex: limpar ou agregar), e **Carregar** em um destino (ex: PostgreSQL). Prefect é ideal para orquestrar este tipo de processo.

---