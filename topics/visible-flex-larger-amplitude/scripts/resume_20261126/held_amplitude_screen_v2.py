#!/usr/bin/env python3
"""Complete sampled held-amplitude screen with a bounded working-row proposal.

The caller supplies every actual grid F and every permanent arbitrary F
from its unchanged R671 six-jet reader. No field is reconstructed here.
Every supplied position has separate body-radius and BOTH witness-distance
constraints. Finite heap limits affect QP row proposals only: maxima, true
feasibility, grid coverage, and permanent location memory are never capped.
No continuous geometry or amplitude certificate follows from this module.
"""
import hashlib
import heapq
import math
import os
from pathlib import Path

import numpy as np

ROWS_SHA256='d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'
SCHEMA='complete-sampled-held-amplitude-screen-v2'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific amplitude screening belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def point_key(location):
    return (int(location['cell']),float(location['u']).hex(),float(location['phi']).hex())


class Accumulator:
    """Read one actual candidate, retaining exact extrema and both signs.

    Complete grid coverage is checked by an exact stage bitset. Arbitrary
    locations are deduplicated only at the same binary cell/u/phi. A failed
    or interrupted read is not an accepted screen. The object is private
    temporary state; only finish() returns JSON-compatible scalar records.
    """
    def __init__(self,problem,prepared,rows,budgets,*,top_radius=2,top_distance=4,active_band=.025):
        require_actions()
        if sha(rows.__file__)!=ROWS_SHA256:
            raise ValueError('Use the complete reviewed amplitude covector/values source')
        if (int(top_radius)!=top_radius or int(top_distance)!=top_distance
                or min(top_radius,top_distance)<1 or not math.isfinite(active_band) or active_band<=0):
            raise ValueError('Use positive explicit bounded row-proposal counts and band')
        if float(problem.R).hex()!=budgets.cap_radius.hex():
            raise ValueError('The scalar cap row must use the actual same FullHold radius')
        self.problem=problem;self.prepared=prepared;self.rows=rows;self.budgets=budgets
        self.top_radius=int(top_radius);self.top_distance=int(top_distance);self.active_band=float(active_band)
        self.r0=rows.current_witness_radius(problem,prepared)
        self.height=float(prepared.height)
        self.stages=np.zeros(problem.P,dtype=bool)
        self.arbitrary=set();self.grid_points=0;self.arbitrary_points=0
        self.radius=[];self.distance=[];self.sequence=0
        self.maximum={key:dict(value=-float('inf'),location=None) for key in
            ('body_diameter','witness_plus','witness_minus')}
        self.maximum_body_radius_squared=0.
        self.minimum_witness_distance_squared=float('inf')

    def _retain(self,heap,limit,value,location):
        # Unique sequence numbers prevent heap comparisons between dicts.
        self.sequence+=1
        entry=(float(value),self.sequence,location)
        if len(heap)<limit:heapq.heappush(heap,entry)
        elif value>heap[0][0]:heapq.heapreplace(heap,entry)

    def _consume(self,F,phi,location_at):
        F=np.asarray(F);phi=np.asarray(phi)
        if F.shape!=(phi.size,3):raise ValueError('One finite physical position per actual angle is required')
        values=self.rows.point_values(F,phi,self.r0,self.budgets)
        for key,data in values.items():
            if data.shape!=(phi.size,) or not np.isfinite(data).all():
                raise ValueError('A true amplitude screen has a nonfinite actual inequality')
            index=int(np.argmax(data))
            if float(data[index])>self.maximum[key]['value']:
                self.maximum[key]=dict(value=float(data[index]),location=location_at(index))
        radii=np.sum(F*F,axis=1)
        self.maximum_body_radius_squared=max(self.maximum_body_radius_squared,float(np.max(radii)))
        distance_violation=np.maximum(values['witness_plus'],values['witness_minus'])
        min_distance=(1-float(np.max(distance_violation)))*self.budgets.witness_lower_budget**2
        self.minimum_witness_distance_squared=min(self.minimum_witness_distance_squared,min_distance)
        for data,heap,limit in ((values['body_diameter'],self.radius,self.top_radius),
                (distance_violation,self.distance,self.top_distance)):
            count=min(limit,data.size)
            indices=np.argpartition(data,data.size-count)[data.size-count:]
            for index in indices:
                self._retain(heap,limit,float(data[index]),location_at(int(index)))

    def add_grid(self,stage,F):
        stage=int(stage)
        if not 0<=stage<self.problem.P or self.stages[stage]:
            raise ValueError('Read each actual current radial observation stage exactly once')
        if np.asarray(F).shape!=(self.problem.N,3):
            raise ValueError('Every current quarter-angle observation must be included')
        def location(index):
            return dict(stage=stage,angle=index,
                cell=int(self.problem.observation_cells[stage]),
                u=float(self.problem.observation_u[stage]),phi=float(self.problem.phi[index]))
        self._consume(F,self.problem.phi,location)
        self.stages[stage]=True;self.grid_points+=self.problem.N

    def add_arbitrary(self,location,F):
        where={key:location[key] for key in ('cell','u','phi')}
        cell,u,phi=int(where['cell']),float(where['u']),float(where['phi'])
        if not 0<=cell<self.problem.J-1 or not 0<=u<=1 or not math.isfinite(phi):
            raise ValueError('A permanent amplitude point is outside the actual current cell domain')
        where=dict(cell=cell,u=u,phi=phi)
        key=point_key(where)
        if key in self.arbitrary:return
        value=np.asarray(F)
        if value.shape!=(3,):raise ValueError('One actual rotating-frame position is required')
        self._consume(value[None,:],np.array([phi]),lambda index:where)
        self.arbitrary.add(key);self.arbitrary_points+=1

    def finish(self,*,expected_arbitrary_locations):
        grid_complete=bool(np.all(self.stages))
        expected={point_key(location) for location in expected_arbitrary_locations}
        arbitrary_complete=self.arbitrary==expected
        complete=bool(grid_complete and arbitrary_complete)
        scalars=self.rows.scalar_values(self.height,self.budgets)
        maxima={key:dict(value=value['value'],location=value['location'])
            for key,value in self.maximum.items()}
        finite=all(math.isfinite(record['value']) for record in maxima.values())
        finite=finite and all(math.isfinite(value) for value in scalars.values())
        passed=bool(complete and finite and max([v['value'] for v in maxima.values()]+list(scalars.values()))<=0)
        selections=[]
        # The worst point of each family is always proposed. Further entries
        # need the declared band. Every selected distance location keeps BOTH
        # signs, even when one branch has much more positive margin.
        for heap,kind in ((self.radius,'body_diameter'),(self.distance,'witness_distance')):
            seen=set()
            for order,(value,_,location) in enumerate(sorted(heap,key=lambda item:(-item[0],item[1]))):
                if order and value < -self.active_band:continue
                key=point_key(location)
                if key in seen:continue
                seen.add(key)
                selections.append(dict(kind=kind,location=location,protected=False,
                    selection_inequality_value=float(value),
                    both_distance_signs_retained=kind=='witness_distance'))
        remembered={}
        for record in list(maxima.values())+selections:
            location=record.get('location')
            if location is not None:
                actual={key:location[key] for key in ('cell','u','phi')}
                remembered[point_key(actual)]=actual
        proposed_rows=sum(2 if item['kind']=='witness_distance' else 1 for item in selections)+2
        return dict(schema=SCHEMA,complete=complete,finite=finite,passed=passed,
            budgets=self.budgets.metadata(),current_witness_radius=float(self.r0),height=self.height,
            maximum_inequality_by_kind=maxima,scalar_inequalities=scalars,
            maximum_inequality_value=max([v['value'] for v in maxima.values()]+list(scalars.values())),
            grid_stages_read=int(np.count_nonzero(self.stages)),required_grid_stages=self.problem.P,
            grid_quarter_points_read=self.grid_points,required_grid_quarter_points=self.problem.P*self.problem.N,
            literal_full_orbit_point_count=self.problem.P*getattr(self.problem,'full_N',self.problem.N),
            distinct_arbitrary_points_read=self.arbitrary_points,
            required_distinct_arbitrary_points=len(expected),
            exact_arbitrary_location_set_equals_required_set=arbitrary_complete,
            complete_grid_coverage=grid_complete,
            all_grid_points_and_both_witness_signs_read=grid_complete,
            all_permanent_locations_and_both_witness_signs_read=arbitrary_complete,
            maximum_body_radius_squared=self.maximum_body_radius_squared,
            minimum_witness_distance_squared=self.minimum_witness_distance_squared,
            amplitude_row_selections=selections,proposed_appended_rows_including_cap_and_height=proposed_rows,
            selected_radius_limit=self.top_radius,selected_distance_location_limit=self.top_distance,
            working_active_band=self.active_band,
            newly_observed_extreme_and_selected_locations=list(remembered.values()),
            location_identity='exact cell and binary64 u/phi; no neighborhood merge in permanent memory',
            fixed_grip_and_held_budget_algebra_validated=True,
            continuous_amplitude_certified=False,global_embedding_or_reach_certified=False,
            scope='Necessary finite inequalities for the selected sufficient D/L certificate; all-point numerical screen and bounded QP proposals are distinct')
