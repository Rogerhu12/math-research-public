# R133：实际两输入帽图的完整 long tame、物理 DN 型和独立 Poisson 列

2026-11-15，visible-exact-astra-0df9。

**已证明的解析接口；root全文及两位独立窄核。** 本篇把已存在的真实两输入帽
$\Phi_\gamma(f_B)$ 接到同一新 fixed-stop 长段。它直接消费
$\|\Phi_\gamma(f_B)\|_{\dot A^2}<10^{-8}$，
不要求当前实际帽的 $Z=C_{R,\ne0}-C_{r,\ne0}$ 落入旧K的小输入球。
全部模、真实 holonomy mean、未匹配端口、真正adjoint、物理高度单位
及独立源保留。高范数只作one-high费用，未知输入没有复角取值。

本篇的实际小门属于完整物理B端。经过全部有限connector及深层Poisson
后的weighted网络差，必须再用单独的两actual外图Schur合同支付；
局部小门不替代那一步。本文也不把设计时随状态变化的第一参数图
冒作整个族的固定metric结论。

## 1. 对象、完整图和新低域

使用已发布：

- [M两输入实际帽](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)，
  SHA256 8d9e0bf3c0a212b5525bb017b772728967dcea13d9b61c24bc189b2e6be46f1b；
- [S真实加权long核](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)；
- [N物理DN与完整源](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md)；
- [K原两层long](R133-supplement-two-level-finite-Sobolev-true-long-DN-and-Poisson-tame.md)；
- [P新fixed-stop94链](R119-supplement-new-fixed-stop-small-width-cap-and-full-94-step-chain.md)。

下文使用S的准确有限长核及代数式，不移用其旧数值中心或旧角宽。
新对象的同一个真实长段满足
$$
 L=\omega(2^{24}-25/8)>23000000,\quad 7/5<\omega<3/2,\quad
 \epsilon=e^{-7L/4}<2^{-57000000}.
 \tag{O.1}
$$
最后一个严格上界已在P付清。原所有反射项保留，不取无限长极限。

置
$$
 r_\gamma=10^{-9},\quad r_B=2^{-60},\quad r_f=10^{-8},\quad
 \sigma_0=2^{-13},\quad h=2^{-15},\quad s_B=a_Bw_B .
 \tag{O.2}
$$
$\gamma$ 是帽内端的非mean物理C曲率输入；
$f=f_B$ 是B端归一非mean高度，physical高度为 $s_Bf$。
$\mathbf V_T=(P_T,U_T,K_T,V_T)$ 是短侧真实四态，$K_T$ 含其
holonomy mean，不把它误记为非mean量。

M在整个零宽product域
$\|\gamma\|_{A_0}<r_\gamma,\ \|f\|_{\dot A^2_0}<r_B$
给同一个唯一帽/long图，且
$$
 f_*=\Phi_\gamma(f),\qquad \|f_*\|_{\dot A^2_0}<r_f.
 \tag{O.3}
$$
为mixed Taylor及短侧系数使用
$$
 \Xi=(G,U,\mathbf W)
   =(\gamma/r_\gamma,\ |D_\theta|^2f/r_B,\ 64\mathbf V_T),
 \qquad \|\Xi\|_{A_0,\mathrm{sum}}\le1/16.
 \tag{O.4}
$$
所有输入/输出频率为完整 $4\mathbb Z$；$G,U$ 只有按定义的非mean，
短侧四态及输出mean完整。常高度 $\lambda$ 不包含在 $U$ 中。

## 2. 直接重实例化真正长段导数

S.8--S.17的有限长kernel、平方为零module和所有mean majorant
在宽零使用完全相同的绝对卷积界。
原条件只需 $M=|m|\ge4$、$1-e^{-2ML}>255/256$、
总Dirichlet预算≤$2^{-25}$。它们在新(O.1)和(O.3)上成立。

记真正完整远端斜率
$$
 \mathcal K(f,g)=2f+h_t(0;f,g)+\kappa(0;f,g)
       \in\dot A^1_0\oplus\mathbb C,\quad
 \mathsf C_L=|D_\theta|\coth(L|D_\theta|)P_\perp .
