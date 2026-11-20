"""R141 same-model exact refinement and bounded-memory directed Gram engine.

No work at import and no filesystem or numerical-library access.  Private
matrix storage consists of standard array('d') midpoint/radius pairs.  Every
packed entry is checked by directed Arb arithmetic to enclose its original
ball; unpacking uses exact binary64 integer ratios and an enclosing interval.
The lossy storage is therefore an explicit outward enclosure, never a float
certificate.  Exact parent model definitions and true coordinate maps remain.
"""


N = 193
P = 97
Q = 96
MAX_REFINED_CELLS = 1536
MAX_PACKED_BYTES = 8*1024*1024*1024
MAX_DECODED_ENTRIES = 200000
INTEGRATION_SUBBOXES = 4
LOCAL_TAYLOR_ORDER = 16


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact_float(api, value):
    numerator, denominator = value.as_integer_ratio()
    result = api.rational(numerator, denominator)
    require(result.is_finite() and result.lower() == result.upper(),
            "exact binary64 value at current directed precision")
    return result


class PackedMatrices:
    """Compact private ball arrays, with a small bounded decoded-matrix cache."""
    def __init__(self, api, km, maximum_bytes=MAX_PACKED_BYTES,
                 maximum_decoded_entries=MAX_DECODED_ENTRIES):
        from collections import OrderedDict
        self.api, self.km = api, km
        self.maximum_bytes = maximum_bytes
        self.maximum_decoded_entries = maximum_decoded_entries
        self.data = {}
        self.cache = OrderedDict()
        self.live_bytes = self.peak_bytes = self.decoded_entries = 0
        self.entries_packed = self.radius_guards_passed = 0

    def put(self, key, matrix):
        import math
        from array import array
        require(isinstance(key, tuple) and key not in self.data,
                "one private compact matrix definition per key")
        size = 16*matrix.rows*matrix.cols
        require(self.live_bytes+size <= self.maximum_bytes,
                "complete compact payload memory bound")
        values = array("d")
        require(values.itemsize == 8, "declared binary64 compact array element")
        for row in matrix.values:
            for entry in row:
                require(entry.is_finite(), "finite whole directed matrix entry")
                midpoint = float(entry.mid())
                require(math.isfinite(midpoint), "finite compact binary64 midpoint")
                midpoint_exact = exact_float(self.api, midpoint)
                radius = abs(entry-midpoint_exact).upper()
                require(radius.is_finite() and self.api.lower(radius) >= 0,
                        "whole outward packing error")
                radius_float = float(radius)
                require(math.isfinite(radius_float) and radius_float >= 0,
                        "finite compact binary64 error radius")
                radius_exact = exact_float(self.api, radius_float)
                # No assumption about binary conversion direction is used:
                # the chosen double is compared to the actual Arb upper.
                for _ in range(4):
                    if bool(radius_exact >= radius):
                        break
                    radius_float = math.nextafter(radius_float, math.inf)
                    require(math.isfinite(radius_float), "finite outward compact radius")
                    radius_exact = exact_float(self.api, radius_float)
                require(bool(radius_exact >= radius), "directed compact radius containment")
                values.extend((midpoint, radius_float))
                self.entries_packed += 1
                self.radius_guards_passed += 1
        require(len(values)*values.itemsize == size, "exact compact payload bytes")
        self.data[key] = (matrix.rows, matrix.cols, values)
        self.live_bytes += size
        self.peak_bytes = max(self.peak_bytes, self.live_bytes)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        rows, cols, packed = self.data[key]
        entries = []
        offset = 0
        for _ in range(rows):
            row = []
            for _ in range(cols):
                midpoint = exact_float(self.api, packed[offset])
                radius = exact_float(self.api, packed[offset+1])
                if radius.lower() == 0 and radius.upper() == 0:
                    value = midpoint
                else:
                    value = self.api.interval(midpoint-radius, midpoint+radius)
                require(value.is_finite(), "finite reconstructed complete ball")
                row.append(value)
                offset += 2
            entries.append(row)
        result = self.km.Matrix(rows, cols, entries)
        self.cache[key] = result
        self.decoded_entries += rows*cols
        while self.decoded_entries > self.maximum_decoded_entries and len(self.cache) > 1:
            _, old = self.cache.popitem(last=False)
            self.decoded_entries -= old.rows*old.cols
        return result

    def remove(self, key):
        rows, cols, _ = self.data.pop(key)
        self.live_bytes -= 16*rows*cols
        if key in self.cache:
            old = self.cache.pop(key)
            self.decoded_entries -= old.rows*old.cols

    def release(self, prefix):
        for key in list(self.data):
            if key[:len(prefix)] == prefix:
                self.remove(key)

    def metadata(self):
        require(self.entries_packed == self.radius_guards_passed,
                "every private packed entry has a directed containment guard")
        return {"kind": "directed_binary64_midpoint_radius_private_arrays_v1",
                "live_payload_bytes": self.live_bytes, "peak_payload_bytes": self.peak_bytes,
                "maximum_payload_bytes": self.maximum_bytes,
                "decoded_cache_entry_cap": self.maximum_decoded_entries,
                "entries_packed": self.entries_packed,
                "complete_radius_guards_passed": self.radius_guards_passed,
                "private_arrays_written_to_disk": False,
                "rounded_matrix_replaces_exact_target": False}


