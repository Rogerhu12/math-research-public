# R682 — 同八角域的第二算术观察、完整三次项与统一有限单位差

日期：2026-11-15。**状态：已证明。**

本篇继续 R678 的同八个原角域，完整计算第二套
$q_{1,N}^\dagger/S_1/T_1$ 的相对行。
同一组有界差商系数没有消掉这第二行；
原 $x^2/y$ 项和深度奇偶必须保留。

把两套实际行按一个明确的整系数组合，
其三次项中的原负一矩准确抵消，
剩余由同一 pair 的正二矩给出单位首项。
这个组合的**原全 S/T 返回系数仍为单位**，
所以全部外部补偿也在同一算术式内。
没有据有限角域非零给主目标作结论。

## 1. 同一来源和八个有限原角域

保持 R674/R678 的原子族、原 ray、固定坏集、
同一个 $N\in4\mathbf Z_{\ge1}$ 与 $q_N^\dagger$。
取 $M\ge2$，r 偶，先要求 $r>N+M+3$。
沿用 R678 的
$$
k_m=r+m,\qquad n_j=r+M+j,\qquad
x=\kappa^r,\quad z_m=\kappa^m,\quad t_j=\kappa^{M+j},
$$
$$
\mathcal D_{r,m,j}
=\{A\in p^{2r},\ Q\in p^{k_m}\mathbf Z_p^\times,\
L\in p^{n_j}\mathbf Z_p^\times\},
\quad m=0,1,\quad j=0,1,2,3 .
\tag{1}
$$
八个域互不相交，并准确满足
$Y_0$ 环带 $k_m$、$Y_1$ 环带 $n_j$、$c,d$ 环带 $k_m$。
所有完整来源和伙伴均使用 R678(2) 的实际返回，
标量为 $\lambda^{2r}\beta^{k_m+n_j}$，$\beta=-\lambda$。

记
$$
\mathfrak c=\frac{b_Q-b_Y}{b_Y}
=\frac{348}{349}+\frac{1479}{1745}\omega,\qquad
h=\frac{b_L}{b_Y},\qquad
\mathfrak d=\frac{1-b_Y}{b_Y}.
\tag{2}
$$
$\ell_0,b_F,a,g,b_Y$ 沿用 R678。
令
$$
q_{1,N}^\dagger=q_N^\dagger\circ J^{-1},\qquad
J(c,d)=(d,-c).
$$
这是原真实旋转测试；$J_*\mu_0=-\mu_0$。
它不是在同一角域上任意更换 q。

在返回域
$$
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\},
\qquad Q,L\ {\rm unit},
$$
第二套完整权是
$$
\boxed{
q_{1,N}^\dagger\circ B_{r,m,j}
=1_{\mathcal G_*}
 \frac{\widehat P^\dagger
  \bigl(X_*+[x(-\ell_0z_mQ+b_Ft_jL)+a x^2A]v_N\bigr)}
      {b\Omega^6}.
}
\tag{3}
$$
$X_*,v_N$ 与 R678 相同，$v_N=(\kappa^{-N},1,g)$；
完整实际右逆及所有高层项保持。

令 $\varepsilon_j=(-1)^{M+j}$。返回后的第二套观察准确为
$$
S_{1,m,j}=\varepsilon_j(L+x t_j^{-1}A),
$$
$$
T_{1,m,j}=b_YS_{1,m,j}
 +x\{-b_Lz_mQ+(b_Q-b_Y)t_jL\}
 +(1-b_Y)x^2A .
\tag{4}
$$
这里 $x t_j^{-1}=x^2/y_j$，没有将它省去。
两个原单位 cut 在 (1) 上都准确成立。

第二套实际相对 log 因而是
$$
\boxed{
\ell_{1,m,j}(x)=
\log\left(
1+\varepsilon_j
 \frac{x(\mathfrak c t_j-hz_mQ/L)
          +\mathfrak d x^2A/L}
      {1+x t_j^{-1}A/L}
\right).
}
\tag{5}
$$
(3)–(5) 包含真实权差和观察差。
它不是 R678 中固定同一解析 y 函数的三阶差商：
这里 $\varepsilon_j$ 随 j 变，分母还含 $t_j^{-1}$。

