# -*- coding: utf-8 -*-
"""
Module to benchmark pygeoops operations.
"""

from datetime import datetime
import inspect
import logging
from pathlib import Path

import os

os.environ["USE_PYGEOS"] = "0"
import geopandas as gpd  # noqa: E402
import shapely  # noqa: E402

from benchmarker import RunResult  # noqa: E402
from benchmarks import testdata  # noqa: E402
import pygeoops  # noqa: E402

################################################################################
# Some init
################################################################################

logger = logging.getLogger(__name__)
nb_rows_simplify = 50000

################################################################################
# The real work
################################################################################


def _get_package() -> str:
    return "pygeoops"


def _get_version() -> str:
    return pygeoops.__version__


def simplify_lang(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    pygeoops.simplify(geometry=geoms_gdf.geometry.array, tolerance=1, algorithm="lang")
    operation_descr = (
        f"{function_name} on agri parcel layer BEFL (~{nb_rows_simplify} polygons)"
    )
    result = RunResult(
        package=_get_package(),
        package_version=_get_version(),
        operation=function_name,
        secs_taken=(datetime.now() - start_time).total_seconds(),
        operation_descr=operation_descr,
        run_details=None,
    )

    # Cleanup and return
    return result


def simplify_rdp(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    pygeoops.simplify(geometry=geoms_gdf.geometry.array, tolerance=1, algorithm="rdp")
    operation_descr = (
        f"{function_name} on agri parcel layer BEFL (~{nb_rows_simplify} polygons)"
    )
    result = RunResult(
        package=_get_package(),
        package_version=_get_version(),
        operation=function_name,
        secs_taken=(datetime.now() - start_time).total_seconds(),
        operation_descr=operation_descr,
        run_details=None,
    )

    # Cleanup and return
    return result


def simplify_rdp_keep_points_on(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")

    keep_points_on = shapely.LineString(
        [
            (150000, 150000),
            (150000, 200000),
            (200000, 200000),
            (200000, 150000),
            (150000, 150000),
        ]
    )

    # Go!
    start_time = datetime.now()
    pygeoops.simplify(
        geometry=geoms_gdf.geometry.array,
        tolerance=1,
        algorithm="rdp",
        keep_points_on=keep_points_on,
    )
    operation_descr = (
        f"{function_name} on agri parcel layer BEFL (~{nb_rows_simplify} polygons)"
    )
    result = RunResult(
        package=_get_package(),
        package_version=_get_version(),
        operation=function_name,
        secs_taken=(datetime.now() - start_time).total_seconds(),
        operation_descr=operation_descr,
        run_details=None,
    )

    # Cleanup and return
    return result


def simplify_rdp_geopandas(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    geoms_gdf.simplify(tolerance=1)
    operation_descr = (
        f"{function_name} on agri parcel layer BEFL (~{nb_rows_simplify} polygons)"
    )
    result = RunResult(
        package=_get_package(),
        package_version=_get_version(),
        operation=function_name,
        secs_taken=(datetime.now() - start_time).total_seconds(),
        operation_descr=operation_descr,
        run_details=None,
    )

    # Cleanup and return
    return result
