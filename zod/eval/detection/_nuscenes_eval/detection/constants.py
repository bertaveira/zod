# nuScenes dev-kit.
# Code written by Oscar Beijbom and Varun Bankiti, 2019.

DETECTION_NAMES = [
    "Vehicle",
    "VulnerableVehicle",
    "Pedestrian",
    "TrafficSign",
    "TrafficSignal",
]

PRETTY_DETECTION_NAMES = {
    "car": "Car",
    "truck": "Truck",
    "bus": "Bus",
    "trailer": "Trailer",
    "construction_vehicle": "Constr. Veh.",
    "pedestrian": "Pedestrian",
    "motorcycle": "Motorcycle",
    "bicycle": "Bicycle",
    "traffic_cone": "Traffic Cone",
    "barrier": "Barrier",
}

DETECTION_COLORS = {
    "car": "C0",
    "truck": "C1",
    "bus": "C2",
    "trailer": "C3",
    "construction_vehicle": "C4",
    "pedestrian": "C5",
    "motorcycle": "C6",
    "bicycle": "C7",
    "traffic_cone": "C8",
    "barrier": "C9",
}

TP_METRICS = ["trans_err", "scale_err", "orient_err"]

PRETTY_TP_METRICS = {
    "trans_err": "Trans.",
    "scale_err": "Scale",
    "orient_err": "Orient.",
}

TP_METRICS_UNITS = {
    "trans_err": "m",
    "scale_err": "1-IOU",
    "orient_err": "rad.",
}
