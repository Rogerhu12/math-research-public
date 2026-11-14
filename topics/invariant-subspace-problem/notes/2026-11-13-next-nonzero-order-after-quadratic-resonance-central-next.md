# 二次共振之后的首个非零阶：临界弱 $\ell^1$ 行的真实逆与循环性

日期：2026-11-13（UTC）。作者：central_next（Astra-ISP-0c017065）。
状态：已证明；原 Haar 模型的中间结论，普通 ISP 未完成。

R270 第一附录的二次非共振条件在辅助系数趋近 $2a_j^2$ 时退化；
R270 第三附录已经关闭完全相等的情形。
本稿处理其后保留一个固定有限非零阶的情形。
新增的是共同逆半径 $\delta^{2\kappa-2}$、核内准确线性逆，
以及该尺度下的全部真实导子、自然域和共同平均。

## 1. 范围与主定理

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
$$
其非零幅度递减重排 $\rho_n$ 满足
$$
\boxed{
0<\limsup_{n\to\infty}n\rho_n
\le B_a:=\sup_{n\ge1}n\rho_n<\infty.
}
\tag{1.1}
$$
相位与物理排列任意。
固定整数 $\kappa\ge3$。
设复系数 $c_j$ 满足，对全部 $j$，
$$
|c_j|\le C_0|a_j|^\kappa,
\tag{1.2}
$$
且对充分大的物理位 $j$，只要 $a_j\ne0$ 就有
$$
|c_j|\ge c_0|a_j|^\kappa,\qquad c_0>0.
\tag{1.3}
$$
特别，$c_j=\gamma a_j^\kappa+o(|a_j|^\kappa)$、
$\gamma\ne0$，以及 $c_j=\gamma a_j^\kappa$ 均符合条件。
(1.2) 蕴含 $c\in\ell^1$，且 $a_j=0$ 时 $c_j=0$。

定义真正有界辅助
$$
v=\sum_j(2a_j^2+c_j)(\chi_j-1).
\tag{1.4}
$$
取任意复 first 指数权
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$

**定理。**
$$
\boxed{(u^2+v)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$
这个输出自动非零。
条件 (1.1) 不要求物理顺序单调，也不要求系数同相。
(1.3) 只需要最终成立；选位时会避开有限低位。

该结论不由 R270 原非共振下界得到，因为
$$
\frac{2a_j^2+c_j}{a_j^2}\longrightarrow2
$$
沿非零高位成立。
也不能直接由完全抵消的 $c=0$ 情形得到，
因为本稿的 $Y_c$ 一般是慢算子，未被声称属于 $\mathcal G$。

## 2. 真实闭核与准确共振分解

记
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j),
\qquad V(z)=(I-z)(I+z)^{-1},
$$
并令 $X=X_b$ 为实际倾斜闭 first。
固定 $b$ 后，全部 $(I\pm t_jN_j)^{-1}$ 一致有界：
高位使用真实平方关系，有限低位用其准幂零预解式。

置
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_j a_j^2(R_j-I)^2.
\tag{2.1}
$$
两者在 $\mathcal A$ 中按范数绝对收敛，字符为零。
R270B 已证明 $B\in\mathcal G$，保留所有实际 carry。
原混合 Bell 恒等式给
$$
\boxed{
T=X^2+Y-B,\qquad
Te^w=(u^2+v)e^w.
}
\tag{2.2}
$$
R176 给准确的闭自然域与完整共轭：
$$
\operatorname{Dom}T=\operatorname{Dom}X^2,\qquad
T=C_0T^*C_0.
\tag{2.3}
$$
若 $M=\ker T$，则
$$
M\subseteq\mathcal D_\infty:=
\bigcap_{n\ge0}\operatorname{Dom}X^n,\qquad
X_M:=X|_M\in B(M).
\tag{2.4}
$$
全部 $\mathcal A$ 系数保持 $M$ 并完整交换 $X$。
在这个同一实际核上，
$$
\boxed{X_M^2=(B-Y)|_M.}
\tag{2.5}
$$
不假设 $X_M$ 可逆，也不将 $B$ 有界除以某个 $A$ 幂。

以下反证 $M\ne0$，记 $B_M=\|X_M\|$。

## 3. 辅助慢和的真实分阶预算

### 3.1 正锥主控与 $\kappa-1$ 阶乘幂

