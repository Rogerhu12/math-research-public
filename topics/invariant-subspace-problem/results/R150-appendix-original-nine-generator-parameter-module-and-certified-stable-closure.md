# 原九生成元临界商的十二参数稳定闭包与完整来源递推

作者：Astra-ISP-789f / normal_annihilator；与 /root 联合推导。AI-assisted: GPT-6 Astra Pro。2026-11-16 UTC。

**状态：已证明的完整代数接口。** 本稿把已付原9×57表示转为12个参数上的九行模及五个参数矩阵的稳定闭包。它保留所有原参数与原18来源，不要求任何参数单位，也不宣称该商已为零。尚未运行新的模块 Gröbner 计算。

## 1. 同一个原完整临界商

沿用[原全局九生成元完整表示](R150-appendix-complete-original-global-nine-generator-critical-presentation.md)，取
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
\quad B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],
\quad S=B[u_0,\ldots,u_4].
$$
记 $b=y^{\mathsf T}w$，以及全部原生成元
$$
\mathcal G=(F_0,\ldots,F_4,W_0,\ldots,W_5,Y_0,\ldots,Y_5,b-1).
$$
原理想为 $I=(\mathcal G)$。已付完整矩阵与原来源给
$$
\mathcal Q:S^{57}\longrightarrow S^9,\qquad
\operatorname{coker}_S\mathcal Q\cong S/I.
\tag{1.1}
$$
所有矩阵条目对 $u$ 至多一次。第0生成元对应原常数1。

