# R260：任意物理跨度的真实导子预算与非 little-weak-ℓ¹ 行的 Bell 分支排核

日期：2026-11-13（UTC）。作者：kernel。

状态：已证明的实际中间结论；root已全文核验真实导子域、壳层、选位及Bell图接口。本文支付任意有孔、任意大跨度高位集合的全部嵌套交换子；不再以最大选中位之前的粗头范数估计全部 carry。结合幅度排序计数，得到一个不依赖物理排列的正向排核定理。

## 1. 设置及主结论

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\qquad a_*\in\mathbb C.
$$
令 $\rho_n$ 是非零幅度 $|a_j|$ 的非增重排；必要时在有限序列后补零。相同幅度按任意固定次序排列。假设
$$
\boxed{\limsup_{n\to\infty}n\rho_n>0.}
\tag{1.1}
$$
这里允许上极限为无穷。行 $a$ 的相位及物理排列完全任意。

取任意复指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
沿用 R176/R259 的真实闭算子和有界累积量：
$$
c_j=e^{-2b_j},\qquad
R_j=V(c_jN_j),\qquad V(z)=(I-z)(I+z)^{-1},
$$
$$
X_b=X_u+H_{a,b}
=a_*I+\sum_j a_jR_j,\qquad
\operatorname{Dom}X_b=\operatorname{Dom}X_u,
$$
$$
K_\nu=\sum_j a_j^\nu L_\nu(R_j)\in\mathcal A,\qquad
L_\nu(v)=
\left.\frac{d^\nu}{dt^\nu}
 \log(\cosh t+v\sinh t)\right|_{t=0},
\quad \nu\ge2.
\tag{1.2}
$$
$H_{a,b}\in\mathcal A$ 是范数绝对收敛的有界交换扰动。
$L_\nu(1)=0$，故全部 $K_\nu$ 字符为零。

**定理。** 对任意固定 $d\ge2$ 及原点邻域上的任意固定多变量解析芽 $\Phi$，
$$
\boxed{
\ker\bigl(X_b-\Phi(K_2,\ldots,K_d)\bigr)=\{0\}.
}
\tag{1.3}
$$
因而任意非零简单根多项式 $q$ 都满足
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.4}
$$
非零常数也包括在内。

特别，任意物理重排、任意相位的幅度行
$|a_j|=1/(j+1)$ 满足结论；不要求物理次序中的系数和收敛。
本稿始终使用同一个原 $X_u$ 和原常数 $a_*$，没有把重排标量和写入算子定义。

本稿的新增核心是 §§3–6 的局部壳层和真实导子 Banach 代数。
R236 的对称平均及 R259 的多变量、倾斜机制在 §§7–10 以新预算重新闭合。

## 2. 固定有界因子与真实闭尾域

以下固定 $a,b,d,\Phi$，置
$$
Y=\Phi(K_2,\ldots,K_d),\qquad
T=X_b-Y,\qquad
\mathcal D=\operatorname{Dom}T,\qquad M=\ker T.
$$
$\mathcal D=\operatorname{Dom}X_u$，有限 Walsh 柱是图核心。
所有 $\mathcal A$ 元素保持 $\mathcal D$ 并与 $T$ 完整域交换。

记 $g=\|a\|_2$。有固定常数
$$
0<c_-\le|c_j|\le c_+<\infty,\qquad c_j\to1.
$$
对全部 $j$、两种符号及全部有限头截断，以下逆范数一致有界：
$$
\|(I\pm c_jN_j)^{-1}\|,\qquad
\|(I\pm c_jN_j^{[h]})^{-1}\|\quad(h\ge j+1).
\tag{2.1}
$$
这里
$$
N_j^{[h]}
=\sum_{\ell=j}^{h-1}\frac{\alpha_\ell}{\alpha_j}
 E_j^*\cdots E_{\ell-1}^*E_\ell
\tag{2.2}
$$
是前 $[j,h)$ 位的真实有限截断，$\|N_j^{[h]}\|\le1$。

