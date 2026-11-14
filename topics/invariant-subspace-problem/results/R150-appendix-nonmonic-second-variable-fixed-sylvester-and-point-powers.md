# R150 附录：非首一第二变量、固定次数 Sylvester 与全部点态幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已核固定次数 Sylvester、补零因子、形式分簇及完整实际混合域。
状态：已证明，完整证明。新增 $s>0$ 的非首一范围；只在形式系数环中归一最高系数，不对实际 $a_m(X)$ 作除法。

## 1. 结论与范围

取任意复 $\ell^2$ first
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=c_*+\sum_j c_j\chi_j,
$$
两者非常数，且 $X_u$ 空谱。
记
$$
j_0=\min\{j:(a_j,c_j)\ne(0,0)\},\quad
h=2^{j_0},\quad \alpha=a_{j_0},\quad\gamma=c_{j_0}.
\tag{1.1}
$$

给定整数 $p,m\ge1$、$s\ge0$，
以及标量多项式
$$
F(x,y)=a_m(x)y^m+\cdots+a_0(x),
$$
其中
$$
\deg a_m=s,\qquad [x^s]a_m=1.
\tag{1.2}
$$
一般非零最高系数可先整体除去，不影响结论。

假设每个非零单项式 $x^iy^j$ 满足
$$
mi+pj\le W:=m(p+s).
\tag{1.3}
$$
记 $F_0$ 为权恰为 $W$ 的部分，并设
$$
H(Z)=F_0(1,Z)
$$
有 $m$ 个两两不同且非零的复根 $\Omega$。
由 (1.2)，$H$ 关于 $Z$ 首一、次数 $m$。

置 $\delta=\min(p,m)$，对 $\omega\in\Omega$ 定义
$$
d_\omega=
\begin{cases}
-2\alpha\,\partial_xF_0(1,\omega),&m<p,\\
-2\gamma\,\partial_yF_0(1,\omega),&p<m,\\
-2[\alpha\,\partial_xF_0(1,\omega)
+\gamma\,\partial_yF_0(1,\omega)],&p=m.
\end{cases}
\tag{1.4}
$$
要求
$$
\boxed{d_\omega\ne0\qquad(\omega\in\Omega).}
\tag{1.5}
$$

**定理 1。** 对任意 $\lambda\in\mathbb C$、
任意整数 $r\ge1$ 及任意复 $\ell^2$ 指数权 $w$，
$$
\boxed{[F(u,v)-\lambda]^r e^w
\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.6}
$$

$s=0$ 已属[非退化 Newton 上边附录](R150-appendix-nondegenerate-newton-edge-all-point-powers-and-one-empty-anchor.md)，不重复登记。
本稿新增 $s>0$：
关于第二变量的最高系数可为真正的正次数标量多项式，
例如 $xy-x^3-\lambda$。

### 1.1 首位条件的简化

加权 Euler 恒等式在根上给
$$
m\,\partial_xF_0(1,\omega)+p\omega H'(\omega)=0.
$$
故 $p>m$ 时只需 $\alpha\ne0$（$j_u\le j_v$），
$p<m$ 时只需 $\gamma\ne0$（$j_v\le j_u$）。

当 $p=m$ 时，条件是
$$
\gamma-\alpha\omega\ne0\quad(\omega\in\Omega).
\tag{1.7}
$$
等价于 $H$ 的次数 $m$ 齐次化在 $(\alpha,\gamma)$ 不为零。
$s>0$ 时不可把它误写成 $F_0(\alpha,\gamma)\ne0$：
$F_0$ 额外带有一个 $x^s$ 因子，
而 $\alpha=0,\gamma\ne0$ 本身可以满足 (1.7)。

## 2. 全部实际 Bell 多项式与有限除法

固定 $\lambda,r,w$，将 $\lambda$ 吸入 $F$ 常数。
令
$$
X=X_{u,b},\quad Y=X_{v,b},\quad \xi=e^w,\qquad L=X^{-1}.
$$
R176 §10、R186 给真实倾斜域、全部混合自然词和共同正则化。
$X$ 仍空谱，$L\in\mathfrak C=\{A\}'$ 有界且拟幂零。

