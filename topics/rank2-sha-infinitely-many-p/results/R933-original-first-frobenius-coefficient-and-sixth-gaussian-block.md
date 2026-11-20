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
