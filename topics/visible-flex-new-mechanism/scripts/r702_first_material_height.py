"""Propose first-material stationary heights and certify individual physical witnesses."""
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
from flint import arb, ctx
from r654_actual_seed_balls import fr
from r674_centered_material_physical_frontier import PhysicalFrontier
from r674_actual23_aligned_ruling_resume import InwardModel
from r674_actual23_paid_suffix_diagnostics import emit

MODES=np.arange(129)
DIV=1+MODES**2


def stationary_candidates(q,right,left=0.):
    """Candidates for a witness/model only. A missed stationary point conveys no certificate."""
    if not left<right:
        return []
    coeff=np.asarray(q[:129],float)/DIV
    freq=MODES*np.pi
    locations=np.linspace(left,right,65)
    slopes=-np.sin(locations[:,None]*freq)@(coeff*freq)
    points=[left,right]
    for i in range(len(locations)-1):
        if slopes[i]<=0<=slopes[i+1] and not slopes[i]==slopes[i+1]==0:
            def derivative(x):
                return float(-np.sin(x*freq)@(coeff*freq))
            a,b=locations[i:i+2]
            # Re-evaluate endpoints by the same scalar contraction used by brentq.
            fa,fb=derivative(a),derivative(b)
            if fa<=0<=fb:
                points.append(brentq(derivative,a,b,xtol=5.e-15))
    return sorted(set(points))


class WitnessFrontier(PhysicalFrontier):
    def __init__(self,*args):
        super().__init__(*args)
        self.witness_checks=0
        self.witnesses={}
        self.new_keys=set()
        self.old_prefix_keys=set()

    def qualify(self,q,tau,paid):
        key=self.key(q,tau)
        self.new_keys.add(key)
        if paid is not None:
            self.old_prefix_keys.add(key)
        times=[p.duration if p.control is None else Fraction(float(tau[p.control])) for p in self.pieces]
        L=sum(times)
        T=times[0]
        H=self.pieces[0].h[0]
        if any(self.pieces[0].h[1:]):
            raise ValueError("The first true leg must have constant background height")
        if (min(times)>0 and Fraction(21,10)<=L<=Fraction(79,10)
                and (paid is None or paid["piece"]==0)):
            left=Fraction(0) if paid is None else T*Fraction(paid["path"],2**paid["depth"])/L
            right=T/L
            qrat=[Fraction(float(v))/(1+j*j) for j,v in enumerate(q[:129])]
            points=stationary_candidates(q,float(right),float(left))
            for x in points:
                xx=Fraction(x)
                if not left<=xx<=right:
                    continue
                # Numerics above select the abscissa only. The proof below uses
                # its exact binary rational value and the unrounded physical shape.
                ctx.prec=192
                a=arb(fr(xx))*arb.pi()
                val=arb(fr(H))+sum((arb(fr(v))*(j*a).cos() for j,v in enumerate(qrat) if v),arb(0))
                self.witness_checks+=1
                if val<=arb(fr(Fraction(4,5))) or val>=arb(3):
                    rec={"state":"verified_first_material_point_violation","field":"h",
                        "shape_parameters":list(key[0]),"durations":list(key[1]),"x_exact":str(xx),
                        "first_piece_right_exact":str(right),"physical_h_ball":val.str(48),"precision_bits":192,
                        "source_closed_cells_carried":0 if paid is None else paid["closed_cells"],
                        "new_closed_cells":0,"new_visited_cells":0}
                    self.witnesses[key]=rec
                    self.records.append(rec)
                    self.violations[key]="Certified first-material height point violation"
                    self.unclosed.pop(key,None)
                    emit("R702_CERTIFIED_POINT_VIOLATION",rec)
                    raise FloatingPointError(self.violations[key])
        try:
            valid=super().qualify(q,tau,paid)
        except FloatingPointError:
            if key in self.violations:
                emit("R702_NEW_PHYSICAL_VIOLATION",self.records[-1])
            raise
        emit("R702_NEW_CLOSED_PHYSICAL_KEY",{"shape":list(key[0]),"times":list(key[1]),"certificate":valid})
        return valid


class StationaryInwardModel(InwardModel):
    def __init__(self,current,clock,index):
        super().__init__(current,clock,index)
        curve=current["data"]["curve"]
        first_duration,base_height=curve["first_material_constants"]
        q=curve["shape_parameters"]
        right=float(first_duration/float(curve["length"].value))
        points=stationary_candidates(q,right)
        normals=[];locations=[];orthogonal=[]
        def add(row,x):
            u=row.copy()
            for old in orthogonal:
                u-=(u@old)*old
            norm=np.linalg.norm(u)
            if norm>1.e-8*max(1.,np.linalg.norm(row)):
                normals.append(row)
                locations.append(float(x))
                orthogonal.append(u/norm)
        for x in points:
            if not 0<x<right:
                continue
            weights=np.cos(np.pi*x*MODES)/DIV
            if float(base_height)+weights@q[:129]<.80005:
                add(np.r_[weights,np.zeros(127)],x)
        real_minima=list(locations)
        for row,x in zip(self.N,self.positions):
            add(row,x)
        self.N=np.asarray(normals,float)
        self.positions=locations
        emit("R702_ACTUAL_FIRST_MATERIAL_MODEL",{"iteration":index,"interior_stationary_abscissae":real_minima,
            "all_direction_normals":locations,"first_piece_right":right,
            "certification_uses_the_original_full_five_fields":True})
