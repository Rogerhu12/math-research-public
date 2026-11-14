# R230 附录：任意最小正秩的逐对比例全谱与实际共同分母

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明的结构加强。**
对任意最小正秩 $r\ge2$ 的真实慢理想见证，
仅选两行具有广义预解的原最小源乘子，
它们从边界图到最大比例图之间的全部闭交换实现，
对任意有界交换单位倍数及有界交换扰动，都没有预解点。
不需要其余 $r-2$ 行有预解数据。

[R244 旧比例谱附录](R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)
已经证明真秩二的整个中间图结论，
也已证明“非空广义预解自动给真空最小图及 C 自伴性”。
本稿复用并完整重述这两项工具，新增的是任意最小秩的两行版本：
使用原整体正见证的有界模秩压缩，
不假设所选两项本身湮灭慢理想，也不使用高秩时未证的严格双图缺口。
证明还从任何假设的比例预解子直接构造一个有真空原像的实际共同分母。

## 1. 最小正秩与所选两行

记 $\mathfrak C=A'$，$B(u,v)=\langle u,Cv\rangle$，
内积对第一变量线性。
沿用实际有界交换子交换性与 $T^\top=CT^*C=T$。
固定真正最小秩正见证
$$
\rho=\sum_{\nu=1}^r f_\nu\otimes f_\nu,\qquad
r\ge2,\qquad
\tau=\sum_\nu\|f_\nu\|^2>0,
$$
$$
\phi(F)=\sum_\nu\langle Ff_\nu,f_\nu\rangle,\qquad
\phi(S\mathfrak C)=0.
\tag{1.1}
$$
这里最小正秩等于最小一般分离秩，见
[R228A §1](R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md)。

选任意不同的 $i,j$，只假设这两行
$$
x_\nu=Cf_\nu,\qquad M_\nu=X_{x_\nu}\qquad(\nu=i,j)
$$
有实际广义预解数据
$$
R_\nu=(M_\nu U_\nu+B_\nu)^{-1}\in\mathfrak C,\qquad
U_\nu\in\mathfrak C^\times,\quad B_\nu\in\mathfrak C.
\tag{1.2}
$$
原域均为最小闭乘子域。
[广义预解附录](R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)
给
$$
R_\nu\text{ 单射},\quad
R_\nu H=\operatorname{Dom}M_\nu,\quad
D_\nu=M_\nu R_\nu\in\mathfrak C,\quad
U_\nu D_\nu+B_\nu R_\nu=I.
\tag{1.3}
$$
并有准确逆源
$$
g_\nu=U_\nu x_\nu+B_\nu1,\qquad
R_\nu g_\nu=1,\qquad D_\nu g_\nu=x_\nu.
\tag{1.4}
$$

本文所需的两行秩压缩结论可直接核：
若存在 $v\in H$ 及 $T_i,T_j\in\mathfrak C$ 满足
$$
x_i=T_iv,\qquad x_j=T_jv,
\tag{1.5}
$$
则对全部 $F\in\mathfrak C$，
$$
\langle Ff_i,f_i\rangle+\langle Ff_j,f_j\rangle
=\left\langle F(T_if_i+T_jf_j),Cv\right\rangle.
\tag{1.6}
$$
只用有界 C 对称性
$B(Ff_\nu,T_\nu v)=B(FT_\nu f_\nu,v)$。
以 (1.6) 替换原 $\phi$ 的两项，
整泛函至多剩 $r-1$ 个一般配对项，
仍湮灭 $S\mathfrak C$ 且在 $I$ 取值 $\tau>0$。
这与最小秩等价矛盾，故 (1.5) 不可能。

