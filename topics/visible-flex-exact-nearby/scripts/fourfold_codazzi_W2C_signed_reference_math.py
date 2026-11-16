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
    result.reference_profiles = profiles
    result.reference_modes = modes
    result.reference_output_scales = scales
    result.reference_thetas = thetas
    result.reference_has_mean = include_mean
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


# Stable complete modal matrix-field actions. These are internal function
# enclosures for the SAME fixed reference; no completed q/rho/norm is called.

def _phi1_point(api, x):
    """Enclose (1-exp(-x))/x at a nonnegative directed endpoint, with x=0 exact."""
    require(api.lower(x) >= 0, "nonnegative exponential-integral endpoint")
    if _upper(api, x) == 0:
        return api.one
    if api.lower(x) <= 0:
        return api.interval(api.lower(api.exp(-_upper(api, x))), api.one)
    return _clip(api, (api.one-api.exp(-x))/x, api.zero, api.one)


def _phi1_range(api, x):
    lo, hi = api.lower(x), _upper(api, x)
    require(lo >= 0 and lo <= hi, "whole nonnegative exponential-integral argument")
    return api.interval(api.lower(_phi1_point(api, hi)),
                        _upper(api, _phi1_point(api, lo)))


def _complete_decay_mass(api, rate_lower, rate_upper, length):
    """Both endpoints of a whole positive, variably decaying integration mass.

    If l<=h<=u and k_lower<=k(t)<=k_upper, the exact mass lies in
    [l*phi1(k_upper*u), u*phi1(k_lower*l)]. This works in both orientations;
    it does not identify those two exact integrals with each other.
    """
    lo, hi = api.lower(length), _upper(api, length)
    rl, ru = api.lower(rate_lower), _upper(api, rate_upper)
    require(0 <= lo <= hi and 0 <= rl <= ru,
            "complete variable-length and rate enclosure")
    if hi == 0:
        return api.zero
    lower = api.lower(lo*_phi1_range(api, _clip(api, ru*hi, api.zero)))
    upper = _upper(api, hi*_phi1_range(api, _clip(api, rl*lo, api.zero)))
    return api.interval(max(api.zero, lower), upper)


def _complete_rate_bounds(profiles, j, box):
    api = profiles.api
    i = profiles.domain.cell_index(box)
    a, c, _ = profiles._coefficients(j, i)
    value = a+c*profiles.at(j, box)["p"]
    # The reference barrier is an exact proved qualification, not a lower
    # inferred from an independently stored upper bound.
    lo = max(api.zero, api.lower(value), api.lower(c/32))
    hi = _upper(api, value)
    require(lo <= hi, "complete same-reference damping rate")
    return lo, hi


