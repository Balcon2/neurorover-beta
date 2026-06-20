// Raspberry Pi optional mounting plate, units mm
$fn=48; L=72; W=60; T=3; pix=58; piy=49; m25=2.8;
difference(){
 cube([L,W,T]);
 translate([L/2-pix/2,W/2-piy/2,-1]){
  cylinder(h=T+2,d=m25); translate([pix,0,0]) cylinder(h=T+2,d=m25);
  translate([0,piy,0]) cylinder(h=T+2,d=m25); translate([pix,piy,0]) cylinder(h=T+2,d=m25);
 }
 translate([L/2,W/2,-1]) cylinder(h=T+2,d=14);
}
