#!/usr/bin/env python3
"""
3D Printer Buddy Check Box - CadQuery STL Generator
Toggle switches on the FRONT face, LEDs on the top, labels on top.
Text labels CUT THROUGH the lid so they glow when LEDs are on.
Inspired by aviation BuddyCheck boxes.
Dimensions: 6.75" x 3" x 1.5" (171.45mm x 76.2mm x 38.1mm)
"""

import cadquery as cq
import os

# ============================================================
# DIMENSIONS (all in mm)
# ============================================================
BOX_L = 171.45    # 6.75 inches (left to right)
BOX_W = 76.2      # 3.00 inches (front to back / depth)
BOX_H = 38.1      # 1.50 inches (height)

WALL = 2.5
BOTTOM = 2.5
LID_T = 3.0
LID_INSET = 4.0
LID_GAP = 0.3
FILLET_R = 2.0

# Toggle switches - FRONT FACE (Y=0 wall)
NUM_TOGGLES = 8
TOGGLE_DIA = 6.2
TOGGLE_Z = BOX_H / 2
TOGGLE_X_START = 16.0
TOGGLE_X_END = BOX_L - 16.0
TOGGLE_SPACING = (TOGGLE_X_END - TOGGLE_X_START) / (NUM_TOGGLES - 1)

# LEDs - TOP (lid), near front edge
LED_DIA = 3.2
LED_Y = 10.0

# ============================================================
# CHECKLIST LABELS - cut through the lid so they glow!
# Change these to customize your daily checklist
# ============================================================
CHECKLIST_LABELS = [
    "COFFEE",
    "EMAIL",
    "CALENDAR",
    "STANDUP",
    "SECURITY",
    "BACKUPS",
    "TASKS",
    "READY",
]

# Text settings - on FRONT FACE above each toggle
TEXT_SIZE = 3.0        # font size in mm - smaller to fit full words
TEXT_DEPTH = WALL + 0.2  # cut all the way through the front wall
TEXT_Z_ABOVE = 9.0     # how far above toggle center the text sits

# USB-C input (back wall)
USBC_W = 9.5
USBC_H = 3.8
USBC_X = BOX_L / 2
USBC_Z = BOX_H / 2 - 3

# USB-A outputs (right side)
USBA_W = 14.5
USBA_H = 7.5
NUM_USBA = 2
USBA_SPACING = 20.0
USBA_Y = BOX_W / 2
USBA_Z = BOX_H / 2 - 3

# Screw posts
POST_OD = 7.0
POST_ID = 3.0
POST_INSET = 8.0
POST_H = BOX_H - BOTTOM - LID_T - LID_INSET + 1

# Ventilation
VENT_W = 2.0
VENT_L = 30.0
NUM_VENTS = 5
VENT_SPACING = 8.0

OUTPUT_DIR = "/Users/stephenhi/Desktop/3DPrinterBuddyCheck"

