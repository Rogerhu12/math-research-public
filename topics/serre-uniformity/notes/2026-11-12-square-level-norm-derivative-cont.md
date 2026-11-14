# 平方水平新形式的范数、导数与非消失数：独立核验

日期：2026-11-12
会话：nonsplit-frobenius
状态：以下解析引理证明完整；供 global-geometry 的 Heegner 商维数论证使用，尚未单独编号。

## 0. 可直接使用的结论

设 $p$ 为素数，$M=p^2$，$f=\sum_{n\ge1}a_n(f)e^{2\pi inz}$ 为
$S_2(\Gamma_0(M))^{\mathrm{new}}$ 中 $a_1(f)=1$ 的新形式，特征平凡。范数使用

$$
\|f\|_M^2
=
\int_{\Gamma_0(M)\backslash\mathbb H}|f(z)|^2\,dx\,dy,
\tag{0.1}
$$

不除以双曲体积。对每个 $\epsilon>0$，有一致估计

$$
\|f\|_M^2\gg_\epsilon M^{1-\epsilon},
\qquad
|L'(f,1)|\ll_\epsilon M^{1/4+\epsilon}.
\tag{0.2}
$$

第一式允许无效常数，包含 CM 形式与所有 $p$ 处局部类型；第二式可取有效常数。
两个估计都对 Fricke 正负号成立。正 Fricke 形式还满足较精细的

$$
|L'(f,1)|\ll M^{1/4}\log(2M).
\tag{0.3}
$$

结合 Dogra–Le Fourn（下称 DLF）的**平方水平**一阶矩可推出：若
$r(p)$ 为正 Fricke、精确水平 $p^2$、满足 $L'(f,1)\ne0$ 的归一化复新形式数，
则对每个 $\delta>0$，

$$
r(p)\gg_\delta p^{3/2-\delta}\log p.
\tag{0.4}
$$

此处每个系数域嵌入对应一个形式；不能把 $r(p)$ 误读成 Galois 轨道数。
因此对任意固定 $C>0$，充分大的 $p$ 满足 $r(p)>Cp$。
在 DLF 的 Heegner 商定义下，Galois 稳定性把这个数解释为商的维数；
几何代理另行处理该解释及与超奇异分量数的比较。

## 1. 原始文献的范围与归一化

**HL.** J. Hoffstein–P. Lockhart，
*Coefficients of Maass forms and the Siegel zero*，
Annals of Mathematics **140** (1994), 161–181（正文至 176，后附 GHL 附录）。

