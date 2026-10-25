# Attack Plan — Kelompok 7

**Red Team:** Riris Mulyanti Yusup, Nita Putri Azahra
**Target:** Target Node replika — Ubuntu Server 24.04 LTS + PostgreSQL + Aplikasi Web Custom (Flask), IP 192.168.7.5
**Lingkup:** Hanya menyasar Target Node di lab (192.168.7.0/24). Dilarang menyasar sistem apa pun di luar segmen ini.

---

## Skenario 1 — Reconnaissance & Enumerasi

| | |
|---|---|
| **Kategori** | Reconnaissance |
| **Teknik** | Port/service scanning, OS fingerprinting, enumerasi banner |
| **Tools** | Nmap, Wireshark |
| **Target** | 192.168.7.5, port 22, 80, 5432 |
| **Hasil diharapkan** | Daftar port terbuka, versi service (OpenSSH, Flask dev server/werkzeug, PostgreSQL), dan celah potensial |
| **Celah terkait** | Aplikasi web berjalan tanpa reverse proxy/TLS pada port 80; PostgreSQL dapat diakses langsung dari segmen jaringan (port 5432 terbuka) |

## Skenario 2 — SQL Injection & XSS pada Aplikasi Web (+ Ekstraksi Data PostgreSQL)

| | |
|---|---|
| **Kategori** | Web/API/Protokol IoT |
| **Teknik** | SQL Injection untuk bypass autentikasi login, Stored XSS pada form catatan batch, akses langsung ke endpoint API tanpa autentikasi, dilanjutkan ekstraksi data via sqlmap atau koneksi langsung ke PostgreSQL |
| **Tools** | Burp Suite, sqlmap, browser (Firefox), psql client |
| **Target** | http://192.168.7.5/ (halaman login & form catatan, port 80), endpoint `/api/readings` (tanpa autentikasi), PostgreSQL (port 5432) |
| **Hasil diharapkan** | Bypass login tanpa kredensial valid (payload `' OR '1'='1' --`), payload XSS tereksekusi pada form catatan batch, data sensor terbaca langsung dari `/api/readings` tanpa login, dump tabel `users`/`readings` dari PostgreSQL |
| **Celah terkait** | Query SQL pada form login dibangun manual tanpa parameterized query; output catatan batch dirender tanpa escaping (`\|safe`); endpoint `/api/readings` tidak memeriksa sesi login; kredensial database (`appuser`/`admin123`) lemah |

## Skenario 3 — Brute-force Autentikasi SSH

| | |
|---|---|
| **Kategori** | Exploitation / Akses |
| **Teknik** | Brute-force kredensial login menggunakan wordlist |
| **Tools** | Hydra |
| **Target** | 192.168.7.5, port 22 |
| **Hasil diharapkan** | Kredensial valid ditemukan (uji terhadap akun admin VM sebagai baseline sebelum hardening) |
| **Celah terkait** | Kredensial login VM yang dipakai saat setup awal relatif sederhana dan belum ada rate-limiting; menjadi bukti kondisi "before" untuk kontrol hardening A (fail2ban, key-based auth) |

---

## Catatan

- Skenario DoS/DDoS **tidak digunakan** pada rencana ini (opsional, maksimal 1 dari 3 skenario sesuai Bagian IX — kelompok memilih fokus pada 3 kategori selain Availability).
- Setiap skenario akan melalui **Purple Team Loop** (Bagian X) mulai Minggu ke-10: serang → deteksi → analisis → mitigasi → verifikasi ulang, dicatat di `docs/purple-team-log.md`.
- Eksekusi penuh dan bukti lengkap baru dilakukan mulai Minggu ke-10, sesuai Roadmap Bagian VI. Dokumen ini adalah rencana untuk checkpoint Minggu ke-9.
- **Revisi dari draf awal:** Skenario semula dirancang untuk target Metasploitable 2/DVWA (MySQL). Setelah Target Node dimigrasi ke Ubuntu Server + PostgreSQL + aplikasi web custom, detail teknis (endpoint, query, kredensial) disesuaikan, namun pola serangan dan kategori tetap sama.
