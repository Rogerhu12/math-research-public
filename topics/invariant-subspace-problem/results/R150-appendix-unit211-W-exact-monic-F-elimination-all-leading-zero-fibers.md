# R150：全余 W 的首一二次 F 原方程消去，含全部 F 首项零面

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。以下是完整代数证明；不以尚未运行的新系数探针为成立条件。范围为已发表全 W 首一三次／二次环境和十一条原行输入所在的同一个局部化域。

## 1. 一般首一二次消去引理

设 K 为代数闭域，特征任意。固定同一点的系数 p,q,A_i,B_i，i=1,...,n。考虑同一个未知 F 的方程

$$
q_F(F)=F^2+pF+q=0,\qquad R_i(F)=A_i+B_iF=0.
$$

定义

$$
H_{ij}=B_jA_i-B_iA_j,\qquad
\Theta_i=A_i^2-pA_iB_i+qB_i^2.
$$

那么存在共同的 F 当且仅当所有 H_{ij} 与所有 Theta_i 同时为零。此命题允许任意 B_i 为零，也允许所有 B_i 同时为零。

必要性由两个完整多项式身份给出：

$$
H_{ij}=B_jR_i-B_iR_j,
$$

$$
\Theta_i=B_i^2q_F-(B_iF+B_ip-A_i)R_i.
$$

第二式直接展开右侧：乘积中的 F 项交叉消去，所余恰为 A_i^2-pA_iB_i+qB_i^2。没有倒置 B_i、Theta_i 或任何范数。

充分性分两类，覆盖所有情形。若某个 B_j 非零，取 F=-A_j/B_j。Theta_j=0 正是 B_j^2q_F(F)=0，所以 q_F(F)=0。对每个 i，H_ij=0 给出 A_i+B_iF=0，且所有原行使用同一个 F。若所有 B_i 均为零，则 Theta_i=A_i^2=0，在域中迫 A_i=0；此时全部 R_i 恒零，而首一二次 q_F 在 K 中有根。两类都没有遗漏首项零纤维。

这里给出的是逐点存在性的精确等价。它不声称由 H_ij、Theta_i 生成的理想与原消元理想逐项相等，也不把原方程商当作自由模。

## 2. 原 W 三条均值／N1 行的直接应用

沿用：

- [全 W 首一 T 三次、F 二次环境](R150-appendix-unit211-W-global-monic-T-three-F-two-and-six-column-environment.md)；
- [完整耦合四行三列余子式](R150-appendix-unit211-W-coupled-original-Gram-value-four-by-three-complete-minors.md)；
- [原完整十三行六列返回](R150-appendix-unit211-W-global-monic-three-two-thirteen-original-rows-six-columns.md)。

S=T-2lambda，F=2f-u lambda。真实首一环境为

$$
q_3(S)=0,\qquad
q_F(F,S)=F^2+p(S)F+q(S)=0.
$$

在已经实际核回的原 E1、EBe、N1 三行中，清除已付分母、只剥已付公共内容后，得到

$$
R_i=A_i(S)+B_i(S)F,\qquad
\deg A_i\le2,\quad\deg B_i\le1.
$$

q_F 的 p 对 S 至多一次、q 对 S 至多二次。固定任一满足原 q_3 的 S 后，上一节引理逐点适用。因此原 q_F 和这三条原行有同一个 F 根，当且仅当三条 H_ij 与三条 Theta_i 在同一个 S 处全为零。

每条 Theta_i 对 S 至多四次。按已付首一 q_3 除法得到

$$
\Theta_i=\overline\Theta_i+U_iq_3,\qquad
\deg\overline\Theta_i\le2.
$$

所有 H_ij 同样约化至二次。保留每个真实约化迹，故可以完全在三个真实值列 (1,S,S^2) 上进行后续原常数余子式运算。这样增加的是原 q_F 约束，不能只由先前两两 H_ij 的必要关系代替。

q_F 原定义为已付单位倍数的 m EBe+ell(1-Q) EBo；m、ell、1-Q 及 q_F 的归一化首项均已支付。因此 q_F、EBe 同时为零恢复 EBo=0。本节的逐点等价也覆盖完整四条原 E1、EBe、EBo、N1，而不是任意选择了一个 F 首项非零的补图。

## 3. 完整十一条原输入的一次性一般应用

参见：

- [原奇 N/P 与完整 NV 的低 D 理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)；
- [十一条完整原行的六列返回](R150-appendix-unit211-W-global-D-linear-eleven-original-six-column-return.md)。

这份实际原输入含六条 Gram 行 E1、EBe、EBo、N1、NS、PS，两条纯 S 的完整 r_2、R_6，以及完整 N_low、P_low、V_low。后者分别保持个别 N、个别 P 和整个 N4(V)，在原物理 D 非零域与已发表旧十三行理想等价。

在 q_F、q_3 环境中，每条行都唯一写成 A(S)+B(S)F，A,B 对 S 至多二次。去掉由 q_F、EBe 已经恢复的 EBo，取八条

$$
E1,\ EBe,\ N1,\ NS,\ PS,\ N_{\rm low},\ P_{\rm low},\ V_{\rm low}.
$$

对这八条逐一形成 A_i、B_i。对所有 28 个配对形成 H_ij，再形成 8 条 Theta_i。全部 36 条都可按首一 q_3 精确约化至 S 二次，没有新的几何首项分母。连同原两条纯 S 行 r_2、R_6，可得到 38 条二次余式。

对每个固定的已付权参数、lambda 及满足 q_3 的 S，所有这 38 条同时为零，逐点等价于存在共同 F 使整个十一行原输入同时为零。证明正是第一节八行版本，加上第二节 EBo 的已付恢复。全程保留原物理 D 非零以及此前的全部局部化约束；没有将某个范数设为单位。物理 D=ell A_lambda-T^2 只依赖 S、lambda 和权，所以本段的同 F 恢复不会改变其非零条件。

这是一条完整的代数存在性接口，不声称已展开这 38 条大系数，也不声称已计算它们的全部余子式。实际系数可以从已核回的十一条六列原行逐项再生。逐点等价不能替代原 D 非零域之外的独立 h=k 碰撞分析。

## 4. 本次冻结的后续实际输入

新源仅选前三条均值／N1 的 Theta_i，并与此前 r_2、S r_2、H01、H02 组合，准备计算五个新的固定三行余子式：

1. r_2、S r_2、Theta_E1；
2. r_2、S r_2、Theta_EBe；
3. r_2、S r_2、Theta_N1；
4. r_2、H01、Theta_E1；
5. r_2、H02、Theta_E1。

源码：

[2026-11-27-unit211-W-monic-F-norm-original-three-column-minors-8542.py](../notes/2026-11-27-unit211-W-monic-F-norm-original-three-column-minors-8542.py)

SHA256 70603b1611a262467b67e5b41fdabfbb867a5b81e5d6f53f3cf1ef2f5ddb4240；5445 字节；blob 7513ffea9676b49360fdbd625f23e8a5a1fb5c01。其固定依赖是 f5c0226e... 耦合原构造前缀及该源的已有固定依赖。只执行构造，不重复之前四个 cofactor 的完整门。资源上限为 180 秒、4 GiB，所有新原范数身份、q_3 约化迹及每个常数余子式三个列都须实际乘回。

本稿冻结时此新源尚未执行，故上述五个余子式没有任何成功、非零、次数或排空宣称。第一至三节已经由完整纸面恒等与已发表原输入成立；后续实际回执单独登记。A143、r_2 首项、各 B_i 以及任一新的参数首项均不在本结论中支付。
