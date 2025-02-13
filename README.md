# RoBERTa Zero-Shot Classification

This project demonstrates the use of a pre-trained RoBERTa model for zero-shot text classification. Zero-shot classification allows the model to classify text into categories it has not explicitly seen during training by leveraging natural language understanding capabilities.

---

## Features
- Utilizes the Hugging Face `transformers` library for seamless integration with the RoBERTa model.
- Performs zero-shot classification on any dataset, such as AG News.
- Flexible and easy-to-extend implementation.

---

## Requirements
- Python 3.10
- Anaconda
- Pip 21.0 or later

The complete list of dependencies is provided in `environment.yml`.

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local system:

```bash
git clone https://github.com/your-repo/roberta_zero_shot.git
cd roberta_zero_shot
```
### 2. Create the virtual environment
```bash
conda env create -f environment.yml
```
