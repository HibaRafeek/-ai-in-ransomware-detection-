# 🛡️ Ransomware Detection Web App

A simple machine learning web application that detects ransomware behavior based on system activity patterns.

## 🚀 Quick Start

### Option 1: Automatic Installation (EASIEST)
1. Double-click **`install.bat`**
2. Wait for installation to complete
3. Run: `python app.py`
4. Open browser: **http://127.0.0.1:5000/**

### Option 2: Manual Installation
See **`INSTALLATION_GUIDE.md`** for detailed step-by-step instructions.

## 📋 Requirements

- Python 3.8 or higher
- Flask (web framework)
- Pandas (data processing)
- Scikit-learn (machine learning)
- NumPy (mathematical operations)

## 📁 Project Files

- `app.py` - Main web application
- `ransomware.csv` - Training dataset
- `requirements.txt` - Python dependencies
- `install.bat` - Automatic installation script
- `INSTALLATION_GUIDE.md` - Detailed installation guide

## 🎯 How It Works

1. The app trains a machine learning model using behavior data from `ransomware.csv`
2. You enter behavior values (file access, CPU usage, etc.)
3. The model predicts if the behavior looks like ransomware (1) or normal (0)

## 🧪 Test Values

**Normal Behavior:**
- File Access: 10
- File Modify: 5
- CPU Usage: 15
- Disk Usage: 20
- **Result:** ✅ System Safe

**Ransomware Behavior:**
- File Access: 90
- File Modify: 70
- CPU Usage: 85
- Disk Usage: 95
- **Result:** ⚠️ Ransomware Detected

## 📚 Learn More

This is a beginner-friendly project that demonstrates:
- Machine learning with scikit-learn
- Web development with Flask
- Behavior-based security detection

---

**Made for learning purposes** 🎓
