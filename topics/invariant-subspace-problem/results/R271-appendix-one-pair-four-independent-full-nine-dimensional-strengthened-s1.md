# R271 附录：一对等权加四个独立正权的完整九维 S1

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

**状态：以下完整原 S1 已证明。** 原三维共同因子块由先前定理支付；
本次在其原 Schur 商上取得全部三个严格谱系数，覆盖全部五个闭权序域和所有重复权。
只执行了新三叶 companion 输入一次，没有重放已冻结的原第四主子式资源门。

## 1. 原物理结论

设六个物理权为
$$
(\sqrt{x_1},\sqrt{x_2},\sqrt{x_3},\sqrt{x_4},1,1),
\qquad x_i>0.
\tag{1}
$$
共同缩放和置换因此覆盖任意含一对等权的六位正权输入。
沿用 [R288 完整三塔](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md)
的同一个原来源、完整 Moore--Penrose 逆和物理伴随，记
$$
U=K_2=\ker d\cap\mathcal H_2,\quad L=K_1,\quad
F=C_1^2-C_2,\qquad
\Delta=\frac12(C_1B^*L_3-B^*L_2).
$$
则在整个九维 $U$ 上严格有
$$
\boxed{F-\Delta L_3^{-1}\Delta^*>0.}
\tag{2}
$$
这里的下来源是整个五维 $L$，没有删掉任一 lower primitive 方向。

因创新项非负，(2) 同时给 $F>0$，即该原模型的严格普通首边。
每个固定正权点都有
$$
0\le
\left\|F^{-1/2}\Delta L_3^{-1}\Delta^*F^{-1/2}\right\|<1.
\tag{3}
$$
本文没有给跨全部正权点的一致小于一常数。

## 2. 全部约化分量和原六维形式

只交换最后两个等权位作正交分解。
对称部分完整物理一孔、二孔层维数分别为 $5,11$，
其 lower、upper primitive 维数为 $4,6$。
反对称部分是该对的真正 singlet，余四位保持原独立正权，
对应真空及出生一，维数为 $1,3$。
所以
$$
\dim L=4+1=5,\qquad \dim U=6+3=9.
\tag{4}
$$
这些空间同时约化原删除、创建、完整逆和两次 cubic 桥。
反对称三维部分的 (2) 已由
[R288 任意权出生一 S1](R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)
支付；新增工作完全针对同一个对称六维部分。

用容量 $(1,1,1,1,2)$ 的相似系数坐标，令 $J$ 为 pair 变量。
完整两组 primitive 来源是
$$
E_1=(X_i-J)_{i=1}^4,\qquad
E_2=((X_i-J)(X_j-J))_{i<j}.
$$
对容量合法多指标 $I=(i_1,\ldots,i_4,j)$，
原物理度量为
$$
p_I=\binom2j\prod_{\nu=1}^4x_\nu^{i_\nu},
\qquad \|g\|^2=\sum_I|g_I|^2/p_I.
\tag{5}
$$
[原来源全文](../notes/2026-11-28-one-pair-four-independent-original-s1-8542.md)
给完整物理 Gram $\mathcal F_{r,j}$ 和同源矩阵
$$
\Lambda_j=E_1^{\mathsf t}\mathcal F_{1,j}^{-1}E_1,\quad
U_0=E_2^{\mathsf t}P_2^{-1}E_2,\quad
M_2=K_B^{\mathsf t}\Lambda_2K_B,
$$
$$
N_2=K_B^{\mathsf t}\Lambda_2\Lambda_3^{-1}\Lambda_2K_B.
$$
所有 $\mathcal F_{1,j}^{-1}$ 都先在整个五维物理层取逆，再压缩。
在这组非正交来源上，(2) 准确表示为
$$
\mathcal E=
\widehat H U_0^{-1}\widehat H-\widehat F_2
-M_2U_0^{-1}M_2+2N_2+\frac{K_Y^{\mathsf t}K_Y}{4e_4}.
\tag{6}
$$
$\widehat H$ 是原占据算子的源形式，$\widehat F_2$ 是完整第二 creation Gram，
$K_B,K_Y$ 是同一来源的两次真实 cubic 桥。
(6) 保全部交叉项、两个 $U_0^{-1}$ 和第四阶真空量，未换成 Euclidean 系数模型。

