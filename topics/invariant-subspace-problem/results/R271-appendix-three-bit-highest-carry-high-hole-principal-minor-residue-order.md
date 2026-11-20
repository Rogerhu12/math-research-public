# R271 补录：真实三位 N 头最高 carry 极点的高孔主子式与改进残余阶


状态：**已证明，有限有理输入附精确可重建源码与实际运行。** 作者：Astra-ISP-b2a9acde-20261120 / r271_cost，与root；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。

## 0. 结论与核验源

对原三位 N 头，令低 carry 为 $s>0$、最高 carry 为 $t>0$，
加入任意固定偶数 $R=2k$ 个正权强位，固定 $S>0$，取纯三远孔代表。
本条证明最高 $t^{-1}$ 极点系数满足
$$
\boxed{q_{-1}(s)=O_{R,c,S}(s^{R/2-3})\qquad(s\to0^+).}
\tag{0.1}
$$
这估计的是最高极点系数，不是整个 MP 解或整个实际费用。
所有核、Galerkin、MP 及源均为完整物理对象。

有限维输入由可重建源
[verify-r271-three-bit-highest-carry-principal-minors.mjs](../scripts/verify-r271-three-bit-highest-carry-principal-minors.mjs)
核验，参数为
$$
r=3,\quad b_0=1,\ b_1=1/4,\ b_2=1/9,\quad
l\in\{1,3,5,7,9\},\quad \bar C=36C,\ \bar V=36V.
$$
脚本先用有限域选候选，再以 BigInt 整数/有理运算重建并逐项认证；
有限域结果不承担正确性。
依根规则，不把消元数组、证书向量表或 determinant 结果表另存为产物。
运行 ID 与源 SHA 见下述原实际运行。

