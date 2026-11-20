# R271 补录：一般真实 N 头的高孔 Schur 补空间、完整最高极点阶与全部强段常数

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost、root；AI-assisted GPT-6 Astra Pro。

状态：**以下完整最高极点界与明确原强段常数已证明；实际源界仍开放。**

## 0. 范围与所用父结论

本条沿用以下已证结果：

- 完整奇高度最高 carry 简单极点及物理剪切：
  [R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)；
- 完整 Galerkin 极点方程与最小物理范数：
  [R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md](R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md)；
- 原孔分级、真核过滤框架及完整 Galerkin 传播：
  [R271-appendix-high-primitive-support-and-uniform-low-carry-residue-order.md](R271-appendix-high-primitive-support-and-uniform-low-carry-residue-order.md)；
- 强尾中位归一化：
  [R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md](R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md)；
- 一般长坏链的解析 Schur 合同：
  [R271-appendix-general-head-long-bad-chain-analytic-schur-and-three-true-power-flags.md](R271-appendix-general-head-long-bad-chain-analytic-schur-and-three-true-power-flags.md)。

本条不把 primitive 代数分块当作物理正交 Galerkin 分块。
所有源都是完整真核 Galerkin 的原源；所构造的候选只用来上界完整最小范数极点。
结论针对固定三孔高度，N 型；没有把三位头的半高孔主子式直接推广给一般头。
普通 Hilbert ISP、实际完整费用与移动参数源上界仍未闭。

## 1. 原双参数族与完整物理源

取
$$
m\ge5,\qquad n=2^{m-1},\qquad d=2n,\qquad
R\ge d\ \text{为偶数},\qquad N=m+R.
$$
固定正的旧基准权 $\bar d_i$ 与 $d_0=\bar d_0$，置
$$
d_i(s)=s^{2^i-1}\bar d_i\quad(0\le i\le m-2),\qquad
d_{m-1}(s,t)=t\,d_{m-2}(s)^2.
\tag{1.1}
$$
这正是把全部旧相邻 carry 同乘 $s$，最高相邻 carry 单独取 $t$。

令 $H_m(s,t)$ 为原 N 型真实有限头，包含全部旧 carry。
加入原 $R$ 个强位
$$
D_R=\sum_{i=m}^{m+R-1}b_iE_i,\qquad b_i=(i+1)^{-2},
$$
并记
$$
C(s,t)=H_m(s,t)+D_R,\qquad
X(s,t)=C(s,t)^3=X_0(s)+tX_1(s),
$$
$$
H(s,t)=I+\frac{C(s,t)^*C(s,t)}S
+\frac{(C(s,t)^*)^2C(s,t)^2}{2S^2},\qquad S>0.
\tag{1.2}
$$
固定原一孔源 $f=f_1$。
令
$$
K(s)=\ker X_0(s),\qquad
F_0(s)=\lim_{t\downarrow0}\ker X(s,t),
$$
$$
a_0(s)=
(P_{F_0(s)}H(s,0)|_{F_0(s)})^{-1}P_{F_0(s)}f,
\qquad
\xi_0(s)=f-H(s,0)a_0(s).
\tag{1.3}
$$
$H\ge I$ 保证这个完整物理方程唯一可解。
最高 $t$ 极点系数为
$$
q_{-1}(s)=\lim_{t\downarrow0}tq(s,t).
\tag{1.4}
$$
它是以下完整方程的最小物理范数解：
$$
q\in\ker X_0(s)^*,\qquad
P_{K(s)}X_1(s)^*q=P_{K(s)}\xi_0(s).
\tag{1.5}
$$
特别是 $\xi_0(s)\perp F_0(s)$；不能用一部分核列替代这个兼容性。

记物理总孔级投影为 $P_g$，
$$
\mathcal R_s=\sum_{g=0}^N s^gP_g.
$$
真实 N 权给
$$
C(s,0)=s\mathcal R_sC(1,0)\mathcal R_s^{-1},\qquad
X_1(s)=s^2\mathcal R_sX_1(1)\mathcal R_s^{-1},
\tag{1.6}
$$
以及
$$
K(s)=\mathcal R_sK(1),\qquad
F_0(s)=\mathcal R_sF_0(1).
\tag{1.7}
$$

