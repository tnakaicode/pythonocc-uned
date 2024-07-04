import sys, os
from pathlib import Path
import pytest

sys.path.append(os.path.join("./src/"))
import geouned

path_to_mcnp = Path("testing/MCNP_Reverse")
mcnp_files = list(Path("testing/MCNP_Reverse").rglob("*.mcnp")) + list(Path("testing/outMCNP").rglob("*.i"))

@pytest.mark.parametrize("csg_format", ["mcnp", "openmc_xml"])
def test_cylbox_convertion(csg_format):

    if csg_format == "openmc_xml":
        suffix = ".xml"
    elif csg_format == "mcnp":
        suffix = ".mcnp"

    geo = geouned.CsgToCad()

    geo.export_cad(
        # csg file was made from testing/inputSTEP/cylBox.stp
        input_filename=f"tests/csg_files/cylinder_box{suffix}",
        csg_format=csg_format,
        bounding_box=[-1000.0, -500.0, -1000.0, 0, 0, 0.0],
        # TODO add tests for these args that counts volumes in cad file
        # cell_range_type='exclude',
        # cell_range=(2,3,4),
        output_filename=f"tests_outputs/csgtocad/{csg_format}",
    )

    assert Path(f"tests_outputs/csgtocad/{csg_format}.step").exists()
    assert Path(f"tests_outputs/csgtocad/{csg_format}.FCStd").exists()

@pytest.mark.parametrize("input_csg_file", mcnp_files)
def test_reverse_convertion(input_csg_file):

    # sets up an output folder for the results
    output_dir = Path("tests_outputs") / input_csg_file.with_suffix("")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_filename_stem = output_dir / input_csg_file.stem

    geo = geouned.CsgToCad()

    geo.export_cad(
        # csg file was made from testing/inputSTEP/cylBox.stp
        input_filename=input_csg_file,
        csg_format="mcnp",
        bounding_box=[-1000.0, -500.0, -1000.0, 0, 0, 0.0],
        # TODO add tests for these args that counts volumes in cad file
        # cell_range_type='exclude',
        # cell_range=(2,3,4),
        output_filename=f"{output_filename_stem.resolve()}",
    )
