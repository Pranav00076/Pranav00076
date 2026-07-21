import os
import math
import random

os.makedirs('assets', exist_ok=True)

DEFS = """
<defs>
    <linearGradient id="aurora1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#9d4edd" stop-opacity="0.3">
            <animate attributeName="stop-color" values="#9d4edd;#00f2fe;#9d4edd" dur="5s" repeatCount="indefinite" />
        </stop>
        <stop offset="100%" stop-color="#00f2fe" stop-opacity="0.1" />
    </linearGradient>
    <linearGradient id="aurora2" x1="100%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#f72585" stop-opacity="0.2">
            <animate attributeName="stop-color" values="#f72585;#4cc9f0;#f72585" dur="7s" repeatCount="indefinite" />
        </stop>
        <stop offset="100%" stop-color="#4cc9f0" stop-opacity="0.05" />
    </linearGradient>
    
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="4" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-heavy" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="15" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
</defs>
"""

STYLE = """
<style>
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    @keyframes float-delay {
        0% { transform: translateY(0px); }
        50% { transform: translateY(10px); }
        100% { transform: translateY(0px); }
    }
    @keyframes pulse {
        0% { opacity: 0.7; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); }
        100% { opacity: 0.7; transform: scale(1); }
    }
    .glass {
        fill: rgba(255, 255, 255, 0.04);
        stroke: rgba(255, 255, 255, 0.1);
        stroke-width: 1;
    }
    .glass-dark {
        fill: rgba(0, 0, 0, 0.4);
        stroke: rgba(255, 255, 255, 0.15);
        stroke-width: 1;
    }
    .text-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-weight: 800;
        font-size: 58px;
        fill: #ffffff;
    }
    .text-subtitle {
        font-family: system-ui, -apple-system, sans-serif;
        font-weight: 600;
        font-size: 26px;
        fill: #e2e8f0;
    }
    .text-mono {
        font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
        font-size: 16px;
        fill: #00ffcc;
    }
    .text-body {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 15px;
        fill: #94a3b8;
    }
    @keyframes rotate { 100% { transform: rotate(360deg); } }
    @keyframes reverse-rotate { 100% { transform: rotate(-360deg); } }
    @keyframes slide-right {
        0% { transform: translateX(0); opacity: 1; }
        20% { transform: translateX(0); opacity: 1; }
        25% { transform: translateX(50px); opacity: 0; }
        95% { transform: translateX(-50px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
</style>
"""

def make_hero():
    particles = ""
    for _ in range(60):
        x = random.randint(0, 1000)
        y = random.randint(0, 450)
        r = random.uniform(1, 3.5)
        delay = random.uniform(0, 5)
        dur = random.uniform(4, 9)
        color = random.choice(["#9d4edd", "#00f2fe", "#f72585", "#ffffff"])
        particles += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="0.5" style="animation: float {dur}s ease-in-out {delay}s infinite" filter="url(#glow)" />'

    roles = ["AI Engineer", "Full Stack Developer", "Open Source Builder", "Automation Enthusiast", "LLM Explorer"]
    subtitle_anims = ""
    for i, role in enumerate(roles):
        delay = i * 4
        # CSS animation for sliding out and in each role
        subtitle_anims += f'''
        <g style="animation: slide-right {len(roles)*4}s {delay}s infinite; opacity: 0">
            <text y="30" class="text-subtitle" text-anchor="middle">{role}</text>
        </g>
        '''

    svg = f"""
    <svg width="1000" height="450" viewBox="0 0 1000 450" xmlns="http://www.w3.org/2000/svg">
        {DEFS}
        {STYLE}
        <rect width="100%" height="100%" fill="#09090b" />
        <rect width="100%" height="100%" fill="url(#aurora1)" />
        <rect width="100%" height="100%" fill="url(#aurora2)" />
        <g>{particles}</g>
        
        <g transform="translate(500, 180)" text-anchor="middle">
            <text y="-20" class="text-title" filter="url(#glow)">PRANAV THAWAIT</text>
            <g style="animation: pulse 4s infinite">
                {subtitle_anims}
            </g>
            
            <g transform="translate(-300, 90)">
                <rect x="0" y="0" width="600" height="65" rx="12" class="glass-dark" />
                <circle cx="25" cy="32.5" r="6" fill="#ff5f56" />
                <circle cx="45" cy="32.5" r="6" fill="#ffbd2e" />
                <circle cx="65" cy="32.5" r="6" fill="#27c93f" />
                <text x="95" y="38" class="text-mono" text-anchor="start">> whoami</text>
                <text x="195" y="38" class="text-mono" fill="#cbd5e1" text-anchor="start">Building intelligent software powered by AI</text>
                <line x1="565" y1="22" x2="565" y2="43" stroke="#00ffcc" stroke-width="2">
                    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
                </line>
            </g>
        </g>
    </svg>
    """
    with open('assets/hero.svg', 'w') as f:
        f.write(svg)