## 2. 完整强尾坐标与真正的坏链

原强尾作保持孔级的相似变换，分解为完整 Boolean primitive 链。
每条链的 primitive 起始级 $j$ 与奇链长 $l$ 满足
$$
l=R-2j+1.
\tag{2.1}
$$
在标准直和坐标中，该链的总物理孔为
$$
\operatorname{popcount}(\text{头坐标})+j+\text{尾链级}.
$$
最高头在 $t\ne0$ 为单 $d$ 链，在 $t=0$ 为 $(n+1,n-1)$ 两链。
当 $l\ge d+3$，所有相加后的链长至少为 $3$，三次幂核不损失，
所以最高 Schur 型为零。

只有奇 $l\le d+1$ 是坏链。
将这些坏链的尾算子化为单位 $J_l$；好链可以保留标准 $cL_l$，
不需要为它们支付单位链成本。

在完整标准直和中，令
$$
\mathcal J=\bigoplus_l(\mathcal J_d\otimes\mathcal J_l)
$$
（包括全部 primitive 重数），其中 $\mathcal J_h$ 为逆序翻转。
这是单位自伴 involution，
$$
\mathcal JC(s,0)=C(s,0)^*\mathcal J,\qquad
\mathcal JP_g=P_{N-g}\mathcal J.
\tag{2.2}
$$
标准直和中的完整 Schur 自伴型是
$$
B=P_{K(1)}\mathcal JX_1(1)|_{K(1)}.
\tag{2.3}
$$
其根空间恰为 $F_0(1)$，因为奇高度的全部新增秩一阶打开。
所以非退化补空间是完整 $K/F_0$ 的补空间。

## 3. 高孔补空间定理

置
$$
\boxed{A_0=\frac{R-d}{2}+m+2.}
\tag{3.1}
$$

### 定理 3.1

标准直和中存在 $Y:\mathbb C^k\to K(1)$，满足：

1. $K(1)=F_0(1)\dotplus\operatorname{Ran}Y$；
2. $B_Y=Y^*\mathcal JX_1(1)Y$ 可逆；
3. 每列 $Y$ 都支撑在物理总孔级至少 $A_0$；
4. $Y$ 按完整 primitive 链直和构造，包含所有新增约束。

**证明。**

### 3.1 短坏链

若 $l\le n+1$，则由 (2.1)
$$
j\ge\frac{R-n}{2}.
$$
而 $m\ge5$ 时
$$
n/2=2^{m-2}\ge m+2.
$$
因此
$$
j\ge\frac R2-n+m+2=A_0.
\tag{3.2}
$$
这整条链中的任意向量都已经支撑在级 $A_0$ 以上。
在该完整局部核内，取自伴型 (2.3) 的根空间正交补的任意正交基即可。
它给非退化补空间，不需要枚举或登记消元向量表。

### 3.2 长坏链的三个真实幂旗

现在 $n+3\le l\le d+1$。记
$$
h=\frac{d-l+1}{2}\ge0,\qquad q=l-n.
$$
沿用长链解析定理的完整核参数化
$$
\Phi_p(u)=\sum_{a=0}^{n}(-1)^a
\binom{p+a-1}{a}H_m(1,0)^au\otimes e_{p-1+a},
\quad p=1,2,3.
\tag{3.3}
$$
这里 $\Phi=(\Phi_1,\Phi_2,\Phi_3)$ 参数化整个 $\ker C(1,0)^3$。

最高位为 $0$ 的参数在 Schur 根空间中。
最高位为 $1$ 的三个旧头参数，经精确三角合同，型为
$$
\frac2{l(l+1)}GA^{q+2}
\ \oplus\
\left(-\frac{l+1}{l-1}\right)GA^q
\ \oplus\
\frac{l(l-1)}2GA^{q-2},
\tag{3.4}
$$
其中 $A=H_{m-1}(1)$、$G=\mathcal J_n\rho g(B)^n$。
这仍是原真实 $A$ 的幂，不是单位 Jordan 头。

