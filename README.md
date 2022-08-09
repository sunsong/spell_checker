# Spell Checker

A pre-commit hook to do spell checks.


* Free software: MIT license


## Features

* Prevent non English characters from being commited to source code.

## TODO

* Do spell checks for English.

## Installation

* For MacOS, `brew install pre-commit`. For all platform, `pip3 install --user pre-commit`

* Add the following lines to `.pre-commit-config.yaml` in your repo root
```
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/sunsong/spell_checker
    rev: v0.0.1
    hooks:
    -   id: check-chinese
```

* Run `pre-commit install`

## Usage

pre-commit hook will be triggered when commiting code using `git commit`