令 $L=\max(1,\sup_j|t_j|)$，取
$$
W(z)=\frac{2Lz}{1-Lz}.
$$
它的 Taylor 系数非负，且在原函数非负锥上有
$$
|(R_j-I)f|\le W(N_j)|f|.
$$
这里使用逐点函数锥，而非 Hilbert 自伴正性。
令
$$
M_c=\sum_j|c_j|W(N_j).
$$
该和范数收敛，且
$$
|Y^nf|\le M_c^n|f|.
\tag{3.1}
$$

真实 $N_j^2=\eta_jN_{j+1}$、$\|N_j\|=1$ 给
$$
W(N_j)=2L N_j+N_j^2W_2(N_j),
\qquad \sup_j\|W_2(N_j)\|<\infty.
$$
将偶奇幂分开可得，对 $q\ge0$，
$$
\|e^{zqW(N_j)}\|
\le(1+C|z|q)\exp(C'|z|q\sqrt{\eta_j}).
\tag{3.2}
$$

这正是既有分阶预算的实际头尾证明，简述其参数支付。
令 $t=|z|$，取最小 $h\ge1$ 使
$$
385\,16^h\ge2\log(2+t).
$$
物理尾的额外 carry 因子由
$$
t\sum_{j\ge h}|c_j|\sqrt{\eta_j}\le C
$$
支付。物理有限头真实地写成 $AU_h$，其中
$$
\|U_h\|\le C\Bigl(\sum_j|c_j|\Bigr)e^{125\,16^{h-1}}.
$$
原四次幂界给其指数成本
$K\exp[C(1+\log(2+t))^{4/3}]$。
没有对物理位作排序算子。

仅在非负标量乘积中使用 (1.1)--(1.2)：
$c$ 的非零幅度重排满足 $c_n^*\le C_0B_a^\kappa n^{-\kappa}$，故
$$
\sum_{n\ge1}\log(1+Ctc_n^*)\le C_\kappa t^{1/\kappa}.
$$
由 (3.2)，并把 $(\log(2+t))^{4/3}$ 吸入固定 $\kappa$ 下的
$t^{1/\kappa}$，得到
$$
\|e^{zM_c}\|\le K_\kappa e^{D_\kappa|z|^{1/\kappa}}.
$$
Cauchy 取半径 $R=(\kappa n/D_\kappa)^\kappa$，
并使用 $n!\le n^n$，给
$$
\boxed{
\|Y^n\|\le K D^n/(n!)^{\kappa-1}.
}
\tag{3.3}
$$

### 3.2 真正预解式

由绝对 Neumann 级数，任意 $z\ne0$ 有
$$
z(z-Y)^{-1}=\sum_{n\ge0}z^{-n}Y^n.
$$
对整数 $s=\kappa-1\ge2$，$(e^x)^s$ 的对角项给
$$
\sum_{n\ge0}\frac{u^n}{(n!)^s}
\le e^{s u^{1/s}}.
$$
于是
$$
\boxed{
\|z(z-Y)^{-1}\|
\le K\exp(C|z|^{-1/(\kappa-1)}).
}
\tag{3.4}
$$

$B\in\mathcal G$ 且非零首阶为正，R151 给某些固定 $K_B,d_B>0$ 使
$$
\|B^n\|\le K_Be^{-d_Bn^4}.
$$
同一真实 Neumann 级数及四次 Young 不等式给
$$
\boxed{
\|z(z-B)^{-1}\|
\le K_B'\exp[C_B(1+\log^+|z|^{-1})^{4/3}].
}
\tag{3.5}
$$

### 3.3 新共同半径只付一次

取固定 $\varepsilon>0$，$0<\delta\ll1$，共同圆周为
$$
|z_B|=|z_Y|=\varepsilon\delta^{\,2\kappa-2}.
\tag{3.6}
$$
由 (3.4)，$Y$ 圆周成本恰为 $\exp(C_\varepsilon\delta^{-2})$。
(3.5) 的成本只是
$\exp[C(1+\log\delta^{-1})^{4/3}]$，可吸入同一上界。

所以对在稍大闭双圆盘邻域全纯、边界模长 $\le M_F$ 的 $F$，
实际联合 Cauchy 演算给
$$
\boxed{
\|F(B,Y)\|\le K M_F\exp(C_\varepsilon\delta^{-2}).
}
\tag{3.7}
$$
圆周长度消去预解式的逆半径。
常数与 $F,\delta$ 及后续选位数无关。
后面的整个逆乘积共同求值一次；不按各个位重复支付 (3.7)。

## 4. 同一核上的准确线性逆

选中位满足 $\delta\le|a_j|$ 及 (1.3) 时，置
$$
\tau_j=\frac{c_j}{2a_j},\qquad
L_j=8a_jX+4c_jI=8a_j(X+\tau_jI).
\tag{4.1}
$$
有
$$
|\tau_j|^2\ge\frac{c_0^2}{4}\delta^{\,2\kappa-2}.
\tag{4.2}
$$
取固定
$$
0<\varepsilon<c_0^2/64.
$$
在 (3.6) 的两倍闭圆盘内，
$$
|z_B-z_Y-\tau_j^2|
\ge c_*\delta^{\,2\kappa-2}
\tag{4.3}
$$
对某个固定 $c_*>0$ 成立。
因此对 $r$ 元位集 $F$，
$$
G_F(z_B,z_Y)
=\prod_{j\in F}(z_B-z_Y-\tau_j^2)^{-1}
$$
在同一邻域全纯，且
$$
|G_F|\le(c_*^{-1}\delta^{-(2\kappa-2)})^r.
$$

定义 $M$ 上的实际有界算子
$$
\boxed{
\mathfrak R_F
=
\left(\prod_{j\in F}(8a_j)^{-1}\right)
\left(\prod_{j\in F}(X_M-\tau_jI)\right)
G_F(B,Y)|_M.
}
\tag{4.4}
$$
所有因子保持同一个 $M$ 并交换。
由 (2.5)，
$$
(X_M+\tau_j)(X_M-\tau_j)
=(B-Y-\tau_j^2)|_M.
$$
故得到精确核内恒等式
$$
\boxed{
\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M.
}
\tag{4.5}
$$
它不使用形式除法，也不声称 $L_j^{-1}$ 是原全空间的有界算子。

后面所选位有 $\max_F|\tau_j|\to0$。
由 (3.7) 与 (4.4)，存在固定 $K,C_M$ 使
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K\delta^{-2}+(2\kappa-1)r\log(\delta^{-1})
+C_Mr+C.
}
\tag{4.6}
$$
分母乘积的高额实际预解成本只出现一次。
分子是 $X_M$ 的 $r$ 次多项式；它仍保持 $M$ 及全部自然幂域，
并且其高阶输入 jets 由 (2.4) 直接控制。

