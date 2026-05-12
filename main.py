from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/profile/{username}")
async def get_profile(username: str):
    async with httpx.AsyncClient() as client:
        user_res = await client.get(f"https://api.github.com/users/{username}")
        if user_res.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found")
        if not user_res.is_success:
            raise HTTPException(status_code=502, detail="GitHub API error")

        repos_res = await client.get(
            f"https://api.github.com/users/{username}/repos",
            params={"sort": "updated", "per_page": 100}
        )

        user = user_res.json()
        all_repos = repos_res.json()

        # Only original repos, sorted by stars
        repos = sorted(
            [r for r in all_repos if not r["fork"]],
            key=lambda r: r["stargazers_count"],
            reverse=True
        )

        # Language breakdown
        lang_counts = {}
        for r in repos:
            if r["language"]:
                lang_counts[r["language"]] = lang_counts.get(r["language"], 0) + 1

        total = sum(lang_counts.values()) or 1
        languages = [
            {"name": k, "pct": round(v / total * 100)}
            for k, v in sorted(lang_counts.items(), key=lambda x: -x[1])[:6]
        ]

        return {
            "name": user.get("name") or user["login"],
            "login": user["login"],
            "avatar_url": user["avatar_url"],
            "bio": user.get("bio", ""),
            "location": user.get("location", ""),
            "public_repos": user["public_repos"],
            "followers": user["followers"],
            "following": user["following"],
            "total_stars": sum(r["stargazers_count"] for r in repos),
            "languages": languages,
            "repos": [
                {
                    "name": r["name"],
                    "description": r.get("description", ""),
                    "url": r["html_url"],
                    "language": r.get("language", ""),
                    "stars": r["stargazers_count"],
                    "forks": r["forks_count"],
                    "topics": r.get("topics", [])[:3],
                }
                for r in repos[:20]
            ],
        }
