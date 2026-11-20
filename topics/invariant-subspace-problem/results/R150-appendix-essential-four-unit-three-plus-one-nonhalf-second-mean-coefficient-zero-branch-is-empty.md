# R150 附录：单位 3+1 非半权支路的第二 mean 系数零边界为空

日期：2026-11-20 UTC。AI-assisted GPT-6 Astra Pro；Astra-ISP-b2a9acde-20261120 / r150_structure，根会话独立复核。

## 1. 剩余范围与一个适合原 jets 的坐标

沿用外均值 essential-four、rank $H=4$、孤立约化零点与活跃单位
$3+1$ 补空间的记号。已登记的完整排除依次处理了
$p=0$、半权 $a=b=1/2$ 与 $\alpha=0$。本稿独立限制在 $q\ne0$ 的图；$q=0$ 另按其原方程处理，不作为本稿前提中的已闭结论。
本附录在
$$
 p=1,\qquad b\ne0,1/2,\qquad q\ne0,\qquad \alpha\ne0
                                                               \tag{1.1}
$$
中排除另一个完整的 mean 系数零边界，并证明两个后续有理图所需的非零性。

仍使用原物理 jets
$$
 \tau(z)=(1-b)z_0+z_2+bz_3,\qquad
 K_{\mathcal B}=\begin{pmatrix}
 0&0&A&1\\
 0&-2A&B&q\\
 A&B&C&r\\
 1&q&r&0
 \end{pmatrix},
$$
$$
 A=x-b,\quad
 r=x(1+\kappa)-(1-2b)/2,\quad
 C=b\{1-2b+\kappa(1-2x)\},
$$
$$
 \phi=x+b\kappa/2,\qquad
 \alpha=x+b(\kappa-2),\qquad \beta_0=1/2-\kappa x.             \tag{1.2}
$$
代数是 $\mathcal B=\mathbb C[\epsilon]/(\epsilon^3)\oplus\mathbb C$。
$D_K,d,P,N_{\mathcal B},E$ 都从前一附录的原公式重建：
$$
 (D_Kz)_i=\tau((K_{\mathcal B})_{i,\bullet}z),\quad
 d=D_K1,\quad
 P(z)=\tfrac12\tau(z-\tau(z)1)^3,
$$
$$
 N_{\mathcal B}(z)=
 \tfrac12\tau((d-\phi)z^2)-(\tau z)\tau(dz)
 +\phi(\tau z)^2+\tfrac14\tau(zD_Kz),
$$
$$
 E=e-2D_Kd-2d^2+4\phi d.
                                                               \tag{1.3}
$$
原最高阶与二次梯度仍是 $T_3=P+R^3,\ N=N_{\mathcal B}+mR^2$。

因 $q\ne0$，定义
$$
                         s=B/q+b.
$$
原一次 mean 现在恰为
$$
                 \alpha s+b\beta_0=0.                         \tag{1.4}
$$
另两个原 mean 写成
$$
 R_2+\{b(1+2s)-4s^2\}q^2=0,\qquad
 R_P+(1-2s)q^2=0,                                             \tag{1.5}
$$
其中 $R_2,R_P$ 是从原 $E_2,E_3$ 置 $B=q=0$ 取得的原多项式；
上一附录已逐项给出。

令
$$
 \gamma=\alpha+2b\beta_0
       =x+b\kappa-b-2b\kappa x.
$$
由 (1.4)、$\alpha\ne0$，有 $1-2s=\gamma/\alpha$。
本附录的主要结论是
$$
                              \gamma\ne0.                    \tag{1.6}
$$

## 2. 两个原相容式及完整的 $s=x$、$p_0=0$ 排除

在三重点将 $P,N_{\mathcal B}$ 的原前三阶系数写作
$p_0,p_1,p_2,n_0,n_1,n_2$。原最高阶与 $N$ 不含除法地给出
$$
 c_0=3p_0n_1-2n_0p_1=0,\qquad
 c_1=6p_0n_2+p_1n_1-4n_0p_2=0.                              \tag{2.1}
$$
它们保留所有零值、零交叉配对与 $m=0$ 的候选。

从 (1.2)、(1.3) 直接展开，
$$
 p_0=x^3+\tfrac b2(1-3x),\qquad
 n_0=\tfrac b4\{1-2b+\kappa(2x-b-2x^2)\},
$$
$$
 \frac{p_1}{q}
 =3\{(x^2-b/2)s+b(1-2x)/2\},                                \tag{2.2}
$$
$$
 \frac{c_0}{q}
 =3\{p_0(x-b)(2xs-b)+n_0(2x^2-b)(x-s)\}.                     \tag{2.3}
$$

假设 $s=x$。原 (1.4) 立即化为
$$
                         x^2-2bx+b/2=0.
$$
所以 $x\ne0,\ 4x-1\ne0$，并且
$b=2x^2/(4x-1)$。
因 $b\ne1/2$，也有 $2x-1\ne0$。
将这个原关系代入 (2.3)，得到
$$
 \frac{c_0}{q}
       =\frac{12x^5(2x-1)^4}{(4x-1)^3}\ne0,
$$
与 (2.1) 矛盾。因此
$$
                               s\ne x.                       \tag{2.4}
$$

再假设 $p_0=0$。原最高阶在三重点常数项给
$p_0=-u_0^3$，故 $u_0=0$，原一次项也必须 $p_1=0$。
另一方面，
$$
 b=\frac{2x^3}{3x-1},\qquad x(3x-1)\ne0.
$$
$x=1/2$ 给 $b=1/2$，已排除。由 (2.2)
$$
 \frac{p_1}{q}=\frac{3x^2(2x-1)(s-x)}{3x-1}.
$$
故 $p_1=0$ 迫 $s=x$，违反 (2.4)。因此
$$
                               p_0\ne0.                      \tag{2.5}
