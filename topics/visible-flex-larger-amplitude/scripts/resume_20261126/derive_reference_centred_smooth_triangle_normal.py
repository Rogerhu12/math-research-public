#!/usr/bin/env python3
"""Pure full-source derivation of the R715 reference-centred R711 entry."""
from pathlib import Path
import argparse
import ast
import hashlib
import json

HELPER_SHA = "a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873"
HELPER_NAME = "reference_centred_smooth_triangle_calibration.py"
OLD_NORMAL_SHA = "66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68"
OLD_NORMAL = "so3_supported_smooth_triangle_normal_lift_operator.py"
NEW_NORMAL = "so3_reference_centred_smooth_triangle_normal_lift_operator.py"
OLD_SCHEMA = "complete-supported-smooth-triangle-reference-SO3-fixed-normal-plane-six-control-zero-layer-v1"
NEW_SCHEMA = "complete-R711-reference-centred-SO3-fixed-normal-plane-six-control-layer-v1"

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError("Expected one complete original source fragment: "+old[:100])
    return text.replace(old, new, 1)

def method(text, name, replacement):
    lines = text.splitlines(keepends=True)
    tree = ast.parse(text)
    cls = next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=="ZeroClosureOperator")
    node = next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==name)
    begin = min([node.lineno]+[d.lineno for d in node.decorator_list])-1
    return "".join(lines[:begin])+replacement.strip("\n")+"\n"+"".join(lines[node.end_lineno:])

DETACH = '''
    @staticmethod
    def _detach_data(data):
        return dict(meridians={k:v.detach() for k,v in data['meridians'].items()},
            core=tuple(v.detach() for v in data['core']),
            cap=tuple(v.detach() for v in data['cap']),
            W={k:v.detach() for k,v in data['W'].items()},
            reference={k:v.detach() for k,v in data['reference'].items()},
            reference_core=tuple(v.detach() for v in data['reference_core']),
            reference_cap=tuple(v.detach() for v in data['reference_cap']),
            order=int(data['order']))
'''

SUBSET = '''
    @staticmethod
    def _subset_data(data, indices):
        index = torch.as_tensor(indices,dtype=torch.long)
        return dict(meridians={k:v[:,index] for k,v in data['meridians'].items()},
            core=tuple(v[index] for v in data['core']),
            cap=tuple(v[index] for v in data['cap']),
            W={k:v[:,index] for k,v in data['W'].items()},
            reference={k:v[:,index] for k,v in data['reference'].items()},
            reference_core=tuple(v[index] for v in data['reference_core']),
            reference_cap=tuple(v[index] for v in data['reference_cap']),
            order=int(data['order']))
'''

CLOSURE = '''
    def _closure_jets(self, controls, data, order):
        corrected = self._corrected_jets(data['meridians'],data['W'],controls,order)
        names = ('T','Tp','Tpp')
        self.normal_counts['closure_jet_angle_evaluations'] += len(controls)
        return torch.stack(tuple(((data['core'][j]-data['reference_core'][j])
            -(data['cap'][j]-data['reference_cap'][j])
            +self._total(corrected[names[j]]-data['reference'][names[j]]))/self.S
            for j in range(order+1)),dim=1)
'''

REFERENCE = '''
    def _reference_data(self, phi):
        return self.reference_calibration.reference_data(phi)
'''

