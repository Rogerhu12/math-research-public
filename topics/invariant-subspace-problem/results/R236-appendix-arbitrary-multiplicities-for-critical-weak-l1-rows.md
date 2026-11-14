# R236 附录：临界弱ℓ¹行的任意跨度与全部重数循环性

日期：2026-11-13（UTC）。独占作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明；根会话已独立全文核验真实导子壳、全阶词域、Bézout预算及弱平均配对。
本稿接 [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) 的真实导子壳、[R236规范全部重数](../results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md) 的保重数 Bézout 余式，以及[分阶累积量预解预算第8节](../results/R236-appendix-factorial-cumulant-powers-and-joint-resolvent-budgets.md)的弱 $\ell^1$ 物理任排扩展。
本稿是中间结论，普通 ISP 仍未完成。

## 1. 目标、范围与原算子的固定

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
\qquad a_*\in\mathbb C.
$$
设非零幅度的非增重排为 rho_n，假设
$$
\boxed{
0<\limsup_{n\to\infty}n\rho_n
\le B:=\sup_{n\ge1}n\rho_n<\infty.
}
\tag{1.1}
$$
相位与实际物理排列任意。
固定任意复 first 指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,\qquad
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j).
$$
令 X=X_b 为 R176 的真实倾斜 first，常数项仍为原 a_*。
记
$$
G_n=\sum_ja_j^nL_n(R_j),\quad
L_n(v)=\left.\frac{d^n}{dt^n}\log(\cosh t+v\sinh t)\right|_{t=0},
\quad n\ge2.
$$

给定非零标量多项式 q，除去非零首系数后设其首一、次数为 p≥2。
定义
$$
\mathcal P(z;\kappa)
=\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad T=\mathcal P(X;G).
\tag{1.2}
$$
指数在有限多项式空间上实际是有限和。
R176 给 T 在准确域 DomX^p 上闭且 C 自伴。
若 M=kerT，则
$$
M\subseteq\mathcal D_\infty:=\bigcap_{k\ge0}\operatorname{Dom}X^k,
\qquad X_M=X|_M\in B(M),
\tag{1.3}
$$
并且全部 Acal 元素及 X 保持 M。

**定理（已证明）。**
$$
\boxed{
\ker T=0,\qquad q(u)e^w\text{ 对实际 }A\text{ 循环}.
}
\tag{1.4}
$$
q 的根可有任意有限重数。
常数、一次情形由既有 R16/R147 处理。
本稿只用幅度排序选有限实际位，不将排序和写入原 X，不更换 a_*。

## 2. 物理任排下的分阶预解预算

这是根会话分阶预解稿的弱 ell¹ 扩展；给出所需变化以核实量词。
对固定 n，取包含复倾斜的实际正主控
$$
M_n=\sum_j|a_j|^nW_n(N_j),
$$
其中 W_n 的 Taylor 系数非负、W_n(0)=0，且 W_n 是分母为
(1-Lz)^n 的固定有理函数，L=max(1,sup|t_j|)。
原 L² 函数非负锥给
$$
|G_n^k f|\le M_n^k|f|.
$$
这不是 Hilbert 自伴正性。

在参数 t 下仍按物理位截到 h(t)，使
385·16^h≥2log(2+t)。
高尾真实局部指数界给纯标量乘积
$$
\prod_j(1+C_nt|a_j|^n).
$$
只在这个非负标量乘积中使用重排：
$$
\sum_j\log(1+C_nt|a_j|^n)
\le\sum_{k\ge1}\log(1+C_nB^nt/k^n)
\le I_n(C_nB^nt)^{1/n}.
\tag{2.1}
$$
物理尾 carry 用 |a_j|≤B 与
Σ_{j≥h}sqrt(eta_j)≤2exp(−385·16^h) 控制。
有限物理头仍能明确写作 A U_h，而且
$$
\|U_h\|\le C_nB^n\zeta(n)\exp(125\,16^{h-1}),
$$
因为 Σ|a_j|^n≤B^n zeta(n)。
原 A 的四次幂界把低头指数成本压到
exp(C(log(2+t))^(4/3))，可吸入 exp(C_n t^(1/n))。
由 Cauchy 系数界及实际 Neumann 级数，
$$
\|G_n^k\|\le K_n\frac{D_n^k}{(k!)^{n-1}},
$$
$$
\|(z-G_n)^{-1}\|
\le \frac{K_n}{|z|}
\exp\left((n-1)(D_n/|z|)^{1/(n-1)}\right).
\tag{2.2}
$$