# ============================================================
# BOTTOM ENCLOSURE
# ============================================================
def make_bottom():
    print("Building bottom enclosure (toggles on front face)...")
    box_h = BOX_H - LID_INSET

    outer = (
        cq.Workplane("XY")
        .box(BOX_L, BOX_W, box_h, centered=False)
        .edges("|Z")
        .fillet(FILLET_R)
    )

    inner = (
        cq.Workplane("XY")
        .transformed(offset=(WALL, WALL, BOTTOM))
        .box(BOX_L - 2*WALL, BOX_W - 2*WALL, box_h, centered=False)
        .edges("|Z")
        .fillet(max(FILLET_R - WALL/2, 0.5))
    )
    result = outer.cut(inner)

    # Toggle switch holes + CUT-THROUGH TEXT on FRONT FACE
    for i in range(NUM_TOGGLES):
        tx = TOGGLE_X_START + i * TOGGLE_SPACING
        label = CHECKLIST_LABELS[i] if i < len(CHECKLIST_LABELS) else f"ITEM {i+1}"

        # Toggle hole
        toggle_hole = (
            cq.Workplane("XZ")
            .transformed(offset=(tx, TOGGLE_Z, -0.1))
            .circle(TOGGLE_DIA / 2)
            .extrude(WALL + 0.2)
        )
        result = result.cut(toggle_hole)

        # CUT-THROUGH TEXT above toggle on FRONT FACE
        # XZ plane at Y=0 (front wall), text centered at X=tx, Z=toggle_z + offset
        text_z = TOGGLE_Z + TEXT_Z_ABOVE
        text_cut = (
            cq.Workplane("XZ")
            .transformed(offset=(tx, text_z, -0.1))
            .text(label, TEXT_SIZE, TEXT_DEPTH, font="Arial", halign="center", valign="center")
        )
        result = result.cut(text_cut)

    # USB-C (back wall)
    usbc_hole = (
        cq.Workplane("XZ")
        .transformed(offset=(USBC_X, USBC_Z, BOX_W - WALL))
        .rect(USBC_W, USBC_H)
        .extrude(WALL + 1)
    )
    result = result.cut(usbc_hole)

    # USB-A (right side)
    for i in range(NUM_USBA):
        y_pos = USBA_Y + (i - (NUM_USBA-1)/2) * USBA_SPACING
        usba_hole = (
            cq.Workplane("YZ")
            .transformed(offset=(y_pos, USBA_Z, BOX_L - WALL))
            .rect(USBA_W, USBA_H)
            .extrude(WALL + 1)
        )
        result = result.cut(usba_hole)

    # Ventilation slots
    for i in range(NUM_VENTS):
        vx = BOX_L/2 + (i - (NUM_VENTS-1)/2) * VENT_SPACING
        vent = (
            cq.Workplane("XY")
            .transformed(offset=(vx - VENT_W/2, BOX_W/2 - VENT_L/2, -0.1))
            .box(VENT_W, VENT_L, BOTTOM + 0.2, centered=False)
        )
        result = result.cut(vent)

    # Screw posts
    corners = [
        (POST_INSET, POST_INSET),
        (BOX_L - POST_INSET, POST_INSET),
        (POST_INSET, BOX_W - POST_INSET),
        (BOX_L - POST_INSET, BOX_W - POST_INSET),
    ]
    for cx, cy in corners:
        post = (
            cq.Workplane("XY")
            .transformed(offset=(cx, cy, BOTTOM))
            .circle(POST_OD / 2)
            .extrude(POST_H)
        )
        hole = (
            cq.Workplane("XY")
            .transformed(offset=(cx, cy, BOTTOM - 0.1))
            .circle(POST_ID / 2)
            .extrude(POST_H + 0.2)
        )
        result = result.union(post).cut(hole)

    # Lid support ledge
    ledge_z = box_h - LID_T
    ledge = (
        cq.Workplane("XY")
        .transformed(offset=(WALL - 1.2, WALL - 1.2, ledge_z))
        .box(BOX_L - 2*(WALL - 1.2), BOX_W - 2*(WALL - 1.2), LID_T, centered=False)
    )
    ledge_cut = (
        cq.Workplane("XY")
        .transformed(offset=(WALL + 0.8, WALL + 0.8, ledge_z - 0.1))
        .box(BOX_L - 2*(WALL + 0.8), BOX_W - 2*(WALL + 0.8), LID_T + 0.2, centered=False)
    )
    result = result.union(ledge).cut(ledge_cut)

    return result


