# R616 — 原 Gaussian 余项的完整首坏带与第 p 个 Newton 中央项

日期：2026-11-14。**状态：已证明。**

本篇把 R615 的唯一原参数进位扩展到整个首坏带。对原 $f_4,f_1,S,T$，该带的每个 residue 都由同一来源的低系数准确给出。原 S/T 第 $p$ 个 Newton 中央项因此直接返回其第一个指定中央系数；没有把非中央的单位 residue 代为中央非消失。

依赖 R614 的全 addition 整性窗口和完整 Newton 尾；原参数进位与全部 residue 的绝对常数在本篇自含证明。

## 1. 窗口和原规范

保持
$$
p=6s-1>71,\qquad
L=\frac{p^2-1}{6}=s(p-1),\qquad
w=z^6,\qquad b=17.
\tag{1}
$$
记
$$
A(w)=z^2x(z)=\sum X_nw^n,\qquad
Y(w)=-z^3y(z)=\sum Y_nw^n,
$$
$$
Y=A-3w\partial_wA,\qquad
Y_n=(1-3n)X_n.
\tag{2}
$$
令
$$
F(w)=\log(\sigma(z)/z),\qquad
c=[w^s]F,\qquad c'-c\in\mathcal O,
$$
$$
F^\circ=F-c'w^s,\qquad U=\exp(F^\circ).
\tag{3}
$$
R614 已付 $[w^n]U\in\mathcal O$ 对全部 $n<L$ 成立。下文所有 residue 均在准确的带
$$
L\le n=L+r<ps=L+s
\tag{4}
$$
中计算。

## 2. 原 H 参数只有一个坏系数

使用 R615 的同一参数
$$
u=x^{-1/2},\quad t=bu^6,\quad
z=uH(t),\quad dz=C(t)du,
$$
$$
C_n=\frac{(-1)^n}{4^n}\binom{2n}{n},\qquad
H_n=\frac{C_n}{6n+1}.
\tag{5}
$$

**引理 1。** 在全部 $0\le n<ps$ 中，只有 $H_L$ 有 $p$ 分母，且
$$
\boxed{
v_p(H_L)=-1,\qquad pH_L\equiv-1\pmod p.
}
\tag{6}
$$

确实写 $n=pa+r$，则 $a\le s-1$。原分母 $6n+1$ 含 $p$ 当且仅当
$r=p-s$。当 $a<s-1$ 时，R615 的唯一二项式进位消去分母的那个 $p$；当 $a=s-1$ 时，指标正是
$$
n=L,\qquad 6L+1=p^2.
$$
R615 的带进位单位公式仍给
$$
\frac{C_L}{p}
=\delta(2s-1)C_{s-1}
=-2s\,\delta C_s
=-1\quad\text{于 }k,
$$
因为 $\delta C_s=3$、$6s=1$。因此原 $H_L=C_L/p^2$ 恰有一次分母，其余 $n<ps$ 全整。这保留了真实的 $p^2$ 端点，而非只用估值上界。

于是，在这个有限窗口中可以写成
$$
H=H_{\rm int}+H_Lt^L,\qquad
H_{\rm int}\in\mathcal O[t]/(t^{ps}),\qquad
H_{\rm int}(0)=1.
\tag{7}
$$

## 3. 原 x、y、log sigma 的全首坏带

原留数恒等式是
$$
X_n=b^n[t^n]\,CH^{1-6n}.
\tag{8}
$$
若 $n=L+r<ps<2L$，在 (7) 的幂展开中至多出现一次 $H_Lt^L$。因此 $pX_n$ 整，且
$$
pX_{L+r}
\equiv
-b^{L+r}(1-6L-6r)
 [t^r]\,C H_{\rm int}^{-6L-6r}.
$$
用 $6L=p^2-1$，低 $r<s$ 窗口中的 Frobenius 因子
$H_{\rm int}^{-p^2}$ 为 $1$。再次使用 (8) 的低指标 $r$，得到
$$
\boxed{
pX_{L+r}\equiv b^L(6r-2)X_r\pmod p,
\qquad0\le r<s.
}
\tag{9}
$$
这一步是在原 $u\mapsto z$ 留数内作完整变分，没有更换原系数观察。

