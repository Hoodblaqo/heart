
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Neon Heart</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    background: radial-gradient(circle, #260018, #050008 70%);
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    font-family: Arial, sans-serif;
    color: white;
}

.container {
    text-align: center;
    z-index: 2;
}

.heart {
    font-size: 130px;
    color: #ff174f;
    animation: heartbeat 1s infinite;
    filter: drop-shadow(0 0 15px #ff174f)
            drop-shadow(0 0 45px #ff174f);
}

h1 {
    margin-top: 30px;
    font-size: 28px;
    letter-spacing: 5px;
    text-shadow: 0 0 15px #ff174f;
}

p {
    margin-top: 12px;
    color: #ff8ca9;
    letter-spacing: 3px;
    font-size: 12px;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.25); }
    30% { transform: scale(1); }
    45% { transform: scale(1.15); }
    60% { transform: scale(1); }
}

.particle {
    position: absolute;
    bottom: -20px;
    color: #ff174f;
    animation: float 7s linear infinite;
    opacity: 0;
}

@keyframes float {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }
    20% { opacity: 0.8; }
    100% {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>
</head>
<body>

<div class="container">
    <div class="heart">♥</div>
    <h1>BEATING HEART</h1>
    <p>MADE WITH LOVE</p>
</div>

<script>
function createParticle() {
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.innerHTML = "♥";
    particle.style.left = Math.random() * 100 + "vw";
    particle.style.fontSize = (10 + Math.random() * 20) + "px";
    particle.style.animationDuration = (4 + Math.random() * 5) + "s";

    document.body.appendChild(particle);

    setTimeout(() => particle.remove(), 9000);
}

setInterval(createParticle, 250);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
