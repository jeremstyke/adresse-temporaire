// Service worker : appli installable (PWA) et page d'accueil disponible hors ligne.
const C = "tm-v1";
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
