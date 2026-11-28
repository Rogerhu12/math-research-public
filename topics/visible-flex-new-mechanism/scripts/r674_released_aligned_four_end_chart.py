"""Released four-time chart on moving material panels and original fixed readouts."""
from collections import Counter
from math import ceil
import numpy as np

from r654_released_rest_four_end_chart import (
    ReleasedChart, FourEndPending, LD, Jet, original, paid, coefficients, polynomial_jet, number)
from r674_moving_material_integral_grid import MaterialGrid, fixed_readout


class AlignedChart(ReleasedChart):
    def __init__(self,base,source_times,order,clock,fine=False):
        original.reduced.require_public_science()
        self.base,self.clock,self.order=base,clock,order
        self.polys=[(coefficients(p.h),coefficients(p.k)) for p in base.pieces]
        times=[float(p.duration) if p.control is None else float(source_times[p.control])
               for p in base.pieces]
        self.subdivisions=[(2 if fine else 1)*max(1,ceil(64*t/sum(times))) for t in times]
        self.observations=fixed_readout(128 if fine else 64,order)
        self.knots=np.linspace(0.,1.,65)
        self.counts=Counter()
        self.progress={}
        self.first_control_rows=None
        self.grid=None

    def solve_controls(self,*args,**kwargs):
        curve,report=super().solve_controls(*args,**kwargs)
        curve["grid"].control_chain=curve["implicit_four_time_derivatives"]
        return curve,report

    def _joint(self,q,tau,mode,fixed_center):
        q,tau=np.asarray(q,float),np.asarray(tau,float)
        if (q.shape!=(256,) or tau.shape!=(4,) or not np.all(np.isfinite(q))
                or not np.all(np.isfinite(tau)) or np.any(tau<=0)):
            raise ValueError("256 finite shapes and four positive actual times required")
        try:
            qualification=self.base.physical_enclosure(q,tau)
        except FourEndPending as exc:
            self.progress["current_map"]["unclosed_continuous_physical_frontier"]=exc.record
            raise
        self.progress["current_map"]["continuous_physical_qualification"]=qualification
        if not qualification["sufficient_bounds_closed"]:
            raise FourEndPending(self.progress)
        dimension={"full":260,"controls":4,"fixed":0}[mode]
        if fixed_center is not None and mode!="fixed":
            raise ValueError("Fixed-center fine requires fixed actual parameters")
        def constant(x):
            return Jet(x,np.zeros(dimension))
        durations=[]
        for p in self.base.pieces:
            d=constant(number(p.duration) if p.control is None else tau[p.control])
            if p.control is not None and dimension:
                d.derivative[-4+p.control]=1.
            durations.append(d)
        starts=[constant(0)]
        for d in durations:
            starts.append(starts[-1]+d)
        length=starts[-1]
        self.grid=MaterialGrid(starts,durations,self.subdivisions,self.order,self.observations,self.clock)
        x=self.grid.x[:,None]
        bases=[]
        for width,sine in ((129,False),(127,True)):
            modes=np.arange(width,dtype=LD)
            w=np.arccos(LD(-1))*(modes+(LD(".5") if sine else 0))
            scale=1+(2*modes+1 if sine else modes)**2
            sn,cs=np.sin(x*w),np.cos(x*w)
            if sine:
                sn[self.grid.x==0]=0
                cs[self.grid.x==1]=0
                fields=(sn,cs*w,-sn*w**2,-cs*w**3)
            else:
                sn[(self.grid.x==0)|(self.grid.x==1)]=0
                fields=(cs,-sn*w,-cs*w**2,sn*w**3)
            basis=[b/scale for b in fields]
            values=[b@q[129 if sine else 0:256 if sine else 129].astype(LD) for b in basis]
            bases.append((basis,values))
        cuts=np.asarray([s.value for s in starts[1:]],dtype=LD)
        raw=[]
        for i,(piece,local_t,x_tau) in enumerate(self.grid.tags):
            x=float(self.grid.x[i]) if piece<0 else self.grid.x[i]
            if piece<0:
                piece=min(int(np.searchsorted(cuts,length.value*x,side="right")),len(durations)-1)
            D=durations[piece]
            if local_t is not None:
                t=constant(local_t)
            elif x==0 or x==1:
                t=constant(x)
            else:
                t=(length*LD(x)-starts[piece])/D
            fields=[]
            for side,((basis,values),coeff) in enumerate(zip(bases,self.polys[piece])):
                offset,width=(0,129) if side==0 else (129,127)
                for j in range(3):
                    perturb=constant(values[j][i])
                    if mode=="full":
                        perturb.derivative[offset:offset+width]=basis[j][i]
                    if dimension:
                        perturb.derivative[-4:]=values[j+1][i]*x_tau
                    fields.append(polynomial_jet(coeff[j:j+2],t)/D**j+perturb/length**j)
            raw.append(fields)
        eta=self.grid.integrate([[length*r[4]/(2*r[0])] for r in raw])
        geometry=[[r[0],r[3],e[0],r[1],r[4]] for r,e in zip(raw,eta)]
        acceleration=[[r[2],r[5]] for r in raw]
        physical=original.physical_attainers(geometry,self.grid.x,length.value)
        physical["released_shape_continuous_original_field_enclosure"]=qualification
        physical["all_represented_shape_fields_in_original_box"]=True
        # These shapes are polynomial-plus-trigonometric. Keep the original
        # actual fields and give their own continuous certificate an explicit name.
        if not physical["all_sampled_original_physical_fields_in_box"]:
            raise FloatingPointError("A reconstructed physical sample leaves an original box")
        center=geometry[0]
        beta=acceleration[0][0]-center[0]*center[4]**2/4
        physical.update(physical_center_v=float(center[4].value),physical_center_beta=float(beta.value))
        if center[4].value>=0 or beta.value>=0:
            raise FloatingPointError("The selected nonzero negative R620 center branch is unavailable")
        primitive=self.grid.integrate([[length*v for v in paid.density(g)] for g in geometry])
        total=primitive[-1]
        if fixed_center is None:
            history=[[v-total[j] if j in original.original.ODD else v for j,v in enumerate(row)]
                     for row in primitive]
        else:
            history=[[v+constant(LD(fixed_center[j])) for j,v in enumerate(row)] for row in primitive]
        p,t,s,r=(history[-1][j] for j in (1,3,6,4))
        E=[8*t+2*p,p,4*s,8*r]
        H=center[0]
        observed=[total[1]/length,(8*total[3]+2*total[1])/length,
                  8*H**2*total[4]/length,4*H**2*total[6]/length]
        curve={"geometry":geometry,"acceleration":acceleration,"history":history,
            "total_integral":total,"length":length,"grid":self.grid,"knots":self.knots,
            "end":observed,"reduced_end":[p,t,s,r],"shape_parameters":q.copy(),
            "parameters":q.copy(),"four_rest_controls_binary64":tau.copy(),
            "physical_attainers":physical,"fixed_physical_centers":fixed_center is not None}
        if mode=="controls" and self.first_control_rows is None:
            self.first_control_rows={"shape_identity":original.identity(q.tolist()),
                "four_times":tau.tolist(),"E_at_actual_source_times":[float(v.value) for v in E],
                "current_E_tau_at_actual_source_times":[v.derivative.tolist() for v in E]}
        self.counts[mode+"_completed"]+=1
        self.clock.check("after_R654_current_true_density_integrals")
        return curve,E