令
$$
e_p=q+4-2p\quad(p=1,2,3).
$$
$GA^{e_p}$ 自伴，真核为前 $e_p$ 个旧坐标；
因而它在后面的真实坐标旗
$$
\operatorname{span}(e_{e_p},\ldots,e_{n-1})
\tag{3.5}
$$
上非退化；当 $e_p\ge n$ 时该块为空。

把 (3.5) 中一个坐标写成新最高位占据的
$$
e_{d-1-z},\qquad
0\le z\le n-1-e_p=2\bigl(h-(3-p)\bigr).
\tag{3.6}
$$
对任意整数 $u\ge0$，若 $z\le2u$，则
$$
\operatorname{popcount}(z)\le u.
\tag{3.7}
$$
因为含 $u+1$ 个 $1$ 的最小整数为
$2^{u+1}-1>2u$。
故 (3.6) 中的头孔数至少为
$$
m-h+(3-p).
\tag{3.8}
$$

合同逆变换为
$$
u_1=w_1,\qquad
u_2=w_2+\frac2{l+1}Aw_1,
$$
$$
u_3=w_3+\frac2{l-1}Aw_2+
\frac2{l(l+1)}A^2w_1.
\tag{3.9}
$$
每次额外作用 $A^a$，参数编号也恰增加 $a$。
原 N 型的一步最多删去一个物理孔，因此这两种变化不降低
“头孔加参数编号减一”。

再代入 (3.3)，其第 $a$ 项头孔至多减少 $a$，尾级增加 $a$。
由 (3.8)，所有这些列的最低局部总孔至少为
$$
m-h+(3-p)+(p-1)=m+2-h.
\tag{3.10}
$$
加入 primitive 起始级 $j$，并用
$$
j-h=(R-d)/2,
$$
即得最低总孔恰至少 $A_0$。

(3.5) 的每个限制均非退化，(3.9) 可逆；
故这些列给整个长链 Schur 型的非退化补空间。
将全部短、长坏链直和，好链全部置于根空间，即得所需 $Y$。
证毕。

这里 $m\ge5$ 用于 (3.2)。
本条没有未经检验地覆盖 $m=4$；三位头的更强专门证书属于另一条结论。

## 4. 完整源的解析性与孔传播

由 (1.7)，对固定 $m,R,\bar d_i,S$，
$F_0(s)=\mathcal R_sF_0(1)$。
按最低孔过滤选择适配基，将每个最低级为 $a$ 的列除以 $s^a$，
得到在 $s=0$ 满列秩的多项式框架 $Z(s)$。
它参数化的是真核极限，不是 $s=0$ 处可能更大的退化核。

完整物理方程是
$$
a_0(s)=Z(s)v(s),\qquad
Z(s)^*H(s,0)Z(s)v(s)=Z(s)^*f.
\tag{4.1}
$$
零点 Gram 矩阵严格正定，故 $a_0(s)$ 在零点解析。
由 (1.6)，$H(s,0)$ 的 $s^\nu$ 系数只连接相差至多 $\nu$ 的孔级。
逐阶解 (4.1)，得到
$$
a_0(s)=\sum_{\nu\ge0}s^\nu a_\nu,\qquad
a_\nu\in\bigoplus_{g\le1+\nu}\mathcal H_g.
$$
同一性质传给完整残余：
$$
\boxed{
\xi_0(s)=\sum_{\nu\ge0}s^\nu\xi_\nu,\qquad
\xi_\nu\in\bigoplus_{g\le1+\nu}\mathcal H_g.
}
\tag{4.2}
$$
全体 primitive 链之间的物理 Gram 混合都保留在 (4.1) 中。

定义实际加权源
$$
\boxed{
\mathcal Z_{m,R}(s)=
\left\|\sum_{g\ge A_0}s^{1-g}P_g\xi_0(s)\right\|.
}
\tag{4.3}
$$
对固定全部参数，(4.2) 保证它在 $s\downarrow0$ 有界。
这个固定参数事实没有给出它在原 $s=e^{-1070}$、移动 $m,R$ 下的数值上界。

