
import os

def file_dir_paths(directory):
    paths = []
    dir_paths = []
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            paths.append(os.path.join(directory, path))
        if os.path.isdir(os.path.join(directory, path)):
            dir_paths.append(os.path.join(directory, path))
            p1, d1 = file_dir_paths(os.path.join(directory, path))
            paths.extend(p1)
            dir_paths.extend(d1)
    #sorted_dir_paths = dir_paths.sort(key=lambda d_path: d_path.count("/"))

    return paths, dir_paths




"""
'''
def all_paths(directory):
    file_paths = []
    dir_paths = []

    if len(os.listdir(directory)) == 0:
        print("Directory is empty")

    for path in os.listdir(directory):
        if os.path.isfile(f"{directory}/{path}"):
            file_paths.append(f"{directory}/{path}")
        else:
            dir_paths.append(f"{directory}/{path}")
            fp1 , dp1 = all_paths(f"{directory}/{path}")
            file_paths.extend(fp1)
            dir_paths.extend(dp1)


    final_paths = list(set(file_paths))
    final_dir_paths = list(set(dir_paths))

    return final_paths, final_dir_paths


'''



#dir_paths = list(set(["/".join(path.split("/")[:-1]) for path in list_file_paths]))




'''
def remove_all_files(delete_directory):
    file_paths, dir_paths = all_paths(delete_directory)

    if len(file_paths) > 0:
        for path in file_paths:
            os.remove(path)
    if len(dir_paths) > 0:
        for path in dir_paths:
            os.path.rmdir(path)
            print(f"removing {path}")
    #    os.rmdir(path)

'''

all_paths("/Users/furnesjobb/workspace/github.com/Static-site-generator/public")















'''
def remove_files(dir_to_delete_from, ls_files):
    if len(ls_files) == 0:
        return "Recursion done"
    path_ = f"{dir_to_delete_from}/{ls_files[0]}"
    print(path_)
    if os.path.isfile(path_):
        print(f"Removing File {ls_files[0]}")
        os.remove(path_)
        return remove_files(dir_to_delete_from, ls_files[1:])

    if os.path.isdir(path_):
        if len(os.listdir(path_)) == 0:
            os.rmdir(path_)
            print(f"Removing dir {ls_files[0]}")
            return remove_files(dir_to_delete_from, ls_files[1:])
        else:
            ls_files.extend([ls_files[0] + "/" + x for x in os.listdir(path_)])
            #ls_files.extend(list(map(lambda x: f"{ls_files[0]}/{x}"), os.listdir(path_)))
            ls_files.append(ls_files[0])
            print(ls_files)
            return remove_files(dir_to_delete_from, ls_files[1:])
        return f"{ls_files[0]} removed"
    return "This shouldn ever return we failed", f"{dir_to_delete_from}/{ls_files[0]}"
remove_files("/Users/furnesjobb/workspace/github.com/Static-site-generator/public", os.listdir("/Users/furnesjobb/workspace/github.com/Static-site-generator/public"))
'''

'''
def all_paths(directory_path, all_file_paths = [], all_dir_paths = []):
    all_file_paths.extend([directory_path + "/" + x for x in os.listdir(directory_path)])
    only_files =[]
    for path in all_file_paths:
        if os.path.isdir(path):
            all_dir_paths.append(path)
            all_file_paths.remove(path)

            dir_paths = all_dir_paths.copy()
            file_paths = all_file_paths.copy()

            return all_paths(path, file_paths, dir_paths)
        else:
            only_files.append(path)

    final_file_paths = list(set(only_files))
    final_dir_paths = list(set(all_dir_paths))

    return final_file_paths, final_dir_paths
'''




'''
def all_paths(directory_path, all_file_paths = [], all_dir_paths = []):
    all_paths_in_directory = ([directory_path + "/" + x for x in os.listdir(directory_path)])
    for path in all_paths_in_directory:
        if os.path.isfile(path):
            all_file_paths.append(path)

        if os.path.isdir(path):
            all_dir_paths.append(path)


    for dir_path in all_dir_paths:
        return all_paths(dir_path, all_file_paths, None)

    final_file_paths = list(set(all_file_paths))
    final_dir_paths = list(set(all_dir_paths))

    return final_file_paths, final_dir_paths



def delete_all_files(directory_to_delete_from):
    if len(os.listdir(directory_to_delete_from)) == 0:
        return "No files in directory"
    file_paths_del, dir_paths_del = all_paths(directory_to_delete_from)
    for file_path in file_paths_del:
        os.remove(file_path)


    if len(dir_paths_del) != 0:
        dir_paths_del.sort(key=lambda x: x.count("/"), reverse=True)

        for dir_path in dir_paths_del:
            os.rmdir(dir_path)

    return "Finished deleting all files"

    #if len(os.listdir(directory_to_delete_from)) == 0:
    #    return "All files and folders are deleted"
    #else:
    #    return "Failed to delete all files"






def copy_all_directories(from_directory, to_directory):
    from_file_paths, from_dir_paths = all_paths(from_directory)

    #to_file_paths = [to_directory + path[len(from_directory):] for path in from_file_paths]
    to_dir_paths = [to_directory + path[len(from_directory):] for path in from_dir_paths]


    to_dir_paths.sort(key=lambda x: x.count("/"))

    for dir in to_dir_paths:
        os.mkdir(dir)

    return "All folders copied"




def copy_all_files(from_directory, to_directory):
    from_file_paths, from_dir_paths = all_paths(from_directory)

    to_file_paths = [to_directory + path[len(from_directory):] for path in from_file_paths]
    #to_dir_paths = [to_directory + path[len(from_directory):] for path in from_dir_paths]

    print(to_file_paths)





    for i in range(len(to_file_paths)):
        print(from_file_paths[i])
        print(to_file_paths[i])
        shutil.copy(from_file_paths[i], to_file_paths[i])

    return "All files copied"
    #for i in range(len(to_file_paths)):
    #    shutil.copy(from_file_paths[i], to_file_paths[i])
'''

"""
