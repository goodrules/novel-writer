import json
import random

class Novel:
    def __init__(self):
        self.one_liner = None
        self.prose = None
        self.extra_context_story_structure = None
        self.extra_context_story = None
        self.extra_context_characters = None
        self.extra_context_settings = None
        self.extra_context_world = None
        self.synopsis = None
        self.characters = None
        self.settings = None
        self.title = None
        self.plot = None
        self.plot_outline = None
        self.chapter_outlines = {}
        self.chapters = {}
    
    def setup(self):
        with open('context/prose.txt', 'r') as file:
            self.prose = file.read()
        with open('context/one_liner.txt', 'r') as file:
            self.one_liner = file.read()
        with open('context/story_structure.txt', 'r') as file:
            self.extra_context_story_structure = file.read()
        with open('context/story.txt', 'r') as file:
            self.extra_context_story = file.read()
        with open('context/characters.txt', 'r') as file:
            self.extra_context_characters = file.read()
        with open('context/settings.txt', 'r') as file:
            self.extra_context_settings = file.read()
        with open('context/world.txt', 'r') as file:
            self.extra_context_world = file.read()
    
    def create_characters(self, writer):
        print("I'm writing a list of characters...")
        prompt = f"""Write a json object that describes at least 10 characters of the novel. The list should
include the main character, at least 3 supporting character, a main antagonist, at least 2 secondary antagonists,
and at least 3 neutral characters.  Consider the information below and create or adjust characters as needed.

One line description for the novel:
{self.one_liner}


Extra information about the story:
{self.extra_context_story}


Extra information about subplots and plot seeds:
{self.extra_context_subplots_seeds}


Extra information about the characters:
{self.extra_context_characters}


Extra information about the world in which the story takes place:
{self.extra_context_world}


Here is the format to follow:

[
{{
"name": "The name of the character.",
"personality": "A paragraph describing the character's personality. Include some likeable attributes and dislikeable attributes. Write a considerable amount about the character's personality and use colorful language to describe him or her. Write in the tone of the novel. Do not write about what the character does in the novel.",
"physique": "Some details about the character's physique."
}},
...
]


Do not write anything except json. Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.characters = writer.write(prompt)
        return self.characters
            
    def create_settings(self, writer):
        print("I'm writing a list of settings...")
        prompt = f"""Write a json object that describes at least 6 settings of the novel.  Consider the information below.


One line description for the novel:
{self.one_liner}


Extra information about the story:
{self.extra_context_story}


Extra information about subplots and plot seeds:
{self.extra_context_subplots_seeds}


Extra information about locations:
{self.extra_context_settings}


Extra information about the world in which the story takes place:
{self.extra_context_world}


Novel characters:
{self.characters}


Here is the format to follow:

[
{{
"name": "The name of the setting.",
"description": "A paragraph describing the setting. Describe its attributes in detail so a reader can clearly picture the place. Use words that inspire the right emotions that will accentuate the plot elements that take place in the setting. Write in the correct tone for the novel."
}},
...
]


Do not write anything except json. Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.settings = writer.write(prompt)
        return self.settings

    def create_plot(self, writer):
        print("I'm writing a plot...")
        prompt = f"""Write a json object that describes every act of the novel in a paragraph each.

One line description for the novel:
{self.one_liner}


How the novel is written (structure):
{self.extra_context_story_structure}


Extra information about the story:
{self.extra_context_story}


Extra information about subplots and plot seeds:
{self.extra_context_subplots_seeds}


Extra information about the world in which the story takes place:
{self.extra_context_world}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Here is the format to follow:

[
{{
"act-number": 1,
"act-description": "A paragraph describing this act of the novel. It should consist of at least 10 sentences outlining the setup of the story, including the exposition, world foundation, inciting incident, and call for adventure. Write it in the style of the novel."
}},
{{
"act-number": 2,
"act-description": "A paragraph describing this act of the novel. It should consist of at least 10 sentences outlining the confrontation of the story, including the rising action, midpoint, and crisis. Write it in the style of the novel."
}},
{{
"act-number": 3,
"act-description": "A paragraph describing this act of the novel. It should consist of at least 10 sentences outlining the resolution of the story, including the climax, falling action, and resolution. Write it in the style of the novel."
}}
]

The json object should have three main elements representing each act of the story, and each part
should have a description. Each part description is a paragraph consisting of at least 10 sentences.
Do not write anything except json. Escape all double-quote characters within string output with backslash.  
Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.plot = writer.write(prompt)
        return self.plot

    def create_subplots(self, writer):
        print("I'm writing a list of possible sub-plots...")
        prompt = f"""Write a json object that describes at least 4 subplots of the novel.  Consider the information below.