$$
这两个引理适用于整个 (1.1)，并非只在下面的 $\gamma=0$ 边界上成立。

## 3. $\gamma=0$ 的原多项式必要条件

现假设 $\gamma=0$，即 $s=1/2$。
把 $x=1/2$ 代入原 (1.4) 得 $(1-2b)/4=0$，不可能。
故可以合法地置
$$
 D=b(1-2x)\ne0,\qquad
 \kappa=\frac{b-x}{b(1-2x)}.                                  \tag{3.1}
$$
在 (1.5) 中 $1-2s=0$，而
$b(1+2s)-4s^2=2b-1\ne0$。因此
$$
 R_P=0,\qquad q^2=\frac{R_2}{1-2b}.                           \tag{3.2}
$$
这里除数 $1-2b$ 已由 (1.1) 保证非零，不把 $q^2$ 当作新的自由量。

先从原点 mean 定义
$$
 \mathcal P(b,x)=D^2
 R_P\!\left(b,x,\frac{b-x}{D}\right).
$$
直接展开得一个关于 $b$ 的三次多项式：
$$
\begin{split}
 \mathcal P={}&b^3+
 (8x^3-12x^2+2x-\tfrac12)b^2
 +(8x^3-4x^4)b-2x^4.                                       \tag{3.3}
\end{split}
$$
再从原第一相容式定义
$$
 \mathcal C_0(b,x)
 =\left.\frac{c_0}{q}\right|_{s=1/2,\ \kappa=(b-x)/D}.
$$
它没有剩余分母，精确为
$$
 \mathcal C_0=\frac38\{
 (1-8x)b^3+(28x^2-7x+1)b^2
 -12(x^4+x^3)b+4x^5+4x^4\}.                                \tag{3.4}
$$

最后使用原第二相容式，定义
$$
 \mathcal C_1(b,x)=
 b(1-2x)^2(1-2b)\!
 \left.c_1\right|_{
 B=(1/2-b)q,\ \kappa=(b-x)/D,\
 q^2=R_2/(1-2b)}.                                           \tag{3.5}
$$
$c_1$ 在此处只含 $q^0,q^2$，所以 (3.5) 无需选择平方根。
按原 (1.3)、(2.1) 重建后，(3.5) 是一个关于 $b$ 的六次多项式。
它的定义就是原方程经过合法分母消去；配套源据此即时生成，
不保存可重算的三十五项展开表。

每一个原临界候选必有
$$
                   \mathcal P=\mathcal C_0=\mathcal C_1=0.    \tag{3.6}
$$

## 4. 两个小结式只剩已排除的原边界

直接在 $\mathbb Q[b,x]$ 计算关于 $b$ 的两个结式。
第一式为
$$
 \operatorname{Res}_b(\mathcal P,\mathcal C_0)=
 -\frac{27}{64}x^{10}(2x-1)^9(8x+15).                        \tag{4.1}
$$
第二式 $\operatorname{Res}_b(\mathcal P,\mathcal C_1)$ 是关于 $x$
的三十九次多项式。两者在 $\mathbb Q[x]$ 的 monic gcd 精确为
$$
                         x^{10}(x-1/2)^9.                   \tag{4.2}
$$
配套源从 (1.3) 生成 (3.3)–(3.5)，只做三次与三次、
三次与六次这两个小结式，再做一元 QQ gcd。
没有一般多元 Gröbner，也没有有限域正证提升。

由 (3.6)，两个结式都必须为零。即使某个关于 $b$ 的首项在特殊
$x$ 处降阶，原公共根仍保证两个结式为零；这里仅使用必要性。
故 (4.2) 迫 $x=0$ 或 $x=1/2$。

$x=1/2$ 已由原一次 mean 排除。
若 $x=0$，回到原 (3.3)：
$$
                    \mathcal P(b,0)=b^2(b-1/2).
$$
因 $b\ne0$，必有 $b=1/2$，再次矛盾。
这关闭了整个 $\gamma=0$ 边界。

## 5. 精确推进范围

在活跃单位 $3+1$ 加孤立零点的非半权原临界支路，
在 $p,q,\alpha\ne0$ 的图内，本附录进一步证明
$$
        \gamma\ne0,\qquad s=B/q+b\ne x,\qquad p_0\ne0.
$$
这些非零条件允许后续把原 $q^2$ 与 $\kappa$ 在合法图上消去。
它们没有把余下的一般支当成空集，
也没有关闭其他单位补空间分拆、rank $H=5$，或普通 Hilbert ISP 主问题。


## 6. 原源执行与复核身份

[完整验证源](../notes/2026-11-20-essential-four-unit-three-plus-one-gamma-zero-verify.py)在[run44737090302](https://github.com/Rogerhu12/math-research-public/actions/runs/44737090302)、job136291084777的独立标签 `unit31_gamma_zero` 成功，exit0；源内计时1.484秒，外层计时1.924369274秒。触发提交 `407bc3459de35815ac85b18640397eb60843e272`，Python3.12.14、SymPy1.13.3、mpmath1.3.0。

源SHA-256 `dcbec1c0afeec4ede34dc899540855e0d39c8b229ba88b4aaaa928f9c32afc9b`；完整独立stdout SHA-256 `4f551d1a966400f778c38fbdbee641c7ea11a74bcde4c723da5c03f74bb76b5c`。它从原代数重新构造mean与前三jets，核全部s=x/p0=0返回、gamma零的两个小QQ结式和准确gcd。此独立标签的成功不依赖同一job内两个其他源的JSON序列化失败；失败程序未完成的结式不用于本证明。[批次身份](../notes/2026-11-20-exact-source-run44737090302-b2a9.json)只存参数/时间/SHA，不存展开表。
