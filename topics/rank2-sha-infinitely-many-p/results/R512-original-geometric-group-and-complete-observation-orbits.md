# R512 — 原六输入几何群、完整观测轨道与真实压深词域

日期：2026-11-14。**状态：已证明。** R493 的两个实际六变量变换生成一个准确的十八阶群，结构为 $C_3\times S_3$。本篇列出原 $Y$ 的全部六条观测轴、原 $W$ 的全部九条观测轴及其真正边际，给出稳定子和原来源上的忠实二维作用。六条 $Y$ 轴各有同一个完整反射核心；任意正压深词因此有准确的原像格及原曲线中央行。

这里的群是物理六输入上的几何群，不是 R501 的九十六阶来源核心群。多个轨道轴依旧读取原固定 $S/T$，没有据此增加独立曲线或证明跨素数非消失。

## 1. 固定原来源和矩阵

保 R493 的同一个原来源及物理输入：
$$
\xi=(\xi_1,\xi_2,\xi_3,x=\xi_4,c,d_0)^t,\qquad
\rho=-\nu_\sigma^{\otimes6}/84,
$$
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=(5+\delta)/2,\quad
\lambda=-\bar\pi_0^{-1},\quad\kappa=p\lambda^2.
\tag{1}
$$
以下一切矩阵先作用于这六个未压缩的输入。R509 的四输入推前、R515 的二维推前不能用来删去矩阵交叉项。

在 $I=(\xi_1,\xi_3,x,c)$ 上，
$$
T_I=\frac12
\begin{pmatrix}
-\omega&1&\omega^2&\omega\\
-\omega^2&-\omega&1&-\omega^2\\
-1&-\omega^2&-\omega&1\\
-\omega&1&-\omega^2&-\omega
\end{pmatrix}.
\tag{2}
$$
在 $\xi_2,d_0$ 上 $T$ 恒等。令
$$
b=(1,0,\omega,-\omega^2,-1,0)^t,\qquad
C=\bar b^{\,t}\xi/2,\qquad
U=I-\frac12b\bar b^{\,t}.
\tag{3}
$$
原完整 Hermitian 等距恒等式为
$$
T^3=I,\quad U^2=I,\quad
T\bar T^{\,t}=U\bar U^{\,t}=I.
\tag{4}
$$
两个原观察行是
$$
Y=(\delta,2\delta,\gamma,\bar\gamma,1,2),\qquad
W=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4).
\tag{5}
$$
它们满足 $YT=Y,\ WU=W$；边际分别是 $S,6\delta T_{\rm ar}$。
这里用 $T_{\rm ar}$ 表示原七十二度算术来源，以免与几何矩阵 $T$ 混淆。

R493 的原完整来源身份给
$$
h=\omega^2T_*\rho,\qquad
U_*\rho=\rho+h,\qquad
T_*h=-\omega(\rho+h),\qquad U_*h=-h.
\tag{6}
$$
这些是整个六变量测度身份，所有附带条件必须沿同一物理矩阵运输。

## 2. 几何群的准确结构

置 $P=TU$。R493 已给出其实际单项矩阵；在 $I$ 上为
$$
P_I=
\begin{pmatrix}
0&1&0&0\\
0&0&0&-\omega^2\\
0&0&-\omega&0\\
-\omega&0&0&0
\end{pmatrix}.
\tag{7}
$$
新增的关键是其平方
$$
\mathcal Z=P^2,\qquad
\mathcal Z_I=
\begin{pmatrix}
0&0&0&-\omega^2\\
1&0&0&0\\
0&0&\omega^2&0\\
0&-\omega&0&0
\end{pmatrix}
\tag{8}
$$
在整个几何群中居中。由 (2)、(3)、(8) 逐项相乘，准确有
$$
\boxed{
\mathcal Z^3=I,\quad
\mathcal ZT=T\mathcal Z,\quad
\mathcal ZU=U\mathcal Z,\quad
UTU=T^{-1}\mathcal Z.
}
\tag{9}
$$
因此每个词都能写成
$$
\boxed{T^i\mathcal Z^jU^e,\qquad
0\le i,j<3,\quad e\in\{0,1\}.}
\tag{10}
$$
九个 $T^i\mathcal Z^j$ 不同：非平凡 $T,T^2$ 的选中四维行均有四个非零半单位，而 $\mathcal Z^j$ 是单项矩阵，故 $\langle T\rangle\cap\langle\mathcal Z\rangle=\{I\}$。$U$ 不属于这个阿贝尔子群，因为 (9) 中 $UTU\ne T$。所以 (10) 的十八个矩阵全部不同。

进一步令 $A=T\mathcal Z$。由 (9)
$$
A^3=I,\qquad UAU=A^{-1}.
$$
故 $\langle A,U\rangle\simeq S_3$；其中心平凡，而 $\mathcal Z$ 是独立的三阶中心元。得到
$$
\boxed{G=\langle T,U\rangle\simeq C_3\times S_3,\qquad |G|=18.}
\tag{11}
$$
这是所有长度的词分类，没有只检查一个有限词长后猜测群阶。

