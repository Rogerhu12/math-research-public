# R933 — 原首 Frobenius 系数的实际倍点读取与第六 Gaussian 块

日期：2026-11-20。**状态：下述同原严格低输入到首Frobenius系数的单位恒等式已证明；root/deep全文独审。未执行数学计算，未证明四中央联合非零。**
本注只补 R887 §19 中尚以共同数保留或消去的实际
$f_p=c_2(p)$。R711/R714 已有第六 Cartier 的有限部、
$7\kappa _5 a_m^+$ 坐标项及 $L_{m,5}/p^6$ 的完整必要式；
这些不是本注的新结论，也不在此重做。

## 1. 同一个原 sigma 与严格低输入

固定共同模型 $y^2=x^3+1$、$D_zx=2y$、
$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$，以及

$$
p=6s-1>211,\qquad w=z^6,\qquad
c=[w^s]\log(\sigma/z),\qquad
U(w)=\frac{\sigma(z)}z e^{-cw^s}.
\tag{1}
$$

这是 R708/R887 的原首 Gaussian，取 R929 的 $\Delta=0$，
不另选提升。设

$$
W(w)=z^2x(z),\quad Y(w)=-z^3y(z),\quad
f(w)=U(w)^{-2},\qquad \theta=w\frac d{dw}.
\tag{2}
$$

R614 的直接 $U/W$ 整窗包含 $w^{\le p}$，因为
$p<(p^2-1)/6$。这些都是常数一的整单位；以下系数可以先在
特征零中读取，再按需要约化。记

$$
W_{<p}=\sum_{i=0}^{p-1}W_iw^i,\quad
f_{<p}=\sum_{i=0}^{p-1}f_iw^i,\quad
Y_{<p}=(1-3\theta)W_{<p},\quad
Q_p(2)=\frac{2^{p-1}-1}{p}\in\mathbf Z.
\tag{3}
$$

这批严格低系数始终来自同一原整来源。若按 R929 的输入取得它们，
用同一个整反函数 $t=t(w)$ 及 $\Delta=0$，准确有

$$
f(w)=W(w)\left\{
\frac{g(t(w))}{1+8t(w)}\right\}^{-1/17}.
$$

指数 $-1/17\in\mathbf Z_p$，常数一的原二项式分支保持整性和
所需两位精度；$pc=a_\kappa/34$ 亦由 R929 的实际常数读取。
因此这里没有默添一份独立的 sigma 高精度输入。

## 2. 实际 $W_p$ 和 $f_p$ 的两个单位方程

定义两个完全指定的低卷积

$$
A_p=[w^p](Y_{<p}^{\,2}-W_{<p}^{\,3}),
\tag{4}
$$

$$
D_p=[w^p]\left\{
f_{<p}^{\,4}Y_{<p}^{-2}
\sum_{k=0}^{5}\frac{(8pcQ_p(2))^k}{k!}w^{ks}
\right\}.
\tag{5}
$$

所有负幂都取常数一单位的真实形式逆，保全部卷积。
$pc$ 整且为单位；$k!$ 在本范围也均为单位。

**命题。** 在特征零中准确有

$$
\boxed{
(1+6p)W_p=A_p,\qquad
(64^p-4)f_p=D_p-2(1-3p)W_p.
}
\tag{6}
$$

两个分母在当前 $p$ 都是单位。特别在原剩余域中

$$
\boxed{
\overline W_p=\overline A_p,\qquad
\overline f_p=(\overline D_p-2\overline A_p)/60.
}
\tag{7}
$$

**证明。** 由原微分及曲线方程，

$$
Y=W-3wW',\qquad Y^2=W^3+w.
\tag{8}
$$

在 $w^p$ 处，$Y_p=(1-3p)W_p$；两侧的首未知系数分别
为 $2(1-3p)W_p$ 和 $3W_p$。因 $p>1$，单项式 $w$
不贡献。移项即得 (6) 第一式，符号为正的 $1+6p$。

原绝对倍点身份是 R812(3) 的

$$
\sigma(2z)=-2y(z)\sigma(z)^4.
$$

