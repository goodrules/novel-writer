import sys

from writer_assist import *

writer = AnthropicWriterOpus()
response = writer.write("hello")
print(response)
