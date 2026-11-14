# R273 四维首边的共同低阶矩规范与实际三次桥

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态。** 本文的规范变换和桥身份已证明；任意参数四维相邻序尚未证明。目的在于保留 [R273](R273-two-exceptional-weights-complete-schur-recovery.md) 的完整 MP、同一非正交源和硬约束，把相对出生 $t=2$ 的首边化到实际两组计数的 $j=0,1,2,3,4$ 阶矩。它没有以任意正标量族替代实际矩，也没有分别更换三个高度的源。

## 1. 实际计数矩与四维规范

保留 R273 的两个普通组 $(q,a)$、$(L,1)$ 和两个异常位 $(u,v)$，记
$$
z=a^2,\qquad w_1=u^2,\qquad w_2=v^2,\qquad
N=q+L,\quad h=N-2.
$$
固定相对出生 $t=2$，所以原缺失多项式次数 $d=q$。对 $0\le j\le N$ 定义真实有限权
$$
\nu_j(i)=\binom qi\binom L{j-i}z^i,
\qquad m_r(j)=\sum_i i^r\nu_j(i),\qquad e_j=m_0(j),
$$
$$
\Delta_2(j)=e_jm_2(j)-m_1(j)^2,\qquad
\Delta_3(j)=\det[m_{r+s}(j)]_{r,s=0}^2.
$$
当 $1\le j\le N-1$，置
$$
\mu_j=\frac{m_1(j)}{e_j},\qquad
\nu_j^{(2)}=\frac{m_2(j)}{e_j},\qquad
\chi_j=\frac{e_jm_3(j)-m_1(j)m_2(j)}{\Delta_2(j)}.
\tag{1.1}
$$
$\mu_j,\nu_j^{(2)}$ 也按同样式子定义于两端；$\chi_0,\chi_N$ 仅为不可用低阶通道的辅助值，取零即可，不声称存在相应首一问题。

去掉所有高度共同的正因子 $C_q=(q!)^2z^q$ 后，标量通道为
$$
\mathsf A_j=e_j^{-1},\qquad
\mathsf B_j=\frac{e_j}{\Delta_2(j)}\quad(1\le j\le N-1),
$$
$$
\eta_j=\frac{\Delta_3(j)}{\Delta_2(j)}\quad(1\le j\le N-1),\qquad
\eta_0=\eta_N=0.
\tag{1.2}
$$
其中 $\eta_j$ 是可用第三通道范数的**倒数**；$\eta_1=\eta_{N-1}=0$ 表示该残差通道不存在。$\mathsf B_0,\mathsf B_N$ 不定义，必须继续使用硬约束。

定义
$$
\mathsf D_n=\chi_n-2\chi_{n+1}+\chi_{n+2},\qquad
\mathsf E_n=\chi_{n+2}-\chi_{n+1},
$$
$$
\mathsf F_n=\Delta_n^2(\nu^{(2)}-\chi\mu),\qquad
\lambda_n=\frac{w_1w_2}
{w_1w_2\eta_n+(w_1+w_2)\eta_{n+1}+\eta_{n+2}},
$$
$$
\mathfrak a_n=\mathsf A_n+(w_1+w_2)\mathsf A_{n+1}
+w_1w_2\mathsf A_{n+2}.
\tag{1.3}
$$
则 R273 在**同一个**源合同 $J=\operatorname{diag}(1,-1,-1,1)$ 下准确等于
$$
\widetilde H_n=C_q^{-1}J^*H_nJ,
$$
并有
$$
\boxed{\begin{aligned}
\widetilde H_n[\alpha,\beta,\gamma,\delta]
=\min_x\bigg\{&\mathfrak a_n|\alpha|^2\\
&+\sum_{y,z_0:\,\mathsf B_{n+y+z_0}\text{ exists}}
w_1^yw_2^{z_0}\mathsf B_{n+y+z_0}
|x+y\beta+z_0\gamma-\mu_{n+y+z_0}\alpha|^2\\
&+\lambda_n|\delta-\mathsf D_nx-\mathsf E_n(\beta+\gamma)
-\mathsf F_n\alpha|^2\bigg\}.
\end{aligned}}
\tag{1.4}
$$
硬端准确为
$$
n=0:\ x=0,\qquad
n=h:\ x=q\alpha-\beta-\gamma.
\tag{1.5}
$$
内点才对 $x$ 自由最小化。

