# R301 — 新 j=0 原来源的惰性解析半因子、显式首分母与完整导数证书

日期：2026-11-13。**状态：以下同一实际来源的有理缩放、全部高度二系数估计、显式首分母、过收敛半因子及严格有限尾界均已证明。本篇是局部解析结论；与完整惰性 Selmer 的比较另由原参考/周期证明支付，不能仅凭一个裸系数声称主目标完成。**

## 1. 同一固定原来源及单位缩放

在基曲线
$$E_1:y^2=x^3+1,\qquad dz=dx/(2y)$$
上取 $x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$，记
$$
\begin{aligned}
A(z)&=\sigma^{34}\left(
x^{14}-\frac{53}{7}x^{11}-\frac{12}{7}x^8
-\frac{80}{7}x^5-\frac{128}{7}x^2\right)
=\sum_{m\ge0}\alpha_mz^m,\\
B(z)&=x\sigma^2=\sum_{m\ge0}\beta_mz^m.
\end{aligned}\tag{1}
$$
$A=z^6+\cdots$、$B=1+\cdots$，二者都只含 $6$ 的倍数次。
这里 $A$ 是 R297 的目标 $E_{17}:y^2=x^3+17$ 来源的固定同次缩放，
不是另添一条目标曲线。准确地，若 $\theta^6=17$，
$$
\boxed{S_{17}(z)=17^{-1}A(\theta z),\qquad
s_m=17^{m/6-1}\alpha_m\quad(6\mid m).}\tag{2}
$$
证明是 $x_b(z)=b^{1/3}x_1(b^{1/6}z)$、
$\sigma_b(z)=b^{-1/6}\sigma_1(b^{1/6}z)$ 代入 R297 的齐次式。
特别在 $p\ne17$ 处，两组对应系数的赋值完全相同。

固定
$$p\ge11,\qquad p\equiv5\pmod6,\qquad p\ne17,\qquad
d=p+1=6s.\tag{3}$$
下文所有 $v_p$ 均以 $v_p(p)=1$ 归一。
写
$$
W(z)=z^2x(z)=1+\sum_{n\ge1}X_nz^{6n},\qquad
F(z)=\log(\sigma(z)/z),\qquad c=[z^d]F.
\tag{4}
$$
首分母的精确剩余类为
$$
\boxed{v_p(c)=-1,\qquad
pc\equiv-(-1)^s4^{-s}\binom{2s}{s}\pmod p.}\tag{5}
$$
右边为单位。它决定原半因子的全部尺度，不是可任意选择的参数。

## 2. 高度二形式对数的统一系数估计

取原点附近的正式坐标 $t=x^{-1/2}$，指定 $t=z+\cdots$ 的支。于是
$$x=t^{-2},\qquad y=-t^{-3}\sqrt{1+t^6},\qquad
dz=\frac{dt}{\sqrt{1+t^6}}.$$
此坐标与通常的 $-x/y=t/\sqrt{1+t^6}$ 在所有奇素数处整可逆。
实际形式对数为
$$
L(t)=z(t)=t+\sum_{n\ge1}\ell_nt^{6n+1},\qquad
\ell_n=\frac{(-1)^n\binom{2n}{n}}{4^n(6n+1)}.
\tag{6}
$$

若 $a=v_p(6n+1)>0$，$n$ 的前 $a$ 个 $p$ 进位数依次为
$$5s-1,\ s-1,\ 5s-1,\ s-1,\ldots.\tag{7}$$
这是由 $6(5s-1)+1=5p$ 和 $6(s-1)+5=p$ 交替递推得到。
将 $n$ 与自身相加，第一位产生进位，下一位不产生，依此交替。
Kummer 的二项式进位公式因此给
$$
v_p\binom{2n}{n}\ge\lceil a/2\rceil,\qquad
v_p(\ell_n)\ge-\lfloor a/2\rfloor.
\tag{8}
$$
对 $q=6n+1$ 还有
$$\frac{q-1}{p^2-1}\ge\lfloor v_p(q)/2\rfloor.\tag{9}$$
偶数赋值 $2a$ 时由
$(p^{2a}-1)/(p^2-1)=1+p^2+\cdots+p^{2a-2}\ge a$ 得到；
奇数赋值给更强下界。

令 $R_E=p^{-1/(p^2-1)}$。对每个 $R'<R_E$，(8)、(9) 使
$L(t)/t$ 的非恒项 Gauss 范数严格小于一，且尾项趋于零。
严格收缩给实际解析逆 $t(z)$，并有
$$\|t(z)/z\|_{R'}=\|z/t(z)\|_{R'}=1.$$
因此 $W=(z/t(z))^2$ 在该圆盘范数一。让 $R'\uparrow R_E$，
逐个系数得到
$$
\boxed{v_p(X_n)\ge-\frac{6n}{p^2-1}.}\tag{10}
$$
特别当 $6n<p^2-1$ 时，$X_n$ 是 $p$ 整数。
这里没有声称逆函数在临界边界上仍是等距同构。