## 2. 第二个实际有界行及完整质量

用第二套原 q 和观察，在 (1) 上定义
$\mathcal K^{1,S}_{r,m,j}$、$\mathcal K^{1,T}_{r,m,j}$。
保持 R678 的同一整权 $\alpha_j$：
$$
D_\kappa=(1-\kappa)(1-\kappa^2)(1-\kappa^3),\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\frac{(\kappa^3,-\kappa-\kappa^2-\kappa^3,
                  1+\kappa+\kappa^2,-1)}{D_\kappa}.
$$
置
$$
\boxed{
\mathcal B^{1,Z}_{r,M}(w)=
\sum_{j=0}^3\alpha_j\lambda^{-2r}
 \{\beta^{-r-n_j}\mathcal K^{1,Z}_{r,0,j}(w)
  -\beta^{-r-1-n_j}\mathcal K^{1,Z}_{r,1,j}(w)\}.
}
\tag{6}
$$
以 $\mathcal B^{0,Z}$ 表示 R678 的第一套行，并记
$$
\mathfrak B^i_{r,M}=
\frac1{d_p}\left.
\partial_w\{\mathcal B^{i,T}_{r,M}
       -\langle b_Y\rangle^{d_pw}\mathcal B^{i,S}_{r,M}\}
\right|_{w=0}.
\tag{7}
$$

两个单位限制保持 pair 的共同 $\mu_6$ 旋转。
原六次权中的 $Q^aL^b$ 质量只允许 $a+b=2$，
所以 (3) 的完整质量作为 y 的多项式次数至多二。
$\varepsilon_j$ 不进入零阶质量。
同一 $\alpha$ 准确给
$$
\boxed{
\mathcal B^{1,S}_{r,M}(0)=
\mathcal B^{1,T}_{r,M}(0)=0.
}
\tag{8}
$$
第一套也由 R678 已有相同结论。
因此 (7) 中的尺度 log 质量已完整支付。

## 3. 低于三次的全部项为何严格消失

令 $F_{m,j}(x)$ 为 (3) 的完整权乘 (5) 后的返回积分。
其常数为零。下面逐项支付一次、二次以及三次中可能出现的
$A$ 分母项，不能仅凭一个形式首项舍去它们。

原 $\nu_4$ 的共同 $\mu_6$ 角型为四；
$\mathcal G_*$ 保持该旋转。
对 $\widehat P^\dagger$ 作 j 阶导数后，其第一四输入次数为 $6-j$。

在权中选 $a_q$ 个 $a x^2A$ 因子，
在 log 的分子、分母合计选 $a_\ell$ 个 A 因子，
则第一四输入总次数为
$$
6-j+a_q+a_\ell .
$$
总 x 次数至多三时，满足该次数同余四的唯一可能是：
$$
\boxed{
j=2,\qquad a_q=a_\ell=0,\qquad
\text{log 只取一次线性项。}
}
\tag{9}
$$
附脚本完整枚举分子中 x、$x^2A$、
分母中 $xA/t_j$ 以及 log 各次幂：
38 个其余低阶项全部被真实角型杀掉，
六个保留单项式恰为 (9)。

所以
$$
[x^0]F_{m,j}=[x^1]F_{m,j}=[x^2]F_{m,j}=0.
$$
三次项只用
$$
\mathcal J_N=
\int_{\mathcal G_*}
 \frac{\partial_{v_N}^2\widehat P^\dagger(X_*)}{2b\Omega^6}\,d\nu_4
=\frac{J_N^\dagger}{\ell_0^2}
=\frac{\lambda^N\kappa^{-2N}}{2b\Omega^2}.
\tag{10}
$$
最后一个等式来自 R674 的完整实际归一，
没有重新以低阶近似替换原 carry。

## 4. 三次项的完整 pair 收缩

