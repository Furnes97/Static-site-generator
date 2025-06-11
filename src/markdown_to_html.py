from markdown_blocks import markdown_to_html_node
from pathlib import Path
import os

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:]

    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md_file = file.read()

    with open(template_path, "r") as file:
        template_file = file.read()


    html_txt = markdown_to_html_node(md_file).to_html()


    title = extract_title(md_file)

    new_html = template_file.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html_txt)


    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(new_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


"""
for path in os.listdir(dir_path_content):
    if os.path.isfile(os.path.join(dir_path_content, path)):
        new_path = os.path.join(dest_dir_path, os.path.relpath(path, dir_path_content))
        generate_page(path,template_path, new_path.replace("md","html"))

    if os.path.isdir(os.path.join(dir_path_content, path)):
        new_path = os.path.join(dir_path_content, path)
        print("___-------______ HELLLOOOOOOOOO")
        print(new_path)
        return generate_pages_recursive(os.path.join(dir_path_content, path), template_path , dest_dir_path)


"""


"""
generate_page(markdown_1_path, html_temp_path, destination)


path_to_content = "content"
file_paths_blog, dir_paths_blog = file_dir_paths(path_to_content)
dir_paths_blog.sort(key=lambda d_path: d_path.count("/"))

for path in dir_paths_blog:
    os.mkdir(os.path.join(path_to_public, os.path.relpath(path, path_to_content)))


for path in file_paths_blog:
    new_path = os.path.join(path_to_public, os.path.relpath(path, path_to_content))
    generate_page(f"content/{os.path.relpath(path, path_to_content)}", html_temp_path, new_path.replace("md", "html"))


"""
