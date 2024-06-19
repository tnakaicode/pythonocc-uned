import os
from pathlib import Path

import geouned
from geouned.GEOUNED.utils_occ.DataExchange import read_step_file_with_names_colors

if __name__ == '__main__':
    print(geouned)

    my_options = geouned.Options(
        forceCylinder=False,
        newSplitPlane=True,
        delLastNumber=False,
        enlargeBox=2,
        nPlaneReverse=0,
        splitTolerance=0,
        scaleUp=True,
        quadricPY=False,
        Facets=False,
        prnt3PPlane=False,
        forceNoOverlap=False,
    )

    my_tolerances = geouned.Tolerances(
        relativeTol=False,
        relativePrecision=0.000001,
        value=0.000001,
        distance=0.0001,
        angle=0.0001,
        pln_distance=0.0001,
        pln_angle=0.0001,
        cyl_distance=0.0001,
        cyl_angle=0.0001,
        sph_distance=0.0001,
        kne_distance=0.0001,
        kne_angle=0.0001,
        tor_distance=0.0001,
        tor_angle=0.0001,
        min_area=0.01,
    )

    my_numeric_format = geouned.NumericFormat(
        P_abc="14.7e",
        P_d="14.7e",
        P_xyz="14.7e",
        S_r="14.7e",
        S_xyz="14.7e",
        C_r="12f",
        C_xyz="12f",
        K_xyz="13.6e",
        K_tan2="12f",
        T_r="14.7e",
        T_xyz="14.7e",
        GQ_1to6="18.15f",
        GQ_7to9="18.15f",
        GQ_10="18.15f",
    )

    my_settings = geouned.Settings(
        matFile="",
        voidGen=True,
        debug=False,
        compSolids=True,
        simplify="no",
        exportSolids="",
        minVoidSize=200.0,  # units mm
        maxSurf=50,
        maxBracket=30,
        voidMat=[],
        voidExclude=[],
        startCell=1,
        startSurf=1,
        sort_enclosure=False,
    )

    geo = geouned.CadToCsg(
        options=my_options,
        settings=my_settings,
        tolerances=my_tolerances,
        numeric_format=my_numeric_format,
    )
    
    step_file = f"../testing/inputSTEP/large/Triangle.stp"
    read_step_file_with_names_colors(step_file)
    geo.load_step_file(filename=step_file, skip_solids=[])

    geo.start()

    geo.export_csg(
        title="Converted with GEOUNED",
        geometryName=f"test",
        outFormat=(
            "mcnp",
        ),
        volSDEF=True,  # changed from the default
        volCARD=False,  # changed from the default
        UCARD=None,
        dummyMat=True,  # changed from the default
        cellCommentFile=False,
        cellSummaryFile=False,  # changed from the default
    )