由 (2) 直接得到
$$
\boxed{
pY_{L+r}\equiv b^L(6r-3)Y_r\pmod p.
}
\tag{10}
$$
特别
$$
pX_L=-2b^L,\qquad pY_L=-3b^L\quad\text{于 }k.
\tag{11}
$$
本题 $b\in\mathbf F_p^\times$ 且 $L$ 是 $p-1$ 的倍数，故 $b^L=1$；为保来源尺度，后式仍显示这个因子。

原 log 系数准确为
$$
F_n=-\frac{X_n}{6n(6n-1)}\quad(n>0).
$$
在 (4) 内，$6n$ 与 $6n-1$ 都是单位；代 (9) 得
$$
\boxed{
pF^\circ_{L+r}
\equiv
-\frac{b^L X_r}{6r-1}
=b^L Z_r\pmod p,
}
\tag{12}
$$
其中
$$
Z(w)=z\zeta(z)=\sum Z_rw^r,\qquad
Z_0=1,\quad Z_r=-\frac{X_r}{6r-1}\ (r>0).
$$
$\zeta=D\log\sigma$ 是原规范。式 (12) 只读取 $r<s$ 的整 zeta 系数。

## 4. 从 log 到原指数的完整带运输

不能仅由 (12) 就把同一 residue 赋给指数。这里使用已付的真实整低段。

令 $U_{\rm int}$ 是原 $U$ 到 $w^{L-1}$ 的截断，并把其后系数取零。它属于
$1+w\mathcal O[[w]]$，且
$$
\Delta=F^\circ-\log U_{\rm int}
$$
从指标 $L$ 开始。在带 (4) 中 $n=L+r$ 不被 $p$ 整除；又
$w\partial_w\log U_{\rm int}$ 整，所以这些 $\log U_{\rm int}$ 系数整。故
$$
p\Delta_{L+r}=b^L Z_r\quad\text{于 }k.
$$
由于 $2L>ps$，同一个带中
$$
U=U_{\rm int}\exp\Delta
=U_{\rm int}(1+\Delta).
$$
这严格给出
$$
pU_{L+r}\equiv b^L[\,UZ\,]_r.
$$
在低 $r<s$ 中 Gaussian 的导数项尚未进入，所以
$$
UZ=U+6w\partial_wU\pmod{w^s}.
$$
于是
$$
\boxed{
pU_{L+r}\equiv b^L(6r+1)U_r\pmod p,
\qquad0\le r<s.
}
\tag{13}
$$
这里同时证明整带系数的 $v_p\ge-1$，并保留了指数和 log 的全部差别。$r=s$ 不在这个论证内：该处 $n=ps$ 被 $p$ 整除，且原 Gaussian 导数开始参与，不能直接延长 (13)。

### 4.1 任意固定原 theta 多项式