采用联合规范 Bell 系数 $B_{ij}$。
它们是
$$
\prod_j e^{-(sa_j+tc_j)R_j(b)}
\bigl[\cosh(sa_j+tc_j)I+R_j(b)\sinh(sa_j+tc_j)\bigr]
$$
的 $(i,j)$ 导数，属于 $\mathcal A_h$，
$B_{00}=I$，正阶字符为零。
真正点态幂多项式为
$$
P_r(x,y)=
\sum_{i,j\ge0}\frac{B_{ij}}{i!j!}
\partial_x^i\partial_y^jF(x,y)^r.
\tag{2.1}
$$
它关于 $y$ 的次数为
$$
n=mr,
$$
其最高系数为
$$
A_r(x)=\sum_{i\ge0}\frac{B_{i0}}{i!}
\partial_x^i a_m(x)^r
=x^{sr}+\text{低次项}.
\tag{2.2}
$$
因此 $s>0$ 时 $P_r$ 确实不是关于 $y$ 首一。

R186 §§4–6、10 对任意有界交换系数多项式的规范最大实现（不要求最高系数为单位） $\mathsf P_r$ 为真实自然混合图闭包，
在原 $H$ 上完整 $C$ 自伴，且
$$
\mathsf P_r\xi=F(u,v)^r e^w
$$
有 $\xi$ 的真实循环图核心。

对 dyadic $\zeta$，实际同域差满足
$$
D_X,D_Y\in A^h\mathcal A_h.
$$
R124/R139 的真实 residue 除法（含 $h=1$）给
$$
P_{r,\zeta}=(\gamma_\zeta P_r)(x+D_X,y+D_Y),\qquad
P_{r,\zeta}-P_r=A^hQ_{r,\zeta},
\tag{2.3}
$$
其中 $Q_{r,\zeta}\in\mathcal A_h[x,y]$、$\deg_yQ\le n$。
此处不能继续声称 $\deg_yQ\le n-1$，
因为 (2.2) 的最高系数发生真实变化。

若
$$
\kappa_\zeta=
e^{-2b_{j_0}}(\zeta^h-1)/W_h,
$$
完整首位生成式仍给
$$
\boxed{
\chi(P_r)=F^r,\qquad
\chi(Q_{r,\zeta})
=\kappa_\zeta[
F(x-2\alpha,y-2\gamma)^r-F(x,y)^r].
}
\tag{2.4}
$$
这是联合生成式 $e^{-2(\alpha s+\gamma t)}-1$，
包含所有交叉 Bell 系数。
商先按 (2.3) 实际构造，随后才取字符。

## 3. 固定 $(n,n)$ 次数 Sylvester 行列式

对 $\deg_yP,\deg_yQ\le n$，
定义 $\operatorname{Syl}_{n,n}(P,Q)$ 为固定大小 $2n$ 的 Sylvester 行列式；
即有限线性映射
$$
(U,V)\longmapsto UP+VQ,\qquad
\deg_yU,\deg_yV<n,
$$
到次数小于 $2n$ 的系数向量的行列式，采用通常结果式符号。

即使 $Q$ 的真实次数低于 $n$，也保留这个固定大小。
若 $P$ 最高系数为 $a$，并且在某扩展环中 $a$ 可逆，则
$$
\boxed{
\operatorname{Syl}_{n,n}(P,Q)
=a^n\,\operatorname{Norm}_{\,\mathcal B[y]/(a^{-1}P)}(Q).
}
\tag{3.1}
$$
$Q$ 的次数降低时，这与不补零的通常结果式相差一个相应 $a$ 幂；
本稿不省略该因子。

取
$$
E_\zeta(x)=
\operatorname{Syl}_{n,n}(P_r,Q_{r,\zeta})
\in\mathcal A_h[x].
\tag{3.2}
$$
原 Sylvester 矩阵的伴随矩阵作用于常数坐标，
直接给有限多项式
$$
\boxed{
E_\zeta=A_\zeta P_r+B_\zeta Q_{r,\zeta}.
}
\tag{3.3}
$$
这是原交换系数环中的有限恒等式，
不逆 $A_r(x)$，也不逆实际 $a_m(X)$。

## 4. 实际次数界：形式最高系数只作形式单位

定义
$$
F_t(X_0,Z_0)=
t^W F(t^{-m}X_0,t^{-p}Z_0)
\in\mathbb C[t,X_0,Z_0],
$$
$$
\widetilde P(t,Z)=t^{rW}P_r(t^{-m},t^{-p}Z),\qquad
\widetilde Q(t,Z)=t^{rW}Q_{r,\zeta}(t^{-m},t^{-p}Z).
\tag{4.1}
$$
(1.3) 和全部有限导数的降权说明 $\widetilde P,\widetilde P_\zeta$
没有负 $t$ 次幂；
再从 (2.3) 逐个系数消去单射 $A^h$，得 $\widetilde Q$ 亦如此。

