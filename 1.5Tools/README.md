# 🛠️ Data Analytics & Engineering Bootcamp - Required Tools & Setup Guide

## 📋 Overview

This comprehensive guide covers all tools and platforms required for the Data Analytics & Engineering Bootcamp. Follow the installation steps carefully to ensure your environment is ready for Day 1.

---

## ✅ Installation Checklist

Use this checklist to track your setup progress:

- [ ] GitHub Account & Git
- [ ] Kaggle Account
- [ ] Visual Studio Code
- [ ] Python 3.x
- [ ] SQL Server Management Studio (SSMS)
- [ ] Databricks Account
- [ ] Snowflake Account
- [ ] Canva Account
- [ ] Google Colab Access
- [ ] Google BigQuery Access
- [ ] Miro Account
- [ ] Figma Account
- [ ] Looker Studio Access
- [ ] Azure DevOps Account

---

## 1️⃣ GitHub & Git

### Purpose
Version control, code collaboration, and portfolio building.

### Setup Instructions

#### Create GitHub Account
1. Visit [github.com](https://github.com)
2. Click "Sign up"
3. Use your professional email
4. Choose a professional username (e.g., firstname-lastname)
5. Verify your email address

#### Install Git
**Windows:**
```bash
# Download from: https://git-scm.com/download/win
# Run the installer
# Use default settings (recommended)
```

**Mac:**
```bash
# Install via Homebrew
brew install git

# Or download from: https://git-scm.com/download/mac
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git
```

#### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

#### Set Up SSH Key (Recommended)
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key
ssh-add ~/.ssh/id_ed25519

# Copy public key (then add to GitHub)
cat ~/.ssh/id_ed25519.pub
```

**Cost:** Free  
**Required For:** All weeks

---

## 2️⃣ Kaggle

### Purpose
Datasets, competitions, notebooks, and community learning.

### Setup Instructions
1. Visit [kaggle.com](https://www.kaggle.com)
2. Click "Register"
3. Sign up with Google/GitHub (recommended) or email
4. Complete your profile
5. Verify your phone number (required for competitions)
6. Enable two-factor authentication (recommended)

#### Get Kaggle API Key
1. Go to Account settings
2. Scroll to "API" section
3. Click "Create New API Token"
4. Download `kaggle.json`
5. Place in `~/.kaggle/` directory

```bash
# Linux/Mac
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Windows
mkdir %USERPROFILE%\.kaggle
move Downloads\kaggle.json %USERPROFILE%\.kaggle\
```

#### Install Kaggle Python Package
```bash
pip install kaggle
```

**Cost:** Free  
**Required For:** Weeks 1-6, 9-12

---

## 3️⃣ Visual Studio Code

### Purpose
Primary code editor for Python, SQL, and data projects.

### Setup Instructions
1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Run installer for your OS
3. Launch VS Code

#### Essential Extensions
Install these extensions (Ctrl+Shift+X):

**Core Extensions:**
```
- Python (Microsoft)
- Jupyter (Microsoft)
- Pylance (Microsoft)
- SQL Server (mssql)
- SQLTools
- GitLens — Git supercharged
- GitHub Pull Requests and Issues
- Prettier - Code formatter
- Live Server
- Markdown All in One
- Rainbow CSV
- Excel Viewer
- Data Wrangler (Microsoft)
```

**Install via Command Palette:**
```bash
# Open Command Palette (Ctrl+Shift+P)
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-mssql.mssql
code --install-extension GitHub.vscode-pull-request-github
```

#### Recommended Settings
```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.wordWrap": "on",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "files.autoSave": "afterDelay",
  "terminal.integrated.fontSize": 13
}
```

**Cost:** Free  
**Required For:** All weeks

---

## 4️⃣ Python

### Purpose
Primary programming language for data analysis and engineering.

### Setup Instructions

#### Download & Install
**Windows:**
1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11+ (latest stable version)
3. Run installer
4. ✅ **IMPORTANT:** Check "Add Python to PATH"
5. Click "Install Now"

**Mac:**
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Verify installation
python3 --version
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3-pip python3-venv

# Fedora
sudo dnf install python3.11
```

#### Verify Installation
```bash
python --version
# or
python3 --version

pip --version
# or
pip3 --version
```

