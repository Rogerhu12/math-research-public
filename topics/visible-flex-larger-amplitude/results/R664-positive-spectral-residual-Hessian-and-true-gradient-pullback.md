# R664：正谱残差的准确 Hessian、真实梯度及完整空间拉回

2026-11-20，Astra-larger-resume-24b2ab87-20261120；recover_evidence。

**状态：完整数学证明与小规模新实现验证均已完成；完整源码已交给真实求解器消费。** 本条保持 [R660](R660-positive-spectral-Gram-blocks-and-maximum-control.md) 的同一正权、同一全部观察行、同一固定 p/epsilon/scale 和同一真实目标，提供其对三项 Gram 残差的准确正定 Hessian。

对自由变量的模型使用这个 Hessian 的 Jacobian 拉回，保留原真实梯度。它一般不是整个自由变量目标的完整 Hessian；更不能以新 Hessian 乘原残差替代梯度。本条给出两者的准确区别以及 LSMR 所需的新右端项。

## 1. 同一个目标与其原真实梯度

在任一观察点设

$$r=(e,f,g)^T,\qquad
E=T r=\begin{pmatrix}e&f\\f&g\end{pmatrix},\qquad p=2k\ge2,$$

$$\ell(E)=\operatorname{tr}\varphi(E),\quad
\varphi(\lambda)=\left({\lambda^2+\epsilon^2\over c^2}\right)^k,
\quad\epsilon>0,\ c>0.\tag{1}$$

矩阵空间使用 Frobenius 内积。映射 T 的伴随满足

$$T^*\begin{pmatrix}a&b\\b&d\end{pmatrix}=(a,2b,d)^T.$$

定义奇多项式

$$h(\lambda)=\lambda\left({\lambda^2+\epsilon^2\over c^2}\right)^{k-1},
\qquad\varphi'(\lambda)={2k\over c^2}h(\lambda).\tag{2}$$

因为 $\operatorname{tr}(E^m)$ 的方向导数是 $m\operatorname{tr}(E^{m-1}V)$，对(1)的多项式逐项求导即得

$$\nabla_r\ell={2k\over c^2}\,g_0(r),\qquad
g_0(r)=T^*h(E).\tag{3}$$

若 $W=((E^2+\epsilon^2I)/c^2)^{k-1}$，则 $h(E)=EW=WE$。R660 的原正块 $K(E)$ 满足

$$g_0(r)=K(E)r.\tag{4}$$

新模块独立计算同一矩阵多项式(3)；未修改(3)，未丢任何 f 的因子2，也未用后文的新 L 代替 K 再乘 r。

## 2. 矩阵多项式的准确差商 Hessian

令 $E=Q\operatorname{diag}(\lambda_+,\lambda_-)Q^T$，Q 正交。对任意对称扰动 V，写

$$\widetilde V=Q^TVQ=\begin{pmatrix}a&b\\b&d\end{pmatrix}.$$

对单项式 $E^m$ 有

$$D(E^m)[V]=\sum_{j=0}^{m-1}E^jVE^{m-1-j}.$$

在上述谱基中，(i,j) 元乘上

$$\sum_{q=0}^{m-1}\lambda_i^q\lambda_j^{m-1-q}
=\begin{cases}
(\lambda_i^m-\lambda_j^m)/(\lambda_i-\lambda_j),&\lambda_i\ne\lambda_j,\\
m\lambda_i^{m-1},&\lambda_i=\lambda_j.
\end{cases}$$

因此对 h 的各单项式线性相加，得到

$$\langle V,Dh(E)[V]\rangle_F
=h'(\lambda_+)a^2+h'(\lambda_-)d^2+2d_h b^2,\tag{5}$$

$$d_h=\begin{cases}
{h(\lambda_+)-h(\lambda_-)\over\lambda_+-\lambda_-},&\lambda_+\ne\lambda_-,\\
h'(\lambda_+),&\lambda_+=\lambda_-.
\end{cases}$$

连同(2)，这给出点目标的准确二阶导数

$$D^2\ell(E)[V,V]
=\varphi''(\lambda_+)a^2+\varphi''(\lambda_-)d^2
+2{\varphi'(\lambda_+)-\varphi'(\lambda_-)\over\lambda_+-\lambda_-}\,b^2,\tag{6}$$

重根时最后差商取连续导数。这里

$$\varphi''(\lambda)
={2k(\lambda^2+\epsilon^2)^{k-2}\bigl(\epsilon^2+(2k-1)\lambda^2\bigr)\over c^{2k}}>0.\tag{7}$$

当 k=1 时式(7)简化为常数 $2/c^2$。正 epsilon 使任何残差、任何重根均无奇异点。

