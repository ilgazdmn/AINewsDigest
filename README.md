# 📰 AINewsDigest

An automated AI-powered news digest tool that fetches the latest news articles on a chosen topic, summarizes them using **Google Gemini** (via LangChain), and delivers the analysis directly to your inbox via **Gmail SMTP**.

---

## 🚀 Features

- 📡 **Real-time News Fetching** — Retrieves latest articles from [NewsAPI](https://newsapi.org/) filtered by topic and date
- 🤖 **AI-Powered Summarization** — Uses Google Gemini (`gemini-2.0-flash`) via LangChain to analyze articles and assess stock market impact
- 📧 **Automated Email Delivery** — Sends the digest to your inbox via Gmail SMTP with SSL
- 🔐 **Secure Config** — All credentials managed via `.env` file using `python-dotenv`

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| News Source | [NewsAPI](https://newsapi.org/) |
| AI Model | Google Gemini via LangChain |
| Email Delivery | Gmail SMTP (SSL, port 465) |
| Config Management | `python-dotenv` |

---

## 📁 Project Structure

```
AINewsDigest/
├── main.py           # Entry point: fetches news, calls AI, sends email
├── send_email.py     # Gmail SMTP email sender
├── simple_ai.py      # Standalone LangChain/Gemini test script
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (NOT committed to git)
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ilgazdmn/AINewsDigest.git
   cd AINewsDigest
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create your `.env` file** (see [Configuration](#configuration) below)

---

## 🔑 Configuration

Create a `.env` file in the root directory with the following variables:

```env
NEWS_API_KEY=your_newsapi_key_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
GOOGLE_APP_PASSWORD=your_gmail_app_password_here
EMAIL_SENDER=your_email@gmail.com
EMAIL_RECEIVER=recipient@example.com
```

> ⚠️ **Never commit your `.env` file to Git.** Add it to `.gitignore`.

### How to get the credentials:
- **NewsAPI key** → Register at [newsapi.org](https://newsapi.org/register)
- **Google Gemini API key** → Get one from [Google AI Studio](https://aistudio.google.com/app/apikey)
- **Gmail App Password** → Enable 2FA on your Google account, then generate an App Password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

## ▶️ Usage

1. Set your desired news topic in `main.py`:
   ```python
   topic = 'artificial intelligence'  # Change to any topic
   ```

2. Run the script:
   ```bash
   python main.py
   ```

The script will:
1. Fetch the latest English news articles about the topic
2. Send them to Gemini for AI analysis and stock impact assessment
3. Email the digest to your configured receiver

---

## 🔒 Security Notice

> ⚠️ **Important:** The file `simple_ai.py` contains a hardcoded API key. This is a security risk — the key is publicly exposed in your repository history.
>
> **Act immediately:**
> 1. Revoke the exposed key at [Google AI Studio](https://aistudio.google.com/app/apikey)
> 2. Replace all hardcoded keys with environment variables:
>    ```python
>    import os
>    from dotenv import load_dotenv
>    load_dotenv()
>    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
>    ```
> 3. Add `.env` to your `.gitignore`

---

## 📌 Roadmap

- [ ] Configurable topic via CLI argument or config file
- [ ] Scheduling with `APScheduler` or cron for daily digests
- [ ] Multi-topic support with categorized email sections
- [ ] Telegram bot delivery option
- [ ] Web dashboard for digest history
- [ ] Docker containerization

---

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss changes before submitting a pull request.

1. Fork the repository
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request



## 👤 Author

**ilgazdmn**  
[GitHub Profile](https://github.com/ilgazdmn)
