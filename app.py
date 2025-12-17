from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>DHL-Style Python Web App</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {
      --dhl-yellow: #FFCC00;
      --dhl-red: #D40511;
      --dark: #111;
      --light: #fff;
      --muted: #666;
    }

    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: #f4f4f4;
      color: #111;
    }

    header {
      background: var(--dhl-red);
      color: white;
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .logo {
      background: var(--dhl-yellow);
      color: var(--dhl-red);
      font-weight: 900;
      padding: 8px 14px;
      border-radius: 4px;
      letter-spacing: 1px;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin-left: 16px;
      font-weight: 600;
    }

    nav a:hover {
      text-decoration: underline;
    }

    .hero {
      background: linear-gradient(
        135deg,
        var(--dhl-yellow) 0%,
        #ffd633 60%,
        #fff 100%
      );
      padding: 60px 24px;
    }

    .hero h1 {
      font-size: 40px;
      margin-bottom: 10px;
      color: var(--dhl-red);
    }

    .hero p {
      font-size: 18px;
      max-width: 600px;
      color: #333;
    }

    .content {
      max-width: 1100px;
      margin: -40px auto 40px;
      padding: 24px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 24px;
    }

    .card {
      background: white;
      border-radius: 10px;
      padding: 22px;
      box-shadow: 0 8px 22px rgba(0,0,0,.1);
      border-top: 6px solid var(--dhl-red);
    }

    .card h3 {
      margin-top: 0;
      color: var(--dhl-red);
    }

    footer {
      background: #222;
      color: #ccc;
      padding: 16px;
      text-align: center;
      font-size: 14px;
    }
  </style>
</head>
<body>

<header>
  <div class="logo">DHL</div>
  <nav>
    <a href="#">Home</a>
    <a href="#">Tracking</a>
    <a href="#">Services</a>
    <a href="#">Contact</a>
  </nav>
</header>

<section class="hero">
  <h1>Fast. Global. Reliable.</h1>
  <p>
    This is a Python-powered web application running on Azure App Service,
    styled with a DHL-inspired design.
  </p>
</section>

<section class="content">
  <div class="card">
    <h3>Global Logistics</h3>
    <p>End-to-end delivery solutions across the globe.</p>
  </div>

  <div class="card">
    <h3>Tracking</h3>
    <p>Real-time shipment tracking with enterprise reliability.</p>
  </div>

  <div class="card">
    <h3>Cloud-Native</h3>
    <p>Built with Python and deployed on Azure App Service.</p>
  </div>
</section>

<footer>
  © 2025 · Python Web App Demo · DHL-style theme
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
