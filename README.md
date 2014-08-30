#jack

---

###'Jack-o-nine-tails', fix development


You can download english version from here: WILL BE AVAILABLE SOON

Changelog (untranslated): http://pastebin.com/HCiCKAxx

###Installation

You have to download full version from author's blog (1.2 ATM), then install this on top with replacing files.

###How to collect all the files together from the repository?
Main file in the repository is split by a `split_file.py`

**split_file.py SCRIPT WORKS ONLY WITH A 2 VERSION OF PYTHON!**

Before you start be sure to download and mount `txt2gam` path to it in qgen!

Warning - if one of the text files when editing was not saved in `utf8 without bom` format, then `txt2gam` can ignore it while merging!

Do not download the source code from the site using the button ``Download ZIP``! Text files are downloaded from the site will be converted to UNIX format, which makes their contents into a mess and makes it impossible to build a file! Download the source code from GitHub client directly, and make sure that the file format was dos/win!

###Note for translators
Text is placed between either `'` or `"` symbol.
If you use `'` symbol in word when text is closed with same symbol, you will break line prematurely and also break the game. So use double quotes `''`, or ` symbol. 

If line is closed with `"` symbol, you can use single quotes without any problem. The problem is, you can't just replace all `'` symbols with `"`, because it will break some certain places in code when using variable in the text. Also, you can use ` symbol instead of ', but it looks not that great. Example:

``'Yo, I''m testing it.'``

``"Yo, I'm testing it."``

``'Yo, I`m testing it.' ``

Also check for "`content`" word if it used in text. It's doesn't matter if it is a part of a word like "discontent". Content with large "C" letter will not count. Replace english "`o`" or "`c`" letter with russian. Otherwise game will try to insert path to your game location, example what will happen:

`"You dumped the contents of a tin can in a shabby bowl standing in a cage."`

will be something like that:

`"You dumped the E:\games\Jack-o-nine-tails\content of a tin can in a shabby bowl standing in a cage."`

Blame QSP for that.

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