const CACHE_NAME = 'safewalk-cache-v1';
const urlsToCache = [
  '/',
  '/static/style.css',
  '/static/main.js',
  '/static/icon-192.png',
  '/static/icon-512.png'
];

// Install
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Fetch
self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() =>
      caches.match(event.request))
  );
});
