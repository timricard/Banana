# nano-banana-pro

A Claude Code skill that generates custom images with Google's **Nano Banana Pro** (Gemini 3 Pro Image, model id `gemini-3-pro-image-preview`). Once the plugin is loaded, Claude Code will automatically call this skill whenever you ask for a hero image, OG image, illustration, or any other custom visual for your project.

## Install

This skill ships as part of the `nano-banana-json-prompting` plugin. Load the plugin, then install the Python deps and set an API key.

### 1. Load the plugin

```bash
claude --plugin-dir /path/to/nano-banana-json-prompting
```

### 2. Install Python deps

```bash
bash "${CLAUDE_PLUGIN_ROOT}/skills/nano-banana-pro/install.sh"
```

This runs `pip install -r requirements.txt` (`google-genai` + `pillow`).

### 3. Get an API key and export it

Grab one at <https://aistudio.google.com/apikey> (free tier available), then add to your shell rc (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export GEMINI_API_KEY=your_key_here
```

Reload your shell: `source ~/.zshrc`.

## Use

Just talk naturally inside Claude Code:

- *"Generate a hero image for the landing page — moody mountain sunrise, cinematic, leave room on the right for headline text. Save to `public/hero.png`."*
- *"I need a 1:1 OG image for the blog with our brand color #1F6FEB."*
- *"Take `assets/logo.png` and put it on a deep navy gradient background, 16:9, save to `public/og.png`."*

Claude will pick the prompt, parameters, and output path, then run the script and wire the image into your code.

You can also call the script directly:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/nano-banana-pro/generate_image.py" \
  "A wide cinematic shot of a misty pine forest at sunrise" \
  -o public/hero.png \
  --aspect-ratio 16:9 \
  --size 2K
```

### Flags

| Flag | Default | Notes |
|---|---|---|
| `prompt` (positional) | required | The text description. |
| `-o, --output` | required | Output file path. Parent dirs are created. |
| `--aspect-ratio` | `16:9` | One of: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`. |
| `--size` | `2K` | One of: `1K`, `2K`, `4K`. |
| `--input PATH` | (none) | Reference image to edit/compose. Repeatable. |
| `--model` | `gemini-3-pro-image-preview` | Override the model id. |

## Use Vertex AI instead of the Gemini API

The same script works with Vertex AI — useful if your team already has GCP billing set up and wants enterprise auth (no API key floating around).

```bash
gcloud auth application-default login
gcloud services enable aiplatform.googleapis.com --project YOUR_PROJECT

export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=global   # or us-central1
```

The script auto-detects the Vertex flag and switches client modes. ADC is used for auth — no API key needed.

## Troubleshooting

- **`GEMINI_API_KEY is not set`** — export the key (step 3) and restart your shell.
- **`No module named google.genai`** — re-run `install.sh`. If you have multiple Python installs, point the script at the right one: `PYTHON=$(which python3) "$PYTHON" "${CLAUDE_PLUGIN_ROOT}/skills/nano-banana-pro/generate_image.py" ...`
- **`RAI filtered` / safety block** — soften the prompt. Avoid named real people, branded characters, violent or explicit content.
- **HTTP 429 / quota** — you've hit the free-tier limit. Wait, raise quota in AI Studio, or switch to the Vertex path.
- **Skill doesn't trigger** — confirm the plugin is loaded; try a more explicit prompt like "use the nano-banana-pro skill to make an image of...".

## Costs

The Gemini API has a free tier suitable for experimenting. Paid tier pricing is per image and depends on size — check <https://ai.google.dev/pricing> for the current rates. Vertex AI is billed through your GCP project.

## License

MIT — do whatever you want.