证明 (2.1)：大 $j$ 时 $|c_j|\le2$，且实际及截断平方都含 $\eta_j$，
所以用
$$
(I\pm cN)^{-1}=(I\mp cN)(I-c^2N^2)^{-1}
$$
得到统一界。余下有限个 $j$，真实 $N_j$ 准幂零，因而真实逆存在；
$N_j^{[h]}\to N_j$ 按范数收敛，所以充分大 $h$ 的逆有界，
再将余下有限个截断的逆取最大值。不能省略这个有限低位步骤。

设 $D$ 是支撑在前 $\ell+1$ 位的任意局部矩阵。令
$$
X_{b,>\ell}=X_b-a_*I-\sum_{j\le\ell}a_jR_j.
$$
它与 $X_b$ 相差有界项，完整域仍是 $\mathcal D$。
在有限柱上，$D$ 与各有限尾截断交换；R125 的核心收敛及倾斜差的范数收敛给
$X_{b,>\ell}D=DX_{b,>\ell}$。
以有限柱图逼近及闭性延拓，得到
$$
\boxed{
D\mathcal D\subseteq\mathcal D,\qquad
X_{b,>\ell}D=DX_{b,>\ell}\text{ 于 }\mathcal D.
}
\tag{2.3}
$$

置
$$
D_\ell^{\rm bd}=a_*I+\sum_{j\le\ell}a_jR_j-Y,\qquad
d_\ell=2\|D_\ell^{\rm bd}\|.
$$
该有界算子在 $\mathcal A$ 中，与闭尾 first 完整交换。
因此局部 $D$ 满足全部真实域等式
$$
\boxed{
\operatorname{ad}_T^sD
=\operatorname{ad}_{D_\ell^{\rm bd}}^sD,\qquad
\|\operatorname{ad}_T^sD\|\le d_\ell^s\|D\|.
}
\tag{2.4}
$$
每一阶右端都保持 $\mathcal D$，并与同一个闭尾 first 交换。
同时
$$
d_\ell\le A_0+A_1\sum_{j\le\ell}|a_j|
\le A_0+A_1g\sqrt{\ell+1}
\tag{2.5}
$$
对固定常数 $A_0,A_1$ 成立。
这是逐局部壳使用的估计，不是将所有误差粗乘最大选中位的头范数。

## 3. 任意有限反射集的局部壳层

设 $F$ 是任意非空有限位集，$m=\min F\ge1$。
令
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
\gamma_F(Q)=J_FQJ_F,\qquad
s_j=\begin{cases}-1,&j\in F,\\1,&j\notin F.\end{cases}
$$

对 $h\ge j+1$ 定义
$$
R_j^{[h]}(s)=V(sc_jN_j^{[h]}),\qquad s\in\{1,-1\}.
$$
令
$$
\Lambda_{j,\ell}(s)
=R_j^{[\ell+1]}(s)-R_j^{[\ell]}(s),
\qquad \ell\ge j+1.
$$
由 (2.1)、准确逆差式及
$$
N_j^{[\ell+1]}-N_j^{[\ell]}
=\frac{\alpha_\ell}{\alpha_j}E_j^*\cdots E_{\ell-1}^*E_\ell,
$$
得到
$$
\boxed{
\|\Lambda_{j,\ell}(s)\|
\le C_b\frac{\alpha_\ell}{\alpha_j}.
}
\tag{3.1}
$$
它只作用于 $[j,\ell]$。

基本的纯位项
$$
R_j^{[j+1]}(s)=I-2sc_jE_j
$$
在 $\gamma_F$ 下准确变号。因此
$$
\gamma_F(R_j)-V(s_jc_jN_j)
=\sum_{\ell\ge j+1}
 \bigl(\gamma_F(\Lambda_{j,\ell}(1))-\Lambda_{j,\ell}(s_j)\bigr).
\tag{3.2}
$$
该级数按范数绝对收敛。

