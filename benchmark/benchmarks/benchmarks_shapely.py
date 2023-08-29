# -*- coding: utf-8 -*-
"""
Module to benchmark pygeoops operations.
"""

from datetime import datetime
import inspect
import logging
from pathlib import Path

import shapely

from benchmark.benchmarker import RunResult
from benchmark.benchmarks.testdata import TestData

logger = logging.getLogger(__name__)


def _get_package() -> str:
    return "shapely"


def _get_version() -> str:
    return shapely.__version__


def difference_collection(tmp_dir: Path) -> RunResult:
    # Init
    function_name = inspect.currentframe().f_code.co_name  # type: ignore[union-attr]

    # Prepare some complex polygons to test with
    poly_complex, complex_poly_descr = TestData.get_complex_poly()
    print(complex_poly_descr)
    poly_complex_coll, complex_coll_descr = TestData.get_complex_poly_collection()
    print(complex_coll_descr)

    # Go!
    # poly_complex_coll = shapely.unary_union(poly_complex_coll)
    start_time = datetime.now()

    """
    result = poly_complex
    for poly_complex2 in shapely.get_parts(poly_complex_coll):
        result = shapely.difference(result, poly_complex2)
    """
    result = shapely.difference(poly_complex, poly_complex_coll)

    operation_descr = (
        f"{function_name}: {complex_poly_descr} differenced with "
        f"{complex_coll_descr} gave area: {result.area}"
    )
    print(operation_descr)
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
