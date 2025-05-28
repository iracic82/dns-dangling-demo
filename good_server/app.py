from flask import Flask

app = Flask(__name__)

@app.route("/marketing.js")
def good_script():
    return """
    document.addEventListener('DOMContentLoaded', function () {
      console.log('✅ Legit content loaded from trusted MyCorp CDN.');
      document.body.innerHTML += `
        <div style='margin-top:40px; font-size:18px; color:green; text-align:center;'>
          ✅ This content was securely loaded from the trusted MyCorp CDN.
        </div>
      `;
    });
    """, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