## 5. 任意跨度的真实高位误差，包括 $B$

本节明确支付新的 $B$，不把一般 $\mathcal G$ 元素都当成有相同高位预算。

设 $F$ 为任意有限位集，$m=\min F\ge1$，
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
\gamma_F=\operatorname{Ad}J_F,\qquad
\sigma_j=(-1)^{1_{j\in F}}.
$$
定义
$$
\widehat R_j=V(\sigma_jt_jN_j),
$$
$$
\widehat X=X+\sum_{j\in F}a_j(\widehat R_j-R_j),
$$
$$
\widehat Y=\sum_jc_j(\widehat R_j-I),\qquad
\widehat B=\sum_ja_j^2(\widehat R_j-I)^2.
\tag{5.1}
$$
带帽的有界差与全部系数都在 $\mathcal A$ 中，完整交换 $X$。

### 5.1 完整导子壳

记 $\delta_XD=[X,D]$，采用 R260 的真实完整域定义。
实际串展开
$$
N_j
=E_j+\sum_{\ell>j}
(\eta_j\cdots\eta_{\ell-1})
E_j^*\cdots E_{\ell-1}^*E_\ell
$$
说明
$\gamma_FN_j-\sigma_jN_j$ 的非零差壳只从 $\ell\ge m$ 起；
同位纯项已经由 $\sigma_j$ 准确吸收。
每个差壳范数至多 $2\eta_{\ell-1}$。
固定的第 $\ell$ 壳与原完整 first 尾 $k>\ell$ 交换，
因此其所有真实 $\delta_X$ 导数可用有界头 $H_\ell$ 计算，
$$
2\|H_\ell\|\le C_1+C_2\|a\|_2\sqrt{\ell+1}.
$$
即使首个交换子已不是局部矩阵，$H_\ell$ 仍与同一闭尾交换，
所以这个等式逐阶成立。

