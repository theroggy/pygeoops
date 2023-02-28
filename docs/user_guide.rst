.. currentmodule:: pygeoops

User guide
==========

PyGeoOps provides some less common or extended spatial algorithms and utility functions.

A full list of functionalities can be found in the 
:ref:`API reference<API-reference>`. 

As a quick start, here are some examples on how PyGeoOps can be used.

Determine a centerline for a shapely polygon
--------------------------------------------

.. code-block:: python

    import pygeoops
    import shapely

    polygon = shapely.from_wkt("POLYGON ((0 0, 0 8, -2 10, 4 10, 2 8, 2 2, 10 2, 10 0, 0 0))")
    centerline = pygeoops.centerline(polygon)


|centerline_L_shape|


.. |centerline_L_shape| image:: ./_static/images/centerline_fancy_Lshape.png
        :alt: Centerline of a fancy L shaped polygon