
# PaperInsight 📊📄

<p align="center">
  <img src="https://github.com/vikasharma005/PaperInsight/blob/main/logo.png" width="300" alt="PaperInsight Logo">
</p>

[![GitHub license](https://img.shields.io/github/license/vikasharma005/PaperInsight.svg)](https://github.com/vikasharma005/PaperInsight/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/vikasharma005/PaperInsight.svg)](https://github.com/vikasharma005/PaperInsight/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vikasharma005/PaperInsight.svg)](https://github.com/vikasharma005/PaperInsight/network)
[![GitHub issues](https://img.shields.io/github/issues/vikasharma005/PaperInsight.svg)](https://github.com/vikasharma005/PaperInsight/issues)

> Transform your research papers into insightful dashboards with ease! 🚀

PaperInsight is a powerful web application built with Django that converts academic research papers into interactive and visually appealing dashboards. Unlock the potential of your research with just a few clicks!

## 🌟 Features

- 📤 Easy file upload for PDF, DOCX, and TXT formats
- 🔍 Advanced Natural Language Processing (NLP) for text analysis
- 📊 Dynamic visualization generation
- 📈 Word frequency and key phrase analysis
- 🖥️ User-friendly interface built with Django templates
- 🔧 Robust backend powered by Django ORM

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Django 3.2.10
- Node.js and npm (for frontend dependencies)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vikasharma005/PaperInsight.git
   cd PaperInsight
   ```

2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```bash
   cd dashboard/static/dashboard
   npm install
   ```

### Running the Application

1. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to `http://localhost:8000`

## 🖼️ Screenshots

<details>
<summary>Click to view screenshots</summary>

![Dashboard Overview](https://via.placeholder.com/800x400.png?text=Dashboard+Overview)
![Word Frequency Chart](https://via.placeholder.com/800x400.png?text=Word+Frequency+Chart)
![Key Phrases Analysis](https://via.placeholder.com/800x400.png?text=Key+Phrases+Analysis)

</details>

## 🛠️ Technologies Used

- Backend: Django, NLTK, PyPDF2, python-docx
- Frontend: HTML, CSS, JavaScript (Vue.js removed)
- Visualization: Matplotlib

## 🤝 Contributing

We welcome contributions to PaperInsight! Please check out our [Contributing Guide](CONTRIBUTING.md) for guidelines on how to proceed.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## 🙌 Acknowledgements

- [NLTK](https://www.nltk.org/) for natural language processing
- [Matplotlib](https://matplotlib.org/) for data visualization
- [Django](https://www.djangoproject.com/) for the backend framework

## 🔮 Future Enhancements

- [ ] Implement user authentication and authorization
- [ ] Add more advanced NLP techniques (e.g., topic modeling, sentiment analysis)
- [ ] Enhance frontend with interactive and customizable dashboards
- [ ] Develop a citation network visualization feature
- [ ] Integrate with academic databases for paper recommendations

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/vikasharma005">Vikas Sharma</a>
</p>

