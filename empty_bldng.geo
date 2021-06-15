cs=2.;
cl=10.;
Point(1) = {-160, 75, 0, cl};
Point(2) = {-160, -75, 0, cl};
Point(3) = {160, -75, 0, cl};
Point(4) = {160, 75, 0, cl};
Point(5) = {160, 75, 120, cl};
Point(6) = {160, -75, 120, cl};
Point(7) = {-160, -75, 120, cl};
Point(8) = {-160, 75, 120, cl};
Line(1) = {7, 2};
Line(2) = {2, 1};
Line(3) = {1, 8};
Line(4) = {8, 7};
Line(5) = {7, 6};
Line(6) = {6, 5};
Line(7) = {5, 4};
Line(8) = {4, 3};
Line(9) = {3, 6};
Line(10) = {3, 2};
Line(11) = {8, 5};
Line(12) = {4, 1};
Line Loop(13) = {1, -10, 9, -5};
Plane Surface(14) = {13};
Line Loop(15) = {8, 10, 2, -12};
Plane Surface(16) = {15};
Line Loop(17) = {4, 1, 2, 3};
Plane Surface(18) = {17};
Line Loop(19) = {3, 11, 7, 12};
Plane Surface(20) = {19};
Line Loop(21) = {6, -11, 4, 5};
Plane Surface(22) = {21};
Line Loop(23) = {6, 7, 8, 9};
Plane Surface(24) = {23};
Point(9) = {12, 12, 0, cs};
Point(10) = {-12, 12, 0, cs};
Point(11) = {-12, -12, 0, cs};
Point(12) = {12, -12, 0, cs};
Point(13) = {12, -12, 24, cs};
Point(14) = {12, 12, 24, cs};
Point(15) = {-12, 12, 24, cs};
Point(16) = {-12, -12, 24, cs};
Line(25) = {11, 16};
Line(26) = {13, 16};
Line(27) = {16, 15};
Line(28) = {15, 14};
Line(29) = {14, 13};
Line(30) = {13, 12};
Line(31) = {12, 11};
Line(32) = {11, 10};
Line(33) = {10, 15};
Line(34) = {14, 9};
Line(35) = {12, 9};
Line(36) = {9, 10};
Delete {
  Surface{16};
}
Line Loop(37) = {31, 32, -36, -35};
Plane Surface(38) = {15, 37};
Line Loop(39) = {26, -25, -31, -30};
Plane Surface(40) = {39};
Line Loop(41) = {25, 27, -33, -32};
Plane Surface(42) = {41};
Line Loop(43) = {33, 28, 34, 36};
Plane Surface(44) = {43};
Line Loop(45) = {29, 30, 35, -34};
Plane Surface(46) = {45};
Line Loop(47) = {29, 26, 27, 28};
Plane Surface(48) = {47};
Surface Loop(49) = {14, 18, 22, 24, 20, 38, 46, 48, 40, 42, 44};
Volume(50) = {49};
Physical Surface(1) = {18};
Physical Surface(2) = {20, 14};
Physical Surface(3) = {22};
Physical Surface(4) = {24};
Physical Surface(5) = {38};
Physical Surface(6) = {42, 46, 48, 44, 40};
Physical Volume(56) = {50};