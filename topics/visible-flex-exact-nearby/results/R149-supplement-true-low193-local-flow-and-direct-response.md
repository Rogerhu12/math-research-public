# R149 补充：真 low193 的局部流、有限横截与完整源响应

2026-11-28，visible-exact-astra-b0d5a16-20261128 / alternative_route。

**本篇已经证明新的直接认证方法及其转授公式。实际新 low193 枢轴尚未计算，
不能由本文或可执行入口声称低逆已经成立。** 新目标直接包围原真实变系数
$A_L^c$ 的流，再认证有限矩阵横截，不要求比较 Green 的缺陷范数小于 1。
原已完成的比较 HS 和 signed-loop 目标均不调用。

对象、坐标和原边界沿用
[R141](R141-low193-directed-green-and-complete-observation-certification.md)。
这仍是原 WVC hybrid：保留 full-family principal $\eta$、修复后 lower
coefficients、独立 mean、ordinary $dr$ 和真根 $r_*$；不是整个真实
$DF(Q_{\rm repair})$，也不由低逆推出完整 CFB、finite/high Schur、有限
$\rho$ 桥、原七输入端口或最终闭曲面。纯实现为
`scripts/fourfold_codazzi_true_low193_direct_flow_math.py`。

## 1. 固定对象与原完整数据

写原坐标为 $(u_1,\ldots,u_{96},v_0,v_1,\ldots,v_{96})$，$P=97,Q=96$。
边界算子为

$$
B_a x=(v_1,\ldots,v_{96})(r_*),\qquad
B_bx=((u_j+\tfrac{13}{80}v_j)_{j=1}^{96},v_0)(R),\quad R=25/8.
\tag{TF.1}
$$

观察空间是原
$L^2(dr;\mathbb R^{193})\oplus\mathbb R^{97}\oplus\mathbb R^{96}$，
观察为 $Sx$、根端 $(u_1,\ldots,u_{96},v_0)$ 和外端 $\Theta(v_1,\ldots,v_{96})$。
$S_i=\operatorname{diag}(I_{96},q_i,q_iI_{96})$、
$\Theta_j=(1+16j^2)^{-5/12}$ 都保持原值。

来源仍是完整 21 个历史 native、4650 个原 body rows、65 项 repair、155
个父区间及原 reference chain。新入口可读既有 1424 个 cuts、balance 和
reference charts 定义作为数值坐标；不重新执行旧 AL QR/SVD、旧比较 Green
目标、旧 HS 积分或旧 signed-loop trace。原 signed-loop run 45917913526/1
的完整 false gate 原样保留。其 false 仅表示旧充分门没有闭合。

每个新局部盒 $J$ 的矩阵 $\mathcal A_J$ 来自已有
`fourfold_codazzi_low_centre_child_coefficients.py` 的
`WholeChildSignedCoefficientProvider`：先对实际 child 与原闭 rows 的交集
组装所有 signed 系数，再 hull，并与原父包围相交。原独立 mean、内禀
误差球和 full-family $\eta$ 不按细分数缩小。内部 balance $D$ 仅是
局部计算的相似变换，最后完全共轭回 raw 坐标，不取代物理 $S$。

## 2. 变系数 Peano–Baker 包围

设 $A(r)\in\mathcal A$ 在整个长度为 $h\ge0$ 的真实盒上成立；$h$ 使用
完整正长度球。令区间矩阵 $G=h\mathcal A$，递推

$$
T_0=I,\qquad T_k=GT_{k-1}/k,\qquad
P_p^+=\sum_{k=0}^{p}T_k,\qquad P_p^-=\sum_{k=0}^{p}(-1)^kT_k.
\tag{TF.2}
$$

所有矩阵运算为 directed interval 运算。虽然不同时间的 $A$ 一般不交换，
每个有序 $k$ 重积都在区间乘积 $\mathcal A^k$ 内。其积分单纯形体积为
$h^k/k!$，区间矩阵是凸集，故相应 Peano–Baker 项在 $T_k$ 内。
逆向时间方程的系数为反序的 $-A$，其有序项同理在 $(-1)^kT_k$ 内。
**这里没有把普通矩阵指数 $\exp(h\mathcal A)$ 当作变系数流。**

