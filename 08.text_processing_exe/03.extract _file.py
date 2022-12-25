___doc___ = """
Write a program that reads the path to a file and subtracts the file name and its extension.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
C:\Internal\training-internal\Template.pptx
Output--->
File name: Template
File extension: pptx

---------------------------------------------------
--->Input
C:\Projects\Data-Structures\LinkedList.cs
Output--->
File name: LinkedList
File extension: cs
---------------------------------------------------
"""

file_patn_and_name = input().split('\\')
file_name = file_patn_and_name[-1].split('.')
print(f'File name: {file_name[0]}')
print(f'File extension: {file_name[1]}')
