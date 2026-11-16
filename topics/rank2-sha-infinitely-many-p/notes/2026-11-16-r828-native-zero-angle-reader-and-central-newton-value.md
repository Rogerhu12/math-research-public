# R828 增补 — 原零角左行的全三位读取与实际中央 Newton 值

日期：2026-11-16。**状态：下列原左行、整除式、中央 Newton 精度及同一修正的指定三位必要行已证明。指定值是否非零仍开放。**

本注使用[实际一标量四位系统](2026-11-16-r828-actual-one-scalar-four-digit-and-same-correction-pages.md)和[三条原 carry 递推](2026-11-16-r828-three-native-carry-recursions-and-last-block-tails.md)的同一个 $M_{\rm act}$。它给出一条具体 native 左行，直接读取原来源的三段系数，而不是另选一个未识别的余核元素。

## 1. 一条真正原零角左行

保持
$$
p=6s-1>211,\quad1\le\ell<s-13,\quad a=a_p\in\mathcal O^\times,
$$
$$
\Gamma=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^4,
w^{\ell+13}\epsilon^3).
$$
四个标准基行 $\epsilon^jw^{13}$，$0\le j\le3$，全部实际存在。
本节使用原 canonical 单部分，没有将第四算术来源免费添成一列。

原零角帽使只有相对 charge $0,1,2$ 的列有非零常数，
其总 charge 分别为 $40,41,42$。令
$$
r(Q)=(Q-40)(Q-41)(Q-42)
=Q^3-123Q^2+5042Q-68880.
\tag{1}
$$
定义目标上的**整行**
$$
\boxed{
\Lambda_0=
-68880[\epsilon^0w^{13}]
+\frac{5042}{a}[\epsilon w^{13}]
-\frac{246}{a^2}[\epsilon^2w^{13}]
+\frac6{a^3}[\epsilon^3w^{13}].
}
\tag{2}
$$
原公共四十、完整公共单位和十三前缀均在此式内。由
$r(40)=r(41)=r(42)=0$，
$$
\boxed{\bar\Lambda_0\,\bar M_0=0.}
\tag{3}
$$
所以它是同一个原首余核的实际左行。它就是原 $k=13$ 零角机制所用
三次 moment 行；以下支付它对任意同源向量的完整更高位读取。

对于只在源端使用的多项式 $\varphi(Q)$，记
$$
W_\varphi(X)=\sum_\Phi X_\Phi\varphi(Q_\Phi)A_\Phi(w).
$$
这没有新增来源：$\varphi(\mathcal E_{\rm tot})$ 在原 charge 直和中对角作用，
仍保原帽。记恢复实际高轴后的级数为
$$
\widetilde W_\varphi(X;H)
=\sum_\Phi X_\Phi\varphi(Q_\Phi)A_\Phi(w)
            e^{Q_\Phi H w^{s-4}B(w)},\qquad H=H_p.
\tag{4}
$$
所需次数不超过 $3s<p$，其整性由原实际窗口支付。
从现在起每个 $W$ 和 $\widetilde W$ 都包括原参考公共单位，
不能换成裸角多项式。

## 2. 全原来源上的准确 p-divided 行

