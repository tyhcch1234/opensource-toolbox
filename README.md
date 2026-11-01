# 開源工具箱 · Open Source Toolbox

按用途分類的 GitHub 開源專案精選，一頁看完 81 個真正會用到的工具。每個專案都有繁體中文說明、實際星數、語言、授權與官方連結；標上「線上即用」的專案點一下就能在瀏覽器開啟，免安裝。

**線上瀏覽：** https://tyhcch1234.github.io/opensource-toolbox/

## 收錄內容

10 個分類、81 個專案：

| 分類 | 內容 |
| --- | --- |
| AI 與機器學習 | Ollama、llama.cpp、Transformers、LangChain、ComfyUI、vLLM、Open WebUI 等 |
| 開發與編程 | VS Code、Neovim、Git、Oh My Zsh、Lazygit、ripgrep、fzf、GitHub CLI |
| 前端與 Web | React、Vue 3、Tailwind CSS、Vite、Next.js、Svelte、shadcn/ui、Axios |
| 後端與基建 | Kubernetes、Redis、PostgreSQL、NGINX、Traefik、Grafana、Prometheus、Docker Engine |
| 資料庫與數據 | Supabase、PocketBase、DuckDB、ClickHouse、Superset、Metabase、Jupyter、pandas |
| 效率與自動化 | n8n、Home Assistant、Rclone、Hoppscotch、IT-Tools、Logseq、Joplin、Stirling PDF、AppFlowy |
| 設計與創作 | Blender、Excalidraw、tldraw、Penpot、Inkscape、GIMP、draw.io、Squoosh |
| 影音與下載 | FFmpeg、VLC、mpv、yt-dlp、Jellyfin、OBS Studio、Kdenlive、HandBrake |
| 安全與隱私 | KeePassXC、Bitwarden、Tailscale、Wireshark、Signal、OpenVPN、VeraCrypt、Hashcat |
| 系統與終端 | Linux Kernel、tmux、Windows Terminal、PowerShell、Nushell、btop、Ventoy、Rufus |

## 功能

- **分類導覽**：頂部膠囊分類，點擊直達；捲動時自動高亮目前分類。
- **即時搜尋**：按 `/` 聚焦，可搜專案名、作者、說明、語言與標籤；`Esc` 清除。
- **三種排序**：分類排序、星數、名稱。
- **篩選**：全部 / 線上即用 / 我的收藏（收藏存在瀏覽器 localStorage）。
- **一鍵使用**：線上版直接開新分頁；桌面版連到 Releases 下載頁；亦可一鍵複製 `git clone` 指令。
- 單一 HTML 檔、零依賴、響應式（手機／平板／桌面），可直接丟到任何靜態主機。

## 專案結構

```
index.html          # 產生的網站（唯一需要的檔案）
favicon.svg
_build/             # 資料與建置腳本
├── source.json     # 人工整理的清單：分類、中文說明、標籤、線上版網址
├── meta.json       # GitHub API 抓回的快照：星數、語言、授權
├── fetch.py        # 依 source.json 抓取 repo metadata
├── template.html   # 版型（CSS / JS / 佔位符 __DATA__）
└── build.py        # 合併資料 → 輸出 ../index.html
```

## 更新星數 / 新增專案

```bash
gh auth login                 # fetch.py 需要 GitHub token（5000 次/小時）
python _build/fetch.py        # 重新抓取 meta.json
python _build/build.py        # 重新產生 index.html
```

新增專案只要在 `_build/source.json` 的 `tools` 陣列加一筆，並在 `_build/build.py` 的 `TITLES` 補上顯示名稱，再跑上面兩步即可。

## 備註

- 星數為 2026-11-01 以 GitHub REST API 取得的快照，頁面上的數字不會自動更新，需重跑 `fetch.py`。
- 專案說明為編輯整理，非官方文案；各專案版權與授權依其 repository 為準。

## License

本頁面的程式碼與整理內容採 MIT License；收錄的開源專案各自採用其原有授權。