$$
准确有
$$
 \|\mathcal K(f,0)+\mathsf C_Lf\|<2^{23}\|f\|_{\dot A^2_0}^2,
 \quad
 \|D_f\mathcal K(f,0)+\mathsf C_L\|<2^{25}\|f\|_{\dot A^2_0}.
 \tag{O.5}
$$
$F=0$ 情形用二次零点，绝不作零半径Cauchy。
令 $\Delta\mathcal K(f,g)=\mathcal K(f,g)-\mathcal K(f,0)$。
同一加权module给
$$
 \|\Delta\mathcal K(f,g)\|<25\epsilon\|g\|_{\dot A^2_0},
 \quad \|D_g\mathcal K(f,g)\|<25\epsilon .
 \tag{O.6}
$$
这两式均保独立mean斜率。

只对long方程，$f$ 周围半径 $\delta_B=2^{-27}$ 的圆盘保持
$\delta_B+r_B+r_f<2^{-25}$，故
$$
 \|D_f\Delta\mathcal K(f,g)\|
       <25\epsilon r_f/\delta_B<2^6\epsilon .
 \tag{O.7}
$$
帽图没有被扩张到这个大圆盘。

在M的原product域内，若
$\|\gamma/r_\gamma\|+\||D|^2f/r_B\|\le3/4$，
Cauchy在原 $f$ 变量剩余的半径 $r_B/4$ 给
$$
 \|D_f\Phi_\gamma(f)\|\le4r_f/r_B<2^{36}.
 \tag{O.8}
$$
相同理由给 $D_\gamma\Phi$ 的 $A^0\to\dot A^2$ 界小于
$4r_f/r_\gamma=40<2^6$。
完整链式法则于是为
$$
 \mathscr K_\gamma(f)=\mathcal K(f,\Phi_\gamma(f)),\quad
 T_{\gamma,f}=D_f\mathscr K_\gamma(f)+\mathsf C_L,
$$
$$
 \boxed{\ 
 \|T_{\gamma,f}:\dot A^2_0\to\dot A^1_0\oplus\mathbb C\|
 <2^{25}\|f\|_{\dot A^2_0}+2^{43}\epsilon .\ }
 \tag{O.9}
$$
这里保了 $D_g\mathcal K\,D_f\Phi$；未固定 $f_*$ 来省该列。
(O.9)不使用旧K的 $Z/(3.3\,10^{-10})$ 小球。

long左端的完整四态和raw系数仍由N.19--20直接给
$$
 \|\mathbf V_L\|_{A_0}<2^8\|f\|_{\dot A^2_0}
                                  +2^6\epsilon r_f,
$$
$$
 \|\mu_L/\mu_0-1\|_{A_0}+\|d_L\|_{A_0}
      <2^{16}(\|f\|_{\dot A^2_0}+\epsilon r_f),
 \quad \mu_0=1/(4\omega).
 \tag{O.10}
$$
$\mu_L=\mu_0JD^{-3/2}$，
$d_L=(1+w_B^2)(V_L-P_L)/J$，均为当前实际解的系数。
短侧用同一个真实公式定义 $\mu_T,d_T$。

## 3. Known-only参数与完整mixed Fourier核

M构造了 $|\operatorname{Im}z|<2h$ 的完整已知系数族：
只把known centre、精确残差和已知非径向系数平移；
$G,U,\mathbf W$ 留在零宽空间，不求它们的复角值。
帽图的(O.3)、long的(O.5)--(O.10)在该族内一致成立。
短侧radial系数不动。对实 $t$，
$$
 \mathcal F_t(C_t\Xi)=C_t\mathcal F_0(\Xi)C_{-t}
 \tag{O.11}
$$
用于实际边界算子族，nonlinear/scalar输出使用相应协变式。
mean输出的 $C_t$ 为恒等。