### 原来源二维作用也是忠实的

在列基 $(\rho,h)$ 中，(6) 给
$$
T_*=
\begin{pmatrix}0&-\omega\\ \omega&-\omega\end{pmatrix},
\qquad
U_*=\begin{pmatrix}1&0\\1&-1\end{pmatrix},
\qquad
\boxed{\mathcal Z_*=\omega^2I.}
\tag{12}
$$
$\rho,h$ 确实线性独立：$W_*\rho=6\delta\nu_{T_{\rm ar}}\ne0$、$W_*h=0$，且 $Y_*h=\omega^2\nu_S\ne0$。$A_*$ 是标准 $S_3$ 二维作用中的三阶元，$U_*$ 是反射；其像没有非平凡标量。再加上 (12) 的独立三阶标量，作用忠实，仍有十八个不同的算子。

R501 的九十六阶群还含不同的核心/CM 操作，作用于另一完整四态空间；(11) 不替代那个结果。

## 3. 原 Y 的全部六条观测

由 $YT=Y$ 和 (10)，完整轨道恰为
$$
\boxed{Y_{j,e}=Y\mathcal Z^jU^e,\qquad
0\le j<3,\ e=0,1.}
\tag{13}
$$
所有行的 $\xi_2,d_0$ 系数恒为 $2\delta,2$；其余四系数准确如下：

| $(j,e)$ | $\xi_1$ | $\xi_3$ | $x$ | $c$ |
|---|---|---|---|---|
| $(0,0)$ | $\delta$ | $(5+\delta)/2$ | $(5-\delta)/2$ | $1$ |
| $(0,1)$ | $(1-\delta)/2$ | $\delta$ | $(1-3\delta)/2$ | $(1+3\delta)/2$ |
| $(1,0)$ | $(5+\delta)/2$ | $(1-\delta)/2$ | $-2-\delta$ | $(-3+\delta)/2$ |
| $(1,1)$ | $\delta$ | $(5+\delta)/2$ | $-(5-\delta)/2$ | $1$ |
| $(2,0)$ | $(1-\delta)/2$ | $\delta$ | $-(1-3\delta)/2$ | $(1+3\delta)/2$ |
| $(2,1)$ | $(5+\delta)/2$ | $(1-\delta)/2$ | $2+\delta$ | $(-3+\delta)/2$ |

这些半系数均在 $\mathbb Z[\omega]$ 中。六行不同、范数全为 $34$，轨道张成的 $K$ 向量空间维数恰为三。上表按行序的完整 Gram 矩阵为
$$
\begin{pmatrix}
34&20&a&20&\bar a&20\\
20&34&20&a&20&\bar a\\
\bar a&20&34&20&a&20\\
20&\bar a&20&34&20&a\\
a&20&\bar a&20&34&20\\
20&a&20&\bar a&20&34
\end{pmatrix},
\qquad a=13+7\delta.
\tag{14}
$$
精确消元给秩三。轨道—稳定子公式给
$$
\boxed{\operatorname{Stab}_G(Y)=\langle T\rangle.}
\tag{15}
$$
即使只要求 $Yg$ 与 $Y$ 相差一个 CM 单位，稳定子也不扩大：所有行都有同一非零 $d_0$ 系数 $2$，迫该单位为一。

(12) 及 $Y_*h=\omega^2\nu_S$ 给真正边际
$$
\boxed{(Y_{j,e})_*\rho
=\omega^{2j}(-\omega)^e\nu_S.}
\tag{16}
$$
六个系数依次是 $1,-\omega,\omega^2,-1,\omega,-\omega^2$。
这是六个实际不同输出的来源标量，不是默默把输出乘单位后省去 Mellin 归一。

## 4. 原 W 的全部九条观测

由 $WU=W$ 以及 (9) 把 $U$ 移到左端，全部轨道为
$$
\boxed{W_{i,j}=WT^i\mathcal Z^j,\qquad
0\le i,j<3.}
\tag{17}
$$
(2)、(8) 完全指定这些行；附数据列出每个原六维系数。
九行都是 CM 整行、范数全为 $72$，且全部不同，故
$$
\boxed{\operatorname{Stab}_G(W)=\langle U\rangle.}
\tag{18}
$$
同样因固定非零 $d_0$ 系数 $4$，不再有额外的单位比例稳定子。
九行张成的向量空间维数为四。

原 $W_*h=0$ 与 (6) 给
$$
\boxed{
(W_{i,j})_*\rho
=6\delta\,\omega^{2j}a_i\nu_{T_{\rm ar}},
\qquad (a_0,a_1,a_2)=(1,0,-\omega^2).
}
\tag{19}
$$
准确系数除去 $6\delta$ 后为：

| $j\backslash i$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $0$ | $1$ | $0$ | $-\omega^2$ |
| $1$ | $\omega^2$ | $0$ | $-\omega$ |
| $2$ | $\omega$ | $0$ | $-1$ |

三条 $i=1$ 观测的边际恒零，其中 $W_{1,0}=W'$；这不说明其完整联合来源为零。其余六条读取原同一 $T_{\rm ar}$。这些零边际不能用来给任意附带混合条件赋零。

