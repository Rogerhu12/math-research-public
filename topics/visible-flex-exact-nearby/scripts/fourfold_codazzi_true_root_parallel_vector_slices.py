"""TCXV: retain all96 coordinates when a complete upper vector is zero.

The entire original scheduler remains byte-pinned. Only its three sums of
already complete vectors use a shape-preserving exact-zero branch. The
original cell evaluator, saved binary64 endpoints and fixed slices remain.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_true_root_parallel_cell_slices.py"
BASE_BYTES = 19803
BASE_SHA256 = "f9a35f1972e961027af7488747c1cb035d3fb7d531e9690637ccb984c70441b0"

VECTOR_SUM = '''def _whole96_add_upper(c, *values):
    require(values, "a nonempty complete-vector sum")
    checked = [c.upper(value) for value in values]
    require(all(value.hi.shape == (ROWS,) for value in checked),
            "every summand has all96 directed coordinates")
    if not any(c.np.any(value.hi) for value in checked):
        # Each input is the exact nonnegative upper zero vector. Its sum is
        # exactly zero in all96 coordinates, not a scalar broadcast promise.
        return c.Box(c.np.zeros(ROWS, dtype=c.np.float64))
    result = c.add_upper(*checked)
    require(result.hi.shape == (ROWS,), "the original nonzero upper sum retains96 coordinates")
    return result


'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the entire actual failed scheduler must remain unchanged")
    source = raw.decode()
    insertion = "def whole_sums(c, seed, slices):\n"
    if source.count(insertion) != 1:
        raise ValueError("one complete original saved-vector sum boundary")
    source = source.replace(insertion, VECTOR_SUM+insertion)
    replacements = (
        ("c.add_upper(union[name], value[name])", "_whole96_add_upper(c, union[name], value[name])"),
        ("c.add_upper(contiguous[name], value[name])", "_whole96_add_upper(c, contiguous[name], value[name])"),
        ("c.add_upper(sums[name], value)", "_whole96_add_upper(c, sums[name], value)"),
    )
    for old, new in replacements:
        if source.count(old) != 1:
            raise ValueError("the explicit whole-vector adaptation did not match: "+old)
        source = source.replace(old, new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
