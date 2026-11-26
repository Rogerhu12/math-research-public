# R271 附录：大辅助方差下真实最高核的完整 Galerkin 逼近

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：本稿的真实核包含、完整能量误差、原允许窗及同源修正均已证明。**
这里的方差是 $s\ge2^{24}/(m+2^m)$，不是物理方差 $S_x$。
结论直接作用于最高 carry 真核极限 $F_0$ 的原未加权 Galerkin 解；
没有把 $F_0$ 改成退化处较大的 $\ker C_0^r$。
本稿不给这个原解的指数孔权，也不将小残量当作完整物理 MP 返回费用。

依赖：

- [任意新增强位的完整最小源与绝对物理孔权](R271-appendix-all-strong-bit-extension-weighted-complete-source.md)，尤其 §§2–6；
- [最高 carry 的真实 Galerkin 极点](R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md)，§§1–2；
- [指数强前缀的实际方差完整源极限](R271-appendix-exponential-strong-prefix-actual-variance-source-limit.md)；
- [原放大方差的同源物理列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)，§4。

## 1. 全部最高参数共用的真实低新孔子空间

取原 N 或 Y 头的真实最高参数族 $A_m(t)$，保留全部旧 carry。
令
$$
d=2^m,\qquad y=m+d,\qquad h_y=2d,\qquad x\ge y,
$$
$$
C_{y,t}=A_m(t)+D_{[m,y)},\qquad
C_{x,t}=C_{y,t}+D_{[y,x)}.
\tag{1.1}
$$
原 $A_m(t)$ 在 $d$ 维物理基中严格三角，故对所有 $0\le t\le1$ 都有
$A_m(t)^d=0$。两因子交换，因此
$$
C_{y,t}^{h_y}=0 .
\tag{1.2}
$$
这只是原有限头的幂零性，不使用 Jordan 相似或替代内积。

令 $N_{\rm new}=N_{[y,x)}$，$P_{\le L}=\mathbf1_{\{N_{\rm new}\le L\}}$。
对任意整数 $L\ge0$，$D_{[y,x)}^{L+1}P_{\le L}=0$。
二项式中阶数至少为 $h_y+L$ 的每项，或者含至少 $h_y$ 次旧头，
或者含至少 $L+1$ 次新位删除。所以
$$
\boxed{C_{x,t}^{r}P_{\le L}=0
\quad\text{只要 }r\ge h_y+L,\quad0\le t\le1.}
\tag{1.3}
$$
特别，对 $t>0$ 的真实核 $F_t=\ker C_{x,t}^r$，
$$
\operatorname{Ran}P_{\le L}\subseteq F_t .
\tag{1.4}
$$
在原偶 $R=x-m$、奇 $r$ 的最高 carry 族，令
$$
F_0=\lim_{t\downarrow0}F_t
$$
为原满列秩解析框架给出的真实核极限。有限维正交投影收敛，
而 (1.4) 中每个向量在全部 $F_t$ 内，故
$$
\boxed{\operatorname{Ran}P_{\le L}\subseteq F_0 .}
\tag{1.5}
$$
没有将 $F_0$ 与 $\ker C_{x,0}^r$ 等同。

## 2. 原完整源在旧列空间中的准确反像

