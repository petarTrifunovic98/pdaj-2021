from inspect import trace
from django.shortcuts import render
import libs.sequential as seq
import json
import time
import tracemalloc
from .models import Table
from .serializers import TableSerializer
from django.http import JsonResponse

def get_closest_special_sequential(request):
    data = json.loads(request.body)
    n, m, points = int(data["n"]), int(data["m"]), data["points"]
    point_list = _get_points_from_json(points)

    tracemalloc.start()
    start = time.time()
    result = seq.get_closest_special(n, m, point_list)
    _, max_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    elapsed_time = end - start
    table = Table()
    table.result = json.dumps(result)
    table.time_in_s = elapsed_time
    table.max_memory_in_MB = max_memory / 10**6
    serializer = TableSerializer(table, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)


def _get_points_from_json(json_points):
    point_list = []
    for point in json_points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        point_list.append((x, y))
    return point_list