对任意同格整向量 $X$，不先假设它是首核，准确有
$$
\boxed{
\frac{\Lambda_0M_{\rm act}(X)}p
\equiv
\frac1a[w^s]\widetilde W_{r'}(X;H)
+\frac p{a^2}[w^{2s}]\widetilde W_{r''}(X;H)
+\frac{p^2}{a^3}[w^{3s}]\widetilde W_{r'''}(X;H)
\pmod{p^3}.
}
\tag{5}
$$
特别左边是实际整向量的整标量商。

证明直接按原标准基折回。第 $j$ 块的 $w^{13}$ 行为
$$
\sum_{d=0}^j
 p^d\frac{a^{j-d}}{(j-d)!}
 [w^{ds}]\widetilde W_{Q^{j-d}}(X;H).
$$
乘上 (2) 的 $r_jj!a^{-j}$ 并求和，得到
$$
\Lambda_0M_{\rm act}(X)=
\sum_{d=0}^3\frac{p^d}{a^d}
 [w^{ds}]\widetilde W_{r^{(d)}}(X;H).
\tag{6}
$$
这里没有额外的 $1/d!$：
$j!/(j-d)!$ 本来就是 $r^{(d)}$ 的系数。
$d=0$ 项严格等于零，因为常数 charge 只在 (1) 的三个根上。
剩余各项均含 $p$，遂得 (5)。

原末端四次 carry 仍存在于完整 $M$；它的最小位置是
$\epsilon^3w^{s-3}$，而 $s-3>13$，
故它不进入这一条特定左行。没有将其从全矩阵删除。

为了明确 (5) 的全部实际高尾，置其右端为 $\mathcal N_H(X)$。
指数按所读次数准确截断，得到
$$
\boxed{
\begin{aligned}
\mathcal N_H(X)={}&
\frac1a\left([w^s]W_{r'}
           +H[w^4]B W_{Qr'}\right)\\
&+\frac p{a^2}\left(
 [w^{2s}]W_{r''}
 +H[w^{s+4}]B W_{Qr''}
 +\frac{H^2}{2}[w^8]B^2W_{Q^2r''}\right)\\
&+\frac{p^2}{a^3}\left(
 [w^{3s}]W_{r'''}
 +H[w^{2s+4}]B W_{Qr'''}
 +\frac{H^2}{2}[w^{s+8}]B^2W_{Q^2r'''}
 +\frac{H^3}{6}[w^{12}]B^3W_{Q^3r'''}\right)
 \pmod{p^3}.
\end{aligned}}
\tag{7}
$$
所有 $W$ 作用于同一 $X$。
$r'=3Q^2-246Q+5042$、$r''=6Q-246$、$r'''=6$，
因此 (7) 只涉及同一 $W_0,\ldots,W_3$，
但必须保所显示的 $s+4,2s+4,s+8$ 全卷积。

对真正 $\bar P\in K_1$，原首核的低阶消失使 (5) 首位收紧为
$$
\boxed{
\Lambda_0\beta_1^{\rm act}(P)
=\frac1a\left(
 [w^s]W_{r'}(P)+3H_p[w^4]B W_3(P)\right)\pmod p .
}
\tag{8}
$$
若 $\ell\ge5$，第二项在这一行确实为零；
$\ell\le4$ 时它读取原十二尾中的一个实际组合。
第一项仍是同一来源的指定 prime-diagonal，不预赋零。

## 3. 原完整中央给同 M 所需的唯一 Newton 值

沿前注记 $h_0=-a/18$，
$\mathfrak F(H)\in\mathcal O[H]^4$ 为四个原完整中央的模 $p^4$ 多项式，
并取
$$
\eta_0=e_0^tB_4^{-1},\qquad
C=\eta_0\mathfrak F(h_0),\qquad
D=\eta_0\mathfrak F'(h_0)\in\mathcal O^\times.
\tag{9}
$$
固定分子坏集仍按 R821 删除。
本节假设四个原完整中央同时为零；只在此假设下使用
$\mathfrak F(H_p)=0\bmod p^4$。因 $H_p-h_0\in p\mathcal O$，必有
$C\in p\mathcal O$。

定义这个由实际中央参考卷积确定的数
$$
\boxed{H_c=h_0-\frac CD.}
\tag{10}
$$
则
$$
\boxed{H_p-H_c\in p^3\mathcal O.}
\tag{11}
$$
证明使用前注已经支付的
$\mathfrak F''\in p\mathcal O[H]$、
$\mathfrak F'''\in p^2\mathcal O[H]$。
令 $\delta=H_p-h_0\in p\mathcal O$，Taylor 式给
$$
0=C+D\delta+\frac12\eta_0\mathfrak F''(h_0)\delta^2
 \pmod{p^4}.
$$
二次项属 $p^3$，而三次及以上项已在 $p^5$。
因此 $C+D\delta\in p^3$，得到 (11)。

更准确地，令
$$
\Delta_c=
\frac{\eta_0\mathfrak F''(h_0)}{2D}
       \left(\frac CD\right)^2\in p^3\mathcal O.
\tag{12}
$$
则
$$
H_p\equiv H_c-\Delta_c\pmod{p^4},\qquad
\mathfrak F(H_c)-\Delta_c\mathfrak F'(h_0)
 \in p^4\mathcal O^4.
\tag{13}
$$
除了投影 $\eta_0$ 外，其余三个完整中央条件仍在 (13) 中，
没有因 (10) 可写就被自动满足。

原矩阵的高轴一次项已经含 $p$，所以 (11) 准确推出
$$
\boxed{M_{\rm act}\equiv M_{H_c}\pmod{p^4}.}
\tag{14}
$$
也就是说，一次实际中央 Newton 读取已达到这个原四块矩阵的全部所需
高轴精度；中央的 $p^3$ 修正 $\Delta_c$ 在矩阵中从 $p^4$ 才开始出现。
它不是额外长窗或第五条深核。

这里没有把实际 $\mathcal R_p$ 删掉：
原 $M_0$、$B$、参考中央 $C,D$ 都保其实际 sigma 低卷积与全部高位。
(10) 是中央零假设下的精确替换，不是可以独立挑选的新 Gaussian。

## 4. 同一 P、R、S 上的指定三位条件

结合 (5)、(11)，对所有同源 $X$，
$$
\boxed{
\frac{\Lambda_0M_{\rm act}(X)}p
 \equiv\mathcal N_{H_c}(X)\pmod{p^3}.
}
\tag{15}
$$
右边就是 (7) 将 $H$ 换成实际 (10)；
所有除法整，且全 $s+4,2s+4,s+8$ 高卷积仍保。

若同一个真实提升满足
$$
M_{\rm act}(P+pR+p^2S+p^3T)\in p^4\Gamma,
$$
则必有这一个明确标量条件
$$
\boxed{
\mathcal N_{H_c}(P)+p\,\mathcal N_{H_c}(R)
+p^2\mathcal N_{H_c}(S)\in p^3\mathcal O.
}
\tag{16}
$$
等价地按同一修正依次读取：
$$
\mathcal N_{H_c}(P)\in p\mathcal O,
\tag{17}
$$
$$
\frac{\mathcal N_{H_c}(P)}p+
 \mathcal N_{H_c}(R)\in p\mathcal O,
\tag{18}
$$
$$
\frac{\mathcal N_{H_c}(P)/p+\mathcal N_{H_c}(R)}p+
 \mathcal N_{H_c}(S)\in p\mathcal O.
\tag{19}
$$
每一整商由上一条件支付。$T$ 不进入这条特定标量读取，
但仍参与全矩阵其余行。不能用不同的 $R$ 分别解 (18) 与其它 normal 行，
也不能以 (19) 替代原末短块或四次 carry。

(16) 是原真实左行的全三位必要条件，不只是一个尚未识别的
$C_1^*$ 元素的符号配对。另一方面，它仍只是全原矩阵的一条投影；
本注不将其单独可解性称为全提升可解。

## 5. 中央授权的边界

$r'(\mathcal E_{\rm tot})X$ 等仍是实际同格来源，
因此 (7) 完全可以在原有限格读取。但原四个中央零仅授权
$S,T,U,V$ 的四个指定算术函数；
它们不授权这些新的导子来源有中央零。

因此不能把 (5) 的三个系数当作三条新的零，
也不能因为 (10) 用到了四个完整中央就删掉 (7) 的 native prime-diagonal。
真正未闭的是：对一个实际 $P$ 与同一 $R,S$，
是否由其完整帽、原 normal 条件及其余三个中央残差迫使
(16) 非零，或者与全部其它原行不能相容。

本注完成的是这一指定问题的实际同源公式和精度运输，
不宣称已经得到所需的非零或无穷性。
本注为整符号证明，没有新增数值运行。