把 (1) 的同一 Gaussian 同时代入两边，准确得

$$
U(64w)=Y(w)U(w)^4
\exp\{-c(2^{p+1}-4)w^s\}.
$$

$2^{p+1}-4=4pQ_p(2)$，因此倒平方给

$$
\boxed{
f(64w)=f(w)^4Y(w)^{-2}
\exp\{8pcQ_p(2)w^s\}.
}
\tag{9}
$$

这里的正号、因子八及同一个 $pc$ 都由实际 Gaussian 给出。
在次数 $p=6s-1$，指数的贡献恰只到 $k=5$；不能把该指数
先约成一。右边 $f_p$ 的系数为四，$Y_p$ 的系数为负二，
其余项准确为 (5)。这证明 (6) 第二式。
最后 $1+6p\equiv1$、$64^p-4\equiv60\pmod p$，证明 (7)。

本命题没有给未知 Frobenius 常数自由赋值。若输入已知模
$p^a$，(4)–(6) 以整单位运算给同一实际 $W_p,f_p$ 模 $p^a$；
这里只要求同时保 $pc$ 与实际 $Q_p(2)$ 的该精度。
R929 给出的整两位输入因而可直接使用，未在指数计算中损一位。

在单模 $p$ 时还可直接使用**已经登记**的 R615(21)：
$W_{pk}\equiv-W_k^p/(6k-1)$ 对 $1\le k<s$ 成立。
原 $W_1=-1/7$，所以

$$
\overline A_p=\overline W_p=1/35,\qquad
\overline f_p=(\overline D_p-2/35)/60.
\tag{9a}
$$

这个 $W_p$ 常数不是新结论；(6) 第一式同时保留它所需的
特征零低卷积及高精度读法。

## 3. 四个原第六块的直接读取

保 R647/R821/R923 的全部原有限多项式 $P_\nu$，规范为
$P_\nu(0)=1$。四个 charge 是

$$
(n_S,n_T,n_U,n_V)=(17,36,68,33),\qquad m_\nu=2n_\nu.
$$

在共同 $b=1$ 模型，原来源逐字为

$$
\mathscr G_\nu(w)
=w f(w)^{-n_\nu}W(w)^{n_\nu-3}
P_\nu\!\left(\frac w{W(w)^3}\right).
\tag{10}
$$

这只是原 $\sigma^{m_\nu}\phi_\nu$ 的有限分子表示。
第四来源同样使用 R923(1) 的完整多项式，不按 degree 另选来源。
定义

$$
C_{\nu,p}=[w^p]\left\{
f_{<p}^{-n_\nu}W_{<p}^{n_\nu-3}
P_\nu\!\left(\frac w{W_{<p}^{3}}\right)\right\}.
\tag{11}
$$

因 $6s=p+1$，真正的第六 Gaussian 块是
$g_{\nu,6}=[w^{p+1}]\mathscr G_\nu$。完整幂展开给

$$
\boxed{
g_{\nu,6}=(n_\nu-3)W_p-n_\nu f_p+C_{\nu,p}.
}
\tag{12}
$$

确实，$W_p$ 在 $W^{n_\nu-3}$ 中的线性系数是 $n_\nu-3$，
$f_p$ 在 $f^{-n_\nu}$ 中的线性系数是 $-n_\nu$；
$P_\nu(w/W^3)-1$ 从 $w$ 起，所以其所需 $W$ 输入严格低于 $p$。
两个高系数的乘积从 $w^{2p}$ 起，不进入 (12)。
这证明的是同原系数的特征零等式。

把 (7) 代入，获得只用严格低数据的实际四行

$$
\boxed{
\overline g_{\nu,6}
=\overline C_{\nu,p}
+\frac{31n_\nu-90}{30}\overline A_p
-\frac{n_\nu}{60}\overline D_p.
}
\tag{13}
$$

使用 (9a)，同一式也准确为
$\overline g_{\nu,6}=\overline C_{\nu,p}+(n_\nu-3)/35
-n_\nu\overline f_p$。例如两行的真正共同高项消去式是
$4\overline g_{S,6}-\overline g_{U,6}
=4\overline C_{S,p}-\overline C_{U,p}-9/35$；
这里的固定常数不可以省去。