## 3. 首个 sigma 分母及其准确单位

因为 $D_z^2\log\sigma=-x$，
$$
F(z)=-\sum_{n\ge1}\frac{X_n}{6n(6n-1)}z^{6n}.
\tag{11}
$$
我们直接计算 $X_s\bmod p$，不只证明它非零。设
$$\mathscr L(u)=\sum_{n\ge0}
\frac{(-1)^n\binom{2n}{n}}{4^n(6n+1)}u^n,\qquad
L(t)=t\mathscr L(t^6).$$
所需的 $n\le s$ 系数全部 $p$ 整。
负幂版本的 Lagrange 反演给
$$
X_s=[z^{d-2}]t(z)^{-2}
=-\frac2{d-2}[u^s]\mathscr L(u)^{-(d-2)}.
\tag{12}
$$
$d-2=p-1$，而在所读 $s<p$ 的有限窗口，
$$\mathscr L(u)^{-(p-1)}
=\mathscr L(u)/\mathscr L(u)^p\equiv\mathscr L(u)\pmod{p,u^p}.$$
故
$$
X_s\equiv
2\frac{(-1)^s\binom{2s}{s}}{4^s(6s+1)}
\equiv(-1)^s4^{-s}\binom{2s}{s}\pmod p.
\tag{13}
$$
$2s<p$ 使二项式系数为单位。
由 $c=-X_s/(d(d-1))$ 及 $d-1=p$，即得 (5)。

这个计算在原加法坐标 $z$ 中完成。换用 Dixon 角坐标时，R299 的
$h^{-6}$ 与原乘子仍须保留；(5) 不等同于该处的 $18/17$ 对数进位。

## 4. 删去这一个真实项后的较大解析圆盘

令 $R=p^{-1/(2p)}$、$g=p^{-1/(p-1)}$。我们证明
$$\boxed{\|F-cz^d\|_R<g.}\tag{14}$$

对 (11) 的某项记 $q=6n$。
若 $q<p^2-1$ 且 $p\nmid q(q-1)$，(10) 给整性，
其加权赋值至少 $q/(2p)\ge3/p>1/(p-1)$。
若 $p\mid q$，则 $q\ge6p$。
若 $p\mid q-1$，由 $q\equiv0\pmod6$、$p\equiv-1\pmod6$，
有 $q-1=bp$ 且 $b\equiv1\pmod6$；删去的第一项是 $q=d$，
下一项至少 $7p+1$。在 $q<p^2-1$ 的范围，分母至多有一个 $p$，
因此所有剩余带分母项的加权赋值至少 $6p/(2p)-1=2$。

边界 $q=p^2-1$ 的分母为单位；(10) 给加权赋值至少
$$\frac{p^2-1}{2p}-1>\frac1{p-1}.$$
若 $q\ge p^2$，令 $b=\lfloor\log_pq\rfloor\ge2$。
由于 $q,q-1$ 连续，$v_p(q(q-1))\le b$，所以加权赋值至少
$$
q\left(\frac1{2p}-\frac1{p^2-1}\right)-b
\ge p^b\left(\frac1{2p}-\frac1{p^2-1}\right)-b.
\tag{15}
$$
在 $b=2$ 时右边为 $p/2-3-1/(p^2-1)>1/(p-1)$；
其后正项乘 $p$，负项只多减一。该界也保证尾项趋于无穷。
三段合并证明 (14)。

现在定义真实解析余项
$$
G=Ae^{-34cz^d}=\sum g_nz^n,\qquad
G_0=Be^{-2cz^d}=\sum g_n^0z^n.
\tag{16}
$$
这里首先是形式恒等式；不要求被单独取出的指数在整个 $R$ 圆盘收敛。
准确的解析表达是
$$
\begin{aligned}
G=z^6\big(&W^{14}-\tfrac{53}{7}z^6W^{11}
-\tfrac{12}{7}z^{12}W^8
-\tfrac{80}{7}z^{18}W^5-\tfrac{128}{7}z^{24}W^2\big)
e^{34(F-cz^d)},\\
G_0&=W e^{2(F-cz^d)}.
\end{aligned}\tag{17}
$$
因为 $R<R_E$、$p\nmid7$，(14) 使最后两个指数及其逆都实际解析、范数一。
因此
$$
\boxed{\|G\|_R\le R^6,\qquad \|G_0\|_R\le1,\qquad G_0(0)=1.}
\tag{18}
$$
这一步保留了整个原四次多项式，未把其所有角向列当作中央零。

## 5. 原解析半因子及其全部整数权

