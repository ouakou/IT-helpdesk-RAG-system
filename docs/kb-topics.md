# KB topic list (draft — edit freely)

Article IDs become `expected_source` in the eval files, so keep them stable once chosen.
File name = `data/kb/<article_id>.md`.

| # | article_id | Topic | Trap |
|---|---|---|---|
| 1 | kb-password-reset | Password reset and self-service portal | |
| 2 | kb-mfa-setup | MFA setup, lost or new phone | |
| 3 | kb-account-lockout | Account lockout | |
| 4 | kb-new-starter-access | New starter access and onboarding checklist | |
| 5 | kb-access-requests | Access requests and permission changes (approval flow) | |
| 6 | kb-vpn-setup | VPN setup and troubleshooting (current client) | **Contradiction A** |
| 7 | kb-vpn-legacy-client | VPN legacy client instructions | **Contradiction B** |
| 8 | kb-wifi-networks | Wi-Fi: office and guest networks | **Outdated** |
| 9 | kb-slow-network | Slow network or internet performance | |
| 10 | kb-printer-setup | Printer setup and common faults | |
| 11 | kb-laptop-problems | Laptop won't boot, slow or crashing | |
| 12 | kb-equipment-requests | Equipment requests, replacement and returns | **Injected instruction** |
| 13 | kb-software-install | Software installation and approved-software list | |
| 14 | kb-software-updates | Software updates and patching | |
| 15 | kb-app-crashes | Application crashes and freezes | |
| 16 | kb-m365-teams | Microsoft 365 and Teams issues | |
| 17 | kb-outlook-email | Outlook and email: mailbox full, shared mailboxes, calendar | |
| 18 | kb-shared-drives | Shared drives and file permissions | |
| 19 | kb-backup-recovery | Backup and file recovery | |
| 20 | kb-remote-byod | Remote working and BYOD policy | |
| 21 | kb-data-protection | Data protection and handling sensitive data | |
| 22 | kb-report-phishing | Reporting phishing and suspicious emails | |
| 23 | kb-security-incident | Suspected breach, malware or ransomware (escalate) | |
| 24 | kb-lost-device | Lost or stolen device (escalate) | |
| 25 | kb-sla-priorities | Helpdesk SLAs, priorities and how to raise a ticket | |
| 26 | kb-ticket-status | Ticket status and escalation process | |
| 27 | kb-outage-comms | Outages and incident communications | |
| 28 | kb-leavers-offboarding | Leavers and offboarding | |

Peripherals (monitor, dock, headset) were dropped to make room for the legacy VPN article.

## Trap design notes
- **Contradiction (#6 vs #7):** both articles answer the same question (e.g. "how do I connect to VPN from home?") with different, incompatible steps (different client, different MFA method). Give them different last-updated dates. How the assistant should resolve it depends on SPEC open question 4.
- **Outdated (#8):** an old last-updated date and references to something retired (an old SSID, a decommissioned tool) that a newer article or common sense contradicts.
- **Injected instruction (#12):** an instruction aimed at the AI, hidden in the article body (an HTML comment, a footer line, or a "note to assistant"), that a safe system must not obey. Vary the style across articles later if you add more.

## Writing guidelines
- 200–400 words each, realistic and slightly messy; overlap with neighbouring articles is good.
- Front-matter: article_id, title, last_updated (YYYY-MM-DD), applies_to.
- Include concrete, checkable facts (names, numbers, steps) so answers can be graded.
- Every article should be answerable by at least one golden question.