在真实导子 Banach 代数范数
$$
\|D\|_{\delta_X}
=\sum_{s\ge0}\frac{\|\delta_X^sD\|}{s!}
$$
中，壳成本不超过
$2\eta_{\ell-1}e^{C_1+C_2\|a\|_2\sqrt{\ell+1}}$。
按壳求和给出与 $j,F,\max F$ 无关的
$Ce^{-385\,16^{m-1}}$ 上界。
这些范数收敛同时给完整保域导数；其闭尾/弱核心机制正是 R260 的原论证。

带帽有理逆与 $X$ 完整交换且范数统一有界。
对足够大 $m$，实际逆差可在同一个导子代数内用 Neumann 级数展开。
因此
$\gamma_FR_j-\widehat R_j$ 具有同一统一导子预算。
对 $Y$ 用 $\sum|c_j|<\infty$ 求和；
对 $B$ 用
$$
(\gamma_FR_j-I)^2-(\widehat R_j-I)^2
$$
的有序乘积差及 $\sum|a_j|^2<\infty$ 求和。
R260 同时支付非可和 first 的加权差。
结果为
$$
\boxed{
\|\delta_X^s E_X\|
+\|\delta_X^s E_Y\|
+\|\delta_X^s E_B\|
\le s!\epsilon_m,
\quad
\epsilon_m\le C e^{-385\,16^{m-1}},
}
\tag{5.2}
$$
其中
$$
E_X=\gamma_FX-\widehat X,\quad
E_Y=\gamma_FY-\widehat Y,\quad
E_B=\gamma_FB-\widehat B.
$$
全部误差及导数保持 $\mathcal D_\infty$。

$J_F$ 也保持 $\mathcal D_\infty$。
其实际有限支撑足以用完整闭尾交换与有限有界头扰动证明域保持；
只为域使用最大支撑，不让其进入 (5.2) 的范数预算。

### 5.2 $B$ 的符号差本身是真进位余项

准确的有理恒等式为
$$
V(-z)-V(z)=\frac{4z}{1-z^2},
$$
$$
(V(-z)-I)^2-(V(z)-I)^2
=\frac{16z^3}{(1-z^2)^2}.
\tag{5.3}
$$
因而
$$
\boxed{
\widehat B-B
=\sum_{j\in F}16a_j^2(t_jN_j)^3
(I-t_j^2N_j^2)^{-2}.
}
\tag{5.4}
$$
由 $N_j^3=\eta_jN_jN_{j+1}$，
$$
\|\widehat B-B\|\le C\eta_m\sum_{j\in F}|a_j|^2.
\tag{5.5}
$$
这解释了 $B$ 不贡献 Boolean 一次项。
同样，$\widehat X-X$ 与 $\widehat Y-Y$ 分别等于
$$
4\sum_{j\in F}a_jt_jN_j,\qquad
4\sum_{j\in F}c_jt_jN_j
$$
加上同样有真实 $\eta_m$ 因子的有界误差。

## 6. 选位与全部所需自然 jets

由 (1.1)，选固定 $b_a>0$ 及无穷尺度 $N$，使
$$
\rho_N\ge b_a/N.
$$
从最大的 $N$ 个实际幅度位中，
删掉幅度排序前 $\lfloor N/4\rfloor$ 项，
再删掉物理位置小于 $\lfloor N/4\rfloor$ 的位。
至少留下 $N/2$ 项；取恰有
$$
Q_N=\lfloor N/2\rfloor
$$
项的集合 $I_N$。
置
$$
m_N=\lfloor N/4\rfloor,\qquad \delta_N=b_a/N.
$$
则
$$
\boxed{
\min I_N\ge m_N,\qquad
\delta_N\le|a_j|\le4B_a/N\quad(j\in I_N).
}
\tag{6.1}
$$
不限制最大物理位；充分大 $N$ 后 (1.3) 对全部选中位成立。

取一个稍后固定的小 $c>0$，令
$$
r=r_N=\lceil\sqrt{N/c}\rceil.
\tag{6.2}
$$
充分大时 $r\le Q_N$。
对每个 $r$ 元子集 $F\subset I_N$，
$$
\sum_F|a_j|\le4B_ar/N,\qquad
\sum_F|c_j|\le C_0(4B_a/N)^{\kappa-1}\sum_F|a_j|.
\tag{6.3}
$$
两者都趋零，故带帽 first 的有界差统一有界。

