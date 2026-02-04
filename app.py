# from flask import Flask, request, jsonify, render_template
# from google import genai
# #
# import os

# app = Flask(__name__)

# client = genai.Client(api_key=os.getenv("AIzaSyCNiSCeA92P7P8yFVBrC7UvsKIgVpg5yk0"))

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()

#     if not data or "message" not in data:
#         return jsonify({"reply": "No message received"}), 400

#     user_msg = data["message"]


#     try:
#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=user_msg
#         )

#         return jsonify({"reply": response.text})

#     except Exception as e:
#         return jsonify({"reply": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
#=======================================


from flask import Flask, request, jsonify, render_template
from groq import Groq
import os

app = Flask(__name__)

# create Groq client
client = Groq(
    api_key="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"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_msg = data["message"]

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