没有新的有理模型误差。若仍使用 R711/R714 的 Cartier 行，
则 R887(106) 给原误差的具体值

$$
\boxed{
\eta_p=e_{2,p}=\overline f_p-\kappa _5\overline f_s
=\frac{\overline D_p-2\overline A_p}{60}
-\kappa _5\overline f_s.
}
\tag{14}
$$

由此可直接回填它们的既有公式；不重定义有限部，也不删
$7\kappa _5a_m^+$。R887 §19 先前支付的是若干模型差中
共同 $f_p$ 的消去，(6)/(14) 支付这个数自身的实际读取。

## 4. 同原中央除商与物理尺度

R711(18) 已准确说明，若原 $j_\nu=0$，则

$$
B_{\nu,6}=L_{\nu,5}/p^6\in\mathcal O,\qquad
\overline g_{\nu,6}=
\frac{\overline{\gamma_\nu}^{\,6}}{120}\overline B_{\nu,6},
\quad \gamma_\nu=m_\nu pc.
\tag{15}
$$

所以本次读取对中央的实际用途，是将 (13) 作为 (15) 左边的
完整值；右边原低部分和的真实除 $p^6$ 商仍在。
四个中央同时零时，举例有精确的两个必要式

$$
3\overline g_{S,6}+16\overline g_{T,6}-19\overline g_{V,6}
=3\overline C_{S,p}+16\overline C_{T,p}-19\overline C_{V,p},
$$

$$
35\overline g_{S,6}+16\overline g_{U,6}-51\overline g_{V,6}
=35\overline C_{S,p}+16\overline C_{U,p}-51\overline C_{V,p}.
\tag{16}
$$

两式的系数分别同时杀掉常数向量和 charge 向量，因而杀掉
(12) 的两个共同高系数。它们本身是恒等式；在中央零假设下
必须把每个 $\overline g_{\nu,6}$ 按 (15) 换成真实除商，
不能把左边直接设为零。第一/二位的 R929 输入并未支付 (15) 的完整高精度除商。
准确计算 $B_{\nu,6}\bmod p$ 要先知道 $L_{\nu,5}\bmod p^7$，
等价于知道 $L_{\nu,5}/p$ 的六位，而非只知道 $L_{\nu,5}\bmod p^6$。
在没有另付逐项整除时，一组充分输入是
$g_{\nu,h}\bmod p^{7-h}$（$1\le h\le5$）及
$\gamma_\nu\bmod p^6$；所有项合并后才作实际除 $p^6$。

返回物理 $b$ 时，仍是 R929 §7 的同一运输

$$
g_{\nu,h}^{(b)}=b^{sh-1}g_{\nu,h}^{(1)},\quad
\gamma_\nu^{(b)}=b^s\gamma_\nu^{(1)},\quad
j_\nu^{(b)}=b^{-1}j_\nu^{(1)}.
$$

第四来源另外保 R923 的 $-17/11$。本注未证明 (13) 的某个
指定值非零，未推出中央零到 R708/R923 的全边界前缀零。
它完成的是同一个原首 Frobenius 输入的读取，不是又添一个
任意可选的 CM 运输来源或中央条件。

依赖：R614 原整窗、R615 已登记的原 p 倍指标同余；R647/R821/R923 原全部有限分子；
R812(3) 原绝对二倍点常数；R887(104)–(106) 的同原初值；
R711/R714 已有第六 Cartier/中央必要式；R929 原两位输入。

原入口：[R929](R929-original-hypergeometric-two-digit-blocks-and-gaussian-prefix.md)、[R887](R887-original-z-all-cm-transport-and-exact-hasse-normalization.md)、[R923](R923-original-v66-complete-boundary-trace-and-fixed-denominator.md)。

## 附录 A：同 W 的真实六位中央部分和与规范二倍点 carry

日期：2026-11-20。**状态：精确恒等式与完整精度已证明；root/deep全文独核原H端点、全部卷积、完整高尾及规范二倍点carry。未执行数学计算。**