## 3. 已付三维块与本次真正的新 Schur 目标

置换前四位，可设 $x_1\ge x_2\ge x_3\ge x_4>0$。
按来源
$$
S_i=(X_1-J)(X_i-J),\quad i=2,3,4,
$$
$$
Q_i=(X_j-J)(X_k-J),\quad
\{i,j,k\}=\{2,3,4\}
$$
将原六维形式写为
$$
\mathcal E=\begin{pmatrix}A&C\\C^{\mathsf t}&D\end{pmatrix}.
$$
[共同因子三来源定理](R271-appendix-one-pair-four-independent-common-factor-three-source-s1-block.md)
已证明全部正权处 $A>0$。
令 $G$ 为三列 $Q_i$ 的原物理 Gram，故同样在全部正权处 $G>0$。
本次目标从始至终是
$$
S=D-C^{\mathsf t}A^{-1}C,\qquad
\frac{\det(tG+S)}{\det G}
=t^3+c_1t^2+c_2t+c_3.
\tag{7}
$$
没有重算 $A$ 的正性，也没有把原第四主子式简单换次序重跑。

[三叶原来源与碰撞证明](../notes/2026-11-28-one-pair-four-independent-s1-three-leaf-companion-schur-8542.md)
完整给出此计算的实际物理映射。
为说明三个系数的来源，记
$$
a=x_1,\quad(z_1,z_2,z_3)=(x_2,x_3,x_4),\quad
s=\sum z_i,\ p=\sum_{i<j}z_iz_j,\ q=z_1z_2z_3.
$$
互异叶权上使用 $V_{ik}=z_i^k$ 和三根乘法 companion。
一孔、二孔叶度量分别是
$$
H_{-1}=(\sum_\nu z_\nu^{i+j-1})_{i,j=0}^2,\qquad
H_1/q=(\sum_\nu z_\nu^{i+j+1}/q)_{i,j=0}^2.
$$
完整物理层维数保持 $1,5,11,14,11,5,1$。
源码实际核验两个 primitive 身份、两次 cubic 桥、完整五维两逆、
原四维 $\Lambda_3$ 逆、六维 $U_0$ 逆和原真空 $e_4$。

对六个源的变化正是 $\operatorname{diag}(V,V)$ 同余，因此
$$
\widetilde S=V^{\mathsf t}SV,\qquad \widetilde G=V^{\mathsf t}GV,
$$
$$
\frac{\det(t\widetilde G+\widetilde S)}{\det\widetilde G}
=\frac{(\det V)^2\det(tG+S)}{(\det V)^2\det G}.
\tag{8}
$$
Vandermonde 平方完整消去。重复权处不把退化 $V$ 或 Hankel 矩阵当成基底：
(7) 的原 $A,G$ 和全部原物理 Gram 均严格正、连续。
对称化原正分母后，约简的 $c_i(a,s,p,q)$ 在整个原正域无极点；
于是 (8) 给原连续三个系数的准确延拓。

## 4. 唯一首次精确返回与十五个闭域证书

唯一执行的可读来源是
[三叶 companion 精确源](../notes/2026-11-28-one-pair-four-independent-s1-three-leaf-companion-schur-8542.py)，
Git blob 7ed6dd024e44427cc3b117f39e81737342797b0b。
[实际小回执](../notes/2026-11-28-one-pair-four-independent-full-s1-schur-spectrum-receipt-8542.json)
保留完整来源定位、阶段、十五项摘要及哈希，不保存扩展系数数据。