考虑一个原纯 $\mu_6$ 型 theta 来源
$$
\mathcal F(z)=\sigma(z)^m P(x(z),y(z)),
$$
其中 $P$ 为固定的原椭圆多项式，系数在当前好素数处整，并写
$$
\mathcal F(z)=z^d\bigl(a_0+O(w)\bigr),\qquad
B_{\mathcal F}(w)=z^{-d}e^{-mc'w^s}\mathcal F(z).
\tag{14}
$$
对原 $f_4,f_1,S,T$，$a_0=1$，$d$ 分别为 $4,1,6,6$。

先用 $y^2=x^3+b$ 将 $P$ 化为 $y$ 次数至多一的原椭圆基；各项的极阶互异。按原点最低阶 $d$ 提出首项后，各 $j\ge0$。把 (14) 的每项写成
$$
\text{固定系数}\cdot
w^jA^\alpha Y^\beta U^m,\qquad
m-2\alpha-3\beta-6j=d.
$$
首坏带中两个坏因子不能同时出现。故 (9)、(10)、(13) 的 residue 按真正的乘法 Leibniz 规则相加；乘上 $w^j$ 时低指标同时改为 $r-j$。准确结果是：

**定理 2。**
$$
\boxed{
p[w^{L+r}]B_{\mathcal F}
\equiv
b^L(6r+d)[w^r]B_{\mathcal F}\pmod p,
\qquad0\le r<s.
}
\tag{15}
$$
全部原多项式项和其 $w^j$ 位移都保留了；没有只用 sigma 的 charge 代替实际原点阶数 $d$。

对本题四条来源，首坏项的 residue 依次为 $4b^L,b^L,6b^L,6b^L$，均为单位。因此其归一 Gaussian 余项在指标 $L$ 的估值确为 $-1$。

## 5. 两个指定 forcing 的实际回读

对 R607 的原 $G_4,G_1$，式 (15) 就是
$$
p g_{4,L+r}=b^L(6r+4)g_{4,r},\qquad
p g_{1,L+r}=b^L(6r+1)g_{1,r}\quad\text{于 }k.
\tag{16}
$$
取 $r=s-1$，准确得到最后一个实际窗口系数
$$
\boxed{
p g_{4,ps-1}=-b^L c_{4,p},\qquad
p g_{1,ps-1}=-4b^L c_{1,p}.
}
\tag{17}
$$
因此两个指定 forcing 控制的是这两条原 Gaussian 余项的实际最末带行。首项 $r=0$ 的单位没有被拿来推断 (17) 的非零。

## 6. 原 S/T 的第 p 个 Newton 中央项

本节取原规范 $c'=c$。对 $X=S,T$，令 $m=34,72$，保持 R598 的完整原对象
$$
G_m(w)=e^{-mcw^s}X(z)=wB_X(w),\qquad
g_{m,h}=[w^{hs}]G_m,
$$
$$
\gamma_m=mpc\in\mathcal O^\times,\qquad
j_m=\sum_{h\ge1}
 \frac{(-1)^{h-1}(h-1)!\,p^h}{\gamma_m^h}\,g_{m,h}.
\tag{18}
$$
令
$$
C_X=\overline{g_{m,1}}
=\overline{[w^s]X}.
$$
最后等号使用 $X$ 首项为 $w$：原 Gaussian 的首次乘积影响从 $w^{s+1}$ 才开始。

现在
$$
ps-1=L+(s-1).
$$
对 $B_X$ 使用 (15) 的合法末端 $r=s-1$、$d=6$，得到
$$
\boxed{
p\,g_{m,p}\equiv b^L C_X\pmod p.
}
\tag{19}
$$
这里先去掉原首项因子 $w$ 是必要的；它没有把 $U$ 的未付 $r=s$ 端点直接拿来使用。

R614 已付 $g_{m,h}$ 对 $1\le h\le p-1$ 整，并且 (18) 中所有
$h\ge p+1$ 项的完整尾在 $p^p\mathcal O$ 中。因此由 Wilson 的
$(p-1)!\equiv-1$ 得到准确的下一端点：
$$
\boxed{
j_m\equiv
\sum_{h=1}^{p-1}
 \frac{(-1)^{h-1}(h-1)!\,p^h}{\gamma_m^h}\,g_{m,h}
-\frac{p^{p-1}b^L}{\gamma_m^p}\,C_X
\pmod{p^p}.
}
\tag{20}
$$
右端的 $C_X$ 可取任何整提升；不同提升只改变模 $p^p$ 已忽略的部分。

若原完整 $j_m=0$，其必要首层条件是 $C_X=0$。由 (19) 此时原
$g_{m,p}$ 本身整，故第 $p$ 项也进入 $p^p\mathcal O$，完整截断改进为
$$
\boxed{
\sum_{h=1}^{p-1}
 \frac{(-1)^{h-1}(h-1)!\,p^h}{\gamma_m^h}\,g_{m,h}
\equiv0\pmod{p^p}.
}
\tag{21}
$$
这是真正的原中央条件和同源末端相消，未给任何非中央来源赋零。

## 7. 范围和证书

[check-r616-first-bad-band-and-newton-endpoint.mjs](../scripts/check-r616-first-bad-band-and-newton-endpoint.mjs) 在既有 $p=17,23$ 的合法 $b=1,17$ 纤维中，从原有理 Weierstrass 系数构造足精度的 Gaussian 后 Hurwitz 递推，再除原阶乘读取普通系数；完成 328 项精确检查，逐个复核：

- 原 $H$ 的唯一坏系数和 $pH_L=-1$；
- 整条 $X,Y,F^\circ$ 带；
- 原 Gaussian 后 $\sigma^6/z^6,f_4/z^4,f_1/z$ 的全带，保高阶有理系数的实际相消；
- 最末 $ps-1$ 两 forcing 回读及显示首项单位。

一般全带由原参数、指数运输和原来源同质式 (14)–(15) 证明。Newton 尾使用
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md) 的完整估计。

这些结论没有证明 $C_X$、$c_{4,p}$ 或 $c_{1,p}$ 非零；它们也没有把第 $p$ 个同源中央回读替代整个真前缀或把有限窗口算子另加成全局列。主目标仍须继续。
