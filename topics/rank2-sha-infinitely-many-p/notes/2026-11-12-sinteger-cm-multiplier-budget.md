# 固定 S-integer CM 乘子把惰性常数降至 0.26103

日期：2026-11-12。**状态：以下固定对象、分母预算与常数均已证明；主问题仍未完成。**

此前将乘子限为 Gaussian 整数并非必要。一个固定的 $K^\times$ 元
在有限个素数以外仍给整的 CM 形式自同态；
其复绝对值大于一时也仍有严格收缩的一致化。
但其 cyclotomic 因子的分母随权增长，不能当作固定误差略去。
本篇对一个具体乘子完整计入这些分母。

## 1. 新的固定乘子

沿用 $E/K$、$f=34(1+i)$ 和非零的 $\mu_4$ 不变函数 $\ell_0$。
取
$$
b=2+i,\qquad
\beta=(1+i)\frac b{\bar b}
=\frac{-1+7i}{5},\qquad
N(\beta)=2,\quad |\beta|=\sqrt2.
\tag{1.1}
$$
它不是 Gaussian 整数，但在所有 $p\nmid10$ 的局部环中为单位。
形式映射 $[\beta]$ 可写成 $[1+i]\circ[b]\circ[\bar b]^{-1}$；
在这些地方逆映射整且唯一。
不需要把它认作一个全局整同源或固定理想的 Frobenius。

记
$$
h(z)=\ell_0(\operatorname{Exp}_Ez)
=\sum_{\substack{k\ge4\\4\mid k}}h_kz^k.
$$
对 $m\ge1$，定义
$$
F_{\beta,m}(z)=\sum_{\substack{k\ge4\\4\mid k}}
\frac{h_k}{(\beta^k-1)^m}z^k
=\sum_{n\ge0}\binom{m+n-1}{n}
h(z/\beta^{m+n}).
\tag{1.2}
$$
这是 $(\sigma_\beta-1)^mF_{\beta,m}=h$ 的常数项为零的唯一正则解。
因为 $|\beta|>1$，右边在紧集上正常收敛为亚纯函数。
此前的缩放格计数直接给
$$
T(R,F_{\beta,m})=O(R^2).
\tag{1.3}
$$
使用 genus-two canonical product 对极点作整齐次表示，
可对每个 $\varepsilon>0$ 得到 Herblot 意义的增长阶数
$\rho\le2+\varepsilon$；无需额外宣称整数阶的有限型分解。

## 2. 共轭迹的非代数性

令
$$
\mathcal J_m=F_{\beta,m}+\overline{F_{\beta,m}}\in\mathbb Q[[t]].
\tag{2.1}
$$
取 $\ell_0$ 的一个极点 $s$，留数 $r_s\ne0$。
选择复对数 $z_s=\Omega\eta/f$，并用 CRT 使 $\eta$ 在 $b,\bar b$ 处均为单位。
令 $z_n=\beta^{m+n}z_s$。

在 (1.2) 的第 $j$ 项中，对应的内部点是
$\operatorname{Exp}_E(\beta^{n-j}z_s)$。
若 $n-j>0$，它有不能消去的 $\bar b$ 分母；
若 $n-j<0$，它有不能消去的 $b$ 分母。
两种情况下都不是 $f$-division 点。
因此只有 $j=n$ 一项有极点，留数为
$$
\operatorname{Res}_{z_n}F_{\beta,m}(z)\,dz
=\binom{m+n-1}{n}\beta^{m+n}r_s\ne0.
\tag{2.2}
$$
共轭项的任何内部比值
$\beta^{m+n}/\bar\beta^{m+j}$
在 $\bar b$ 处都有严格负的赋值，所以共轭项在 $z_n$ 正则。

另一方面，$P_n=\operatorname{Exp}_Ez_n$ 的 $\bar b$-primary 阶
恰随 $m+n$ 增长。因为 $f,\eta,1+i,b$ 都在 $\bar b$ 处为单位，
这一分母不能被抵消。所以这些 $P_n$ 两两不同。
若 $\mathcal J_m$ 代数于 $\overline{\mathbb Q}(E)$，
它在某个有限覆盖曲线上成为代数函数，其极点在 $E$ 上的像只有有限多个。
式 (2.2) 却给出无限多个不同的极点像，矛盾。
故
$$
\boxed{\mathcal J_m\text{ 不代数于 }\overline{\mathbb Q}(E).}
\tag{2.3}
$$
这里无需假定新乘子在原极点支撑上置换，也没有把分式乘子误作全局整同源。

## 3. 惰性处的阶数分解

