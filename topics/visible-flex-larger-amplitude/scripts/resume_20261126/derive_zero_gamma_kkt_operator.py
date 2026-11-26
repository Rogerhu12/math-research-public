"""Pure source derivation; never imports or executes a scientific module."""
import ast
import hashlib
from pathlib import Path
import re
import argparse

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo', type=Path, required=True)
p.add_argument('--new-input-binder-source', type=Path, required=True)
p.add_argument('--outdir', type=Path, required=True)
args = p.parse_args()
HERE = args.outdir.resolve()
PARENT = args.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_zero_moment_continuation_operator.py'
PARENT_SHA = '3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a'
EXPECTED_BINDER_SHA = 'ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39'
EXPECTED_OUTPUT_SHA = 'b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a'
source = PARENT.read_text()
assert hashlib.sha256(source.encode()).hexdigest() == PARENT_SHA
original = source
BINDER_PATH = args.new_input_binder_source.resolve()
BINDER_SHA = hashlib.sha256(BINDER_PATH.read_bytes()).hexdigest()
assert BINDER_SHA == EXPECTED_BINDER_SHA
HERE.mkdir(parents=True, exist_ok=True)


def replace_once(old, new):
    global source
    assert source.count(old) == 1, (old[:120], source.count(old))
    source = source.replace(old, new)


def node_text(name, *, method=True):
    tree = ast.parse(source)
    nodes = (next(n for n in tree.body if isinstance(n, ast.ClassDef)
                  and n.name == 'ZeroClosureOperator').body if method else tree.body)
    node = next(n for n in nodes if getattr(n, 'name', None) == name)
    lines = source.splitlines(keepends=True)
    first = min([node.lineno]+[n.lineno for n in getattr(node, 'decorator_list', [])])
    return ''.join(lines[first-1:node.end_lineno])


def replace_node(name, text, *, method=True):
    replace_once(node_text(name, method=method), text.rstrip()+'\n')


first_doc = ast.parse(source).body[0]
old_doc = ''.join(source.splitlines(keepends=True)[first_doc.lineno-1:first_doc.end_lineno])
replace_once(old_doc, '''"""Complete added-gamma six-control, nine-KKT zero-closure SO3 field.

The same fixed scalar, frozen chart, literal Q matrices and ALL original
core/omega/H variables remain. A genuinely independent C2 gamma shape inside
the original support adds three WORLD axial controls. The selected numerical
KKT stationary branch has six dimensionless controls and three multipliers;
its angular second-jet implicit system is 27 dimensional, not the old nine.
The full first parameter J/J* retains every multiplier and mixed fourth
derivative. Numerical continuation is detached and is not a physical flex.

Stationarity, numerical closure and numerical small-matrix singular values
are not SOSC, global-minimum, continuous-branch, metric or geometry proofs.
All scientific calls require the public repository Actions environment.
"""\n''')
replace_once("SCHEMA = 'complete-direct-R690-frozen-Q-residual-continuation-zero-endpoint-layer-v1'",
             "SCHEMA = 'complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1'")
replace_once("TORCH_VERSION = '2.5.1'", "TORCH_VERSION = '2.5.1'\nGAMMA_KKT_DERIVED_FROM_CONTINUATION_SHA256 = '"+PARENT_SHA+"'\nCONTROL_DIMENSION = 6\nKKT_DIMENSION = 9")

replace_node('EndpointPolicy', r'''
@dataclass(frozen=True)
class EndpointPolicy:
    endpoint_tolerance: float = 2.e-12
    kkt_tolerance: float = 2.e-12
    maximum_iterations: int = 24
    maximum_backtracks: int = 18
    armijo: float = 1.e-4
    control_radius: float = 2.
    multiplier_radius: float = 64.

    def __post_init__(self):
        for name in ('endpoint_tolerance', 'kkt_tolerance', 'armijo',
                     'control_radius', 'multiplier_radius'):
            value = float(getattr(self, name))
            if not math.isfinite(value) or value <= 0:
                raise ValueError('Use explicit finite positive KKT numerical parameters: '+name)
            object.__setattr__(self, name, value)
        if self.armijo >= 1:
            raise ValueError('The numerical KKT residual decrease factor must be below one')
        for name in ('maximum_iterations', 'maximum_backtracks'):
            value = int(getattr(self, name))
            if value != getattr(self, name) or value < 1:
                raise ValueError('Use an explicit positive KKT stage budget: '+name)
            object.__setattr__(self, name, value)

    def metadata(self):
        return dict(schema='complete-six-control-nine-KKT-numerical-policy-v1',
            endpoint_tolerance=self.endpoint_tolerance,
            kkt_tolerance=self.kkt_tolerance,
            maximum_iterations=self.maximum_iterations,
            maximum_backtracks=self.maximum_backtracks, armijo=self.armijo,
            control_radius=self.control_radius, multiplier_radius=self.multiplier_radius,
            control='u=(z/S,v); six dimensionless entries, including every new gamma axis',
            multiplier='ell: three dimensionless equality multipliers',
            merit='Euclidean norm of all nine dimensionless KKT equations',
            stage_tolerance='min(kkt_tolerance, endpoint_tolerance / actual S carrier)',
            final_acceptance='fresh ORIGINAL KKT norm <= kkt_tolerance AND physical closure norm <= endpoint_tolerance AND both declared open domains',
            domains='|u| < control_radius and |ell| < multiplier_radius; independent new algorithmic domains',
            old_three_coordinate_radius_or_IFT_ball_inherited=False,
            initial_root='literal u=ell=0 independently for every new angle/full point at continuation_parameter=0',
            actual_root_failure='reject this candidate; no failed root or multiplier is replaced by zero',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, continuous_branch_certified=False,
            root_iteration_graph_differentiated=False)
''', method=False)

