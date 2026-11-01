#!/usr/bin/env python3
import os, json, datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = json.load(open("source.json"))
meta = json.load(open("meta.json"))

TITLES = {
    "facebook/react": "React",
    "react/react": "React",
    "redis/redis": "Redis",
    "nginx/nginx": "NGINX",
    "PowerShell/PowerShell": "PowerShell",
    "ventoy/Ventoy": "Ventoy",
    "microsoft/vscode": "VS Code",
    "vuejs/core": "Vue 3",
    "git/git": "Git",
    "postgres/postgres": "PostgreSQL",
    "moby/moby": "Docker Engine",
    "torvalds/linux": "Linux Kernel",
    "FFmpeg/FFmpeg": "FFmpeg",
    "videolan/vlc": "VLC",
    "mpv-player/mpv": "mpv",
    "jellyfin/jellyfin": "Jellyfin",
    "AUTOMATIC1111/stable-diffusion-webui": "Stable Diffusion WebUI",
    "open-webui/open-webui": "Open WebUI",
    "Comfy-Org/ComfyUI": "ComfyUI",
    "vercel/next.js": "Next.js",
    "axios/axios": "Axios",
    "ohmyzsh/ohmyzsh": "Oh My Zsh",
    "BurntSushi/ripgrep": "ripgrep",
    "cli/cli": "GitHub CLI",
    "shadcn-ui/ui": "shadcn/ui",
    "pandas-dev/pandas": "pandas",
    "jupyter/notebook": "Jupyter Notebook",
    "n8n-io/n8n": "n8n",
    "Stirling-Tools/Stirling-PDF": "Stirling PDF",
    "laurent22/joplin": "Joplin",
    "CorentinTh/it-tools": "IT-Tools",
    "hoppscotch/hoppscotch": "Hoppscotch",
    "GNOME/gimp": "GIMP",
    "inkscape/inkscape": "Inkscape",
    "jgraph/drawio": "draw.io",
    "GoogleChromeLabs/squoosh": "Squoosh",
    "obsproject/obs-studio": "OBS Studio",
    "HandBrake/HandBrake": "HandBrake",
    "keepassxreboot/keepassxc": "KeePassXC",
    "bitwarden/clients": "Bitwarden",
    "signalapp/Signal-Desktop": "Signal Desktop",
    "veracrypt/VeraCrypt": "VeraCrypt",
    "tmux/tmux": "tmux",
    "microsoft/terminal": "Windows Terminal",
    "nushell/nushell": "Nushell",
    "aristocratos/btop": "btop",
    "Ventoy/Ventoy": "Ventoy",
    "pbatard/rufus": "Rufus",
    "hashcat/hashcat": "Hashcat",
    "wireshark/wireshark": "Wireshark",
    "OpenVPN/openvpn": "OpenVPN",
    "tailscale/tailscale": "Tailscale",
    "penpot/penpot": "Penpot",
    "excalidraw/excalidraw": "Excalidraw",
    "tldraw/tldraw": "tldraw",
    "blender/blender": "Blender",
    "KDE/kdenlive": "Kdenlive",
    "yt-dlp/yt-dlp": "yt-dlp",
    "logseq/logseq": "Logseq",
    "AppFlowy-IO/AppFlowy": "AppFlowy",
    "pocketbase/pocketbase": "PocketBase",
    "duckdb/duckdb": "DuckDB",
    "ClickHouse/ClickHouse": "ClickHouse",
    "apache/superset": "Apache Superset",
    "metabase/metabase": "Metabase",
    "supabase/supabase": "Supabase",
    "traefik/traefik": "Traefik",
    "grafana/grafana": "Grafana",
    "prometheus/prometheus": "Prometheus",
    "kubernetes/kubernetes": "Kubernetes",
    "neovim/neovim": "Neovim",
    "jesseduffield/lazygit": "Lazygit",
    "junegunn/fzf": "fzf",
    "tailwindlabs/tailwindcss": "Tailwind CSS",
    "vitejs/vite": "Vite",
    "sveltejs/svelte": "Svelte",
    "huggingface/transformers": "Transformers",
    "langchain-ai/langchain": "LangChain",
    "vllm-project/vllm": "vLLM",
    "ollama/ollama": "Ollama",
    "ggml-org/llama.cpp": "llama.cpp",
    "rclone/rclone": "Rclone",
    "home-assistant/core": "Home Assistant",
}

cats = src["categories"]
cat_names = {c["id"]: c["name"] for c in cats}
tools, missing = [], []
for t in src["tools"]:
    m = meta[t["repo"]]
    full = m["full_name"]
    owner, repo_name = full.split("/")
    if full not in TITLES:
        missing.append(full)
    tools.append({
        "name": TITLES.get(full, repo_name),
        "repo": full,
        "owner": owner,
        "cat": t["cat"],
        "catName": cat_names[t["cat"]],
        "desc": t["desc"],
        "tags": t["tags"],
        "online": t.get("online"),
        "url": m["url"],
        "stars": m["stars"],
        "lang": m["lang"],
        "license": m["license"],
    })

data = {"cats": cats, "tools": tools}
html = open("template.html").read()
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
open("../index.html", "w").write(html)

print("tools:", len(tools))
print("stars total:", sum(t["stars"] for t in tools))
print("online:", sum(1 for t in tools if t["online"]))
print("missing titles:", missing)
print("built index.html", len(html), "bytes")
