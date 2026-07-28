# Privacy and publication checklist

Run this checklist before every commit, push, release, or archive upload.

## Filesystem and identity

- [ ] No absolute Windows, macOS, or Linux paths.
- [ ] No usernames, home-directory names, email addresses, account IDs, device names, or organization-internal names.
- [ ] No `.env` files, API keys, tokens, cookies, browser profiles, session data, or application caches.
- [ ] No Git author identity is being exposed unintentionally; use the GitHub-provided no-reply address if attribution is desired without publishing a private email.

## Pet-generation material

- [ ] No source dossier or private reference directory.
- [ ] No reference art without explicit redistribution permission.
- [ ] No prompts or transcripts containing private user context.
- [ ] No run manifests or QA logs containing local paths.
- [ ] No rejected generations or debug artifacts.
- [ ] No pre-despill chroma-key previews presented as final artwork.

## Images and archives

- [ ] Images have been checked for EXIF, XMP, comments, author fields, and embedded paths.
- [ ] Images contain no accidental text, signatures, watermarks, sensitive symbols, or private background details.
- [ ] Archives have been listed and inspected before upload.
- [ ] Checksums correspond to the exact files being released.

## Repository and Git history

- [ ] `git status` contains only intended files.
- [ ] A case-insensitive search for local usernames, platform-specific home-directory paths, secrets, and tokens returns no findings.
- [ ] The full Git history—not only the current working tree—has been checked before publication.
- [ ] Repository visibility is explicitly chosen.
- [ ] The repository license matches the intended visibility and distribution terms.

If any check fails, keep the repository local or private until the issue is resolved. Deleting a file in a later commit does not remove it from earlier Git history.