Novel main plot:
{self.plot}


Extra information about subplots and plot seeds:
{self.extra_context_subplots_seeds}


Extra information about the world in which the story takes place:
{self.extra_context_world}


Novel characters:
{self.characters}


Extra information about locations:
{self.settings}


Here is the format to follow:

[
{{
"subplot-name": "The name of the subplot.",
"subplot-description": "A paragraph describing the subplot. asdf. Write in the correct tone for the novel."
}},
...
]


Do not write anything except json. Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.subplots = writer.write(prompt)
        return self.subplots

    def create_synopsis(self, writer):
        print("I'm writing a synopsis...")
        prompt = f"""Write a synopsis for a novel based on the following information.  Summarize into 5 sentences.  

Novel main plot:
{self.plot}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Extra information about the world in which the story takes place:
{self.extra_context_world}

Do not include any characters by name.  Do not write the title or any additional formatting. Only write a single long paragraph.
"""
        self.synopsis = writer.write(prompt)
        return self.synopsis

    def create_plot_outline(self, writer):
        print("I'm writing an outline...")
        prompt = f"""Write a json object that describes every chapter of the novel in a paragraph each.

Each chapter should have the following structure:
- Opening Scene: Start with immediacy - either action or a strong character moment that hooks readers while naturally incorporating world details. Your techno-magical setting offers great opportunities for this.
- Middle Scene(s): Layer in complications and developments while deepening the subplots you've outlined (family legacy, romantic tension, ethical dilemmas, etc.)
- Closing Scene: End with something that propels readers forward - either a revelation, a new complication, or a character decision point.

How the novel is written (prose and layering):
{self.prose}


Novel main plot:
{self.plot}


Novel sub-plots:
{self.subplots}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Extra information about the world in which the story takes place:
{self.extra_context_world}


Here is the format to follow:

[
{{
"act-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the sixth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel."
]
}},
{{
"act-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the sixth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the seventh chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the eighth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the ninth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the tenth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the eleventh chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the twelth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.
]
}},
{{
"act-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel.",
"A paragraph describing the sixth chapter of this part. It should consist of at least 5 sentences. Write it in the style of the novel."
]
}}
]

The json object should have three main elements representing each act of the story. Act 1 should have 6 chapters, Act 2 should have 12 chapters, 
and Act 3 should have 6 chapters. Each chapter description is a paragraph consisting of at least 6 sentences.
Do not write anything except json. Escape all double-quote characters within string output with backslash.
Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.plot_outline = writer.write(prompt)
        return self.plot_outline

    def create_title(self, writer):
        print("I'm writing a title...")
        prompt = f"""Create 3 different titles for this story.
        
Novel plot:
{self.plot}

Respond with only the titles. Do not respond with an introduction or statement before the title."""
        self.title = writer.write(prompt)
        return self.title

    def parse_outline_json(self):
        print("Parsing outline JSON into native objects...")
        try:
            self.parsed_characters = json.loads(self.characters)
        except Exception as e:
            print("Characters weren't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e

        try:
            self.parsed_settings = json.loads(self.settings)
        except Exception as e:
            print("Settings weren't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e
            
        try:
            self.parsed_plot = json.loads(self.plot)
        except Exception as e:
            print("Plot wasn't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e

    def parse_outline_expanded_json(self):
        try:
            self.parsed_plot_outline = json.loads(self.plot_outline)
        except Exception as e:
            print("Plot outline wasn't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e

    def write_chapter_outline(
            self, 
            writer, 
            chapter_number, 
            chapter_summary, 
            previous_chapter_summary, 
            next_chapter_summary, 
            previous_outline
        ):
        print(f"I'm writing an outline for chapter {chapter_number}...")
        print(f"Previous chapter summary:\n{previous_chapter_summary}")
        print(f"Chapter summary:\n{chapter_summary}")
        print(f"Next chapter summary:\n{next_chapter_summary}")
        num_paragraphs = random.randint(10,20)
        output_format = ",\n".join([
            f"""{{
"paragraph-number": {pn},
"paragraph-summary": "A sentence outlining paragraph {pn} of the chapter written in the correct tone for the novel."
}}"""
            for pn in range(1,num_paragraphs)
        ])
        prompt = f"""Write JSON that outlines the chapter {chapter_number} of this novel as {num_paragraphs} paragraph summaries.

