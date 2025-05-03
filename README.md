# hello-docker-app

🚀 **A minimal Python app** that prints “👋 Hello from inside a Docker container!” — built to demonstrate a simple **CI/CD flow** with **GitHub → Jenkins → Docker**.

---

## 🔍 Overview

This repository contains:

- `app.py` – a one-line Python script  
- `Dockerfile` – builds a container image running `app.py`  
- `Jenkinsfile` – defines a pipeline to:
  1. **Checkout** your code  
  2. **Build** the Docker image  
  3. **Run** the container  

Use it to verify your Jenkins+Docker setup end-to-end.

---

## ⚙️ Prerequisites

- **Docker** (on your Jenkins node/VM)  
- A **GitHub** repository with this code  
- A **Jenkins** server with:
  - Docker installed & Jenkins user in the `docker` group  
  - **Git plugin** & **Pipeline plugin** enabled  
  - A **GitHub Personal Access Token** stored in Credentials as `github-token`

---

## 🏃‍♀️ Quickstart

1. **Clone** this repo:
   ```bash
   git clone https://github.com/<YOUR_GH_USERNAME>/hello-docker-app.git
   cd hello-docker-app

---

## 🔍 Overview

This repository contains:

- `.github/workflows/ci.yml` – GitHub Actions CI: lint, build & smoke-test  
- `Jenkinsfile` – Jenkins pipeline to build, tag, push & deploy your Docker image  
- `app.py` – a tiny Python HTTP server serving “👋 Hello from inside a Docker container!”  
- `Dockerfile` – builds a container running `app.py` on port 8080  
- `k8s/deployment.yaml` & `k8s/service.yaml` – Kubernetes Deployment (2 replicas) + NodePort Service  
- Helm values & commands to install **Prometheus** & **Grafana** for cluster/app monitoring  

Use it as a reference end-to-end CI/CD and observability demo. 
