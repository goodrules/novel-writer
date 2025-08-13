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

# Plot outline
if not getattr(novel, "plot_outline", None):
    redo = True
    while redo:
        print(novel.create_plot_outline(writer))
        redo = redo_prompt()
    save(novel, novel_number)


# Title
if not getattr(novel, "title", None):
    redo = True
    while redo:
        print(novel.create_title(writer))
        redo = redo_prompt()
    save(novel, novel_number)


print(f"This concludes the novel outlining process. You should now review the file at novels/{novel_number}.json and make edits as needed. After editing the file, run draft.py.")
