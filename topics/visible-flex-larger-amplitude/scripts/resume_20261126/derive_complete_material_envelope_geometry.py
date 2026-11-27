#!/usr/bin/env python3
"""Pure text derivation of the complete new-envelope world geometry source."""
import argparse
import ast
import hashlib
from pathlib import Path

PARENT_SHA = '353196a4faadc7537d04d6be139c9d9d8f47ee7e25e1f007e33588ac48cfa0ff'

COLLECT = r'''
    def _envelope_extra_fields(self):
        q = self.q
        if not self.envelope.extra_cells:
            return
        query = q.base.make_query(self.envelope.extra_cells,self.envelope.extra_u)
        with torch.no_grad():
            xt = torch.as_tensor(self._x,dtype=torch.float64,device='cpu')
            for begin,end in q._blocks():
                values = q.fields_torch(xt,query,q.phi[begin:end],curvature=True,
                    query_label='complete_historical_material_envelope')
                yield begin,end,{key:value.cpu().numpy() for key,value in values.items()}

    def _envelope_location(self, radial, angle, historical=False, **metadata):
        if not historical:
            return self._grid_location(radial,angle,**metadata)
        result = dict(cell=int(self.envelope.extra_cells[radial]),
            u=float(self.envelope.extra_u[radial]),phi=float(self.q.phi[angle]),
            protected=False,historical_envelope_grid=True)
        result.update(metadata)
        return result

    def _collect_complete_grid(self,cells,local,iterator,*,historical):
        q = self.q
        count = len(cells)
        if count == 0:
            raise ValueError('Empty grids are handled explicitly without fabricated extrema')
        kappas,radii = np.empty((count,q.N,2)),np.empty((count,q.N))
        covered = np.zeros(q.N,dtype=bool)
        radius_pool,distance_pool = {},{}
        maxima = {key:-math.inf for key in ('body_diameter','distance_plus','distance_minus')}
        worst_by_family = {}
        minimum_area = math.inf
        radial_index = {}
        for index,(cell,u) in enumerate(zip(cells,local)):
            radial_index.setdefault((int(cell),float(u).hex()),index)
        needed = {}
        for item in list(self._curvature_memory.values())+list(self._radius_memory.values()):
            radial = radial_index.get((item['cell'],float(item['u']).hex()))
            angle = self._angle_index.get(float(item['phi']).hex())
            if radial is not None and angle is not None:
                needed.setdefault(angle,[]).append((radial,_key(item)))
        blocks = 0
        for begin,end,supplied in iterator:
            begin,end = int(begin),int(end)
            if not 0 <= begin < end <= q.N or np.any(covered[begin:end]):
                raise ValueError('An actual complete material angular block overlaps or is invalid')
            z = self._validate_fields(supplied,(count,end-begin,3))
            V,W = z['Fs'],z['Fphi']
            cross = np.cross(V,W)
            area = np.sqrt(np.sum(cross*cross,axis=-1))
            if not np.isfinite(area).all() or np.any(area<=0):
                raise FloatingPointError('A material envelope point has nonpositive or nonfinite tangent area')
            minimum_area = min(minimum_area,float(np.min(area)))
            normal = cross/area[...,None]
            E,F,G = np.sum(V*V,axis=-1),np.sum(V*W,axis=-1),np.sum(W*W,axis=-1)
            e = np.sum(normal*z['Fss'],axis=-1)
            f = np.sum(normal*z['Fsphi'],axis=-1)
            g = np.sum(normal*z['Fphiphi'],axis=-1)
            determinant = area*area
            trace = (e*G+g*E-2*f*F)/determinant
            gauss = (e*g-f*f)/determinant
            gap = np.sqrt(np.maximum(0.,trace*trace-4*gauss))
            block_k = np.stack(((trace-gap)/2,(trace+gap)/2),axis=-1)
            block_r = np.sqrt(np.sum(z['F']*z['F'],axis=-1))
            if not np.isfinite(block_k).all() or not np.isfinite(block_r).all():
                raise FloatingPointError('A complete envelope curvature/radius is nonfinite')
            kappas[:,begin:end] = block_k
            radii[:,begin:end] = block_r
            amplitude = self._amplitude_values(z)
            for family in maxima:
                values = amplitude[family]
                radial,angle = tuple(int(v) for v in np.unravel_index(np.argmax(values),values.shape))
                maximum = float(values[radial,angle])
                if maximum > maxima[family]:
                    maxima[family] = maximum
                    loc = self._envelope_location(radial,begin+angle,historical)
                    worst_by_family[family] = dict(location=loc,physical_g=maximum)
                    self._field_cache[_key(loc)] = {name:value[radial,angle].copy() for name,value in z.items()}
            paired = np.maximum(amplitude['distance_plus'],amplitude['distance_minus'])
            for family,values,keep,pool in (
                    ('body_diameter',amplitude['body_diameter'],self.amplitude_top_radius,radius_pool),
                    ('witness_distance',paired,self.amplitude_top_distance,distance_pool)):
                flat = np.asarray(values).ravel()
                take = min(len(flat),max(64,8*keep))
                while True:
                    indices = np.argpartition(flat,len(flat)-take)[-take:]
                    indices = indices[np.argsort(flat[indices])[::-1]]
                    chosen,keys = [],set()
                    for index in indices:
                        radial,angle = tuple(int(v) for v in np.unravel_index(int(index),values.shape))
                        loc = self._envelope_location(radial,begin+angle,historical)
                        key = _key(loc)
                        if key not in keys:
                            keys.add(key)
                            chosen.append((loc,float(flat[index]),radial,angle))
                            if len(chosen)==keep:
                                break
                    if len(chosen)==keep or take==len(flat):
                        break
                    take = min(len(flat),2*take)
                for loc,score,radial,angle in chosen:
                    self._offer(pool,loc,score,keep,kind=family)
                    self._field_cache[_key(loc)] = {name:value[radial,angle].copy() for name,value in z.items()}
            for angle in range(begin,end):
                for radial,key in needed.get(angle,()):
                    self._field_cache[key] = {name:value[radial,angle-begin].copy() for name,value in z.items()}
            covered[begin:end] = True
            blocks += 1
        if not covered.all():
            raise ValueError('The complete material envelope angular coverage is incomplete')
        worst = tuple(int(v) for v in np.unravel_index(np.argmax(np.abs(kappas)),kappas.shape))
        farthest = tuple(int(v) for v in np.unravel_index(np.argmax(radii),radii.shape))
        K,radius = float(abs(kappas[worst])),float(radii[farthest])
        diameter = max(2.,2*abs(float(self._prepared.height)),2*radius)
        summary = dict(complete=True,maximum_absolute_principal_curvature=K,maximum_radius=radius,
            diameter_point_lower=diameter,necessary_reach_product=self.reach_ratio*diameter*K,
            min_area=minimum_area,worst=self._envelope_location(*worst[:2],historical,branch=worst[2]),
            farthest=self._envelope_location(*farthest,historical),point_count=count*q.N,
            observed_stages=count,angular_orbits=q.N,angular_blocks=blocks,
            every_requested_grid_point_read=True,angular_coverage_complete=True,
            historical_extra_grid=historical,continuous_geometry_certified=False)
        return dict(kappas=kappas,radii=radii,summary=summary,radius_pool=radius_pool,
            distance_pool=distance_pool,maximum_body_g=maxima['body_diameter'],
            maximum_plus_g=maxima['distance_plus'],maximum_minus_g=maxima['distance_minus'],
            worst_by_family=worst_by_family)

    def _ensure_grid(self):
        if self._grid is None:
            domain = self.q.domain(self._x)
            self._grid = self._collect_complete_grid(self.q.observation_cells,self.q.observation_u,
                self.q.grid_fields(self._x),historical=False)
            self._grid['summary']['domain'] = domain
        if self._extra_grid is None and self.envelope.extra_cells:
            self._extra_grid = self._collect_complete_grid(self.envelope.extra_cells,self.envelope.extra_u,
                self._envelope_extra_fields(),historical=True)
        self._extra_complete = self._extra_grid is not None or not self.envelope.extra_cells

    def envelope_grids(self):
        if self._grid is None or not self._extra_complete:
            raise ValueError('Every actual grid must be complete before row selection')
        result = [(self.q.observation_cells,self._grid['kappas'],
            lambda radial,angle:self._envelope_location(radial,angle,False))]
        if self._extra_grid is not None:
            result.append((self.envelope.extra_cells,self._extra_grid['kappas'],
                lambda radial,angle:self._envelope_location(radial,angle,True)))
        return result
'''

