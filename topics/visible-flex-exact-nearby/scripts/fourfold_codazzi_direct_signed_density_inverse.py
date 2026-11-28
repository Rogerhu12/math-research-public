"""ASQ25. A new direct C solve and full ordinary signed residual on the genuine physical row."""
from fractions import Fraction

GRID, TRIAL, HEAD, SOURCE, MODEL, LOW=8192,1024,4096,2560,512,96

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def exact_source_contributions(api,source):
    require(len(source)==MODEL and all(v.is_finite() for v in source),"full original signed model source")
    p=[(abs(v).upper()/(4*n)).upper() for n,v in enumerate(source,1)]
    i2=(2*sum((x*x for x in p),api.zero)).sqrt().upper()
    w=sum(p,api.zero).upper()
    fees=[(api.rational(Fraction(".348"))*i2).upper(),
          (api.rational(2).sqrt()*api.rational(Fraction(".06524"))*w).upper()]
    return min(fees),fees

def proposal_matrix(np,pgrid):
    """Only proposes a trial. All node errors, projection errors and tails are checked independently below."""
    require(len(pgrid)==GRID,"entire saved 8192 compound")
    points=np.asarray([float(v.mid()) for v in pgrid])
    require(np.all(np.isfinite(points)),"finite trial phase nodes")
    phase=-4j*points
    matrix=np.empty((TRIAL,TRIAL),dtype=np.complex128)
    for k in range(1,TRIAL+1):
        # integral(exp(+4iny-4ik phat(y))) in the original positive input block
        matrix[k-1]=np.fft.ifft(np.exp(k*phase))[1:TRIAL+1]
    return matrix

def trial_from_matrix(c,matrix,columns):
    np=c.np
    dims=(TRIAL,len(columns))
    rhs=np.array([[complex(float(col[n].real.mid()),float(col[n].imag.mid())) for col in columns]
                  for n in range(TRIAL)],dtype=np.complex128)
    require(rhs.shape==dims,"all finite RHS")
    try:
        trial=np.linalg.solve(matrix,rhs)
        choice="finite_same_sign_complex_system"
    except np.linalg.LinAlgError:
        trial=rhs
        choice="original_finite_RHS_as_trial"
    require(np.all(np.isfinite(trial)),"full dyadic trial")
    return c.CBox(c.Box(trial.real),c.Box(trial.imag)),choice

def midpoint_box(c,x):
    return c.Box(x.lo+(x.hi-x.lo)/2)

def complex_rows(c,batch,columns):
    return c.CBox(batch.whole_real(c,[[v.real for v in row] for row in columns]),
                  batch.whole_real(c,[[v.imag for v in row] for row in columns]))

def all_residual_rows(c,api,batch,pgrid,trial,vcols,progress,partial):
    """All4096 signed same-sign physical output coefficients before taking any modulus."""
    np=c.np
    width=len(vcols)
    require(trial.real.lo.shape==(TRIAL,width) and all(len(v)==SOURCE for v in vcols),"all trial and finite exact source rows")
    spectrum=c.zeros((GRID,width))
    spectrum[1:TRIAL+1]=trial
    samples=c.fft.fft(spectrum,inverse=True)*GRID
    abs_samples=c.Box(samples.magnitude_upper())
    step=complex_rows(c,batch,[[api.acb((4*g).cos(),-(4*g).sin())] for g in pgrid])
    center=c.CBox(midpoint_box(c,step.real),midpoint_box(c,step.imag))
    tau=c.Box((step-center).magnitude_upper())
    power=c.CBox(c.Box(np.ones((GRID,1))))
    radius=c.Box(np.zeros((GRID,1)))
    coefficients=c.zeros((HEAD,width))
    z=c.zeros((HEAD,width))
    z[:SOURCE]=complex_rows(c,batch,[[v[n] for v in vcols] for n in range(SOURCE)])
    for k in range(1,HEAD+1):
        product=power*center
        power=c.CBox(midpoint_box(c,product.real),midpoint_box(c,product.imag))
        rounding=c.Box((product-power).magnitude_upper())
        radius=c.add_upper(radius,c.mul_upper(c.add_upper(c.Box(1.),radius),tau),rounding)
        row=samples*power
        value=c.CBox(c.reduce_box(row.real,axis=0)/GRID,c.reduce_box(row.imag,axis=0)/GRID)
        fee=c.upper(c.reduce_box(c.mul_upper(abs_samples,radius),axis=0)/GRID)
        coefficients[k-1]=value.pad(fee)-z[k-1]
        if k%128==0:
            partial(k,power,radius,coefficients[:k])
            progress("whole_direct_same_sign_residual",{"complete_modes":k,"end":HEAD,"columns":width})
    return coefficients

