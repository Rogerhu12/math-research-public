# R1192：原 Hermitian 第四插入的完整五个端点块

**状态：下列恒等式已证明；原 $e,K_4$ 不同时为零仍未证明。**
日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

本文沿用 R1183 的实际覆盖及原 Fermat 六次笔记的 $c,\delta,e,K_4$。不使用有限域正性、一般 Padé 正常性或未识别的 Jacobi 范数。

## 1. 实际第四插入与全部低层补偿

置
$$
p=6k-1\ge41,\qquad A=2k-1,\qquad N=k-1,\qquad d=p-5=6k-6.
$$
在 R1183 的同一曲线上取
$$
\mathscr H:X^{p+1}+Y^{p+1}=1,\quad
\Omega=\frac{dX}{Y^p},\quad
D_H=Y^p\partial_X-X^p\partial_Y.
$$
原覆盖为 $\pi(X,Y)=(X^k,Y^k)$。令
$$
f=kX^AY^A,\qquad g=kX^{k-1}Y^A,\qquad
P=\pi^*P_{22}.
$$
因此 $dP=f\Omega$，而 $g\Omega=\pi^*\omega_{12}$。此处的 $P_{22}$ 是原已锁定的 $-\Psi/(b_0\delta)$，不另换 primitive 的规范。

在本节的 $e=0$ 分支，原第零至第三插入全部为零：
$$
C_{\rm abs}(P^j g\Omega)=0\qquad(0\le j<4).
\tag{E.1}
$$
写
$$
X_s=X+sY^p,\quad Y_s=Y-sX^p,\quad
I(s)=\int_0^s f(X_t,Y_t)\,dt.
$$
$f$ 的次数是 $4k-2<p-1$，故 $I$ 的全部分母最多为 $4k-1<p$。实际导子杀掉 $X^p,Y^p$，所以这些是原 Taylor 系数；不需要把 $(X_s,Y_s)$ 当作超出 $s^p$ 精度的曲线上点。

由 $D_H^p=0$ 和 $(p-1)!=-1$，对任意原函数 $h$ 有
$$
\left(\frac{C_{\rm abs}(h\Omega)}{\Omega}\right)^p
=[s^{p-1}]\exp(sD_H)h.
$$
对 $(P+I(s))^4g(X_s,Y_s)$ 作完整二项展开，再用 (E.1)，准确得到
$$
\left(\frac{C_{\rm abs}(P^4g\Omega)}{\Omega}\right)^p
=[s^{p-1}]I(s)^4g(X_s,Y_s).
\tag{E.2}
$$
这一步使用了全部低插入；它不是未经核对地把有理 primitive 的常数项删掉。

## 2. 两变量原系数与准确的 $K_4$ 标量

定义分母全为单位的多项式
$$
\mathcal P(a,b)=\int_0^1(1+at)^A(1+bt)^A\,dt
=\sum_{i,j=0}^A\binom Ai\binom Aj\frac{a^ib^j}{i+j+1}.
\tag{E.3}
$$
最大分母为 $4k-1<p$。由于
$$
I(s)=ksX^AY^A\mathcal P\!\left(s\frac{Y^p}{X},-s\frac{X^p}{Y}\right),
$$
(E.2) 的右边可准确写成
$$
X^{3k+1}Y^{4k+1}\mathcal F(X^{p+1},Y^{p+1}),
\tag{E.4}
$$
其中 $\mathcal F$ 为齐次次数 $d$ 的二元多项式，系数为
$$
[z_1^Jz_2^{d-J}]\mathcal F
=k^5(-1)^J[a^{d-J}b^J]
\mathcal P(a,b)^4(1+a)^{k-1}(1+b)^A.
\tag{E.5}
$$

另一方面，原 Fermat 六次笔记 (G4.85) 在 $e=0$ 给
$$
C_{\rm abs}(P_{22}^4\omega_{12})
=\frac{4c^{2k-2}}{\delta^2}K_4\,\omega_{32}.
$$
这里 $c^p=-c$，故 $c^{2k-2}\in\mathbf F_p$；$K_4,\delta\in\mathbf F_p$。拉回再取 $p$ 次幂不会额外改变这个标量。将 (E.4) 的 $X,Y$ 指数逐一相减，并以 $z_1+z_2=1$ 齐次化，得到
$$
\boxed{\quad
\mathcal F(z_1,z_2)
=\frac{4kc^{2k-2}}{\delta^2}K_4\,
z_1^{3k-2}z_2^{2k-2}(z_1+z_2)^{k-2}.
\quad}
\tag{E.6}
$$
齐次度两边均为 $6k-6$。因此没有通过在曲线上相等而忽略一个额外的齐次倍数。

