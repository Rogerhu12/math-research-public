# R697 — 轴端平面两形状可达族与控制球的准确关系

**状态：已证明（仅指正文完整证明的恒等式、条件命题与适用范围）。**

本文件按根README3、8、12正式登记已有完整证明；没有重做科学计算或把旧结论算作新进展。[原完整笔记](../notes/2026-11-26-zero-endpoint-axis-planar-control-equivalence.md)保持原字节（SHA256 `26a6bf9e0d0429e3a968be0b767e1dd16a53aff39d5ae5f74ce212aa7809c406`）。原文中实施/运行状态以其记录时点理解；当前真实结果见[HANDOFF](../HANDOFF.md)。没有将条件界、失败或数值证据升级为所求闭族的存在证明。

日期：2026-11-26。类型：已证明的有限控制族恒等式与适用范围。本文只读取完整源码和已刊的十八个固定输入字，作解析推导；没有执行端点积分、矩阵数值分解、root、F/J 或新的科学计算。结论限于所述零 omega 轴对称基底和反射轴上的子午线，不证明当前有限控制有根，也不证明等距曲面存在。

## 1. 来源和对象

旧端轴输入是 [so3_zero_closure_endpoint_operator.py](../scripts/resume_20261126/so3_zero_closure_endpoint_operator.py)，完整 SHA256 5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46。新的固定 moment 输入是 [so3_zero_closure_moment_operator.py](../scripts/resume_20261126/so3_zero_closure_moment_operator.py)，完整 SHA256 44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e。

全部十八个准确 literal binary64 参数及其来源在 [frozen-zero-moment-Q-actual16-parameters.json](../computations/frozen-zero-moment-Q-actual16-parameters.json)，definition SHA256 为 05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e。本文不把这些工作矩选出的参数称为真实连续积分的准确逆。

沿用 [R695](../results/R695-so3-zero-closure-bubble-uniform-IFT.md) 的世界左乘约定。两个 C² bubble 记为 beta_0、beta_1；当前宽支撑的精确相对三节点为

$$
(1/32,1/4,15/32),\qquad(17/32,3/4,31/32).
$$

只在本节所述初点，omega=0，当前 core 等于固定 chart core；所有这些量在完整外层问题仍是原自由变量，本分析没有将它们从求解中固定。准确单位基底写成

$$
T_0(s,\phi)=b(s)e_r(\theta_0(\phi))+c(s)e_z,
\quad b=a_s,\quad b^2+c^2=1.
$$

固定 phi=0。偶频 core 使 theta_0(0)=0，Gamma(0)=p(0)e_x，cap 为 R e_x+H e_z，所以 T0 位于 xz 平面。以下把端点校正变量明确写为 z=(z_x,z_y,z_z)，不把第二角导数 z_phiphi 与分量 z_y 混淆。

## 2. 十八字输入在平面分支上的准确化简

每个固定矩阵都有准确稀疏形状

$$
Q_i=
\begin{pmatrix}
0&A_i&0\\
B_i&0&C_i\\
0&D_i&0
\end{pmatrix},\qquad i=0,1.
$$

在反射固定子空间 z_y=0 上，直接矩阵乘法给

$$
Q_i z=t_i e_y,\qquad
t_i=B_i z_x+C_i z_z.
\tag{1}
$$

决定这两个平面角的四个准确输入字是

| 系数 | 准确 binary64 hex |
| --- | --- |
| B0 | 0x1.972524c4f8e87p+0 |
| C0 | -0x1.e6c4f7d8b8182p+0 |
| B1 | 0x1.03bb57b63d53dp-1 |
| C1 | 0x1.41266339b41f3p+1 |

这些字的符号严格为 (+,−,+,+)。因此

$$
L=\begin{pmatrix}B_0&C_0\\B_1&C_1\end{pmatrix},
\qquad \det L=B_0C_1-C_0B_1>0.
\tag{2}
$$

(2) 是只用符号即可完成的准确证明，没有求工作行列式、逆矩阵或数值条件数。t0、t1 因而可以独立遍历整个实平面。

新的完整修正角在该分支恰为

$$
W(s,0)z=
\bigl(\beta_0(s)t_0+\beta_1(s)t_1\bigr)e_y.
\tag{3}
$$

原端轴输入在 phi=0 为

$$
Q^{\rm end}_0=m_0[e_z]_\times G^{-1},\qquad
Q^{\rm end}_1=-m_1[e_x]_\times G^{-1},
$$

$$
G^{-1}=\operatorname{diag}
\left(m_0^{-2},(m_0^2+m_1^2)^{-1},m_1^{-2}\right),
\quad m_i=\int\beta_i>0.
$$

在同一 z_y=0 平面，其两角为 t0=z_x/m0、t1=z_z/m1，也独立遍历整个实平面。因此得到准确结论：

**不限制校正坐标球时，原端轴 Q 和已冻结 moment-Q 在 phi=0 的反射平面分支给出完全相同的两独立 bubble Ry 修正子午线族。** 两者只是以不同可逆二乘二矩阵描述这同一族。对相应配对的控制，T(s,0)、由同 cap 径向积分得到的 F(s,0) 及其径向导数相同。

