from pathlib import Path

svg = """<svg width="900" height="260" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg">
<style>
  .bg { fill:#0d1117; }
  .title { font:700 24px monospace; fill:#fff; }
  .txt { font:600 15px monospace; fill:#9ca3af; }
  .pac { fill:#facc15; }
  .snake { fill:#22c55e; }
  .enemy { fill:#ef4444; }
  .heart { fill:#ef4444; font:700 20px monospace; }
  .boom { font:700 34px monospace; opacity:0; animation:boom 6s infinite; }
  .pacman { animation:movePac 6s infinite linear; }
  .snakeGroup { animation:moveSnake 6s infinite linear; }
  .enemyGroup { animation:enemyMove 6s infinite linear; }

  @keyframes movePac {
    0% { transform:translateX(0px); }
    45% { transform:translateX(290px); }
    55% { transform:translateX(290px); }
    100% { transform:translateX(0px); }
  }

  @keyframes moveSnake {
    0% { transform:translateX(0px); }
    45% { transform:translateX(-290px); }
    55% { transform:translateX(-290px); }
    100% { transform:translateX(0px); }
  }

  @keyframes enemyMove {
    0% { transform:translateY(0px); opacity:1; }
    45% { transform:translateY(60px); opacity:1; }
    55% { transform:translateY(60px); opacity:.2; }
    100% { transform:translateY(0px); opacity:1; }
  }

  @keyframes boom {
    0%,40% { opacity:0; transform:scale(.5); }
    48%,55% { opacity:1; transform:scale(1.2); }
    70%,100% { opacity:0; transform:scale(.5); }
  }
</style>

<rect class="bg" width="900" height="260" rx="18"/>

<text x="450" y="38" text-anchor="middle" class="title">Pacman vs Snake Battle</text>
<text x="450" y="62" text-anchor="middle" class="txt">Experimental SVG animation • collision • lives</text>

<text x="80" y="95" class="txt">Pacman HP</text>
<text x="80" y="122" class="heart">♥ ♥ ♥</text>

<text x="690" y="95" class="txt">Snake HP</text>
<text x="690" y="122" class="heart">♥ ♥ ♥</text>

<line x1="110" y1="170" x2="790" y2="170" stroke="#30363d" stroke-width="6" stroke-linecap="round"/>

<g class="pacman">
  <path class="pac" d="M130 170 L170 145 A45 45 0 1 1 170 195 Z"/>
  <circle cx="150" cy="155" r="5" fill="#111827"/>
</g>

<g class="snakeGroup">
  <circle class="snake" cx="770" cy="170" r="22"/>
  <circle class="snake" cx="810" cy="170" r="18"/>
  <circle class="snake" cx="845" cy="170" r="15"/>
  <circle cx="762" cy="162" r="4" fill="#111827"/>
</g>

<g class="enemyGroup">
  <rect class="enemy" x="430" y="70" width="38" height="38" rx="8"/>
  <text x="449" y="96" text-anchor="middle" fill="#fff" font-size="22">!</text>
</g>

<text x="432" y="182" class="boom">💥</text>

<text x="450" y="230" text-anchor="middle" class="txt">
  Java • Spring Boot • GitHub Actions • SVG generated automatically
</text>
</svg>
"""

Path("dist/pacman-snake-battle.svg").write_text(svg, encoding="utf-8")