class _CompleteModalIntegral:
    """One signed row-field, with both complete damped integral orientations.

    All entries of row_field are first formed as signed whole-box expressions.
    The positive mass has TWO directed endpoints. No g or tau is divided.
    Prefix and suffix keep distinct signed states and complete boundary data.
    j=None is the ordinary integral, including the independent physical mean.
    """
    def __init__(self, profiles, j, row_field, kernel_api, label):
        self.profiles, self.domain, self.api = profiles, profiles.domain, profiles.api
        self.j, self.field, self.km, self.label = j, row_field, kernel_api, label
        require(row_field.domain is self.domain and row_field.rows == 1,
                "complete signed row-field integral")
        require(j is None or j in profiles.mode, "declared prepared modal integral")
        self.cols, self.n = row_field.cols, len(self.domain.cells)
        self.full = {}
        self.prefix_nodes = [None]*(self.n+1)
        self.suffix_nodes = [None]*(self.n+1)
        self.prefix_nodes[0] = kernel_api.zeros(self.api, 1, self.cols)
        self.suffix_nodes[self.n] = kernel_api.zeros(self.api, 1, self.cols)
        self.prefix_count, self.suffix_count = 0, self.n

    def _mass(self, box, length):
        if self.j is None:
            return length
        lo, hi = _complete_rate_bounds(self.profiles, self.j, box)
        return _complete_decay_mass(self.api, lo, hi, length)

    def _integral_box(self, box, length):
        if _upper(self.api,length)==0:
            return self.km.zeros(self.api,1,self.cols)
        return self.km.scale(self.api, self._mass(box, length), self.field.at(box))

    def full_cell(self, i):
        require(type(i) is int and 0 <= i < self.n, "complete integral cell")
        if i not in self.full:
            self.full[i] = self._integral_box(
                self.domain.whole_cell_box(i), self.domain.full_length(i))
        return self.full[i]

    def _tau(self, i):
        return self.api.one if self.j is None else self.profiles.mode[self.j]["tau"][i]

    def before(self, index):
        require(type(index) is int and 0 <= index <= self.n, "complete prefix boundary")
        while self.prefix_count < index:
            i = self.prefix_count
            self.prefix_nodes[i+1] = self.km.add(self.api,
                self.km.scale(self.api, self._tau(i), self.prefix_nodes[i]),
                self.full_cell(i))
            self.prefix_count += 1
        return self.prefix_nodes[index]

    def after(self, index):
        require(type(index) is int and 0 <= index <= self.n, "complete suffix boundary")
        while self.suffix_count > index:
            i = self.suffix_count-1
            self.suffix_nodes[i] = self.km.add(self.api,
                self.full_cell(i),
                self.km.scale(self.api, self._tau(i), self.suffix_nodes[i+1]))
            self.suffix_count -= 1
        return self.suffix_nodes[index]

    def prefix(self, box):
        self.domain.validate_box(box)
        i = self.domain.cell_index(box)
        cell = self.domain.whole_cell_box(i)
        endpoint = (i, cell[1], cell[1])
        tau = (self.api.one if self.j is None else
               self.profiles.ordered_decay(self.j, endpoint, box))
        part = self.domain.partial_box(box, "prefix")
        return self.km.add(self.api,
            self.km.scale(self.api, tau, self.before(i)),
            self._integral_box(part, self.domain.partial_length(box, "prefix")))

    def suffix(self, box):
        self.domain.validate_box(box)
        i = self.domain.cell_index(box)
        cell = self.domain.whole_cell_box(i)
        endpoint = (i, cell[2], cell[2])
        tau = (self.api.one if self.j is None else
               self.profiles.ordered_decay(self.j, box, endpoint))
        part = self.domain.partial_box(box, "suffix")
        return self.km.add(self.api,
            self._integral_box(part, self.domain.partial_length(box, "suffix")),
            self.km.scale(self.api, tau, self.after(i+1)))


def _matrix_action_context(operator, forcing, kernel_api):
    require(hasattr(operator, "reference_profiles")
            and operator.continuous_kernel_has_no_rho2_divisor is True,
            "complete fixed-WVC reference action metadata")
    profiles = operator.reference_profiles
    require(operator.fixed_reference_identity == profiles.identity
            and forcing.domain is operator.domain
            and forcing.rows == len(operator.inputs),
            "same true reference and whole matrix-field source")
    return profiles, operator.domain, operator.api, kernel_api


