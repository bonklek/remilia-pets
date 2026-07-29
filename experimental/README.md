# Experimental pets

These builds are available for local testing and motion-template research. They passed deterministic Codex v2 atlas validation, but use the preview review profile and are not release-qualified.

Included packages:

- Bremo
- Moxie
- Piko
- Rizzo
- Shilo
- Tavi 3D
- Velo
- Zimbo

Each pet has three matching directories:

- `pets/<pet>/` — installable `pet.json` and `spritesheet.webp`
- `previews/<pet>/` — animation GIFs plus contact and direction sheets
- `motion-donors/<pet>/` — reusable source rows and a hash-bearing manifest

To test one, copy the complete `experimental/pets/<pet>/` directory to your Codex custom-pet directory. Treat duplicate choreography as valid character output, not as new movement-template coverage.