对 $f_F=\mathfrak R_Ff\in M$，
$$
\|X^kf_F\|\le B_M^k\|f_F\|\qquad(k\ge0).
$$
真实恒等式
$$
X^kJ_Ff_F
=J_F(X+\widehat X-X+E_X)^kf_F
$$
与 (5.2) 给：存在固定 $R_{M,c}$，充分大 $N$ 时
$$
\boxed{
\|X^kJ_Ff_F\|\le2R_{M,c}^k\|f_F\|,
\qquad0\le k\le4r.
}
\tag{6.4}
$$

这里的非交换词支付如下。
逐字使用 $XD=DX+\delta_XD$ 将 $X$ 移到右侧；
含一个基本误差的词始终保留某个误差导数。
$k$ 个 $X$、$\ell$ 个有界字母至多给 $(\ell+1)^k$ 种去处，
导数阶数 $s_i$ 满足 $\prod s_i!\le k!$。
当 $k\le4r,\ell=O(r)$ 时总成本
$\epsilon_{m_N}e^{Cr\log(r+2)}$。
所有字母及导数保 $\mathcal D_\infty$，故这是真实域等式。
不把 $X$ 当作全空间有界算子。

对任意固定物理头 $h$，
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j
$$
与 $X$ 相差固定有界交换子，因而 (6.4) 也给相同阶数的
$Z_h$ jets，常数可依赖固定 $h$。

## 7. 真实反射幂与正确 Boolean 一次项

令
$$
\widehat T=\widehat X^2+\widehat Y-\widehat B,\qquad
A_F=\widehat T-T.
$$
它们是 $\mathcal A$ 系数的 $X$ 多项式，
在 $\mathcal D_\infty$ 上完整交换；
$A_F$ 保持 $M$，其在 $M$ 上有界。

按 (5.2) 展开 $(\gamma_FT)^r-\widehat T^r$，
每个词至少含一个基本误差，
$X$ 字母总数至多 $2r$，其他字母数 $O(r)$。
§6 的正规排序给
$$
\|[(\gamma_FT)^r-\widehat T^r]f_F\|
\le\epsilon_{m_N}e^{Cr\log(r+2)}\|f_F\|.
\tag{7.1}
$$
因 $Tf_F=0$ 且 $A_F$ 保持 $M$，
$$
\widehat T^rf_F=A_F^rf_F.
$$

在 $M$ 上，用 (5.3)--(5.5) 将 $A_F$ 换成
$$
\widetilde A_F
=
8X\sum_{j\in F}a_jt_jN_j
+16\left(\sum_{j\in F}a_jt_jN_j\right)^2
+4\sum_{j\in F}c_jt_jN_j.
\tag{7.2}
$$
替换误差 $\le C_M\eta_{m_N}$，
两者在 $M$ 上范数统一有界。
这是在原核内使用 $X_M$，并非全 $H$ 上的有界断言。

(7.2) 无零次项，其关于 $N_j$ 的准确一次系数为
$$
t_j(8a_jX+4c_j)=t_jL_j.
$$
$r$ 个正次因子、$r$ 个变量，模全部 $N_j^2$ 后只剩
$$
\boxed{
\widetilde A_F^r
\equiv r!t_FN_F\prod_{j\in F}L_j
\pmod{(N_j^2:j\in F)},
}
\tag{7.3}
$$
其中 $N_F=\prod_FN_j$、$t_F=\prod_Ft_j$。
每个弃项真含 $N_j^2=\eta_jN_{j+1}$。
由 (6.3) 和固定 $X_M$ 范数，原多项式全部系数绝对范数和至多 $C_M^r$，
所以重复位余项确实为 $\eta_{m_N}C_M^r$。

采用左反射顺序
$$
T^rJ_Ff_F=J_F(\gamma_FT)^rf_F.
$$
先在 $M$ 内用 (4.5) 消去整个有限差乘积，
再施 $J_F$。
由 $J_jE_j=-E_j$ 及
$\|N_F-\prod_FE_j\|\le r\eta_{m_N}$，
得到
$$
T^rJ_F\mathfrak R_Ff
=(-1)^rr!t_F\prod_{j\in F}E_jf+\mathcal E_Ff,
\tag{7.4}
$$
其中
$$
\|\mathcal E_Ff\|
\le
\epsilon_{m_N}e^{Cr\log(r+2)}
\|\mathfrak R_F\|\|f\|
+r!|t_F|r\eta_{m_N}\|f\|.
\tag{7.5}
$$
没有把随 $F$ 变化的逆移过反射，也没有假设 $J_FM\subset M$。

