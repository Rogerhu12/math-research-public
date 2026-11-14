"""Explicit independent prefix/tail angular truncation for numerical research.

The retained low modes use the actual nonlinear finite tail. Higher prefix
modes use its physical linear Robin data ONLY in the BVP closure; the literal
tail reconstruction omits those modes. Both jet sets and the omitted cut jet
norms are returned. This is not a full-M nonlinear DN or an exact seam.
Astra curve_transition, AI-assisted, 2026-11-08.
"""
import copy,math
import numpy as np


class MixedTailPort:
    def __init__(self,low,linear_data,modes,base_mode):
        self.low=low;self.M=int(modes);self.lowM=low.M;self.cut=low.cut;self.config=low.config
        if not 0<self.lowM<self.M:raise ValueError('Mixed truncation requires 0 < tail modes < prefix modes')
        if int(low.ready['parameters']['spacing'])!=base_mode:raise ValueError('Mixed tail fundamental frequency mismatch')
        lp=linear_data.get('linearParameters',{});np_=low.ready['parameters']
        for key in ('rCut','wCut','width','curvatureBound','slopeCap','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset'):
            if lp.get(key)!=np_.get(key):raise ValueError('Mixed physical tail profile mismatch: '+key)
        slopes=np.asarray(linear_data['linearSlope'][:self.M],float)
        if len(slopes)!=self.M or not np.all(np.isfinite(slopes)):raise ValueError('Full physical high-mode linear port required')
        expected=base_mode*np.arange(1,self.M+1)
        actual=np.asarray(linear_data.get('linearModes',expected)[:self.M])
        if not np.array_equal(actual,expected):raise ValueError('Mixed linear port physical frequencies mismatch')
        self.frequencies=expected;self.linearD=slopes.copy()
        mismatch=np.max(abs(slopes[:self.lowM]-low.linearD)/np.maximum(1.,abs(low.linearD)))
        if mismatch>2e-4:raise ValueError('Linear port and nonlinear low tail disagree beyond initialization tolerance')
        self.linearD[:self.lowM]=low.linearD
        r=self.cut['radius'];w=self.cut['backgroundSlope'];wr=self.cut['backgroundSecond']
        self.linearSecond=-(wr/w)*(self.linearD-expected**2/r)
        self.ready={**low.ready,'parameters':{**low.ready['parameters'],'modes':self.M,'actualNonlinearModes':self.lowM},'linearSlope':self.linearD.tolist()}
        self.description=dict(scope=__doc__,prefix_modes=self.M,actual_nonlinear_tail_modes=self.lowM,
            high_modes_boundary_model='Physical linear finite-far Robin data; nonlinear high/high and low/high interactions are not included.',
            literal_tail_model='Only the retained nonlinear low modes are reconstructed; high cut mismatch is reported separately for jet repair.',
            linear_port_source=linear_data.get('source'),linear_low_relative_discrepancy=float(mismatch))
        self.radial_comparison=linear_data.get('linearRadialComparison')

    @property
    def calls(self):return self.low.calls

    def solve(self,height,jacobian=True,audit=False):
        H=np.asarray(height,float)
        if H.shape!=(self.M,):raise ValueError('Mixed height dimension mismatch')
        low=self.low.solve(H[:self.lowM],jacobian=jacobian,audit=audit)
        L=self.lowM;M=self.M;actual=copy.deepcopy(low['jets']);mixed=copy.deepcopy(actual)
        for key in ('height','slope','second'):
            actual[key]=list(actual[key])+[0.]*(M-L)
        mixed['height']=H.tolist()
        mixed['slope']=list(low['jets']['slope'])+(self.linearD[L:]*H[L:]).tolist()
        mixed['second']=list(low['jets']['second'])+(self.linearSecond[L:]*H[L:]).tolist()
        J=None
        if jacobian:
            jl=np.asarray(low['heightJetJacobian']).reshape(3*L+2,L);J=np.zeros((3*M+2,M))
            J[:L,:L]=jl[:L];J[M:M+L,:L]=jl[L:2*L]
            J[2*M:2*M+2,:L]=jl[2*L:2*L+2]
            J[2*M+2:2*M+2+L,:L]=jl[2*L+2:]
            for j in range(L,M):J[j,j]=self.linearD[j];J[M+j,j]=self.linearSecond[j];J[2*M+2+j,j]=1.
            J=J.ravel().tolist()
        modes=self.frequencies[L:];hh=H[L:];ds=self.linearD[L:]*hh;dds=self.linearSecond[L:]*hh
        E=self.cut['E'];rss=-self.cut['Ep']/(2*E*E)
        omitted=dict(height_l1=float(np.sum(abs(hh))),radial_first_l1=float(np.sum(abs(ds))),radial_second_l1=float(np.sum(abs(dds))),
            angular_first_l1=float(np.sum(modes*abs(hh))),angular_second_l1=float(np.sum(modes*modes*abs(hh))),
            radial_angular_l1=float(np.sum(modes*abs(ds))),meridian_first_l1=float(np.sum(abs(ds))/math.sqrt(E)),
            meridian_second_l1=float(np.sum(abs(dds/E+ds*rss))),
            scope='Whole-angle bounds for the explicitly omitted height-jet trigonometric polynomial at the cut. These are neither full Cartesian seam bounds nor estimates of omitted nonlinear tail interactions.')
        refinement=None
        if self.radial_comparison:
            rows=self.radial_comparison['modes'][L:M]
            if [v['mode'] for v in rows]!=modes.tolist():raise ValueError('High-mode radial comparison frequencies differ')
            refinement=dict(slope_l1_change_weighted_by_actual_cut_height=float(sum(v['slope_change']*abs(h) for v,h in zip(rows,hh))),
                second_l1_change_weighted_by_actual_cut_height=float(sum(v['second_change']*abs(h) for v,h in zip(rows,hh))),
                coarse_steps=self.radial_comparison['coarse_steps'],fine_steps=self.radial_comparison['fine_steps'],
                scope='Observed linear radial-refinement difference weighted by this cut trace; not a certified error bound.')
        return {**low,'jets':mixed,'actual_tail_jets':actual,'heightJetJacobian':J,
            'mixed_truncation':{**self.description,'high_cut_modes':modes.tolist(),'high_cut_height':hh.tolist(),
                'high_linear_slope':ds.tolist(),'high_linear_second':dds.tolist(),'omitted_height_jet_bounds':omitted,'linear_radial_refinement_effect':refinement},
            'audit_scope':'The tail audit concerns only the literal low-mode nonlinear tail, not the high-mode linear boundary closure.'}

    def close(self):self.low.close()