采用归一算子族，例如
$a(D)T|D|^{-2}$、$a(D)\mathcal B_{\rm bare}$，
$a_m=\max(1,|m|)$，并按原单位读取短侧乘子和rank-one mean行。
它们在 $\|\Xi\|<1$ 全纯，在3/4球内有上面给出的完整界。
各次Taylor系数含 $1/k!$；复极化付 $4^k$。
对一个方向模 $n$ 和背景模 $\ell_1,\ldots,\ell_k$，
(O.11)加known参数的 $\pm ih$ 给真正的完整输出列和
$$
 \sum_{m\in4\mathbb Z}
  e^{h|m-n-\sum\ell_i|}
  |F_k(m;n,\ell_1,\ldots,\ell_k)|
 \le2M4^k .
 \tag{O.12}
$$
径向输出先取其逐模sup。所有species以原sum norm求和，
没有隐藏维数乘方，也没有把任意Wiener算子界直接认作Hilbert界。

有 $f$ 或短侧因子的项，分别保一份真实 $f$ 或 $\mathbf V_T$；
其余参数仍使用归一 $\Xi$。没有这两种因子的(O.9)--(O.10)项
统一带 $\epsilon$。
这从完整子族 $f=0,\mathbf V_T=0$ 的一致界及逐Taylor
telescoping得到；至多增加两个 $k$ 因子，不把gamma高norm变成小量。
在这个拆分中，$f$ 的Taylor归一可能带出
$r_B^{-1}\epsilon=2^{60}\epsilon$。这项仍是原screening小量，
由(O.1)及每次8192 bits的固定余量吸收；不能把纯$\gamma$子族的
$\epsilon$项改写成一份不存在的$f$。对含$f$的部分，
先用(O.9)的$2^{25}\|f\|$零点界及同product Cauchy，
再恢复真实物理$f$；短侧因子同样先作其零点telescoping。
known centre的非radial Fourier lag也完整包含在(O.12)中。

## 4. Two-level范数与明确常数

对 $64\le q\le8144$ 定义
$$
 g_q=r_\gamma^{-1}\|\gamma\|_{H^{q+32}},\quad
 f_q=\|f\|_{H^{q+34}},\quad
 n_q=\|\mathbf V_T\|_{H^{q+32},\mathrm{sum}},
$$
$$
 \mathcal A_q=n_q+f_q+
       (n_{64}+f_{64}+\epsilon)(1+g_q),\qquad
 \mathcal D_q=1+g_q+r_B^{-1}f_q+64n_q .
 \tag{O.13}
$$
$\mathcal A$ 是真实small budget；$\mathcal D$ 只需有限。
$q=8144$只读state/curvature8176、physical高度8178，
没有越过原8192窗口。

一个完整signed-lag majorant是 $K_h(\ell)=e^{-h|\ell|}$。
对所需整数 $p\le8176$，
$$
 \|\langle\ell\rangle^pK_h\|_{\ell^1(4\mathbb Z)}
 \le2^{p+3}p!h^{-p-1},\qquad
 \sum_{k\ge0}(k+1)^p4^{-k}\le p!2^{p+1}.
 \tag{O.14}
$$
$p!<2^{12p}$，因为 $p\le8176$ 时
$p!\le((p+1)/2)^p<4096^p$。
为每一次完整one-high kernel/adjoint估计宽取
$$
 L_{\rm ker}(q)=48(q+32)+8192
$$
bits：两个factorial、$h^{-p-1}$、完整lag符号和、至多两个
telescoping因子以及两侧Bessel权均在其中。
$\gamma$、height和短侧的固定归一至多 $2^{60}$，
在每次8192的固定余量内。

真实one-high Young把高角权分给唯一方向或唯一背景因子；
其余因子用完整$\ell^1$，低方向由 $H^{64+1/2}$ 控制。
slope的还原权 $|n|^2/a_m$、Poisson的 $1/a_m$、
其真正adjoint的相反权，以及mean $m=0$ 均计入。
至多六次这样的族估计，连同K.14的全部乘法和rank-one读取，
可由
$$
 \boxed{\ C_q^{\rm act}=2^{384(q+32)+262144}\ }
 \tag{O.15}
$$
统一覆盖。原K的六次组合费用仍是
$6L_{\rm ker}(q)+4(q+8)+256$，严格小于(O.15)的指数。
这里增加的是known系数的真实lag费用，未借用未知背景的解析宽。