class MatrixSequence:
    def __init__(self, store, prefix, count):
        self.store, self.prefix, self.count = store, prefix, count

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if index < 0:
            index += self.count
        if not 0 <= index < self.count:
            raise IndexError(index)
        return self.store.get(self.prefix+(index,))


class NodeSequence:
    def __init__(self, store, count):
        self.store, self.count = store, count

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if index < 0:
            index += self.count
        if not 0 <= index < self.count:
            raise IndexError(index)
        return {name: self.store.get(("model", "node", index, name))
                for name in ("left", "right", "ell", "rho")}


class RefinedDomain:
    """Exact affine subcells, including all variable-root collar subends."""
    def __init__(self, original, counts):
        self.original, self.api = original, original.api
        self.fzero, self.fone = original.fzero, original.fone
        require(len(counts) == len(original.cells)
                and all(type(n) is int and n >= 1 for n in counts),
                "one positive exact subdivision count per original panel")
        self.counts = tuple(counts)
        self.cells = tuple({"parent_panel": i, "slice": j, "count": n}
                           for i, n in enumerate(counts) for j in range(n))
        require(len(self.cells) <= MAX_REFINED_CELLS, "complete refined-cell memory/work cap")

    def exact(self, value):
        return self.original.exact(value)

    def validate_box(self, box):
        require(isinstance(box, tuple) and len(box) == 3 and type(box[0]) is int,
                "immutable exact refined box")
        i, a, b = box
        require(0 <= i < len(self.cells) and self.fzero <= a <= b <= self.fone,
                "whole box in the declared refined cell")

    def to_parent_box(self, box):
        self.validate_box(box)
        i, a, b = box
        cell = self.cells[i]
        return (cell["parent_panel"], (cell["slice"]+a)/cell["count"],
                (cell["slice"]+b)/cell["count"])

    def whole_cell_box(self, index):
        box = (index, self.fzero, self.fone)
        self.validate_box(box)
        return box

    def point(self, index, fraction):
        box = (index, fraction, fraction)
        self.validate_box(box)
        return box

    def cell_index(self, box):
        self.validate_box(box)
        return box[0]

    def full_length(self, index):
        cell = self.cells[index]
        value = self.original.full_length(cell["parent_panel"])/cell["count"]
        require(self.api.lower(value) > 0, "true positive affine subcell length")
        return value

    def cache_key(self, box):
        self.validate_box(box)
        i, a, b = box
        return (i, int(a.numerator), int(a.denominator), int(b.numerator), int(b.denominator))

    def exact_physical_cover(self, box):
        return self.original.exact_physical_cover(self.to_parent_box(box))

    def physical_interval(self, box):
        return self.original.physical_interval(self.to_parent_box(box))

    def node_parent_point(self, index):
        if index == len(self.cells):
            return self.to_parent_box(self.point(index-1, self.fone))
        return self.to_parent_box(self.point(index, self.fzero))


class RefinedContext:
    def __init__(self, context, counts):
        self.original = context
        self.domain = RefinedDomain(context.domain, counts)
        parents = [c["parent_panel"] for c in self.domain.cells]
        self.reference_qs = [context.reference_qs[i] for i in parents]
        self.reference_etas = [context.reference_etas[i] for i in parents]
        self.reference_diagonals = [context.reference_diagonals[i] for i in parents]
        self.reference_thetas = context.reference_thetas
        self.reference_identity = context.reference_identity
        self.qualifications = dict(context.qualifications)
        self.parent_indices = [context.parent_indices[i] for i in parents]

    def centre_matrix(self, outputs, inputs, box):
        return self.original.centre_matrix(outputs, inputs, self.domain.to_parent_box(box))