令 $(u)_h=u(u-1)\cdots(u-h+1)$、$(u)_0=1$，定义
$$
\begin{aligned}
J_p(u)&=\sum_{h\ge0}a_h(u)_h,
&a_h&=g_{dh}(34c)^{-h},\\
J_{0,p}(u)&=\sum_{h\ge0}a_h^0(u)_h,
&a_h^0&=g_{dh}^0(2c)^{-h}.
\end{aligned}\tag{19}
$$
$a_0=0$、$a_0^0=1$。由 (5)、(18) 得到准确下界
$$
\boxed{
v_p(a_h)\ge
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
v_p(a_h^0)\ge
\left\lceil\frac{h(p-1)}{2p}\right\rceil\quad(h\ge1).
}\tag{20}
$$
所以两式在 $|u|_p<p^{(p-1)/(2p)}$ 上解析，且
$$
\boxed{J_p\in pu\mathbf Z_p\langle u\rangle,\qquad
J_{0,p}\in1+p\mathbf Z_p\langle u\rangle.}\tag{21}
$$
对每个整数 $k\ge0$，形式乘积 (16) 的有限系数卷积准确给
$$
\boxed{J_p(k)=k!(34c)^{-k}\alpha_{dk},\qquad
J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.}\tag{22}
$$
因为 $(k)_h=0$ 对 $h>k$ 成立，无须在该步骤交换无限和。
特别，$J_{0,p}(k)$ 为单位，故所有正整数 $k$ 都满足
$$
\boxed{v_p(\beta_{dk})=-k-v_p(k!).}\tag{23}
$$
这是真实固定参考函数 $B=x\sigma^2$ 的全权系数陈述。
其全球 Hecke 身份与常数另由原 Schwartz/周期计算支付。

## 6. 首层只剩原首权，且全部深度有严格有限证书

当 $h\ge2$ 时，(20) 的第一项至少为二。
又 $A(0)=0$，故 $g_d=\alpha_d$。于是在整个 Tate 代数中
$$
\boxed{J_p(u)\equiv\frac{\alpha_d}{34c}u\pmod{p^2},\qquad
\frac{J_p'(0)}p\equiv\frac{\alpha_d}{34pc}\pmod p.}\tag{24}
$$
结合 (2)、(5)，有准确等价
$$
s_{p+1}\in\mathbf Z_p^\times
\quad\Longleftrightarrow\quad
\alpha_{p+1}\in\mathbf Z_p^\times
\quad\Longleftrightarrow\quad
J_p'(0)/p\in\mathbf Z_p^\times.
\tag{25}
$$
其中 $s_m$ 是 R295 同一个 $E_{17}$ 原来源的系数。
这是一个指定原系数，不能改成不同 tame 分支或任一 Cartier 矩阵项。

全部精度的导数为
$$J_p'(0)=\sum_{h\ge1}(-1)^{h-1}(h-1)!\,a_h.$$
令 $L_{p,H}$ 为前 $H$ 项，则
$$
\boxed{
v_p(J_p'(0)-L_{p,H})\ge
M_{p,H}:=
\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).
}\tag{26}
$$
证明是 (20) 加上每项的 $v_p((h-1)!)$；这个下界随 $h$ 不减。
因 $M_{p,H}\to\infty$，
$$
\boxed{J_p'(0)\ne0
\quad\Longleftrightarrow\quad
\exists H\ge1:\ v_p(L_{p,H})<M_{p,H}.}\tag{27}
$$
该证书允许首导数有更高但有限的赋值，未把首层失败当作完整失败。

## 7. 与后续算术比较的接口

这里的局部对象完全来自 R297 的原截面，未重新选择 Schwartz 函数。
普通分支由 R295/R300 已经接到完整 Selmer；当前惰性分支须继续支付：

1. $B=x\sigma^2$ 是 $E_1$ 的实际秩零 theta 来源及其全部权常数；
2. 同一个局部 signed 整格内，原 $E_{17}$ 与 $E_1$ 的椭圆单位比较；
3. 所有混合中央权的周期、阶乘和非单位 Euler 因子的准确抵消。

只有在这些比较完成后，(27) 才成为原 Sha 的逐素数充分证书。
即使如此，仍须证明该证书对无穷多个不同素数命中。
本文所有对可变 $p$ 的结论均由上述统一证明给出，未使用有限素数扫描。

## 依赖

- [R294：新曲线的精确秩二](R294-jzero-exact-rank-two-by-rational-three-isogeny.md)。
- [R297：原来源、CM7 乘积及其准确首项](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R299：真实角参数及首次共振](R299-jzero-actual-source-first-integral-frame-correction-and-resonance.md)。
- [R295：同一固定系数的普通中央比较](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)。

形式反演、二项式进位、Gauss 收敛及所有常数均在本文给出完整推导。