FIELDS = '''
    def fields_torch(self, x, query, phi, *, curvature=True, query_label='arbitrary'):
        require_actions()
        self._select_point(x)
        phi = np.asarray(phi,dtype=float)
        if phi.ndim != 1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Use an actual finite one-dimensional material-chart angle list')
        data,direct,Wdirect,rho0 = self._meridian_data(x,query,phi,curvature,query_label)
        order = 2 if curvature else 1
        controls = self._implicit_jet_value(data,phi,order,x)
        integrated = self._corrected_jets(data['meridians'],data['W'],controls,order)
        requested = self._corrected_jets(direct,Wdirect,controls,order,need_s=curvature)
        result,defects,centered = {},[],[]
        h,hp,hpp = query['h'],query['hp'],query['hpp']
        for j,(name,output) in enumerate(zip(('T','Tp','Tpp'),('F','Fphi','Fphiphi'))):
            if j > order:
                break
            integral,total = self.base._integrate(integrated[name],query)
            C,P = data['core'][j][None],data['cap'][j][None]
            defect = C-P+total[None]
            # h=1-S5: complete physical lift, including the ACTUAL current defect.
            result[output] = (1-h)*P+h*C+integral-(1-h)*total[None]
            defects.append(defect)
            centered.append((data['core'][j]-data['reference_core'][j])
                -(data['cap'][j]-data['reference_cap'][j])
                +self._total(integrated[name]-data['reference'][name]))
        result['Fs'] = requested['T']+hp*defects[0]
        if curvature:
            result['Fss'] = requested['Ts']+hpp*defects[0]
            result['Fsphi'] = requested['Tp']+hp*defects[1]
        result['rho0'] = rho0
        result['closure_delta'] = defects[0][0]
        result['centered_closure_residual'] = centered[0]
        if any(not bool(torch.isfinite(v.detach()).all()) for v in result.values()):
            self._fail('Nonfinite complete reference-centred physical field with its full lift')
        self.reference_calibration.observe_field(defects,centered)
        self.counts['evaluated_field_points'] += len(query['cells'])*len(phi)
        return result
'''