(O.12)--(O.15)同时给一阶导数、完整二次差及真正adjoint的
one-high版本。高范数只出现一次；不是一个$\mathcal D_q^2$
或两个最高背景norm的乘积。

## 5. 真物理DN、完整未匹配行和mean

给定物理Jacobi高度 $y$，准确输入是
$\delta f=P_\perp y/s_B$。
$aw$在真实slope读出中抵消一次，故
$$
 \mathcal N_B y=-\mu_L
       \{D_f\mathscr K_\gamma(f)P_\perp y-d_Ly_\theta\},
 \qquad \mathcal N_{B,0}=\mu_0\mathsf C_L .
 \tag{O.16}
$$
不能在(O.16)之前删除 $D_f\mathscr K$ 的mean。

原完整未匹配行保持
$$
 \mathcal E_B=P_{\mu_T}
 \{-M_a\mathsf C_L+M_aT_{\gamma,f}P_\perp+M_b\partial_\theta\},
$$
$$
 a=\mu_T-\mu_L,\quad b=\mu_Ld_L-\mu_Td_T,\quad
 P_{\mu_T}v=v-\frac{\mu_T}{\langle\mu_T\rangle}\langle v\rangle .
 \tag{O.17}
$$
$P_{\mu_T}$ 的输出高频rank-one部分完整收费。
因而对 $\mathcal O=\mathcal N_B-\mathcal N_{B,0}$ 或
$\mathcal E_B$ 及它们的真正Hilbert adjoint，
$$
 \|\mathcal O y\|_{H^{q-1/2}}
 \le C_q^{\rm act}\{
  \mathcal A_{64}\|y\|_{H^{q+1/2}}
  +\mathcal A_q\|y\|_{H^{64+1/2}}\},
 \quad64\le q\le8144 .
 \tag{O.18}
$$
对 $0\le q\le64$，逐阶Peetre/完整Schur给
$$
 \|\mathcal O:H^{q+1/2}\to H^{q-1/2}\|
                    \le C_{64}^{\rm act}\mathcal A_{64}.
 \tag{O.19}
$$
negative阶由真实adjoint对偶，不能用一个高阶norm倒推所有低阶界。

完整mean零式也有直接验证。对long的holonomy函数
$\mathcal H_q=(1+q(1+K)U/B)/\sqrt D$，
$\mathcal H_{q,K}=qJD^{-3/2}$，并且
$$
 \mathcal H_{q,P}-\partial_\theta\mathcal H_{q,U}
   =-q(1+q)(V-P)D^{-3/2}.
$$
固定metric的真实高度方向满足
$\delta P=y_\theta/(aw),\delta K=y_t/(aw),
\delta U=y_{\theta\theta}/(aw)$。
微分 $\langle\mathcal H_q\rangle=1$ 并在实际圆上分部积分，得
$$
 \left\langle JD^{-3/2}(y_t-d_Ly_\theta)\right\rangle=0 .
 \tag{O.20}
$$
所以(O.16)的total conormal mean准确为0；
(O.17)亦因其完整projection有mean0。
常高度输入被两算子准确杀掉。
这些是homogeneous图的实际恒等式，不是先删input/output mean。
独立affine flux荷、物理曲率Bmean/Cmean仍须另行保留。

## 6. 实际低球给出的完整局部小门

在同一个N/E graph低域中，令
$$
 \mathscr R_{1856}\le2^{-8192000},\quad
 n_{1824}+f_{1824}\le2^{1024}\mathscr R_{1856},
$$
$$
 \|\gamma/r_\gamma\|_{A_0}\le1/32,\qquad
 g_{1824}\le2^{1048576}.
 \tag{O.21}
$$
后两个是明确的帽内输入域，不从高norm仅有限推出。
它包含 $\gamma=0$ 的实际种子；原小正宽
$\|\gamma\|_{A_{\sigma_0}}\le r_\gamma/128$ 的数据也满足该高阶充分界。
例如完整Fourier矩给
$\|\gamma/r_\gamma\|_{H^{1856}}\le2^{32\cdot1856}$
这一更强的宽界；仅使用有限阶，不需未知的复角值。