$\widetilde P$ 的 $Z^n$ 系数是
$$
a(t)=t^{msr}A_r(t^{-m})
=I+O(t^m)\in\mathcal A_h[t].
\tag{4.2}
$$
所以它在形式环 $\mathcal A_h[[t]]$ 中为单位。
这里只定义形式多项式
$$
\overline P=a(t)^{-1}\widetilde P
\in\mathcal A_h[[t]][Z],
\tag{4.3}
$$
它关于 $Z$ 首一、次数 $n$，并且
$$
\overline P(0,Z)=H(Z)^r.
$$
(4.3) 仅服务于有限行列式的次数证明，
不对应任何实际无界算子的倒数操作。

### 4.1 所有混合导数的分支内阶数

对每个简单根 $\omega$，
标量隐函数递归给
$$
z_\omega(t)\in\mathbb C[[t]],\qquad
z_\omega(0)=\omega,\qquad
F_t(1,z_\omega(t))=0.
$$
在 $Z=z_\omega(t)+t^\delta U$ 上，
$F_t$ 被 $t^\delta$ 整除。

对任意 $(i,j)$，
缩放后的 $\partial_x^i\partial_y^jF^r$
有前因子 $t^{mi+pj}$；
乘积求导至少保留 $\max(r-i-j,0)$ 个未求导的 $F_t$ 因子。
所以总阶数至少
$$
mi+pj+\delta\max(r-i-j,0)\ge\delta r.
\tag{4.4}
$$
此界覆盖每个交叉 $B_{ij}$。
对 $P_{r,\zeta}$ 也成立：取值点变为
$X_0=1+t^mD_X$、
$Z_0=z_\omega(t)+t^\delta U+t^pD_Y$，
$F_t$ 仍被 $t^\delta$ 整除。
由 (2.3) 的单射消因子和 (4.3) 的形式单位，
$$
\overline P(t,z_\omega(t)+t^\delta U),\
\widetilde Q(t,z_\omega(t)+t^\delta U)
\in t^{\delta r}\mathcal A_h[U][[t]].
\tag{4.5}
$$

### 4.2 分簇与固定次数行列式的缩放

因 $H$ 根简单，
逐阶标量 Hermite 余数分解将 $\overline P$
分成 $m$ 个首一的 $r$ 次形式因子，
常数项分别为 $(Z-\omega)^r$。
其他因子在本簇取值的常数是非零标量，
故 (4.5) 使该因子和 $\widetilde Q$ 在本簇归一后都可除 $t^{\delta r}$。

秩 $r$ 的自由模范数于是每簇贡献 $t^{\delta r^2}$。
用 (3.1)、(4.2)，形式单位 $a(t)^n$ 不改变阶数：
$$
\operatorname{Syl}_{n,n}(\widetilde P,\widetilde Q)
\in t^{\delta mr^2}\mathcal A_h[[t]].
\tag{4.6}
$$
整个过程只逆标量矩阵或常数项为 $I$ 的形式级数；
从未对实际 $a_m(X)$ 求逆。

固定次数 Sylvester 的两个参数各缩放 $t^{rW}$，
变量 $y=t^{-p}Z$ 又贡献 $t^{-pn^2}$，故
$$
\boxed{
\operatorname{Syl}_{n,n}(\widetilde P,\widetilde Q)
=t^{2rWn-pn^2}E_\zeta(t^{-m})
=t^{(p+2s)n^2}E_\zeta(t^{-m}).
}
\tag{4.7}
$$
结合 (4.6)，严格得到实际次数界
$$
\boxed{
\deg_xE_\zeta\le
D=r^2\bigl[m(p+2s)-\delta\bigr].
}
\tag{4.8}
$$
左侧是实际有限算子系数多项式；
高于 $D$ 的系数都等于零，不能仅用字符零替代。

## 5. 最高系数的实际可逆性

记 $F^{\rm sh}(x,y)=F(x-2\alpha,y-2\gamma)$。
固定次数 Sylvester 在第二参数减去第一参数时不变，
(2.4) 因而给
$$
\boxed{
\chi(E_\zeta)
=\kappa_\zeta^{mr}
\operatorname{Syl}_{m,m}(F,F^{\rm sh})^{r^2}.
}
\tag{5.1}
$$
这是固定次数行列式的乘法公式，
包括 $a_m(x)$ 所带的全部最高系数因子。

