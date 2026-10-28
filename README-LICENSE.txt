ELEVATION DATA - SOURCE AND LICENSE
===================================

This file ships inside every download from the ATS Global Elevation Explorer
(https://elevation.allthingsspatial.io/). Keep it with the GeoTIFF: the
attribution below is required whenever the data, or anything derived from it,
is published or passed on.

Downloaded from the ATS Global Elevation Explorer on Oct 26, 2026.

  Product      Copernicus GLO-30 (cop-dem-glo-30)
  Resolution   30 m nominal
  Contents     Whole 1-degree tile as published, Float32 Cloud-Optimized GeoTIFF, EPSG:4326
  Files        Copernicus_DSM_COG_10_N42_00_E024_00_DEM.tif
  Source tiles N42 E024 (Copernicus_DSM_COG_10_N42_00_E024_00_DEM)
  Edition      Apr 22, 2021 (publication date of this edition; radar acquired 2011-2015)

-----------------------------------------------------------------------------
COPERNICUS DEM (GLO-30 / GLO-90)
-----------------------------------------------------------------------------

Required attribution, verbatim:

  (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018
  provided under COPERNICUS by the European Union and ESA; all rights reserved.

Citation DOI:  https://doi.org/10.5270/ESA-c5d3d65

Product description:
  https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

About the product:
  - Digital SURFACE model (DSM): includes buildings, forest canopy and other
    features standing on the terrain. It is not a bare-earth (DTM) product.
  - Horizontal datum: WGS84 (EPSG:4326). Vertical datum: EGM2008 geoid.
    Heights are metres above the geoid, NOT above the WGS84 ellipsoid.
  - Edition date 2021-04-22. That is the publication date of this edition; the
    underlying TanDEM-X radar acquisitions are from 2011-2015.
  - Pixel values are Float32 metres. No-data is a very large negative value.

-----------------------------------------------------------------------------
NASADEM
-----------------------------------------------------------------------------

Required credit:

  NASADEM (NASA/JPL-Caltech); Microsoft Planetary Computer.

About the product:
  - Reprocessed SRTM, acquired February 2000. Coverage 56 S to 61 N.
  - Also a surface model. Heights are metres above the EGM96 geoid.

-----------------------------------------------------------------------------
DELIVERY
-----------------------------------------------------------------------------

Data accessed live from the Microsoft Planetary Computer STAC and data APIs
(https://planetarycomputer.microsoft.com/). Planetary Computer terms of use:
https://planetarycomputer.microsoft.com/terms

All Things Spatial LLC does not host, alter or redistribute a stored copy of
this data. The app reads the published product and, where you asked for a clip,
resamples it to the area you drew. No warranty is given as to fitness for any
particular purpose; verify the data before relying on it.

Tool: ATS Global Elevation Explorer, All Things Spatial LLC
      https://www.allthingsspatial.io/