因此所选两行也不能有
$$
P\in\mathfrak C,\qquad
PH\subset\operatorname{Dom}M_i\cap\operatorname{Dom}M_j,\qquad
Pv=1.
\tag{1.7}
$$
因为闭图定理及域交换给 $T_\nu=M_\nu P\in\mathfrak C$，
且 $T_\nu v=x_\nu$，从而落入 (1.5)。
(1.7) 是已保存的
[有界模与逐对共同真空证明](../notes/2026-11-13-minimal-positive-rank-module-compression-and-pairwise-common-vacuum-obstruction-normal-complex.md)
中的结论；上面已列出这里需要的完整短证。

## 2. 逆源循环与三个真实比例图

R88 的有界强多项式逼近意味着：
每个闭的 $A$ 不变空间都被所有 $\mathfrak C$ 元保持。
令
$$
\mathscr M_\nu=\overline{\{p(A)g_\nu:p\in\mathbb C[z]\}}.
$$
它被 $R_\nu$ 保持，故含 $R_\nu g_\nu=1$。
原 $1$ 循环，因此
$$
\boxed{g_i,\ g_j\text{ 都对 }A\text{ 循环}.}
\tag{2.1}
$$

固定以下图坐标顺序：第一坐标为输入，第二坐标为输出。
定义
$$
\Gamma_{\max}
=\{(u,v):R_iv=R_ju\}
=\operatorname{Graph}T_{\max},
$$
$$
T_{\max}=R_i^{-1}R_j,\qquad
\operatorname{Dom}T_{\max}
=\{u:R_ju\in R_iH\}.
\tag{2.2}
$$
$R_i$ 单射使图单值，方程的连续性使它闭。
其定义域含 $R_iH$，因为
$$
T_{\max}R_ih=R_jh.
$$
$R_iH$ 稠密，所以 $T_{\max}$ 稠密定义；
同一式给值域含稠密的 $R_jH$。
$R_j$ 单射还给 $T_{\max}$ 单射。

边界图为
$$
\Gamma_{\min}
=\overline{\{(R_ih,R_jh):h\in H\}}.
\tag{2.3}
$$
它包含于 $\Gamma_{\max}$，故是单值闭算子的图。
利用 $g_i$ 循环及 $R_ig_i=1$，
$$
\begin{aligned}
\Gamma_{\min}
&=\overline{\{(R_ip(A)g_i,R_jp(A)g_i)\}}\\
&=\overline{\{(p(A)1,p(A)h_{ij})\}},
\qquad h_{ij}=R_jg_i.
\end{aligned}
$$
因此
$$
\boxed{\Gamma_{\min}=\operatorname{Graph}X_{h_{ij}},\qquad
T_{\min}=X_{h_{ij}}.}
\tag{2.4}
$$
特别 $1\in\operatorname{Dom}T_{\min}$。

源循环图是
$$
\Gamma_{\mathrm{src}}
=\overline{\{(p(A)g_j,p(A)g_i):p\in\mathbb C[z]\}}.
\tag{2.5}
$$
$R_jg_j=R_ig_i=1$ 说明每个图向量都在 $\Gamma_{\max}$；
所以闭包仍为单值闭算子的图。
其定义域与值域均稠密，分别来自 $g_j,g_i$ 循环。
并且它准确含
$$
(g_j,g_i).
\tag{2.6}
$$
所有这些图都对 $A^{(2)}$ 不变，
从而对全部 $F^{(2)},F\in\mathfrak C$ 不变。

还可核 $\Gamma_{\min}\subset\Gamma_{\mathrm{src}}$：
在 (2.6) 上施加 $R_i^{(2)}$，得到
$$
(R_ig_j,R_ig_i)=(R_ig_j,1).
$$
而对源轨道向量改施加 $R_j^{(2)}$，得到
$$
(R_jp(A)g_j,R_jp(A)g_i)
=(p(A)1,p(A)R_jg_i).
$$
后者的闭包就是 (2.4)。
故
$$
\Gamma_{\min}\subseteq\Gamma_{\mathrm{src}}\subseteq\Gamma_{\max}.
\tag{2.7}
$$
本稿在一般 $r$ 情形只主张这些非严格包含；
不把真秩二已知的严格双缺口自动搬来。