class RefinedGenerators:
    def __init__(self, api, km, parents, domain):
        self.api, self.km, self.parents, self.domain = api, km, parents, domain
        self.cache_key = self.cache_value = None

    def __len__(self):
        return len(self.domain.cells)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if not 0 <= index < len(self):
            raise IndexError(index)
        cell = self.domain.cells[index]
        key = (cell["parent_panel"], cell["count"])
        if key != self.cache_key:
            self.cache_value = self.km.scale(self.api, self.api.rational(1, key[1]), self.parents[key[0]])
            self.cache_key = key
        return self.cache_value


def refined_plan(api, km, core, context, parent_generators, completed_rows):
    """Recheck a new directed local-span condition, never the old float norm.

    Start with every completed v3 cut.  If the exact directed span is not at
    most4, only double that parent's subdivision, retaining all old cuts.
    The complete plan and cap are resolved before any carrier propagation.
    """
    require(len(parent_generators) == len(completed_rows) == len(context.domain.cells) == 155,
            "same entire prior parent model")
    counts, balances, spans, doubled = [], [], [], []
    for i, (generator, row) in enumerate(zip(parent_generators, completed_rows)):
        require(row[0] == i and row[1] == context.parent_indices[i]
                and type(row[6]) is int and row[6] > 0,
                "exact original complete-plan identity")
        balance = exact_float(api, row[3])
        require(api.lower(balance) > 0, "same positive exact dyadic v3 similarity")
        factors = [api.one]*96+[balance]*97
        maximum = api.zero
        for r, values in enumerate(generator.values):
            total = sum((api.magnitude(factors[r]*value/factors[c])
                         for c, value in enumerate(values)), api.zero).upper()
            maximum = core.maximum_upper(api, [maximum, total])
        n = row[6]
        if not bool(maximum <= 4*n):
            n *= 2
            doubled.append(i)
        require(bool(maximum <= 4*n), "strictly bounded complete directed local span")
        counts.append(n)
        balances.append(balance)
        spans.append((maximum/n).upper())
    require(sum(counts) <= MAX_REFINED_CELLS, "complete refined carrier cap before propagation")
    return {"counts": counts, "balances": balances, "spans": spans,
            "doubled_original_panels": doubled,
            "original_completed_substeps": sum(row[6] for row in completed_rows),
            "complete_refined_cells": sum(counts),
            "every_original_cut_retained": True,
            "directed_local_span_at_most4": True,
            "actual_coefficient_enclosures_refined": False}


def prepare_chart_specs(api, context, refined_context, progress=None):
    """Two exact binary64 parameters per reference mode/node, no AL QR."""
    from array import array
    domain = refined_context.domain
    result = []
    profiles = context.reference_profiles
    for node in range(len(domain.cells)+1):
        point = domain.node_parent_point(node)
        values = array("d")
        for j in range(1, 97):
            reference = profiles.at(j, point)
            p = float(reference["p"].mid())
            H = float(reference["H"].mid())
            # Exact conversion is checked now, at the declared model precision.
            require(api.lower(exact_float(api, p)) > 0 and api.lower(exact_float(api, H)) >= 0,
                    "complete deterministic reference chart proposal")
            values.extend((p, H))
        result.append(values)
        # These evaluations are proposal materialization, not old norm targets.
        # The provider's point cache must not retain all137000 node/mode boxes.
        profiles.cache.clear()
        if progress is not None and (node % 32 == 0 or node == len(domain.cells)):
            progress("refined_reference_chart_proposals", {"nodes_complete": node+1,
                "nodes": len(domain.cells)+1, "actual_AL_QR_called": False})
    return result


def _chart(api, values, first=False, last=False):
    require(len(values) == 192, "all96 determinant-one proposal pairs")
    answer = []
    for j in range(96):
        p_trial, H = exact_float(api, values[2*j]), exact_float(api, values[2*j+1])
        K = api.one-p_trial*H
        if first:
            K, H = api.one, api.zero
        p = api.rational(13, 80) if last else p_trial
        determinant = K+p*H
        require(api.lower(determinant) > 0,
                "complete original boundary chart has a positive exact2x2 determinant")
        answer.append((K, p, H, determinant))
    return answer


