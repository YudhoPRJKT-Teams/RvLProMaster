import subprocess
import io
import sys
import textwrap
import traceback
import ast
import asyncio
from .create_log import CreateLog
class _Terminal:
    def __init__(self):
        self.output_terminal = ''

    def Bash(self, command: str):
        try:
            """
            Run a bash command and return the output.
            """
            pr = subprocess.run(
                command,
                shell=True,
                check=True,
                text=True,
                capture_output=True,
            )

            self.output_terminal = pr.stdout or pr.stderr
            return self
        except subprocess.CalledProcessError as e:
            CreateLog("ERROR", f"{e}")
            return self

    async def Python(self, command: str):
        # Dedent input code for proper formatting
        corrected_code = textwrap.dedent(command)
        output_buffer = io.StringIO()
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = output_buffer
        sys.stderr = output_buffer

        error_message = ""
        try:
            parsed = ast.parse(corrected_code)
            last_expr = None
            if parsed.body and isinstance(parsed.body[-1], ast.Expr):
                last_expr = parsed.body.pop()
            code_body = compile(ast.Module(body=parsed.body, type_ignores=[]), filename="<input>", mode="exec")
            exec_locals = {}
            exec_globals = globals()
            exec(code_body, exec_globals, exec_locals)
            if last_expr:
                if isinstance(last_expr, ast.Expr) and hasattr(last_expr, 'value'):
                    expr_code = compile(ast.Expression(last_expr.value), filename="<input>", mode="eval")
                else:
                    raise ValueError("The last expression is not a valid AST expression with a 'value' attribute.")
                result = eval(expr_code, exec_globals, exec_locals)
                if result is not None:
                    print(repr(result))

        except Exception:
            error_message = traceback.format_exc()
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr

        return output_buffer.getvalue() + (error_message if error_message else "")


Terminal = _Terminal()
