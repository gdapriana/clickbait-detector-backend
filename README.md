# Clickbait Detector Backend

## 🌟 Project Overview

Clickbait Detector is an intelligent backend application designed to identify and classify clickbait headlines using advanced machine learning techniques. This project aims to help users distinguish between genuine and sensationalist news headlines.

## 🚀 Technologies Used

- **Programming Language**: Python
- **Machine Learning Frameworks**:
    - TensorFlow
    - Scikit-learn
- **Data Processing**:
    - NLTK
    - Pandas
    - NumPy
- **Web Framework**: Flask

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/dataset` | GET | Retrieve information about the dataset |
| `/model` | GET | Get details about the machine learning model |
| `/member` | GET | View information about the team |
| `/tech` | GET | Learn about technologies used |
| `/predict` | POST | Predict clickbait probability |

### Prediction Endpoint Example
```json
POST /predict
Request Body:
{
  "text": "Your headline text to be analyzed"
}
```

## 🌐 Base URL
```
https://living-madella-gedeapriana-2f6e9d4d.koyeb.app/
```

## 🤝 Frontend Repository
Check out the frontend application:
[Clickbait Detector Frontend](https://github.com/gdapriana/clickbait-detector-frontend)

## 📦 Installation

### Prerequisites
- Python 3.10+
- pip

### Steps
1. Clone the repository
```bash
git clone <repository-url>
cd clickbait-detector-backend
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

## 🤖 How It Works
The Clickbait Detector uses machine learning models trained on a comprehensive dataset to analyze news headlines. It applies natural language processing techniques to determine the likelihood of a headline being clickbait.

## 🛡️ Contributing
Interested in contributing? Great!
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Team
For more information about the team, visit the `/member` endpoint of the API.

## 🔍 Support
For any questions or issues, please open an issue in the GitHub repository.