def evaluate(c,api,batch,pgrid,eta,ep,model_columns,finite_source_columns,matrix,io,stage,progress):
    width=len(model_columns)
    require(0<eta<1 and ep>0 and width>0 and len(finite_source_columns)==width,"whole compound and true lift error")
    require(all(len(v)==MODEL for v in model_columns) and all(len(v)==SOURCE for v in finite_source_columns),
            "every signed source and full model row")
    trial,choice=trial_from_matrix(c,matrix,finite_source_columns)
    trial=io.complex(stage+"_exact_dyadic_trial",trial,exact=True)
    def partial(k,power,radius,rows):
        io.checkpoint(stage,{"complete_modes":k,"total":HEAD,"columns":width},
                      power=power,radius=radius,signed_residual=rows)
    defects=all_residual_rows(c,api,batch,pgrid,trial,finite_source_columns,progress,partial)
    defects=io.complex(stage+"_whole_signed_residual_4096",defects)
    # Convert scalar boxes by exact enclosure; retain every signed cross term.
    def at(x):
        return batch.box_ball(c,x)
    u=[[api.acb(at(trial.real[n,j]),at(trial.imag[n,j])) for n in range(TRIAL)] for j in range(width)]
    sigma=api.rational(1,256)
    q=(-4*(1-eta)*sigma).exp().upper()
    require(q<1,"entire signed compressed-density tail")
    alias_den=1-(-4*GRID*sigma).exp().upper()
    require(alias_den.lower()>0,"positive complete two-ray quadrature denominator")
    alias=[(2*((-4*GRID+4*k*(1+eta))*sigma).exp()/alias_den).upper() for k in range(1,HEAD+1)]
    alias_l2=(2*sum((a*a for a in alias),api.zero)).sqrt().upper()
    tail_unit=(api.rational(2).sqrt()*q**(HEAD+1)/(1-q*q).sqrt()).upper()
    caps,centres=[],[]
    for j in range(width):
        ws=[abs(x).upper() for x in u[j]]
        W=sum((x*(4*n*sigma).exp() for n,x in enumerate(ws,1)),api.zero).upper()
        U=(2*sum((x*x for x in ws),api.zero)).sqrt().upper()
        U1=(2*sum(((4*n*x)**2 for n,x in enumerate(ws,1)),api.zero)).sqrt().upper()
        alph,alph_both=exact_source_contributions(api,model_columns[j])
        phase_fee=(ep*(275*U+api.rational(Fraction("1.07"))*U1)).upper()
        positives=[api.acb(at(defects.real[i,j]),at(defects.imag[i,j])) for i in range(HEAD)]
        # Sum the coefficientwise complete aliases before the ordinary norm.
        h=(2*sum(((abs(x).upper()+W*a)**2 for x,a in zip(positives,alias)),api.zero)+(W*tail_unit)**2).sqrt().upper()
        error=(api.rational(Fraction("1.11"))*(h+phase_fee+alph)).upper()
        caps.append(dict(directed_head_and_infinite_tail=h,inverse_radius=error,
                 physical_phase_map_fee=phase_fee,both_source_alpha_fees=alph_both,
                 positive_exponential_norm=W,trial_L2=U,trial_D1_L2=U1,
                 whole_trapezoidal_alias=(W*alias_l2).upper(),whole_infinite_tail=(W*tail_unit).upper()))
        centres.append([v.real-v.imag for v in u[j][:LOW]])
    gram=[]
    for j in range(width):
        row=[]
        for m in range(width):
            if m<j:
                row.append(gram[m][j])
                continue
            a,b=defects[:,j],defects[:,m]
            entry=2*at(c.reduce_box(a.real*b.real+a.imag*b.imag,axis=0))
            row.append(entry)
        gram.append(row)
    return {"exact_trial":trial,"signed_centres":centres,"whole_upper_records":caps,"signed_grid_Gram":gram,
            "dyadic_proposal":choice,"complete_head":HEAD,"complete_source":SOURCE,"infinite_tail_paid":True}
