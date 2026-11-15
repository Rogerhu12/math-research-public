#!/usr/bin/env python3
"""Exact L[z] arithmetic and streamed unimodular modules for R811.

This module is only imported by the public-Actions mathematical consumer.
L is the original degree-seven b field with the frozen R754 zeta adapter.
It does not select embeddings, change b, or construct a numerical field.
"""
import gzip
import hashlib
import json
from pathlib import Path
import time

from flint import fmpq, fmpq_poly


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(specification):
    return {key: specification[key] for key in ("file", "bytes", "sha256")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as source:
        return json.load(source)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as target:
            with gzip.GzipFile(filename="", fileobj=target, mode="wb", mtime=0, compresslevel=2) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


class Algebra:
    """The original L, followed by an independent polynomial variable."""
    def __init__(self, field, tick=lambda: None):
        assert field.degree == 7
        self.F, self.tick = field, tick
        self.stride = 2*field.degree-1
        assert self.stride == 13
        self.zero = Poly(self, ())
        self.one = Poly(self, (field.one,))
        self.variable = Poly(self, (field.zero, field.one))

    def poly(self, value=0):
        if isinstance(value, Poly):
            assert value.A is self
            return value
        if isinstance(value, (list, tuple)):
            return Poly(self, tuple(self.F.elt(x) for x in value))
        return Poly(self, (self.F.elt(value),))

    def decode(self, encoded):
        assert isinstance(encoded, list)
        result = Poly(self, tuple(self.F.decode(x) for x in encoded))
        assert result.encode() == encoded, "Noncanonical original-field polynomial"
        return result

    def field_from_b_s(self, coordinates):
        assert len(coordinates) == 14
        a = fmpq_poly(coordinates[:7])
        c = fmpq_poly(coordinates[7:])
        # s=1+2*zeta: a+s*c=(a+c)+zeta*(2*c).
        return self.F.elt(a+c, 2*c)

    def xgcd(self, a, b):
        a, b = self.poly(a), self.poly(b)
        assert a or b
        old_r, r = a, b
        old_s, s = self.one, self.zero
        old_t, t = self.zero, self.one
        while r:
            self.tick()
            quotient, remainder = old_r.divmod(r)
            old_r, r = r, remainder
            old_s, s = s, old_s-quotient*s
            old_t, t = t, old_t-quotient*t
        unit = old_r.leading().inverse()
        d, s, t = old_r.scale(unit), old_s.scale(unit), old_t.scale(unit)
        assert d.leading() == self.F.one
        assert s*a+t*b == d, "Actual polynomial Bezout identity"
        a1, b1 = a.exact_div(d), b.exact_div(d)
        assert s*a1+t*b1 == self.one, "Actual determinant-one Bezout operator"
        return d, s, t, a1, b1


class Poly:
    """Immutable canonical dense L[z] polynomial; coefficient zero is exact."""
    __slots__ = ("A", "c", "_packed")

    def __init__(self, algebra, coefficients):
        data = list(coefficients)
        assert all(x.F is algebra.F for x in data)
        while data and not data[-1]:
            data.pop()
        self.A, self.c, self._packed = algebra, tuple(data), None

    def __bool__(self):
        return bool(self.c)

    def __len__(self):
        return len(self.c)

    def degree(self):
        return len(self.c)-1

    def order(self):
        assert self
        return next(i for i, x in enumerate(self.c) if x)

    def leading(self):
        assert self
        return self.c[-1]

    def __eq__(self, other):
        other = self.A.poly(other)
        return self.c == other.c

    def __neg__(self):
        return Poly(self.A, tuple(-x for x in self.c))

    def __add__(self, other):
        other = self.A.poly(other)
        result = [self.A.F.zero]*max(len(self), len(other))
        for i, x in enumerate(self.c):
            result[i] = x
        for i, x in enumerate(other.c):
            result[i] = result[i]+x
        return Poly(self.A, result)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-self.A.poly(other))

    def __rsub__(self, other):
        return self.A.poly(other)-self

    def scale(self, scalar):
        scalar = self.A.F.elt(scalar)
        if not scalar or not self:
            return self.A.zero
        if scalar == self.A.F.one:
            return self
        return Poly(self.A, tuple(x*scalar for x in self.c))

    def shift(self, amount):
        assert isinstance(amount, int) and amount >= 0
        if not self:
            return self
        return Poly(self.A, (self.A.F.zero,)*amount+self.c)

    def packed(self):
        if self._packed is None:
            a, b = [], []
            for coefficient in self.c:
                for j in range(self.A.stride):
                    a.append(coefficient.a[j] if j < 7 else fmpq(0))
                    b.append(coefficient.b[j] if j < 7 else fmpq(0))
            self._packed = fmpq_poly(a), fmpq_poly(b)
        return self._packed

    def __mul__(self, other):
        other = self.A.poly(other)
        if not self or not other:
            return self.A.zero
        if len(self) == 1:
            return other.scale(self.c[0])
        if len(other) == 1:
            return self.scale(other.c[0])
        self.A.tick()
        a, b = self.packed()
        c, d = other.packed()
        ac, bd = a*c, b*d
        first = ac-bd
        second = (a+b)*(c+d)-ac-2*bd
        count = len(self)+len(other)-1
        # Each b-polynomial factor has degree <=6. Thus products have
        # degree <=12 and stride13 cannot spill into the next z coefficient.
        assert first.degree() < self.A.stride*count
        assert second.degree() < self.A.stride*count
        coefficients = []
        for k in range(count):
            self.A.tick()
            offset = k*self.A.stride
            aa = fmpq_poly([first[offset+j] for j in range(self.A.stride)])
            bb = fmpq_poly([second[offset+j] for j in range(self.A.stride)])
            coefficients.append(self.A.F.elt(aa, bb))
        return Poly(self.A, coefficients)

    __rmul__ = __mul__

    def divmod(self, divisor):
        divisor = self.A.poly(divisor)
        assert divisor
        if not self or self.degree() < divisor.degree():
            return self.A.zero, self
        if len(divisor) == 1:
            return self.scale(divisor.c[0].inverse()), self.A.zero
        remainder = list(self.c)
        quotient = [self.A.F.zero]*(len(self)-len(divisor)+1)
        inverse_leading = divisor.leading().inverse()
        while remainder and len(remainder) >= len(divisor):
            self.A.tick()
            old_length = len(remainder)
            offset = len(remainder)-len(divisor)
            coefficient = remainder[-1]*inverse_leading
            quotient[offset] = quotient[offset]+coefficient
            for i, value in enumerate(divisor.c):
                if value:
                    remainder[offset+i] = remainder[offset+i]-coefficient*value
            while remainder and not remainder[-1]:
                remainder.pop()
            assert len(remainder) < old_length
        return Poly(self.A, quotient), Poly(self.A, remainder)

    def exact_div(self, divisor):
        quotient, remainder = self.divmod(divisor)
        assert not remainder, "Required L[z] division is not exact"
        return quotient

    def encode(self):
        return [value.encode() for value in self.c]