def chart_left(api, km, chart, matrix, inverse=False):
    require(matrix.rows == N, "whole raw row chart action")
    values = [list(row) for row in matrix.values]
    for j, (K, p, H, determinant) in enumerate(chart):
        a, b = matrix.values[j], matrix.values[97+j]
        if inverse:
            values[j] = [(x+p*y)/determinant for x, y in zip(a, b)]
            values[97+j] = [(-H*x+K*y)/determinant for x, y in zip(a, b)]
        else:
            values[j] = [K*x-p*y for x, y in zip(a, b)]
            values[97+j] = [H*x+y for x, y in zip(a, b)]
    return km.Matrix(N, matrix.cols, values)


def chart_right(api, km, matrix, chart, inverse=False):
    require(matrix.cols == N, "whole raw column chart action")
    values = [list(row) for row in matrix.values]
    for row, original in zip(values, matrix.values):
        for j, (K, p, H, determinant) in enumerate(chart):
            a, b = original[j], original[97+j]
            if inverse:
                row[j], row[97+j] = (a-H*b)/determinant, (p*a+K*b)/determinant
            else:
                row[j], row[97+j] = K*a+H*b, -p*a+b
    return km.Matrix(matrix.rows, N, values)


def _store_node(api, km, core, store, index, chart, Z, Y):
    """Exact block inverse of T[[I,Y],[Z,I]], using one96-square pivot."""
    W = core.directed_inverse(api, km,
        km.add(api, km.eye(api, Q), km.scale(api, -api.one, km.multiply(api, Z, Y))))
    YW = km.multiply(api, Y, W)
    WZ = km.multiply(api, W, Z)
    left = chart_left(api, km, chart, km.vcat(km.eye(api, P), Z))
    right = chart_left(api, km, chart, km.vcat(Y, km.eye(api, Q)))
    ell = chart_right(api, km,
        km.hcat(km.add(api, km.eye(api, P), km.multiply(api, YW, Z)),
                km.scale(api, -api.one, YW)), chart, inverse=True)
    rho = chart_right(api, km,
        km.hcat(km.scale(api, -api.one, WZ), W), chart, inverse=True)
    for name, value in (("left", left), ("right", right), ("ell", ell), ("rho", rho)):
        store.put(("model", "node", index, name), value)