设 $p\equiv3\pmod4$、$p\nmid10$，并置
$$
d_p=\operatorname{ord}_{\mathbb F_{p^2}^\times}(\beta),\quad
a_p=\operatorname{ord}_{\mathbb F_p^\times}(2),\quad
r_p=\operatorname{ord}_{\mathbb F_{p^2}^\times}(\beta/\bar\beta),
$$
$$
D_p=\operatorname{lcm}(d_p,4),\qquad
c_p=v_p(\beta^{d_p}-1).
\tag{3.1}
$$
Frobenius 是共轭，故
$$
a_p=\frac{d_p}{\gcd(d_p,p+1)},\qquad
r_p=\frac{d_p}{\gcd(d_p,p-1)}.
\tag{3.2}
$$
写 $p-1=2s$、$p+1=2^tv$，其中 $s,v$ 奇且 $t\ge2$。
若 $d_p=2^e d_-d_+$，则 $d_-\mid s,d_+\mid v$，且
$$
a_p=2^{\max(e-t,0)}d_-,
\qquad r_p=2^{\max(e-1,0)}d_+.
$$
所以
$$
\begin{array}{c|c}
\text{条件}&D_p\\ \hline
a_p\text{ 奇},\ r_p\text{ 奇}&4a_pr_p\\
a_p\text{ 奇},\ r_p\text{ 偶}&2a_pr_p\\
a_p\text{ 偶}&a_pr_p.
\end{array}
\tag{3.3}
$$
还有本乘子特有的限制：
$$
a_p\text{ 偶}\Longrightarrow p\equiv3\pmod8
\Longrightarrow v_2(p+1)=2
\Longrightarrow v_2(r_p)=2.
\tag{3.4}
$$
第一步用 $(2/p)=-1$ 与 $v_2(p-1)=1$，
最后一步用 $a_p$ 偶迫使 $e=t+1$。

深度满足
$$
c_p\le v_p(2^{a_p}-1),\qquad
c_p\le v_p((\beta/\bar\beta)^{r_p}-1).
\tag{3.5}
$$
这是对范数、商取深度，再用 $p$ 不整除各个阶数的提升指数公式。
整个共轭迹的局部估计仍使用相同的 $c_p,D_p$。

## 4. 逐权分母的准确清除