所有以下矩都在同一个 $Q,L$ 双单位域上。记
$$
M_{20}=\int Q^2\,d\nu_{\rm pair},\quad
M_{11}=\int QL\,d\nu_{\rm pair},\quad
R_{31}=\int Q^3L^{-1}\,d\nu_{\rm pair}.
$$
R653/R665 的整个五项 S5 分离与 whole odd5 核给
$$
\boxed{
\begin{aligned}
M_{20}&=4\Omega^2(1-\beta)(1-\beta\kappa^2),\\
M_{02}&=-M_{20},\\
M_{11}&=3\Omega^2(1-\beta\kappa)^2,\\
R_{31}&=36b\Omega^3(1-\beta\kappa^3)I_{\Sigma_5,-1}.
\end{aligned}}
\tag{11}
$$
这里 Q 的正三矩是单位正矩，L 的负一已经是单位积分。
原 period、方向和 Euler 因子全部保持。

置两个固定常数
$$
\boxed{
C_a=\mathfrak c\ell_0^2+2h\ell_0b_F,\qquad
C_b=-2\mathfrak c\ell_0b_F-hb_F^2 .
}
\tag{12}
$$
把
$(-\ell_0zQ+b_FtL)^2(\mathfrak c t-hzQ/L)$
逐项对 (11) 收缩，得到完整三次系数
$$
\boxed{
[x^3]F_{m,j}
=\varepsilon_j\mathcal J_N
 \{-h\ell_0^2z_m^3R_{31}
   +C_at_jz_m^2M_{20}
   +C_bt_j^2z_mM_{11}
   -\mathfrak c b_F^2t_j^3M_{20}\}.
}
\tag{13}
$$
最后一个项也保留；它只在准确作 m=0 减 m=1 后才相消。

令
$$
A_\kappa(z)=\sum_{j=0}^3\alpha_jz^j
=-\frac{(z-1)(z-\kappa)(z-\kappa^2)}{D_\kappa}.
$$
三个真实交错和为
$$
\boxed{
\begin{aligned}
A_\kappa(-1)&=\frac{2(1+\kappa)(1+\kappa^2)}{D_\kappa},\\
A_\kappa(-\kappa)&=\frac{2\kappa^2(1+\kappa)^2}{D_\kappa},\\
A_\kappa(-\kappa^2)&=\frac{2\kappa^3(1+\kappa)(1+\kappa^2)}{D_\kappa}.
\end{aligned}}
\tag{14}
$$
因此
$$
\boxed{
\begin{aligned}
[x^3]\mathfrak B^1_{r,M}
=(-1)^M\mathcal J_N\{&
-h\ell_0^2(1-\kappa^3)A_\kappa(-1)R_{31}\\
&+C_a\kappa^M(1-\kappa^2)A_\kappa(-\kappa)M_{20}\\
&+C_b\kappa^{2M}(1-\kappa)A_\kappa(-\kappa^2)M_{11}\}.
\end{aligned}}
\tag{15}
$$
左边表示把同一实际行按 x 展开后的三次系数，
最后仍代 $x=\kappa^r$。
它有三个完整项，不能只留下原负一矩。

## 5. 保 $x^2/y$ 的统一高阶界

对每个固定 m、j，置
$$
R_0=N+M+3 .
$$
(3)、(5) 的完整表达准确满足
$$
F_{m,j}(\kappa^{R_0}X)\in\mathcal O[[X]] .
$$
权的逆 $\kappa^N$ 已由 $\kappa^{R_0}$ 支付；
最坏观察分母是 $t_3^{-1}=\kappa^{-M-3}$，
所以其修正仍有至少 $p^N$。
所有 log 分母也由这些正深度支付。

由 (9)，低于三次的项为零；故在 $r>R_0$ 时，
(15) 的完整余项严格为
$$
\boxed{
\mathfrak B^1_{r,M}
=x^3 U_{N,M,p}+p^{4r-4N-4M-12}\mathcal O,
}
\tag{16}
$$
其中 U 就是 (15) 的完整显示系数。
这包括所有来自 $x^2/y$、$a x^2A$、
高 log 幂及原六次权的剩余项。

R678 的第一套真实行同样给
$$
\boxed{
\mathfrak B^0_{r,M}
=\kappa^{3M+3}x^3
 \{2hJ_N^\dagger R_{31}\}
 +p^{4r+3M+3-4N}\mathcal O .
}
\tag{17}
$$
(16)、(17) 都是有限层估计，
不是分别取不同极限后的源比较。

