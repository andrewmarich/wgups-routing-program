# WGUPS Routing Program

Coursework for WGU's C950 (Data Structures and Algorithms II). A delivery simulation: 40 packages, three trucks, one route per truck, and a console interface to check any package's status at any time of day.

## What it does

- Loads the package file, address table, and distance matrix from `data/`.
- Stores every package in a hash table built from scratch (`HashTable.py`): chained buckets keyed by package ID, with insert, lookup, and remove.
- Orders each truck's deliveries with a nearest-neighbor heuristic and tracks mileage and delivery times at 18 mph (`main.py`).
- Answers "where is package N at HH:MM?" as at the hub, en route, or delivered with the delivery time.
- Shows package 9's corrected address (410 S State St) in status output from 10:20, as the scenario describes. This is display only: routing still uses the original address.

## Run it

Python 3, no dependencies.

```sh
python3 main.py
```

Type `start`, then choose a menu option: package status at a time (one package or all 40) or total mileage.

With the included data the total distance is **101.3 miles** (truck 1: 27.9, truck 2: 29.2, truck 3: 44.2).

## How it works

| File | Role |
|---|---|
| `HashTable.py` | Chained hash table for package lookup |
| `Package.py` | Package record and time-based status |
| `Truck.py` | Truck state: capacity 16, speed 18 mph, mileage, clock |
| `main.py` | Data loading, truck loads, routing, and the menu |

## Limitations

- Nearest-neighbor is a greedy heuristic: it is simple and fast but not optimal.
- Packages are assigned to trucks by hand from the scenario's notes. The program orders each truck's deliveries but does not check deadlines or special instructions itself.
- Truck 3's departure time is set to when truck 1 finishes (9:33), but its route clock still starts at its initial 10:20 departure. Its delivery times are calculated from 10:20, while its "en route" status can show from 9:33, so truck 3's scheduling is inconsistent.
- Package 9's address correction affects displayed status only, not the route.
- Return trips to the hub are not counted in mileage.
- The hash table has a fixed 100 buckets and does not resize.
- Input handling is minimal.

The scenario files in `data/` come from the course.
