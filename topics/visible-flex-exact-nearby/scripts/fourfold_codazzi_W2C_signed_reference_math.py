"""W2C fixed-WVC signed continuous reference profiles and Green-kernel bridge.

NO entry point, file access, native decoding, numerical import, old producer
call, old q/rho/norm target, or scientific execution occurs in this module.
The new owner admits the whole completed WVC and the exact definition chain
before calling it. The only inputs to numerical preparation are enclosures
of THAT fixed reference definition and the true radial integration sets.

The continuous body-source map is G_f = (S G_D, root_odd/mean, theta*outer_even)
or the unchanged high G_0. It has NO pointwise rho2 divisor. The finite circuit
Q_f still uses rho2 = 1+h^2*(a^2+c^2*q^2)/12 on the original fine mesh.
Its exact paired-source identity and the full saved q/e_rho/odd fees remain
separate owner inputs. This bridge never changes Q_f, Y, Z, P, Q, S, or the
actual A/B/C/R and never replaces the genuine high inverse by a finite band.

Whole-box signed p,H,K,g,g_inverse values are new PRIVATE function enclosures,
not old pmax/Hsup upper bounds used as function values. Each scalar profile
has the SAME raw state across every reference seam; S is applied on output.
The reference partition refines all original153 D/S parents, the collar cut,
and cutoff joins. Actual coefficient pieces may instead be covered by their
verified whole-panel hulls when raw transmission is identity. Nonidentity
transmission or an independent affine jump is never silently absorbed here.

Injected API: zero, one, rational(n,d=1), lower(x), upper(x), magnitude(x),
sqrt(x), exp(x), interval(lo,hi). Every result must be a finite enclosure.
lower accepts signed intervals. interval encloses its two directed endpoints.
No original diagnostic float is a mathematical value.

Domain API: api, cells, validate_box(box), cell_index(box), cache_key(box),
whole_cell_box(i), full_length(i), partial_length(box,'prefix'/'suffix'),
ordered_span(left,right). cache_key is an immutable unique identity for the
whole mathematical box, not a sample or an object-id reuse. partial lengths
refer to the actual variable root and actual cell edges. ordered_span bounds
the ordered set left<=right, including a same-cell triangle.

The scalar product tree stores O(number_of_cells) PRIVATE values per mode;
ordered-decay queries take O(log number_of_cells) products. No N-by-N matrix
or public coefficient array is created. The owner preserves complete target
and preparation prefixes under its existing durable-save contract.
"""


WVC_ACTUAL_FILE = {
    "role": "WVC_actual",
    "path": "topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json",
    "git_blob_sha": "746ec1e16befe8914c64521ad087c1f1dd23ab73",
    "bytes": 78627,
    "sha256": "85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88",
}
REFERENCE_CHAIN = {
    "count": 153,
    "sha256": "6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac",
}
DIAGONAL_CHAIN = {
    "count": 153,
    "sha256": "b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2",
}
LOW_MODES = tuple(range(1, 97))
HIGH_MODES = tuple(range(97, 161))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _upper(api, value):
    return -api.lower(-value)


def _clip(api, value, lower, upper=None):
    lo = max(api.lower(value), api.lower(lower))
    hi = _upper(api, value)
    if upper is not None:
        hi = min(hi, _upper(api, upper))
    require(lo <= hi, "true reference invariant intersects the complete enclosure")
    return api.interval(lo, hi)


def _positive_lower(api, value, label):
    result = api.lower(value)
    require(result > 0, "positive complete reference lower: " + label)
    return result


def _same_exact_one(api, value):
    return api.lower(value) == api.one and _upper(api, value) == api.one


def _validate_identity(identity):
    """Data-only binding; byte admission remains the owner's prerequisite."""
    require(isinstance(identity, dict)
            and identity.get("kind") == "complete_fixed_WVC_signed_reference_identity_v1",
            "explicit fixed-WVC signed-profile identity")
    require(identity["complete_original_WVC_file"] == WVC_ACTUAL_FILE
            and identity["original_reference_chain"] == REFERENCE_CHAIN
            and identity["selected_diagonal_chain"] == DIAGONAL_CHAIN,
            "same complete WVC file and both exact153-parent chains")
    require(identity["same_original_D_S_and_true_root"] is True
            and identity["all_original_parent_definitions_verified"] is True
            and identity["no_completed_bound_target_recomputed"] is True
            and identity["scalar_trace_identically_zero"] is True,
            "fixed tracefree WVC, never WCTR or a newly selected reference")
    require(identity["reference_outer_impedance"] == "13/80"
            and identity["fine_refinement"] == 160
            and identity["fine_cell_count"] == 24480
            and identity["finite_normalizer_rule"] ==
                "rho2=1+h^2*(a^2+c^2*q^2)/12",
            "unchanged finite paired-source and rho2 qualification")


