"""A three-amplitude physical mean functional with the actual JI scalar denominator."""


def coefficient_rows(words,inverse):
    """Unshifted physical coefficients; the normalized mean pairing is bilinear."""
    b=words.b
    au_over_D=b.scale(1/inverse.D,inverse.c_weight)
    tau=b.scale(-1/inverse.eta,b.coeff_I(au_over_D))
    wc=(b.scale(words.K,words.v_minus_m)-words.b0*tau
        +b.scale(words.cB,words.v*b.coeff_I(words.vp*tau)))
    return (tau,au_over_D,b.coeff_P(wc))


def signed_readout(words,coefficients,columns):
    """Merge the *same* physical input column before taking its one true mean."""
    b=words.b;t,ah,aw=coefficients
    value=b.add(b.mul(t,columns['Fg']),b.mul(ah,columns['Fh']),b.mul(aw,columns['Fw']))
    return b.scale(2*words.beta*words.m,b.Pi(value))
