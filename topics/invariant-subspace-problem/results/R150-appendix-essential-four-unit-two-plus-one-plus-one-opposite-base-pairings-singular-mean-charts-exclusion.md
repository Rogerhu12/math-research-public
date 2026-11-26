# R150 附录：单位 2+1+1 相反基点配对的两个奇异 mean 图均为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 在原单位 $2+1+1$ 与孤立零点分支中，令 $p=1,q=-1$、$u=b-c\ne0$、$\ell=b+c$。本条排除下面两个线性 mean 的系数行列式为零的整个集合 $D_1D_2=0$。整个零基点 mean 支路、$\ell=0$ 和 $\ell=1/2$ 已分别由前稿排除。本条没有把尚余的 $D_1D_2\ne0$ 图宣称为空。

## 1. 同一原方程与全部参数

完整沿用[半总单点权专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-half-total-weight-exclusion.md)第一节的原长度五除子 $2A+B+C+Z$、六维非退化配对、活跃单位 Frobenius 代数、全部原最高式及第二梯度的值和一阶 jet。原 $K_B,P,N,E$ 均不改变。

这里
$$
a=1-\ell,\quad b=(\ell+u)/2,\quad c=(\ell-u)/2,
\quad e=u^2\ne0,\quad e\ne\ell^2.                              \tag{1.1}
$$
最后一个不等式正是 $bc\ne0$。设 $x=d_B,y=d_C$，并令
$$
X=(x+y)/2,\quad v=x-y-1,\quad T=uX,\quad w=ut.
$$
原基点 mean $E_0=0$ 等价于
$$
f=\frac X2+\frac u2+\frac{\ell v}{4u},
$$
而原参数全部恢复为
$$
r=x-a-ct,\quad s=y+a-bt,\quad
A_1=2f-2bx-2cy+2bct.                                          \tag{1.2}
$$
原两个单点 mean 的可逆组合为
$$
\begin{aligned}
E_+&=u^2(E_B+E_C)\\
 &=2T\ell v-2T\ell w+2e\ell w+2e\ell-ev^2-evw+ew-e+\ell w^2,
\end{aligned}
$$
$$
\begin{aligned}
E_-&=u(E_B-E_C)\\
 &=4T\ell-2Tv+2Tw-2T-4e\ell+2ev-2ew+2e\\
 &\hspace{8mm}+\ell v^2+\ell vw-\ell v-\ell w-w^2.
\end{aligned}                                                  \tag{1.3}
$$
它们对 $(T,e)$ 的系数行列式精确为
$$
-2D_1D_2,
\quad D_1=-2\ell+v-w+1,
\quad D_2=-2\ell(v+1)+v^2+vw-w+1.                              \tag{1.4}
$$
保留原 $M=u^2E_1$，以及前稿由原孤立零点 mean、原最高式和第二梯度证明的
$$
S=\overline P-2\overline N=0,\qquad
c_0=3P_0N_1-2N_0P_1=0.                                      \tag{1.5}
$$
以下计算使用 $S/u$，所除 $u$ 已由范围假设非零。所有表达式在 $u\mapsto-u$ 后为偶式，故可唯一写成 $e=u^2$ 的有理式，不选择平方根。

在本条余下证明中可引用完整的[$\ell=0$ 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-zero-total-weight-exclusion.md)和[$\ell=1/2$ 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-half-total-weight-exclusion.md)，因此
$$
\ell(2\ell-1)\ne0.                                           \tag{1.6}
$$
这两条已独立支付全部相应纤维，而不是本图的分母约定。

## 2. 第一奇异面 $D_1=0$

令 $w_1=v+1-2\ell$。在这面上 (1.3) 第二式精确成为与 $T,e$ 无关的条件
$$
K_1=-2\ell^2(v+1)+(2v^2+3v+3)\ell-(v+1)^2=0.                  \tag{2.1}
$$
第一式中 $T$ 的系数是 $2\ell(2\ell-1)\ne0$，所以
$$
T_1=\frac{2e(2\ell^2-2\ell v-\ell+v^2)-\ell w_1^2}
 {2\ell(2\ell-1)}.                                           \tag{2.2}