## 3. 无相消且正权的差商公式

由微积分基本定理，所有两实数 $\lambda_\pm$ 都满足

$$d_h=\int_0^1 h'((1-t)\lambda_-+t\lambda_+)\,dt.\tag{8}$$

对 k=1，$h'\equiv1$；对 k≥2，

$$h'(\lambda)
=\left({\lambda^2+\epsilon^2\over c^2}\right)^{k-2}
{\epsilon^2+(2k-1)\lambda^2\over c^2}.\tag{9}$$

这是次数 $2k-2$ 的偶多项式，其偶次系数非负，且

$$h'(\lambda)\ge\kappa:=\left({\epsilon\over c}\right)^{2k-2}>0.\tag{10}$$

因此 d_h 也至少为 $\kappa$。

实现用 [0,1] 上 k 点正 Gauss 规则计算(8)：

$$d_h=\sum_{j=1}^k\omega_j
h'((1-t_j)\lambda_-+t_j\lambda_+),\quad
\omega_j>0,\quad\sum_j\omega_j=1.\tag{11}$$

为说明(11)没有新增积分余项，记 $P_k$ 为区间[0,1]上与所有次数小于 k 的多项式正交的 k 次多项式。正交性迫使其有 k 个互异的内部实根：若内部变号根较少，将这些根的一次因子相乘得到次数小于 k 的 q，则 $P_kq$ 在区间上同号而非恒零，与 $\int P_kq=0$ 矛盾。

取这些根为 $t_j$，其 Lagrange 基为 $l_j$，设 $\omega_j=\int_0^1 l_j$。因为 $l_j^2-l_j$ 可被 $P_k$ 整除且商次数至多 k−2，正交性给
$\omega_j=\int_0^1 l_j^2>0$。任意次数至多2k−1的多项式都能写成 $P_kq+r$，其中 q,r 次数至多k−1；积分的第一部分为0，第二部分由插值准确得到 $\sum_j\omega_jr(t_j)$。故此规则对(8)的 $2k-2$ 次被积式准确，证明(11)。

数值代码使用普通浮点计算节点和权重，并明确标记为普通数值实现，不是向外证书。其表达式是正项求和，避免两近值相减再除小 gap 的相消；在完全重根时直接采用 $d_h=h'$。数学公式的准确性由上述多项式恒等式支付，不把有限浮点值说成准确实数积分。

## 4. 直接作用于原三个残差的正块

设 gap=$\sqrt{(e-g)^2+4f^2}$。gap>0 时置

$$n={e-g\over\mathrm{gap}},\qquad s={2f\over\mathrm{gap}},\qquad n^2+s^2=1.$$

重根时选 $n=1,s=0$，结果与任选谱基一致。对原三维扰动 $v=(v_e,v_f,v_g)$，定义谱 Frobenius 坐标

$$\begin{aligned}
(Cv)_1&={v_e+v_g\over2}+n{v_e-v_g\over2}+s v_f,\\
(Cv)_2&=\sqrt2\left(-s{v_e-v_g\over2}+n v_f\right),\\
(Cv)_3&={v_e+v_g\over2}-n{v_e-v_g\over2}-s v_f.
\end{aligned}\tag{12}$$

这正是 $(a,\sqrt2b,d)$，从而

$$C^TC=\operatorname{diag}(1,2,1)=:D_F.$$

令

$$B=\operatorname{diag}\bigl(\sqrt{h'(\lambda_+)},\sqrt{d_h},\sqrt{h'(\lambda_-)}\bigr)C,
\qquad L=B^TB.\tag{13}$$

由(5)可得

$$L=T^*Dh(E)T,\qquad \nabla_r^2\ell={2k\over c^2}L.\tag{14}$$

所以 L 是准确的未乘 $2k/c^2$ 的三项残差 Hessian。特别是

$$v^TLv\ge\kappa(v_e^2+2v_f^2+v_g^2)\ge\kappa|v|^2.\tag{15}$$

若 $m_\mathrm{eig}$ 和 $M_\mathrm{eig}$ 分别是 $h'_+,d_h,h'_-$ 的最小、最大值，则原三维 Euclidean 块有

$$m_\mathrm{eig}I\preceq L\preceq2M_\mathrm{eig}I.\tag{16}$$

接口的 minimum_eigenweight/maximum_eigenweight 记录的是上述 Frobenius 正交坐标的特征权，不误称它们恰好等于原 r 坐标 L 的最小、最大特征值。

