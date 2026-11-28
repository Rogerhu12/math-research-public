# R1193：原最高 primitive 整 packet 与 CM 首 normal 层的 simple-Cauchy 泛函

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明，原 $p\equiv11\pmod{12}$ 行。** 取最高 primitive 指标 $r=m=(p-1)/2$。在原有限角代数中，尖点型 $\tau_m$ 与主系列 $\mathrm{PS}_{m-1}$ 的和有实际整幂等元。其负 deck、最高 generic-tail Hodge 向量的首中心层是原 Igusa 曲线上唯一的 simple-Cauchy 微分。它在原 $c_1$ 尾的完整首 normal 阶为 $2m$，精确投影为 $d(x^{g-1}y)$ 的原单位倍；前因子是指定原底向量的明确线性泛函。原有理盘 $w=(a-1)/p^3$ 上，除 $\varepsilon^m$ 后的真正 Abel primitive 为整 Tate 级数，约化次数至多 $2g-1$，整个所述 packet 的该最高系数确实非零。

这里的目标是 $\tau_m+\mathrm{PS}_{m-1}$ 的整 packet，**不是**把单独 $\tau_m$ 在整个原 Jacobian 上宣称整分裂。更没有把 packet 中一个单位自动传给 R1191 的指定非 CM 半秩因子，或给同一 $\beta$ 的 MW 横截值赋值为零。后者仍须实际比较原 log 列与本篇 simple-Cauchy 列。

## 1. 原模型、原点与指标

全部沿用 R1018、R1021、R1023、R1028、R1032 的原曲线 $X_1$、原六标记 $H_6$、原 $\kappa_4$ 下降、原 $c_1$ 及同一个 ordinary trace-zero quotient。设
$$
p=12g-1>37,\qquad m=6g-1=(p-1)/2,\qquad
e_0=m(p+1),\qquad \pi_0^{e_0}=p,\qquad
\varepsilon=\pi_0^m.
\tag{1193.1}
$$
在足够的未分歧底上工作，记剩余域为 $k$。原惯性及 deck 约定为
$$
\sigma(\pi_0)=\xi\pi_0,\qquad \xi^{e_0}=1,
\qquad \delta^*b=\zeta^2b,\qquad \delta^*u=\zeta u.
$$
中心的准确模型是
$$
I:\quad u^m=(1-b^3)^{2g}A_p(b),\qquad
A_p(b)=bQ_p(b^3),\qquad \deg A_p=m-1.
\tag{1193.2}
$$
$A_p$ 单首、根简单、与 $1-b^3$ 互素。记原 generic supersingular 尾集合为 $S=\{A_p(s)=0\}$。

因为 $m$ 是奇数且
$$
\gcd(m,p+1)=\gcd(m,2m+2)=1,
$$
指标 $r=m$ 确属于 R1191 的同一个 primitive 轨道。其与最低型存在局部二次 twist 关系，但本文不据此识别任何全局 newform 为另一个 newform 的 twist；本篇全部计算直接在这个原 finite-type packet 上进行。

在每个原 generic 尾写
$$
D_s:\quad Y_s^2=X_s(X_s^{(p+1)/2}+A_s),\qquad
\omega_s^{\rm hi}=X_s^{(m-1)/2}\frac{dX_s}{Y_s}.
\tag{1193.3}
$$
其完整 Hodge 权为 $m^2$。在原无穷节点参数 $z_s$ 中，
$$
\omega_s^{\rm hi}
=-2\bigl(1+O(z_s^{p+1})\bigr)\,dz_s.
\tag{1193.4}
$$
底向量记为 $L=\sum_s L_s\omega_s^{\rm hi}$，并要求其真实 deck 角色为 $\delta^*L=\zeta^2L$。这里对全部被 $\delta$ 置换的尾同时取特征向量，不把单一尾上的一个基向量擅称为 deck 特征向量。

## 2. 原有限角的整幂等元

