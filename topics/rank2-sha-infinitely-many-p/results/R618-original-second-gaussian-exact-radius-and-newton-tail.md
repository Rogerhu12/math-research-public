# R618 — 原 Gaussian 余项的第二临界项、精确半径与完整 Newton 尾

日期：2026-11-14。**状态：已证明。**

R614 已证明原 Gaussian 后 sigma 在整个高度二首窗内整。
本篇利用这段真实整性，先除去一个整单位多项式，再把剩余对数中
唯一决定下一收敛边界的项准确分离。其指标为 $ps$，系数恰有两次
$p$ 分母；全部其他对数项在该边界严格可指数化。

因此同一个原余项及 $f_4,f_1,S,T$ 的规范化余项都有精确半径
$p^{-(2p-1)/(p(p^2-1))}$，且在临界闭盘不是 Tate 元。
这比 R602 已付的可用开盘更大，并给全部系数和原完整 Newton 尾
一个新的统一界。未去掉第一 Gaussian 的原来源仍保留 R588 的旧
精确半径；本篇不把有限因子分解添为新的全局来源。

## 1. 同一个原函数与已经支付的整窗

保持
$$
p=6s-1>71,\qquad L=\frac{p^2-1}{6}=s(p-1),\qquad w=z^6,
$$
以及原 $y^2=x^3+b$ 的好惰性单位模型；本题 $b=17$，
共同 $b=1$ frame 按已付物理单位伸缩运输。
在同一非分歧系数环 $\mathcal O$ 上取 $v_p(p)=1$，写
$$
W=z^2x=\sum_{n\ge0}X_nw^n,\quad X_0=1,\qquad
Y=-z^3y=W-3wW',
$$
$$
F=\log(\sigma/z),\qquad c=F_s,\qquad
c'-c\in\mathcal O,\qquad U=\exp(F-c'w^s).
\tag{1}
$$

R301/R602 和 R614 分别给
$$
v_p(X_n)\ge-\lfloor n/L\rfloor,\qquad
F_n=-\frac{X_n}{6n(6n-1)},\qquad v_p(c)=-1,
\tag{2}
$$
$$
U_n=[w^n]U\in\mathcal O\qquad(0\le n<L).
\tag{3}
$$
(3) 是原完整二变量 addition 的结论，不是从对数低系数的整性
直接推指数整性。

