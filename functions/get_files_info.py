import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        items = os.listdir(abs_target_dir)
    except Exception as e:
        return f'Error: {str(e)}'
        
    files_info = []
    for entry in items:
        entry_path = os.path.join(abs_target_dir, entry)
        try:
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path)
            files_info.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        except Exception as e:
            files_info.append(f"- {entry}: Error: {str(e)}")
    return "\n".join(files_info)