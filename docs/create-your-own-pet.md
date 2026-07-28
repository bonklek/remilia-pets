# Create your own Codex pet

There are two useful paths: the guided desktop flow and the full production workflow.

## Quick desktop flow

1. Open **Settings → Pets** in the ChatGPT desktop app.
2. Select **Create your own pet**.
3. Describe the character, colors, silhouette, style, personality, and distinctive features.
4. Let the generated pet task finish.
5. Return to **Settings → Pets**, select **Refresh**, and choose the new pet.
6. Use `/pet` to wake or hide it.

Custom pets created in the desktop app are stored locally and do not automatically sync to the web.

## A strong pet brief

Include:

- a short name
- species or character type
- a compact full-body silhouette
- palette and material or drawing style
- face and eye construction
- hair, ears, headwear, clothing, markings, or props that must remain consistent
- personality and emotional range
- explicit avoidances such as text, logos, scenery, or detached effects
- the intended rights scope: private review, internal use, or cleared publication

Example:

> Create a friendly moth librarian with charcoal wings, warm amber eyes, oversized round glasses, and a tiny canvas satchel. Use rough storybook ink, a compact full-body silhouette, and gentle, slightly anxious expressions. Keep the same glasses, markings, palette, and proportions in every animation. No text, logos, scenery, shadows, or detached sparkles. Private review only.

## Remilia inspiration

For Remilia-inspired pets, we recommend using the assets from [Remilia Achievements](https://achievements.remilia.org/) as inspiration. Browse its achievement art and collection traits for ideas about palette, silhouette, clothing, props, expressions, and personality, then translate those cues into a compact original pet design that remains readable at Codex pet size.

## Full v2 workflow with an agent

Inside a project that contains this repository, ask Codex:

> Follow `AGENTS.md` and the installed `hatch-pet` and `$imagegen` workflows. Help me turn the following concept into a complete private-review Codex v2 pet. Keep a visible four-stage checklist, validate every row incrementally, complete the cardinal and sixteen-direction system, run blind and independent final QA, and package only after all hard gates pass: `<your concept>`.

The agent should:

1. Confirm or infer the name, description, references, style, and rights scope.
2. Create a canonical base image as the identity source of truth.
3. Generate and validate the nine standard animation rows.
4. Write a character-specific look-mechanics plan.
5. Generate and approve the four cardinal anchors.
6. Generate both coherent look-direction rows.
7. Assemble the 8×11 v2 atlas deterministically.
8. Run chroma cleanup, structural validation, contact-sheet review, motion review, direction semantics, three blind reviews, and independent final visual QA.
9. Package `pet.json` and `spritesheet.webp` together.

## Frame-rate expectations

The Codex pet format uses fixed, small animation budgets. Waving uses four frames, jumping uses five, common idle/work states use six, and directional running uses eight. Timing is controlled by the app, not `pet.json`. Smoothness comes from thoughtful pose spacing, easing, loop closure, and secondary motion rather than adding unlimited frames.

## Installing a packaged pet

A package directory contains:

```text
my-pet/
  pet.json
  spritesheet.webp
```

Copy that complete directory into:

- macOS/Linux: `~/.codex/pets/`
- Windows: `%USERPROFILE%\.codex\pets\`

Refresh **Settings → Pets**, then choose the pet.

## Web uploads

The web pet uploader uses a different standard sprite-sheet shape: a transparent PNG or WebP exactly 1536×1872 and no larger than 20 MiB. A Codex v2 desktop package uses the extended 1536×2288 atlas and `spriteVersionNumber: 2`; do not confuse the two formats.

## Before sharing

Review `PRIVACY.md`, include the repository's `LICENSE`, and confirm that the package contains only publication-safe material.

Official product overview: <https://learn.chatgpt.com/docs/pets>