class _ScalarProducts:
    """Ordered range product with O(n) storage, without dividing prefixes."""
    def __init__(self, api, values):
        self.api, self.n = api, len(values)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [api.one for _ in range(2*self.size)]
        self.tree[self.size:self.size+self.n] = list(values)
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[2*i] * self.tree[2*i+1]

    def between(self, left, right):
        require(type(left) is int and type(right) is int
                and 0 <= left <= right <= self.n,
                "complete ordered cell-product range")
        before = after = self.api.one
        left += self.size
        right += self.size
        while left < right:
            if left % 2:
                before = before * self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                after = self.tree[right] * after
            left //= 2
            right //= 2
        return before * after


class SignedReferenceProfiles:
    """Exact-function enclosures for one complete piecewise constant reference."""
    def __init__(self, api, domain, etas, qs, diagonals, parent_indices,
                 identity, modes):
        _validate_identity(identity)
        require(domain.api is api, "one directed arithmetic backend")
        n = len(domain.cells)
        require(n > 0 and all(len(v) == n for v in
                (etas, qs, diagonals, parent_indices)),
                "whole same-reference partition")
        require(all(type(i) is int and 0 <= i < 153 for i in parent_indices)
                and list(parent_indices) == sorted(parent_indices)
                and set(parent_indices) == set(range(153)),
                "every original153 parent retained in order")
        require(all(set(row) == set(LOW_MODES) for row in diagonals),
                "all96 exact selected diagonal definitions on each panel")
        modes = tuple(modes)
        require(len(modes) == len(set(modes))
                and all(type(j) is int and 1 <= j <= 160 for j in modes),
                "finite declared original reference modes")
        self.api, self.domain, self.n = api, domain, n
        self.etas, self.qs, self.diagonals = etas, qs, diagonals
        self.parent_indices, self.identity = tuple(parent_indices), identity
        self.modes, self.mode = modes, {}
        self.lengths = [domain.full_length(i) for i in range(n)]
        self.cache = {}
        self.pstar = api.rational(1, 16)
        self.p_outer = api.rational(13, 80)
        for i in range(n):
            _positive_lower(api, self.lengths[i], "actual panel length")
            require(api.lower(etas[i]) >= 0
                    and api.lower(qs[i]) >= api.rational(1, 8),
                    "complete nonnegative eta and unchanged positive q floor")
            if parent_indices[i] == 0:
                require(_upper(api, etas[i]) == 0
                        and _same_exact_one(api, qs[i])
                        and all(_upper(api, api.magnitude(a)) == 0
                                for a in diagonals[i].values()),
                        "original collar reference D=0 and physical S=Id")
        for j in modes:
            self._prepare_mode(j)

    def _coefficients(self, j, i):
        c = (4*j) * self.etas[i]
        a = self.diagonals[i][j] if j <= 96 else self.api.zero
        return a, c, self.qs[i]

    def _segment(self, j, i, length, p_right):
        """p_left,tau,sigma,tau_inverse for the same true oriented segment."""
        api = self.api
        require(api.lower(length) >= 0, "true nonnegative segment length")
        _positive_lower(api, p_right, "right impedance")
        a, c, q = self._coefficients(j, i)
        if _upper(api, c) == 0:
            require(_upper(api, api.magnitude(a)) == 0,
                    "zero-rate reference diagonal")
            return p_right, api.one, api.zero, api.one
        _positive_lower(api, c, "positive nonroot reference speed")
        omega = api.sqrt(a*a+c*c*q*q)
        _positive_lower(api, omega, "tracefree frequency")
        decay = api.exp(-omega*length)
        e = decay*decay
        A = (api.one+e)/2
        B = (api.one-e)/(2*omega)
        den = A+B*(a+c*p_right)
        _positive_lower(api, den, "complete scaled impedance pivot")
        p_left = (B*c*q*q+p_right*(A-B*a))/den
        p_left = _clip(api, p_left, self.pstar)
        tau = _clip(api, decay/den, api.zero, api.one)
        sigma = _clip(api, B*c/den, api.zero)
        # True reciprocal of tau, defined without division by an enclosure
        # of a tiny global g or by a possibly wide decay interval.
        tau_inverse = _clip(api, api.exp(omega*length)*den, api.one)
        return p_left, tau, sigma, tau_inverse

    def _prepare_mode(self, j):
        api, n = self.api, self.n
        p = [api.zero for _ in range(n+1)]
        p[n] = self.p_outer
        tau, sigma, inverse_tau = ([api.zero for _ in range(n)] for _ in range(3))
        for i in range(n-1, -1, -1):
            p[i], tau[i], sigma[i], inverse_tau[i] = self._segment(
                j, i, self.lengths[i], p[i+1])
        H = [api.zero for _ in range(n+1)]
        g = [api.one for _ in range(n+1)]
        gi = [api.one for _ in range(n+1)]
        for i in range(n):
            H[i+1] = _clip(api, tau[i]*tau[i]*H[i]+sigma[i], api.zero,
                            api.one/_positive_lower(api, p[i+1], "next impedance"))
            g[i+1] = g[i]*tau[i]
            gi[i+1] = gi[i]*inverse_tau[i]
        self.mode[j] = {
            "p": p, "H": H, "g": g, "g_inverse": gi,
            "tau": tau, "sigma": sigma, "inverse_tau": inverse_tau,
            "products": _ScalarProducts(api, tau),
        }

    def at(self, j, box):
        """Enclose each exact profile on the WHOLE supplied radial box."""
        require(j in self.mode, "mode prepared once on the admitted reference")
        self.domain.validate_box(box)
        i = self.domain.cell_index(box)
        key = (j, self.domain.cache_key(box))
        if key in self.cache:
            return dict(self.cache[key])
        api, data = self.api, self.mode[j]
        remaining = self.domain.partial_length(box, "suffix")
        p, _, _, _ = self._segment(j, i, remaining, data["p"][i+1])
        elapsed = self.domain.partial_length(box, "prefix")
        _, tau, sigma, inverse_tau = self._segment(j, i, elapsed, p)
        H = _clip(api, tau*tau*data["H"][i]+sigma, api.zero,
                    api.one/_positive_lower(api, p, "interior impedance"))
        K = _clip(api, api.one-p*H, api.zero, api.one)
        value = {
            "p": p, "H": H, "K": K,
            "g": data["g"][i]*tau,
            "g_inverse": data["g_inverse"][i]*inverse_tau,
        }
        self.cache[key] = value
        return dict(value)

    def ordered_decay(self, j, left, right):
        """True exp(-integral_left^right(a+c*p)), never a prefix quotient."""
        self.domain.validate_box(left)
        self.domain.validate_box(right)
        li, ri = self.domain.cell_index(left), self.domain.cell_index(right)
        require(li <= ri, "whole ordered reference boxes")
        data = self.mode[j]
        if li == ri:
            _, length = self.domain.ordered_span(left, right)
            return self._segment(j, li, length, self.at(j, right)["p"])[1]
        first = self._segment(j, li, self.domain.partial_length(left, "suffix"),
                              data["p"][li+1])[1]
        middle = data["products"].between(li+1, ri)
        last = self._segment(j, ri, self.domain.partial_length(right, "prefix"),
                             self.at(j, right)["p"])[1]
        return first*middle*last

    def to_right(self, j, box):
        """True propagation from any point of the box to the actual outer end."""
        self.domain.validate_box(box)
        i, data = self.domain.cell_index(box), self.mode[j]
        first = self._segment(j, i, self.domain.partial_length(box, "suffix"),
                              data["p"][i+1])[1]
        return first*data["products"].between(i+1, self.n)


