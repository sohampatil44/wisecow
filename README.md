# 🐮 Wisecow – Secure CI/CD Kubernetes Deployment (DevOps Assignment)

## 📌 Overview

**Wisecow** is a lightweight shell-based web application that displays humorous cow messages using `cowsay` and `fortune`.

This repository demonstrates **end-to-end DevOps implementation** including:
- Containerization
- Kubernetes deployment (Kind)
- HTTPS security using TLS
- CI/CD automation
- Runtime security and monitoring

All tasks are implemented **exactly as required by the assignment problem statement**.

---

## 🎯 Assignment Objectives & Exact Implementation

### 1️⃣ Containerize the Application

**Objective:** Package the application so it runs consistently across environments.

**Implementation:**
- `Dockerfile` builds the Wisecow image
- Installs required binaries (`cowsay`, `fortune`, `netcat`)
- Runs the `wisecow.sh` script inside the container

📁 Files involved:
- `Dockerfile`
- `wisecow.sh`

✅ **Objective satisfied**

---

### 2️⃣ Deploy Application using Kubernetes

**Objective:** Deploy the containerized app on Kubernetes.

**Implementation:**
- Kubernetes manifests are stored in `k8s/manifests/`
- A **Deployment** ensures pod availability
- A **NodePort Service** exposes the application
- All resources run inside a dedicated namespace

📁 Files involved:
- `k8s/manifests/deployment.yaml`
- `k8s/manifests/service.yaml`

✅ **Objective satisfied**

---

### 3️⃣ Secure the Application using TLS (HTTPS)

**Objective:** Secure application access using TLS certificates.

**Implementation:**
- Self-signed certificate generated:
  - `wisecow.crt`
  - `wisecow.key`
- TLS stored as Kubernetes Secret
- Ingress configured for HTTPS access

📁 Files involved:
- `wisecow.crt`
- `wisecow.key`
- `k8s/manifests/ingress.yaml`

⚠️ Browser warnings are expected due to self-signed certificates.

✅ **Objective satisfied**

---

### 4️⃣ Implement CI/CD using GitHub Actions

**Objective:** Automate build and deployment pipeline.

**Implementation:**
- GitHub Actions workflow triggers on:
  - Push to `main`
  - Manual trigger
- Pipeline performs:
  1. Docker image build
  2. Push to Docker Hub
  3. Create Kind cluster
  4. Deploy Kubernetes manifests
  5. Validate deployment readiness
  6. Test service inside cluster

📁 Files involved:
- `.github/workflows/cicd.yaml`
- `kind-config.yaml`

✅ **Objective satisfied**

---

### 5️⃣ Enable Local & Multi-Environment Deployment

**Objective:** Support multiple deployment methods.

**Implementation:**
- Docker Compose for local testing
- Kubernetes YAML for cluster deployment

📁 Files involved:
- `compose.yaml`
- `deploy.yaml`

✅ **Objective satisfied**

---

### 6️⃣ Runtime Security using Kubearmor (Zero Trust)

**Objective:** Enforce runtime security policies.

**Implementation:**
- Kubearmor policy enforces Zero Trust runtime rules
- Blocks unauthorized process execution
- Violations captured and verified

📁 Files involved:
- `kubearmor/wisecow-zero-trust.yaml`
- `kubearmor/violation_ss.png`

✅ **Objective satisfied**

---

### 7️⃣ Application & System Health Monitoring

**Objective:** Monitor application and system health.

**Implementation:**
- Python scripts monitor:
  - Application availability
  - System resource usage
- Logs generated for audit and validation

📁 Files involved:
- `scripts/app_health_check.py`
- `scripts/system_health_monitor.py`
- `scripts/*.log`

✅ **Objective satisfied**

---

## 🧱 Repository Structure

```text
.
├── Dockerfile
├── compose.yaml
├── deploy.yaml
├── kind-config.yaml
├── wisecow.sh
├── wisecow.crt
├── wisecow.key
├── k8s/
│   └── manifests/
├── kubearmor/
│   ├── wisecow-zero-trust.yaml
│   └── violation_ss.png
├── scripts/
│   ├── app_health_check.py
│   └── system_health_monitor.py
└── .github/workflows/cicd.yaml
