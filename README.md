# 🚀 Hello Docker App — CI/CD + DevOps Automation Project

This project demonstrates a complete CI/CD pipeline with Docker, GitHub Actions, Ansible automation, and monitoring using Prometheus + Grafana — deployed and tested on a GCP VM.

---

## 🧩 Tech Stack

- **Python**: Backend app with test coverage
- **Docker**: Containerized the app
- **GitHub Actions**: CI/CD pipeline for testing, building, and optionally pushing Docker image
- **Ansible**: Infrastructure setup (Docker, Jenkins, Minikube, Helm, kubectl)
- **Prometheus + Grafana**: Node monitoring
- **Google Cloud Platform (GCP)**: Hosting VM (Ubuntu)

---

## 🔧 Features & Setup

### 🐳 Docker

- Created `Dockerfile` for Python HTTP server app
- Built & tested locally and via GitHub Actions
- Smoke test using `curl`

### ⚙️ GitHub Actions CI Workflow

- Linting with `flake8`
- Testing & coverage with `pytest` + `pytest-cov`
- Uploads reports to **Codecov**
- Docker image build + local smoke test
- DockerHub push step added (currently skipped due to login issue)

### 🛠 Ansible Playbook

- Automated setup of DevOps toolchain on GCP instance:
  - Docker
  - Jenkins
  - Minikube
  - kubectl
  - Helm

- Logs stored in `/logs` directory for execution trace

### 📈 Monitoring with Prometheus + Grafana

- Node Exporter metrics visualized via Grafana dashboards
- Accessed locally through secure SSH tunnel

---

## 🗂️ Project Structure

```

.
├── app/                      # Python application
├── k8s/                      # Kubernetes YAML files for Jenkins setup
├── logs/                     # Ansible playbook execution logs
├── Dockerfile
├── Jenkinsfile               # Pipeline definition (optional)
├── devops-setup-playbook.yml
├── hosts.ini                 # Ansible inventory
├── requirements.txt
└── .github/workflows/ci.yml # GitHub Actions pipeline

````

---

## ✅ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/khushii007/hello-docker-app.git
cd hello-docker-app
````

### 2. Run the Ansible playbook

```bash
ansible-playbook -i hosts.ini devops-setup-playbook.yml
```

### 3. Verify installations on your GCP instance

* Docker, Jenkins, Minikube, Helm, kubectl
* Grafana and Prometheus are active and dashboard is accessible

---

## 📌 Status

✅ Core app setup
✅ Docker build + test
✅ CI pipeline functional
✅ Monitoring live
⏭️ DockerHub push (optional, currently skipped)

---

## 👩🏻‍💻 Author

**Khushi Israni**
DevOps | Cloud | Python
MIT Manipal · Intern @ Mphasis

---

## 📸 Screenshots

Setup and execution screenshots were captured at each stage and can be attached separately for documentation/demo purposes.
