
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="your-api-key-here")  # Replace with your actual key

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        report_text = request.form["report"]
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant who explains medical reports in plain language."},
                    {"role": "user", "content": report_text}
                ]
            )
            summary = response.choices[0].message.content
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
