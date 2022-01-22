from inspect import trace
from django.shortcuts import render
import libs.sequential as seq
import libs.list_comprehension as lc
import libs.generator as gen
import libs.multiprocessing_solution as mp
import json
import time
import tracemalloc
from .models import Table
from .serializers import TableSerializer
from django.http import JsonResponse

def get_closest_special_sequential(request):
    n, m, points = _get_data_from_request(request)
    res = _do_work_with_measuring(seq.get_closest_special, n, m, points)
    json_res = json.dumps(res)
    return JsonResponse(json_res, safe=False, status=200)

def get_closest_special_list_comprehension(request):
    n, m, points = _get_data_from_request(request)
    res = _do_work_with_measuring(lc.get_closest_special, n, m, points)
    json_res = json.dumps(res)
    return JsonResponse(json_res, safe=False, status=200)

def get_closest_special_generator(request):
    n, m, points = _get_data_from_request(request)
    res = _do_work_with_measuring(gen.get_closest_special, n, m, points)
    json_res = json.dumps(res)
    return JsonResponse(json_res, safe=False, status=200)

def get_closest_special_multiprocessing(request):
    n, m, points = _get_data_from_request(request)
    res = _do_work_with_measuring(mp.get_closest_special, n, m, points)
    json_res = json.dumps(res)
    return JsonResponse(json_res, safe=False, status=200)

def _do_work_with_measuring(func_to_execute, n, m, points):
    tracemalloc.start()
    start = time.time()
    result = func_to_execute(n, m, points)
    _, max_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    elapsed_time = end - start
    response_data = {"result": result, "time_in_s": elapsed_time, "max_memory_in_MB": max_memory / 10**6}
    return response_data

def _get_data_from_request(request):
    data = json.loads(request.body)
    n, m, points = int(data["n"]), int(data["m"]), data["points"]
    point_list = _get_points_from_json(points)
    return n, m, point_list

def _get_points_from_json(json_points):
    point_list = []
    for point in json_points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        point_list.append((x, y))
    return point_list