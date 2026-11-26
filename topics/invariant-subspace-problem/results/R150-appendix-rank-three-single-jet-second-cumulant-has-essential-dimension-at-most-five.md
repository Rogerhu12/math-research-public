# R150 附录：单一三重 H jet 的最后负谱支由二阶局部系数排空

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 原完整临界点若 rankH3 的唯一物理支撑为一个三重 jet，且 rankV2，则 $\dim\operatorname{ess}(T_3)\le5$。本稿关闭此前唯一剩余的 $Hp\ne0,F=-m,e^3=-4m^3$ 本质六维支。证明只用完整原 mean、H、最高梯度的常数、一阶及二阶局部系数；没有新增计算门。

## 1. 精确接续范围与原方程

使用原六维非退化 $K$、物理曲线、Hankel 累积量、$T_3=y^3-6yH+4V$、$p=Ky$、$F=yKy/2$。假设本质维数为六，则 $(y,z_0,z_1,z_2,u,v)$ 为原六空间的一组基。这里前三个 z 为 H 的实际局部 Taylor 列，u、v 为约化 V 的两个不同物理点代表。

[三重 H 的完整初始归约](R150-appendix-rank-three-single-jet-second-cumulant-essential-six-gaussian-reduction.md)已经排除特殊自接触、全部非约化 V 和 $F=2m$；[零 Hp 支排除](R150-appendix-rank-three-single-jet-second-cumulant-zero-hp-essential-six-exclusion.md)已经排除 $Hp=0$。因此只需处理
$$
H=h(z_0z_2+z_1^2+z_2z_0),\quad h\ne0,
\qquad m=hb\ne0,\quad b=K(z_1,z_1),
$$
$$
V=\frac12(u^3+v^3),\qquad
F=-m,\qquad Hp\ne0,\qquad e=uKv,\qquad e^3=-4m^3.
\tag{1.1}
$$
特别 $e\ne0$。保 V 的两个三次单位根尺度可使 $p(u)=p(v)=e$，所有这些尺度分支已在前稿完整覆盖。

记 $\mathfrak b=p^{\mathsf T}Hp$。独立的 Gaussian mean 系数给
$$
(2HK+mI)Hp=0,\qquad \mathfrak b=2m^2.
\tag{1.2}
$$
两个 V mean 系数准确给
$$
H(Ku,Ku)=H(Kv,Kv)=e^2/2.
\tag{1.3}
$$
这些不是删去 V 项的近似：完整 mean 的 Gaussian 和 V 向量分别落在六列基的互补部分，故分别为零。

完整最高恒等式与 H 梯度为
$$
P(t)^3-6P(t)G_H(t)+2(C(t)^3+D(t)^3)=0,
\tag{1.4}
$$
$$
k(t)^{\mathsf T}N k(t)=0,
\quad
N=Fyy^{\mathsf T}-2FH
-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+4HKH+4V_p.
\tag{1.5}
$$
这里 $k(t)=Kx(t)$，$x(t)$ 为实际物理局部曲线，
$P(t)=p(x(t))$、$G_H(t)=H(k(t),k(t))$、
$C(t)=K(x(t),u)$、$D(t)=K(x(t),v)$，而
$V_p=e(u^2+v^2)/2$。我们只使用 (1.5) 的原极线零式，绝不将它替换为矩阵等式 $N=0$。

## 2. 不改变 H 的合法 jet 规范