取 $\beta\ge\|h\mathcal A\|_\infty$。若 $\beta<p+2$，则完整流尾项满足

$$
\epsilon_p=
\frac{\beta^{p+1}}{(p+1)!}\frac1{1-\beta/(p+2)}.
\tag{TF.3}
$$

在 $P_p^\pm$ 每一项加上 $[-\epsilon_p,\epsilon_p]$ 即包围完整正反流。
原因是尾项的 induced infinity norm 被 (TF.3) 控制，所以其每一 entry
均被同一数控制。计算中的 powers、阶乘、分母及 upper 全部有向舍入。
首版本取 $p=24$，每个原 refined cell 再分 4 个 exact 子盒；若新的真实
局部条件或有限枢轴失败，保存该真实失败位置，不把失败推成算子奇异。

还需整个子盒内任意前缀的流。对长度 $uh$、$0\le u\le1$，第 $k$ 项
在 $[0,1]T_k$ 内，尾项仍由 (TF.3) 包围。因此

$$
I+\sum_{k=1}^{p}[0,1]T_k+[-\epsilon_p,\epsilon_p],\quad
I+\sum_{k=1}^{p}(-1)^k[0,1]T_k+[-\epsilon_p,\epsilon_p]
\tag{TF.4}
$$

分别包围全部正向前缀及其逆。不额外计算一遍多项式 powers，也没有把
前缀置于中点。按真实顺序乘接后，(TF.2) 给整 cell transfer，(TF.4)
给整 cell 中每个子盒上的 $\Phi_i(r)$、$\Phi_i(r)^{-1}$。

若同时有完整 signed forcing $f(r)\in\mathcal F$，则相应 affine 增量的
前 $p+1$ 项为

$$
d^+=\sum_{k=0}^{p}\frac{T_kh\mathcal F}{k+1},\qquad
d^-=\sum_{k=0}^{p}\frac{(-1)^{k+1}T_kh\mathcal F}{k+1}.
\tag{TF.5}
$$

每个 entry 的尾项由
$\|h\mathcal F\|_\infty\beta^{p+1}/((p+2)!(1-\beta/(p+3)))$
控制。它要求整个盒上的函数包围，不要求径向导数；所有 forcing columns
一起保留。拼接时 $d_{J_2\circ J_1}=F_{J_2}d_{J_1}+d_{J_2}$。

## 3. 所有真实有限枢轴成立才授 BVP 逆

使用原 exact trial charts $T_i$；端点 first97/last96 仍分别张成
$\ker B_a$、$\ker B_b$。令实际 forward transfer 为 $\Phi_i$，设

$$
E_i=T_{i+1}^{-1}\Phi_iT_i,\qquad
\widetilde E_i=T_i^{-1}\Phi_i^{-1}T_{i+1}.
\tag{TF.6}
$$

依 $97+96$ 分块。从 $Z_0=0_{96\times97}$ 向外递推

$$
U_i=E_{11}+E_{12}Z_i,\qquad
Z_{i+1}=(E_{21}+E_{22}Z_i)U_i^{-1}.
\tag{TF.7}
$$

从 $Y_m=0_{97\times96}$ 向内递推

$$
V_i=\widetilde E_{21}Y_{i+1}+\widetilde E_{22},\qquad
Y_i=(\widetilde E_{11}Y_{i+1}+\widetilde E_{12})V_i^{-1}.
\tag{TF.8}
$$

**每一个** $U_i^{-1}$、$V_i^{-1}$ 必须由完整 directed finite matrix
inverse 成功包围。每个节点另外认证 $(I_{96}-Z_iY_i)^{-1}$，随后用原
block inverse 构造

$$
L_i=T_i\binom I{Z_i},\quad R_i=T_i\binom{Y_i}I,\qquad
(L_i,R_i)^{-1}=\binom{\ell_i}{\rho_i}.
\tag{TF.9}
$$

只有全部 $m$ 个 97 维、$m$ 个 96 维、$m+1$ 个横截 96 维枢轴成功，
函数才返回 `true_hybrid_BVP_verified=True`。浮点 trial chart、极小 residual
或某一个节点可逆都不能替代全流程。私有矩阵保存采用原逐 entry outward
guard 的 midpoint/radius packing；之后实际消费的是读回的完整球。

