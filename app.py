from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from cofig import my_key
app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=my_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