## 3. 边界与最大比例图的准确共轭转置

对稠密定义算子，仍记 $T^\top=CT^*C$。
由 (2.3)，$(u,v)$ 属于 $T_{\min}^\top$ 的图，
当且仅当
$$
B(R_jh,u)=B(R_ih,v)\qquad(h\in H).
$$
两个 $R_\nu$ 都有界且 C 对称，因此该式等价于
$$
B(h,R_ju-R_iv)=0\qquad(h\in H),
$$
也就是 $R_iv=R_ju$。
所以
$$
\boxed{T_{\min}^\top=T_{\max}.}
\tag{3.1}
$$
$T_{\min}$ 已闭且稠密定义，再取一次共轭转置，得到
$$
\boxed{T_{\max}^\top=T_{\min}.}
\tag{3.2}
$$
(3.1)--(3.2) 是有界分母图的直接配对计算，
没有假设未知自然乘积域正合。

## 4. 复用的真空核心引理：非空广义预解迫最小及 C 自伴

为使证明自足，重述旧比例谱附录 §§2--3 的完整机制。

设 $T$ 闭、稠密定义，完整交换 $A$，且
$1\in\operatorname{Dom}T$。
其闭图与 R88 的强逼近给
$$
F\operatorname{Dom}T\subset\operatorname{Dom}T,\qquad
TF=FT\quad(F\in\mathfrak C).
\tag{4.1}
$$
对每个单位 $U\in\mathfrak C^\times$，
$U$ 及其逆都保持该域，所以
$TU=UT$、$\operatorname{Dom}TU=\operatorname{Dom}T$。

假设某个 $B\in\mathfrak C$ 使
$$
L=TU+B
$$
具有有界全域逆 $Z=L^{-1}$。
逆的唯一性给 $Z\in\mathfrak C$。
令 $s=L1$，则
$$
Zs=1.
\tag{4.2}
$$
和 §2 相同，$s$ 对 $A$ 循环。
$L=Z^{-1}$ 的图由
$$
w\longmapsto(Zw,w)
$$
连续参数化；其参数范数与图范数等价。
因 $p(A)s$ 在 $H$ 稠密，
$$
(Zp(A)s,p(A)s)=(p(A)1,p(A)s)
$$
在完整逆图中稠密。
故多项式 $1$ 轨道是 $L$ 的图核心。

又
$$
L=UT+B,\qquad T=U^{-1}(L-B)
$$
使两者图范数等价。
所以多项式 $1$ 轨道同样是 $T$ 的图核心，
从而
$$
T=X_{T1}.
\tag{4.3}
$$

还需最大 C 自伴性。
有界逆满足 $Z^\top=Z$，
对其逆图取共轭转置得到
$$
(Z^{-1})^\top=Z^{-1}.
$$
$U^{\pm1},B$ 保持自然域 $\operatorname{Ran}Z$，
且与 $Z^{-1}$ 在该域上交换。
因此
$$
T=U^{-1}(Z^{-1}-B)
$$
的共轭转置为 $(Z^{-1}-B)U^{-1}$，
两式自然域相同、作用相同。
于是
$$
\boxed{T=X_{T1},\qquad T^\top=T.}
\tag{4.4}
$$
这一引理没有使用 $Z\mathfrak C$ 的强主理想单位。

## 5. 所有中间实现都没有任何广义预解点

取任意闭的 $A^{(2)}$ 不变空间 $\Gamma$，
满足
$$
\Gamma_{\min}\subseteq\Gamma\subseteq\Gamma_{\max}.
\tag{5.1}
$$
它是单值、闭、稠密定义算子 $T_\Gamma$ 的图：
单值性由上界图保证，稠密域由下界图保证。
图不变性与 R88 给完整 $\mathfrak C$ 域交换。
(2.4) 还给
$$
1\in\operatorname{Dom}T_\Gamma,\qquad
T_\Gamma1=h_{ij}.
\tag{5.2}
$$

