# R271 附录：原两模型的首二进位完整 Schur、统一物理度量与准确顶端来源

日期：2026-11-15。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：下述表示、度量比较和最小化公式均已证明。** 本文处理原 $\mathsf N/\mathsf Y$ 权，不改成任意幂零头。首二进位的消元在全部头长度、全部孔截断及并入的强尾位数上支付一个绝对常数。消元后的完整算子 $P=K-T^2$ 及其完整最小逆仍然保留；本文不声称已付普通右费、返回量或 $N=M$。

依赖仅为 [R239 的实际头与权恒等式](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) §1，以及原物理孔分级。以下重新给出消元所需的全部常数和来源条件。

## 1. 原权的首位分块及一个严格小于一的共同常数

沿用
$$
B e_n=\alpha_{v_2(n)}e_{n-1},\qquad
W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_i=W_{2^i},
$$
$$
d_0=e^{-20},\qquad
\Lambda_i=-\log d_i
=100\,16^i-105\,8^i+(150i+25)2^i,
\qquad b_i=(i+1)^{-2}.
\tag{1.1}
$$
把头的偶、奇物理坐标分别排在前、后。固定真实头 $B_m$ 时，两块均为 $2^{m-1}$ 维；对全局 $B$，两块均为 $\ell^2(\mathbb N_0)$。在任一情形，
$$
\frac{B}{d_0}=
N_0=\begin{pmatrix}0&I\\K&0\end{pmatrix},
\qquad
N_0^2=\begin{pmatrix}K&0\\0&K\end{pmatrix},
\qquad
\|K\|\le\kappa_0:=\frac{d_1}{d_0^2}=e^{-1070}.
\tag{1.2}
$$
这里有限头时把 $B$ 理解为 $B_m$。$K$ 是把每个偶输入送到前一个奇坐标的真实高位加权移位，除以 $d_0$；没有删除进位。若该块非空，其最大权恰为 $\alpha_1/d_0=d_1/d_0^2$。

全部 $i\ge1$ 的 $B^{2^i}/d_i$ 均在这两个块上给出同一个对角算子。强尾删除和远尾删除也在两个块上相同，并与 $K$ 对易。

记
$$
\sigma=\sum_{i\ge1}b_i.
$$
无需使用小数近似：积分上界给
$$
\sigma<
\sum_{n=2}^{10}\frac1{n^2}+\frac1{10}
=\frac{4126285}{6350400}
<\frac{13}{20}.
\tag{1.3}
$$
末一个差为 $1475/6350400$。

对 Cayley 项，设 $N_i=B^{2^i}/d_i$。原权满足
$$
\|N_i\|\le1,\qquad
\|N_i^2\|\le\kappa_i:=\frac{d_{i+1}}{d_i^2},
$$
$$
-\log\kappa_i
=1400\,16^i-630\,8^i+300\,2^i
\ge1000\,16^i.
\tag{1.4}
$$
有限头顶端 $N_i^2=0$ 时，上界仍有效。由
$$
N_i(I+N_i)^{-1}
=(N_i-N_i^2)(I-N_i^2)^{-1}
$$
及 $\kappa_i<1/3$，
$$
\|N_i(I+N_i)^{-1}\|
\le\frac{1+\kappa_i}{1-\kappa_i}
\le1+3\kappa_i.
\tag{1.5}
$$
又 $\sum_{i\ge1}\kappa_i\le2e^{-16000}$。

令 $S$ 表示除了首项以外的全部同对角项。它可包含真实高头项、已经并入头的有限强尾位，以及全部或有限孔截断的纯远尾。各物理位只计算一次。因此
$$
\|S_N\|\le\sigma,\qquad
\|S_Y\|\le\sigma+6e^{-16000}\le\sigma+\kappa_0.
\tag{1.6}
$$

两模型的实际算子 $\mathcal A$ 分别具有以下精确形式：
$$
\mathcal A_N=
\begin{pmatrix}T&I\\K&T\end{pmatrix},
\qquad T=S_N,
\tag{1.7}
$$
以及
$$
\mathcal A_Y
=\begin{pmatrix}U&0\\0&U\end{pmatrix}
\begin{pmatrix}T&I\\K&T\end{pmatrix},
\qquad
U=(I-K)^{-1},\quad
T=(I-K)S_Y-K.
\tag{1.8}
$$
式 (1.8) 来自
$(I-K)N_0(I+N_0)^{-1}=N_0-KI$。
全部因子与 $K$ 对易。