- [期刊页](https://annals.math.princeton.edu/1994/140-1/p04)
- [作者托管正文](https://www.math.columbia.edu/~goldfeld/CoeffMaassForms.pdf)

所需精确位置：

1. p.164，Theorem 0.2 及紧随其后的说明：对任意 $\eta>0$，
   $L(1,\operatorname{Ad}f)\gg_\eta (\lambda N)^{-\eta}$，
   可对所有形式统一取一个无效正常数。
2. 同页最后的 Remark 将结论推广到全纯权 $k$，将 $\lambda N$ 换成 $kN$。
   因而固定权 $2$ 给 $L(1,\operatorname{Ad}f)\gg_\eta N^{-\eta}$。
3. p.175，Theorem 0.2 证明首段明确先处理来自 $\mathrm{GL}_1$ 的
   monomial 形式，利用二次 Dirichlet 因子与二次域 Hecke 因子及 Siegel 下界；
   之后才假定 nonmonomial。故不能在本引理中删去 CM 形式。
4. pp.162–163，(0.7)–(0.9) 的坏 Euler 因子满足
   $N^{-\eta}\ll_\eta L_N(1)\ll_\eta N^\eta$，覆盖各局部分歧类型。
5. HL p.161 的 Maass 范数除以体积；下文不直接移用其首 Fourier
   系数公式，而重新展开，避免把这一归一化搬错。

这里仅使用无效的一致下界，不使用“一个有效例外”的更细表述：
同一个 adjoint lift 可能来自多个二次扭曲，HL p.164 已提醒这一点。

**DLF.** N. Dogra–S. Le Fourn，
*Quadratic Chabauty for modular curves and modular forms of rank one*，
Mathematische Annalen **380** (2021), 393–448，
[DOI / 全文](https://doi.org/10.1007/s00208-020-02112-3)。

使用 §5 开头的范数定义、Lemma 15、Lemma 16 与公式 (37)–(38)。
其范数正是 (0.1)，其正 Fricke 空间的函数方程符号为 $-1$。
Remark 8 中引用的 $7/8$ 比例明确至少限制于素数水平；
这里完全不调用该比例。

**AL.** A. O. L. Atkin–J. Lehner，
*Hecke operators on $\Gamma_0(m)$*，
Math. Ann. **185** (1970), 134–160，
[DOI](https://doi.org/10.1007/BF01359701)，Theorem 3，p.147：
平凡特征新形式在 $q^2\mid N$ 时有 $a_q=0$，
在 $q\parallel N$ 时有 $|a_q|=q^{k/2-1}$，且 $a_{qn}=a_qa_n$。

**D.** P. Deligne，
*La conjecture de Weil. I*，
Publ. Math. IHÉS **43** (1974), 273–307，
[原刊存档](https://www.numdam.org/articles/10.1007/BF02684373/)，
Théorème (8.2)，p.302：
精确水平、任意特征的全纯归一化新形式，在 $q\nmid N$ 的 Satake
根绝对值为 $q^{(k-1)/2}$。

## 2. 重新展开 Petersson 范数

暂令 $N$ 为任意正整数，$f$ 为权 $2$、特征平凡的归一化新形式。
记

$$
I_N=[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)]
=
N\prod_{q\mid N}(1+q^{-1}),
\qquad
\lambda_n=\frac{a_n}{\sqrt n},
\qquad
R_f(s)=\sum_{n\ge1}|\lambda_n|^2n^{-s}.
$$

取无穷尖点宽度为 $1$ 的非全纯 Eisenstein 级数
$E_\infty(z,s)=\sum_{\Gamma_\infty\backslash\Gamma_0(N)}
\operatorname{Im}(\gamma z)^s$。其在 $s=1$ 的留数为
$\operatorname{vol}(\Gamma_0(N)\backslash\mathbb H)^{-1}
=3/(\pi I_N)$。Rankin–Selberg 展开逐项给

$$
\begin{aligned}
\int_{\Gamma_0(N)\backslash\mathbb H}
|f(z)|^2y^2E_\infty(z,s)\frac{dx\,dy}{y^2}
&=
\int_0^\infty\int_0^1|f(x+iy)|^2y^s\,dx\,dy\\
&=
\frac{\Gamma(s+1)}{(4\pi)^{s+1}}
\sum_{n\ge1}\frac{|a_n|^2}{n^{s+1}}\\
&=
\frac{\Gamma(s+1)}{(4\pi)^{s+1}}R_f(s).
\end{aligned}
\tag{2.1}
$$

在 $s=1$ 比较留数（$\Gamma(2)=1$）：

$$
\boxed{\quad
\|f\|_N^2=\frac{I_N}{48\pi}
\operatorname*{Res}_{s=1}R_f(s).
\quad}
\tag{2.2}
$$

用 HL 的坏因子定义，即

$$
\zeta(2s)R_f(s)
=
\zeta(s)L_N(s)L(s,\operatorname{Ad}f),
\tag{2.3}
$$

得到

$$
\boxed{\quad
\|f\|_N^2
=
\frac{I_N}{8\pi^3}
L_N(1)L(1,\operatorname{Ad}f).
\quad}
\tag{2.4}
$$

这个公式采用 HL 的单位化 Hecke 系数 $\lambda_n$，
而不是算术系数 $a_n$；$\zeta(2)=\pi^2/6$ 正是常数中的来源。

对给定 $\epsilon>0$，分别对 HL 的两个因子使用 $\eta=\epsilon/2$：

$$
L_N(1)\gg_\epsilon N^{-\epsilon/2},
\qquad
L(1,\operatorname{Ad}f)\gg_\epsilon N^{-\epsilon/2}.
$$

又 $I_N\ge N$，故

$$
\|f\|_N^2\gg_\epsilon N^{1-\epsilon}.
\tag{2.5}
$$

这已证明所需范数估计，并且实际上允许任意水平。
证明没有假定局部分量属于 principal series、Steinberg 或 supercuspidal 中的某一类。

### 2.1. 平方水平的精确核对

令 $N=p^2$。AL Theorem 3 给 $a_p=0$ 与 $a_{pn}=a_pa_n=0$。
因而 $R_f(s)$ 的 $p$ Euler 因子为 $1$。对 $q\ne p$，
设单位化 Satake 根为 $\alpha_q,\alpha_q^{-1}$；
Hecke 关系给局部恒等式

$$
\sum_{r\ge0}\lambda_{q^r}^2q^{-rs}
=
\frac{1+q^{-s}}
{(1-q^{-s})(1-\alpha_q^2q^{-s})(1-\alpha_q^{-2}q^{-s})}.
$$

特征平凡保证系数实数，故平方就是绝对值平方。于是

$$
R_f(s)
=
\frac{\zeta^{(p)}(s)}
{\zeta^{(p)}(2s)}
L^{(p)}(s,\operatorname{Ad}f).
\tag{2.6}
$$

上标 $(p)$ 表示删除整个 $p$ 局部因子。因此

$$
\operatorname*{Res}_{s=1}R_f(s)
=
\frac{L^{(p)}(1,\operatorname{Ad}f)}
{\zeta(2)(1+p^{-1})},
$$

而 $I_{p^2}=p^2(1+p^{-1})$。代入 (2.2)：

$$
\boxed{\quad
\|f\|_{p^2}^2
=
\frac{p^2}{8\pi^3}
L^{(p)}(1,\operatorname{Ad}f).
\quad}
\tag{2.7}
$$

(2.7) 与 (2.4) 相容，因为此时
$L_{p^2}(1)=[(1+p^{-1})L_p(1,\operatorname{Ad}f)]^{-1}$。
本笔记不需要再以某个局部类型公式替代 HL 的统一坏因子估计；
这也避免遗漏 CM 或 ramified principal-series 形式。

## 3. 从函数方程直接控制中心导数

对于精确水平 $M=p^2$，AL 与 D 的结论及乘法性给出

$$
|a_n(f)|\le d(n)\sqrt n
\quad(n\ge1).
\tag{3.1}
$$

在 $p\mid n$ 时左边为 $0$，其他素幂由两个绝对值 $\sqrt q$
的 Satake 根展开：$|a_{q^r}|\le(r+1)q^{r/2}$。
这一步同样不区分 CM 与非 CM。

置

$$
X=\frac{\sqrt M}{2\pi},\qquad
\Lambda(f,s)=X^s\Gamma(s)L(f,s).
$$

若 $f|w_M=w f$，$w\in\{\pm1\}$，则

$$
\Lambda(f,2-s)=\eta\Lambda(f,s),\qquad \eta=-w.
$$

为同时核对两个符号，可从 Mellin 积分在 $t=1$ 切开得到

$$
\Lambda(f,s)
=
\int_1^\infty f(it/\sqrt M)
\bigl(t^{s-1}+\eta t^{1-s}\bigr)\,dt.
\tag{3.2}
$$

由于积分下限远离 $0$ 且尖点处指数衰减，可在紧集上一致微分。

### 3.1. 正 Fricke：根数 $-1$

此时 $\eta=-1$，所以 $L(f,1)=0$。由 (3.2) 的导数：

$$
L'(f,1)
=
2\sum_{n\ge1}\frac{a_n(f)}{n}E_1(n/X),
\qquad
E_1(u)=\int_u^\infty\frac{e^{-t}}t\,dt.
\tag{3.3}
$$

这与 DLF Lemma 15 完全一致。对任意 $\epsilon>0$，取一个固定
$0<\eta_0\le\epsilon$，用 $d(n)\ll_{\eta_0}n^{\eta_0}$ 及 Tonelli：

$$
\begin{aligned}
|L'(f,1)|
&\ll_{\eta_0}\sum_{n\ge1}
n^{-1/2+\eta_0}E_1(n/X)\\
&=
O_{\eta_0}\left(
\int_0^\infty\frac{e^{-t}}t
\sum_{n\le Xt}n^{-1/2+\eta_0}\,dt
\right)\\
&\ll_{\eta_0}
X^{1/2+\eta_0}
\int_0^\infty e^{-t}t^{-1/2+\eta_0}\,dt\\
&\ll_{\epsilon}M^{1/4+\epsilon}.
\end{aligned}
\tag{3.4}
$$

空和按 $0$ 处理，故 $Xt<1$ 没有端点问题；
最后积分是有限的 $\Gamma(1/2+\eta_0)$。

如要得到对数版本，写 $d(n)=\sum_{ab=n}1$，则对 $T\ge1$，

$$
\begin{aligned}
\sum_{n\le T}\frac{d(n)}{\sqrt n}
&=
\sum_{a\le T}\frac1{\sqrt a}
\sum_{b\le T/a}\frac1{\sqrt b}\\
&\le
2\sqrt T\sum_{a\le T}\frac1a\\
&\le2\sqrt T(1+\log T).
\end{aligned}
$$

将此替入 (3.4)，由
$\log(2+Xt)\ll\log(2+X)+|\log t|+t$ 可得
$|L'(f,1)|\ll\sqrt X\log(2+X)$，
即 (0.3)（有限个小 $M$ 可吸收进绝对常数）。

### 3.2. 负 Fricke：根数 $+1$

此时 $\eta=1$，从函数方程得 $\Lambda'(f,1)=0$，而 (3.2) 给

$$
L(f,1)=2\sum_{n\ge1}\frac{a_n(f)}n e^{-n/X}.
\tag{3.5}
$$

因此

$$
L'(f,1)
=
-\bigl(\log X+\Gamma'(1)\bigr)L(f,1)
=
-(\log X-\gamma)L(f,1),
\tag{3.6}
$$

其中 $\gamma>0$ 是 Euler–Mascheroni 常数；写成 $\Gamma'(1)$
可以避免不同文献对 $\gamma$ 的符号记法引起混淆。

由 (3.1)、(3.5) 与同一加权除数和估计，

$$
|L(f,1)|\ll M^{1/4}\log(2M),
\qquad
|L'(f,1)|\ll M^{1/4}\log^2(2M).
\tag{3.7}
$$

故任意 $\epsilon>0$ 时仍有 $|L'(f,1)|\ll_\epsilon M^{1/4+\epsilon}$。
这证明 (0.2) 所声称的全部符号范围，无需另行调用导数的凸性界。

## 4. 确实在平方水平求和

记 $\mathcal B^{+,\mathrm{new}}(p^2)$ 为所有正 Fricke
归一化新形式组成的正交复基。DLF 的定义给

$$
S_1(p^2)
=
\langle a_1,L'\rangle_{p^2}^{+,\mathrm{new}}
=
\sum_{f\in\mathcal B^{+,\mathrm{new}}(p^2)}
\frac{L'(f,1)}{\|f\|_{p^2}^2}.
\tag{4.1}
$$

其公式 (37)–(38)，取 $m=1$、$N=p$，给

$$
\frac{S_1(p^2)}{4\pi}
=
E_1(2\pi/p)
-\frac{E_1(2\pi/\sqrt p)}{p-1}
-\frac{\log p}{2(p-1)}e^{-2\pi/\sqrt p}
+O\!\left(\frac1p+\frac{\log p}{p^{3/2}}\right).
\tag{4.2}
$$

$E_1(x)=-\log x-\gamma+O(x)$，故

$$
S_1(p^2)
=
4\pi\log p+O(1).
\tag{4.3}
$$

特别地，充分大的 $p$ 满足 $|S_1(p^2)|\gg\log p$。
Lemma 16 的旧形式扣除已经包含在 (4.2) 中，
不能拿整个平方水平空间的一阶矩代替新空间一阶矩。

由 (0.2)，对每个形式有

$$
\left|\frac{L'(f,1)}{\|f\|_{p^2}^2}\right|
\ll_\epsilon(p^2)^{-3/4+2\epsilon}
=
p^{-3/2+4\epsilon}.
\tag{4.4}
$$

三角不等式就给

$$
\log p
\ll |S_1(p^2)|
\le
r(p)\max_f
\left|\frac{L'(f,1)}{\|f\|_{p^2}^2}\right|
\ll_\epsilon r(p)p^{-3/2+4\epsilon}.
\tag{4.5}
$$

这里**不需要**先证明每一项非负。置 $\epsilon=\delta/4$ 即得到 (0.4)。
例如固定 $\delta=1/4$，便有
$r(p)\gg p^{5/4}\log p$，已经严格快于任何 $O(p)$ 的分量数。

DLF Lemma 14 引用 Gross–Zagier Corollary V.1.3，说明
$L'(f,1)\ne0$ 对 $f$ 的所有 Galois 共轭同时成立。
因而把每个整轨道对应的 $A_f$ 加入 Heegner 商时，轨道内形式数
$[K_f:\mathbb Q]=\dim A_f$；求和正好得到商的维数。

## 5. 精确边界

此论证给出可证明的“充分大”维数增长，常数及阈值可以无效。
它没有给出平方水平上非消失形式的正比例，也没有把素数水平比例结果外推。

维数不等式本身不等于 Serre 一致性：还需几何论证建立
相应对称对应的退化限制、非零性与有理点约束。
本笔记完成的是这一几何路线所需的解析输入。
