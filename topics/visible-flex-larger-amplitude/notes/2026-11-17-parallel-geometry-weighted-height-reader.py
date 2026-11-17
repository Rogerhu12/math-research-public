"""The same actual-height reader in the fixed physical angle phi.

The JSON state contains Ptilde=rho*P, the nonconstant physical cosine K,
and the ordinary physical-angle mean c.  The full frozen rho coefficients
are retained.  No material-angle truncation is substituted for this field.
"""
from pathlib import Path
import importlib.util
import numpy as np

_path = Path(__file__).with_name('2026-11-17-parallel-geometry-tail-readout.py')
_spec = importlib.util.spec_from_file_location('unweighted_height_reader', _path)
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)


class HeightReader(_base.HeightReader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rho_coefficients = np.asarray(self.data['rho_cos_coefficients'])
        frequency = 2*np.arange(1, len(self.rho_coefficients)+1)
        if self.N <= 2*frequency[-1]:
            raise ValueError('The actual complete rho must fit below angular Nyquist')
        self.rho = 1+np.cos(self.angle[:, None]*frequency)@self.rho_coefficients
        self.rho_phi = -np.sin(self.angle[:, None]*frequency)@(frequency*self.rho_coefficients)
        if np.min(self.rho) <= 0:
            raise ValueError('The fixed physical angular density must be positive')

    def mean_fields(self, Ptilde, Ttilde, K, z):
        rho, rho_phi = self.rho[None, :], self.rho_phi[None, :]
        P = Ptilde/rho
        T = Ttilde/rho**2-Ptilde*rho_phi/rho**3
        fields = super().mean_fields(P, T, K, z)
        BK, BT = 1+fields['BK1'], 1+fields['BT1']
        # These are derivatives of rho*B with respect to Ptilde, K and
        # Ttilde=d_phi Ptilde.  Constants can be subtracted from the Kbar_r
        # and Ttilde_r coefficients because their literal Fourier means vanish.
        fields['B'] = rho*fields['B']
        fields['BP'] = fields['BP']-BT*rho_phi/rho**2
        fields['BK1'] = rho*BK-1
        fields['BT1'] = BT/rho-1
        fields['Bz'] = rho*fields['Bz']
        # The base reader's mu=1+c+mean(BK1-K-(1+z)Ttilde) is now exactly
        # mean(rho*BK), since mean(K)=c and mean(Ttilde)=0.  The same chain
        # therefore gives the derivative of this literal weighted mean root.
        return fields
