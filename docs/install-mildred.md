# Install Mildred

Mildred is packaged as a Codex v2 desktop pet. Installation only requires copying one folder containing `pet.json` and `spritesheet.webp`.

## Download

1. Open the repository on GitHub.
2. Select **Code**, then **Download ZIP**.
3. Extract the downloaded repository ZIP.
4. Open the extracted `pets` folder and locate `mildred-neochibi`.

If a GitHub Release provides `mildred-neochibi.zip`, download that asset instead and extract it. The extracted folder should directly contain `pet.json` and `spritesheet.webp`; avoid an extra nested `mildred-neochibi/mildred-neochibi` directory.

## Install on Windows

1. Press **Win+R**.
2. Enter `%USERPROFILE%\.codex\pets` and press **Enter**.
3. Create the `pets` directory if Windows reports that it does not exist.
4. Copy the complete `mildred-neochibi` folder into it.

The resulting files should be:

```text
%USERPROFILE%\.codex\pets\mildred-neochibi\pet.json
%USERPROFILE%\.codex\pets\mildred-neochibi\spritesheet.webp
```

## Install on macOS or Linux

1. Open your home directory and show hidden files if necessary.
2. Open `.codex`, then `pets`. Create either directory if it does not exist.
3. Copy the complete `mildred-neochibi` folder into `~/.codex/pets/`.

The resulting files should be:

```text
~/.codex/pets/mildred-neochibi/pet.json
~/.codex/pets/mildred-neochibi/spritesheet.webp
```

## Activate Mildred

1. Open the ChatGPT desktop app.
2. Open **Settings → Pets**.
3. Select **Refresh**.
4. Choose **Mildred**.
5. Use `/pet` in a Codex task to wake or hide her.

## Verify the installation

Open `mildred-neochibi` in your local pets directory and confirm that:

- `pet.json` and `spritesheet.webp` are directly inside the folder
- the folder is named `mildred-neochibi`
- `pet.json` contains `"spriteVersionNumber": 2`
- `spritesheet.webp` has not been renamed or moved elsewhere

## Troubleshooting

### Mildred does not appear after Refresh

- Confirm that you are using the desktop app and have opened **Settings → Pets**.
- Check for an accidental extra directory level. The correct path ends with `mildred-neochibi/pet.json`, not `mildred-neochibi/mildred-neochibi/pet.json`.
- Confirm that both package files are present and retain their original names.
- Restart the desktop app, return to **Settings → Pets**, and select **Refresh** again.

### Mildred appears but does not animate

- Replace both local package files with fresh copies from the same download.
- Do not mix `pet.json` from one release with `spritesheet.webp` from another.
- Verify the downloaded files against the hashes in `SHA256SUMS.txt` if corruption is suspected.

### The ZIP opens but no pet package is obvious

For a full repository download, use `pets/mildred-neochibi`. Preview images in `previews` are documentation and cannot be installed as a pet.