仍用 R1030 的
$$
G=\operatorname{PGL}_2(\mathbf F_p),\qquad
N=N_{\rm ns}/\mathbf F_p^\times,\qquad |N|=2(p+1),\qquad
e_N=\frac1{|N|}\sum_{n\in N}n.
$$
令 $V_m$ 为有限尖点表示 $\theta_m=\widetilde\omega_2^{m(p-1)}$，令 $P_{m-1}$ 为主系列参数 $a=m-1$ 的有限表示。两者维数分别是 $p-1,p+1$；R1029 的完整正规化子奇偶性给两者的 $N$-固定空间都为一维。

记其特征零中央幂等元为 $e_{V_m},e_{P_{m-1}}$，定义
$$
\boxed{\quad E_m=(e_{V_m}+e_{P_{m-1}})e_N.\quad}
\tag{1193.5}
$$
先证明 $E_m$ 确实属于 $e_N\mathbf Z_p[G]e_N$，不只是在泛纤维存在。

### 2.1 两个有限表示的真实共同剩余因子

对一般奇 $1<r\le m$，置 $a=r-1$。有限表示的剩余半单化为
$$
\overline V_r^{\rm ss}
=\bigl(\operatorname{Sym}^{2r-2}k^2\otimes\det^{1-r}\bigr)
\oplus
\bigl(\operatorname{Sym}^{p-1-2r}k^2\otimes\det^r\bigr),
$$
$$
\overline P_a^{\rm ss}
=\bigl(\operatorname{Sym}^{2a}k^2\otimes\det^{-a}\bigr)
\oplus
\bigl(\operatorname{Sym}^{p-1-2a}k^2\otimes\det^a\bigr).
\tag{1193.6}
$$
这里只用半单化，不假设原整表示分裂。可直接用 Brauer characters 自证这些式子：在 split 元的特征值比 $z$ 上，第一项是 $\sum_{j=-a}^a z^j$；第二项补成全 $\mathbf F_p^\times$ 指数和，并在主系列情形重复两端。因此得到 $0$ 或 $z^a+z^{-a}$。在 nonsplit 元上取 $z^{p+1}=1$，尖点两项的指数并恰少 $\pm r$，故和为 $-z^r-z^{-r}$；主系列则恰为全部 $p+1$ 个指数，和为零。中心处维数分别是 $p-1,p+1$。这覆盖全部 $p$-regular classes，并由 Brauer–Nesbitt 给 (1193.6)。其中每个对称幂次数小于 $p$；其不可约性也可由两个根子群的有限差分提取所有 divided derivatives 直接验证，因次数内的阶乘和 Vandermonde 都可逆。

用 Cartan eigenvariables $A,B$，一个 norm 元作用为 $A\mapsto\lambda A,B\mapsto\lambda^pB$。共同因子
$$
W_a=\operatorname{Sym}^{2a}k^2\otimes\det^{-a}
$$
的 Cartan 固定线是 $k A^aB^a$；正规化子交换元在该线上作用为 $(-1)^a=1$。故 $\dim W_a^N=1$。

两个第二因子都没有 Cartan 固定向量。确切地，尖点第二因子的单项式下标必须满足
$$
i\equiv p-r\pmod{p+1},\qquad 0\le i\le p-1-2r,
$$
主系列第二因子则要求 $i\equiv p-a\pmod{p+1}$、$0\le i\le p-1-2a$；两个区间中都无解。

### 2.2 整系数及真正几何作用

对两表示定义整 spherical trace
$$
\phi_V(g)=\operatorname{Tr}(e_Ng\mid V_m),\qquad
\phi_P(g)=\operatorname{Tr}(e_Ng\mid P_{m-1}).
$$
稳定格存在，且 $|N|$ 是 $p$-单位；故这些值整。有限 character 的全部相关值属于 $\mathbf Q_p$：split Teichmüller 值已在 $\mathbf Q_p$，nonsplit character 的两个项被未分歧 Frobenius 互换。于是 $\phi_V,\phi_P$ 取值于 $\mathbf Z_p$。

