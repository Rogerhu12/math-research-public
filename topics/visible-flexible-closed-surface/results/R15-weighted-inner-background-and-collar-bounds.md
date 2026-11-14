# R15：当前 weighted 内尾背景曲率与固定度量圆领代数界

2026-11-09，Astra-visible-flex-db6f0b0e / tail_theory。

状态：已证明（第1–3节条件命题），未参与推导者 independent_geometry 全文独审PASS；root核对证明后采用。审稿见 ../notes/2026-11-09-db6f-audit-tail-background-proof.md/.json；补后审稿SHA为73794d7ccd88206ae92e1c225e97a4c9ec08f5549a415cdefded042eaf4dc23e。没有证明某个已存有限Robin状态属于真正无限非线性图。

## 1. 适用的固定背景

使用 `scripts/closing_weighted_tail.mjs` 与 `closing_recalibrated_tail.mjs` 定义的同一个无限背景。本文不改任何物理控制参数。条件如下。

- `orientation=+1`，`curvatureBound=6`，`protectCell=160`，圆领半径 $a>7/50$。
- 原始深源 $d_0\in[1/200,1/160]$、$c_0\in[1/25,1/16]$、$w_{cut}=1/2$、$a_{exp}=11/4$、$R=64$、$\delta_n=d_0 2^{-n}$、$\eta_n=d_0c_0 2^{-3n/2}$。实际 binary 参数均在这些区间内。
- 除 cell 0 的 special caps 外，所有 finite cells 的 slope cap 是同一个正数 $c_{cap}\le1/49$，transition 大于零；实际 binary64 `0.02` 严格处于此区间。只修改 cell 0 的 positive warp weight；其余 weights 为 1。`flatOuterThroughCell` 未启用。
- 原始深校准根在 $[1/2,2]$，从 $n\ge80$ 成立；这一步沿用已审 R46 §2 的同一 uniform box 证明，实际 $d_0,c_0$ 满足它的全部宽度条件。
- 有限重分配采用一个固定正数 $\alpha>0$，由真实积分构造 radial coordinates。若以浮点 quadrature 实现，其偏差须在外部几何证书中另外控制；本文不把程序的 `alpha > 0` 判断提升为积分区间证明。

结论只用于 raw node $N\ge1$ 的内侧 $a\le r\le r_N$。前缀和 cell 0 不在本结论内。

## 2. 旋转背景的全内尾曲率界 $|\kappa_i|\le6$

设 $w>0$ 为 cap 后的 slope，$E=1+w^2$，$r_o(x)$ 为旧 profile 的原始径向参数。除唯一保护端之外，程序定义的正 radial speed 为

$$
v_r=\frac{|w_x|}{6E^{3/2}}+\alpha\,\frac{|(r_o)_x|}{E}.
\tag{2.1}
$$

故对于旋转图 $(r\cos\theta,r\sin\theta,h(r))$、$h'=w$，

$$
|\kappa_r|=\frac{|w_x|}{v_r E^{3/2}}\le6.
\tag{2.2}
$$

这个估计包含每个 profile 的所有内部点，包括 $w_x=0$ 的 cusp；后者的 $w_r$ 连续并为零。正的 free term 使 $v_r>0$，所以没有径向退化。

### 2.1 cap 的精确上界

源码的 smooth cap 在过渡区满足 $0\le d\log w_{new}/d\log w_{old}\le1$，且上端等于 $\log c_{cap}$；下区仍小于它，上区恒等于它。因此 finite raw cells $1\le n\le159$ 满足

$$0<w\le1/49,\qquad |\kappa_\theta|=w/(r\sqrt E)<50/343<1/6<6.$$

cell 0 的特殊 pulse/valley cap 和 cut-preserving 修补不在这条上界的使用域。

### 2.2 保护端和未经修改的无限深源

唯一混合区是 cell 159 的第一个 flat port。这里

$$
v_r=(1-\chi)|(r_o)_x|+\chi\frac{|w_x|}{6E^{3/2}}
+\chi\alpha\frac{|(r_o)_x|}{E},\qquad 0\le\chi\le1.
\tag{2.3}
$$

如果原 profile 的 $|\kappa_{r,o}|\le6$，则 $|(r_o)_x|\ge|w_x|/(6E^{3/2})$，故 (2.2) 仍成立。