def derive_normal(text):
    if digest(text) != OLD_NORMAL_SHA:
        raise ValueError("Bind the complete published R711 normal source")
    first=text.index('"""')
    last=text.index('"""',first+3)+3
    text=text[:first]+'''"""Complete R715 reference-centred R711 normal-plane field.

All original variables, 32-stage default, full implicit chains and true Gram
rows remain. Every closure/target angular jet subtracts the SAME frozen
reference. Physical sixjets include the complete CURRENT closure lift.
The accurate unit-speed equivalence is conditional on exact reference and
normal roots; the working lifted radial Gram is always really evaluated.
All scientific execution remains public Actions only.
"""'''+text[last:]
    text=once(text, "SCHEMA = '"+OLD_SCHEMA+"'", "SCHEMA = '"+NEW_SCHEMA+"'")
    text=once(text,"CONTROL_DIMENSION = 6","CONTROL_DIMENSION = 6\nREFERENCE_CENTRED_FROM_SHA256 = '"+OLD_NORMAL_SHA+"'\nREFERENCE_CENTERING_SOURCE_SHA256 = '"+HELPER_SHA+"'")
    text=once(text,"'_integrate', 'prepare', 'unpack', 'make_query', '_parent_tensor'):",
        "'_integrate', 'prepare', 'unpack', 'make_query', '_parent_tensor', 'initial'):")
    text=once(text,"                 endpoint_policy=None, normal_step_nodes=None, new_input_binder=None):",
        "                 endpoint_policy=None, normal_step_nodes=None, new_input_binder=None, reference_centering_module=None):")
    text=once(text,"        self.base_source_sha256 = expected_base_source_sha256",
        """        if (reference_centering_module is None
                or sha(reference_centering_module.__file__) != REFERENCE_CENTERING_SOURCE_SHA256
                or sha(reference_centering_module.FrozenReferenceCalibration.__init__.__code__.co_filename)
                    != REFERENCE_CENTERING_SOURCE_SHA256):
            raise ValueError('Bind the complete independent frozen-reference calibration helper')
        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(
            base,self._core_and_cap,self._total,endpoint_source_sha256=sha(__file__))
        self.reference_point_sha256 = self.reference_calibration.reference_point_sha256
        self.base_source_sha256 = expected_base_source_sha256""")
    text=once(text,"            field='Pcap + integral_S^s Exp((S W zeta(phi0)+gamma v(phi0)) cross) Exp(omega cross) T0; fixed successive normal planes select six controls',\n            endpoint_equation='Gamma_current-Pcap+integral_0^S corrected_T=0',",
        """            field='complete hDelta lift of CURRENT corrected T, with reference-centred normal-plane roots',
            endpoint_equation='(Gamma-Gamma0)-(P-P0)+integral_0^S(corrected_T-Tref)=0',
            reference_centering_definition=self.reference_calibration.definition,""")
    text=once(text,"        self.identity = canonical(self.model)",
        "        self.identity = canonical(self.model)\n        self.reference_calibration.bind_field(self.model,self.identity)")
    text=once(text,"            dimensionless_constraint='f=(Gamma-Pcap+integral corrected_T)/S',",
        "            dimensionless_constraint='f=((Gamma-Gamma0)-(P-P0)+integral(corrected_T-Tref))/S',")
    text=once(text,"            radial_Gram_error_identically_zero=True,\n            radial_identity_scope='the declared exact supported-smooth-triangle reference, rotation and integral definition; exact mean/normal branches require their stated conditions and all working errors remain unpaid',",
        """            radial_Gram_error_identically_zero=False,
            accurate_zero_root_radial_Gram_error_identically_zero=True,
            radial_identity_scope='only exact reference and final implicit roots; working complete-lift Gram is actually read',""")
    text=once(text,"            self._last_normal_batch = None\n\n    def initial(self):",
        """            self._last_normal_batch = None
            self.reference_calibration.select_point(self._current_point_sha256)

    def initial(self):""")
    text=method(text,"_detach_data",DETACH)
    text=method(text,"_subset_data",SUBSET)
    text=method(text,"_closure_jets",CLOSURE)
    text=once(text,"    def _meridian_data(self, x, query, phi, curvature, query_label):",
        REFERENCE.strip("\n")+"\n\n    def _meridian_data(self, x, query, phi, curvature, query_label):")
    text=once(text,"        data = dict(meridians=integration, core=core_jets, cap=cap_jets,\n                    W=self._W(self.integration_query, phi), order=order)",
        """        reference,reference_core,reference_cap = self._reference_data(phi)
        data = dict(meridians=integration, core=core_jets, cap=cap_jets,
                    reference=reference,reference_core=reference_core,reference_cap=reference_cap,
                    W=self._W(self.integration_query, phi), order=order)""")
    text=method(text,"fields_torch",FIELDS)
    text=once(text,"        # of the structurally zero radial error. The fixed g is unchanged.",
        "        # of the actual non-unit WORKING lifted Fs. The exact fixed g is unchanged.")
    text=once(text,"            base_complete_metadata=base_metadata,",
        "            base_complete_metadata=base_metadata,\n            reference_centering=self.reference_calibration.metadata(),\n            current_reference_calibration=self.reference_calibration.current_record(),")
    text=once(text,"            radial_metric_identity_in_exact_definition=True,numerical_radial_Gram_row_omitted=False,",
        """            radial_metric_identity_in_exact_definition=True,numerical_radial_Gram_row_omitted=False,
            working_radial_Gram_error_identically_zero=False,
            endpoint_residual_scope='centred equation; raw quadrature closure defect is reported separately',
            complete_current_raw_defect_lift_in_physical_sixjets=True,""")
    text=text.replace("final_acceptance='fresh physical closure norm <= endpoint_tolerance and all declared open control domains'",
        "final_acceptance='fresh centred closure norm <= endpoint_tolerance and all declared open control domains'")
    ast.parse(text)
    compile(text,NEW_NORMAL,"exec")
    return text

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    args=p.parse_args()
    source=args.repo/"topics/visible-flex-larger-amplitude/scripts/resume_20261126"/OLD_NORMAL
    text=derive_normal(source.read_text())
    args.out_dir.mkdir(parents=True,exist_ok=True)
    output=args.out_dir/NEW_NORMAL
    output.write_text(text)
    print(json.dumps({"file":str(output),"bytes":len(text.encode()),"sha256":digest(text),
        "scientific_execution":False,"complete_original_sha256":OLD_NORMAL_SHA}))

if __name__=="__main__":
    main()
