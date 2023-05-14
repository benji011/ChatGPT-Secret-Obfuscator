## ChatGPT Secret Obfuscator

A CLI tool that allows you to obfuscate sensitive information in Python. The idea is that you have full control of where how your code is serialized before & after going into some AI tool, which tends to be a blackbox. i.e. stuff goes in, stuff goes out (but you aren't aware what happens inside the box).

## Installation

```bash
git clone git@github.com:benji011/ChatGPT-Secret-Obfuscator.git
cd chatgpt-secret-obfuscator
pip install -e .
```

## Usage

Run the below command as

```bash
cgso <file-name>
```

e.g.

```bash
cgso mycode.py
```

The obfuscated code will be printed to the console, so you can copy and paste it to the ChatGPT prompt