continuation = node_text('EndpointContinuationPolicy', method=False)
continuation = continuation.replace("schema='fixed-final-endpoint-residual-continuation-policy-v1'",
                                    "schema='fixed-final-nine-KKT-residual-continuation-policy-v1'")
continuation = continuation.replace("equation='H(z,lambda;x,phi)=C(z;x,phi)-(1-lambda)*C(0;x,phi)'",
    "equation='R(Y; x,phi) - (1-continuation_parameter)*(0_6,f(x,0,phi)) = 0'")
continuation = continuation.replace("origin='lambda=0,z=0 at the SAME fixed original x,phi,Q'",
    "origin='continuation_parameter=0,u=ell=0 at the SAME x,phi,Q,gamma'")
continuation = continuation.replace("target='lambda=1 and a fresh read of the ORIGINAL C(z;x,phi)=0'",
    "target='continuation_parameter=1 and a fresh ORIGINAL KKT plus physical closure read'")
continuation = continuation.replace("rejected_stage='restore the exact last accepted z and lambda, then shrink the lambda step'",
    "rejected_stage='restore the exact last accepted full Y=(u,ell) and continuation_parameter, then shrink its step'")
continuation = continuation.replace("corrector='same complete C/Cz and original per-stage Newton/Armijo/ball policy'",
    "corrector='complete nine-KKT residual and Hessian/Jacobian with declared Newton/Armijo/control/multiplier domains'")
continuation = continuation.replace("implicit_derivatives_use_final_original_equation=True,",
    "implicit_derivatives_use_final_original_equation=True,\n            final_angular_implicit_dimension=27, auxiliary_parameter_is_README_physical_flex=False,")
replace_node('EndpointContinuationPolicy', continuation, method=False)

init = node_text('__init__')
init = init.replace('bubble_nodes, frozen_moment_input, endpoint_policy=None, continuation_policy=None):',
    "bubble_nodes, frozen_moment_input, gamma_nodes=('1/16', '1/8', '3/16'),\n                 endpoint_policy=None, continuation_policy=None):")
init = init.replace('        self._frozen_Q0 = tensor(frozen_matrices)\n', '''        self._frozen_Q0 = tensor(frozen_matrices)
        self.gamma_nodes = tuple(Fraction(value) for value in gamma_nodes)
        if (len(self.gamma_nodes) != 3
                or not 0 < self.gamma_nodes[0] < self.gamma_nodes[1] < self.gamma_nodes[2] < 1):
            raise ValueError('Specify a complete strictly ordered exact relative gamma triple')
        if not any(row[0] < self.gamma_nodes[0] < self.gamma_nodes[2] < row[2]
                   for row in self.bubble_nodes):
            raise ValueError('The complete gamma support must lie strictly inside one original support')
        self._gamma_query_cache = {}
        self.kkt_counts = dict(KKT_angle_evaluations=0, KKT_matrix_angle_evaluations=0,
            closure_jet_angle_evaluations=0, stationarity_reverse_products=0,
            jet_constraint_angle_evaluations=0, actual_nine_dimensional_solves=0,
            actual_implicit_matrix_rows=0)
        self.maximum_kkt_root_residual = 0.
        self.maximum_multiplier_norm = 0.
''')
init = init.replace("field='Pcap + integral_S^s Exp((W z(phi0)) cross) Exp(omega cross) T0; C(y,z)=0'",
    "field='Pcap + integral_S^s Exp((S W zeta(phi0)+gamma v(phi0)) cross) Exp(omega cross) T0; full nine-KKT selects controls'")
init = init.replace('correction_dimension=3, original_bubble_axis_controls=6,', '''correction_dimension=6, original_bubble_axis_controls=6,
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            complete_second_angular_implicit_dimension=27,
            exact_relative_gamma_nodes=[str(value) for value in self.gamma_nodes],
            gamma='independent C2 S5 rise/fall shape strictly inside an original support; zero outside',
            implicit_control_cost='(|z/S|^2+|v|^2)/2',
            dimensionless_controls='u=(z/S,v); actual world rotation is [S W,gamma I] u',
            dimensionless_constraint='f=(Gamma-Pcap+integral corrected_T)/S',
            KKT_residual='(u+f_u^T ell,f)',
            KKT_jacobian='[[I+sum ell_i f_i,uu, f_u^T],[f_u,0]]',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False,
            old_admissible_control_family_included_at_v_zero=True,
            old_selected_root_or_field_inherited=False,
            gamma_support_does_not_enlarge_original_support_union=True,''')
init = init.replace("correction_matrix='W=sum_i beta_i(s) Rz(theta0) Q_i0 Rz(theta0)^T'",
    "correction_matrix='B=[S*sum_i beta_i(s) Rz(theta0) Q_i0 Rz(theta0)^T, gamma(s)*I3]'")
init = init.replace("root_numerical_method='detached residual continuation to the SAME final endpoint equation'",
    "root_numerical_method='detached per-angle residual continuation to the full final nine-KKT stationary system and physical closure'")
init = init.replace("root_branch='numerical continuation from lambda=0,z=0 inside the same open ball; exact existence, uniqueness and cross-angle association remain unproved'",
    "root_branch='same-seed per-angle continuation_parameter in [0,1] with explicit NEW control/multiplier domains; exact branch and cross-angle association unproved'")
init = init.replace("root_branch_radius_hex=float(self.policy.branch_radius).hex(),", '''root_control_radius_hex=float(self.policy.control_radius).hex(),
            root_multiplier_radius_hex=float(self.policy.multiplier_radius).hex(),
            root_KKT_policy=self.policy.metadata(),
            new_KKT_implementation_derived_from_continuation_sha256=GAMMA_KKT_DERIVED_FROM_CONTINUATION_SHA256,''')