**命题。** 上述认证全部成功时，原混合边界问题
$x'-A_L^c x=f$、(TF.1) 齐次，在 $H^1$ 上对每个 $f\in L^2$ 唯一可解。

**证明。** (TF.7) 精确表示从根端齐次自由空间传播的 graph，(TF.8)
精确表示从外端向内传播的 graph。区间递推包含每个实际参数对应的图。
完整枢轴保证图始终有定义，(TF.9) 保证两个传播空间互补。任一点经真实
可逆 fundamental flow 后仍互补。将 variation of constants 分解到两空间，
得到下节的真实 Green，直接满足微分方程、跳跃恒等和两端齐次边界。
齐次解若同时满足两端条件，属于两个互补空间的交，故为零。系数分片有界、
区间有限，核分片有界，因此 $L^2$ 源给 $H^1$ 解。证毕。

这个证明只检查实际有限逆，不以 $\|\bar G\Delta\|$、HS upper 或
对称部范数是否小于 1 决定实际横截。

## 4. 真 Green 与全部原 source maps

记 $C_i=U_i^{-1},D_i=V_i^{-1}$，以及 cell 内真实前缀 $\Phi_i(r)$。
对 $r\in I_i,s\in I_j$，$r<s$ 时

$$
G(r,s)=-\Phi_i(r)L_i(C_i\cdots C_{j-1})\ell_j\Phi_j(s)^{-1};
\tag{TF.10}
$$

$r>s$ 时

$$
G(r,s)=\Phi_i(r)R_i(D_{i-1}\cdots D_j)\rho_j\Phi_j(s)^{-1}.
\tag{TF.11}
$$

同 cell 的积为空积。这是实际 $A_L^c$ 的核，不是原比较核。
保留四个完整源 $W$：$I_{193}$、$S^{-1}$、原
$(A_L^c-D_f)S^{-1}$，以及原完整 $193\times128$ high0 return。
最后一个仅是原 high0 return，未包含完整 finite/high CFB 消去。

在计算每个真实 cell 的新 transfer 时，同时用 (TF.4) 直接包围五个 raw
193 阶积分矩阵

$$
X_i=\int_{I_i}\Phi_i(r)^TS_i^2\Phi_i(r)\,dr,\qquad
J_i^W=\int_{I_i}\Phi_i(s)^{-1}W(s)W(s)^T\Phi_i(s)^{-T}\,ds.
\tag{TF.12}
$$

每个子盒取完整 interval integrand 乘其真实长度，再按盒相加。它是整域
包围，不是采点 quadrature。数学上的 $X_i,J_i^W$ 为 PSD；数值 interval
matrix 本身不被假设为某个单一 PSD matrix。后续 interval products 继续
包含这些真实、相互关联的积分矩阵。

设

$$
O_{L,i}=L_i^TX_iL_i,\ O_{R,i}=R_i^TX_iR_i,\quad
I_{L,i}^W=\ell_iJ_i^W\ell_i^T,\ I_{R,i}^W=\rho_iJ_i^W\rho_i^T.
\tag{TF.13}
$$

令 $A_0=0,B_0^W=0$，按原顺序递推

$$
A_{i+1}=C_i^T(A_i+O_{L,i})C_i,\qquad
B_{i+1}^W=D_i(B_i^W+I_{R,i}^W)D_i^T.
\tag{TF.14}
$$

不同 cell 的完整 squared kernel 积分严格由
$\operatorname{tr}(A_iI_{L,i}^W)+\operatorname{tr}(O_{R,i}B_i^W)$ 给出。
同 cell 的两个三角各自是非负 squared kernel 的积分，分别被该 branch
在完整 square 上的积分控制。因此

$$
\|SGW\|_{\rm HS}^2\le
\sum_i\left\{\operatorname{tr}((A_i+O_{L,i})I_{L,i}^W)
 +\operatorname{tr}(O_{R,i}(B_i^W+I_{R,i}^W))\right\}.
\tag{TF.15}
$$

这里只在同 cell 多计非负区域，未丢任何三角或 signed cross covariance。
所有 cross-cell 递推保完整 97/96 矩阵，不先替换为范数乘积。

