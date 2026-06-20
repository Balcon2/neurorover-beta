// Front camera and sensor mount, units mm
$fn=48; W=70; H=48; T=4; m25=2.8; m3=3.3;
difference(){
 union(){cube([T,W,H]); cube([22,W,T]);}
 translate([-1,W/2-12,22]) cube([T+2,24,18]);
 translate([-1,W/2-21,16]) rotate([0,90,0]) cylinder(h=T+2,d=m25);
 translate([-1,W/2+21,16]) rotate([0,90,0]) cylinder(h=T+2,d=m25);
 translate([-1,W/2-14,6]) cube([T+2,28,10]);
 translate([12,14,-1]) cylinder(h=T+2,d=m3);
 translate([12,W-14,-1]) cylinder(h=T+2,d=m3);
}