def apply_G_to_matrix_field(operator, forcing, kernel_api, label):
    """Complete signed G applied to every column of one actual matrix field.

    Returns a body Field and an atom-value callable. The callable contains
    ALL original output observations, including the independent mean.
    No body integral is replaced by a sampled value or a constant-source
    approximation; the whole variable source is enclosed on every panel.
    """
    profiles, domain, api, km = _matrix_action_context(operator, forcing, kernel_api)
    modes, scales = operator.reference_modes, operator.reference_output_scales
    coords, k = operator.inputs, forcing.cols
    pos = {v:i for i,v in enumerate(coords)}
    forcing_cache = {}
    def whole_forcing(box):
        key=domain.cache_key(box)
        if key not in forcing_cache:
            forcing_cache[key]=forcing.at(box)
        return forcing_cache[key]
    prefix, suffix = {}, {}
    for j in modes:
        def jf(box, j=j):
            f = whole_forcing(box)
            p = profiles.at(j, box)
            odd, even = pos[(0,j)], pos[(1,j)]
            return km.Matrix(1,k,[[-p["H"]*f.values[odd][b]
                                   +p["K"]*f.values[even][b] for b in range(k)]])
        def lf(box, j=j):
            f = whole_forcing(box)
            p = profiles.at(j, box)
            odd, even = pos[(0,j)], pos[(1,j)]
            return km.Matrix(1,k,[[f.values[odd][b]+p["p"]*f.values[even][b]
                                   for b in range(k)]])
        prefix[j] = _CompleteModalIntegral(profiles,j,
            km.Field(domain,1,k,jf,label+":Jf:"+str(j)),km,label+":prefix:"+str(j))
        suffix[j] = _CompleteModalIntegral(profiles,j,
            km.Field(domain,1,k,lf,label+":Lf:"+str(j)),km,label+":suffix:"+str(j))
    mean = None
    if operator.reference_has_mean:
        mean = _CompleteModalIntegral(profiles,None,
            km.Field(domain,1,k,lambda box:km.Matrix(1,k,
                [list(whole_forcing(box).values[pos[(1,0)]])]),label+":mean_source"),
            km,label+":mean_integral")
    def body(box):
        out = [[api.zero for _ in range(k)] for _ in operator.outputs]
        scale = scales[domain.cell_index(box)]
        for j in modes:
            p = profiles.at(j,box)
            y,b = prefix[j].prefix(box).values[0],suffix[j].suffix(box).values[0]
            odd,even = pos[(0,j)],pos[(1,j)]
            for col in range(k):
                out[odd][col] = -p["p"]*y[col]-p["K"]*b[col]
                out[even][col] = scale*(y[col]-p["H"]*b[col])
        if mean is not None:
            b=mean.suffix(box).values[0]
            out[pos[(1,0)]]=[-scale*x for x in b]
        return km.Matrix(len(operator.outputs),k,out)
    atom_cache = []
    def atoms():
        if atom_cache:
            return atom_cache[0]
        out = [[api.zero for _ in range(k)] for _ in range(operator.atom_count)]
        if operator.atom_count:
            lookup={coord:i for i,coord in enumerate(operator.atom_coordinates)}
            require(operator.atom_count==193 and mean is not None,
                    "complete low observations, not a body-only surrogate")
            for j in modes:
                out[lookup[(0,j)]]=[-x for x in suffix[j].after(0).values[0]]
                out[lookup[(2,j)]]=[operator.reference_thetas[j]*x
                    for x in prefix[j].before(len(domain.cells)).values[0]]
            out[lookup[(1,0)]]=[-x for x in mean.after(0).values[0]]
        value=km.Matrix(operator.atom_count,k,out)
        atom_cache.append(value)
        return value
    return {"body":km.Field(domain,len(operator.outputs),k,body,label+":whole_body"),
            "atoms":atoms,"atom_coordinates":operator.atom_coordinates,
            "complete_original_atom_count":operator.atom_count,
            "whole_matrix_columns":k,
            "same_continuous_reference_without_rho2_division":True}