**精确消失条件：** 若
$$
F\cap\{j+1,\ldots,\ell\}=\varnothing,
$$
则 (3.2) 的第 $\ell$ 个差壳为零。
事实上，在 $N_j^{[\ell+1]}$ 的每个实际串中，第 $j$ 位只出现一次，
其余位置没有反射；所以
$\gamma_F(N_j^{[\ell+1]})=s_jN_j^{[\ell+1]}$，
较短截断同样成立。
这不是只说误差很小，而是实际有限矩阵的精确相等。

因此所有非零差壳都满足 $\ell\ge m$。
将 (3.2) 乘 $a_j$ 后按最高位收集，得到
$$
E_{X,F}:=\gamma_F(X_b)-
 \left(X_b+\sum_{j\in F}a_j(V(-c_jN_j)-R_j)\right)
=\sum_{\ell\ge m}B_{1,\ell,F},
\tag{3.3}
$$
其中 $B_{1,\ell,F}$ 只作用于前 $\ell+1$ 位，且
$$
\|B_{1,\ell,F}\|
\le C_b\sum_{j<\ell}|a_j|\frac{\alpha_\ell}{\alpha_j}.
$$
真实权比及 Cauchy–Schwarz 给
$$
\begin{aligned}
\sum_{j<\ell}|a_j|\frac{\alpha_\ell}{\alpha_j}
&=\eta_{\ell-1}
 \sum_{j<\ell}|a_j|\frac{\alpha_{\ell-1}}{\alpha_j}\\
&\le
\frac{g}{\sqrt{1-\eta_*^2}}\,\eta_{\ell-1},
\qquad \eta_*=\sup_j\eta_j<1.
\end{aligned}
$$
故
$$
\boxed{
\|B_{1,\ell,F}\|\le C_1\eta_{\ell-1}.
}
\tag{3.4}
$$
常数完全不依赖 $|F|$ 或 $\max F$。

(3.3) 是完整域上的等式：先在有限柱核心用有限 first 截断验证，
双重误差级数由 (3.4) 绝对收敛；$\gamma_F(X_b)$ 与括号中的算子
都在同一 $\mathcal D$ 上且是 $X_b$ 的有界扰动。
后一点由 (2.3) 对有限局部 $J_F$ 得到。
因此核心等式延到完整域。

### 3.1 固定高阶累积量也有同样局部壳

对固定 $\nu\ge2$，把上述 $R_j^{[h]}(s)$ 换成
$L_\nu(R_j^{[h]}(s))$。
$L_\nu$ 是固定多项式；(2.1) 给全部输入的一致范数界，故幂差公式仍给
第 $\ell$ 个壳不超过固定常数乘 $\alpha_\ell/\alpha_j$。
其精确消失条件与 (3.2) 完全相同。

令
$$
\widehat K_{\nu,F}
=K_\nu+\sum_{j\in F}a_j^\nu
 \bigl(L_\nu(V(-c_jN_j))-L_\nu(R_j)\bigr).
$$
于是
$$
\boxed{
\gamma_F(K_\nu)-\widehat K_{\nu,F}
=\sum_{\ell\ge m}B_{\nu,\ell,F},\qquad
\|B_{\nu,\ell,F}\|\le C_\nu\eta_{\ell-1}.
}
\tag{3.5}
$$
每个壳仍局部于前 $\ell+1$ 位。
这里将 (3.4) 的 $g$ 换成
$(\sum_j|a_j|^{2\nu})^{1/2}<\infty$ 即可。
全部常数只依赖原固定行及固定 $\nu$。

## 4. 真实完整域上的导子 Banach 代数

写 $\delta B=[T,B]$。
本节只将已经满足
$$
B\mathcal D\subseteq\mathcal D,\qquad
TB-BT\text{ 在 }\mathcal D\text{ 上有界延拓}
$$
的算子纳入导子域；高阶导数递归采用同一真实域要求。

定义
$$
\mathfrak D_T
=\left\{B\in B(H):
 \delta^sB\text{ 全部具有上述真实域性质，且 }
 \|B\|_{\delta}:=\sum_{s\ge0}\frac{\|\delta^sB\|}{s!}<\infty
\right\}.
\tag{4.1}
$$
其中 $\delta^0B=B$。