def make_status():
    svg = f"""
    <svg width="1000" height="280" viewBox="0 0 1000 280" xmlns="http://www.w3.org/2000/svg">
        {DEFS}
        {STYLE}
        <rect width="100%" height="100%" fill="#09090b" />
        <rect width="100%" height="100%" fill="url(#aurora1)" opacity="0.3" />
        
        <g transform="translate(40, 20)">
            <rect x="0" y="0" width="920" height="240" rx="16" class="glass" />
            <text x="40" y="50" class="text-title" font-size="22" fill="#ffffff">LIVE STATUS</text>
            <line x1="40" y1="70" x2="880" y2="70" stroke="rgba(255,255,255,0.1)" />
            
            <text x="40" y="110" class="text-mono" fill="#94a3b8">Currently Building: <tspan fill="#00ffcc">PromptForge</tspan></text>
            <text x="40" y="150" class="text-mono" fill="#94a3b8">Latest Project: <tspan fill="#f72585">Local AI</tspan></text>
            <text x="40" y="190" class="text-mono" fill="#94a3b8">Latest Package: <tspan fill="#ffffff">PromptForge</tspan></text>
            
            <text x="480" y="110" class="text-mono" fill="#94a3b8">Learning: <tspan fill="#00ffcc">AI Agents</tspan></text>
            <text x="480" y="150" class="text-mono" fill="#94a3b8">Open Source: <tspan fill="#27c93f">Active</tspan></text>
            <text x="480" y="190" class="text-mono" fill="#94a3b8">Coffee Level: <tspan fill="#ffbd2e">██████████ 100%</tspan></text>
        </g>
    </svg>
    """
    with open('assets/status.svg', 'w') as f:
        f.write(svg)

def make_tech():
    techs = ["Python", "TypeScript", "React", "Next.js", "Node.js", "LangChain", "OpenAI", "Ollama", "Docker", "Supabase", "Firebase", "Tailwind"]
    radius = 200
    center_x, center_y = 500, 300
        
    svg = f"""
    <svg width="1000" height="600" viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
        {DEFS}
        {STYLE}
        <rect width="100%" height="100%" fill="#09090b" />
        <rect width="100%" height="100%" fill="url(#aurora2)" opacity="0.2" />
        
        <text x="500" y="60" class="text-title" font-size="36" text-anchor="middle" filter="url(#glow)">TECH ECOSYSTEM</text>
        
        <!-- Orbits -->
        <circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.5" stroke-dasharray="4 6" />
        <circle cx="{center_x}" cy="{center_y}" r="{radius+80}" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="1" />
        
        <!-- AI Core -->
        <g transform="translate({center_x}, {center_y})">
            <circle cx="0" cy="0" r="60" fill="url(#aurora1)" filter="url(#glow-heavy)" style="animation: pulse 3s infinite" />
            <circle cx="0" cy="0" r="45" fill="#09090b" />
            <text x="0" y="6" font-family="system-ui" font-weight="800" font-size="18" fill="#00ffcc" text-anchor="middle">AI CORE</text>
        </g>
        
        <g transform="translate({center_x},{center_y})">
            <g style="animation: rotate 60s linear infinite">
"""
    for i, t in enumerate(techs):
        angle = (i / len(techs)) * 2 * math.pi
        cx = radius * math.cos(angle)
        cy = radius * math.sin(angle)
        svg += f'''
                <g transform="translate({cx}, {cy})">
                    <g style="animation: reverse-rotate 60s linear infinite">
                        <circle cx="0" cy="0" r="40" class="glass-dark" filter="url(#glow)" />
                        <text x="0" y="5" font-family="system-ui" font-size="12" fill="#ffffff" font-weight="bold" text-anchor="middle">{t}</text>
                    </g>
                </g>
'''
    svg += f"""
            </g>
        </g>
    </svg>
    """
    with open('assets/tech.svg', 'w') as f:
        f.write(svg)