## 5. 一个完整候选解与严格消失阶

先在标准直和中工作，源记为 $\xi$。
令 $Y$ 如定理 3.1。对 $s>0$，
$\mathcal R_sY$ 仍为 $K(s)/F_0(s)$ 的补空间。
由翻级 (2.2) 和齐次性 (1.6)，
$$
(\mathcal R_sY)^*\mathcal JX_1(s)(\mathcal R_sY)
=s^{N+2}B_Y.
\tag{5.1}
$$
因此
$$
\widetilde q(s)=
s^{-N-2}\mathcal J\mathcal R_sY
B_Y^{-1}Y^*\mathcal R_s\xi
\tag{5.2}
$$
在 $\ker X_0(s)^*$ 中。
它在 $\mathcal R_sY$ 的全部方程上满足 (1.5)；
在根空间 $F_0(s)$ 上，左右两边均为零，
所以它满足整个 $K(s)$ 的方程。
真实 $q_{-1}$ 的最小物理范数性允许用这个完整候选上界。

由于 $Y$ 支撑在级 $A_0$ 以上，对 $0<s\le1$，
$$
\|\mathcal R_sY\|\le s^{A_0}\|Y\|.
$$
若 $z=\sum_{g\ge A_0}s^{1-g}P_g\xi$，则
$$
\|Y^*\mathcal R_s\xi\|
=\left\|Y^*\sum_{g\ge A_0}s^{2g-1}P_gz\right\|
\le s^{2A_0-1}\|Y\|\|z\|.
$$
故 (5.2) 给
$$
\|\widetilde q(s)\|
\le \|Y\|^2\|B_Y^{-1}\|
s^{3A_0-N-3}\|z\|.
\tag{5.3}
$$
指数恰为
$$
\boxed{
3A_0-N-3=\frac{R-3d}{2}+2m+3.
}
\tag{5.4}
$$

结合 (4.2)，得到固定参数定理
$$
\boxed{
q_{-1}(s)=
O_{m,R,\bar d,S}
\!\left(s^{(R-3d)/2+2m+3}\right).
}
\tag{5.5}
$$
它估计的是实际最高 $t^{-1}$ 极点系数，而非整个 $q(s,t)$。
一般 $R=d$ 时指数为 $-d+2m+3$，不能据此声称费用变小。
$R\ge3d$ 后才出现这里保证的正阶。

## 6. 有限头常数与全体 primitive 重数

这里给出不隐藏 $R$ 的费用。
先假设基准头满足已证的真实头界
$$
\|A\|<6,\qquad
\kappa(V_{\rm old})\le e^{221a},\qquad
\kappa(\widehat V)\le e^{441a},
\qquad a=16^{m-2}.
\tag{6.1}
$$
$\widehat V$ 是删除最高 Boolean 项、最高参考 carry 取 $1$ 的真实参考头相似。
一般固定基准也可用其实际有限相似条件数代替 (6.1)，以下构造不变。

### 6.1 短坏链

在单位 $J_l$、奇 $l\le n+1$ 上，
$$
D=A+J_l.
$$
标准 sl2 链变换付
$(n-1)!(l-1)!$，其三次幂非零奇值至少为 $3!=6$，所以
$$
\|(D^3)^\dagger\|
\le e^{221a}(n-1)!(l-1)!/6.
$$
又 $\|D^2\|<49$。
最高 carry 剪切因子
$(1+3b\|D^2\|\|(D^3)^\dagger\|)^2$
以及参考三次幂逆共同给
$$
\limsup_{t\downarrow0}t\|X_t^\dagger\|
\le110 e^{883a}((n-1)!)^2(d-1)!((l-1)!)^3,
\tag{6.2}
$$
其中 $b=b_{m-1}<1$，
$(1+49/2)^2/6<110$。