这是幺 Banach 代数，而且
$$
\|BC\|_\delta\le\|B\|_\delta\|C\|_\delta,\qquad
\|I\|_\delta=1.
\tag{4.2}
$$
证明乘积估计：完整域上的 Leibniz 公式逐阶给
$$
\delta^s(BC)=\sum_{k=0}^s\binom sk(\delta^kB)(\delta^{s-k}C).
$$
除以 $s!$ 求和即得 (4.2)；每个导数的域保持也由有限乘积和递归支付。

证明完备性：若 $B_n$ 在该范数下 Cauchy，则每阶 $\delta^sB_n$ 都在
算子范数下收敛到某个 $C_s$。
对任意 $f\in\mathcal D$，
$$
T(\delta^sB_n f)=\delta^sB_n Tf+\delta^{s+1}B_n f.
$$
两端图向量收敛；$T$ 闭性给 $C_sf\in\mathcal D$ 及
$TC_sf=C_sTf+C_{s+1}f$。
所以 $C_s=\delta^sC_0$ 且每阶完整域保持成立。
对有限阶部分和取极限，再控制 Cauchy 尾，得到范数收敛到 $C_0$。
这就证明完备性。

特别，在该代数中范数小于1的算子可用真正的 Neumann 级数求逆；
其和同时是 $B(H)$ 中的实际逆，且所有导数及完整域保持都已由完备性支付。
不把“有界逆”自动当作保域。

由 (2.4)，局部壳满足
$$
\|B_{\nu,\ell,F}\|_\delta
\le e^{d_\ell}\|B_{\nu,\ell,F}\|.
$$
因此 (3.3)、(3.5) 都在这个真实代数中绝对收敛，且
$$
\|E_{X,F}\|_\delta+
 \sum_{\nu=2}^d\|\gamma_F(K_\nu)-\widehat K_{\nu,F}\|_\delta
\le C_2\sum_{\ell\ge m}
 \eta_{\ell-1}e^{A_0+A_1g\sqrt{\ell+1}}.
$$
$\eta_\ell\le e^{-770\,16^\ell}$，故充分大 $m$ 时可统一写成
$$
\boxed{
\|E_{X,F}\|_\delta+
 \sum_{\nu=2}^d\|\gamma_F(K_\nu)-\widehat K_{\nu,F}\|_\delta
\le\varepsilon_m,\qquad
\varepsilon_m\le C_3e^{-385\,16^{m-1}}.
}
\tag{4.3}
$$
这里及以后不出现 $\max F$。
这正是任意大跨度集合需要的新增实际预算。

## 5. 多变量预解式在导子代数中的逆与误差

假设选中系数足够小，使
$$
\sum_{j\in F}|a_j|^2\longrightarrow0
\tag{5.1}
$$
沿后续集合序列成立。
固定原元组 $\mathbf K=(K_2,\ldots,K_d)$ 的小多圆周 $\Gamma$，
完全位于 $\Phi$ 的解析域内并围住各坐标零谱。

固定多项式的范数界给
$$
\|\widehat K_{\nu,F}-K_\nu\|
\le C_\nu'\sum_{j\in F}|a_j|^\nu
\le C_\nu''\sum_{j\in F}|a_j|^2.
$$
所以充分远处，所有
$$
\widehat R_{\nu,F}(\zeta)
=(\zeta-\widehat K_{\nu,F})^{-1}
$$
在 $\Gamma$ 上统一有界。
它们属于 $\mathcal A$，因此与 $T$ 完整交换，且
$$
\|\widehat R_{\nu,F}(\zeta)\|_\delta
=\|\widehat R_{\nu,F}(\zeta)\|.
\tag{5.2}
$$

置 $E_{\nu,F}=\gamma_F(K_\nu)-\widehat K_{\nu,F}$。
由 (4.3)，充分大 $m$ 时
$\|\widehat R_{\nu,F}E_{\nu,F}\|_\delta<1/2$。
因此在真实 Banach 代数中
$$
(\zeta-\gamma_F(K_\nu))^{-1}
=(I-\widehat R_{\nu,F}E_{\nu,F})^{-1}
 \widehat R_{\nu,F}.