实际 run 46080372041 / job 140777712507，
内层用时 57.527394568 秒、最高 165024 KiB、退出码 $0$。
原完整矩阵在 1.178247009 秒返回，
原剩余 Schur 和原三角来源度量在 16.089495317 秒返回。
全部三个系数于 57.443005924 秒完成，不以外层绿色代替数学结果。

三个约简分子的精确参数为：

| 系数 | 普通次数 | 权次 $(1,1,2,3)$ | 项数 | 所有域的严格正常数 |
|---|---:|---:|---:|---:|
| $c_1$ | 26 | 39 | 8965 | 154279448064000 |
| $c_2$ | 25 | 38 | 8764 | 352638738432000 |
| $c_3$ | 24 | 37 | 7794 | 261213880320000 |

每个约简分母为 7792 项，在全等正权 $(a,s,p,q)=(1,3,3,1)$
的同向值均为 22039921152000；原无极点论证支付其全域符号。
不根据这一个取值假设分母处处正。

五域使用
$$
v_0=1,\quad v_1=1+A,\quad v_2=1+A+B,\quad
v_3=1+A+B+C,\quad v_4=1+A+B+C+D,
$$
其中 $A,B,C,D\ge0$，pair 位于 $k\in\{0,\ldots,4\}$，
其平方权 $\tau=v_k$。
将另外四值按降序写为 $s_1,s_2,s_3,s_4$，并代入
$$
a=s_1/\tau,\quad
s=(s_2+s_3+s_4)/\tau,\quad
p=(s_2s_3+s_2s_4+s_3s_4)/\tau^2,\quad
q=s_2s_3s_4/\tau^3.
\tag{9}
$$
使用权次 $(1,1,2,3)$ 齐次化，乘的只是正数 $\tau^d$。
这些闭域覆盖全部正权和全部碰撞。

十五个实际展开均无负系数，且分别有上表的严格正常数；
本次不需要任何平方消项。各域的项数如下：

| pair 位置 $k$ | $c_1$ 分子 | $c_2$ 分子 | $c_3$ 分子 |
|---:|---:|---:|---:|
| 0 | 93585 | 86955 | 78574 |
| 1 | 93517 | 86955 | 78574 |
| 2 | 100362 | 91199 | 82042 |
| 3 | 107450 | 98319 | 88774 |
| 4 | 121775 | 110355 | 98225 |

每一项都实际完成全多项式返回核对，负系数数为 $0$，
平方项数为 $0$，保留正常数。
因此 $c_1,c_2,c_3>0$ 在所有闭域成立，包括每个零差变量边界。

## 5. 原广义谱的严格收尾

原 $G>0$、$S=S^{\mathsf t}$，所以 $G^{-1}S$ 相似于真实 Hermitian 矩阵
$G^{-1/2}SG^{-1/2}$，全部特征值为实数。
已经证明
$$
t^3+c_1t^2+c_2t+c_3>0\qquad(t\ge0).
$$
若某个原广义特征值 $\lambda\le0$，在 $t=-\lambda$ 会给 (7) 零点，矛盾。
故 $S>0$。
合原 $A>0$，真实 Schur 恒等式给 $\mathcal E>0$。
再加 §2 已付的三维 singlet 部分，得到完整九维 (2)。

这里的严格性在重权处由原系数的严格证书直接支付，
没有把互异域正性经连续性所得的半正偷换为正定。

令 $E=F-\Delta L_3^{-1}\Delta^*$。
既然 $E>0$ 且 $F=E+\Delta L_3^{-1}\Delta^*>0$，
有限维相对正度量的最小特征值
$\varepsilon(x)=\lambda_{\min}(F^{-1/2}EF^{-1/2})$ 严格正，
于是 (3) 的准确上界是 $1-\varepsilon(x)<1$。

完整 S2 仍需保整个低来源及其另一个原 Schur 预算。
本文不据 (2) 自动宣布新增七位联合首末边，
也不证明原 $W$ 的来源费用、$K_\infty=M$ 或 $N=M$。
