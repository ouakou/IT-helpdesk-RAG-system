---
article_id: kb-mfa-setup
title: MFA setup, lost or new phone
last_updated: 2026-02-03
applies_to: All Acme staff; Microsoft Authenticator on iOS and Android
---

# MFA setup, lost or new phone

Acme requires multi-factor authentication (MFA) for email, Teams, the VPN and the password reset portal. We use the **Microsoft Authenticator** app. SMS codes are not supported.

## First-time setup

1. Install Microsoft Authenticator from the App Store or Google Play.
2. On your laptop, go to `mysignins.acme.example` and sign in.
3. Choose **Add sign-in method**, then **Authenticator app**.
4. Scan the QR code with the app and approve the test notification.
5. Save the **8 backup codes** shown at the end somewhere safe (not on the same phone). Each works once.

## Getting a new phone

Before you wipe or hand in your old phone:

1. In Authenticator on the old phone, turn on **Cloud backup** in Settings.
2. On the new phone, install the app and choose **Restore from backup**.
3. Check that notifications work by signing in somewhere.

## Lost phone, or the old one is already gone

- Use a backup code to sign in, then add the new phone at `mysignins.acme.example`.
- If you have no backup codes, raise a ticket (or call the helpdesk, ext. 4000). We verify your identity with your line manager before resetting your MFA, which can take up to 1 working day.
- If the phone was lost or stolen, follow the Lost or stolen device article as well.

## Common problems

- **No notification arrives:** open the app and check that notifications are allowed, and that the phone has a data connection.
- **"Number matching" prompt:** type the number shown on the sign-in screen into the app. This is expected.
