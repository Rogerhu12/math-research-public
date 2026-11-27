# R271 新输入：两对等权与两个独立权的完整联合来源

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：下面的原来源身份与覆盖已支付；新的七个正性判据尚未实际执行。
- 唯一可读源：[完整三塔与双交叉](2026-11-28-two-pairs-two-independent-original-joint-three-tower-8542.py)，Git blob 31fc1f24557da7073b58e67a6cda4bc50365adf6。
- 首次数学资源界：180 秒、4 GiB。仅打印小状态、项数、符号与 SHA；不导出展开矩阵、数据文件或编码载荷。

## 1. 新目标及与既有首边的区别

取六位物理权
$$
b=(\sqrt x,\sqrt x,\sqrt y,\sqrt z,1,1),\qquad x,y,z>0.
$$
目标是原整个九维出生二 $K$ 和五维出生一 $L$ 的两项联合来源：
$$
F-\Delta L_3^{-1}\Delta^*>0,\qquad
I_L-A^*G_1A-L_1L_2^{-1}L_1>0.
\tag{1.1}
$$
这里保留 R275 原定义
$$
C_i=G_i^{-1},\quad F=C_1^2-C_2,\quad
B=d_{b^3}|_K,
$$
$$
\Delta=(C_1B^*L_3-B^*L_2)/2,\qquad
A=(C_1B^*L_2+B^*L_2L_3^{-1}L_2)/2.
$$
所有伴随和完整 MP 均取原物理内积。

[旧 R292](../results/R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)
已经给这个六位族的普通首边；本输入不重证那条结论。
它检验的是这个六位族自身作为再加一位的完整旧上/下来源时所需的 (1.1)。
若二者均完整支付，再合已刊六位低出生一内部 half，
R275 才能给一般五种权值的
$(a,\sqrt x,\sqrt x,\sqrt y,\sqrt z,1,1)$ 七位新首边。
倒数权后同一族封闭，可以再付该七位出生二的末边。
这些后果目前只是条件性的，不据源码已经存在就登记为定理。

这也是不同于已冻结六个独立权特征门的新有限输入：
这里只处理两个真实二位对称组，使用原四维/三维共同源，
并直接处理 S1/S2，没有重跑旧五维 $I-2K$ 特征或假 quarter-trace 门。

## 2. 全部物理块，无遗漏低来源

两个二位等权组各有长度二对称串与出生一 singlet，
两个单独位各为长度一串。共同约化分块为：

| 二位组的 singlet 数 | 上相对出生与维数 | 下相对出生与维数 |
|---|---|---|
| $0$ | 出生二，$4$ 维 | 出生一，$3$ 维 |
| $1$，两个选择 | 出生一，各 $2$ 维 | 真空，各 $1$ 维 |
| $2$ | 真空，$1$ 维 | 无 |

一个 singlet 的块是余下四个物理位的出生一共同约化部分。
[全部正权出生一 S1](../results/R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)
和[全部正权出生一 S2](../results/R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)
已支付它们。
两个 singlet 的块只余两个不同正权的真空，桥为零；
其 $F=(y+z)^2-yz=y^2+yz+z^2>0$。

故新任务只余同一个四维上源和三维低源，
但其完成后的结论会按真正正交直和返回全部九维/五维。
不把未约化试源或单条上升塔当作完整核。

## 3. 旧八维聚合来源的实际原式

采用 [R273 八维完整物理核](../results/R273-appendix-eight-dimensional-aggregate-polynomial-gram.md)
的原固定来源，组容量为
$$
c=(2,1,1,2),\qquad I=(i,j,k,\ell),\qquad
p_I=\binom2i\binom2\ell x^iy^jz^k .
$$
聚合坐标的物理范数为 $\sum |g_I|^2/p_I$。
令
$$
(v_I)_O=\prod_{\nu=1}^4\binom{I_\nu}{O_\nu},\qquad
\mathcal F_{r,j}=\sum_{|I|=r+j}p_Iv_Iv_I^*.
\tag{3.1}
$$
求和保所有合法输入，各个非零高度均先在完整物理层取逆。

