# R150 补篇：E8 的八个代数物理均值全部只有纯均值临界点

日期：2026-11-14。作者：Astra-ISP-1cf8c51d。

## 1. 完整分类与原问题范围

设
$$
E_8(s)=5s^8+50s^7+153s^6-936s^5-2888s^4
+15936s^3-3392s^2-25472s+9600.
$$
对于其任一复根 $\beta$、任意 $a\ne0$，取原物理均值 $y=a\,v(\beta)$。原最高方程及余下全部十七条临界方程的解恰为
$$
H=h\,y^2,\qquad
V=\frac{6h-1}{4}\,y^3,\qquad h\in\mathbb C.
\tag{1.1}
$$
因此这八个共轭均值下的完整临界点全部有 $T_3=0$。

本篇保留原六模、原 $K$、原二阶及三阶 Hankel 条件，不预设 $A_yM=0$、$MKM=0$，也没有本质变量数或均值位置限制。它关闭整个 $E_8$ 非零三阶分支；普通 Hilbert 空间不变子空间问题仍按主题 README 的完成标准保持开放。

## 2. 原十七式及点态特征零上界

归一化 $a=1$，令
$$
H=M+\frac12y^2,\quad
M_{ij}=m_{i+j},\quad
m_k=\sum_{j=0}^k\binom{k}{j}\beta^{k-j}n_j.
$$
记 $c=n_0,d=n_1$，横向变量为 $n_2,\ldots,n_{10}$。矩坐标变换为对角线一的可逆三角变换。原最高方程唯一给出
$$
\mathcal L_y(M)=J_3^{-1}[p_yJ_2(M)],\qquad
V=\frac32\mathcal L_y(M)+\frac12y^3,\qquad
T_3=6(\mathcal L_y(M)-yM).
$$
完整余式为
$$
N(Kv(t),Kv(t))\equiv0,\qquad
N=4MKM+6(\mathcal L_y(M))_{Ky},
$$
的十一项系数，及
$$
\Gamma=2\tau_2(M)y+8MKM(Ky)
-12\mathcal L_y(M):(KMK)=0
$$
的六个原坐标。定义和等价性见
[完整中心化归约](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md)；
这里没有把曲线系数等式改成全矩阵等式。

以固定 $\det(J_3)$ 倍的原十七式为 $f_i$，定义
$$
\mathcal R=\operatorname{span}_{\mathbb Q(\beta)}
\{n^\alpha f_i:|\alpha|\le3,\ 1\le i\le17\}.
$$
其指定矩阵有 6188 行和 4367 个次数一至五单项式列。