**定理。** 对所有 $U\in\mathfrak C^\times,F\in\mathfrak C$，
$$
\boxed{\sigma(T_\Gamma U+F)=\mathbb C.}
\tag{5.3}
$$

若某个 $\lambda$ 属于这个算子的预解集，
把 $F-\lambda I$ 记为 $B$。
§4 得
$$
T_\Gamma=X_{h_{ij}}=T_{\min},\qquad
T_{\min}^\top=T_{\min}.
$$
与 (3.1) 联合便有
$$
T_\Gamma=T_{\min}=T_{\max}.
\tag{5.4}
$$
因此即使原来未假定 $\Gamma$ 包含源图，
这个假设的预解点也已迫它包含源点 (2.6)。

令
$$
Z=(T_\Gamma U+B)^{-1}\in\mathfrak C,\qquad
v=Ug_i+Bg_j.
\tag{5.5}
$$
因为 $T_\Gamma g_j=g_i$，
真实域交换给
$$
(T_\Gamma U+B)g_j=v,\qquad Zv=g_j.
\tag{5.6}
$$
有界逆恒等式还给
$$
T_\Gamma Z=U^{-1}(I-BZ)\in\mathfrak C.
\tag{5.7}
$$
于是
$$
g_i=T_\Gamma Zv=U^{-1}(I-BZ)v.
\tag{5.8}
$$
用 (1.4)，得到两个原见证源的有界同源表达式
$$
x_i=D_iU^{-1}(I-BZ)v,\qquad x_j=D_jZv.
\tag{5.9}
$$
(5.9) 恰违反 (1.5)--(1.6)。
矛盾证明 (5.3)。

这个论证没有使用 $\Gamma_{\min}\ne\Gamma_{\max}$；
即使二者相等，(5.3) 仍由最小秩模压缩成立。
它也没有把所选两项当作一个秩二正湮灭者。
被压缩并用于最小性的始终是整个原 $\phi$。

## 6. 假设的预解式会显式产生实际共同分母

上面的矛盾还可以完全写成一个实际有界共同分母。
保留假设预解式 (5.5)，定义
$$
P=R_jZ.
\tag{6.1}
$$
因 (5.4)，在 $T_\Gamma$ 的原域上准确有
$R_iT_\Gamma=R_j$。
又 $Z$ 的全像包含于该域，故
$$
\boxed{
P=R_jZ=R_iT_\Gamma Z
=R_iU^{-1}(I-BZ)\in\mathfrak C.
}
\tag{6.2}
$$
这使 $P$ 同时具有两个实际有界右因子，因而
$$
PH\subset R_iH\cap R_jH
=\operatorname{Dom}M_i\cap\operatorname{Dom}M_j.
\tag{6.3}
$$
两行乘子都已全域有界化：
$$
M_iP=D_iU^{-1}(I-BZ),\qquad
M_jP=D_jZ.
\tag{6.4}
$$
另一方面，(5.6) 给
$$
Pv=R_jZv=R_jg_j=1.
\tag{6.5}
$$
(6.3)--(6.5) 正好是被 (1.7) 排除的共同真空原像。
这里没有把 $R_i^{-1}R_j$ 作未付域的形式消去；
(6.2) 先使用有界逆的真实像落在定义域中，再用最大图方程。

## 7. 反向比例及精确范围

交换两坐标，交换 $i,j$，
同样结论适用于全部反向中间比例图。
源图的输入输出均循环，最大图也单射稠密像；
因此反向图仍是稠密定义闭算子的图，不是多值关系。

本稿的结论强于仅说原 $M_i,M_j$ 缺少某个共同自然词，
但仍是必要结构限制：
它没有排除满复平面谱的闭比例算子，
没有证明高秩时边界图、源图、最大图必须严格不同，
没有把 (5.3) 的所有谱点称为连续谱点。
也未证明某个具体比例实现应当具有预解点。
原正常态问题及普通 Hilbert ISP 完成标准仍未关闭。

