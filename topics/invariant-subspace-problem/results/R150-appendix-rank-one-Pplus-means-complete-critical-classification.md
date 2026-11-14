# R150 补篇：P+ 的三个代数物理均值全部只有纯均值临界点

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 完整分类

设
$$
P_+(s)=s^3-5s^2+\frac{32}{5}s-\frac85,
$$
$\beta$ 为它的任一复根，$a\ne0$，$y=a\,v(\beta)$ 为原物理均值。原最高方程及全部十七条低阶临界方程的解恰为
$$
H=h\,y^2,\qquad
V=\frac{6h-1}{4}\,y^3,\qquad h\in\mathbb C.
\tag{1.1}
$$
特别地，所有解都满足 $T_3=0$。这同时关闭 $P_+$ 的三个共轭物理均值下全部非零三阶临界候选，不附加 $A_yM=0$、$MKM=0$、本质变量数或均值位置条件。

本篇继续使用原六模、原 $K$ 和原 Hankel 矩。它是原标量分支的完整结果，不宣告普通 Hilbert 空间不变子空间问题完成。

## 2. 原十七式与逐点秩上界

先令 $a=1$，并写
$$
H=M+\frac12y^2,\qquad
M_{ij}=m_{i+j},\qquad
m_k=\sum_{j=0}^k\binom{k}{j}\beta^{k-j}n_j.
$$
这是对角线为一的可逆矩坐标变换。切向变量为 $c=n_0,d=n_1$，横向变量为 $n_2,\ldots,n_{10}$。原最高方程精确消去 $V$：
$$
\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)],\quad
V=\frac32\mathcal L_y(M)+\frac12y^3,\quad
T_3=6(\mathcal L_y(M)-yM).
$$
剩余原式是
$$
\bigl[4MKM+6(\mathcal L_y(M))_{Ky}\bigr](Kv(t),Kv(t))\equiv0
$$
的十一项系数，以及
$$
2\tau_2(M)y+8MKM(Ky)
-12\mathcal L_y(M):(KMK)=0
$$
的六个原向量坐标；没有把曲线系数恒等式换成全矩阵恒等式。