replace_node('__init__', init)

replace_node('_W', r'''
    def _gamma_values(self, query):
        key = array_sha(np.asarray(query['s']))
        if key not in self._gamma_query_cache:
            s = np.asarray(query['s'], dtype=float)
            a, c, b = [float(value)*self.S for value in self.gamma_nodes]
            if not 0 < a < c < b < self.S:
                raise ValueError('The actual gamma carrier loses its complete strict order')
            value, derivative = np.zeros_like(s), np.zeros_like(s)
            for left, right, rising in ((a, c, True), (c, b, False)):
                mask = (s >= left)&(s <= right)
                u = (s[mask]-left)/(right-left)
                S5 = 10*u**3-15*u**4+6*u**5
                D5 = (30*u*u-60*u**3+30*u**4)/(right-left)
                value[mask] = S5 if rising else 1-S5
                derivative[mask] = D5 if rising else -D5
            self._gamma_query_cache[key] = (tensor(value), tensor(derivative))
        return self._gamma_query_cache[key]

    def _W(self, query, phi):
        theta, rho, rhop, er, et = self._chart(phi)
        bubbles, slopes, _ = self._bubble_values(query)
        zero = torch.zeros_like(theta)
        ez = torch.stack((zero, zero, torch.ones_like(theta)), -1)
        frame = torch.stack((er, et, ez), dim=-1)
        Q = torch.stack(tuple(frame@self._frozen_Q0[i]@frame.transpose(-1, -2)
                              for i in range(2)))
        old = sum(bubbles[i, :, None, None, None]*Q[i][None] for i in range(2))
        old_s = sum(slopes[i, :, None, None, None]*Q[i][None] for i in range(2))
        Z = hat(tensor([0., 0., 1.]))
        commutator = Z@old-old@Z
        old_p = rho[None, :, None, None]*commutator
        old_pp = (rhop[None, :, None, None]*commutator
            +rho[None, :, None, None]**2*(Z@commutator-commutator@Z))
        gamma, gamma_s = self._gamma_values(query)
        eye = torch.eye(3, dtype=torch.float64)
        g = (gamma[:, None, None, None]*eye[None, None]).expand(-1, len(phi), -1, -1)
        gs = (gamma_s[:, None, None, None]*eye[None, None]).expand(-1, len(phi), -1, -1)
        zeros = torch.zeros_like(g)
        # Existing W keys retain their physical-jet meaning; each value is
        # now the complete 3x6 B matrix for u=(z/S,v), not an old 3x3 W.
        return dict(W=torch.cat((self.S*old, g), dim=-1),
            Ws=torch.cat((self.S*old_s, gs), dim=-1),
            Wp=torch.cat((self.S*old_p, zeros), dim=-1),
            Wpp=torch.cat((self.S*old_pp, zeros), dim=-1))
''')

replace_node('_C0', r'''
    def _closure_jets(self, controls, data, order):
        corrected = self._corrected_jets(data['meridians'], data['W'], controls, order)
        names = ('T', 'Tp', 'Tpp')
        self.kkt_counts['closure_jet_angle_evaluations'] += len(controls)
        return torch.stack(tuple((data['core'][j]-data['cap'][j]
            +self._total(corrected[names[j]]))/self.S
            for j in range(order+1)), dim=1)
''')
replace_node('_constraints', r'''
    def _constraints(self, Yjets, data, order):
        """All nine KKT equations and their COMPLETE total angular jets.

        If g_j is the j-th physical closure jet, d g_j / d u0 is the
        j-th total angular derivative of f_u, with u1/u2 independent.
        Its graph MUST retain the original parameter and multiplier chains.
        The enclosing numerical solve may detach the returned VALUES only.
        """
        if (order not in (0, 1, 2) or Yjets.ndim != 3
                or Yjets.shape[-1] != KKT_DIMENSION or Yjets.shape[1] < order+1):
            raise ValueError('Use complete nine-component KKT jets of the declared order')
        outer_grad_enabled = torch.is_grad_enabled()
        with torch.enable_grad():
            controls = Yjets[:, :order+1, :CONTROL_DIMENSION]
            if not controls.requires_grad:
                # A local independent control leaf is needed to EVALUATE
                # f_u even during no-grad Newton. It never detaches data/y.
                controls = controls.detach().clone().requires_grad_(True)
            multipliers = Yjets[:, :order+1, CONTROL_DIMENSION:]
            closure = self._closure_jets(controls, data, order)
            residuals = []
            for j in range(order+1):
                scalar = sum(math.comb(j, k)*(closure[:, j-k]*multipliers[:, k]).sum()
                             for k in range(j+1))
                gradient, = torch.autograd.grad(scalar, controls,
                    create_graph=True, retain_graph=True, allow_unused=False)
                stationarity = controls[:, j]+gradient[:, 0]
                residuals.append(torch.cat((stationarity, closure[:, j]), dim=-1))
                self.kkt_counts['stationarity_reverse_products'] += len(Yjets)
            result = torch.stack(residuals, dim=1)
        self.kkt_counts['jet_constraint_angle_evaluations'] += len(Yjets)
        return result if outer_grad_enabled else result.detach()

    def _K0(self, state, data):
        self.kkt_counts['KKT_angle_evaluations'] += len(state)
        return self._constraints(state[:, None, :], data, 0)[:, 0]

    def _inside_domain(self, state):
        return (torch.isfinite(state).all(-1)
            &(torch.linalg.vector_norm(state[:, :CONTROL_DIMENSION], dim=-1)<self.policy.control_radius)
            &(torch.linalg.vector_norm(state[:, CONTROL_DIMENSION:], dim=-1)<self.policy.multiplier_radius))

    def _stage_tolerance(self):
        return min(self.policy.kkt_tolerance, self.policy.endpoint_tolerance/self.S)
''')
replace_node('_C0_jacobian', r'''
    def _K0_jacobian(self, state, data):
        with torch.enable_grad():
            local = state.detach().clone().requires_grad_(True)
            value = self._K0(local, data)
            rows = [torch.autograd.grad(value[:, j].sum(), local,
                retain_graph=j < KKT_DIMENSION-1, create_graph=False)[0]
                for j in range(KKT_DIMENSION)]
            result = torch.stack(rows, dim=1).detach()
        self.kkt_counts['KKT_matrix_angle_evaluations'] += len(state)
        self.kkt_counts['actual_implicit_matrix_rows'] += KKT_DIMENSION*len(state)
        if not bool(torch.isfinite(result).all()):
            raise EndpointRootFailure('Nonfinite complete nine-dimensional KKT Hessian/Jacobian')
        return result
''')
replace_node('_jet_jacobian', r'''
    def _jet_jacobian(self, Yjets, data, order):
        size = KKT_DIMENSION*(order+1)
        with torch.enable_grad():
            local = Yjets[:, :order+1].detach().clone().requires_grad_(True)
            value = self._constraints(local, data, order).reshape(len(local), size)
            rows = [torch.autograd.grad(value[:, j].sum(), local,
                retain_graph=j < size-1, create_graph=False)[0].reshape(len(local), size)
                for j in range(size)]
            result = torch.stack(rows, dim=1).detach()
        if not bool(torch.isfinite(result).all()):
            raise EndpointRootFailure('Nonfinite COMPLETE 9/18/27 KKT angular-jet Jacobian')
        self.endpoint_counts['implicit_jacobian_blocks'] += len(Yjets)
        self.kkt_counts['actual_implicit_matrix_rows'] += size*len(Yjets)
        return result
''')

