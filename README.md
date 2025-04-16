# 💻 Laboratório 1 — Automação com Prefect 2.x, Python e Docker

Este repositório contém o material prático do Laboratório 1 da disciplina de Engenharia Elétrica (UFF), focado na orquestração de workflows com Prefect 2.x. O objetivo é capacitar o aluno a construir e executar pipelines de dados com integração entre Prefect, Docker, GitHub Actions e Prefect Cloud.

---

## 🎯 Objetivos do Laboratório

- Instalar e configurar o ambiente local com Python, Docker e Prefect
- Executar flows Prefect localmente e na nuvem (Prefect Cloud)
- Utilizar deploys, work pools, e workers com eficiência
- Automatizar deploys com GitHub Actions
- Monitorar execuções com o dashboard do Prefect
- Encadear tarefas e montar um pipeline ETL simples

---

## 📁 Estrutura do Projeto

```
prefect_lab/
├── flows/                 # Flows Prefect (.py)
├── infra/                 # docker-compose.yml e configs de infraestrutura
├── scripts/               # Scripts utilitários
├── .github/workflows/     # GitHub Actions workflows
├── requirements.txt       # Dependências do projeto
└── prefect.yaml           # Configuração base do Prefect
```

---

## ⚙️ Pré-requisitos

- macOS (Apple Silicon)
- Python 3.10+
- Docker Desktop
- Homebrew
- Git
- VSCode com extensões:
  - Python
  - Docker
  - GitLens
  - Remote - Containers

---

## 🚀 Etapas do Laboratório

### 1. Clonar o Projeto e Instalar Dependências

```bash
git clone https://github.com/SEU_REPO/prefect_lab.git
cd prefect_lab
pip install -r requirements.txt
```

---

### 2. Subir o Servidor Local com Docker

```bash
cd infra
docker compose up -d
docker ps
```

Acesse o dashboard local em: http://localhost:4200

---

### 3. Executar o Flow Localmente

```bash
python flows/hello_world.py
```

Verifique no dashboard se o flow foi executado com sucesso.

---

### 4. Criar e Aplicar o Deployment

```bash
prefect init
prefect work-pool create hello-pool --type process
prefect deploy -n hello-deploy
prefect worker start --pool 'hello-pool'
prefect deployment run hello-world/hello-deploy
```

---

### 5. Conectar com o Prefect Cloud

```bash
prefect cloud login -k SUA_API_KEY
prefect config view | grep PREFECT_API_URL
prefect deploy -n hello-deploy --force
```

Verifique o flow no dashboard do Prefect Cloud e execute via Quick Run.

---

### 6. GitHub Actions — CI/CD

Crie o arquivo `.github/workflows/deploy.yaml` com o workflow de deploy automatizado e configure os segredos no GitHub:

- PREFECT_API_KEY
- PREFECT_API_URL

Após isso, faça o commit e push:

```bash
git add .github/workflows/deploy.yaml
git commit -m "feat: workflow deploy"
git push origin main
```

---

## ✅ Checklist Final

- [x] Ambiente local com Docker ativo
- [x] Flow executado localmente com sucesso
- [x] Deploy no Prefect Cloud realizado
- [x] Worker vinculado ao work pool
- [x] GitHub Actions funcionando

---

## 🧪 Desafios Extras

1. Crie um flow que soma dois números.
2. Crie uma task com falha condicional e recuperação.
3. Monte um pipeline completo: leitura de CSV → transformação → gravação no PostgreSQL.

---

## 📚 Documentação do Projeto

### `flows/`
Contém os arquivos `.py` com os flows definidos com `@flow` e `@task`.

### `infra/`
Arquivos de infraestrutura, como `docker-compose.yml`, usados para levantar o servidor Prefect local.

### `.github/workflows/`
Contém workflows CI/CD do GitHub Actions usados para automatizar deploys com Prefect.

### `prefect.yaml`
Arquivo de configuração do deployment e work pool. Gerado com `prefect init` e personalizado com o nome do deployment.

---

## 🔐 Segurança

O Prefect Cloud usa autenticação por API Key. Nunca exponha sua chave diretamente no repositório. Use os GitHub Secrets para protegê-las.

---

## 🧠 Dicas Finais

- Use `docker compose down` antes de alternar para Prefect Cloud.
- Não execute flows a cada minuto no plano gratuito — pode atingir o limite de uso.
- Consulte a [documentação oficial](https://docs.prefect.io) para recursos avançados (parameters, schedules, automations).

---

## 📞 Suporte

Para dúvidas, utilize o fórum de discussões ou entre em contato com o professor responsável pelo laboratório.

---