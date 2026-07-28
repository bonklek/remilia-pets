# Install Remy

Remy is packaged as a Codex v2 desktop pet. Installation only requires copying one folder containing `pet.json` and `spritesheet.webp`.

## Download

1. Open the repository on GitHub.
2. Select **Code**, then **Download ZIP**.
3. Extract the downloaded repository ZIP.
4. Open the extracted `pets` folder and locate `remy`.

If a GitHub Release provides `remy.zip`, download that asset instead and extract it. The extracted folder should directly contain `pet.json` and `spritesheet.webp`; avoid an extra nested `remy/remy` directory.

## Install on Windows

1. Press **Win+R**.
2. Enter `%USERPROFILE%\.codex\pets` and press **Enter**.
3. Create the `pets` directory if Windows reports that it does not exist.
4. Copy the complete `remy` folder into it.

The resulting files should be:

```text
%USERPROFILE%\.codex\pets\remy\pet.json
%USERPROFILE%\.codex\pets\remy\spritesheet.webp
```

## Install on macOS or Linux

1. Open your home directory and show hidden files if necessary.
2. Open `.codex`, then `pets`. Create either directory if it does not exist.
3. Copy the complete `remy` folder into `~/.codex/pets/`.

The resulting files should be:

```text
~/.codex/pets/remy/pet.json
~/.codex/pets/remy/spritesheet.webp
```

## Activate Remy

1. Open the ChatGPT desktop app.
2. Open **Settings → Pets**.
3. Select **Refresh**.
4. Choose **Remy**.
5. Use `/pet` in a Codex task to wake or hide them.

## Verify the installation

Open `remy` in your local pets directory and confirm that:

- `pet.json` and `spritesheet.webp` are directly inside the folder
- the folder is named `remy`
- `pet.json` contains `"spriteVersionNumber": 2`
- `spritesheet.webp` has not been renamed or moved elsewhere

## Troubleshooting

### Remy does not appear after Refresh

- Confirm that you are using the desktop app and have opened **Settings → Pets**.
- Check for an accidental extra directory level. The correct path ends with `remy/pet.json`, not `remy/remy/pet.json`.
- Confirm that both package files are present and retain their original names.
- Restart the desktop app, return to **Settings → Pets**, and select **Refresh** again.

### Remy appears but does not animate

- Replace both local package files with fresh copies from the same download.
- Do not mix `pet.json` from one release with `spritesheet.webp` from another.
- Verify the downloaded files against the hashes in `SHA256SUMS.txt` if corruption is suspected.

### The ZIP opens but no pet package is obvious

For a full repository download, use `pets/remy`. Preview images in `previews` are documentation and cannot be installed as a pet.