\tag{5.3}
$$
这是真正的有界逆，且保全部所需完整域。
Neumann 范数预算给
$$
\left\|(\zeta-\gamma_F(K_\nu))^{-1}
       -\widehat R_{\nu,F}(\zeta)\right\|_\delta
\le C_\Gamma\varepsilon_m.
\tag{5.4}
$$

在多变量 Cauchy 公式中按固定顺序逐因子相减，得到
$$
\boxed{
\|\gamma_F(Y)-\widehat Y_F\|_\delta
\le C_\Phi\varepsilon_m,\qquad
\widehat Y_F=\Phi(\widehat K_{2,F},\ldots,\widehat K_{d,F}).
}
\tag{5.5}
$$
各元组内部交换以定义演算；两个元组之间不要求互相交换。
被积函数在 $\mathfrak D_T$ 范数中连续并有统一界，
故积分也在该 Banach 代数中取值。

定义
$$
\widehat X_F=X_b+\sum_{j\in F}a_j(V(-c_jN_j)-R_j),
$$
$$
A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F).
$$
$A_F\in\mathcal A$ 与 $T$ 完整交换；
由 (4.3)、(5.5)，扩大固定常数后
$$
\boxed{
\|E_F\|_\delta\le\widetilde\varepsilon_m,\qquad
\|\delta^sE_F\|\le s!\widetilde\varepsilon_m,\qquad
\widetilde\varepsilon_m\le C_4e^{-385\,16^{m-1}}.
}
\tag{5.6}
$$
这是全部阶数同时的真实域估计，不是固定阶后允许常数依赖最大位。

## 6. 允许阶乘导数预算的真实幂递推

设 $f\in M$、$v=J_Ff$。由 (2.3)，$J_F$ 双向保持 $\mathcal D$，
且
$$
Tv=-(A_F+E_F)v.
$$
定义
$$
Q_0=I,\qquad Q_{n+1}=\delta Q_n-Q_n(A_F+E_F).
\tag{6.1}
$$
$A_F$、$E_F$ 及各导数保持 $\mathcal D$，
所以递归同时给
$$
v\in\operatorname{Dom}T^n,\qquad T^nv=Q_nv.
\tag{6.2}
$$

给 $A_F$ 权1，给 $\delta^sE_F$ 权 $s+1$。
$Q_n$ 的每个单项式总权为 $n$，系数绝对值总和至多 $(n+1)!$；
唯一没有误差因子的项是 $(-A_F)^n$。
若某项含误差导数阶数 $s_1,\ldots,s_k$，则
$$
\prod_{i=1}^k s_i!\le\left(\sum_i s_i\right)!\le n!.
$$
当 $\widetilde\varepsilon_m\le1$ 时，多余误差因子可用1控制。
因此
$$
\boxed{
\|T^nJ_Ff-(-A_F)^nJ_Ff\|
\le(n+1)!\,n!\,\widetilde\varepsilon_m
 (1+\|A_F\|)^n\|f\|.
}
\tag{6.3}
$$
与 R259 相比只多出一个 $n!$；
它的对数为 $O(n\log n)$，不会破坏后面的三次对四次比较。

## 7. 幅度排序给足够多的高位同幅系数

由 (1.1)，存在固定 $c_0>0$ 和趋于无穷的整数 $N$，使
$$
N\rho_N\ge c_0.
\tag{7.1}
$$
从幅度最大的 $N$ 个实际指标中，先去掉幅度排序最前
$\lfloor N/4\rfloor$ 项，再去掉物理位置
$j<\lfloor N/4\rfloor$ 的项。
每次至多去掉 $\lfloor N/4\rfloor$ 项，故至少留下 $N/2$ 项。
剩下所有指标均满足
$$
j\ge m_N:=\lfloor N/4\rfloor,\qquad
\frac{c_0}{N}\le|a_j|
\le \rho_{\lfloor N/4\rfloor+1}
\le\frac{2g}{\sqrt N}
\tag{7.2}
$$
对充分大 $N$ 成立。