#### Essential Python Packages
```bash
# Update pip first
python -m pip install --upgrade pip

# Core data science packages
pip install pandas numpy matplotlib seaborn scipy

# Machine learning
pip install scikit-learn xgboost lightgbm

# Database connectors
pip install sqlalchemy pymysql psycopg2-binary pyodbc

# Jupyter
pip install jupyter jupyterlab notebook

# Data visualization
pip install plotly dash bokeh

# Excel & file handling
pip install openpyxl xlrd xlsxwriter

# API & web scraping
pip install requests beautifulsoup4 selenium

# Cloud SDKs
pip install google-cloud-bigquery snowflake-connector-python azure-storage-blob

# Development tools
pip install pylint black autopep8 pytest

# Kaggle
pip install kaggle
```

#### Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv bootcamp_env

# Activate (Windows)
bootcamp_env\Scripts\activate

# Activate (Mac/Linux)
source bootcamp_env/bin/activate

# Install packages in virtual environment
pip install -r requirements.txt
```

**Cost:** Free  
**Required For:** All weeks

---

## 5️⃣ SQL Server Management Studio (SSMS)

### Purpose
Database management and SQL query development for SQL Server.

### Setup Instructions

#### Download & Install
1. Visit [Microsoft SSMS Download](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
2. Download latest version (SSMS 19+)
3. Run installer (requires 500MB+ space)
4. Complete installation (may take 10-15 minutes)
5. Restart computer if prompted

#### Optional: Install SQL Server Express (Local Database)
1. Download [SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
2. Choose "Basic" installation
3. Accept license terms
4. Install to default location
5. Note the connection string provided

#### First Connection
1. Open SSMS
2. Server name: `localhost` or `.\SQLEXPRESS`
3. Authentication: Windows Authentication
4. Click "Connect"

**Cost:** Free  
**Required For:** Weeks 1-4, 9-12  
**Platform:** Windows only (Mac users: use Azure Data Studio or Docker)

---

## 6️⃣ Databricks

### Purpose
Big data processing, collaborative notebooks, and Spark development.

### Setup Instructions

#### Community Edition (Free)
1. Visit [community.cloud.databricks.com](https://community.cloud.databricks.com)
2. Click "Sign up for Community Edition"
3. Enter your email
4. Verify email address
5. Complete profile setup
6. Create your first cluster

#### Account Configuration
- Create a cluster (select smallest size)
- Import sample notebooks
- Connect to data sources
- Enable GitHub integration

#### Install Databricks CLI (Optional)
```bash
pip install databricks-cli

# Configure CLI
databricks configure --token
```

**Cost:** Free (Community Edition)  
**Limitations:** Limited compute, no production features  
**Required For:** Weeks 5-8

---

## 7️⃣ Snowflake

### Purpose
Cloud data warehouse, SQL development, and data sharing.

### Setup Instructions

#### Free Trial Account
1. Visit [signup.snowflake.com](https://signup.snowflake.com)
2. Choose "Standard" edition
3. Select cloud provider (AWS recommended)
4. Choose region closest to you
5. Enter business email
6. Complete registration
7. Check email for activation link

#### Initial Setup
1. Log into Snowflake web UI
2. Create a database:
   ```sql
   CREATE DATABASE BOOTCAMP_DB;
   CREATE SCHEMA BOOTCAMP_DB.ANALYTICS;
   ```
3. Load sample data from Snowflake Marketplace
4. Create virtual warehouse

#### Install SnowSQL (Command Line)
```bash
# Download from: https://docs.snowflake.com/en/user-guide/snowsql-install-config.html

# Configure connection
snowsql -a <account_name> -u <username>
```

#### Python Connector
```bash
pip install snowflake-connector-python
pip install snowflake-sqlalchemy
```

**Cost:** Free trial (30 days, $400 credit)  
**After Trial:** Pay-as-you-go or pause account  
**Required For:** Weeks 5-8, 11-12

---

## 8️⃣ Canva

### Purpose
Data visualization, presentation design, and infographics.

### Setup Instructions
1. Visit [canva.com](https://www.canva.com)
2. Click "Sign up"
3. Sign up with Google (recommended) or email
4. Choose "Education" if student
5. Explore templates

#### For Students
1. Visit [canva.com/education](https://www.canva.com/education/)
2. Verify student status with school email
3. Get Canva Pro for free

**Cost:** Free (basic), Canva Pro available for students  
**Required For:** Presentations throughout bootcamp

---

## 9️⃣ Google Colab

### Purpose
Cloud-based Jupyter notebooks with free GPU/TPU access.

### Setup Instructions
1. Requires Google account
2. Visit [colab.research.google.com](https://colab.research.google.com)
3. Sign in with Google account
4. No installation needed!

#### Enable GPU (Optional)
1. Runtime → Change runtime type
2. Hardware accelerator → GPU or TPU
3. Save

#### Connect to Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')
```

