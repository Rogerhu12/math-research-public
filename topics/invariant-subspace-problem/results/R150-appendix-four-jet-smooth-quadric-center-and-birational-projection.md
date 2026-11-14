# R150 附录：完整低梯度迫四维二次曲面的投影中心光滑

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明的进一步排除。** 在原非割线均值、第三矩本质三维而均值在其外、原二阶矩秩四的临界情形中，原二阶梯度产生的非零二次曲面在投影中心必光滑。因此三维物理投影必双有理，排除先前允许的双覆盖二次曲线型。若四维物理投影的四个五次式没有公共因子，还只可能留下不可约三次曲线型。这些结论使用同一原累积量及完整低梯度，不另选矩。

## 1. 明确的原假设与已付恒等式

沿用[共同长度四归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)和[完整低梯度](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)。当前点是原全部三十三个梯度的零点，并满足：

- 原均值 $y$ 的 $4\times3$ Hankel 矩阵秩为三；
- 非零第三普通矩 $T_3$ 的本质支撑 $W$ 恰三维，且 $y\notin W$；
- 原 Hankel 二阶矩 $H$ 的秩为四。

已知 $E=W\oplus\mathbb Cy$ 是准确长度四的曲线 jet 空间。定义
$$
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky,\quad
M=H-\tfrac14yy^{\mathsf T},\quad
b=p^{\mathsf T}Hp,\quad \tau_2=\operatorname{tr}((KH)^2).
$$
有 $\operatorname{Ran}M\subset W$；在 $W$ 的任意基矩阵 $U$ 中，
$$
M=UCU^{\mathsf T},\qquad C=C^{\mathsf T}\text{ 可逆}.
\tag{1.1}
$$
令 $\lambda\in E^*$ 满足 $\lambda|_W=0,\lambda(y)=1$。前稿给
$$
H\lambda=y/4,\quad
\operatorname{tr}(KM)=-F/2,\quad
\mathcal Q_{F_0^2}=F^2-2b+2\tau_2=0.
\tag{1.2}
$$
这里最后一式是完整原一次梯度的后果。

完整原二阶梯度给非零对称张量
$$
\begin{aligned}
N&=T_{3,p}-F(yy^{\mathsf T}-2H)+4HKH\\
 &=T_{3,p}+2FM+4MKM
   +y(Mp)^{\mathsf T}+(Mp)y^{\mathsf T},
\end{aligned}
\tag{1.3}
$$
其像包含于 $E$，且
$$
v(z)^{\mathsf T}KNKv(z)\equiv0,qquad N\ne0.
\tag{1.4}
$$
因此
$$
\boxed{N\lambda=Mp,\qquad N(\lambda,\lambda)=0.}
\tag{1.5}
$$
以上收缩均只用 $E^*$ 上的值，与延长到六维对偶的选择无关。

还需一个原物理恒等式：
$$
\boxed{K:T_3=-4Mp.}
\tag{1.6}
$$
它直接是前稿二次差分公式中 $q(r)=r^{\mathsf T}Kr$ 的情形，因为 $v(z)^{\mathsf T}Kv(z)=0$。也可由 $K:H=0,K:V=0$ 逐项收缩 $T_3=y^3-2\operatorname{Sym}_{\Sigma}(yH)+4V$ 得到。式 (1.6) 对所有原物理参数成立，无需临界性。

## 2. 原二次曲面不能降到秩一或二

取 $E$ 的基 $E_4$，四个齐次二元五次式
$$
\rho=E_4^{\mathsf T}K v_{\mathrm{hom}}
$$
线性无关：$E_4$ 列满秩、$K$ 可逆，而六个五次单项式独立。除去它们的最大公因子，所得像曲线 $C_E\subset\mathbb P(E^*)$ 是不可约且不在任何平面内的曲线。

$N$ 在此四维坐标下给一个非零二次式，其零集包含 $C_E$。若其秩不超过二，它在复数域上是两个线性式的乘积，包括平方的情况。不可约的 $C_E$ 必被其中一个线性式湮灭，这与四个坐标式独立矛盾。因此
$$
\boxed{\operatorname{rank}N\ge3.}
\tag{2.1}
$$

## 3. 完整临界性排除投影中心为奇点

假设相反 $Mp=0$。由 (1.1)，$U^{\mathsf T}p=0$，故 $T_{3,p}=0$。式 (1.3) 化为
$$
N=2FM+4MKM\in\operatorname{Sym}^2W.
\tag{3.1}
$$
由 (2.1)，$N$ 在三维 $W$ 上恰为非退化二次式。

记
$$
G=U^{\mathsf T}KU,\qquad R=CG,\qquad
A=2FC+4CGC.
$$
所以 $N=UAU^{\mathsf T}$，而 $A$ 可逆。由 $Mp=0$ 有
$$
Hp=Fy/2,\qquad b=F^2,
$$
$$
\tau_2=\operatorname{tr}(R^2)+F^2/4.
$$
把这些代入 (1.2)，得到
$$
\boxed{\operatorname{tr}R=-F/2,\qquad
\operatorname{tr}(R^2)=F^2/4.}
\tag{3.2}
$$
因此 $R$ 的第二基本对称式为零，其特征多项式准确为
$$
\det(tI-R)=t^3+(F/2)t^2-\det R.
\tag{3.3}
$$
在 $t=-F/2$ 代值，给
$$
\det(R+(F/2)I)=\det R.
$$
另一方面
$$
A=4(R+(F/2)I)C,
$$
所以
$$
\det A=64\det C\det R.
\tag{3.4}
$$
$A,C$ 可逆迫 $R$ 和 $G$ 亦可逆。这一步包含 $F=0$，没有除以 $F$。

