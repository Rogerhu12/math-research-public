#!/usr/bin/env python3
"""R827 prime-field adapter for the frozen streamed polynomial-module engine.

No old L-valued stage is relabelled.  Only the generic column-operation code is
imported; every new stage has the R827 mathematical configuration and explicitly
records the original residue field.  Mathematical use belongs to public Actions.
"""
import hashlib
import io
from pathlib import Path
import tarfile

from flint import nmod_poly
import R811_exact_L_polynomial_modules as generic

GENERIC_SHA = "09f21a903e4906666d63f58575b389be7a04c20b68c7fcac624d3821837a9126"
RENAMES = {
    "unit_determinant_verified_over_original_L":
        "unit_determinant_verified_over_original_residue_field",
    "nonzero_original_L_unit_verified":
        "nonzero_original_residue_field_unit_verified",
    "all_column_operations_unimodular_over_original_L_polynomial_ring":
        "all_column_operations_unimodular_over_original_residue_polynomial_ring",
}


def semantic_copy(value):
    if isinstance(value, dict):
        return {RENAMES.get(key, key): semantic_copy(item) for key, item in value.items()}
    if isinstance(value, list):
        return [semantic_copy(item) for item in value]
    if isinstance(value, tuple):
        return [semantic_copy(item) for item in value]
    return value


class Scalar:
    __slots__ = ("F", "v")

    def __init__(self, field, value):
        if isinstance(value, Scalar):
            assert value.F is field
            value = value.v
        self.F, self.v = field, int(value) % field.p

    def __bool__(self):
        return bool(self.v)

    def __int__(self):
        return self.v

    def __eq__(self, value):
        return self.v == self.F.elt(value).v

    def __neg__(self):
        return Scalar(self.F, -self.v)

    def __add__(self, value):
        return Scalar(self.F, self.v+self.F.elt(value).v)

    __radd__ = __add__

    def __sub__(self, value):
        return Scalar(self.F, self.v-self.F.elt(value).v)

    def __rsub__(self, value):
        return self.F.elt(value)-self

    def __mul__(self, value):
        return Scalar(self.F, self.v*self.F.elt(value).v)

    __rmul__ = __mul__

    def inverse(self):
        assert self.v
        return Scalar(self.F, pow(self.v, -1, self.F.p))

    def encode(self):
        return self.v


class PrimeField:
    def __init__(self, prime):
        self.p = int(prime)
        assert 3 < self.p < 2**31
        self.zero, self.one = Scalar(self, 0), Scalar(self, 1)

    def elt(self, value):
        if isinstance(value, Scalar):
            assert value.F is self
            return value
        return Scalar(self, value)

    def decode(self, value):
        assert type(value) is int and 0 <= value < self.p
        return self.elt(value)


class Polynomial:
    __slots__ = ("A", "p")

    def __init__(self, algebra, value=0):
        self.A = algebra
        if isinstance(value, Polynomial):
            assert value.A is algebra
            self.p = value.p
        elif isinstance(value, nmod_poly):
            self.p = nmod_poly([int(x) for x in value.coeffs()], algebra.F.p)
        elif isinstance(value, (tuple, list)):
            self.p = nmod_poly([int(algebra.F.elt(x)) for x in value], algebra.F.p)
        else:
            self.p = nmod_poly([int(algebra.F.elt(value))], algebra.F.p)

    def __bool__(self):
        return self.p.degree() >= 0

    def __len__(self):
        return self.p.degree()+1

    @property
    def c(self):
        return tuple(self.A.F.elt(int(x)) for x in self.p.coeffs())

    def degree(self):
        return self.p.degree()

    def order(self):
        assert self
        return next(i for i in range(len(self)) if self.p[i])

    def leading(self):
        assert self
        return self.A.F.elt(int(self.p[self.p.degree()]))

    def __eq__(self, value):
        return self.p == self.A.poly(value).p

    def __neg__(self):
        return Polynomial(self.A, -self.p)

    def __add__(self, value):
        return Polynomial(self.A, self.p+self.A.poly(value).p)

    __radd__ = __add__

    def __sub__(self, value):
        return Polynomial(self.A, self.p-self.A.poly(value).p)

    def __rsub__(self, value):
        return self.A.poly(value)-self

    def __mul__(self, value):
        value = self.A.poly(value)
        self.A.tick()
        return Polynomial(self.A, self.p*value.p)

    __rmul__ = __mul__

    def scale(self, scalar):
        return Polynomial(self.A, self.p*int(self.A.F.elt(scalar)))

    def shift(self, amount):
        assert isinstance(amount, int) and amount >= 0
        return Polynomial(self.A, [0]*amount+self.encode()) if self else self.A.zero

    def divmod(self, divisor):
        divisor = self.A.poly(divisor)
        assert divisor
        self.A.tick()
        quotient, remainder = divmod(self.p, divisor.p)
        return Polynomial(self.A, quotient), Polynomial(self.A, remainder)

    def exact_div(self, divisor):
        quotient, remainder = self.divmod(divisor)
        assert not remainder, "Exact polynomial division in the original residue field"
        return quotient

    def encode(self):
        return [int(x) for x in self.p.coeffs()]


