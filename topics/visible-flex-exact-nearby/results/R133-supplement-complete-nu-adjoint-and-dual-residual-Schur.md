# R133 补篇：完整 mean 的 ν 伴随列、紧支消去及双残差标量门

2026-11-14。**准确恒等式及实际外边界费用已证明；26 个精确有理/代数门已执行。**
本篇把最终 ac1 中心的参数标量改写为真实伴随配对。紧支参数的 $w'$ 项在完整
moving 算子中消去，保留非局部原函数、独立 mean、径向多项式跳和 normalized
背景列。此式不需要除 $\sqrt{-K}$。

当前尚未恢复完整伴随候选或 $\nu$ response，也没有实际全补逆常数。
因此不宣称 $\nu$ Schur 已非零。已执行的有理预算支付了真正 nonlinear
regular 边界相对于原数值 proposal 的完整算子费用；后面的双残差门规定
仍须消费的实际量，不以有限矩阵条件数替代。

## 1. 同一中心、空间和完整线性化

实际中心、精确 $\alpha,\nu$、完整 primitive 及目标身份沿用
[最终真实端口](R133-supplement-final-moving-centre-actual-regular-boundary.md)。
中心 SHA256 为
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。

始终使用实际四重反射空间：$u,h_1,\psi_1$ 奇，
$v,h_2,\psi_2$ 偶；偶部分的 mean 包含在完整空间中。
$I=\partial_\phi^{-1}P_{\ne0}$ 取零 mean 原函数。
归一化圆周积分下 $I^*=-I$；反射保持实际腰及外端的原函数 gauge。

记

$$
 Q=(u,v),\quad m=\langle v\rangle,\quad S=u^2+Kv^2,\quad
 d=-\beta I S,\qquad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},
 \quad \mathsf A=dI_2+\gamma mJ.                         \tag{S.1}
$$

准确 moving 方程为
$Q_r=dQ_\phi+\gamma mJQ_\phi+
(-\beta u(1+S),\,\beta v(1-S))$。
其 residual 线性化在任意完整近似中心都准确为

$$
 \mathcal D h=h_r-\mathsf A h_\phi-Lh-Nh,                \tag{S.2}
$$
$$
 L=\begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix},
 \qquad
 Nh=-2\beta Q_\phi I(uh_1+Kvh_2)
                   +\gamma JQ_\phi\langle h_2\rangle.  \tag{S.3}
$$

最后一项是真 rank-one mean 列，不可删除。
(S.2) 不要求近似中心已满足 PDE；没有用 PDE 偷换任何 PPoly 径向导数。

## 2. 全伴随和准确 Green 恒等式

实域系数为实，先在实 Hilbert 配对推导后可复化。
由 $I^*=-I$，

$$
 N^*\psi=2\beta(u,Kv)I(Q_\phi\cdot\psi)
            +\gamma e_2\langle JQ_\phi\cdot\psi\rangle.
                                                               \tag{S.4}
$$

因此

$$
 \boxed{\mathcal D^*\psi
 =-\psi_r+\mathsf A^T\psi_\phi+d_\phi\psi
                -L^T\psi-N^*\psi.}                    \tag{S.5}
$$

即使保持反射，$\langle JQ_\phi\cdot\psi\rangle$ 一般也不为零。
在每个真实光滑径向片，完整角积分给

$$
 \langle\psi,\mathcal D h\rangle
 -\langle\mathcal D^*\psi,h\rangle
              =\partial_r\langle\psi,h\rangle.         \tag{S.6}
$$

非局部原函数及 mean 均由其完整伴随准确消去。
对固定真实径向接缝记 $[h]_i=h_i^+-h_i^-$，允许 trial 分片，则

$$
 \int\langle\psi,\mathcal D h\rangle\,dr
 =[\langle\psi,h\rangle]_0^R+
   \int\langle\mathcal D^*\psi,h\rangle\,dr
 -\sum_i\{\langle[\psi]_i,h_i^-\rangle
                         +\langle\psi_i^+,[h]_i\rangle\}.           \tag{S.7}