# Continuation and publication bodies are added by the second source-only
# section below. No numerical module is imported by this derivation.

replace_node('_fail', r'''
    def _fail(self, reason, *, residual=None, state=None, angles=None, physical_endpoint=None):
        self.endpoint_counts['root_failures'] += 1
        finite = lambda value: float(value) if math.isfinite(float(value)) else None
        record = dict(schema='actual-added-gamma-nine-KKT-root-failure-v1',
            reason=str(reason), current_full_point_sha256=self._current_point_sha256,
            root_policy=self.policy.metadata(),
            continuation_policy=self.continuation_policy.metadata(),
            continuation_summary=self._continuation_summary(),
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            failed_candidate_is_not_an_accepted_field=True,
            failed_root_replaced_by_zero=False,
            SOSC_verified=False, global_minimum_verified=False,
            uniform_IFT_failure_or_nonexistence_claimed=False)
        if residual is not None:
            record['maximum_actual_dimensionless_KKT_residual'] = finite(residual)
        if physical_endpoint is not None:
            record['maximum_actual_physical_endpoint_residual'] = finite(physical_endpoint)
        if state is not None:
            value = state.detach().cpu().numpy() if isinstance(state, torch.Tensor) else np.asarray(state)
            if value.ndim != 2 or value.shape[1] != KKT_DIMENSION:
                raise ValueError('Failure records must retain every control and multiplier')
            record['actual_states'] = [[finite(v) for v in row] for row in value]
            record['actual_states_binary64_hex'] = [
                [float(v).hex() if math.isfinite(float(v)) else None for v in row] for row in value]
            record['state_component_order'] = ['zeta_x','zeta_y','zeta_z',
                'v_x','v_y','v_z','ell_x','ell_y','ell_z']
        if angles is not None:
            record['failed_angle_indices'] = [int(v) for v in angles]
            record['failed_angle_count'] = len(angles)
        self._last_root_failure = record
        raise EndpointRootFailure(json.dumps(record, sort_keys=True, separators=(',', ':'),
                                             allow_nan=False))
''')

for name, old, new in (
        ('_continuation_value', 'self._C0(z, data)', 'self._K0(z, data)'),
        ('_continuation_jacobian', 'self._C0_jacobian(z, data)', 'self._K0_jacobian(z, data)')):
    body = node_text(name)
    assert body.count(old) == 1
    replace_node(name, body.replace(old, new))

corrector = node_text('_continuation_corrector')
corrector = re.sub(r'\bz\b', 'state', corrector)
corrector = corrector.replace('Same complete C and C_z, with a fixed residual offset for this stage.',
    'Complete original nine-KKT equations with only the endpoint residual offset.')
corrector = corrector.replace('(state,lambda)', '(state,continuation_parameter)')
corrector = corrector.replace('original open branch ball', 'declared control and multiplier domains')
corrector = corrector.replace('untouched 3/6/9 implicit derivative chain', 'complete new 9/18/27 KKT implicit derivative chain')
corrector = corrector.replace('self.policy.tolerance', 'self._stage_tolerance()')
corrector = corrector.replace("                try:\n                    direction[j] = torch.linalg.solve(matrix[j], value[j, :, None])[:, 0]",
    "                try:\n                    self.kkt_counts['actual_nine_dimensional_solves'] += 1\n                    direction[j] = torch.linalg.solve(matrix[j], value[j, :, None])[:, 0]")
corrector = corrector.replace('admissible = (candidate_norm < self.policy.branch_radius) & torch.isfinite(candidate).all(-1)',
    'admissible = self._inside_domain(candidate)')
corrector = corrector.replace('inside = torch.linalg.vector_norm(state, dim=-1) < self.policy.branch_radius',
    'inside = self._inside_domain(state)')
corrector = corrector.replace('original ball', 'new control/multiplier domains')
corrector = corrector.replace("correction_norm=(float(torch.linalg.vector_norm(state[j]))",
    "dimensionless_state_norm=(float(torch.linalg.vector_norm(state[j]))")