def prepare_signed_reference_profiles(api, domain, etas, qs, diagonals,
                                      parent_indices, identity,
                                      modes=tuple(range(1, 161))):
    return SignedReferenceProfiles(api, domain, etas, qs, diagonals,
                                   parent_indices, identity, modes)


def _coordinates(modes, include_mean):
    return (tuple((0, j) for j in modes)
            + (((1, 0),) if include_mean else ())
            + tuple((1, j) for j in modes))


def complete_signed_reference_kernel(api, domain, profiles, modes, scales,
        thetas, include_mean, include_atoms, kernel_api, coordinates=None,
        label="complete_fixed_WVC_signed_Green"):
    """Exact signed continuous body kernel plus ALL declared output atoms.

    Low case: modes1..96, all193 body coordinates and all193 observations.
    High case: modes97..160, no mean/atoms, explicitly zero extended to the
    supplied finite high carrier (e.g.97..288). Such extension is Pi0 G Pi0;
    it is not projection of the actual complete high inverse/error legs.
    """
    require(profiles.domain is domain and profiles.api is api,
            "same full-box signed profile provider")
    modes = tuple(modes)
    require(modes in (LOW_MODES, HIGH_MODES)
            and set(modes).issubset(profiles.mode), "complete declared low or high map")
    require(type(include_mean) is bool and type(include_atoms) is bool,
            "explicit physical mean and endpoint-atom qualification")
    low = modes == LOW_MODES
    require((include_mean and include_atoms) if low else
            (not include_mean and not include_atoms),
            "low map has its entire193 observations; high trial has none")
    require(len(scales) == profiles.n, "complete physical output S")
    if low:
        require(scales is profiles.qs,
                "exact SAME original physical q/S objects, not replacement weights")
    else:
        require(all(_same_exact_one(api, x) for x in scales),
                "unchanged high trial has raw output, S=Id")
    active = _coordinates(modes, include_mean)
    coords = tuple(active if coordinates is None else coordinates)
    require(len(coords) == len(set(coords))
            and all(isinstance(v, tuple) and len(v) == 2 and
                    type(v[0]) is int and type(v[1]) is int and
                    v[0] in (0, 1) and v[1] >= 0 and
                    (v[0] == 1 or v[1] > 0) for v in coords)
            and set(active).issubset(coords), "complete normalized physical carrier")
    if low:
        require(coords == active, "exact193 low coordinate order including mean1")
        require(all(j in thetas and api.lower(thetas[j]) > 0 for j in modes),
                "all original outer H^(-5/6) Riesz factors")
    else:
        require(all(j >= 97 for _, j in coords),
                "explicit high zero extension, no artificial mean")
    position = {v:i for i,v in enumerate(coords)}
    no, rank = len(coords), len(modes)
    atom_coords = ((tuple((0,j) for j in modes) + ((1,0),)
                   + tuple((2,j) for j in modes)) if low else ())
    atom_position = {v:i for i,v in enumerate(atom_coords)}
    Matrix, Field = kernel_api.Matrix, kernel_api.Field

    def blank(rows, cols):
        return [[api.zero for _ in range(cols)] for _ in range(rows)]

    def scale_at(box):
        return scales[domain.cell_index(box)]

    def lower_U(box):
        out = blank(no, rank)
        scale = scale_at(box)
        for col,j in enumerate(modes):
            v = profiles.at(j, box)
            out[position[(0,j)]][col] = -v["g"]*v["p"]
            out[position[(1,j)]][col] = v["g"]*scale
        return Matrix(no,rank,out)

    def lower_V(box):
        out = blank(rank, no)
        for row,j in enumerate(modes):
            v = profiles.at(j,box)
            out[row][position[(0,j)]] = -v["g_inverse"]*v["H"]
            out[row][position[(1,j)]] = v["g_inverse"]*v["K"]
        return Matrix(rank,no,out)

    upper_rank = rank + (1 if include_mean else 0)

    def upper_P(box):
        out = blank(no,upper_rank)
        scale = scale_at(box)
        for col,j in enumerate(modes):
            v = profiles.at(j,box)
            out[position[(0,j)]][col] = -v["g_inverse"]*v["K"]
            out[position[(1,j)]][col] = -v["g_inverse"]*scale*v["H"]
        if include_mean:
            out[position[(1,0)]][rank] = -scale
        return Matrix(no,upper_rank,out)

    def upper_Q(box):
        out = blank(upper_rank,no)
        for row,j in enumerate(modes):
            v = profiles.at(j,box)
            out[row][position[(0,j)]] = v["g"]
            out[row][position[(1,j)]] = v["g"]*v["p"]
        if include_mean:
            out[rank][position[(1,0)]] = api.one
        return Matrix(upper_rank,no,out)

    def atoms(box):
        out = blank(len(atom_coords),no)
        if include_atoms:
            for j in modes:
                v = profiles.at(j,box)
                ro = atom_position[(0,j)]
                out[ro][position[(0,j)]] = -v["g"]
                out[ro][position[(1,j)]] = -v["g"]*v["p"]
                decay = profiles.to_right(j,box)
                re = atom_position[(2,j)]
                out[re][position[(0,j)]] = -thetas[j]*decay*v["H"]
                out[re][position[(1,j)]] = thetas[j]*decay*v["K"]
            out[atom_position[(1,0)]][position[(1,0)]] = -api.one
        return Matrix(len(atom_coords),no,out)

    result = kernel_api.SignedKernel(domain,coords,coords,
        kernel_api.zero_field(domain,no,no,label+":local_zero"),
        Field(domain,no,rank,lower_U,label+":U"),
        Field(domain,rank,no,lower_V,label+":V"),
        Field(domain,no,upper_rank,upper_P,label+":P"),
        Field(domain,upper_rank,no,upper_Q,label+":Q"),
        Field(domain,len(atom_coords),no,atoms,label+":all_atoms"),label)

    def direct(r,s,orientation):
        require(orientation in (-1,0,1), "true two-triangle radial ordering")
        if orientation == 0:
            return kernel_api.hull(api,direct(r,s,1),direct(r,s,-1))
        out = blank(no,no)
        scale = scale_at(r)
        for j in modes:
            vr,vs = profiles.at(j,r),profiles.at(j,s)
            odd,even = position[(0,j)],position[(1,j)]
            if orientation == 1:
                decay = profiles.ordered_decay(j,s,r)
                out[odd][odd] = decay*vr["p"]*vs["H"]
                out[odd][even] = -decay*vr["p"]*vs["K"]
                out[even][odd] = -decay*scale*vs["H"]
                out[even][even] = decay*scale*vs["K"]
            else:
                decay = profiles.ordered_decay(j,r,s)
                out[odd][odd] = -decay*vr["K"]
                out[odd][even] = -decay*vr["K"]*vs["p"]
                out[even][odd] = -decay*scale*vr["H"]
                out[even][even] = -decay*scale*vr["H"]*vs["p"]
        if include_mean and orientation == -1:
            out[position[(1,0)]][position[(1,0)]] = -scale
        return Matrix(no,no,out)

    result.kernel_override = direct
    result.atom_coordinates = atom_coords
    result.fixed_reference_identity = profiles.identity
    result.reference_projection_coordinates = active
    result.continuous_kernel_has_no_rho2_divisor = True
    result.actual_infinite_high_inverse_is_not_this_reference = True
    return result