# ============================================================
# LID / TOP PANEL with CUT-THROUGH TEXT LABELS
# ============================================================
def make_lid():
    print("Building lid with cut-through text labels...")
    print(f"  Labels: {CHECKLIST_LABELS}")

    lid_inner_l = BOX_L - 2*WALL - 2*LID_GAP
    lid_inner_w = BOX_W - 2*WALL - 2*LID_GAP

    # Main lid plate
    lid = (
        cq.Workplane("XY")
        .box(BOX_L, BOX_W, LID_T, centered=False)
        .edges("|Z")
        .fillet(FILLET_R)
    )

    # Inset lip
    lip = (
        cq.Workplane("XY")
        .transformed(offset=(WALL + LID_GAP, WALL + LID_GAP, -LID_INSET))
        .box(lid_inner_l, lid_inner_w, LID_INSET, centered=False)
        .edges("|Z")
        .fillet(max(FILLET_R - WALL, 0.5))
    )
    lid = lid.union(lip)

    # --- LED holes only (text labels are on the front face of the bottom box) ---
    for i in range(NUM_TOGGLES):
        tx = TOGGLE_X_START + i * TOGGLE_SPACING

        # LED hole through top
        led_hole = (
            cq.Workplane("XY")
            .transformed(offset=(tx, LED_Y, -LID_INSET - 0.1))
            .circle(LED_DIA / 2)
            .extrude(LID_T + LID_INSET + 0.2)
        )
        lid = lid.cut(led_hole)

    # Screw holes + countersinks
    corners = [
        (POST_INSET, POST_INSET),
        (BOX_L - POST_INSET, POST_INSET),
        (POST_INSET, BOX_W - POST_INSET),
        (BOX_L - POST_INSET, BOX_W - POST_INSET),
    ]
    for cx, cy in corners:
        screw = (
            cq.Workplane("XY")
            .transformed(offset=(cx, cy, -LID_INSET - 0.1))
            .circle(3.4 / 2)
            .extrude(LID_T + LID_INSET + 0.2)
        )
        lid = lid.cut(screw)

        csink = (
            cq.Workplane("XY")
            .transformed(offset=(cx, cy, LID_T - 1.5))
            .circle(6.0 / 2)
            .extrude(1.6)
        )
        lid = lid.cut(csink)

    return lid


# ============================================================
# MAIN
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate bottom
    bottom = make_bottom()
    bottom_path = os.path.join(OUTPUT_DIR, "buddy_check_bottom.stl")
    cq.exporters.export(bottom, bottom_path)
    print(f"  Saved: {bottom_path}")

    # Generate lid with text
    lid = make_lid()
    lid_path = os.path.join(OUTPUT_DIR, "buddy_check_lid.stl")
    cq.exporters.export(lid, lid_path)
    print(f"  Saved: {lid_path}")

    # Lid flipped for printing
    lid_flipped = lid.mirror("XY", basePointVector=(0, 0, LID_T/2))
    lid_print_path = os.path.join(OUTPUT_DIR, "buddy_check_lid_print_orientation.stl")
    cq.exporters.export(lid_flipped, lid_print_path)
    print(f"  Saved: {lid_print_path}")

    print(f"\n{'='*60}")
    print(f"3D PRINTER BUDDY CHECK BOX - STL Generation Complete!")
    print(f"{'='*60}")
    print(f"  Box: {BOX_L:.1f} x {BOX_W:.1f} x {BOX_H:.1f} mm")
    print(f"       ({BOX_L/25.4:.2f}\" x {BOX_W/25.4:.2f}\" x {BOX_H/25.4:.2f}\")")
    print(f"")
    print(f"  FRONT FACE: {NUM_TOGGLES} toggle switch holes ({TOGGLE_DIA}mm)")
    print(f"  TOP LID:")
    print(f"    {NUM_TOGGLES} LED holes ({LED_DIA}mm) near front edge")
    print(f"    {NUM_TOGGLES} CUT-THROUGH text labels (glow when lit!):")
    for i, label in enumerate(CHECKLIST_LABELS):
        print(f"      Toggle {i+1}: {label}")
    print(f"  BACK: USB-C input ({USBC_W}x{USBC_H}mm)")
    print(f"  RIGHT: {NUM_USBA}x USB-A ({USBA_W}x{USBA_H}mm)")
    print(f"  BOTTOM: {NUM_VENTS} vent slots")
    print(f"  CORNERS: 4x M3 screw posts")
    print(f"\n  Output dir: {OUTPUT_DIR}")
    print(f"\n  TIP: Print the lid in a light color (white/natural)")
    print(f"  and use colored LEDs for best glow-through effect!")


if __name__ == "__main__":
    main()
