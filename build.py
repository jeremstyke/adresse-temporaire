# Generates the static site: / (FR) and /en/ (EN), legal pages, sitemap.
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://adresse-temporaire.fr"
API = "https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/tmail"
DOMAIN = "adresse-temporaire.fr"

T = {
 "fr": {
  "lang": "fr", "path": "/", "other": "/en/", "other_label": "English",
  "title": "Mail jetable gratuit : adresse mail temporaire en 1 clic",
  "desc": "Mail jetable gratuit, sans inscription : votre adresse mail jetable est prête en un clic. Recevez codes et liens de validation, puis tout s'efface.",
  "h1": "Votre mail jetable, prêt tout de suite.",
  "lead": "Gardez votre vraie boîte loin des spams. Utilisez cette adresse pour vous inscrire, recevez le code ou le lien de validation ici, et oubliez-la.",
  "your": "Votre adresse temporaire",
  "copy": "Copier", "copied": "Copiée", "new": "Nouvelle adresse", "choose": "Choisir mon adresse",
  "choose_ph": "nom-de-votre-choix", "choose_ok": "Utiliser", "choose_bad": "3 à 40 caractères : lettres, chiffres, point, tiret.",
  "app_t": "Installez l'appli sur votre téléphone ou votre ordinateur", "app_p": "Gratuite, sans store : votre adresse jetable en un geste depuis l'écran d'accueil, avec une alerte à chaque e-mail reçu.", "app_b": "Installer l'appli", "app_ios": "Sur iPhone : touchez le bouton Partager de Safari, puis « Sur l'écran d'accueil ».", "app_other": "Ouvrez le menu de votre navigateur, puis « Installer l'application » ou « Ajouter à l'écran d'accueil ».",
  "ban_t": "Installez l'appli sur votre téléphone", "ban_pc": "Installez l'appli sur votre ordinateur", "app_mac": "Sur Mac avec Safari : menu Fichier, puis « Ajouter au Dock ».", "ban_p": "Gratuit, sans store", "ban_b": "Installer", "ban_x": "Fermer",
  "push_off": "🔔 Être alerté à chaque e-mail", "push_on": "🔔 Alertes activées (désactiver)", "push_no": "Alertes refusées. Autorisez les notifications pour ce site dans les réglages du navigateur.", "push_ios": "Sur iPhone : touchez Partager puis « Sur l'écran d'accueil », ouvrez l'appli et activez les alertes.", "push_ok": "C'est noté : une notification arrivera à chaque nouvel e-mail, même site fermé.",
  "inbox": "Boîte de réception", "live": "Actualisation auto", "waiting": "En attente de messages...", "waiting_sub": "Les nouveaux messages arrivent ici automatiquement.",
  "back": "Retour à la boîte", "delete": "Supprimer", "from": "De", "imgs": "Afficher les images",
  "imgs_note": "Images masquées pour protéger votre vie privée.",
  "kept": "Les messages sont effacés automatiquement au bout d'une heure.",
  "err": "Connexion impossible pour le moment. Nouvel essai dans quelques secondes.",
  "how_h": "Comment ça marche",
  "how": [["Copiez l'adresse", "Une adresse est créée pour vous dès l'ouverture de la page. Aucune inscription, aucun mot de passe."],
          ["Utilisez-la", "Collez-la dans le formulaire d'inscription, de téléchargement ou de jeu-concours qui vous demande un e-mail."],
          ["Lisez le message", "Le code ou le lien de validation s'affiche ici en quelques secondes. Une heure plus tard, tout est effacé."]],
  "why_h": "Pourquoi utiliser une adresse mail jetable ?",
  "why": "Chaque fois que vous donnez votre vraie adresse, vous prenez le risque de recevoir des pubs pendant des années, ou de la voir fuiter lors d'un piratage. Une adresse jetable vous protège : vous testez un service, téléchargez un livre blanc ou accédez à un Wi-Fi sans rien laisser derrière vous. Ce générateur d'e-mail jetable crée une nouvelle adresse à chaque clic, gratuitement et sans inscription, sur un domaine français.",
  "faq_h": "Questions fréquentes",
  "faq": [["C'est vraiment gratuit ?", "Oui. Sans compte, c'est gratuit et sans inscription. Le compte gratuit ajoute une adresse réservée et privée. Le Premium, à 2,99 € par mois, en permet jusqu'à 100, garde les messages 30 jours, transfère vos messages vers votre vraie boîte et garde les pièces jointes."],
          ["Combien de temps les messages restent-ils ?", "Une heure sans compte, 24 heures sur une adresse réservée avec le compte gratuit, 30 jours en Premium. Ensuite, ils sont supprimés définitivement."],
          ["Puis-je recevoir mes e-mails sur Telegram ?", "Oui. Le bot @JetboxMailBot vous donne une adresse jetable dans Telegram et affiche les messages reçus. Si vous avez un compte sur le site, ouvrez « Mon compte » puis « Recevoir mes e-mails sur Telegram » : chaque message reçu sur vos adresses réservées vous arrive aussi dans Telegram, gratuitement."],
          ["Puis-je envoyer des e-mails ?", "Non. L'adresse sert uniquement à recevoir, ce qui évite qu'elle soit utilisée pour envoyer du spam."],
          ["Quelqu'un d'autre peut-il lire mes messages ?", "Sans compte, toute personne qui connaît exactement l'adresse peut voir sa boîte : préférez une adresse générée au hasard. Avec un compte, vos adresses réservées sont privées : vous seul pouvez lire leurs messages. Dans tous les cas, ne l'utilisez pas pour des informations sensibles (banque, santé, administration)."],
          ["Quelle différence entre e-mail jetable et adresse mail temporaire ?", "Aucune : on parle de mail jetable, d'e-mail jetable, d'adresse mail jetable ou d'adresse mail temporaire pour le même service, une boîte que l'on utilise le temps d'une inscription puis que l'on abandonne."],
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
  "app_t": "Get the app on your phone or computer", "app_p": "Free, no app store: your disposable address one tap away on your home screen, with an alert for every email.", "app_b": "Install the app", "app_ios": "On iPhone: tap the Share button in Safari, then Add to Home Screen.", "app_other": "Open your browser menu, then Install app or Add to Home Screen.",
  "ban_t": "Install the app on your phone", "ban_pc": "Install the app on your computer", "app_mac": "On a Mac with Safari: File menu, then Add to Dock.", "ban_p": "Free, no app store", "ban_b": "Install", "ban_x": "Close",
  "push_off": "🔔 Alert me for every email", "push_on": "🔔 Alerts on (turn off)", "push_no": "Alerts blocked. Allow notifications for this site in your browser settings.", "push_ios": "On iPhone: tap Share, then Add to Home Screen, open the app and turn alerts on.", "push_ok": "Done: you will get a notification for every new email, even with the site closed.",
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
.doms{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin-top:10px;font-size:13px;color:var(--ink2)}.doms button{font:inherit;font-size:13px;padding:3px 9px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--ink);cursor:pointer}.doms button[aria-pressed=true]{background:#2852b8;border-color:#2852b8;color:#fff}.doms small{flex-basis:100%;color:var(--ink2)}
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
.tgb{margin:6px 0 14px}.tgb .btn{width:100%}
.iban{position:fixed;left:10px;right:10px;bottom:10px;z-index:50;display:flex;align-items:center;gap:12px;background:#fff;color:#16213b;border:1px solid var(--line);border-radius:14px;box-shadow:0 8px 28px rgba(22,33,59,.22);padding:10px 10px 10px 12px;max-width:520px;margin:0 auto}.iban[hidden]{display:none}.iban img{border-radius:10px;flex:none}.iban div{flex:1;min-width:0;line-height:1.25}.iban b{display:block;font-size:15px}.iban span{font-size:13px;color:#4a5672}.iban .btn{flex:none;background:#2852b8;border-color:#2852b8;color:#fff;padding:9px 14px;font-size:14px}.iban .x{flex:none;background:none;border:0;font-size:24px;line-height:1;color:#4a5672;cursor:pointer;padding:4px 6px}
.tgx.app{border-left-color:#2852b8}.tgx.app .btn{background:#2852b8;border-color:#2852b8;color:#fff}.tgx.app .sm:empty{display:none}
.tgx{display:flex;gap:18px;align-items:center;justify-content:space-between;flex-wrap:wrap;background:var(--card);border:1px solid var(--line);border-left:4px solid #2aabee;border-radius:6px;padding:18px 22px;margin:0 0 28px}.tgx p{margin:4px 0 0;color:var(--ink2);max-width:560px}.tgx .btn{background:#2aabee;border-color:#2aabee;color:#fff;text-decoration:none}
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
<link rel="canonical" href="{canon}">{('<link rel="alternate" hreflang="fr" href="' + alt_fr + '"><link rel="alternate" hreflang="en" href="' + alt_en + '"><link rel="alternate" hreflang="x-default" href="' + alt_fr + '">') if alt_fr and alt_en and alt_fr != alt_en else ''}
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="website"><meta property="og:image" content="https://adresse-temporaire.fr/og.png"><meta property="og:locale" content="{"fr_FR" if t["lang"] == "fr" else "en_US"}"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#16213b">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="{"Adresse temp" if t["lang"] == "fr" else "Jetbox Mail"}"><script>if("serviceWorker"in navigator)addEventListener("load",function(){{navigator.serviceWorker.register("/sw.js").catch(function(){{}})}})</script>
{FONTS}<style>{CSS}{BCSS}</style>{extra}</head><body><div class="air"></div>"""

def topbar(t, other_href):
    return f"""<div class="wrap"><header class="top"><a class="brand" href="/">adresse<span>-</span>temporaire.fr</a><nav class="nav"><a href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire-menu" target="_blank" rel="sponsored noopener">VPN</a><a href="/blog/">Guides</a><a class="lng" href="{other_href}" hreflang="{"en" if t["lang"] == "fr" else "fr"}" lang="{"en" if t["lang"] == "fr" else "fr"}">{"EN" if t["lang"] == "fr" else "FR"}</a><button class="acct" id="acct" type="button">Mon compte</button></nav></header>"""

def foot(t):
    return f"""<footer><div>{esc(t['rules'])}</div><div class="fl"><a href="/blog/">Guides du mail jetable</a><a href="{t['legal_href']}">{esc(t['legal'])}</a><a href="mailto:contact@{DOMAIN}">{esc(t['report'])}</a><span>&copy; 2026 adresse-temporaire.fr</span></div></footer></div>"""


DIALOG = """<dialog id="dlg" aria-labelledby="dlgt"><div class="dh"><h2 id="dlgt">Mon compte</h2><button class="x" id="dlgx" type="button" aria-label="Fermer">&times;</button></div>
<div class="db" id="s1"><p>Recevez un code par e-mail pour vous connecter. Pas de mot de passe.</p><form id="f1"><label for="em">Votre adresse e-mail</label><input id="em" type="email" autocomplete="email" required placeholder="vous@exemple.fr"><button class="btn" type="submit" id="b1">Recevoir mon code</button><p class="derr" id="e1" role="alert"></p></form></div>
<div class="db" id="s2" hidden><p id="s2t"></p><form id="f2"><label for="cd">Code à 6 chiffres</label><input id="cd" class="code" inputmode="numeric" autocomplete="one-time-code" maxlength="6" required><button class="btn" type="submit" id="b2">Me connecter</button><p class="derr" id="e2" role="alert"></p></form><button class="link sm" id="back1" type="button">Changer d'adresse e-mail</button></div>
<div class="db" id="s3" hidden><div class="plan"><div><b id="pn"></b><div class="sm" id="pd"></div></div><span class="tag" id="ptag"></span></div>
<label>Mes adresses réservées</label><ul class="my" id="my"></ul><p class="sm" id="mye"></p><p class="sm" id="fwdn"></p>
<div class="tgb"><button class="btn ghost" id="tgl" type="button">Recevoir mes e-mails sur Telegram</button><p class="sm" id="tgs"></p></div>
<form id="f3"><div class="row2"><input id="ra" maxlength="40" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="nom-de-votre-choix" aria-label="Adresse à réserver"><button class="btn ghost" type="submit">Réserver</button></div></form>
<p class="derr" id="e3" role="alert"></p>
<a class="btn prem" id="gopro" href="#" target="_blank" rel="noopener">Passer Premium, 2,99 € par mois</a>
<p class="sm" id="me-em"></p><button class="link sm out" id="logout" type="button">Me déconnecter</button></div>
</dialog>"""

JS = r"""
(function(){
var L=__T__,API="__API__",DOMS=["adresse-temporaire.fr","jetboxmail.com"],DOM="__DOM__",GUM="https://jeremstyke.gumroad.com/l/anvfvt",K="at_addr",KT="at_tok",seen={},cur=null,showImgs=false,tm=null,fails=0,acct=null;
var $=function(i){return document.getElementById(i)};
var RX=/^[a-z0-9][a-z0-9._-]{2,39}$/;
function rnd(){var c="abcdefghijkmnpqrstuvwxyz23456789",s="";var a=new Uint32Array(10);crypto.getRandomValues(a);for(var i=0;i<10;i++)s+=c[a[i]%c.length];return s}
function lg(k){try{return localStorage.getItem(k)}catch(e){return null}}
function ls(k,v){try{if(v==null)localStorage.removeItem(k);else localStorage.setItem(k,v)}catch(e){}}
var tok=lg(KT);
function H(x){var h=x||{};if(tok)h.Authorization="Bearer "+tok;return h}
function api(p,o){o=o||{};o.headers=H(o.headers);o.cache="no-store";return fetch(API+p,o).then(function(r){return r.json().then(function(j){j._s=r.status;return j})})}
function post(p,b){return api(p,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(b||{})})}
if(location.hostname==="adresse-temporaire.fr"&&location.pathname==="/"&&/[?&]a=/.test(location.search)&&lg("at_lang")!=="fr"&&!/^fr/i.test(navigator.language||"")){location.replace("https://jetboxmail.com/"+location.search);return}
Array.prototype.forEach.call(document.querySelectorAll("a.lng"),function(x){x.onclick=function(){ls("at_lang",x.getAttribute("hreflang"))}});
var me=lg(K);var qa=(location.search.match(/[?&]a=([a-z0-9._-]{3,40})/)||[])[1];if(qa&&RX.test(qa)){me=qa;ls(K,me)}if(!me||!RX.test(me)){me=rnd();ls(K,me);ping()}
function ping(){try{fetch(API+"/new",{method:"POST"})}catch(e){}}
function full(){return me+"@"+DOM}
function mine(a){return !!(acct&&acct.addrs.indexOf(a)>=0)}
function setAddr(v){me=v;ls(K,v);seen={};cur=null;$("addr").textContent=full();closeView();last=[];render([]);keep();load();if(lg("at_push")==="1")pushSub(false)}
(function(){var d=lg("at_dom");if(d&&DOMS.indexOf(d)>=0)DOM=d})();
function doms(){var pd=$("pickdom");if(pd)pd.textContent="@"+DOM;Array.prototype.forEach.call(document.querySelectorAll("#doms button"),function(b){b.setAttribute("aria-pressed",b.getAttribute("data-d")===DOM?"true":"false");b.onclick=function(){DOM=b.getAttribute("data-d");ls("at_dom",DOM);$("addr").textContent=full();doms();if(acct)fill()}})}doms();
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
  $("err").textContent=L.err;last=j.msgs||[];render(last)}).catch(function(){fails++;if(fails>1){$("err").textContent=L.err;$("err").style.display="block"}})}
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
var acct0=false; // 22 nov 2026 (Jeremy): a signed-in visitor with a reserved address lands on it, not on a random one
function setAcct(a){if(a&&!acct&&lg("at_push")==="1")setTimeout(function(){pushSub(false)},0);acct=a;$("acct").textContent=a?(a.premium?"Mon compte Premium":"Mon compte"):"Mon compte";$("acct").classList.toggle("on",!!a);var first=!!a&&!acct0;acct0=!!a;if(first&&!qa&&a.addrs&&a.addrs.length&&!mine(me)){setAddr(a.addrs[0]);return}keep()}
function fill(){if(!acct)return;$("pn").textContent=acct.premium?"Premium":"Compte gratuit";
 $("pd").textContent=acct.addrs.length+" / "+acct.max+" adresse"+(acct.max>1?"s":"")+" réservée"+(acct.max>1?"s":"")+", messages gardés "+(acct.premium?"30 jours":"24 heures")+(acct.premium&&acct.premium_until?", jusqu'au "+new Date(acct.premium_until).toLocaleDateString("fr-FR"):"");
 $("ptag").textContent=acct.premium?"Premium":"Gratuit";$("ptag").className="tag"+(acct.premium?" p":"");
 var ul=$("my");ul.innerHTML="";$("mye").textContent=acct.addrs.length?"":"Aucune adresse réservée pour l'instant.";
 acct.addrs.forEach(function(a){var li=document.createElement("li");var s=el("span","a"+(a===me?" cur":""),a+"@"+DOM);s.appendChild(document.createElement("br"));s.appendChild(document.createTextNode(a+"@"+(DOM===DOMS[0]?DOMS[1]:DOMS[0])));
  var o=el("button","link sm",a===me?"Ouverte":"Ouvrir");o.type="button";o.disabled=(a===me);o.onclick=function(){setAddr(a);fill();closeDlg()};
  var r=el("button","link sm","Libérer");r.type="button";r.onclick=function(){if(!confirm("Libérer "+a+"@"+DOM+" ? Ses messages seront supprimés."))return;post("/release",{addr:a}).then(function(j){if(j.email){setAcct(j);fill()}})};
  li.appendChild(s);li.appendChild(o);li.appendChild(r);
  if(acct.premium){var se=document.createElement("select");se.setAttribute("aria-label","Transfert de "+a);[["off","Pas de transfert"],["notif","Alerte par e-mail"],["full","Transfert complet"]].forEach(function(p){var op=document.createElement("option");op.value=p[0];op.textContent=p[1];se.appendChild(op)});se.value=(acct.fwd&&acct.fwd[a])||"off";
   se.onchange=function(){post("/fwd",{addr:a,mode:se.value}).then(function(j){if(j.email){acct=j}})};li.appendChild(se)}
  ul.appendChild(li)});
 $("fwdn").textContent=acct.premium&&acct.addrs.length?"Transfert : les messages reçus sont envoyés à "+acct.email+" (alerte simple ou message complet avec pièces jointes), jusqu'à 30 par jour. Au-delà, les messages restent lisibles ici.":"";
 $("tgs").textContent=acct.tg?"Telegram relié : chaque message reçu sur vos adresses réservées arrive aussi dans Telegram"+(acct.premium?", avec ses pièces jointes.":"."):"Gratuit : une alerte Telegram à chaque message reçu sur vos adresses réservées.";$("tgl").textContent=acct.tg?"Relier un autre compte Telegram":"Recevoir mes e-mails sur Telegram";
 $("f3").style.display=acct.addrs.length<acct.max?"block":"none";
 if(!$("ra").value)$("ra").value=mine(me)?"":me;
 var g=$("gopro");g.style.display=acct.premium?"none":"block";g.href=GUM+"?wanted=true&uid="+encodeURIComponent(acct.uid)+"&email="+encodeURIComponent(acct.email);
 $("me-em").textContent="Connecté avec "+acct.email}
function reserve(a){$("e3").textContent="";post("/reserve",{addr:a}).then(function(j){
  if(j.email){setAcct(j);$("ra").value="";if(a!==me)setAddr(a);else keep();fill();return}
  if(j.error==="limit"){openDlg();$("e3").textContent=acct&&acct.premium?ERR.limit:"Le compte gratuit permet 1 adresse. Passez Premium pour en avoir jusqu'à 100.";return}
  if(!dlg.open)openDlg();$("e3").textContent=ERR[j.error]||"Erreur, réessayez."})}
$("f3").onsubmit=function(e){e.preventDefault();var v=$("ra").value.trim().toLowerCase();if(!RX.test(v)){$("e3").textContent=ERR.addr;return}reserve(v)};
$("tgl").onclick=function(){var w=window.open("","_blank");post("/tglink").then(function(j){if(j.url){if(w)w.location=j.url;else location.href=j.url}else if(w)w.close()}).catch(function(){if(w)w.close()})};
$("logout").onclick=function(){post("/logout").finally(function(){tok=null;ls(KT,null);setAcct(null);closeDlg();if(!RX.test(me))setAddr(rnd());load()})};
function refresh(){if(!tok){keep();return Promise.resolve()}return api("/me").then(function(j){if(j.email)setAcct(j);else{tok=null;ls(KT,null);setAcct(null)}}).catch(function(){keep()})}
// alertes à chaque e-mail (notifications du navigateur, même site fermé)
var VK="BCWWlQ7VXaXH1E6Fse0IjuQIZFOlM0URL2X4KAzcY8A1it0NEHDDaIQyhsRbgkS5uOOpXJh7LPjL0GDIXghXVFc",LNG=document.documentElement.lang==="en"?"en":"fr";
var canPush="serviceWorker"in navigator&&"PushManager"in window&&"Notification"in window;
var iosTab=/iP(hone|ad|od)/.test(navigator.userAgent)&&!(navigator.standalone||matchMedia("(display-mode: standalone)").matches);
function u8(x){x=x.replace(/-/g,"+").replace(/_/g,"/");var r=atob(x+"===".slice((x.length+3)%4));return Uint8Array.from(r,function(c){return c.charCodeAt(0)})}
function pushUi(on){var b=$("push");b.hidden=!canPush&&!iosTab;b.textContent=on?L.push_on:L.push_off;b.classList.toggle("on",!!on)}
function pushSub(ask){if(!canPush)return Promise.resolve(false);return navigator.serviceWorker.register("/sw.js").then(function(){return navigator.serviceWorker.ready}).then(function(reg){return reg.pushManager.getSubscription().then(function(x){if(x)return x;if(!ask)return null;return Notification.requestPermission().then(function(p){if(p!=="granted")return null;return reg.pushManager.subscribe({userVisibleOnly:true,applicationServerKey:u8(VK)})})})}).then(function(x){if(!x)return false;return post("/push/sub",{sub:x.toJSON(),addr:RX.test(me)?me:"",lang:LNG}).then(function(j){if(j.error)return false;ls("at_push","1");pushUi(true);return true})}).catch(function(){return false})}
$("push").onclick=function(){var m=$("pushmsg");
 if(!canPush){m.textContent=L.push_ios;return}
 if(lg("at_push")==="1"){navigator.serviceWorker.ready.then(function(reg){return reg.pushManager.getSubscription()}).then(function(x){if(x){post("/push/unsub",{endpoint:x.endpoint});x.unsubscribe()}}).finally(function(){ls("at_push",null);pushUi(false);m.textContent=""});return}
 pushSub(true).then(function(ok){m.textContent=ok?L.push_ok:L.push_no})};
// installer l'appli (PWA)
var standalone=navigator.standalone||matchMedia("(display-mode: standalone)").matches,dip=null;
if(standalone)$("appx").hidden=true;
window.addEventListener("beforeinstallprompt",function(e){e.preventDefault();dip=e});
window.addEventListener("appinstalled",function(){$("appx").hidden=true});
var mob=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent),banOff=+(lg("at_ban")||0)>Date.now();
var mac=/Macintosh/.test(navigator.userAgent)&&/Safari/.test(navigator.userAgent)&&!/Chrome|Chromium|Edg|Firefox/.test(navigator.userAgent);
function showBan(){if(standalone||banOff)return;$("iban").querySelector("b").textContent=mob?L.ban_t:L.ban_pc;$("iban").hidden=false}
if(mob||mac)setTimeout(showBan,2500);
window.addEventListener("beforeinstallprompt",function(){if(!mob)setTimeout(showBan,1500)});
$("ibanx").onclick=function(){$("iban").hidden=true;ls("at_ban",String(Date.now()+14*864e5))};
$("ibanb").onclick=function(){$("iban").hidden=true;if(dip){dip.prompt();dip.userChoice.finally(function(){dip=null});return}$("appx").scrollIntoView({behavior:"smooth",block:"center"});$("appmsg").textContent=/iP(hone|ad|od)/.test(navigator.userAgent)?L.app_ios:mac?L.app_mac:L.app_other};
window.addEventListener("appinstalled",function(){$("iban").hidden=true});
$("appbtn").onclick=function(){if(dip){dip.prompt();dip.userChoice.finally(function(){dip=null});return}$("appmsg").textContent=/iP(hone|ad|od)/.test(navigator.userAgent)?L.app_ios:mac?L.app_mac:L.app_other};
pushUi(lg("at_push")==="1");if(lg("at_push")==="1")pushSub(false);
refresh().then(function(){load();if(/[?&]compte=1/.test(location.search))openDlg();if(tok&&lg("at_push")==="1")pushSub(false)});loop();
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
    h = head(t, t["title"], t["desc"], canon, SITE + "/", "https://jetboxmail.com/",
             '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "WebApplication", "name": "Adresse-Temporaire.fr", "url": SITE + "/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "description": t["desc"], "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "EUR", "name": "Gratuit"}, {"@type": "Offer", "price": "2.99", "priceCurrency": "EUR", "name": "Premium"}]}, ensure_ascii=False) + '</script><script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": t["lang"], "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}, ensure_ascii=False) + "</script>")
    how = "".join(f"<li><b>{esc(a)}</b><p>{esc(b)}</p></li>" for a, b in t["how"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
    HOMECARDS = "".join(card(a) for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True)[:4])
    jsT = {k: t[k] for k in ["copy", "copied", "choose_bad", "from", "ago", "nosubj", "push_off", "push_on", "push_no", "push_ios", "push_ok", "app_ios", "app_other", "ban_t", "ban_pc", "app_mac", "err"]}
    js = JS.replace("__T__", json.dumps(jsT, ensure_ascii=False)).replace("__API__", API).replace("__DOM__", DOMAIN)
    return h + topbar(t, other) + f"""<main>
<h1>{esc(t['h1'])}</h1><p class="lead">{esc(t['lead'])}</p>
<div class="env">
 <div class="addr"><label for="addr" id="addrl">{esc(t['your'])}</label>
  <div class="row"><output id="addr" aria-labelledby="addrl" aria-live="polite">&nbsp;</output><button class="btn" id="copy" type="button">{esc(t['copy'])}</button></div>
  <div class="tools"><button class="link" id="new" type="button">{esc(t['new'])}</button><button class="link" id="choose" type="button" aria-controls="pick">{esc(t['choose'])}</button><button class="link" id="push" type="button" hidden>{esc(t['push_off'])}</button></div><p class="sm" id="pushmsg" role="status"></p>
  <div class="doms" id="doms" role="group" aria-label="{'Domaine' if t['lang'] == 'fr' else 'Domain'}"><span>{'Domaine :' if t['lang'] == 'fr' else 'Domain:'}</span><button type="button" data-d="adresse-temporaire.fr">@adresse-temporaire.fr</button><button type="button" data-d="jetboxmail.com">@jetboxmail.com</button><small>{'même boîte, au choix si un site refuse l\'une des deux' if t['lang'] == 'fr' else 'same inbox, switch if a site refuses one of them'}</small></div>
  <form id="pickform"><div id="pick"><input id="pickin" autocomplete="off" autocapitalize="none" spellcheck="false" maxlength="40" placeholder="{esc(t['choose_ph'])}" aria-label="{esc(t['choose'])}"><span class="dom" id="pickdom">@{DOMAIN}</span><button class="btn ghost" type="submit">{esc(t['choose_ok'])}</button><span id="pickerr" role="alert"></span></div></form>
  <p class="keep" id="keep"></p>
 </div>
 <div class="box">
  <div id="listwrap"><div class="boxh"><span>{esc(t['inbox'])}</span><span class="live"><i></i>{esc(t['live'])}</span></div>
   <div id="err" role="status"></div>
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
 <div><h3>Compte gratuit</h3><p class="pr">0 €</p><ul><li>1 adresse réservée à votre nom (libérée après 30 jours sans aucun message reçu)</li><li>Privée : vous seul lisez ses messages</li><li>Messages gardés 24 heures</li><li>Alerte sur Telegram à chaque message</li></ul><button class="btn ghost" type="button" data-acct>Créer mon compte</button></div>
 <div class="hi"><h3>Premium</h3><p class="pr">2,99 € <small>par mois</small></p><ul><li>Jusqu'à 100 adresses réservées et privées</li><li>Messages transférés vers votre vraie boîte, ou simple alerte par e-mail (30 par jour)</li><li>Messages gardés 30 jours</li><li>Pièces jointes conservées (10 Mo par message), reçues aussi sur Telegram</li><li>Sans engagement</li></ul><button class="btn" type="button" data-acct>Passer Premium</button></div>
</div></section>
<div class="iban" id="iban" hidden role="region" aria-label="{esc(t['ban_t'])}"><img src="/icon-192.png" alt="" width="44" height="44"><div><b>{esc(t['ban_t'])}</b><span>{esc(t['ban_p'])}</span></div><button class="btn" id="ibanb" type="button">{esc(t['ban_b'])}</button><button class="x" id="ibanx" type="button" aria-label="{esc(t['ban_x'])}">&times;</button></div>
<aside class="tgx app" id="appx"><div><b>{esc(t['app_t'])}</b><p>{esc(t['app_p'])}</p><p class="sm" id="appmsg" role="status"></p></div><button class="btn" id="appbtn" type="button">{esc(t['app_b'])}</button></aside>
<aside class="tgx"><div><b>Aussi sur Telegram</b><p>Le bot Temp Mail Inbox vous donne une adresse jetable et affiche vos codes de confirmation directement dans Telegram. Gratuit, sans inscription. Déjà inscrit ici ? Reliez votre compte depuis « Mon compte ».</p></div><a class="btn" href="https://t.me/JetboxMailBot?start=src_site" target="_blank" rel="noopener">Ouvrir le bot Telegram</a></aside>
<section class="c"><h2>{esc(t['how_h'])}</h2><ol class="steps">{how}</ol></section>
<section class="c"><h2>{esc(t['why_h'])}</h2><p>{esc(t['why'])}</p></section>
<section class="c"><h2>Guides du mail jetable</h2><div class="posts home">{HOMECARDS}</div><p class="more"><a class="btn ghost" href="/blog/">Voir tous les guides</a></p></section>
<section class="c"><h2>{esc(t['faq_h'])}</h2>{faq}</section>
<section class="c"><aside class="vpn"><span class="sp">Partenaire</span><b>Protégez aussi votre connexion</b><p>Le mail jetable protège votre adresse. Sur un Wi-Fi public ou pour masquer votre adresse IP, un VPN chiffre tout votre trafic. Nous recommandons NordVPN.</p><a class="btn ghost" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=adresse-temporaire" target="_blank" rel="sponsored noopener">Découvrir NordVPN</a><small>Lien affilié : nous touchons une commission si vous vous abonnez, sans surcoût pour vous.</small></aside></section>
</main>""" + foot(t) + DIALOG + f"<script>{js}</script></body></html>"

LEGAL_FR = f"""<main><h1>Mentions légales et confidentialité</h1>
<section class="c"><h2>Éditeur</h2><p>Le site adresse-temporaire.fr est édité par Jérémy Dacier-Jury, entrepreneur individuel (immatriculation en cours). Contact : <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Hébergement</h2><p>Pages du site : GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis. Réception des e-mails : Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis. Stockage temporaire des messages : Supabase, Inc., 970 Toa Payoh North #07-04, Singapour.</p></section>
<section class="c"><h2>Fonctionnement et conservation</h2><p>Les adresses servent uniquement à recevoir des messages. Sans compte, chaque message est conservé une heure au maximum. Sur une adresse réservée, il est conservé 24 heures (compte gratuit) ou 30 jours (Premium), puis supprimé définitivement. Avec le compte gratuit, une adresse réservée qui ne reçoit aucun message pendant 30 jours est libérée et peut être reprise par quelqu'un d'autre ; en Premium, vos adresses restent à vous tant que l'abonnement est actif. En Premium, les pièces jointes sont conservées avec le message, et si vous l'activez, chaque message reçu est transféré (ou signalé) à l'adresse e-mail de votre compte, via Resend, dans la limite de 30 transferts par jour. Si vous reliez votre compte à notre bot Telegram (@JetboxMailBot), chaque message reçu sur vos adresses réservées vous est aussi envoyé dans Telegram (Telegram FZ-LLC), qui conserve alors une copie dans votre conversation avec le bot. L'adresse que vous utilisez et votre session sont gardées dans votre navigateur (stockage local).</p></section>
<section class="c"><h2>Comptes</h2><p>Si vous créez un compte, nous conservons votre adresse e-mail, vos adresses réservées et la date de fin de votre Premium, tant que le compte existe. Les codes de connexion sont envoyés par Resend (Resend, Inc., États-Unis). Le paiement du Premium est géré par Gumroad (Gumroad, Inc., États-Unis), qui nous transmet uniquement l'e-mail d'achat et le statut de l'abonnement. Si vous reliez Telegram, nous conservons aussi votre identifiant Telegram et la langue de votre application. Le Premium acheté dans le bot est payé en étoiles Telegram, géré par Telegram. Pour supprimer votre compte, écrivez à <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Liens affiliés</h2><p>Certains liens du site sont des liens affiliés (NordVPN) : si vous vous abonnez via ces liens, nous touchons une commission, sans surcoût pour vous. Ils sont signalés par la mention « Partenaire » ou « Lien affilié ».</p></section>
<section class="c"><h2>Cookies et statistiques</h2><p>Le site n'utilise pas de cookies. Seul un compteur anonyme du nombre d'adresses créées et de messages reçus par jour est tenu, sans adresse IP ni identifiant.</p></section>
<section class="c"><h2>Usage interdit et signalement</h2><p>Il est interdit d'utiliser ce service pour une fraude, du harcèlement, l'usurpation d'identité ou toute activité illégale. Pour signaler un abus ou un contenu illicite, écrivez à <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a> en indiquant l'adresse concernée. Les contenus signalés sont supprimés sans délai.</p></section>
<section class="c"><h2>Vos droits</h2><p>Conformément au RGPD, vous pouvez demander l'accès ou la suppression de données vous concernant à l'adresse de contact ci-dessus. Les messages étant effacés au bout d'une heure, il est en général impossible d'en fournir une copie après ce délai.</p></section></main>"""

LEGAL_EN = f"""<main><h1>Legal notice and privacy</h1>
<section class="c"><h2>Publisher</h2><p>adresse-temporaire.fr is published by Jérémy Dacier-Jury, sole trader (registration in progress), France. Contact: <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Hosting</h2><p>Site pages: GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Email reception: Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, USA. Temporary message storage: Supabase, Inc., 970 Toa Payoh North #07-04, Singapore.</p></section>
<section class="c"><h2>How it works and retention</h2><p>Addresses can only receive messages. Without an account, each message is kept for one hour at most. On a reserved address, it is kept for 24 hours (free account) or 30 days (Premium), then permanently deleted. With a free account, a reserved address that receives no message for 30 days is released and can be taken by someone else; with Premium, your addresses stay yours while the subscription is active. With Premium, attachments are kept with the message and, if you turn it on, each message received is forwarded (or announced) to your account email address through Resend, up to 30 forwards per day. If you link your account to our Telegram bot (@JetboxMailBot), each message received on your reserved addresses is also sent to you in Telegram (Telegram FZ-LLC), which then keeps a copy in your chat with the bot. The address you use and your session are stored in your browser (local storage).</p></section>
<section class="c"><h2>Accounts</h2><p>If you create an account, we keep your email address, your reserved addresses and your Premium end date for as long as the account exists. Sign-in codes are sent by Resend (Resend, Inc., USA). Premium payment is handled by Gumroad (Gumroad, Inc., USA), which only sends us the purchase email and the subscription status. If you link Telegram, we also keep your Telegram ID and app language. Premium bought in the bot is paid in Telegram Stars, handled by Telegram. To delete your account, email <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a>.</p></section>
<section class="c"><h2>Affiliate links</h2><p>Some links on the site are affiliate links (NordVPN): if you subscribe through them, we earn a commission at no extra cost to you. They are marked \u201cPartner\u201d or \u201cAffiliate link\u201d.</p></section>
<section class="c"><h2>Cookies and statistics</h2><p>The site uses no cookies. Only an anonymous daily count of addresses created and messages received is kept, with no IP address or identifier.</p></section>
<section class="c"><h2>Forbidden use and reporting</h2><p>Using this service for fraud, harassment, impersonation or any illegal activity is forbidden. To report abuse or illegal content, email <a href="mailto:contact@{DOMAIN}">contact@{DOMAIN}</a> with the address concerned. Reported content is removed without delay.</p></section>
<section class="c"><h2>Your rights</h2><p>Under the GDPR, you can request access to or deletion of data about you at the contact address above. Since messages are erased automatically, a copy usually cannot be provided once they have expired.</p></section></main>"""

def legal(t, body, path, title):
    canon = SITE + path
    return head(t, title, title, canon, SITE + "/mentions-legales.html", SITE + "/en/legal.html", '<meta name="robots" content="noindex,follow">') + topbar(t, t["other"]) + body + foot(t) + "</body></html>"

def w(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

w("index.html", index(T["fr"]))
w("mentions-legales.html", legal(T["fr"], LEGAL_FR, "/mentions-legales.html", "Mentions légales et confidentialité | Adresse-Temporaire.fr"))
# ---------------- VERSION ANGLAISE (/en/) : la page d'accueil et les mentions, sans les guides (en français) ----------------
GUM_EN = "https://jeremstyke.gumroad.com/l/jssxfa"  # offre Premium en anglais, 2,99 dollars par mois
EN_REPL = [
 ('href="/blog/">Guides</a>', 'href="/blog/" hreflang="fr">Guides (FR)</a>'),
 ("Partenaire recommandé", "Recommended partner"),
 ("Votre adresse est cachée. Et votre connexion ?", "Your address is hidden. What about your connection?"),
 ("Sur un Wi-Fi public, à l'hôtel ou au café, n'importe qui peut espionner ce que vous faites. NordVPN chiffre tout votre trafic et masque votre adresse IP, sur téléphone comme sur ordinateur.", "On public Wi-Fi, at a hotel or a café, anyone can snoop on what you do. NordVPN encrypts all your traffic and hides your IP address, on your phone and your computer."),
 ("Protéger ma connexion avec NordVPN", "Protect my connection with NordVPN"),
 ("Lien affilié, sans surcoût pour vous.", "Affiliate link, no extra cost for you."),
 ("source=adresse-temporaire-accueil", "source=adresse-temporaire-en-home"),
 ("source=adresse-temporaire-menu", "source=adresse-temporaire-en-menu"),
 ("source=adresse-temporaire\"", "source=adresse-temporaire-en\""),
 ("<h2>Gratuit ou Premium</h2>", "<h2>Free or Premium</h2>"),
 ('<p class="pr">0 €</p>', '<p class="pr">$0</p>'),
 ('<a class="brand" href="/">', '<a class="brand" href="/en/">'),
 ("<h3>Sans compte</h3>", "<h3>No account</h3>"),
 ("<li>Une adresse jetable tout de suite</li><li>Messages effacés après 1 heure</li><li>Boîte publique : toute personne qui connaît l'adresse peut la lire</li>", "<li>A disposable address right away</li><li>Messages erased after 1 hour</li><li>Public inbox: anyone who knows the address can read it</li>"),
 ("<h3>Compte gratuit</h3>", "<h3>Free account</h3>"),
 ("<li>1 adresse réservée à votre nom (libérée après 30 jours sans aucun message reçu)</li><li>Privée : vous seul lisez ses messages</li><li>Messages gardés 24 heures</li><li>Alerte sur Telegram à chaque message</li>", "<li>1 address reserved for you (released after 30 days without any message)</li><li>Private: only you can read its messages</li><li>Messages kept 24 hours</li><li>Telegram alert for every message</li>"),
 ("Créer mon compte", "Create my account"),
 ('2,99 € <small>par mois</small>', '$2.99 <small>per month</small>'),
 ("<li>Jusqu'à 100 adresses réservées et privées</li><li>Messages transférés vers votre vraie boîte, ou simple alerte par e-mail (30 par jour)</li><li>Messages gardés 30 jours</li><li>Pièces jointes conservées (10 Mo par message), reçues aussi sur Telegram</li><li>Sans engagement</li>", "<li>Up to 100 reserved, private addresses</li><li>Messages forwarded to your real inbox, or a simple email alert (30 per day)</li><li>Messages kept 30 days</li><li>Attachments kept (10 MB per message), also delivered on Telegram</li><li>Cancel anytime</li>"),
 ("Passer Premium, 2,99 € par mois", "Go Premium, $2.99 per month"),
 ("Passer Premium", "Go Premium"),
 ("<b>Aussi sur Telegram</b><p>Le bot Temp Mail Inbox vous donne une adresse jetable et affiche vos codes de confirmation directement dans Telegram. Gratuit, sans inscription. Déjà inscrit ici ? Reliez votre compte depuis « Mon compte ».</p>", "<b>Also on Telegram</b><p>The Temp Mail Inbox bot gives you a disposable address and shows your verification codes right inside Telegram. Free, no sign-up. Already have an account here? Link it from \u201cMy account\u201d.</p>"),
 ("Ouvrir le bot Telegram", "Open the Telegram bot"),
 ("start=src_site", "start=src_site_en"),
 ("<b>Protégez aussi votre connexion</b><p>Le mail jetable protège votre adresse. Sur un Wi-Fi public ou pour masquer votre adresse IP, un VPN chiffre tout votre trafic. Nous recommandons NordVPN.</p>", "<b>Protect your connection too</b><p>A disposable email protects your address. On public Wi-Fi or to hide your IP address, a VPN encrypts all your traffic. We recommend NordVPN.</p>"),
 ("Découvrir NordVPN", "Discover NordVPN"),
 ("Lien affilié : nous touchons une commission si vous vous abonnez, sans surcoût pour vous.", "Affiliate link: we earn a commission if you subscribe, at no extra cost to you."),
 ('<span class="sp">Partenaire</span>', '<span class="sp">Partner</span>'),
 ("Guides du mail jetable</a>", "Guides (in French)</a>"),
 # fenêtre Mon compte
 ("Mon compte", "My account"),
 ('aria-label="Fermer"', 'aria-label="Close"'),
 ("Recevez un code par e-mail pour vous connecter. Pas de mot de passe.", "Get a code by email to sign in. No password."),
 ("Votre adresse e-mail", "Your email address"), ('placeholder="vous@exemple.fr"', 'placeholder="you@example.com"'),
 ("Recevoir mon code", "Send me my code"), ("Code à 6 chiffres", "6-digit code"), ("Me connecter", "Sign in"),
 ("Changer d'adresse e-mail", "Use another email address"),
 ("Mes adresses réservées", "My reserved addresses"), ('placeholder="nom-de-votre-choix"', 'placeholder="name-of-your-choice"'),
 ('aria-label="Adresse à réserver"', 'aria-label="Address to reserve"'), (">Réserver</button>", ">Reserve</button>"),
 ("Me déconnecter", "Sign out"),
 ("Recevoir mes e-mails sur Telegram", "Get my emails on Telegram"),
 # textes du script
 ('"il y a "+Math.floor(d/1440)+" j"', 'Math.floor(d/1440)+" d ago"'),
 ('"Adresse privée"', '"Private address"'),
 ('" : réservée à votre compte, messages gardés "+(acct.premium?"30 jours":"24 heures")+"."', '": reserved for your account, messages kept "+(acct.premium?"30 days":"24 hours")+"."'),
 ('"Seul votre compte peut lire cette boîte."', '"Only your account can read this inbox."'),
 ('"Réserver cette adresse":"Garder cette adresse et la rendre privée"', '"Reserve this address":"Keep this address and make it private"'),
 ('" (compte gratuit)"', '" (free account)"'),
 ('"Cette adresse est réservée par un autre compte. Choisissez-en une autre."', '"This address is reserved by another account. Pick another one."'),
 ('" Mo":', '" MB":'), ('" Ko"', '" KB"'), ('"piece-jointe"', '"attachment"'),
 ('"Téléchargement impossible."', '"Download failed."'),
 ('{email:"Adresse e-mail invalide.",rate:"Trop de tentatives. Réessayez dans un moment.",send:"Le code n\'a pas pu être envoyé. Réessayez.",expired:"Code expiré. Demandez-en un nouveau.",code:"Code incorrect.",limit:"Limite atteinte pour votre offre.",taken:"Cette adresse est déjà réservée par quelqu\'un d\'autre.",addr:"3 à 40 caractères : lettres, chiffres, point, tiret."}',
  '{email:"Invalid email address.",rate:"Too many attempts. Try again in a moment.",send:"The code could not be sent. Try again.",expired:"Code expired. Ask for a new one.",code:"Wrong code.",limit:"Your plan limit is reached.",taken:"This address is already reserved by someone else.",addr:"3 to 40 characters: letters, numbers, dot, dash."}'),
 ('"Code envoyé à "+email+". Pensez à regarder dans les spams."', '"Code sent to "+email+". Check your spam folder too."'),
 ('"Erreur, réessayez."', '"Error, try again."'), ('"Connexion impossible."', '"Can\'t connect."'),
 ('"My account Premium"', '"My Premium account"'),
 ('"Premium":"Compte gratuit"', '"Premium":"Free account"'),
 ('" adresse"+(acct.max>1?"s":"")+" réservée"+(acct.max>1?"s":"")+", messages gardés "+(acct.premium?"30 jours":"24 heures")+(acct.premium&&acct.premium_until?", jusqu\'au "+new Date(acct.premium_until).toLocaleDateString("fr-FR"):"")',
  '" reserved address"+(acct.max>1?"es":"")+", messages kept "+(acct.premium?"30 days":"24 hours")+(acct.premium&&acct.premium_until?", until "+new Date(acct.premium_until).toLocaleDateString("en-GB"):"")'),
 ('"Premium":"Gratuit"', '"Premium":"Free"'),
 ('"Aucune adresse réservée pour l\'instant."', '"No reserved address yet."'),
 ('"Ouverte":"Ouvrir"', '"Open now":"Open"'), ('"Libérer"', '"Release"'),
 ('"Libérer "+a+"@"+DOM+" ? Ses messages seront supprimés."', '"Release "+a+"@"+DOM+"? Its messages will be deleted."'),
 ('"Transfert de "+a', '"Forwarding for "+a'),
 ('[["off","Pas de transfert"],["notif","Alerte par e-mail"],["full","Transfert complet"]]', '[["off","No forwarding"],["notif","Email alert"],["full","Full forwarding"]]'),
 ('"Transfert : les messages reçus sont envoyés à "+acct.email+" (alerte simple ou message complet avec pièces jointes), jusqu\'à 30 par jour. Au-delà, les messages restent lisibles ici."', '"Forwarding: received messages are sent to "+acct.email+" (simple alert or full message with attachments), up to 30 per day. Beyond that, messages stay readable here."'),
 ('"Telegram relié : chaque message reçu sur vos adresses réservées arrive aussi dans Telegram"+(acct.premium?", avec ses pièces jointes.":"."):"Gratuit : une alerte Telegram à chaque message reçu sur vos adresses réservées."', '"Telegram linked: every message received on your reserved addresses also arrives in Telegram"+(acct.premium?", with its attachments.":"."):"Free: a Telegram alert for every message received on your reserved addresses."'),
 ('"Relier un autre compte Telegram":"Get my emails on Telegram"', '"Link another Telegram account":"Get my emails on Telegram"'),
 ('"Connecté avec "', '"Signed in as "'),
 ('"Le compte gratuit permet 1 adresse. Passez Premium pour en avoir jusqu\'à 100."', '"The free account allows 1 address. Go Premium for up to 100."'),
]
def index_en():
    t = T["en"]
    h = index(t)
    i = h.index('<section class="c"><h2>Guides du mail jetable</h2>'); h = h[:i] + h[h.index('</section>', i) + 10:]
    h = h.replace('"name": "Gratuit"', '"name": "Free"')
    for a, b in EN_REPL:
        assert a in h, ("EN manquant", a[:60])
        h = h.replace(a, b)
    h = h.replace('GUM="https://jeremstyke.gumroad.com/l/anvfvt"', 'GUM="' + GUM_EN + '"').replace('"inLanguage": "fr"', '"inLanguage": "en"').replace('"priceCurrency": "EUR", "name": "Premium"', '"priceCurrency": "USD", "name": "Premium"')
    return h
JET = "https://jetboxmail.com"
def jetify(h):
    h = h.replace('<a class="brand" href="/en/">adresse<span>-</span>temporaire.fr</a>', '<a class="brand" href="/">jetbox<span>mail</span>.com</a>')
    h = h.replace(SITE + "/en/legal.html", JET + "/legal.html").replace('href="/en/legal.html"', 'href="/legal.html"')
    h = h.replace('<link rel="canonical" href="' + SITE + '/en/">', '<link rel="canonical" href="' + JET + '/">').replace('<meta property="og:url" content="' + SITE + '/en/">', '<meta property="og:url" content="' + JET + '/">')
    h = h.replace('href="/blog/" hreflang="fr">Guides (FR)</a>', 'href="/guides/">Guides</a>').replace('<a href="/blog/">Guides (in French)</a>', '<a href="/guides/">Disposable email guides</a>')
    h = h.replace('<a class="lng" href="/" hreflang="fr"', '<a class="lng" href="' + SITE + '/" hreflang="fr"')
    h = h.replace('DOM="adresse-temporaire.fr"', 'DOM="jetboxmail.com"').replace("&copy; 2026 adresse-temporaire.fr", "&copy; 2026 jetboxmail.com")
    h = h.replace("Adresse-Temporaire.fr", "Jetbox Mail").replace('"url": "' + SITE + '/"', '"url": "' + JET + '/"')
    h = h.replace("post(\"/auth/start\",{email:email})", "post(\"/auth/start\",{email:email,lang:\"en\"})")
    h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex">', 1)
    return h
EN_HOME = index_en()
w("jet/index.html", jetify(EN_HOME))
w("jet/legal.html", jetify(legal(T["en"], LEGAL_EN, "/en/legal.html", "Legal notice and privacy | Adresse-Temporaire.fr").replace("Mon compte", "My account").replace('href="/blog/">Guides</a>', 'href="/blog/" hreflang="fr">Guides (FR)</a>').replace("Guides du mail jetable</a>", "Guides (in French)</a>").replace('<a class="brand" href="/">', '<a class="brand" href="/en/">')))
w("jet/404.html", jetify(head(T["en"], "Page not found | Jetbox Mail", "Page not found", SITE + "/en/", "", "", "") + topbar(T["en"], "/") + '<main><h1>This page does not exist.</h1><p class="lead"><a href="/">Get a disposable email address</a></p></main>' + foot(T["en"]) + "</body></html>").replace("Mon compte", "My account").replace('<a class="brand" href="/">adresse<span>-</span>temporaire.fr</a>', '<a class="brand" href="/">jetbox<span>mail</span>.com</a>'))
# ---------------- GUIDES ANGLAIS (jetboxmail.com/guides/) ----------------
from guides_en import GUIDES_EN
import datetime as _dt, re
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
def edate(d):
    y, m, dd = map(int, d.split("-")); return f"{MONTHS[m-1]} {dd}, {y}"
def jcard(a):
    return f'<div class="post"><span class="cat">{esc(a["cat"])}</span><h3 class="pt"><a href="/guides/{a["slug"]}/">{esc(a["title"])}</a></h3><p>{esc(a["desc"])}</p><span class="meta">{edate(a["date"])}, {rtime(a["body"])} min read</span></div>'
JCTA = '<div class="cta"><b>Need an address right now?</b><p>Your disposable address is ready on the home page, no sign-up needed.</p><a class="btn" href="/">Get my temporary email</a></div>'
def jpage(title, desc, canon, schema, body, art=False):
    ld = "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in schema)
    h = head(T["en"], title, desc, canon, "", "", ld) + topbar(T["en"], "/") + body + foot(T["en"]) + "</body></html>"
    h = h.replace("Mon compte", "My account").replace('<button class="acct" id="acct" type="button">My account</button>', '<a class="acct" href="/?compte=1" style="text-decoration:none">My account</a>')
    h = h.replace('<a class="brand" href="/">adresse<span>-</span>temporaire.fr</a>', '<a class="brand" href="/">jetbox<span>mail</span>.com</a>').replace('<a href="/blog/">Guides</a>', '<a href="/guides/">Guides</a>')
    h = h.replace('<a class="lng" href="/" hreflang="fr" lang="fr">FR</a>', '<a class="lng" href="' + SITE + '/" hreflang="fr" lang="fr">FR</a>')
    h = h.replace('<a href="/blog/">Guides du mail jetable</a>', '<a href="/guides/">Disposable email guides</a>').replace("&copy; 2026 adresse-temporaire.fr", "&copy; 2026 jetboxmail.com")
    h = h.replace('href="/en/legal.html"', 'href="/legal.html"')
    if art: h = h.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
    h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex">', 1)  # retiré par le worker sur jetboxmail.com
    return h
garts = sorted(GUIDES_EN, key=lambda a: (a["date"], a["slug"]), reverse=True)
assert len({a["slug"] for a in garts}) == len(garts), "slug en double"
for a in garts:
    assert "\u2014" not in a["body"] + a["title"] + a["desc"] and "\u2013" not in a["body"] + a["title"] + a["desc"], "tiret long dans " + a["slug"]
    assert len(a["title"]) <= 65, "title trop long " + a["slug"]
    for l in re.findall(r'href="/guides/([^"/]+)/"', a["body"]):
        assert any(o["slug"] == l for o in garts), "lien cassé " + a["slug"] + " -> " + l
crumb = lambda extra: {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": JET + "/"}, {"@type": "ListItem", "position": 2, "name": "Guides", "item": JET + "/guides/"}] + extra}
w("jet/guides/index.html", jpage("Disposable Email Guides: Temp Mail Tips and Answers", "Guides to temp mail and disposable email addresses: how they work, how to stay safe, how to keep the same address and answers to the questions people ask most.", JET + "/guides/",
  [{"@context": "https://schema.org", "@type": "Blog", "name": "Disposable email guides", "url": JET + "/guides/", "inLanguage": "en", "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f'{JET}/guides/{a["slug"]}/', "datePublished": a["date"]} for a in garts]}, crumb([])],
  f"""<main><div class="bh"><p class="kick">Jetbox Mail guides</p><h1>Disposable email guides</h1><p class="lead">How temp mail works, how to keep your real inbox out of reach, and straight answers to the questions people ask us most.</p></div><div class="posts">{"".join(jcard(a) for a in garts)}</div>{JCTA}</main>"""))
for a in garts:
    url = f'{JET}/guides/{a["slug"]}/'
    rel = "".join(f'<li><a href="/guides/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in [o for o in garts if o["slug"] != a["slug"]][:4])
    body = a["body"].strip(); first, rest = body.split("</p>", 1)
    sch = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "datePublished": a["date"], "dateModified": a.get("updated", a["date"]), "inLanguage": "en", "mainEntityOfPage": url, "image": SITE + "/og.png", "author": {"@type": "Organization", "name": "Jetbox Mail", "url": JET + "/"}, "publisher": {"@type": "Organization", "name": "Jetbox Mail", "url": JET + "/"}}, crumb([{"@type": "ListItem", "position": 3, "name": a["title"], "item": url}])]
    w(f'jet/guides/{a["slug"]}/index.html', jpage(a["title"] if len(a["title"]) > 42 else a["title"] + " | Jetbox Mail", a["desc"], url, sch, f"""<main><article class="art">
<p class="crumb"><a href="/">Home</a> / <a href="/guides/">Guides</a> / {esc(a["cat"])}</p>
<h1>{esc(a["title"])}</h1><p class="meta">Published {edate(a["date"])}, {rtime(body)} min read</p>
{first.replace('<p>', '<p class="lead">', 1)}</p><aside class="vpnb"><div><span class="sp">Recommended partner</span><b>Your address is hidden. What about your connection?</b><p>On public Wi-Fi, at a hotel or a café, anyone can snoop on what you do. NordVPN encrypts all your traffic and hides your IP address, on your phone and your computer.</p></div><a class="btn vb" href="https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=155375&amp;source=jetboxmail-guide" target="_blank" rel="sponsored noopener">Protect my connection with NordVPN</a><small>Affiliate link, no extra cost for you.</small></aside>{rest}
{JCTA}
<div class="rel"><h2>Read next</h2><ul>{rel}</ul></div>
</article></main>""", art=True))
# accueil anglais : derniers guides
_jh = open(os.path.join(ROOT, "jet/index.html")).read()
_jh = _jh.replace("</main><footer>", f'<section class="c"><h2>Disposable email guides</h2><div class="posts home">{"".join(jcard(a) for a in garts[:3])}</div><p class="more"><a class="btn ghost" href="/guides/">See all guides</a></p></section></main><footer>', 1)
w("jet/index.html", _jh)
w("jet/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {JET}/sitemap.xml\n")
w("jet/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{JET}/</loc><priority>1.0</priority></url><url><loc>{JET}/guides/</loc><priority>0.8</priority></url>' + "".join(f'<url><loc>{JET}/guides/{a["slug"]}/</loc><lastmod>{a.get("updated", a["date"])}</lastmod><priority>0.7</priority></url>' for a in garts) + f'<url><loc>{JET}/legal.html</loc><priority>0.2</priority></url></urlset>\n')
w("jet/site.webmanifest", json.dumps({"id": "/", "name": "Jetbox Mail", "short_name": "Jetbox Mail", "description": "Free disposable email address. Get verification codes without giving your real email.", "lang": "en", "start_url": "/?source=pwa", "scope": "/", "display": "standalone", "orientation": "portrait", "theme_color": "#16213b", "background_color": "#1d3c94", "categories": ["utilities", "productivity"], "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}, {"src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, ensure_ascii=False))
import shutil
for f in ["favicon.ico", "favicon.svg", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "icon-maskable-512.png", "sw.js"]:
    shutil.copy(f, "jet/" + f)
# l'ancienne page anglaise renvoie vers jetboxmail.com
REDIR = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="{u}"><meta http-equiv="refresh" content="0;url={u}"><title>Jetbox Mail</title><script>location.replace("{u}"+location.search)</script></head><body><a href="{u}">jetboxmail.com</a></body></html>'
w("en/index.html", REDIR.replace("{u}", JET + "/"))
# lien court vers l'offre partenaire (messages de bienvenue, bot) : adresse-temporaire.fr/vpn et jetboxmail.com/vpn
VPN_AFF = "https://go.nordvpn.net/aff_c?offer_id=15&aff_id=155375&source=adresse-temporaire-bienvenue"
_vpn = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=' + VPN_AFF.replace("&", "&amp;") + '"><title>NordVPN</title><script>location.replace("' + VPN_AFF + '")</script></head><body><a href="' + VPN_AFF.replace("&", "&amp;") + '" rel="sponsored">NordVPN</a></body></html>'
w("vpn/index.html", _vpn); w("jet/vpn/index.html", _vpn)
w("en/legal.html", REDIR.replace("{u}", JET + "/legal.html"))
w("CNAME", DOMAIN + "\n")
w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
w(".nojekyll", "")
w("site.webmanifest", json.dumps({"id": "/", "name": "Adresse-Temporaire.fr", "short_name": "Adresse temp", "description": "Adresse mail jetable gratuite. Recevez vos codes sans donner votre vraie adresse.", "lang": "fr", "start_url": "/?source=pwa", "scope": "/", "display": "standalone", "orientation": "portrait", "theme_color": "#16213b", "background_color": "#1d3c94", "categories": ["utilities", "productivity"], "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}, {"src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, ensure_ascii=False))
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
w("blog/index.html", bhead("Guides du mail jetable et de l'adresse mail temporaire", "Nos guides pour bien utiliser un mail jetable : créer une adresse mail temporaire, éviter les spams, alias Gmail, sécurité et réponses aux questions fréquentes.", SITE + "/blog/", bl_schema) + btop() + f"""<main><div class="bh"><p class="kick">Le blog d'adresse-temporaire.fr</p><h1>Guides du mail jetable</h1><p class="lead">Comment protéger votre vraie boîte mail, quand utiliser une adresse temporaire, et les réponses aux questions qu'on nous pose le plus.</p></div>
<div class="posts">{cards}</div>{CTA}</main>""" + bfoot())

for a in arts:
    url = f'{SITE}/blog/{a["slug"]}/'
    others = [o for o in arts if o["slug"] != a["slug"]][:4]
    rel = "".join(f'<li><a href="/blog/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in others)
    sch = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "fr", "mainEntityOfPage": url, "image": SITE + "/og.png", "author": {"@type": "Organization", "name": "Adresse-Temporaire.fr", "url": SITE + "/"}, "publisher": {"@type": "Organization", "name": "Adresse-Temporaire.fr", "url": SITE + "/"}},
           {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/blog/"}, {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]}]
    body = a["body"].strip()
    first, rest = body.split("</p>", 1)
    html = bhead(a["title"] if len(a["title"]) > 42 else a["title"] + " | Adresse-Temporaire.fr", a["desc"], url, sch).replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">') + btop() + f"""<main><article class="art">
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
# vérification Google Search Console de jetboxmail.com sur toutes les pages anglaises
for _d, _s, _fs in os.walk(os.path.join(ROOT, "jet")):
    for _f in _fs:
        if _f.endswith(".html"):
            _p = os.path.join(_d, _f); _h = open(_p).read()
            _h = _h.replace('<meta name="google-site-verification" content="zOVKFpJBh1jvzMQHPHjjrzCtxGgENVeCLLiVSmmgdzg">', '<meta name="google-site-verification" content="YRyT8TIFGofnyG1bvcECIIZoKJFyJ_LC3cA9w4c7yek">')
            open(_p, "w").write(_h)
