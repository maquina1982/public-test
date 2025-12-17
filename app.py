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
        #