为明确原列编号，原十个生成单项式为
$$
m^{(10)}=(1,u_0,u_1,u_2,u_3,u_4,
 u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
删去轴 $*=6$，保留集合 $K=(0,1,2,3,4,5,7,8,9)$。令
$$
m=m^{(10)}_K.
$$
前稿已经给出 $c\in B^9$ 和真实原关系
$$
r_h=e_*+\iota c\in\operatorname{im}\mathcal P_{57},
$$
以及
$$
P\iota=I_9,\quad P(e_*)=-c,\quad
I_{10}-\iota P=r_he_*^{\mathsf T},\quad
\mathcal Q=P\mathcal P_{57}.
\tag{1.2}
$$
此处 $\iota$ 是保留九轴的字面包含。

## 2. 五个原参数矩阵及全部剩余列

记原十生成元的五个边界矩阵为 $\widetilde N_i\in\operatorname{Mat}_{10}(B)$。从原45个保留轴的边界列读取
$$
N_i=P\widetilde N_i\iota\in\operatorname{Mat}_9(B),
\qquad
R_i=u_iI_9-N_i\quad(0\le i<5).
\tag{2.1}
$$
这45列就是原9×57中的对应原列；没有用一般点求解。

另外五个被删轴的原边界列是
$$
C_i=P(u_ie_*-\widetilde N_ie_*)
=-u_i c-P\widetilde N_i e_*.
$$
用已经保留的 $R_i$ 消去其字面 $u_i$，得到真正的参数列
$$
V_i=C_i+R_ic=-N_ic-P\widetilde N_i e_*\in B^9.
\tag{2.2}
$$
替换 $C_i$ 为 $V_i$ 是双向原列操作。因此原完整关系模也可写为
$$
\sum_i R_i S^9+\sum_i SV_i+\sum_{j=0}^5 SH_j
 +S(b-1)e_0,
\tag{2.3}
$$
其中 $H_j=P h_j\in B^9$ 是前稿全部六个 mean 列。

前稿保留单项式的字面路径给
$$
e_a=m_a(u)e_0\pmod{\operatorname{im}\mathcal Q}
\quad(0\le a<9).
\tag{2.4}
$$
具体而言，五个一次轴由 $R_{i,0}$ 给出，三个保留二次轴分别由
$u_2R_{3,0}+R_{2,u_3}$、
$u_2R_{4,0}+R_{2,u_4}$、
$u_3R_{4,0}+R_{3,u_4}$给出。
因此 $(b-1)e_a$ 的全部九列本来都在原关系模内。

## 3. 完整参数种子与稳定闭包

在 $B^9$ 中保留以下110个字面种子列，包括任何实际为零的列：

- 五个 $V_i$；
- 六个 $H_j$；
- 九个 $(b-1)e_a$；
- 所有 $0\le i<j<5$ 的九列交换子
  $$(N_iN_j-N_jN_i)e_a.$$

令 $L_0$ 为它们生成的 $B$-子模，并递归定义
$$
L_{n+1}=L_n+\sum_{i=0}^4N_iL_n,\qquad
L=\bigcup_{n\ge0}L_n.
\tag{3.1}
$$
这是含全部种子的最小共同 $N_i$-稳定 $B$-子模。

由于 $B$ 是 Noether 环，$B^9$ 的升链最终稳定，但本稿没有提供一个数值停止阶。九个生成坐标绝不意味着九轮后必然稳定；参数关系可能含非平凡扭子。

得到精确同构
$$
\boxed{\quad B^9/L\ \cong\ S/I,\quad
u_i\text{ 在左侧由 }N_i\text{ 作用。}\quad}
\tag{3.2}
$$
尤其，把源算法转到九行、12个参数不会丢掉任何原 $u$ 关系、rank3例外或 Bell=1 的参数分支。

### 证明

先在 $M=S^9/\operatorname{im}\mathcal Q$ 中考察自然映射
$B^9\to M$。由(2.1)，任何含 $u$ 的系数均能逐次用 $N_i$ 回代，故此映射满。

(2.2)及原mean、Bell关系使前20个种子为零。在 $M$ 中 $N_i$ 与 $u_i$ 的作用相同，所以全部交换子也为零，且任一零关系经 $N_i$ 作用仍为零。因此
$$
L\subset\ker(B^9\to M),
$$
得到满射 $B^9/L\to M$。

反向，由 $N_iL\subset L$，五个矩阵在 $B^9/L$ 上给良定义的算子；全部交换子已在 $L$ 中，所以这些算子可交换。它们赋予 $B^9/L$ 一个真正的 $S$-模结构。此时 $R_i$ 自动为零；由种子 $V_i,H_j,(b-1)e_0$ 及
$C_i=V_i-R_ic$，原全部57列均为零。因此有反向映射
$$
M\longrightarrow B^9/L.
$$
两个复合在全部九个字面生成元上为恒等，故互逆。这证明(3.2)，并与(1.1)识别为同一个原临界商。

同一构造在任意参数基变换后仍按同一关系给同构；在非 Noether 基上不额外断言(3.1)有有限停止阶。

## 4. 逐列原18来源：不靠矩阵计数代替身份

前稿实际给每个保留边界矩阵的完整来源
$$
m R_i=\mathcal G S_i,\qquad S_i\in\operatorname{Mat}_{18\times9}(S).
\tag{4.1}
$$
五个原额外边界列及六个mean列的来源也完整保留，分别写为
$$
m C_i=\mathcal G T_i,\qquad mH_j=\mathcal G\sigma_j.
$$
因此(2.2)的准确来源是
$$
mV_i=\mathcal G(T_i+S_ic).
\tag{4.2}
$$
九个Bell种子的来源是 $m_a e_{\mathrm{Bell}}$，其中 $e_{\mathrm{Bell}}$ 指向原第18个生成元 $b-1$。

由 $mN_i=u_i m-\mathcal G S_i$ 直接相减可得全部交换子来源
$$
\boxed{
m(N_iN_j-N_jN_i)
=\mathcal G\bigl(
u_jS_i-u_iS_j+S_jN_i-S_iN_j
\bigr).
}
\tag{4.3}
$$
该式逐九列成立，符号与矩阵顺序均固定。

更一般地，若当前参数列 $v\in B^9$ 有真实原来源
$$
mv=\mathcal G\sigma,
$$
那么下一层列的来源由
$$
\boxed{
mN_iv=\mathcal G\bigl(u_i\sigma-S_iv\bigr)
}
\tag{4.4}
$$
精确给出。所有参数行列组合也同步线性组合来源。

所以(3.1)的每个实际有限前缀都有完整、可追溯的原18来源。可用共享算术图保留这些乘法，而不复制原参数大多项式；仍必须按同一原字典验证实际候选。这里没有加入任何参数分母，也不把某个数值纤维的关系升为全参数关系。

## 5. 正证与完整停止的不同验证门

**正证门。** 若某个有限前缀中实际找到
$$
e_0=\sum_\nu a_\nu(y,w)v_\nu,
$$
并同步保留(4.2)–(4.4)的原来源 $\sigma_\nu$，则
$$
1=me_0=\mathcal G\left(\sum_\nu a_\nu\sigma_\nu\right).
\tag{5.1}
$$
这就是原17梯度与原Bell−1的完整多项式身份。只要(5.1)在原 $E$ 上逐式成立，便已是正证；不需要另付其余 Gröbner 列或所有 S-pairs 的完备性。

若只在有限域发现并核验了这条身份，它仍只是该有限域上的正证与原特征零来源的候选支撑。必须另外恢复真正的 $E$ 系数并核验全部原乘积，才能使用特征零结论。不得由一次有限域空纤维推全参数 $E$ 商为零。

**完整停止门。** 若希望把某个前缀作为全部参数关系模，必须实际证明
$$
N_iL_n\subset L_n\quad\text{对全部五个 }i.
\tag{5.2}
$$
例如使用已完整核验的模块标准基，并逐原列付出全部(5.2)的来源。只有在此之后才可由(3.1)断言 $L_n=L$。一次候选算法正常返回、某些参数点秩不再增长或预定轮数用尽，都不替代(5.2)。

本稿不把特征零商的非零性从有限域负结果中推出，也没有宣称某个有限前缀已经满足(5.1)或(5.2)。

## 6. 与当前 Bell 自然幂任务的关系

本稿直接复用已发表的原9×57表示及其完整来源，保全部12个参数，不重复完整权十二矩阵。它也不依赖把原19图中任何一个开集当成一般位置；若后续另按[完整19图覆盖](R150-appendix-original-mean-quadrics-dual-normalization-and-complete-bell-cover.md)分图，仍须保该图的全部原关系与清幂来源。

若最终(5.1)真实完成，使用已付[自然幂齐次化与正来源门](R150-appendix-original-bell-natural-power-homogenization-and-positive-source-gate.md)可将其运输为某个有限原 Bell 自然幂的来源。当前没有提供这样一个新指数或新来源。

[完整权九原核与三次非成员结论](R150-appendix-original-bell-cube-nonmembership-and-complete-weight-nine-source-kernel.md)仍保持原有范围；本稳定闭包接口没有改变已付的三次障碍，也没有预先确定四次方是否在原理想中。
