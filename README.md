# 🔐 Basic Encryption & Decryption in Python

A simple Python project that demonstrates **text encryption and decryption using the Caesar Cipher technique**.

## 📌 About the Project

This program allows the user to enter a text message and a shift key. The program then:

1. Encrypts the text using the given shift key.
2. Displays the encrypted text.
3. Decrypts the encrypted text using the same key.
4. Displays the original text again.

The project is designed to understand the basic concepts of **cryptography and Python programming**.

## ✨ Features

* 🔒 Caesar Cipher-based encryption
* 🔓 Text decryption
* 🔠 Supports uppercase and lowercase letters
* 🔢 Accepts a user-defined shift key
* 📝 Preserves spaces and special characters
* 🐍 Built entirely with Python
* 🎓 Beginner-friendly cybersecurity project

## 🛠️ Technologies Used

* **Python 3**
* `ord()` and `chr()` functions
* String manipulation
* Modular arithmetic

## ⚙️ How It Works

The Caesar Cipher shifts each alphabetic character by a specified number of positions.

For example, with a shift key of **3**:

```text
A → D
B → E
C → F
```

The program also uses modulo `26` to ensure that letters wrap around the alphabet.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd <project-folder>
```

### 3. Run the Python program

```bash
python encryption.py
```

## 💻 Example

### Input

```text
Enter the text: Hi, I am Pavan.V.H
Enter the shift key: 6
```

### Output

```text
Encrypted Text: No, O gs Vg bgt.B.N
Decrypted Text: Hi, I am Pavan.V.H
```

## 📚 Learning Outcomes

Through this project, I learned:

* How the Caesar Cipher works
* Basic encryption and decryption concepts
* Python functions
* String processing
* ASCII/Unicode character conversion using `ord()` and `chr()`
* Modular arithmetic
* Handling uppercase and lowercase characters

## ⚠️ Disclaimer

This project is created for **educational purposes**. Caesar Cipher is a simple classical cipher and is **not suitable for protecting real-world sensitive information**.

## 👨‍💻 Author

**Pavan V Halapeti**

ECE Student | Interested in Cybersecurity, AI & Programming

---

⭐ If you found this project useful, consider giving the repository a star!

