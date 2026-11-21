// Service worker : appli installable (PWA) et page d'accueil disponible hors ligne.
const C = "tm-v2";
const CORE = ["/", "/favicon.svg", "/icon-192.png", "/icon-512.png", "/site.webmanifest"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(C).then((c) => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener("activate", (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== C).map((k) => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", (e) => {
  const r = e.request, u = new URL(r.url);
  if (r.method !== "GET" || u.origin !== location.origin) return; // l'API et les sites externes passent toujours par le réseau
  if (r.mode === "navigate") {
    // pages : le réseau d'abord (contenu toujours à jour), la copie en cache si hors ligne
    e.respondWith(fetch(r).then((res) => { const cp = res.clone(); if (res.ok) caches.open(C).then((c) => c.put(r, cp)); return res; })
      .catch(() => caches.match(r).then((m) => m || caches.match("/"))));
    return;
  }
  if (/\.(png|ico|svg|webmanifest|woff2?)$/.test(u.pathname)) {
    e.respondWith(caches.match(r).then((m) => m || fetch(r).then((res) => { const cp = res.clone(); if (res.ok) caches.open(C).then((c) => c.put(r, cp)); return res; })));
  }
});

// alertes : le serveur envoie un simple signal, on va chercher le texte des nouveaux e-mails
const API = "https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/tmail";
self.addEventListener("push", (e) => {
  e.waitUntil(self.registration.pushManager.getSubscription().then((s) => s ? fetch(API + "/push/peek", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ endpoint: s.endpoint }) }).then((r) => r.json()) : { notes: [] })
    .catch(() => ({ notes: [] }))
    .then((j) => {
      const notes = (j && j.notes) || [];
      const fr = self.location.hostname !== "jetboxmail.com";
      if (!notes.length) notes.push({ t: fr ? "Nouvel e-mail reçu" : "New email received", b: fr ? "Ouvrez votre boîte pour le lire." : "Open your inbox to read it.", a: "" });
      return Promise.all(notes.slice(-3).map((n, i) => self.registration.showNotification(n.t, { body: n.b, icon: "/icon-192.png", badge: "/icon-192.png", tag: "mail-" + (n.a || "x") + "-" + Date.now() + i, data: { url: "/" + (n.a ? "?a=" + encodeURIComponent(n.a) : "") } })));
    }));
});
self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const url = (e.notification.data && e.notification.data.url) || "/";
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((ws) => {
    for (const w of ws) if ("focus" in w) { w.navigate(url).catch(() => {}); return w.focus(); }
    return self.clients.openWindow(url);
  }));
});