$$

不能因体 residual 小就忽略 response 或 adjoint 的准确 dyadic 跳。
真实目标连续的接缝不产生虚构跳。

## 3. 固定未规范化状态的 ν 源与全部 mean

目标为 $E_\nu=E e^{\nu w}$，
$w=4096t^6(1-t)^6$、$t=(r-1/20)/(13/100)$，
支于 $[1/20,9/50]$。记

$$
 T=\frac{\beta}{2E_\nu},\qquad
 \partial_\nu K=-Kw+Tw',\qquad
 \partial_\nu\gamma=\gamma w/2.                         \tag{S.8}
$$

$\beta$ 不依赖这个参数。固定未规范化 $Q$ 时定义

$$
 P=I(v^2),\qquad W=P Q_\phi+v^2Q,
$$
$$
 A_\nu=-\beta T W+\gamma mT(v_\phi,0),\qquad
 B_\nu=\beta K W-\frac{\gamma m}{2}(Kv_\phi,u_\phi).
                                                               \tag{S.9}
$$

直接对准确 nonlinear 方程微分得

$$
 \boxed{\partial_\nu F=A_\nu w'+B_\nu w.}               \tag{S.10}
$$

其第二平均分别为

$$
 \langle(A_\nu)_2\rangle=-\beta Tm\langle v^2\rangle,
 \qquad
 \langle(B_\nu)_2\rangle=\beta Km\langle v^2\rangle.     \tag{S.11}
$$

所以完整 mean 是 $-\beta m(\partial_\nu K)\langle v^2\rangle$，
与[原完整 ν 列](R133-supplement-compact-metric-parameter-source-and-ray-return-twist.md)
准确相同。原精确 bump 在两个端点至五阶导数均为零，且

$$
 \int_{1/20}^{9/50}w(r)\,dr=\frac{256}{5775}>0.          \tag{S.12}
$$

本次有理算术实际核对了全部这些端点恒等式。

## 4. 伴随局部式：不除 turning weight

沿用[振幅坐标与完整 mean Schur](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
的同一输出 $b_4$：暂列为输出的真实物理四次 Robin 行。
$\overline A$ 保留全部其余非mean 行、外 mean 行、腰 $u=0$、
实际物理振幅行及径向 jump 行。

若完整伴随泛函 $\Lambda$ 满足 $b=\Lambda\overline A$，其体密度为 $\psi$，
而 $\overline A h_\nu=-g_\nu$，未规范化体列 $g_\nu=-\partial_\nu F$，
则紧支控制的两端显式 curvature 参数列为零，因而

$$
 \mathscr S_\nu=b[h_\nu]
       =\int\langle\psi,\partial_\nu F\rangle\,dr.       \tag{S.13}
$$

体源和状态 mean 没有因此删除。
若 $\psi$ 连续且 $\mathcal D^*\psi=0$，对 $w'$ 分部积分并用 (S.6)，得到

$$
 G_\nu:=B_\nu-\mathcal D A_\nu,
 \qquad
 \boxed{\mathscr S_\nu
 =\int w\,\langle\psi,G_\nu\rangle\,dr
        -\sum_iw(r_i)\langle\psi(r_i),[A_\nu]_i\rangle.} \tag{S.14}
$$

积分完整覆盖控制支集；内截区间须另保留
$[w\langle\psi,A_\nu\rangle]$。跳为右值减左值，所以接口符号为负。

$\mathcal D$ 必须包含 (S.3) 的**全部**原函数和 mean 项。
不能用只含 $L$ 的局部算子计算 $G_\nu$。
这里没有 $\sqrt{-K}$ 的倒数。

有限 $M$ 模 moving 中心上，$A_\nu,B_\nu$ 支持至 $3M$，
$G_\nu$ 至 $5M$。这是完整有限中心的代数支持，不限制未知真方向的
无限 Fourier 尾；原 intrinsic primitive 尾仍保留在径向系数盒中。
$\partial_r A_\nu$ 必须由真实保存的 $Q_r,m_r$ 与完整目标 jet 计算，
不能换成 PDE 右侧。

## 5. 近似伴随、normalized 列和全部接口

令 $r_\psi=\mathcal D^*\psi$。任意分片 trial 的准确可计算式是

$$
 \int\langle\psi,\partial_\nu F\rangle\,dr
 =\int w\{\langle\psi,G_\nu\rangle+
                         \langle r_\psi,A_\nu\rangle\}\,dr
 -\sum_iw(r_i)[\langle\psi,A_\nu\rangle]_i,              \tag{S.15}
$$

端点项如上。现在跳的是**整个乘积**：

$$
 [\langle\psi,A_\nu\rangle]_i
 =\langle[\psi]_i,A_\nu^-\rangle+
                         \langle\psi_i^+,[A_\nu]_i\rangle.
$$

不能在消去 $w'$ 时删掉 trial 的体误差或接口误差。

实际有限变量为 $u=\alpha U,v=s+\alpha V$。
固定 $U,V,\alpha$ 的附加背景列
$z_\nu=(0,\sigma_s w)$，
$\sigma_s=-s(a')^2/[2(E_\nu-(a')^2)]$。
normalized 参数 residual 含 $\mathcal D z_\nu-\partial_\nu F$。
$z_\nu$ 连续且支集端点为零，所以

