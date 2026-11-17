"""Audit actual Cartesian jets of the radial mixed interpolant, interval by interval.

v and t use the Hermite cubic fixed by nodal values and the complete ODE.
L uses its quadratic nodal interpolant. Derivatives do not assume Gauss and
are not replaced by the root-implied second height derivative. Jumps and
background finite-difference sensitivity are retained explicitly.
"""
import argparse, gzip, hashlib, json
from pathlib import Path
import numpy as np
from mu_free_fields import MuFreeFields
from probe_actual_cell import height_jets
from cartesian_interpolant import cartesian_jets, relative_geometry


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--solution',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a = p.parse_args()
    data = json.loads(gzip.decompress(a.input.read_bytes()))
    solution = json.loads(a.solution.read_text())
    if solution['input']['sha256'] != digest(a.input):
        raise ValueError('Fixed input was changed')
    state_path = Path(solution['checkpoint']['path'])
    if digest(state_path) != solution['checkpoint']['sha256']:
        raise ValueError('Checkpoint was changed')
    array = np.load(state_path)
    x,Y = array['x'],array['Y']
    nodes,param = data['nodes'],data['parameters']
    f = MuFreeFields(param['M'],param['spacing'],param['N'],False,param['mixedProjectionFloor'])
    r = np.array([v['r']for v in nodes]);w=np.array([v['w']for v in nodes]);wr=np.array([v['wr']for v in nodes])
    flow = f.evaluate(Y,r,w,-1.,-wr/w)['flow']
    rows=[];previous=None
    keys=('metric_error','full_tensor_defect','actual_gauss_difference','actual_curvature')
    for j in range((len(x)-1)//2):
        ids=[2*j,2*j+1,2*j+2];l,m,rr=ids;h=x[rr]-x[l]
        L=Y[ids,2*f.d:]
        Lx=np.stack([-3*L[0]+4*L[1]-L[2],L[2]-L[0],L[0]-4*L[1]+3*L[2]])/h
        Lxx=4*(L[0]-2*L[1]+L[2])/(h*h)
        vl,vr=Y[l,:f.d],Y[rr,:f.d];fl,fr=flow[l,:f.d],flow[rr,:f.d]
        vxx=np.stack([6*(vr-vl)/h**2-(4*fl+2*fr)/h,(fr-fl)/h,-6*(vr-vl)/h**2+(2*fl+4*fr)/h])
        row=dict(interval=j,stage=int(nodes[m]['stage']),raw_segment=int(nodes[m]['raw_segment']),
                 x_left=float(x[l]),x_right=float(x[rr]),
                 actual_geometry={k:0. for k in keys},reference_geometry={k:0. for k in keys},
                 height_jet_reference_errors=[0.]*6,cartesian_jet_reference_errors=[0.]*6,
                 cartesian_join_jump=[0.]*6,height_rr_ode_interpolation_gap=0.,
                 background_rr_step_discrepancy=0.,cartesian_rr_background_step_sensitivity=0.,
                 angular_holonomy=0.,translation_period=0.,cartesian_reference_nodes=0)
        for k,n in enumerate(ids):
            node=nodes[n]
            actual,extra=cartesian_jets(f,Y[n],-flow[n,:f.d],vxx[k],-Lx[k],Lxx,r[n],w[n],wr[n],node['wrr'])
            geo=relative_geometry(actual,r[n],w[n],wr[n])
            for key in keys:row['actual_geometry'][key]=max(row['actual_geometry'][key],geo[key])
            for key in ('angular_holonomy','translation_period'):row[key]=max(row[key],extra[key])
            height=np.stack([actual[:,0,2],actual[:,1,2]+w[n],actual[:,2,2],actual[:,3,2]+wr[n],actual[:,4,2],actual[:,5,2]],axis=1)
            reference=np.asarray(node['height_jets'])
            row['height_jet_reference_errors']=np.maximum(row['height_jet_reference_errors'],np.max(abs(height-reference),axis=0)).tolist()
            formal,_=height_jets(f,Y[n],-Lx[k],r[n],w[n],wr[n],flow[n])
            row['height_rr_ode_interpolation_gap']=max(row['height_rr_ode_interpolation_gap'],float(np.max(abs(height[:,3]-formal[:,3]))))
            if node.get('cartesian_jets') is not None:
                cj=np.asarray(node['cartesian_jets']);cj[:,0,2]-=cj[:,0,2].mean()
                row['cartesian_jet_reference_errors']=np.maximum(row['cartesian_jet_reference_errors'],np.max(np.linalg.norm(actual-cj,axis=2),axis=0)).tolist()
                rg=relative_geometry(cj,r[n],w[n],wr[n])
                for key in keys:row['reference_geometry'][key]=max(row['reference_geometry'][key],rg[key])
                row['cartesian_reference_nodes']+=1
            dw=node['wrr_finite_difference_discrepancy']
            row['background_rr_step_discrepancy']=max(row['background_rr_step_discrepancy'],dw)
            if dw:
                changed,_=cartesian_jets(f,Y[n],-flow[n,:f.d],vxx[k],-Lx[k],Lxx,r[n],w[n],wr[n],node['wrr']+dw)
                row['cartesian_rr_background_step_sensitivity']=max(row['cartesian_rr_background_step_sensitivity'],float(np.max(np.linalg.norm(changed[:,3]-actual[:,3],axis=1))))
            if k==0 and previous is not None:
                row['cartesian_join_jump']=np.max(np.linalg.norm(actual-previous,axis=2),axis=0).tolist()
            if k==2:previous=actual
        rows.append(row)
    report=dict(scope=__doc__,input=dict(path=str(a.input),sha256=digest(a.input)),
        solution=dict(path=str(a.solution),sha256=digest(a.solution),finite_residuals_accepted=solution['success']),
        sources={p.name:digest(p)for p in [Path(__file__),Path(__file__).with_name('cartesian_interpolant.py')]},
        parameters=param,actual_geometry={k:max(row['actual_geometry'][k]for row in rows)for k in keys},
        reference_geometry={k:max(row['reference_geometry'][k]for row in rows)for k in keys},
        maximum_height_jet_reference_errors=np.max([row['height_jet_reference_errors']for row in rows],axis=0).tolist(),
        maximum_cartesian_jet_reference_errors=np.max([row['cartesian_jet_reference_errors']for row in rows],axis=0).tolist(),
        maximum_cartesian_join_jumps=np.max([row['cartesian_join_jump']for row in rows],axis=0).tolist(),
        maximum_height_rr_ode_interpolation_gap=max(row['height_rr_ode_interpolation_gap']for row in rows),
        maximum_background_rr_step_discrepancy=max(row['background_rr_step_discrepancy']for row in rows),
        maximum_cartesian_rr_background_step_sensitivity=max(row['cartesian_rr_background_step_sensitivity']for row in rows),
        derivative_order=['position (section vertical mean removed)','r','u','rr','ru','uu'],intervals=rows)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k!='intervals'},indent=2))


if __name__=='__main__':main()