在任何剩余 Jordan–Hölder 过滤上，$e_Ng$ 的 trace 可逐因子相加。(1193.6) 的第二因子上 $e_N=0$，所以
$$
\phi_V(g)\equiv\phi_P(g)\pmod p.
\tag{1193.7}
$$
完整 character 幂等公式因而给
$$
E_m=
\frac1{p(p^2-1)}\sum_{g\in G}
\bigl((p-1)\phi_V(g^{-1})+(p+1)\phi_P(g^{-1})\bigr)g
\in e_N\mathbf Z_p[G]e_N,
\qquad E_m^2=E_m.
\tag{1193.8}
$$
每个分子都被 $p$ 整除，未把整体 trace 的整性代替逐系数整性。

由同一个 full-$p$ 模型取 pull–push，再作原 $H_6$ 平均与 $\kappa_4$ 下降，得到实际原 Jacobian 上的整 $p$-进幂等元。其特征零目标准确是 $\tau_m+\mathrm{PS}_{m-1}$；两个 finite-type 固定方向均为一维，原旧球面空间 $S_2(H_6)=0$。本篇不把 $E_m$ 改称单独 $\tau_m$ 投影。

R1021/R1030 的完整模 $p$ 仿射作用同时保留全部 Weil 配对分支。因 (1193.8) 的系数整，$E_m$ 逐 $\pi_0$-normal 层作用，不会用一个 $p$ 分母把未算的更高层回灌到当前层。

## 3. 原负 Hodge 向量及首中心层的唯一性

在原特殊晶体中，$E_m$ 的 tame 权只可能为
$$
\pm m^2,\qquad \pm(m-1)(m+1)=\pm(m^2-1)
\pmod{e_0}.
\tag{1193.9}
$$
前一对来自 $\tau_m$，后一对来自 $\mathrm{PS}_{m-1}$。原特殊 Hodge 的权 $m^2$ 只在 (1193.3) 的 generic 尾上，所以 $E_m$ 在这个整个底 Hodge 空间为恒等。原 compact-type Hodge 自由性与 base change、tame 及 deck 平均，给权 $m^2$、deck $\zeta^2$ 的整提升；施 $E_m$ 后仍提升同一个 $L$。将所得实际微分记为 $\Omega_L$。

在原节点，保留真正单位并写
$$
z_sw_s=\rho_s\pi_0,\qquad
b-s=\kappa_s w_s^m+\cdots,\qquad
u=\lambda_s w_s+\cdots,
\quad \rho_s,\kappa_s,\lambda_s\ne0.
\tag{1193.10}
$$
由 (1193.4)，从尾到中心的首 polar part 准确是
$$
2L_s\rho_s\pi_0 w_s^{-2}\,dw_s.
\tag{1193.11}
$$
中心的完整惯性权均为 $p+1$ 的倍数，而
$m^2\equiv1\pmod{p+1}$。因此在 $0<n\le2m$ 中，只允许中心第 $n=1$ 层；下一可能层为 $2m+3$。

这个中心层的 character 是 $u^{-1}$。在 SS 点，$db/u$ 的阶为 $m-2$；在三个 CM 标记处的阶为 $4g-2$；在每个无穷远点的阶为零。故所有只在 $S$ 具有本节所需二阶极部、在其余点正则的微分，准确为
$$
\eta_T=\frac{T(b)}{uA_p(b)}\,db,\qquad
\deg T\le m-1.
\tag{1193.12}
$$
说明无遗漏：在 SS 点，允许 $T/A_p$ 至多一阶基极点；在 CM 点，$4g-2<m$，不允许额外基极点；其余有限点亦不允许。无穷远要求 $T/A_p$ 有界，正给所示次数界。其零 polar part 空间恰为 $k\,db/u$。

但 $\delta^*(db/u)=\zeta\,db/u$，属于正 deck 角色。相反，$db/(uA_p)$ 的角色是 $\zeta^2$。所以负角色中的首中心层唯一，且
$$
\boxed{\quad
\overline{\pi_0^{-1}\Omega_L}|_I
=\frac{T_L(b)}{uA_p(b)}\,db,
\qquad T_L\in k[b^3],\quad \deg T_L<m-1.
\quad}
\tag{1193.13}
$$
这个除法仅沿 $I$ 读取指定 normal 层，不称整个模型上均可除 $\pi_0$。

