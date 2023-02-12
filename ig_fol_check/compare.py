import difflib
import tkinter as tk
from tkinter import filedialog

# Open file dialog to select the first file
root = tk.Tk()
root.withdraw()
print("Select the earlier .txt file")
file1_path = filedialog.askopenfilename(
    title="Select first file", filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
)
print("Select the newest .txt file")
# Open file dialog to select the second file
file2_path = filedialog.askopenfilename(
    title="Select second file",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
)

# Read the contents of both files
with open(file1_path, "r") as file1:
    file1_contents = file1.readlines()

with open(file2_path, "r") as file2:
    file2_contents = file2.readlines()

# Compare the contents of the two files using difflib
differ = difflib.Differ()
diff = list(differ.compare(file1_contents, file2_contents))
fol = list("\n".join(diff).split("\n"))

fol = [fol[i] for i in range(len(fol)) if i % 2 == 0]

if not diff:
    print("No difference")
else:
    print("Unfollowers: ")
    for i in fol:
        if i[0] == "-":
            print(i[2:])
    print()
    print("New followers:")
    for i in fol:
        if i[0] == "+":
            print(i[2:])