class Laurent:
    """L[z,z^-1], with the exact power of z kept outside a nonvanishing-at-zero polynomial."""
    __slots__ = ("A", "shift", "p")

    def __init__(self, algebra, shift=0, polynomial=0):
        polynomial = algebra.poly(polynomial)
        if polynomial:
            removed = polynomial.order()
            self.shift = int(shift)+removed
            self.p = Poly(algebra, polynomial.c[removed:])
        else:
            self.shift, self.p = 0, algebra.zero
        self.A = algebra

    def __bool__(self):
        return bool(self.p)

    def __eq__(self, other):
        if isinstance(other, (int, Poly)):
            other = Laurent(self.A, 0, other)
        assert isinstance(other, Laurent) and other.A is self.A
        return self.shift == other.shift and self.p == other.p

    def __neg__(self):
        return Laurent(self.A, self.shift, -self.p)

    def __add__(self, other):
        if isinstance(other, (int, Poly)):
            other = Laurent(self.A, 0, other)
        assert other.A is self.A
        if not self:
            return other
        if not other:
            return self
        offset = min(self.shift, other.shift)
        return Laurent(self.A, offset,
            self.p.shift(self.shift-offset)+other.p.shift(other.shift-offset))

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, Poly)):
            other = Laurent(self.A, 0, other)
        return self+(-other)

    def __mul__(self, other):
        if isinstance(other, (int, Poly)):
            other = Laurent(self.A, 0, other)
        assert other.A is self.A
        return Laurent(self.A, self.shift+other.shift, self.p*other.p)

    __rmul__ = __mul__

    def divide_polynomial(self, divisor):
        divisor = self.A.poly(divisor)
        assert divisor
        if not self:
            return self
        removed = divisor.order()
        unit_at_zero = Poly(self.A, divisor.c[removed:])
        quotient, remainder = self.p.divmod(unit_at_zero)
        assert not remainder, "Containment coefficient has a nonmonomial denominator"
        answer = Laurent(self.A, self.shift-removed, quotient)
        assert answer*divisor == self, "Exact Laurent containment multiply-back"
        return answer

    def encode(self):
        return {"power": self.shift, "polynomial": self.p.encode()}

    @classmethod
    def decode(cls, algebra, encoded):
        result = cls(algebra, encoded["power"], algebra.decode(encoded["polynomial"]))
        assert result.encode() == encoded
        return result


class StageStore:
    """Complete immutable small stages plus explicitly mutable current checkpoints."""
    def __init__(self, directory, configuration, budget):
        self.root, self.tag, self.budget = Path(directory), configuration, budget
        self.root.mkdir(parents=True, exist_ok=True)

    def path(self, name):
        assert Path(name).name == name
        if not name.endswith(".json.gz"):
            name += ".json.gz"
        return self.root/name

    def exists(self, name):
        return self.path(name).is_file()

    def load(self, value, complete=True):
        path = self.path(value["file"] if isinstance(value, dict) else value)
        if isinstance(value, dict):
            assert file_spec(path) == plain(value)
        data = read(path)
        assert data["configuration"] == self.tag
        assert data["complete"] is complete
        return data

    def put(self, name, payload, complete=True, replace=False):
        path = self.path(name)
        value = dict(payload, complete=complete, configuration=self.tag)
        if path.exists() and not replace:
            assert read(path) == value, ("Existing source-bound stage differs", path.name)
        else:
            save(path, value)
        return file_spec(path)

    def remove_if_owned(self, name, prefix):
        path = self.path(name)
        assert path.name.startswith(prefix+"-")
        path.unlink(missing_ok=True)

    def spec(self, name):
        return file_spec(self.path(name))


