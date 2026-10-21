---
article_id: kb-m365-teams
title: Microsoft 365 and Teams issues
last_updated: 2026-02-17
applies_to: All Acme staff; Microsoft 365 apps, Teams and OneDrive
---

# Microsoft 365 and Teams issues

Acme uses Microsoft 365 for email, Teams, OneDrive and Office apps. Sign in with your Acme email address and approve MFA when asked.

## Cannot sign in

- Check the password on `portal.acme.example` in a browser. If it fails, see the Password reset or Account lockout articles.
- Sign out of all Office apps and sign in again. Ensure you use your work account, not a personal one.

## Teams problems

**No sound or camera in calls:** In Teams, open Settings, Devices and choose the correct headset and camera. Check the laptop is not muted.

**Teams is slow or messages do not send:** Quit Teams from the system tray, then clear the cache:
1. Press Windows+R and enter `%appdata%\Microsoft\Teams`.
2. Delete the contents of the folder (not the folder).
3. Restart Teams.

**Missing meeting recordings:** Recordings are stored in OneDrive (for private meetings) or SharePoint (for channel meetings) and expire after 60 days.

## OneDrive sync errors

A red cross or a pause icon means syncing has stopped. Click the cloud icon, choose **Resume syncing**, and check there is enough disk space. Files names must not contain `\ / : * ? " < > |`.

## Licences

Standard staff licence covers Word, Excel, PowerPoint, Outlook, Teams and 1 TB of OneDrive. Power BI and Visio need a separate licence; request it through the Software installation process.

## Still not working?

Raise a ticket with the category **Microsoft 365** and state the app, the error and a screenshot.