在每个标量根 $z_\omega(t)$ 上，
$$
F_t(1-2\alpha t^m,z_\omega(t)-2\gamma t^p)
=t^\delta d_\omega+\text{高次项}.
\tag{5.2}
$$
$F_t(1,Z)$ 的最高系数
$t^{ms}a_m(t^{-m})=1+O(t^m)$ 是标量形式单位。
所以 (3.1) 在 $r=1$ 的标量情形给
$$
\deg_x\operatorname{Syl}_{m,m}(F,F^{\rm sh})
=m(p+2s)-\delta,
$$
其最高系数恰为 $\prod_\omega d_\omega$。
由 (4.8)、(5.1)，若
$E_\zeta=e_Dx^D+\cdots+e_0$，则
$$
\boxed{
\chi(e_D)=
\kappa_\zeta^{mr}
\left(\prod_{\omega\in\Omega}d_\omega\right)^{r^2}
\ne0\qquad(\zeta^h\ne1).
}
\tag{5.3}
$$
故 $e_D\in\mathcal A_h^\times$ 为真实 Banach 代数单位。
这是最终排核使用的实际单位；(4.3) 的形式归一不被代入算子。

## 6. 真实混合深域与排核

令 $M=\ker\mathsf P_r$。
由 (3.3)、(2.3)，
$$
A^hE_\zeta=(A^hA_\zeta-B_\zeta)P_r+B_\zeta P_{r,\zeta}.
\tag{6.1}
$$
利用实际空谱逆 $L=X^{-1}$，定义
$$
\rho_\zeta=e_D+\sum_{j<D}e_jL^{D-j}
=e_D(I+LK_\zeta).
$$
$L$ 拟幂零并与 $K_\zeta\in\mathfrak C$ 交换，
所以由 (5.3)，
$$
\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C,\qquad
\rho_\zeta M=M.
\tag{6.2}
$$
最后一步使用 R88，不把全空间稠密像搬到未知限制。

取 R186 共同正则器 $R$，选有限阶覆盖 (6.1) 的全部次数、
每个中间自然词及 $X^D$。
在 $f\in R^{N_*}M$、$g\in U_\zeta R^{N_*}M$ 上，
$P_rf=0$、$P_{r,\zeta}g=0$，
全部实际混合域合法且被 $L^D$ 保持。
原 $H$ 的完整 $C$ 自伴给
$$
B(A^h\rho_\zeta f,g)
=B(P_{r,\zeta}L^DB_\zeta f,g)
=B(L^DB_\zeta f,P_{r,\zeta}g)=0.
$$
用测试空间稠密、(6.2) 及 $A^h$ 的普遍限制稠密像，
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
$$
有限 Fourier 支撑、严格正权下的总支撑全测和逐柱一维性
迫 $\dim M\le h$；
单射拟幂零 $A$ 排除非零有限维不变空间。
故 $M=0$。
完整 $C$ 自伴与真实循环图核心完成定理。

## 7. 普通非首一双慢例子

取
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
\quad \frac12<\sigma\le1.
$$
$u$ 为空谱锚，$v$ 为独立全平面 first，
首位同为0，$\alpha=1$。

取
$$
F(x,y)=xy-x^3,\qquad m=1,\ p=2,\ s=1.
$$
有 $W=3$、$H(Z)=Z-1$、$\delta=1$、$d_1=4$，
以及
$$
D=3r^2.
$$
所以
$$
\boxed{
[uv-u^3-\lambda]^r e^w
\text{ 对全部 }\lambda\in\mathbb C,\ r\ge1,\ w\text{ 循环}.}
\tag{7.1}
$$
这里 $y$ 最高系数是 $x$，不满足原首一 Newton 假设。

特别 $r=1,w=0$ 的实际乘子包含
$$
XY+B_{11}
-X^3-3B_{20}X-B_{30}-\lambda I.
$$
$B_{11}$、$B_{20}$、$B_{30}$ 是原慢 Bell 系数，
一般不属于 $\mathcal G$。
此前 $\mathcal G[X,Y]$ 的排核不能直接把它们删掉，
因此这不是把旧共振修正式重新命名为普通点态式。

保持 (1.3) 的任意低权单项式也可加入，
只要最高边的简单根与横截条件保持。

## 8. 边界

$s=0$ 是已发表子类；
重根、零根及首位切向上边仍须另作实际次数分析。
固定 $(n,n)$ Sylvester 的补零因子不能删掉；
形式最高系数单位不被当成实际 $a_m(X)$ 的有界逆。
完整域只由 R186 的真实混合正则化支付，
不存在未知限制上的免费密度推断。

完整 Hilbert 不变子空间问题仍未完成。
