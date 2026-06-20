from pathlib import Path
from PIL import Image

ROOT = Path('/home/user/心海鏡像_website')
PAGES = ROOT / 'pages'
EPISODES = ROOT / 'episodes'
IMAGES = ROOT / 'images'

episodes = [
    ('01', '白色之路', 'White Road', '悲傷之後，如何慢慢放下', '在失去與思念之間，替自己留下一條能慢慢往前走的路。'),
    ('02', '慢慢呼吸', 'Slow Breath', '當你很累的時候，先回到呼吸', '把世界放慢一點，讓身體先帶你回到此刻。'),
    ('03', '微光', 'Faint Light', '在黑暗裡，替自己留一點點光', '即使還沒有答案，也能先守住那一點點希望。'),
    ('04', '靜海', 'Still Sea', '讓恐懼慢慢沉下去', '在凝視與安靜裡，讓內在重新變得清澈。'),
    ('05', '自由之浪', 'Free Wave', '把生命感重新喚回來', '允許情緒流動，重新感受自己還活著。'),
    ('06', '最好的安排', 'Best Arrangement', '當下看不懂，也可能是祝福', '從回望中理解，有些路會在未來才顯出意義。'),
    ('07', '無名之月', 'Nameless Moon', '安靜的陪伴，比答案更重要', '在沒有結論的夜裡，學會成為自己的陪伴。'),
    ('08', '今夜', 'Tonight', '今夜先不要解決人生，只要存在', '先讓自己在夜裡停下來，陪自己度過今天。'),
    ('09', '靜謐的思念', 'Quiet Longing', '思念可以從傷口變成溫柔', '讓記憶不只帶來痛，也慢慢留下柔軟。'),
    ('10', '深憩', 'Deep Rest', '真正的休息，是允許自己不再撐', '把疲憊放下，練習被安靜地接住。'),
    ('11', '新的太陽', 'New Sun', '走過夜晚之後，重新迎向生命', '當光再度照進來，生命也能再次開始。'),
    ('12', '感恩之光', 'Light of Gratitude', '走過風與水，終於可以溫柔回望', '把經歷過的一切收進心裡，化成感謝與整合。'),
]

pages = {
    'about.html': {
        'label': 'ABOUT',
        'title': '關於心海鏡像',
        'subtitle': 'A Quiet Place to Return To',
        'body': '''
        <p>「心海鏡像」是胡理安 Gabriel Hu 的創作宇宙。</p>
        <p>它以音樂、書寫、藝術治療與聲音節目為媒介，陪伴人們重新觀看自己的內在世界。</p>
        <p>在這裡，創作不是表演，而是一種陪伴；療癒不是承諾，而是一種真實相遇的可能。</p>
        <p>這個網站會慢慢長成一個安靜而完整的集散地，收納作品，也收納那些還在路上的人。</p>
        '''
    },
    'podcast.html': {
        'label': 'PODCAST',
        'title': '《心海鏡像》Podcast',
        'subtitle': 'Season One · Wind and Water',
        'body': '''
        <p>第一季〈風與水〉以《我心中的風與水》十二首原創作品為核心，一集一首歌，一集一段內在旅程。</p>
        <p>節目結合音樂、名畫觀看、藝術治療練習與創作者真實生命經驗，讓聽眾在二十分鐘裡，得到一段安靜的陪伴。</p>
        <p><a class="cta-button" href="../index.html#episodes">回到 12 集總覽</a></p>
        '''
    },
    'music.html': {
        'label': 'MUSIC',
        'title': 'Bossa Healing 音樂頁',
        'subtitle': 'Wind and Water Within',
        'body': '''
        <p>《我心中的風與水》是一張以 Bossa Nova 為基底、融合中文與葡萄牙語、情緒聲景與靜謐節奏的原創專輯。</p>
        <p>這十二首歌，都是胡理安在多年生命困境中親自創作的作品；每一首都陪他跨越過當時的難關。</p>
        <p>我不能說它們會療癒每一個人，但它們絕對能陪伴你。</p>
        <p><a class="cta-button" href="https://ghgwdbta.gensparkclaw.com/" target="_blank" rel="noopener noreferrer">前往 Bossa Healing 音樂網頁</a></p>
        '''
    },
    'books.html': {
        'label': 'BOOKS',
        'title': '書籍與新書計畫',
        'subtitle': 'Words to Rest In',
        'body': '''
        <p>這裡將整理胡理安已完成的心靈書寫作品，以及未來即將推出的新書計畫。</p>
        <p>文字會比聲音停留得更久，也能在你需要的時候，被一頁一頁地重新打開。</p>
        <p>目前頁面先保留為品牌與作品集入口，後續可逐步補上書介、試讀、購買通路與新書預購資訊。</p>
        '''
    },
    'workshops.html': {
        'label': 'WORKSHOPS',
        'title': '藝術治療與課程',
        'subtitle': 'The Art of Seeing Within',
        'body': '''
        <p>未來這裡會整理線上與實體工作坊、名畫導讀、內在書寫課，以及結合音樂與觀看的深度陪伴課程。</p>
        <p>課程不追求快速改變，而是為情緒、記憶與自我理解留下一個可被接住的空間。</p>
        <p>目前此頁先作為預告頁，之後可加入報名表、課程大綱與活動行事曆。</p>
        '''
    },
    'contact.html': {
        'label': 'CONTACT',
        'title': '聯絡與合作',
        'subtitle': 'For Collaborations and Invitations',
        'body': '''
        <p>如果你希望邀請胡理安進行演講、合作、節目邀訪、藝術治療工作坊或品牌企劃，可以先透過此頁作為入口。</p>
        <p>正式上線後，這裡可加入 Email、表單、社群連結與合作說明。</p>
        <p>目前可先導回首頁訂閱區，作為第一階段的聯繫方式。</p>
        <p><a class="cta-button" href="../index.html#newsletter">前往首頁訂閱區</a></p>
        '''
    }
}

