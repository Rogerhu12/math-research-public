"""R710. Resume exact represented height paths at the two true scalar-root bracket endpoints."""
from types import SimpleNamespace
import time
import numpy as np
from r641_projected_velocity_frontier import ExtendedFrontier, VelocityFaces, source, LD
from r641_center_implicit_length_faces import CompleteCone
from r641_paid48_source_chart import Paid48Chart
from r641_fixed_physical_center_chart import sparse_affine_coefficients, adaptive
from r632_extremum_physical_faces import near_bound


class Chart(Paid48Chart):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.bracket_cache={}
        self.height_suffix_records=[]
        self.last_bracket_work=None

    def height_key(self,q,control):
        return (np.asarray(q,float).tobytes(),source.shapes.ld_text(control))

    def finish_height(self,q,control,partial):
        ext=np.r_[np.asarray(q,dtype=LD),LD(control)]
        # Only h is involved here. No length or amplitude is needed for this field.
        work={'fields':{'h':partial},'inflight_polynomial_field':partial,'unevaluated_fields':[]}
        checkpoint=dict(shape_parameters=np.asarray(q,float).tolist(),control_LD_decimal=source.shapes.ld_text(control),
                        source_pending_field=partial)
        self.last_bracket_work=checkpoint
        result=self.boxes.close(self,ext,LD(1),LD(1),work)
        field=result['fields']['h']
        checkpoint.update(exact_result=result['exact_remaining_frontier'],field_status=field['state'])
        self.height_suffix_records.append(dict(shape_identity=source.shapes.identity(checkpoint['shape_parameters']),
            control=checkpoint['control_LD_decimal'],exact_result=checkpoint['exact_result']))
        self.bracket_cache[self.height_key(q,control)]=field
        return field

    def _height_bracket(self,q,lo,hi,report):
        records=report['continuous_height_on_scalar_control_bracket']=[]
        for c in (lo,hi):
            key=self.height_key(q,c)
            saved=self.bracket_cache.get(key)
            if saved is None:
                hull=sparse_affine_coefficients(self.extended_h_coeff,np.r_[q,c],self.background_h_coeff)
                if (c==hi and records and records[0]['qualification']['state']=='certified_represented_polynomial'
                        and np.all(self.extended_h_coeff[:,:,-1]>=0)
                        and np.max(hull[1])<adaptive.BOUNDS['h'][1]):
                    # A nonnegative Bernstein control direction makes every high-control point
                    # at least its already strictly legal low-control value. Independently bind
                    # the real high-control upper hull. No low-bound subdivision is due again.
                    saved=dict(field='h',state='certified_represented_polynomial',
                               strict_lower_transferred_from_left_actual_control=True,
                               all_represented_control_Bernstein_coefficients_nonnegative=True,
                               upper_outward_hull_LD_decimal=source.shapes.ld_text(np.max(hull[1])))
                else:
                    saved,_=self.boxes.certify_field('h',hull)
                if saved['state']=='pending':
                    saved=self.finish_height(q,c,saved)
                self.bracket_cache[key]=saved
            records.append(dict(control_LD_decimal=source.shapes.ld_text(c),qualification=saved))
            if saved['state']=='pending':
                raise adaptive.PolynomialPhysicalPending(saved)
            if saved['state']!='certified_represented_polynomial':
                raise FloatingPointError('The selected P-control bracket leaves the original h box')