声明半径 r 的数值搜索球经 L 映成不同椭圆，所以有限球内的可搜索部分不一定相同。这个恒等式也没有比较角一、二导数，更没有说全角面的两种参数化相同；角导数取决于邻近角度的实际根分支。

## 3. 平面端点方程的完整形式

令 f(s)=beta_0(s)t0+beta_1(s)t1。采用世界正 y 轴旋转，准确修正切向量为

$$
\widehat T(s,0)=
\left(b\cos f+c\sin f,\ 0,\ c\cos f-b\sin f\right).
\tag{4}
$$

闭合的两个独立端点式为

$$
\begin{aligned}
C_x(t_0,t_1)&=p(0)-R+
 \int_0^S(b\cos f+c\sin f)\,ds=0,\\
C_z(t_0,t_1)&=-H+
 \int_0^S(c\cos f-b\sin f)\,ds=0.
\end{aligned}
\tag{5}
$$

C_y 在该对称子空间恒为零，不能把它当成第三个独立平面方程。原始零校正的准确缺陷为

$$
C_x(0,0)=p(0)-1,\qquad C_z(0,0)=I_*-H,
\quad I_*=\int_0^S c(s)\,ds,
\tag{6}
$$

其中用了 a(0)=1、a(S)=R。因此 H 只直接改变 (5) 的竖直目标，不会消掉水平 p(0)−1。工作 normalized-c、Gauss、求和及 scalar carrier 的费用没有在 (4)–(6) 中被冒称为零。

同一结论在其它反射轴的相应局部 (er,et,ez) 基下成立；这里的证明和已列参数不需要增加一次角样本或积分。

## 4. 为什么原六轴释放仍不扩大这个对称平面族

考虑把两 bubble 的 world 轴控制完全释放成 a0、a1∈R³：

$$
\widehat T=exp\left([\beta_0a_0+\beta_1a_1]_\times\right)T_0.
$$

本结论的前提是**保持原表示对控制的反射协变**。对 y 反射 S=diag(1,−1,1)，旋转向量是轴向量，所以

$$
a_i(-\phi)=\det(S)S a_i(\phi)
=\operatorname{diag}(-1,1,-1)a_i(\phi).
$$

在 phi=0 固定点必有 a_i=(0,t_i,0)。因而这种六轴释放在该反射平面仍只有两个独立 Ry 角，还是 (3)–(5) 的同一族。它可改变一般角度的控制余量，但不能仅凭“六变量多于三变量”宣称解决这个轴端的两角可达问题。

这里没有反向声称“某个输出恰巧在 xz 平面就必然每个旋转控制沿 ey”：旋转冗余或特殊退化表示可能使那种无条件反推不成立。本条只使用原构造的明确控制协变；若新方法放弃此协变，就须重新支付全角反射接合责任。

若在轴端直接把变量限制到对称子空间，应只解 (5) 的两个独立式。若用完整六轴和三端点式再用对称不变的唯一局部根/极小点选支，则须在完整空间另核其 Jacobian/KKT 非奇异，并由唯一性推出协变，不能对已经删去横向变量的平面系统仍套用 rank=3。

## 5. 一般角度的区别与本结论的实际用途

在一般 phi，Q_i(phi)=Rz(theta0)Q_i(0)Rz(theta0)^T，而 core 的位移通常含相对 er(theta0) 的切向分量。所需 z_t 因而未必为零，(1) 的平面化简不再覆盖完整端点问题。

也不存在一个共同可逆三乘三线性变换 A，使全矩阵 W_moment=W_end A：两个独立 bubble 的系数必须分别满足 Q_i^moment=Q_i^end A；但旧 Q0^end 的第三行恒零，新 Q0^moment 的第三行第二列 D0=0x1.956cca02ca83bp-3 非零，已直接矛盾。这个判断只排除了完整控制场的共同线性重参数化，不额外宣称所有可能的物理输出像之间的关系。

实际 [阶段15（03b 第4卷）](../notes/2026-11-26-public-actions-45820592817-1-part-004.md) 和 [阶段19（第5卷）](../notes/2026-11-26-public-actions-45820592817-1-part-005.md) 都在首八角中的索引5报告同方程回溯未下降；索引5不是 phi=0。阶段15还实际返回小的数值 Cz 最小奇异值和仍在球内的最后候选。这是研究附近控制映射转折的数值动机，不是由本轴端恒等式证明实际索引5无根，也不是已证发生严格 fold。

同一 [第5卷的阶段23](../notes/2026-11-26-public-actions-45820592817-1-part-005.md) 已让原 H 通过完整全角、完整两支撑补集的单位速必要条件。阶段21的 Istar 工作字与原 H 只在末字不同，且算法求和路径不同；本文不由此推断必须降低 H。

有针对性的后继应区别三件事：同一两角方程换坐标、同一方程改变找根路径、以及真正加入与 beta0/beta1 不线性相关的新径向控制形状。前两者不能扩大 (5) 的完整平面可达像。第三者可以扩大控制函数空间，但仍须另证或实际找到闭合根，并支付全角平滑、完整隐式导数及几何责任。
