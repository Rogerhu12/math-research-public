# R1189：原 CM 点差的统一形式倍数与分歧范数下降

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root。

**状态：已证明。** 对全部 $p>37,\ p\equiv5\pmod6$，在原 $X_1$ 的同一个 Jacobian 上，明确整数

$$
\boxed{\quad M_0(p)=p^2(p-1)(p^2-1)\quad}
\tag{1189.1}
$$

将原 $D_0$ 送入其在 $\mathbf Q_p$ 上的实际 Néron 形式核。故任意实际有理同态 $q:J_{X_1}\to A$，包括 R1011、R1187 的同一个半秩目标，均满足 $M_0(p)q(D_0)$ 在原 $A/\mathbf Q_p$ 的 Néron 形式核中。无需计算目标的分量群、环面点数或其它坏纤维群阶。

关键新增点是：在 $p\equiv5\pmod{12}$ 的原双中心模型上，完整惯性把所有图环路反向，因此原 CM 点差的环面 clutching 至多二挠；这把已知的良好部分形式点提升为整个 Jacobian 的实际形式点。之后必须先将其推深到模 $pR$ 真正为零，再作实际范数下降。仅在模 $\pi_0$ 为零时不能跳过这个步骤。

本文保留 R1182 的射影指数 chart 和导子分母成本 $s_{\exp},\delta_L$，不声称目标 Néron 格饱和，也不据此推出 Chabauty 首项为单位或完整候选盘已排除。无数学程序执行。

## 1. 原对象与形式滤过

始终取

$$
X=X_1=\operatorname{Norm}(X_{\rm ns}^+(p)\times_j\mathbf P^1_b),
\quad j=6912b^3(1-b^3),\quad J=J_X,
$$
$$
N=1+\delta+\delta^2,\quad
D_0=(3-N)[c_1-c_0],\quad
P=(p-1)D_0.
\tag{1189.2}
$$

这些是 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 的原点和原除子；$D_0$、$P$ 均定义在 $\mathbf Q$ 上。为避免与原曲线的 $b$ 参数混淆，扩域的底环记为

$$
K_0=\widehat{\mathbf Q_p^{\rm ur}},\quad R_0=\mathcal O_{K_0}=W(\overline{\mathbf F}_p),
$$
$$
e_0=\frac{p^2-1}{2},\quad
m=\frac{p-1}{2},\quad e_0=(p+1)m,
$$
$$
L=K_0(\pi_0),\quad \pi_0^{e_0}=p,
\quad R=R_0[\pi_0].
\tag{1189.3}
$$

$K_0$ 含全部素于 $p$ 的单位根，所以 $L/K_0$ 是次数 $e_0$ 的实际循环扩张。令 $\sigma(\pi_0)=\xi\pi_0$，其中 $\xi$ 为原始 $e_0$ 次单位根。惯性在剩余域 $k=\overline{\mathbf F}_p$ 上恒等。

用 $\mathscr J_0/R_0$、$\mathscr J_R/R$ 分别表示 $J_{K_0}$、$J_L$ 的完整 Néron 模型。它们之间的分歧基变映射不被假设为同构。对任一实际光滑群模型 $\mathscr G/R$，定义

$$
F^a\mathscr G(R)
=\ker\bigl(\mathscr G(R)\to\mathscr G(R/\pi_0^aR)\bigr),\qquad a\ge1.
\tag{1189.4}
$$

它在单位形式坐标中正是各坐标属于 $\pi_0^aR$ 的条件。

## 2. compact-type 行直接消费原实际形式深度

若 $p\equiv11\pmod{12}$，[R1018, Theorem 1018.1](R1018-original-CM-divisor-exact-first-formal-layer.md) 已在同一个 $R$ 上证明

$$
P\in F^m\mathscr J_R(R).
\tag{1189.5}
$$

这是实际形式点的结论，不只是 $\log P$ 的一个赋值结论。原 compact-type 模型使 $\mathscr J_R$ 为阿贝尔方案；原点、Igusa 主化和全部惯性权已经登记，本篇不重复证明它们。由整群律也有

$$
2P\in F^m\mathscr J_R(R).
\tag{1189.6}
$$

## 3. 双中心行的真实环面 clutching 被二杀掉

现在取 $p\equiv5\pmod{12}$。消费 [R1038 §§1–4](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md) 的实际 Raynaud 图

$$
0\longrightarrow T\longrightarrow G\longrightarrow B\longrightarrow0,
\qquad
0\longrightarrow\Lambda\longrightarrow G^{\rm an}
\longrightarrow J^{\rm an}\longrightarrow0.
\tag{1189.7}
$$