以下统一写
$$
\mathcal A=\operatorname{diag}(U,U)\mathcal A_0,\qquad
\mathcal A_0=\begin{pmatrix}T&I\\K&T\end{pmatrix},
\tag{1.9}
$$
其中 N 模型取 $U=I$。由 (1.3)--(1.6)，两模型均有
$$
\boxed{\|T\|<\tau:=\frac{13}{20}.}
\tag{1.10}
$$
确实 Y 模型的上界不超过 $\sigma+4\kappa_0$，而
$4e^{-1070}<4\cdot2^{-20}<1475/6350400$。
另外
$$
\|U\|\le(1-\kappa_0)^{-1},\qquad
\|U^{-1}\|\le1+\kappa_0.
\tag{1.11}
$$

这些常数与 $m$、孔截断 $Q$、并入的强尾位数 $R$ 均无关。

## 2. 完整核的物理 Schur，而非压缩逆的交换

令
$$
P=K-T^2,\qquad Z=\ker P,\qquad
Jx=(x,-Tx).
\tag{2.1}
$$
直接解 $\mathcal A_0(x,y)=0$ 得
$$
\boxed{\ker\mathcal A=JZ.}
\tag{2.2}
$$
$Z$ 是整个 $P$ 的核，未先限制到某个 primitive 或低孔子空间。

两侧消元的准确式为
$$
\begin{pmatrix}I&0\\-T&I\end{pmatrix}
\mathcal A_0
\begin{pmatrix}I&0\\-T&I\end{pmatrix}
=
\begin{pmatrix}0&I\\P&0\end{pmatrix}.
\tag{2.3}
$$
这是两个不同输入、输出度量下的等价变换，不是相似变换，也不是 MP 逆的直接公式。

$J$ 上的真实物理 Gram 是
$$
G_Z=J^*J
=P_Z(I+T^*T)|_Z,
$$
故
$$
\boxed{I_Z\le G_Z\le\frac{569}{400}I_Z.}
\tag{2.4}
$$
这里及下文 $P_Z$ 为正交投影，右端伴随均为原物理伴随。完整核投影因而为
$$
\boxed{
P_{\ker\mathcal A}
=J G_Z^{-1}J^*.
}
\tag{2.5}
$$
该逆是整个真实核源 $Z$ 上的 $G_Z^{-1}$；式 (2.4) 支付了它。它并未支付 $P^\dagger$ 或 $(P^*)^\dagger$。

因为 $T$ 与 $P$ 对易，$T$ 保持 $Z$。记 $V=T|_Z$，则也可写 $G_Z=I+V^*V$。

## 3. 原 $B$ 理想和真实 $W$ 的准确运输

在 (2.2) 的同一空间上，
$$
\frac{B}{d_0}Jx=(-Tx,Kx)=J(-Tx)\qquad(x\in Z),
\tag{3.1}
$$
其中只用了 $Kx=T^2x$。因此
$$
\overline{B\ker\mathcal A}
=J\,\overline{VZ}.
\tag{3.2}
$$
若
$$
W_{\mathcal A}
=\ker\mathcal A\ominus\overline{B\ker\mathcal A},
$$
则完整物理正交条件为
$$
\boxed{
W_{\mathcal A}
=J\{x\in Z:V^*G_Zx=0\}
=J G_Z^{-1}\ker V^*.
}
\tag{3.3}
$$
在局部模型中，这里是其真实 $B_m$ 理想；在原全局 N/Y 模型中，这里就是原全局 $B$ 理想。二者不混同。

式 (3.3) 保留了 $W$ 来源，而没有把 $G_Z$ 误换成单位度量。它把所需稠密像问题准确留在 $\overline{VZ}=Z$；$G_Z$ 的良好界本身不证明该稠密性。

## 4. 原有限 left 空间及其真实顶端来源

现在固定同一远尾孔计数，写
$$
S_N=S_{N,\mathrm{head}}+D,\qquad
S_Y=S_{Y,\mathrm{head}}+D.
$$
并入的强尾位在 head 中，$D$ 只删除远尾孔。取
$$
\mathscr H_{\le Q}
=\bigoplus_{n=0}^Q\mathscr H_n,\qquad
D_Q=D|_{\mathscr H_{\le Q}},
$$
以及第 $Q$ 层的等距嵌入 $\iota_Q$。定义
$$
T_Q=T_{\mathrm{head}}+J_DD_Q,
\tag{4.1}
$$
其中
$$
\begin{array}{c|c|c}
 &T_{\mathrm{head}}&J_D\\ \hline
N&S_{N,\mathrm{head}}&I\\
Y&(I-K)S_{Y,\mathrm{head}}-K&I-K
\end{array}
$$
全部算子仍是同一个真实物理算子的限制，且 $\|T_Q\|<13/20$。