先固定 $t$，略去下标 $t$。令 $J=r-1$、$s>0$，并用全部高度的原列
$$
\mathcal R_Xv=\sum_{j=0}^J
\frac{(-X)^jv}{\sqrt{j!s^j}}\otimes e_j,
\qquad H_X=\mathcal R_X^*\mathcal R_X .
\tag{2.1}
$$
固定同一个旧头 forcing $g\in\mathcal H_{<y}$，在新增位补真空，记为 $f$。
完整空间的原最小者为
$$
a=H_{C_x}^{-1}f,\qquad k=\mathcal R_{C_x}a.
\tag{2.2}
$$
旧列空间 $\mathscr E_0=\operatorname{Ran}\mathcal R_{C_y}$ 在新增位上是恒等张量；
它的辅助次数至多 $\min(J,h_y-1)$。设
$$
D=D_{[y,x)},\quad
M=\exp(-Da^*/\sqrt s),\quad B=P_{\{N_a\le J\}}M|_{\mathscr E_0},
\quad K=B^*B.
$$
这里 $a^*$ 是辅助创建，与头最小者 $a$ 的字体含义不同。
依赖稿给准确卷积 $B\mathcal R_{C_y}=\mathcal R_{C_x}$，包括截断 $J<h_y$。
若 $k_0=P_{\mathscr E_0}(f\otimes e_0)$，则
$$
k=BK^{-1}k_0,
\qquad v:=K^{-1}k_0=\mathcal R_{C_y}a .
\tag{2.3}
$$
最后一式也可直接由 $B$ 保第零系数及其单射性核对。

对 $0<\gamma\le1$ 记
$$
\alpha=\|D\|/\sqrt s,\qquad
\theta_h(u)=u\sqrt h+u^2/2,
$$
$$
\Theta=\theta_{h_y}(\gamma\alpha)
       +\theta_{h_y}(\gamma^{-1}\alpha),\qquad
\Gamma=\gamma^{-N_{\rm new}}.
$$
若 $\Theta<\log2$，依赖稿的双向共轭是在原 $K^{-1}$ 上证明的，因而
$$
\|\Gamma v\|\le\frac{\|g\|}{2-e^\Theta}.
\tag{2.4}
$$
原 $P_{\mathscr E_0}$ 与 $\Gamma$ 交换是这里的合法依据。
后面没有要求 $P_{F_t}$ 或 $P_{F_0}$ 与它交换。

## 3. 到真正 Galerkin 解的能量误差

以 $F$ 表示 $F_t$（$t>0$）或 $F_0$（此时用 $C_{x,0}$）。令
$$
a_F=(P_FH_{C_x}|_F)^{-1}P_Ff,\qquad
\xi_F=f-H_{C_x}a_F.
\tag{3.1}
$$
它仍是原完整环境 Gram 在真正 $F$ 上的压缩，$H_{C_x}\succeq I$。
取可行列
$$
a_{\rm low}=P_{\le L}a\in F.
$$
由于 $P_{\le L}$ 与旧列 $\mathcal R_{C_y}$ 交换，
$$
\mathcal R_{C_x}(a-a_{\rm low})
=P_{\{N_a\le J\}}M P_{\{N_{\rm new}>L\}}v.
$$
右端的乘子输入仍支撑辅助次数小于 $h_y$。依赖稿的全低辅助空间估计给
$$
\|\mathcal R_{C_x}(a-a_{\rm low})\|
\le e^{\theta_{h_y}(\alpha)}\gamma^{L+1}\|\Gamma v\|.
\tag{3.2}
$$
两条 Galerkin 方程表明 $a_F$ 是 $a$ 在原 $H_{C_x}$ 内积下到 $F$ 的正交投影。
因此其误差不超过 (3.2) 的真实可行列误差。得到
$$
\boxed{
\|\mathcal R_{C_x}(a-a_F)\|
=\|H_{C_x}^{-1/2}\xi_F\|
\le
\frac{e^{\theta_{h_y}(\alpha)}}{2-e^\Theta}
\gamma^{L+1}\|g\| .}
\tag{3.3}
$$
尤其同一右端也控制 $\|a-a_F\|$。
源能量的损失还有准确平方身份
$$
\langle f,a\rangle-\langle f,a_F\rangle
=\|\mathcal R_{C_x}(a-a_F)\|^2.
\tag{3.4}
$$