这里 $B/R$ 良好，整个 $J$ 不被称为良好。R1038 的原 vertical twister 和两个中心的主函数已证明

$$
P\in\mathscr J_R^0(R),\qquad
P\text{ 在 }B_k\text{ 中的像为零}.
\tag{1189.8}
$$

由同一篇的 bounded lifting，$P$ 有唯一 $P_G\in G(R)$。唯一性来自原周期格的正定 tropical monodromy 配对，给 $\Lambda\cap G(R)=0$。因此 $P$ 的下降固定性精确提升为

$$
\sigma(P_G)=P_G.
\tag{1189.9}
$$

没有在此丢掉一个可能的周期平移：若两 bounded lifts 相差周期，刚述交为零将它消去。

令 $t=\overline{P_G}\in T_k(k)$。R1038 §3 已证明完整生成元 $\sigma$ 交换两个中心，逐条反向所有连接路径，故在实际图 $H_1$ 上为 $-1$。环面角色格由该图给出，Raynaud 函子性使其上的作用也为 $-1$。因为 $\sigma$ 在 $k$ 上恒等，它在 $T_k$ 上的群态射就是 inversion；不存在一个额外的剩余域 Frobenius。由 (1189.9)，

$$
\boxed{\quad t=\sigma(t)=t^{-1},\qquad t^2=1.\quad}
\tag{1189.10}
$$

所以 R1038 中原先保留的素于 $p$ 的阶 $r_0$，在这一个指定点上实际上满足 $r_0\mid2$。

取 $T(R)[2]$ 中唯一约化为 $t$ 的点 $\tau$。它存在且唯一，因为 $2$ 为单位且 $R$ 严格 henselian，$T[2]$ 有限 étale。唯一性同时给 $\sigma(\tau)=\tau$。于是

$$
\widetilde P=P_G-\tau\in\widehat G_0(R),\qquad
\sigma(\widetilde P)=\widetilde P,
\qquad 2P_G=2\widetilde P.
\tag{1189.11}
$$

这里仅用真实群上的二倍，不需要一个 $p$ 进完备 Hecke 幂等元作用在 $\tau$ 上。

接着保留整个 $G$ 的形式方向。R1038 (1038.12) 及其后给原 $B$ 的全部形式权；环面另给权 $e_0/2$。所有权取代表 $0\le w_i<e_0$ 后均满足

$$
m\le w_i<e_0-m.
\tag{1189.12}
$$

在完整单位形式环内对任意提升参数作 $e_0$ 阶 character 平均；因 $e_0$ 为 $p$ 单位，可选一组实际整参数 $Z_i$ 使 $\sigma Z_i=\xi^{w_i}Z_i$。其线性部仍是一组余切基，故仍是形式坐标。对固定点 $\widetilde P$ 代值后，$Z_i(\widetilde P)\in R$ 是相应 character 的元素。由

$$
R=\bigoplus_{a=0}^{e_0-1}R_0\pi_0^a
$$

的完整惯性分解可知其赋值至少为 $w_i$。因此

$$
\widetilde P\in F^mG(R),\qquad
2\widetilde P\in F^mG(R).
\tag{1189.13}
$$

原 Raynaud 形式同构 $\widehat G\simeq\widehat{\mathscr J_R^0}$ 保实际群律和 uniformization，所以 (1189.11)–(1189.13) 准确给

$$
\boxed{\quad 2P\in F^m\mathscr J_R(R)\quad}
\tag{1189.14}
$$

在双中心行成立。结合 §2，(1189.14) 现覆盖全部 $p>37,\ p\equiv5\pmod6$，包括真实非平凡环面。

## 4. 两次乘 $p$ 将点推到模 $pR$ 的真实单位截面

下面的形式群估计不要求好约化。令 $\mathscr G/R$ 为任意光滑交换群方案，单位形式群写成 $R[[Z_1,\ldots,Z_d]]$。整不变微分构成一组基；在该基下 $[p]^*\omega=p\omega$。模 $pR$ 后，$[p]$ 的全部坐标偏导均为零。

更具体地，不变微分基与 $dZ$ 的转换矩阵在形式环内可逆，故其等式迫 $[p]$ 的 Jacobian 矩阵系数都被 $p$ 整除。若坐标级数中的一个单项式 $c_\alpha Z^\alpha$ 有某个 $\alpha_i$ 不被 $p$ 整除，对 $Z_i$ 微分即得 $c_\alpha\in pR$。剩下的非恒定单项式每个指数均为 $p$ 的倍数，故总次数至少 $p$。因此可写

