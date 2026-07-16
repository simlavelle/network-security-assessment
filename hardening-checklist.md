# Hardening Checklist (WLAN · Mobile · Host)

## WLAN
- [ ] Replace WEP/WPA2-PSK with **WPA3-Enterprise** + 802.1X authentication.
- [ ] Deploy a wireless IDS/IPS to detect rogue APs and evil-twin attacks.
- [ ] Segment guest and IoT wireless onto isolated VLANs.
- [ ] Disable WPS; hide/limit SSID broadcast where appropriate.
- [ ] Reference: NIST SP 800-153 (securing WLANs).

## Mobile / BYOD
- [ ] Enroll devices in **MDM**; enforce encryption, screen lock, and OS patch level.
- [ ] Containerize corporate data; enable remote wipe of the container.
- [ ] Block sideloaded/unapproved apps; require app vetting.
- [ ] Enforce VPN for corporate access from mobile.
- [ ] Reference: NIST SP 1800-22 (mobile device / BYOD security).

## Hosts
- [ ] Retire end-of-life OSes (Windows Server 2012, Windows 7).
- [ ] Patch SSH/services to supported versions.
- [ ] Close plaintext HTTP (port 80); enforce HTTPS + HSTS.
- [ ] Restrict/secure open DNS resolvers to prevent amplification.
