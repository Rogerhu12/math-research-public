#!/usr/bin/env python3
"""Sharpen already proved full-circle component bounds using exact m3 covariance.

If v(psi+2pi/3)=R(2pi/3)v(psi), at least one of its three rotated
x projections has magnitude >=sqrt(3)/2 times its planar norm.  The
same holds for y.  Thus |v|^2 <= 4/3 min(Ax^2,Ay^2)+Az^2 from
full-circle component bounds.  No inverse solve or angular scan is rerun.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse,hashlib,json,math,sys
import numpy as np


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def square_root_upper(x):
    y=math.sqrt(float(x))
    while Q.from_float(y)**2<x:y=math.nextafter(y,math.inf)
    return y


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data',type=Path,required=True)
    p.add_argument('--certificate',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();old_sha=sha(a.certificate)
    c=json.loads(a.certificate.read_text());x=np.load(a.data)
    assert c['input_sha256']==sha(a.data) and c['full_circle']
    assert np.all((x['planar_modes']-1)%3==0)
    assert np.all(x['height_modes']%3==0) and np.all(x['core_frequencies']%3==0)
    c['component_triangle_norm_before_m3_covariance']=c['uniform_delta_norm_angular_then_radial']
    bounds=[]
    for order in c['component_bounds_angular_radial_axis']:
        row=[]
        for vector in order:
            ax,ay,az=[Q.from_float(float(v))for v in vector]
            row.append(square_root_upper(Q(4,3)*min(ax*ax,ay*ay)+az*az))
        bounds.append(row)
    c['uniform_delta_norm_angular_then_radial']=bounds
    c['covariance_sharpening']=dict(scope=__doc__,command=sys.argv,
        component_certificate_sha256=old_sha,source_sha256=sha(Path(__file__)),
        exact_covariance='delta_j^(k)(psi+2pi/3)=R_z(2pi/3) delta_j^(k)(psi), j=0,1,2 and k=0,1',
        new_norm_upper_squared_checked_as_exact_rational=True)
    a.out.write_text(json.dumps(c,indent=2)+'\n')
    print(json.dumps({'uniform_delta_norm_angular_then_radial':bounds,'original_sha256':old_sha,'output_sha256':sha(a.out)}))


if __name__=='__main__':main()
