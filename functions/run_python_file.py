import subprocess
from common.validate_path import validate_path


def run_python_file(working_directory, file_path, args=None):
    try:
        path = validate_path(working_directory, file_path)

        if not path["is_valid_target_dir"]:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not path["is_file"]:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", path["full_path"]]
        if args:
            command.extend(args)

        completed_process = subprocess.run(
            command,
            capture_output=True,
            cwd=working_directory,
            text=True,
            timeout=30,
        )

        output_string_list = []

        if completed_process.returncode != 0:
            output_string_list.append(
                f"Process exited with code {completed_process.returncode}"
            )

        if not completed_process.stdout and not completed_process.stderr:
            output_string_list.append("No output produced")

        if completed_process.stdout:
            output_string_list.append(f"STDOUT: {completed_process.stdout}")
        if completed_process.stderr:
            output_string_list.append(f"STDERR: {completed_process.stderr}")

        return "\n".join(output_string_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"