$$
把 $(w,T)=(w_1,T_1)$ 代回原 $M,S/u,c_0$，分别记为 $M_1,S_1,C_1$。其分母只含非零常数、$e,\ell,2\ell-1$。

为准确说明结式来源，约定 $\operatorname{num}$ 先约掉分子分母公因子，再取分子。先对这三个分子关于 $v$ 除以 $K_1$ 取余，再对余式取分子，得到
$$
M_R=\operatorname{num}(\operatorname{rem}_v(\operatorname{num}M_1,K_1)),
$$
$$
S_{\rm raw}=\operatorname{num}(\operatorname{rem}_v(\operatorname{num}S_1,K_1)),
\quad
C_R=\operatorname{num}(\operatorname{rem}_v(\operatorname{num}C_1,K_1)).
$$
$K_1$ 对 $v$ 的首项系数为 $2\ell-1\ne0$，所以取余引入的分母都已支付。原式精确给多项式整除
$$
S_{\rm raw}=(e-\ell^2)S_R.                                   \tag{2.3}
$$
这里仅除去已经在 (1.1) 中非零的 $e-\ell^2$；不取某个因子来代替原分子。由此每个原解都必须 $K_1=M_R=S_R=C_R=0$。三个新多项式关于 $(e,v,\ell)$ 的次数分别为
$$
(2,1,10),\quad(2,1,11),\quad(4,1,12).
$$

在 $\mathbb Q$ 上依次计算完整结式
$$
R_S(\ell)=\operatorname{Res}_v\bigl(\operatorname{Res}_e(M_R,S_R),K_1\bigr),
$$
$$
R_C(\ell)=\operatorname{Res}_v\bigl(\operatorname{Res}_e(M_R,C_R),K_1\bigr).
$$
它们的次数为 $75,115$，精确 gcd 除非零常数外为
$$
\ell^{14}(2\ell-1)^{36}(\ell-1)^6.                             \tag{2.4}
$$
故 (1.6) 下只剩 $\ell=1$。此时 $K_1=v(v-1)$，保留两个完整纤维，并在未经结式替换的原有理式中回代：
$$
M_1\big|_{\ell=1,v=0}=e/2\ne0,
\qquad
S_1\big|_{\ell=1,v=1}=-2(e-1)\ne0.                            \tag{2.5}
$$
第二个不等式来自原 Frobenius 条件 $e\ne\ell^2=1$。所以 $D_1=0$ 整面为空，包括与第二奇异面的交集。

## 3. 第二奇异面 $D_2=0,D_1\ne0$ 的所有新边界

先处理 $v=-1$。由 $D_2=0$ 得 $w=1$，而原 (1.3) 两式为
$$
E_+=\ell(-4T+4e+1),\qquad E_-=(4\ell+2)(T-e)-1.
$$
已知 $\ell\ne0$，第一式给 $T-e=1/4$，第二式再迫 $\ell=1/2$，已由独立完整结论排除。故 $v+1\ne0$，可以且必须解为
$$
\ell_2=\frac{v^2+vw-w+1}{2(v+1)}.                            \tag{3.1}
$$
这时
$$
D_1=\frac{2v(1-w)}{v+1}\ne0,\qquad
2\ell_2-1=\frac{(v-1)(v+w)}{v+1}\ne0.                         \tag{3.2}
$$
于是 $v\ne0,w\ne1,v\ne1,v+w\ne0$。

原第一式简化为
$$
E_+=\ell_2\bigl(2(v-w)(T-e)+w^2\bigr).
$$
若 $v=w$，则由 $\ell_2\ne0$ 得 $w=v=0$，与 (3.2) 矛盾。因此 $v-w\ne0$，并有
$$
T_2=e-\frac{w^2}{2(v-w)}.                                    \tag{3.3}
$$
代回原第二式的完整因子身份为
$$
E_-\big|_{(\ell,T)=(\ell_2,T_2)}
 =\frac{(v-1)(v+w)K_2}{2(v+1)(v-w)},