标准正交 Schur 分块说明：
局部完整自伴 Schur 型的 MP 范数不超过 (6.2)。
也可由一阶打开的奇值
$t\sigma_j(E_1)+O(t^2)$ 直接得出。
按 §3.1 取正交非根基，因此
$$
\|Y_l\|^2\|(B_{Y_l})^{-1}\|
\le C_{\rm short},
$$
$$
C_{\rm short}
=110e^{883a}((n-1)!)^2(d-1)!(n!)^3.
\tag{6.3}
$$

### 6.2 长坏链

§3.2 取的列为完整 $\Phi$ 经合同逆和真实尾坐标旗得到。
已证
$$
\|\Phi\|\le3(n+2)^3 7^n,\qquad
\|P^{-1}\|<4,
$$
$$
\|(GA^e)^\dagger\|\le e^{662a}.
$$
(3.4) 的最小非零系数倒数至多 $l(l+1)/2$。
所以
$$
\|Y_l\|^2\|(B_{Y_l})^{-1}\|
\le72l(l+1)(n+2)^6 49^n e^{662a}
\le C_{\rm long},
$$
$$
C_{\rm long}
=72(d+1)(d+2)(n+2)^6 49^n e^{662a}.
\tag{6.4}
$$
置
$$
\boxed{C_m=C_{\rm short}+C_{\rm long}.}
\tag{6.5}
$$
例如 $m\ge5$ 时可粗记
$$
\log C_m\le883a+8d\log(2d).
\tag{6.6}
$$

以上每条链的候选都满足本链全部极点方程。
在标准完整直和中取各候选直和，平方范数按块相加，
统一费用取 (6.5)；不乘 primitive 条数或 $2^{R/2}$。
这是候选解的块估计，不是把原 Galerkin 源假设为块对角。

## 7. 原强权还原与对全部 $0<s\le1$ 的明确界

取
$$
y=m+R/2,\qquad c=y^{-2}.
$$
中位强尾归一化的条件数不超过 $4^R$。
只把坏链 $l\le d+1$ 从 $cL_l$ 变成单位 $J_l$，
附加条件数至多
$$
c^{-(l-1)}/(l-1)!\le y^{2d}.
$$
可各块统一归一化，使整块相似满足
$$
\boxed{\kappa(\mathcal S)\le4^R y^{2d}.}
\tag{7.1}
$$
$\mathcal S$ 保持物理孔级。

若物理原源为 $\xi_0$，相似坐标中的源是
$\xi'=\mathcal S^*\xi_0$；
候选解还原为
$\widetilde q_{\rm phys}=\mathcal S^{-*}\widetilde q'$。
因 $\mathcal S$ 保级，
相似源的 (4.3) 范数至多
$\|\mathcal S\|\mathcal Z_{m,R}(s)$。
源与解两侧成本合计恰为 $\kappa(\mathcal S)$。

于是对每个 $0<s\le1$ 都有明确不等式
$$
\boxed{
\|q_{-1}(s)\|
\le
C_m\,4^R(m+R/2)^{2d}\,
s^{(R-3d)/2+2m+3}\,
\mathcal Z_{m,R}(s).
}
\tag{7.2}
$$
若使用一般固定基准，(7.2) 仍成立，只需用 §6 中真实有限头条件数形成的 $C_m$；
强段 $R$ 的全部额外因子仍已明确列出。

没有遗漏把代数 primitive 分解还原到物理内积的费用。
此式也没有把 $\mathcal Z$ 用未证的常数替代。

### 7.1 较弱的几何孔衰减也足够形成强段预算