def build_refined_model(api, km, core, context, parent_generators, plan, chart_specs,
                        store, progress=None):
    """One parent step exponential per direction; streaming exact Riccati."""
    refined = RefinedContext(context, plan["counts"])
    count = len(refined.domain.cells)
    require(len(chart_specs) == count+1 and all(g.shape == (N, N)
            and all(x.lower() == x.upper() for row in g.values for x in row)
            for g in parent_generators), "complete exact dyadic parent definition")
    generators = RefinedGenerators(api, km, parent_generators, refined.domain)
    ix, iy = tuple(range(P)), tuple(range(P, N))
    Z = km.zeros(api, Q, P)
    store.put(("temporary", "Z", 0), Z)
    parent_key = None
    for i, cell in enumerate(refined.domain.cells):
        key = (cell["parent_panel"], cell["count"])
        if key != parent_key:
            step = core.directed_exp(api, km, generators[i], api.one)
            parent_key = key
        chart = _chart(api, chart_specs[i], first=i == 0)
        next_chart = _chart(api, chart_specs[i+1], last=i+1 == count)
        transfer = chart_left(api, km, next_chart,
            chart_right(api, km, step, chart), inverse=True)
        aa, ab = core.submatrix(km, transfer, ix, ix), core.submatrix(km, transfer, ix, iy)
        ba, bb = core.submatrix(km, transfer, iy, ix), core.submatrix(km, transfer, iy, iy)
        inverse = core.directed_inverse(api, km, km.add(api, aa, km.multiply(api, ab, Z)))
        Z = km.multiply(api, km.add(api, ba, km.multiply(api, bb, Z)), inverse)
        store.put(("model", "C", i), inverse)
        store.put(("temporary", "Z", i+1), Z)
        # Propagate the enclosed packed value, so all later claims include
        # every storage rounding rather than silently using an exact point.
        Z = store.get(("temporary", "Z", i+1))
        if progress is not None and (i+1 == count or
                refined.domain.cells[i+1]["parent_panel"] != cell["parent_panel"]):
            progress("refined_complete_left_carrier_parent", {"cells_complete": i+1,
                "cells": count, "original_panels_complete": cell["parent_panel"]+1})
    Y = km.zeros(api, P, Q)
    end_chart = _chart(api, chart_specs[count], last=True)
    _store_node(api, km, core, store, count, end_chart,
                store.get(("temporary", "Z", count)), Y)
    store.remove(("temporary", "Z", count))
    parent_key = None
    for i in range(count-1, -1, -1):
        cell = refined.domain.cells[i]
        key = (cell["parent_panel"], cell["count"])
        if key != parent_key:
            step = core.directed_exp(api, km, generators[i], -api.one)
            parent_key = key
        chart = _chart(api, chart_specs[i], first=i == 0)
        next_chart = _chart(api, chart_specs[i+1], last=i+1 == count)
        transfer = chart_left(api, km, chart,
            chart_right(api, km, step, next_chart), inverse=True)
        aa, ab = core.submatrix(km, transfer, ix, ix), core.submatrix(km, transfer, ix, iy)
        ba, bb = core.submatrix(km, transfer, iy, ix), core.submatrix(km, transfer, iy, iy)
        inverse = core.directed_inverse(api, km, km.add(api, km.multiply(api, ba, Y), bb))
        Y = km.multiply(api, km.add(api, km.multiply(api, aa, Y), ab), inverse)
        store.put(("model", "D", i), inverse)
        _store_node(api, km, core, store, i, chart, store.get(("temporary", "Z", i)), Y)
        store.remove(("temporary", "Z", i))
        if progress is not None and (i == 0 or
                refined.domain.cells[i-1]["parent_panel"] != cell["parent_panel"]):
            progress("refined_complete_right_carrier_parent", {"cells_complete": count-i,
                "cells": count, "original_panels_complete": 155-cell["parent_panel"]})
    nodes = NodeSequence(store, count+1)
    root_atoms = core.rows(km, nodes[0]["left"], tuple(range(P)))
    outer_values = core.rows(km, nodes[-1]["right"], tuple(range(97, N)))
    outer_atoms = km.Matrix(Q, Q, [[refined.reference_thetas[j+1]*value for value in row]
                                  for j, row in enumerate(outer_values.values)])
    return {"context": refined, "generators": generators, "nodes": nodes,
            "Uinv": MatrixSequence(store, ("model", "C"), count),
            "Vinv": MatrixSequence(store, ("model", "D"), count),
            "root_atoms": root_atoms, "outer_atoms": outer_atoms,
            "comparison_BVP_verified": True, "actual_low_BVP_verified": False,
            "reference_identity": context.reference_identity, "private_model_token": object(),
            "refined_plan": plan, "private_store": store,
            "same_exact_parent_midpoint_model": True}


class PacketTotals:
    def __init__(self, store, prefix, panel):
        self.store, self.prefix, self.panel = store, prefix, panel

    def __getitem__(self, name):
        require(name in ("IL", "IR", "OL", "OR"), "one complete source/output Gram")
        prefix = ("packet_output",) if name in ("OL", "OR") else self.prefix
        return self.store.get(prefix+(self.panel, name))


class PackedPackets:
    """A complete ordered source family with only scalar metadata resident."""
    def __init__(self, store, model, role):
        self.store, self.model, self.role = store, model, role
        self.prefix, self.metadata = ("packet", role), []

    def append(self, packet):
        require(packet["panel"] == len(self.metadata)
                and packet["source_role"] == self.role
                and packet["private_model_token"] is self.model["private_model_token"],
                "one whole ordered packet from the same exact comparison model")
        for name in ("IL", "IR"):
            self.store.put(self.prefix+(packet["panel"], name), packet["totals"][name])
        for name in ("OL", "OR"):
            key = ("packet_output", packet["panel"], name)
            # These exact output integrals depend only on the same model
            # and physical S, never on the source role.  The first full
            # enclosure is retained and reused, not replaced by a midpoint.
            if key not in self.store.data:
                self.store.put(key, packet["totals"][name])
        self.metadata.append({key: value for key, value in packet.items() if key != "totals"})

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if not 0 <= index < len(self):
            raise IndexError(index)
        return {**self.metadata[index], "totals": PacketTotals(self.store, self.prefix, index)}

    def release(self):
        self.store.release(self.prefix)
        self.metadata.clear()