初始实际 Taylor 列的 Gram 矩阵是
$$
K_R=
\begin{pmatrix}
0&0&-b/2\\
0&b&c\\
-b/2&c&d
\end{pmatrix}.
$$
对任意 a，作
$$
z_0'=z_0,\qquad
z_1'=z_1+a z_0,\qquad
z_2'=z_2-a z_1-\frac{a^2}{2}z_0.
\tag{2.1}
$$
直接展开可知
$$
z_0'z_2'+(z_1')^2+z_2'z_0'
=z_0z_2+z_1^2+z_2z_0,
$$
所以 H 和 h 均不变。这也是合法的物理 Taylor 改变：将旧局部参数取为 $t-2at^2+O(t^3)$，再乘非零局部平凡化 $1+at-a^2t^2/2+O(t^3)$ 即给 (2.1)。

此变换保持 b，且 $c'=c-3ab/2$。因 $b=m/h\ne0$，取 $a=2c/(3b)$ 后可设 $c=0$。仍记新列为 $z_i$，新 $d$ 为 d。此时
$$
HK\bigm|_{\operatorname{Ran}H}
=
\begin{pmatrix}
-m/2&0&hd\\
0&m&0\\
0&0&-m/2
\end{pmatrix}.
\tag{2.2}
$$
令 $p_i=p(z_i)$，则 $Hp=h(p_2z_0+p_1z_1+p_0z_2)$。将其代入 (1.2) 得
$$
p_1=0,\qquad dp_0=0.
$$
又 $\mathfrak b=h(2p_0p_2+p_1^2)=2m^2$，所以
$$
\boxed{p_0p_2=\frac{m^2}{h}=hb^2\ne0,\qquad d=0.}
\tag{2.3}
$$
因此所有剩余点都可在合法实际 jet 中满足
$$
K_R=
\begin{pmatrix}
0&0&-b/2\\
0&b&0\\
-b/2&0&0
\end{pmatrix},\qquad
p_1=0.
\tag{2.4}
$$
这里没有删去 $p_0=0$ 或 d 非零的分支；它们由原 Gaussian 式直接排除。

在 (2.4) 中有准确张量恒等式
$$
HKH=-\frac m2H+\frac{3mh}{2}z_1^2.
$$
故完整 (1.5) 简化为
$$
\boxed{
N=-my^2-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+6mhz_1^2+2e(u^2+v^2).
}
\tag{2.5}
$$
全部 V 项仍明确保留。

## 3. 常数系数迫使两个 V 值非零且不同

写
$$
C_i=K(z_i,u),\qquad D_i=K(z_i,v).
$$
在 H 值处 $G_H(0)=0$。因此 (1.4) 的常数项给
$$
p_0^3+2(C_0^3+D_0^3)=0.
\tag{3.1}
$$
又 $K(z_0,Hp)=-mp_0/2$、$K(z_0,z_1)=0$，所以完整 (2.5) 的常数项给
$$
mp_0^2+2e(C_0^2+D_0^2)=0.
\tag{3.2}
$$

首先，若 $C_0=0$，则 (3.1) 给 $D_0^6=p_0^6/4$；将 (3.2) 立方后代入得 $2e^3=-m^3$。与 $e^3=-4m^3$ 合并便是 $7m^3=0$，矛盾。$D_0=0$ 同理。

其次，若 $C_0=D_0=c$，则 (3.1) 给 $c^6=p_0^6/16$，而 (3.2) 的立方给 $4e^3=-m^3$。这与 (1.1) 合并为 $15m^3=0$，仍矛盾。

所以完整必要条件为
$$
\boxed{C_0D_0(C_0-D_0)\ne0.}
\tag{3.3}
$$
以上只用 $p_0,m\ne0$，没有遗漏任一立方根或平方根分支。

## 4. 一阶系数使两个 V 一阶值同时为零

由 $p_1=0$、(2.4)，
$$
P(t)=p_0+p_2t^2+O(t^3),\qquad
G_H(t)=O(t^2).
$$
因此 (1.4) 的一次系数为
$$
C_0^2C_1+D_0^2D_1=0.
\tag{4.1}
$$

完整 H 梯度 (2.5) 的一次系数中，所有 Gaussian 项都为零：$p_1=0$；
$K(z_1,Hp)=mp_1=0$；
$K(z_0,z_1)=0$。仅剩 V 项，故
$$
C_0C_1+D_0D_1=0.
\tag{4.2}
$$
(4.1)—(4.2) 的二乘二系数行列式为
$C_0D_0(D_0-C_0)$，由 (3.3) 非零。所以
$$
\boxed{C_1=D_1=0.}
\tag{4.3}
$$
将它代回完整 V mean 式 (1.3)，准确得到
$$
\boxed{C_0C_2=D_0D_2=\frac{e^2}{4h}.}
\tag{4.4}
$$

## 5. 二阶最高系数给 $1=5/2$ 的矛盾

在 (2.4) 的实际物理 Taylor 参数中，
$$
K(x(t),z_0)=-\frac b2t^2+O(t^3),\quad
K(x(t),z_1)=bt+O(t^3),\quad
K(x(t),z_2)=-\frac b2+O(t^3).
$$
因此
$$
G_H(t)=\frac32hb^2t^2+O(t^3).
\tag{5.1}
$$
用 (2.3)、(4.3)，最高式 (1.4) 的二次项完整为
$$
3p_0^2p_2-9hb^2p_0
+6(C_0^2C_2+D_0^2D_2)=0.
$$
因 $p_0p_2=hb^2$，该式等价于
$$
C_0^2C_2+D_0^2D_2=hb^2p_0.
$$
再用 (4.4) 得
$$
\boxed{S:=\frac{C_0+D_0}{p_0}=\frac{4m^2}{e^2}.}
\tag{5.2}
$$
所有此处除法仅涉及已经证明非零的 h、e、$p_0$。

最后令 $X=C_0/p_0,\ Y=D_0/p_0$。原常数项 (3.1)—(3.2) 仍要求
$$
X^3+Y^3=-\frac12,\qquad
X^2+Y^2=-\frac{m}{2e}.
$$
使用 $S=X+Y$ 和 $XY=(S^2+m/(2e))/2$ 消去 XY，得到
$$
\boxed{S^3+\frac{3mS}{2e}=1.}
\tag{5.3}
$$
然而 (5.2) 与 $e^3=-4m^3$ 给
$$
S^3=\frac{64m^6}{e^6}=4,\qquad
\frac{3mS}{2e}=\frac{6m^3}{e^3}=-\frac32.
$$
所以 (5.3) 的左边准确等于 $5/2$，不等于 1，矛盾。

## 6. 结论与边界

本稿完整排除三重 H 的最后 $Hp\ne0,F=-m$ 本质六维支。结合已登记的初始分支排除和零 Hp 支排除，得到
$$
\boxed{\operatorname{rank}H=3,\ H\text{ 为单一三重物理 jet},
\ \operatorname{rank}V=2
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le5.}
$$
特殊自接触源 $0,2,-6,\infty$ 与非约化 V 均已由初始归约完整处理；本稿的唯一局部规范除法 $b\ne0$ 恰对应此前剩余的普通源。V 支撑在无穷远也没有例外，因为本证明只用原物理代表、完整收缩和 H 源局部 Taylor 系数，并未对 V 点采用仿射坐标或除以其任何坐标。

所有新步骤为显示的特征零手证，没有新增数值或有限域门。本质四、五维、H 的其他长度三类型、更高秩层以及 ISP 的完成标准仍未由本结论解决。

