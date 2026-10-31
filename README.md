# Office Days

A one-button tracker for the days you go to the office (target: 9 a month by default).

Live: https://manideepgrandhi.github.io/office-days/

- Tap **I went to office today** to log today. Tap it again to unlog.
- Tap any day in the calendar to log or unlog it. Use ‹ › to change month.
- The counter shows *X of target*. Change the target in the box next to it.
- The year summary shows days per month.
- **Undo** reverts your last change in this session.
- Export a CSV (`date,weekday,month`) or JSON, and import a JSON array of `YYYY-MM-DD` dates.
- Add to home screen from your phone browser's menu for an app-like button.

Your days are always saved in the browser (localStorage). GitHub sync is optional.

## GitHub sync setup

1. On GitHub go to **Settings > Developer settings > Personal access tokens > Fine-grained tokens > Generate new token**.
2. Name it `office-days`, pick an expiry, and set **Resource owner** to your account.
3. Under **Repository access** choose **Only select repositories** and select **office-days**.
4. Under **Permissions > Repository permissions** set **Contents: Read and write**. Leave everything else as No access.
5. Generate the token and copy it.
6. Open the page, paste the token in **GitHub sync**, and tap **Connect**.

Every log or unlog then commits `days.json` in this repo. If two devices write at the same time, the page re-reads the file and retries.
Use **Clear token** to remove the token from that browser. The token is kept only in that browser's localStorage, is sent only to `api.github.com`, and is never shown or logged.

**Privacy:** this repo is public, so `days.json` (your office dates) is public too. Make the repo private if you don't want that. GitHub Pages on a private repo needs a paid plan, but you can still run the page from a local copy of `index.html`.

## Security

- One static `index.html`, no external scripts, fonts or images.
- A strict Content-Security-Policy: inline scripts and styles are allowed by hash only, and network access is limited to `api.github.com` and the site search index.
- All data is written with `textContent`, and dates are validated as real `YYYY-MM-DD` dates.

## Development

The shared top bar comes from [manideepgrandhi.github.io](https://github.com/manideepgrandhi/manideepgrandhi.github.io). After editing `index.html`, run `python3 build.py` with that repo checked out next to this one. It refreshes the shared bar and recomputes the CSP hashes.
