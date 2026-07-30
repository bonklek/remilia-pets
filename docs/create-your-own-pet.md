# Create a Codex pet from a PFP

This guide turns one profile picture into a local animated Codex pet. You do not need to draw a spritesheet or choose every technical setting yourself: attach the image, give Codex a short brief, and let the repository's pet workflow handle the poses, validation, previews, and package.

## 1. Make or choose your PFP

You can use your own artwork or start with one of the Remilia makers:

- [Milady Maker](https://maker.remilia.org/milady)
- [Remilio Maker](https://maker.remilia.org/remilio)
- [Bonkler Factory](https://maker.remilia.org/bonkler)
- [Kagami Academy Maker](https://maker.remilia.org/kagami)

The maker navigation also links these collections from the [main Milady Maker page](https://maker.remilia.org/). Use the random picker or trait controls, then download the highest-resolution version available.

For the cleanest pet:

- Prefer a single character on a plain or transparent background.
- Avoid meme panels, captions, UI, scenery, and extra overlays.
- Keep the face, hair, headwear, clothing, markings, and silhouette easy to see.
- Start without a handheld prop if you want to add, remove, or swap props later.
- A bust or head-and-shoulders PFP can work, but a visible full-body reference gives the agent less anatomy to infer.
- Keep the original image outside the repository unless you have permission to redistribute it.

## 2. Give the PFP to Codex

Download or clone this repository, open its folder in the Codex desktop app, create a task, and attach the PFP. Then paste this prompt:

> Follow `AGENTS.md` and the installed `hatch-pet` and `$imagegen` workflows. Turn the attached PFP into a complete Codex v2 pet. Start with the `preview` review profile and do not publish anything. Ask me short questions about the pet's name, personality, identity-defining traits, prop policy, and motion choices before generating. Preserve the same character, style, palette, face, proportions, outfit, and accessories across every pose. Keep a visible four-stage checklist, validate each row, complete the four cardinals and sixteen-direction look system, run final despill and QA, and package `pet.json` with `spritesheet.webp` only after the hard gates pass.

Codex should ask only for decisions it cannot safely infer. A useful intake covers:

1. The pet's short name and one-sentence description.
2. The traits that must never drift from the PFP.
3. Its personality and emotional range.
4. Whether a visible prop is permanent, removable, or excluded from the first version.
5. The desired motion for each runtime state.
6. Whether the result is private, internal, or cleared for publication.

## 3. Choose motions with personality

Codex uses nine runtime states, but the animation does not have to be literal. The state name tells the app when to play the row; you can choose a different behavior that still communicates the state clearly.

| Runtime state | What it must communicate | Example custom behaviors |
| --- | --- | --- |
| `idle` | Calm resting loop | breathing, hat adjustment, checking a pocket |
| `running-right` | Movement and screen-right orientation | skating, cartwheeling, moonwalking right |
| `running-left` | Movement and screen-left orientation | slalom glide, scooter ride, leftward dance step |
| `waving` | Greeting or acknowledgment | salute, bow, peace sign, wrist flick |
| `jumping` | Clear airborne action | heel click, tuck jump, boardless grab |
| `failed` | Setback or recovery | stumble, crouch, facepalm, resilient stand |
| `waiting` | Needs approval or user input | checking a watch, toe tapping, expectant shrug |
| `running` | Active task work | sorting, typing pantomime, planning gestures |
| `review` | Inspection or evaluation | skeptical scan, slow nod, thoughtful appraisal |

The left and right rows may use different activities, but each must unmistakably face or travel toward its assigned screen edge. Avoid repeating a movement already present in the repository if your goal is to contribute a reusable motion template.

## 4. Let the workflow hatch the pet

The task should maintain this checklist:

1. Getting `<pet>` ready.
2. Imagining `<pet>`'s main look.
3. Picturing `<pet>`'s poses.
4. Hatching `<pet>`.

The workflow will:

- make a clean, compact full-body canonical reference from the PFP
- generate and validate all nine standard animation rows
- define how the character naturally looks up, right, down, and left
- create two coherent look rows covering all sixteen directions
- assemble and despill a transparent 1536x2288 v2 atlas
- create contact sheets, direction sheets, and motion GIFs for review
- package the final pet only after deterministic and visual checks pass

Do not treat a generated atlas as complete merely because it opens. The four cardinal directions, row semantics, transparency, registration, and `spriteVersionNumber: 2` are hard requirements.

## Review cost and quality

Choose the review profile before generation:

- `preview` is the default for local experiments. It uses deterministic validation, one labeled visual review, no blind reviewers, and bounded retries.
- `standard` adds one blind direction review for more polished private or internal use.
- `publication` uses three isolated blind direction reviews plus independent final QA and is required before publishing a package here.

If a preview reaches its retry limit with a subjective warning, inspect the best candidate yourself instead of starting an unlimited review loop.

## What you receive

The installable folder contains exactly:

```text
my-pet/
  pet.json
  spritesheet.webp
```

The package's `pet.json` must set `spriteVersionNumber` to `2`. Keep the contact sheet, direction sheet, motion GIFs, validation report, and donor manifest as QA evidence; they do not belong inside the two-file installable folder.

## Install the pet

Copy the complete package directory into:

- macOS/Linux: `~/.codex/pets/<pet-name>/`
- Windows: `%USERPROFILE%\.codex\pets\<pet-name>\`

Open **Settings -> Pets**, select **Refresh**, choose the pet, and use `/pet` to wake or hide it.

Custom pets installed this way are local and do not automatically sync to the web.

## Before sharing or publishing

- Confirm that you may redistribute the PFP and every retained trait or asset.
- Do not commit the source PFP unless its redistribution rights are explicit.
- Remove source paths, usernames, prompts, generation caches, metadata, and other private material.
- Review [`PRIVACY.md`](../PRIVACY.md) and retain the repository's [`LICENSE`](../LICENSE).
- Run the privacy check and verify `SHA256SUMS.txt` before committing.
- Keep `preview` and `standard` packages private; use the `publication` profile for public packages.

Official product overview: <https://learn.chatgpt.com/docs/pets>