class VectorMatrix:
    """A matrix stored as independently tiled columns or rows.

    Only the current version of a changed work vector is retained. Complete
    plans and small receipts retain the superseded versions' sizes and hashes.
    A plan's output tiles are atomically committed together by the current
    checkpoint, so a hard interruption never changes half of a two-vector
    operation. Source vectors with another matrix label are never deleted.
    """
    def __init__(self, store, algebra, label, vector_count, vector_length,
                 orientation="columns", tile_size=16):
        assert orientation in ("columns", "rows")
        assert vector_count >= 1 and vector_length >= 1 and tile_size >= 1
        self.S, self.A, self.label = store, algebra, label
        self.count, self.length = int(vector_count), int(vector_length)
        self.orientation, self.tile_size = orientation, int(tile_size)
        self.current_name = label+"-current"
        self.initial_name = label+"-initialization"
        self.final_name = label+"-final-index"
        self._indices = {}
        self.finished = self.S.exists(self.final_name)
        if self.finished:
            self.state = self.S.load(self.final_name)
        elif self.S.exists(self.current_name):
            self.state = self.S.load(self.current_name, complete=False)
            self.cleanup_latest()
        else:
            self.state = None
        if self.state is not None:
            self.check_shape(self.state)

    def check_shape(self, value):
        assert value["matrix_label"] == self.label
        assert value["vector_count"] == self.count and value["vector_length"] == self.length
        assert value["orientation"] == self.orientation and value["tile_size"] == self.tile_size
        assert len(value["vectors"]) == self.count

    def shape(self):
        return {"matrix_label": self.label, "vector_count": self.count,
                "vector_length": self.length, "orientation": self.orientation,
                "tile_size": self.tile_size}

    def index_name(self, vector, version):
        return self.label+"-v-"+str(vector).zfill(4)+"-"+version+"-index"

    def tile_name(self, vector, version, first):
        return self.label+"-v-"+str(vector).zfill(4)+"-"+version+"-r-"+str(first).zfill(5)

    def ranges(self):
        return [(first, min(first+self.tile_size, self.length))
                for first in range(0, self.length, self.tile_size)]

    def vector(self, specification, expected_index=None):
        key = specification["sha256"]
        if key not in self._indices:
            value = self.S.load(specification)
            assert value["kind"] == "exact_polynomial_vector"
            assert value["length"] == self.length and value["orientation"] == self.orientation
            assert value["tile_size"] == self.tile_size
            assert len(value["tiles"]) == len(self.ranges())
            for tile, (first, stop) in zip(value["tiles"], self.ranges()):
                assert (tile["first"], tile["stop"]) == (first, stop)
            if len(self._indices) >= 1024:
                self._indices.clear()
            self._indices[key] = value
        value = self._indices[key]
        if expected_index is not None:
            assert value["vector_index"] == expected_index
        return value

    def block(self, vector_spec, first, decode=True):
        assert first % self.tile_size == 0
        index = self.vector(vector_spec)
        entry = index["tiles"][first//self.tile_size]
        value = self.S.load(entry)
        assert value["kind"] == "exact_polynomial_vector_tile"
        assert value["matrix_label"] == index["matrix_label"]
        assert value["vector_index"] == index["vector_index"]
        assert (value["first"], value["stop"]) == (entry["first"], entry["stop"])
        assert len(value["coefficients"]) == entry["stop"]-entry["first"]
        coefficients = value["coefficients"]
        return ([self.A.decode(x) for x in coefficients] if decode else coefficients), entry

    def entry(self, vector_spec, position):
        assert 0 <= position < self.length
        first = position//self.tile_size*self.tile_size
        block, _ = self.block(vector_spec, first, decode=False)
        return self.A.decode(block[position-first])

    def initial_tile_exists(self, vector, first):
        return self.S.exists(self.tile_name(vector, "initial", first))

    def put_initial_tile(self, vector, first, coefficients, source):
        assert 0 <= vector < self.count and first % self.tile_size == 0
        stop = min(first+self.tile_size, self.length)
        assert len(coefficients) == stop-first
        encoded = [x.encode() if isinstance(x, Poly) else x for x in coefficients]
        return self.S.put(self.tile_name(vector, "initial", first), {
            "kind": "exact_polynomial_vector_tile", "matrix_label": self.label,
            "vector_index": vector, "orientation": self.orientation,
            "first": first, "stop": stop, "coefficients": encoded,
            "source": source, "original_field_adapter_preserved": True})

    def initial_vector(self, vector):
        name = self.index_name(vector, "initial")
        if self.S.exists(name):
            entry = self.S.spec(name)
            self.vector(entry, vector)
            return entry
        tiles = []
        for first, stop in self.ranges():
            entry = self.S.spec(self.tile_name(vector, "initial", first))
            value = self.S.load(entry)
            assert value["matrix_label"] == self.label and value["vector_index"] == vector
            assert (value["first"], value["stop"]) == (first, stop)
            assert len(value["coefficients"]) == stop-first
            tiles.append(dict(entry, first=first, stop=stop))
        return self.S.put(name, {
            "kind": "exact_polynomial_vector", "matrix_label": self.label,
            "vector_index": vector, "orientation": self.orientation,
            "length": self.length, "tile_size": self.tile_size, "tiles": tiles})

    def initialize(self, vector_specs, control, source):
        assert len(vector_specs) == self.count
        if self.state is not None:
            initial = self.S.load(self.state["initialization"])
            assert initial["source"] == source
            return
        for i, entry in enumerate(vector_specs):
            self.vector(entry, i)
        initial_spec = self.S.put(self.initial_name, dict(self.shape(),
            kind="matrix_initialization", vectors=vector_specs, control=control, source=source))
        payload = dict(self.shape(), kind="polynomial_matrix_checkpoint",
            vectors=vector_specs, control=control, operation_count=0,
            initialization=initial_spec, last_operation_receipt=None,
            only_latest_large_work_vectors_retained=True)
        self.S.put(self.current_name, payload, complete=False)
        self.state = self.S.load(self.current_name, complete=False)

    def update_control(self, control):
        assert self.state is not None and not self.finished
        payload = {k: v for k, v in self.state.items() if k not in ("complete", "configuration")}
        payload["control"] = control
        self.S.put(self.current_name, payload, complete=False, replace=True)
        self.state = self.S.load(self.current_name, complete=False)

    def plan_name(self, number):
        return self.label+"-op-"+str(number).zfill(10)+"-plan"

    def receipt_name(self, number):
        return self.label+"-op-"+str(number).zfill(10)+"-receipt"

    def pending(self):
        assert self.state is not None and not self.finished
        number = self.state["operation_count"]
        if not self.S.exists(self.plan_name(number)):
            return None
        specification = self.S.spec(self.plan_name(number))
        value = self.S.load(specification)
        assert value["operation_number"] == number and value["matrix_label"] == self.label
        assert value["before_control"] == self.state["control"]
        assert value["before_vectors"] == [self.state["vectors"][i] for i in value["indices"]]
        assert value["previous_operation_receipt"] == self.state["last_operation_receipt"]
        return value, specification

    def plan(self, indices, operator, side, kind, next_control, witness=None):
        """operator is the actual elementary E, not its transpose or inverse."""
        assert side in ("right_columns", "left_rows")
        assert side == ("right_columns" if self.orientation == "columns" else "left_rows")
        assert len(indices) in (1, 2) and len(indices) == len(set(indices))
        assert all(0 <= i < self.count for i in indices)
        assert len(operator) == len(indices) and all(len(row) == len(indices) for row in operator)
        operator = [[self.A.poly(x) for x in row] for row in operator]
        determinant = operator[0][0] if len(indices) == 1 else \
            operator[0][0]*operator[1][1]-operator[0][1]*operator[1][0]
        assert determinant and determinant.degree() == 0, "Every column operator must be unimodular"
        number = self.state["operation_count"]
        value = {
            "kind": "unimodular_operation_plan", "matrix_label": self.label,
            "operation_number": number, "operation_kind": kind, "indices": list(indices),
            "operator_side": side, "elementary_matrix": [[x.encode() for x in row] for row in operator],
            "actual_unit_determinant": determinant.encode(),
            "unit_determinant_verified_over_original_L": True,
            "before_vectors": [self.state["vectors"][i] for i in indices],
            "before_control": self.state["control"], "after_control": next_control,
            "previous_operation_receipt": self.state["last_operation_receipt"],
            "mathematical_witness": witness or {},
            "plan_complete_but_not_an_applied_matrix_checkpoint": True,
        }
        entry = self.S.put(self.plan_name(number), value)
        return self.S.load(entry), entry

    def apply(self, plan, plan_spec):
        assert not self.finished and self.state is not None
        number = self.state["operation_count"]
        assert plan["operation_number"] == number and plan["matrix_label"] == self.label
        assert plan["before_control"] == self.state["control"]
        indices = plan["indices"]
        assert plan["before_vectors"] == [self.state["vectors"][i] for i in indices]
        side = plan["operator_side"]
        operator = [[self.A.decode(x) for x in row] for row in plan["elementary_matrix"]]
        assert len(operator) == len(indices)
        determinant = operator[0][0] if len(indices) == 1 else \
            operator[0][0]*operator[1][1]-operator[0][1]*operator[1][0]
        assert determinant.encode() == plan["actual_unit_determinant"]
        assert determinant and determinant.degree() == 0
        unchanged = []
        for k in range(len(indices)):
            factors = [operator[j][k] if side == "right_columns" else operator[k][j]
                       for j in range(len(indices))]
            unchanged.append(all(factor == int(j == k) for j, factor in enumerate(factors)))
        version = "op-"+str(number).zfill(10)
        new_tiles = [[] for _ in indices]
        for first, stop in self.ranges():
            self.S.budget()
            expected = [self.tile_name(index, version, first) for index in indices]
            missing = [k for k, name in enumerate(expected)
                       if not unchanged[k] and not self.S.exists(name)]
            old_blocks, input_tiles = [], []
            if missing:
                for old in plan["before_vectors"]:
                    block, tile = self.block(old, first)
                    old_blocks.append(block)
                    input_tiles.append(plain(tile))
                for k in missing:
                    coefficients = []
                    for position in range(stop-first):
                        self.A.tick()
                        value = self.A.zero
                        for j in range(len(indices)):
                            factor = operator[j][k] if side == "right_columns" else operator[k][j]
                            if factor and old_blocks[j][position]:
                                value = value+factor*old_blocks[j][position]
                        coefficients.append(value)
                    self.S.put(expected[k], {
                        "kind": "exact_polynomial_vector_tile", "matrix_label": self.label,
                        "vector_index": indices[k], "orientation": self.orientation,
                        "first": first, "stop": stop, "coefficients": [x.encode() for x in coefficients],
                        "operation_plan": plan_spec, "input_vector_tiles": input_tiles,
                        "actual_elementary_operator_applied": True,
                        "original_field_adapter_preserved": True})
            for k, name in enumerate(expected):
                if unchanged[k]:
                    continue
                entry = self.S.spec(name)
                value = self.S.load(entry)
                assert value["operation_plan"] == plan_spec
                assert value["vector_index"] == indices[k]
                assert (value["first"], value["stop"]) == (first, stop)
                assert len(value["coefficients"]) == stop-first
                new_tiles[k].append(dict(entry, first=first, stop=stop))
        new_vectors = []
        for k, index in enumerate(indices):
            if unchanged[k]:
                new_vectors.append(plan["before_vectors"][k])
                continue
            value = {
                "kind": "exact_polynomial_vector", "matrix_label": self.label,
                "vector_index": index, "orientation": self.orientation,
                "length": self.length, "tile_size": self.tile_size,
                "tiles": new_tiles[k], "operation_plan": plan_spec}
            entry = self.S.put(self.index_name(index, version), value)
            new_vectors.append(entry)
        expected_pivot = plan["mathematical_witness"].get("expected_after_row")
        if expected_pivot is not None:
            row = plan["mathematical_witness"]["pivot_row"]
            assert len(expected_pivot) == len(new_vectors)
            for entry, expected in zip(new_vectors, expected_pivot):
                assert self.entry(entry, row).encode() == expected
        receipt_spec = self.S.put(self.receipt_name(number), {
            "kind": "completed_unimodular_operation", "matrix_label": self.label,
            "operation_number": number, "operation_plan": plan_spec,
            "before_vectors": plan["before_vectors"], "after_vectors": new_vectors,
            "indices": indices, "before_control": plan["before_control"],
            "after_control": plan["after_control"],
            "previous_operation_receipt": self.state["last_operation_receipt"],
            "all_affected_tiles_completed_before_checkpoint_commit": True,
            "actual_unit_determinant": plan["actual_unit_determinant"],
            "unit_determinant_verified_over_original_L": True,
            "superseded_large_work_vectors_may_be_pruned_after_atomic_commit": True})
        updated = {k: v for k, v in self.state.items() if k not in ("complete", "configuration")}
        updated["vectors"] = list(self.state["vectors"])
        for index, entry in zip(indices, new_vectors):
            updated["vectors"][index] = entry
        updated["operation_count"] = number+1
        updated["last_operation_receipt"] = receipt_spec
        updated["control"] = plan["after_control"]
        self.S.put(self.current_name, updated, complete=False, replace=True)
        self.state = self.S.load(self.current_name, complete=False)
        self.cleanup_latest()

    def cleanup_latest(self):
        receipt_spec = self.state.get("last_operation_receipt") if self.state else None
        if receipt_spec is None:
            return
        receipt = self.S.load(receipt_spec)
        active = {x["file"] for x in self.state["vectors"]}
        for old in receipt["before_vectors"]:
            # Borrowed immutable input vectors use another label and are kept.
            if not old["file"].startswith(self.label+"-v-") or old["file"] in active:
                continue
            path = self.S.path(old["file"])
            if not path.exists():
                continue
            value = self.S.load(old)
            assert value["matrix_label"] == self.label
            for tile in value["tiles"]:
                self.S.remove_if_owned(tile["file"], self.label)
            # Delete the index last. Its presence is the cleanup recovery record.
            self.S.remove_if_owned(old["file"], self.label)
            self._indices.pop(old["sha256"], None)

    def verify_history(self):
        initial = self.S.load(self.state["initialization"])
        vectors = list(initial["vectors"])
        previous = None
        for number in range(self.state["operation_count"]):
            plan_spec = self.S.spec(self.plan_name(number))
            plan = self.S.load(plan_spec)
            receipt_spec = self.S.spec(self.receipt_name(number))
            receipt = self.S.load(receipt_spec)
            assert plan["operation_number"] == receipt["operation_number"] == number
            assert plan["matrix_label"] == receipt["matrix_label"] == self.label
            assert receipt["operation_plan"] == plan_spec
            assert receipt["previous_operation_receipt"] == plan["previous_operation_receipt"] == previous
            assert receipt["before_vectors"] == plan["before_vectors"] == [vectors[i] for i in plan["indices"]]
            assert receipt["indices"] == plan["indices"]
            assert receipt["after_control"] == plan["after_control"]
            assert receipt["unit_determinant_verified_over_original_L"] is True
            for i, entry in zip(plan["indices"], receipt["after_vectors"]):
                vectors[i] = entry
            previous = receipt_spec
        assert vectors == self.state["vectors"] and previous == self.state["last_operation_receipt"]
        return {"operation_count": self.state["operation_count"],
                "initialization": self.state["initialization"], "last_operation_receipt": previous,
                "complete_unimodular_transcript_metadata_chain_verified": True,
                "all_operation_plans_and_receipts_retained": True,
                "superseded_large_intermediate_vectors_retained": False}

    def finish(self, additional):
        if self.finished:
            for key, value in additional.items():
                assert self.state[key] == value
            return self.S.spec(self.final_name)
        history = self.verify_history()
        for i, entry in enumerate(self.state["vectors"]):
            index = self.vector(entry, i)
            for tile in index["tiles"]:
                assert file_spec(self.S.path(tile["file"])) == plain(tile)
        payload = {k: v for k, v in self.state.items() if k not in ("complete", "configuration")}
        payload.update(kind="completed_polynomial_matrix", history=history, **additional)
        final = self.S.put(self.final_name, payload)
        self.S.path(self.current_name).unlink(missing_ok=True)
        self.state, self.finished = self.S.load(final), True
        return final


def reducer_control(pivot_rows, canonical):
    return {"phase": "find_pivot", "pivot_row": 0, "next_other_column": 0,
            "pivot_rows": int(pivot_rows), "canonical_remainders": bool(canonical)}


def reduce_columns(matrix, pivot_rows, canonical):
    """Unimodular column reduction; extra lower rows are transported unchanged as data."""
    assert matrix.orientation == "columns"
    assert 1 <= pivot_rows <= min(matrix.length, matrix.count)
    if matrix.finished:
        assert matrix.state["actual_pivot_rank"] == pivot_rows
        assert matrix.state["canonical_column_Hermite_remainders"] is bool(canonical)
        return matrix.S.spec(matrix.final_name)
    A = matrix.A
    while matrix.state["control"]["phase"] != "done":
        matrix.S.budget()
        pending = matrix.pending()
        if pending is not None:
            matrix.apply(*pending)
            continue
        control = matrix.state["control"]
        assert control["pivot_rows"] == pivot_rows
        assert control["canonical_remainders"] is bool(canonical)
        row, phase = control["pivot_row"], control["phase"]
        assert 0 <= row < pivot_rows
        if phase == "find_pivot":
            selected = None
            for j in range(row, matrix.count):
                matrix.S.budget()
                if matrix.entry(matrix.state["vectors"][j], row):
                    selected = j
                    break
            assert selected is not None, "Actual polynomial matrix failed its required full row rank"
            next_control = dict(control, phase="gcd_row", next_other_column=row+1)
            if selected == row:
                matrix.update_control(next_control)
            else:
                matrix.apply(*matrix.plan([row, selected], [[0, 1], [1, 0]],
                    "right_columns", "swap", next_control,
                    {"pivot_row": row, "actual_nonzero_pivot_column": selected}))
        elif phase == "gcd_row":
            other = control["next_other_column"]
            if other == matrix.count:
                matrix.update_control(dict(control, phase="normalize_pivot"))
                continue
            assert row < other < matrix.count
            a = matrix.entry(matrix.state["vectors"][row], row)
            b = matrix.entry(matrix.state["vectors"][other], row)
            assert a
            next_control = dict(control, next_other_column=other+1)
            if not b:
                matrix.update_control(next_control)
                continue
            d, s, t, a1, b1 = A.xgcd(a, b)
            operator = [[s, -b1], [t, a1]]
            witness = {"pivot_row": row, "actual_before_row": [a.encode(), b.encode()],
                "actual_monic_gcd": d.encode(), "quotients_by_gcd": [a1.encode(), b1.encode()],
                "Bezout_and_both_exact_divisions_verified": True,
                "expected_after_row": [d.encode(), A.zero.encode()]}
            matrix.apply(*matrix.plan([row, other], operator, "right_columns",
                                      "Bezout_pair", next_control, witness))
        elif phase == "normalize_pivot":
            pivot = matrix.entry(matrix.state["vectors"][row], row)
            assert pivot
            if canonical and row:
                next_control = dict(control, phase="reduce_earlier", next_other_column=0)
            else:
                next_control = dict(control, phase="advance_pivot")
            if pivot.leading() == A.F.one:
                matrix.update_control(next_control)
                continue
            scalar = pivot.leading().inverse()
            expected = pivot.scale(scalar)
            matrix.apply(*matrix.plan([row], [[A.poly(scalar)]], "right_columns",
                "nonzero_constant_scale", next_control,
                {"pivot_row": row, "expected_after_row": [expected.encode()],
                 "nonzero_original_L_unit_verified": True}))
        elif phase == "reduce_earlier":
            other = control["next_other_column"]
            if other == row:
                matrix.update_control(dict(control, phase="advance_pivot"))
                continue
            assert 0 <= other < row
            pivot = matrix.entry(matrix.state["vectors"][row], row)
            value = matrix.entry(matrix.state["vectors"][other], row)
            quotient, remainder = value.divmod(pivot)
            next_control = dict(control, next_other_column=other+1)
            if not quotient:
                matrix.update_control(next_control)
                continue
            matrix.apply(*matrix.plan([row, other], [[1, -quotient], [0, 1]],
                "right_columns", "Euclidean_shear", next_control,
                {"pivot_row": row, "actual_before_row": [pivot.encode(), value.encode()],
                 "Euclidean_quotient": quotient.encode(),
                 "expected_after_row": [pivot.encode(), remainder.encode()],
                 "actual_remainder_degree_strictly_below_pivot": True}))
        else:
            assert phase == "advance_pivot"
            if row+1 == pivot_rows:
                matrix.update_control(dict(control, phase="done", pivot_row=pivot_rows))
            else:
                matrix.update_control(dict(control, phase="find_pivot", pivot_row=row+1,
                                           next_other_column=row+1))
    diagonal, maximum_degree = [], -1
    for column, entry in enumerate(matrix.state["vectors"]):
        matrix.S.budget()
        for first, stop in matrix.ranges():
            block, _ = matrix.block(entry, first)
            for offset, value in enumerate(block):
                position = first+offset
                maximum_degree = max(maximum_degree, value.degree())
                if position < pivot_rows:
                    if column >= pivot_rows or position < column:
                        assert not value, "Final upper or kernel block is not zero"
                    elif position == column:
                        assert value and value.leading() == A.F.one
                        diagonal.append({"index": column, "polynomial": value.encode(),
                                         "degree": value.degree(), "order_at_zero": value.order()})
                    elif canonical:
                        pivot = matrix.entry(matrix.state["vectors"][position], position)
                        assert value.degree() < pivot.degree()
    assert [x["index"] for x in diagonal] == list(range(pivot_rows))
    return matrix.finish({
        "actual_pivot_rank": pivot_rows, "all_diagonal_entries_nonzero_and_monic": True,
        "actual_diagonal": diagonal, "actual_maximum_entry_degree": maximum_degree,
        "canonical_column_Hermite_remainders": bool(canonical),
        "all_columns_after_pivot_block_zero_in_pivot_rows": True,
        "all_column_operations_unimodular_over_original_L_polynomial_ring": True,
        "exact_original_column_module_preserved": True})


def reverse_kernel_replay(reduced, kernel_rows, pivot_rows):
    """Uker = E1(...(Em(0;I))) by reverse-time LEFT multiplication of each original E."""
    assert reduced.finished and reduced.orientation == "columns"
    assert reduced.state["actual_pivot_rank"] == pivot_rows
    assert kernel_rows.orientation == "rows"
    assert kernel_rows.count == reduced.count
    assert kernel_rows.length == reduced.count-pivot_rows
    source = reduced.S.spec(reduced.final_name)
    count = reduced.state["operation_count"]
    if kernel_rows.finished:
        assert kernel_rows.state["source_reduced_matrix"] == source
        assert kernel_rows.state["source_operation_count"] == count
        return kernel_rows.S.spec(kernel_rows.final_name)
    if kernel_rows.state is None:
        for vector in range(kernel_rows.count):
            for first, stop in kernel_rows.ranges():
                if kernel_rows.initial_tile_exists(vector, first):
                    continue
                values = [kernel_rows.A.zero]*(stop-first)
                if vector >= pivot_rows and first <= vector-pivot_rows < stop:
                    values[vector-pivot_rows-first] = kernel_rows.A.one
                kernel_rows.put_initial_tile(vector, first, values,
                    {"definition": "(0;I) before reverse-time original elementary matrices",
                     "source_reduced_matrix": source, "pivot_rows": pivot_rows})
        initial = [kernel_rows.initial_vector(i) for i in range(kernel_rows.count)]
        kernel_rows.initialize(initial, {
            "phase": "reverse_left_replay", "next_source_operation": count-1},
            {"source_reduced_matrix": source, "source_operation_count": count,
             "starting_matrix": "(0;I)", "source_pivot_rows": pivot_rows})
    while kernel_rows.state["control"]["next_source_operation"] >= 0:
        kernel_rows.S.budget()
        pending = kernel_rows.pending()
        if pending is not None:
            kernel_rows.apply(*pending)
            continue
        number = kernel_rows.state["control"]["next_source_operation"]
        original_spec = reduced.S.spec(reduced.plan_name(number))
        original = reduced.S.load(original_spec)
        assert original["operator_side"] == "right_columns"
        operator = [[kernel_rows.A.decode(x) for x in row]
                    for row in original["elementary_matrix"]]
        next_control = {"phase": "reverse_left_replay", "next_source_operation": number-1}
        witness = {"original_operation_plan": original_spec, "source_reduced_matrix": source,
            "original_operation_number": number,
            "original_matrix_used_not_inverse": True,
            "left_multiplication_in_reverse_time": True}
        kernel_rows.apply(*kernel_rows.plan(original["indices"], operator, "left_rows",
            "reverse_"+original["operation_kind"], next_control, witness))
    assert kernel_rows.state["operation_count"] == count
    return kernel_rows.finish({
        "source_reduced_matrix": source, "source_operation_count": count,
        "all_original_operators_left_multiplied_in_reverse_time": True,
        "operators_inverted_or_reordered": False,
        "complete_original_polynomial_kernel_basis_constructed": True})


def transpose_kernel_rows(rows_matrix, columns_matrix, pivot_rows):
    """Storage transpose only: no field arithmetic and no original producer recomputation."""
    assert rows_matrix.finished and rows_matrix.orientation == "rows"
    assert columns_matrix.orientation == "columns"
    assert columns_matrix.count == rows_matrix.length
    assert columns_matrix.length == rows_matrix.count
    assert columns_matrix.tile_size == rows_matrix.tile_size
    source = rows_matrix.S.spec(rows_matrix.final_name)
    if columns_matrix.state is not None:
        initial = columns_matrix.S.load(columns_matrix.state["initialization"])
        assert initial["source"] == {"source_kernel_row_matrix": source, "operation": "storage transpose"}
        return
    for first, stop in columns_matrix.ranges():
        for column_first in range(0, columns_matrix.count, columns_matrix.tile_size):
            column_stop = min(column_first+columns_matrix.tile_size, columns_matrix.count)
            missing = [column for column in range(column_first, column_stop)
                       if not columns_matrix.initial_tile_exists(column, first)]
            if not missing:
                continue
            columns_matrix.S.budget()
            raw_rows, input_tiles = [], []
            for row in range(first, stop):
                encoded, tile = rows_matrix.block(rows_matrix.state["vectors"][row],
                                                 column_first, decode=False)
                raw_rows.append(encoded)
                input_tiles.append(plain(tile))
            for column in missing:
                encoded = [data[column-column_first] for data in raw_rows]
                columns_matrix.put_initial_tile(column, first, encoded,
                    {"source_kernel_row_matrix": source, "source_row_tiles": input_tiles,
                     "operation": "storage transpose; exact original coefficients unchanged"})
    initial = [columns_matrix.initial_vector(i) for i in range(columns_matrix.count)]
    columns_matrix.initialize(initial, reducer_control(pivot_rows, True),
        {"source_kernel_row_matrix": source, "operation": "storage transpose"})


def verify_full_kernel_product(source_matrix, joint_kernel, label):
    """Check P*(H;W)=0 exactly in L[z], after the kernel's column Hermite reduction."""
    assert source_matrix.finished and joint_kernel.finished
    assert source_matrix.orientation == joint_kernel.orientation == "columns"
    n = source_matrix.length
    assert source_matrix.count == joint_kernel.length
    assert joint_kernel.count == n
    A, S = source_matrix.A, source_matrix.S
    source_spec, kernel_spec = S.spec(source_matrix.final_name), S.spec(joint_kernel.final_name)
    index_name = label+"-full-polynomial-kernel-verification"
    if S.exists(index_name):
        value = S.load(index_name)
        assert value["source_original_pair_matrix"] == source_spec
        assert value["source_joint_Hermite_kernel"] == kernel_spec
        for entry in value["full_row_block_certificates"]:
            S.load(entry)
        return S.spec(index_name)
    certificates = []
    for column in range(n):
        kernel_vector = joint_kernel.state["vectors"][column]
        for first, stop in source_matrix.ranges():
            name = label+"-kernel-col-"+str(column).zfill(4)+"-rows-"+str(first).zfill(5)
            current_name = name+"-current"
            binding = {"source_original_pair_matrix": source_spec,
                       "source_joint_Hermite_kernel": kernel_spec,
                       "source_kernel_column": kernel_vector,
                       "kernel_column": column, "row_first": first, "row_stop": stop}
            if S.exists(name):
                value = S.load(name)
                assert all(value[k] == v for k, v in binding.items())
                assert value["all_exact_polynomial_entries_zero"] is True
                certificates.append(S.spec(name))
                S.path(current_name).unlink(missing_ok=True)
                continue
            if S.exists(current_name):
                current = S.load(current_name, complete=False)
                assert all(current[k] == v for k, v in binding.items())
                start = current["next_input_column"]
                residual = [A.decode(x) for x in current["partial_sum"]]
                assert len(residual) == stop-first
            else:
                start, residual = 0, [A.zero]*(stop-first)
            assert 0 <= start <= source_matrix.count
            assert start == source_matrix.count or start % joint_kernel.tile_size == 0
            for k0 in range(start, source_matrix.count, joint_kernel.tile_size):
                S.budget()
                coefficients, _ = joint_kernel.block(kernel_vector, k0)
                for offset, coefficient in enumerate(coefficients):
                    if not coefficient:
                        continue
                    block, _ = source_matrix.block(source_matrix.state["vectors"][k0+offset], first)
                    for j, value in enumerate(block):
                        if value:
                            residual[j] = residual[j]+value*coefficient
                S.put(current_name, dict(binding, kind="exact_kernel_product_checkpoint",
                    next_input_column=k0+len(coefficients), partial_sum=[x.encode() for x in residual],
                    complete_polynomial_identity_claimed=False), complete=False, replace=True)
            assert all(not value for value in residual), "Original polynomial kernel identity failed"
            entry = S.put(name, dict(binding,
                all_input_columns_consumed=source_matrix.count,
                all_exact_polynomial_entries_zero=True,
                arithmetic_ring="original L[z]; exact coefficients, no modular rank inference"))
            certificates.append(entry)
            S.path(current_name).unlink(missing_ok=True)
    assert len(certificates) == n*len(source_matrix.ranges())
    return S.put(index_name, {
        "source_original_pair_matrix": source_spec,
        "source_joint_Hermite_kernel": kernel_spec,
        "full_matrix_shape": [n, n], "all_input_columns": source_matrix.count,
        "full_row_block_certificates": certificates,
        "full_original_Mp_H_equals_Mq_W_verified_exactly": True,
        "complete_kernel_from_unimodular_transcript_also_required": True})


def transported_function_coefficient(polynomial, epsilon):
    """Same-function basis transition, with no homogeneous section factor."""
    if not polynomial:
        return Laurent(polynomial.A)
    return Laurent(polynomial.A, -int(epsilon)-polynomial.degree(),
                   Poly(polynomial.A, tuple(reversed(polynomial.c))))


def verify_laurent_inclusion(source_basis, target_basis, epsilon, label, from_chart, to_chart):
    """Triangular solve and full exact multiply-back on the overlap."""
    assert source_basis.finished and target_basis.finished
    assert source_basis.orientation == target_basis.orientation == "columns"
    n = source_basis.count
    assert target_basis.count == n and len(epsilon) == n
    assert source_basis.length == target_basis.length == 2*n
    assert (from_chart, to_chart) in (("tau", "sigma"), ("sigma", "tau"))
    A, S = source_basis.A, source_basis.S
    source_spec, target_spec = S.spec(source_basis.final_name), S.spec(target_basis.final_name)
    index_name = label+"-Laurent-inclusion-index"
    if S.exists(index_name):
        value = S.load(index_name)
        assert value["source_basis"] == source_spec and value["target_basis"] == target_spec
        assert value["from_chart"] == from_chart and value["to_chart"] == to_chart
        for entry in value["column_certificates"]:
            S.load(entry)
        return S.spec(index_name)
    certificates = []
    for column in range(n):
        S.budget()
        name, current_name = label+"-column-"+str(column).zfill(4), label+"-column-"+str(column).zfill(4)+"-current"
        binding = {"source_basis": source_spec, "target_basis": target_spec,
                   "from_chart": from_chart, "to_chart": to_chart, "source_column": column}
        if S.exists(name):
            value = S.load(name)
            assert all(value[k] == v for k, v in binding.items())
            assert value["all_normal_rows_exactly_zero_after_triangular_multiply_back"] is True
            certificates.append(S.spec(name))
            S.path(current_name).unlink(missing_ok=True)
            continue
        if S.exists(current_name):
            current = S.load(current_name, complete=False)
            assert all(current[k] == v for k, v in binding.items())
            next_pivot = current["next_pivot"]
            residual = [Laurent.decode(A, x) for x in current["residual"]]
            solution = [Laurent.decode(A, x) for x in current["solution"]]
        else:
            next_pivot, solution, residual = 0, [], []
            vector = source_basis.state["vectors"][column]
            for row in range(n):
                value = source_basis.entry(vector, row)
                residual.append(transported_function_coefficient(value, epsilon[row]))
        assert len(residual) == n and len(solution) == next_pivot
        for pivot in range(next_pivot, n):
            S.budget()
            vector = target_basis.state["vectors"][pivot]
            diagonal = target_basis.entry(vector, pivot)
            assert diagonal
            quotient = residual[pivot].divide_polynomial(diagonal)
            for first in range(pivot//target_basis.tile_size*target_basis.tile_size,
                               n, target_basis.tile_size):
                block, _ = target_basis.block(vector, first)
                for offset, value in enumerate(block):
                    row = first+offset
                    if pivot <= row < n and value and quotient:
                        residual[row] = residual[row]-quotient*value
            assert not residual[pivot]
            solution.append(quotient)
            S.put(current_name, dict(binding, kind="exact_Laurent_triangular_solve_checkpoint",
                next_pivot=pivot+1, residual=[x.encode() for x in residual],
                solution=[x.encode() for x in solution]), complete=False, replace=True)
        assert len(solution) == n and all(not value for value in residual)
        entry = S.put(name, dict(binding,
            coefficient_ring="original L[t,t^-1] or L[z,z^-1]",
            containment_coefficients=[x.encode() for x in solution],
            all_reduced_denominators_are_constant_times_variable_powers=True,
            all_normal_rows_exactly_zero_after_triangular_multiply_back=True,
            homogeneous_function_pair_factor_has_already_canceled=True,
            ideal_basis_not_transported_as_a_degree_r_section=True))
        certificates.append(entry)
        S.path(current_name).unlink(missing_ok=True)
    return S.put(index_name, {
        "source_basis": source_spec, "target_basis": target_spec,
        "from_chart": from_chart, "to_chart": to_chart,
        "normal_basis_rank": n, "normal_basis_degrees": list(epsilon),
        "column_certificates": certificates,
        "full_exact_Laurent_module_containment_verified": True,
        "transport_formula": "diag(variable^-eps)*source_basis(1/variable)",
        "reverse_direction_uses_D(1/z)^-1_equal_diag(z^-eps)": from_chart == "sigma",
        "source_function_pair_constant_preserved": True})
