# Python Web App Deployment on AWS ECS 🚀

This repository contains the code and configuration for a scalable Python web application containerized with Docker and deployed to Amazon Elastic Container Service (ECS) using AWS Fargate.

## 🎯 Objective
To build, containerize, and deploy a Flask web application in a production-ready environment using Docker, AWS ECR, and AWS ECS.

## ⚙️ Tech Stack
* **Language:** Python 3.9
* **Framework:** Flask
* **Containerization:** Docker
* **Cloud Provider:** Amazon Web Services (AWS)
* **Services Used:** Amazon ECR (Elastic Container Registry), Amazon ECS (Fargate)

## 📂 Project Structure
\`\`\`text
.
├── app.py               # Main Flask application
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── images/              # Deployment screenshots
\`\`\`

## 📸 Deployment Proof

### 1. Local Container Testing
*(Proof that the container builds and runs locally on port 5000)*
![Local Test](images/local-container.png)

### 2. AWS ECR Repository
*(Proof that the Docker image was successfully pushed to Elastic Container Registry)*
![ECR Repo](images/ecr-repo.png)

### 3. AWS ECS Service Running
*(Proof that the Fargate service is active and managing the task)*
![ECS Service](images/ecs-service.png)

### 4. Live Browser Access
*(Proof that the application is publicly accessible via the ECS Public IP)*
![Browser Output](images/browser-output.png)

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