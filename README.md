
# 🐱🐶 Cats vs Dogs Classification with CNN

## 📌 Overview
This project uses a **Convolutional Neural Network (CNN)** to classify images of cats and dogs.  
The dataset comes from Kaggle’s **Dogs vs Cats** challenge. The workflow covers **data preprocessing, model building, training, evaluation, and visualization**.

---

## ⚙️ Workflow
1. **Dataset Preparation**
   - Original dataset contains two folders: `cats/` and `dogs/`.
   - Data was split into **train** and **validation** sets (80/20).
   - Images were resized to **128×128** and normalized (pixel values scaled to [0,1]).

2. **Model Architecture**
   - Convolutional layers with ReLU activation
   - MaxPooling layers for downsampling
   - Flatten + Dense layers for classification
   - Dropout for regularization
   - Sigmoid output for binary classification

3. **Training**
   - Optimizer: Adam  
   - Loss: Binary Crossentropy  
   - Metrics: Accuracy  
   - Trained for 10 epochs

4. **Evaluation**
   - Plotted **Training vs Validation Accuracy**  
   - Plotted **Training vs Validation Loss**  
   - Generated **Confusion Matrix** and **Classification Report**


5. **Deployment using Streamlit**
   - Deployed an app which can classify images into cat or dog.
---

## 📊 Results
- Achieved high accuracy on both training and validation sets.     