中间trace门是实际graph的安全宽界。
B在所有Γ bump之外，$\psi=0$；
E.2--3的finite部分准确含 $2^{440}$ 乘四态norm。
因此非mean $U_T=\partial_\theta^2f$、$P_T=\partial_\theta f$ 的
端点读取有其真实 $aw_B$ 单位，$f$ 的两额外角导由 $U_T$ 给出。
$K_T$的mean由同一小root补回，使用E/M的低二次界。
完整Bessel比、mean和固定trace换算远小于(O.21)的 $2^{1024}$。
没有把 $1/s_B$ 偷当有界常数；它已由E定义的实际state单位准确抵消。

由(O.1)、(O.13)、(O.21)，保留宽整数余量有
$$
 \mathcal A_{1824}<2^{-7000000},\qquad
 C_{1824}^{\rm act}=2^{974848}.
 \tag{O.22}
$$
所以第一局部N2门 $\mathcal A_{1824}<2^{-2097152}$ 已付。
更准确以(O.21)的未放宽指数相乘，(O.18)--(O.19)和真adjoint给
$$
 \boxed{\ 
 \max_{|s|\le1796}
 \|\Lambda^s[
   (\mathcal N_B-\mathcal E_B)-\mu_0\mathsf C_L]
          \Lambda^{-s}:H^{1/2}\to H^{-1/2}\|
 <2^{-6000000}.\ }
 \tag{O.23}
$$
这包括完整rank-one/mean行；对$s<0$用实际adjoint。
例如$n_{1824}+f_{1824}\le2^{-8190976}$，
$1+g_{1824}<2^{1048577}$，先得
$\mathcal A_{1824}<2^{-7142397}$。
加$974848$及两算子的有限和仍严格小于$-6167547$，
因而留出了比(O.23)更大的真实余量；
未用浮点下溢的0代表screening。

$\mathcal N_{B,0}\ge|D|/6$。
由(O.19)和两种半阶的完整范数换算，actual相对form及adjoint form
在非mean高度上保原严格正gap；常高度核按(O.20)保留。
若再接短connector，仍须按其真实source/relative-form合同收费。
这里没有从局部门直接推最终weighted网络差。

(O.23)比较的是当前actual图与明确的radial B行。
若全网络采用另一个已经给定的actual外图$T_0$，
必须先用它自己的已付低界控制$T_0-\mu_0\mathsf C_L$，
再合成$T_1-T_0$；不能假定旧$T_0$就是radial行。

本次可以准确选用原uniform I/Y定理中的
$Z^0=f_B^0=0$ 真fixed-$C_R$参考，短侧仍为当前实际四态。
该点在旧K的合法球内；径向解和唯一性给$\Phi_R(0,0)=0$。
它的$D_f\Phi_R(0,0)$及finite-length reflection仍保留，
所以$T_0$仍不等于$\mu_0\mathsf C_L$，$\mathcal E_{B,0}$也不为零。
对它用旧K的完整六组tame式，在相同窗口可安全取
$C_{1824}^{\rm ref}<2^{194560}$；
其真实预算是
$\mathcal A^{\rm ref}_{1824}=n_{1824}+n_{64}+\epsilon
 \le2n_{1824}+\epsilon$，下面的固定$2^3$余量包含这个因子2。
结合(O.21)有
$$
 \max_{|s|\le1796}
 \|\Lambda^s(T_0-\mu_0\mathsf C_L)\Lambda^{-s}\|_{H^{1/2}\to H^{-1/2}}
 <2^{194563}(n_{1824}+\epsilon)<2^{-7996412}.
 \tag{O.23a}
$$
所有短侧rank-one/mean行包含在旧K这次合法实例化中。
与上段actual的未放宽$2^{-6167547}$界相加，
得到相同短侧背景的两个真实外图
$$
 d_{1792}=
 \max_{|s|\le1796}\|\Lambda^s(T_1-T_0)\Lambda^{-s}\|_{H^{1/2}\to H^{-1/2}}
 <2^{-6000000}.
 \tag{O.23b}
