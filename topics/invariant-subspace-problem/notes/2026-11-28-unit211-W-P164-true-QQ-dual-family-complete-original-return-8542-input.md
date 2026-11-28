# R150：真正 QQ(k) 原双数族与泛型 D 返回的新输入

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。尚未执行。180 秒 / 4 GiB。

## 1. 已完成上界与这次唯一新目标

此前完整 1164 维 A 环境保留全部 I11；七个 primary 已单位，另外两完整 24×264 原矩阵均秩 22。因此

$$
\dim_{\mathbf Q(k)}\mathcal M_{\mathbf Q(k)}\le4.
\tag{1}
$$

这是有限 A 模的真实 Nakayama 上界。两个模商中 lambda−1/2 均非零而平方零；不能只构造两个约化点，也不能由模 D=0 直接提升 QQ。

这次唯一目标是在 QQ(k) 上构造真正四维的同原理想族，并返回原模型到它的满射。由 (1) 和这个独立四维下界，才可推出同构和真正 QQ 上的 D=0。没有重跑旧 primary、P determinant、QQ 特征系数或参数范数。

## 2. 完整二次权代数与双数方向

令 F=QQ(k)，定义

$$
E=F[e]\big/\left(
e^2-\frac{k^2+4k+8}{4k}e-\frac{k^2+6k+8}{4k}
\right),\qquad
S=E[\epsilon]/(\epsilon^2).
\tag{2}
$$

E 是完整首一二次代数，不预设为域或先取一个根。S 在 F 上有真实自由基

$$
1,\ e,\ \epsilon,\ e\epsilon.
\tag{3}
$$

对 E 中 v=a+be，记

$$
r_1=(k^2+4k+8)/(4k),\qquad r_0=(k^2+6k+8)/(4k).
$$

所有需要的逆只用整个二次代数的乘法范数：

$$
N(v)=a^2+r_1ab-r_0b^2,\qquad
v^{-1}=\frac{a+r_1b-be}{N(v)}.
\tag{4}
$$

只有 N(v) 是 F 的非零元素，才使用 (4)，并实际检查两个乘积都等于 1。任何所需非单位都明确报出并停止该满射宣称，不改成选择一个好分量。

## 3. 显式原几何族

在 (2) 中设

$$
u=e+1,\quad Q=ek,\quad
\ell=\frac{(e+1)((k+2)^2-2ek)}{k((e+1)k+2)}=\tfrac12,
$$

$$
\lambda=\tfrac12+\epsilon,\qquad T=-\tfrac12,
$$

$$
x=\tfrac12+2(1-e)\epsilon,\quad
y=\tfrac12,\quad t=0,\quad
f=\frac{e+1}{2}-(e-1)\epsilon.
\tag{5}
$$

权等式由完整 Lhalf 关系给出。ellhalf 下准确恒等

$$
P_{02}=(2-u)T_0,\qquad T_0-J+Q=0.
\tag{6}
$$

(6) 连同原 E0/N0/P1 恢复式使原 f、lambda、T 分别等于 (5)，源码逐式返回。

原 rho 二次扩张仍满足 rho²=1−Q，p=1+rho、q=1−rho。原 Gram 变成

$$
\begin{pmatrix}
0&0&p&q\\
0&0&r&r\\
p&r&0&0\\
q&r&0&0
\end{pmatrix},
\qquad r=2(2-u)\epsilon,\quad r^2=0.
\tag{7}
$$

(7) 只是说明原输入变小；实际源码使用已经发表的完整原 Gram 多项式，逐个返回 E1、EBe、EBo、N1、NS、PS 在 S 的全部四个 F 坐标为零。没有用均值的必要条件替代 NS/PS，也没有只取零阶点。

## 4. 与原有限模型的系数环和首一关系对接

源码从此前原完整值源只读 5551 字节必要定义前缀，取得原 N1 行、纯权斜率行列式、qZ 和所有原坐标；不运行旧十行、二十行、cofactor 或 determinant 尾段。

原模型采用的 pure-weight 分母有两类。