原 left 空间是
$$
V_Q=
\{v:\operatorname{supp}_{\mathrm{far}}v\subset[0,Q],\
P_{\le Q-1}\mathcal A v=0\}.
\tag{4.2}
$$
写 $v=(x,y)$，并定义实际顶端变量
$$
b=y_Q+T_{\mathrm{head}}x_Q.
\tag{4.3}
$$
由于 $U$ 只作用 head，原低行方程等价于归一算子 $\mathcal A_0$ 的低行方程。其第一行准确给
$$
\boxed{y=-T_Qx+\iota_Qb.}
\tag{4.4}
$$
第二行准确给
$$
\boxed{
P_{\le Q-1}
\big[(K-T_Q^2)x+T_Q\iota_Qb\big]=0.
}
\tag{4.5}
$$
因此 (4.4)--(4.5) 是整个 $V_Q$ 的一一参数化，既无头支撑假设，也未去掉高孔 nuisance。

如果原 top 来源为
$$
r=(r_{\mathrm e},r_{\mathrm o})
=(\mathcal A v)_Q,
$$
令
$$
\widehat r
=(U^{-1}r_{\mathrm e},U^{-1}r_{\mathrm o}).
$$
则准确的来源条件是
$$
\boxed{
b=\widehat r_{\mathrm e},\qquad
(K-T_{\mathrm{head}}^2)x_Q+
T_{\mathrm{head}}b=\widehat r_{\mathrm o}.
}
\tag{4.6}
$$
N 模型的 $\widehat r=r$；Y 模型两分量均乘 $I-K$。特别，$b$ 不是可以删去的误差项。

真实零源空间是
$$
K_Q=\ker\mathcal A|_{\mathscr H_{\le Q}}
=\{(x,-T_Qx):x\in\ker(K-T_Q^2)\}.
\tag{4.7}
$$
在 (4.4)--(4.6) 中，零源恰为 $b=0$ 及 $(K-T_Q^2)x=0$ 的全部行，不仅是低行。

## 5. 全 left 最小化的绝对常数比较

参数 $(x,b)$ 上的完整物理能量是
$$
\mathfrak g_Q(x,b)
=\|x\|^2+\|-T_Qx+\iota_Qb\|^2.
\tag{5.1}
$$
单位三角算子及其逆的范数均不超过 $1+\|T_Q\|<33/20$，故
$$
\boxed{
\left(\frac{20}{33}\right)^2
(\|x\|^2+\|b\|^2)
\le \mathfrak g_Q(x,b)
\le
\left(\frac{33}{20}\right)^2
(\|x\|^2+\|b\|^2).
}
\tag{5.2}
$$
此式在 (4.5) 的整个闭来源空间上成立。

固定原来源 $r$，以 $\mathcal F_Q(r)$ 表示满足 (4.5)--(4.6) 的全部 $(x,b)$。则原真实 left 最小费用准确为
$$
\boxed{
\mu_Q(r)^2
=\inf_{(x,b)\in\mathcal F_Q(r)}
\mathfrak g_Q(x,b).
}
\tag{5.3}
$$
若令
$$
\mu_{Q,0}(r)^2
=\inf_{(x,b)\in\mathcal F_Q(r)}
(\|x\|^2+\|b\|^2),
$$
则
$$
\boxed{
\left(\frac{20}{33}\right)^2\mu_{Q,0}(r)^2
\le\mu_Q(r)^2
\le\left(\frac{33}{20}\right)^2\mu_{Q,0}(r)^2.
}
\tag{5.4}
$$
两个 infimum 使用完全相同的原来源、低行方程、顶端条件和零源核。给定可行来源时，其仿射集合闭，最小者存在；不可行来源按费用 $+\infty$ 处理。没有将先压缩的矩阵逆代替完整极小化。

## 6. 全部 head 旗与 bare 高旗的运输

为避免把首位消元误用成删旗，给出显式检查方法。设 $C$ 是相应真实有限 head（可含 $R$ 个强物理位），并令
$$
C_0=U^{-1}C
=\begin{pmatrix}T_{\mathrm{head}}&I\\K&T_{\mathrm{head}}\end{pmatrix}.
$$
$U$ 与 $C_0$ 对易且可逆，因此 $\ker C^j=\ker C_0^j$。定义
$$
E_j=\sum_{r=0}^{\lfloor j/2\rfloor}
\binom j{2r}T_{\mathrm{head}}^{j-2r}K^r,
$$
$$
O_j=\sum_{r=0}^{\lfloor(j-1)/2\rfloor}
\binom j{2r+1}T_{\mathrm{head}}^{j-2r-1}K^r.
\tag{6.1}
$$
则
$$
C_0^j=\begin{pmatrix}E_j&O_j\\KO_j&E_j\end{pmatrix}.
\tag{6.2}
$$
所以一个物理行 $(x,y)$ 属于 $\ker C^j$ 的完整条件是
$$
E_jx+O_jy=0,\qquad KO_jx+E_jy=0.
\tag{6.3}
$$
若该行由 (4.4) 参数化，必须代入得到两条条件
$$
(E_j-O_jT_Q)x+O_j\iota_Qb=0,
$$
$$
(KO_j-E_jT_Q)x+E_j\iota_Qb=0.
\tag{6.4}
$$
不能用某个单独的 $\ker P^j$ 替代它们。