$$
$$
K_2=v^3-vw^2-vw+v-w^2-w.                                    \tag{3.4}
$$
由 (3.2) 得 $K_2=0$。这里没有舍去 $v=1$ 或 $v+w=0$ 的未处理因子：它们都已经精确对应完整排除的 $\ell=1/2$ 纤维。

## 4. 第二面完整结式及最后的二次纤维

把 $(\ell,T)=(\ell_2,T_2)$ 代回同一原 $M,S/u,c_0$，得到 $M_2,S_2,C_2$；分母只含非零常数、$e,v+1,v-w$。对各自化简分子关于 $w$ 除以 $K_2$ 取余，再取余式分子，得到 $\widetilde M,\widetilde S,\widetilde C$。$K_2$ 对 $w$ 的首项系数为 $-(v+1)\ne0$，所以这一步仍没有新未付除数。

三个多项式关于 $(e,w,v)$ 的次数分别为
$$
(1,1,10),\quad(2,1,13),\quad(4,1,14).
$$
不从中删去任何因子，计算两个完整有理数结式
$$
Q_S(v)=\operatorname{Res}_w\bigl(\operatorname{Res}_e(\widetilde M,\widetilde S),K_2\bigr),
$$
$$
Q_C(v)=\operatorname{Res}_w\bigl(\operatorname{Res}_e(\widetilde M,\widetilde C),K_2\bigr).
$$
它们的次数为 $54,89$，精确 gcd 除非零常数外为
$$
v^{23}(v-1)^4(v+1)^8(v^2+1)^8.                               \tag{4.1}
$$
每个原解使这两个结式为零，(3.2) 与 $v+1\ne0$ 排除前三种因子，所以只剩
$$
v^2+1=0.
$$
原 (3.4) 此时是 $-(v+1)w(w+1)=0$。因 $v+1\ne0$，必须 $w=0$ 或 $w=-1$。$w=0$ 代入 (3.1) 给 $\ell_2=0$，已完整排除。$w=-1$ 则在原 $M_2$ 中得到精确余式
$$
\operatorname{num}\bigl(M_2|_{w=-1}\bigr)\bmod(v^2+1)
 =-16e(v+1)\ne0.                                              \tag{4.2}
$$
因此两个 $v$ 共轭值和两个 $w$ 纤维均已支付，第二奇异面也为空。所有结式只用于有限共同根的必要条件；可能来自首项下降的额外根均由 (2.5) 与 (4.2) 的原式回代一并排除。

## 5. 自含 QQ 核验与范围

[第一奇异面源码](../notes/2026-11-26-unit211-opposite-first-singular-mean-chart-347c.py)和[第二奇异面源码](../notes/2026-11-26-unit211-opposite-second-singular-mean-chart-347c.py)分别从原 Frobenius 乘法、原 Gram、原 $E,P,N$ 与一阶 jets 重建全部表达式，核验行列式、完整边界、结式次数、精确 gcd 和最后纤维。依赖 Python 3.12.14、SymPy 1.14.0、python-flint 0.9.0；全部结式在特征零 $\mathbb Q$ 上计算，计算数组仅在内存中。

第一源实际 exit 0，程序计时 2.553077 秒，峰值 RSS 66876 KiB；源码 SHA256 为 `80a126c3661fd5f41ded25ab73e542de0d34bda0ae49ab4765e018ca7cabf2cd`。第二源实际 exit 0，程序计时 4.203470 秒，峰值 RSS 65216 KiB；源码 SHA256 为 `01b974c3281c3436286a5aab8b81c6418e8473d6b28d5929168348b95d4ffcc2`。两源均用 `PYTHONPATH=/tmp/isp-347c05929dd3/deps python 源文件.py` 执行，不重跑已登记的 $\ell=0,1/2$ 排除。

本条保留同一原最高式、mean、第二梯度及物理 jets 的必要条件，没有把抽象范数条件当作充分条件，也没有把此图的空性当成全局幂的来源。它完整支付相反配对下 Cramer 图的全部奇异除数，允许继续研究 $D_1D_2\ne0$ 的真正一般图。
