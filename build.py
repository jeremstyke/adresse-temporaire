# Generates the static site: / (FR) and /en/ (EN), legal pages, sitemap.
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://adresse-temporaire.fr"
API = "https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/tmail"
DOMAIN = "adresse-temporaire.fr"

T = {
 "fr": {
  "lang": "fr", "path": "/", "other": "/en/", "other_label": "English",
  "title": "Mail jetable gratuit : adresse mail temporaire en 1 clic | Adresse-Temporaire.fr",
  "desc": "Mail jetable gratuit et sans inscription : votre adresse mail temporaire est prête en un clic. Recevez codes et liens de validation, en français, messages effacés automatiquement.",
  "h1": "Votre mail jetable, prêt tout de suite.",
  "lead": "Gardez votre vraie boîte loin des spams. Utilisez cette adresse pour vous inscrire, recevez le code ou le lien de validation ici, et oubliez-la.",
  "your": "Votre adresse temporaire",
  "copy": "Copier", "copied": "Copiée", "new": "Nouvelle adresse", "choose": "Choisir mon adresse",
  "choose_ph": "nom-de-votre-choix", "choose_ok": "Utiliser", "choose_bad": "3 à 40 caractères : lettres, chiffres, point, tiret.",
  "inbox": "Boîte de réception", "live": "Actualisation auto", "waiting": "En attente de messages...", "waiting_sub": "Les nouveaux messages arrivent ici automatiquement.",
  "back": "Retour à la boîte", "delete": "Supprimer", "from": "De", "imgs": "Afficher les images",
  "imgs_note": "Images masquées pour protéger votre vie privée.",
  "kept": "Les messages sont effacés automatiquement au bout d'une heure.",
  "err": "Connexion impossible pour le moment. Nouvel essai dans quelques secondes.",
  "how_h": "Comment ça marche",
  "how": [["Copiez l'adresse", "Une adresse est créée pour vous dès l'ouverture de la page. Aucune inscription, aucun mot de passe."],
          ["Utilisez-la", "Collez-la dans le formulaire d'inscription, de téléchargement ou de jeu-concours qui vous demande un e-mail."],
          ["Lisez le message", "Le code ou le lien de validation s'affiche ici en quelques secondes. Une heure plus tard, tout est effacé."]],
  "why_h": "Pourquoi utiliser une adresse mail temporaire ?",
  "why": "Chaque fois que vous donnez votre vraie adresse, vous prenez le risque de recevoir des pubs pendant des années, ou de la voir fuiter lors d'un piratage. Une adresse jetable vous protège : vous testez un service, téléchargez un livre blanc ou accédez à un Wi-Fi sans rien laisser derrière vous.",
  "faq_h": "Questions fréquentes",
  "faq": [["C'est vraiment gratuit ?", "Oui. Sans compte, c'est gratuit et sans inscription. Le compte gratuit ajoute une adresse réservée et privée. Le Premium, à 2,99 € par mois, en permet jusqu'à 100, garde les messages 30 jours, transfère vos messages vers votre vraie boîte et garde les pièces jointes."],
          ["Combien de temps les messages restent-ils ?", "Une heure sans compte, 24 heures sur une adresse réservée avec le compte gratuit, 30 jours en Premium. Ensuite, ils sont supprimés définitivement."],
          ["Puis-je envoyer des e-mails ?", "Non. L'adresse sert uniquement à recevoir, ce qui évite qu'elle soit utilisée pour envoyer du spam."],
          ["Quelqu'un d'autre peut-il lire mes messages ?", "Sans compte, toute personne qui connaît exactement l'adresse peut voir sa boîte : préférez une adresse générée au hasard. Avec un compte, vos adresses réservées sont privées : vous seul pouvez lire leurs messages. Dans tous les cas, ne l'utilisez pas pour des informations sensibles (banque, santé, administration)."],
          ["Je retrouve mon adresse si je reviens ?", "Oui, elle est gardée dans votre navigateur. Vous pouvez aussi en créer une nouvelle à tout moment."],
          ["Pourquoi certains sites refusent l'adresse ?", "Certains services bloquent les adresses jetables. Dans ce cas, utilisez votre adresse habituelle."]],
  "rules": "Usage interdit pour toute fraude, harcèlement ou activité illégale.",
  "legal": "Mentions légales et confidentialité", "legal_href": "/mentions-legales.html",
  "report": "Signaler un abus",
  "ago": ["à l'instant", "il y a {} min", "il y a {} h"],
  "nosubj": "(sans objet)",
 },
 "en": {
  "lang": "en", "path": "/en/", "other": "/", "other_label": "Français",
  "title": "Free temporary email address, disposable inbox | Adresse-Temporaire.fr",
  "desc": "Get a free temporary email address in one click, no sign-up. Receive verification codes and links, then everything is erased after one hour.",
  "h1": "A disposable email address, ready right now.",
  "lead": "Keep your real inbox away from spam. Use this address to sign up, receive the code or confirmation link here, and forget about it.",
  "your": "Your temporary address",
  "copy": "Copy", "copied": "Copied", "new": "New address", "choose": "Pick my address",
  "choose_ph": "name-of-your-choice", "choose_ok": "Use", "choose_bad": "3 to 40 characters: letters, numbers, dot, dash.",
  "inbox": "Inbox", "live": "Auto refresh", "waiting": "Waiting for messages...", "waiting_sub": "New messages show up here automatically.",
  "back": "Back to inbox", "delete": "Delete", "from": "From", "imgs": "Show images",
  "imgs_note": "Images hidden to protect your privacy.",
  "kept": "Messages are erased automatically after one hour.",
  "err": "Can't connect right now. Retrying in a few seconds.",
  "how_h": "How it works",
  "how": [["Copy the address", "An address is created for you as soon as the page opens. No sign-up, no password."],
          ["Use it", "Paste it into any sign-up, download or giveaway form that asks for an email."],
          ["Read the message", "The code or confirmation link shows up here within seconds. One hour later, everything is erased."]],
  "why_h": "Why use a temporary email address?",
  "why": "Every time you give out your real address, you risk years of marketing emails, or seeing it leak in a data breach. A disposable address protects you: try a service, download a white paper or get on a Wi-Fi network without leaving anything behind.",
  "faq_h": "Frequently asked questions",
  "faq": [["Is it really free?", "Yes, completely, with no sign-up."],
          ["How long are messages kept?", "One hour after they arrive, then they are permanently deleted. Nothing is kept."],
          ["Can I send emails?", "No. The address can only receive, so it can't be used to send spam."],
          ["Can someone else read my messages?", "Anyone who knows the exact address can see its inbox. Don't use it for anything sensitive (banking, health, government) and prefer a randomly generated address."],
          ["Will I get my address back if I come back?", "Yes, it's kept in your browser. You can also create a new one at any time."],
          ["Why do some sites reject the address?", "Some services block disposable addresses. In that case, use your usual address."]],
  "rules": "Use for fraud, harassment or any illegal activity is forbidden.",
  "legal": "Legal notice and privacy", "legal_href": "/en/legal.html",
  "report": "Report abuse",
  "ago": ["just now", "{} min ago", "{} h ago"],
  "nosubj": "(no subject)",
 },
}

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@500;700&family=Public+Sans:wght@400;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'

