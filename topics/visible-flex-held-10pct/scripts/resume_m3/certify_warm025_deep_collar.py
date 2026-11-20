#!/usr/bin/env python3
"""Actual M24 warm-.25 deep physical-R collar and R58 background disk.

The last saved stage's literal Cartesian Fourier two-jets define a NEW exact
shared-Hermite map. The planar FD rr values are parameters of this map, not
claimed derivatives of the original unprojected shooting solution. Nonlinear
perturbations are killed after this one finite collar; only the already proved
true 4.625 rotational background continues to its C2 planar cuff/disk.
"""
import argparse,hashlib,json,math,time
from fractions import Fraction as Q
from pathlib import Path
from math import comb

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):
    x=float(x)
    if not math.isfinite(x):raise ValueError('Nonfinite literal datum')
    return Q.from_float(x)
def upper(x):
    v=float(x)
    return math.nextafter(v,math.inf) if fq(v)<x else v
def lower(x):
    v=float(x)
    return math.nextafter(v,-math.inf) if fq(v)>x else v
def sqrt_upper(x):
    if x<0:raise ValueError('Negative exact square')
    scale=10**100
    k=math.isqrt(x.numerator*scale*scale//x.denominator)
    if k*k*x.denominator<x.numerator*scale*scale:k+=1
    return Q(k,scale)
def der(p):return [(i+1)*p[i+1] for i in range(len(p)-1)]
def val(p,x):
    v=Q(0)
    for a in p[::-1]:v=v*x+a
    return v
def bernstein(p):
    n=len(p)-1
    return [sum((p[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),Q(0)) for k in range(n+1)]

# Right-end Hermite basis: common zero 2-jet at u=0; prescribed 2-jet at u=1.
H=[[Q(0),0,0,Q(10),-Q(15),Q(6)],
   [Q(0),0,0,-Q(4),Q(7),-Q(3)],
   [Q(0),0,0,Q(1,2),-Q(1),Q(1,2)]]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('stage-data','stage-packet','tail-constants','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    data=json.loads(a.stage_data.read_text());packet=json.loads(a.stage_packet.read_text())
    constants=json.loads(a.tail_constants.read_text())
    definition={key:constants[key] for key in ('parameters','cells','checkpoint_sha256','factory_sha256')}
    definition_sha=hashlib.sha256(json.dumps(definition,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
    assert definition_sha=='e764e2cc370f0b7a8a55324f2744702017c16690195f45db92ca66b9781bae56'
    assert data['status']=='existing_stage_literal_R_two_jet_data_exported'
    assert packet['status']=='existing_native_flow_exact_input_states_matched'
    assert data['inputSHA256']==sha(a.stage_packet)
    assert data['stage']==packet['stage']['stage']==1151
    assert packet['checkpoint']['sha256']=='302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de'
    assert packet['all_stage_input_maximum_difference']==0
    assert packet['checkpoint']['converged'] and packet['checkpoint']['residual']<2e-9
    assert data['finiteScope']['M']==24 and data['finiteScope']['quadrature']==512
    assert data['rawCell']==7 and data['rawSegment']==0 and data['rawLeft']==0
    params=constants['parameters'];actual=data['physicalParameters']
    assert all(key in actual and actual[key]==value for key,value in params.items())
    factories=[digest for name,digest in data['sourceSHA256'].items() if name.endswith('/closing_weighted_tail.mjs')]
    assert factories==[constants['factory_sha256']]
    assert params['valleyControls'][0]==4.625 and params['protectCell']==160
    assert packet['inner_mean_perturbation_and_background']==[0.,0.]
    node=data['nodes'][0]
    assert node['xi']==0 and node['sourceX']==0 and node['meanPerturbation']==node['meanBackground']==0
    R0=fq(node['radiusJS']);cuff=fq(params['rCuff']);Ri=(R0+cuff)/2;L=R0-Ri
    assert Q(1,25)<cuff<Ri<R0<Q(3,10)
    planar=list(map(int,data['planarModes']));height=list(map(int,data['heightModes']))
    modes=planar+height;P=len(planar);C=len(modes)
    assert height==list(range(0,73,3)) and len(node['coefficients'])==3
    jet=[[fq(x)*(1 if j<P else -1) for j,x in enumerate(row)] for row in node['coefficients']]
    assert all(len(row)==C for row in jet)
    B=[[Q(0)]*3 for _ in range(3)]
    norms=[[Q(0)]*C for _ in range(3)]
    matched=0
    for index,m in enumerate(modes):
        pp=[sum((L**j*jet[j][index]*Q(H[j][k]) for j in range(3)),Q(0)) for k in range(6)]
        c=pp
        for radial in range(3):
            assert val(c,Q(0))==0 and val(c,Q(1))/L**radial==jet[radial][index]
            matched+=2
            bb=max(map(abs,bernstein(c)))/L**radial;norms[radial][index]=bb
            for angular in range(3):B[radial][angular]+=abs(m)**angular*bb
            c=der(c)
    # R58 exact inputs and geometry, for THIS 4.625 background. No 3.125
    # finite integral or old nonrotating field constant is reused.
    K0=Q(8);W=Q(41,100);Rmin=Q(1,25)
    Zmin,Zmax=Q(1,10),Q(32,25)
    Hmax=Q(7446320975220351,288230376151711744)
    Emax=1+W*W
    assert Emax<Q(11,10)**2
    base_radius=sqrt_upper(Q(3,10)**2+(Zmax+Hmax)**2)
    base_support=Q(1,11)
    # Full target-normalized material first derivative, including all modes.
    eta1=sqrt_upper(B[1][0]**2+(B[0][1]/Rmin)**2)
    metric=2*eta1+eta1*eta1
    eta2=sqrt_upper(B[2][0]**2+2*(B[1][1]/Rmin)**2+(B[0][2]/Rmin**2)**2)
    # Ambient normalized Hessian of the background: RR/E <=8 sqrt(Emax),
    # Rtheta/(R sqrt(E)) <=25, thetatheta/R^2 <=25; Frobenius norm <45.
    assert K0*K0*Emax+3/Rmin**2<Q(45)**2
    assert eta1<1
    normal=sqrt_upper(Q(2))*eta1
    curvature=(K0+45*normal+eta2)/(1-eta1)**2
    radius=base_radius+B[0][0]
    support=base_support-base_radius*normal-B[0][0]
    assert metric<Q(1,10**6) and curvature<Q(8001,1000)
    assert radius<Q(67,50) and support>Q(9,100)
    # The same eta1 bounds the planar projection derivative in Euclidean
    # polar coordinates. Its global Lipschitz constant <1 gives injectivity
    # on the disk, since the perturbation vanishes inside Ri.
    report={
        'status':'actual_warm025_deep_C2_collar_and_disk_certified',
        'source_sha256':sha(__file__),'stage_data_sha256':sha(a.stage_data),
        'stage_packet_sha256':sha(a.stage_packet),'tail_constants_sha256':sha(a.tail_constants),
        'true_background_definition_sha256':definition_sha,
        'original_checkpoint_sha256':packet['checkpoint']['sha256'],
        'original_native_record_sha256':packet['native_record']['sha256'],
        'source_stage':1151,'physical_depth':8,'M':24,'spacing':3,
        'planar_fourier_terms':P,'height_fourier_terms':len(height),
        'literal_two_jet_scalars':3*C,'exact_endpoint_scalar_equalities':matched,
        'outer_R_exact':str(R0),'inner_R_exact':str(Ri),'cuff_R_exact':str(cuff),
        'collar_width_exact':str(L),
        'finite_R_Hermite_map_explicit':True,'planar_rr_scope':'literal nodal parameters of the new map; no exact PDE rr claim',
        'physical_height_contract':'r_JS^4 u at the source datum; no replacement by true_R^4 u',
        'upper_height_sign':-1,'mean_contract':'Only perturbation mean is in V; true R58 background primitive separately. Deep inner perturbation mean is exactly zero.',
        'cut_background_height_window_exact':[str(Zmin),str(Zmax)],
        'Fourier_Bernstein_derivative_upper':[[upper(x) for x in row] for row in B],
        'normalized_first_jet_upper':upper(eta1),'normalized_second_jet_upper':upper(eta2),
        'metric_relative_operator_upper':upper(metric),'principal_curvature_upper':upper(curvature),
        'radius_upper':upper(radius),'support_lower':lower(support),
        'disk_planar_projection_Lipschitz_upper':upper(eta1),
        'C2_collar_outer_jet_match_exact':True,'C2_collar_inner_zero_two_jet_exact':True,
        'rotational_background_to_planar_disk':'R58 same frozen 4.625 background and same deep source, with no nonlinear perturbation for R<=Ri',
        'embedding_of_this_disk_component':True,
        'background_integrals_recomputed':False,'nonlinear_solves_executed':0,
        'fullH_tail_solved':False,'prefix_to_tail_Cartesian_seam_proved':False,
        'whole_closed_surface':False,'seconds':time.monotonic()-start}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)
if __name__=='__main__':main()