## 6. 同一实际八角域上取消负一三次项

设
$$
U_\kappa=\frac{1+\kappa^2}{(1-\kappa)^2},\qquad
\sigma_M=(-1)^{M+1}U_\kappa .
$$
准确恒等式
$$
\frac{(1-\kappa^3)A_\kappa(-1)}2=U_\kappa
$$
使下列**整且有界的实际组合**
$$
\boxed{
\mathfrak D_{r,M}
=\kappa^{3M+3}\mathfrak B^1_{r,M}
       -\sigma_M\mathfrak B^0_{r,M}
}
\tag{18}
$$
在三次项中准确取消 $R_{31}$。
这是同八角域的两套原算术观察的组合，
没有把一个新的裸矩插入当前测试。

将 (10)、(11)、(14) 的全部正矩项代回，
得到完整主式
$$
\boxed{
\begin{aligned}
\mathfrak D_{r,M}
={}&
\frac{(-1)^M\lambda^N
       \kappa^{3r+4M+5-2N}}
     {b(1-\kappa)(1-\kappa^3)}
 \Bigl[
 4C_a(1+\kappa)^2(1-\beta)(1-\beta\kappa^2)\\
&\hspace{31mm}
 +3C_b\kappa^{M+1}(1+\kappa^2)(1-\beta\kappa)^2
 \Bigr]
+p^{4r-4N-M-9}\mathcal O .
\end{aligned}}
\tag{19}
$$
括号中两个项都保留；尾界来自
$\kappa^{3M+3}$ 乘 (16) 以及 (17)，取两者较弱的共同界。
只有三次项中的负一部分被消去，
完整高阶积分并未因此赋零。

固定常数准确为
$$
\boxed{
C_a=\frac{16623+110820\omega}{43625}
=\frac{3\cdot1847(3+20\omega)}{125\cdot349},
\qquad
C_b=\frac{54796+55860\omega}{43625}.
}
\tag{20}
$$
且
$$
N(C_a)=\frac{9\cdot1847^2}{5^6\cdot349}.
$$
1847、349 均为素数，模64分别为55、29，
故原 $p\equiv7\bmod64$ 射线已经排除它们。
所以 $C_a$ 是单位，$C_b$ 整，不需增添射线或新密度条件。
原 R410 还给 $1-\beta=1+\lambda$ 单位。

因此 (19) 的括号模 p 恰为 $4C_a(1-\beta)$，是单位。
只要
$$
\boxed{r\ \text{为偶数},\qquad r>2N+5M+14,}
\tag{21}
$$
主项严格支配完整尾部，得到
$$
\boxed{
v_p(\mathfrak D_{r,M})=3r+4M+5-2N .
}
\tag{22}
$$
这里的深度门不依赖原负矩的赋值：
它来自同一实际行的准确三次消去和正二矩。

一个统一有限选择是
$$
M=2,\qquad r=2N+26.
$$
此时 (22) 为 $4N+91$。
特别取 $N=4$，原八角域恰为
$$
A\in p^{68},\qquad
Q\in p^{34}\mathbf Z_p^\times\ \text{或}\ p^{35}\mathbf Z_p^\times,
\qquad
L\in p^{36},p^{37},p^{38},p^{39}\ \text{的相应单位环带},
$$
同一个实际有界组合的相对中央行准确赋值107。

## 7. 两套全算术行和全部外部的同步组合

第一套已有 R678 的完整外部
$\mathcal E^{0,Z}_{r,M}$ 和共同单位系数
$$
c_0=2\lambda^{-2r}\beta^{N-r-M}A_\kappa(\beta^{-1}),
$$
$$
\mathcal B^{0,S}+\mathcal E^{0,S}=c_0J_S,\qquad
\mathcal B^{0,T}+\mathcal E^{0,T}=6\delta c_0J_T .
\tag{23}
$$