下面给出覆盖实际 binary 参数的独立有理粗界，不使用 decimal 等于 binary 的假设。原始总 log 长度

$$
Y_0=6d_0+6d_0c_0/(1-2^{-3/2})<1/20,
$$

且 $\exp(7Y_0/\sqrt{12})<6/5$、$2^{11/4}>6$。原深源的最大 slope 因而满足

$$
W_n\le1280\,2^{-7n/4}.
\tag{2.4}
$$

在 $n=160$，$W_{160}\le1280\,2^{-280}$。在 cell 159 的 first flat port，$w_r=-7w/r$，故

$$|w_r|\le 7\cdot4W_{160}/(7/50)<2\cdot10^{-79}<6.$$

这里 $W_{159}<4W_{160}$，而 cap 因 slope 极小而完全未激活。因此 (2.3) 的条件已付。

对于所有原始 cells $n\ge160$，log jump 上界可取 $H_n=17+7n/5$，quintic log 插值有 $\|S'\|_\infty=15/8$。因此

$$
|w_r|\le B_n:=\frac{(7/2)(15/8)W_n H_n}{a\eta_n}+\frac{7W_n}{a}.
\tag{2.5}
$$

在 $n=160$ 使用 $a>7/50$、$\eta_{160}\ge2^{-240}/5000$，得到

$$B_{160}<0.066<1/10.$$

第一项从 $n$ 到 $n+1$ 的比至多 $(6/7)(H_n+7/5)/H_n<1$，因为 $2^{-1/4}<6/7$；第二项也严格下降。故对全部 $n\ge160$ 有 $|\kappa_r|\le|w_r|<1/10$、$|\kappa_\theta|\le W_n/a<1/10$。

综上，对本节规定的固定背景，所有 $a\le r\le r_N$、$N\ge1$ 的两个主曲率绝对值均不超过 6。$w,w_r\to0$，所以保持真实 C² 平圆领连接。有限 warp 只有有限个 pieces；$w_x$ 与 $v_r$ 连续、$v_r>0$，故每个 cusp 和有限 join 的 $h''=w_x/v_r$ 连续。没有要求辅助坐标 $r(x)$ 自己在所有 cusp 处 C²。

## 3. 圆领闭合的精确代数证书如何使用

邻题已审 R6 `smooth-unrippled-twist-flex/results/R6-fixed-metric-c2-collar-closure.md` 给出固定背景上的 Hermite 公式。对同一材料 $r,\theta$ 和同一 rigid gauge，记

$$A_{j,N}=\partial_r^j(F_N-F_{rot})(r_N,\theta),\quad L_N=r_N-a,$$

$$K_N=\|A_{0,N}\|_{2,\theta}/L_N^2+\|A_{1,N}\|_{2,\theta}/L_N+\|A_{2,N}\|_{2,\theta}.$$

本程序的 finite angular polynomials 明确定义了每个 $A_j$；其 cos/sin binary coefficients 作为精确有理数解释，使用

$$\|A\|_{2,\theta}\le\sum_{m\ge0}(1+m)^2\sum_{q=1}^3(|a_{mq}|+|b_{mq}|).$$

`db6f-tail-collar-exact-check.py` 用 Fraction 对这个上界逐项求和。对于 $L\le a$、$LB\le1$，以

$$\eta_1=(9/4)LK,\qquad\eta_2=15K$$

分别代替 R6 的一阶和二阶界。相对 metric、完整 XYZ Darboux tensor 和实际主曲率上界为

$$e_g\le2\eta_1+\eta_1^2,$$

$$e_D\le(3/2)B\eta_2+\eta_2^2/2+B^2(2\eta_1+\eta_1^2),$$

$$|\kappa_i|\le(B+\eta_2)/(1-\eta_1)^2.$$

全部比较是有理的。$B=6.001$ 是对第 2 节界的有余量输入；若实际冻结 geometry 不满足第 1 节，不能使用此绑定。

版本 v2 把 finite Fourier trace 精确投影到 C3 和 reflection symmetry：height 仅含 cos(3kθ)，planar complex component 仅含 frequency $1\bmod3$。记录 projection 的有限多项式范数差，并不是把投影误差丢掉。若 outer explicit XYZ map 未采用相同 projected shared jets，则还未完成拼接。

