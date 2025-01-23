from flask import Flask, render_template, request
from langchain_ollama import OllamaLLM

app = Flask(__name__)

# Initialize the Llama 3.2 model using langchain_ollama
llm = OllamaLLM(model="llama3.2")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        # Generate response from the model
        response = llm.invoke(user_input)
    
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