对任意固定 $0<\gamma\le1$，在同一原参数 $s$ 定义
$
\mathcal Z^{(\gamma)}_{m,R}(s)
=\left\|\sum_{g\ge A_0}\gamma^{1-g}P_g\xi_0(s)\right\|.
$
仍使用 (5.2) 的同一个完整候选。若 $z_\gamma$ 是上述加权源，则
$
\|Y^*\mathcal R_s\xi_0\|
=\left\|Y^*\sum_{g\ge A_0}s^g\gamma^{g-1}P_gz_\gamma\right\|
\le s^{A_0}\gamma^{A_0-1}\|Y\|\|z_\gamma\|.
$
这里 $s\gamma\le1$，所以最高系数取最低级 $A_0$；没有改变真核或源。
结合 $2A_0-N-2=m+2-d$，得对全部 $0<s,\gamma\le1$ 的另一明确界：
$
\boxed{
\|q_{-1}(s)\|
\le C_m4^R(m+R/2)^{2d}
s^{m+2-d}\gamma^{(R-d)/2+m+1}
\mathcal Z^{(\gamma)}_{m,R}(s).
}
\tag{7.3}
$
取 $\gamma=s$ 恰恢复 (7.2)。取固定 $\gamma<1/16$ 时，已列出的强段指数
$R\log4+(R/2)\log\gamma$ 为负；例如 $\gamma=1/32$ 给 $-(\log2)R/2$。
此时 $s$ 的显式代价与 $R$ 脱钩。因此后续可以估计较弱的固定几何孔衰减，
无须先证明准确的 $s^{g-1}$ 衰减。然而 $\mathcal Z^{(\gamma)}(s_*)$
的移动参数上界仍未给出，不能将这一替代接口当作已经完成的费用估计。

## 8. 统一缩放取原最大低 carry 时，头条件数界仍可用

原相邻 carry 的最大值为
$$
s_*=\kappa_0=e^{-1070}.
$$
取
$$
\bar\kappa_i=\kappa_i/s_*,\qquad
\bar d_i=d_i/s_*^{2^i-1}.
\tag{8.1}
$$
原 carry 递减，所以 $0<\bar\kappa_i\le1$；
在 $s=s_*$ 处恢复全部原旧权。

这里基准变换并不会破坏 (6.1)：
$$
-\log\bar d_i=\Lambda_i-1070(2^i-1)\le\Lambda_i,
\qquad \bar d_0=d_0.
\tag{8.2}
$$
N 型每个真实归一化删除算子的权不超过 $1$，
因为每次借位系数是若干 $\bar\kappa_i\le1$ 的乘积。
所以基准旧头及删除最高 Boolean 项的参考头范数仍小于 $6$。

[R239 真实逆芽证明](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §2 的圆盘估计只用 $d_0$ 固定、
各 $\Lambda_i$ 的上界和各高阶系数的绝对值；
由 (8.2)，相同圆盘和 Cauchy 界仍成立。
其 §3 的逆矩阵仍为
$$
(K^{-1})_{kj}=[w^k]\psi(w)^j/\bar W_j,
$$
输入权的联合指数估计因 $\bar\Lambda_i\le\Lambda_i$ 只会改善。
故旧头 $e^{221a}$ 界保持。
最高参考权为 $\bar d_{m-2}^2$；
原 $441a$ 证明对该最高位仅用
$2\bar\Lambda_{m-2}\le2\Lambda_{m-2}$，其余仍用旧逆芽圆盘。
所以参考头 $e^{441a}$ 界也保持。

因此 (7.2) 的显式 $C_m$ 确可用于 (8.1) 的原参数重标度。
这只支付有限头与强尾的线性代数常数，不支付完整原源。

## 9. 当前实际接口

在 $s=s_*=e^{-1070}$ 处，(7.2) 中强段的明确对数部分为
$$
R\log4-\frac{1070}{2}R
=-(535-\log4)R,
$$
另有已列出的 $O(d^4)+O(d\log(m+R))$ 头成本与指数平移。
因此，若后来能把完整
$\log\mathcal Z_{m,R}(s_*)$
控制在足够小的线性 $R$ 增长加可支付的头成本，
则允许取较大的多项式强段有真实预算空间。

但本条尚未证明这种 $\mathcal Z$ 上界，也没有控制完整
$q(s,t)-t^{-1}q_{-1}(s)$ 在原最高 $t$ 处的有效常数。
它们是明确保留的实际费用门。
固定 $m,R$ 的 (5.5) 不能替代这两项估计；
本条不声称原联合倒数预算已发散或 $N=M$ 已证。