def complete_reference_adjoint_blocks(operator, kernel_api, label):
    """Full adjoint = body-kernel adjoint PLUS all finite-port source columns.

    The body view is explicitly created only to invoke body_adjoint. The
    returned finite_port_columns is atoms(r)^T and must be used for all
    original finite dual inputs. No output atom is discarded or differentiated
    as an L2 trace; the supplied S and outer-Riesz factors are already in the kernel.
    Any further source Sobolev weights must wrap the full ordered operator.
    Independent actual boundary/affine ports remain with the owner as before.
    """
    domain,api = operator.domain,operator.api
    body = kernel_api.SignedKernel(domain,operator.outputs,operator.inputs,
        operator.local,operator.U,operator.V,operator.P,operator.Q,
        kernel_api.zero_field(domain,0,len(operator.inputs),label+":no_observations"),
        label+":body_view")
    body.kernel_override = operator.kernel_override
    adjoint = kernel_api.body_adjoint(body,label+":body_adjoint")
    finite = kernel_api.transposed_field(operator.atoms,label+":finite_port_columns")
    return {
        "body_adjoint": adjoint,
        "finite_port_columns": finite,
        "finite_port_coordinates": tuple(getattr(operator,"atom_coordinates",())),
        "complete_original_atom_count": operator.atom_count,
        "all_original_output_observations_transposed_once": True,
        "declared_S_and_outer_Riesz_factors_already_in_kernel": True,
    }
