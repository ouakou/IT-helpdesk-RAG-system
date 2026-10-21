---
article_id: kb-shared-drives
title: Shared drives and file permissions
last_updated: 2025-10-02
applies_to: All Acme staff; network shares and SharePoint team sites
---

# Shared drives and file permissions

Team files live on department shared drives. Most teams use the **S: drive** (network share), and some use SharePoint team sites.

## Connecting to a drive

- In the office, the S: drive connects automatically when you sign in.
- At home, connect to the VPN first (see the VPN setup article), then restart File Explorer or sign out and in.
- On macOS, in Finder choose Go, Connect to Server, and enter `smb://files.acme.example/dept`.

## "Access denied" or missing folder

You can only see folders your team has access to. If you need one that you cannot open, raise an Access Request (see the Access requests article). IT cannot override the folder owner.

## Sharing files

- Share inside Acme using OneDrive or SharePoint links, set to **specific people**, not "anyone with the link".
- Do not email sensitive files as attachments. See the Data protection article.
- External sharing needs your manager's approval and is limited to 30 days.

## Deleted or overwritten files

The S: drive keeps daily snapshots for **14 days**. To restore a file, right-click the folder, choose Properties, Previous Versions. For older files, raise a ticket (see the Backup and file recovery article).

## Naming and size

Keep the full path under 255 characters. Do not store personal files such as photos or music on shared drives; they will be removed.
