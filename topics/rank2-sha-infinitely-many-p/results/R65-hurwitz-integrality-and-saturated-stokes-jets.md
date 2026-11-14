# R65. 惰性 Hurwitz 整性与实际滤子的饱和方向

日期：2026-11-12。**状态：完整证明；一般低次数高接触 jet 范数仍未控制。**

## 1. 固定 Euler 原函数在每个惰性处 Hurwitz 整

使用 R57 的实际整数 $h_m=m![z^m]A_1$，并令
$$
\mathscr H(z)=\int_0^zA_1(w)\,dw/w
             =\sum_{m\ge1}\frac{h_m}{m}\frac{z^m}{m!}.
$$
对任意惰性 $p\ge7$，R62 的全部余类给
$$
[z^m]A_1=\frac{a^k}{k!}\mathcal J_{p,j}(k),\qquad
m=(p+1)k+j>0,\quad j\in\{0,4,\ldots,p-3\},
$$
其中 $v_p(a)=-1$、$\mathcal J_{p,j}(k)\in\mathbb Z_p$。
因为 $m-1\ge pk$，有
$v_p((m-1)!)\ge k+v_p(k!)$。因此
$$
\boxed{h_m/m\in\mathbb Z_p\quad\text{对全部 }m,
                \ p\ge7,\ p\equiv3\pmod4.}
\tag{1}
$$
原 $E_{17}$ 的整数只差 $17$ 的幂，结论相同。
这是全部 Hurwitz 系数的定理，不要求目标中央导数为零；
普通侧 R58 的 $h_{4p}/(4p)$ 则准确有分母 $p$。

## 2. 全局流格与 Hurwitz jet 饱和确实不同

取实际单流
$$
u'=v,\quad v'=-2u^3,\quad L'=u^2,\quad\theta'=L\theta,
\quad v^2+u^4=1,
$$
以及自然全局坐标环
$\mathcal R_{(p)}=\mathbb Z_{(p)}[z,u,v,L,\theta]/(v^2+u^4-1)$。
周期平移和 theta 的二次指数增长证明
$z,L,\theta$ 在 $\mathbb C(u,v)$ 上代数独立，故这个环确实注入实际函数域。

设 $r=(p+1)/4$、$\epsilon(n)=\mathbf1_{r\mid n}$，并取 Newton 滤子
$$
Q_p(Y)=\sum_{k=0}^p\Delta^k\epsilon(0)\binom Yk,
\qquad \Pi_p=Q_p(zD/4),\qquad
P_p^{\rm flow}=\Pi_p\mathscr H-\mathscr H.
$$
在次数不超过 $4p$ 的四倍数 jet 中，$\Pi_p$ 是中央 $(p+1)$ 倍数的
准确 $0/1$ 投影。它的像和核都饱和，但全局多项式表达式有真实的分母：
$$
\boxed{pP_p^{\rm flow}\equiv-\frac14T_p\pmod p,
\qquad T_p=\sum_{k=0}^{p-1}\frac{(-z)^k}{k!}\mathscr V^kA_1\ne0.}
\tag{2}
$$
这里 $D=\partial_z+\mathscr V$，$\mathscr V$ 为上述整数流导子。
式 (2) 来自 $(zD)^p-zD=z^pD^p$ 及 Wilson 定理。
把独立坐标 $z$ 设为零后右边为 $-A_1/4$，所以它在全局环模 $p$ 确实非零。
特征零坐标环的注入排除把同一个函数改写成全局整多项式。

另一方面，$Q_p(n)$ 对所有非负整数 $n$ 都为整数，(1) 因而给
$\Pi_p\mathscr H-\mathscr H$ 的全部 Hurwitz jets 都整。
实际 Hurwitz Taylor 映射满足
$$
\boxed{\overline T_p\ne0\text{ 在 }\mathcal R_{(p)}/p,
\qquad \operatorname{ev}_{\rm H}(\overline T_p)=0.}
\tag{3}
$$
这是一个明确的非零模 $p$ Taylor 核，证明全局分母确被实际 jet 饱和吸收。
不能把全局坐标注入当作有限 jet 的饱和结论。

## 3. 精确滤子与有限近似的范围

R62 的非中央模型为
$E_j=d e^{-az^d}\int_0^z t^{j-1}e^{at^d}dt$，$0<j<d=p+1$。
每个 $E_j$ 的复增长阶恰 $d$，而固定整数流的有理函数域内各函数的阶至多二。
用 $D+ad z^{d-1}$ 作 Ore 右除，可证明：该实际函数域系数的任意有限阶
线性微分算子若准确杀掉一个 $E_j$，也必杀掉中央模型 $E_0=e^{-az^d}$。
有限个 $p$ 进常数系数可经有限生成域嵌入给同一结论。

这不妨碍有限 jet 的 Newton 投影。对于只用整 Euler 多项式的滤子，
其中央常数原始化的最小损失准确为
$$
\gamma_p(0;M)=v_p(\lfloor M/4\rfloor!)
                   -v_p(\lfloor M/(p+1)\rfloor!).
$$
首次为 $M=4p$；除幂 Newton 投影则在有限 jet 上已经原始。
二者差异由 (2)–(3) 在真正流中实现。

最后，普通 Taylor jet 与 Hurwitz jet 的任何相同 minor 有准确换算
$$
v_p\det B^{\rm ord}_{I,J}
 =v_p\det B^{\rm H}_{I,J}-\sum_{m\in I}v_p(m!).
$$
这笔行权不能省略。仍需计算低次数、高接触的实际前缀行格，
尤其 $D\asymp\sqrt{k}$ 时的统一界。

完整证明见[Stokes 滤子与有限 Euler 代价](../notes/2026-11-12-stokes-filters-in-integer-flow-field.md)
及[首个全局分母与 Hurwitz 饱和](../notes/2026-11-12-first-filter-denominator-and-hurwitz-saturation.md)。