从 $c_0/N$ 起，把这个幅度区间按二进档 $[2^sc_0/N,2^{s+1}c_0/N)$ 分桶，记桶左端为 $\tau$。
档数为 $O(\log N)$，故有一档含至少 $c_1N/\log N$ 项。
取
$$
r=\lceil\sqrt{\log N}\rceil,\qquad q=r^4.
$$
充分大 $N$ 时，该档容量大于 $q$；
从中任取一个恰有 $q$ 个元素的实际指标集 $I_r$。
于是
$$
\boxed{
\min I_r\ge m_N,\qquad
\tau_N\le|a_j|<2\tau_N\ (j\in I_r),\qquad
\frac{c_0}{N}\le\tau_N\le\frac{2g}{\sqrt N}.
}
\tag{7.3}
$$
不控制 $\max I_r$，也不需要控制。

沿子序列可使 $r\to\infty$ 严格增加。
由
$(r-1)^2<\log N\le r^2$，有
$$
r\log(\tau_N^{-1})\le r^3+O(r),
\qquad
\tau_N C^r\to0
\quad\text{对每个固定 }C>0.
\tag{7.4}
$$
同时 $r\tau_N^2\to0$、$r\tau_N\to0$，
所以 §5 的近元组轮廓条件自动满足。

这里的幅度排序仅用于挑选有限实际位集；
没有更改原 first、原常数项或原物理算子的定义。

## 8. 对任意跨度桶进行真实对称平均

对 $F\subset I_r$、$|F|=r$，置
$$
p_F=\prod_{j\in F}a_jc_j,\qquad
\mathcal B_r=\frac1{(-2q)^r}\sum_{|F|=r}p_F^{-1}J_F.
\tag{8.1}
$$
其绝对系数预算为
$$
S_r\le\frac{(2c_-\tau_N)^{-r}}{r!},
$$
故
$$
\boxed{
\|\mathcal B_r\|\le\frac{\exp(r^3+O(r))}{r!}.
}
\tag{8.2}
$$

准确有理差
$$
V(-cN)-V(cN)=4cN(I-c^2N^2)^{-1}
$$
及固定多变量 Cauchy 差给
$$
P_F=4\sum_{j\in F}a_jc_jN_j,\qquad
\|P_F\|\le C_P r\tau_N,
$$
$$
\boxed{
\|A_F-P_F\|\le C_A r\tau_N^2,\qquad
\|A_F\|\le C_0r\tau_N.
}
\tag{8.3}
$$
这里真实有理余项至多 $Cr\tau_N\eta_{m_N}$；
因 $\tau_N\ge c_0/N$ 而 $m_N\sim N/4$，该项已吸收到右侧。
所有常数不依赖 $\max I_r$。

将 (6.3) 以 $n=r$ 对全部 $F$ 相加。
由 (8.2)、$r\tau_N\to0$、(5.6)，非交换误差不超过
$$
\widetilde\varepsilon_{m_N}\exp(r^3+O(r\log r))\|f\|
\longrightarrow0.
\tag{8.4}
$$

真实幂差给
$$
\|A_F^r-P_F^r\|
\le C_A r^2(C_0r)^{r-1}\tau_N^{r+1}.
$$
乘完整 $S_r$，并用 $r!\ge(r/e)^r$，剩余不超过
$$
\boxed{C_2r\tau_N C_3^r\|f\|\longrightarrow0.}
\tag{8.5}
$$
这是选择同幅桶与 (7.4) 的用途。

所有 $N_j$ 交换，含重复位的项有实际因子 $\eta_j$，所以
$$
P_F^r
=4^r r!p_F\prod_{j\in F}N_j+\mathcal R_F,
\qquad
\|\mathcal R_F\|
\le\eta_{m_N}(C_Pr\tau_N)^r.
$$
经 $S_r$ 求和后误差至多 $\eta_{m_N}C_4^r\|f\|\to0$。
再用
$$
E_jJ_j=E_j,\qquad
\left\|\left(\prod_{j\in F}N_j\right)J_F-\prod_{j\in F}E_j\right\|
\le r\eta_{m_N},
$$
最后误差至多 $2^rr\eta_{m_N}\|f\|\to0$。

