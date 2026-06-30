# nano-banana-json-prompting

A Claude Code plugin that converts natural language descriptions into structured
JSON schemas for **Nano Banana Pro (Gemini 3 Pro Image)**. JSON prompting gives
precise, reproducible control over image generation — the same spec produces the
same result, and you can iterate on a single element without regenerating
everything else.

## What it does

The plugin ships a single skill, `json-prompting-for-nano-banana`, that acts as a
translator from plain-English requests into one of five schema types:

| Schema | Use for |
|--------|---------|
| `marketing_image` | Product shots, hero images, brand photography, ads |
| `ui_builder` | App screens, dashboards, websites, interface mockups |
| `diagram_spec` | Flowcharts, architecture diagrams, process maps |
| `data_viz` | Charts and graphs where numerical accuracy matters |
| `social_graphic` | Platform-specific social posts with text overlays |

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

## Layout

```
.
├── .claude-plugin/
│   └── plugin.json                       # plugin manifest
├── skills/
│   └── json-prompting-for-nano-banana/
│       └── SKILL.md                      # the translator skill
└── README.md
```

## Credits

The skill is derived from
[jawhnycooke/claude-code-nano-banana](https://github.com/jawhnycooke/claude-code-nano-banana).