base_css = '''
:root{--deep:#1B2A41;--moon:#F4F1EA;--gold:#C8A96A;--text:#2C3543;--light:#6B7380;--zh:"Noto Serif TC",serif;--en:"Cormorant Garamond",Georgia,serif}
*{margin:0;padding:0;box-sizing:border-box} body{font-family:var(--zh);background:var(--moon);color:var(--text);line-height:1.9;letter-spacing:.02em;-webkit-font-smoothing:antialiased}
a{text-decoration:none;color:inherit} img{max-width:100%;display:block}
.container{max-width:1080px;margin:0 auto;padding:0 28px}
.nav{position:sticky;top:0;z-index:10;background:rgba(244,241,234,.94);backdrop-filter:blur(10px);border-bottom:1px solid rgba(27,42,65,.08)}
.nav-inner{display:flex;justify-content:space-between;align-items:center;padding:18px 0}.nav-logo{font-size:20px;letter-spacing:.15em;color:var(--deep)} .nav-logo small{display:block;font-family:var(--en);font-size:10px;letter-spacing:.25em;color:var(--gold)}
.nav-menu{display:flex;gap:24px;list-style:none;flex-wrap:wrap}.nav-menu a{font-size:13px;letter-spacing:.12em}.nav-menu a:hover,.link:hover{color:var(--gold)}
.hero-mini{padding:84px 0 44px;text-align:center}.label{font-family:var(--en);font-size:13px;letter-spacing:.28em;color:var(--gold);margin-bottom:14px}.title{font-size:44px;font-weight:400;letter-spacing:.12em;color:var(--deep)}.subtitle{font-family:var(--en);font-style:italic;font-size:18px;color:var(--gold);margin-top:10px}
.card{background:#fffdf8;border:1px solid rgba(27,42,65,.06);box-shadow:0 10px 30px rgba(27,42,65,.05);padding:42px;margin:0 auto 60px;max-width:860px}.card p{margin-bottom:18px}
.cta-button{display:inline-block;margin-top:10px;padding:14px 24px;background:var(--deep);color:var(--moon);letter-spacing:.12em;font-size:14px}.cta-button:hover{background:var(--gold);color:var(--deep)}
.episode-layout{display:grid;grid-template-columns:360px 1fr;gap:42px;align-items:start}.cover{width:100%;border-radius:2px;box-shadow:0 14px 40px rgba(27,42,65,.12)}
.meta{display:grid;gap:14px}.meta-block{padding-bottom:14px;border-bottom:1px solid rgba(27,42,65,.08)}.meta-label{font-family:var(--en);font-size:12px;letter-spacing:.24em;color:var(--gold);margin-bottom:6px}.meta-value{font-size:16px}
.footer{padding:50px 0 30px;text-align:center;color:var(--light);font-size:12px}
@media(max-width:860px){.episode-layout{grid-template-columns:1fr}.title{font-size:34px}.nav-menu{gap:14px}}
'''

page_template = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}｜心海鏡像</title>
  <meta name="description" content="{title}｜心海鏡像 Mirror of the Inner Sea">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Noto+Serif+TC:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
  <style>{css}</style>