def make_projects():
    projects = [
        ("PromptForge", "AI Prompt Engineering Studio", ["Next.js", "OpenAI"]),
        ("Local AI", "Private RAG Assistant", ["Python", "Ollama", "Chroma"]),
        ("ConferAI", "Real-time conferencing", ["Node.js", "WebSockets"]),
        ("Omnikon", "Organization Website", ["React", "Firebase"]),
        ("Code-9", "Community Website", ["React", "Tailwind"]),
        ("AI Business Suite", "Automation Workflows", ["n8n", "Airtable"])
    ]
    cards = ""
    for i, (title, desc, tags) in enumerate(projects):
        x = 50 + (i % 2) * 460
        y = 120 + (i // 2) * 160
        
        tags_svg = ""
        for j, tag in enumerate(tags):
            tags_svg += f'''
            <rect x="{24 + j * 80}" y="95" width="70" height="24" rx="12" fill="rgba(0,255,204,0.08)" stroke="#00ffcc" stroke-width="0.8" />
            <text x="{59 + j * 80}" y="111" font-family="system-ui" font-weight="600" font-size="11" fill="#00ffcc" text-anchor="middle">{tag}</text>
            '''
            
        anim = "float" if i % 2 == 0 else "float-delay"
        
        cards += f'''
        <g transform="translate({x}, {y})">
            <g style="animation: {anim} {6 + i*0.5}s ease-in-out infinite">
                <rect x="0" y="0" width="440" height="140" rx="16" class="glass" />
                <rect x="0" y="0" width="440" height="140" rx="16" fill="none" stroke="url(#aurora1)" stroke-width="1" />
                <text x="24" y="45" font-family="system-ui" font-weight="800" font-size="24" fill="#ffffff">{title}</text>
                <text x="24" y="75" class="text-body">{desc}</text>
                {tags_svg}
            </g>
        </g>
        '''
        
    svg = f"""
    <svg width="1000" height="650" viewBox="0 0 1000 650" xmlns="http://www.w3.org/2000/svg">
        {DEFS}
        {STYLE}
        <rect width="100%" height="100%" fill="#09090b" />
        <rect width="100%" height="100%" fill="url(#aurora1)" opacity="0.1" />
        
        <text x="500" y="60" class="text-title" font-size="36" text-anchor="middle" filter="url(#glow)">PROJECT SHOWCASE</text>
        <text x="500" y="90" class="text-body" text-anchor="middle">Building scalable intelligence and real-world systems.</text>
        
        {cards}
    </svg>
    """
    with open('assets/projects.svg', 'w') as f:
        f.write(svg)
        
def make_footer():
    svg = f"""
    <svg width="1000" height="200" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg">
        {DEFS}
        {STYLE}
        <rect width="100%" height="100%" fill="#09090b" />
        <path d="M0,100 Q250,50 500,100 T1000,100 L1000,200 L0,200 Z" fill="url(#aurora2)" opacity="0.3">
            <animate attributeName="d" values="M0,100 Q250,50 500,100 T1000,100 L1000,200 L0,200 Z;M0,100 Q250,150 500,100 T1000,100 L1000,200 L0,200 Z;M0,100 Q250,50 500,100 T1000,100 L1000,200 L0,200 Z" dur="10s" repeatCount="indefinite" />
        </path>
        <path d="M0,120 Q250,170 500,120 T1000,120 L1000,200 L0,200 Z" fill="url(#aurora1)" opacity="0.4">
            <animate attributeName="d" values="M0,120 Q250,170 500,120 T1000,120 L1000,200 L0,200 Z;M0,120 Q250,70 500,120 T1000,120 L1000,200 L0,200 Z;M0,120 Q250,170 500,120 T1000,120 L1000,200 L0,200 Z" dur="8s" repeatCount="indefinite" />
        </path>
        <text x="500" y="160" class="text-title" font-size="24" text-anchor="middle" filter="url(#glow)">SYSTEM.EXIT()</text>
    </svg>
    """
    with open('assets/footer.svg', 'w') as f:
        f.write(svg)

if __name__ == "__main__":
    make_hero()
    make_status()
    make_tech()
    make_projects()
    make_footer()
    print("SVGs generated successfully in assets/")