令 $\zeta_8=(1+i)/\sqrt2$，并置
$$
\alpha=\zeta_8b^2,\qquad
\alpha'=\bar\zeta_8\bar b^2.
$$
则
$$
\alpha\alpha'=25,\qquad
(\alpha+\alpha')^2=2,\qquad
\alpha/\alpha'=\beta/\bar\beta,
\qquad |\alpha|=|\alpha'|=5.
\tag{4.1}
$$
$\alpha,\alpha'$ 为代数整数，且其商不是根单位。
因此 Stewart §4、Lemma 4.1 的原始假设均满足。

对 $r>2$，令
$$
L_r=\Phi_r(\alpha,\alpha').
$$
它是一个非零有理整数。
证明是：$\Phi_r(X,Y)$ 为对称齐次整系数多项式，其次数 $\varphi(r)$ 为偶数，
故可以写成 $(X+Y)^2$ 与 $XY$ 的整系数多项式；
再代入 (4.1)。
准确的分母恒等式是
$$
\boxed{\quad
\Phi_r(\beta,\bar\beta)
=2^{\varphi(r)/2}5^{-\varphi(r)}L_r.
\quad}
\tag{4.2}
$$
因此在所有 $p\ne2,5$ 处，其正赋值准确来自整数 $L_r$。
Stewart 的估计给
$$
\log|L_r|
=\varphi(r)\log5
+O(2^{\omega(r)}\log(r+1)).
\tag{4.3}
$$
这就是本篇角向预算的整个主项 $\log5$。
它既不是 $\tfrac12\log2$，也没有把随 $r$ 增长的 $5^{-\varphi(r)}$
误放进 $O(1)$。
若直接使用 raw numerator $-1\pm7i$，其公共的
$2^{\varphi(r)/2}$ 也由 (4.2) 显式剥离，因为只计 $p\ne2$。

由实际阶数和 $p\nmid a_p,r_p$，primitive 因子比较给
$$
\sum_{a_p=a}c_p\log p\le\log|\Phi_a(2)|,
\qquad
\sum_{r_p=r}c_p\log p\le\log|L_r|\quad(r>2).
\tag{4.4}
$$
$r=1,2$ 只涉及固定有限素数，贡献可单独并入常数。
两侧对应的高度主系数准确为
$$
L_N=\log2,\qquad L_R=\log5.
\tag{4.5}
$$

## 5. 优化后的完整加权和

定义
$$
M_\beta(k)=\sum_{D_p\le k}c_p\log p,\qquad
W_\beta(k)=\sum_{D_p\le k}\frac{c_p\log p}{D_p-1}.
$$
先看 $a_p$ 奇数部分，按 $a_p\le x$ 与 $a_p>x$ 划分。
后者在 $r_p$ 奇、偶两种情况下分别有
$r_p\le k/(4x)$、$r_p\le k/(2x)$。
由
$$
\sum_{\substack{n\le x\\n\text{ 奇}}}\varphi(n)\sim\frac{2x^2}{\pi^2},
\qquad
\sum_{\substack{n\le x\\n\text{ 偶}}}\varphi(n)\sim\frac{x^2}{\pi^2},
$$
和 (4.4)，得到主项
$$
\frac1{\pi^2}
\left(2L_Nx^2+\frac{3L_R}{8}\frac{k^2}{x^2}\right).
$$
优化后为 $\sqrt{3L_NL_R}\,k/\pi^2$。

对 $a_p$ 偶数部分，使用 $v_2(a_p)=1$ 和更强的 $v_2(r_p)=2$。
相应 totient 和的二次主系数为 $1/(2\pi^2)$、$1/(4\pi^2)$。
由 $D_p=a_pr_p$，得到
$$
\frac1{\pi^2}
\left(\frac{L_N}{2}x^2+\frac{L_R}{4}\frac{k^2}{x^2}\right),
$$
优化后为 $\sqrt{L_NL_R/2}\,k/\pi^2$。
阈值均为 $\sqrt k$ 的固定倍数，误差为 $O(\sqrt k\log^2k)$。
因此
$$
\boxed{\quad
M_\beta(k)\le C_\beta k+O(\sqrt k\log^2k),\qquad
W_\beta(k)\le C_\beta\log k+O(1),
\quad}
\tag{5.1}
$$
其中
$$
\boxed{\quad
C_\beta=
\frac{\sqrt3+1/\sqrt2}{\pi^2}\sqrt{\log2\,\log5}
=0.2610297209\ldots.
\quad}
\tag{5.2}
$$
第二式用已经证明的分部求和接口，误差项的相应积分收敛。

## 6. 实际 jet 界与 ordinary 接口

惰性局部的 height-two 坐标估计、整 tame 分解和直化证明仍适用：
$[\beta]$ 在所考虑的局部环上是整自同态，
而 $\beta^k-1$ 的赋值由 $d_p,c_p$ 和提升指数准确控制。
故
$$
S_p(\widehat{\operatorname{graph}}F_{\beta,m})
\ge p^{-1/(p^2-1)-mc_p/(D_p-1)}.
\tag{6.1}
$$
当 $D_p>k$ 时，前 $k$ 阶仍整；
由 (5.1)，整个惰性部分的实际 jet 预算至多为
$$
mC_\beta\log k+O(1).
\tag{6.2}
$$
对本题有用的 $m=3$，其系数是
$$
3C_\beta=0.7830891626\ldots.
$$
它比原 Gaussian 整数乘子方案的 $0.9450820411\ldots$ 下降，
但仍高于同一 $\mathbb Q$-曲面图像的 $1/4$ 门槛。

在普通目标素数处，$\beta\in\mathbb Z_p^\times$。
原先 $\sigma_b-b$ 的中心比较逐字适用于 $\sigma_\beta-\beta$：
若 $(T-p)^m\mid H_p(T)$，并且
$$
v_p(\beta^{p-1}-1)=1,
$$
则 $e_0F_{\beta,m}$ 为整级数。
额外的 ordinary tame 共振块与该非 Wieferich 条件失败时的深度，
本篇都没有统一控制。常数下降不等于本题完成。

## 7. 当前两预算法本身仍有明显余量缺口

若一般固定分式 Gaussian 乘子写为 $(a+bi)/c$，约去公共整数因子，
且其角向商不是根单位，则 norm 因子的有理高度至少为 $\log2$。
角向 primitive 因子在剥去公共 ramified 因子后，
其本类估计使用的复高度至少为 $\tfrac12\log5$：
对互素整数 $a,b$，排除 $ab=0$、$a=\pm b$ 后，
$(a^2+b^2)/g\ge5$，其中 $g=2$ 当 $a,b$ 同为奇数，否则 $g=1$。

因此，仅仅把新的高度放入本篇的“全部奇数 $a_p$”二预算覆盖公式，
其主系数就不会低于
$$
\frac{\sqrt{(3/2)\log2\,\log5}}{\pi^2}
=0.1310677151\ldots.
$$
即使先忽略偶数部分，乘以 $m=3$ 仍为 $0.3932031453\ldots>1/4$。
这是当前特定覆盖估计的限制，不是最优算术常数的下界；
更强的同时公因子估计、更多真实阶数限制或新的固定核仍可能改善它。
它说明只在同一个粗覆盖公式内继续换小乘子，尚不足以闭合本题。

## 来源

- R19 及此前加法 CM、惰性加权和、Herblot jet 三篇笔记。
- C. L. Stewart，*On divisors of Lucas and Lehmer numbers*，
  Acta Math. 211 (2013)，§4、Lemma 4.1，原文范围 $r>2$；
  [出版原文](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s11511-013-0105-y.pdf)。
- 本篇对 Lehmer pair 的全部假设、分母清除、正赋值预算、
  极点不相消及各个二进阶分支都给出了直接核查。