因此固定 epsilon>0 后，对任意 0<s≤1，
若 F 在多圆盘
$$
|\kappa_n|\le\varepsilon s^n,\qquad 2\le n\le p
$$
的邻域全纯、边界 |F|≤M_F，则
$$
\boxed{\|F(G)\|\le K M_F e^{C_\varepsilon/s^2}.}
\tag{2.3}
$$
K,C_epsilon 与 s、F 及所选物理位集合无关。
本节没有把重排实现为原 Hilbert 空间上的一个交织算子。

## 3. 高位同幅桶：固定桶数与小平均参数

由 (1.1)，存在固定 c_0>0 与趋于无穷的整数子序列 N，
使 N rho_N≥c_0。
从幅度最大的 N 个实际指标中，先删去排序最前 floor(N/4) 项，
再删去物理位置 j<floor(N/4) 的项。
至少剩 N/2 项，且
$$
j\ge h_N:=\lfloor N/4\rfloor,\qquad
\frac{c_0}{N}\le|a_j|
\le\frac{4B}{N}.
\tag{3.1}
$$
这里上界使用的是 B/n，不再使用 R260 的较粗 ell² 上界。

令
$$
J=\left\lceil\log_2(4B/c_0)\right\rceil+1,\qquad
\kappa=\frac1{4J}.
$$
按二进幅度分桶，桶数至多 J。
至少一桶含 N/(2J) 项。
从此桶任取恰有
$$
Q_N=\lfloor\kappa N\rfloor
$$
个实际指标组成 I_N，并记桶左端为 tau_N。
于是
$$
\boxed{
\min I_N\ge h_N,\quad
\tau_N\le|a_j|<2\tau_N\ (j\in I_N),\quad
c_0/N\le\tau_N\le4B/N.
}
\tag{3.2}
$$
不限制 max I_N。

取稍后固定的小 c>0，令
$$
r=r_N=\left\lfloor\sqrt{Q_N/c}\right\rfloor.
\tag{3.3}
$$
沿子序列 r→∞；充分大 N 时 r≤Q_N。
并有
$$
\frac{Q_N}{r^2}\to c,\qquad
\frac N{r^2}\to\frac c\kappa,\qquad
r\tau_N\to0.
\tag{3.4}
$$
后续所有 F 都满足 F⊂I_N、|F|=r。

## 4. 不依赖最大物理位的基本真实导子误差

记 delta B=[X,B]。
R260 §§2–4 取 Y=0 后直接适用。
其局部壳是原完整域上的真实等式，并给
$$
\widehat X_F
=X+\sum_{j\in F}a_j[V(-t_jN_j)-R_j]
=X+A_{X,F},
$$
$$
\widehat G_{n,F}
=G_n+\sum_{j\in F}a_j^n
[L_n(V(-t_jN_j))-L_n(R_j)],
$$
$$
E_{X,F}=\gamma_F(X)-\widehat X_F,\qquad
E_{n,F}=\gamma_F(G_n)-\widehat G_{n,F},
\tag{4.1}
$$
其中 gamma_F=Ad mathsf J_F、mathsf J_F=∏_{j∈F}M_(chi_j)。

A_(X,F)、widehat G 都属于 Acal，完整交换 X。
基本误差 E_X、E_n 及其全部 delta 导数都有 R260 的真实域保持性质。
统一于全部 F，存在
$$
\boxed{
\|\delta^sE_{X,F}\|+
\sum_{n=2}^p\|\delta^sE_{n,F}\|
\le s!\,\epsilon_N,\qquad
\epsilon_N\le C e^{-385\,16^{h_N-1}}.
}
\tag{4.2}
$$
这不包含 max I_N。
固定 p 只将有限个壳常数合并。

