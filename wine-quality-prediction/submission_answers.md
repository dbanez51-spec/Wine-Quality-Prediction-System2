# Wine Quality Prediction System - Submission Answers (Section B)

## 1. SAD mini-analysis

| SAD element | Response |
|---|---|
| Problem statement | A wine producer needs a consistent, preliminary way to screen wine samples using recorded physicochemical measurements. |
| Users | Quality-control staff, production supervisor, or data analyst. |
| Inputs | Fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol. |
| Process | Validate input columns -> preprocess data -> apply trained model -> classify quality category. |
| Outputs | GOOD QUALITY / NEEDS IMPROVEMENT label and a model evaluation summary. |
| Key limitation | Trained on one red-wine dataset, so it may not work well for other wine types, producers, regions, or testing conditions. |

**Mini use-case:** The user uploads a CSV -> the system checks required columns -> the model predicts the quality category -> the system shows and exports the results.

## 2. Model evaluation results (from running `train_model.py`; your run should match because random_state=42)

| Class | Precision | Recall | F1-score |
|---|---|---|---|
| Needs improvement | 0.74 | 0.79 | 0.77 |
| Good quality | 0.80 | 0.76 | 0.78 |

Overall accuracy: 0.772 (test set of 272 samples after removing 240 duplicates)

Confusion matrix: [[101, 27], [35, 109]]

Simple explanation: The model is correct about 77% of the time. Both classes score similarly (about 0.74 to 0.80), so it is not just favoring one class. For GOOD QUALITY, precision is 0.80: when it says good, it is right 80% of the time. Recall is 0.76: it finds about 76% of the truly good wines and misses about 24% (35 of 144). Accuracy alone cannot show these misses. Accuracy shows how many samples were correct overall, but it can hide problems. Precision for "Good quality" tells how many samples predicted as good are really good. Recall for "Good quality" tells how many of the truly good samples the model found. F1-score balances precision and recall.

## 3. Screenshot checklist (do these yourself)
- [ ] Dashboard: the three metrics and the dataset preview
- [ ] Prediction results table after uploading `sample_wine_input.csv`
- [ ] Error message after uploading a CSV with a column removed

## 4. GitHub steps
1. On github.com, click **New repository**. Name it `wine-quality-prediction`, set it to **Public**, click **Create repository**.
2. Open a terminal in your project folder, then run:
```bash
git init                                   # start tracking the folder
git add train_model.py app.py requirements.txt README.md   # choose the files to save
git commit -m "Build wine quality prediction prototype"    # save a snapshot
git branch -M main                         # name the branch "main"
git remote add origin https://github.com/YOUR-USERNAME/wine-quality-prediction.git   # replace YOUR-USERNAME
git push -u origin main                    # upload to GitHub
```
3. Sign in using the approved GitHub method (browser login or GitHub Desktop). Never put passwords or tokens in your code.
4. Ask your instructor if you should also upload `wine_quality.csv` and `wine_model.pkl`.
5. Copy the repository URL for your submission.

## 5. Test table

| Test | How to do it | Pass? |
|---|---|---|
| Run train_model.py | `python train_model.py`; check `wine_quality.csv` and `wine_model.pkl` appear with no errors | ☐ |
| Run Streamlit app | `streamlit run app.py`; open http://localhost:8501 | ☐ |
| Upload sample CSV | Click "Download sample input CSV", then upload it; predictions appear | ☐ |
| Upload CSV missing a column | Delete one column (e.g. `alcohol`) from the sample CSV and upload; a red "Missing required columns" message appears | ☐ |
| Download results | Click "Download prediction results"; open the CSV and check the `Prediction` column | ☐ |
| Open GitHub repository | Visit your repo URL; files and README are visible | ☐ |

## 6. Reflection answers

1. **Target and excluded column:** The target is the quality category: GOOD QUALITY if the quality score is 6 or higher, NEEDS IMPROVEMENT if it is below 6. The original `quality` column is removed from the inputs because it is the answer itself. Keeping it would be target leakage: the model would look perfect in testing but would be useless for new samples that have no quality score.

2. **Recall for GOOD QUALITY:** Recall tells us how many of the truly good wines the model correctly found. Low recall means the model misses many good wines and labels them NEEDS IMPROVEMENT. For the business, this could cause extra re-testing or good batches being held back, which wastes time and money. In this lab, recall for GOOD QUALITY is 0.76, so about 1 in 4 good wines is wrongly flagged as needing improvement.

3. **Different producers:** The model learned patterns only from one set of red wines, made by certain producers and tested by certain tasters. Another producer may use different grapes, methods, or lab equipment, so the measurements and quality scores may follow different patterns. Accuracy can then drop.

4. **Preliminary screening:** The model uses only 11 measurements and cannot taste, smell, or check safety. It is also not 100% accurate and can make mistakes in both directions. So it should only help decide which batches need a closer look, with laboratory testing, sensory evaluation, and professional quality-control making the final decision.

5. **Improving reliability:** More data from many producers, regions, vintages, and wine types would help. Having several trained tasters score the same wines would give more reliable labels. Other helpful steps are testing on new batches, trying other models and cross-validation, and checking performance again regularly.

## 7. Submission checklist
- [x] SAD mini-analysis
- [x] `train_model.py` and `app.py`
- [x] `requirements.txt` and `README.md`
- [x] Model evaluation results (section 2; rerun `train_model.py` to confirm on your computer)
- [ ] Screenshots (section 3)
- [ ] GitHub repository URL (section 4)
- [x] Reflection answers
