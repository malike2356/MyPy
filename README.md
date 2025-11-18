# MyPy - Python Learning Repository

A comprehensive collection of Python tutorials, Django projects, and machine learning experiments.

## 📚 About

This repository contains my Python learning journey, including:
- **Python Basics**: Fundamentals, data structures, control flow, functions, OOP
- **Django Projects**: E-commerce web application (vShop)
- **Machine Learning**: Datasets and Jupyter notebooks for data analysis
- **Utilities**: Spreadsheet automation, file processing, and more

**Note**: This is a **learning repository**. Code is for educational purposes and is not production-ready. See security notes in Django settings.

## 📂 Repository Structure

```
MyPy/
├── python/              # Python tutorial files (numbered 1-20)
│   ├── 1_Strings.py     # String operations
│   ├── 2_Math&Numbers.py
│   ├── 3_Lists.py
│   ├── 4_Tuples.py
│   ├── 5_Functions.py
│   ├── 6_If_Statements.py
│   ├── 7_If_elif_Statement.py
│   ├── 8_If_Statement__Booleans.py
│   ├── 9_Dictionaries.py
│   ├── 10_While_loops.py
│   ├── 11_Guess Game.py
│   ├── 12_For_Loops.py
│   ├── 13_For_Loop_Functions.py
│   ├── 14_2DList_and_Nested_Loops.py
│   ├── 15_Translator.py
│   ├── 16_Try_Except.py
│   ├── 17_Opening_External_Files.py
│   ├── 18_Git.py
│   ├── 19_Objects_Classes.py
│   ├── 20_Practice_Objects_Classes.py
│   ├── Student_Class.py
│   ├── Automating_Spreadsheets.py
│   ├── PathLibs.py
│   ├── Roll_Dice_Program.py
│   └── Time_Function.py
├── django/              # Django web development projects
│   ├── vShop/           # E-commerce Django application
│   │   ├── products/    # Products app
│   │   ├── vshop/       # Project settings
│   │   └── templates/   # HTML templates
│   ├── helloworld/      # Django hello world example
│   └── How_to_django.txt
├── ML/                  # Machine Learning
│   ├── HelloWorld.ipynb # Jupyter notebook
│   ├── music.csv        # Music dataset
│   └── vgsales.csv      # Video game sales dataset
└── gbda/                # GBDA project
    └── main.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- (Optional) Django 4.1+ for Django projects
- (Optional) Jupyter Notebook for ML files

### Python Tutorials

Navigate to the `python/` directory and run any tutorial file:

```bash
cd python
python3 1_Strings.py
```

### Django Project (vShop)

```bash
cd django/vShop
pip install django
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application.

**⚠️ Security Note**: The Django settings contain development-only configurations. Do NOT use in production without proper security settings (environment variables, SECRET_KEY, DEBUG=False, etc.).

## 📖 Learning Path

The Python tutorial files are numbered 1-20 to follow a logical learning progression:

1. **Basics** (1-5): Strings, Math, Lists, Tuples, Functions
2. **Control Flow** (6-10): If statements, While loops
3. **Advanced Control** (11-15): Games, For loops, Translators
4. **Error Handling** (16): Try/Except blocks
5. **File I/O** (17): File operations
6. **OOP** (18-20): Classes and Objects

## 🛠️ Tools & Libraries Used

- **Python Standard Library**: math, datetime, random, pathlib, etc.
- **Django**: Web framework for Python
- **openpyxl**: Excel file manipulation
- **Pandas**: Data analysis (for ML datasets)
- **Jupyter**: Interactive notebooks

## 📝 Code Quality

- All Python files have been syntax-checked and tested
- Code follows PEP 8 style guidelines
- Comments included for educational purposes
- Fixed typos and bugs

## ⚠️ Important Notes

- This is a **learning repository**, not production-ready code
- Django settings are configured for development only
- Some files require user input (interactive programs)
- File dependencies: Some scripts require text files (myProfile.txt, spider.txt, etc.)

## 📄 License

This is a personal learning repository. Feel free to use the code for learning purposes.

## 🤝 Contributing

This is a personal learning project. Suggestions and feedback are welcome!

---

**Last Updated**: November 2024  
**Status**: Learning Repository - Clean and Organized
