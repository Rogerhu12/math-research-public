#!/usr/bin/env python3
"""Replace T47 by the effective cyclic4 correspondence in the actual Hecke basis.

The corresponding trace pairing calibrates s via h(B,S_i B).  It does
not assign uncomputed global height values or non47 local contributions.
"""
import argparse,gzip,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path

Q=47**4


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def mm(a,b,q=Q):
    return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*b)] for row in a]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke_height_basis47_certificate.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from p41_cm_height_calibration47 import invert
    files=['p41_small_hecke_cm_transport47_certificate.json.gz','p41_full_chow_heegner_certificate.json.gz','p41_cm_height_calibration47_certificate.json.gz']
    loaded=[read(folder/'data'/name) for name in files]
    old,full,cal=[a for a,b in loaded];inputs={name:b for name,(a,b) in zip(files,loaded)}
    assert old['source_sha256']['p41_full_chow_heegner_certificate.json.gz']==inputs[files[1]]
    assert cal['source_sha256']['p41_full_chow_heegner_certificate.json.gz']==inputs[files[1]]
    indices=old['indices'];position=indices.index(47)
    C=old['basis_matrix_mod47_4'];Ci=old['inverse_basis_matrix_mod47_4']
    G=cal['trace_gram'];identity=[[int(i==j) for j in range(54)] for i in range(54)]
    assert mm(C,Ci)==mm(Ci,C)==identity
    row=[];exact=[]
    for field in full['fields']:
        f=field['factor_descending'][::-1];degree=len(f)-1;assert f[-1]==1
        denominator,numerator=field['directions'][indices.index(2)-1][0]
        a=[F(x,denominator) for x in numerator[::-1]];a += [F(0)]*(degree-len(a))
        c=[F(0)]*(2*degree-1)
        for i,x in enumerate(a):
            for j,y in enumerate(a):c[i+j]+=x*y
        while len(c)>degree:
            leading=c[-1];offset=len(c)-degree-1
            for j,value in enumerate(f):c[offset+j]-=leading*value
            c.pop()
        c[0]-=3
        denominator=math.lcm(*[x.denominator for x in c]);assert denominator%47
        exact.append({'factor_descending':field['factor_descending'],
                      'cyclic4_denominator':denominator,
                      'cyclic4_numerator_ascending':[int(x*denominator) for x in c]})
        row += [x.numerator*pow(x.denominator,-1,Q)%Q for x in c]
    coordinates=mm([row],Ci)[0]
    assert mm([coordinates],C)[0]==row
    assert coordinates[position]==918409 and coordinates[position]%47==29
    changed=[a[:] for a in C];changed[position]=row
    inverse,det=invert(changed,Q)
    assert mm(changed,inverse)==mm(inverse,changed)==identity
    height=mm(changed,G);height_inverse,height_det=invert(height,Q)
    assert mm(height,height_inverse)==mm(height_inverse,height)==identity
    assert det%47==29 and height_det%47==18
    trace_inverse,trace_det=invert(G,Q);assert trace_det%47==46
    assert height_det==det*trace_det%Q
    assert det==old['basis_determinant_mod47_4']*coordinates[position]%Q
    change=identity[:];change=[r[:] for r in change];change[position]=coordinates
    assert mm(change,C)==changed
    labels=[{'kind':'Hecke','index':n,'effective_degree':sum(i for i in range(1,n+1) if n%i==0)} for n in indices]
    labels[position]={'kind':'cyclic4','index':4,'effective_degree':6,'expression':'T2 composed T2 minus3 diagonal'}
    assert all(label['index']%47 for label in labels)
    result={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'dimension':54,
      'input_sha256':inputs,'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'source_sha256':old['source_sha256'],'old_indices':indices,'new_correspondence_labels':labels,
      'replaced_row_1based':position+1,'effective_cyclic4_expression':'T2^2-3*identity; six cyclic4 subgroups',
      'exact_cyclic4_field_coordinates':exact,'cyclic4_coordinates_in_old_Hecke_basis_mod47four':coordinates,
      'coefficient_on_old_T47_mod47four':coordinates[position],
      'basis_change_matrix_mod47four':change,'new_basis_matrix_mod47four':changed,
      'inverse_new_basis_matrix_mod47four':inverse,'trace_gram_mod47four':G,
      'height_matrix_mod47four':height,'inverse_height_matrix_mod47four':height_inverse,
      'determinants_mod47':{'basis':det%47,'trace':trace_det%47,'height':height_det%47},
      'determinants_mod47four':{'basis':det,'trace':trace_det,'height':height_det},
      'unknowns':'same s as R133: h(aB,bB)=Trace(s*a*b), with actual B and the fixed Poincare height',
      'right_hand_side':'actual global h(B,S_i B), including every finite local contribution; not yet evaluated',
      'equation':'height_vector=height_matrix*s_coordinates; no division by logB^2 or47^2',
      'cyclic4_height_identity':'h(B,C4 B)=h(T2 B,T2 B)-3*h(B,B) by actual Rosati symmetry',
      'status':'complete actual prime-to47 Hecke integral basis and unit trace-height calibration; global heights and non47 terms uncomputed'}
    raw=gzip.compress((json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    args.output.write_bytes(raw)
    print('ACTUAL PRIME-TO47 HEIGHT BASIS PASS','row',position+1,'T47 coefficient',coordinates[position],
          'det',det%47,'trace',trace_det%47,'height',height_det%47,
          len(raw),hashlib.sha256(raw).hexdigest(),flush=True)


if __name__=='__main__':main()
