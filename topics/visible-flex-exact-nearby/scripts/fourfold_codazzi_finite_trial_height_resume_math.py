"""The unchanged H96 contraction on its missing suffix and all 96 old signed balls."""
import ast
import hashlib
from fractions import Fraction
from pathlib import Path

ORIGINAL_SHA = "c18d273a44a3f066a707791daf135163c7ae68d0309c78ec00a50a972f7bf0aa"
START = 728
END = 2847
SEAM = Fraction(5854679515581645, 144115188075855872)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def initial_state(bundle):
    """Only compare old mesh coordinates, never evaluate an old radial contraction."""
    prefix = bundle["original_prefix"]
    plan, tc = bundle["rhi_plan"], bundle["tc_plan"]
    require(len(plan) == END and len(tc) == 7724 and
            Fraction(plan[START-1]["interval"][1]) == SEAM == Fraction(plan[START]["interval"][0])
            and prefix["complete_relative_cells"] == prefix["complete_intersections"] == START
            and prefix["exact_interval"] == ["0", str(SEAM)], "exact original chronological seam")
    # Determine the TC pointer from metadata, without building any old Hermite coefficients.
    index = next(i for i, cell in enumerate(tc) if Fraction(cell["interval"][1]) > SEAM)
    require(tc[index]["side"] == "negative" and Fraction(tc[index]["interval"][0]) <= SEAM,
            "the first old trial interval on the right of the paid seam")
    arb = bundle["flint"].arb
    prior = [arb(text) for text in prefix["all96_signed_polynomial_integrals"]]
    error = arb(prefix["complete_uniform_adjoint_error_upper"])
    require(len(prior) == 96 and all(x.is_finite() for x in prior) and error.is_finite() and error >= 0,
            "all 96 complete outward Arb balls and the whole adjoint error, with no midpoint choice")
    return prior, error.upper(), index


def carried_vector(c, suffix, previous, vector_balls):
    added = vector_balls(c, suffix)
    require(len(added) == len(previous) == 96, "one single whole 96-column prefix")
    result = [old + new for old, new in zip(previous, added)]
    require(all(c.arb(x.str(60)).contains(x) for x in result), "each carried signed ball survives complete serialization")
    return result


def build_compute(raw):
    require(hashlib.sha256(raw).hexdigest() == ORIGINAL_SHA, "whole original H96 math source")
    tree = ast.parse(raw)
    original, = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "compute"]
    # Replace only the four initialization/iteration statements, then both complete-vector readouts.
    original_init = ast.parse("""
total, maximum_error = c.Box(np.zeros(96)), c.arb(0)
cursor, tc_cursor, intersections, last_trial = F(0), 0, 0, None
maximum_degree, maximum_radial_degree = 0, 0
""").body
    new_init = ast.parse("""
previous, maximum_error, tc_cursor = initial_state(bundle)
total = c.Box(np.zeros(96))
cursor, intersections, last_trial = SEAM, START, None
maximum_degree = bundle["original_prefix"]["maximum_complete_angular_degree"]
maximum_radial_degree = bundle["original_prefix"]["maximum_complete_radial_degree"]
""").body
    dump = ast.dump
    indices = [i for i in range(len(original.body)-2)
               if list(map(dump, original.body[i:i+3])) == list(map(dump, original_init))]
    require(len(indices) == 1, "one exact original zero-prefix initialization")
    i = indices[0]
    loop = original.body[i+3]
    require(isinstance(loop, ast.For) and dump(loop.target) == dump(ast.parse("for index,item in []: pass").body[0].target)
            and dump(loop.iter) == dump(ast.parse("enumerate(plan)", mode="eval").body),
            "one exact original chronological RHI sweep")
    loop.iter = ast.parse("enumerate(plan[START:], start=START)", mode="eval").body
    original.body[i:i+3] = new_init
    call = ast.parse("vector_balls(c,total)", mode="eval").body
    count = 0
    class Carry(ast.NodeTransformer):
        def visit_Call(self, node):
            nonlocal count
            if dump(node) == dump(call):
                count += 1
                return ast.copy_location(ast.parse("carried_vector(c,total,previous,vector_balls)", mode="eval").body, node)
            return self.generic_visit(node)
    original = Carry().visit(original)
    require(count == 2, "old signed balls enter each saved checkpoint and the final canonical height")
    return ast.fix_missing_locations(ast.Module(body=[original], type_ignores=[]))


def compute(original, bundle, publish, save_prefix, progress):
    raw = Path(original.__file__).read_bytes()
    namespace = {**vars(original), "START":START, "SEAM":SEAM, "initial_state":initial_state,
                 "carried_vector":carried_vector}
    exec(compile(build_compute(raw), "<H96 whole original contraction on [728,2847)>", "exec"), namespace)
    return namespace["compute"](bundle, publish, save_prefix, progress)