取 $m\ge10$、$s\ge2^{24}/y$、$\gamma=1/32$。
因为 $\|D\|\le1/y$、$h_y\le2y$，依赖稿证明 $\Theta<1/32$，并给
$$
\boxed{
\|\mathcal R_{C_x}(a-a_F)\|,\quad
\|H_{C_x}^{-1/2}\xi_F\|,\quad
\|a-a_F\|
\le\frac{16}{15}\,32^{-L-1}\|g\| .}
\tag{3.5}
$$
此常数与 $x-y$、$r$ 及最高参数 $t$ 无关；$r$ 只须满足 (1.3)。
原物理空间中若 $\|C_x\|\le M_*$，则完整有限和满足
$H_{C_x}\preceq e^{M_*^2/s}I$，故
$$
\boxed{
\|\xi_F\|\le\frac{16}{15}
\exp\!\left(\frac{M_*^2}{2s}\right)32^{-L-1}\|g\| .}
\tag{3.6}
$$
在原实际 N/Y 头及最高参数零头，可取既有粗界 $M_*=7$。
需要别的参数族时，(3.6) 保留其真实 $M_*$，不无条件套用 $7$。

## 4. 奇数高度、偶强段和母空间的同时可行选择

给一组全部显式的原合法参数：
$$
m\in4\mathbb N,\quad m\ge20,\quad d=2^m,\quad y=m+d,
$$
$$
L=d,\qquad r=3d+1,\qquad J=3d,
$$
$$
R=576(m+1)^2d^2,\qquad x=m+R,\qquad Q=R+3d+1.
\tag{4.1}
$$
$R$ 是偶数，$r$ 是奇数，$r\ge h_y+L$，且 $r<d+R$。
原高度窗准确满足
$$
\frac{\sqrt{x+1}}{8(m+1)}
\ge \frac{\sqrt R}{8(m+1)}=3d=r-1,
$$
所以
$$
r\le1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor.
\tag{4.2}
$$
原基头 $m$ 的支持条件 $Q\ge R+J$ 成立；最高参数零头改用基头 $m-1$ 时，
强段长为 $R'=R+1$，此时仍准确有 $Q=R'+J=R+r$。
没有漏掉改基头后增加的一位。
因 $m+1\le d$、$d\ge2^{20}$，
$$
Q\le577d^4<2^{10}d^4<e^{26d^3}.
\tag{4.3}
$$
因此同一整数 $Q$ 也在原 c26 母支持上限内。
此处只核对实际使用的支持条件；若另调用要求 $Q\ge R+h+1$ 的全反馈定理，
仍须把 $Q$ 相应增大并重新保留该定理条件，不能把 (4.3) 当作已经调用它。

固定 $K\ge2^{24}$，取 $s=K/y$。对实际最高参数或零头，(3.6) 给
$$
\|\xi_F\|
\le\frac{16}{15}\exp\!\left(\frac{49y}{2K}\right)32^{-d-1}\|g\|.
\tag{4.4}
$$
由于 $y\le2d$ 且 $49/K<1$，有一个便于阅读的统一弱化
$$
\boxed{\|\xi_F\|\le e^{-2d}\|g\|.}
\tag{4.5}
$$
更高精度可直接增加 $L$，并选奇 $r\ge2d+L$、偶
$R\ge64(m+1)^2(r-1)^2$；母上限仍须单独检查。
(4.1) 已足够同时实现原窗口、能量误差趋零及无权残余趋零。

## 5. 真 $F_0$ 与实际真核的完整来源强极限

沿 (4.1)，令 $m\to\infty$，$K\ge2^{24}$ 固定，并取同一个固定有限物理 forcing $f$。
有 $s=K/y\to0$、$s\ge S_x$。
在实际最高参数处，完整强头源定理给
$$
a\to P_Mf,\qquad \mathcal R_{C_x}a\to P_Mf\otimes e_0.
\tag{5.1}
$$
在最高参数零点，准确有
$$
C_{x,0}=A_{m-1}+D_{[m-1,x)}.
$$
使用同一定理的基头 $m-1$ 即可。
设 $n=2^{m-1}$；(4.1) 的多项式 $x$ 满足
$x+1\le e^{26n^3}/4$，且 $1\le J=3d\le n+x-(m-1)-1$。
因此零头的完整源也满足 (5.1)，没有换用小于物理 $S_x$ 的方差。

