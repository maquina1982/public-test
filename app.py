from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Expert Services | Modern Strategy & Execution</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b1020;
      --bg-soft: #121a34;
      --panel: rgba(255, 255, 255, 0.06);
      --text: #eaf0ff;
      --muted: #b3bfdc;
      --primary: #5eead4;
      --secondary: #7c3aed;
      --accent: #60a5fa;
      --ring: rgba(94, 234, 212, 0.45);
      --maxw: 1120px;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 15% 15%, rgba(124, 58, 237, 0.25), transparent 40%),
        radial-gradient(circle at 80% 0%, rgba(96, 165, 250, 0.25), transparent 35%),
        linear-gradient(150deg, #070b18, var(--bg) 35%, #0d1530 100%);
      min-height: 100vh;
      line-height: 1.55;
    }

    .container {
      width: min(var(--maxw), 92%);
      margin: 0 auto;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
      background: rgba(11, 16, 32, 0.75);
      border-bottom: 1px solid rgba(255,255,255,.08);
    }

    .nav-wrap {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 0;
    }

    .brand {
      font-weight: 800;
      letter-spacing: .4px;
      display: inline-flex;
      align-items: center;
      gap: .55rem;
      font-size: 1.05rem;
    }

    .dot {
      width: 12px;
      height: 12px;
      border-radius: 999px;
      background: linear-gradient(120deg, var(--primary), var(--secondary));
      box-shadow: 0 0 0 6px rgba(94, 234, 212, 0.15);
    }

    nav a {
      color: var(--muted);
      text-decoration: none;
      margin-left: 1.2rem;
      font-weight: 600;
      transition: .2s ease;
    }

    nav a:hover { color: var(--text); }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      border-radius: 12px;
      padding: 0.75rem 1.05rem;
      font-weight: 700;
      border: 1px solid transparent;
      transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
    }

    .btn-primary {
      background: linear-gradient(120deg, var(--primary), var(--accent));
      color: #06201c;
      box-shadow: 0 10px 30px rgba(94, 234, 212, 0.25);
    }

    .btn-primary:hover { transform: translateY(-2px); }

    .btn-ghost {
      color: var(--text);
      border-color: rgba(255,255,255,.22);
      background: rgba(255,255,255,.02);
    }

    .hero {
      padding: 88px 0 42px;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.1fr .9fr;
      gap: 28px;
      align-items: stretch;
    }

    .eyebrow {
      color: var(--primary);
      font-weight: 700;
      letter-spacing: .07em;
      text-transform: uppercase;
      font-size: .79rem;
    }

    h1 {
      font-size: clamp(2rem, 4.6vw, 4rem);
      line-height: 1.05;
      margin: 12px 0 16px;
      letter-spacing: -0.03em;
    }

    .lead {
      color: var(--muted);
      font-size: 1.07rem;
      max-width: 60ch;
    }

    .hero-actions {
      margin-top: 26px;
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    .metrics {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-top: 28px;
    }

    .metric {
      background: var(--panel);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 14px;
      padding: 14px;
    }

    .metric strong { font-size: 1.2rem; display: block; }
    .metric span { color: var(--muted); font-size: .88rem; }

    .feature-panel {
      background: linear-gradient(160deg, rgba(124,58,237,.23), rgba(96,165,250,.16));
      border: 1px solid rgba(255,255,255,.12);
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 18px 60px rgba(0,0,0,.28);
      display: grid;
      gap: 16px;
      align-content: center;
    }

    .feature {
      background: rgba(7, 11, 24, .48);
      border: 1px solid rgba(255,255,255,.09);
      border-radius: 14px;
      padding: 14px;
    }

    .feature h3 { margin: 0 0 6px; font-size: 1rem; }
    .feature p { margin: 0; color: var(--muted); font-size: .92rem; }

    .section { padding: 28px 0 70px; }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
    }

    .card {
      background: var(--panel);
      border: 1px solid rgba(255,255,255,.09);
      border-radius: 16px;
      padding: 20px;
    }

    .card h4 { margin: 0 0 8px; }
    .card p { margin: 0; color: var(--muted); }

    footer {
      border-top: 1px solid rgba(255,255,255,.08);
      color: var(--muted);
      text-align: center;
      padding: 18px;
      font-size: .9rem;
    }

    @media (max-width: 900px) {
      .hero-grid { grid-template-columns: 1fr; }
      nav { display: none; }
    }
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <div class="brand"><span class="dot"></span> Your Name · Expert Consulting</div>
      <nav>
        <a href="#services">Services</a>
        <a href="#results">Results</a>
        <a href="#approach">Approach</a>
      </nav>
      <a class="btn btn-primary" href="#contact">Book a Call</a>
    </div>
  </header>

  <main>
    <section class="hero container">
      <div class="hero-grid">
        <div>
          <div class="eyebrow">Built for ambitious teams</div>
          <h1>Turn your expertise into premium client demand.</h1>
          <p class="lead">
            I help founders and operators clarify their offer, position their value, and execute a modern go-to-market
            strategy that drives measurable growth.
          </p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#contact">Start Your Project</a>
            <a class="btn btn-ghost" href="#results">See Case Studies</a>
          </div>

          <div class="metrics" id="results">
            <div class="metric"><strong>120+</strong><span>Engagements delivered</span></div>
            <div class="metric"><strong>94%</strong><span>Client retention rate</span></div>
            <div class="metric"><strong>3.2x</strong><span>Average ROI uplift</span></div>
          </div>
        </div>

        <aside class="feature-panel" id="approach">
          <div class="feature">
            <h3>Strategic Positioning</h3>
            <p>Differentiate your offer so premium clients instantly understand your value.</p>
          </div>
          <div class="feature">
            <h3>Revenue Systems</h3>
            <p>Build repeatable acquisition and conversion systems that scale with confidence.</p>
          </div>
          <div class="feature">
            <h3>Execution Partnership</h3>
            <p>Get senior-level support from strategy through implementation.</p>
          </div>
        </aside>
      </div>
    </section>

    <section class="section container" id="services">
      <div class="cards">
        <article class="card">
          <h4>Offer Design</h4>
          <p>Create high-value service packages aligned to your best-fit clients.</p>
        </article>
        <article class="card">
          <h4>Authority Marketing</h4>
          <p>Build trust with modern content, social proof, and demand-generation campaigns.</p>
        </article>
        <article class="card">
          <h4>Sales Enablement</h4>
          <p>Streamline your pipeline with messaging, objections handling, and conversion assets.</p>
        </article>
        <article class="card" id="contact">
          <h4>Private Advisory</h4>
          <p>One-on-one advisory for leaders who want rapid, focused execution and outcomes.</p>
        </article>
      </div>
    </section>
  </main>

  <footer>
    © 2026 · Your Name Consulting · Built to convert expertise into growth.
  </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