取实际 Taylor 多项式
$$
U_0(w)=\sum_{0\le n<L}U_nw^n\in1+w\mathcal O[w],
$$
$$
\Delta=F-c'w^s-\log U_0=\sum_{n\ge L}\Delta_nw^n.
\tag{4}
$$
其从 $L$ 起始是一个特征零形式恒等式。
因 $U_0^{-1}\in\mathcal O[[w]]$，
$$
w\frac{U_0'}{U_0}\in\mathcal O[[w]],\qquad
v_p([w^n]\log U_0)\ge-v_p(n).
\tag{5}
$$
所以对全部 $n\ge L$，
$$
\boxed{
v_p(\Delta_n)\ge-\lfloor n/L\rfloor-e_n,\qquad
e_n=v_p(6n(6n-1)).
}
\tag{6}
$$
这里 $e_n\ge v_p(n)$；没有忽略有限整单位的 log 分母。

## 2. ps 处的实际两次分母及其绝对 residue

只需把 R616 原留数变分延长到一个指定端点。
保持原参数
$$
u=x^{-1/2},\quad t=bu^6,\quad z=uH(t),\quad dz=C(t)\,du,
$$
$$
C_n=(-1)^n4^{-n}\binom{2n}{n},\qquad
H_n=\frac{C_n}{6n+1}.
\tag{7}
$$
R616 已证明 $n<ps$ 中仅 $H_L$ 非整，且
$pH_L\equiv-1\pmod p$。在新端点 $n=ps$，
$6ps+1=p(p+1)+1$ 为单位，故 $H_{ps}$ 整。
因此同一唯一极点分解在 $n\le ps$ 仍然成立。

原准确留数式为
$$
X_n=b^n[t^n]CH^{1-6n}.
\tag{8}
$$
因 $ps=L+s<2L$，在 $H_Lt^L$ 中只需保留一次项。
原 R616 的计算对 $r=s$ 仍合法：
低输出次数 $s<p^2$，所以 $H^{-p^2}$ 的 Frobenius 因子不贡献。
由此
$$
\boxed{
pX_{ps}\equiv b^L(6s-2)X_s=-b^LX_s\pmod p.
}
\tag{9}
$$
这里延长的是 (8) 的原 $x$ 留数；没有延长 R616 中只适用于
$r<s$ 的指数运输公式。

因为
$$
pc=-\frac{X_s}{p+1},\qquad
X_s\equiv b^sC_s\in k^\times,
$$
代入原 $F_{ps}$ 得
$$
\boxed{
p^2F_{ps}
=-\frac{pX_{ps}}{6s(6ps-1)}
\equiv-b^LX_s=b^Lpc\in k^\times.
}
\tag{10}
$$
而 (5) 在 $n=ps$ 仅容许一次分母。因此令
$$
a_2=\Delta_{ps},
$$
便有
$$
\boxed{v_p(a_2)=-2,\qquad p^2a_2\equiv b^Lpc\pmod p.}
\tag{11}
$$
此 residue 不依赖任何整改变量 $c'-c$。
本篇保 $b^L$ 以显示实际尺度；当 $b\in\mathbf F_p^\times$ 时它为一。

## 3. 全部其他对数项在第二临界闭盘严格收敛

置
$$
D_2=6ps=p(p+1),\qquad
\tau_2=\frac{2+1/(p-1)}{D_2}
      =\frac{2p-1}{p(p^2-1)},\qquad
R_2=p^{-\tau_2}.
\tag{12}
$$
记
$$
\Delta_{\rm reg}=\Delta-a_2w^{ps}.
$$

**引理 1。** 在闭 $z$ 盘 $R_2$ 上，
$\Delta_{\rm reg}(z^6)$ 为 Tate 元，且其 Gauss 范数严格小于
$p^{-1/(p-1)}$。它和其指数实际上在某个略大于 $R_2$ 的闭盘上
仍满足同样严格界。

证明须支付全部无限尾。分四段。

**第一段 $L\le n<ps$。** 写 $n=L+r$，$0\le r<s$。
$6n$ 和 $6n-1$ 均为 $p$ 单位，故 (6) 给 $v_p(\Delta_n)\ge-1$。
于是
$$
v_p(\Delta_n)+6n\tau_2
\ge-1+6L\tau_2=1-\frac1p>\frac1{p-1}.
\tag{13}
$$

**第二段 $ps<n<2L$。** 这里 $e_n\le1$，故
$v_p(\Delta_n)\ge-2$。由 $6ps\tau_2=2+1/(p-1)$，
$$
v_p(\Delta_n)+6n\tau_2>
-2+6ps\tau_2=\frac1{p-1}.
\tag{14}
$$
被单独提出的 $n=ps$ 正好达到临界值。

**第三段 $2L\le n<3L$。** 仍有 $e_n\le1$。
确实在 $6n<3p^2$ 内，
$6n=ap^2$ 要求 $a\equiv0\pmod6$，
而 $6n-1=ap^2$ 要求 $a\equiv5\pmod6$；
它们都不可能。因此
$$
v_p(\Delta_n)+6n\tau_2
\ge-3+12L\tau_2
=1-\frac2p>\frac1{p-1}.
\tag{15}
$$
第二段的 $e_n\le1$ 也由同一个论证覆盖。

**第四段 $n\ge3L$。** 令 $N=6n$。
两个相邻因子中至多一个含 $p$，故 $e_n\le\log_pN$。
使用
$$
\tau_2-\frac1{p^2-1}=\frac1{p(p+1)}
$$
得到
$$
v_p(\Delta_n)+N\tau_2
\ge\frac{N}{p(p+1)}-\log_pN.
\tag{16}
$$
右边在 $N\ge3(p^2-1)$ 严格递增并趋于无穷。
其左端值严格大于
$$
1-\frac3p-\log_p3>
\frac23-\frac3p>\frac1{p-1},
\tag{17}
$$
其中使用 $p>71>27$。
因此整个无限尾趋零，且与指数临界赋值有统一正间隔。

最后稍微降低 $\tau_2$：取降低量小于
$\tfrac12(\tau_2-1/(p^2-1))$，则 (16) 的尾仍有正线性斜率；
再对有限剩余系数取更小降低量，(13)–(15) 和全部有限严格不等式
仍保持。这便支付略大的闭盘，而不只给逐系数严格界。证毕。

所以
$$
V(z):=U_0(z^6)\exp(\Delta_{\rm reg}(z^6))
$$
及其逆在闭 $R_2$ 上都是实际 Tate 单位，且范数均为一。
它们亦在某个更大闭盘上解析；$U_0$ 的单位性来自其常数一、
其余系数整和 $R_2<1$。
特征零形式恒等式 (4) 于是给
$$
\boxed{U(z^6)=V(z)\exp(a_2z^{D_2}).}
\tag{18}
$$
(18) 是同一个原 $U$ 的解析因子分解，不是改变原全局来源。

## 4. 原余项的精确半径与闭边界非 Tate

**定理 2。** 原 $U(z^6)$ 的精确幂级数收敛半径为 $R_2$；
它在每个严格内闭盘上为范数一的解析单位，
但在闭 $R_2$ 上不是 Tate 元。
任意 $c'-c\in\mathcal O$ 均有同一结论。

证明中，唯一尚需计算的因子是 (18) 的指数。
其第 $D_2k$ 个系数赋值为
$$
v_p(a_2^k/k!)=-2k-v_p(k!).
$$
Legendre 公式给
$$
-2k-v_p(k!)+D_2k\tau_2
=\frac{s_p(k)}{p-1}.
\tag{19}
$$
所以它的精确半径为 $R_2$；
取 $k=p^j$，(19) 恒为 $1/(p-1)$，故临界闭盘不是 Tate 元。
在严格内盘指数及其逆范数均为一。

由引理 1，$V$ 和 $V^{-1}$ 在临界闭盘都是 Tate 元。
若 $U$ 在该闭盘也为 Tate 元，则 $V^{-1}U$ 亦然，与 (19) 矛盾。
若 $U$ 的半径更大，也必在闭 $R_2$ 上为 Tate 元。
故 (18) 同时证明下界、准确上界及边界断言。证毕。

有准确大小关系
$$
p^{-p/(p^2-1)}
<R_*=p^{-1/[6(p-1)]}<R_2<R_E=p^{-1/(p^2-1)}.
\tag{20}
$$
左端是未去掉第一 Gaussian 的原坏半径。
本篇没有改变它，也没有把去 Gaussian 的解析单位当成同预算新列。

## 5. 全部原指定 theta 余项和逐系数新界

在闭 $R_2$ 上，(2) 给
$$
v_p(X_n)+6n\tau_2
\ge\frac{6n}{p(p+1)}>0\qquad(n>0).
$$
因此 $W,Y$ 及其逆均为范数一的 Tate 单位，
并在更大于 $R_2$、小于 $R_E$ 的闭盘上保持这一性质。

原 R602 的具体多项式给
$$
B_4=WU^6,\qquad B_1=WYU^6,\qquad B_{\rm ref}=WU^2,
$$
$$
B_{34}=P_S(w,W)U^{34},\qquad
B_{72}=P_T(w,W)U^{72}.
\tag{21}
$$
这里 $P_S,P_T$ 是同篇 (15)–(16) 的完整原多项式，
其系数在当前好素数处整，常数均为一；
其余带正 $w$ 次数的项及 $W-1$ 在闭 $R_2$ 上范数严格小于一。
因此 $P_S,P_T$ 及其逆在该闭盘为 Tate 单位，
也在略大闭盘解析。

每个 (21) 都可准确写成
$$
B_m=V_m(z)\exp(m a_2 z^{D_2})
$$
且 $V_m,V_m^{-1}$ 在闭 $R_2$ 为范数一的 Tate 元。
对显示的 $m=2,6,34,72$，$m$ 是 $p$ 单位。
于是定理 2 对这些**原指定余项**逐一成立。

特别，对 $U$ 或 (21) 的每个普通系数 $b_n$，
在所有严格内闭盘上范数不超过一，取半径趋向 $R_2$ 得
$$
\boxed{
v_p(b_n)\ge-\lfloor6n\tau_2\rfloor\qquad(n\ge0).
}
\tag{22}
$$
系数赋值在当前非分歧环中为整数，故可取 floor。
这是一条对所有 $n$ 的界；R614 的前两有限带仍给其中某些指标
更强的界，继续同时使用，不能用 (22) 丢掉已付整窗。

还可在唯一端点直接核定准确度：
因 $ps<2L$，(4) 中至多出现一次坏因子，
$$
p^2U_{ps}\equiv b^Lpc,\qquad
p^2[w^{ps}]B_m\equiv m b^Lpc\pmod p.
\tag{23}
$$
原椭圆多项式的 $n<2L$ 系数至多一次分母；
因此其与更低坏带的所有乘积不影响 (23) 的二次 residue。
(23) 为原非中央余项的单位端点，不是指定中央非消失。

## 6. 同一完整 Newton 导数的新无限尾

本节回到原 $c'=c$。
对 $m=34,72$ 保持
$$
\mathscr G_m=e^{-mcw^s}A_m=wB_m(w),\quad
g_{m,h}=[w^{hs}]\mathscr G_m=[w^{hs-1}]B_m,
$$
$$
\gamma_m=mpc\in\mathcal O^\times,\qquad
a_{m,h}=(p/\gamma_m)^h g_{m,h}.
\tag{24}
$$
定义
$$
\delta_p=(p+1)\tau_2=\frac{2p-1}{p(p-1)},\qquad
\eta_p=1-\delta_p>0.
$$
由 (22) 对全部 $h\ge1$，
$$
\boxed{
v_p(a_{m,h})\ge
h-\lfloor6(hs-1)\tau_2\rfloor
=\lceil h\eta_p+6\tau_2\rceil.
}
\tag{25}
$$
这替换 R602 的全尾斜率，而不削弱 R614/R616 的更强有限窗。

同一个原函数及完整导数仍为
$$
J_{m,p}(u)=\sum_{h\ge1}a_{m,h}(u)_h,\qquad
j_m=\sum_{h\ge1}(-1)^{h-1}(h-1)!a_{m,h}.
\tag{26}
$$
若 $|u|>1$，则 $|(u)_h|=|u|^h$；若 $|u|\le1$，则该乘积范数
不超过一。因此 (25) 支付更大的开解析盘
$$
|u|_p<p^{\eta_p}.
\tag{27}
$$
对原截断
$$
L_{m,H}=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_{m,h}
$$
有整个无限尾界
$$
\boxed{
v_p(j_m-L_{m,H})\ge
M^{(2)}_{p,H}:=
\lceil(H+1)\eta_p+6\tau_2\rceil+v_p(H!).
}
\tag{28}
$$
理由是 (25) 的下界和 $v_p((h-1)!)$ 均随 $h$ 不减，
且趋于无穷；不是只检查若干后项。

R602 的有限二项式交换完全不变：
$$
L_{m,H}=\sum_{k=1}^H
(-1)^{k-1}(k-1)!\binom Hk
(p/\gamma_m)^k[w^{ks}]A_m.
\tag{29}
$$
所以原 $j_m=0$ 迫 (29) 对每个 $H$ 落入
$p^{M^{(2)}_{p,H}}\mathcal O$。
这是同一完整中央的一族实际必要条件；
没有给各个裸系数、乘积来源或辅助 theta 赋零。
当有限窗给更强余量时，以两条已付尾界的较大者为准。

## 7. 同一个中央 Euler 解的更大延拓盘

R598/R602 的固定零初值 Euler 原函数、原中央投影 $\Pi_0$ 和
全部周期继续保持。写 $d=p+1$、$X=z^d$、$\alpha_m=mc$，则
$$
H_m=d e^{-\alpha_mX}\Pi_0U_m
=-j_m e^{-\alpha_mX}+\mathcal R_m(X),
$$
$$
\mathcal R_m=
\sum_{n,j\ge0}(-1)^j\frac{(n+j)!}{n!}
\alpha_m^{-j-1}g_{m,n+j+1}X^n.
\tag{30}
$$
对任意 $\rho=p^{-1/(2p)}\le R<R_2$，原
$\mathscr G_m$ 在该闭盘的范数不超过 $R^6$。
R602 的同一估计因此给 $j$ 方向加权赋值至少
$$
(j+1)(1-d\tau)+6\tau,\qquad R=p^{-\tau}.
$$
这里 $1-d\tau>0$；固定 $j$ 时，原 $B_m$ 的 Tate 尾支付
$n$ 方向。因此 (30) 在闭 $X$ 盘 $R^d$ 一致收敛。

原未去第一 Gaussian 的临界边界及其非 Tate 性不变。
由同一准确 Stokes 恒等式，
$$
\boxed{
j_m=0
\iff H_m\text{ 在每个闭 }z\text{ 半径 }R<R_2
\text{ 的中央盘上解析}.
}
\tag{31}
$$
变量 $X$ 的半径是 $R^d$。
充分方向已由 (30) 支付；必要方向只需取大于原坏半径的一内闭盘，
其上非零的 $j_m e^{-\alpha_mX}$ 不可能被解析的 $\mathcal R_m$ 消去。

本篇不声称 $j_m=0$ 时 (30) 的精确最大半径，
也不删原 $\Pi_0$，不把依赖 $p$ 的投影添为同预算全局列。

## 8. 原全局门的边界

本篇支付了同一个原余项的精确第二半径、临界非 Tate 性、
所有系数界以及完整原 Newton 高尾。
原 R588 未去 Gaussian 的非线性原来源和长塔结论继续成立，
两者观察的是不同的准确因子。

(22) 可用于重估真实整来源的普通部分，但尚须保每个来源的
charge、Euler 分母、次数帽、固定乘子、全部角及连续真前缀。
它本身不证明全 $D/k$ 的成本严格门，也不使中央零推出所有来源零。
尤其 (23) 的确定非中央单位仍不能替代原 $g_{m,h}$ 指定行的
无穷非零。固定曲线的主目标继续保持。

## 依赖

- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
  [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  同一高度二模型、两原算术来源及完整物理缩放。
- [R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)：
  全系数高度二界、原完整多项式和 Newton/Stokes 恒等式。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：
  原 $U_n$ 在 $n<L$ 的完整整性。
- [R616](R616-original-first-bad-band-and-pth-newton-endpoint.md)：
  原 $H$ 唯一极点及实际留数变分；本篇 §2 支付新端点。
- [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)：
  原未去 Gaussian 的全来源半径，适用范围照原文保留。

全篇为原全参数证明，不使用新增素数扫描。
