# R150 补充：排序计数与归一化柱预算的二分，全部正主行及实受控辅助

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / normal_resume_1cf / Astra-ISP-1cf8c51d；根与 normal 已分别完整复核有限计数到对数增长、未来最大点、Abel 平方和及两个实际域分支。
本补充依赖[归一化全柱根界与复受控辅助行](R150-appendix-normalized-column-root-bounds-complex-controlled-auxiliaries-and-shear-powers.md)的已付域判据，以及[谐和/好时间条带附录](R150-appendix-harmonic-positive-anchor-sharp-strip-budget-and-all-shear-powers.md)。
以下只证明新增的数列二分及其精确应用；不重新计已有两条算子预算。

## 1. 排序二分

令 $r_1\ge r_2\ge\cdots>0$，$r\in\ell^2\setminus\ell^1$，置
$$
S_n=\sum_{k\le n}r_k,\qquad
G_n^2=\sum_{k>n}r_k^2,\qquad
\Theta(t)=\sum_k\lfloor tr_k\rfloor.
$$
则至少下列一项成立：
$$
\boxed{\liminf_{n\to\infty}\frac{nG_n^2}{S_n^2}=0,}
\tag{1.1}
$$
或
$$
\boxed{\limsup_{t\to\infty}\frac{\Theta(t)}{t\log t}=+\infty.}
\tag{1.2}
$$
更准确地，若 (1.2) 的上极限有限，则 (1.1) 成立。
允许两项同时成立。

### 1.1 有限计数比迫排序部分和至多对数增长

设
$$
\Lambda=\limsup_{t\to\infty}\frac{\Theta(t)}{t\log t}<\infty.
$$
选固定 $K>\max(\Lambda,0)$。
充分大时 $\Theta(t)\le Kt\log t$。
在 $t_n=2/r_n$ 上，因为 $S_n\ge nr_n$，
$$
\frac{\Theta(t_n)}{t_n}
\ge\sum_{k\le n}\left(r_k-\frac1{t_n}\right)
=S_n-\frac{nr_n}{2}\ge\frac{S_n}{2}.
$$
所以
$$
S_n\le2K\log(2/r_n).
\tag{1.3}
$$
记 $C=2K>0$，则 $r_ne^{S_n/C}\le2$。
由 $S_n-S_{n-1}=r_n$，
$$
e^{S_n/C}-e^{S_{n-1}/C}
=e^{S_n/C}(1-e^{-r_n/C})
\le C^{-1}r_ne^{S_n/C}\le2/C.
$$
逐项求和，得到
$$
\boxed{S_n\le C\log(n+O(1))+O(1)=O(\log n).}
\tag{1.4}
$$
这里没有假设规则变差、幂尾下界或 $nr_n$ 有界。

### 1.2 任意次幂上界的未来最大点给小尾平方比

事实上只要 $S_n=o(n^\alpha)$ 对每个 $\alpha>0$ 成立，
便足以推出 (1.1)。

固定 $0<\alpha<1/2$ 和整数 $N$。
因 $S_n/n^\alpha\to0$，在 $n\ge N$ 上的正的最大值由某个有限 $m\ge N$ 取到。
因此对每个整数 $\ell\ge1$，
$$
\sum_{j=1}^{\ell}r_{m+j}
=S_{m+\ell}-S_m
\le S_m\left[\left(\frac{m+\ell}{m}\right)^\alpha-1\right].
\tag{1.5}
$$
定义两个非负递减列
$$
x_j=r_{m+j},\qquad
y_j=\frac{S_m}{m^\alpha}
\big[(m+j)^\alpha-(m+j-1)^\alpha\big].
$$
(1.5) 正是每个有限前缀上 $\sum x_j\le\sum y_j$。

为完整付平方和比较，固定 $L$，置
$A_\ell=\sum_{j\le\ell}(x_j-y_j)\le0$。
离散分部求和给
$$
\sum_{j=1}^Lx_j(x_j-y_j)
=x_LA_L+\sum_{j=1}^{L-1}(x_j-x_{j+1})A_j\le0.
$$
故 $\sum_{j\le L}x_j^2\le\sum_{j\le L}x_jy_j$。
Cauchy–Schwarz 随即给
$$
\sum_{j\le L}x_j^2\le\sum_{j\le L}y_j^2.
\tag{1.6}
$$
令 $L\to\infty$。

每个单位区间上 Cauchy–Schwarz 又给
$$
\begin{aligned}
\sum_{j\ge1}y_j^2
&=\frac{\alpha^2S_m^2}{m^{2\alpha}}
\sum_{j\ge1}
\left(\int_{m+j-1}^{m+j}t^{\alpha-1}\,dt\right)^2\\
&\le\frac{\alpha^2S_m^2}{m^{2\alpha}}
\int_m^\infty t^{2\alpha-2}\,dt\\
&=\frac{\alpha^2}{1-2\alpha}\frac{S_m^2}{m}.
\end{aligned}
\tag{1.7}
$$
所以
$$
\frac{mG_m^2}{S_m^2}\le\frac{\alpha^2}{1-2\alpha}.
\tag{1.8}
$$
$N$ 任意，故这控制原比值的下极限。
再令 $\alpha\downarrow0$，得到 (1.1)。
结合 (1.4)，排序二分证明完毕。

