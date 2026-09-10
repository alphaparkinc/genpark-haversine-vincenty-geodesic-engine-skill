from client import GeodesicEngine

def main():
    print("=== Testing Haversine Geodesic Engine ===")
    geo = GeodesicEngine()
    # SF to NYC approx 4100km
    d = geo.haversine(37.7749, -122.4194, 40.7128, -74.0060)
    print(f"Distance SF -> NYC: {d/1000.0:.1f} km")
    assert 4000000 < d < 4300000
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
