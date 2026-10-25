# Hardening Checklist — Kelompok 7 (Target Node: Ubuntu Server 24.04 LTS + PostgreSQL + Web App Custom)

Status: **Selesai** / **Sebagian** / **Belum**
Bukti lengkap (screenshot/output) disimpan di `docs/blueteam/evidence/`.

---

## Kategori A — Access & Authentication

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| A1 | Nonaktifkan login root langsung via SSH (`PermitRootLogin no`) + wajibkan key-based auth (`PasswordAuthentication no`, `ChallengeResponseAuthentication no`) | Sebagian | `evidence/a1-sshd-config-before.png`, `evidence/a1-sshd-config-after.png`, `evidence/a1-login-root-rejected.png` |
| A2 | Ganti password default akun admin VM | Belum | `evidence/a2-login-old-fail.png`, `evidence/a2-login-new-success.png` |
| A3 | Rate-limit percobaan login SSH (fail2ban) | Belum | fail2ban sudah terinstal, jail SSH belum diaktifkan |

## Kategori B — Service & Attack Surface

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| B1 | Nonaktifkan service tidak terpakai, batasi Flask dev server agar tidak expose debug mode | Belum | `evidence/b1-netstat-before.png`, `evidence/b1-netstat-after.png` |
| B2 | Firewall (ufw) whitelist port 22/80/5432 hanya dari IP Attacker/Monitoring | Belum | ufw sudah terinstal, belum diaktifkan; `evidence/b2-nmap-before.txt`, `evidence/b2-nmap-after.txt` |
| B3 | Ganti kredensial default PostgreSQL (`appuser`/`admin123`) | Belum | `evidence/b3-pg-login-old-fail.png`, `evidence/b3-pg-login-new-success.png` |

## Kategori C — Data & Application

| No | Kontrol | Status | Bukti |
| :--- | :--- | :--- | :--- |
| C1 | Perbaiki query login agar parameterized (hilangkan celah SQL Injection) | Belum | `evidence/c1-code-before.png`, `evidence/c1-code-after.png`, `evidence/c1-sqli-blocked.png` |
| C2 | Logging aktivitas mencurigakan aktif di Security Onion (Zeek http.log) | Belum | `evidence/c2-zeek-http-log.png` |
| C3 | Least-privilege user database untuk aplikasi (batasi privilege `appuser`, jangan jadi owner database setelah skema final) | Belum | `evidence/c3-db-config-before.png`, `evidence/c3-db-config-after.png` |

---

## Ringkasan

- Total kontrol direncanakan: **9** (memenuhi minimum 8, tersebar di 3 kategori, masing-masing minimal 2)
- Status saat Minggu ke-9: sebagian besar kontrol dalam tahap perencanaan/persiapan tooling (fail2ban dan ufw sudah terinstal namun belum diaktifkan agar bukti before/after tetap valid), eksekusi penuh dilanjutkan setelah checkpoint sesuai Roadmap Bagian VI (Minggu ke-10/11)
- Verifikasi akhir: `nmap -sV 192.168.7.5` before vs after, dilampirkan sebagai `evidence/nmap-diff.txt`

### Catatan Revisi

Target Node semula direncanakan Metasploitable 2/DVWA (MySQL). Checklist ini direvisi menyesuaikan migrasi ke Ubuntu Server 24.04 LTS + PostgreSQL + aplikasi web custom (lihat `docs/presentation-minggu9/tech_stack_declaration.md`), sehingga detail kontrol B3 dan C1 disesuaikan dari konteks DVWA/MySQL menjadi PostgreSQL/Flask.