全部基本误差保持 mathcal D_infty。
理由是：每阶 delta 导数有界且保持 DomX；
在真实一阶等式
X Bf=B Xf+delta Bf 上逐次归纳，
得到 B 保持每个 DomX^k，及通常 Leibniz 域公式。
Acal 因子同样保持这些域。
有限局部 mathsf J_F 本身也保持 mathcal D_infty；
这里只为定义域使用有限最大位的闭尾核心，不对其头范数作定量估计。

由 (3.2)--(3.4) 与统一真实分母界，
$$
\|A_{X,F}\|\le C r\tau_N\longrightarrow0,\qquad
\|\widehat G_{n,F}-G_n\|\le C_nr\tau_N^n\longrightarrow0.
\tag{4.3}
$$
所以后面使用的 Acal 系数范数统一有界。

## 5. 正规排序词引理：全部高阶误差只付阶乘

本节明确取代最大位之前的粗头范数。

**词引理。**
设一个算子词有 k 个 X 字母、ell 个有界字母，作用于 mathcal D_infty。
有界字母分两类：

- Acal 因子 C_i，||C_i||≤C≥1、delta C_i=0；
- 基本误差 E_i，所有阶数满足
  ||delta^sE_i||≤s! epsilon，0<epsilon≤1。

假设该词至少有一个基本误差。
若 v 的真实 jet 满足
$$
\|X^jv\|\le H R^j,\qquad 0\le j\le k,\qquad R\ge1,
$$
则
$$
\boxed{
\|\operatorname{word}(v)\|
\le H\,\epsilon\,C^\ell(\ell+1)^k k!R^k.
}
\tag{5.1}
$$

**证明。**
逐个用 X B=B X+delta B 把 X 移到右端。
给原来每个 X 加标签。
该 X 最终或者到达最右端，或者消耗为某个原有界字母的一次导数；
至多 ell+1 个去处。因此全部正规排序项的系数绝对值总和
至多 (ell+1)^k。
每个非零项仍含至少一个误差导数。
若各误差接受的总导数阶数为 s_1,...,s_t，则
Σs_i≤k，且
$$
\prod_i s_i!\le(\sum_i s_i)!\le k!.
$$
多个 epsilon 因子用 epsilon^t≤epsilon 控制。
余下 X 次数不超过 k，由给定 jet 界处理。
每个步骤都在 mathcal D_infty 上成立，因为全部字母及导数保这个域。
这证明 (5.1)。

特别，当 ell≤C_p r、k≤p r，有限多个此类词的数量至多 C_p^r 时，
总误差可写成
$$
H\epsilon\exp(Cr\log(r+2))R^{pr}.
\tag{5.2}
$$
常数可依赖固定 p、系数范数；不依赖物理跨度。

## 6. 反射输入的统一 X-jets

假设 M非零，令 B_M=||X_M||。
稍后使用的核内输入 f_F 都在 M。
由 (4.1)，在共同深域上
$$
X^k\mathsf J_F f_F
=\mathsf J_F\bigl(X+A_{X,F}+E_{X,F}\bigr)^k f_F.
\tag{6.1}
$$
不含误差的部分为
$(X+A_{X,F})^k f_F$；
A_(X,F) 是保 M 的 Acal 元素，
故充分大 N 时它的范数不超过
$(B_M+1)^k||f_F||$。