def apply_G_adjoint_to_matrix_field(operator, body_forcing, finite_port_inputs,
                                    kernel_api, label):
    """Full G*: signed body forcing PLUS every declared finite dual input.

    finite_port_inputs is an explicit atom_count-by-k matrix. Supplying its
    exact zero matrix restricts that input; omission is rejected. This routine
    never identifies the body adjoint with the complete adjoint domain.
    """
    profiles, domain, api, km = _matrix_action_context(operator,body_forcing,kernel_api)
    modes,scales=operator.reference_modes,operator.reference_output_scales
    coords,k=operator.inputs,body_forcing.cols
    pos={v:i for i,v in enumerate(coords)}
    require(isinstance(finite_port_inputs,km.Matrix)
            and finite_port_inputs.shape==(operator.atom_count,k),
            "all finite-port dual columns explicitly supplied")
    forcing_cache={}
    def whole_forcing(box):
        key=domain.cache_key(box)
        if key not in forcing_cache:
            forcing_cache[key]=body_forcing.at(box)
        return forcing_cache[key]
    prefix,suffix={},{}
    for j in modes:
        def uy(box,j=j):
            v=whole_forcing(box);p=profiles.at(j,box)
            scale=scales[domain.cell_index(box)]
            odd,even=pos[(0,j)],pos[(1,j)]
            return km.Matrix(1,k,[[p["K"]*v.values[odd][b]
                +scale*p["H"]*v.values[even][b] for b in range(k)]])
        def fy(box,j=j):
            v=whole_forcing(box);p=profiles.at(j,box)
            scale=scales[domain.cell_index(box)]
            odd,even=pos[(0,j)],pos[(1,j)]
            return km.Matrix(1,k,[[-p["p"]*v.values[odd][b]
                +scale*v.values[even][b] for b in range(k)]])
        prefix[j]=_CompleteModalIntegral(profiles,j,
            km.Field(domain,1,k,uy,label+":UstarSstar:"+str(j)),km,label+":prefix:"+str(j))
        suffix[j]=_CompleteModalIntegral(profiles,j,
            km.Field(domain,1,k,fy,label+":FstarSstar:"+str(j)),km,label+":suffix:"+str(j))
    mean=None
    if operator.reference_has_mean:
        mean=_CompleteModalIntegral(profiles,None,
            km.Field(domain,1,k,lambda box:km.Matrix(1,k,[[
                scales[domain.cell_index(box)]*x
                for x in whole_forcing(box).values[pos[(1,0)]]]]),label+":mean_dual"),
            km,label+":mean_prefix")
    lookup={coord:i for i,coord in enumerate(operator.atom_coordinates)}
    def evaluate(box):
        out=[[api.zero for _ in range(k)] for _ in coords]
        for j in modes:
            p=profiles.at(j,box)
            y,b=prefix[j].prefix(box).values[0],suffix[j].suffix(box).values[0]
            odd,even=pos[(0,j)],pos[(1,j)]
            for col in range(k):
                out[odd][col]=-p["H"]*b[col]-y[col]
                out[even][col]=p["K"]*b[col]-p["p"]*y[col]
            if operator.atom_count:
                root=finite_port_inputs.values[lookup[(0,j)]]
                outer=finite_port_inputs.values[lookup[(2,j)]]
                terminal=operator.reference_thetas[j]*profiles.to_right(j,box)
                for col in range(k):
                    out[odd][col] += -p["g"]*root[col]-terminal*p["H"]*outer[col]
                    out[even][col] += -p["g"]*p["p"]*root[col]+terminal*p["K"]*outer[col]
        if mean is not None:
            out[pos[(1,0)]]=[-x for x in mean.prefix(box).values[0]]
            if operator.atom_count:
                for col in range(k):
                    out[pos[(1,0)]][col] -= finite_port_inputs.values[lookup[(1,0)]][col]
        return km.Matrix(len(coords),k,out)
    return km.Field(domain,len(coords),k,evaluate,label+":complete_body_and_finite_dual")


def _complete_two_decay_mass(api, m_lower, m_upper, n_lower, n_upper, length):
    """Whole mass of two endpoint decays; no difference of nearly equal decays.

    For exact nonnegative a,b,h the average mass is
    exp(-min(a,b)*h)*phi1(abs(a-b)*h).
    Variable rates and l<=h<=u are enclosed by l*average(upper rates,u)
    and u*average(lower rates,l). Both middle orientations are covered.
    """
    lo, hi = api.lower(length), _upper(api,length)
    ml,mu=api.lower(m_lower),_upper(api,m_upper)
    nl,nu=api.lower(n_lower),_upper(api,n_upper)
    require(0<=lo<=hi and 0<=ml<=mu and 0<=nl<=nu,
            "complete two-rate positive mass data")
    if hi==0:
        return api.zero
    def average(a,b,h):
        first,last=min(a,b),max(a,b)
        gap=_clip(api,last-first,api.zero)
        return api.exp(-first*h)*_phi1_range(api,_clip(api,gap*h,api.zero))
    low=api.lower(lo*average(mu,nu,hi))
    high=_upper(api,hi*average(ml,nl,lo))
    return api.interval(max(api.zero,low),high)


