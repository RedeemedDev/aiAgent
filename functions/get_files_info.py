import os
from functions.config import char_limit

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

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    #try: read the file content
    try:
        with open(abs_target_dir, 'r') as f:
            content = f.read()
            if len(content) > char_limit:
                content = content[:char_limit] + f'[...File "{abs_target_dir}" truncated at {char_limit} characters]'
            return content
    except Exception as e:
        return f'Error: {str(e)}'    

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_target_dir), exist_ok=True)
    
        with open(abs_target_dir, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'
    
def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target_dir):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        import subprocess
        result = subprocess.run(['python3', file_path] + args, cwd=working_directory, timeout=30, capture_output=True, text=True)
        if result.returncode != 0:
            return f'STDOUT: {result.stdout.strip()}, \nSTDERR: {result.stderr.strip()}, \nProcess exited with code {result.returncode}'
        if result.stdout == '' and result.stderr == '':
                return f'No output produced.'
        return f'STDOUT: {result.stdout.strip()}, \nSTDERR: {result.stderr.strip()}'

    except Exception as e:
        return f'Error: executing Python file: {e}'