置
$$
C_{I_r}=\frac2q\sum_{j\in I_r}E_j.
$$
不同位纯 $E_j$ 平方为零，故最终得到
$$
\boxed{
\mathcal B_rM\subseteq\operatorname{Dom}T^r,\qquad
\|T^r\mathcal B_rf-C_{I_r}^rf\|\le\epsilon_r\|f\|,
\quad\epsilon_r\to0.
}
\tag{8.6}
$$
$p_F$ 消去全部复系数及倾斜系数，主项是同一个纯平均。

### 8.1 有孔集合不改变强近单位

在这 $q$ 个独立物理位上，层估计仍给
$$
\|C_{I_r}\|\le1+1/q,\qquad
\|C_{I_r}^r\|\le e^{r/q}.
$$
若 $f$ 是任意固定有限柱，充分大 $r$ 时
$\min I_r$ 已高于其支撑，故
$$
\|(C_{I_r}-I)f\|=q^{-1/2}\|f\|,
$$
$$
\|(C_{I_r}^r-I)f\|
\le r q^{-1/2}(1+1/q)^{r-1}\|f\|\to0.
$$
只使用所选位之间的独立性，不要求相邻。
有限柱稠密与一致范数界给
$$
C_{I_r}^r\longrightarrow I\quad\text{强于整个原 Haar 空间}.
$$
因此
$$
\boxed{T^r\mathcal B_rf\longrightarrow f\qquad(f\in M).}
\tag{8.7}
$$

## 9. 固定局部交换子的四次衰减及排核

对任意固定局部矩阵 $D$，设其支撑在前 $h$ 位。
R259 的明确有限低头分解在这里不需要任何系数慢尾假设：
$$
T=Z_h+G_h,\qquad G_h=A U_h,\quad U_h\in\mathcal A,
$$
其中 $Z_h$ 是实际闭尾 first 加常数、减去尾多变量 Bell 函数。
$D$ 与 $Z_h$ 完整交换。
为说明 $A$ 因子的准确来源，
$$
R_j-I=-2c_jN_j(I+c_jN_j)^{-1}
=A\left(-2c_jd_j^{-1}A^{2^j-1}(I+c_jN_j)^{-1}\right),
$$
而 $L_\nu(1)=0$ 使每个有限低头累积量差也有同类 $A$ 因子。
多圆周预解式逐坐标相减，将这些因子带过 $\Phi$。
只有固定有限低头被除以 $A$，没有将一般零字符元直接除以 $A$。

所以
$$
\operatorname{ad}_T^rD=\operatorname{ad}_{G_h}^rD.
$$
域保持和全部自然 Leibniz 公式由完整尾交换逐阶得到。
原实际权的 R109 界
$$
\|A^n\|\le
\exp\left[-\frac{100}{15}n^4+105n^3\right]
$$
与有界交换子展开给
$$
\boxed{
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_h\|)^r
 \exp\left[-\frac56r^4+105r^3\right].
}
\tag{9.1}
$$

$T$ 在其真实完整域 $C$ 自伴。
对 $f,g\in M$，取 $v_r=\mathcal B_rf$，
自然域 Leibniz 及 $Tg=0$ 给
$$
\mathcal B(DT^r\mathcal B_rf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal B_rf,g),
\quad
\mathcal B(x,y)=\langle x,Cy\rangle.
$$
由 (8.2)、(9.1)，右端至多固定常数乘
$$
\frac{\exp[-\frac56r^4+106r^3+O(r)]}{r!}
 \|f\|\,\|g\|\longrightarrow0.
$$
左端由 (8.7) 趋于 $\mathcal B(Df,g)$，所以
$$
\mathcal B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意固定局部矩阵}).
\tag{9.2}
$$
实际 Haar 局部全矩阵代数不可约，其任意非零向量的局部轨道线性张成稠密。
取非零 $f=g\in M$，(9.2) 将迫 $Cf$ 正交于这个稠密轨道，矛盾。
故 $M=0$，证明 (1.3)。