令
$$
T(\rho)=[a^d]\mathcal P(a,\rho a)^4
(1+a)^{k-1}(1+\rho a)^A.
\tag{E.7}
$$
由 $\mathcal F(z_1,z_2)=k^5z_2^dT(-z_1/z_2)$，(E.6) 等价于
$$
\boxed{\quad
T(\rho)=\kappa_4\rho^{3k-2}(1-\rho)^{k-2},\qquad
\kappa_4=4(-1)^k k^{-4}\frac{c^{2k-2}}{\delta^2}K_4.
\quad}
\tag{E.8}
$$

## 3. 原 primitive 的两个端点

置
$$
H(z)=\sum_{j=0}^A\binom Aj\frac{z^j}{2k+j},\qquad
\widetilde H(\rho)=(1-\rho)^A
H\!\left(\frac{\rho}{1-\rho}\right).
\tag{E.9}
$$
$H,\widetilde H$ 都是次数至多 $A$ 的多项式，所有 $2k+j<p$；且 $\widetilde H(0)=1/(2k)$。

在 $w=\rho/(1-\rho)$ 下，直接以 $u=1+at$ 换元，得完整恒等式
$$
\mathcal P(a,\rho a)
=\frac{(1-\rho)^A}{a}
\bigl((1+a)^{2k}H(w(1+a))-H(w)\bigr).
\tag{E.10}
$$
右边分子实际被 $a$ 整除。可先在 $a(1-\rho)\ne0$ 的环中证明，再作为多项式身份延伸；后面不在 $\rho=0,1$ 删除任何端点项。

为记录各窗口，定义
$$
\begin{aligned}
C_1&=[z^{3k-1}](1+z)^AH(z),&
C_2&=[z^{k-1}](1+z)^AH(z)^2,\\
C_3&=[z^{5k-2}](1+z)^AH(z)^3,&
C_{4a}&=[z^{3k-2}](1+z)^AH(z)^4,\\
C_{4b}&=[z^{9k-3}](1+z)^AH(z)^4.
\end{aligned}
\tag{E.11}
$$

## 4. 全部五块，包含四上端的第二个 $p$ 窗口

不附 $e=0$ 前提，(E.7) 的多项式准确为
$$
\begin{aligned}
T(\rho)={}&-4C_1\rho^{3k-1}(1-\rho)^{k-1}\widetilde H^3\\
&+6C_2\rho^{k-1}(1-\rho)^{5k-2}\widetilde H^2\\
&-4C_3\rho^{5k-2}(1-\rho)^{3k-2}\widetilde H\\
&+C_{4a}\rho^{3k-2}(1-\rho)^{7k-3}
+C_{4b}\rho^{9k-3}(1-\rho)^{k-2}.
\end{aligned}
\tag{E.12}
$$

以下逐一支付全部窗口。展开 (E.10) 的第四次幂，令 $l$ 为选择上端点的次数，$0\le l\le4$。若 $[z^j]H(z)^l=h_{l,j}$，则需读取
$$
[a^{p-1}](1+a)^{(2l+1)k-1+j}(1+\rho a)^A.
$$
原第一指数小于 $3p$。写它模 $p$ 的代表为 $e_0\in[0,p-1]$；由 $(1+a)^p=1+a^p$，此系数只取决于 $e_0$，并且只有 $p-1-e_0\in[0,A]$ 时非零。若 $L=p-1-e_0$，则
$$
[a^{p-1}](1+a)^{e_0}(1+\rho a)^A
=\binom AL\rho^L(1-\rho)^{A-L}.
\tag{E.13}
$$
这是逐项使用
$\binom{p-1-L}{p-1-h}=(-1)^{h-L}\binom hL$
的有限二项式恒等式。

