import sys
import json
from client import GeodesicEngine

def main():
    geo = GeodesicEngine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "distance":
            d = geo.haversine(params.get("lat1"), params.get("lon1"), params.get("lat2"), params.get("lon2"))
            res = {"distance_meters": d, "distance_km": d / 1000.0}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
