import geometry as geo


wcp = geo.WeightedColoredPoint("A", 1.0, -5.0, "red", 4.0)
p = geo.Point("B", 4.0, -9.0)
d1 = p.distance(wcp) # MRO: Point=found here [, F, object]
d2 = wcp.distance(p) # MRO: WCP, WP=found here [, CP, P, F, object]
print(wcp, p, d1, d2, sep='\n')

print(geo.WeightedColoredPoint.__mro__)