CSS = """
:root{--ink:#16213b;--ink2:#4a5672;--paper:#f6f7fa;--card:#fff;--line:#dde2ec;--red:#c8323a;--blue:#2852b8;--blue-d:#1d3f92;--ok:#1d7a4b}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 "Public Sans",system-ui,sans-serif}
a{color:var(--blue)}a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.air{height:8px;background:repeating-linear-gradient(-45deg,var(--red) 0 14px,#fff 14px 22px,var(--blue) 22px 36px,#fff 36px 44px)}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
header.top{display:flex;align-items:center;justify-content:space-between;padding:18px 0}
.brand{font:700 18px "Familjen Grotesk",sans-serif;color:var(--ink);text-decoration:none;letter-spacing:-.01em}
.brand span{color:var(--red)}
.lng{font-size:14px;color:var(--ink2)}
h1{font:700 clamp(30px,5.4vw,46px)/1.08 "Familjen Grotesk",sans-serif;letter-spacing:-.025em;margin:18px 0 12px;max-width:16ch}
.lead{color:var(--ink2);max-width:60ch;margin:0 0 26px;font-size:17px}
.env{background:var(--card);border:1px solid var(--line);border-radius:6px;position:relative;box-shadow:0 1px 0 var(--line)}
.env:before{content:"";position:absolute;inset:0 0 auto 0;height:5px;border-radius:6px 6px 0 0;background:repeating-linear-gradient(-45deg,var(--red) 0 10px,#fff 10px 15px,var(--blue) 15px 25px,#fff 25px 30px)}
.addr{padding:24px 22px 18px}
.addr label{display:block;font-size:14px;color:var(--ink2);margin-bottom:8px}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:stretch}
#addr{flex:1 1 320px;min-width:0;font:500 clamp(16px,3.4vw,22px) "JetBrains Mono",monospace;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:4px;padding:12px 14px;overflow-wrap:anywhere}
.btn{cursor:pointer;font:600 15px "Public Sans",sans-serif;border-radius:4px;padding:12px 18px;border:1px solid var(--blue);background:var(--blue);color:#fff}
.btn:hover{background:var(--blue-d)}
.btn.ghost{background:#fff;color:var(--blue)}.btn.ghost:hover{background:#eef2fb}
.btn.done{background:var(--ok);border-color:var(--ok)}
.tools{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-size:14px}
.link{background:none;border:0;padding:0;color:var(--blue);font:inherit;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
#pick{display:none;margin-top:12px;gap:8px;flex-wrap:wrap;align-items:center}
#pick.on{display:flex}
#pick input{font:500 15px "JetBrains Mono",monospace;padding:9px 10px;border:1px solid var(--line);border-radius:4px;width:220px}
#pick .dom{font:500 15px "JetBrains Mono",monospace;color:var(--ink2)}
#pickerr{color:var(--red);font-size:14px;width:100%}
.box{border-top:1px solid var(--line)}
.boxh{display:flex;justify-content:space-between;align-items:center;padding:14px 22px;font-weight:600}
.live{font-size:13px;color:var(--ink2);font-weight:400;display:flex;align-items:center;gap:7px}
.live i{width:8px;height:8px;border-radius:50%;background:var(--ok);display:inline-block}
@media (prefers-reduced-motion:no-preference){.live i{animation:p 2s ease-in-out infinite}@keyframes p{50%{opacity:.25}}}
ul.msgs{list-style:none;margin:0;padding:0}
ul.msgs li{border-top:1px solid var(--line)}
ul.msgs button{all:unset;box-sizing:border-box;display:grid;grid-template-columns:1fr auto;gap:2px 14px;width:100%;padding:14px 22px;cursor:pointer}
ul.msgs button:hover{background:#f3f5fa}ul.msgs button:focus-visible{outline:3px solid var(--blue);outline-offset:-3px}
.f{font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.t{font-size:13px;color:var(--ink2);white-space:nowrap}
.s{grid-column:1/-1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.p{grid-column:1/-1;font-size:14px;color:var(--ink2);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.new .f:before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--red);margin-right:8px;vertical-align:middle}
.empty{padding:34px 22px 38px;text-align:center;color:var(--ink2)}
.empty b{display:block;color:var(--ink);font-weight:600;margin-bottom:4px}
#view{display:none;border-top:1px solid var(--line);padding:16px 22px 22px}
#view.on{display:block}
.vh{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:12px}
#vsubj{font:700 22px/1.25 "Familjen Grotesk",sans-serif;margin:6px 0 4px}
#vfrom{font-size:14px;color:var(--ink2);overflow-wrap:anywhere}
.imgbar{font-size:13px;color:var(--ink2);margin:10px 0;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
#vframe{width:100%;min-height:420px;border:1px solid var(--line);border-radius:4px;background:#fff}
#vtext{white-space:pre-wrap;overflow-wrap:anywhere;font-size:15px;background:var(--paper);border:1px solid var(--line);border-radius:4px;padding:14px}
.note{font-size:13px;color:var(--ink2);padding:0 22px 16px}
#err{display:none;color:var(--red);font-size:14px;padding:0 22px 12px}
section.c{margin:56px 0}
section.c h2{font:700 26px/1.2 "Familjen Grotesk",sans-serif;letter-spacing:-.015em;margin:0 0 18px}
ol.steps{list-style:none;counter-reset:s;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px}
ol.steps li{counter-increment:s}
ol.steps li:before{content:counter(s);display:inline-grid;place-items:center;width:30px;height:30px;border:2px solid var(--blue);color:var(--blue);border-radius:50%;font:700 15px "Familjen Grotesk";margin-bottom:8px}
ol.steps b{display:block;margin-bottom:4px}
ol.steps p,section.c>p{margin:0;color:var(--ink2);max-width:66ch}
details{border-top:1px solid var(--line);padding:14px 0}
details:last-child{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:12px}summary::-webkit-details-marker{display:none}summary:after{content:"+";font:400 24px/1 "Public Sans",sans-serif;color:var(--blue)}details[open] summary:after{transform:rotate(45deg)}summary:after{transition:transform .15s}
details p{margin:8px 0 0;color:var(--ink2);max-width:66ch}
footer{margin-top:60px;padding:26px 0 40px;border-top:1px solid var(--line);font-size:14px;color:var(--ink2)}
footer a{color:var(--ink2)}
@media (max-width:520px){.row .btn{flex:1}}
.nav{display:flex;align-items:center;gap:16px}.brand,.acct{white-space:nowrap}@media (max-width:420px){.brand{font-size:15px}.nav{gap:10px}.acct{padding:7px 9px;font-size:13px}.nav>a{font-size:13px}}.nav>a{color:var(--ink);font-weight:600;font-size:14px;text-decoration:none}.nav>a:hover{color:var(--blue)}
.acct{cursor:pointer;font:600 14px "Public Sans",sans-serif;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:4px;padding:8px 12px}
.acct:hover{border-color:var(--blue);color:var(--blue)}
.acct.on{border-color:var(--blue);color:var(--blue)}
.keep{margin:12px 0 0;font-size:14px;color:var(--ink2)}
.keep b{color:var(--ok)}
dialog{border:1px solid var(--line);border-radius:6px;padding:0;max-width:460px;width:calc(100% - 32px);color:var(--ink);box-shadow:0 20px 60px rgba(22,33,59,.25)}
dialog::backdrop{background:rgba(22,33,59,.45)}
.dh{display:flex;justify-content:space-between;align-items:center;padding:16px 20px;border-bottom:1px solid var(--line)}
.dh h2{font:700 20px "Familjen Grotesk",sans-serif;margin:0}
.x{all:unset;cursor:pointer;font-size:24px;line-height:1;padding:4px 8px;color:var(--ink2)}
.x:focus-visible{outline:3px solid var(--blue)}
.db{padding:18px 20px 22px}
.db p{margin:0 0 12px;color:var(--ink2);font-size:15px}
.db label{display:block;font-size:14px;margin:0 0 6px;color:var(--ink2)}
.db input{width:100%;font:16px "Public Sans",sans-serif;padding:11px 12px;border:1px solid var(--line);border-radius:4px;margin-bottom:12px}
.db input.code{font:500 24px "JetBrains Mono",monospace;letter-spacing:8px;text-align:center}
.db .btn{width:100%}
.derr{color:var(--red);font-size:14px;min-height:20px;margin:6px 0 0}
.plan{display:flex;justify-content:space-between;align-items:center;gap:10px;background:var(--paper);border:1px solid var(--line);border-radius:4px;padding:12px 14px;margin:0 0 16px}
.plan b{font:700 16px "Familjen Grotesk",sans-serif}
.tag{font-size:12px;font-weight:600;padding:3px 8px;border-radius:20px;background:#e8ecf6;color:var(--blue)}
.tag.p{background:var(--red);color:#fff}
ul.my{list-style:none;padding:0;margin:0 0 14px}
ul.my li{display:flex;align-items:center;gap:8px;border-top:1px solid var(--line);padding:9px 0}
ul.my li:last-child{border-bottom:1px solid var(--line)}
ul.my .a{flex:1;min-width:0;font:500 14px "JetBrains Mono",monospace;overflow-wrap:anywhere}
ul.my .cur{color:var(--blue)}
.sm{font-size:13px}
.row2{display:flex;gap:8px;margin-bottom:12px}.row2 input{margin:0;flex:1;min-width:0;font-family:"JetBrains Mono",monospace;font-size:15px}.row2 .btn{width:auto}
.prem{display:block;text-align:center;text-decoration:none;margin:4px 0 12px;background:var(--red);border-color:var(--red)}
.prem:hover{background:#a8272e}
.out{margin-top:6px}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}
.plans>div{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:20px 22px}
.plans h3{font:700 19px "Familjen Grotesk",sans-serif;margin:0 0 4px}
.plans .pr{font:700 26px "Familjen Grotesk",sans-serif;margin:0 0 10px}
.plans .pr small{font:400 14px "Public Sans",sans-serif;color:var(--ink2)}
.plans ul{margin:0 0 14px;padding-left:18px;color:var(--ink2)}
ul.gl{margin:0 0 10px;padding-left:20px}ul.gl li{margin:6px 0}
.atts{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 0}.atts button{font:600 13px "Public Sans",sans-serif;background:var(--card);border:1px solid var(--line);border-radius:4px;padding:6px 10px;cursor:pointer;color:var(--ink)}.atts button:hover{border-color:var(--blue)}
.vpn{border:1px dashed var(--line);border-radius:6px;padding:18px 20px;margin:28px 0;background:var(--card)}.vpn b{display:block;font:700 18px "Familjen Grotesk",sans-serif;margin:2px 0 6px}.vpn p{margin:0 0 12px;color:var(--ink2)}.vpn small{display:block;margin-top:10px;font-size:12px;color:var(--ink2)}.vpn .sp{font-size:12px;color:var(--ink2)}
.my select{font:13px "Public Sans",sans-serif;border:1px solid var(--line);border-radius:4px;padding:3px 4px;background:var(--card);color:var(--ink);max-width:150px}
.vpnb{display:grid;grid-template-columns:1fr auto;gap:10px 24px;align-items:center;background:var(--ink);color:#fff;border-radius:6px;padding:22px 24px;margin:28px 0;box-shadow:inset 6px 0 0 var(--red)}.vpnb b{display:block;font:700 21px/1.25 "Familjen Grotesk",sans-serif;margin:4px 0 6px}.vpnb p{margin:0;color:#d5dbea}.vpnb .sp{font-size:12px;color:#aeb8d0}.vpnb small{grid-column:1/-1;font-size:12px;color:#aeb8d0}.top .nav{margin-left:14px}@media(max-width:420px){.top .brand{font-size:14px}.top .nav{margin-left:8px;gap:8px}.top .nav a,.top .acct{font-size:13px}.top .acct{padding:6px 8px}}.vpnb .vb{text-decoration:none;background:#fff;color:var(--ink);border-color:#fff;white-space:nowrap}.vpnb .vb:hover{background:#e8ecf6}@media(max-width:700px){.vpnb{grid-template-columns:1fr}.vpnb .vb{white-space:normal;text-align:center}}
.plans .hi{border-color:var(--red);box-shadow:inset 0 4px 0 var(--red)}
footer .fl{display:flex;gap:18px;flex-wrap:wrap;margin-top:6px}
"""