class BracketFaces(VelocityFaces):
    def __init__(self,graph,curve,args):
        super().__init__(graph,curve,args)
        self.extra=[]
        root=curve['physical_attainers']['scalar_P_root']
        for sign,c,label in ((1.,-graph.root_radius,'left'),(-1.,graph.root_radius,'right')):
            # At fixed bracket control the last basis is an offset. It has no q derivative.
            offset=graph.background_h_coeff+c*graph.extended_h_coeff[:,:,-1]
            layout=SimpleNamespace(h_coeff=[graph.extended_h_coeff[:,:,:-1]],background_h_coeff=[offset],knots=graph.knots)
            h=near_bound(layout,curve,'h',args.height_activity_distance)
            if h is not None and h['inward_sign']==sign:
                # A literal center-coordinate row is already an exact active-coordinate face.
                existing={r['field'] for r in self.normals}
                if not (h['coordinate']==0 and 'center_h' in existing):
                    self.extra.append({**h,'field':label+'_bracket_height','control':source.shapes.ld_text(c)})
            event=next(e for e in root['events'] if e['phase']=='initial_'+label)
            if sign*LD(event['P0_LD_decimal'])<=args.bracket_P_activity_distance:
                qld=np.asarray(curve['shape_parameters'],dtype=LD)
                P=graph._base_map(qld,c,'full')[-1]
                if source.shapes.ld_text(P.value)!=event['P0_LD_decimal']:
                    raise ArithmeticError('Original full bracket P value differs from its accepted scalar integral')
                self.extra.append(dict(field=label+'_bracket_P',gap=float(sign*P.value),
                    value=float(P.value),control=source.shapes.ld_text(c),row=sign*np.asarray(P.derivative[:-1],float)))
        self.normals.extend({k:v for k,v in row.items() if k!='row'} for row in self.extra)

    def bases(self,end_row=None):
        faces=list(super().bases(end_row))
        for rec in self.extra:
            ext=[]
            for active,T in faces:
                row=rec['row']@T
                if np.any(row):
                    ext.append((active+[rec['field']],T@source.complete_nullspace([row],T.shape[1])))
            faces.extend(ext)
        yield from faces

    def feasible(self,direction,active):
        good,signs=super().feasible(direction,active)
        for data in self.extra:
            field=data['field'];row=data['row']
            val=float(row@direction);signs[field]=val
            tol=32*len(direction)*np.finfo(float).eps*np.linalg.norm(row)*np.linalg.norm(direction)
            good=good and (abs(val)<=tol if field in active else val>=0.)
        return bool(good),signs


class BracketCone(CompleteCone):
    def __init__(self,current,graph,args,retained,iteration,enforce_ends):
        self.current,self.clock=current,graph.clock
        self.physical=BracketFaces(graph,current['data']['curve'],args)
        self.end_row=current['jacobian'][0] if enforce_ends else None
        self.factors=[]
        self.record=retained['latest_original_physical_cone_model']=dict(state='building',iteration=iteration,
            normals=self.physical.normals,actual_remaining_true_end_rows_enforced=int(enforce_ends),
            all_256_input_columns=True,faces=[],damped_models=[])
        start=time.monotonic()
        try:
            for active,tangent in self.physical.bases(self.end_row):
                self.clock.check('before_R710_full_original_face')
                item=dict(active=active,dimension=tangent.shape[1],state='pending')
                self.record['faces'].append(item)
                factor=source.EuclideanCompleteRowFactor(current['jacobian']@tangent,-current['residual'],
                    self.clock,source.COUNTS,'R710_'+str(iteration)+'_'+'_'.join(active))
                self.factors.append((active,tangent,factor))
                item.update(state='completed',factor_id=factor.receipt['factor_id'])
            self.record['state']='completed'
        finally:
            self.record['factor_seconds_including_partial']=time.monotonic()-start

    def solve(self,penalty):
        direction,rec=super().solve(penalty)
        baseline=rec['selected']['model_decrease']
        walls=[w for w in [self.physical.velocity,*self.physical.extra] if w is not None]
        if not walls or baseline<=0:
            return direction,rec
        other=self.physical.center_length
        other_active=[r['field'] for r in other.normals]
        T=next(t for a,t in other.bases(self.end_row) if a==other_active)
        rows=np.asarray([w['row'] for w in walls])
        length=np.linalg.norm(rows,axis=1)
        if np.any(length==0):
            return direction,rec
        rows=rows/length[:,None]
        restricted=rows@T
        Q,R=np.linalg.qr(restricted.T,mode='reduced')
        if np.any(np.diag(R)==0):
            return direction,rec
        tests=rec['strict_original_wall_corrections']=[]
        for ratio in (.01,.001,.0001,.00001):
            want=ratio*np.linalg.norm(direction)
            missing=np.maximum(0.,want-rows@direction)
            if not np.any(missing):
                break
            v=direction+T@(Q@np.linalg.solve(R.T,missing))
            active=[s for s in rec['selected']['face'] if s in other_active]
            good,signs=self.physical.feasible(v,active)
            delta=self.current['jacobian']@v
            gain=float(-self.current['residual']@delta-(delta@delta+penalty*(v@v))/2)
            tests.append(dict(ratio=ratio,model_gain=gain,signs=signs,feasible=good))
            if good and all(signs[w['field']]>0 for w in walls) and gain>=.99*baseline:
                rec['strict_correction_selected']=len(tests)-1
                return v,rec
        return direction,rec
