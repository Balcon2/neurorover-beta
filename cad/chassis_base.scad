// NeuroRover V1 main chassis base, units mm
$fn=64;
L=190; W=125; T=4; R=8; m3=3.3; m25=2.8; pix=58; piy=49;
module h(x,y,d){translate([x,y,-1]) cylinder(h=T+2,d=d);}
module slot(x,y,l,w){translate([x,y,-1]) cube([l,w,T+2]);}
module rounded(){hull(){
translate([R,R,0]) cylinder(h=T,r=R);
translate([L-R,R,0]) cylinder(h=T,r=R);
translate([R,W-R,0]) cylinder(h=T,r=R);
translate([L-R,W-R,0]) cylinder(h=T,r=R);}}
difference(){
 rounded();
 slot(14,-1,48,23); slot(128,-1,48,23); slot(14,W-22,48,23); slot(128,W-22,48,23);
 translate([L/2-pix/2,W/2-piy/2,0]){h(0,0,m25);h(pix,0,m25);h(0,piy,m25);h(pix,piy,m25);}
 h(24,18,m3);h(46,18,m3);h(144,18,m3);h(166,18,m3);
 h(24,107,m3);h(46,107,m3);h(144,107,m3);h(166,107,m3);
 h(L-20,W/2-18,m3);h(L-20,W/2+18,m3);h(L-38,W/2-12,m25);h(L-38,W/2+12,m25);
 h(75,22,10);h(75,W-22,10);h(118,W/2,14);
 slot(20,W/2-24,6,48);slot(78,W/2-24,6,48);
}
translate([28,W/2-22,T]) cube([46,3,3]);
translate([28,W/2+19,T]) cube([46,3,3]);
translate([20,8,T]) linear_extrude(height=.8) text("NeuroRover V1",size=8);
