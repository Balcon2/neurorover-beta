// N20 motor mount, print 4x, units mm
$fn=48; l=34; w=18; h=16; m3=3.3;
difference(){
 cube([l,w,h]);
 translate([l/2,w/2,h/2]) rotate([90,0,0]) cylinder(h=w+2,d=12.5);
 translate([3,-1,4]) cube([27,w+2,9]);
 translate([8,w/2,-1]) cylinder(h=h+2,d=m3);
 translate([26,w/2,-1]) cylinder(h=h+2,d=m3);
 translate([l/2-8,-1,h-5]) cube([16,w+2,2.5]);
}
