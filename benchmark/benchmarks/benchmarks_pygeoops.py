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

from benchmark.benchmarker import RunResult  # noqa: E402
from benchmark.benchmarks import testdata  # noqa: E402
import pygeoops  # noqa: E402

logger = logging.getLogger(__name__)
nb_rows_simplify = 50000


def _get_package() -> str:
    return "pygeoops"


def _get_version() -> str:
    return pygeoops.__version__


def difference_collection(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]

    # Prepare some complex polygons to test with
    poly_complex1 = testdata.create_complex_poly(
        xmin=0.123,
        ymin=0.123,
        width=20000,
        height=20000,
        line_distance=500,
        max_segment_length=100,
    )
    print(f"num_coordinates: {shapely.get_num_coordinates(poly_complex1)}")
    poly_complex_list = []
    for offset in range(0, 000, 10):
        poly_complex_list.append(
            testdata.create_complex_poly(
                xmin=100 + offset,
                ymin=100 + offset,
                width=1000,
                height=1000,
                line_distance=500,
                max_segment_length=500,
            )
        )
    print(
        f"nb in complex list: {len(poly_complex_list)}, each "
        f"{shapely.get_num_coordinates(poly_complex_list[0])} points"
    )

    # Go!
    start_time = datetime.now()

    poly_complex_collection = shapely.GeometryCollection(poly_complex_list)
    result = pygeoops.difference_all_tiled(poly_complex1, poly_complex_collection)

    operation_descr = (
        f"{function_name} with {shapely.get_num_coordinates(poly_complex1)} and "
        f"{shapely.get_num_coordinates(poly_complex1)} points gave area {result.area}"
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


def simplify_lang(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")
    input_filtered_path = tmp_dir / f"input_{nb_rows_simplify}rows.gpkg"
    if not input_filtered_path.exists():
        geoms_gdf.to_file(input_filtered_path, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    geoms_gdf.geometry = pygeoops.simplify(
        geometry=geoms_gdf.geometry, tolerance=1, algorithm="lang"
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

    geoms_gdf.to_file(tmp_dir / f"{function_name}_output.gpkg")

    # Cleanup and return
    return result


def simplify_lang_plus(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")
    input_filtered_path = tmp_dir / f"input_{nb_rows_simplify}rows.gpkg"
    if not input_filtered_path.exists():
        geoms_gdf.to_file(input_filtered_path, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    geoms_gdf.geometry = pygeoops.simplify(
        geometry=geoms_gdf.geometry, tolerance=1, algorithm="lang+"
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

    geoms_gdf.to_file(tmp_dir / f"{function_name}_output.gpkg")

    # Cleanup and return
    return result


def simplify_rdp(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")
    input_filtered_path = tmp_dir / f"input_{nb_rows_simplify}rows.gpkg"
    if not input_filtered_path.exists():
        geoms_gdf.to_file(input_filtered_path, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    geoms_gdf.geometry = pygeoops.simplify(
        geometry=geoms_gdf.geometry, tolerance=1, algorithm="rdp"
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

    geoms_gdf.to_file(tmp_dir / f"{function_name}_output.gpkg")

    # Cleanup and return
    return result


def simplify_rdp_keep_points_on(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")
    input_filtered_path = tmp_dir / f"input_{nb_rows_simplify}rows.gpkg"
    if not input_filtered_path.exists():
        geoms_gdf.to_file(input_filtered_path, engine="pyogrio")

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
    geoms_gdf.geometry = pygeoops.simplify(
        geometry=geoms_gdf.geometry,
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

    geoms_gdf.to_file(tmp_dir / f"{function_name}_output.gpkg")

    # Cleanup and return
    return result


def simplify_rdp_geopandas(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]
    input_path = testdata.TestFile.AGRIPRC_2018.get_file(tmp_dir)
    geoms_gdf = gpd.read_file(input_path, rows=nb_rows_simplify, engine="pyogrio")
    input_filtered_path = tmp_dir / f"input_{nb_rows_simplify}rows.gpkg"
    if not input_filtered_path.exists():
        geoms_gdf.to_file(input_filtered_path, engine="pyogrio")

    # Go!
    start_time = datetime.now()
    geoms_gdf.geometry = geoms_gdf.geometry.simplify(tolerance=1)
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

    geoms_gdf.to_file(tmp_dir / f"{function_name}_output.gpkg")

    # Cleanup and return
    return result