corrector = corrector.replace('last_candidate_correction_norm=last_candidate_norm[j])', '''last_candidate_state_norm=last_candidate_norm[j],
            dimensionless_control_norm=(float(torch.linalg.vector_norm(state[j, :CONTROL_DIMENSION]))
                if bool(torch.isfinite(state[j]).all()) else None),
            multiplier_norm=(float(torch.linalg.vector_norm(state[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(state[j]).all()) else None),
            stationarity_norm=(float(torch.linalg.vector_norm(final[j, :CONTROL_DIMENSION]))
                if bool(torch.isfinite(final[j]).all()) else None),
            physical_auxiliary_endpoint_norm=(float(self.S*torch.linalg.vector_norm(final[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(final[j]).all()) else None),
            state_values=[float(v) if math.isfinite(float(v)) else None for v in state[j]],
            nine_KKT_values=[float(v) if math.isfinite(float(v)) else None for v in final[j]])''')
replace_node('_continuation_corrector', corrector)

roots = node_text('_solve_roots')
roots = re.sub(r'\bz\b', 'state', roots)
roots = roots.replace('lambda', 'continuation_parameter')
roots = roots.replace('Detached residual continuation, ending at the original C(state)=0.',
    'Detached residual continuation, ending at the original NINE KKT equations.')
roots = roots.replace('Auxiliary continuation_parameter is neither the physical flex parameter nor a changed',
    'The auxiliary continuation_parameter is neither the README physical flex nor a changed')
roots = roots.replace("schema='actual-same-endpoint-equation-residual-continuation-batch-v1'",
    "schema='actual-added-gamma-nine-KKT-residual-continuation-batch-v1'")
roots = roots.replace('torch.zeros((count, 3), dtype=torch.float64)',
    'torch.zeros((count, KKT_DIMENSION), dtype=torch.float64)')
roots = roots.replace('self.policy.tolerance', 'self._stage_tolerance()')
roots = roots.replace("            anchor = self._continuation_value(state, data).detach()\n", '''            anchor = self._continuation_value(state, data).detach()
            if bool((anchor[:, :CONTROL_DIMENSION] != 0).any()):
                self._fail('The zero-control/zero-multiplier KKT origin has nonzero stationarity', state=state)
''')
roots = roots.replace("log['initial_endpoint_residual_norms'] = [\n                float(norm0[j]) if bool(torch.isfinite(norm0[j])) else None for j in range(count)]", '''log['initial_endpoint_residual_norms'] = [
                float(self.S*torch.linalg.vector_norm(anchor[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(anchor[j]).all()) else None for j in range(count)]
            log['initial_dimensionless_KKT_residual_norms'] = [
                float(norm0[j]) if bool(torch.isfinite(norm0[j])) else None for j in range(count)]''')
roots = roots.replace("correction=float(torch.linalg.vector_norm(state, dim=-1).max()),", "state=state,")
roots = roots.replace("                                tangent = torch.linalg.solve(matrix[j], -anchor[j, :, None])[:, 0]",
    "                                self.kkt_counts['actual_nine_dimensional_solves'] += 1\n                                tangent = torch.linalg.solve(matrix[j], -anchor[j, :, None])[:, 0]")
roots = roots.replace("and float(torch.linalg.vector_norm(candidate)) < self.policy.branch_radius):",
    "and bool(self._inside_domain(candidate[None])[0])):")
roots = roots.replace('inside = torch.linalg.vector_norm(state, dim=-1) < self.policy.branch_radius',
    'inside = self._inside_domain(state)')
roots = roots.replace('original ball', 'new control/multiplier domains')
roots = roots.replace('3/6/9', '9/18/27')
finish_start = roots.index('        if (not log[\'all_final_parameters_reached_one\']')
roots = roots[:finish_start]+r'''        physical_norm = self.S*torch.linalg.vector_norm(final_value[:, CONTROL_DIMENSION:], dim=-1)
        stationarity_norm = torch.linalg.vector_norm(final_value[:, :CONTROL_DIMENSION], dim=-1)
        if (not log['all_final_parameters_reached_one']
                or not bool(torch.isfinite(final_norm).all())
                or not bool(torch.isfinite(physical_norm).all())
                or bool((final_norm > self.policy.kkt_tolerance).any())
                or bool((physical_norm > self.policy.endpoint_tolerance).any())
                or not bool(inside.all())):
            self._fail('Returned continuation candidate has unpaid ORIGINAL KKT, physical closure or declared domain',
                residual=float(final_norm.max()), state=state,
                physical_endpoint=float(physical_norm.max()))
        log['final_original_equation_checked'] = True
        try:
            K = self._continuation_jacobian(state, data)
            singular = torch.linalg.svdvals(K)[..., -1]
        except (RuntimeError, EndpointRootFailure) as error:
            self._fail('Actual final COMPLETE nine-KKT matrix read failed: '+str(error), state=state)
        if not bool(torch.isfinite(singular).all()):
            self._fail('Nonfinite actual complete KKT singular-value diagnostic', state=state)
        controls = torch.linalg.vector_norm(state[:, :CONTROL_DIMENSION], dim=-1)
        multipliers = torch.linalg.vector_norm(state[:, CONTROL_DIMENSION:], dim=-1)
        self.endpoint_counts['root_angles_solved'] += count
        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,
                                                   float(physical_norm.max()))
        self.maximum_kkt_root_residual = max(self.maximum_kkt_root_residual, float(final_norm.max()))
        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,
                                                     float(controls.max()))
        self.maximum_multiplier_norm = max(self.maximum_multiplier_norm, float(multipliers.max()))
        self.minimum_endpoint_sample_singular_value = min(self.minimum_endpoint_sample_singular_value,
                                                           float(singular.min()))
        records = [dict(numerical_endpoint_residual_norm=float(physical_norm[j]),
            numerical_KKT_residual_norm=float(final_norm[j]),
            numerical_stationarity_residual_norm=float(stationarity_norm[j]),
            numerical_normalized_endpoint_residual_norm=float(physical_norm[j]/self.S),
            dimensionless_control_norm=float(controls[j]), multiplier_norm=float(multipliers[j]),
            physical_z_norm=float(self.S*torch.linalg.vector_norm(state[j, :3])),
            gamma_axis_norm=float(torch.linalg.vector_norm(state[j, 3:6])),
            numerical_iterations=int(updates[j]),
            actual_KKT_smallest_singular_value=float(singular[j]),
            continuation_final_parameter=float(parameter[j]),
            continuation_stage_attempts=int(attempts[j]),
            continuation_accepted_stages=int(accepted_stages[j]),
            continuation_rejected_stages=int(rejected_stages[j]),
            numerical_root_tolerances_met=True,
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, uniform_IFT_conditions_verified=False,
            exact_continuous_root_certified=False) for j in range(count)]
        return state.detach(), K.detach(), records
'''
replace_node('_solve_roots', roots)

