from OCC.Core.TopoDS import TopoDS_Builder
from OCC.Core.TopoDS import TopoDS_Compound, TopoDS_CompSolid


def compsolid(topo):
    """
    accumulate a bunch of TopoDS_* in list `topo` to a TopoDS_Compound
    @param topo: list of TopoDS_* instances
    """
    bd = TopoDS_Builder()
    comp = TopoDS_Compound()
    bd.MakeCompSolid(comp)
    for i in topo:
        bd.Add(comp, i)
    return comp
