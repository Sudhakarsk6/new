from dotenv import load_dotenv
from google import genai
from pathlib import Path
load_dotenv()
source_file = "C:\\Users\\Indrani\\Desktop\\Python_Project_1\\streamlit_app.py"
code = Path(source_file).read_text(encoding='utf-8')
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Write 3 test cases for the following code:\n\n" + code
)
print(interaction.output_text)