replace_node('_finish_jets', r'''
    def _finish_jets(self, data, state, K, order, existing=None):
        with torch.no_grad():
            Yjets = torch.zeros((len(state), 3, KKT_DIMENSION), dtype=torch.float64)
            Yjets[:, 0] = state
            if existing is not None:
                Yjets[:, 1] = existing[:, 1]
            else:
                first = self._constraints(Yjets, data, 1)[:, 1]
                try:
                    self.kkt_counts['actual_nine_dimensional_solves'] += len(state)
                    Yjets[:, 1] = torch.linalg.solve(K, -first[..., None])[..., 0]
                except RuntimeError as error:
                    self._fail('Actual complete first angular KKT-jet solve failed: '+str(error), state=state)
            if order == 2:
                second = self._constraints(Yjets, data, 2)[:, 2]
                try:
                    self.kkt_counts['actual_nine_dimensional_solves'] += len(state)
                    Yjets[:, 2] = torch.linalg.solve(K, -second[..., None])[..., 0]
                except RuntimeError as error:
                    self._fail('Actual complete second angular KKT-jet solve failed: '+str(error), state=state)
            if not bool(torch.isfinite(Yjets).all()):
                self._fail('Nonfinite COMPLETE control/multiplier angular jets', state=state)
            residual = self._constraints(Yjets, data, order)
            if not bool(torch.isfinite(residual).all()):
                self._fail('Nonfinite complete angular KKT residual', state=state)
            norms = torch.linalg.vector_norm(residual, dim=-1)
        # Every residual here has all six stationarity and three endpoint
        # components. A numerical jet residual is never a continuous proof.
        return Yjets.detach(), norms.detach()
''')

get_roots = node_text('_get_roots')
get_roots = get_roots.replace('size = 3*(order+1)', 'size = KKT_DIMENSION*(order+1)')
replace_node('_get_roots', get_roots)

implicit = node_text('_implicit_jet_value')
implicit = implicit.replace('6x6 or 9x9 jet constraint Jacobian at fixed original y.',
    '18x18 or 27x27 KKT jet Jacobian at fixed original y, including ALL multipliers.')
implicit = implicit.replace('correction.reshape(len(phi), order+1, 3)',
    'correction.reshape(len(phi), order+1, KKT_DIMENSION)')
replace_node('_implicit_jet_value', implicit)

fields = node_text('fields_torch')
fields = fields.replace("integrated = self._corrected_jets(data['meridians'], data['W'], Zjets, order)",
    "controls = Zjets[:, :, :CONTROL_DIMENSION]\n        integrated = self._corrected_jets(data['meridians'], data['W'], controls, order)")
fields = fields.replace('self._corrected_jets(direct, Wdirect, Zjets, order, need_s=curvature)',
    'self._corrected_jets(direct, Wdirect, controls, order, need_s=curvature)')
replace_node('fields_torch', fields)

metadata = node_text('metadata')
metadata = metadata.replace("current_maximum_endpoint_correction_norm=max((v['endpoint_correction_norm'] for v in records), default=None),", '''current_maximum_dimensionless_control_norm=max((v['dimensionless_control_norm'] for v in records), default=None),
            current_maximum_multiplier_norm=max((v['multiplier_norm'] for v in records), default=None),
            current_maximum_KKT_residual=max((v['numerical_KKT_residual_norm'] for v in records), default=None),
            current_maximum_stationarity_residual=max((v['numerical_stationarity_residual_norm'] for v in records), default=None),
            current_maximum_physical_z_norm=max((v['physical_z_norm'] for v in records), default=None),
            current_maximum_gamma_axis_norm=max((v['gamma_axis_norm'] for v in records), default=None),''')
metadata = metadata.replace("current_minimum_endpoint_sample_singular_value=min((v['actual_endpoint_smallest_singular_value'] for v in records), default=None),",
    "current_minimum_KKT_sample_singular_value=min((v['actual_KKT_smallest_singular_value'] for v in records), default=None),")
metadata = metadata.replace('all_attempted_fields_maximum_successful_correction_norm=self.maximum_endpoint_correction_norm,', '''all_attempted_fields_maximum_successful_dimensionless_control_norm=self.maximum_endpoint_correction_norm,
            all_attempted_fields_maximum_successful_KKT_residual=self.maximum_kkt_root_residual,
            all_attempted_fields_maximum_successful_multiplier_norm=self.maximum_multiplier_norm,''')
metadata = metadata.replace('all_attempted_fields_minimum_sample_endpoint_singular_value=',
    'all_attempted_fields_minimum_sample_KKT_singular_value=')
