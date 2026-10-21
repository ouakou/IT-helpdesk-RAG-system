---
article_id: kb-vpn-setup
title: VPN setup and troubleshooting
last_updated: 2026-04-14
applies_to: All Acme staff working remotely; Windows 11 and macOS 13 or later company laptops
---

# VPN setup and troubleshooting

Use the Acme VPN to reach internal systems (file shares, the intranet and the ticket system) when you are not in an Acme office. This article explains how to install and use **Acme Secure Connect**, the VPN client for all staff.

## Before you start

- You need a company laptop that is up to date with security patches.
- Your multi-factor authentication (MFA) must already be set up in the Authenticator app. See the MFA setup article if it is not.

## Installing the client

1. Open the Software Centre (Windows) or the Self Service app (macOS).
2. Install **Acme Secure Connect 6.1**.
3. If you have an older VPN client installed, uninstall it first, because the two cannot run together.

## Connecting

1. Open **Acme Secure Connect** and set the gateway to `vpn.acme.example`.
2. Sign in with your Acme email address and password.
3. Approve the **push notification in the Authenticator app** on your phone. SMS codes are not accepted.
4. Wait for the status to show **Connected**. Your session lasts 12 hours; reconnect after that.

## Troubleshooting

- **No push notification:** open the Authenticator app manually and check that notifications are enabled for it.
- **"Authentication failed":** check your password on webmail first. If your account is locked, see the Account lockout article.
- **Connected but nothing loads:** disconnect, wait 30 seconds and reconnect. If it persists, restart the laptop.
- **Gateway not found:** check that you typed `vpn.acme.example` exactly and that your home internet works.

## Still stuck?

Raise a ticket in the helpdesk portal with the category **Network / VPN** and include any error message shown.