## 8. 同一个核上的共同平均与非零弱极限

令
$$
\mathcal V_N=
(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F:M\to H.
\tag{8.1}
$$
其像在 $\mathcal D_\infty$。
记
$$
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|,
\qquad
L_b=\max(1,\sup_j|t_j|^{-1}).
$$
则 $\|\mathcal V_N\|\le A_N$。
(4.6) 和 $\delta_N=b_a/N$ 给
$$
\boxed{
\log A_N\le K_0N^2+K_1r\log N+C_Mr+C.
}
\tag{8.2}
$$
常数 $K_0,K_1$ 与 $N,r,F$ 无关。

令
$$
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
将 (7.4) 求和，纯平方零关系给
$$
\|T^r\mathcal V_Nf-C_{I_N}^rf\|
\le
\left[
\epsilon_{m_N}e^{Cr\log(r+2)}A_N
+2^rr\eta_{m_N}
\right]\|f\|.
\tag{8.3}
$$
由 $m_N\asymp N$、(8.2)，右侧趋零。

原提升矩阵的范数公式给
$$
\|C_{I_N}^r\|\le(1+1/Q_N)^r\to1.
$$
对两个固定有限柱，充分大 $N$ 后选位全在其外，
矩阵元准确为 $(Q_N)_r/Q_N^r$ 乘原内积。
因 $Q_N\sim N/2$、$r^2\sim N/c$，
$$
\frac{(Q_N)_r}{Q_N^r}\longrightarrow e^{-1/c}>0.
$$
一致范数界将其延拓到全 $H$：
$$
\boxed{
C_{I_N}^r\rightharpoonup e^{-1/c}I,\qquad
T^r\mathcal V_Nf\rightharpoonup e^{-1/c}f.
}
\tag{8.4}
$$
这里只使用弱收敛，不要求未知核向量的尾速率。

§6 的 $Z_h$ jets 逐项求和还给
$$
\boxed{
\|Z_h^k\mathcal V_Nf\|
\le2A_NR_{h,M,c}^k\|f\|,
\qquad0\le k\le r.
}
\tag{8.5}
$$

## 9. 固定局部矩阵的真实 $A$ 因子与四次消去

固定支撑在前 $h$ 位的任意局部矩阵 $D_0$。
写
$$
s_h=a_*+\sum_{j<h}a_j,\qquad
L_h=\sum_{j<h}a_j(R_j-I).
$$
$L_h$ 是有限真解析和，准确有 $L_h=AU_h$、$U_h\in\mathcal A$。
同样，有限头
$$
Y_{<h}=\sum_{j<h}c_j(R_j-I),\qquad
B_{<h}=\sum_{j<h}a_j^2(R_j-I)^2
$$
具有真实有界 $A$ 因子。
没有对整个 $B$ 作除法。

原完整尾
$$
T_{\rm tail}=(Z_h+s_h)^2+Y_{\ge h}-B_{\ge h}
$$
与 $D_0$ 完整交换。
而
$$
T-T_{\rm tail}
=
2L_h(Z_h+s_h)+L_h^2+Y_{<h}-B_{<h}
=A W_h(Z_h),
$$
其中
$$
W_h(z)=B_{h,1}z+B_{h,0},\qquad B_{h,i}\in\mathcal A.
\tag{9.1}
$$
系数范数可依赖固定 $h$，不随 $N$ 改变。

$T_{\rm tail}$ 与 $AW_h(Z_h)$ 在共同深域上交换。
因此
$$
\operatorname{ad}_T^rD_0
=
\sum_{s=0}^r(-1)^s\binom rs
[AW_h(Z_h)]^{r-s}D_0[AW_h(Z_h)]^s
\tag{9.2}
$$
于 $\mathcal D_\infty$ 上成立。
$Z_h$ 与 $D_0$ 完整交换，且展开只消耗至多 $r$ 阶 $Z_h$ jets。
原真实四次幂界给
$$
\|A^{r-s}\|\|A^s\|
\le e^{-(5/6)r^4+105r^3}.
$$
保持 $A$ 在 $D_0$ 的两侧，不把它移过 $D_0$。
结合 (8.5)，得到
$$
\boxed{
\|(\operatorname{ad}_T^rD_0)\mathcal V_Nf\|
\le
2\|D_0\|A_N C_{h,M,c}^r
e^{-(5/6)r^4+105r^3}\|f\|.
}
\tag{9.3}
$$
没有声称这个高阶交换子在全 $H$ 有界。

由 (8.2)，
$$
\limsup_{N\to\infty}\frac{\log A_N}{r^4}
\le K_0c^2.
$$
选择一个固定 $c>0$，使 $K_0c^2<1/4$。
这个选择与局部测试 $D_0,h$ 无关。
于是 (9.3) 趋零。

## 10. 全部域上的配对排核

令
$$
\mathcal B(f,g)=\langle f,C_0g\rangle.
$$
$f,g\in M$、$\mathcal V_Nf$ 及所需局部测试都处于真实共同深域。
有限 Leibniz 展开和完整 $C_0$ 自伴性给
$$
\mathcal B(D_0T^r\mathcal V_Nf,g)
=(-1)^r
\mathcal B((\operatorname{ad}_T^rD_0)\mathcal V_Nf,g).
\tag{10.1}
$$
右侧由 (9.3) 趋零；
左侧由 (8.4) 趋于 $e^{-1/c}\mathcal B(D_0f,g)$。
所以
$$
\mathcal B(D_0f,g)=0
$$
对每个固定局部全矩阵 $D_0$ 及 $f,g\in M$ 成立。

原 Haar 局部全矩阵代数不可约，非零向量的局部轨道稠密。
若 $0\ne f\in M$，取 $g=f$，上式迫 $C_0f=0$，矛盾。
故 $M=0$。
由 (2.3)，$T$ 像稠密；
R176 的准确图循环判据遂给 (1.5)。

(1.1) 还迫 $a\notin\ell^1$：
在满足 $\rho_N\ge b_a/N$ 的尺度中取倍增子列，
对应不交区间 $[N/2,N]$ 的 $\ell^1$ 质量各有固定正下界。
因此 $X$ 真无界；正次数首一自然 $T$ 不可能为零算子。
若 (2.2) 的输出为零，循环指数向量的图核心会迫使 $T=0$，
矛盾。输出自动非零已证。

## 11. 一个直接的解析系数推论

设 $h$ 是零点邻域的标量解析芽，
$$
h(0)=2,\qquad h\not\equiv2.
$$
令辅助系数在充分高位为
$$
2a_j^2+c_j=a_j^2h(a_j).
$$
若 $h(z)-2=\gamma z^m+O(z^{m+1})$，
其中 $m\ge1$、$\gamma\ne0$，则
$$
c_j=\gamma a_j^{m+2}+O(|a_j|^{m+3}).
$$
因为 $a_j\to0$，(1.2)--(1.3) 在高位满足，$\kappa=m+2\ge3$。
有限低位可按同一式定义在解析域内，
或取满足 (1.2) 的任意值；它们不影响最终下界。
所以主定理覆盖该解析接近共振的族。

若有限低位需要另加任意辅助系数，也可以把其有限真解析乘子
并入 $B$ 的快项，并分别重付 §5 的有限低位尾壳；
本稿主定理为保持假设直接可核验，采用 (1.2) 的全局版本。

$h\equiv2$ 是 R270C 已闭的完全抵消情形。
$h(0)\ne2$ 则属于 R270 第一附录的原非共振范围。
本稿新增的正是 $h(0)=2$ 但在有限更高阶离开常值2的情形。

## 12. 准确边界

证明已经支付：新共同半径、一次真实联合逆、
同一闭核上的线性逆、$B$ 的任意跨度完整导子、
全部反射输入 jets、Boolean 重复位 carry、共同弱平均、
固定局部 $A$ 因子和完整自然域跨配对。

本稿只在 (1.1) 的临界弱 $\ell^1$ 主行上陈述主定理。
没有把新的预解半径本身当成任意主行的排核；
更慢主行或其他同阶辅助形状仍须重新核算其真实输入。
一般原始 $q(u)$ 的更快指数混合重根、独立慢多模式、
正常湮灭者、实际边界缺陷以及普通 ISP 均未因此完成。

## 依赖

R109 原四次幂；R176 真正自然域与指数图核心；
R260 任意跨度完整导子壳与正规排序接口；
R236 临界弱 $\ell^1$ 全重数附录的共同平均机制；
R270B 的真实局部二阶消去与 $B\in\mathcal G$；
R270C 的完全共振闭合仅用于区分范围，不用来推本稿的扰动结论。
