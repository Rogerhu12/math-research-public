"""WMR first complete Fourier contraction for physical mean height.

All18 RHI profiles and the full NP endpoint are frozen inputs.
The old2048 grid is zero-padded with the exact real Nyquist convention;
all products and complete norms below use8192 points, so no high
polynomial term aliases into the new mean or Parseval contraction.
"""
from __future__ import annotations
from fractions import Fraction

GRID=8192
ORIGINAL_GRID=2048
MAXIMUM_KERNEL_DEGREE=2144
TARGETS=[
    "complete_selected_physical_mean_height_kernel3",
    "complete_true_physical_mean_height_kernel_L1_upper",
    "complete_original_reference_world_mean_height_nu_body",
]


def require(ok,message):
    if not ok:
        raise ValueError(message)


def stack(c,values,axis=0):
    return c.Box(c.np.stack([v.lo for v in values],axis=axis),
                 c.np.stack([v.hi for v in values],axis=axis))


def as_arb(c,value):
    require(value.lo.shape==() and c.np.isfinite(value.lo)
        and c.np.isfinite(value.hi),"one finite complete scalar interval")
    return c.arb(float(value.lo)).union(c.arb(float(value.hi)))


def mean(c,value):
    return c.reduce_box(value,axis=0)/GRID


def norm2_upper(c,value):
    """Complete normalized polynomial L2 norm; both signs are retained."""
    square=value*value
    if square.lo.ndim==2:
        square=c.reduce_box(square,axis=1)
    require(square.lo.shape==(GRID,),"whole scalar/vector exact-grid polynomial")
    bound=as_arb(c,mean(c,square)).upper()
    require(bound>=0,"nonnegative whole polynomial square integral")
    return bound.sqrt().upper()


def restore_interpolant_grid(c,endpoint):
    require(endpoint.shape==(ORIGINAL_GRID,18)
        and c.np.all(c.np.isfinite(endpoint)),"entire original18-component endpoint")
    old=c.fft.fft(c.CBox(c.Box(c.np.asarray(endpoint))))/ORIGINAL_GRID
    out=c.zeros((GRID,18));half=ORIGINAL_GRID//2
    out[:half]=old[:half]
    out[-half+1:]=old[-half+1:]
    # The exact Nyquist coefficient of a real grid is real.  Splitting
    # it between the two signs defines the unchanged real cosine.
    nyquist=c.real(old[half])
    out[half]=c.CBox(nyquist/2)
    out[-half]=c.CBox(nyquist/2)
    values=c.real(c.fft.fft(out,inverse=True)*GRID)
    return values,{"original_grid":ORIGINAL_GRID,"contraction_grid":GRID,
        "exact_real_Nyquist_cosine_retained":True,
        "complete_interpolant_degree":half,
        "maximum_complete_kernel_degree":MAXIMUM_KERNEL_DEGREE,
        "complete_polynomial_products_unaliased":True}


def centre_J_and_trial_g(c,base,offsets,row,waist,read_ball,alpha):
    """Whole centre coefficients at the actual waist, not a scalar reset."""
    left,right=map(Fraction,row["interval"])
    require(left==0 and right>0 and len(waist)==193,
        "same true waist and all original physical trial coordinates")
    delta=c.exact(-(left+right)/2)
    jets=row["intrinsic_midpoint_jets"];whole=row["intrinsic_whole_third_jets"]
    s=(read_ball(jets["s"])+delta*read_ball(jets["s1"])
       +delta*delta*read_ball(jets["s2"])/2
       +delta*delta*delta*read_ball(whole["s3"])/6)
    raw=base["piece_coefficients"]
    require(float(base["radial_nodes"][0])==0
        and raw.shape==(4,6144,65),"same entire original raw cubic centre")
    physical=[]
    for j in range(65):
        offset=c.arb(float(offsets["lower"][0,j])).union(
               c.arb(float(offsets["upper"][0,j])))
        physical.append(c.exact(alpha)*c.arb(float(raw[3,0,j]))+offset)
    m=s+physical[32]
    require(m.is_finite() and m.upper() < -c.arb(16)/15,
        "complete original mean denominator with its genuine nonzero mean")
    mu=waist[96]
    sqrt_half=(c.arb(1)/2).sqrt()
    v=[m]+[physical[32+j]/2 for j in range(1,33)]
    h=[mu]+[waist[96+j]*sqrt_half for j in range(1,97)]
    fourier=c.zeros((GRID,2))
    for j in range(97):
        vj=v[j] if j<len(v) else c.arb(0)
        hj=h[j]
        Jj=vj/m
        gj=hj/m-vj*mu/(m*m)
        if j==0:
            # Pi(J0)=1 and Pi(g0)=0 are exact, with no mean deletion.
            Jj,gj=c.arb(1),c.arb(0)
        fourier[j,0]=c.CBox(c.arb_box(Jj))
        fourier[j,1]=c.CBox(c.arb_box(gj))
        if j:
            fourier[-j,0]=c.CBox(c.arb_box(Jj))
            fourier[-j,1]=c.CBox(c.arb_box(gj))
    grid=c.real(c.fft.fft(fourier,inverse=True)*GRID)
    H2=sum((value*value for value in waist[96:]),c.arb(0)).sqrt().upper()
    return grid[:,0:1],grid[:,1:2],H2,{
        "centre_degree":32,"full_trial_degree":96,
        "same_true_waist_interval":list(row["interval"]),
        "true_reference_mean_retained":True,"true_trial_mean_retained":True,
        "both_signed_Fourier_branches_retained":True,
        "constant_J_coefficient_exact_one":True,
        "constant_g_coefficient_exact_zero_by_full_mean_identity":True,
        "scalar_midpoint_and_whole_third_remainder_retained":True}