本附录接 R933，而不重登 R614 的整窗、R615 的 Cartier 身份、
R711 的第六中央必要式或 R812 的二倍点分布关系。
新增支付的是：只从同一原椭圆级数 W 的严格低系数，完整恢复
L_{ν,5} mod p^7 所需的真实输入；随后在 S/U 的联合第六行中，
逐项保留同 charge 来源 B 和二倍点的低部分和 carry。
固定常数 −9/35 因此落在一个完全指定的有限检验中，
不被单独宣称为非消失证明。

### A.1 同一原 W 决定严格低 Gaussian 的全部精度

沿用 R933 的共同 b=1 模型与原首 Gaussian：

$$
p=6s-1>211,\qquad w=z^6,\qquad
W=z^2x,\qquad c=[w^s]\log(\sigma/z),
$$

$$
U_\sigma=(\sigma/z)e^{-cw^s},\qquad f=U_\sigma^{-2}.
\tag{A1}
$$

这里 U_σ 是 sigma 的整单位；来源 U 仍专指原 E_{2312} 的
完整 degree 136 来源。所有等式先在特征零中成立，再约化到同一
原数域的整剩余环；不另选 Gaussian 提升。

由原 Dζ=−x、ζ=D log σ，已知的精确系数式是

$$
[w^n]\log(\sigma/z)=-\frac{W_n}{6n(6n-1)}.
\tag{A2}
$$

因 6s−1=p，准确有

$$
pc=-\frac{W_s}{p+1},\qquad
\gamma_\nu=m_\nu pc=-\frac{2n_\nu W_s}{p+1},
\quad(n_S,n_T,n_U,n_V)=(17,36,68,33).
\tag{A3}
$$

R614 的 v_p(c)=−1 保证这些 γ_ν 都是原整单位。
对任意 0≤N<p，置

$$
\Lambda_N(w)=
\sum_{\substack{1\le n\le N\\n\ne s}}
 \frac{W_n}{3n(6n-1)}w^n,
\qquad
F_N=\exp(\Lambda_N)\pmod{w^{N+1}}.
\tag{A4}
$$

则 F_N 就是同一个实际 f mod w^{N+1}，而非一个可选模型。
n=s 的项被原 Gaussian **准确**消去，不是丢掉该项的分母。
在 1≤n<p 中，6n−1 只有 n=s 时被 p 整除：若
6n−1=kp，则 1≤k≤5、k≡1 mod 6，故 k=1。
因此 (A4) 的显示分母全是单位；指数所用阶乘也只到 N!，
其中 N<p。于是 W_{≤N} mod p^a 给实际 F_N mod p^a，
不损失一位。整单位的正整数幂、负整数幂和代入同样保精度。

这一证明使用原严格低窗。没有将 log f 的整性外推到 n=p，
也没有把 R929 的两位数据当成六位数据。

### A.2 原 H 的唯一低窗除 p 项有全单位读法

为使 (A4) 成为完全指定的有限输入，而不是另一份未赋值的 W，
使用 R615 的原参数；这里明确改写为**正角**

$$
v=x^{-1/2}\sim z,\quad t_+=v^6,\quad
C(t_+)=(1+t_+)^{-1/2},\quad
C_n=(-1)^n4^{-n}\binom{2n}{n},
$$

$$
H(t_+)=\sum_{n\ge0}\frac{C_n}{6n+1}t_+^n,
\quad z=vH(t_+),\quad
w=t_+H(t_+)^6,\quad W(w)=H(t_+(w))^2.
\tag{A5}
$$

这与 R929/R812 的负角 t=−x^{-3} 满足 t=−t_+，
没有改变椭圆微分或物理尺度。反函数 t_+(w) 的线性系数为一。

在 0≤n<p 内，6n+1 的唯一 p 因子发生于

$$
r_0=5s-1=(5p-1)/6,\qquad 6r_0+1=5p.
\tag{A6}
$$

又 r_0<p、p<2r_0<2p，所以 binom(2r_0,r_0) 恰含一个 p。
将原整数阶乘中的这个 p **先准确提出**，得到特征零等式