class CompleteModalSandwich:
    """G0 W G0 with signed 2-by-2 modal entries and stable endpoint moments.

    W is the ENTIRE same-point signed matrix, before any magnitude. It may be
    chi^2 E or the compact WJK factor chi*chi_prime*I+chi^2 E.
    All64 high modes97..160 and both normalized real parities are retained.
    The result is an exact-function enclosure, not an operator-norm bound.

    pair(m,n) deliberately does NOT retain all4096 pair states. The owner
    chooses an explicit bounded batch and its sweep order. This avoids an
    unannounced multi-million-scalar cache. Releasing a private pair state
    never releases a completed scientific target.
    """
    def __init__(self, profiles, weight, kernel_api, label):
        self.profiles,self.domain,self.api=profiles,profiles.domain,profiles.api
        self.km,self.label,self.weight=kernel_api,label,weight
        self.modes=HIGH_MODES
        self.coords=_coordinates(self.modes,False)
        self.position={v:i for i,v in enumerate(self.coords)}
        require(weight.domain is self.domain and
                (weight.rows,weight.cols)==(128,128) and
                set(self.modes).issubset(profiles.mode),
                "complete raw high128 sandwich factor on fixed WVC")
        self.weight_cache={}

    def _weight(self,box):
        key=self.domain.cache_key(box)
        if key not in self.weight_cache:
            self.weight_cache[key]=self.weight.at(box)
        return self.weight_cache[key]

    def contractions(self,m,n,box):
        """C=Jm W Un, A=Jm W Fn, B=Lm W Un, D=Lm W Fn."""
        matrix=self._weight(box)
        pm,pn=self.profiles.at(m,box),self.profiles.at(n,box)
        mi,me=self.position[(0,m)],self.position[(1,m)]
        ni,ne=self.position[(0,n)],self.position[(1,n)]
        w=((matrix.values[mi][ni],matrix.values[mi][ne]),
           (matrix.values[me][ni],matrix.values[me][ne]))
        def bilinear(left,right):
            return left[0]*(w[0][0]*right[0]+w[0][1]*right[1])+\
                   left[1]*(w[1][0]*right[0]+w[1][1]*right[1])
        J=(-pm["H"],pm["K"]);L=(self.api.one,pm["p"])
        U=(pn["K"],pn["H"]);F=(-pn["p"],self.api.one)
        return (bilinear(J,U),bilinear(J,F),bilinear(L,U),bilinear(L,F))

    def pair(self,m,n):
        require(type(m) is int and type(n) is int and m in self.modes and n in self.modes,
                "complete declared high modal pair")
        return _StableModalSandwichPair(self,m,n)


