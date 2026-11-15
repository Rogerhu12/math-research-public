# R728 — 冻结型5负一行的真实连接源、S34中央与完整近消返回

日期：2026-11-15。**状态：已证明。**

本篇将 R719 斜门 note 的真正首负一行送回一个明确的
$\sigma\otimes\mathcal S_{33}$ 卷积表示。协变导数中的
$\zeta F$ 不被删除：它准确是 $\sigma'\cdot(F/\sigma)$。
原 Y-unit 负一矩中的普通导数项，才由完整 unit 质量为零严格消去。

进一步，两个卷积输入均为单位而总和深 m 的整个近消来源
具有一个准确的两来源返回。它的完整负一 Mellin 行包含
原 $\mathcal S_{34}$ 的中央行；换用 $p^m$ 归一时也显示
全部尺度 log。这里没有把新的正型来源自动认成原 S，
也没有将 native I 与其相反 O 外部补偿分别赋零。

## 1. 规范与两个完整五维空间

沿用 R715、R719 的同一普通射线、固定坏集和整返回，
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad \kappa=p\lambda^2,\quad d_p=p-1 .
\tag{1}
$$
$\Omega$ 是原有界测度的同一普通周期。
对本文每个函数 F，测度规范为
$$
\int e^{Yz/\Omega}\,d\nu_F(Y)=F(z),\qquad
\nu_{F'}=(Y/\Omega)\nu_F .
\tag{2}
$$
$\sigma,x,y$ 均为原规范，$x'=2y$；
$\zeta=\sigma'/\sigma$ 只是该原 sigma 的对数导数，
没有另外选择一个拟周期或 Gaussian 归一。

置
$$
a_j=14-3j,\qquad
F_j=b^j\sigma^{34}x^{a_j},\qquad
\Xi_j=-b^j\sigma^{34}x^{a_j-1}y
\quad(0\le j\le4).
\tag{3}
$$
$F_j$ 的首阶为 $6+6j$。
它们构成原 $\mathcal S_{34}$ 型0的零质量子空间：
整个型0空间为六维，(3) 去掉唯一可能有非零质量的首阶0坐标。
$\Xi_j$ 则构成原 $\mathcal S_{34}$ 型5的整个五维空间，
首阶为 $5+6j$。

这里的完整 degree34 核可直接从 R601(11) 的已付绝对式
$K_{136}=R_YB_{136}$ 下降：
对任意标准 $\mathcal S_{34}$ 截面 F，真正 $[2]$ 拉回 $F(2z)$
的全部二挠 lift 固定，故 $B_{136}F(2z)=F(2z)$。
$[2]$ 在当前处为单位，与 restriction 和物理 $\kappa$ 缩放交换，
于是整个 $\mathcal S_{34}$ 的绝对核就是反射。
所有 $F_j$ 为偶型，
所有 $\Xi_j$ 为奇型，因此
$$
\nu_{F_j}|_{p\mathcal O}
 =\lambda[\kappa]_*\nu_{F_j},\qquad
\nu_{\Xi_j}|_{p\mathcal O}
 =\beta[\kappa]_*\nu_{\Xi_j}.
\tag{4}
$$
这是同一标准 theta 格上的整核，不是仅对某个 Y 边际猜一个相位。
特别
$$
\nu_{F_j}(\mathcal O^\times)
=(1-\lambda)F_j(0)=0 .
\tag{5}
$$

直接对 (3) 求导得
$$
F_j'=34\zeta F_j-2a_j\Xi_j .
\tag{6}
$$
所有 $2a_j$ 的素因子只涉及 $2,5,7,11$；
它们已经在原固定坏集中。
所以 (6) 是两个五维整格之间的精确协变微分关系。

## 2. 任意实际型5差源的唯一正型伙伴

令
$$
D=\sum_{j=0}^4d_j\Xi_j,\qquad d_j\in\mathcal O,
$$
其中系数允许是 R715 的实际 $(\lambda,\kappa,u,\eta)$ 函数，
也允许带同一固定 N 的斜门参数 t。
定义
$$
\boxed{
P=\sum_{j=0}^4\frac{17d_j}{a_j}F_j,\qquad
H=P/\sigma,\qquad G=\zeta P .
}
\tag{7}
$$
由 (6)，
$$
\boxed{P'=34(G-D),\qquad D=G-\frac1{34}P'.}
\tag{8}
$$
P 是原 $\mathcal S_{34}$ 型0的零质量来源；
H 是真正全纯的 odd $\mathcal S_{33}$ 型5来源。
事实上各基函数
$$
H_j=b^j\sigma^{33}x^{a_j}
\tag{9}
$$
在每个格点至少有五阶零，没有因除以 sigma 引入极点或新 flat twist。
其半特征正是原 odd33 半特征。

G 的正确来源是
$$
\boxed{G=\sigma'H.}
\tag{10}
$$
$\nu_{\sigma'}=(c/\Omega)\nu_\sigma$ 是有界测度，
所以 (10) 是完整有界卷积恒等式，而不是删去 $\zeta$ 的形式写法。
本文不把 G 当成另一个标准 $\mathcal S_{34}$ 截面；
其拟周期部分准确由 (8) 保留。

为避免把边际身份误当联合身份，
以下用 $c,z_{33}$ 表示 (10) 的两个**实际卷积坐标**：
$$
\mu_H=\nu_\sigma(c)\otimes\nu_H(z_{33}),\qquad
Y=c+z_{33},\qquad
\rho_H=(c/\Omega)\mu_H .
\tag{11}
$$
于是
$$
Y_*\mu_H=\nu_P,\qquad Y_*\rho_H=\nu_G .
\tag{12}
$$
$c,z_{33}$ 不被认作 R719 原六输入中的全部伙伴。
(12) 可用于所有 Y 测试；若还附原 W、E 或斜门条件，
必须先使用 R719 已付的完整转置，不能在忘却这些伙伴之后重新添门。

## 3. 完整负一 Mellin 行：普通导数与真实连接项

定义
$$
\begin{aligned}
J_P(w)&=\int_{Y\ {\rm unit}}
                   \langle Y\rangle^{d_pw}\,d\nu_P,\\
I_F(w)&=\Omega\int_{Y\ {\rm unit}}
                   Y^{-1}\langle Y\rangle^{d_pw}\,d\nu_F .
\end{aligned}
\tag{13}
$$
这里 $Y^{-1}$ 只在原单位域使用，所有积分均有界。
由 (2)、(8)，对整个 Mellin 变量 w，
$$
\boxed{I_D(w)=I_G(w)-\frac1{34}J_P(w).}
\tag{14}
$$
又由 (10)–(12)，
$$
\boxed{
I_G(w)=
\int_{\{c+z_{33}\ {\rm unit}\}}
 \frac{c}{c+z_{33}}\,
 \langle c+z_{33}\rangle^{d_pw}\,d\mu_H .
}
\tag{15}
$$
这就是原负一行的真实有理单位测试。
分母的 unit cut 与 c、$z_{33}$ 的独立深浅条件同时保留。

由于 P 质量为零且 (4) 给其完整 unit 质量为零，
$$
J_P(0)=0,\qquad
\boxed{I_D(0)=I_G(0).}
\tag{16}
$$
但对中央导数只能说
$$
\boxed{I_D'(0)=I_G'(0)-\frac1{34}J_P'(0).}
\tag{17}
$$
(16) 不能用来删除 (17) 的原正型中央行。
只有实际证明 $P=cS$ 或某个已经识别的完整算术组合以后，
才能相应代入其中央关系。

例如在 (3) 的基中，原 S 准确是
$$
S=F_0-\frac{53}{7}F_1-\frac{12}{7}F_2
                    -\frac{80}{7}F_3-\frac{128}{7}F_4 .
\tag{18}
$$
所以 (7) 是否为 S 的倍数，是五个完整系数的严格条件，
而不是由型、degree、零质量或相同 core 得出的结论。

## 4. 三个原单位分支及未删除的两单位补项

令
$$
h=\chi_{33,p}\lambda,\qquad \chi_{33,p}^2=1
\tag{19}
$$
为 R454 已付的 entire odd33 核。
本篇不猜 $\chi_{33,p}$ 的绝对号。
原两个输入分别满足
$$
\nu_\sigma|_{p\mathcal O}=\beta[\kappa]_*\nu_\sigma,\qquad
\nu_H|_{p\mathcal O}=h[\kappa]_*\nu_H .
\tag{20}
$$
Y-unit 域准确是不交并
$$
\begin{gathered}
\{c\ {\rm unit},z_{33}\in p\},\qquad
\{c\in p,z_{33}\ {\rm unit}\},\\
\{c,z_{33}\ {\rm unit},c+z_{33}\ {\rm unit}\}.
\end{gathered}
\tag{21}
$$
在 $w=0$，(15)、(20) 因而给
$$
\begin{aligned}
I_G(0)
={}&h\int_{c\ {\rm unit}}
       \frac{c}{c+\kappa z_{33}}\,d\mu_H\\
 &+\beta\int_{z_{33}\ {\rm unit}}
       \frac{\kappa c}{\kappa c+z_{33}}\,d\mu_H\\
 &+\int_{\substack{c,z_{33}\ {\rm unit}\\c+z_{33}\ {\rm unit}}}
       \frac{c}{c+z_{33}}\,d\mu_H .
\end{aligned}
\tag{22}
$$
前两项的分母确为单位。
第三项仍是同一来源的完整两单位补项；
不能因前两项存在几何级数就把它删除。
两单位而 Y 深的部分不在 (21) 的原负一单位域中。
下一节给它自己的准确归一来源，并不将它的值赋零。

## 5. 真正两单位近消的完整两来源闭包

在有界来源的二维张成中定义算子
$$
\mathcal A G=\lambda\kappa G+(\beta-\lambda\kappa)D,\qquad
\mathcal A D=\beta D .
\tag{23}
$$
其来源于 (4)、(8) 的**真实** Y 深核。
因为 $\nu_{P'}=(Y/\Omega)\nu_P$，
$$
\nu_{P'}|_{p^m}
=(\lambda\kappa)^m[\kappa^m]_*\nu_{P'} .
$$
结合 D 的 odd 核，逐层得到
$$
\boxed{
\nu_G|_{p^m}
=[\kappa^m]_*
\bigl((\lambda\kappa)^m\nu_G+
      (\beta^m-(\lambda\kappa)^m)\nu_D\bigr).
}
\tag{24}
$$
这不是把协变导数误作乘 Y；
两项都出现在 (24) 中。

对 $m\ge1$ 定义真正的近消来源
$$
\mathscr C_m=
(Y/\kappa^m)_*
\left(
  1_{\{c,z_{33}\ {\rm unit},\,Y\in p^m\}}\rho_H
\right).
\tag{25}
$$
当 Y 深而两个输入不同时为单位时，它们必都属于 p。
后一个分支由 (20) 返回，且 $\rho_H$ 的 c 权多给一个 $\kappa$。
因此在 (25) 的同一总和归一中，
$$
\mathscr C_m
=\mathcal A^m\nu_G-\beta h\kappa\,\mathcal A^{m-1}\nu_G .
\tag{26}
$$
两个被减来源是完整的同域分割；没有把浅 Y 分支或移位分母丢掉。

令
$$
\ell_m=\kappa(\lambda-\beta h)(\lambda\kappa)^{m-1}.
\tag{27}
$$
将 (24) 代入 (26)，再用 (8)，即得
$$
\boxed{
\mathscr C_m=
\beta^m(1-h\kappa)\nu_D+\frac{\ell_m}{34}\nu_{P'} .
}
\tag{28}
$$
这是 (25) 的整个一变量来源身份。
$1-h\kappa$ 是单位；$\lambda-\beta h
=\lambda(1+\chi_{33,p}\lambda)$ 在原射线上也是单位，
故 $v_p(\ell_m)=m$。这些固定单位来自原 R410，
不新增射线条件。

将 (13) 的原负一 Mellin 测试代入 (28)，得到
$$
\boxed{
\begin{aligned}
&\int_{\substack{c,z_{33}\ {\rm unit}\\v_p(Y)=m}}
 \frac{c}{Y/\kappa^m}
 \langle Y/\kappa^m\rangle^{d_pw}\,d\mu_H\\
&\qquad=
\beta^m(1-h\kappa)I_D(w)+\frac{\ell_m}{34}J_P(w).
\end{aligned}}
\tag{29}
$$
左侧是原近消环带上的有界测试。
其负一加权质量为
$\beta^m(1-h\kappa)I_D(0)$，并不因为
$\mathscr C_m$ 的未加权质量为零而自动为零。

(29) 给出一个完整中央联系：
$$
\boxed{
\left.\partial_w\right|_0(29)_{\rm left}
=
\beta^m(1-h\kappa)I_D'(0)+\frac{\ell_m}{34}J_P'(0).
}
\tag{30}
$$
它保持原 P 中央以及全部近消分支，
没有把新负一值或其导数单独认作原 S 中央。

## 6. p 与 kappa 两种归一的完整尺度项

置
$$
v_m=(\kappa/p)^m=\lambda^{2m}\in\mathcal O^\times .
$$
若将 (29) 的观察改成原 $Y/p^m$，则其完整 Mellin 行
$\mathscr K_m^{(p)}$ 与 (29) 左侧 $\mathscr K_m^{(\kappa)}$
准确满足
$$
\boxed{
\mathscr K_m^{(p)}(w)
=v_m^{-1}\langle v_m\rangle^{d_pw}
                 \mathscr K_m^{(\kappa)}(w).
}
\tag{31}
$$
所以中央导数是
$$
\boxed{
(\mathscr K_m^{(p)})'(0)
=v_m^{-1}\left\{
(\mathscr K_m^{(\kappa)})'(0)
+d_p\log\langle v_m\rangle\,
 \beta^m(1-h\kappa)I_D(0)
\right\}.
}
\tag{32}
$$
$\lambda^{2m}$ 的完整单位倒数和尺度 log 都保留。
不能由 $J_P(0)=0$ 删除 (32) 中的负一加权质量。

## 7. 应用于同一原 native 配对，外部仍准确相反

取 R719 斜门 note 的整个型5来源
$$
D=\mathcal D_N(t),\qquad t=\kappa^{n-N},
$$
其系数为已付的同一 q715 或同一 $\zeta$ 的
$d_{j,N}(t)$。按 (7) 得到 $P_N(t),H_N(t),G_N(t)$。
(14)–(32) 对每个固定 p、N、t 都是完整恒等式，
不需要一个新的测试或新的数值逆矩阵。

特别该 note 的偶步提取式(30)中，
冻结首项可以准确写为
$$
I_{\mathcal D_N(0)}(0)
=
\int_{\{c+z_{33}\ {\rm unit}\}}
  \frac{c}{c+z_{33}}\,d\mu_{H_N(0)} .
\tag{33}
$$
它也可由任一真实两单位近消环带 (29) 除以单位
$\beta^m(1-h\kappa)$ 读取。
(22) 的两混合深支和完整两单位 Y-unit 补项仍保原样。

这种读取并未把新卷积坐标的环带认作原六输入的 W/E 角域。
原斜门已经通过完整 joint 返回后，才使用 (33) 的 Y 来源身份。
原 native 的整个配对 T 行仍满足
$$
\mathcal O^T_{\rm pair}=-\mathcal I^T_{\rm pair},
\qquad
\mathcal V^T_{\rm pair}=\mathcal X^T_{\rm pair}=0 .
\tag{34}
$$
所以本篇不从 (29) 或 (33) 单独宣称原 $J'_T$ 非零。
若要把 (30) 的 $J'_{P_N(t)}$ 换成原 S 中央，
仍必须支付 (18) 的完整来源条件及其同一个单位测试。

本篇没有新增数值执行或可重算输出。
它支付的新增接口是：整个五维型5负一行的正确连接项、
真实 sigma/odd33 卷积的完整单位分区、
(28) 的所有近消层来源闭包，以及
(29)–(32) 中原 S34 中央、负一质量和尺度 log 的同时保留。

主要依赖：
[R715](R715-complete-first-z-source-and-fifty-neutral-returns.md)；
[R601](R601-original-q-tensors-complete-y-w-cores-and-fifteen-source-spectrum.md)；
[R719](R719-native-second-fibre-and-exact-mixed-source-relation.md)；
[两斜门完整 note](../notes/2026-11-15-two-adjacent-s-slanted-cores-and-native-pair.md)；
[R713](R713-symmetric-frozen-sources-and-exact-paired-mixed-remainder.md)；
[R454](R454-original-odd33-core-and-exact-residual-slope-transport.md)；
[R410](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)。