$$
\boxed{
\frac{C_{r_0}}p
=(-1)^{r_0}4^{-r_0}
 \frac{(p-1)!\prod_{j=1}^{2r_0-p}(p+j)}{(r_0!)^2},
\qquad H_{r_0}=\frac15\frac{C_{r_0}}p.
}
\tag{A7}
$$

右边所有分子、分母都是 p 单位。其余 H_n 在 n<p 中
直接用 (A5) 的单位分母读取。因此，对任意 a≥1，
H_{≤N} mod p^a、N<p，可由显示有限整数乘积及单位除法直接取得。
形式反演和复合在首项一的整环上完成，故 (A5) 同精度恢复
W_{≤N} mod p^a。全程没有“先只知 C_{r_0} mod p^a，
再除以 p”造成的未支付精度损失。

用于第五块时 N_5=5s−1 恰为 r_0：该真实端点必须保留。
前四块不碰这个 H 分母；第五块所需的 H_{r_0} mod p^2
由 (A7) 直接给出。

若只需要 W_{<p} mod p，还可使用 R615 已登记的稀疏式

$$
H(t_+)\equiv P(t_+)+(\delta/5)t_+^{r_0}
\pmod{p,t_+^p},\quad
P(t_+)=\sum_{n=0}^{3s-1}\frac{\overline C_n}{6n+1}t_+^n,
\tag{A8}
$$

其中 δ 完全保 R615(7)，且 δ C_s=3。
(A8) 是旧式 (8) 在当前严格低窗的直接截断，未作为新 Cartier
结论登记。高精度使用 (A5)–(A7)，不能把 (A8) 当成多位公式。

### A.3 完整原五块与真正 L5 mod p7

取 R647/R821/R923 的全部原正角分子 P_ν，P_ν(0)=1。
R933 的同源身份为

$$
\mathscr G_\nu
=w f^{-n_\nu}W^{n_\nu-3}
 P_\nu(w/W^3),\qquad
g_{\nu,h}=[w^{sh}]\mathscr G_\nu.
\tag{A9}
$$

不替换 P_ν 的任何低角因子。对 1≤h≤5，N_h=sh−1<p，
故由 (A4) 得特征零的实际系数读取

$$
\boxed{
g_{\nu,h}
=[w^{N_h}]
 \exp(-n_\nu\Lambda_{N_h})
 W^{n_\nu-3}P_\nu(w/W^3).
}
\tag{A10}
$$

右边只读 W_{≤N_h}；单位复合、幂和完整卷积不增加分母。
于是原部分和被完全恢复为

$$
\boxed{
L_{\nu,5}=
\sum_{h=1}^5(-1)^{h-1}(h-1)!p^h\gamma_\nu^{-h}
 [w^{sh-1}]
 \exp(-n_\nu\Lambda_{sh-1})
 W^{n_\nu-3}P_\nu(w/W^3).
}
\tag{A11}
$$

为了读取该数 mod p^7，一个逐块充分输入表是：

| 块 h | 所读 W 的最高次数 | W 与 g_{ν,h} 的精度 |
|---|---:|---:|
| 1 | s−1 | mod p^6 |
| 2 | 2s−1 | mod p^5 |
| 3 | 3s−1 | mod p^4 |
| 4 | 4s−1 | mod p^3 |
| 5 | 5s−1 | mod p^2 |

另外 W_s mod p^6 支付 γ_ν mod p^6；(p+1) 的除法是单位除法。
也可以统一读取 W_{≤5s−1} mod p^6，代价较大但同样准确。
这说明所有输入都可由 (A5)–(A7) 的原有限乘积取得；
没有任意指定的 carry，也没有额外数域提升。

必须区别 L5 mod p^7 与 L5 mod p^6：在实际中央零时要读
L5/p^6 mod p，需前者，等价于 L5/p mod p^6。
表中 g_{ν,1} 的六位、g_{ν,2} 的五位等不能用 R929 的两位统一替代。

R614 的整窗与全尾估计适用于 (A9) 的完整有限分子，
R821(16a) 对 U/V 明确保全部非负 W 幂及无限 Hurwitz 尾。
因此在同一个实际中央上，准确有