写 $A_0=X-J,\ B_0=Y-J,\ C_0=Z-J$。源列为
$$
E_1=(A_0,B_0,C_0),\qquad
E_2=(A_0^2,A_0B_0,A_0C_0,B_0C_0).
\tag{3.2}
$$
它们分别穷尽四维一层内的三维核及八维二层内的四维核。
令
$$
U_0=E_2^*P_2^{-1}E_2,\qquad
\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,\quad j=0,1,2,3.
$$
$j=0$ 时 $\mathcal F_{1,0}=P_1$。

三次下降在此为
$x\partial_X+y\partial_Y+z\partial_Z+\partial_J$。
其真实两次来源为
$$
K_B=
\begin{pmatrix}
2(x-1)&y-1&z-1&0\\
0&x-1&0&z-1\\
0&0&x-1&y-1
\end{pmatrix},
$$
$$
K_Y=2((x-1)^2,(x-1)(y-1),(x-1)(z-1),(y-1)(z-1)).
\tag{3.3}
$$
源码在全四维/八维层逐项核 primitive 方程、
第一次桥 $d_{b^3}E_2=E_1K_B$，
以及连续第二次桥到真空的 (3.3)；
没有只检查列维数。

## 4. 新原 S1/S2 矩阵

置 $S=2x+y+z+2$，
$$
\widehat H=E_2^*P_2^{-1}
 \operatorname{diag}(S-2(ix+jy+kz+\ell))E_2,
$$
$$
\widehat F_2=E_2^*P_2^{-1}\mathcal F_{2,2}P_2^{-1}E_2,\quad
M=K_B^*\Lambda_2K_B,\quad
N=K_B^*\Lambda_2\Lambda_3^{-1}\Lambda_2K_B .
$$
原第四真空系数 $e_4=\sum_{|I|=4}p_I>0$。
[R288 全三塔身份](../results/R288-appendix-general-birth-three-tower-s1-schur-cancellation.md) §6 准确给
$$
\mathcal E_1=
\widehat H U_0^{-1}\widehat H-\widehat F_2
-MU_0^{-1}M+2N+K_Y^*K_Y/(4e_4).
\tag{4.1}
$$
它是原 S1 在同一四维物理源上的二次型。
末项是真正深塔，$U_0^{-1}$ 是同一源度量，
$\widehat F_2$ 不是 $G_2^{-1}$。

同一原两塔身份给
$$
C=\widehat H-M=U_0H_1^{-1}U_0>0,\qquad
H_1=E_2^*\mathcal F_{2,1}^{-1}E_2.
$$
定义
$$
Y=U_0^{-1}K_B^*\Lambda_2,\quad
Z=K_B^*\Lambda_2\Lambda_3^{-1}\Lambda_2,\quad
D=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1 .
$$
原三维低源上的 S2 缺陷准确为
$$
\mathcal E_2=D-\frac14(CY+Z)^*C^{-1}(CY+Z).
\tag{4.2}
$$
这里在完整四维上源取 $C^{-1}$，两项 cross 全保。
并没有从旧普通首边推新联合来源。

## 5. 全参数覆盖与准确正性判据

交换两个二位组并共同缩放，可以取 $x\ge1$；
再交换两个单独位，可取 $y\ge z>0$。
因此下式覆盖全部原正权模型：
$$
x=1+U,\qquad y=V+W,\qquad z=W,
\qquad U,V\ge0,\ W>0.
\tag{5.1}
$$
这不是只取两个独立权也大于一的较小域。

所有原完整层 Gram、源度量和所需压缩 Gram 在此连通域严格正定。
中间所有分母是这些非零物理因子的积，约分后的分母也不消失；
其符号由 $(U,V,W)=(0,0,1)$ 定向。

源码将对 (4.1) 的四个和 (4.2) 的三个前导主子式逐一作完整计算。
准确定号后的分子只有满足以下两点，才判定该主子式已证明严格正：

1. 全部有理系数非负；
2. 至少有一个不含 $U,V$ 的正系数 $W^j$。

第二点在每个 $W>0$ 给严格正，故也支付 $U=0$ 或 $V=0$ 的重复权边界；
不能以 $U=V=W=0$ 的常数项代替，因为该点不是原正权域。

全部七项通过才可合 Sylvester 判据、§2 的真实直和，
得到整个物理模型的 (1.1)。
负系数、部分返回、外层绿色或超时都不构成原 S1/S2 的反例或证明。
本输入只留可读源码、原紧凑定义及实际小回执；
不传输或入库展开参数。