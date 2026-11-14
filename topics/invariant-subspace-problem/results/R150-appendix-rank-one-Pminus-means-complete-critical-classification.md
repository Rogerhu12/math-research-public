# R150 补篇：P− 的三个代数物理均值全部临界点分类

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 完整结论

令
$$
P_-(s)=s^3+27s^2+\frac{864}{5}s+\frac{864}{5}.
$$
对于它的任一复根 $\beta$ 及任意 $a\ne0$，固定原物理均值 $y=a\,v(\beta)$。原最高方程与全部十七条余临界方程的解恰为
$$
H=h\,y^2,\qquad V=\frac{6h-1}{4}\,y^3,\qquad h\in\mathbb C.
\tag{1.1}
$$
所有解都满足 $T_3=0$。本篇同时覆盖三个共轭均值，不预设 $A_yM=0$、$MKM=0$，不限制三阶张量本质变量数或均值位置。

使用原六模、原 $K$ 和原 Hankel 矩；此有限标量分支的完成不宣告普通不变子空间问题完成。

## 2. 原系统的次数五空间及精确上界

先取 $a=1$，写
$$
H=M+\frac12y^2,\quad M_{ij}=m_{i+j},\quad
m_k=\sum_{j=0}^k\binom{k}{j}\beta^{k-j}n_j.
$$
令 $c=n_0,d=n_1$，横向变量为 $n_2,\ldots,n_{10}$。原最高方程给出
$$
V=\frac32\mathcal L_y(M)+\frac12y^3,\qquad
T_3=6(\mathcal L_y(M)-yM),
$$
其中 $\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)]$。原十七式按
[完整中心化归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)
精确保留为
$$
N(Kv(t),Kv(t))\equiv0,\quad
N=4MKM+6(\mathcal L_y(M))_{Ky},
$$
的十一项系数，以及
$$
\Gamma=2\tau_2(M)y+8MKM(Ky)
-12\mathcal L_y(M):(KMK)=0
$$
的六个原坐标。没有加强为全矩阵等式。

以 $f_i$ 表示固定 $\det(J_3)$ 倍的这些原式，取全部 $|\alpha|\le3$ 的 $n^\alpha f_i$，其线性包 $\mathcal R$ 的指定矩阵有 6188 行、4367 列。

由
[原中心化算子精确秩](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)，
每个 $P_-$ 根都有 $\operatorname{rank}A_y=8$。同时
$$
g=(v'(\beta))^{\mathsf T}Kv'(\beta)
=-2\beta^2(\beta-2)(\beta+6)\ne0,
$$
因为下节将证明 $P_-$ 不可约，故其根不是 $0,2,-6$。

在次数至多五空间中，投影 $\pi$ 保留 20 个纯切向列和 135 个恰一个横向因子列，杀去 4212 个至少两个横向因子列。完整投影由原 $224\times155$ 矩阵 $P(\beta)$ 控制；它包含纯切向乘子及必要的带一个横向因子的乘子。逐点上界
[非接触均值的秩控制](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)
给出
$$
\operatorname{rank}P(\beta)\le124+2\operatorname{rank}A_y=140.
$$
因此
$$
\dim_{\mathbb Q(\beta)}\mathcal R\le4212+140=4352.
\tag{2.1}
$$

## 3. 模十七下界及三共轭的同时提升

令 $\theta=5\beta$，则
$$
F_-(\theta)=\theta^3+135\theta^2+4320\theta+21600.
$$
它在模十一的 $0,\ldots,10$ 上的值为
$$
7,\ 8,\ 10,\ 8,\ 8,\ 5,\ 5,\ 3,\ 5,\ 6,\ 1.
$$
没有零点，故首一三次 $F_-$ 在 $\mathbb F_{11}$ 上不可约，在 $\mathbb Q$ 上也不可约。

模十七取
$$
s=4,\qquad\theta=3,\qquad5s\equiv3\pmod{17}.
$$
有 $F_-(3)=0$、$F_-'(3)=6\ne0$，且原 $\det(J_3)\equiv9\pmod{17}$。

下界输入从原 $K,\operatorname{adj}(J_3),\det(J_3)$ 在整数代表元 $s=4$ 重建，作同一矩坐标平移后，**逐行乘回保存的 scale**。于是每一行是固定 $\det(J_3)$ 倍原方程的真正专门化，系数来自 $\mathbb Z[s]$；不会对可能在该素数消失的参数因子作除法。

模十七精确消元在全部 6188 个指定行的前 5643 行已达到秩 4352，随后停止。该子矩阵仍有全部 4367 列，其一至五次枢轴数分别是
$$
4,\ 64,\ 284,\ 999,\ 3001.
$$
故原符号矩阵有 4352 阶整数子式 $q(s)$，满足
$$
q(4)\not\equiv0\pmod{17}.
$$
若 $q(\beta)=0$，取 $N=\deg q$，则整系数多项式 $5^Nq(\theta/5)$ 被首一最小多项式 $F_-$ 整除；模十七代入 $\theta=3$，将与 $5^Nq(4)\ne0$ 矛盾。故
$$
\dim_{\mathbb Q(\beta)}\mathcal R\ge4352.
\tag{3.1}
$$
数域中的非零子式在每个复嵌入下仍非零，因而一次下界覆盖三个共轭根。这是整数子式与不可约数域的提升，不是用有限域零点集合推断复数解。

## 4. 完整原理想与纯均值分类

(2.1)、(3.1) 相等，所以
$$
4352=\dim\mathcal R
=\dim(\mathcal R\cap\ker\pi)+\dim\pi\mathcal R
\le4212+140.
$$
两部分必须各达到上界，特别地 $\ker\pi\subset\mathcal R$。因此
$$
n_j^2\in\mathcal R\subset(f_1,\ldots,f_{17}),
\qquad j=2,\ldots,10.
$$
任一复数临界点的横向坐标全零，故
$$
M=c\,y^2+d(yu^{\mathsf T}+uy^{\mathsf T}),
\qquad u=v'(\beta).
$$

原物理恒等式给出 $\mathcal L_y(M)=yM$、$M(Ky)=0$ 和
$$
MKM=d^2g\,y^2.
$$
所以原二阶系数方程迫
$$
4d^2g\,p_y(t)^2\equiv0.
$$
$g\ne0$ 且 $p_y$ 非零，得 $d=0$。令 $h=c+\tfrac12$，由最高方程立即得到 (1.1)，并有 $T_3=0$。反向由 $y^{\mathsf T}Ky=0$ 直接代入原式成立。任意非零振幅按权重二、三缩放 $H,V$，完成全部均值振幅的分类。

## 5. 精确重建

[小回执](../notes/2026-11-14-rank-one-Pminus-algebraic-lower-bound-receipt.json)
保存三次不可约证书、模十七简单根、矩阵哈希和完整下界记录。原固定整数系统 SHA256 为
~~~text
f3bafe36269a9ca4aece5d18c63023c789046b5faf500fd4551d3d6fdd0cd9a7
~~~
运行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js Pminus
~~~
[入口](../notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js)
保留已完成的 $P_+$ 分支，新增本篇 $P_-$，调用相同
[模十七/十九精确程序](../notes/2026-11-14-rank-one-macaulay-f17-f19.js)。
全过程对原系数、有限域算术和非零枢轴作精确操作；到足够下界即停止，不需处理多余行。

至此 $P_+$、$P_-$ 两组三次代数均值都已逐组完整闭合。$E_8$ 与其他仍未显式排除的有限例外继续保留在 open.md，不能从本条外推。