其余词至少含一个 E_X，展开后用 §5，
其范数总和不超过
$$
\epsilon_N\exp(Ck\log(k+2))\|f_F\|
\tag{6.2}
$$
（把固定 B_M 因子吸入 C）。
因为 r=O_c(sqrt N)，而 epsilon_N 具有 (4.2) 的真实超快衰减，
(6.2) 的系数对全部 0≤k≤2pr 同时趋零。
因此取固定 R_M≥B_M+2，
充分大 N 时
$$
\boxed{
\|X^k\mathsf J_F f_F\|
\le2R_M^k\|f_F\|,
\qquad 0\le k\le2pr.
}
\tag{6.3}
$$
R_M 不含 max I_N；所有 F 统一。
没有假定 mathsf J_F 在未知核中保持不变。

对任何固定物理头 h，令
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j .
$$
它与 X 只差固定有界 Acal 元素 H_h。
完整域二项式和 (6.3) 给
$$
\boxed{
\|Z_h^k\mathsf J_F f_F\|
\le2(R_M+\|H_h\|)^k\|f_F\|,
\qquad 0\le k\le2pr.
}
\tag{6.4}
$$
这正是最后局部 p 阶交换子需要的全部 jet 预算。

## 7. 保重数 Bézout 逆：一次共同求值

这一代数步骤不依赖物理排列。
保留已核规范全重数稿的完整定义，指出全部适用条件。

有精确有限差恒等式
$$
4L_n'(1)=-2(-2)^n,\qquad
\partial_{\kappa_n}\mathcal P=\frac1{n!}\partial_z^n\mathcal P,
$$
所以
$$
\boxed{
\mathscr L_a(z;\kappa)
=4a\partial_z\mathcal P+
 \sum_{n=2}^p4L_n'(1)a^n\partial_{\kappa_n}\mathcal P
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
}
\tag{7.1}
$$

设 q 的不同根 lambda_nu 的重数为 mu_nu。
存在固定 epsilon>0 和 tau_0>0，使
$|\kappa_n|\le2\varepsilon\tau^n$ 时，
mathcal P 的每个根团位于
$|z-\lambda_\nu|<\tau/4$，
且保原重数 mu_nu。
这是 Bell 权重为 n 的系数界与 Rouché 的直接结果。
当 tau≤|a_j|<2tau 时，平移 2a_j 后的根团与原团闭圆盘不相交；
不同团由 q 的固定根距控制。
因此对
$$
H_F(z;\kappa)=\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)]
$$
可在原根团圆盘内取 h_F=H_F⁻¹。

