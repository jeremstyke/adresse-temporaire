# English guides for jetboxmail.com (built into jet/guides/ by build.py).
# One guide per weekday, Monday to Friday, written by the scheduled task. See KEYWORDS-EN.md for the topic queue.
# RULES: 900 to 1300 words, American English, several H2 written as real questions, one table or concrete list,
# "Frequently asked questions" block with H3, links to 1 or 2 existing guides (/guides/<slug>/), never an em dash or en dash.
# Product facts (keep them exact): no account = public inbox, messages erased after 1 hour; free account = 1 private reserved
# address (released after 30 days without any message), messages kept 24 hours, Telegram alerts; Premium $2.99/month =
# up to 100 private addresses, forwarding to your real inbox or email alert (30 per day), messages kept 30 days, attachments
# up to 10 MB. Receive only, sending is impossible. Two domains, same inbox: @jetboxmail.com and @adresse-temporaire.fr.

GUIDES_EN = [
{
"slug": "what-is-temp-mail",
"title": "What Is Temp Mail? How a Disposable Email Works",
"desc": "What is temp mail, how does a disposable email address work, and when should you use one? A plain guide to the benefits, the limits and the safe habits.",
"date": "2026-11-21",
"cat": "The basics",
"body": """
<p><strong>Temp mail</strong> is an email address you use for a short time and then forget. It receives real messages, verification codes and confirmation links, but it is not tied to your name, your phone number or your main inbox. You open a page, an address is already waiting, and you paste it wherever a form asks for an email.</p>
<p>People also call it a disposable email, a throwaway address or a burner email. The idea is the same in every case: give a website something that works today, without handing over the address you will still be using in ten years.</p>
<h2>How does a disposable email address actually work?</h2>
<p>A temp mail service owns one or more domain names, like <code>jetboxmail.com</code>. It accepts every message sent to any name on that domain and shows it on a web page. When you open the site, it simply picks a random name for you, for example <code>k7xq2mfa9p@jetboxmail.com</code>, and watches for mail sent to it.</p>
<p>There is no account to create, because the address does not need one. The service never sends anything from it either: it only receives. That is a big part of why these addresses exist. They are a mailbox with a front door and no back door.</p>
<p>On Jetbox Mail, the same name works on two domains, <code>@jetboxmail.com</code> and <code>@adresse-temporaire.fr</code>, and both land in the same inbox. If a website refuses one, you switch to the other in one tap.</p>
<h2>When is a temp mail address worth using?</h2>
<p>Any time a website wants your email for something you do not plan to keep. A few typical cases:</p>
<ul>
<li>Downloading a free guide, a template or a white paper that sits behind a form.</li>
<li>Trying an app or an online tool before you decide whether you like it.</li>
<li>Getting onto hotel, airport or café Wi-Fi that asks for an email first.</li>
<li>Entering a giveaway, or reading one article behind a "sign up to continue" wall.</li>
<li>Testing your own website or newsletter signup form if you are a developer.</li>
</ul>
<p>In all of these, the site gets a working address, you get your code or your link, and the marketing emails that follow go somewhere you will never look.</p>
<h2>When should you use your real address instead?</h2>
<p>This is the part most temp mail sites skip, and it matters. A disposable address is the wrong tool for anything you may need to get back into later. If you lose the address, you also lose the way to reset the password.</p>
<table>
<thead><tr><th>Situation</th><th>Temp mail?</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Free download or one-time code</td><td>Yes</td><td>You need the message once, then never again</td></tr>
<tr><td>Trying a new app for a week</td><td>Yes, with a reserved address</td><td>You can come back to the same inbox</td></tr>
<tr><td>Online shopping with delivery</td><td>Better not</td><td>Order updates and refunds go to that address</td></tr>
<tr><td>Banking, health, taxes, government</td><td>No</td><td>Sensitive messages and account recovery</td></tr>
<tr><td>Work tools and anything you pay for</td><td>No</td><td>You will need the account for a long time</td></tr>
</tbody>
</table>
<p>Our advice: if losing access to the account would annoy you, give it an address you control for the long run.</p>
<h2>Is anyone else able to read my temp mail?</h2>
<p>It depends on the kind of address. Without an account, a temp mail inbox is public in practice: anyone who types the exact same address on the site can see its messages. That is why random names are safer than short ones like <code>john@</code>, and why you should never send anything private to a public inbox.</p>
<p>A reserved address is different. With a free Jetbox Mail account, one address belongs to you and only you can read it. We go through the risks in more detail in <a href="/guides/is-temp-mail-safe/">Is temp mail safe?</a></p>
<h2>How long do the messages stay?</h2>
<p>Short lives are the point of temp mail, so messages do not stay forever. Here is how it works on this site:</p>
<ul>
<li><strong>No account:</strong> messages are erased one hour after they arrive.</li>
<li><strong>Free account:</strong> one private address, messages kept 24 hours, and an alert on Telegram for each new message if you want it.</li>
<li><strong>Premium ($2.99 a month):</strong> up to 100 private addresses, messages kept 30 days, attachments up to 10 MB, and forwarding to your real inbox if you choose.</li>
</ul>
<p>If you need to come back to the same address next week, read <a href="/guides/temporary-email-with-password/">how to keep a temporary email you can return to</a>.</p>
<h2>Why do some websites refuse disposable emails?</h2>
<p>Some services keep lists of known temp mail domains and block them at signup. They do it to limit fake accounts and free trial abuse. It is not personal, and there is no trick worth fighting it with. You have two honest options: switch to the other domain, which a site may not have on its list, or use your real address for that one service.</p>
<h2>Can I send email from a temp mail address?</h2>
<p>No, and that is on purpose. An address that can send mail without any account would be a gift to spammers and scammers. Jetbox Mail addresses only receive. If you need to reply to someone, use an inbox you own.</p>
<h2>Frequently asked questions</h2>
<h3>Is temp mail free?</h3>
<p>Yes. You get an address the moment the page opens, with no sign-up and no payment. A free account adds one private address. Premium is optional and only matters if you want many addresses, longer storage or forwarding.</p>
<h3>Is temp mail legal?</h3>
<p>Using a disposable address to protect your privacy is legal. Using any email address for fraud, harassment or to break a website's rules is not, and the address will not hide you from the consequences.</p>
<h3>What is the difference between temp mail and an email alias?</h3>
<p>An alias forwards to your real inbox, so it is tied to you and lasts. Temp mail is separate from your real inbox and is meant to be dropped. Aliases suit long-term accounts; temp mail suits quick, one-time signups.</p>
"""
},
{
"slug": "temporary-email-with-password",
"title": "Temporary Email With Password: Keep the Same Address",
"desc": "Want a temporary email with a password so you can come back to the same inbox? Here is how to keep a disposable address private and reusable, and when not to.",
"date": "2026-11-21",
"cat": "How to",
"body": """
<p>A <strong>temporary email with a password</strong> is what most people look for after their first bad surprise: they signed up somewhere with a throwaway address, came back two days later, and the inbox was gone. What you really want is not a password as such, it is a disposable address that stays yours, that nobody else can open, and that you can find again.</p>
<p>That is possible. It just works a little differently from the "type a password" model you might expect.</p>
<h2>Why does a normal temp mail address disappear?</h2>
<p>A basic temp mail address has no owner. The site gives you a random name, keeps it in your browser, and erases messages after a short time (one hour on this site). If you clear your browser data, switch phones or simply forget the name, there is nothing to log back into.</p>
<p>The second issue is privacy. With no owner, the inbox is public: anyone who types the exact address can read it. For a one-time download code, that is fine. For an account you plan to keep using, it is not.</p>
<h2>How do I keep the same temporary address?</h2>
<p>You reserve it. On Jetbox Mail, a free account lets you claim one address so that it belongs to you. From then on:</p>
<ol>
<li>Only you can read its messages, from any device where you are signed in.</li>
<li>Messages are kept 24 hours instead of one hour.</li>
<li>You can turn on a Telegram alert for each new message.</li>
</ol>
<p>To do it, open <strong>My account</strong>, enter your usual email, type the 6-digit code you receive, and reserve the address shown on screen or pick a name of your own.</p>
<h2>Is there really no password?</h2>
<p>Right, there is no password to create or forget. You sign in with a one-time code sent to your real email. That is the "password" part handled for you, without one more string of characters to store somewhere.</p>
<p>It also means your real address is only used to let you in. Websites you sign up to with the temporary address never see it.</p>
<table>
<thead><tr><th></th><th>No account</th><th>Free account</th><th>Premium</th></tr></thead>
<tbody>
<tr><td>Who can read the inbox</td><td>Anyone with the address</td><td>Only you</td><td>Only you</td></tr>
<tr><td>Reserved addresses</td><td>0</td><td>1</td><td>Up to 100</td></tr>
<tr><td>How long messages stay</td><td>1 hour</td><td>24 hours</td><td>30 days</td></tr>
<tr><td>Forward to your real inbox</td><td>No</td><td>No</td><td>Yes, up to 30 a day</td></tr>
<tr><td>Price</td><td>$0</td><td>$0</td><td>$2.99 a month</td></tr>
</tbody>
</table>
<h2>How long does a reserved address last?</h2>
<p>On the free plan, your reserved address stays yours as long as it keeps receiving mail. If it gets no message at all for 30 days, it is released so that names do not pile up unused. Premium addresses do not have that limit while your plan is active.</p>
<p>So a reserved temp address is a good fit for a trial that lasts a few weeks, a forum you visit now and then, or a newsletter you want to read without filling your main inbox. It is still not the place for your bank.</p>
<h2>Can I choose the name of my address?</h2>
<p>Yes. Instead of the random name, tap <strong>Pick my address</strong> and type something like <code>shop.tests</code>. A few tips:</p>
<ul>
<li>Avoid your real name or anything that points to you, or the address stops being anonymous.</li>
<li>Short, common words are often taken already. Add a word or a number.</li>
<li>The same name works on both domains, <code>@jetboxmail.com</code> and <code>@adresse-temporaire.fr</code>, and lands in the same inbox.</li>
</ul>
<h2>What if a website refuses the address?</h2>
<p>Some sites block known temp mail domains when you sign up. Before giving up, switch domains: your reserved name works on both <code>@jetboxmail.com</code> and <code>@adresse-temporaire.fr</code>, and a site that blocks one may accept the other. Messages sent to either one arrive in the same private inbox, so you do not have to manage two accounts.</p>
<p>If both are refused, the site has decided it only wants long-term addresses. That is its right. You can then either skip the service or give it an address you are happy to keep, ideally one you use only for signups so your personal inbox stays quiet. Trying to sneak past the block with tricks is rarely worth the time, and it can get the new account closed later.</p>
<h2>When is a reserved temp address still a bad idea?</h2>
<p>Ask yourself one question: if this account got locked tomorrow, would I need to recover it? If the answer is yes, use a long-term address you control. A temporary inbox, even a private one, is built to be let go. Accounts that hold money, medical data, official documents or your work belong on an address you will keep for years.</p>
<p>For the full picture of what temp mail is good at, see <a href="/guides/what-is-temp-mail/">What is temp mail?</a> and the safety checklist in <a href="/guides/is-temp-mail-safe/">Is temp mail safe?</a></p>
<h2>Frequently asked questions</h2>
<h3>Can I get my old temp mail address back without an account?</h3>
<p>Only if it is still saved in the same browser. Without an account the address is not linked to you, so there is no way to prove it is yours. Reserve it next time.</p>
<h3>Do I need Premium to keep my address?</h3>
<p>No. The free account already gives you one private address. Premium is for people who want several addresses, 30 days of storage, attachments or forwarding.</p>
<h3>Can I use the reserved address on my phone too?</h3>
<p>Yes. Sign in with the same email on your phone and your addresses are there. You can also link the Telegram bot to get your codes inside Telegram.</p>
"""
},
{
"slug": "is-temp-mail-safe",
"title": "Is Temp Mail Safe? Risks, Limits and Good Habits",
"desc": "Is temp mail safe to use? An honest look at what a disposable email protects, what it does not, the risk of public inboxes and the habits that keep you safe.",
"date": "2026-11-21",
"cat": "Safety",
"body": """
<p>Yes, <strong>temp mail is safe</strong> for what it is designed to do: receiving a code or a link from a site you do not fully trust, without exposing your real address. It becomes unsafe when people use it for things it was never meant for, like bank accounts, or when they treat a public inbox as if it were private.</p>
<p>Here is what a disposable address really protects, where its limits are, and a short list of habits that cover almost every risk.</p>
<h2>What does a disposable email protect you from?</h2>
<p>Mostly from what happens to your address after you give it away. Every signup is a chance for your email to end up on a marketing list, be sold to partners, or leak in a data breach. A temp address takes that hit instead of your real one.</p>
<ul>
<li><strong>Spam:</strong> the newsletters and "special offers" go to an inbox you will never open again.</li>
<li><strong>Data leaks:</strong> if the website is breached, the leaked address is a throwaway one that is not linked to your other accounts.</li>
<li><strong>Tracking:</strong> it is harder for companies to connect your activity across sites when each one gets a different address.</li>
<li><strong>Phishing:</strong> scammers who buy leaked lists cannot reach your real inbox through that address.</li>
</ul>
<h2>What temp mail does not hide</h2>
<p>A disposable email protects your address, not your whole identity. Be clear about what stays visible:</p>
<ul>
<li>Your IP address and rough location are still seen by the websites you visit. A VPN is the tool for that, not an email address.</li>
<li>Anything you type in a form, like your name, phone number or card details, is still yours and still shared.</li>
<li>If you use the same unusual temp name everywhere, it can link your accounts together. Random names avoid that.</li>
</ul>
<p>Our view: temp mail is one layer of privacy. It is a good one, but it does not make you anonymous on its own.</p>
<h2>The real risk: public inboxes</h2>
<p>Without an account, a temp mail inbox can be opened by anyone who types the exact address. That is how most free temp mail sites work, and it is the biggest risk people miss. If someone guesses or sees your address, they can read your codes and use the "forgot password" link of the account you created.</p>
<p>Three ways to stay safe:</p>
<ol>
<li>Keep the random name the site gives you. Easy names like <code>test@</code> or <code>john123@</code> are the ones others try.</li>
<li>Never use a public inbox for an account you care about.</li>
<li>If you need the address for more than a few minutes, reserve it with a free account. A reserved address is private: only you can read it.</li>
</ol>
<p>The guide <a href="/guides/temporary-email-with-password/">Temporary email with password</a> shows how to reserve one in under a minute.</p>
<h2>Is it safe to open links and attachments?</h2>
<p>The same rules apply as in your normal inbox, because the sender does not know or care that the address is temporary. Do not open attachments you were not expecting, and check where a link goes before you tap it. On this site, images in messages are hidden by default, which also blocks the tracking pixels that tell a sender you opened their email. Show them only when you trust the message.</p>
<h2>What are the safe and unsafe uses?</h2>
<table>
<thead><tr><th>Safe uses</th><th>Unsafe uses</th></tr></thead>
<tbody>
<tr><td>Download codes and confirmation links</td><td>Bank, payment or crypto accounts</td></tr>
<tr><td>Free trials you may cancel</td><td>Health, tax or government services</td></tr>
<tr><td>Public Wi-Fi login pages</td><td>Your main social or work accounts</td></tr>
<tr><td>Testing signup forms</td><td>Anything that needs account recovery later</td></tr>
<tr><td>Contests and one-off newsletters</td><td>Receiving private documents or contracts</td></tr>
</tbody>
</table>
<h2>I used temp mail for an account that matters. What now?</h2>
<p>It happens: you signed up somewhere "just to try", and now the account holds your saved work, your purchases or your followers. Do not wait until you get locked out. Sign in today, open the account settings and change the email to an address you will keep. Most services send a confirmation link to the new address and sometimes a notice to the old one, so do it while the temp inbox is still reachable.</p>
<p>If the temp address was a public one, also change the password, since anyone who opened that inbox could have used a reset link. And if the old address is already gone, contact the service's support quickly: some can verify you another way, but many cannot.</p>
<h2>Is the temp mail service itself trustworthy?</h2>
<p>A fair question, since the service sees what arrives. Look for a site that says clearly how long messages are kept, that deletes them on schedule, and that does not let anyone send mail from its addresses. On Jetbox Mail, messages without an account are erased after one hour, after 24 hours on a free account and after 30 days on Premium, and addresses can only receive. Our <a href="/legal.html">legal notice and privacy page</a> explains what is stored and for how long.</p>
<p>New to all this? Start with <a href="/guides/what-is-temp-mail/">What is temp mail?</a></p>
<h2>Frequently asked questions</h2>
<h3>Can a temp mail address be traced back to me?</h3>
<p>The address itself is not linked to your name. But the websites you use still see your IP address and anything you enter in their forms, so it is not a cloak of invisibility.</p>
<h3>Can someone hack my temp mail?</h3>
<p>There is nothing to hack on a public inbox: anyone with the address can already read it. That is why private, reserved addresses exist for anything you want to keep to yourself.</p>
<h3>Is temp mail safe for online shopping?</h3>
<p>For browsing deals and getting a discount code, yes. For an actual order, use an address you keep, so that receipts, delivery updates and refunds reach you.</p>
"""
},
]
