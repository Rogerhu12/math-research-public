# 新输入：三对普通权的完整出生二 S1/S2

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：本篇固定新原输入、完整来源与判定条件；尚未收到该源的实际运行结果，不声称正性。

## 1. 整个物理对象及真正未闭块

取六位权
$$
(\sqrt x,\sqrt x,\sqrt y,\sqrt y,1,1),\qquad x,y>0.
$$
完整上来源为 $K_2$，维数九；低来源为 $K_1$，维数五。
每个二位等权组有长度二的出生零串，以及长度零的出生一 singlet。

全部原正交块为：

| 组内出生数 | 上相对出生 | 上来源总维数 | 下相对出生 | 下来源总维数 |
|---|---:|---:|---:|---:|
| 零个 singlet | $2$ | $3$ | $1$ | $2$ |
| 一个 singlet | $1$ | $3$ | $0$ | $3$ |
| 两个 singlet | $0$ | $3$ | 无 | $0$ |

这些块同时约化删除、creation、三次下降、完整 Gram、完整逆与 primitive 压缩。
一个 singlet 的块由[任意正权出生一 S1](../results/R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)
及[实际出生一 S2](../results/R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)支付。
两个 singlet 的块桥为零，退化为真空 Newton。
所以新目标恰是三组都取长度二时的同一个三维上源、二维低源；
不能仅证某一条上源或把它错当整个九维。

旧两组加一位的 S1/S2 定理不直接覆盖三个各二位的权组。
旧两组加两异常位的出生二普通首边，也没有把上源创新 S1 作为结论给出。
本输入不重算那些已登记的普通相邻比较。

## 2. 完整物理计数核与固定 primitive 源

在三个组的聚合坐标中，合法占据为
$$
I=(i,j,k)\in\{0,1,2\}^3,\qquad |I|=r,
$$
物理权为
$$
p_I=\binom2i\binom2j\binom2k x^iy^j .
$$
聚合系数的实际范数为 $\sum_I|g_I|^2/p_I$。
删除变成 $\partial_X+\partial_Y+\partial_Z$，除阶幂的完整 incidence 是
$$
(v_I)_O=\prod_{\nu=1}^3\binom{I_\nu}{O_\nu}.
$$
使用整个合法输入层，定义
$$
\mathcal F_{r,j}=\sum_{|I|=r+j}p_Iv_Iv_I^*.
\tag{2.1}
$$
低出生完整层维数三，高出生完整层维数六。
它们与普通欧氏 Gram 的区别已包含在 $p_I$ 内。

两个固定源矩阵分别是下列多项式的系数列：
$$
E_1=(X-Z,\ Y-Z),
$$
$$
E_2=((X-Z)^2,\ (X-Z)(Y-Z),\ (Y-Z)^2).
\tag{2.2}
$$
它们分别穷尽三维、六维完整层中的 primitive 核。
定义真实源度量和全部低来源
$$
U_0=E_2^*P_2^{-1}E_2,\qquad
\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,\quad j=0,1,2,3.
\tag{2.3}
$$
$j=0$ 时 $\mathcal F_{1,0}=P_1$。
所有非零高度均先求完整三维逆，再压到二维源；
不取压缩矩阵的普通逆替代它。

真实三次桥及深桥为
$$
B_0=
\begin{pmatrix}
2(x-1)&y-1&0\\
0&x-1&2(y-1)
\end{pmatrix},
$$
$$
Y_0=2\bigl((x-1)^2,\ (x-1)(y-1),\ (y-1)^2\bigr).
\tag{2.4}
$$
它们直接来自 $x\partial_X+y\partial_Y+\partial_Z$，
不是按非正交源坐标取普通转置猜出的伴随。
深真空第四 Gram 是 $e_4^{-1}$，其中
$e_4=\sum_{|I|=4}p_I>0$。

## 3. 一次完整 S1 的原三塔消元

令 $S=2x+2y+2$，并保留同一物理源，置
$$
\widehat H=E_2^*P_2^{-1}
\operatorname{diag}\bigl(S-2(ix+jy+k)\bigr)E_2,
$$
$$
\widehat F_2=E_2^*P_2^{-1}\mathcal F_{2,2}P_2^{-1}E_2,
$$
$$
M=B_0^*\Lambda_2B_0,\qquad
N=B_0^*\Lambda_2\Lambda_3^{-1}\Lambda_2B_0.
$$
[原完整三塔身份](../results/R288-appendix-general-birth-three-tower-s1-schur-cancellation.md) §6 给精确二次型
$$
\boxed{
\mathcal E_1
=\widehat H U_0^{-1}\widehat H-\widehat F_2
-MU_0^{-1}M+2N+\frac{Y_0^*Y_0}{4e_4}.
}
\tag{3.1}
$$
它等于原 $C_1^2-C_2-\Delta L_3^{-1}\Delta^*$ 在同一源上的形式。
$\widehat F_2$ 是完整第二物理 Gram 的直接压缩，绝非第二最小逆 Gram 的逆。
本式完整保留深真空塔，因此不需要重新求六维上第二 Gram 的逆。

## 4. 同源完整 S2 及两个交叉

原两塔身份给
$$
C=\widehat H-M=U_0H_1^{-1}U_0>0,
$$
其中 $H_1=E_2^*\mathcal F_{2,1}^{-1}E_2$ 是真实完整上最小逆形式。
令
$$
Y=U_0^{-1}B_0^*\Lambda_2,\quad
Z=B_0^*\Lambda_2\Lambda_3^{-1}\Lambda_2,\quad
D=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
$$
同一低源中的准确 S2 缺陷为
$$
\boxed{
\mathcal E_2
=D-\frac14(CY+Z)^*C^{-1}(CY+Z).
}
\tag{4.1}
$$
$C^{-1}$ 在整个三维上源上取，两个 cross 都保留；
没有用迹、单列界或任意低源替换它。

## 5. 唯一新参数域与完整判定

三个二位组可置换，全部物理权可共同缩放。
因此不损失任何正权模型，可令 $x\ge y\ge1$，写
$$
x=1+U+V,\qquad y=1+V,\qquad U,V\ge0.
\tag{5.1}
$$
所有实际物理核、源度量及必要的完整逆在整个闭象限严格正定。
最终已约分分母只含这些已知非零分母的因子，
故在连通域中不变号，并可在 $(U,V)=(0,0)$ 准确定号。

[新可读源](2026-11-28-three-pairs-original-joint-three-tower-8542.py)
直接生成 (2.1)–(2.4)，精确核对 primitive 方程及原三次桥，
构造 (3.1) 与 (4.1)，并分别检查全部三个和两个前导主子式。
若每个准确定号分子的全部系数非负且常数项严格正，
则两个完整矩阵在整个域严格正；反之源只报告未闭，负系数不是反例。
源完整返回 S1_all_passed、S2_all_passed 两个不同状态，
不得把任一中途逆、局部系数或外层绿色状态当作两者已证。

源自身设 180 秒报警和 4 GiB 地址空间界。
只打印小阶段摘要、系数项数/次数/符号计数和摘要哈希；
不输出矩阵数据、编码载荷或可重算结果文件。
本篇记录输入，不记录尚未发生的执行。

若此唯一实际计算完整支付两式，则 §1 的正交直和支付整个六位来源；
再合已付六位低出生一内部 half 和 R275，
可给七位 $(a,\sqrt x,\sqrt x,\sqrt y,\sqrt y,1,1)$ 的整个出生二首边。
这条后续蕴含仍以两式全部完成为前提，
不提前声称结果，更不外推普通 ISP 或无限 $N=M$。