$$
j_\nu\equiv L_{\nu,5}
 -120p^6\gamma_\nu^{-6}g_{\nu,6}\pmod{p^7}.
\tag{A12}
$$

这里准确使用R614(21)–(24)的完整尾门：7≤h≤p−1的原g_h整，所以各项属于p7；h=p及以后的分段界、再接全Hurwitz界支付全部无限余尾。R821(16a)的非负W幂与A的同一性质把这个门逐源保留。
原零质量和同一 Gaussian 保证它就是原中央导数的单位归一。

### A.4 S/U 的完全指定六位检验

用 (A4) 取得实际 f_{<p}=F_{p-1}，令 W_{<p} 为原严格低截断，
并保 R933 的全部低卷积

$$
C_{\nu,p}=[w^p]\left\{
 f_{<p}^{-n_\nu}W_{<p}^{n_\nu-3}
 P_\nu(w/W_{<p}^3)\right\}.
\tag{A13}
$$

计算 (A13) 只需 W_{<p} mod p；单位幂展开到 w^p
使用的是已经取得的有限多项式 f_{<p}，不需要 log f 的 n=p 项，
也不需除以 p!。R933 及旧 R615 的 W_p≡1/35 给

$$
4\overline g_{S,6}-\overline g_{U,6}
=4\overline C_{S,p}-\overline C_{U,p}-9/35.
\tag{A14}
$$

记 γ=γ_S，于是 γ_U=4γ。定义模 p^7 的实际数

$$
\boxed{\begin{aligned}
\mathcal E_p={}&4\gamma^6L_{S,5}
 -(4\gamma)^6L_{U,5}\\
&-120p^6\bigl(4C_{S,p}-C_{U,p}-9/35\bigr).
\end{aligned}}
\tag{A15}
$$

最后括号只需 mod p；任意整代表都给相同的 E_p mod p^7。
(A3)、(A5)–(A7)、(A11)、(A13) 完整指定其全部有限输入，
连 γ 的高精度也由同 W 支付。特别 (A15) 不含未读的 f_p，
也不含一个独立可选的 Q_p(2)。

将 (A12) 与 (A14) 相减，准确得到

$$
\boxed{
\mathcal E_p\equiv
4\gamma^6j_S-(4\gamma)^6j_U\pmod{p^7}.
}
\tag{A16}
$$

所以 E_p≠0 mod p^7 是同一素数处 S/U 至少一条原中央非零
的充分有限证书。两中央同时零强迫 E_p=0。
本附录还未证明这个明确数在无穷多个 p 非零。

### A.5 同 charge B 与二倍点的真实第六 carry

保 R812 的完整原来源

$$
A=S(2z)/64,\qquad B=U-A,
\quad B=1890w^2+O(w^3),\quad
\gamma_A=\gamma_B=4\gamma.
\tag{A17}
$$

这里 B 的所有固定角因子和首常数 1890 都保留，
不将 B 换成 S^4 或只保它的首项。R812 的原全分布关系给

$$
j_A=j_S/64,\qquad j_B=j_U-j_S/64.
\tag{A18}
$$

置 Q=Q_p(2)=(2^{p-1}−1)/p、ρ=4(1+pQ)、ε=4γQ。
取原 Δ=0 后，R812(19)–(20) 在每个实际系数上准确为

$$
g_{A,h}=\frac1{64}\sum_{k=1}^{h}
 \frac{\varepsilon^{h-k}}{(h-k)!}\rho^k g_{S,k}.
\tag{A19}
$$

这些是同一个 Gaussian 的真实因子；没有只改 Gaussian 而
不同时运输来源。对 h=6 模 p，(A19) 给

$$
\boxed{
\overline g_{A,6}=64\overline g_{S,6}+K_{6,p},\qquad
K_{6,p}=64\sum_{h=1}^{5}
 \frac{(\overline\gamma\,\overline Q)^{6-h}}{(6-h)!}
 \overline g_{S,h}.
}
\tag{A20}
$$

五个低块全部保留。即使 j_S=0 只先给 g_{S,1}≡0，
也不能据此将第二至第五项逐个删去。