**实际精确运行。** [Actions run44724947207](https://github.com/Rogerhu12/math-research-public/actions/runs/44724947207)，job136249870826，在冻结提交 a945aec4331160c285f6187b0cecb3bc2e92db39 上以 Node 24.22.2 无参数执行本源。五个短链的完整整数核方程、支撑/系数门、主子式非零及理论全新增秩检查全部通过；纯重建用时0.032998534秒。根已取得原job日志，核对源码SHA-256 2413523513b60f8296990491b759e3721cac3ed9925150ef273f33f803359c42。完整重建内容的合并SHA-256为8e351cbeb79369058872f1a42e91dcb06ffa52e48293c27e9c98c7306da09446；本源有界输出SHA-256为b33b2ae3a473ae1bdffbb857d457c7a2f4558d6b3b55e889eef46625f16c4469，完整decoded job-log SHA-256为993d4afe61b0f8da2e665d1fa783be4b97e854cb34c94dab7fe0749c3c280aab。[运行身份与输入参数](../notes/2026-11-20-exact-source-run44724947207-b2a9.json)仅保脚本/参数/run/SHA，不保存计算证书、矩阵或日志正文。


对原强权 $c_i=b_i$、$i=3,\ldots,3+R-1$，本条还给出对全部
$0<s\le1$ 的明确源不等式
$$
\boxed{
\|q_{-1}(s)\|
\le10^{100}\,4^R(3+R/2)^{16}\,
s^{R/2-3}\,\mathcal Z_R(s),
}
\tag{0.2}
$$
其中 $\mathcal Z_R(s)$ 是 §7 定义的真实完整高孔加权残差。
固定参数下它在零点有界；本条没有把这项有界性变成原移动参数的统一常数。

## 1. 原两级 carry 与完整源

记
$$
A_s=
\begin{pmatrix}
0&1&1/4&0\\
0&0&s&1/4\\
0&0&0&1\\
0&0&0&0
\end{pmatrix},
$$
$$
V_s=\tfrac14|e_2\rangle\langle e_0|
+s|e_3\rangle\langle e_0|
+\tfrac14|e_3\rangle\langle e_1|,
$$
$$
A_3(s,t)=
\begin{pmatrix}A_s&(1/9)I_4+tV_s\\0&A_s\end{pmatrix}.
\tag{1.1}
$$
原参数为 $s=e^{-1070},t=e^{-17960}$，但以下先把两者作为独立参数。
加入完整强尾
$$
D_R=\sum_{\ell=1}^R c_\ell E_\ell,\qquad c_\ell>0,
\quad C(s,t)=A_3(s,t)+D_R.
$$
令
$$
X(s,t)=C(s,t)^3=X_0(s)+tX_1(s),
$$
$$
H(s,t)=I+\frac{C(s,t)^*C(s,t)}S+
\frac{(C(s,t)^*)^2C(s,t)^2}{2S^2}.
$$
对原物理一孔源 $f_1$，定义完整
$$
F(s,t)=\ker X(s,t),\qquad
a(s,t)=(P_FH(s,t)|_F)^{-1}P_Ff_1,
$$
$$
\xi(s,t)=f_1-H(s,t)a(s,t),\qquad
q(s,t)=(X(s,t)^*)^\dagger\xi(s,t).
\tag{1.2}
$$

固定 $s>0$。旧四维头为单 Jordan 链，$R$ 偶，故
$A_s+D_R$ 的全部链长为偶。
已证奇高度最高 carry 剪切定理适用，给
$\|(X(s,t)^*)^\dagger\|=O_{s,R}(t^{-1})$，并开齐全部一阶新增秩。
因此
$$
F_0(s)=\lim_{t\to0}F(s,t),\qquad
a_0(s)=\lim_{t\to0}a(s,t),\qquad
\xi_0(s)=f_1-H(s,0)a_0(s)
$$
均有意义，且
$$
q_{-1}(s)=\lim_{t\to0}tq(s,t).
\tag{1.3}
$$
$a_0(s)$ 在完整 $F_0(s)$ 上解 Galerkin，不是退化较大核上的替代源。

## 2. 真实极点方程与最小范数域

记
$$
K(s)=\ker X_0(s),\quad Z(s)=\ker X_0(s)^*,\quad
\mathcal E(s)=P_{Z(s)}X_1(s)|_{K(s)}.
$$
完整一阶开秩给
$$
F_0(s)=\ker\mathcal E(s),\qquad
E(s)=\operatorname{Ran}\mathcal E(s).
$$
真实极点由
$$
q_{-1}(s)\in E(s),\qquad
\mathcal E(s)^*q_{-1}(s)=P_{K(s)}\xi_0(s)
\tag{2.1}
$$
唯一确定。
等价地，它是在整个 $Z(s)$ 中满足
$$
\langle X_1(s)v,q\rangle=\langle v,\xi_0(s)\rangle
\quad\text{对全部 }v\in K(s)
\tag{2.2}
$$
的最小物理范数解。
因为 $\mathcal E(s)^*$ 在 $Z(s)$ 上的核为
$Z(s)\ominus E(s)$，该最小性直接来自正交分解。

后面的候选解不必等于 $q_{-1}$ 或属于 $E(s)$；
只要它在完整 $Z(s)$ 中满足所有 (2.2)，就有
$\|q_{-1}\|\le\|q_{\rm candidate}\|$。
这里没有用某个低源压缩的最小性替换真实 MP 的最小性。

## 3. 非正交强尾分解及翻转孔级的自伴形式

通过固定有界可逆的、保持尾孔级的相似，把完整强尾分解为 Jordan 链。
每条链具有 primitive 起始孔数 $j$，长度
$$
l=R-2j+1.
$$
它的局部级 $v=0,\ldots,l-1$ 对应物理尾孔数 $j+v$。
由于 $R$ 偶，全部 $l$ 为奇数。

在 $l\ge11$ 的链上，最高 $t$ 退化的三次幂秩不变。
事实上，$t>0$ 时八维头型为 $J_8$，$t=0,s>0$ 时头型为
$J_5\oplus J_3$；当 $l\ge11$ 时，所有张量和链的长度均至少为 $3$，
两边三次幂的秩都为 $8l-24$。
因此只有 $l=1,3,5,7,9$ 需要新增极点约束。

把这些短链化为单位 $J_l$，在其余链上可保留标准等权 sl2 链。
令完整相似为 $\mathcal S$，其范数和逆范数都是实际成本。
每个局部块选择逆序矩阵 $J_{\rm rev}$，同时翻转八维头与局部尾链。
定义
$$
\mathfrak J
=\mathcal S^{-*}\left(\bigoplus J_{\rm rev}\right)\mathcal S^{-1}.
\tag{3.1}
$$
这是原物理空间上的固定自伴可逆算子，一般不是等距算子。
由局部矩阵的 palindromic 身份，
$$
\mathfrak J C(s,t)=C(s,t)^*\mathfrak J,\qquad
\mathfrak J X_i(s)=X_i(s)^*\mathfrak J.
\tag{3.2}
$$
所以 $\mathfrak J K(s)=Z(s)$。

设总物理孔数为 $N=R+3$。
一条链中局部总级上界为 $l+2$，而
$2j+l+2=R+3=N$。
保持级的相似与其逆伴随均保留这个对应，
所以
$$
\mathfrak J\mathcal H_g\subset\mathcal H_{N-g}.
\tag{3.3}
$$
(3.3) 不需要任何非正交分块在物理内积中相互正交。

厄米型
$
B_s(u,v)=\langle u,\mathfrak J X_1(s)v\rangle
\quad(u,v\in K(s))
\tag{3.4}
$$
在原复内积下为厄米型（所用实基中的矩阵对称），其根空间正是 $F_0(s)$。
这是因为 $\mathfrak J K(s)=Z(s)$，所以 (3.4) 为零的条件恰是
$P_{Z(s)}X_1(s)v=0$。

## 4. 五条短链的可重建有限引理

在一条短链上取 $s=1,t=0$，令
$$
C_l=A_3(1,0)\otimes I_l+I_8\otimes J_l,\qquad
V_l=(\partial_tA_3(1,t))\otimes I_l.
$$
令
$$
\bar X_{0,l}=(36C_l)^3,
$$
$$
\bar X_{1,l}
=(36C_l)^2(36V_l)
+(36C_l)(36V_l)(36C_l)
+(36V_l)(36C_l)^2.
\tag{4.1}
$$
这些是整数矩阵。
按 $u_{hl+v}=e_h\otimes e_v$ 编号，局部物理孔级为
$\operatorname{popcount}(h)+v$，逆序矩阵把 $u_a$ 送到 $u_{8l-1-a}$。

用链长公式定义理论新增秩
$$
\rho_l=
\operatorname{rank}(J_8+J_l)^3
-\operatorname{rank}(J_5+J_l)^3
-\operatorname{rank}(J_3+J_l)^3,
\tag{4.2}
$$
其中
$$
\operatorname{rank}(J_a+J_l)^3
=\sum_{j=0}^{\min(a,l)-1}\max(a+l-1-2j-3,0).
$$
没有把数值消元输出当成这个理论上界。

### 有限引理 4.1

对 $l\in\{1,3,5,7,9\}$，重建源构造整数列矩阵 $Y_l$，满足
$$
\bar X_{0,l}Y_l=0,\qquad
\operatorname{supp}Y_l\subset
\{\text{局部孔级}\ge(l+1)/2\},
\tag{4.3}
$$
$$
\#\operatorname{cols}Y_l=\rho_l,\qquad
\det(Y_l^*J_{\rm rev}\bar X_{1,l}Y_l)\ne0.
\tag{4.4}
$$
每列至多 $12$ 个非零整数，绝对值至多 $128$，且 $\rho_l\le7$。

**核验方法。** 重建源先限制到 (4.3) 的高孔列。
有限域行消元只选择一组候选核列和对称 principal minor。
随后从原整数矩阵重新做 fraction-free Bareiss 消元及精确有理回代，
把每个核列约分为 primitive 整数列，并逐坐标核对
$\bar X_0Y=0$、支撑及系数界。
最后对完整整数 $Y^*J_{\rm rev}\bar X_1Y$ 精确求 determinant 并断言非零。
新增列数同时与 (4.2) 的理论秩差比较。
任何选候选的误差都会被这些整数/有理断言拒绝。
源不输出或保存证书数组；只输出成功断言与重建哈希。

由 (4.2)、完整一阶开秩及 (4.4)，这些列在全部新约束上已满秩，
并非只打开新增秩的一个子集。

## 5. 全强尾高孔补空间

在每一条短尾链中嵌入有限引理的 $Y_l$，串接得到完整列矩阵 $Y\subset K(1)$。
长链没有新增约束，不需要列。
由于物理起始孔数 $j=(R-l+1)/2$，每一列的最低物理孔级 $a_i$ 满足
$$
a_i\ge j+(l+1)/2=R/2+1=k+1.
\tag{5.1}
$$
令
$$
B_1=Y^*\mathfrak J X_1(1)Y.
$$
在所选链坐标中，它是有限引理的非奇异块的直和；
其中每块只是整数证书型除以 $36^3$。
因此 $B_1$ 可逆，且
$$
K(1)=F_0(1)\dotplus\operatorname{Ran}Y.
\tag{5.2}
$$
(5.2) 是代数直和，不声称物理正交。

所有局部块的列数与矩阵大小有统一上界，故
$\|Y_{\rm local}(s)\|$ 与 $\|B_1^{-1}\|$ 的局部常数不乘 primitive 的数量。
完整直和的算子范数取各块上确界，不能额外引入一个未说明的
$\sqrt{2^R}$ 或把它隐藏在常数里。

## 6. 完整真核框架给出的源孔传播

按总物理孔级定义
$\mathcal R_s|_{\mathcal H_g}=s^gI$。
原两级 N 族具有精确齐次性
$$
C(s,t)=s\mathcal R_s C(1,t/s)\mathcal R_s^{-1},
$$
所以
$$
K(s)=\mathcal R_sK(1),\qquad
F_0(s)=\mathcal R_sF_0(1),\qquad
X_1(s)=s^2\mathcal R_sX_1(1)\mathcal R_s^{-1}.
\tag{6.1}
$$

按 $F_0(1)$ 的最低孔级过滤选适配基，列除以各自最低 $s$ 次数，
得到在零点仍满列秩的多项式真核框架 $Z(s)$。
它的 $s^a$ 系数将列初始孔级 $g$ 送入物理级 $g+a$。
注意
$\operatorname{Ran}Z(0)=\lim_sF_0(s)$，
不需要等于更大的实际 $\ker X(0,0)$。

完整物理 Gram 矩阵
$Z(s)^*H(s,0)Z(s)$ 在零点严格正定。
又 $H(s,0)$ 的 $s^b$ 系数只改变孔级至多 $b$，
因为 $C(s,0)$ 的 $s^a$ 系数改变孔级 $a-1$。
逐阶解完整 Gram 方程，因此
$$
a_0(s)=\sum_{\nu\ge0}s^\nu a_\nu,\qquad
\xi_0(s)=\sum_{\nu\ge0}s^\nu\xi_\nu,\qquad
a_\nu,\xi_\nu\in\bigoplus_{g\le1+\nu}\mathcal H_g.
\tag{6.2}
$$
所有强尾混链项都留在这个物理 Gram 方程内。
特别地，对 $g\ge1$，
$$
P_g\xi_0(s)=O(s^{g-1}).
\tag{6.3}
$$

定义
$$
Y_i(s)=s^{-a_i}\mathcal R_sY_i.
$$
这些列在 $s=0$ 有界、对 $s>0$ 在 $K(s)$ 中。
由 (3.3)，
$\mathcal R_s\mathfrak J\mathcal R_s=s^N\mathfrak J$，从而
$$
B(s)_{ij}
=Y_i(s)^*\mathfrak J X_1(s)Y_j(s)
=s^{N+2-a_i-a_j}(B_1)_{ij}.
\tag{6.4}
$$
这是准确的单项式权恒等式。

## 7. 完整极点候选解及改进阶

令
$$
r_i(s)=\langle Y_i(s),\xi_0(s)\rangle,\qquad
u(s)=B(s)^{-1}r(s),
$$
$$
\widetilde q(s)=\mathfrak J Y(s)u(s).
\tag{7.1}
$$
它属于完整 $Z(s)$。
(6.4) 使其在所有 $Y_i(s)$ 上满足极点方程；
而 $\xi_0(s)\perp F_0(s)$、$F_0(s)$ 是型 (3.4) 的根空间，
所以由 (5.2) 它满足全部 $K(s)$ 上的 (2.2)。
于是
$$
\|q_{-1}(s)\|\le\|\widetilde q(s)\|.
\tag{7.2}
$$

由 (6.3)，$r_i(s)=O(s^{a_i-1})$。
(6.4) 给
$$
u_i(s)=\sum_j
s^{a_i+a_j-N-2}(B_1^{-1})_{ij}r_j(s).
$$
使用全部 $a_i,a_j\ge k+1$ 与 $N=2k+3$，
$$
u_i(s)=O(s^{k-3}).
$$
$Y_i(s)$ 在零点有界，$\mathfrak J$ 为固定有界算子，
所以 (7.2) 证明 (0.1)。

### 7.1 显式保留所有强段项的源界

现在取原强权 $c_i=b_i$，$i=3,\ldots,3+R-1$，令
$$
y=3+R/2,\qquad
\mathcal Z_R(s)=
\left\|\sum_{g\ge k+1}s^{1-g}P_g\xi_0(s)\right\|.
\tag{7.3}
$$
它是实际完整源的加权物理范数。
由 (6.3)，每个固定 $R,S$ 下 $\mathcal Z_R(s)=O(1)$。

中位尺度归一化给强尾对角条件数至多 $4^R$，公共尺度 $c=y^{-2}$。
标准 unitary sl2 分解后，只在 $l\le9$ 的短链上继续把 $cL_l$
化成单位 $J_l$。这个对角转换的条件数不超过
$c^{-(l-1)}/(l-1)!\le y^{16}$。
长链保持 $cL_l$ 即可；它们的逆序矩阵也满足所需自伴翻转身份。
因此可选
$$
\kappa(\mathcal S)\le4^R y^{16}.
\tag{7.4}
$$

令 $\widehat r_i=s^{1-a_i}r_i$。
每列 $Y_i(s)$ 的第 $g$ 级带因子 $s^{g-a_i}$，所以
$$
\widehat r_i
=\sum_{g\ge a_i}s^{2(g-a_i)}
\langle P_gY_i,\ s^{1-g}P_g\xi_0(s)\rangle.
$$
由于 $0<s\le1$，这些附加因子不增大局部列矩阵的 Frobenius 上界。
若统一局部上界为 $C_Y$，则
$$
\|\widehat r\|
\le\|\mathcal S\|C_Y\mathcal Z_R(s).
$$
同时 (6.4) 可准确写成
$$
u=s^{k-3}
\operatorname{diag}(s^{a_i-k-1})\,
B_1^{-1}\,
\operatorname{diag}(s^{2(a_j-k-1)})\,\widehat r.
$$
两侧对角矩阵范数均至多 $1$，并且
$$
\|\mathfrak JY(s)\|\le\|\mathcal S^{-1}\|C_Y.
$$
因此对全部 $0<s\le1$ 有
$$
\|q_{-1}(s)\|
\le\kappa(\mathcal S)C_Y^2\|B_1^{-1}\|
s^{k-3}\mathcal Z_R(s).
\tag{7.5}
$$

有限核验给每列至多 $12$ 项、系数绝对值至多 $128$、每块至多 $7$ 列，
故可取 $C_Y^2\le7\cdot12\cdot128^2<1.4\cdot10^6$。
又 $\|36C_l\|<108,\ \|36V_l\|\le54$，
所以 $\|\bar X_{1,l}\|<2\cdot10^6$，
证书型每个整数元素绝对值小于 $10^{13}$。
非零整数 determinant 绝对值至少为 $1$，
用至多六阶余子式展开及 $36^3$ 的还原因子，可粗取
$$
C_Y^2\|B_1^{-1}\|<10^{100}.
$$
这不需要保存或引用任何消元输出表。
与 (7.4)–(7.5) 合并即得 (0.2)；
全部显式 $R$ 项都在 $4^R y^{16}s^{R/2-3}$ 中，
剩余未知量就是清楚命名的原源 $\mathcal Z_R(s)$。

## 8. 保留的实际边界

- (0.1) 比全局 pole operator 范数给出的较粗阶数更好；
  原因是使用完整 Schur 型的高孔非奇异主子式，
  而不是把最坏逆范数乘到整个残差上。
- 对任意固定正强权，结论为固定 $R,c,S$ 的渐近。
  (0.2) 对原强权和任意 $0<s\le1$ 成立，但没有上界化
  原实际 $\mathcal Z_R(e^{-1070})$。
- 没有证明原 $s=e^{-1070}$ 已进入某个随 $R$ 统一的渐近有效区，
  也没有把最高 $t$ 极点项的估计当成整个 $q(s,t)$ 的估计。
- 本条只处理三位 N 头的两个 carry。
  一般原 $A_m$ 的逐 carry 分级、移动 $m,R,r$ 的完整源费用仍未闭。
  普通 Hilbert ISP 仍未完成。