SCAN = r'''
    def scan(self,x,witnesses=(),radius_witnesses=()):
        require_actions()
        witnesses,radius_witnesses = list(witnesses),list(radius_witnesses)
        self.envelope.admit_explicit(witnesses+radius_witnesses)
        self._remember(witnesses,self._curvature_memory)
        self._remember(radius_witnesses,self._radius_memory)
        current_complete=extra_complete=explicit_complete=False
        attempted=np.asarray(x,dtype=float)
        attempted_token=(array_sha(attempted) if attempted.shape==(self.q.free_size,)
            and np.isfinite(attempted).all() else None)
        try:
            self._set_x(x)
            self._ensure_grid()
            current_complete = self._grid is not None
            extra_complete = self._extra_complete
            grids = [(self._grid,False)]
            if self._extra_grid is not None:
                grids.append((self._extra_grid,True))
            K=radius=-math.inf
            minimum_area=math.inf
            worst=farthest=None
            maxima={key:-math.inf for key in ('body_diameter','distance_plus','distance_minus')}
            worst_by_family={}
            radius_pool,distance_pool={},{}
            for grid,historical in grids:
                curv=self.pure.pick_extremes(grid['kappas'],16,branches=True)
                radii=self.pure.pick_extremes(grid['radii'],2)
                self._remember([self._envelope_location(s,a,historical) for s,a,_ in curv]
                    +[grid['summary']['worst']],self._curvature_memory)
                self._remember([self._envelope_location(s,a,historical) for s,a in radii]
                    +[grid['summary']['farthest']],self._radius_memory)
                if grid['summary']['maximum_absolute_principal_curvature']>K:
                    K=float(grid['summary']['maximum_absolute_principal_curvature'])
                    worst=grid['summary']['worst']
                if grid['summary']['maximum_radius']>radius:
                    radius=float(grid['summary']['maximum_radius'])
                    farthest=grid['summary']['farthest']
                minimum_area=min(minimum_area,float(grid['summary']['min_area']))
                for family in maxima:
                    item=grid['worst_by_family'][family]
                    if item['physical_g']>maxima[family]:
                        maxima[family]=float(item['physical_g'])
                        worst_by_family[family]=dict(item)
                for pool,key,count in ((radius_pool,'radius_pool',self.amplitude_top_radius),
                                        (distance_pool,'distance_pool',self.amplitude_top_distance)):
                    for item in grid[key].values():
                        self._offer(pool,item['location'],item['score'],count,kind=item['kind'])
            self._remember([v['location'] for v in radius_pool.values()]
                +[v['location'] for v in distance_pool.values()]
                +[v['location'] for v in worst_by_family.values()],self._radius_memory)
            union=dict(self._curvature_memory)
            union.update(self._radius_memory)
            point_records=[]
            for location in union.values():
                if not self.envelope.contains(location):
                    raise ValueError('A physical location escaped its complete declared envelope')
                fields=self._point(location)
                values,point_radius,area=self._point_geometry(fields)
                branch=int(np.argmax(np.abs(values)))
                value=abs(float(values[branch]))
                if value>K:
                    K,worst=value,dict(location,branch=branch)
                if point_radius>radius:
                    radius,farthest=point_radius,dict(location)
                minimum_area=min(minimum_area,area)
                av=self._amplitude_values(fields)
                for family in maxima:
                    if float(av[family])>maxima[family]:
                        maxima[family]=float(av[family])
                        worst_by_family[family]=dict(location=dict(location),physical_g=float(av[family]))
                self._offer(radius_pool,location,av['body_diameter'],self.amplitude_top_radius,kind='body_diameter')
                self._offer(distance_pool,location,max(av['distance_plus'],av['distance_minus']),
                    self.amplitude_top_distance,kind='witness_distance')
                point_records.append(dict(location=location,signed_principal_curvatures=[float(v) for v in values],
                    radius=point_radius,area=area,amplitude={key:float(v) for key,v in av.items()}))
            explicit_complete=True
            self._remember([worst],self._curvature_memory)
            self._remember([farthest]+[v['location'] for v in radius_pool.values()]
                +[v['location'] for v in distance_pool.values()]
                +[v['location'] for v in worst_by_family.values()],self._radius_memory)
            diameter=max(2.,2*abs(float(self._prepared.height)),2*radius)
            product=self.reach_ratio*diameter*K
            scalar=self._scalar_values()
            maximum_g=max(product-self.safety,*maxima.values(),*scalar.values())
            if not math.isfinite(maximum_g):
                raise FloatingPointError('Nonfinite complete envelope inequality maximum')
            result=dict(schema=SCHEMA,complete=True,passed=bool(maximum_g<=0),
                current_full_point_sha256=self._token,actual_model_identity_sha256=self.q.identity,
                maximum_physical_g=float(maximum_g),maximum_absolute_principal_curvature=K,
                maximum_radius=radius,diameter_point_lower=diameter,necessary_reach_product=product,
                reach_physical_g=product-self.safety,min_area=minimum_area,worst=worst,farthest=farthest,
                current_height=float(self._prepared.height),current_witness_radius=float(1.+np.sum(self._prepared.core)),
                grid=self._grid['summary'],
                historical_extra_grid=None if self._extra_grid is None else self._extra_grid['summary'],
                permanent_unique_locations_read=len(union),permanent_curvature_locations=len(self._curvature_memory),
                permanent_radius_locations=len(self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=True,all_six_world_jets_read=True,
                both_witness_signs_read_at_every_point=True,
                amplitude=dict(complete=True,**maxima,**scalar,worst_by_family=worst_by_family,
                    radius_working_candidates=sorted(radius_pool.values(),key=lambda v:-v['score']),
                    distance_working_candidates=sorted(distance_pool.values(),key=lambda v:-v['score']),
                    budgets=self.budgets.metadata()),
                new_curvature_locations=self._new_locations(witnesses,self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses,self._radius_memory),
                continuous_geometry_certified=False,continuous_metric_certified=False,
                rigorous_quadrature_or_root_errors_paid=False,old_continuous_certificates_inherited=False,
                source_binding=self.binding,permanent_point_records=point_records)
            result['material_envelope']=self.envelope.observe_scan(result,
                extra_complete=extra_complete,explicit_complete=explicit_complete,
                full_current_complete=current_complete)
            self._last_scan=result
            return result
        except (ValueError,ArithmeticError,OverflowError,np.linalg.LinAlgError) as error:
            current_complete=bool(self._grid is not None and self._token==attempted_token)
            extra_complete=bool(current_complete and self._extra_complete)
            self._grid=None
            self._extra_grid=None
            self._extra_complete=False
            self._last_scan=None
            result=dict(schema=SCHEMA,complete=False,passed=False,current_full_point_sha256=attempted_token,
                actual_model_identity_sha256=self.q.identity,maximum_physical_g=None,
                error_type=type(error).__name__,error=str(error),
                new_curvature_locations=self._new_locations(witnesses,self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses,self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=False,
                continuous_geometry_certified=False,old_continuous_certificates_inherited=False)
            result['material_envelope']=self.envelope.observe_scan(result,
                extra_complete=extra_complete,explicit_complete=explicit_complete,
                full_current_complete=current_complete)
            return result
'''


