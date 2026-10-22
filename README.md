# Experiment 8: Implementation of Case Study on GitHub Actions for CI/CD Pipeline

**Course:** Software Engineering Lab  
**Project:** Smart Society System  
**Framework:** Django 4.2 / Python 3.11  
**CI/CD Engine:** GitHub Actions  

---

## 📌 Experiment Aim & Outcome
- **Aim:** To learn and study CI/CD pipeline implementation.
- **Expected Outcome:** Understand the core concepts of Continuous Integration (CI), Continuous Delivery (CD), and Continuous Deployment for a software engineering project.

---

## 🏗️ Architecture & Pipeline Design
The CI/CD pipeline consists of four sequential jobs configured in [`.github/workflows/ci.yml`](.github/workflows/ci.yml):

```
+-----------+       +-----------+       +-------------+       +------------+
|   Build   |  -->  |   Test    |  -->  |   Release   |  -->  |   Deploy   |
| (manage   |       |  (Django  |       |  (Artifact  |       | (Simulated |
|  check)   |       |   tests)  |       |   upload)   |       |  deploy)   |
+-----------+       +-----------+       +-------------+       +------------+
```

1. **Build (`build`):**
   - Checks out repository code.
   - Sets up Python 3.11 environment.
   - Installs dependencies from `requirements.txt`.
   - Executes `python manage.py check` to validate project configuration and models.

2. **Test (`test`):**
   - Runs only after `build` succeeds (`needs: build`).
   - Runs unit tests via `python manage.py test`.
   - Any test failure stops execution immediately, ensuring faulty code is not delivered.

3. **Release (`release`):**
   - Runs only after `test` succeeds (`needs: test`).
   - Packages the project files and uploads them as a downloadable artifact (`smart-society-release`) using `actions/upload-artifact@v4`.

4. **Deploy (`deploy`):**
   - Runs only on pushes to the `main` branch after `release` passes.
   - Simulates deployment to production server with:
     ```bash
     echo "Deploying Smart Society app (simulated - no server)"
     ```

---

## 💻 Local Testing Commands

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run system checks (Build stage)
python manage.py check

# 3. Run unit tests (Test stage)
python manage.py test
```

---

## 🚀 How to Show the Teacher
1. Open GitHub repository in the browser.
2. Go to the **Actions** tab.
3. Show the latest workflow run for `Django CI/CD`.
4. Point out the 4 green checkmarks:
   - ✅ `build`
   - ✅ `test`
   - ✅ `release` (Show downloadable `smart-society-release` artifact in summary)
   - ✅ `deploy` (Show console output: *"Deploying Smart Society app (simulated - no server)"*)
5. Explain how a failure in `test` prevents `release` and `deploy` from executing, ensuring pipeline safety.