现在 (3.5) 以真实 $F_t$ 或真实极限 $F_0$ 为投影空间，直接给
$$
\boxed{
a_F\to P_Mf,\qquad
\mathcal R_{C_x}a_F\to P_Mf\otimes e_0 .}
\tag{5.2}
$$
这是上述大辅助方差和具体增长窗下真实压缩源的强极限。
它没有给 $P_Mf$ 本身的非零性或普通不变子空间结论。

## 6. 实际最高参数处的原同 $u$ 修正

本节只在原实际最高参数使用 $C_x$ 和 $F=\ker C_x^r$。
置 $\omega_j=(D_x^*)^j\Omega$、$S_x=\sum_{i\ge x}(i+1)^{-4}$。
定义由真正 Galerkin 列产生的物理列及其第零层修正
$$
f_F^{\rm phys}
=\sum_{j=0}^{J}\frac{(-C_x)^ja_F\otimes\omega_j}{s^j j!},
\qquad
\widehat f_F=f_F^{\rm phys}+i_0\xi_F .
\tag{6.1}
$$
所有项都是有限头、有限远孔层的真正 Hilbert 向量。
对原 $P=P_{V_Q}$ 或 $P_{K_Q}$，在 $Q\ge R+J$ 下逐列恒等式准确给
$$
P f_F^{\rm phys}=(Pi_0)H_{C_x}a_F.
$$
加上原残余后，得到
$$
\boxed{P\widehat f_F=Pi_0f,
\qquad
(P_{V_Q}-P_{K_Q})\widehat f_F
=(P_{V_Q}-P_{K_Q})i_0f.}
\tag{6.2}
$$
因此同一原 $u$ 及其全部内部顶部和两端 partial 保持。
其他 joined/full 投影仍按各自原 cut 条件使用，不从这里自动推出。

映射 $e_j\mapsto\omega_j/\sqrt{j!s^j}$ 是逐层收缩，因为 $s\ge S_x$。
若 $f^{\rm phys}$ 是完整源 $a$ 的原同源阻尼列，则
$$
\|f_F^{\rm phys}-f^{\rm phys}\|
\le\|\mathcal R_{C_x}(a_F-a)\|,
$$
$$
\boxed{
\|\widehat f_F-f^{\rm phys}\|
\le\frac{16}{15}\bigl(1+e^{49/(2s)}\bigr)
32^{-L-1}\|g\|.}
\tag{6.3}
$$
沿 (4.1)，右端趋零；故 $\widehat f_F\to P_Mf$，并同时保持 (6.2) 的原来源。

这一步的准确代价是新增的 $i_0\xi_F$，没有删掉它。
$f_F^{\rm phys}$ 通常仍不是真正 $C_x+D_x$ 的核列；
$\widehat f_F$ 也没有因此变成真核。
在 $t>0$ 处虽有 $\xi_F\in\operatorname{Ran}(C_x^*)^r$，
把它交给完整 $((C_x^*)^r)^\dagger$ 或完整物理返回仍须支付实际费用。
在 $t=0$ 的 $F_0$ 情形，更不能把 $F_0^\perp$ 当成
$\operatorname{Ran}(C_{x,0}^*)^r$，因为二者一般不同。

## 7. 尚未跨过的准确接口

本稿已把大辅助方差完整源的新增孔衰减用于真正 $F_0$ 的原能量投影，
并在原奇高度、偶强段和母支持范围中给出无权残余趋零及同源修正。
没有使用 $P_{F_0}\Gamma=\Gamma P_{F_0}$。

待付的是原物理方差 $S_x$ 下的绝对高孔残余，或者把这里的实际同源大方差列
送回原完整物理核/纯高度代表的全部 MP、双塔、真帽及外投影费用。
辅助方差到物理方差的逐层逆收缩会含 $(s/S_x)^{j/2}$，
本稿的无权能量误差不自动支付它。
因此 (4.5) 不能单独替代原同 $w$ 倒数预算，也不关闭普通 Hilbert ISP。