BCSS = """
.bh{padding:26px 0 8px}
.bh h1{max-width:20ch}
.kick{font-size:14px;color:var(--ink2);margin:0}
.posts{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin:26px 0 10px}.posts.home{margin-top:8px}.more{margin:18px 0 0}.more .btn{display:inline-block;text-decoration:none}
.post{position:relative;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:22px 22px 20px;display:flex;flex-direction:column;align-items:flex-start}
.post:before{content:"";position:absolute;inset:0 0 auto 0;height:5px;border-radius:6px 6px 0 0;background:repeating-linear-gradient(-45deg,var(--red) 0 10px,#fff 10px 15px,var(--blue) 15px 25px,#fff 25px 30px)}
.post h2,.post .pt{font:700 20px/1.25 "Familjen Grotesk",sans-serif;margin:12px 0 8px;padding-right:8px;letter-spacing:-.01em}
.post h2 a,.post .pt a{color:var(--ink);text-decoration:none}.post h2 a:after,.post .pt a:after{content:"";position:absolute;inset:0}
.post:hover h2 a,.post:hover .pt a{color:var(--blue)}
.post p{margin:0 0 14px;color:var(--ink2);font-size:15px;flex:1;width:100%}
.post .cat{margin-right:70px}
.meta{font-size:13px;color:var(--ink2)}
.cat{display:inline-block;font-size:12px;font-weight:600;color:var(--blue);background:#e8ecf6;border-radius:20px;padding:3px 9px}
.stamp{position:absolute;top:16px;right:16px;width:60px;height:60px;border:2px dashed var(--red);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--red);transform:rotate(-8deg);line-height:1.05}
.stamp b{font:700 20px "Familjen Grotesk",sans-serif}.stamp i{font-style:normal;font-size:10px;font-weight:600;letter-spacing:.04em}
article.art{max-width:68ch}
.crumb{font-size:13px;color:var(--ink2);margin:20px 0 0}.crumb a{color:var(--ink2)}
article.art h1{max-width:22ch;margin-top:14px}
article.art .lead{margin-bottom:10px}
article.art h2{font:700 24px/1.25 "Familjen Grotesk",sans-serif;margin:36px 0 10px;letter-spacing:-.01em}
article.art h3{font:700 18px/1.3 "Familjen Grotesk",sans-serif;margin:22px 0 6px}
article.art p,article.art li{font-size:17px;line-height:1.7}
article.art ul{padding-left:22px}
article.art li{margin:6px 0}
article.art code{font:500 15px "JetBrains Mono",monospace;background:#eef1f7;padding:1px 6px;border-radius:3px;overflow-wrap:anywhere}
article.art table{width:100%;border-collapse:collapse;margin:16px 0;font-size:15px}
article.art th,article.art td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
article.art th{background:#eef1f7}
.cta{position:relative;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:24px 22px 22px;margin:40px 0}
.cta:before{content:"";position:absolute;inset:0 0 auto 0;height:5px;border-radius:6px 6px 0 0;background:repeating-linear-gradient(-45deg,var(--red) 0 10px,#fff 10px 15px,var(--blue) 15px 25px,#fff 25px 30px)}
.cta b{font:700 20px "Familjen Grotesk",sans-serif;display:block;margin-bottom:4px}
.cta p{margin:0 0 14px!important;color:var(--ink2)}
.cta .btn{display:inline-block;text-decoration:none}
.rel h2{font:700 20px "Familjen Grotesk",sans-serif!important;margin:10px 0!important}
.rel ul{padding-left:20px}
"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def head(t, title, desc, canon, alt_fr, alt_en, extra=""):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="google-site-verification" content="zOVKFpJBh1jvzMQHPHjjrzCtxGgENVeCLLiVSmmgdzg">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:image" content="https://adresse-temporaire.fr/og.png"><meta property="og:locale" content="fr_FR"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#16213b">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='2' y='7' width='28' height='19' rx='2' fill='%23fff' stroke='%2316213b' stroke-width='2'/%3E%3Cpath d='M3 9l13 9 13-9' fill='none' stroke='%23c8323a' stroke-width='2'/%3E%3C/svg%3E">
{FONTS}<style>{CSS}{BCSS}</style>{extra}</head><body><div class="air"></div>"""

