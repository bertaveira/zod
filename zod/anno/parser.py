"""Annotation parsers."""
import json
from typing import Any, Dict, List

from zod.anno.lane import LaneAnnotation, parse_lane_annotation
from zod.anno.road_condition import RoadConditionAnnotation
from zod.constants import AnnotationProject

from .object import ObjectAnnotation
from .tsr.traffic_sign import TrafficSignAnnotation


def _read_annotation_file(annotation_file: str) -> List[Dict[str, Any]]:
    """Read an annotation file."""
    with open(annotation_file, "r") as file:
        return json.load(file)


def parse_object_detection_annotation(annotation_path: str) -> List[ObjectAnnotation]:
    """Parse the objects annotation from the annotation string."""
    annotation = _read_annotation_file(annotation_path)
    return [ObjectAnnotation.from_dict(obj) for obj in annotation]


def parse_traffic_sign_annotation(annotation_path: str) -> List[TrafficSignAnnotation]:
    """Parse the traffic sign annotation from the annotation string."""
    annotation = _read_annotation_file(annotation_path)
    return [TrafficSignAnnotation.from_dict(sign) for sign in annotation]


def parse_lane_markings_annotation(annotation_path: str) -> List[LaneAnnotation]:
    """Parse the lane markings annotation from the annotation string."""
    annotations = _read_annotation_file(annotation_path)
    return [parse_lane_annotation(marker) for marker in annotations]


def parse_ego_road_annotation(annotation_path: str) -> List[Dict]:
    """Parse the egoroad annotation from the annotation string."""
    annotations = _read_annotation_file(annotation_path)
    polygons = []
    for annotation in annotations:
        if "class" in annotation["properties"]:
            polygons.append(annotation["geometry"]["coordinates"])
        else:
            # TODO: what does it mean if we end up here?
            pass
    return polygons


def parse_road_condition_annotation(annotation_path) -> RoadConditionAnnotation:
    with open(annotation_path, "r") as file:
        annotation = json.load(file)
    return RoadConditionAnnotation.from_dict(annotation["properties"])


ANNOTATION_PARSERS = {
    AnnotationProject.LANE_MARKINGS: parse_lane_markings_annotation,
    AnnotationProject.EGO_ROAD: parse_ego_road_annotation,
    AnnotationProject.OBJECT_DETECTION: parse_object_detection_annotation,
    AnnotationProject.TRAFFIC_SIGNS: parse_traffic_sign_annotation,
    AnnotationProject.ROAD_CONDITION: parse_road_condition_annotation,
}