另一方面，$T_Q$、$U$、$E_j$、$O_j$ 均与远尾删除 $D_Q$ 对易，并保持每个 $\ker D_Q^a$。两个单位三角变换及其逆因而保持
$(\ker D_Q^a)\oplus(\ker D_Q^a)$。对于原 right 第 $j$ 行的 bare 高旗 $\ker D^{j-1}$，应同时运输 (6.3) 的 head 条件和这整个高旗；交集以及零源核均随同一可逆映射运输。

在相应物理正交商中，诱导变换及其逆仍不超过 $33/20$：这是对完整高子空间取距离后，由原范数界直接得到。它不表示原正交低代表逐项保持；任何最小代表仍须对完整变换后高子空间作 Schur 消去。

本节给出的只是准确旗运输及其统一度量成本，不把新 left 表示误称为已付整个普通 right 逆。

## 7. 完整 adjoint Green 的剩余 Schur 与自然域

下面明确度量良好之后尚存的完整逆。先对 $\mathcal A_0$。给定物理 $f=(f_0,f_1)$，令
$$
F=f_0-T^*f_1,\qquad
x=G_Z^{-1}P_ZF,\qquad
a=f_1+Tx,
$$
$$
r=F-(I+T^*T)x.
\tag{7.1}
$$
由 §2，$Jx=P_{\ker\mathcal A_0}f$，且 $r\perp Z$。解
$$
\mathcal A_0^*g=(I-P_{\ker\mathcal A_0})f
$$
时，全部可行向量恰为
$$
\boxed{
g=(a-T^*z,z),\qquad P^*z=r.
}
\tag{7.2}
$$
这由第二分量先给 $g_0=a-T^*g_1$，再代第一分量直接得到。因而真实最小 Green 费用是
$$
\boxed{
\|(\mathcal A_0^*)^\dagger f\|^2
=
\inf_{P^*z=r}
\big(\|z\|^2+\|a-T^*z\|^2\big).
}
\tag{7.3}
$$
等价地，被最小化的二次型为
$$
\|a\|^2-2\Re\langle Ta,z\rangle
+\langle(I+TT^*)z,z\rangle.
\tag{7.4}
$$
其 Hessian 仍在 $[I,569I/400]$。但是约束仍是整个 $P^*$ 的真实像，并且须对整个 $\ker P^*$ 极小化。

对 Y 原算子，(7.1) 不变，全部可行向量为
$$
g=\operatorname{diag}(U^{-*},U^{-*})(a-T^*z,z),
\qquad P^*z=r,
\tag{7.5}
$$
其真实费用为 (7.5) 的完整物理范数平方的 infimum。由 (1.11)，这只在 (7.3) 外再支付 $(1\pm\kappa_0)^2$ 的双侧因子。

本节中的 MP 表达采用标准自然域
$\operatorname{Ran}\mathcal A^*\oplus\ker\mathcal A$。
如果 $r\notin\operatorname{Ran}P^*$，则 (7.2) 的可行集合为空，费用为 $+\infty$；只知 $r\perp\ker P$ 并不把闭包像提升成真实像。没有假设 $P^*$ 闭像，也未把 $G_Z^{-1}$ 的界外推到 $(P^*)^\dagger$。

## 8. 对当前来源与剩余目标的准确意义

本文已经支付：

1. 原 N/Y 首位消元的来源、完整核和物理度量；
2. 同一个实际 $u_Q$ 的完整 left 参数化及其真实 top $b$；
3. 所有原 head/高孔旗的可重建运输；
4. 原 $B$ 理想和 $W$ 条件的同一物理表示；
5. 固定物理 forcing 的完整 Green 最小化中，哪些度量有绝对常数、哪一个完整逆仍在。

尚未支付的是 (7.3) 中与原同一 $W$ forcing 相容的 $P^*$ 费用，或其与原 bare/flat 两费的共同返回配对。尤其不能把 $\|T\|<1$、$G_Z$ 的统一正定性或首位单位块，单独称为普通右费上界。后继研究继续保留 (4.6) 的真实顶端来源及 (7.3) 的完整 nuisance 极小化。