$$
 \int\langle\psi,\mathcal D z_\nu\rangle\,dr
 =\int\langle r_\psi,z_\nu\rangle\,dr
                -\sum_i\langle[\psi]_i,z_\nu(r_i)\rangle.          \tag{S.16}
$$

只有真正连续、零 residual 的伴随才使这个配对准确为零。
这说明 normalized 与未规范化真实标量相同，也规定了 trial 中不能
免费消去的实际费用。

## 6. 双残差标量门

$\mathcal X,\mathcal Y$ 必须是实际全补逆所授的同一状态/数据空间，
包括全部体源、保留边界和跳；不可暗中更改导损阶数。
给 trial $\psi$ 及边界乘子 $\lambda_0,\lambda_R$，令

$$
 \Lambda(f,g_0,g_R,j)
 =\int\langle\psi,f\rangle\,dr+
  \lambda_0g_0+\lambda_Rg_R+
                      \sum_i\langle\psi_i^+,j_i\rangle.           \tag{S.17}
$$

$\lambda_R$ 包含外 mean，$\lambda_0$ 包含实际振幅。
若 $B_0,B_R$ 为全部保留的真边界算子，则由 (S.7)，

$$
 \ell_\psi:=b-\Lambda\overline A
$$
$$
 =\langle b_R^*-B_R^*\lambda_R-\psi_R,h_R\rangle
  +\langle b_0^*-B_0^*\lambda_0+\psi_0,h_0\rangle
  -\int\langle r_\psi,h\rangle\,dr
  +\sum_i\langle[\psi]_i,h_i^-\rangle.                  \tag{S.18}
$$

通常 $b_0=0$。这是完整原 moving 状态的恒等式；
边界必须使用已经支付的真实物理矩变换和 nonlinear 外帽导数，
不能仅把有限矩阵转置当作 (S.18)。

另取完整 trial response $\widetilde h_\nu$，计算

$$
 r_\nu=\overline A\widetilde h_\nu+g_\nu,\qquad
 S_{\rm corr}=b[\widetilde h_\nu]-\Lambda(r_\nu).         \tag{S.19}
$$

若真正全频 $\overline A^{-1}$ 已支付，则准确有

$$
 \boxed{\mathscr S_\nu
    =S_{\rm corr}-\ell_\psi[
                         \overline A^{-1}r_\nu].}       \tag{S.20}
$$

所以严格标量门为

$$
 |S_{\rm corr}|>
 \|\ell_\psi\|_{\mathcal X^*}
        \|\overline A^{-1}r_\nu\|_{\mathcal X}.          \tag{S.21}