## 2. 任意正 non-l1 主行的完整实受控剪切结论

设
$$
u=u_*+\sum_j a_j\chi_j,\qquad
v=v_*+\sum_j c_j\chi_j,
$$
其中 $a_j\ge0$、$a\in\ell^2\setminus\ell^1$，
$c_j\in\mathbb R$ 且 $|c_j|\le C_0a_j$，$C_0<\infty$。
常数可以先取实数；任意复常数在原完整 Bell 变换后作为有界仿射项吸收，证明相同。

令 $G(x,z)$ 对 $z$ 首一 $m$ 次，且 $(x,z)$ 总次数不超过 $m$。
则对全部 $\lambda\in\mathbb C$、整数 $r\ge1$、
任意复 $\ell^2$ first 指数权 $w$，
$$
\boxed{[G(u,v-u^2)-\lambda]^re^w
\text{ 是实际 }A\text{ 的循环向量}.}
\tag{2.1}
$$
不再有主行的增长、排序下界、计数比、幂率或尾小量条件。

证明按同一实际行的递减重排应用 §1：

- 若 $\Lambda_a=\infty$，已推谐和/好时间条带附录的原生条件
  $\Lambda_a>C_0/(2\pi)$ 自动成立。
  其完整混合 Bell、相伴图和正 first 域证明给 (2.1)。
- 若 $\Lambda_a<\infty$，§1 给 (1.1)。
  归一化全柱根界稿的重排判据遂适用，给 (2.1)。
  该分支甚至允许 $c$ 任意复，只需原有系数支配。

两个分支分别使用已经付清的实际域机制，
没有把其中一条的假设从另一条中免费删除，
也没有对未知闭图转移通常伴随或空谱增长性质。

特别，任意正不可和 $\ell^2$ 主行、任意实受控辅助行，
现在都满足
$$
\boxed{[(v-u^2)^2-\beta u^2-\lambda]^re^w
\text{ 对所有 }\beta,\lambda\in\mathbb C,\ r\ge1\text{ 循环}.}
\tag{2.2}
$$
这包括实 $\beta=4a_0^2$ 的全部真正剪切碰撞。

### 2.1 两行均允许任意复可和余项

上述结论还适用于
$$
u=u_*+\sum_j(a_j+d_j)\chi_j,\qquad
v=v_*+\sum_j(c_j+e_j)\chi_j,
\tag{2.3}
$$
其中 $a$ 是上述任意正不可和主行，$c$ 是实受控辅助骨架，$d,e\in\ell^1(\mathbb C)$ 任意，$u_*,v_*\in\mathbb C$ 任意。若骨架满足归一全柱判据，$c$ 本身也可以是任意复受控行。预算只施加于骨架 $a,c$，不要求余项满足其逐项支配或尾比。

证明先用原行 $a+d,c+e$ 和原指数权 $w$ 构造完整普通 Bell 最大实现；所有联合 cumulant 都保留原值，不改成未扰动行的值。令
$$
D=u_*I+X_d,\qquad E=v_*I+X_e.
$$
由于 $d,e\in\ell^1$ 且 $\sup_j\|V_j\|<\infty$，两个有限截断按算子范数收敛，故 $D,E\in\mathcal A$。原倾斜 first 可写为
$$
X+D+H_w,\qquad Y+E+K_w,
$$
其中 $H_w,K_w\in\mathcal A$ 是针对原两行与原 $w$ 的实际有界倾斜。

在完整 Bell 式中才作代换
$$
x\longmapsto x+D+H_w,\qquad
z\longmapsto z-2(D+H_w)x+E+K_w-(D+H_w)^2.
\tag{2.4}
$$
它不增加 $(x,z)$ 总次数，且唯一最高 $z^{mr}$ 的系数仍为实际单位 $I$。所有新有界系数仍在 $\mathcal A$，所以相伴图、有限谱分支及全柱测试的相应证明均保持。

定义域用 R186 的同一个有限共同正则器支付：把原两行、骨架两行和所需有界项同时纳入，取足够深的固定正则幂，先在共同自然词域验证 (2.4)，再由两边规范最大实现的共同图核心识别完整闭图。这里没有假定原自然和已经闭，也没有把 $D,E$ 当作点态乘法。最终排除的是原完整 Bell 实现的核，结论仍是原 (2.3) 的指定点态向量。

## 3. 复辅助和其余边界

当 $\Lambda_a<\infty$ 时，(2.1) 允许任意复受控辅助。
当 $\Lambda_a=\infty$ 且新全柱尾比不趋小，
本补充仍只得到实受控骨架与 §2.1 的复可和余项；不能把实正 first 的条带证明用于一般复行。

本稿没有覆盖不受控的独立辅助行、全部多模式核或普通 ISP。
新增的是：两个已核实际预算通过一个完全证明的数列二分，
共同覆盖所有正不可和主行的实受控剪切类。
