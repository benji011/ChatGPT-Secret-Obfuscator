## ChatGPT Secret Obfuscator

A CLI tool that allows you to obfuscate sensitive information in Python. The idea is that you have full control of where how your code is serialized before & after going into some AI tool, which tends to be a blackbox. i.e. stuff goes in, stuff goes out (but you aren't aware what happens inside the box).

e.g. if your code looks like this:

```python
def make_ice_cream(flavor, toppings):
    """Make an ice cream with the given flavor and toppings."""
    ice_cream = f"A delicious {flavor} ice cream with {', '.join(toppings)} toppings!"
    return ice_cream
```

Then your output will look like this:

```python
def mmmmmmmmmmmmmm(ffffff, tttttttt):
    """MMMM aa iii ccccc with ttt ggggg ffffff aad tttttttt."""
    iii_ccccc = f"A ddddddddd {ffffff} iii ccccc with {', '.join(tttttttt)} tttttttt!"
    return iii_ccccc
```

It's not perfect though

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

```bash
cgso mycode.py
```

The obfuscated code will be printed to the console, so you can copy and paste it to the ChatGPT prompt