### 1.1 共同规范的推导

R273 的互补权满足
$$
\widehat\omega_j(R)=C_q^{-1}\nu_j(i),\qquad i=q-R.
$$
令 $e_1^{\rm grid}=q(q+1)/2$、$e_2^{\rm grid}=\sum_{0\le r<t\le q}rt$，并记
$a_*=q-e_1^{\rm grid}$、$c_*=2q-e_1^{\rm grid}$。R273 首一系数在可用通道中为
$$
p_j=a_*-\mu_j,\qquad
\tau_j=c_*-\chi_j,
$$
$$
s_j=\nu_j^{(2)}-c_*\mu_j+
q^2-e_1^{\rm grid}q+e_2^{\rm grid}.
$$
因此
$$
\Delta_n^2(s-\tau p)
=\mathsf F_n+a_*\mathsf D_n.
$$
将原源写成 $(\alpha,-\beta,-\gamma,\delta)$，并对唯一 nuisance 作所有高度共用的变换
$$
x_{\rm old}=a_*\alpha-x,
$$
每个二次通道剩余量恰变成 (1.4) 中剩余量的负数，混合残差恰变成 (1.4) 的最后一行，故费用不变。不存在 $Q_j$ 时，其辅助 $\tau_j$ 可以任意改变，因为实际硬约束迫相应 $u_i=0$；按上式选择辅助值并不创造不存在的通道。两硬端分别变成 (1.5)。

这个推导同时保留 $H_0$ 的非正交物理源度量。共同正因子和共同可逆合同保持全部相邻矩阵序。

## 2. 首边真正只依赖五个小阶实际矩

首边的目标为
$$
\boxed{\widetilde H_1\widetilde H_2^{-1}\widetilde H_1
\prec\widetilde H_0,}
\tag{2.1}
$$
等价于同源 $8\times8$ 块
$$
\begin{pmatrix}\widetilde H_0&\widetilde H_1\\
\widetilde H_1&\widetilde H_2\end{pmatrix}>0.
$$
(1.4) 只用 $j=0,\ldots,4$ 的矩。所有 $q$ 阶首一多项式系数和 $q!$ 公因子已经准确消去。

$q=2$ 或 $L=2$ 的整个模型属于已证“至多四异常位加一等权池”的情形；见 [R271 四异常位全出生结论](R271-appendix-four-exceptional-weights-full-birth-uniform-primitive-gram-bound.md)。该稿通常给统一常数 $16$，不能据此声称这些边界的严格常数 $1$ 已付。以下符号证书先处理真正的新内部范围 $q,L\ge3$；若要将 (2.1) 结论扩展到所有合法池长，还须另付 $q=2$ 或 $L=2$ 的常数 $1$ 边界（$q=L=2$ 的高度二情形由 [R239 高度二定理1](R239-appendix-four-exceptional-weights-full-height-two-primitive-gram-bound.md) 对四头 $(a,a,u,v)$、两单位池位再平均同权头对支付）。在 $q,L\ge3$ 时，$n=1,2$ 都是内点，$\Delta_2(j)>0$（$1\le j\le4$）、$\Delta_3(j)>0$（$2\le j\le4$），只有 $n=0$ 的 $x=0$ 硬约束仍须保留。

写 $q=3+Q,L=3+R$，则这里所需的全部 $\binom qk,\binom Lk$（$0\le k\le4$）在 $Q,R\ge0$ 中都有非负整数/有理系数。交换普通组并整体缩放还允许在证明时取 $z\ge1$。这些只是实际参数域的规范，尚不意味着 (2.1) 清分母后的矩阵或主子式系数全正。

