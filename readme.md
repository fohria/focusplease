# focus please

are you easily distracted? do you often forget what you're doing and start randomly browsing cat pictures?

focus please allows you to set your browser's start/new tab page to show a message telling you what task you're currently (supposed to be) working on.

## how to use

currently you need to know a little python to use it.

i'll get to packaging this as a proper downloadable application as soon as i feel like procrastinating actual work again.

### requirements

- pysimplegui

### installation

1. download this repo
2. i recommend using conda/mamba to create a virtual environment:

```bash
mamba create -n focusplease
conda activate focusplease
mamba install -c conda-forge pysimplegui
```

3. run it:

```bash
python focus.py
```