Each chapter should have the following structure:
- Opening Scene: Start with immediacy - either action or a strong character moment that hooks readers while naturally incorporating world details. Your techno-magical setting offers great opportunities for this.
- Middle Scene(s): Layer in complications and developments while deepening the subplots you've outlined (family legacy, romantic tension, ethical dilemmas, etc.)
- Closing Scene: End with something that propels readers forward - either a revelation, a new complication, or a character decision point.

Current chapter number:
{chapter_number}


Current chapter summary (the paragraphs should all describe this):
{chapter_summary}


Previous chapter summary (the first paragraph should lead from this):
{previous_chapter_summary}


Previous chapter outline (the first paragraph should lead from this):
{previous_outline}


Next chapter summary (the last paragraph should lead into this):
{next_chapter_summary}


How the novel is written (prose and layering):
{self.prose}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Novel plot:
{self.plot}


Here is the format to follow:

[
{output_format}
]


Create a JSON object that has a paragraph summary for each of the chapter's {num_paragraphs} paragraphs.
Every paragraph summary you write is a part of the current chapter and should be described by the
current chapter summary. None of the paragraph summaries should be described by the rest of the plot.
The first paragraph should begin where from the previous chapter summary leaves off. The last paragraph 
should lead to the next chapter summary. Do not write anything except json. Escape all double-quote characters within string output with backslash.
Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.chapter_outlines[chapter_number] = writer.write(prompt)
        return self.chapter_outlines[chapter_number]

    def parse_chapter_outline_json(self):
        print("Parsing chapter outline JSON into native objects...")
        self.parsed_chapter_outlines = {}
        for key, value in self.chapter_outlines.items():
            try:
                self.parsed_chapter_outlines[key] = json.loads(value)
            except Exception as e:
                print(f"Chapter {key}'s outline wasn't able to be parsed to JSON. Fix it in the novel json file then rerun.")
                raise e

    def write_paragraph_block(
            self,
            writer,
            chapter_paragraph_block_number,
            previous_paragraph_block,
            paragraph_descriptions,
            next_paragraph_descriptions,
            chapter_number,
            chapter_summary,
            chapter_num_paragraphs
        ):
        start_paragraph_number = paragraph_descriptions[0]["paragraph-number"]
        end_paragraph_number = paragraph_descriptions[-1]["paragraph-number"]

        paragraph_descriptions_unrolled = "\n\n".join([
            paragraph_data["paragraph-summary"]
            for paragraph_data in paragraph_descriptions
        ])

        next_paragraph_descriptions_unrolled = "\n\n".join([
            paragraph_data["paragraph-summary"]
            for paragraph_data in next_paragraph_descriptions
        ])

        print(f"I'm writing paragraphs {start_paragraph_number}-{end_paragraph_number} for chapter {chapter_number} (block number {chapter_paragraph_block_number})...")
        print(f"Paragraph descriptions:\n{paragraph_descriptions}")

        prompt = f"""Continue writing {len(paragraph_descriptions)} more paragraphs of the novel using the information below.


How the novel is written (prose and layering):
{self.prose}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Novel synopsis:
{self.synopsis}


Summary of the current chapter:
{chapter_summary}


Descriptions of the paragraphs you will write (PARAGRAPH DESCRIPTIONS):
{paragraph_descriptions_unrolled}


Descriptions of paragraphs that will be directly after the paragraphs you write (NEXT PARAGRAPHS):
{next_paragraph_descriptions_unrolled}


Continue writing the story for {len(paragraph_descriptions)} more paragraphs based on the PARAGRAPH DESCRIPTIONS 
above. Each paragraph should have 5-10 sentences. Make sure what your writing leads well into NEXT
PARAGRAPHS. Only write the novel's paragraphs. Do not write an introduction or description before
or after the paragraphs. Below are the paragraphs that are directly before the paragraphs you will write:

{previous_paragraph_block}"""
        if getattr(self, "chapters", None) is None:
            self.chapters = {}
        if chapter_number not in self.chapters:
            self.chapters[chapter_number] = {}
        self.chapters[chapter_number][chapter_paragraph_block_number] = writer.write(prompt)
        return self.chapters[chapter_number][chapter_paragraph_block_number]
