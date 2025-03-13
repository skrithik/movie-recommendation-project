**Movie Recommendation System using Cosine Similarity**

### **Project Overview**
This project implements a **Movie Recommendation System** using **cosine similarity**. The system recommends similar movies based on their content, such as descriptions, genres, and other textual features.

---
### **Steps Involved**

#### **1. Data Collection**
- Collected movie dataset containing **titles, genres, descriptions, and other metadata**.
- Ensured data availability and consistency.

#### **2. Data Cleaning**
- **Handled missing values**: Filled or removed missing entries to avoid errors.
- **Removed duplicate values**: Ensured each movie entry is unique.

#### **3. Text Processing**
- **Stemming**: Reduced words to their root forms (e.g., *running* → *run*).
- **Stopword Removal**: Eliminated common words (e.g., *the, is, and*).

#### **4. Feature Extraction**
- Used **CountVectorizer** to convert processed text into numerical vectors.
- Represented movie content as feature vectors for similarity comparison.

#### **5. Similarity Calculation**
- Used **cosine similarity** to measure the similarity between movie vectors.
- Higher cosine similarity indicates more relevant recommendations.

#### **6. Recommendation Generation**
- Retrieved and displayed the most similar movies based on user input.

---
### **Usage**
1. Run the script and enter a movie name.
2. The system returns a list of similar movies based on their content.

---
### **Technologies Used**
- **Python** (for implementation)
- **Pandas & NumPy** (for data processing)
- **NLTK** (for text preprocessing)
- **Scikit-learn** (for CountVectorizer & cosine similarity)

This system provides content-based recommendations by analyzing movie features and their similarities using vectorized representations.