metadata = metadata.replace("J_method='complete first-parameter implicit 6x6 metric / 9x9 six-jet system; value-preserving zero-residual surrogate'", '''J_method='complete first-parameter implicit 18x18 metric / 27x27 six-jet KKT system; all multipliers and constraint-Hessian derivatives retained',
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            complete_second_angular_implicit_dimension=27,
            exact_relative_gamma_nodes=[str(value) for value in self.gamma_nodes],
            implicit_control_cost='(|z/S|^2+|v|^2)/2',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, actual_KKT_counts=dict(self.kkt_counts),
            old_selected_root_or_field_inherited=False,
            maximum_required_mixed_exponential_derivative_order=4,
            rotation_coefficient_source_sha256=self.base_source_sha256,
            rotation_small_branch='z=|w|^2 < 1/4; same degree-12 A/B polynomials and their exact first/second polynomial derivatives; further mixed derivatives use their retained graph',
            unused_large_rotation_branch='same source clamps scalar z to >=1/4 before sqrt/division; no zero denominator',
            rotation_truncation_branch_seam_or_rounding_error_enclosed=False''')
metadata = metadata.replace("scope='Actual finite NEW frozen-literal-moment-Q zero candidate and complete implicit first derivatives; continuous root/quad/geometry/refinement obligations remain'",
    "scope='Actual finite NEW added-gamma six-control nine-KKT stationary candidate with complete 27-jet implicit first derivatives; continuous branch/quad/SOSC/geometry/refinement remain'")
metadata = metadata.replace("actual complete-batch direct C evaluations and separate Cz evaluations (including their internal C graph)",
    "actual complete-batch nine-KKT evaluations and separate full K matrices (including their internal retained constraint-Hessian graphs)")
replace_node('metadata', metadata)

# Historical source names and cost counters state their actual scope. A
# batched or failed linear solve is an attempted angle solve, not a proved
# successful inverse; the old three-root source is provenance only.
source = source.replace('original_implicit_root_algorithm_source_sha256=',
    'historical_original_three_root_algorithm_source_sha256=')
source = source.replace('final_implicit_J_uses_original_endpoint_equation=',
    'final_implicit_J_uses_original_KKT_equation=')
source = source.replace("right_inverse_fixed_from='one ACTUAL initial working-moment proposal, now an explicit immutable literal input'",
    "literal_Q_parameter_origin='eighteen adopted words from a historical working-moment proposal; no current inverse property assumed'")
source = source.replace('stationarity_reverse_products',
    'stationarity_reverse_angle_products')
source = source.replace('actual_nine_dimensional_solves',
    'nine_dimensional_linear_solve_angle_attempts')
source = source.replace('correction_dimension=6, original_bubble_axis_controls=6,',
    'correction_dimension=6, original_shared_control_dimension=3,\n'
    '            added_gamma_axis_control_dimension=3,')
source = source.replace('global_minimum_verified=False, actual_KKT_counts=dict(self.kkt_counts),',
    "global_minimum_verified=False, actual_KKT_counts=dict(self.kkt_counts),\n"
    "            actual_KKT_counter_scope='angle-equation and retained-graph reverse products; every attempted nine-dimensional solve counts before success, including rejected stages and failures; implicit matrix rows count all angle rows assembled',")

# Preserve only already-computed local matrices on FAILED stages. The
# matrix record carries its own state and iteration, so a later accepted
# state is never misidentified as the matrix evaluation point. No F/J/SVD
# is evaluated by this diagnostic addition.
corrector = node_text('_continuation_corrector')
corrector = corrector.replace('        last_norm = [None]*count\n',
    '        last_norm = [None]*count\n        last_matrix_record = [None]*count\n')
corrector = corrector.replace('            direction = torch.zeros_like(state)\n', '''            for j in torch.nonzero(active).flatten().tolist():
                last_matrix_record[j] = dict(
                    scope='already evaluated ORIGINAL nine-KKT Jacobian at its explicitly recorded state; not a matrix at an unlabelled later state',
                    current_full_point_sha256=self._current_point_sha256,
                    local_angle_index=j, newton_iteration=iteration,
                    continuation_parameter_target=float(target[j]),
                    state_values=[float(v) for v in state[j]],
                    shifted_stage_residual_values=[float(v) for v in value[j]],
                    matrix_values=[[float(v) for v in row] for row in matrix[j]],
                    extra_field_or_J_evaluations=0, extra_SVD_evaluations=0)
            direction = torch.zeros_like(state)
''')
corrector = corrector.replace('            actual_newton_updates=int(advances[j]), reason=reasons[j],\n',
    '            actual_newton_updates=int(advances[j]), reason=reasons[j],\n'
    '            last_evaluated_KKT_matrix=(None if bool(success[j]) else last_matrix_record[j]),\n')
replace_node('_continuation_corrector', corrector)

# An explicitly different input schema adopts the same eighteen words on
# the ACTUAL new reference. The original same-reference validator stays
# byte-for-byte intact; the independent whole-source binder owns the new
# definition and provenance contract.
replace_once("KKT_DIMENSION = 9\n", "KKT_DIMENSION = 9\n"
    "NEW_REFERENCE_INPUT_SCHEMA = 'new-reference-literal-zero-endpoint-Q-input-v1'\n"
    "NEW_REFERENCE_INPUT_BINDER_SHA256 = "+repr(BINDER_SHA)+"\n")