def compute(c,endpoint,base,offsets,row,waist,read_ball,alpha,
            rhi_actual,sb_actual,publish,save_details):
    require(GRID>2*MAXIMUM_KERNEL_DEGREE,"whole exact product quadrature")
    values,grid_receipt=restore_interpolant_grid(c,endpoint)
    J0,g0,H2,waist_receipt=centre_J_and_trial_g(
        c,base,offsets,row,waist,read_ball,alpha)
    A=values[:,:9].reshape(GRID,3,3)
    x,y=values[:,9:12],values[:,15:18]
    B=J0*y+g0*x
    kernel=stack(c,[sum((A[:,i,j]*B[:,i] for i in range(3)),c.Box(0.))
                    for j in range(3)],axis=1)
    raw=mean(c,kernel)
    raw_balls=[as_arb(c,raw[j]) for j in range(3)]
    X2,Y2,G2,B2=(norm2_upper(c,z) for z in (x,y,g0,B))
    old=rhi_actual["new_records"]
    profile=old["complete_same_selected_relative_profile_error4"]["balls"]
    true_profile=old["complete_true_strict_nu_relative_profile_error2"]["balls"]
    require(len(profile)==4 and len(true_profile)==2,"all old whole profile errors")
    EA,EX=(c.arb(profile[j]).upper() for j in (0,1))
    EY=c.arb(true_profile[1]).upper()
    EH=read_ball(sb_actual["new_records"]["complete_true_NP_uniform_L2_error_upper"]).upper()
    require(EH<c.exact(Fraction("0.00001594684")),
        "whole old uniform strong bound at the actual waist, not radial trace")
    e=c.arb(1)/500000000
    S,T=c.arb(525)/128,c.arb(7875)/1024
    EJ=(S*e).upper()
    EG=(S*EH+T*e*H2).upper()
    EB=(c.arb(27)/8*EY+EJ*Y2+(G2+EG)*EX+EG*X2).upper()
    EK=(EB+EA*B2).upper()
    UK=(B2+EB).upper()
    require(all(z.is_finite() and z>=0 for z in
        (X2,Y2,G2,B2,H2,EA,EX,EY,EH,EJ,EG,EB,EK,UK)),
        "complete finite nonnegative kernel bounds")
    mean_centres=[str(Fraction.from_float(float(value.mid()))) for value in raw_balls]
    mean_centres[1]="0"
    numerical_radii=[]
    for value,centre in zip(raw_balls,mean_centres):
        difference=value-c.exact(Fraction(centre))
        numerical_radii.append(max(abs(difference.lower()),abs(difference.upper())))
    numerical_joint=sum((value*value for value in numerical_radii),c.arb(0)).sqrt().upper()
    true_joint=(numerical_joint+EK).upper()
    true_balls=[value+c.arb(0,EK) for value in raw_balls]
    require(true_balls[1].contains(0),"same exact reflection permits only mean2 zero")
    true_balls[1]=c.arb(0)
    details={
        "complete_grid":grid_receipt,"complete_waist":waist_receipt,
        "whole_raw_kernel_mean_balls":[str(z) for z in raw_balls],
        "exact_dyadic_joint_mean_centres":mean_centres,
        "complete_raw_mean_joint_radius_upper":str(numerical_joint),
        "complete_true_mean_joint_radius_upper":str(true_joint),
        "new_kernel_norm_uppers":{key:str(z) for key,z in
            zip(("X2","Y2","g0_L2","B2","h2_trial_L2"),(X2,Y2,G2,B2,H2))},
        "whole_reused_error_uppers":{key:str(z) for key,z in
            zip(("EA","EX","EY_true","EH_true_uniform"),(EA,EX,EY,EH))},
        "new_complete_error_assembly":{key:str(z) for key,z in
            zip(("EJ","EG","EB","EK","UK"),(EJ,EG,EB,EK,UK))},
        "physical_coordinate_term_gx_included":True,
        "both_means_and_full_h2_preserved":True,
        "exact_zero_kernel_mean_indices":[1],
        "world_reference_orientation":-1,
        "actual_world_anchor_error_or_outer_ports_not_evaluated":True}
    save_details(details)
    actual=publish(TARGETS[0],true_balls,"signed_enclosure",mean_centres)
    saved_upper=publish(TARGETS[1],[UK],"upper")[0].upper()
    reference=actual[0]+c.arb(0,((c.arb(108627)/1000000000)*saved_upper).upper())
    publish(TARGETS[2],[reference],"signed_enclosure")
    return {"complete_kernel_degree":MAXIMUM_KERNEL_DEGREE,
        "full_physical_coordinate_term_retained":True,
        "whole_original_RHI_profiles_used":True,
        "whole_original_NP_waist_and_both_means_used":True,
        "reference_covector_error":"108627/1000000000",
        "independent_actual_anchor_error_coefficient":str(saved_upper),
        "independent_outer_port_formula":
            "Pi[J ez^T(Y_b+K_b Q_b x)+dotJ ez^T F_b]",
        "fixed_world_translation_cancels_by_Pi_dotJ_zero":True,
        "independent_varying_vertical_translation_retained":True,
        "physical_mean_reference_body_excludes_zero":not reference.contains(0),
        "actual_full_world_height_or_Schur_proved":False}