def derive(parent,memory_sha,rows_sha):
    if hashlib.sha256(parent.encode()).hexdigest()!=PARENT_SHA:
        raise ValueError('Use the complete original C1 geometry body')
    tree=ast.parse(parent)
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='GeometryScreen')
    lines=parent.splitlines(True)
    replacements=[]
    for n in cls.body:
        if isinstance(n,ast.FunctionDef) and n.name in ('_ensure_grid','scan'):
            replacements.append((n.lineno-1,n.end_lineno,COLLECT if n.name=='_ensure_grid' else SCAN))
    for start,end,text in sorted(replacements,reverse=True):
        lines[start:end]=[text.strip('\n')+'\n']
    result=''.join(lines)
    changes=[
        ("SCHEMA = 'complete-R711-reference-centred-C1-normal-SO3-world-geometry-and-original-192-amplitude-rows-v1'",
         "SCHEMA = 'complete-R715-C1-material-envelope-world-geometry-and-preserved-prefix-rows-v1'"),
        ('import numpy as np\n','import numpy as np\nimport torch\n\nMATERIAL_ENVELOPE_MEMORY_SHA256 = '+repr(memory_sha)+'\nMATERIAL_ENVELOPE_ROWS_SHA256 = '+repr(rows_sha)+'\n'),
        ('amplitude_top_distance=4):','amplitude_top_distance=4, envelope=None):'),
        ("or set(fields)-set(KEYS)-{'rho0', 'closure_delta'}):",
         "or set(fields)-set(KEYS)-{'rho0', 'closure_delta', 'centered_closure_residual'}):"),
        ('        self.budgets = budgets\n','''        self.budgets = budgets
        if envelope is None or sha(type(envelope).__init__.__code__.co_filename) != MATERIAL_ENVELOPE_MEMORY_SHA256:
            raise ValueError('The complete actual envelope consumer is required')
        if envelope.model_identity != problem.identity:
            raise ValueError('The envelope belongs to another full physical model')
        self.envelope = envelope
        self.envelope_rows = load_source(Path(__file__).with_name('complete_material_envelope_rows.py'),
            MATERIAL_ENVELOPE_ROWS_SHA256)
        self._extra_grid = None
        self._extra_complete = False
'''),
        ("        for name in ('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain'):",
         "        if sha(problem.base.make_query.__code__.co_filename) != BASE_SOURCE_SHA256:\n            raise ValueError('Historical grid queries require the actual complete base query maker')\n        for name in ('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain', 'fields_torch'):"),
        ('        self._grid = None\n        self._last_scan = None\n',
         '        self._grid = None\n        self._extra_grid = None\n        self._extra_complete = False\n        self._last_scan = None\n'),
        ('        return matrix, result_bounds, metadata\n',
         '        return self.envelope_rows.append_rows(self,matrix,result_bounds,metadata,transpose,coordinate_size,\n            active_band=active_band,block_columns=block_columns)\n'),
        ("        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),",
         "        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),\n            material_envelope_memory_source_sha256=MATERIAL_ENVELOPE_MEMORY_SHA256,\n            material_envelope_rows_source_sha256=MATERIAL_ENVELOPE_ROWS_SHA256,\n            material_envelope_definition_identity_sha256=self.envelope.identity,\n            complete_old_current_grid_union=True,unknown_historical_protected_order_reconstructed=False,")]
    for old,new in changes:
        count=result.count(old)
        expected=2 if old=='        self._grid = None\n        self._last_scan = None\n' else 1
        if count!=expected:
            raise ValueError('Literal complete-body derivation mismatch '+repr(old[:80])+': '+str(count))
        result=result.replace(old,new)
    ast.parse(result)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent',type=Path,required=True)
    p.add_argument('--memory',type=Path,required=True)
    p.add_argument('--rows',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    a=p.parse_args()
    result=derive(a.parent.read_text(),hashlib.sha256(a.memory.read_bytes()).hexdigest(),
        hashlib.sha256(a.rows.read_bytes()).hexdigest())
    if a.verify_existing:
        if a.output.read_text()!=result:
            raise ValueError('Actual full new body differs from its complete derivation')
    else:
        a.output.write_text(result)
    print(hashlib.sha256(result.encode()).hexdigest(),len(result.encode()))


if __name__=='__main__':
    main()
