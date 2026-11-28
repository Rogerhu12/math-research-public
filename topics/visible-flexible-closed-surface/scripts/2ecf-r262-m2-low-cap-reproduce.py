#!/usr/bin/env python3
"""Regenerate both larger-cuff branches and the low-height corrected seeds with the original reported arguments."""
import argparse,json,os,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
p=argparse.ArgumentParser();p.add_argument('--scripts',type=Path,required=True);p.add_argument('--work',type=Path,required=True);a=p.parse_args();S=a.scripts.resolve();W=a.work.resolve();W.mkdir(exist_ok=True,parents=True)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
def w(n):return W/(n+'.json')
def go(script,*args):subprocess.run([sys.executable,str(S/('2ecf-r262-m2-'+script+'.py')),*map(str,args)],check=True)
A='g12-m2-lambda8over5-';C='g12-m2-exact-cuff32-';H='g12-m2-true32-low575-';M=S.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json';sc=F(8,25)/F(json.loads(M.read_bytes())['parameters']['rCuff'])
for tag,l in [(A,F(8,5)),(C,sc)]:go('similar-infinite-tail','--source',w('g12-original-full160-m2-seams'),'--table',W/'g12-full160-m2-physical-table192.npz','--proof',w('g12-m2-real-buffer-seam'),'--manifest',M,'--scale',l,'--out',w(tag+'tail'),'--new-table',W/(tag+'tail.npz'))
for tag,r,cut,out in [(A,.4,.6,'buffer'),(A,.4,.8,'buffer-cut8'),(C,float(sc)*.25,.85,'cut85-buffer')]:go('finite-outer-buffer-actual-II','--source',w(tag+'tail'),'--radius',r,'--cut',cut,'--power',16,'--out',w(tag+out))
for tag,src,b,out,powr,co,fi in [(A,'buffer-matched-short-meridians','buffer','short',15,18,128),(A,'scaled-radius-physical-meridians','buffer-cut8','short-cut8',16,18,128),(C,'low-cap-window-physical-meridians','cut85-buffer','lowcap-cut85',14,18,160),(C,'low-cap-double-return','cut85-buffer','low-double-cut85',15,16,160)]:go(src,'--full',w(tag+'tail'),'--buffer',w(tag+b),'--power',powr,'--coarse',co,'--fine',fi,'--out',w(tag+out))
def setup(t,m,b):return ['--meridian',w(t+m),'--buffer',w(t+b),'--tail-table',W/(t+'tail.npz')]
def act(src,ep,out,*extra):go(src,*b,'--epsilon',ep,'--out',w(out),*extra)
b=setup(A,'short','buffer');act('complete-physical-continuation',.03125,A+'cut6-eps1over32','--steps',14,'--spans',32,'--modes',6)
b=setup(A,'short-cut8','buffer-cut8');act('complete-physical-continuation',.0625,A+'cut8-eps1over16','--steps',14,'--spans',32,'--modes',6);act('deep-active-curvature-response',.125,A+'cut8-curved-eps1over8','--parent',w(A+'cut8-eps1over16'),'--steps',20,'--mu',.03)
b=setup(C,'low-double-cut85','cut85-buffer');act('low-cap-physical-continuation',.03125,C+'low-double-eps1over32','--steps',16,'--spans',32,'--modes',6)
e=['--index',1,'--guide',9.4,'--stadium-p',32];act('low-cap-stadium-active',.0625,H+'small-eps1over16',*e,'--steps',20,'--mu',.015,'--stadium-mix',0);e+=['--stadium-mix',1,'--horizontal-scale',.75,'--vertical-scale',.25];act('low-cap-stadium-active',.34,H+'stadium-eps034',*e,'--steps',24,'--mu',.055)
go('nested-physical-coeffs','--parent',w(H+'stadium-eps034'),'--out',w(H+'stadium-n64'),'--spans',64,'--modes',10);act('low-cap-slab-active',.34,H+'stadium-slab64',*e,'--parent',w(H+'stadium-n64'),'--steps',35,'--mu',.045,'--train-radial',279,'--train-angular',128,'--slab-weight',1.7)
go('low-cap-geometry-observer',*b,'--state',w(H+'stadium-eps034'),'--out',w(H+'stadium-geometric'))