</head>
<body>
  <nav class="nav">
    <div class="container nav-inner">
      <a href="../index.html" class="nav-logo">心海鏡像<small>MIRROR OF THE INNER SEA</small></a>
      <ul class="nav-menu">
        <li><a href="about.html">關於</a></li>
        <li><a href="podcast.html">Podcast</a></li>
        <li><a href="music.html">音樂</a></li>
        <li><a href="books.html">書籍</a></li>
        <li><a href="workshops.html">課程</a></li>
        <li><a href="contact.html">聯絡</a></li>
      </ul>
    </div>
  </nav>
  <section class="hero-mini">
    <div class="container">
      <p class="label">{label}</p>
      <h1 class="title">{title}</h1>
      <p class="subtitle">{subtitle}</p>
    </div>
  </section>
  <div class="container">
    <div class="card">{body}</div>
  </div>
  <footer class="footer">© 2026 胡理安 Gabriel Hu · Mirror of the Inner Sea</footer>
</body>
</html>
'''

episode_template = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EP {num}｜{title}｜心海鏡像</title>
  <meta name="description" content="EP {num} {title}｜{theme}｜心海鏡像 Podcast">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Noto+Serif+TC:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
  <style>{css}</style>
</head>
<body>
  <nav class="nav">
    <div class="container nav-inner">
      <a href="../index.html" class="nav-logo">心海鏡像<small>MIRROR OF THE INNER SEA</small></a>
      <ul class="nav-menu">
        <li><a href="../index.html#philosophy">關於</a></li>
        <li><a href="../pages/podcast.html">Podcast</a></li>
        <li><a href="../pages/music.html">音樂</a></li>
        <li><a href="../pages/books.html">書籍</a></li>
        <li><a href="../pages/workshops.html">課程</a></li>
      </ul>
    </div>
  </nav>
  <section class="hero-mini">
    <div class="container">
      <p class="label">EP {num} · {en_title}</p>
      <h1 class="title">{title}</h1>
      <p class="subtitle">{theme}</p>
    </div>
  </section>
  <div class="container">
    <div class="card episode-layout">
      <div>
        <img class="cover" src="../images/episodes/{image}" alt="EP {num} {title} 封面">
      </div>
      <div class="meta">
        <div class="meta-block"><div class="meta-label">SONG</div><div class="meta-value">《{title}》 / {en_title}</div></div>
        <div class="meta-block"><div class="meta-label">THEME</div><div class="meta-value">{theme}</div></div>
        <div class="meta-block"><div class="meta-label">EPISODE NOTE</div><div class="meta-value">{desc}</div></div>
        <div class="meta-block"><div class="meta-label">STRUCTURE</div><div class="meta-value">開場金句 → 歌曲播放 → 名畫觀看 → 藝術治療練習 → 書寫延伸 → 結尾預告</div></div>
        <div class="meta-block"><div class="meta-label">STATUS</div><div class="meta-value">頁面骨架已完成，內容可隨後補上逐字稿、播放器、延伸書摘與練習單。</div></div>
        <div><a class="cta-button" href="../pages/music.html">前往音樂頁</a> <a class="cta-button" href="../index.html#newsletter">訂閱更新</a></div>
      </div>
    </div>
  </div>
  <footer class="footer">© 2026 胡理安 Gabriel Hu · Mirror of the Inner Sea</footer>
</body>
</html>
'''

for filename, info in pages.items():
    (PAGES / filename).write_text(page_template.format(css=base_css, **info), encoding='utf-8')

for num, title, en_title, theme, desc in episodes:
    slug_map = {
        '01':'ep01-white-road.jpg','02':'ep02-slow-breath.jpg','03':'ep03-faint-light.jpg','04':'ep04-still-sea.jpg',
        '05':'ep05-free-wave.jpg','06':'ep06-best-arrangement.jpg','07':'ep07-nameless-moon.jpg','08':'ep08-tonight.jpg',
        '09':'ep09-quiet-longing.jpg','10':'ep10-deep-rest.jpg','11':'ep11-new-sun.jpg','12':'ep12-light-of-gratitude.jpg'
    }
    out = EPISODES / f'ep{num}.html'
    out.write_text(episode_template.format(css=base_css, num=num, title=title, en_title=en_title, theme=theme, desc=desc, image=slug_map[num]), encoding='utf-8')

logo = IMAGES / 'logo.png'
favicon = IMAGES / 'favicon.ico'
if logo.exists():
    img = Image.open(logo).convert('RGBA')
    img.thumbnail((256, 256))
    img.save(favicon, format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64)])

print('Generated pages, episodes, and favicon.')