## 3. 两个异常位的精确中间通道分拆

置
$$
T=w_1+w_2,\quad P=w_1w_2,\quad
\sigma=\beta+\gamma,\quad \varepsilon=\beta-\gamma,
\quad \varkappa=\frac{w_1-w_2}{T}.
$$
则中间两个通道准确合为
$$
\begin{aligned}
&w_1\mathsf B_{n+1}|x+\beta-\mu_{n+1}\alpha|^2
+w_2\mathsf B_{n+1}|x+\gamma-\mu_{n+1}\alpha|^2\\
&\quad=T\mathsf B_{n+1}
|x+\sigma/2+\varkappa\varepsilon/2-\mu_{n+1}\alpha|^2
+\frac PT\mathsf B_{n+1}|\varepsilon|^2.
\end{aligned}
\tag{3.1}
$$
全部其余项只依赖 $\alpha,\sigma,\delta,x$。因此 $w_1=w_2$ 时反对称方向确实同时约化，给一个标量块；$w_1\ne w_2$ 时，它通过同一个 nuisance 和显示的 $\varkappa$ 项耦合，不能删去。

## 4. 先加入一个异常位时的真实三次桥

为直接对接 R275，可先取两个普通组加第一异常位的旧系统，权平方为 $z,1,w$。在相对出生 $t$ 的共同源中，记 $d_0=q+1-t$，用
$$
f(R,y)=\alpha R^{\underline{d_0}}
+\beta yR^{\underline{d_0-1}}.
$$
源映射仍取该模型实际缺失多项式参数化。三个真实删除部分在源中分别作用为
$$
aE_{\rm group}:\ f\mapsto Rf(R-1,y),
$$
uE_{\rm exceptional}:\ f\mapsto yf(R,0),
$$
E_{\rm pool}:\ f\mapsto-(R+y-d_0)f(R,y).
$$
它们的和为零，正是 primitive 源身份。故三次下降
$\mathcal C=\sum b_i^3E_i$ 在出生 $t\to t-1$ 中为
$$
f\longmapsto(z-1)Rf(R-1,y)+(w-1)yf(R,0).
$$
使用 $R(R-1)^{\underline r}=R^{\underline{r+1}}$，得到在这两个真实、但非正交源基间的准确矩阵
$$
\boxed{K=\begin{pmatrix}z-1&0\\w-1&z-1\end{pmatrix}.}
\tag{4.1}
$$
它不依赖 $q,L,t$。对当前首边研究取 $t=2$，上下两个源块都是完整二维块。

若旧上、下出生的 Gram **形式矩阵**分别记为 $H_j,L_j$，则物理源度量为 $H_0,L_0$。因此 $K$ 的物理伴随在坐标中是
$$
H_0^{-1}K^*L_0,
$$
而不是普通转置 $K^*$。R275 的两条剪切在坐标中准确为
$$
Q=H_0^{-1}K^*L_2,\qquad
\Theta=H_1^{-1}K^*L_3,\qquad
\Delta=(\Theta-Q)/2.
\tag{4.2}
$$
例如旧上高度至少二时，R275 (S1) 在此基中等价于
$$
H_2^{-1}+\Delta L_3^{-1}\Delta^*
\preceq H_1^{-1}H_0H_1^{-1}.
\tag{4.3}
$$
另令
$$
\mathsf A=\tfrac12\bigl(H_1^{-1}K^*L_2
+H_0^{-1}K^*L_2L_3^{-1}L_2\bigr),
$$
则 R275 (S2) 等价于
$$
\mathsf A^*H_1\mathsf A+L_1L_2^{-1}L_1\preceq L_0.
\tag{4.4}
$$
旧下出生第二边已属于两普通组加一异常位的已证范围；(4.3)、(4.4) 在这个实际族上仍待证明。它们是可用于新第二异常位的充分条件，不应仅凭旧两维相邻序就宣称成立。

