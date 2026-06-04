# abeer's macropad

A custom 3-key macropad built from scratch — PCB, case, and firmware — as part of Hack Club's hackpad program. The three keys map to **Copy, Paste, and Cut**, making it a handy little clipboard companion.

## Overview

| | |
|---|---|
| **Keys** | 3 (MX-style mechanical switches) |
| **Microcontroller** | Seeed XIAO RP2040 |
| **Firmware** | KMK (CircuitPython) |
| **Case** | Sandwich-mount, fully 3D-printed |
| **Wiring** | Direct (each switch to GND, no diodes) |

## What each key does

| Key | Action |
|-----|--------|
| SW1 | Copy (Ctrl+C) |
| SW2 | Paste (Ctrl+V) |
| SW3 | Cut (Ctrl+X) |

## Design

### Assembled render
![Assembled macropad](screenshots/render.png)

### Schematic
![Schematic](screenshots/schematic.png)

### PCB layout
![PCB layout](screenshots/pcb.png)

### 3D case
![3D case](screenshots/case.png)

## Bill of Materials (BOM)

| Component | Qty | Notes |
|-----------|-----|-------|
| Seeed XIAO RP2040 | 1 | Microcontroller |
| MX-style mechanical switch | 3 | One per key |
| DSA keycap (blank) | 3 | |
| M3 × 16 mm screw | 4 | Holds the sandwich together |
| M3 heatset insert (M3×5×4mm) | 4 | Seated in the bottom shell |
| 3D-printed case (top plate) | 1 | Top.STEP |
| 3D-printed case (bottom shell) | 1 | Bottom.STEP |
| Custom PCB | 1 | 2-layer, ~27 × 61 mm |

## Firmware

Firmware is written in **KMK** (runs on CircuitPython).

To flash:
1. Install CircuitPython on the XIAO RP2040 (hold BOOT, plug in USB, drag the `.uf2` onto the `RPI-RP2` drive).
2. Copy the `kmk` folder onto the `CIRCUITPY` drive.
3. Copy `main.py` onto the `CIRCUITPY` drive.

The switches are wired directly to pins **D10, D9, D8** and GND, using internal pull-ups.

## Repository structure