第一类是原 native P 和 chi 证书的完整已付权原子。源码完整取原列表 e、k、u、ek−1、(e+1)k+2、k+4、P02 分子、M 分子，加 k+1、k+2、旧 H、整 C9、整 J19；它们在 E 中逐个按 (4) 真逆并乘回。这支付 P 属于 I6、chi 属于 I4 的既有原身份在该族上的系数；不以只是“当前物理非零”代替这个检查。

第二类是实际原 N1、qZ、原值系数及坐标恢复的分母。源码对每个完整分母求整个 E 的真逆，尤其检查纯权 DeltaN 的真逆。所有分母均只含权，完全不倒 D、epsilon 或 lambda 的几何首项。

因此已刊原理想身份严格给出

$$
P|_S=0,\qquad \chi_6(\lambda)|_S=0.
\tag{8}
$$

它们通过已有完整原来源和本次真权逆下降，不重新计算旧 P 或 chi 系数。qZ 则还由新代入直接实际返回：

$$
z=ax+cy,\quad
x=(p_2z+cp_0)/\Delta_N,\quad
y=(-p_1z-ap_0)/\Delta_N,\quad
q_z(\lambda,z)=0.
\tag{9}
$$

两向原坐标全部实际乘回。这个 z 是原模型同一个值，不是独立引入另一个根。

## 5. 全部五条 D 清分母原值

令

$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell TA_2+2T^3.
$$

式 (5) 与 epsilon²=0 给出真正 QQ 上的 D=K=0。源码同时按原公式完整形成 qT4、R6、Nlow、Plow、Vlow；原 NB/PB 奇部以及整个 N4(V) 的三个系数也取自原 Gram，并检查它们在这个系数环中有定义。

五式每一项都含 D 或 K，故全部返回零。这里得到的是之前定义的辅助 I11，不声称 D=0 点满足已经要求 D 非零的物理原图，也不把清分母公式在 D0 外推为全部个别值的充分条件。

## 6. 若完整返回，如何合法得到 QQ 泛型原结论

由 (8)、(9)、全部 I11 以及实际系数逆，可得原有限模型的同态

$$
\mathcal M_F\longrightarrow S.
\tag{10}
$$

因为 e 和 lambda−1/2 的像就是 e、epsilon，它们产生 (3) 的全部四个基元，故 (10) 满射。S 的 F 维数恰为 4，而 (1) 给出来源维数至多 4。因此 (10) 是 F 代数同构。

只有在这一步，才能严格推出原辅助商中的 D 真为零。因此其 D 非零局部化为零，即当前 H198 补图的 QQ(k) 泛型物理原系统排空。不是由模 D0 得到这一结论。

已刊真 P 没有未付竖直分量，H198=0 与 P 的交已独立有限。若上述新同构全部实际完成，则泛型物理空意味着有非零纯 k 多项式支撑剩余有限 k 纤维；结合无竖直分量可推出整个当前 W 物理权支持零维。这里没有显式 k 覆盖或新数值点数界，也不宣称所有有限纤维已排尽。

## 7. 冻结源和依赖

新源：

2026-11-28-unit211-W-P164-true-QQ-dual-family-complete-original-return-8542.py

SHA-256：529eb09a14f050f9cb086a1f42d8313c3fd3cdd45d59e5894f6699e6715c1753。

直接依赖为此前 full-original-values-first-mean-reduction-twenty-two-model 源，SHA f6f07b2f3fdb50f59565ef6501cbc2121d5882ce7cb32f7d17a4a1d2d139b6a1。只执行 5551 字节前缀，SHA 9a6f12dad89cc77c651f902bf881b53eca708cd8f0dcfab2961dabb089ed3523。该前缀的 N1 slope、K7 corrected、physical lambda 和 original C9 四个固定依赖维持原 basename/SHA。

所有 alarm 和 setitimer 均钳至本源最初 180 秒截止；地址空间 4 GiB。只输出参数定义、原返回标记、计数和 SHA，不保存或传送可重算系数、编码或分片载荷。尚未执行，不先标成功。
