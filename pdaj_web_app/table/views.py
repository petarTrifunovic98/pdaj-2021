from django.shortcuts import render
import libs.pdaj_project_lib as ppl
import json

def get_closest_special_sequential(request):
    data = json.loads(request.body)
    n, m, points = data["n"], data["m"], data["points"]
    point_list = _get_points_from_json(points)


def _get_points_from_json(json_points):
    point_list = []
    for point in json_points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        point_list.append((x, y))
    return point_list