def topbar(t, other_href):
    return f"""<div class="wrap"><header class="top"><a class="brand" href="/">adresse<span>-</span>temporaire.fr</a><nav class="nav"><a href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire-menu" target="_blank" rel="sponsored noopener">VPN</a><a href="/blog/">Guides</a><button class="acct" id="acct" type="button">Mon compte</button></nav></header>"""

def foot(t):
    return f"""<footer><div>{esc(t['rules'])}</div><div class="fl"><a href="/blog/">Guides du mail jetable</a><a href="{t['legal_href']}">{esc(t['legal'])}</a><a href="mailto:contact@{DOMAIN}">{esc(t['report'])}</a><span>&copy; 2026 adresse-temporaire.fr</span></div></footer></div>"""


DIALOG = """<dialog id="dlg" aria-labelledby="dlgt"><div class="dh"><h2 id="dlgt">Mon compte</h2><button class="x" id="dlgx" type="button" aria-label="Fermer">&times;</button></div>
<div class="db" id="s1"><p>Recevez un code par e-mail pour vous connecter. Pas de mot de passe.</p><form id="f1"><label for="em">Votre adresse e-mail</label><input id="em" type="email" autocomplete="email" required placeholder="vous@exemple.fr"><button class="btn" type="submit" id="b1">Recevoir mon code</button><p class="derr" id="e1" role="alert"></p></form></div>
<div class="db" id="s2" hidden><p id="s2t"></p><form id="f2"><label for="cd">Code à 6 chiffres</label><input id="cd" class="code" inputmode="numeric" autocomplete="one-time-code" maxlength="6" required><button class="btn" type="submit" id="b2">Me connecter</button><p class="derr" id="e2" role="alert"></p></form><button class="link sm" id="back1" type="button">Changer d'adresse e-mail</button></div>
<div class="db" id="s3" hidden><div class="plan"><div><b id="pn"></b><div class="sm" id="pd"></div></div><span class="tag" id="ptag"></span></div>
<label>Mes adresses réservées</label><ul class="my" id="my"></ul><p class="sm" id="mye"></p><p class="sm" id="fwdn"></p>
<form id="f3"><div class="row2"><input id="ra" maxlength="40" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="nom-de-votre-choix" aria-label="Adresse à réserver"><button class="btn ghost" type="submit">Réserver</button></div></form>
<p class="derr" id="e3" role="alert"></p>
<a class="btn prem" id="gopro" href="#" target="_blank" rel="noopener">Passer Premium, 2,99 € par mois</a>
<p class="sm" id="me-em"></p><button class="link sm out" id="logout" type="button">Me déconnecter</button></div>
</dialog>"""

