# nano-banana-json-prompting

A Claude Code plugin with two skills for working with **Nano Banana Pro
(Gemini 3 Pro Image)** — one that turns plain English into precise, reproducible
JSON specs, and one that actually renders images via the Gemini API and saves
them into your project.

## What it does

### `json-prompting-for-nano-banana` — write a spec

Translates plain-English requests into one of five structured JSON schema types.
JSON prompting gives precise, reproducible control — the same spec produces the
same result, and you can iterate on a single element without regenerating
everything else.

| Schema | Use for |
|--------|---------|
| `marketing_image` | Product shots, hero images, brand photography, ads |
| `ui_builder` | App screens, dashboards, websites, interface mockups |
| `diagram_spec` | Flowcharts, architecture diagrams, process maps |
| `data_viz` | Charts and graphs where numerical accuracy matters |
| `social_graphic` | Platform-specific social posts with text overlays |

### `nano-banana-pro` — render an image

Calls Google's Gemini 3 Pro Image model (`gemini-3-pro-image-preview`) to
generate a PNG/JPG and save it into your project — hero images, OG/social
images, illustrations, icons, backgrounds, product mockups, or edits/compositions
of existing images. Requires a `GEMINI_API_KEY` (or Vertex AI auth) and the
`google-genai` + `pillow` Python deps. See
[`skills/nano-banana-pro/README.md`](skills/nano-banana-pro/README.md) for setup.

## Installation

Load the plugin directly from this directory:

```bash
claude --plugin-dir /path/to/nano-banana-json-prompting
```

Once loaded, the skill activates automatically when you ask Claude to create the
kinds of images listed above, or you can invoke it explicitly.

## Usage

Describe the image you want in natural language, for example:

> Hero shot for a lime seltzer brand called Aurora Lime. 12oz can on a
> reflective surface with lime slices and ice cubes. Dark teal background,
> dramatic side lighting.

The skill classifies the intent, gathers any missing requirements, and emits a
complete, valid JSON spec. Copy that spec into Nano Banana Pro (the Gemini app
with the "Thinking" model, or Google AI Studio) with the instruction:

> Render this specification as a high-fidelity image

To iterate, modify specific fields (lighting, camera angle, theme colors, data
values, …) and re-render. See the skill for detailed iteration patterns.

For the `nano-banana-pro` rendering skill, after loading the plugin, install its
deps and set an API key (one-time):

```bash
bash "${CLAUDE_PLUGIN_ROOT}/skills/nano-banana-pro/install.sh"
export GEMINI_API_KEY=your_key_here
```

Then ask naturally — e.g. *"generate a 16:9 hero image of a misty pine forest at
sunrise and save it to public/hero.png"* — and Claude runs the bundled script.

## Layout

```
.
├── .claude-plugin/
│   └── plugin.json                       # plugin manifest
├── skills/
│   ├── json-prompting-for-nano-banana/
│   │   └── SKILL.md                      # NL → JSON spec translator
│   └── nano-banana-pro/
│       ├── SKILL.md                      # renders images via the Gemini API
│       ├── generate_image.py             # bundled generation script
│       ├── install.sh                    # installs Python deps
│       ├── requirements.txt
│       └── README.md
└── README.md
```

## Credits

The `json-prompting-for-nano-banana` skill is derived from
[jawhnycooke/claude-code-nano-banana](https://github.com/jawhnycooke/claude-code-nano-banana).