代码保存 n,s 和三个正平方根，共每点5个标量数组；以 B、$B^T$ 直接作用得到 L。无需先通过包含近相消项的显式六个元素再做 Cholesky，也不丢小特征权。混合项的 $\sqrt2$ 已包含在(12)，外部不应再给旧中间残差额外乘一次 $\sqrt2$。

在名义 p8、epsilon=.001、scale=.05 下，$\kappa$ 约为 $6.4\cdot10^{-11}$。数值实现仍按实际给定正参数计算，不靠夹断小权或移除观察行获得正定性。

## 5. 与旧冻结谱权的区别

旧 K 满足(4)，故仍给准确真实梯度。其二次型 $v^TKv=\operatorname{tr}(W(Tv)^2)$ 则不是一般 p>2 的准确残差二阶型。

沿一条谱值的对角扰动，旧权为 $w(\lambda)=((\lambda^2+\epsilon^2)/c^2)^{k-1}$，而新权满足

$$ {h'(\lambda)\over w(\lambda)}
=1+{2(k-1)\lambda^2\over\lambda^2+\epsilon^2}\in[1,2k-1].\tag{17}$$

因此 p8 在该谱值远离 epsilon 时新旧局部曲率相差接近7。式(17)仅解释这种具体二阶差异；它不证明实际受几何约束求解器必然接受更长步，也不替代真实目标回溯。

尤其不能把 K 全部换成 L 后仍令梯度为 Lr。一般 $Lr\ne g_0$；对 $\epsilon$ 可忽略的单谱值，前者近似比后者大 $p-1$ 倍，已经改变了真实一阶导数。

## 6. 全部正权行、物理粗列与原完整自由空间

令观察行索引 i 包含原径向点及四分之一角轨道，正权 $w_i=\omega_s m_j$，其中 $m_j$ 是精确角轨道重数。令

$$C_0=\sum_iw_i,\qquad
\Phi(x)={1\over C_0}\sum_iw_i\ell(E_i(x)),\qquad J_i=Dr_i(x).$$

本条定义未除 $C_0$ 的半梯度和半 Hessian 拉回

$$g={k\over c^2}\sum_iw_iJ_i^Tg_{0,i},\qquad
N={k\over c^2}\sum_iw_iJ_i^TL_iJ_i.\tag{18}$$

则

$$\nabla_x\Phi={2g\over C_0},\qquad
\text{残差 Hessian 拉回}={2N\over C_0}.\tag{19}$$

对原全部自由方向、任意既有物理粗列以及两者的增广，式(18)均成立。只要各列代表原场的真实 Jacobian，没有因为采用粗列而改变目标行。N 对所有被 J 看见的方向为正；J 的真实核仍可能存在，不会由点块正定性凭空消失，因此既有物理 H² 正尺度/阻尼仍有作用。

新的接口 HessianBlocks(raw,parameters).normal_and_gradient(J,raw,weights) 返回

$$\left(\sum_iw_iJ_i^TL_iJ_i,\quad\sum_iw_iJ_i^TK(E_i)r_i\right).$$

外层对两者同时乘 $k/c^2$，再使用同一 $C_0$ 归一。名义 p8,c=.05 对应因子1600，实施按固定参数计算实际浮点值，与 R660 接口保持同一单位。

线性模型的真实 Phi 预测变化为

$$\Delta\Phi_{\rm model}(\alpha d)
={2\alpha g^Td+\alpha^2d^TNd\over C_0}.\tag{20}$$

物理 H² 范数、阻尼或线性几何不等式可照原求解器加入；真实接受仍计算固定参数的 Phi，并同步读旧 Jw、maxGram 和原几何约束。

## 7. 为什么这不是完整自由变量 Hessian

对任意自由方向 d，链式法则准确给

$$D^2\Phi(x)[d,d]
={1\over C_0}\sum_iw_i\left[
D^2\ell(E_i)[T J_i d,T J_i d]
+\nabla_r\ell(r_i)\cdot D^2r_i(x)[d,d]\right].\tag{21}$$

本条 $2d^TNd/C_0$ 是第一项；它没有包括真实 Gram 残差关于自由变量的第二导数项。第二项一般非零且不必非负。因此准确的名称是“残差 Hessian 的正拉回”，不能简称为已得到完整 x-Hessian。

它也不是所有步长上的 MM 上界。即使完整点 Hessian 在当前点准确，高次多项式在远处的曲率仍可能更大；场映射本身还非线性。所以回溯不能用(20)替代真实目标。

若无约束的正阻尼系统为 $(N+\mu^2C_0G)d=-g$、G正定，则非零步有
$g^Td=-d^T(N+\mu^2C_0G)d<0$，这是局部真实下降方向。对含约束 QP，仅在零方向可行且二次模型确实下降时同样推出真实一阶下降；本文不对零方向不满足约束的情形作未经证明的保证。

## 8. 完整空间 LSMR 的正确右端项

原 operator 已带角轨道平方根：$J_{\rm native,i}=\sqrt{m_j}J_i$。新完整空间桥选择

$$A_i=\sqrt{\omega_s}\,B_iJ_{\rm native,i},\qquad
v_i=\sqrt{\omega_s m_j}\,B_i^{-T}g_{0,i}.\tag{22}$$

直接相乘得到

$$A^TA=\sum_iw_iJ_i^TL_iJ_i,\qquad
A^Tv=\sum_iw_iJ_i^Tg_{0,i}.\tag{23}$$

所以解 $Ad\simeq-v$ 给出(18)的未乘共同系数系统。A的转置必须按 $B_i^T$ 和原 native 的 vjp 实现；原角轨道每侧只出现一次。

式(22)的 v 是为匹配真实梯度而构造的虚拟右端，**不是** $\sqrt{\omega_s}B_i r_{{\rm native},i}$，其平方范数也不是当前 Phi。后一个旧形式会错误地产生 $J_i^TL_i r_i$，违反(3)。

无需数值拟合来求 $B^{-T}$。由 $C^TC=D_F$ 有

$$C^{-T}=CD_F^{-1},\qquad
B^{-T}=\operatorname{diag}(1/\sqrt{h'_+},1/\sqrt{d_h},1/\sqrt{h'_-})\,C D_F^{-1}.\tag{24}$$

实现先把 cotangent 的中间分量除2，再应用(12)的变换和三个正倒平方根，恰是(24)。NativeLinearization 保留外部 true_gradient_factor=$2k/(c^2C_0)$，并调用 R660 的同一 statistics 对真实新候选回溯。

## 9. 新完整源码与一次必要的实现核验

完整小源为 scripts/resume_20261120/positive_spectral_gram_hessian.py，SHA256

29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4。

它独立于正在运行的 R660 模块，不改旧字节。Parameters 和真实目标统计仍由旧模块提供；点块及其导数公式采用本文的新完整实现。

一次3×4点、7列的小检查使用固定 seed=20261120664，p8、epsilon=.001、scale=.05；覆盖零残差、正/负重根、近重根和一般随机对称块。参照值由独立完整2×2矩阵乘法计算多项式 h(E)，以 complex step 求其方向导数；没有使用本条的谱差商公式作自己的对照。

| 新实现风险 | 相对差 |
|---|---:|
| 点 Hessian 对独立矩阵多项式梯度的 complex step | 1.1925922226443216e−15 |
| 各点中最大 Hessian 相对差 | 1.2767658988816504e−15 |
| 原真实梯度对 R660 K(E)r | 6.490794817411646e−16 |
| 真实 Phi 一阶导数 | 7.953895052238625e−17 |
| B 与 Bᵀ 的伴随 | 1.2585595470381747e−16 |
| B−T 真梯度右端的恢复 | 5.971594184560426e−17 |
| 7列新正规矩阵装配 | 7.884551273744472e−16 |
| 同方向二阶导数 | 0.0（本次浮点相等） |
| 小 native 桥正规算子 | 3.111764229740983e−16 |
| 小 native 桥真实梯度右端 | 2.1306883758574178e−16 |

零值那行不表示一般误差严格为零。以上均是普通数值验证，不是向外证书；数学正定性和尺度关系由前八节证明。原三项块的最小数值特征值为6.4e−11，小粗正规矩阵最小特征值为1.2668545964776365。

完整检查脚本为 scripts/resume_20261120/check_positive_spectral_gram_hessian.py，SHA256
78aef15c5f63870b80ef4011096ac4658ad8487d7ba8ff8dad16374d1b09b3f5。
其最初一次尚未返回检查结果的调用因独立 probe 的 einsum 省略索引写法报错；修正的是 probe 的缩并索引，新模块字节未变。随后一次完整检查自然结束，exit0。没有重跑任何真实旧候选、全域证书或旧算子大 probe。

完整报告仅 scratch：positive-spectral-hessian-small-check.json，SHA256
1c78e66cee7aea0000e6ba08e09cc4d3a24c4a110f7a6abf62c94b6d1af2b97c。
旧 R660 源 SHA256 为
e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91。

把三个源码放在同一公开目录后，执行检查脚本即可复算这项小验证；其参数与种子完整写在脚本中。真实全场 v7 的接受步、实际 Phi/Jw/max 与几何约束结果另据对应真实运行记录，不由本条小模型代替。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