def complete_gram_norm_packed(api, km, core, model, packets, prefix, progress=None):
    """R141 exact recurrences, with directed compact storage at every step.

    The stored entries enclose the exact covariance matrices.  Their
    midpoint matrices need not be PSD; positivity belongs to the exact
    Gram/covariance object, and every final upper uses its whole enclosure.
    Only A/B are retained for possible whole-point receiver calculations.
    The outer-atom covariance is released after its complete contribution.
    """
    count = core.require_complete_packets(model, packets)
    store = model["private_store"]
    prefix = tuple(prefix)
    require(prefix and prefix[0] == "norm", "private complete norm namespace")
    left_prefix, right_prefix, outer_prefix = (prefix+(key,) for key in ("A", "B", "K"))
    store.put(left_prefix+(0,), km.zeros(api, P, P))
    for i in range(count):
        value = core.congruence(api, km, km.transpose(model["Uinv"][i]),
            km.add(api, store.get(left_prefix+(i,)), packets[i]["totals"]["OL"]))
        store.put(left_prefix+(i+1,), value)
        if progress is not None and (i % 64 == 63 or i+1 == count):
            progress("refined_complete_Gram_left_covariance", {"source_role": packets.role,
                "cells_complete": i+1, "cells": count})
    store.put(right_prefix+(count,), km.zeros(api, Q, Q))
    store.put(outer_prefix+(count,), core.output_gram(api, km, model["outer_atoms"]))
    for i in range(count-1, -1, -1):
        Dtranspose = km.transpose(model["Vinv"][i])
        value = km.add(api, packets[i]["totals"]["OR"],
            core.congruence(api, km, Dtranspose, store.get(right_prefix+(i+1,))))
        store.put(right_prefix+(i,), value)
        store.put(outer_prefix+(i,), core.congruence(api, km, Dtranspose,
                                                   store.get(outer_prefix+(i+1,))))
        if progress is not None and (i % 64 == 0 or i+1 == count):
            progress("refined_complete_Gram_right_and_outer_covariances", {
                "source_role": packets.role, "cells_complete": count-i, "cells": count})
    root_carry = core.output_gram(api, km, model["root_atoms"])
    body_HS2 = root_HS2 = outer_HS2 = api.zero
    for i in range(count):
        packet, integral = packets[i], packets[i]["totals"]
        next_right = core.congruence(api, km, km.transpose(model["Vinv"][i]),
                                    store.get(right_prefix+(i+1,)))
        body_HS2 += core.positive_upper(api, core.trace_product(api,
            store.get(left_prefix+(i,)), integral["IL"]))
        body_HS2 += core.positive_upper(api, core.trace_product(api, next_right, integral["IR"]))
        body_HS2 += packet["same_panel_left_HS2_upper"]+packet["same_panel_right_HS2_upper"]
        root_HS2 += core.positive_upper(api, core.trace_product(api, root_carry, integral["IL"]))
        outer_HS2 += core.positive_upper(api, core.trace_product(api,
            store.get(outer_prefix+(i,)), integral["IR"]))
        root_carry = core.congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
        if progress is not None and (i % 64 == 63 or i+1 == count):
            progress("refined_complete_Gram_body_and193_atoms", {"source_role": packets.role,
                "cells_complete": i+1, "cells": count})
    body_HS2, root_HS2, outer_HS2 = (core.positive_upper(api, x)
                                     for x in (body_HS2, root_HS2, outer_HS2))
    store.release(outer_prefix)
    return {"source_role": packets.role, "private_model_token": model["private_model_token"],
            "body_HS2_upper": body_HS2, "root97_HS2_upper": root_HS2,
            "outer96_HS2_upper": outer_HS2,
            "body_norm_upper": core.positive_upper(api, api.sqrt(body_HS2)),
            "atoms193_norm_upper": core.positive_upper(api, api.sqrt(root_HS2+outer_HS2)),
            "complete_norm_upper": core.positive_upper(api, api.sqrt(body_HS2+root_HS2+outer_HS2)),
            "private_output_left_covariances": MatrixSequence(store, left_prefix, count+1),
            "private_output_right_covariances": MatrixSequence(store, right_prefix, count+1),
            "private_storage_prefix": prefix, "complete_refined_cells": count}