JS = r"""
(function(){
var L=__T__,API="__API__",DOM="__DOM__",GUM="https://jeremstyke.gumroad.com/l/anvfvt",K="at_addr",KT="at_tok",seen={},cur=null,showImgs=false,tm=null,fails=0,acct=null;
var $=function(i){return document.getElementById(i)};
var RX=/^[a-z0-9][a-z0-9._-]{2,39}$/;
function rnd(){var c="abcdefghijkmnpqrstuvwxyz23456789",s="";var a=new Uint32Array(10);crypto.getRandomValues(a);for(var i=0;i<10;i++)s+=c[a[i]%c.length];return s}
function lg(k){try{return localStorage.getItem(k)}catch(e){return null}}
function ls(k,v){try{if(v==null)localStorage.removeItem(k);else localStorage.setItem(k,v)}catch(e){}}
var tok=lg(KT);
function H(x){var h=x||{};if(tok)h.Authorization="Bearer "+tok;return h}
function api(p,o){o=o||{};o.headers=H(o.headers);o.cache="no-store";return fetch(API+p,o).then(function(r){return r.json().then(function(j){j._s=r.status;return j})})}
function post(p,b){return api(p,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(b||{})})}
var me=lg(K);var qa=(location.search.match(/[?&]a=([a-z0-9._-]{3,40})/)||[])[1];if(qa&&RX.test(qa)){me=qa;ls(K,me)}if(!me||!RX.test(me)){me=rnd();ls(K,me);ping()}
function ping(){try{fetch(API+"/new",{method:"POST"})}catch(e){}}
function full(){return me+"@"+DOM}
function mine(a){return !!(acct&&acct.addrs.indexOf(a)>=0)}
function setAddr(v){me=v;ls(K,v);seen={};cur=null;$("addr").textContent=full();closeView();last=[];render([]);keep();load()}
$("addr").textContent=full();
$("copy").onclick=function(){var b=this;var done=function(){b.textContent=L.copied;b.classList.add("done");setTimeout(function(){b.textContent=L.copy;b.classList.remove("done")},1600)};
 if(navigator.clipboard)navigator.clipboard.writeText(full()).then(done,function(){sel();done()});else{sel();done()}};
function sel(){var r=document.createRange();r.selectNodeContents($("addr"));var s=getSelection();s.removeAllRanges();s.addRange(r);try{document.execCommand("copy")}catch(e){}}
$("new").onclick=function(){setAddr(rnd());ping()};
$("choose").onclick=function(){$("pick").classList.toggle("on");$("pickin").focus()};
$("pickform").onsubmit=function(e){e.preventDefault();var v=$("pickin").value.trim().toLowerCase();
 if(!RX.test(v)){$("pickerr").textContent=L.choose_bad;return}
 $("pickerr").textContent="";$("pick").classList.remove("on");setAddr(v);ping()};
function ago(t){var d=(Date.now()-new Date(t).getTime())/60000;if(d<1)return L.ago[0];if(d<60)return L.ago[1].replace("{}",Math.floor(d));if(d<2880)return L.ago[2].replace("{}",Math.floor(d/60));return "il y a "+Math.floor(d/1440)+" j"}
function txt(s){return document.createTextNode(s||"")}
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.appendChild(txt(x));return e}
function render(ms){var ul=$("list");ul.innerHTML="";$("empty").style.display=ms.length?"none":"block";
 ms.forEach(function(m){var li=document.createElement("li");var b=document.createElement("button");b.type="button";if(!seen[m.id])li.className="new";
  b.appendChild(el("span","f",m.from));b.appendChild(el("span","t",ago(m.at)));b.appendChild(el("span","s",m.subject||L.nosubj));b.appendChild(el("span","p",m.preview));
  b.onclick=function(){open(m.id)};li.appendChild(b);ul.appendChild(li)})}
var last=[];
function keep(){var k=$("keep");k.innerHTML="";
 if(mine(me)){k.appendChild(el("b",null,"Adresse privée"));k.appendChild(txt(" : réservée à votre compte, messages gardés "+(acct.premium?"30 jours":"24 heures")+"."));$("knote").textContent="Seul votre compte peut lire cette boîte.";return}
 $("knote").textContent=L.kept;
 var b=el("button","link",acct?"Réserver cette adresse":"Garder cette adresse et la rendre privée");b.type="button";
 b.onclick=function(){if(!acct){openDlg();return}reserve(me)};
 k.appendChild(b);if(!acct)k.appendChild(txt(" (compte gratuit)"))}
function load(){var a=me;api("/box?a="+encodeURIComponent(a)).then(function(j){if(a!==me)return;fails=0;$("err").style.display="none";
  if(j._s===403){$("err").textContent="Cette adresse est réservée par un autre compte. Choisissez-en une autre.";$("err").style.display="block";last=[];render([]);return}
  $("err").textContent=L.err;last=j.msgs||[];render(last)}).catch(function(){fails++;if(fails>1)$("err").style.display="block"})}
function loop(){clearTimeout(tm);tm=setTimeout(function(){if(!document.hidden)load();loop()},5000)}
document.addEventListener("visibilitychange",function(){if(!document.hidden)load()});
function closeView(){$("view").classList.remove("on");$("listwrap").style.display="block"}
$("back").onclick=function(){closeView();render(last)};
$("del").onclick=function(){if(!cur)return;var id=cur.id;api("/del?a="+encodeURIComponent(me)+"&id="+id,{method:"POST"}).then(function(){last=last.filter(function(m){return m.id!==id});closeView();render(last)})};
$("imgs").onclick=function(){showImgs=true;paint()};
function paint(){var m=cur;if(!m)return;var fr=$("vframe"),tx=$("vtext");
 if(m.html){tx.style.display="none";fr.style.display="block";$("imgbar").style.display=showImgs?"none":"flex";
  var csp=showImgs?"default-src 'none'; img-src data: https: http:; style-src 'unsafe-inline' https:; font-src https: data:":"default-src 'none'; img-src data:; style-src 'unsafe-inline'";
  fr.srcdoc='<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="'+csp+'"><base target="_blank"><style>body{font:15px/1.5 system-ui,sans-serif;margin:12px;color:#16213b;overflow-wrap:anywhere}img{max-width:100%;height:auto}</style></head><body>'+m.html+'</body></html>';
  fr.onload=function(){try{fr.style.height=Math.max(420,fr.contentDocument.documentElement.scrollHeight+20)+"px"}catch(e){}}}
 else{fr.style.display="none";$("imgbar").style.display="none";tx.style.display="block";tx.textContent=m.text||""}}
function kb(n){return n>1048576?(n/1048576).toFixed(1)+" Mo":Math.max(1,Math.round(n/1024))+" Ko"}
function atts(list){var d=$("vatts");d.innerHTML="";list.forEach(function(x){var b=el("button",null,"\u{1F4CE} "+x.name+" ("+kb(x.size)+")");b.type="button";
 b.onclick=function(){fetch(API+"/att?a="+encodeURIComponent(me)+"&id="+x.id,{headers:H(),cache:"no-store"}).then(function(r){if(!r.ok)throw 0;return r.blob()}).then(function(bl){var u=URL.createObjectURL(bl),a=document.createElement("a");a.href=u;a.download=x.name||"piece-jointe";document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u)},4000)}).catch(function(){alert("Téléchargement impossible.")})};d.appendChild(b)})}
function open(id){api("/msg?a="+encodeURIComponent(me)+"&id="+id).then(function(m){if(!m||!m.id)return;seen[id]=1;cur=m;showImgs=false;
 $("vsubj").textContent=m.subject||L.nosubj;$("vfrom").textContent=L.from+" : "+(m.from||"")+", "+ago(m.at);atts(m.atts||[]);
 $("listwrap").style.display="none";$("view").classList.add("on");paint();$("vsubj").focus()})}

/* ---- compte ---- */
var dlg=$("dlg"),email="";
function step(n){["s1","s2","s3"].forEach(function(i,k){$(i).hidden=(k!==n-1)})}
function openDlg(){if(acct){fill();step(3)}else step(1);if(dlg.showModal)dlg.showModal();else dlg.setAttribute("open","");setTimeout(function(){var f=acct?$("ra"):$("em");f&&f.focus()},50)}
function closeDlg(){if(dlg.close)dlg.close();else dlg.removeAttribute("open")}
$("acct").onclick=openDlg;$("dlgx").onclick=closeDlg;
dlg.addEventListener("click",function(e){if(e.target===dlg)closeDlg()});
Array.prototype.forEach.call(document.querySelectorAll("[data-acct]"),function(b){b.onclick=openDlg});
var ERR={email:"Adresse e-mail invalide.",rate:"Trop de tentatives. Réessayez dans un moment.",send:"Le code n'a pas pu être envoyé. Réessayez.",expired:"Code expiré. Demandez-en un nouveau.",code:"Code incorrect.",limit:"Limite atteinte pour votre offre.",taken:"Cette adresse est déjà réservée par quelqu'un d'autre.",addr:"3 à 40 caractères : lettres, chiffres, point, tiret."};
$("f1").onsubmit=function(e){e.preventDefault();email=$("em").value.trim().toLowerCase();$("e1").textContent="";$("b1").disabled=true;
 post("/auth/start",{email:email}).then(function(j){$("b1").disabled=false;if(j.ok){$("s2t").textContent="Code envoyé à "+email+". Pensez à regarder dans les spams.";$("cd").value="";step(2);$("cd").focus()}else $("e1").textContent=ERR[j.error]||"Erreur, réessayez."}).catch(function(){$("b1").disabled=false;$("e1").textContent="Connexion impossible."})};
$("back1").onclick=function(){step(1);$("em").focus()};
$("f2").onsubmit=function(e){e.preventDefault();$("e2").textContent="";$("b2").disabled=true;
 post("/auth/verify",{email:email,code:$("cd").value.trim()}).then(function(j){$("b2").disabled=false;if(j.token){tok=j.token;ls(KT,tok);setAcct(j.me);fill();step(3)}else $("e2").textContent=ERR[j.error]||"Erreur, réessayez."}).catch(function(){$("b2").disabled=false;$("e2").textContent="Connexion impossible."})};
function setAcct(a){acct=a;$("acct").textContent=a?(a.premium?"Mon compte Premium":"Mon compte"):"Mon compte";$("acct").classList.toggle("on",!!a);keep()}
function fill(){if(!acct)return;$("pn").textContent=acct.premium?"Premium":"Compte gratuit";
 $("pd").textContent=acct.addrs.length+" / "+acct.max+" adresse"+(acct.max>1?"s":"")+" réservée"+(acct.max>1?"s":"")+", messages gardés "+(acct.premium?"30 jours":"24 heures")+(acct.premium&&acct.premium_until?", jusqu'au "+new Date(acct.premium_until).toLocaleDateString("fr-FR"):"");
 $("ptag").textContent=acct.premium?"Premium":"Gratuit";$("ptag").className="tag"+(acct.premium?" p":"");
 var ul=$("my");ul.innerHTML="";$("mye").textContent=acct.addrs.length?"":"Aucune adresse réservée pour l'instant.";
 acct.addrs.forEach(function(a){var li=document.createElement("li");var s=el("span","a"+(a===me?" cur":""),a+"@"+DOM);
  var o=el("button","link sm",a===me?"Ouverte":"Ouvrir");o.type="button";o.disabled=(a===me);o.onclick=function(){setAddr(a);fill();closeDlg()};
  var r=el("button","link sm","Libérer");r.type="button";r.onclick=function(){if(!confirm("Libérer "+a+"@"+DOM+" ? Ses messages seront supprimés."))return;post("/release",{addr:a}).then(function(j){if(j.email){setAcct(j);fill()}})};
  li.appendChild(s);li.appendChild(o);li.appendChild(r);
  if(acct.premium){var se=document.createElement("select");se.setAttribute("aria-label","Transfert de "+a);[["off","Pas de transfert"],["notif","Alerte par e-mail"],["full","Transfert complet"]].forEach(function(p){var op=document.createElement("option");op.value=p[0];op.textContent=p[1];se.appendChild(op)});se.value=(acct.fwd&&acct.fwd[a])||"off";
   se.onchange=function(){post("/fwd",{addr:a,mode:se.value}).then(function(j){if(j.email){acct=j}})};li.appendChild(se)}
  ul.appendChild(li)});
 $("fwdn").textContent=acct.premium&&acct.addrs.length?"Transfert : les messages reçus sont envoyés à "+acct.email+" (alerte simple ou message complet avec pièces jointes), jusqu'à 30 par jour. Au-delà, les messages restent lisibles ici.":"";
 $("f3").style.display=acct.addrs.length<acct.max?"block":"none";
 if(!$("ra").value)$("ra").value=mine(me)?"":me;
 var g=$("gopro");g.style.display=acct.premium?"none":"block";g.href=GUM+"?wanted=true&uid="+encodeURIComponent(acct.uid)+"&email="+encodeURIComponent(acct.email);
 $("me-em").textContent="Connecté avec "+acct.email}
function reserve(a){$("e3").textContent="";post("/reserve",{addr:a}).then(function(j){
  if(j.email){setAcct(j);$("ra").value="";if(a!==me)setAddr(a);else keep();fill();return}
  if(j.error==="limit"){openDlg();$("e3").textContent=acct&&acct.premium?ERR.limit:"Le compte gratuit permet 1 adresse. Passez Premium pour en avoir jusqu'à 100.";return}
  if(!dlg.open)openDlg();$("e3").textContent=ERR[j.error]||"Erreur, réessayez."})}
$("f3").onsubmit=function(e){e.preventDefault();var v=$("ra").value.trim().toLowerCase();if(!RX.test(v)){$("e3").textContent=ERR.addr;return}reserve(v)};
$("logout").onclick=function(){post("/logout").finally(function(){tok=null;ls(KT,null);setAcct(null);closeDlg();if(!RX.test(me))setAddr(rnd());load()})};
function refresh(){if(!tok){keep();return Promise.resolve()}return api("/me").then(function(j){if(j.email)setAcct(j);else{tok=null;ls(KT,null);setAcct(null)}}).catch(function(){keep()})}
refresh().then(function(){load();if(/[?&]compte=1/.test(location.search))openDlg()});loop();
window.addEventListener("focus",function(){if(tok)refresh()});
})();
"""

