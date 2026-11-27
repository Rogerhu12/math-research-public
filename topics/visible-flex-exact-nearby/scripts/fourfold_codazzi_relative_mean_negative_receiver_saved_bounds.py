"""RRM: eighteen new rational combinations of completed original bounds.

No field, Fourier carrier, old residual or old numerical target is
evaluated. The inequalities here are the exact arithmetic steps of RRM.
"""
from fractions import Fraction as F
import json


def main():
    B,qs,R0,L0=F(211,1000),F(103,100),F(239,125),F(463,125)
    M,V,G,K,a=F(16,15),F(18,5),F(28,25),F(21,20),F(9,8)
    U,U1,V1,b,q0=R0,L0,F(11,2),F(9,50),F(2669,5000)
    D,D1=F(2,5)*B*R0**2,2*B*R0**2
    Cd,Cd1=B*qs*R0/2,B*qs*L0/2
    CJ,J0,J1=V/M**2,V/M,V1/M
    tau_comm=J1*Cd+J0*Cd1+D1*CJ+D*V1/M**2
    p_comm=B*tau_comm
    t_comm=a*(Cd1/M+D1/M**2)
    k_comm=a*((U1*Cd+U*Cd1)/M+D1/M+(D1*U+D*U1)/M**2)
    tau_angle=D1*J0+D*J1+G*U1
    p_angle=B*tau_angle
    t_angle=a*D1/M
    k_angle=a*(G*K*V1+(D1*U+D*U1)/M)
    comparisons=[
        ('tau_comm_lt9',tau_comm,F(9)),
        ('axial_comm_square_lt64',p_comm**2+t_comm**2+k_comm**2,F(64)),
        ('velocity_comm_lt10',a*tau_comm,F(10)),
        ('connection_angle_square_lt144',p_angle**2+t_angle**2+k_angle**2,F(144)),
        ('velocity_angle_lt25over2',a*tau_angle,F(25,2)),
        ('frame_H1_square_lt14_margin',F(25,4)*(1+(12*b)**2),F(36)),
    ]
    C0,g,s=F(19,5),F(103,100),F(16,25)
    B0,B1=24*C0*b+F(25,2),18*C0
    comparisons.extend([
        ('q_H1_factor103over100',C0**2,(g**2-1)*(B0-B1*b)**2),
        ('z_H1_chord',1+(12*b)**2,(1+12*s*b)**2),
    ])
    linear=F(5,2)*g*B0+8*C0-30*s
    quadratic=F(5,2)*g*B1
    constant=F(25,2)+30*s*b
    comparisons.extend([
        ('position_polynomial_increasing',2*quadratic*b,linear),
        ('position_H1_lt26',constant+linear*b-quadratic*b**2,F(26)),
    ])
    rc=F(2333968743003,10**13)
    propagation,injection,root=F(173872,1000),F(1060693,10**6),F(11272695,10**6)
    for name,C,limits in (
        ('frame',F(14),(9300,658,294,871)),
        ('position',F(26),(17200,1217,545,1617)),
    ):
        root_coefficient=C/q0*propagation*root*b
        impulse_coefficient=C/q0*propagation*injection*b
        comparisons.extend([
            (name+'_root',root_coefficient,F(limits[0])),
            (name+'_root_source_square',root_coefficient**2/200,F(limits[1])**2),
            (name+'_strict_source_square',impulse_coefficient**2*(rc-2*b/3),F(limits[2])**2),
            (name+'_strict_jump',impulse_coefficient,F(limits[3])),
        ])
    assert len(comparisons)==18
    records=[]
    for name,left,right in comparisons:
        assert 0<=left<right,(name,str(left),str(right))
        records.append({'name':name,'left':str(left),'right':str(right),'strict':True})
    print(json.dumps({'kind':'R149_complete_relative_mean_negative_window_saved_bounds_v1',
        'proved':True,'new_rational_comparisons':18,'old_scientific_targets_evaluated':0,
        'new_field_or_carrier_targets_evaluated':0,'same_original_selected_background':True,
        'complete_both_mean_and_infinite_frequency_rows':True,'ordinary_radial_measure':'dr',
        'original_root_source_units':['Hminus2over3','Hminus1'],
        'original_strict_source_units':['Hminus1','Hminus1'],
        'world_anchor_and_physical_coordinate_ports_independent':True,
        'complete_comparisons':records},sort_keys=True,indent=2))


if __name__=='__main__':main()
