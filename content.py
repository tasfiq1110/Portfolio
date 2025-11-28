# content.py

DATA = {
    "site": {
        "title": "MOHAMMED TASFIQUR RAHMAN | Unreal Engine Developer",
        "description": "Portfolio of an Unreal Engine game developer specializing in real-time graphics and immersive experiences.",
    },
    "hero": {
        "name": "MOHAMMED TASFIQUR RAHMAN",
        "role": "Programmer & Unreal Engine Developer",
        "tagline": "I build immersive, real-time experiences powered by Unreal Engine.",
        "summary": (
            "Passionate and skilled Game Developer with 4 years of experience in Unreal Engine, specializing in AI systems, single-player narrative games, and VR development. 	With hands-on experience in developing AAA-quality games, including projects on Steam, I possess in-depth expertise in game mechanics, optimization, and AI 	programming. My current goal is to secure a position at a leading game development company, where I can continue to work with Unreal Engine, contributing to cutting-	edge game AI, VR, and immersive gameplay systems."
        ),
 	"logo": "TR",
        "primary_cta": {
            "label": "View Projects",
            "href": "#projects",
        },
        "secondary_cta": {
            "label": "Download CV",
            "href":"/static/files/Mohammed_Tasfiqur_Rahman_CV.pdf",  # later you can point this to a PDF in /static
        },
        "socials": [
            {
                "label": "GitHub",
                "icon": "fa-brands fa-github",
                "href": "https://github.com/tasfiq1110",
            },
            {
                "label": "Facebook",
                "icon": "fa-brands fa-facebook",
                "href": "https://www.facebook.com/tasfiqur.rahman.1110",
            },
            {
                "label": "LinkedIn",
                "icon": "fa-brands fa-linkedin",
                "href": "https://www.linkedin.com/in/tasfiqur-rahman-2464a8224/",
            },
        ],
    },
    "about": {
        "title": "About Me",
        "content": [
            "I am a passionate Unreal Engine Game Developer with 4+ years of experience specializing in AI systems, single-player narrative design, VR development, and 		metaverse-focused projects. I’ve contributed to AAA-quality productions, including Steam-published titles, and have led teams in delivering optimized, 	high-	performance virtual worlds. I thrive in collaborative environments and aim to contribute to cutting-edge projects at leading game development studios.",
            "I love pushing the limits of moment-to-moment feel in interactive game worlds.",
        ],
        "highlights": [
            "4+ years working with Unreal Engine (UE4/UE5)",
            "Strong C++ and Blueprint scripting",
            "Experience with multiplayer, networking, and replication",
            "Comfortable profiling & optimizing",
        ],
    },
    "skills": {
        "title": "Skills",
        "groups": [
            {
            "name": "Game Development",
            "icon": "fa-solid fa-gamepad",
            "skills": [
                "Unreal Engine 4 / 5 (Advanced)",
                "C++ Gameplay & Systems Programming",
                "Blueprint Architecture & Tooling",
                "AI Systems (Behavior Trees, EQS, State Machines)",
                "VR Development (Meta Quest / Oculus)",
                "Single-Player Narrative Systems",
                "Multiplayer & Replication Fundamentals",
                "Level Design & World Building"
            ]
        },
            {
            "name": "Graphics & Technical Art",
            "icon": "fa-solid fa-burst",
            "skills": [
                "Niagara VFX & Particle Systems",
                "Material Editor, Shaders & Procedural Effects",
                "Lighting, Post-Processing & Cinematics",
                "Lumen / Nanite Workflow",
                "Performance Optimization & Profiling",
                "Rendering Debugging & GPU Optimization"
            ]
        },
	   {
                "name": "General & Workflow",
            "icon": "fa-solid fa-code",
            "skills": [
                "Git / GitHub / SVN",
                "Cross-Team & International Collaboration",
                "Project Leadership & Mentoring"
                ],
            },
        ],
    },
       "projects": {
        "title": "Featured Projects",
        "items": [
            {
                "name": "Project MUKTIJUDDHO (Liberation War)",
                "role": "Rajarbag Police Line",
                "description": (
                    "A  third-person action prototype featuring dynamic combat, cinematic "
                    "cameras, and reactive environments of bangaldesh liberation war."
                ),
                "tech": ["Unreal Engine 5", "C++", "Multiplayer"],
                "youtube_id": "IBL3QXyYtl8",  # <-- replace with your real video ID
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },
            {
                "name": "Project MUKTIJUDDHO (Liberation War)",
                "role": "Nokhsi BOP",
                "description": (
                    "A  third-person action prototype featuring dynamic combat, cinematic "
                    "cameras, and reactive environments of bangaldesh liberation war."
                ),
                "tech": ["Unreal Engine 4", "Blueprints", "Behavior Trees","Multiplayer"],
                "youtube_id": "rKjJ5FUsy2w",  # another ID
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },
            {
                "name": "The ghost of arena",
                "role": "Horror game",
                "description": (
                    "A immersive horror game inspired from outlast "
                  
                ),
                "tech": ["Unreal Engine", "C++"],
                "youtube_id": "KGU6wkyqFvI",
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },
	{
                "name": "Combat System",
                "role": "Immersive combat experience",
                "description": (
                    "A Simple character selection mode with combat"
                  
                ),
                "tech": ["Unreal Engine", "C++"],
                "youtube_id": "N78YzbRtNkg",
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },
	{
                "name": "Archery",
                "role": "My first demo archery",
                "description": (
                    "A simple archery mechanism"
                  
                ),
                "tech": ["Unreal Engine", "C++"],
                "youtube_id": "t-1WqyUR5ls",
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },
{
                "name": "Archery",
                "role": "My first demo Traffic system",
                "description": (
                    "A simple traffic"
                  
                ),
                "tech": ["Unreal Engine", "C++"],
                "youtube_id": "l32GTdu-mL8",
                "links": [
                    {
                        "label": "YouTube",
                        "href": "https://www.youtube.com/watch?v=8-NbT05VykQ&list=RD8-NbT05VykQ&start_radio=1",
                    }
                ],
            },

        ],
    },
    "experience": {
    "title": "Experience",
    "items": [
        {
            "company": "Future Studio Bangladesh",
            "role": "Game Developer (Unreal Engine / Metaverse & VR)",
            "period": "2024 – Present",
            "location": "Dhaka, Bangladesh",
            "details": [
                "Developing large-scale Metaverse and VR experiences using Unreal Engine 5.",
                "Building persistent virtual worlds featuring avatars, voice chat, social hubs, and virtual economies.",
                "Implementing multiplayer systems, marketplace integrations, and gamified learning environments.",
                "Collaborating with international teams to deliver networked, real-time interactive experiences."
            ]
        },
            {
            "company": "VincatsBD",
            "role": "VR Developer",
            "period": "2024 – 2024",
            "location": "Dhaka, Bangladesh / South Korea (Remote)",
            "details": [
                "Developed interactive VR experiences for Meta Quest with a strong focus on performance optimization.",
                "Created immersive environments and interaction systems using Unreal Engine.",
                "Worked with a South Korea–based team to refine VR gameplay systems and user interaction flows."
            ]
        },

	{
            "company": "SpinOFF Studio",
            "role": "Senior Game Developer & Team Lead",
            "period": "2020 – 2024",
            "location": "Dhaka, Bangladesh",
            "details": [
                "Led development of single-player narrative-focused games built in Unreal Engine.",
                "Designed advanced AI systems, quest mechanics, and narrative gameplay flow.",
                "Optimized game performance across multiple platforms and launched titles on Steam.",
                "Mentored junior developers and coordinated cross-functional teams under tight deadlines.",
                "Successfully launched a single-player narrative game on Steam with positive player reviews."
            ]
        },
        ],
    },
    "education": {
        "title": "Education",
        "items": [
            {
                "institution": "East West University, Dhaka, Bangladesh",
            "degree": "Bachelor of Science in Computer Science and Engineering (B.Sc.)",
            "period": "2020 – 2024",
            "details": [
                "Completed coursework in programming, software engineering, algorithms, and computer graphics.",
                "Studied game development foundations and worked on multiple Unreal Engine projects during academic years."
            ],
            }
        ],
    },
    "contact": {
        "title": "Contact",
        "subtitle": "Let’s build something immersive.",
        "email": "tasfiqur1110@gmail.com",
        "location": "Dhaka, Bangladesh",
        "availability": "Open to full-time, contract, and remote work.",
        "note": "",
    },
}


