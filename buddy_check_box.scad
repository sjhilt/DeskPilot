// ============================================================
// 3D Printer Buddy Check Box - OpenSCAD Design
// Toggle switches + text labels on FRONT FACE
// LED holes on TOP LID
// ============================================================
// Dimensions: 6.75" x 3" x 1.5" (171.45mm x 76.2mm x 38.1mm)
// X = length (left-right), Y = depth (front-back), Z = height
// ============================================================
// IMPORTANT: Use F6 (Render) to see all holes and text properly!
// F5 Preview may not show difference() operations with text.
// ============================================================

// --- RENDER CONTROL ---
render_part = "both"; // "bottom", "lid", or "both"

// --- DIMENSIONS (mm) ---
box_length = 171.45;  // 6.75"
box_width  = 76.2;    // 3.00"  
box_height = 38.1;    // 1.50"

wall = 2.5;
bottom_thick = 2.5;
lid_thick = 3.0;
lid_inset = 4.0;
lid_gap = 0.3;

// Toggle switches - FRONT FACE
num_toggles = 8;
toggle_dia = 6.2;       // 6mm mounting hole + clearance
toggle_z = 14.0;        // center height of toggles on front face
toggle_margin = 16.0;   // margin from edges
toggle_spacing = (box_length - 2*toggle_margin) / (num_toggles - 1);

// LEDs on top
led_dia = 3.2;
led_y_offset = 10.0;   // from front edge of lid

// Text labels on front face
checklist_labels = [
    "COFFEE", 
    "EMAIL", 
    "CAL", 
    "STNDUP",
    "SEC", 
    "BCKUPS", 
    "BREAK", 
    "DONE"
];
text_size = 3.0;
text_z_offset = 9.0;   // above toggle center

// USB ports
usbc_w = 9.5;  usbc_h = 3.8;
usba_w = 14.5; usba_h = 7.5;

// Screw posts
post_od = 7; post_id = 3; post_inset = 8;

// ============================================================
// BOTTOM ENCLOSURE - with toggle holes + text on front
// ============================================================
module bottom_box() {
    box_h = box_height - lid_inset;
    
    difference() {
        // Outer shell - simple cube
        cube([box_length, box_width, box_h]);
        
        // Hollow out inside
        translate([wall, wall, bottom_thick])
            cube([box_length - 2*wall, box_width - 2*wall, box_h]);
        
        // === FRONT FACE FEATURES (Y=0 plane) ===
        for (i = [0 : num_toggles - 1]) {
            tx = toggle_margin + i * toggle_spacing;
            
            // Toggle switch hole - cylinder through front wall
            translate([tx, -1, toggle_z])
                rotate([-90, 0, 0])
                    cylinder(d=toggle_dia, h=wall+2, $fn=32);
            
            // Text label above toggle - cut through front wall
            translate([tx, wall+1, toggle_z + text_z_offset])
                rotate([90, 0, 0])
                    linear_extrude(height=wall+2)
                        text(checklist_labels[i], 
                             size=text_size,
                             font="Liberation Sans:style=Bold",
                             halign="center",
                             valign="center");
        }
        
        // === USB-C on back wall ===
        translate([box_length/2 - usbc_w/2, box_width - wall - 1, box_h/2 - usbc_h/2 - 3])
            cube([usbc_w, wall+2, usbc_h]);
        
        // === USB-A on right side ===
        translate([box_length - wall - 1, box_width/2 - usba_w/2 - 10, box_h/2 - usba_h/2 - 3])
            cube([wall+2, usba_w, usba_h]);
        translate([box_length - wall - 1, box_width/2 - usba_w/2 + 10, box_h/2 - usba_h/2 - 3])
            cube([wall+2, usba_w, usba_h]);
        
        // === Ventilation slots on bottom ===
        for (i = [0:4]) {
            vx = box_length/2 + (i-2) * 8;
            translate([vx - 1, box_width/2 - 15, -1])
                cube([2, 30, bottom_thick+2]);
        }
    }
    
    // Screw posts inside corners
    for (pos = [[post_inset, post_inset],
                [box_length-post_inset, post_inset],
                [post_inset, box_width-post_inset],
                [box_length-post_inset, box_width-post_inset]]) {
        translate([pos[0], pos[1], bottom_thick])
            difference() {
                cylinder(d=post_od, h=box_h - bottom_thick - lid_thick, $fn=32);
                translate([0, 0, -0.5])
                    cylinder(d=post_id, h=box_h, $fn=24);
            }
    }
    
    // Lid support ledge (perimeter shelf)
    difference() {
        translate([wall-1.5, wall-1.5, box_h - lid_thick])
            cube([box_length - 2*(wall-1.5), box_width - 2*(wall-1.5), lid_thick]);
        translate([wall+1, wall+1, box_h - lid_thick - 0.1])
            cube([box_length - 2*(wall+1), box_width - 2*(wall+1), lid_thick+0.2]);
    }
}

// ============================================================
// LID - LED holes on top
// ============================================================
module lid() {
    difference() {
        union() {
            // Top plate
            cube([box_length, box_width, lid_thick]);
            // Inset lip that drops into the box
            translate([wall+lid_gap, wall+lid_gap, -lid_inset])
                cube([box_length - 2*(wall+lid_gap), 
                      box_width - 2*(wall+lid_gap), 
                      lid_inset]);
        }
        
        // LED holes
        for (i = [0 : num_toggles - 1]) {
            tx = toggle_margin + i * toggle_spacing;
            translate([tx, led_y_offset, -lid_inset - 1])
                cylinder(d=led_dia, h=lid_thick + lid_inset + 2, $fn=24);
        }
        
        // Screw holes + countersinks
        for (pos = [[post_inset, post_inset],
                     [box_length-post_inset, post_inset],
                     [post_inset, box_width-post_inset],
                     [box_length-post_inset, box_width-post_inset]]) {
            // Through hole
            translate([pos[0], pos[1], -lid_inset - 1])
                cylinder(d=3.4, h=lid_thick + lid_inset + 2, $fn=24);
            // Countersink
            translate([pos[0], pos[1], lid_thick - 1.5])
                cylinder(d1=3.4, d2=6.5, h=1.6, $fn=24);
        }
    }
}

// ============================================================
// RENDER
// ============================================================
if (render_part == "bottom") {
    bottom_box();
} else if (render_part == "lid") {
    translate([0, 0, lid_thick])
        rotate([180, 0, 0])
            translate([0, -box_width, 0])
                lid();
} else {
    // Assembled view
    color("SlateGray") bottom_box();
    translate([0, 0, box_height - lid_inset])
        color("White", 0.9) lid();
}