$$
这是可交给独立[D完整传输](R119-supplement-actual-outer-row-to-complete-mixed-weighted-Schur.md)
的实际输入；尚未把其finite connector和deep费用省去。

## 7. 独立曲率Poisson及未screen的输出

固定metric下的完整有序变化为
$$
 \delta f_*=D_f\Phi_\gamma(f)\,P_\perp y/s_B
             +D_\gamma\Phi_\gamma(f)\,\dot\gamma
             +f_*^{\rm src}.
 \tag{O.24}
$$
独立curvature列是
$$
 \mathcal B_\gamma
  =-\mu_Ls_BD_g\mathcal K(f,\Phi_\gamma(f))
                          D_\gamma\Phi_\gamma(f).
 \tag{O.25}
$$
(O.6)、(O.8)给bare零宽界 $2^{11}s_B\epsilon$。
用同一个完整kernel及真正adjoint恢复各侧阶数，
$$
 \|\mathcal B_\gamma v\|_{H^{q+1/2}}
 \le C_q^{\rm act}s_B\epsilon
   \{\|v\|_{H^{q-1/2}}+
            \mathcal D_q\|v\|_{H^{64-1/2}}\},
 \quad64\le q\le8144 .
 \tag{O.26}
$$
低窗逐阶完整Schur界为
$C_{64}^{\rm act}s_B\epsilon\mathcal D_{64}$。
所有输入/输出mean和真实adjoint同样保留；
$\gamma$本身按定义非mean，不新增一个虚构input mean。

独立$f_*^{\rm src}$仍是原normalized height source。
其bare列为 $-\mu_Ls_BD_g\mathcal K$，必须按其真实高度导数
单位收费，不把它冒作curvature。
其物理height $y_R^{\rm src}=s_Rf_*^{\rm src}$
需准确除 $s_R$；$s_B/s_R$不得设1。
上述列若改写到短侧total flux，还要保(O.17)的projection和
原K.20完整affine mean/weak source转换。

完整帽的inner $B(L),C_0(L),B_0(L)$、外侧两曲率mean、
physical phase primitive、m/ubar/Gauss A及其adjoint
使用M的已付one-high/weak列，不乘$\epsilon$。
long mean-height span准确为
$$
 \delta[v_0(L)-v_0(0)]
       =\int_0^Law(t)\,D\kappa(h)\dot h\,dt .
 \tag{O.27}
$$
纯incoming部分使用S.21的 $aw(L)/165$，
完整方向使用M的真输出及本篇$\mathcal D_q$，仍不乘$\epsilon$。
一个全局$\lambda$独立；不同端的高度span不再各添常数。

原K.20的完整有序源行、各scalar分母、physical $B_R,C_R$
及独立Robin源没有因更换为actual帽图而消失。
本篇只更新(O.24)中实际输入图与其真实导数。
若改变metric、长度、Γ、ν、$\chi_R,s_B$或$s_R$，
其准确参数导数及全部Hp端值必须另外保留。
帽内νbump没有支集不等于全族ν列为零。

## 8. 可交付给全网络的实际内容

同一个actual两输入帽/long图已有完整zero-width导数、
有限Sobolev one-high及真正弱/adjoint/mean接口。
在明确(O.21)邻域上，(O.23)给完整物理B端局部小门；
最高state/height调用仍在8192内。
这可供独立的正片Poisson-resolvent和两actual外图weighted Schur消费。

本文没有授予另一个未核旧外图的身份、任意大gamma低norm、
一般charged非线性Γ值图、最终Γ1冻结后的fixed-metric族、
完整设计$\nu$ Schur或最终C²嵌入/held/reach。
原[C.6--7](R133-supplement-complete-C0-state-and-nu-geometry-response.md)
明确$E_\nu=E\exp(\nu w)$，故$\nu$也是intrinsic设计参数；
最终同metric族须同时冻结$\nu_*,\Gamma_{1,*},\Gamma_{2,*}$及其它
metric数据，再按原真正extrinsic参数构造，不能让$\nu$变动冒同metric挠曲。
它把原不适用的小Z域换为实际已存在的帽图并支付相应全部费用，
其余全局门继续按同对象逐项处理。