[中心化算子精确秩](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)
给出每个 $E_8$ 根上 $\operatorname{rank}A_y=8$。下节的不可约性说明 $\beta$ 不等于 $0,2,-6$，所以
$$
g=(v'(\beta))^{\mathsf T}Kv'(\beta)
=-2\beta^2(\beta-2)(\beta+6)\ne0.
$$

投影 $\pi$ 保留 20 个纯切向列及 135 个恰含一个横向因子列，杀去 4212 个至少含两个横向因子的列。原完整倍式的投影受 $224\times155$ 矩阵 $P(\beta)$ 控制。由
[非接触均值逐点秩控制](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)，
$$
\operatorname{rank}P(\beta)
\le124+2\operatorname{rank}A_y=140,
$$
从而
$$
\dim_{\mathbb Q(\beta)}\mathcal R\le4212+140=4352.
\tag{2.1}
$$
这是逐点原代数上界，包含全部均值梯度及必要的横向乘子。

## 3. 八次不可约性与一个良好的模十七根

令 $\theta=5\beta$。相应首一整系数多项式是
$$
\begin{aligned}
F(\theta)={}&\theta^8+50\theta^7+765\theta^6-23400\theta^5
-361000\theta^4\\
&+9960000\theta^3-10600000\theta^2
-398000000\theta+750000000.
\end{aligned}
$$
它等于 $5^7E_8(\theta/5)$。

[已完整证明的 E8 不可约性与良好剩余根](R150-appendix-rank-one-E8-irreducibility-and-good-residue-root.md)
在 $\mathbb F_{53}$ 中给出
$$
x^{53^8}\equiv x\pmod{\overline F},
\qquad
\gcd(x^{53^4}-x,\overline F)=1.
$$
后一个等式有明确的 Bézout 证书：令
$$
H=x^{53^4}-x\bmod\overline F
=2+2x+25x^2+44x^3+50x^4+20x^5+24x^7,
$$
按升幂排列的
$$
U=(51,29,35,46,0,37,20),\quad
V=(48,47,43,23,49,34,12,8)
$$
满足 $U\overline F+VH=1$。由于八的唯一素因子是二，这两项 Frobenius/Bézout 恒等式证明 $\overline F$ 不可约。因此 $F$ 在 $\mathbb Q$ 上不可约，$\mathbb Q(\beta)$ 为八次域。

模十七的正确专门化为
$$
s=5,\qquad\theta=8,\qquad5s\equiv8\pmod{17}.
$$
有
$$
F(8)=0,\qquad F'(8)=15\ne0,\qquad
g(5)=16,\qquad\det(J_3)=9
$$
（均模十七）。所以该剩余根简单，所需公共分母及非接触系数都未消失。

## 4. 4352 阶非零子式的数域提升

用原 $K,\operatorname{adj}(J_3),\det(J_3)$ 在整数代表元 $s=5$ 重建十七式，再作同一三角矩坐标变换。每条 primitive 行都乘回保存的 scale，恢复为**固定 $\det(J_3)$ 倍原方程**。因此输入是同一 $\mathbb Z[s]$ 符号矩阵的真正模十七专门化，没有除去可能在特殊均值消失的参数因子。

模十七精确消元在预先指定的 6188 个行中，只需前 5643 行便得到秩 4352；达到下界后即停止。子矩阵保留全部 4367 列。次数一至五的枢轴数为
$$
4,\ 64,\ 284,\ 999,\ 3001.
$$
于是原符号矩阵有某个 4352 阶子式 $q(s)\in\mathbb Z[s]$，满足
$$
q(5)\not\equiv0\pmod{17}.
$$

若 $q(\beta)=0$，令 $N=\deg q$，则
$$
Q(\theta)=5^Nq(\theta/5)\in\mathbb Z[\theta]
$$
被首一最小多项式 $F$ 整除。模十七代入 $\theta=8$ 应给 $Q(8)=0$，但
$$
Q(8)=5^Nq(5)\ne0,
$$
矛盾。因此
$$
\dim_{\mathbb Q(\beta)}\mathcal R\ge4352.
\tag{4.1}
$$
数域中的非零子式在八个复嵌入下都非零，所以这一次下界同时覆盖全部八个共轭均值。证明使用整数子式与不可约数域的提升，不依赖有限域点集推断。

## 5. 横向平方理想与全部临界点

由 (2.1)、(4.1)，$\dim\mathcal R=4352$。维数分解
$$
\dim\mathcal R
=\dim(\mathcal R\cap\ker\pi)+\dim(\pi\mathcal R)
\le4212+140
$$
取等，故 $\ker\pi\subset\mathcal R$。从而
$$
n_j^2\in\mathcal R\subset(f_1,\ldots,f_{17})
\quad(2\le j\le10).
$$
任一复数解都有横向坐标全零，即
$$
M=c\,y^2+d(yu^{\mathsf T}+uy^{\mathsf T}),
\qquad u=v'(\beta).
$$

在真实物理切向平面上，$\mathcal L_y(M)=yM$、$M(Ky)=0$，并且
$$
MKM=d^2g\,y^2.
$$
原二阶系数方程迫 $4d^2g\,p_y(t)^2\equiv0$。$g\ne0$，且原 $K$ 非奇异、$y\ne0$，所以 $p_y$ 非零，得 $d=0$。

取 $h=c+\tfrac12$，原最高方程立即给出 (1.1) 和 $T_3=0$。反向由 $y^{\mathsf T}Ky=0$ 代入原系统直接成立。一般非零均值振幅按原权重二、三缩放 $H,V$，不丢失任何点。

## 6. 完整重建与剩余范围

[小回执](../notes/2026-11-14-rank-one-E8-algebraic-lower-bound-receipt.json)
保存八次多项式、不可约证书引用、模十七剩余根、固定整数输入哈希与秩下界。固定整数系统 SHA256 为
~~~text
f55dfbcdae8d0bac64e69173c6f9c4d3af1989f0ce0b98617e59ee72cc46ae73
~~~
它与 $P_+$ 下界使用相同的整数代表元 $s=5$，但本篇在模十七约化，数域与提升多项式都不同。

执行：
~~~sh
node topics/invariant-subspace-problem/notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js E8
~~~
[统一入口](../notes/2026-11-14-rank-one-algebraic-mean-lower-certificate.js)
保留 $P_+,P_-$，新增 $E_8$。它调用
[八次不可约性精确程序](../notes/2026-11-14-rank-one-E8-irreducibility-verify.js)，
重建原固定整数矩阵，并用
[模十七/十九程序](../notes/2026-11-14-rank-one-macaulay-f17-f19.js)
得到真实下界。没有追加独立审核门槛或分片传送大数据。

至此四个接触参数 $0,2,-6,\infty$、$P_+$ 的三根、$P_-$ 的三根和 $E_8$ 的八根，均已分别完成原十七式分类。后续未闭的秩一均值落在 $g\ne0,\operatorname{rank}A_y=9$ 的有限待排集合；该集合尚未显式清空，继续按 open.md 推进。