## 5. 六条 Y 轴各有完整原核心

现在使用 R510 已由原 $S$ 绝对定标的 whole 身份
$$
K_{34}=R,\qquad g_\pi\equiv-1\pmod{68},
\tag{20}
$$
其中 $R$ 是第一物理输出反射。对 (13) 中任一整行 $L$，以
$\bar L^{\,t}z$ 改变六个生成变量，六 sigma 的总 theta 度数为
$N(L)=34$；偶半特征、Gaussian 交叉项都与同一标准
$\mathcal S_{34}$ 相符。因此 (20) 适用于这个完整 raw 联合。

这里可明确保全另外五个伴随。因 $L_2=2\delta$ 为当前普通处的单位，对 $j\ne2$ 取
$$
B_j=e_j-\frac{\bar L_j}{\bar L_2}e_2.
$$
它们均与 $L$ 正交，框架 $(L,(B_j)_{j\ne2})$ 的行列式除符号外为
$34/\bar L_2$，在当前处可逆。第一轴的实际 theta 变化方向仍是整的 $\bar L^{\,t}z$，故没有删除伴随上的条件或增加未付的 flat character。

反射与普通收缩合并，准确给
$$
\boxed{
\rho|_{\{L\in p\mathcal O\}}
=\lambda(\mathcal A_L)_*\rho,\qquad
\mathcal A_L
=I-\frac{\kappa+1}{34}\bar L^{\,t}L.
}
\tag{21}
$$
$L\mathcal A_L=-\kappa L$，全部五个 $B_j$ 固定。
矩阵整且 $\det\mathcal A_L=-\kappa$。
这个结论只针对原 raw 六 sigma 来源；不能把它未经覆盖支付地直接推广到 $\eta$ 等 quarter 来源。

## 6. 所有正压深词与完整原算术行

令 $\mathscr L=\mathcal O_p^6$。任取由六个 (21) 组成的正词
$$
M=\mathcal A_{L_1}\cdots\mathcal A_{L_m}.
$$
每层事件都使用上一层的实际逆矩阵，逐层限制得到
$$
\boxed{\rho|_{M\mathscr L}=\lambda^m M_*\rho.}
\tag{22}
$$
不要求这些矩阵交换。$M\mathscr L$ 是原完整像格，判据为
$M^{-1}\xi\in\mathscr L$；它不能被替换成“六条轴分别深若干层”的未移动条件。

结合 (16)、(19)，对整个 Mellin 变量 $u$ 都有
$$
\boxed{
\begin{aligned}
&\int_{M\mathscr L}
 {\bf1}_{Y_{j,e}(M^{-1}\xi)\ {\rm unit}}
 \langle Y_{j,e}(M^{-1}\xi)\rangle^{(p-1)u}\,d\rho\\
&\qquad=\lambda^m\omega^{2j}(-\omega)^eJ_S(u),\\
&\int_{M\mathscr L}
 {\bf1}_{W_{i,j}(M^{-1}\xi)\ {\rm unit}}
 \langle W_{i,j}(M^{-1}\xi)\rangle^{(p-1)u}\,d\rho\\
&\qquad=6\delta\,\lambda^m\omega^{2j}a_iJ_T(u).
\end{aligned}}
\tag{23}
$$
因而原两条中央导数若都为零，(23) 的所有准确移动中央行都为零；$a_1=0$ 的三行则对整个 $u$ 恒零。
也可把 R510 的原 $B_{15}$ 压深加入正词，每出现一次只增加其已付系数 $\chi_{65}$，像格和观察仍按同一个完整 $M$ 读取。

这些身份没有将“只依赖第一轴的测试”扩大成任意附带混管测试。若保五伴随算术行，须使用已有完整第一 CM 投影并逐项运输该测试；若要比较原未移动的 $Y/W/T_c$ 条件，必须计算真实交集及补域。六个 (16) 和六个非零 (19) 依旧只属于原两条固定曲线，不提供新的独立非消失假设。

## 证书与依赖

- [原六输入群、全部轴、Gram 和共同伴随的 BigInt 证书](../scripts/check-r512-original-geometric-group-and-observation-orbits.mjs)；
  [准确数据](../scripts/check-r512-original-geometric-group-and-observation-orbits.json)。
  同一有理/CM 主体已在 V8 实际执行，保存十八个矩阵的唯一性、全部整行与 Gram 秩。数据同时保留后续旋转隐藏轴的完整六维几何，不据其范数给未支付的核心。
- [R493：原 T/U 身份、全部相位和真实网格](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R510：whole 三十四度反射及同源正词公式](R510-original-w2-companion-and-fifteen-axis-central-words.md)。
- [R509：原隐藏耦合与四输入推前边界](R509-original-five-sigma-two-y-frames-and-common-st-source.md)。
- [R501：区别于本几何群的完整来源核心群](R501-whole-cm-exchange-and-identical-five-companion-rows.md)。

主目标仍未完成；继续实际移动域与原补域的比较，不把轨道分类本身当作中央非零。
