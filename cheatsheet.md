
# 🧠 Python Project Setup — Command Cheat Sheet

## 🔹 1. Navigate to your project
```powershell
cd "path\to\your\project"
```

---

## 🔹 2. Create a Virtual Environment
```powershell
python -m venv .venv
```

---

## 🔹 3. Activate the Virtual Environment (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```
*You'll see `(.venv)` prefix in your terminal if it's active.*

---

## 🔹 4. Install Packages
✅ Correct format:
```bash
pip install numpy matplotlib SpeechRecognition PyAudio
```

❌ Incorrect formats you learned to avoid:
```bash
install numpy                  # ❌ wrong
pip install pip install ...    # ❌ wrong
```

---

## 🔹 5. Save Installed Packages
```bash
pip freeze > requirements.txt
```

---

## 🔹 6. Install from requirements.txt
```bash
pip install -r requirements.txt
```

---

## 🔹 7. If `pip freeze` fails after renaming folders...
**Reason**: Folder name change breaks `.venv` paths  
**Fix**: Recreate `.venv` and reinstall dependencies:
```bash
# Delete old .venv folder manually or via command
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🔹 8. Deactivate Virtual Environment
```bash
deactivate
```