在 $s$ 处，(1193.12) 的 $w_s^{-2}dw_s$ 系数为
$mT(s)/(\lambda_sA_p'(s))$。与 (1193.11) 比较给
$$
T_L(s)=\frac2m\lambda_s\rho_sA_p'(s)L_s.
$$
Lagrange 插值因此准确写为
$$
\boxed{\quad
T_L(b)=\frac2m\sum_{s\in S}
\lambda_s\rho_s L_s\frac{A_p(b)}{b-s},\qquad
T_L(1)=\frac{2A_p(1)}m
\sum_{s\in S}\frac{\lambda_s\rho_sL_s}{1-s}.
\quad}
\tag{1193.14}
$$
负角色条件使右侧确属于 $k[b^3]$。这里保留原节点全部单位；没有将 $L_s$ 或任何 $\lambda_s,\rho_s$ 规范为一。

## 4. 完整低 normal 归纳与 CM 首阶

在原 $c_1$ 尾继续使用
$$
D:\quad y^2=x(x^{2g}+A_{\rm tail}),\qquad
Q=(0,0),\qquad t=\sqrt x,
$$
并在它与中心的节点固定
$$
z_Dw=\rho_1\pi_0^3,\qquad
b-1=\kappa_1w^m+\cdots,\qquad
u=\lambda_1w^{2g}+\cdots.
\tag{1193.15}
$$
本篇 $\kappa_1$ 特指这一个显示的节点首项；不与 R1032 合并 coarse/fine 后同名字母的单位作无说明等号。

原首中心微分在该标记的首项为
$$
\pi_0\frac{m\kappa_1}{\lambda_1A_p(1)}T_L(1)
w^{4g-2}\,dw.
\tag{1193.16}
$$
厚度三把它准确送到第
$$
1+3(4g-1)=12g-2=2m
\tag{1193.17}
$$
层，在 $D$ 上的最高极部为
$$
-\frac{m\kappa_1\rho_1^{4g-1}}{\lambda_1A_p(1)}
T_L(1)\,\pi_0^{2m}z_D^{-4g}\,dz_D.
\tag{1193.18}
$$

须同时排除所有更早的 CM 层，而不只比较一个选定 monomial。CM 尾全纯 Hodge 权为 $3m(2i+1)$、$0\le i<g$。要出现在权 $m^2$ 的提升第 $n$ 层，最小正数为
$$
n=m^2-3m(2i+1)\ge2m.
$$
因此 $0<n<2m$ 没有 CM holomorphic 自由项。中心在此范围只有第 $1$ 层，且 (1193.13) 在 CM 标记处具有至少 $4g-2$ 阶零，最早传入正是 (1193.17)。

其余尾的往返不改变已确定的第 $1$ 中心层，也不能产生一个角色不允许的更早中心层。中心自身的 smooth deformation 仍按 R1032 §3 在只支撑 SS 标记的充分大极点除子下逐阶提升；它在 CM 标记正则。节点 polar parts 的无 residue 条件按同一个 compact-type 树逐叶检查。若存在最早非零 CM 层 $n<2m$，则既无 incoming polar part，又无同角色全纯项，矛盾。

故对本篇实际 $\Omega_L$，
$$
\Omega_L|_D\equiv0\pmod{\pi_0^{2m}}.
\tag{1193.19}
$$
在第 $2m$ 层，中心下一可能层 $2m+3$ 尚未出现；因此极阶至多 $4g$，最高系数准确是 (1193.18)。

## 5. 首 CM 层的完整二次空间及全部分支单位

该层的角色为
$$
m^2-2m=3m(2g-1).
$$
在 $D$ 上，极只在无穷远，极阶至多 $4g$。仿射正则微分中，$x^jdx/y$ 的角色要求 $j\equiv g-1\pmod{2g}$，极阶界要求 $j\le3g-1$；$x^jdx$ 的偶角色不能出现。所以完整空间为
$$
\langle\mu,\nu\rangle=\langle dF,\nu\rangle,
\quad
\mu=x^{3g-1}\frac{dx}{y},\quad
\nu=x^{g-1}\frac{dx}{y},\quad
F=x^{g-1}y,
$$
$$
dF=\frac{4g-1}{2}\mu+
       \frac{2g-1}{2}A_{\rm tail}\nu.
\tag{1193.20}
$$
这里 $\nu$ 是真正全纯项，不能由最高极部删除。因 $dF$ 的最高项为 $-(4g-1)z_D^{-4g}dz_D$，原首层在单个分支上必为
$$
\kappa_{\rm hi}T_L(1)dF+c_LA_{\rm tail}\nu,
\qquad
\boxed{\quad
\kappa_{\rm hi}=
\frac{m\kappa_1\rho_1^{4g-1}}
{(4g-1)\lambda_1A_p(1)}\in k^\times.
\quad}
\tag{1193.21}
$$
$c_L$ 在施实际角投影前保留全部提升自由项。

现在按原 full-$p$ 来源同时保留全部非零 pairing 分支。仍用 R1030 的
$$
c=A^{p+1}-B^{p+1},\quad U=(A^{p+1}+B^{p+1})/2,
\quad V=AB,
$$
$$
A_{\rm tail}=c^2/4,\qquad x=V^6,\quad y=UV^3,
\qquad F=UV^{m-2}.
\tag{1193.22}
$$
一个 norm 为 $d$ 的 Cartan 元给 $c,U,V$ 同乘 $d$。于是 $F$ 的 norm 角色为 $d^{m-1}$，$\nu$ 为 $d^{m-3}$。因此在分支并上，两个 invariant 微分准确按
$$
c^{1-m}dF,\qquad c^{3-m}\nu
\tag{1193.23}
$$
运输；二者与 (1193.21) 的 $A_{\rm tail}=c^2/4$ 相容。由于 norm 群在非零 $c$ 分支上传递，这已锁定每个系数的分支依赖，只剩原 supersingular 来源上的共同常数。正规化子交换元将 $c$ 送到 $-c$，而 $1-m,3-m$ 均为偶数，所以无额外符号。

### 5.1 $E_m$ 固定真正的 $dF$ 项

令
$$
\mathcal W=\operatorname{Sym}^{2p-4}(k^2)\otimes\det^{1-m}.
$$
它在分支并上正由 $c^{1-m}$ 乘齐次多项式实现，故是原 $G$-模。Cartan 固定单项式下标满足 $i\equiv m-2\pmod{p+1}$，范围内只有 $m-2,3m$；正规化子交换二者，故
$$
\mathcal W^N=k\,c^{1-m}F.
\tag{1193.24}
$$
在抽象 $\det^{1-m}$ 线上保留同一 twist，只对齐次多项式作 $\mathbf F_p^2$ evaluation，取与 R1030 同一 Cartan eigenvariables，使 $A^p=B,B^p=A$。这里不在这些点上评价 $c^{1-m}$：这些点上 $c=0$，该因子只是在实际非零 pairing 分支上的几何实现。多项式 evaluation 与上述抽象 determinant twist 合在一起仍为 $G$-等变映射。于是
$$
F|_{\mathbf F_p^2}=(AB)^{m-1}.
$$
右侧属于 (1193.6) 的共同因子
$W_{m-1}=\operatorname{Sym}^{p-3}k^2\otimes\det^{1-m}$，且是其非零 $N$-固定向量。该低次空间的 evaluation 单射：各变量次数均小于 $p$，在所有 $\mathbf F_p^2$ 点为零迫多项式为零。

在 $W_{m-1}$ 上，$\overline E_m$ 的作用是 $e_N$，因为它是尖点格的一个组成因子，而 $E_m$ 在特征零尖点表示上恰为 $e_N$。evaluation 与所有 $G$ 作用相容。由 (1193.24)，$E_m(c^{1-m}F)$ 是它的一个标量倍；evaluation 后该标量必为一。因此
$$
E_m(c^{1-m}F)=c^{1-m}F,
\qquad
E_m(c^{1-m}dF)=c^{1-m}dF.
\tag{1193.25}
$$
这里 $c$ 在每个所指 pairing 分支为常数，微分与实际 level 换基交换。

### 5.2 $E_m$ 杀掉真正的全纯修正

微分 $c^{3-m}\nu$ 是原三个 CM 尾上的全纯特殊 Hodge 向量；若须固定 deck 角色，先在这三个真实分量上作原平均。其完整惯性权是 $m(m-2)$。该权与 (1193.9) 的四个权均不同模 $e_0$。特殊晶体为无挠格，tame character 分解为整直和，所以实际 $E_m$ 在这个特殊 Hodge 向量上为零：
$$
\boxed{\quad E_m(c^{3-m}\nu)=0.\quad}
\tag{1193.26}
$$
也可先取其实际整 Hodge eigenlift 再约化；不能先固定一个 $c$ 分支后把 $A_{\rm tail}$ 当成能从投影提出的常数。

将 (1193.25)–(1193.26) 施于已在原 packet 中的 $\Omega_L$，得到完整结论
$$
\boxed{\quad
\overline{\varepsilon^{-2}\Omega_L}|_D
=\kappa_{\rm hi}T_L(1)\,d(x^{g-1}y).
\quad}
\tag{1193.27}
$$
它保留 (1193.14)、(1193.21) 的全部实际尺度。

## 6. 原 marked jet 及 packet 非零泛函

在同一个原 $Q=(0,0)$，
$$
F=t^{2g-1}\sqrt{A_{\rm tail}+t^{4g}}.
$$
故首项准确为
$$
\overline{\varepsilon^{-2}\Omega_L}|_D
=\kappa_{\rm hi}T_L(1)(2g-1)\sqrt{A_{\rm tail}}
t^{2g-2}dt+O(t^{6g-2})dt.
\tag{1193.28}
$$
$2g-1=(p-5)/6$ 是 $p$-单位。整个负 Hodge packet 上的泛函 $T_L(1)$ 非零：取 $T=1$，按 (1193.14) 的逆式指定
$$
L_s=\frac{m}{2\lambda_s\rho_sA_p'(s)}.
\tag{1193.29}
$$
所有系数都是原单位；由 (1193.13) 的真实 deck 等变性，这确是负角色底向量，并存在上述实际整提升。它给 $T_L(1)=1$。这是一个显示的实际 packet 向量，不是把某个未知首项反除后再宣单位。

对于 R1191 已选的 $C$，其 $r=m$ 槽确在 (1193.5) 的尖点部分中；但 (1193.29) 尚未被证明属于该指定 $C$ 的整拉回空间。因而不由 (1193.29) 推出该 $C$ 的首项单位，更不省略同一 $\beta$ 的 MW 消去。

## 7. 同一原有理盘上的完整尾界

消费 R1033 的原曲线参数，而非其最低型目标。本节 $a$ 是原 coarse 参数，$b$ 仍是前文的 Igusa 参数；二者在特殊纤维按原 Frobenius 侧关系运输，不互换：
$$
w=(a-1)/p^3,\qquad z=\varepsilon^3w,\qquad
\sigma z=\xi^{3m}z,
\qquad
\lambda_0=(d\bar z/dt)(Q)\in k^\times.
\tag{1193.30}
$$
将本篇实际 $\Omega_L$ 写成
$$
\Omega_L=\sum_{n\ge1}a_nz^{n-1}dz.
$$
完整角色给 $\sigma a_n=\xi^{m(m-3n)}a_n$。若取该指数模 $e_0$ 的最小非负代表，再代入 (1193.30)，就得到
$$
\varepsilon^{-m}\Omega_L
=\sum_{n\ge1}p^{d_n}c_nw^{n-1}dw,
\qquad c_n\in W(k),\qquad
d_n=\left\lceil\frac{3n-m}{p+1}\right\rceil.
\tag{1193.31}
$$
因此同一零常数的真正 Abel primitive
$$
H_L(w)=\varepsilon^{-m}\int_{c_1}^{x(w)}\Omega_L
$$
满足
$$
v_p([w^n]H_L)\ge d_n-v_p(n).
\tag{1193.32}
$$
对 $1\le n\le n_1:=2g-1$，$d_n=0$ 且 $p\nmid n$；对 $n\ge2g$、$p\nmid n$，$d_n\ge1$。若 $v_p(n)=a\ge1$，用 $n\ge p^a\ge pa$ 得
$$
3p^a-m>a(p+1),
$$
所以 $d_n\ge a+1$。故全部 $p$ 倍次数亦至少再含一个 $p$，并且一般估值下界趋向无穷。最终
$$
\boxed{\quad
H_L\in W(k)\langle w\rangle,\qquad
\deg\overline H_L\le n_1=(p-5)/6.
\quad}
\tag{1193.33}
$$
有限未分歧底时，将 $W(k)$ 换为该实际底的整数环。这里没有把 $O(\pi_0)$ 直接当成 $O(p)$。

由于 $2+3n_1=m$，(1193.27)–(1193.30) 给真正最高系数
$$
\boxed{\quad
[w^{n_1}]\overline H_L
=\kappa_{\rm hi}T_L(1)\sqrt{A_{\rm tail}}\lambda_0^{-n_1}.
\quad}
\tag{1193.34}
$$
所以整个所述 packet 的 $\varepsilon^{-m}$ 归一轮廓具有非零最高系数，其共同尺度不再额外含 $p$。这仍是最高系数与全部尾界，不是最低非零项的单位证明，也不排除深盘中的额外零点。

## 8. 与原 O4 的准确接口

R1191 使同一个实际 $C,\beta$ 的 $r=m$ 槽存在，且原有理 Abel 首向量在该槽上与 MW 直线横截。本文补上一个不同于最低型的真实整几何输入：首中心阶 $1$、simple-Cauchy 核、首 CM normal 阶 $2m$、marked 次数 $(p-5)/6$ 和原 $p^3$ 盘的全部尾。

下一步仍需同一个 $\beta$ 的完整 log 在本篇实际特殊基中的系数，并需检验该列与 (1193.14) 在指定 $C$ 槽及其整格中的楔。$E_m$ 包含主系列，因此不能未经 MW 谱核对，将整个 packet 的 primitive 当成一个消去全部有理点的函数。R1190 的至多一个 $p$ Lie 格损失控制实际子簇运输，但不保证指定法向泛函在其约化上非零。

本篇不将这个结果称为旧 $K_{\mathcal Q,p}$ 或 Fermat-six 条件的镜像；若要比较，必须在原对应、原 $\beta$ 和原标记下另外给出箭头。没有重跑任何有限窗口。Serre 主目标仍 OPEN。

## 9. 来源

- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md) §§2–4：原整个模型、generic/CM Hodge 权、同一个 $b_{\rm lift}$ 与 ordinary quotient。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md) §§2–3：全非约化模 $p$ 仿射图、全部 Weil 配对分支、level 的真正常线性作用。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md) §§1–3：原 $u^m=(1-b^3)^{2g}A_p$、各节点阶、完整惯性与 deck 作用。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md) §§2–3：原正规化子谱、尖点/主系列字符和 fixed-line 奇偶性。本文另行证明最高 packet 的整角，不复用最低型整性代替。
- [R1030](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md) §§1、3–5：实际有限角的几何实现、原 $A,B,c,U,V,x,y$ 及全部分支运输。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md) §§2–3：同一节点主部规则、中心变形及全树 residue 归纳；本文重新计算最高型，不套用该文的最低型 double-Cauchy 核。
- [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md) §1：原 $z=\varepsilon^3w$、$\lambda_0$；本文逐项重新支付 (1193.31)–(1193.34)。
- [R1191](R1191-original-half-rank-factor-all-primitive-inertia-slots.md)、[R1190](R1190-original-one-p-Neron-Lie-lattice-bound.md)：同一原半秩因子上的实际多槽与整格界，始终按各自范围消费。

全部有限表示、插值、normal 递推与尾估值均为纸面证明；没有执行数学程序。


### 本次核定

root 全文核对原 R1028/R1030/R1032/R1033 的模型、正常层、分支运输及积分尺度；o2_high_coefficient 独立纸核 §2 的逐系数整角和 §5.1 的完整 determinant twist/evaluation。低次 evaluation 只作用于多项式，未在 c=0 上评价负幂。没有新增数学执行。
