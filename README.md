# lamadava-python

[![Package](https://github.com/adw0rd/lamadava/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/adw0rd/lamadava/actions/workflows/python-package.yml)
![PyPI](https://img.shields.io/pypi/v/lamadava)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lamadava)

[![Downloads](https://pepy.tech/badge/lamadava)](https://pepy.tech/project/lamadava)
[![Downloads](https://pepy.tech/badge/lamadava/month)](https://pepy.tech/project/lamadava)
[![Downloads](https://pepy.tech/badge/lamadava/week)](https://pepy.tech/project/lamadava)


## Installation

```
pip install lamadava
```

## Usage

Create token https://lamadava.com/tokens and copy "Access key"

```
from lamadava import Client
cl = Client(access_key="<ACCESS_KEY>")
user = cl.user_info_by_username("instgram")
print(user)
```
