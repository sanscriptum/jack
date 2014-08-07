#jack

---

###'Jack-o-nine-tails', fix development


You can download english version from here: WILL BE AVAILABLE SOON

Changelog (untranslated): http://pastebin.com/HCiCKAxx

###Installation

You have to download full version from author's blog (1.2 ATM), then install this on top with replacing files.

###How to collect all the files together from the repository?
Main file in the repository is split by a split_file.py

**split_file.py SCRIPT WORKS ONLY WITH A 2 VERSION OF PYTHON!**

Before you start be sure to download and mount txt2gam path to it in qgen!

Warning - if one of the text files when editing was not saved in utf8 without bom format, then txt2gam can ignore it while merging!

Do not download the source code from the site using the button "Download ZIP"! Text files are downloaded from the site will be converted to UNIX format, which makes their contents into a mess and makes it impossible to build a file! Download the source code from GitHub client directly, and make sure that the file format was dos/win!
***

**How get a bunch of sources from the .qsp file?**

1. Qgen -> export -> as txt2gam -> ```jack.txt```
2. ```split_file.py --split jack.txt``` in batch file. src folder will be deleted!
3. In src folder there will be txt files in utf8 format.

**First way to merge this:**

1. ```split_file.py --merge2 jack.txt``` in batch file;
2. Open old version of ```jack.qsp``` in qgen and import of new ```jack.txt```;
3. Make Save as and name it differently, close qgen;
4. Rename new file to ```jack.qsp``` and replace old by it;

**Second way:**

1. ```split_file.py --merge2 jack.txt``` in batch file;
2. Compile the game with TXT2GAM: ```txt2gam jack.txt jack.qsp``` in batch file;
3. Open new ```jack.qsp``` in qgen and make export ```text file in TXT2GAM format``` to jack.txt;
4. Compile the game again with TXT2GAM;

If QSP the file was suspiciously little after its compiling - it 100% corrupted and will not start, check the code for errors.
