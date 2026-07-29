# Remilia Pets

An experimental collection of custom animated pets for Codex. It includes **Mildred**, a green-haired neochibi companion in a vampire costume; **Remy**, a relaxed rough-crayon neochibi companion; and **Wiggum**, a sly blond neochibi with angular black glasses.

<p>
  <img src="previews/mildred-idle.gif" alt="Mildred idle animation" width="192">
  <img src="previews/remy-idle.gif" alt="Remy idle animation" width="192">
  <img src="previews/wiggum/idle.gif" alt="Wiggum idle animation" width="192">
</p>

## Repository contents

- `pets/remy/` — the installable Codex pet package
- `docs/install-remy.md` — download, installation, verification, and troubleshooting
- `pets/mildred/` — the installable Codex pet package
- `previews/` — cleaned review images derived from the packaged atlas
- `docs/install-mildred.md` — download, installation, verification, and troubleshooting
- `docs/create-your-own-pet.md` — a user-facing creation walkthrough
- `AGENTS.md` — instructions for Codex agents helping someone create a pet
- `PRIVACY.md` — the repository's publication-safety checklist
- `LICENSE` — the Viral Public License (VPL)
- `tools/privacy_check.py` — a local and CI publication-safety scan

Generation logs, local paths, source dossiers, prompts, intermediate chroma-key media, and machine-specific files are intentionally excluded.

## Download and install

Choose a package and follow its dedicated guide:

- [Install Mildred](docs/install-mildred.md)
- [Install Remy](docs/install-remy.md)

### Quick install Mildred

For the easiest setup, open the repository on GitHub, select **Code → Download ZIP**, and extract it. Then copy the complete `pets/mildred` directory into your local Codex pets directory:

- macOS/Linux: `~/.codex/pets/mildred`
- Windows: `%USERPROFILE%\.codex\pets\mildred`

Then open **Settings → Pets**, select **Refresh**, choose **Mildred**, and use `/pet` to wake her.

The package contains:

- `pet.json`
- `spritesheet.webp`

The final layout must be:

```text
.codex/
  pets/
    mildred/
      pet.json
      spritesheet.webp
```

For step-by-step Windows, macOS, and Linux instructions—including verification and troubleshooting—see [Install Mildred](docs/install-mildred.md).

The spritesheet uses the Codex v2 contract: an 8×11 atlas, 192×208-pixel cells, final dimensions of 1536×2288, and `spriteVersionNumber: 2`.

## Expected animation style

Codex pets use a deliberately compact frame budget. Depending on the state, standard animations use four to eight frames with app-controlled timing. They therefore have a stepped, sprite-animation feel rather than video-rate motion.

## Create your own

See [Create your own Codex pet](docs/create-your-own-pet.md). If you are working with Codex inside this repository, ask it to follow `AGENTS.md` and the installed `hatch-pet` workflow.

## Privacy and license

This repository is structured to avoid publishing personal filesystem paths, usernames, source dossiers, generation transcripts, or embedded image metadata. Review [PRIVACY.md](PRIVACY.md) before every release.

Run `python tools/privacy_check.py` and verify `SHA256SUMS.txt` before committing. GitHub Actions repeats both checks on pushes and pull requests.

This work is released under the [Viral Public License](LICENSE). Redistributions and derivative or combined works must retain the license in its entirety, and no further restrictions may be applied.
