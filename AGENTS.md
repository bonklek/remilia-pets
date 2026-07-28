# Agent instructions

These instructions apply to the entire repository. They are intended for Codex agents helping a user design, generate, validate, or package a custom pet.

## Start with the user

Help the user define:

1. A short pet name and one-sentence description.
2. The creature or character concept.
3. The visual style, palette, silhouette, and personality.
4. Any identity-defining hair, headwear, clothing, markings, or props.
5. Reference images and the rights or restrictions attached to them.
6. Whether the result is private review material or cleared for publication.

Do not require answers that can be inferred safely from a concrete brief. Do not broaden a private/review-only request into public distribution.

## Required workflows

- Use the installed `hatch-pet` skill for pet preparation, deterministic processing, QA, and v2 packaging.
- Use the installed `$imagegen` skill as the only visual-generation layer.
- Read both skill instruction files completely before generating anything.
- Use the bundled workspace Python runtime for hatch-pet scripts; do not assume a system Python installation.
- Keep visual generation isolated: one lightweight worker per base image or animation-row job when worker capacity permits.
- Never synthesize missing art with local drawing scripts, image APIs, or improvised tiling.

## Visible progress

Maintain this four-stage checklist:

1. Getting `<pet>` ready.
2. Imagining `<pet>`'s main look.
3. Picturing `<pet>`'s poses.
4. Hatching `<pet>`.

Only complete a stage when its real files and required review gates exist.

## Visual contract

Create one compact, connected, full-body character readable inside a 192×208 cell. Preserve the same identity, proportions, face, palette, materials, outfit, and props throughout.

Avoid text, logos, UI, scenery, shadows, detached effects, motion lines, dust, floating symbols, guide marks, and chroma-key-adjacent subject colors.

Complete all standard rows:

0. idle
1. running-right
2. running-left
3. waving
4. jumping
5. failed
6. waiting
7. running/active work
8. review

Then complete the v2 look system:

- Four approved cardinal anchors: `000` up, `090` screen-right, `180` down, and `270` screen-left.
- Row 9: `000` through `157.5` in clockwise 22.5-degree steps.
- Row 10: `180` through `337.5` in clockwise 22.5-degree steps.

Cardinals are hard semantic gates. Use viewer/screen coordinates. Generate each eight-pose look row as one coherent family; never patch a final direction cell independently.

## Acceptance gates

Before packaging, require:

- incremental deterministic inspection of every standard row
- standard contact sheet and motion previews
- a written pet-specific look-mechanics plan
- approved cardinal anchors
- deterministic registration and edge checks for both look rows
- one final deterministic chroma-despill pass
- v2 atlas validation with zero errors
- cleaned extended contact and direction sheets
- explicit semantics for all sixteen directions
- three isolated blind direction reviews combined by strict majority
- independent final visual QA

The final atlas must be 1536×2288 with 192×208 cells. `pet.json` must contain `spriteVersionNumber: 2`.

Do not package through a hard failure. Intermediate blind ambiguity may be documented as a warning only when labeled normal-size review confirms the intended quadrant and the ordered loop has no visible reversal or pop.

## Privacy and publication rules

- Use repository-relative paths in all committed documentation and data.
- Never commit absolute paths, OS usernames, home-directory names, source dossiers, prompts, transcripts, API keys, environment files, browser data, or generated-image cache paths.
- Strip image metadata and inspect archives before publication.
- Keep intermediate chroma-key media and debug artifacts out of Git.
- Do not commit reference images unless the contributor has explicit redistribution rights.
- Record rights limitations without exposing private source or user information.
- Do not push, create a public repository, or publish a release unless the user explicitly approves the visibility and confirms applicable rights.

Before handing off, run the checks in `PRIVACY.md`, provide relative artifact paths, and state whether the package was merely staged, locally installed, or externally published.