## 5. 首层再作一个共同三角规范，保留完整四维度量

令 (1.4) 的源由同一个可逆三角映射表示：
$$
\alpha=\alpha',\quad
\beta=\beta'+\mu_1\alpha',\quad
\gamma=\gamma'+\mu_1\alpha',
$$
$$
\delta=\delta'+\mathsf E_0(\beta'+\gamma')
+(\mathsf F_0+2\mu_1\mathsf E_0)\alpha'.
\tag{5.1}
$$
此映射行列式为一，且对 $n=0,1,2$ 完全相同。仅对每个可自由最小化的 nuisance，另外置
$x_{\rm old}=x+\mu_n\alpha'$；$n=0$ 时 $\mu_0=0$，仍准确保留 $x=0$。

定义
$$
r_n=\mu_{n+1}-\mu_n-\mu_1,\qquad
s_n=\mu_{n+2}-\mu_n-2\mu_1,
$$
$$
e_n=\mathsf E_n-\mathsf E_0,\qquad
f_n=\mathsf F_n-\mathsf F_0+\mathsf D_n\mu_n+2\mu_1e_n.
$$
则四个第二通道行依次为
$$
x,\quad x+\beta'-r_n\alpha',\quad
x+\gamma'-r_n\alpha',\quad x+\beta'+\gamma'-s_n\alpha',
$$
最后残差为
$$
\delta'-\mathsf D_nx-e_n(\beta'+\gamma')-f_n\alpha'.
\tag{5.2}
$$
这是每项直接代入后的等式，没有删除跨通道项。

因此首层的真实 $4\times4$ Gram 约化为一个 $3\times3$ 正对角矩阵加秩一，以及独立的最后一维：
$$
\boxed{
\overline H_0=
\begin{pmatrix}
\operatorname{diag}(\mathfrak a_0,w_1\mathsf B_1,w_2\mathsf B_1)
+w_1w_2\mathsf B_2\,vv^*&0\\
0&\lambda_0
\end{pmatrix},
\qquad v=(2\mu_1-\mu_2,1,1)^T.
}
\tag{5.3}
$$
故 $\overline H_0^{-1}$ 可由普通正对角逆及 Sherman–Morrison 公式准确给出；其额外分母为
$$
1+w_1w_2\mathsf B_2
v^*\operatorname{diag}(\mathfrak a_0,w_1\mathsf B_1,w_2\mathsf B_1)^{-1}v>0.
$$
后续待证矩阵准确为
$$
\overline H_2-\overline H_1\overline H_0^{-1}\overline H_1>0.
\tag{5.4}
$$
该规范只简化证书规模，不把 $\overline H_1,\overline H_2$ 宣称为同时对角。

## 6. 当前待证的准确事项

两条可继续的有限代数入口是：直接对 (1.4) 的 $\widetilde H_0,\widetilde H_1,\widetilde H_2$ 给完整同源正性证书；或利用 (4.1) 的固定三次桥证明旧真实二维族上的 (4.3)、(4.4)。目前两条均未闭。所有后续消元必须保留显示的物理源度量、$n=0$ 硬约束和实际二组矩关系。

[精确规范生成器](../notes/2026-11-14-two-exceptional-first-edge-moment-normal-form-789f-next.py)已用一组有理权在三个所需高度与完整物理层逆核对相同矩阵；这只核实现，没有测试或证明 (5.4)。[FLINT 多项式证书搜索器](../notes/2026-11-14-two-exceptional-first-edge-polynomial-certificate-789f-next.py)使用 (5.1)–(5.4)，将 $q=3+Q,L=3+R,z=1+Z,w_1=U+V,w_2=V$ 作为精确变量。只有完整四个前导主子式的分子全部获得非负系数且保留严格正项，才可能据此整理全参数证明；负系数不构成实际反例。
