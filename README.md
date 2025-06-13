# SurveySmart.ai

An open-source, self-hosted AI-powered feedback platform for collecting, analyzing and acting on customer & employee feedback in real time.

## Features
- **Omni-channel Capture**: Web widget, mobile SDK, Slack app, in-app microsurveys  
- **Sentiment Analysis**: Fine-grained positive/neutral/negative scoring, sarcasm detection  
- **Topic Clustering**: Automatic grouping of free-text feedback using BERT embeddings  
- **Predictive Analytics**: NPS & churn forecasting with XGBoost/LightGBM  
- **Dashboards & Alerts**: Interactive trend charts, cross-channel heatmaps, real-time email/Slack notifications  
- **Actionable Insights**: AI-generated top-3 recommendations  
- **Reporting & Export**: PDF/PPTX generation, white-labeling, full REST API  

## Getting Started

### Prerequisites
- Git  
- Docker & Docker Compose  
- Node.js (v18+) & npm  
- Python (3.11+)  

### Installation

```bash
# Clone repo
git clone https://github.com/lennarddaw/SurveySmartAI.git
cd SurveySmartAI

# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Frontend (in new shell)
cd frontend
npm install