def source_covariances_packed(api, km, core, model, packets, progress=None):
    """Same complete defect covariances for all real point observations."""
    count = core.require_complete_packets(model, packets, "true_coefficient_defect")
    store = model["private_store"]
    left_prefix, right_prefix = ("source_covariance", "left"), ("source_covariance", "right")
    store.put(left_prefix+(count,), km.zeros(api, P, P))
    for i in range(count-1, -1, -1):
        value = km.add(api, packets[i]["totals"]["IL"],
            core.congruence(api, km, model["Uinv"][i], store.get(left_prefix+(i+1,))))
        store.put(left_prefix+(i,), value)
        if progress is not None and (i % 64 == 0 or i+1 == count):
            progress("refined_complete_point_left_covariance", {
                "cells_complete": count-i, "cells": count})
    store.put(right_prefix+(0,), km.zeros(api, Q, Q))
    for i in range(count):
        value = core.congruence(api, km, model["Vinv"][i],
            km.add(api, store.get(right_prefix+(i,)), packets[i]["totals"]["IR"]))
        store.put(right_prefix+(i+1,), value)
        if progress is not None and (i % 64 == 63 or i+1 == count):
            progress("refined_complete_point_right_covariance", {
                "cells_complete": i+1, "cells": count})
    return {"left": MatrixSequence(store, left_prefix, count+1),
            "right": MatrixSequence(store, right_prefix, count+1),
            "source_role": packets.role, "private_model_token": model["private_model_token"]}


