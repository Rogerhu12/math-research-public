# R169. 两条原中央 amplitude 行与完整周期 Frobenius

日期：2026-11-12。**状态：已证明；未得到全部混合 jet 的惰性预算。**

采用 R162 的实际 $A_2=P(s)e^W$、$B=Q(s)e^W$，
$s=u^4$、$P,Q$ 首项均为 $s$。置
$$
 \mathcal L(s)=z/u
   =\sum_{m\ge0}\frac{\binom{2m}{m}}{4^m(4m+1)}s^m,
 \quad Z=(P/s)e^W,\quad V=Q/P-1.
$$
准确有 $w=z^4=s\mathcal L^4$、
$\mathcal L+4s\mathcal L'=(1-s)^{-1/2}$。

## 1. 原两条中央行的准确联立

全特征零换元给
$$
 [z^{4n}]C(s(z))e^{W(s(z))}
 =[s^n]\frac{Ce^W}{\sqrt{1-s}\,\mathcal L^{4n+1}}.
 \tag{1}
$$
令 $p=4r-1\ge7$，
$$
 \mathcal T=\frac{Z}{\sqrt{1-s}\,\mathcal L^2}
               =\sum t_ms^m.
$$
只需它到 $s^{r-1}$ 的整系数，便准确得到
$$
 b_{p+1}(A_2)\equiv t_{r-1},\qquad
 b_{p+1}(B)\equiv[s^{r-1}](1+V)\mathcal T\pmod p.
 \tag{2}
$$
所以两条首中央行同时为零，等价于
$t_{r-1}=0$ 及 $[s^{r-1}]V\mathcal T=0$。
对 $p\ne11$，因 $V_1=-22$，这两行的最高位置分别是
$t_{r-1},t_{r-2}$，确实独立。没有将它们扩大为所有
$[s^{r-1}]V^j\mathcal T$ 的零性。

## 2. 同一真正 Frobenius 下不能删去的周期权

用 R166 的 $\rho_p=D_p/H_p$、$\Phi_p=s\rho_p^4$，有
$$
 D_p\mathcal L(\Phi_p)=pH_p\mathcal L,
 \qquad
 \Phi_p'=p\rho_p^3
       \frac{\sqrt{1-\Phi_p}}{\sqrt{1-s}}.
 \tag{3}
$$
因此 $\mathcal J_p=\Phi_p'/p$ 整，若 $R=(p^2-1)/4$，
则 $\mathcal J_p\equiv-s^{3R}(1-s)^{2R}\pmod p$。

置 $\mathcal E=e^W/(\sqrt{1-s}\mathcal L^2)$，完整式为
$$
 \mathcal E(\Phi_p)\Phi_p'
       =\frac{D_p^5H_p^{63}}p e^{(p^2-1)W}\mathcal E.
 \tag{4}
$$
改用整行 $\mathcal J_p$ 时分母变成 $p^2$。
这些式子保留了正 theta 因子，没有在固定两维分子空间内
构造未经证明的闭合 Frobenius 矩阵。

完整证明、原点规范和有限系数校准见
[联合 amplitude 与周期 Frobenius](../notes/2026-11-12-joint-central-amplitudes-and-period-frobenius.md)。
该文与 R160、R162、R166 的原对象一致。下一步仍须对原全部
混合列及同一饱和前缀证明 R159 所要求的严格成本。
