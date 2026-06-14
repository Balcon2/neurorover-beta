// NeuroRover V1 - Simple 4WD Chassis
// Units: millimeters

$fn = 48;

// --------------------
// Main settings
// --------------------
base_length = 180;
base_width  = 120;
base_thick  = 4;

corner_radius = 8;

// Motor settings
motor_length = 26;
motor_width  = 12;
motor_height = 10;

wheel_cutout_length = 42;
wheel_cutout_width  = 20;

// Screw holes
m3_hole = 3.3;
m25_hole = 2.8;

// Raspberry Pi 4 mounting holes
// Pi hole spacing approx: 58mm x 49mm
pi_x = 58;
pi_y = 49;

// --------------------
// Helper modules
// --------------------
module rounded_plate(length, width, height, radius) {
    hull() {
        translate([ radius,  radius, 0]) cylinder(h=height, r=radius);
        translate([ length-radius, radius, 0]) cylinder(h=height, r=radius);
        translate([ radius, width-radius, 0]) cylinder(h=height, r=radius);
        translate([ length-radius, width-radius, 0]) cylinder(h=height, r=radius);
    }
}

module screw_hole(x, y, d=m3_hole) {
    translate([x, y, -1])
        cylinder(h=base_thick + 2, d=d);
}

module slot(x, y, length, width) {
    translate([x, y, -1])
        cube([length, width, base_thick + 2]);
}

// --------------------
// Main chassis
// --------------------
difference() {
    // base plate
    rounded_plate(base_length, base_width, base_thick, corner_radius);

    // wheel / motor side cutouts
    slot(18, -1, wheel_cutout_length, wheel_cutout_width);
    slot(120, -1, wheel_cutout_length, wheel_cutout_width);

    slot(18, base_width - wheel_cutout_width + 1, wheel_cutout_length, wheel_cutout_width);
    slot(120, base_width - wheel_cutout_width + 1, wheel_cutout_length, wheel_cutout_width);

    // Raspberry Pi mounting holes, centered
    translate([base_length/2 - pi_x/2, base_width/2 - pi_y/2, 0]) {
        screw_hole(0, 0, m25_hole);
        screw_hole(pi_x, 0, m25_hole);
        screw_hole(0, pi_y, m25_hole);
        screw_hole(pi_x, pi_y, m25_hole);
    }

    // motor holder holes
    // front left
    screw_hole(25, 18);
    screw_hole(45, 18);

    // rear left
    screw_hole(25, 102);
    screw_hole(45, 102);

    // front right
    screw_hole(135, 18);
    screw_hole(155, 18);

    // rear right
    screw_hole(135, 102);
    screw_hole(155, 102);

    // front sensor mount holes
    screw_hole(base_length - 15, base_width/2 - 12);
    screw_hole(base_length - 15, base_width/2 + 12);

    // camera mount holes
    screw_hole(base_length - 35, base_width/2 - 10, m25_hole);
    screw_hole(base_length - 35, base_width/2 + 10, m25_hole);

    // cable holes
    screw_hole(base_length/2, 20, 8);
    screw_hole(base_length/2, base_width - 20, 8);
}

// --------------------
// Raised battery area guide
// --------------------
translate([20, base_width/2 - 18, base_thick])
difference() {
    cube([55, 36, 3]);
    translate([5, 5, -1]) cube([45, 26, 5]);
}

// --------------------
// Front sensor/camera wall
// --------------------
translate([base_length - 8, base_width/2 - 30, base_thick])
difference() {
    cube([5, 60, 35]);

    // HC-SR04 / ToF sensor opening
    translate([-1, 18, 15])
        cube([7, 24, 12]);

    // small cable hole
    translate([-1, 27, 4])
        cube([7, 8, 8]);
}

// --------------------
// Text label
// --------------------
translate([20, 8, base_thick])
linear_extrude(height = 1)
text("NeuroRover V1", size = 8);