dispatch = r'''
def validate_control_input(value, base, bubble_nodes, new_input_binder):
    """Explicit disjoint input modes; no old current-reference guard is relaxed."""
    if isinstance(value, dict) and value.get('schema') == FROZEN_MOMENT_INPUT_SCHEMA:
        if new_input_binder is not None:
            raise ValueError('The strict original same-reference input uses its original validator')
        return validate_frozen_moment_input(value, base, bubble_nodes)
    if not isinstance(value, dict) or value.get('schema') != NEW_REFERENCE_INPUT_SCHEMA:
        raise ValueError('Declare either the original same-reference input or the explicit NEW-reference literal input')
    if new_input_binder is None:
        raise ValueError('A NEW-reference input needs its actual independently pinned complete binder')
    if sha(Path(new_input_binder.__file__).resolve()) != NEW_REFERENCE_INPUT_BINDER_SHA256:
        raise ValueError('The complete NEW-reference input binder source differs')
    for name in ('bind_to_base', 'parse_literal_Q'):
        method = getattr(new_input_binder, name)
        if sha(Path(method.__code__.co_filename).resolve()) != NEW_REFERENCE_INPUT_BINDER_SHA256:
            raise ValueError('The actual NEW-reference input validation method differs: '+name)
    identity = new_input_binder.bind_to_base(value,
        base_model=base.model,
        initial_reference_bundle_sha256=base.model['initial_reference_bundle_sha256'],
        fixed_scalar_metric_identity_sha256=base.context.scalar_identity,
        initial_full_point_sha256=array_sha(base.initial()),
        bubble_nodes=[[str(v) for v in row] for row in bubble_nodes])
    words, parsed = new_input_binder.parse_literal_Q(value)
    definition = json.loads(json.dumps(value['definition'], allow_nan=False))
    if (canonical(definition) != identity
            or identity != value.get('definition_identity_sha256')
            or definition.get('Q0_binary64_hex') != words):
        raise ValueError('The NEW-reference exact definition or eighteen literal words changed')
    matrices = np.asarray(parsed, dtype=np.float64)
    if matrices.shape != (2,3,3) or not np.isfinite(matrices).all():
        raise ValueError('The actual adopted parameter matrices must contain all eighteen finite entries')
    if any(float(matrices[i,j,k]).hex() != words[i][j][k]
            for i in range(2) for j in range(3) for k in range(3)):
        raise ValueError('The actual parameter conversion changed a canonical binary64 word')
    forbidden = ((0,0), (0,2), (1,1), (2,0), (2,2))
    if any(matrices[i,j,k] != 0 for i in range(2) for j,k in forbidden):
        raise ValueError('The adopted literal constants must retain the proved full-circle sparse parity')
    matrices.setflags(write=False)
    return definition, identity, matrices

'''
replace_once('\n@dataclass(frozen=True)\nclass EndpointPolicy:',
    '\n'+dispatch+'\n@dataclass(frozen=True)\nclass EndpointPolicy:')
replace_once('                 endpoint_policy=None, continuation_policy=None):',
    '                 endpoint_policy=None, continuation_policy=None, new_input_binder=None):')
replace_once('frozen_matrices) = validate_frozen_moment_input(frozen_moment_input, base, self.bubble_nodes)',
    'frozen_matrices) = validate_control_input(frozen_moment_input, base, self.bubble_nodes, new_input_binder)\n'
    "        self.literal_Q_input_schema = frozen_moment_input['schema']\n"
    "        self.new_reference_input_binding_source_sha256 = (NEW_REFERENCE_INPUT_BINDER_SHA256\n"
    "            if self.literal_Q_input_schema == NEW_REFERENCE_INPUT_SCHEMA else None)")
source = source.replace('frozen_moment_Q_definition=self.frozen_moment_definition,',
    'frozen_moment_Q_definition=self.frozen_moment_definition,\n'
    '            literal_Q_input_schema=self.literal_Q_input_schema,\n'
    '            new_reference_input_binding_source_sha256=self.new_reference_input_binding_source_sha256,\n'
    '            historical_reference_same_mathematical_g_claimed=False,')
for key, member in (
        ('all_attempted_fields_maximum_successful_endpoint_residual', 'maximum_endpoint_root_residual'),
        ('all_attempted_fields_maximum_successful_dimensionless_control_norm', 'maximum_endpoint_correction_norm'),
        ('all_attempted_fields_maximum_successful_KKT_residual', 'maximum_kkt_root_residual'),
        ('all_attempted_fields_maximum_successful_multiplier_norm', 'maximum_multiplier_norm')):
    replace_once(key+'=self.'+member+',',
        key+'=(self.'+member+" if self.endpoint_counts['root_angles_solved'] else None),")

# These source-only assertions do not compute fields, roots, derivatives or
# factors. They reject a partial derivation rather than silently publishing it.
assert 'self.policy.branch_radius' not in source
assert 'self.policy.tolerance' not in source
assert 'self._C0(' not in source
assert 'self._C0_jacobian(' not in source
assert 'size = 3*(order+1)' not in source
assert 'correction.reshape(len(phi), order+1, 3)' not in source
assert 'current_maximum_KKT_residual=' in source
assert 'complete_second_angular_implicit_dimension=27' in source
assert node_text('validate_frozen_moment_input', method=False) in original
source = '\n'.join(line.rstrip() for line in source.splitlines())+'\n'
tree = ast.parse(source)
compile(tree, str(HERE/'so3_zero_gamma_kkt_operator.py'), 'exec')
for node in ast.walk(tree):
    if isinstance(node, ast.Dict):
        keys = [k.value for k in node.keys if isinstance(k, ast.Constant)
                and isinstance(k.value, (str, int, float))]
        assert len(keys) == len(set(keys)), ('duplicate literal dict key', node.lineno)
out = HERE/'so3_zero_gamma_kkt_operator.py'
assert hashlib.sha256(source.encode()).hexdigest() == EXPECTED_OUTPUT_SHA
out.write_text(source)
print(len(source.encode()), hashlib.sha256(source.encode()).hexdigest())