from articles import ARTICLES, CTA
import re as _re
MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def stamp(d):
    y,m,dd = map(int, d.split("-"))
    return f'<span class="stamp" aria-hidden="true"><b>{dd:02d}</b><i>{["JANV","FÉVR","MARS","AVR","MAI","JUIN","JUIL","AOÛT","SEPT","OCT","NOV","DÉC"][m-1]}</i><i>{y}</i></span>'
def rtime(html):
    n = len(_re.sub(r"<[^>]+>", " ", html).split()); return max(2, round(n/200))
def card(a):
    return f'<div class="post">{stamp(a["date"])}<span class="cat">{esc(a["cat"])}</span><h3 class="pt"><a href="/blog/{a["slug"]}/">{esc(a["title"])}</a></h3><p>{esc(a["desc"])}</p><span class="meta">{rtime(a["body"])} min de lecture</span></div>'

def index(t):
    other = t["other"]
    canon = SITE + t["path"]
    h = head(t, t["title"], t["desc"], canon, SITE + "/", SITE + "/en/",
             '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "WebApplication", "name": "Adresse-Temporaire.fr", "url": SITE + "/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "description": t["desc"], "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "EUR", "name": "Gratuit"}, {"@type": "Offer", "price": "2.99", "priceCurrency": "EUR", "name": "Premium"}]}, ensure_ascii=False) + '</script><script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": t["lang"], "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}, ensure_ascii=False) + "</script>")
    how = "".join(f"<li><b>{esc(a)}</b><p>{esc(b)}</p></li>" for a, b in t["how"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
    HOMECARDS = "".join(card(a) for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True)[:4])
    jsT = {k: t[k] for k in ["copy", "copied", "choose_bad", "from", "ago", "nosubj"]}
    js = JS.replace("__T__", json.dumps(jsT, ensure_ascii=False)).replace("__API__", API).replace("__DOM__", DOMAIN)
    return h + topbar(t, other) + f"""<main>
<h1>{esc(t['h1'])}</h1><p class="lead">{esc(t['lead'])}</p>
<div class="env">
 <div class="addr"><label for="addr" id="addrl">{esc(t['your'])}</label>
  <div class="row"><output id="addr" aria-labelledby="addrl" aria-live="polite">&nbsp;</output><button class="btn" id="copy" type="button">{esc(t['copy'])}</button></div>
  <div class="tools"><button class="link" id="new" type="button">{esc(t['new'])}</button><button class="link" id="choose" type="button" aria-controls="pick">{esc(t['choose'])}</button></div>
  <form id="pickform"><div id="pick"><input id="pickin" autocomplete="off" autocapitalize="none" spellcheck="false" maxlength="40" placeholder="{esc(t['choose_ph'])}" aria-label="{esc(t['choose'])}"><span class="dom">@{DOMAIN}</span><button class="btn ghost" type="submit">{esc(t['choose_ok'])}</button><span id="pickerr" role="alert"></span></div></form>
  <p class="keep" id="keep"></p>
 </div>
 <div class="box">
  <div id="listwrap"><div class="boxh"><span>{esc(t['inbox'])}</span><span class="live"><i></i>{esc(t['live'])}</span></div>
   <div id="err" role="status">{esc(t['err'])}</div>
   <ul class="msgs" id="list" aria-live="polite"></ul>
   <div class="empty" id="empty"><b>{esc(t['waiting'])}</b>{esc(t['waiting_sub'])}</div>
   <p class="note" id="knote">{esc(t['kept'])}</p></div>
  <div id="view"><div class="vh"><button class="btn ghost" id="back" type="button">{esc(t['back'])}</button><button class="btn ghost" id="del" type="button">{esc(t['delete'])}</button></div>
   <h2 id="vsubj" tabindex="-1"></h2><div id="vfrom"></div><div id="vatts" class="atts"></div>
   <div class="imgbar" id="imgbar"><span>{esc(t['imgs_note'])}</span><button class="link" id="imgs" type="button">{esc(t['imgs'])}</button></div>
   <iframe id="vframe" title="Message" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin" referrerpolicy="no-referrer"></iframe><div id="vtext"></div></div>
 </div>
</div>
<aside class="vpnb"><div><span class="sp">Partenaire recommandé</span><b>Votre adresse est cachée. Et votre connexion ?</b><p>Sur un Wi-Fi public, à l'hôtel ou au café, n'importe qui peut espionner ce que vous faites. NordVPN chiffre tout votre trafic et masque votre adresse IP, sur téléphone comme sur ordinateur.</p></div><a class="btn vb" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire-accueil" target="_blank" rel="sponsored noopener">Protéger ma connexion avec NordVPN</a><small>Lien affilié, sans surcoût pour vous.</small></aside>
<section class="c" id="offres"><h2>Gratuit ou Premium</h2><div class="plans">
 <div><h3>Sans compte</h3><p class="pr">0 €</p><ul><li>Une adresse jetable tout de suite</li><li>Messages effacés après 1 heure</li><li>Boîte publique : toute personne qui connaît l'adresse peut la lire</li></ul></div>
 <div><h3>Compte gratuit</h3><p class="pr">0 €</p><ul><li>1 adresse réservée à votre nom</li><li>Privée : vous seul lisez ses messages</li><li>Messages gardés 24 heures</li></ul><button class="btn ghost" type="button" data-acct>Créer mon compte</button></div>
 <div class="hi"><h3>Premium</h3><p class="pr">2,99 € <small>par mois</small></p><ul><li>Jusqu'à 100 adresses réservées et privées</li><li>Messages transférés vers votre vraie boîte, ou simple alerte par e-mail (30 par jour)</li><li>Messages gardés 30 jours</li><li>Pièces jointes conservées (10 Mo par message)</li><li>Sans engagement</li></ul><button class="btn" type="button" data-acct>Passer Premium</button></div>
</div></section>
<section class="c"><h2>{esc(t['how_h'])}</h2><ol class="steps">{how}</ol></section>
<section class="c"><h2>{esc(t['why_h'])}</h2><p>{esc(t['why'])}</p></section>
<section class="c"><h2>Guides du mail jetable</h2><div class="posts home">{HOMECARDS}</div><p class="more"><a class="btn ghost" href="/blog/">Voir tous les guides</a></p></section>
<section class="c"><h2>{esc(t['faq_h'])}</h2>{faq}</section>
<section class="c"><aside class="vpn"><span class="sp">Partenaire</span><b>Protégez aussi votre connexion</b><p>Le mail jetable protège votre adresse. Sur un Wi-Fi public ou pour masquer votre adresse IP, un VPN chiffre tout votre trafic. Nous recommandons NordVPN.</p><a class="btn ghost" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire" target="_blank" rel="sponsored noopener">Découvrir NordVPN</a><small>Lien affilié : nous touchons une commission si vous vous abonnez, sans surcoût pour vous.</small></aside></section>
</main>""" + foot(t) + DIALOG + f"<script>{js}</script></body></html>"

LEGAL_FR = f"""<main><h1>Mentions légales et confidentialité</h1>
<section class="c"><h2>Éditeur</h2><p>Le site adresse-temporaire.fr est édité par Jérémy Dacier-Jury, entrepreneur individuel (immatriculation en cours). Contact : <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Hébergement</h2><p>Pages du site : GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. Réception des e-mails : Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis. Stockage temporaire des messages : Supabase, Inc., 970 Toa Payoh North #07-04, Singapour.</p></section>
<section class="c"><h2>Fonctionnement et conservation</h2><p>Les adresses servent uniquement à recevoir des messages. Sans compte, chaque message est conservé une heure au maximum. Sur une adresse réservée, il est conservé 24 heures (compte gratuit) ou 30 jours (Premium), puis supprimé définitivement. En Premium, les pièces jointes sont conservées avec le message, et si vous l'activez, chaque message reçu est transféré (ou signalé) à l'adresse e-mail de votre compte, via Resend, dans la limite de 30 transferts par jour. L'adresse que vous utilisez et votre session sont gardées dans votre navigateur (stockage local).</p></section>
<section class="c"><h2>Comptes</h2><p>Si vous créez un compte, nous conservons votre adresse e-mail, vos adresses réservées et la date de fin de votre Premium, tant que le compte existe. Les codes de connexion sont envoyés par Resend (Resend, Inc., États-Unis). Le paiement du Premium est géré par Gumroad (Gumroad, Inc., États-Unis), qui nous transmet uniquement l'e-mail d'achat et le statut de l'abonnement. Pour supprimer votre compte, écrivez à <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Liens affiliés</h2><p>Certains liens du site sont des liens affiliés (NordVPN) : si vous vous abonnez via ces liens, nous touchons une commission, sans surcoût pour vous. Ils sont signalés par la mention « Partenaire » ou « Lien affilié ».</p></section>
<section class="c"><h2>Cookies et statistiques</h2><p>Le site n'utilise pas de cookies. Seul un compteur anonyme du nombre d'adresses créées et de messages reçus par jour est tenu, sans adresse IP ni identifiant.</p></section>
<section class="c"><h2>Usage interdit et signalement</h2><p>Il est interdit d'utiliser ce service pour une fraude, du harcèlement, l'usurpation d'identité ou toute activité illégale. Pour signaler un abus ou un contenu illicite, écrivez à <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a> en indiquant l'adresse concernée. Les contenus signalés sont supprimés sans délai.</p></section>
<section class="c"><h2>Vos droits</h2><p>Conformément au RGPD, vous pouvez demander l'accès ou la suppression de données vous concernant à l'adresse de contact ci-dessus. Les messages étant effacés au bout d'une heure, il est en général impossible d'en fournir une copie après ce délai.</p></section></main>"""

LEGAL_EN = f"""<main><h1>Legal notice and privacy</h1>
<section class="c"><h2>Publisher</h2><p>adresse-temporaire.fr is published by Jérémy Dacier-Jury, sole trader (registration in progress), France. Contact: <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Hosting</h2><p>Site pages: GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Email reception: Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, USA. Temporary message storage: Supabase, Inc., 970 Toa Payoh North #07-04, Singapore.</p></section>
<section class="c"><h2>How it works and retention</h2><p>Addresses can only receive messages. Each message is kept for one hour at most, then permanently deleted. No account is created and no personal data is requested. The address you use is stored only in your browser (local storage), which you can clear at any time.</p></section>
<section class="c"><h2>Cookies and statistics</h2><p>The site uses no cookies. Only an anonymous daily count of addresses created and messages received is kept, with no IP address or identifier.</p></section>
<section class="c"><h2>Forbidden use and reporting</h2><p>Using this service for fraud, harassment, impersonation or any illegal activity is forbidden. To report abuse or illegal content, email <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a> with the address concerned. Reported content is removed without delay.</p></section>
<section class="c"><h2>Your rights</h2><p>Under the GDPR, you can request access to or deletion of data about you at the contact address above. Since messages are erased after one hour, a copy usually cannot be provided after that time.</p></section></main>"""

def legal(t, body, path, title):
    canon = SITE + path
    return head(t, title, title, canon, SITE + "/mentions-legales.html", SITE + "/en/legal.html", '<meta name="robots" content="noindex,follow">') + topbar(t, t["other"]) + body + foot(t) + "</body></html>"

def w(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

w("index.html", index(T["fr"]))
w("mentions-legales.html", legal(T["fr"], LEGAL_FR, "/mentions-legales.html", "Mentions légales et confidentialité | Adresse-Temporaire.fr"))
w("CNAME", DOMAIN + "\n")
w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
w(".nojekyll", "")
# ---------------- BLOG ----------------
import datetime
def fdate(d):
    y,m,dd = map(int, d.split("-")); return f"{dd} {MOIS[m-1]} {y}"
def bhead(title, desc, canon, schema):
    t = T["fr"]
    return head(t, title, desc, canon, canon, canon, ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in schema)).replace('<link rel="canonical"', '<link rel="alternate" type="application/rss+xml" title="Guides du mail jetable" href="/blog/rss.xml"><link rel="canonical"')
def btop():
    return '<div class="wrap"><header class="top"><a class="brand" href="/">adresse<span>-</span>temporaire.fr</a><nav class="nav"><a href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire-menu" target="_blank" rel="sponsored noopener">VPN</a><a href="/blog/">Guides</a><a class="acct" href="/?compte=1" style="text-decoration:none">Mon compte</a></nav></header>'
def bfoot():
    return foot(T["fr"]) + "</body></html>"

arts = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
cards = "".join(card(a) for a in arts)
bl_schema = [{"@context": "https://schema.org", "@type": "Blog", "name": "Guides du mail jetable", "url": SITE + "/blog/", "inLanguage": "fr", "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f'{SITE}/blog/{a["slug"]}/', "datePublished": a["date"]} for a in arts]},
             {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/blog/"}]}]
w("blog/index.html", bhead("Guides du mail jetable et de l'adresse mail temporaire | Adresse-Temporaire.fr", "Nos guides pour utiliser un mail jetable : créer une adresse temporaire, éviter les spams, alias Gmail, sécurité et questions fréquentes.", SITE + "/blog/", bl_schema) + btop() + f"""<main><div class="bh"><p class="kick">Le blog d'adresse-temporaire.fr</p><h1>Guides du mail jetable</h1><p class="lead">Comment protéger votre vraie boîte mail, quand utiliser une adresse temporaire, et les réponses aux questions qu'on nous pose le plus.</p></div>
<div class="posts">{cards}</div>{CTA}</main>""" + bfoot())

for a in arts:
    url = f'{SITE}/blog/{a["slug"]}/'
    others = [o for o in arts if o["slug"] != a["slug"]][:4]
    rel = "".join(f'<li><a href="/blog/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in others)
    sch = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "fr", "mainEntityOfPage": url, "image": SITE + "/og.png", "author": {"@type": "Organization", "name": "Adresse-Temporaire.fr", "url": SITE + "/"}, "publisher": {"@type": "Organization", "name": "Adresse-Temporaire.fr", "url": SITE + "/"}},
           {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/blog/"}, {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]}]
    body = a["body"].strip()
    first, rest = body.split("</p>", 1)
    html = bhead(a["title"] + " | Adresse-Temporaire.fr", a["desc"], url, sch).replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">') + btop() + f"""<main><article class="art">
<p class="crumb"><a href="/">Accueil</a> / <a href="/blog/">Guides</a> / {esc(a["cat"])}</p>
<h1>{esc(a["title"])}</h1><p class="meta">Publié le {fdate(a["date"])}, {rtime(body)} min de lecture</p>
{first.replace('<p>', '<p class="lead">', 1)}</p><aside class="vpnb"><div><span class="sp">Partenaire recommandé</span><b>Votre adresse est cachée. Et votre connexion ?</b><p>Sur un Wi-Fi public, à l'hôtel ou au café, n'importe qui peut espionner ce que vous faites. NordVPN chiffre tout votre trafic et masque votre adresse IP, sur téléphone comme sur ordinateur.</p></div><a class="btn vb" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire-guide" target="_blank" rel="sponsored noopener">Protéger ma connexion avec NordVPN</a><small>Lien affilié, sans surcoût pour vous.</small></aside>{rest}
{CTA}
<aside class="vpn"><span class="sp">Partenaire</span><b>Protégez aussi votre connexion</b><p>Le mail jetable protège votre adresse. Sur un Wi-Fi public ou pour masquer votre adresse IP, un VPN chiffre tout votre trafic. Nous recommandons NordVPN.</p><a class="btn ghost" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire" target="_blank" rel="sponsored noopener">Découvrir NordVPN</a><small>Lien affilié : nous touchons une commission si vous vous abonnez, sans surcoût pour vous.</small></aside>
<div class="rel"><h2>À lire aussi</h2><ul>{rel}</ul></div>
</article></main>""" + bfoot()
    w(f'blog/{a["slug"]}/index.html', html)

# RSS
items = "".join(f'<item><title>{esc(a["title"])}</title><link>{SITE}/blog/{a["slug"]}/</link><guid>{SITE}/blog/{a["slug"]}/</guid><pubDate>{datetime.datetime.strptime(a["date"],"%Y-%m-%d").strftime("%a, %d %b %Y 08:00:00 +0000")}</pubDate><description>{esc(a["desc"])}</description></item>' for a in arts)
w("blog/rss.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Guides du mail jetable</title><link>{SITE}/blog/</link><description>Guides pour utiliser une adresse mail temporaire</description><language>fr</language>{items}</channel></rss>')

# sitemap complet
today = datetime.date.today().isoformat()
urls = [(SITE + "/", today, "1.0"), (SITE + "/blog/", today, "0.8")] + [(f'{SITE}/blog/{a["slug"]}/', a["date"], "0.7") for a in arts] + [(SITE + "/mentions-legales.html", today, "0.2")]
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n" for u, d, pr in urls) + "</urlset>\n")
w("404.html", head(T["fr"], "Page introuvable | Adresse-Temporaire.fr", "Page introuvable", SITE + "/", "", "", '<meta name="robots" content="noindex">') + btop() + '<main><h1>Cette page n\'existe pas.</h1><p class="lead">Elle a peut-être été déplacée. Votre adresse mail jetable vous attend sur la page d\'accueil.</p><p><a class="btn" style="display:inline-block;text-decoration:none" href="/">Aller à l\'accueil</a></p></main>' + bfoot())
print("blog ok", len(arts))
print("ok")
