import os
from flask import Flask, send_file, Response
import numpy as np

# Use a non-interactive backend for servers
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

APP_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_PATH = os.path.join(APP_DIR, "solarsystem.gif")

app = Flask(__name__)

def generate_solar_system_gif(path: str, fps: int = 30, seconds: int = 12) -> None:
    """
    Generates a simple 2D solar system animation as a GIF.
    Orbits are circular and not to scale (for visibility).
    """
    # "Not to scale" orbital radii (AU-ish) but compressed for a nice view
    planets = [
        {"name": "Mercury", "r": 0.39, "period_days": 88,   "size": 18},
        {"name": "Venus",   "r": 0.72, "period_days": 225,  "size": 22},
        {"name": "Earth",   "r": 1.00, "period_days": 365,  "size": 24},
        {"name": "Mars",    "r": 1.52, "period_days": 687,  "size": 20},
        {"name": "Jupiter", "r": 5.20, "period_days": 4333, "size": 40},
        {"name": "Saturn",  "r": 9.58, "period_days": 10759,"size": 36},
        {"name": "Uranus",  "r": 19.2, "period_days": 30687,"size": 30},
        {"name": "Neptune", "r": 30.1, "period_days": 60190,"size": 30},
    ]

    # Scale radii down so outer planets fit nicely
    scale = 0.35
    for p in planets:
        p["r_scaled"] = p["r"] * scale

    frames = fps * seconds
    t = np.linspace(0, seconds, frames)

    fig, ax = plt.subplots(figsize=(7, 7), dpi=120)
    ax.set_aspect("equal", "box")
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    # Plot orbits
    max_r = max(p["r_scaled"] for p in planets) * 1.15
    ax.set_xlim(-max_r, max_r)
    ax.set_ylim(-max_r, max_r)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("2D Solar System (Python-generated animation)", color="white", pad=12)

    # Sun
    sun = ax.scatter([0], [0], s=120, marker="o")
    sun.set_color("yellow")

    # Orbit lines + planet points
    orbit_lines = []
    planet_pts = []
    labels = []

    theta = np.linspace(0, 2*np.pi, 400)
    for p in planets:
        r = p["r_scaled"]
        (line,) = ax.plot(r*np.cos(theta), r*np.sin(theta), linewidth=0.6)
        line.set_color("gray")
        line.set_alpha(0.45)
        orbit_lines.append(line)

        pt = ax.scatter([r], [0], s=p["size"], marker="o")
        planet_pts.append(pt)

        txt = ax.text(r, 0, f" {p['name']}", color="white", fontsize=8, va="center")
        labels.append(txt)

    # Simple angular speed model: omega ∝ 1/period
    # Use a multiplier so motion is visible in short animation.
    speed = 25.0  # higher => faster orbits in the animation

    def update(frame_idx: int):
        tt = t[frame_idx]
        for i, p in enumerate(planets):
            r = p["r_scaled"]
            omega = speed * (2*np.pi / p["period_days"])
            ang = omega * tt

            x = r * np.cos(ang)
            y = r * np.sin(ang)

            planet_pts[i].set_offsets([x, y])
            labels[i].set_position((x, y))
        return planet_pts + labels

    anim = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

    # Save GIF
    writer = PillowWriter(fps=fps)
    anim.save(path, writer=writer)
    plt.close(fig)

def ensure_gif():
    # Generate once on startup (or regenerate if missing)
    if not os.path.exists(GIF_PATH):
        generate_solar_system_gif(GIF_PATH)

@app.get("/")
def index():
    ensure_gif()
    html = f"""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Solar System (2D, Python)</title>
        <style>
          body {{ background: #000; color: #fff; font-family: Arial, sans-serif; text-align: center; }}
          .wrap {{ max-width: 900px; margin: 40px auto; }}
          img {{ max-width: 100%; height: auto; border: 1px solid #333; border-radius: 10px; }}
          a {{ color: #9cf; }}
        </style>
      </head>
      <body>
        <div class="wrap">
          <h1>2D Solar System (Python-generated animation)</h1>
          <p>This animation is generated server-side using Python (matplotlib) and served as a GIF.</p>
          <img src="/solarsystem.gif" alt="Solar system animation" />
          <p><a href="/regen">Regenerate animation</a></p>
        </div>
      </body>
    </html>
    """
    return Response(html, mimetype="text/html")

@app.get("/solarsystem.gif")
def solarsystem_gif():
    ensure_gif()
    return send_file(GIF_PATH, mimetype="image/gif", max_age=3600)

@app.get("/regen")
def regen():
    # Force regeneration
    generate_solar_system_gif(GIF_PATH)
    return Response("Regenerated. Go back to /", mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