#### Install Additional Packages
```python
!pip install package_name
```

**Cost:** Free (with usage limits)  
**Colab Pro:** $9.99/month (more compute, longer sessions)  
**Required For:** Weeks 1-12 (Python exercises)

---

## 🔟 Google BigQuery

### Purpose
Serverless data warehouse, large-scale SQL analytics.

### Setup Instructions

#### Enable BigQuery
1. Visit [console.cloud.google.com](https://console.cloud.google.com)
2. Create Google Cloud account (requires credit card for verification)
3. Get $300 free credit (new users)
4. Create a new project
5. Enable BigQuery API
6. Go to [BigQuery Console](https://console.cloud.google.com/bigquery)

#### Explore Public Datasets
1. Click "Add Data" → "Explore public datasets"
2. Search for datasets (e.g., "COVID-19", "Stack Overflow")
3. Add to your project

#### Install BigQuery Client
```bash
pip install google-cloud-bigquery
pip install db-dtypes
```

#### Free Tier Limits
- 1 TB of queries per month
- 10 GB storage
- Perfect for learning

**Cost:** Free tier available  
**Required For:** Weeks 6-8, 10-12

---

## 1️⃣1️⃣ Miro

### Purpose
Collaborative whiteboarding, brainstorming, and project planning.

### Setup Instructions
1. Visit [miro.com](https://miro.com)
2. Click "Sign up free"
3. Use Google sign-in (recommended)
4. Choose "Education" or "Personal"
5. Complete onboarding

#### Free Plan Features
- 3 editable boards
- Unlimited team members
- Basic templates

#### For Students/Educators
1. Visit [miro.com/education](https://miro.com/education/)
2. Verify with school email
3. Get free upgrade

**Cost:** Free (limited boards)  
**Required For:** Project planning sessions

---

## 1️⃣2️⃣ Figma

### Purpose
UI/UX design, dashboard mockups, and collaborative design.

### Setup Instructions
1. Visit [figma.com](https://www.figma.com)
2. Click "Sign up"
3. Use Google sign-in (recommended)
4. Choose "Personal" account type
5. Download desktop app (optional)

#### Install Desktop App
- [Download Figma Desktop](https://www.figma.com/downloads/)
- Available for Windows, Mac, Linux

#### Education Plan
1. Visit [figma.com/education](https://www.figma.com/education/)
2. Apply with school email
3. Get Figma Professional for free

**Cost:** Free (3 files, unlimited personal files)  
**Education:** Free Professional plan  
**Required For:** Dashboard design, presentations

---

## 1️⃣3️⃣ Looker Studio (formerly Google Data Studio)

### Purpose
Business intelligence, interactive dashboards, and reporting.

### Setup Instructions
1. Visit [lookerstudio.google.com](https://lookerstudio.google.com)
2. Sign in with Google account
3. No setup required - it's web-based!

#### Create First Report
1. Click "Create" → "Report"
2. Connect data source
3. Choose from 800+ connectors

#### Connect Common Sources
- Google Sheets
- BigQuery
- Google Analytics
- MySQL
- PostgreSQL

**Cost:** Free  
**Required For:** Weeks 10-12 (Visualization projects)

---

## 1️⃣4️⃣ Azure DevOps

### Purpose
CI/CD pipelines, project management, and Azure integration.

### Setup Instructions

#### Create Azure DevOps Account
1. Visit [dev.azure.com](https://dev.azure.com)
2. Click "Start free"
3. Sign in with Microsoft account (or create one)
4. Create organization name
5. Create first project

#### Student Benefits
1. Visit [azure.microsoft.com/en-us/free/students](https://azure.microsoft.com/en-us/free/students/)
2. Verify student status
3. Get $100 Azure credit
4. Free Azure DevOps features

#### Install Azure CLI (Optional)
```bash
# Windows
winget install Microsoft.AzureCLI

# Mac
brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

#### Connect to GitHub
1. Go to Project Settings
2. GitHub connections
3. Authorize Azure Pipelines

**Cost:** Free (up to 5 users)  
**Students:** Additional free credits  
**Required For:** Weeks 11-12 (CI/CD)

---

## 📦 Package Manager Tools

### Homebrew (Mac/Linux)
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Chocolatey (Windows)
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

---

## 🔧 Optional But Recommended Tools

### Docker Desktop
**Purpose:** Containerization, consistent environments
- Download: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
- Cost: Free for education
- Required For: Advanced topics

### Postman
**Purpose:** API testing and development
- Download: [postman.com/downloads](https://www.postman.com/downloads/)
- Cost: Free
- Required For: API projects

### DBeaver
**Purpose:** Universal database tool
- Download: [dbeaver.io/download](https://dbeaver.io/download/)
- Cost: Free (Community Edition)
- Alternative to SSMS for Mac/Linux

### Tableau Public
**Purpose:** Data visualization
- Download: [public.tableau.com](https://public.tableau.com)
- Cost: Free
- Optional: Supplement to other tools

---

## 💾 System Requirements

### Minimum Specifications:
- **OS:** Windows 10/11, macOS 10.15+, or Linux
- **RAM:** 8GB (16GB recommended)
- **Storage:** 50GB free space
- **Internet:** Stable broadband connection
- **Browser:** Chrome, Firefox, or Edge (latest version)

### Recommended Specifications:
- **RAM:** 16GB+
- **Storage:** 100GB+ SSD
- **Processor:** Intel i5/AMD Ryzen 5 or better
- **Graphics:** Dedicated GPU (helpful for data viz)

---

## 📝 Pre-Bootcamp Checklist

### Week Before Start:
- [ ] All accounts created
- [ ] All software installed
- [ ] Test each tool (open and verify it works)
- [ ] Join bootcamp Slack/Discord
- [ ] Set up your workspace
- [ ] Create bootcamp folder structure:
  ```
  bootcamp/
  ├── week-01/
  ├── week-02/
  ├── ...
  ├── projects/
  ├── datasets/
  └── notes/
  ```

### Day 1 Ready Check:
- [ ] Can you open VS Code?
- [ ] Can you run Python in terminal?
- [ ] Can you connect to SSMS?
- [ ] Can you access all cloud platforms?
- [ ] Is your GitHub profile set up?
- [ ] Do you have a note-taking system?

---

## 🆘 Troubleshooting

### Common Issues:

**Python not recognized:**
```bash
# Add Python to PATH (Windows)
# Control Panel → System → Advanced → Environment Variables
# Add Python installation directory to PATH
```

**Git command not found:**
```bash
# Restart terminal after installation
# Or add Git to PATH manually
```

**SSMS won't connect:**
- Check SQL Server service is running
- Try `localhost` instead of server name
- Use Windows Authentication

**VS Code extensions not loading:**
- Restart VS Code
- Check internet connection
- Disable firewall temporarily

**Cloud platform access issues:**
- Clear browser cache
- Try incognito/private mode
- Check email for verification links

---

## 📞 Support Resources

### During Bootcamp:
- **Instructor Support:** Available during class hours
- **TA Support:** Office hours schedule TBD
- **Peer Support:** Class Slack/Discord channel
- **Documentation:** Links provided for each tool

### External Resources:
- Stack Overflow
- GitHub Discussions
- Tool-specific forums
- YouTube tutorials
- Official documentation

---

## 💰 Cost Summary

| Tool | Cost | Notes |
|------|------|-------|
| GitHub | Free | Pro plan optional |
| Kaggle | Free | Phone verification required |
| VS Code | Free | Open source |
| Python | Free | Open source |
| SSMS | Free | Windows only |
| Databricks | Free | Community edition |
| Snowflake | Free | 30-day trial |
| Canva | Free | Pro free for students |
| Google Colab | Free | Pro optional |
| BigQuery | Free | Free tier |
| Miro | Free | 3 boards |
| Figma | Free | Unlimited for students |
| Looker Studio | Free | Fully featured |
| Azure DevOps | Free | 5 users |

**Total Cost:** $0 (with student accounts and free tiers)

---

## 🎓 Ready to Start!

Once you've completed this setup:
1. ✅ Test each tool
2. 📧 Email confirmation to instructor
3. 💬 Introduce yourself in class channel
4. 📚 Review Week 1 materials
5. 🚀 Get excited for the bootcamp!

---

## 📄 License

This setup guide is provided as-is for educational purposes.

---

**Last Updated:** October 2025  
**Version:** 1.0  
**Maintained By:** Bootcamp Instruction Team

---

## 🤝 Need Help?

If you encounter any issues during setup:
1. Check the troubleshooting section
2. Search the issue online
3. Ask in the class channel
4. Email instructor with:
   - Tool name
   - Error message
   - What you've tried
   - Screenshots if relevant

**We're here to help! No question is too small. 💪**