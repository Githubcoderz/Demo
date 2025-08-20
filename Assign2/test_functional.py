import subprocess
import tempfile
import os

test_content = """Hello world.
Run this as a Test.
Give some data."""

def run_wordCount_with_args(args, content=test_content):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".txt") as tmp:
        tmp.write(content)
        tmp.flush()
        result = subprocess.run(["python", "wordCount.py"] + args + [tmp.name], capture_output=True, text=True)
    os.remove(tmp.name)  
    return result.stdout.strip()

def test_word_count_output():
    output = run_wordCount_with_args(["-w"])
    assert output.endswith(".txt")
    assert output.split()[0] == "7"

def test_char_count_output():
    output = run_wordCount_with_args(["-c"])
    assert output.endswith(".txt")
    assert output.split()[0].isdigit()

def test_line_count_output():
    output = run_wordCount_with_args(["-l"])
    assert output.startswith("3")

def test_all_counts():
    output = run_wordCount_with_args([])
    parts = output.split()
    assert parts[0] == "3" 
    assert parts[1] == "7" 
    assert parts[2].isdigit() 