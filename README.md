# 🚀 Helm Docker GitLab CI/CD Project

This project demonstrates a full CI/CD pipeline using **GitLab CI**, **Docker Hub**, **Helm**, and **GitLab Pages** to deploy a simple Flask app on a Kubernetes cluster.

It is designed for beginners who want to learn how CI/CD pipelines, Docker, Helm charts, and Kubernetes deployments work together.

---

## 📌 Technologies Used

| Tool            | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| Flask           | Simple Python web app framework                                         |
| Docker          | Containerizes the Flask app                                             |
| GitLab CI/CD    | Automates building, pushing, and deploying                              |
| Helm            | Packages Kubernetes manifests into installable charts                   |
| GitLab Pages    | Hosts Helm repository (index.yaml + packaged chart .tgz)                |
| Kubernetes      | Runs the containerized app using Helm                                   |

---

## 🔧 Step-by-Step Instructions

### 🔹 1. Clone the project and switch to your feature branch
```bash
git clone https://gitlab.com/<your-user>/helm-docker-gitlab.git
cd helm-docker-gitlab
git checkout -b feature_student
```

---

### 🔹 2. Setup GitLab CI/CD Variables

Go to `GitLab → Settings → CI/CD → Variables` and add:

| Variable          | Example value                     | Notes                                        |
|------------------|-----------------------------------|----------------------------------------------|
| DOCKERHUB_USERNAME | your_dockerhub_user              | Docker Hub username                          |
| DOCKERHUB_TOKEN    | **** (access token)              | From Docker Hub settings                     |
| CI_GIT_USER        | Rotem Gez                        | Name to use in git commits                   |
| CI_GIT_EMAIL       | rotem@example.com                | Email to use in git commits                  |
| CI_PUSH_USER       | your_gitlab_username             | Used for pushing version.txt                 |
| CI_PUSH_TOKEN      | **** (Personal access token)     | Requires `api` or `write_repository` scope   |

---

### 🔹 3. What the `.gitlab-ci.yml` Does

#### 🔸 Stage 1: Build Docker Image
```bash
docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
echo "$IMAGE_NAME" > version.txt
```

#### 🔸 Stage 2: Package Helm Chart
```bash
helm lint helm-docker-gitlab/
helm package helm-docker-gitlab/ --destination public/
helm repo index public/ --url "$CI_PAGES_URL"
```

#### 🔸 Stage 3: Publish Helm Chart
GitLab Pages hosts the chart at:  
`https://<your-user>.gitlab.io/helm-docker-gitlab/`

---

### 🔹 4. Verify GitLab Pages are Working

1. Go to:  
   **Project → Settings → General → Visibility**

2. Make sure:
   - Project is **Public**
   - Pages visibility is set to **Everyone**

3. Visit:  
   [https://<your-user>.gitlab.io/helm-docker-gitlab/index.yaml](#)  
   You should see a YAML list with chart metadata.

---

## 🧪 Local Deployment & Testing (Using Docker Desktop + Kubernetes)

### ✅ Pre-req: Enable Kubernetes in Docker Desktop
1. Open Docker Desktop
2. Go to **Settings → Kubernetes**
3. Check ✅ "Enable Kubernetes"
4. Wait until it's ready

---

### 🔹 5. Add Helm Repo
```bash
helm repo add studentrepo https://<your-user>.gitlab.io/helm-docker-gitlab/
helm repo update
```

---

### 🔹 6. Install the Chart
Find your latest image in `version.txt`, e.g.:
```bash
cat version.txt
# rotem343/helm-docker-gitlab:7
```

Then:
```bash
REPO="rotem343/helm-docker-gitlab"
TAG="7"

helm install student-app studentrepo/helm-docker-gitlab \
  --set image.repository="$REPO" \
  --set image.tag="$TAG"
```

---

### 🔹 7. Check that Everything is Running
```bash
kubectl get pods
kubectl get svc
```

If the service is `ClusterIP`:
```bash
kubectl port-forward svc/student-app 8080:80
```

Then open in browser:
```
http://localhost:8080/student/Rotem
```

---

### 🔹 8. Upgrade the App (New Image Version)
Update `TAG` to a new version (e.g., `8`) and run:
```bash
helm upgrade student-app studentrepo/helm-docker-gitlab \
  --set image.repository="$REPO" \
  --set image.tag="8"
```

---

### 🔹 9. Uninstall and Reset
```bash
helm uninstall student-app
```

---

## ✅ What You Should See Working

| Feature               | How to Verify                              |
|-----------------------|--------------------------------------------|
| Docker Image pushed   | Check your Docker Hub repo                 |
| Chart available       | Visit GitLab Pages: index.yaml loads       |
| App runs              | `/student/<name>` page returns in browser  |
| version.txt created   | Found in GitLab repository with tag        |

---

## 🎁 Bonus Ideas

- Add test job in CI with `pytest`
- Use semantic versioning in version.txt
- Deploy to live Kubernetes via ArgoCD

---

## 👨‍💻 Author

Rotem Gez – DevOps Student Project, 2025