import os
from textnode import TextNode, TextType
from folder_management import file_dir_paths
from shutil import rmtree, copy

from markdown_to_html import generate_page, generate_pages_recursive



def main():
    path_to_public = "public"
    path_to_static = "static"

    rmtree(path_to_public)

    os.mkdir(path_to_public)


    file_paths, dir_paths = file_dir_paths(path_to_static)
    dir_paths.sort(key=lambda d_path: d_path.count("/"))


    for path in dir_paths:
        os.mkdir(os.path.join(path_to_public, os.path.relpath(path, path_to_static)))


    for path in file_paths:
        new_path = os.path.join(path_to_public, os.path.relpath(path, path_to_static))
        copy(path, new_path)





    content_path = "content"
    path_to_template = "template.html"


    generate_pages_recursive(content_path, path_to_template, path_to_public)

    #generate_pages_recursive(content_path, path_to_template, path_to_public)
    #markdown_1_path = "content/index.md"
    #destination = "public/index.html"


    #generate_page(markdown_1_path, html_temp_path, destination)


    #path_to_content = "content"
    #file_paths_blog, dir_paths_blog = file_dir_paths(path_to_content)
    #dir_paths_blog.sort(key=lambda d_path: d_path.count("/"))

    #for path in dir_paths_blog:
    #    os.mkdir(os.path.join(path_to_public, os.path.relpath(path, path_to_content)))


    #for path in file_paths_blog:
    #    new_path = os.path.join(path_to_public, os.path.relpath(path, path_to_content))
    #    generate_page(f"content/{os.path.relpath(path, path_to_content)}", html_temp_path, new_path.replace("md", "html"))



    #blog_paths = ["content/blog/contact/index.html", "content/blog/glorfindel/index.html", "content/blog/majesty/index.html", "content/blog/tom/index.html"]
    #blog_dest_paths = ["public/blog/contact/index.html", "public/blog/glorfindel/index.html", "public/blog/majesty/index.html", "public/blog/tom/index.html"]




    #for i in range(len(blog_paths)):









if __name__ == "__main__":
    main()