根端 atoms 令 $A_0^a=(R_aL_0)^T(R_aL_0)$，
$A_{i+1}^a=C_i^TA_i^aC_i$；其完整 HS 平方为
$\sum_i\operatorname{tr}(A_i^aI_{L,i}^W)$。外端令
$O_b=(\Theta R_bR_m)^T(\Theta R_bR_m)$；其完整 HS 平方为
$\operatorname{tr}(O_bB_m^W)$。三个非负真实平方上界相加再开平方，便给
原 body-plus-193-atoms 范数。它没有对任意 $L^2$ 源求 endpoint value；
endpoint observations 只作用于解 $G W f\in H^1$。

对原二类算子
$H_L=\mathcal O G_{D_f}(A_L^c-D_f)S^{-1}\pi_B$，继续使用 R141 (G.31)：
$ (I-H_L)^{-1}h=h+\mathcal O G(A_L^c-D_f)S^{-1}h_B$。若新真实 correction
的 body、atoms 上界为 $b,a$，同一完整直和空间上的逆界为

$$
\|(I-H_L)^{-1}\|\le
\frac{\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2}}2.
\tag{TF.15a}
$$

首入口保存此界及四种源的 actual norm 字段。全部独立 193 个 atom 输入
仍有 identity；没有把 ordinary body 输入误当 body-plus-atoms 输入。

## 5. 原 signed RHS 与非齐次边界的直接响应

如果提供原完整 forcing 的每个局部盒包围，(TF.5) 得到
$x_{i+1}=\Phi_i x_i+d_i$。写 $x_i=L_ia_i+R_ib_i$，则

$$
a_i=C_i(a_{i+1}-\ell_{i+1}d_i),\qquad
b_{i+1}=D_ib_i+\rho_{i+1}d_i.
\tag{TF.16}
$$

边界 datum $g_a\in\mathbb R^{96},g_b\in\mathbb R^{97}$ 给
$b_0=(B_aR_0)^{-1}g_a$、$a_m=(B_bL_m)^{-1}g_b$；两方阵由同一横截
可逆，实施时仍验证其完整 directed inverse。先向内算 $a$，再向外算 $b$，
即得每个原节点的完整 signed response 和全部 193 atoms。需要整 cell
响应时用同一局部前缀及 affine 公式，不能把节点值当整段上界。

`solve_signed_response` 已实现 (TF.16)，但首个 actual gate 未提供或执行
任何原非线性 RHS。任意常数测试源、单独一列或 source-map norm 均不
冒充原完整 RHS。完整有限/high feedback 消去仍须将实际输入接入此逆，
不能在本篇中省去对应列、mean、边界项或反馈。

## 6. 首 actual 目标及失败账

独立首入口仅有两个有序新目标：原真实低193有限横截；同一真逆的四个
完整 source/193-atoms maps。实际 inverse gate 返回前不设置低逆标志；
若第二目标失败，第一目标的真实成功及完整枢轴账仍保存，不回滚数学状态。
每次 finite inverse 尝试先保存 phase/index/dimension；成功后登记该矩阵
逆范数的 directed 二进制幂 upper、完整连续索引和 hash chain，失败保存
正在尝试的实际矩阵摘要。原输入身份、原 false gates 和全未付条件保留。
大私有矩阵与可重建 moments 不入 git/Release。

局部 tail 或当前 left97 枢轴尚未成功时，可只将当前 cell 的子盒数从 4
逐次倍增至 64；已经成功的整个前缀和末 $Z$ 直接在同作业内复用，不重新
计算它们。全部 accepted cuts 逐 cell 记录。仍未成功时，完整失败矩阵与
必要末 $Z$ 写入该作业私有 checkpoint，公共只存完整矩阵维数、checkpoint
及 retained prefix 的 whole SHA、原始失败位置和完整小 receipt。
它不是耐久的大数组发布，也不声称退出 runner 后能恢复那些私有字节。

本篇提供的是能直接授予真实低逆的不同正向计算。是否通过、实际源范数多大，
必须以新 run 的完整实际输出为准；即使两个新目标都通过，也仍不是本课题
README 的精确闭曲面族完成标准。
