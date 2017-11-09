# Brain- Computer Interface Codebase
------------------------------------

This is the codebase for BCI suite. Designed and written by OHSU and NEU.


## Features
-----------

*RSVPKeyboard* 

```
	*RSVP KeyboardTM* is an EEG (electroencephalography) based BCI (brain
		computer interface) typing system. It utilizes a visual presentation technique
		called rapid serial visual presentation (RSVP). In RSVP, the options are
		presented rapidly at a single location with a temporal separation. Similarly
		in RSVP KeyboardTM, the symbols (the letters and additional symbols) are
		shown at the center of screen. When the subject wants to select a symbol,
		they await the intended symbol during the presentation and elicit a p300 response to a target symbol.

	To run on windows, execute the .exe to start with GUI. Otherwise, run `python gui/RSVPKeyboard.py` in your terminal to begin. 
```
*Shuffle Speller*
```
	TBD.
```

*Matrix*
```
	TBD. 
```

## Dependencies
---------------
This project requires Psychopy, Python v 2.7, and other packages. See requirements.txt


## Installation
---------------

# BCI Setup

In order to run BCI suite on your computer, first install **Python 2.7** [from here.](https://www.python.org/downloads/) Then, you need to install required modules using pip (python's package manager). Pip should already be installed, but if not go [here.](https://pip.pypa.io/en/stable/installing/) There are two methods in this BCI repo to load all packages in:


1. Run `python utils/module_loader.py`.

-or-

  Use pip to iteratively install required modules.
    - `pip install -r requirements.txt`

    After pip is done, download two modules that are left according to your OS(64 or 32 bit), which are numpy+mkl 1.13.1 [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) and scipy 0.19.1 [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy).
    - pip install /path/to/numpy‑1.13.1+mkl‑cp27‑cp27m‑win_amd64.whl
    - pip install /path/to/scipy‑0.19.1‑cp27‑cp27m‑win_amd64.whl

* You will also need to set a python path for your session. If running demo or other files and you get an error that a module doesn't exist, try setting your path again. You can set your path as follows: *

2. run `export PYTHONPATH=.` for Mac or `set PYTHONPATH=.` for Windows

> You are ready to run BCI suite!

Start by running `python gui/BCInterface.py` in your command prompt or terminal

## Modules and Vital Functions
------------------------------

- `acquistion`: acquires data, gives back desired time series, saves at end of session.
- `display`: handles display of stimuli on screen, passing back stimuli timing.
- `eeg_model`: trains and classifies eeg responses based on eeg and triggers.
- `gui`: end-user interface into system. See BCInterface.py and RSVPKeyboard.py.
- `helpers`: input/output functions needed for system, as well as helpful intilization functions.
- `utils`: utility functions needed for operation and installation.
- `language_model`: gives prob of letters during typing.
- `parameters`: json file for parameters.
- `static`: images, misc manuals, and readable texts for gui.
- `bci_main`: executor of experiments.

## Demo and Tests
-----------------

All major functions and modules have demo and test files associated with them. This should help orient you to the functionaly as well as serve as documentation. *If you add to the repo, you should be adding tests and fixing any test that fail when you change the code.* 

For example, you may run the bci_main demo by:
> run `python demo/bci_main_demo.py`

This demo will load in parameters and exceute a demo task defined in the file. There are demo files for all modules listed above except language_model, helpers, and utils.

This repository uses pytest for execution of tests. You may execute them by:

> run `py.test` or `pytest` depending on your OS

## Contribution Guidelines
--------------------------

1. All added code will need tests and a demo (if a large feature).
2. All tests must pass to merge, even if they are seemingly unrelated to your task.
3. Pull requests must be tested locally and by the requester on a different computer.
4. Use Spaces, not Tabs.
5. Use informative names for functions and classes.
6. Document the input and output of your functions / classes in the code. eg in-line commenting
7. Do not push IDE or other local configuration files.
8. All new modules or major functionality should be documented outside of the code.
