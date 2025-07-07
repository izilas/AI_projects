# AI_projects
First AI projects

the script requires the Ollama CLI installed and configured (ollama run mistral command).

Error handling
  Currently, if subprocess.run fails or Ollama is not installed, the script will crash silently or behave oddly.
  Consider adding try/except blocks to handle subprocess errors or timeouts.

Extensibility
Right now the model name "mistral" is hardcoded; consider allowing it as a command-line argument or config option.
Output formatting
The model output might sometimes include special tokens or formatting; you may want to clean/filter that before printing.

Prompt injection caution
Since you directly inject user input into the prompt, you may want to sanitize inputs or be aware of prompt injection risks if you ever expose this to untrusted users.