A 的完整 R812(6) 分子在写成 σ^136φ_A 后有极阶 130，
φ_A=x^2 乘完整 degree 21 的 X=x^3 多项式；
转成 (A9) 时所有 W 幂均非负。因此 R614 同一分段整性及
完整 Hurwitz 尾也适用于 A；B 由同 charge 的准确线性差得到。
于是 (A12) 同时适用于 A/B，并与 (A18)、(A20) 给出

$$
\boxed{
L_{A,5}-L_{S,5}/64
\equiv\frac{120p^6}{4^6\gamma^6}K_{6,p}
\pmod{p^7}.
}
\tag{A21}
$$

尤其左侧确实属于 p^6 O，不需先假设中央零；
它的除 p^6 商却是原 K_{6,p} 的显示非自由倍数，不能略去。
这里 g_{S,6} 的系数准确相消，因为 64/4^6=1/64。

设 P_A 为 R812 完整 A 在 (A9) 中的正角分子，则
P_A(0)=P_U(0)=1。定义 C_{A,p} 如 (A13)。
A/U 的 n 都为 68，因此 R933 的两个共同高项同时相消：

$$
\boxed{
\overline g_{B,6}
=\overline g_{U,6}-\overline g_{A,6}
=\overline C_{U,p}-\overline C_{A,p}.
}
\tag{A22}
$$

这就是同一个原 B 的第六块，不是新独立的中央条件。
其起阶 w^2 使它无需 f_p/W_p，所需输入严格低于 p。
同时由相同 γ_A=γ_B=γ_U，特征零中准确有

$$
L_{B,5}=L_{U,5}-L_{A,5}.
\tag{A23}
$$

将 (A20)、(A22) 代回 (A14)，得到完整实际低卷积等式

$$
4\overline C_{S,p}-\overline C_{U,p}-9/35
=-60\overline g_{S,6}-K_{6,p}-\overline g_{B,6}.
\tag{A24}
$$

最后在 (A15) 中使用 (A21)、(A23)、(A24)，两份 K_{6,p}
分别来自真实的低部分和 carry 与第六系数 carry，精确抵消：

$$
\boxed{
\mathcal E_p\equiv
-60\gamma^6j_S-4^6\gamma^6j_B\pmod{p^7}.
}
\tag{A25}
$$

这与 (A16)、(A18) 逐字一致。
因此 −9/35 没有自行给出矛盾：它和保留的原低卷积、B 的真实
中央以及 (A21) 的真实商处于同一等式。它仍是 (A15) 的必要项；
若删除它或删除 norm 2 的 K_{6,p} carry，所得将不再是原中央。
本附录完成的是 (A15) **全部**实际输入与精度，不仅给第六
系数一个形式表达，也不新增一个由分布身份自动产生的独立零条件。

### A.6 物理尺度及下一可检验命题

共同 b=1 只为表示方便。回到原物理模型时保 R647/R929 的

$$
g_{\nu,h}^{(b)}=b^{sh-1}g_{\nu,h}^{(1)},\quad
\gamma_\nu^{(b)}=b^s\gamma_\nu^{(1)},\quad
j_\nu^{(b)}=b^{-1}j_\nu^{(1)}.
\tag{A26}
$$

原 U 的 E_{2312} 微分尺度仍按 R469，第四来源仍保原 −17/11。
这些固定单位运输后才读原 Selmer 桥；不能将共同模型的
(A18) 无尺度地搬到不同物理周期上。

现在可以精确提出而不留“未知 carry”的下一门：
对同一个无穷 p≡5 mod 6 集，证明按 (A5)–(A15) 完全指定的
E_p mod p^7 非零，或得到足以排除四原中央同时零的其它
实际 W 关系。上述有限恢复本身没有证明这条非消失命题，
也没有从中央零推出 R708/R923 的完整边界前缀零。

依赖：R614 原整窗与完整 Newton 尾；R615 原正角 H、唯一进位
及 W_p 首位；R647/R821/R923 完整四来源；R711 真 L5/p6；
R812 全二倍点与同 charge B；R933 首 Frobenius 的实际读取。