def make_factor_provider(api, km, core, local, model):
    """The pinned shared-scalar formula with two bounded exact reuse caches.

    Every refined cell in one parent has the same exact H_parent/n and the
    same dyadic B.  Hence its local exponential/Taylor template is identical
    and is prepared only once per parent.  A cache of the four current-cell
    boxes reuses output factors and YV across source roles; no box is omitted
    and no previously completed bound is evaluated as a new target.
    """
    count = len(model["generators"])
    plan = model["refined_plan"]
    balances = [plan["balances"][cell["parent_panel"]]
                for cell in model["context"].domain.cells]

    class RefinedFactorProvider(local.SharedScalarFactorProvider):
        def __init__(self):
            super().__init__(api, km, core, model,
                             [INTEGRATION_SUBBOXES]*count, balances, LOCAL_TAYLOR_ORDER)
            self.parent_template = None
            self.box_cache = {}
            self.private_statistics.update({"parent_templates_prepared": 0,
                "exact_parent_templates_reused": 0, "current_cell_factor_boxes_cap": INTEGRATION_SUBBOXES,
                "source_factor_box_reuses": 0})

        def _prepare_panel(self, panel):
            cell = model["context"].domain.cells[panel]
            template_key = (cell["parent_panel"], cell["count"], self.step_counts[panel], self.order)
            if self.parent_template is None or self.parent_template["key"] != template_key:
                n, qb = self.step_counts[panel], self.balances[panel]
                balance, inverse_balance = [api.one]*96+[qb]*97, [api.one]*96+[api.one/qb]*97
                balanced = self._diagonal_right(
                    self._diagonal_left(balance, model["generators"][panel]), inverse_balance)
                short = km.scale(api, api.rational(1, 2*n), balanced)
                half_plus = core.directed_exp(api, km, short, api.one)
                half_minus = core.directed_exp(api, km, short, -api.one)
                majorant = km.Matrix(N, N, [[api.magnitude(x) for x in row] for row in short.values])
                majorant_exp = core.directed_exp(api, km, majorant, api.one)
                signed_power = positive_power = positive_prefix = km.eye(api, N)
                variation = km.zeros(api, N, N)
                odd_range, even_range = api.interval(-api.one, api.one), api.interval(api.zero, api.one)
                for k in range(1, self.order+1):
                    signed_power = km.scale(api, api.rational(1, k), km.multiply(api, signed_power, short))
                    positive_power = km.scale(api, api.rational(1, k), km.multiply(api, positive_power, majorant))
                    positive_prefix = km.add(api, positive_prefix, positive_power)
                    variation = km.add(api, variation,
                        km.scale(api, odd_range if k % 2 else even_range, signed_power))
                remainder = km.add(api, majorant_exp, km.scale(api, -api.one, positive_prefix))
                whole_variation, tail_rows = [], []
                for row, tail_row in zip(variation.values, remainder.values):
                    result, caps = [], []
                    for value, tail in zip(row, tail_row):
                        cap = core.positive_upper(api, tail)
                        caps.append(cap)
                        result.append(value+api.interval(-cap, cap))
                    whole_variation.append(result)
                    tail_rows.append(core.positive_upper(api, sum(caps, api.zero)))
                actual_q = model["context"].reference_qs[panel]
                require(api.lower(actual_q) > 0, "same actual positive physical S")
                self.parent_template = {"key": template_key, "balance": balance,
                    "inverse_balance": inverse_balance, "half_plus": half_plus,
                    "half_minus": half_minus,
                    "step_plus": km.multiply(api, half_plus, half_plus),
                    "step_minus": km.multiply(api, half_minus, half_minus),
                    "variation": km.Matrix(N, N, whole_variation),
                    "remainder_infinity_upper": core.maximum_upper(api, tail_rows),
                    "actual_S_over_B": [api.one]*96+[actual_q/qb]*97}
                self.private_statistics["parent_templates_prepared"] += 1
            else:
                self.private_statistics["exact_parent_templates_reused"] += 1
            data = self.parent_template
            node = model["nodes"][panel]
            columns = self._diagonal_left(data["balance"], km.hcat(node["left"], node["right"]))
            rows = self._diagonal_right(km.vcat(node["ell"], node["rho"]), data["inverse_balance"])
            first_columns = km.multiply(api, data["half_plus"], columns)
            first_rows = km.multiply(api, rows, data["half_minus"])
            self.cache = {**data, "panel": panel, "index": 0,
                "first_columns": first_columns, "first_rows": first_rows,
                "columns": first_columns, "rows": first_rows}
            self.box_cache.clear()
            self.private_statistics["panels_prepared"] += 1

        def local_factors(self, box, source_matrix):
            domain = model["context"].domain
            domain.validate_box(box)
            panel, lo, hi = box
            n = self.step_counts[panel]
            index_fraction = lo*n
            require(index_fraction.denominator == 1, "exact whole local integration cut")
            index = index_fraction.numerator
            require(0 <= index < n and hi == domain.fone*(index+1)/n
                    and source_matrix.rows == N, "one complete declared box and source")
            if self.cache is None or self.cache["panel"] != panel:
                self._prepare_panel(panel)
            data = self.cache
            if index not in self.box_cache:
                require(index >= data["index"], "first evaluation of box follows exact local order")
                while data["index"] < index:
                    data["columns"] = km.multiply(api, data["step_plus"], data["columns"])
                    data["rows"] = km.multiply(api, data["rows"], data["step_minus"])
                    data["index"] += 1
                    self.private_statistics["point_recurrence_steps"] += 1
                X, Y, V = data["columns"], data["rows"], data["variation"]
                output = self._diagonal_left(data["actual_S_over_B"],
                    km.add(api, X, km.multiply(api, V, X)))
                YV = km.multiply(api, Y, V)
                self.box_cache[index] = (output, Y, YV)
                require(len(self.box_cache) <= INTEGRATION_SUBBOXES,
                        "only four current-cell factor boxes live")
            else:
                self.private_statistics["source_factor_box_reuses"] += 1
            output, Y, YV = self.box_cache[index]
            balanced_source = self._diagonal_left(data["balance"], source_matrix)
            source = km.add(api, km.multiply(api, Y, balanced_source), km.multiply(api, YV, balanced_source))
            self.private_statistics["boxes_evaluated"] += 1
            return {"OL": core.columns(km, output, tuple(range(P))),
                    "OR": core.columns(km, output, tuple(range(P, N))),
                    "IL": core.rows(km, source, tuple(range(P))),
                    "IR": core.rows(km, source, tuple(range(P, N)))}

        def release(self):
            super().release()
            self.parent_template = None
            self.box_cache.clear()

    return RefinedFactorProvider()


def contract_metadata():
    return {"kind": "R141_exact_refinement_compact_directed_Gram_v1",
            "same_prior_parent_comparison_model": True,
            "maximum_refined_cells": MAX_REFINED_CELLS,
            "all_previous_equal_fraction_cuts_retained": True,
            "directed_balanced_span_per_refined_cell_at_most": 4,
            "whole_integration_boxes_per_refined_cell": INTEGRATION_SUBBOXES,
            "local_shared_scalar_Taylor_order": LOCAL_TAYLOR_ORDER,
            "maximum_private_packed_payload_bytes": MAX_PACKED_BYTES,
            "decoded_matrix_entry_cap": MAX_DECODED_ENTRIES,
            "each_packed_entry_has_an_Arb_outward_containment_guard": True,
            "all_parent_lengths_and_true_root_maps_retained": True,
            "actual_coefficient_balls_narrowed_by_refinement": False,
            "whole_source_and193atoms_recursions_retained": True,
            "one_shared_complete_output_Gram_per_model_cell": True,
            "parent_constant_local_templates_reused_exactly": True,
            "private_matrices_written_to_disk": False,
            "old_successful_QR_or_SVD_recomputed": False,
            "scientific_targets_evaluated_at_import": 0}
