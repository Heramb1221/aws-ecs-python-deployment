# Python Web App Deployment on AWS ECS 🚀

This repository contains the code and configuration for a scalable Python web application containerized with Docker and deployed to Amazon Elastic Container Service (ECS) using AWS Fargate.

---

## Scenario & Problem Statement
As a DevOps Engineer in a startup, the core objective is to move a local Python development environment into a scalable cloud infrastructure. This project demonstrates how to containerize an application using Docker, manage images via Amazon ECR, and orchestrate serverless containers using Amazon ECS (Fargate).

🎯 Core Objectives
Containerization: Package a Flask web server using Docker.

Registry Management: Store production-ready container images securely in Amazon Elastic Container Registry (ECR).

Cloud Deployment: Deploy and expose the containerized app publicly using Amazon ECS with a serverless Fargate launch type.

📦 Application & Technical Requirements
1. Application Specifications
Built using Flask running on port 5000.

Endpoints:

/ → Returns "Hello from ECS 🚀"

/health → Returns {"status": "App is healthy"}

2. Infrastructure Requirements
Multi-stage or lightweight base Docker image (python:3.9-slim).

Bound to 0.0.0.0 inside the container to handle AWS network mapping.

Exposed publicly on AWS via a dedicated Security Group allowing inbound traffic on port 5000.

⚙️ Tech Stack
Language: Python 3.9

Framework: Flask

Containerization: Docker

Cloud Provider: Amazon Web Services (AWS)

AWS Services: Amazon ECR, Amazon ECS (Fargate Compute)

📂 Project Structure
Plaintext
.
├── app.py                # Main Flask application with custom endpoints
├── Dockerfile            # Multi-layer Docker configuration file
├── requirements.txt      # Bound Python application dependencies
├── README.md             # Project documentation and architectural overview
└── images/               # Production deployment verification assets
📸 Deployment Proof (Deliverables)
1. Local Container Testing
Verification that the container builds perfectly and processes requests locally on port 5000.

2. AWS ECR Repository
Verification that the final built image is successfully pushed with the latest tag inside the private registry.

3. AWS ECS Service Running
Verification of an active, stable Fargate task under the managed cluster service layer.

4. Live Browser Access
Verification that the public-facing endpoint resolves globally via the Fargate task's allocated public IP address.
---

## ⚙️ Tech Stack
* **Language:** Python 3.9
* **Framework:** Flask
* **Containerization:** Docker
* **Cloud Provider:** Amazon Web Services (AWS)
* **Services Used:** Amazon ECR (Elastic Container Registry), Amazon ECS (Fargate)

---

## 📂 Project Structure
\`\`\`text
.
├── app.py               # Main Flask application
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── images/              # Deployment screenshots
\`\`\`

---

## 📸 Deployment Proof

### 1. Local Container Testing
<img width="1917" height="970" alt="Local Test" src="https://github.com/user-attachments/assets/6585819c-6fa9-495e-bb07-6e82cac25389" />

### 2. AWS ECR Repository
<img width="1917" height="867" alt="ECR Repo" src="https://github.com/user-attachments/assets/fc0738d8-ffb1-4ed5-86bb-f6dafb7ab09f" />

### 3. AWS ECS Service Running
<img width="1917" height="862" alt="ECS Service" src="https://github.com/user-attachments/assets/e32d0568-ad8e-4a8d-9bdf-4716d8b11ff8" />

### 4. Live Browser Access
<img width="1917" height="971" alt="Browser Output" src="https://github.com/user-attachments/assets/eace7fd6-cc8a-4bb2-a6c5-2534ee82af43" />

---

## 🚀 How to Run Locally

1. Clone the repository:
   \`\`\`bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   \`\`\`
2. Build the Docker image:
   \`\`\`bash
   docker build -t flask-ecs-app .
   \`\`\`
3. Run the container:
   \`\`\`bash
   docker run -p 5000:5000 flask-ecs-app
   \`\`\`
4. Access the app in your browser at \`http://localhost:5000\`.
