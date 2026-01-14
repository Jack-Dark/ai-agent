import subprocess
from common.validate_path import validate_path
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path path to read from file, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional args",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="FUCK IF I KNOW",
                ),
            ),
        },
        required=["file_path"],
    ),
)


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
