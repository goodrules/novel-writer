import sys
import readline
import json

from novel import *
from save import *
from settings import *
from misc import *

print("LLM Novel Writer - Outlining")
print("----------------------------")

novel_number, novel = load_or_create()

# Characters
if not getattr(novel, "characters", None):
    novel.setup()
    redo = True
    while redo:
        print(novel.create_characters(outliner))
        redo = redo_prompt()
    novel_number = save_new(novel)

# Settings
if not getattr(novel, "settings", None):
    redo = True
    while redo:
        print(novel.create_settings(outliner))
        redo = redo_prompt()
    save(novel, novel_number)

# Plot
if not getattr(novel, "plot", None):
    redo = True
    while redo:
        print(novel.create_plot(outliner))
        redo = redo_prompt()
    save(novel, novel_number)

# Subplots
if not getattr(novel, "subplots", None):
    redo = True
    while redo:
        print(novel.create_subplots(outliner))
        redo = redo_prompt()
    save(novel, novel_number)

# Synopsis
if not getattr(novel, "synopsis", None):
    redo = True
    while redo:
        print(novel.create_synopsis(writer))
        redo = redo_prompt()
    save(novel, novel_number)


print(f"This concludes the initial novel outline. You should now review the file at novels/{novel_number}.json and make edits as needed. After editing the file, run expand_outline.py.")
