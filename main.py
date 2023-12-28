import json

def notebook_to_script(notebook_filename, script_filename):

    with open(notebook_filename) as notebook_file:
        notebook = json.load(notebook_file)
    
    output_text_fragments = []
    
    for cell in notebook["cells"]:
        
        cell_type = cell["cell_type"]
        if cell_type == "code":
            source = cell["source"]
            
            output_text_fragments.extend(source)
            output_text_fragments.append("\n\n\n")
    
    output_text = "".join(output_text_fragments)
    
    with open(script_filename, "w") as script_file:
        script_file.write(output_text)

if __name__ == "__main__":
    notebook_filename = "AtCoder Beginner Contest 252.ipynb"
    script_filename = "test.py"
    notebook_to_script(notebook_filename, script_filename)