在圈 Gamma_nu={|z−lambda_nu|=tau/4} 上定义真正的 Hermite 余式
$$
\mathcal R_F(z;\kappa)=
\frac1{2\pi i}\sum_\nu\int_{\Gamma_\nu}
h_F(\zeta;\kappa)
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
 {(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta .
\tag{7.2}
$$
它对 z 的次数小于 p，系数在多圆盘邻域全纯，
并满足
$$
|[\!z^k\!]\mathcal R_F|
\le C_q^{r+1}\tau^{-pr-p+1}.
\tag{7.3}
$$
Cauchy 公式给 h_F−mathcal R_F 被 mathcal P 局部全纯整除；
因此保留全部根的重数，得到多项式恒等式
$$
\boxed{
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\,\mathcal S_F .
}
\tag{7.4}
$$
不是只在根值上插值。

本稿取 tau=tau_N。
对整个余式的每个系数一次使用 (2.3)，得到
$$
\|[\!z^k\!]\mathcal R_F(z;G)\|
\le KC_q^{r+1}\tau_N^{-pr-p+1}e^{C_\varepsilon/\tau_N^2}.
$$
在 M 上设
$$
\mathfrak R_F=\mathcal R_F(X_M;G|_M):M\to M .
$$
它是实际有界的次数小于 p 的 X 多项式限制，且
$$
\boxed{
\left(\prod_{j\in F}\mathscr L_{a_j}(X;G)\right)
\mathfrak R_Ff=f,\qquad f\in M.
}
\tag{7.5}
$$
由 tau_N≥c_0/N，有固定 K>0 及固定 K_M，
$$
\boxed{
\|\mathfrak R_F\|
\le\exp\!\left(KN^2+Kr\log(N+2)+K_M\right).
}
\tag{7.6}
$$
K 与 N、F、c、未知局部测试矩阵无关；
X_M 的范数只进入固定 K_M。
没有将各个位逆的预解成本重复 r 次。

## 8. p 阶真实反射幂，不使用最大位头范数

定义
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\qquad
A_F=\widehat T_F-T,\qquad
E_F=\gamma_F(T)-\widehat T_F .
\tag{8.1}
$$
A_F 是 Acal 系数的 X 多项式，与 T、widehat T_F 在 mathcal D_infty 上交换。
E_F 通常不是有界算子；后面不用其全 H 范数。

把 gamma_F(X)=X+A_(X,F)+E_(X,F)、
gamma_F(G_n)=widehat G_(n,F)+E_(n,F)
代入有限多项式 mathcal P。
逐因子相减说明 E_F 是有限多个词的和：
每词含至少一个 §4 的基本有界误差，
至多 p 个 X 字母，有界字母总数由固定 p 控制。
其它有界字母在 Acal 中，范数由 (4.3) 统一控制。
这是 §5 可以直接处理的原始词表达，不需要先把 unbounded E_F 纳入有界导子代数。

令 f_F=mathfrak R_F f、v_F=mathsf J_F f_F。
v_F∈mathcal D_infty，且
$$
(\widehat T_F+E_F)v_F=\gamma_F(T)v_F=0.
$$
对每个 k≥1，展开非交换的
$(\widehat T_F+E_F)^k v_F=0$，
把唯一的纯 widehat T_F^k 项移到另一边。
再用 T=widehat T_F−A_F 的交换二项式，得到
$$
T^rv_F-(-A_F)^rv_F
=-\sum_{k=1}^r\binom rk(-A_F)^{r-k}
 \sum_{\substack{\text{词 }W\in\{\widehat T_F,E_F\}^k\\
                 W\ne\widehat T_F^k}}Wv_F.
\tag{8.2}
$$
外层系数绝对和至多 3^r。

每个完全展开的词仍含至少一个基本误差，
X 字母不超过 pr，有界字母不超过 C_p r；
有限多项式展开只另乘 C_p^r 个项。
在 (6.3) 的真实输入 jet 上用 §5，因此
$$
\boxed{
\|T^rv_F-(-A_F)^rv_F\|
\le\epsilon_N\exp(Cr\log(r+2))\|f_F\|.
}
\tag{8.3}
$$
所有展开都在保持不变的 mathcal D_infty 上，故给真实自然幂；
不声称 DomT^r 与某个未经证明的最大形式域相等。
特别，(8.3) 完全不含 max I_N。

## 9. Boolean 一次项、实际重复位与移过反射

用真实 N_j²=eta_j N_(j+1) 把反射替身模二次项写成
$$
\widetilde A_F=
\mathcal P\left(
X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(X;G).
\tag{9.1}
$$
A_F−tilde A_F 的 Acal 系数范数由 C eta_(h_N) 控制；
这是实际有理式中明确提取 N_j² 后的界。
因为 r tau_N→0，固定 p 的全部其它系数范数统一有界。
因此在 (6.3) 上作 r 次幂替换，只增加
eta_(h_N)exp(Cr log(r+2))||f_F||。

在交换形式变量 x_j 中，tilde A_F 没有零次项，
其一次部分准确为
$$
\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G).
$$
r 个正次因子相乘、变量只有 r 个，所以
$$
\widetilde A_F^r\equiv
r!t_FN_F\prod_{j\in F}\mathscr L_{a_j}(X;G)
\pmod{(N_j^2:j\in F)},
\quad t_F=\prod_{j\in F}t_j,\quad N_F=\prod_{j\in F}N_j .
\tag{9.2}
$$
每个弃项真含重复位，实际范数因此多出 eta_(h_N)。
系数绝对和由把每个形式变量模取1得到：
Σ_F|a_j|≤2r tau_N→0、固定 Gn 范数及固定 R_M 足够，
不使用任何物理初段和。

令 L_F=∏ mathscr L_(a_j)(X;G)。
将 gamma_F(L_F) 与其交换替身相减，其每个词含基本误差，
总 X 次数≤pr，故再次由 §5、(6.3) 得
epsilon_N exp(Cr log(r+2)) 的界。
交换替身与 L_F 的每个差项则含一个选中 N_j；
左乘 N_F 后真有重复位。
因此
$$
N_FL_F\mathsf J_F f_F
=N_F\mathsf J_F L_F f_F+\text{已付误差}.
$$
使用的是
$L_F\mathsf J_F-\mathsf J_FL_F
=(L_F-\gamma_F(L_F))\mathsf J_F$，
没有假定 L_F 与反射交换。
(7.5) 使 L_Ff_F=f。

合并各项并扩大 C，得到完整实际主项
$$
\boxed{
\|T^r\mathsf J_F\mathfrak R_Ff
-(-1)^rr!t_FN_F\mathsf J_F f\|
\le\epsilon_N e^{Cr\log(r+2)}
\|\mathfrak R_F\|\|f\|.
}
\tag{9.3}
$$
eta_(h_N) 已吸入更松的 epsilon_N。
所有 F 统一，物理跨度没有进入任何常数。

## 10. 对称平均及非零弱极限

设 L=max(1,sup|t_j|,sup|t_j|⁻¹)，定义 M→H 的输入
$$
\mathcal V_N=
(-1)^r\left(\frac2{Q_N}\right)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}\mathsf J_F\mathfrak R_F .
\tag{10.1}
$$
它保持所需共同深域输入，并且
$$
\|\mathcal V_N\|
\le A_N:=
\frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|
\le e^{KN^2+Kr\log(N+2)+K_M}.
\tag{10.2}
$$
不同位 E_j 交换、平方为零，E_j mathsf J_j=E_j。
用 (9.3) 与 ||N_F mathsf J_F−∏E_j||≤r eta_(h_N) 求和，得
$$
\boxed{
\|T^r\mathcal V_Nf-C_{I_N}^rf\|\le o(1)\|f\|,
\qquad C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
}
\tag{10.3}
$$
可用的总误差预算是固定常数乘
$$
\epsilon_N
e^{KN^2+Kr\log(N+2)+Cr\log(r+2)+K_M}
+2^rr\eta_{h_N}\longrightarrow0 .
$$
(4.2) 的物理最小位超快衰减已支付整个输入逆成本。

所选位可任意有孔。
有限提升矩阵仍给
$$
\|C_{I_N}^r\|\le(1+1/Q_N)^r\longrightarrow1.
$$
对固定有限柱 v,z，充分大 N 时 minI_N 高于它们的支撑，
所以
$$
\langle C_{I_N}^rv,z\rangle
=\frac{(Q_N)_r}{Q_N^r}\langle v,z\rangle
\longrightarrow e^{-1/(2c)}\langle v,z\rangle.
$$
利用一致范数界扩展到全 H，
$$
\boxed{
C_{I_N}^r\rightharpoonup\alpha_c I,\qquad
\alpha_c=e^{-1/(2c)}>0 .
}
\tag{10.4}
$$
因此 T^r mathcal V_N f 弱趋 alpha_c f。
不需要未知核向量的尾速率，也没有误称强趋 I。

## 11. 任意固定局部矩阵的 p 阶交换子与完整配对

固定局部矩阵 D，支撑位小于 h。
沿用 §6 的纯闭尾
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j,
$$
并令 G_(n,≥h) 为真实物理尾累积量。
有限低头有实际有界除法
$$
X-(Z_h+s_h)=A U_{1,h},\qquad
G_n-G_{n,\ge h}=A U_{n,h},
$$
其中
$$
U_{1,h}=-2\sum_{j<h}\frac{a_jt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1},
$$
$$
U_{n,h}=-2\sum_{j<h}\frac{a_j^nt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1}\widetilde L_n(R_j),
\quad L_n(v)=(v-1)\widetilde L_n(v).
\tag{11.1}
$$

有限多项式相减遂给
$$
T=T_{\rm tail}+K_h,\qquad
T_{\rm tail}=\mathcal P(Z_h+s_h;G_{\ge h}),\qquad
K_h=A W_h(Z_h),
$$
$$
W_h(z)=\sum_{k=0}^{p-1}B_{h,k}z^k,\qquad B_{h,k}\in\mathcal A.
\tag{11.2}
$$
D 完整交换 Z_h 和全部尾系数。
在 mathcal D_infty 上，K_h 与 T_tail 交换，D 与 T_tail 交换，
于是
$$
\operatorname{ad}_T^rD
=\sum_{s=0}^r(-1)^s\binom rsK_h^{r-s}DK_h^s.
\tag{11.3}
$$
展开 W_h 后，每项真是
$$
A^{r-s}B_{\rm left}\,D\,A^sB_{\rm right}\,Z_h^k,
\qquad k\le(p-1)r.
$$
没有把 A 移过 D。R109 给
$$
\|A^{r-s}\|\,\|A^s\|
\le e^{-(5/6)r^4+105r^3}.
\tag{11.4}
$$

由 (6.4)、(10.1)，固定 h 后存在 R_(h,M)≥1，
不依赖 N 或任何 maxI_N，使
$$
\|Z_h^k\mathcal V_Nf\|
\le2A_NR_{h,M}^k\|f\|,
\qquad 0\le k\le(p-1)r.
$$
记 $B_h(R)=\sum_k\|B_{h,k}\|R^k$，则
$$
\boxed{
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|
\le2\|D\|A_N[2B_h(R_{h,M})]^r
e^{-(5/6)r^4+105r^3}\|f\|.
}
\tag{11.5}
$$
这是对真正深域输入的估计，不声称该高阶交换子全 H 有界。

现在固定
$$
0<c<\min\left(1,\kappa\sqrt{\frac5{48K}}\right).
\tag{11.6}
$$
由 N/r²→c/kappa，
(10.2)、(11.5) 的对数主项为
$$
-\frac56r^4+KN^2+O(r^3+r\log(N+2)),
$$
它趋于负无穷。
因此 (ad_T^rD)mathcal V_N f→0。

对 f,g∈M，在共同深域作真实 Leibniz 展开。
T 的完整 C 自伴及 Tg=0 使所有低阶项配对为零，
准确得到
$$
B(DT^r\mathcal V_Nf,g)
=(-1)^rB((\operatorname{ad}_T^rD)\mathcal V_Nf,g).
$$
右侧趋零，左侧由 (10.3)--(10.4) 趋于 alpha_c B(Df,g)。
alpha_c>0，故
$$
B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意固定有限局部矩阵}).
$$
原 Haar 局部全矩阵 *-代数不可约，
任意非零 f 的局部轨道稠密。
令 g=f 就迫 Cf=0，矛盾。
因此 M=0。

## 12. 循环性与剩余范围

R176 给 xi_w=e^w 的真实全部幂域、循环性，以及
$$
T\xi_w=q(u)e^w,\qquad
[q(u)e^w]_A=\overline{\operatorname{Ran}T}.
$$
T 在准确自然域 C 自伴，M=0 使其像稠密。
因此 (1.4) 成立，包含任意物理排列与复相位的规范幅度 1/(j+1)，
以及 (1.1) 所写完整临界弱 ell¹ 类。

本稿新增的跨度步骤是 §§5–6、8：
利用 R260 的实际导子壳把每个高阶词的导数总预算固定为 O(pr)，
从而彻底移除最大选中位之前的头范数。
不能用这句话代替上述正规排序、完整域及输入 jet 的实际证明。

没有覆盖 n rho_n→0 的同字符剩余分支，
也没有覆盖 sup n rho_n=∞ 的全部重根情形；
R260 对后者的简单根结论仍独立有效。
多模式点态多项式、一般有限 chaos、正常湮灭者、
两个边界 N=M 及完整普通 Hilbert ISP 仍未由本稿关闭。
