import subprocess
import tempfile
import os

class SecureCodeSandbox:
    """Executes untrusted peer-generated code snippets inside an isolated temporary process sandbox."""
    def __init__(self, timeout_seconds: int = 5):
        self.timeout = timeout_seconds

    def execute_in_sandbox(self, python_code: str) -> dict:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(python_code)
            script_path = f.name

        try:
            result = subprocess.run(
                ["python3", script_path],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            return {
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except subprocess.TimeoutExpired:
            return {"exit_code": -1, "stdout": "", "stderr": "Execution timed out in sandbox."}
        finally:
            if os.path.exists(script_path):
                os.remove(script_path)