若共减去 $q p$，则 $L=C-j$，其中
$$
C=(5-2l)k-1+q p.
$$
乘回 $w^j$ 后，$\rho$ 与 $1-\rho$ 的指数分别恒为 $C$ 与 $A-C$。对 $j$ 求和正好给 $[z^C](1+z)^AH^l$。因此只需保留
$$
0\le C\le(l+1)A.
$$
全部允许的 $(l,C)$ 恰为
$$
(1,3k-1),\ (2,k-1),\ (3,5k-2),\
(4,3k-2),\ (4,9k-3).
$$
对应的符号和二项系数为 $-4,6,-4,1,1$，给出 (E.12)。尤其四个上端点确有两个窗口；第二个 $C_{4b}$ 不能因指数超过 $p$ 就删掉。

## 5. 两上端整块恰为原 $e$ 槽

令原 Dixon 积分为
$$
F_D(x)={}_2F_1(1/3,2/3;4/3;x).
$$
在当前所需次数内，$2k\equiv1/3$、$A\equiv-2/3$ 给
$$
H(z)=\frac1{2k}F_D(-z),\qquad
(1+z)^A=(1+z)^{-2/3}.
$$
等式表示相应的安全截断；不外推至超出多项式次数的无限级数。原 Dixon 笔记 (J.24) 的同一谱归一是
$$
r_N(0)=[x^N](1-x)^{-2/3}F_D(x)^2.
$$
因此
$$
\boxed{\quad C_2=\frac{(-1)^N}{4k^2}r_N(0).\quad}
\tag{E.14}
$$
原 $e=0$ 等价于 $r_N(0)=0$，所以它删除 (E.12) 的**整个**第二行。这不是把各个上端积分分别设零。

## 6. 真正第四槽与仍未解决的消失问题

现用 $e=0$。比较 (E.12) 与 (E.8) 的 $\rho^{3k-2}$ 首项，得到
$$
\boxed{\quad
C_{4a}=\kappa_4,\qquad
K_4=\frac{(-1)^k k^4\delta^2}{4c^{2k-2}}C_{4a}.
\quad}
\tag{E.15}
$$
四上端的第二窗口也必须比较。减去 (E.8)，并除共同多项式 $\rho^{3k-2}(1-\rho)^{k-2}$，由 $(1-\rho)^p=1-\rho^p$ 得
$$
-4C_1\rho(1-\rho)\widetilde H^3
-4C_3\rho^{2k}(1-\rho)^{2k}\widetilde H
+(C_{4b}-C_{4a})\rho^p=0.
$$
因为 $\widetilde H(0)=1/(2k)$，依次读取次数 $1,2k,p$，严格得到
$$
\boxed{\qquad C_1=C_3=0,\qquad C_{4b}=C_{4a}\qquad(e=0).\qquad}
\tag{E.16}
$$
这些是原完整第四插入的后果，没有把一上端或三上端项凭对称性先行删去。

也可直接由 $z^AH(1/z)=-H(z)$ 和
$zH'+2kH=(1+z)^A$ 得
$$
C_{4b}=-\frac{k}{5}[z^{k-2}]H(z)^5.
\tag{E.17}
$$
因此 (E.16) 与原左右半块的临界谱导数相容。它没有制造一个额外独立的单位。

本稿实际完成的是原 Hermitian 输出、全部五个端点块及两个四上端窗口的准确比较。还没有证明：当 (E.14) 为零时，(E.15) 的指定系数必非零。$H$ 的各系数、$H(-1)$ 或全空间 Cartier–Serre 张量非退化，都不能替代这个指定系数的非零性。

## 来源与范围

- [R1183 §§1–5](R1183-original-Hermitian-Cartier-Serre-trilinear-tensor.md)：原 Hermitian 导子、Cartier 与 degree-$k^2$ 覆盖。
- [原 genus 4 / Fermat 六次笔记 §§7、13–14](../notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md)：原 $P_{22}$、全部低插入及 (G4.85) 的绝对 Cartier 标度。
- [原 Dixon–Jordan 笔记 §§6–8](../notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)：同一 $r_N$ 谱多项式和 $r_N(0)=\eta_k$，未引入辅助谱参数。

以上为纸面多项式与函数域证明；没有运行数学程序或扫描素数。

o1_theta 完成原系数推导；root 逐项核定 Taylor/Cartier、五个窗口、齐次度和谱尺度后直接登记。原指定系数非零与主完成标准继续开放。
