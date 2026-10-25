# Attack Plan — Kelompok 7

**Red Team:** Riris Mulyanti Yusup, Nita Putri Azahra
**Target:** Target Node replika — Metasploitable 2 / DVWA (192.168.7.5)
**Lingkup:** Hanya menyasar Target Node di lab (192.168.7.0/24). Dilarang menyasar sistem apa pun di luar segmen ini.

---

## Skenario 1 — Reconnaissance & Enumerasi

| | |
|---|---|
| **Kategori** | Reconnaissance |
| **Teknik** | Port/service scanning, OS fingerprinting, enumerasi banner |
| **Tools** | Nmap, Wireshark |
| **Target** | 192.168.7.5, port 22, 80, 3306 |
| **Hasil diharapkan** | Daftar port terbuka, versi service, dan celah potensial (acuan: riset Minggu ke-4) |
| **Celah terkait (Minggu ke-4)** | Metasploitable 2 dikenal menjalankan versi service lama (vsftpd, Apache, MySQL, OpenSSH) dengan konfigurasi default/rentan |

## Skenario 2 — SQL Injection & XSS pada DVWA (+ Ekstraksi Data MySQL)

| | |
|---|---|
| **Kategori** | Web/API/Protokol IoT |
| **Teknik** | SQL Injection untuk bypass autentikasi/ekstraksi data, Stored/Reflected XSS, dilanjutkan dump database via SQLi |
| **Tools** | Burp Suite, sqlmap, browser (Firefox) |
| **Target** | http://192.168.7.5/dvwa/ (port 80), lanjut ke MySQL (port 3306) via sqlmap |
| **Hasil diharapkan** | Bypass login/ekstraksi tabel database (bukti: dump tabel `users` DVWA), payload XSS tereksekusi di halaman target |
| **Celah terkait (Minggu ke-4)** | DVWA level low tidak melakukan sanitasi input; celah SQLi klasik dan XSS reflected pada parameter GET |

## Skenario 3 — Brute-force Autentikasi SSH

| | |
|---|---|
| **Kategori** | Exploitation / Akses |
| **Teknik** | Brute-force kredensial login menggunakan wordlist |
| **Tools** | Hydra |
| **Target** | 192.168.7.5, port 22 |
| **Hasil diharapkan** | Kredensial valid ditemukan (uji dengan kredensial default `msfadmin`/`msfadmin` sebagai baseline sebelum hardening) |
| **Celah terkait (Minggu ke-4)** | Kredensial default lemah, tidak ada rate-limiting pada percobaan login |

---

## Catatan

- Skenario DoS/DDoS **tidak digunakan** pada rencana ini (opsional, maksimal 1 dari 3 skenario sesuai Bagian IX — kelompok memilih fokus pada 3 kategori selain Availability).
- Setiap skenario akan melalui **Purple Team Loop** (Bagian X) mulai Minggu ke-10: serang → deteksi → analisis → mitigasi → verifikasi ulang, dicatat di `docs/purple-team-log.md`.
- Eksekusi penuh dan bukti lengkap baru dilakukan mulai Minggu ke-10, sesuai Roadmap Bagian VI. Dokumen ini adalah rencana untuk checkpoint Minggu ke-9.
