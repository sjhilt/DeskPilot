# Office Buddy Check Box - Bill of Materials (BOM)

## Project Overview
A toggle-switch checklist box with LED status indicators for office/desk use.  
Inspired by the aviation "Buddy Check" concept, adapted for daily office task checklists.  
**No microcontroller needed** -- pure simple wiring (toggle > resistor > LED). USB-C for power only.

**Three Versions Available:**

| Version | Dimensions | Toggles | Labels | Fits Printer |
|---------|-----------|---------|--------|-------------|
| **V1** | 171.5 x 76.2 x 38.1mm (6.75" x 3" x 1.5") | 8 | Cut-through text | 200mm+ bed |
| **V2** | 171.5 x 76.2 x 38.1mm (6.75" x 3" x 1.5") | 8 | Indent slots (stick-in) | 200mm+ bed |
| **V3 ** | 145 x 70 x 35mm (5.7" x 2.75" x 1.4") | 6 | Indent slots (stick-in) | **FlashForge Adventurer 3** (150mm) |

**Layout (all versions):**
- **FRONT FACE** -- 6 or 8 toggle switches + labels
- **TOP (lid)** -- LED indicator holes near front edge
- **BACK** -- USB-C power input (5V only)
- **RIGHT SIDE** -- 2x USB-A output ports *(optional -- only if adding USB hub)*
- **BOTTOM** -- Ventilation slots

---

## 3D Printed Parts

### V1 -- Cut-Through Text Version
| # | Part | File | Material | Notes |
|---|------|------|----------|-------|
| 1 | Bottom (toggles + engraved text on front) | `buddy_check_bottom.stl` | PLA/PETG | 0.2mm layer, 20% infill |
| 2 | Lid (LED holes on top) | `buddy_check_lid.stl` | PLA/PETG | 0.2mm layer, 30% infill |
| 3 | Lid (flipped for printing) | `buddy_check_lid_print_orientation.stl` | PLA/PETG | Same lid, print-ready |

### V2 -- Label Indent Slot Version (Recommended)
| # | Part | File | Material | Notes |
|---|------|------|----------|-------|
| 1 | Bottom (toggles + 18x8mm label recesses) | `buddy_check_v2_bottom.stl` | PLA/PETG | 0.2mm layer, 20% infill |
| 2 | Lid (LED holes on top) | `buddy_check_v2_lid.stl` | PLA/PETG | 0.2mm layer, 30% infill |
| 3 | Printable Label Template | `label_template.html` | Paper/Sticker | Open in browser, edit, print |

### V3 -- Compact / FlashForge Adventurer 3 (6 toggles, 145x70x35mm)
| # | Part | File | Material | Notes |
|---|------|------|----------|-------|
| 1 | Bottom (6 toggles + 18x8mm label recesses) | `buddy_check_v3_bottom.stl` | PLA/PETG | 0.2mm layer, 20% infill |
| 2 | Lid (6 LED holes on top) | `buddy_check_v3_lid.stl` | PLA/PETG | 0.2mm layer, 30% infill |
| 3 | Printable Label Template | `label_template.html` | Paper/Sticker | Use 6 of 8 labels |

### Design Source Files
| File | Description |
|------|-------------|
| `buddy_check_box.scad` | V1 OpenSCAD source (cut-through text, 8 toggles) |
| `buddy_check_box_v2_labels.scad` | V2 OpenSCAD source (label indent slots, 8 toggles) |
| `buddy_check_box_v3_compact.scad` | V3 OpenSCAD source (compact, 6 toggles, Adventurer 3) |
| `generate_stl.py` | CadQuery Python STL generator (V1) |

**Print Settings:**
- Nozzle: 0.4mm
- Layer Height: 0.2mm
- Infill: 20-30%
- Supports: Not required for box, may need for lid hole overhangs
- Material: PLA for prototyping, PETG for durability
- Estimated print time: ~4-6 hours total

---

## Electronics - Toggle Switches

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 1 | Mini Toggle Switch (ON-OFF) | 6 or 8 | SPST, 6mm mounting hole, 125V 6A | $8-12 (pack of 10) | Amazon / AliExpress |
| 2 | Toggle Switch Labels/Caps | 6 or 8 | Color-coded caps (optional) | $3-5 | Amazon |

**Recommended:** MTS-101 mini toggle switches (most common, cheap, reliable)

---

## Electronics - LED Indicators

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 3 | 3mm Green LEDs | 6 or 8 | 3mm, 20mA, 2.0-2.2V forward voltage | $3-5 (pack of 50) | Amazon / AliExpress |
| 4 | LED Holders/Bezels (3mm) | 6 or 8 | Chrome or black plastic clip-in holders | $3-5 (pack of 20) | Amazon |
| 5 | Resistors (150ohm) | 6 or 8 | 1/4W, for 5V supply with green LEDs | $2-3 (assorted pack) | Amazon |

**LED Color Options:** Green (task complete), Red (urgent), Blue (info), or RGB for customization

---

## Power Input (USB-C for 5V)

> **No microcontroller needed!** This is pure simple wiring -- each toggle switch directly controls its LED through a resistor. USB-C is only used for 5V power.

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 6 | USB-C Breakout Board | 1 | Exposes 5V and GND pads, panel-mountable | $3-5 (pack of 5) | Amazon / AliExpress |
| 7 | USB-C Panel Mount Connector | 1 | Female, for power input on back panel | $3-5 | Amazon |

**How it works:** Plug any USB-C cable into the back > breakout board provides 5V & GND > toggles switch power to LEDs. No code, no programming, no controller. Just solder and go!

**Alternative power options:**
- USB-C phone charger (5V 1A is more than enough for 8 LEDs)
- USB-A to USB-C cable from your computer
- Any 5V DC adapter with USB-C

### Optional: USB Hub Add-On
*If you also want USB ports on the box for charging devices or connecting peripherals:*

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 6a | USB 2.0/3.0 Hub PCB Module | 1 | 4-port USB-A, USB-C input, compact PCB | $5-10 | Amazon / AliExpress |
| 6b | USB-A Panel Mount Connectors | 2 | Female, for side-mounted output ports | $4-6 (pair) | Amazon |

*The USB hub replaces the breakout board -- it provides both 5V power for the LEDs AND USB-A output ports. Look for a FE1.1s-based 4-port USB 2.0 hub board (~30mm x 20mm).*

---

## Wiring & Power

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 9 | USB-C Cable (power input) | 1 | USB-C to USB-A or USB-C to USB-C, 3-6ft | $5-8 | Amazon |
| 10 | Hookup Wire (22 AWG) | 1 roll | Stranded, multiple colors, 22-24 AWG | $6-10 | Amazon |
| 11 | Heat Shrink Tubing | 1 pack | Assorted sizes | $3-5 | Amazon |
| 12 | Solder | 1 | 60/40 or lead-free rosin core | $5-8 | Amazon |

---

## Hardware & Fasteners

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 13 | M3 x 8mm Screws | 4 | Pan head, Phillips or hex | $3-5 (assorted box) | Amazon |
| 14 | M3 Heat-Set Inserts | 4 | Brass, for 3D printed parts | $5-8 (pack of 50) | Amazon |
| 15 | Rubber Feet (adhesive) | 4 | 10mm diameter, self-adhesive | $3-5 (pack of 20) | Amazon |
| 16 | Label Sticker / Dymo Labels | 1 set | For checklist item labels next to toggles | $5-10 | Amazon / Office supply |

### V2 Label Supplies (for indent slot version)
| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 16a | Sticker Paper (full sheet) | 1 sheet | Matte white, inkjet/laser compatible | $5-8 (pack of 25) | Amazon / Office supply |
| 16b | Clear Packing Tape (optional) | 1 roll | To laminate labels for durability | $3-5 | Amazon |
| 16c | Precision Craft Knife / Scissors | 1 | For cutting 18mm x 8mm labels | Already have | -- |

**V2 Label Instructions:**
1. Open `label_template.html` in your browser
2. Click each label to edit the text to your checklist items
3. Print on sticker/adhesive paper at 100% scale (no scaling!)
4. Cut out each 18mm x 8mm label along the borders
5. Press labels into the recessed slots on the front face -- they sit flush!
6. Optional: cover with a strip of clear tape for water/smudge resistance

---

## Optional Enhancements

| # | Component | Qty | Specs | Est. Price | Source |
|---|-----------|-----|-------|------------|--------|
| 17 | Arduino Nano / Pro Micro | 1 | For smart LED control, USB HID, or app integration | $5-10 | Amazon |
| 18 | WS2812B NeoPixel LEDs (3mm) | 8 | Addressable RGB, if using microcontroller | $5-8 | Amazon |
| 19 | Reset Button (momentary) | 1 | 6mm, panel mount, to reset all toggles visually | $2-3 | Amazon |
| 20 | Small Speaker/Buzzer | 1 | Piezo buzzer for completion alert | $2-3 | Amazon |
| 21 | Clear Acrylic Label Window | 1 | Laser-cut, for professional label display on lid | $3-5 | Local fab / Amazon |

---

## Tools Required

| Tool | Notes |
|------|-------|
| 3D Printer | FDM printer (150mm+ bed for V3, 200mm+ for V1/V2) |
| Soldering Iron | For LED/switch wiring |
| Wire Strippers | 22-24 AWG |
| Drill + 6mm & 3mm bits | To clean up printed holes |
| Step Drill Bit | For USB port cutouts (optional) |
| Hot Glue Gun | For securing components |
| Multimeter | For testing connections |
| Heat-Set Insert Tool | Soldering iron tip for M3 inserts |

---

## Wiring Diagram

### Basic Build (Power Only -- No Controller Needed!)
```
USB-C Cable ──> USB-C Breakout Board (back panel)
                    │
                    ├── 5V ──┬── Toggle 1 ── 150ohm ── LED 1 ──┐
                    │        ├── Toggle 2 ── 150ohm ── LED 2 ──┤
                    │        ├── Toggle 3 ── 150ohm ── LED 3 ──┤
                    │        ├── Toggle 4 ── 150ohm ── LED 4 ──┤
                    │        ├── Toggle 5 ── 150ohm ── LED 5 ──┤
                    │        ├── Toggle 6 ── 150ohm ── LED 6 ──┤
                    │        ├── Toggle 7 ── 150ohm ── LED 7 ──┤
                    │        └── Toggle 8 ── 150ohm ── LED 8 ──┤
                    │                                         │
                    └── GND ──────────────────────────────────┘
```

**That's it!** Each toggle switch directly controls its LED. Flip ON = LED lights up green. No code, no microcontroller, no programming. Pure electrical circuit.

**Power draw:** 8 LEDs x 20mA = 160mA total (any USB charger can handle this easily)

### Optional: With USB Hub
```
USB-C Cable ──> USB Hub PCB Module ──> USB-A Port 1 (right side)
                    │                ──> USB-A Port 2 (right side)
                    │
                    ├── 5V (from hub's internal 5V) ──> Toggle/LED circuit (same as above)
                    └── GND ──> Common ground
```

---

## Estimated Total Cost

### Basic Build (power only, no USB hub)
| Category | Est. Cost |
|----------|-----------|
| 3D Printing Filament | $2-4 |
| Toggle Switches (8x) | $8-12 |
| LEDs + Resistors + Holders | $8-13 |
| USB-C Breakout Board + Cable | $8-13 |
| Wiring & Solder | $14-23 |
| Hardware (screws, inserts, feet) | $11-18 |
| **TOTAL (Basic Build)** | **$51-83** |

### With USB Hub Add-On
| Add-On | Est. Cost |
|--------|-----------|
| USB Hub PCB Module | +$5-10 |
| USB-A Panel Mount Connectors (2x) | +$4-6 |
| **TOTAL with USB Hub** | **$60-99** |

### Optional Enhancements | +$17-29

---

## Suggested Office Checklist Labels (Example)

1. Check Email
2. Review Calendar
3. Update Security Logs
4. Check Dashboards
5. Backup Files
6. Update Task Board
7. Sync Reports
8. End-of-Day Shutdown

*Customize labels to match your daily workflow!*

---

## Assembly Notes

### For V1 (cut-through text, 8 toggles):
Print `buddy_check_bottom.stl` + `buddy_check_lid_print_orientation.stl`

### For V2 (label indent slots, 8 toggles):
Print `buddy_check_v2_bottom.stl` + `buddy_check_v2_lid.stl`

### For V3 (compact, 6 toggles, Adventurer 3) :
Print `buddy_check_v3_bottom.stl` + `buddy_check_v3_lid.stl`

### Steps (all versions):
1. **Print** bottom box and lid (see files above for your version)
2. **Clean up** the toggle switch holes (6.2mm) on the FRONT FACE -- use a 6mm drill bit if needed
3. **Clean up** the USB-C cutout on the back wall (and USB-A cutouts on right side if using hub)
4. **Install** M3 heat-set inserts into the 4 corner screw posts (use soldering iron)
5. **Mount** the toggle switches into the FRONT FACE holes (6 for V3, 8 for V1/V2 -- they thread in with included nuts)
6. **Mount** LED holders into the LED holes on the TOP LID (near the front edge)
7. **Wire** each toggle switch (on front) to its corresponding LED (on lid) with a 150ohm resistor in series
8. **Connect** all LEDs to common ground, all toggles to 5V from USB-C breakout board
9. **Mount** USB-C breakout board near back panel cutout (or USB hub if using that option)
10. **Test** all connections with multimeter before closing
11. **Place** lid onto box and secure with 4x M3 screws through countersunk holes
12. **Attach** rubber feet to bottom
13. **Labels:**
    - **V1:** Text is already cut through the front wall -- no labels needed!
    - **V2:** Print labels using `label_template.html`, cut to 18mm x 8mm, press into front face recesses

---

*Generated: 2026-02-16 | Project: Office Buddy Check Box*
