import geometry as geo


wcp = geo.WeightedColoredPoint("A", 1.0, -5.0, "red", 4.0)
p = geo.Point("B", 4.0, -9.0)
d1 = p.distance(wcp) # MRO: Point=found here [, F, object]
d2 = wcp.distance(p) # MRO: WCP, WP=found here [, CP, P, F, object]
print(wcp, p, d1, d2, sep='\n')

print(geo.WeightedColoredPoint.__mro__)

wp = geo.WeightedPoint.from_point_weight(p, 456.789)

print(wp)

p2: geo.Point = geo.Point.copy(p)
wcp2: geo.WeightedColoredPoint = geo.WeightedColoredPoint.copy(wcp)
# wcp3 = geo.Point.copy(wcp) # TODO: improve copy to use only attribute necessary
# wcp4 = geo.WeightedColoredPoint.copy(p)
print("Copies:", p2, wcp2)

# f = geo.Form("F") # Error: cannot instantiate
