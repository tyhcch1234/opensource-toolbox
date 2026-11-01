#!/usr/bin/env python3
import os, json, subprocess, urllib.request, concurrent.futures

token = subprocess.check_output(["gh", "auth", "token"]).decode().strip()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = json.load(open("source.json"))


def fetch(repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "oss-tools-builder",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        return repo, {
            "ok": True,
            "full_name": d["full_name"],
            "url": d["html_url"],
            "stars": d["stargazers_count"],
            "forks": d["forks_count"],
            "lang": d.get("language"),
            "license": (d.get("license") or {}).get("spdx_id"),
            "archived": d.get("archived", False),
            "pushed": d.get("pushed_at", "")[:10],
            "topics": d.get("topics", [])[:6],
        }
    except Exception as e:
        return repo, {"ok": False, "error": str(e)}


repos = [t["repo"] for t in src["tools"]]
out = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for repo, res in ex.map(fetch, repos):
        out[repo] = res

bad = {k: v for k, v in out.items() if not v["ok"]}
print("FETCHED", len(out), "FAILED", len(bad))
for k, v in bad.items():
    print("  FAIL", k, v["error"])

json.dump(out, open("meta.json", "w"), ensure_ascii=False, indent=1)
for t in src["tools"]:
    m = out[t["repo"]]
    if m["ok"]:
        print(f'{t["repo"]:45s} {m["stars"]:>7,}  {m["full_name"]}  {m["lang"]}')