由
[中心化线性算子的精确秩分类](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)，
在每个 $P_+$ 根上 $\operatorname{rank}A_y=8$。另一方面，
$$
g=(v'(\beta))^{\mathsf T}Kv'(\beta)
=-2\beta^2(\beta-2)(\beta+6)\ne0.
$$
其非零性也由第 3 节的三次不可约性立即得到。

对原十七式 $f_i$ 取全部次数至多三的单项式倍式，记次数五线性包为 $\mathcal R$。其指定矩阵有 6188 行、4367 列。投影 $\pi$ 保留全部 20 个纯 $c,d$ 列及 135 个恰含一个横向因子的列；被杀去的至少两个横向因子列共有 4212 个。纯切向二次项只有非零的 $d^2$ 倍数，故所有原倍式的投影包含于原 $224\times155$ 投影矩阵 $P(\beta)$ 的行空间。

[非接触均值的逐点秩控制定理](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)
对每一个非接触物理均值给出
$$
\operatorname{rank}P(\beta)
\le124+2\operatorname{rank}A_y=140.
$$
该上界来自原方程的低次数核维数，不依靠有限域采样。因此
$$
\dim_{\mathbb Q(\beta)}\mathcal R\le4212+140=4352.
\tag{2.1}
$$
上界包含所有均值梯度行及所有必要的带一个横向因子的乘子。

## 3. 一个模十九下界同时覆盖三个共轭根

令 $\theta=5\beta$。其整系数首一多项式为
$$
F_+(\theta)=\theta^3-25\theta^2+160\theta-200.
$$
模十一在 $\theta=0,\ldots,10$ 的值依次是
$$
9,\ 2,\ 6,\ 5,\ 5,\ 1,\ 10,\ 5,\ 3,\ 10,\ 10.
$$
全部非零，所以这个首一三次在 $\mathbb F_{11}$ 上不可约，从而在 $\mathbb Q$ 上不可约。$\mathbb Q(\theta)=\mathbb Q(\beta)$ 是三次域。

模十九取
$$
\theta=6,\qquad s=5,\qquad 5s\equiv6\pmod{19}.
$$
直接有 $F_+(6)=0$、$F_+'(6)=6\ne0$（模十九）。这里的整数 $s=5$ 仅用于重建这个模十九专门化。

**原矩阵的固定整数比例。** 先对任意参数 $s$ 从原 $K,\operatorname{adj}(J_3),\det(J_3)$ 生成十七式，再作矩坐标平移。对每条已经约去最大公因数的行，必须乘回其保存的 scale。所得每一行都是固定 $\det(J_3)$ 倍的原方程，系数是 $\mathbb Z[s]$ 中的多项式。这样模十九得到的是同一符号矩阵的真正专门化，不会把依赖参数、可能在该素数消失的行因子误除掉。这里 $\det(J_3)\equiv2\pmod{19}$。

以这个固定整数矩阵为输入，模十九精确消元在预先指定的 6188 个行中的前 5643 行，已经得到秩 4352。达到所需下界后即停止；其余行不再需要计算。所用子矩阵仍有全部 4367 列。总次数一至五的枢轴数为
$$
4,\ 64,\ 284,\ 999,\ 3001.
$$
因此存在原符号矩阵的一个 4352 阶子式 $q(s)\in\mathbb Z[s]$，满足
$$
q(5)\not\equiv0\pmod{19}.
\tag{3.1}
$$

这给出数域上的严格下界。若 $q(\beta)=0$，令 $N=\deg q$，则
$$
Q(\theta)=5^Nq(\theta/5)\in\mathbb Z[\theta]
$$
被首一最小多项式 $F_+$ 整除。模十九代入 $\theta=6$ 应有 $Q(6)=0$；但
$$
Q(6)=5^Nq(5)\ne0
$$
与 (3.1) 矛盾。所以 $q(\beta)\ne0$，且其每个复共轭像都非零。于是
$$
\dim_{\mathbb Q(\beta)}\mathcal R\ge4352,
\tag{3.2}
$$
并且同一结论同时适用于 $P_+$ 的全部三个复根。

这里用的是非零整数子式及不可约数域的提升，没有从有限域点集推断复数点集。

## 4. 秩相等给出完整原理想约束

合并 (2.1)、(3.2)，$\dim\mathcal R=4352$。又
$$
\dim\mathcal R
=\dim(\mathcal R\cap\ker\pi)+\dim\pi\mathcal R
\le4212+140.
$$
等号强迫 $\ker\pi\subset\mathcal R$。所以次数至多五、至少包含两个横向因子的每个多项式都属于原十七式的理想。特别地
$$
n_j^2\in\mathcal R\subset(f_1,\ldots,f_{17}),
\qquad 2\le j\le10.
$$
任一复数临界点都有 $n_2=\cdots=n_{10}=0$，从而
$$
M=c\,y^2+d(yu^{\mathsf T}+uy^{\mathsf T}),
\qquad u=v'(\beta).
$$

在这条真实物理切向平面上，$\mathcal L_y(M)=yM$，且 $M(Ky)=0$，故线性二阶项消失；二次项满足
$$
MKM=d^2g\,y^2.
$$
原十一项二阶方程于是包含
$$
4d^2g\,p_y(t)^2\equiv0.
$$
$g\ne0$，原 $K$ 非奇异且 $y\ne0$，所以 $p_y$ 不是零多项式。因此 $d=0$。

写 $h=c+\tfrac12$，最高方程给出
$$
H=h y^2,\qquad
V=\frac32c\,y^3+\frac12y^3
=\frac{6h-1}{4}y^3.
$$
$T_3=0$ 随即成立。反向由 $y^{\mathsf T}Ky=0$ 和原完整归约直接代入成立。振幅 $a\ne0$ 按原权重缩放，不丢失任何解。定理得证。

## 5. 可完整重建的下界证书

[小回执](../notes/2026-11-14-rank-one-Pplus-algebraic-lower-bound-receipt.json)
记录不可约模十一值、模十九根、固定整数系统 SHA256、处理行数及秩下界。
固定整数系统的 SHA256 为：
~~~text
f55dfbcdae8d0bac64e69173c6f9c4d3af1989f0ce0b98617e59ee72cc46ae73
~~~

执行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js Pplus
~~~
[完整入口](../notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js)
调用已保存的原系统与坐标平移生成器，显式乘回每行 scale，再调用
[模十七与十九精确位平面程序](../notes/2026-11-14-rank-one-macaulay-f17-f19.js)。
达到秩 4352 的真实下界后停止。有限域算术逐位精确进行，非零枢轴的所有标量倍数也保留精确首系数检查。

本条只关闭 $P_+$ 的三个代数均值。$P_-$、$E_8$ 与其他尚未排除的有限特殊均值继续按 open.md 处理，不把未完成的下界省略。