class Algebra:
    def __init__(self, prime, tick=lambda: None):
        self.F, self.tick = PrimeField(prime), tick
        self.zero, self.one = Polynomial(self, 0), Polynomial(self, 1)
        self.variable = Polynomial(self, [0, 1])

    def poly(self, value=0):
        return value if isinstance(value, Polynomial) and value.A is self else Polynomial(self, value)

    def decode(self, value):
        assert isinstance(value, list)
        assert all(type(x) is int and 0 <= x < self.F.p for x in value)
        assert not value or value[-1]
        answer = self.poly(value)
        assert answer.encode() == value
        return answer

    def xgcd(self, a, b):
        a, b = self.poly(a), self.poly(b)
        assert a or b
        self.tick()
        d, s, t = a.p.xgcd(b.p)
        d, s, t = (Polynomial(self, value) for value in (d, s, t))
        inverse = d.leading().inverse()
        d, s, t = d.scale(inverse), s.scale(inverse), t.scale(inverse)
        assert d.leading() == self.F.one
        assert s*a+t*b == d
        a1, b1 = a.exact_div(d), b.exact_div(d)
        assert s*a1+t*b1 == self.one
        return d, s, t, a1, b1


class Store(generic.StageStore):
    def put(self, name, payload, complete=True, replace=False):
        return super().put(name, semantic_copy(payload), complete, replace)


class Matrix(generic.VectorMatrix):
    def verify_history(self):
        initial = self.S.load(self.state["initialization"])
        vectors = list(initial["vectors"])
        previous = None
        for number in range(self.state["operation_count"]):
            self.S.budget()
            plan_spec = self.S.spec(self.plan_name(number))
            receipt_spec = self.S.spec(self.receipt_name(number))
            plan, receipt = self.S.load(plan_spec), self.S.load(receipt_spec)
            assert plan["operation_number"] == receipt["operation_number"] == number
            assert plan["matrix_label"] == receipt["matrix_label"] == self.label
            assert receipt["operation_plan"] == plan_spec
            assert receipt["previous_operation_receipt"] == plan["previous_operation_receipt"] == previous
            assert receipt["before_vectors"] == plan["before_vectors"] == \
                   [vectors[i] for i in plan["indices"]]
            assert receipt["indices"] == plan["indices"]
            assert receipt["after_control"] == plan["after_control"]
            assert receipt["unit_determinant_verified_over_original_residue_field"] is True
            assert plan["unit_determinant_verified_over_original_residue_field"] is True
            for i, entry in zip(plan["indices"], receipt["after_vectors"]):
                vectors[i] = entry
            previous = receipt_spec
        assert vectors == self.state["vectors"] and previous == self.state["last_operation_receipt"]
        return {
            "operation_count": self.state["operation_count"],
            "initialization": self.state["initialization"],
            "last_operation_receipt": previous,
            "complete_unimodular_transcript_metadata_chain_verified": True,
            "all_operation_plans_and_receipts_retained": True,
            "superseded_large_intermediate_vectors_retained": False,
            "coefficient_ring": "the pinned original residue field, not characteristic-zero L",
        }


def reduce_columns(matrix, pivot_rows):
    assert generic.sha(generic.__file__) == GENERIC_SHA
    assert isinstance(matrix, Matrix) and isinstance(matrix.A, Algebra)
    return generic.reduce_columns(matrix, pivot_rows, canonical=True)


def archive_history(matrix, chunk_size=128):
    """Archive complete immutable history bytes; final basis columns remain live."""
    assert matrix.finished and chunk_size == 128
    root, entries = matrix.S.root, []
    total = matrix.state["operation_count"]
    for first in range(0, total, chunk_size):
        matrix.S.budget()
        stop = min(first+chunk_size, total)
        label = matrix.label+"-history-"+str(first).zfill(10)
        index_name, archive_name = label+"-index", label+".tar"
        if matrix.S.exists(index_name):
            index = matrix.S.load(index_name)
            assert index["first_operation"] == first and index["stop_operation"] == stop
            assert index["completed_Hermite_index"] == matrix.S.spec(matrix.final_name)
            assert generic.file_spec(root/archive_name) == index["archive"]
            # Idempotent after an interruption between the index and deletions.
            for row in index["members"]:
                path = root/row["file"]
                if path.exists():
                    assert generic.file_spec(path) == row
                    path.unlink()
            entries.append(matrix.S.spec(index_name))
            continue
        names = []
        for number in range(first, stop):
            names.extend((matrix.plan_name(number), matrix.receipt_name(number)))
        members = [matrix.S.spec(name) for name in names]
        target, temporary = root/archive_name, root/(archive_name+".tmp")
        if not target.exists():
            with tarfile.open(temporary, "w") as archive:
                for row in members:
                    path = root/row["file"]
                    raw = path.read_bytes()
                    assert len(raw) == row["bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"]
                    info = tarfile.TarInfo(row["file"])
                    info.size, info.mtime, info.mode = len(raw), 0, 0o644
                    archive.addfile(info, io.BytesIO(raw))
            temporary.replace(target)
        with tarfile.open(target, "r:") as archive:
            actual = archive.getmembers()
            assert [row.name for row in actual] == [row["file"] for row in members]
            for member, row in zip(actual, members):
                assert member.isfile() and member.size == row["bytes"]
                stream = archive.extractfile(member)
                digest = hashlib.sha256()
                size = 0
                while True:
                    raw = stream.read(1024*1024)
                    if not raw:
                        break
                    digest.update(raw)
                    size += len(raw)
                assert size == row["bytes"] and digest.hexdigest() == row["sha256"]
        entry = matrix.S.put(index_name, {
            "first_operation": first, "stop_operation": stop,
            "completed_Hermite_index": matrix.S.spec(matrix.final_name),
            "archive": generic.file_spec(target), "members": members,
            "original_completed_plan_and_receipt_bytes_preserved": True,
            "not_a_new_mathematical_reduction": True,
        })
        for row in members:
            path = root/row["file"]
            assert generic.file_spec(path) == row
            path.unlink()
        entries.append(entry)
    return entries


def all_final_entries(matrix):
    assert matrix.finished
    for column, entry in enumerate(matrix.state["vectors"]):
        data, _ = matrix.block(entry, 0)
        assert len(data) == matrix.length
        yield column, data