$$
[p](Z)=p\mathbf A(Z)+\mathbf B(Z),\qquad
\mathbf A\in(Z)R[[Z]]^d,\quad
\mathbf B\in(Z)^pR[[Z]]^d.
\tag{1189.15}
$$

此论证在整个非约化环 $R/pR$ 上进行；不只在约化特殊纤维 $k$ 上进行。因此每个 $r\ge1$ 都有

$$
[p]\bigl(F^r\mathscr G(R)\bigr)
\subset F^{\min\{e_0+r,pr\}}\mathscr G(R).
\tag{1189.16}
$$

在原深度 $r=m$，利用 $e_0=(p+1)m$，第一步给 $pm$；第二步给 $e_0+pm$，因为

$$
pm<e_0+m,\qquad
e_0+pm=(2p+1)m\le p^2m.
$$

故对 (1189.14) 中的同一点

$$
Q:=2p^2P=2p^2(p-1)D_0
\in F^{e_0+pm}\mathscr J_R(R)
\subset F^{e_0}\mathscr J_R(R).
\tag{1189.17}
$$

由 $\pi_0^{e_0}=p$，最后一个条件是

$$
Q=0\quad\text{在 }\mathscr J_R(R/pR)\text{ 中}.
\tag{1189.18}
$$

它比 $Q$ 在 $\mathscr J_R(k)$ 中为零更强，正是下降所需的条件。

## 5. 实际范数经光滑 Weil restriction 下降

本节证明一个适用于当前模型的下降步骤，而不把分歧基变映射倒过来用。

在 $\mathscr J_R$ 中选包含单位截面的光滑 affine 开集 $U$。因为 $Q$ 的特殊值为单位，$Q:\operatorname{Spec}R\to\mathscr J_R$ 的全部像均在 $U$ 内。有限自由扩张 $R/R_0$ 下，Weil restriction

$$
\mathscr U=\operatorname{Res}_{R/R_0}U
\tag{1189.19}
$$

存在、为光滑有限型 $R_0$-方案。可从 $U$ 的有限 affine 方程并取 $R$ 的 $R_0$-基直接构造；光滑性由 infinitesimal lifting 性质保持。正式出处为 Bosch–Lütkebohmert–Raynaud，*Néron Models*，§7.6 Theorem 4、Proposition 5。

泛纤维上有原 $J$ 的实际 trace/norm 态射

$$
\operatorname{Nm}_{L/K_0}:\operatorname{Res}_{L/K_0}J_L\longrightarrow J_{K_0},
\qquad z\longmapsto\sum_{\gamma\in\operatorname{Gal}(L/K_0)}\gamma z.
\tag{1189.20}
$$

这里群律用加法，因而范数就是共轭点之和。该态射经 Galois 下降由几何乘积上的求和给出。限制到 $\mathscr U_{K_0}$ 后，$\mathscr J_0$ 的 Néron 映射性质给唯一延拓

$$
\nu:\mathscr U\longrightarrow\mathscr J_0.
\tag{1189.21}
$$

$\mathscr U$ 本身不必是一个群；只用其光滑性。其单位截面经 $\nu$ 映为单位，因为泛纤维如此且 $\mathscr J_0$ 分离。

把 $Q\in U(R)$ 看成 $\mathscr U(R_0)$ 中的点。Weil restriction 的点函子给

$$
\mathscr U(k)=U(R\otimes_{R_0}k)=U(R/pR).
\tag{1189.22}
$$

由 (1189.18)，这个点在 $\mathscr U(k)$ 中恰为单位截面。故 $\nu(Q)$ 在 $\mathscr J_0(k)$ 中为零。另一方面 $Q$ 本来定义在 $\mathbf Q_p$ 上，在 (1189.20) 中每个共轭都是它自己，所以

$$
\nu(Q)=e_0Q=M_0(p)D_0.
\tag{1189.23}
$$

得到 $M_0(p)D_0$ 在 $K_0$ 上的 Néron 形式核中。

最后下降回 $\mathbf Q_p$。$R_0/\mathbf Z_p$ 的分歧指数为一，剩余扩张可分；BLR §7.2 Theorem 1(ii)、Corollary 2 给

$$
\mathscr J_0\simeq\mathscr J_{\mathbf Z_p}\otimes_{\mathbf Z_p}R_0.
\tag{1189.24}
$$

这里也包含严格未分歧底的完备化。原点 $M_0(p)D_0$ 定义在 $\mathbf Q_p$ 上，其约化在扩域到 $k$ 后为零，故其在 $\mathbf F_p$ 上的约化已为零。因此