$$

若只有逆常数 $K_{\rm inv}$，可用
$K_{\rm inv}\|\ell_\psi\|\|r_\nu\|$。
两个 trial 的误差相乘；全部真实 source、mean 和接口都在
(S.18)–(S.19) 中。无需先对两个近似分支作未经认证的差商。

## 7. 最终真实外边界的实际费用

[全 L2 regular 图](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
在同一最终中心的明确 $r_Z=10^{-12}$ 球给

$$
 L_d<5.898255\,10^{-6},\quad L_0<7.372818\,10^{-7},
 \qquad
 \|\delta Z\|_{L^2_\theta}<.03\|h_2\|_{L^2_\phi}.        \tag{S.22}
$$

原数值 proposal 扩展为明确全频常数 $q_{\rm num}$；
这只定义比较对象，不据有限 solver 宣称全频可逆。
真实 $Q-q_{\rm num}$ 的范数保留正费用

$$
 \epsilon_{\rm prop}=9.1496\,10^{-18}+2^{-512}.          \tag{S.23}
$$

第一项是 whole-$\eta$ 的 $q_*$ 与准确 dyadic proposal 差；
第二项保留全部真实 regular 指数费，包括第四模。
真实 nonlinear Robin 与独立 mean 两行的联合差满足

$$
 \|\Delta B_Rh\|
 \le .03(L_d+L_0+\epsilon_{\rm prop})\|h_2\|_2
 <1.99066104001\,10^{-7}\|h_2\|_2
 <2\,10^{-7}\|h_2\|_2.                                 \tag{S.24}
$$

联合 norm 取非mean $L^2$ 与绝对 mean 的和，因而也控制 Hilbert 直和 norm。
$h_1$ 引起的真实 $\delta B$ 在两个比较算子中相同并准确相消；
没有因实际 $u$ 小就漏掉一行边界。

实际 $\alpha>3/4$。物理 Fourier $L^2$ 转实 sine/cosine 幅度至多付
$\sqrt2$，normalized curvature 行另付 $1/\alpha$；总乘数小于2。
所以全部 normalized 实行的差小于

$$
 4\,10^{-7}\|h_2\|_2,                                  \tag{S.25}
$$

包括暂列输出的真实 $m=4$ 行。
奇 mean 因反射准确不存在，偶 mean 已保留。

独立 $f_B$ 以 $\dot H^2$ 量度，其 normalized 完整输出列不超过

$$
 2(6.55361591650\,10^{-7}+8.1920198958\,10^{-8})
 =1.474563581216\,10^{-6}<1.5\,10^{-6}.                 \tag{S.26}
$$

它必须与 far label 方程联立，不能置零。
这些费用可直接进入 (S.18) 边界 mismatch 和 (S.19) 真实 residual，
不能仅使用 proposal 后宣称低 Schur 已认证。

## 8. 执行范围和实际材料

精确有理/完整 Laurent 源：
[scripts/fourfold_codazzi_nu_adjoint_budget.mjs](../scripts/fourfold_codazzi_nu_adjoint_budget.mjs)；
报告：
[26 门预算](../notes/2026-11-14-R133-final-nu-adjoint-rational.json)。

同一完整函数在可用 V8 实际执行26门；Node CLI 只重放这些 BigInt 运算。
代数单测使用明确人工的非零 mean 有限 Laurent 场，检查完整 adjoint、
参数源、真实径向 jet、5M 支持及 (S.15) 的符号。
一般恒等式由上面的代数推导证明；单测不是最终候选 native 证书。
(S.22)–(S.26) 消费同一最终候选已发表的严格全频常数。

原完整候选分片、trial response/adjoint 和对应闭盒运算尚须恢复；
当前执行环境不可用。后续须保持原 candidate SHA、完整 $\eta$、真实
target 尾、所有 jumps 与完整边界。全补逆、$S_{\rm corr}$ 实际符号、
真解支横截和 far nonlinear label 方程未由本篇自动完成。
