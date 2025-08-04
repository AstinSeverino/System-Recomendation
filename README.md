# 🎵 Song Recommendation System with MLOps 🚀

> “Turning musical tastes into data-driven recommendations!”  

---

## 👋 Project Overview

Welcome to **Recomendación de Canciones**, a fully MLOps-powered content-based song recommendation system built on Spotify data. This project demonstrates how to:

1. **Ingest & prepare** raw Spotify data  
2. **Engineer features** and build a content-based recommendation model  
3. **Track experiments** and optimize hyperparameters  
4. **Orchestrate** end-to-end pipelines  
5. **Containerize & deploy** with Docker and AWS  
6. **Serve** recommendations via a FastAPI REST API  
7. **Monitor** production performance with Grafana  
8. **Automate** testing and deployment with GitHub Actions  

---

## 🧰 Technologies & Tools

| Layer               | Tool / Framework             |  
|---------------------|------------------------------|  
| **Data & Modeling** | Python, Pandas, Scikit-learn |  
| **Experimentation** | MLflow, Optuna               |  
| **Orchestration**   | Apache Airflow               |  
| **Containerization**| Docker                       |  
| **Deployment**      | AWS (EC2 / EKS / Lambda)     |  
| **API**             | FastAPI, Uvicorn             |  
| **Monitoring**      | Grafana, Prometheus          |  
| **Version Control** | Git, GitHub                  |  
| **CI/CD**           | GitHub Actions               |  

---

## 📦 Data Pipeline

1. **Download dataset** from [Kaggle: Spotify Songs Dataset].  
2. **Extract & Clean**  
   - Remove duplicates  
   - Fill missing values  
3. **Feature Engineering**  
   - Compute audio-feature vectors  
   - Normalize & standardize  
4. **Model Training & Tuning**  
   - Content-based similarity (TF-IDF & cosine)  
   - Hyperparameter search with Optuna  
   - Log metrics, params & artifacts in MLflow  
5. **Airflow DAG**  
   - `data_ingest` → `feature_engineering` → `train_model` → `deploy_artifact`  
6. **Docker Build & Push**  
   - `docker build -t song-recommender:latest .`  
   - Push to Docker Hub or AWS ECR  
7. **API Service**  
   - FastAPI app exposes `/recommend?song_id=…` endpoint  
8. **Monitoring**  
   - Grafana dashboard visualizes request latency, model drift, error rates  

---

## 🔧 Installation & Setup

1. **Clone repo**  
   ```bash
   git clone https://github.com/YourUser/song-recommendation-mlops.git
   cd song-recommendation-mlops