$$
\boxed{\quad
M_0(p)D_0\in
\ker\bigl(\mathscr J_{\mathbf Z_p}(\mathbf Z_p)
\to\mathscr J_{\mathbf Z_p}(\mathbf F_p)\bigr).
\quad}
\tag{1189.25}
$$

完整的原分量群、双中心环面和分歧都已进入该证明；没有用目标模型的未知有限群阶。

## 6. 对每个实际商的函子性与 R1182 的具体代入

任意实际有理同态 $q:J\to A$ 延拓为两个完整 Néron 模型之间的同态，且保持单位截面。令 $\beta=q(D_0)$、$\Lambda_A=\operatorname{Lie}(\mathscr A_{\mathbf Z_p})$，由 (1189.25)

$$
M_0(p)\beta\in\mathscr A^1(\mathbf Z_p),\qquad
\log_p(M_0(p)\beta)\in p\Lambda_A.
\tag{1189.26}
$$

后式是实际整不变微分的形式积分：总次数 $r$ 的分母至多 $r$，在 $p\mathbf Z_p$ 上赋值至少 $r-v_p(r)\ge1$。这里没有除以 $dq$，不需要 $q$ 的微分饱和或目标在 $p$ 好约化。

特别适用于 R1187 的 $q_*$，也适用于经该篇同源图再得到的任一实际 $J\to B$。原 CM 点不换，原 Mordell–Weil 对数线不换。

在 R1182 所选射影模型、原 Néron 基和实际指数 chart 中，仍置

$$
s=\max\{s_{\exp},v_p(\delta_L)+1\}.
$$

现在可以明确取

$$
\boxed{\quad
M=p^{s-1}M_0(p)=p^{s+1}(p-1)(p^2-1),
\qquad\beta'=M\beta.
\quad}
\tag{1189.27}
$$

它满足 R1182 的实际指数域和 Fuchs–Pham 严格小球条件。特别 $v_p(M_0(p))=2$，且

$$
M_0(p)<p^5,
\qquad
M<p^{s+4}.
\tag{1189.28}
$$

例如，对 R1187 的同一 $\beta_*$ 与极化 $\mathcal L$，原 CM 点高度界可以写为

$$
h_\iota(M\beta_*)
\le
18p^{2s+2}(p-1)^2(p^2-1)^2K_*
\frac g{g-1}H_{\rm br}(D_p)+\frac{E_{\mathcal L}}3.
\tag{1189.29}
$$

这消去了目标坏纤维 reduction exponent 的独立未知成本。$s_{\exp},\delta_L,E_{\mathcal L}$ 与实际模型、微分基、首项相对位置继续保留。R1182 的本原化虽能消掉同一 $\beta$ 的辅助标量，使用其有效线性形式定理时仍应输入 (1189.27) 的真正点高度，不能省略它。

本篇不将 (1189.25) 改写成一个 Néron 格等同，也不将上述多项式大小的形式倍数改写成固定盘内的唯一性结论。后续继续将实际模型与首项成本代入 R1186，并与原候选深度比较。

## 7. 来源和核对范围

1. [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)，Theorem 1018.1、§§1–2：compact-type 行原实际点 $P$ 的 $F^m$ 深度、同一个 $e_0,m$ 和未分歧底。R1023 的对数首项不是本篇 (1189.5) 的替代输入。
2. [R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)，§§3–4，尤其 (1038.12)、(1038.15)–(1038.17)：双中心完整图惯性、原 multidegree、唯一 bounded lift、原 Raynaud 形式群和全部实际权。本篇新增 (1189.10) 的二挠结论及其对整个 $J$ 的形式提升。
3. Siegfried Bosch, Werner Lütkebohmert, Michel Raynaud，*Néron Models*，Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol.21，Springer，1990。[原书 PDF](https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf)：§7.2 Theorem 1(ii)、Corollary 2，印刷 pp.176–177；§7.6 Theorem 4、Proposition 5，pp.194–196。root 已实读原文和相应页图；§5 另外逐式给出所需范数延拓与点函子证明。
4. [R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md) §§2、9，[R1187](R1187-original-bounded-half-rank-quotient-and-polarization.md) §§6、10：原指数域、点高度和实际同源图。本篇仅替换真实形式倍数，不反改任何首项单位或候选覆盖边界。

o2_high_coefficient 另亲读 R1018、R1038 的相应段，纸核完整图角色、二挠下降、两次 $[p]$ 和实际 norm；root 完成证明后直接登记，无新增数学程序或旧窗口重算。Serre 主目标仍 OPEN，继续原模型与全局排点。