class _StableModalSandwichPair:
    """One pair's O(number of panels) signed prefix/suffix and transfer data.

    For l<u, A(l,u)=int_l^u Dm(t,u) Dn(l,t) Afield(t)dt,
    B(l,u)=int_l^u Dm(l,t) Dn(t,u) Bfield(t)dt.
    Concatenation has no division:
      A(l,u)=Dm(v,u)A(l,v)+A(v,u)Dn(l,v),
      B(l,u)=Dn(v,u)B(l,v)+B(v,u)Dm(l,v).
    Its two diagonal entries are true decays, including exact identity at
    the root cell. No global g times an independently enclosed g_inverse
    is ever formed.
    """
    def __init__(self,parent,m,n):
        self.parent,self.m,self.nmode=parent,m,n
        self.profiles,self.domain,self.api,self.km=\
            parent.profiles,parent.domain,parent.api,parent.km
        self.count=len(self.domain.cells)
        self.full={}
        self.prefix=[None]*(self.count+1)
        self.suffix=[None]*(self.count+1)
        self.prefix[0]=self.api.zero
        self.suffix[self.count]=self.api.zero
        self.prefix_count,self.suffix_count=0,self.count
        self.range_cache={}

    def _rates(self,box):
        ml,mu=_complete_rate_bounds(self.profiles,self.m,box)
        nl,nu=_complete_rate_bounds(self.profiles,self.nmode,box)
        return ml,mu,nl,nu

    def _full(self,i):
        if i not in self.full:
            box=self.domain.whole_cell_box(i)
            length=self.domain.full_length(i)
            ml,mu,nl,nu=self._rates(box)
            C,A,B,D=self.parent.contractions(self.m,self.nmode,box)
            common=_complete_decay_mass(self.api,ml+nl,mu+nu,length)
            middle=_complete_two_decay_mass(self.api,ml,mu,nl,nu,length)
            dm=self.profiles.mode[self.m]["tau"][i]
            dn=self.profiles.mode[self.nmode]["tau"][i]
            # Full C and D are separate exact oriented integrals. Their
            # shared mass enclosure is a comparison, not an equality claim.
            self.full[i]=(dm,dn,middle*A,middle*B,common*C,common*D)
        return self.full[i]

    def _before(self,i):
        require(0<=i<=self.count,"complete pair prefix boundary")
        while self.prefix_count<i:
            k=self.prefix_count
            dm,dn,_,_,C,_=self._full(k)
            self.prefix[k+1]=dm*dn*self.prefix[k]+C
            self.prefix_count+=1
        return self.prefix[i]

    def _after(self,i):
        require(0<=i<=self.count,"complete pair suffix boundary")
        while self.suffix_count>i:
            k=self.suffix_count-1
            dm,dn,_,_,_,D=self._full(k)
            self.suffix[k]=D+dm*dn*self.suffix[k+1]
            self.suffix_count-=1
        return self.suffix[i]

    def _C(self,box):
        i=self.domain.cell_index(box);cell=self.domain.whole_cell_box(i)
        endpoint=(i,cell[1],cell[1])
        dm=self.profiles.ordered_decay(self.m,endpoint,box)
        dn=self.profiles.ordered_decay(self.nmode,endpoint,box)
        part=self.domain.partial_box(box,"prefix")
        ml,mu,nl,nu=self._rates(part)
        length=self.domain.partial_length(box,"prefix")
        value=self.parent.contractions(self.m,self.nmode,part)[0]
        return dm*dn*self._before(i)+\
            _complete_decay_mass(self.api,ml+nl,mu+nu,length)*value

    def _D(self,box):
        i=self.domain.cell_index(box);cell=self.domain.whole_cell_box(i)
        endpoint=(i,cell[2],cell[2])
        dm=self.profiles.ordered_decay(self.m,box,endpoint)
        dn=self.profiles.ordered_decay(self.nmode,box,endpoint)
        part=self.domain.partial_box(box,"suffix")
        ml,mu,nl,nu=self._rates(part)
        length=self.domain.partial_length(box,"suffix")
        value=self.parent.contractions(self.m,self.nmode,part)[3]
        return _complete_decay_mass(self.api,ml+nl,mu+nu,length)*value+\
            dm*dn*self._after(i+1)

    def _identity(self):
        return self.api.one,self.api.one,self.api.zero,self.api.zero

    def _join(self,first,second):
        """The first interval is followed by the second; their order is fixed."""
        am,an,aA,aB=first;bm,bn,bA,bB=second
        return bm*am,bn*an,bm*aA+bA*an,bn*aB+bB*am

    def _range(self,left,right):
        """Balanced ordered full-cell product, with only O(n) cached tree nodes."""
        require(type(left) is int and type(right) is int
                and 0<=left<=right<=self.count,"complete full-cell pair range")
        if left==right:
            return self._identity()
        def node(a,b):
            key=(a,b)
            if key not in self.range_cache:
                if b-a==1:
                    self.range_cache[key]=self._full(a)[:4]
                else:
                    mid=(a+b)//2
                    self.range_cache[key]=self._join(node(a,mid),node(mid,b))
            return self.range_cache[key]
        def query(a,b):
            if right<=a or b<=left:
                return self._identity()
            if left<=a and b<=right:
                return node(a,b)
            mid=(a+b)//2
            return self._join(query(a,mid),query(mid,b))
        return query(0,self.count)

    def _partial(self,left,right):
        box,length=self.domain.ordered_span(left,right)
        if _upper(self.api,length)==0:
            return self._identity()
        dm=self.profiles.ordered_decay(self.m,left,right)
        dn=self.profiles.ordered_decay(self.nmode,left,right)
        ml,mu,nl,nu=self._rates(box)
        _,A,B,_=self.parent.contractions(self.m,self.nmode,box)
        mass=_complete_two_decay_mass(self.api,ml,mu,nl,nu,length)
        return dm,dn,mass*A,mass*B

    def between(self,left,right):
        self.domain.validate_box(left);self.domain.validate_box(right)
        li,ri=self.domain.cell_index(left),self.domain.cell_index(right)
        require(li<=ri,"ordered full modal-pair interval")
        if li==ri:
            return self._partial(left,right)
        lc,rc=self.domain.whole_cell_box(li),self.domain.whole_cell_box(ri)
        first=self._partial(left,(li,lc[2],lc[2]))
        middle=self._range(li+1,ri)
        last=self._partial((ri,rc[1],rc[1]),right)
        return self._join(self._join(first,middle),last)

    def kernel(self,r,s,orientation):
        """Whole signed 2-by-2 block of G0 W G0; no magnitude or norm."""
        require(orientation in (-1,0,1),"complete ordered radial triangles")
        if orientation==0:
            return self.km.hull(self.api,self.kernel(r,s,1),self.kernel(r,s,-1))
        p,q=self.profiles.at(self.m,r),self.profiles.at(self.nmode,s)
        F=(-p["p"],self.api.one);U=(p["K"],p["H"])
        L=(self.api.one,q["p"]);J=(-q["H"],q["K"])
        def term(v,w,c):
            return self.km.Matrix(2,2,[[c*v[i]*w[j] for j in range(2)] for i in range(2)])
        if orientation==1:
            dm,dn,A,_=self.between(s,r)
            return self.km.add(self.api,
                term(F,L,-dm*self._C(s)),
                term(F,J,A),
                term(U,J,-dn*self._D(r)))
        dm,dn,_,B=self.between(r,s)
        return self.km.add(self.api,
            term(F,L,-dn*self._C(r)),
            term(U,L,B),
            term(U,J,-dm*self._D(s)))

    def raw_reference_kernel(self,r,s,orientation):
        """Diagonal original G0 block, including its exact inter-mode zeros."""
        if self.m!=self.nmode:
            return self.km.zeros(self.api,2,2)
        if orientation==0:
            return self.km.hull(self.api,
                self.raw_reference_kernel(r,s,1),self.raw_reference_kernel(r,s,-1))
        require(orientation in (-1,1),"true raw reference triangle")
        p,q=self.profiles.at(self.m,r),self.profiles.at(self.m,s)
        if orientation==1:
            decay=self.profiles.ordered_decay(self.m,s,r)
            return self.km.Matrix(2,2,[
                [decay*p["p"]*q["H"],-decay*p["p"]*q["K"]],
                [-decay*q["H"],decay*q["K"]]])
        decay=self.profiles.ordered_decay(self.m,r,s)
        return self.km.Matrix(2,2,[
            [-decay*p["K"],-decay*p["K"]*q["p"]],
            [-decay*p["H"],-decay*p["H"]*q["p"]]])

    def factored_WJK_body_kernel(self,r,s,orientation,chi):
        """Same Fbb when the parent W is exactly chi*chi_prime I+chi^2 E.

        This identity is used only for the WHOLE joint signed centre.
        No derivative term is removed from the primal or dual residual.
        All exterior Bc/BLHc and the common Gf/atoms still belong to the caller.
        """
        xr,xs=chi(r),chi(s)
        first=self.km.scale(self.api,(2*xr-xr*xr*xr)*xs,
                           self.raw_reference_kernel(r,s,orientation))
        second=self.km.scale(self.api,xr*xs,self.kernel(r,s,orientation))
        return self.km.add(self.api,first,second)
