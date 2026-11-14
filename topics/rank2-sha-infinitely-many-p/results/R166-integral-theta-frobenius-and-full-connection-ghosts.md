# R166. 实际 theta 除法的整 Frobenius 提升与全精度连接展开

**状态：已证明；原有限次数混合源的统一范数改进仍未证明。**

在 R162 的 $E_0:y^2=x^3-x$、$s=x^{-2}$、
$\vartheta=\sigma x^{1/2}$ 规范下，对每个正奇数 $n$，
标准倍乘分子准确分解为

$$
\phi_n(x)=x h_n(x)^2,\qquad h_n\in\mathbb Z[x]\text{ 首一}.
$$

故有整多项式

$$
H_n(s)=x^{-(n^2-1)/2}h_n(x),\qquad
D_n(s)=x^{-(n^2-1)/2}\psi_n(x),
$$

$$
H_n(0)=1,\quad D_n(0)=n,\qquad
\vartheta(nz)=H_n(s)\vartheta(z)^{n^2},\quad
s(nz)=\Phi_n(s)=s(D_n/H_n)^4.
$$

平方来自 $[n]^{-1}(0,0)$ 的真实成对零点；
整性来自首一平方根和整闭性。对惰性 $p\ge7$，
$\psi_p(0)=-1$ 排除竖直零因子，再用
$[p]=-\operatorname{Fr}_p^2$ 及首项，准确得到

$$
H_p\equiv1,\qquad
D_p\equiv-s^{(p^2-1)/4},\qquad
\Phi_p\equiv s^{p^2}\pmod p,\qquad \Phi_p'(0)=p^4.
$$

保留原固定 $\mathcal A=A_2=sZ$、$Z=p_0e^W$，
得到全系数恒等式

$$
\frac{Z(\Phi_p(s))}{Z(s)^{p^2}}
=\frac{p_0(\Phi_p(s))H_p(s)^{68}}{p_0(s)^{p^2}}
=:\mathscr U_p(s)\in1+ps\mathbb Z_p[[s]].
$$

记 $G=\log Z$、$\mathscr L_p=-\log\mathscr U_p/p$。
则 $\mathscr L_p\in s\mathbb Z_p[[s]]$，且

$$
G(s)=\sum_{j=0}^{h-1}
   \frac{\mathscr L_p(\Phi_p^{\circ j}(s))}{p^{2j+1}}
   +\frac{G(\Phi_p^{\circ h}(s))}{p^{2h}}.
$$

余项逐系数趋于零：$\Phi_p^{\circ h}$ 对应真正的 $[p^h]$，
固定次数的系数赋值至少 $4h-C_m$，由原形式对数／指数的有限
截断直接证明。于是有保留原提升的全精度收敛展开。

第一层不能免费提升：若 $r=(p+1)/4$、
$C_p=p[s^{r-1}]W'\bmod p$，则

$$
\mathscr L_p(s)\equiv(C_p/r)s^r+O(s^{r+1})\pmod p,\qquad C_p\ne0.
$$

对原两行自身，显示商
$P(\Phi_p)H_p^{68}/P^{p^2}$ 和
$Q(\Phi_p)H_p^{68}/Q^{p^2}$ 含原点负阶因子，
不能称为 $\mathscr U_p$ 那种整单位。
实际拉回把正 theta 次数 $j$ 改成 $p^2j$，同时运输完整分子。
将这个新输入放回原 $0\le c\le j\le D$ 的共同饱和前缀，
仍须支付真实次数和分子格；本结果不将 Mellin 投影当作乘法。

见[完整证明及一手来源](../notes/2026-11-12-actual-theta-division-frobenius-and-full-ghosts.md)。