现在把最高梯度用于同一个三维投影。三个独立物理坐标 $U^{\mathsf T}Kv$ 的像包含于非退化二次曲线 $q_A=0$；其像不是点，故在该不可约二次曲线上稠密。$T_3$ 也在同一像上为零，因而其三元表达只能为
$$
T_3=q_A L,
\tag{3.5}
$$
其中 $L$ 是非零一次式。写 $L(\xi)=\ell^{\mathsf T}\xi$，则普通对称张量收缩给
$$
G:(q_A L)=\frac13\bigl(\operatorname{tr}(AG)\ell+2AG\ell\bigr).
\tag{3.6}
$$
由 (3.2)，
$$
\operatorname{tr}(AG)
=2F\operatorname{tr}R+4\operatorname{tr}(R^2)=0.
$$
然而 (1.6) 与 $Mp=0$ 又要求 (3.6) 为零。于是 $AG\ell=0$。$A,G$ 均可逆，迫 $\ell=0$，与 $T_3\ne0$ 矛盾。

故
$$
\boxed{Mp\ne0.}
\tag{3.7}
$$
由 (1.5)，$[\lambda]$ 在二次曲面 $N=0$ 上，而且该处梯度 $2N\lambda$ 非零。因此投影中心是二次曲面的光滑点。

## 4. 由真实二次曲面得到双有理投影

取投影中心为 $[1:0:0:0]$。由 (1.5)、(3.7)，原二次曲面可写为
$$
2x_0 L(x_1,x_2,x_3)+Q(x_1,x_2,x_3)=0,
\qquad L\ne0.
\tag{4.1}
$$
从该点投影到后三坐标，在 $L\ne0$ 上具有明确有理逆
$$
[x_1:x_2:x_3]\longmapsto
[-Q(x):2L(x)x_1:2L(x)x_2:2L(x)x_3].
\tag{4.2}
$$
曲线 $C_E$ 不在平面 $L=0$ 内，故此逆在曲线的稠密开集成立。这里无论 $N$ 秩三或四都成立；没有假设整张二次曲面光滑。

此外物理 $\mathbb P^1\to C_E$ 本身双有理。设四个五次式的公共因子次数为 $\delta_E$。除因子后的次数 $n_E=5-\delta_E$ 至少三，因为至少需要四个独立二元式。$C_E$ 不在平面内，故其次数 $e_E\ge3$：取曲线上三个不共线点，其张成的平面不包含整条曲线，其截面至少有三个点。一般超平面拉回的次数计数给
$$
n_E=e_Ed_E,
$$
其中 $d_E$ 为一般覆盖数。$3\le e_E\le n_E\le5$ 迫 $d_E=1$。

二者合成就是原 $W$ 的三维物理投影，因为 $\lambda$ 恰湮灭 $W$。所以原最高矩分类中的一般覆盖数必为一，唯一可能的两型为
$$
\boxed{(\delta_W,e_W,d_W)=(3,2,1)
\quad\text{或}\quad(2,3,1).}
\tag{4.3}
$$
原先的 $(1,2,2)$ 双覆盖二次曲线型在本文明确假设下已被完整低梯度排除。

## 5. 四维投影无公共因子时只剩三次曲线

若 $\delta_E=0$，上节还给 $\deg C_E=5$。若 $W$ 投影像是二次曲线，以它的二次参数化代入 (4.2)，便得到四个次数至多四的二元式。除公共因子后仍为同一 $C_E$ 的双有理参数化，所以 $\deg C_E\le4$，矛盾。因此
$$
\boxed{\delta_E=0\quad\Longrightarrow\quad
(\delta_W,e_W,d_W)=(2,3,1).}
\tag{5.1}
$$
此时 $T_3$ 是该不可约平面三次曲线方程的非零倍数。由于 $W\subset E$，其三个原五次式在投影后恰有一个次数二的公共因子；它准确记录物理参数投向中心 $[\lambda]$ 的基点除子，含重数及无穷远。本文没有把这两个零点假定为不同有限点。

## 6. 当前范围与余下任务

本稿进一步使用了原一次梯度和物理收缩，得到 $Mp\ne0$ 及双有理性，而非仅重新描述已知最高矩条件。它保留非割线均值、$y\notin W$、$\operatorname{rank}H=4$ 三个假设。四不同支撑点且 $\lambda(u_i)\ne0$ 时最后一项自动成立；重 jets 只要同样满秩也适用。

仍须解决允许的平面三次曲线与具有公共因子的二次曲线分支的全部原临界条件，并处理二阶矩降秩、均值割线情形以及第三矩本质维数四至六。这里没有断言所有临界点的匹配 Bell 值消失，没有给出全局幂证书或任何未付的实际算子逆。