## 10. 简单根多项式、物理重排及与 little-weak-ℓ¹ 接口的衔接

对次数 $d$ 的 $q$，R176 给
$$
q(u)e^w=P_{q,b}(X_b)e^w,
\qquad
\operatorname{Dom}P_{q,b}(X_b)=\operatorname{Dom}X_u^d,
$$
且该自然算子闭、$C$ 自伴，具有循环向量 $e^w$ 生成的真实图核心。
其系数是 $K_2,\ldots,K_d$ 的有限 Bell 多项式，字符多项式为 $q$。

若 $q$ 根全简单，原点附近的多变量隐函数分支
$\Phi_1,\ldots,\Phi_d$ 给
$$
P_{q,b}(X_b)=q_d\prod_{\nu=1}^d
 (X_b-\Phi_\nu(K_2,\ldots,K_d))
$$
于准确的自然域 $\operatorname{Dom}X_u^d$。
各有界系数在 $\mathcal A$ 中，与 $X_b$ 完整交换；
自然乘积的反向域由逐阶减去低阶项支付。
(1.3) 使每个因子单射，故乘积无核。
完整 $C$ 自伴性与 R176 的图循环判据遂给 (1.4)。

(1.1) 只取决于幅度多重集。因此该结论对任意物理重排保持，
也不因独立复相位改变。规范幅度 $1/(j+1)$ 有
$n\rho_n\to1$，所以其全部物理重排都满足本稿定理；
即使物理次序中的条件和被改变，也没有更换原 $a_*$ 来“补偿”。

还有一个对全部行有用的必要条件。
若某个非零闭分支
$$
M=\ker(X_b-\Phi(K_2,\ldots,K_d))
$$
存在，则本稿迫
$$
n\rho_n\to0.
$$
在该分支上
$$
X_u|_M=(\Phi(\mathbf K)-H_{a,b})|_M
$$
有界，且谱只可能是单点 $\{\Phi(0)\}$：
括号中是字符 $\Phi(0)$ 的 $\mathcal A$ 元素，
其减去字符后的全空间及限制都是准幂零。
此时 R251 的真实幅度排序中心定理进一步给
$$
\boxed{
a_*+\sum_{k=1}^n a_{\pi(k)}
\longrightarrow\Phi(0),
}
\tag{10.1}
$$
其中 $\pi$ 按幅度排序。这是对同一原闭算子的必要条件，
不是将该极限重新定义为常数项。

所以解析 Bell 分支仍可能存在的行被进一步压到：
little-weak-ℓ¹ 幅度、幅度排序的复系数和收敛，
且其极限恰等于分支字符。
本稿没有排除这个剩余类，也没有将简单根结论推广到一般重复根。

## 11. 已付清与未外推之处

本稿支付了：

- 任意有限高位集合的精确局部壳消失条件；
- 只依赖最小选中位的全部真实嵌套交换子预算；
- 完整域导子 Banach 代数的完备性、乘积及实际 Neumann 逆；
- 在该代数中运输多变量 Bell 预解式；
- 幅度排序的两次 $N/4$ 排除、同幅桶及准确输入成本；
- 任意物理跨度上的全 Haar 强近单位与最高交换子配对。

没有声称：

- 原算子的全部非零向量都循环；
- little-weak-ℓ¹ 同字符剩余分支已消失；
- 一般重复根伴随矩阵的非交换误差已付；
- 边界核或奇异态可以搬回原 Haar 正常向量。

普通 Hilbert 不变子空间问题仍未完成。

## 依赖

R125/R161 的真实图核心与域交换；R176 的复倾斜和自然 Bell 域；
R236 对称高位平均的基本机制；R259 的多变量分支接口；
R109 的原 $A^n$ 四次界；R251 的幅度排序中心定理。


完整前置证明：[R259](R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)、[R251](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md)、[R176](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。
