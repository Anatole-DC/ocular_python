<h1 align="center">OCULAR</h1>

_<h4 align="center">Extract the world's data</h4>_

OCULAR is a computer vision framework, whose purposes is to build workflows to analyse images and extract datas.

___

**Techno :** Python, OpenCV

**Author :** [Anatole de Chauveron](https://github.com/Anatole-DC)

**Licence :** All rights reserved

___

## Summary

- [Installation](#installation)
  - [Requirements](#requirements)
  - [Clone the repository](#clone-the-repository)
  - [Setup virtual environment](#setup-virtual-environment)
  - [Install dependencies](#install-dependencies)
- [Run the project](#run-the-project)

## Installation

### Requirements

**Python**

```bash
python --version
# Python 3.8.10
```

**Virtualenv**

```bash
virtualenv --version
# virtualenv 20.0.17 from /usr/lib/python3/dist-packages/virtualenv/__init__.py
```

### Clone the repository

```bash
git clone https://github.com/ocular-systems/ocular-python
```

### Setup virtual environment

Move to the project folder and create the virtualenv.

```bash
cd occular-python
virtualenv .venv
```

**Activate the environment**

```bash
source .venv/bin/activate
```

> Do not forget do activate the environment before executing the project, or installing dependencies.

**Deactivate the environment**

```bash
deactivate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the project

```bash
python main.py
```