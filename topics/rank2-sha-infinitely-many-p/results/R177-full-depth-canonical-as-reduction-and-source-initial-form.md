# R177. 全深度真实 AS 约化与同一源的初始关系

日期：2026-11-12。**已证明；严格全素数预算及主目标仍未完成。**

固定惰性 $p=4r-1\ge7$，$R=r(p-1)$，取 $\varpi^R=p$、$\lambda=\varpi^r$、$\mu=\varpi^p$。
原曲线 $a=f(b)$ 的完整整缩放满足
$$
x=(f(\mu y)-1)/\lambda\in\mathcal O_{\mathbb Q_p(\varpi)}[[y]],
\qquad \bar x+\bar x^p=\tau y^r,
\quad\tau=p[s^r]\log a\bmod p\ne0.
$$
此式来自全部对数系数及指数的全部 $p$ 次幂项，未只检查有限带。

对 R174 真稀疏图 $U=v^r g(v^R)$，准确有
$$
G(T)=p g(p^pT)\in\mathbb Z_p[[T]],\qquad
\bar G+T\bar G^p=\tau.
$$
所以 $\bar G=\tau\sum_{j\ge0}(-1)^jT^{(p^j-1)/(p-1)}$。
原图的无限系数也精确达到 R173 包络：
$$
p^{(p^{j+1}-1)/(p-1)}[b^{rp^j}]f
 \equiv\tau(-1)^j\pmod p.
$$
这些单坐标系数不被误称为饱和 jet 的下界。

完整反向关系为
$$
V^r=pU C(U^{p-1}/p),\qquad
C\in\mathbb Z_p[[S]],\quad\bar C=\tau^{-1}(1+S).
$$
故 $U^p$ 项真为单位，$V^r/p$ 的旧首带整余式不能直接用于全深度。

对原 $ab$ 源 $E_D=\mathbb Z_p[X,Y]_{\le D}$，定义
$\omega(P)=\min(Rv_pc_{ij}+ri+pj)$。
若实际前缀阶数 $k>\omega(P)$，其非零初始多项式必被
$x^p+x-\tau y^r$ 整除；无 $k<pr$ 限制。
可以在同一原源内明确构造 $Q\in E_{D-p}$，使
$$
\omega\bigl(P-(X^p+pX-\widetilde\tau Y^r)Q\bigr)>\omega(P).
$$
余项仍须与真实缺陷一起处理，未假设它单独保前缀。
特别 $D<p$ 时所有非零源的零阶至多 $pD$。
原 $A_2,B$ 的 degree $17$ 源区别保留。

[完整证明](../notes/2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)。
[独立实际逆级数校准](../scripts/check-canonical-as-reduction.py)。