第二套由真实 J 旋转的原全行给
$$
(\mathcal F^{1,S}_{n_j},\mathcal F^{1,T}_{n_j})
=-\lambda^{n_j}\beta^N(J_S,6\delta J_T).
$$
这里 S 的原域是 $Y_1$ 环带 $n_j$，
T 的原域是 $Y_1$ 深 $n_j$ 配自己的完整移动 W 单位观察。
在 (6) 中逐项以该全行减去相应角域，定义
$\mathcal E^{1,Z}_{r,M}$。
其真实集合差、原 $q_1$ 和所有 Q/A/W 失败支均保留。

因为
$\beta^{-n_j}\lambda^{n_j}=(-1)^{M+j}$，
完整系数准确为
$$
\boxed{
c_1=(-1)^{M+1}\lambda^{-2r}\beta^{N-r}
       (1-\beta^{-1})A_\kappa(-1),
}
\tag{24}
$$
$$
\boxed{
\mathcal B^{1,S}+\mathcal E^{1,S}=c_1J_S,\qquad
\mathcal B^{1,T}+\mathcal E^{1,T}=6\delta c_1J_T .
}
\tag{25}
$$
$c_1$ 是单位；这里没有把 $n_j$ 的交错符号漏掉。

对 Z=S,T 同时作
$$
\mathcal D^Z=\kappa^{3M+3}\mathcal B^{1,Z}
                 -\sigma_M\mathcal B^{0,Z},\qquad
\mathcal X^Z=\kappa^{3M+3}\mathcal E^{1,Z}
                 -\sigma_M\mathcal E^{0,Z}.
$$
令
$$
\boxed{c_D=\kappa^{3M+3}c_1-\sigma_Mc_0.}
$$
由于第一项严格深、第二项为单位，$c_D$ 是单位。
于是完整 Mellin 身份为
$$
\boxed{
\mathcal D^S+\mathcal X^S=c_DJ_S,\qquad
\mathcal D^T+\mathcal X^T=6\delta c_DJ_T .
}
\tag{26}
$$
(18) 正是 $\mathcal D^T-\langle b_Y\rangle^{d_pw}\mathcal D^S$
的 $d_p^{-1}$ 中央导数。

(8)、R678 的零质量和原 $J_S(0)=J_T(0)=0$ 给
所有显示的**完整加权行**零质量。
因此尺度 $\log\langle b_Y\rangle$ 在 (26) 中准确处理，
而不是事后忽略。

若原两个中央导数同时为零，(26) 留下的确切关系是
$$
\boxed{
\frac1{d_p}\left.
 \partial_w\{\mathcal X^T(w)
       -\langle b_Y\rangle^{d_pw}\mathcal X^S(w)\}
\right|_{w=0}
=-\mathfrak D_{r,M},
}
\tag{27}
$$
右边的准确赋值为 (22)。
这支付同八角域两原算术观察的完整非齐次比较；
它没有证明完整外部左边为零。

## 8. 范围

本篇没有用角型省略第二观察的 $x^2/y$，
也没有用同域替换 q。
三次以下的消去由 (9) 的真实第一四输入角型支付；
三次项中的四个 pair 项先全部列出，再按真实 m/j 权相消；
所有高项由统一有限层估计保留。

原外部必须继续按 (23)–(27) 的不同 q 和单位 cut 处理。
已新增的是：它们现在被同一有限有界算术测试迫出一个
统一、准确的非零赋值，而无需新增辅助来源或猜测 log 导数。
尚无将 (27) 的完整外部消掉的证明，主目标仍未完成。

## 精确文件

- [check-r682-opposite-corners-and-uniform-unit-difference.js](../scripts/check-r682-opposite-corners-and-uniform-unit-difference.js)
- [check-r682-opposite-corners-and-uniform-unit-difference.json](../scripts/check-r682-opposite-corners-and-uniform-unit-difference.json)

证书精确核全部低阶允许项、完整三次 pair 多项式、
三个交错权、负一系数的准确取消、两条正矩 Euler 简化，
以及固定 $C_a$ 的范数和旧射线排除。共有23条准确检查。
它没有用取样代有限层误差或原全算术返回。

主要依赖：
[R674](R674-original-double-s-arithmetic-adaptation-and-negative-one.md)；
[R678](R678-original-finite-word-corners-and-negative-one-return.md)；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)。