## 8. 已有共同奇异核心与紧扰动定理的范围推论

本节明确扣除已有机制。
[R244 共同奇异核心附录](R244-appendix-common-singular-core-sequences-and-compact-perturbation-full-spectrum.md)
已在真秩二情形证明：
共同原多项式核心弱零奇异列、pencil 核夹住、点谱参数独立、
任意紧扰动全近似点谱，以及两侧非半 Fredholm。
本稿不重计这些证明。
§5 的任意最小秩两行全谱提供其所需的新范围输入；
下述核查说明旧论证可逐项直接应用。

采用本稿的输入输出顺序，固定 $U,F,\lambda$，记
$$
B=F-\lambda I,\qquad
L_\Gamma=T_\Gamma U+B,\qquad
W=UR_j+BR_i\in\mathfrak C.
\tag{8.1}
$$
原有界列及最大图方程准确给
$$
L_\Gamma R_i y=Wy\quad(y\in H),\qquad
R_iL_\Gamma u=Wu\quad(u\in\operatorname{Dom}L_\Gamma).
\tag{8.2}
$$
这是旧证明使用的全部有界 pencil 接口。

唯一需要替换的旧前提是：旧稿在排 $W=0$ 时使用了严格图缺口。
这里不需要该缺口。
若 $W=0$，令 $V=-U^{-1}B\in\mathfrak C$，
则 $R_j=VR_i=R_iV$。
$R_i$ 单射使 (2.2) 的最大比例图恰为有界全域算子 $V$ 的图。
这与 §5 已证明的最大比例实现全广义谱矛盾。
因此
$$
W\ne0.
\tag{8.3}
$$

其余旧证明的输入完全保留：

1. 若 $L_\Gamma$ 有正下界，(8.2) 与 $R_i$ 单射迫 $W$ 单射；
   $W^\top=W$ 使其值域稠密。
   (8.2) 又使 $L_\Gamma$ 稠密像。
   闭算子有正下界给闭值域，遂产生有界逆，违反 §5。
2. (8.2) 给
   $R_i\ker W\subseteq\ker L_\Gamma\subseteq\ker W$。
   故点谱判据只看 $W$，不看中间图。
   无核时是稠密非满的连续谱；
   有核时，(8.3) 使 $\ker W$ 为原 $H$ 的非零真不变空间。
   原 $A$ 单射、拟幂零排除有限维非零不变空间，
   所以这时 $\ker L_\Gamma$ 无限维。
3. $T_{\min}=X_{h_{ij}}$ 的原多项式真空核心
   $\mathcal D=\{p(A)1\}$ 也是 $L_{\min}$ 的图核心。
   无核时，最小图没有正下界，故有核心单位近似核序列；
   闭线性图弱闭及核零迫该序列弱趋零。
   有核时，先在 $R_i\ker W$ 取正交单位序列，
   再用原图核心逼近。
   所有中间实现在该核心的作用一致，因此同一序列对全部中间图有效。
4. 任何固定有界紧算子把该弱零单位序列送到范数零，
   所以所有紧扰动仍全平面近似点谱。
   (3.1)--(3.2) 使每个中间图的共轭转置仍属于同一夹层；
   对其应用同样序列结论，得到伴随也有弱零单位近似核列。
   闭值域加有限维核与这种序列矛盾；
   对伴随使用闭值域对偶后，两侧半 Fredholm 均被排除。

因此，旧共同奇异核心定理的完整结论扩展为：
对任意最小正秩 $r\ge2$、任意所选两行的广义预解数据，
全部中间比例实现仍具有旧稿的共同核心奇异列、
同一 pencil 点谱判据及任意紧扰动后全近似点谱/两侧非半 Fredholm 结论。

这里只改变该旧定理的适用范围。
没有取得核心多项式的次数、系数或算子范数预算，
没有证明某个非零 $W$ 必有核；
若后者能另行证明，它才会直接给原 $H$ 的非平凡不变子空间。
