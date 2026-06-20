# 心海鏡像 Mirror of the Inner Sea — Website

胡理安 (Gabriel Hu) 創作宇宙官方網站
音樂、書籍、藝術治療、Podcast 的安靜集散地。

---

## 資料夾結構

```
心海鏡像_website/
├── index.html              首頁
├── css/
│   └── style.css           全站樣式
├── images/
│   ├── hero.jpg            首頁主視覺
│   ├── logo.png            品牌 Logo（待補）
│   ├── entries/            四大入口圖
│   │   ├── entry-podcast.jpg
│   │   ├── entry-music.jpg
│   │   ├── entry-books.jpg
│   │   └── entry-workshops.jpg
│   └── episodes/           12 集封面
│       ├── ep01-white-road.jpg
│       ├── ep02-slow-breath.jpg
│       ├── ep03-faint-light.jpg
│       ├── ep04-still-sea.jpg
│       ├── ep05-free-wave.jpg
│       ├── ep06-best-arrangement.jpg
│       ├── ep07-nameless-moon.jpg
│       ├── ep08-tonight.jpg
│       ├── ep09-quiet-longing.jpg
│       ├── ep10-deep-rest.jpg
│       ├── ep11-new-sun.jpg
│       └── ep12-light-of-gratitude.jpg
├── pages/                  子頁面（待補）
│   ├── about.html
│   ├── podcast.html
│   ├── music.html
│   ├── books.html
│   ├── workshops.html
│   └── contact.html
├── episodes/               12 集單集頁（待補）
│   ├── ep01.html
│   └── ... ep12.html
└── README.md               本說明檔
```

---

## 命名規則（請維持一致）

- 全部小寫
- 使用連字號 `-`（不要底線、空格、中文）
- 圖片用內容描述命名（不要只用編號）
- 圖片：照片型用 `.jpg`、Logo / 透明圖用 `.png`

---

## 本機預覽

1. 雙擊 `index.html` 即可在瀏覽器開啟
2. 或在資料夾內開啟終端機，執行：
   ```
   python3 -m http.server 8080
   ```
   然後打開 http://localhost:8080

---

## 線上部署

### 方案 A｜Netlify Drop（最快）
1. 前往 https://app.netlify.com/drop
2. 把整個 `心海鏡像_website` 資料夾拖進去
3. 即時取得 `.netlify.app` 網址

### 方案 B｜GitHub Pages
1. 在 GitHub 建立 repo
2. 把資料夾內容上傳
3. Settings → Pages → Deploy from main / root

---

## 待補內容

- [ ] 品牌 Logo（`images/logo.png`）
- [ ] favicon（`images/favicon.ico`）
- [ ] 各子頁面 HTML（pages/）
- [ ] 12 集單集頁 HTML（episodes/）
- [ ] Newsletter 串接真實訂閱服務（建議 ConvertKit / Substack / Mailerlite）
- [ ] 音樂播放器（建議外嵌 Spotify / Apple Music）
- [ ] 書籍購買連結（博客來 / 誠品 / Readmoo）

---

© 2026 胡理安 Gabriel Hu．All rights reserved.
