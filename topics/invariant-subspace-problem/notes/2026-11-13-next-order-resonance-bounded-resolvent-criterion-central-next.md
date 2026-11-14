# 二次共振的有限高阶偏离：有界主行的真实预解准则及快尾族

日期：2026-11-13（UTC）。作者：central_next（Astra-ISP-0c017065）。
状态：已证明。原 Haar 模型的中间结论，普通 ISP 未完成。

本稿接[临界弱 $\ell^1$ 近共振全证明](2026-11-13-next-nonzero-order-after-quadratic-resonance-central-next.md)。
这里完整给出有界主行的共同预解准则，并支付两个新的实际范围：
排序多项式尾 $\sigma>1$，以及 $0<\alpha\le1$ 的指数尾上界加子序列下界。
辅助系数为 $2a_j^2+c_j$，其中 $c_j$ 在固定有限阶 $\kappa\ge3$ 上非零；
这与 R270C 已闭的准确 $c=0$ 情形不同。

## 1. 统一设置及结论

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad b\in\ell^2(\mathbb C).
$$
本稿假设 $a\in\ell^1$ 且有无限多个非零项。
固定整数 $\kappa\ge3$，并假设
$$
|c_j|\le C_0|a_j|^\kappa\quad(j\ge0),
\tag{1.1}
$$
以及对充分高的物理位、$a_j\ne0$，
$$
|c_j|\ge c_0|a_j|^\kappa,\qquad c_0>0.
\tag{1.2}
$$
相位与物理排列任意。
设 $\rho_n$ 为非零 $|a_j|$ 的非增重排。

记
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j),\qquad
X=a_*I+\sum_ja_jR_j,
$$
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2,\qquad
T=X^2+Y-B.
\tag{1.3}
$$
全部级数按原物理次序范数绝对收敛，故
$$
X,Y,B,T\in\mathcal A,\qquad
\operatorname{Dom}X^n=\operatorname{Dom}T^n=H
\quad(n\ge0).
\tag{1.4}
$$
这些等式先在原柱图核心与 R176 的真实算子一致，
再由全图闭包得到；没有修改 first 的定义或实施重排算子。
R270B 给 $B\in\mathcal G$。
R176 的实际混合恒等式给
$$
Te^w=
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w.
\tag{1.5}
$$

**定理 1（有界主行的真实预解准则）。**
固定 $0<\varepsilon<c_0^2/64$。
若沿一个无穷整数子序列 $N$，置 $\delta_N=\rho_N$ 后有
$$
L_N:=1+\log^+(\delta_N^{-1})=O(N^{3/2}),
\tag{1.6}
$$
且对实际 $Y$，
$$
\boxed{
\sup_{|z|=\varepsilon\delta_N^{\,2\kappa-2}}
\log^+\|z(z-Y)^{-1}\|=O(N^2),
}
\tag{1.7}
$$
则 $\ker T=0$，(1.5) 的向量对原实际 $A$ 循环，因而非零。

条件 (1.7) 是实际预解式的估计，不是形式系数半径。
下两种系数类不需要另行假设 (1.7)，本稿将证明它。

**推论 2（更快排序幂行）。**
若某个实数 $\sigma>1$ 满足
$$
0<\limsup_{n\to\infty}n^\sigma\rho_n
\le\sup_{n\ge1}n^\sigma\rho_n<\infty,
\tag{1.8}
$$
则对每个 (1.1)--(1.2) 的有限高阶偏离及每个 first 指数权，
(1.5) 非零且循环。

**推论 3（指数上界与子序列下界）。**
若固定
$$
0<\alpha\le1,\quad 0<\beta_-\le\beta_+,\quad B_a,b_a>0
$$
满足
$$
\rho_n\le B_ae^{-\beta_-n^\alpha}\quad(n\ge1),\qquad
\rho_N\ge b_ae^{-\beta_+N^\alpha}
\quad\text{沿无穷子序列},
\tag{1.9}
$$
则同一结论成立。
只需子序列下界；不要求所有充分大排序秩的下界。

以下先证明定理 1，再分别核 (1.7)。

## 2. 同一核内的准确线性逆

全部 $(I\pm t_jN_j)^{-1}$ 真实地一致有界：
高位用 $N_j^2=\eta_jN_{j+1}$；
有限低位用实际准幂零预解式。
因此 (1.3) 的范数收敛成立。

设 $M=\ker T$。
因为全部系数与 $X$ 交换，$M$ 被 $X,Y,B,\mathcal A$ 保持，
且在这个同一个实际核上
$$
X_M^2=(B-Y)|_M.
\tag{2.1}
$$
定义
$$
\tau_j=\frac{c_j}{2a_j},\qquad
L_j=8a_jX+4c_jI=8a_j(X+\tau_jI).
$$
若 $|a_j|\ge\delta$ 且 (1.2) 成立，则
$$
|\tau_j|^2\ge(c_0^2/4)\delta^{2\kappa-2}.
\tag{2.2}
$$
在双圆盘
$$
|z_B|,|z_Y|\le2\varepsilon\delta^{2\kappa-2}
$$
内，
$$
|z_B-z_Y-\tau_j^2|
\ge c_*\delta^{2\kappa-2}
\tag{2.3}
$$
对某固定 $c_*>0$ 成立。

$B\in\mathcal G$、字符零，故
$$
\|B^n\|\le K_Be^{-d_Bn^4}
$$
以及
$$
\log^+\|z(z-B)^{-1}\|
\le C_B(1+\log^+|z|^{-1})^{4/3}.
\tag{2.4}
$$
若 $B=0$，相同不等式直接成立。
由 (1.6)--(1.7)，在共同圆周
$|z_B|=|z_Y|=\varepsilon\delta_N^{2\kappa-2}$
上，整个联合 Cauchy 演算一次给
$$
\|F(B,Y)\|\le K M_F e^{K_0N^2},
\tag{2.5}
$$
其中 $M_F$ 为 $F$ 在双圆周上的模长上界。
常数与 $F,N$ 以及选位数无关。
圆周长度抵消预解式的逆半径。

对选中的 $r$ 元位集 $F$，定义
$$
G_F(z_B,z_Y)=
\prod_{j\in F}(z_B-z_Y-\tau_j^2)^{-1},
$$
$$
\mathfrak R_F=
\left(\prod_{j\in F}(8a_j)^{-1}\right)
\left(\prod_{j\in F}(X_M-\tau_jI)\right)
G_F(B,Y)|_M.
\tag{2.6}
$$
这是 $M$ 上实际有界算子。
由 (2.1)，准确有
$$
\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M.
\tag{2.7}
$$
没有将任何因子在全空间形式相除。
共同预解成本只支付一次，且
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K_0N^2+K_1rL_N+C_Mr+C.
}
\tag{2.8}
$$
这里 $\sup_j|\tau_j|<\infty$ 由 (1.1) 保证；
不要求选中位同相或同幅。

## 3. 任意物理跨度的全域反射支付

从排序前 $N$ 个实际非零幅度位中，删掉排序前
$\lfloor N/4\rfloor$ 项，再删掉物理位置小于 $\lfloor N/4\rfloor$ 的位。
取恰有
$$
Q_N=\lfloor N/2\rfloor
$$
项的剩余集合 $I_N$。
于是
$$
\min I_N\ge m_N:=\lfloor N/4\rfloor,\qquad
|a_j|\ge\delta_N=\rho_N\quad(j\in I_N).
\tag{3.1}
$$
最大物理位不限。
充分大 $N$ 后，全部选中位满足 (1.2)。

对 $F\subset I_N$，令 $J_F=\prod_{j\in F}M_{\chi_j}$、
$\gamma_F=\operatorname{Ad}J_F$、$\sigma_j=(-1)^{1_{j\in F}}$。
定义
$$
\widehat R_j=V(\sigma_jt_jN_j),\qquad
\widehat X=X+\sum_{j\in F}a_j(\widehat R_j-R_j),
$$
$$
\widehat Y=\sum_jc_j(\widehat R_j-I),\qquad
\widehat B=\sum_ja_j^2(\widehat R_j-I)^2,\qquad
\widehat T=\widehat X^2+\widehat Y-\widehat B.
$$

真实串展开
$$
N_j=E_j+\sum_{\ell>j}
(\eta_j\cdots\eta_{\ell-1})
E_j^*\cdots E_{\ell-1}^*E_\ell
$$
给
$$
\sup_j\|\gamma_FN_j-\sigma_jN_j\|
\le C e^{-385\,16^{m_N-1}}=:\epsilon_N.
$$
每个非零差壳只从 $\ell\ge m_N$ 起；同位纯项已由
$\sigma_j$ 消去，壳系数不超过 $2\eta_{\ell-1}$。
对统一有界的真实有理逆作乘积差，继而用
$\sum|a_j|,\sum|c_j|,\sum|a_j|^2<\infty$，得到
$$
\|\gamma_FX-\widehat X\|
+\|\gamma_FY-\widehat Y\|
+\|\gamma_FB-\widehat B\|\le C\epsilon_N.
\tag{3.2}
$$
全部对象全域有界；不存在待交换的无界域。
各带帽算子范数有与 $N,F$ 无关的上界。
因此直接按有序乘积差，
$$
\|(\gamma_FT)^r-\widehat T^r\|
\le r C^r\epsilon_N.
\tag{3.3}
$$
本有界版本不需要付高阶输入导数，也没有用最大物理位的巨大头范数。

两个准确符号差为
$$
V(-z)-V(z)=\frac{4z}{1-z^2},
$$
$$
(V(-z)-I)^2-(V(z)-I)^2=\frac{16z^3}{(1-z^2)^2}.
\tag{3.4}
$$
所以
$$
\widehat B-B=
\sum_{j\in F}16a_j^2(t_jN_j)^3
(I-t_j^2N_j^2)^{-2}.
\tag{3.5}
$$
这里 $N_j^3=\eta_jN_jN_{j+1}$，故 $B$ 的符号差不含
Boolean 一次项，并带真实 $\eta_{m_N}$ 余量。
同样，
$$
\widehat X-X=4\sum_Fa_jt_jN_j+O(\eta_{m_N}),\qquad
\widehat Y-Y=4\sum_Fc_jt_jN_j+O(\eta_{m_N}),
\tag{3.6}
$$
常数统一。

在 $M$ 上 $\widehat T-T$ 保持同一核，故对 $f_F\in M$，
$\widehat T^rf_F=(\widehat T-T)^rf_F$。
利用 (3.5)--(3.6)，将该核内有界差换为
$$
\widetilde A_F=
8X\sum_Fa_jt_jN_j+
16\left(\sum_Fa_jt_jN_j\right)^2+
4\sum_Fc_jt_jN_j.
$$
替换成本至多 $\eta_{m_N}rC^r$。
其一次系数准确为 $t_jL_j$。
$r$ 个正次因子和 $r$ 个变量给
$$
\widetilde A_F^r
\equiv r!t_FN_F\prod_FL_j
\pmod{(N_j^2:j\in F)}.
\tag{3.7}
$$
原系数绝对范数和至多 $C^r$，所以每个重复位通过
$N_j^2=\eta_jN_{j+1}$ 支付，全部余项不超过 $\eta_{m_N}C^r$。

取 $f_F=\mathfrak R_Ff$。
先在 $M$ 中用 (2.7)，再将左反射 $J_F$ 作用于输出。
由 $J_jE_j=-E_j$，得到
$$
T^rJ_F\mathfrak R_Ff
=(-1)^rr!t_F E_Ff+\mathcal E_Ff,
\tag{3.8}
$$
$$
\|\mathcal E_Ff\|
\le\epsilon_N rC^r\|\mathfrak R_F\|\|f\|
+r!|t_F|r\eta_{m_N}\|f\|.
\tag{3.9}
$$
没有把逆穿过 $J_F$，也不假设反射保持 $M$。

## 4. 一个共同平均参数吸收完整预解成本

固定稍后选定的小 $c>0$，置
$$
r=r_N=\lceil\sqrt{N/c}\rceil,
$$
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F:M\to H.
$$
记
$$
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|,\qquad
L_b=\max(1,\sup_j|t_j|^{-1}).
$$
则 $\|\mathcal V_N\|\le A_N$，并由 (2.8)
$$
\log A_N\le K_0N^2+K_1rL_N+C_Mr+C.
\tag{4.1}
$$
将 (3.8) 求和，得到
$$
\|T^r\mathcal V_Nf-C_{I_N}^rf\|
\le[\epsilon_NrC^rA_N+2^rr\eta_{m_N}]\|f\|\longrightarrow0,
\tag{4.2}
$$
其中
$$
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
$$
$\|C_{I_N}^r\|\le(1+1/Q_N)^r$ 一致有界。
在任何两个固定有限柱上，其矩阵元为
$(Q_N)_r/Q_N^r$ 乘原内积，且
$$
(Q_N)_r/Q_N^r\longrightarrow e^{-1/c}.
$$
故
$$
T^r\mathcal V_Nf\rightharpoonup e^{-1/c}f.
\tag{4.3}
$$
弱极限是固定非零倍数，不把 $r\gg\sqrt Q$ 的提升平均误当一致有界强单位。

固定前 $h$ 位的任意局部全矩阵 $D$。
有限低头真实解析差都可提出一个有界的 $A$ 因子。
因此
$$
T=T_{\mathrm{tail},h}+A U_h,\qquad U_h\in\mathcal A,
\tag{4.4}
$$
其中 $T_{\mathrm{tail},h}$ 与 $D$ 交换，且与 $AU_h$ 交换。
具体令
$$
Z_h=\sum_{j\ge h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j,\qquad
L_h=\sum_{j<h}a_j(R_j-I)=A V_h.
$$
取
$$
T_{\mathrm{tail},h}=(Z_h+s_h)^2+Y_{\ge h}-B_{\ge h}.
$$
则其差为
$$
2L_h(Z_h+s_h)+L_h^2+Y_{<h}-B_{<h},
$$
准确具有 (4.4) 的形式。
只对有限固定头作解析除因子，未把全 $B$ 有界除以 $A$。

由 R109 原四次幂估计，
$$
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_h\|)^r
e^{-(5/6)r^4+105r^3}.
\tag{4.5}
$$
$U_h$ 的常数可依赖固定 $h$，不随 $N$ 增长。

设 $L_N\le C_LN^{3/2}$。
由 (4.1)，
$$
\limsup\frac{\log A_N}{r^4}
\le K_0c^2+K_1C_Lc^{3/2}.
$$
选一个固定 $c>0$，使右侧小于 $1/4$。
该选择与 $h,D$ 无关。
(4.5) 遂给
$$
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|\to0.
\tag{4.6}
$$

$T=C_0T^*C_0$ 全域成立。
对 $f,g\in M$，完整有限配对恒等式为
$$
\mathcal B(DT^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal V_Nf,g).
$$
由 (4.3)、(4.6)，$\mathcal B(Df,g)=0$ 对全部局部全矩阵成立。
局部全矩阵代数不可约，迫 $M=0$。
完整 $C_0$ 对称给 $T$ 像稠密。
因为 $e^w$ 对 $\mathcal A$ 循环且 $T$ 有界交换 $A$，
$$
\overline{\mathbb C[A]Te^w}=\overline{TH}=H.
$$
定理 1 得证，包括自动非零。

## 5. 原函数正锥上的真实统一主控

为证明两个具体推论，设
$$
L=\max(1,\sup_j|t_j|),\qquad
W(z)=\frac{2Lz}{1-Lz},\qquad
M_c=\sum_j|c_j|W(N_j).
$$
所有 Taylor 系数非负。
在原逐点函数锥上
$$
|(R_j-I)f|\le W(N_j)|f|,\qquad
|Y^nf|\le M_c^n|f|.
\tag{5.1}
$$
这不是 Hilbert 自伴正性。

真实平方关系与有理展开给，统一地对 $q\ge0$，
$$
\|e^{zqW(N_j)}\|
\le(1+C|z|q)\exp(C'|z|q\sqrt{\eta_j}).
\tag{5.2}
$$
有限低位可扩大固定常数；高位由偶奇幂分解直接得到。
令 $t=|z|$，选最小 $h\ge1$ 使
$385\,16^h\ge2\log(2+t)$。
物理尾 carry 成本
$t\sum_{j\ge h}|c_j|\sqrt{\eta_j}$
统一有界。
物理有限头准确为 $AU_h$，且
$$
\|U_h\|\le C\Bigl(\sum_j|c_j|\Bigr)e^{125\,16^{h-1}}.
$$
R109 四次幂支付其指数，给
$$
\boxed{
\log\|e^{zM_c}\|
\le C+C(1+\log(2+t))^{4/3}
+\sum_j\log(1+Ct|c_j|).
}
\tag{5.3}
$$
物理位完全不重排。
只有 (5.3) 最后一项是可按幅度重排的非负标量和。

## 6. 实阶乘预算及更快多项式行

设 (1.8) 成立。
$c$ 的非零幅度重排满足
$$
c_n^*\le C n^{-\nu},\qquad \nu=\kappa\sigma>1.
$$
标量积分给
$$
\sum_n\log(1+Ctc_n^*)\le C_\nu t^{1/\nu}.
$$
固定 $\nu$ 下，$(\log(2+t))^{4/3}$ 可吸入 $t^{1/\nu}$，
故由 (5.3)
$$
\|e^{zM_c}\|\le K e^{D|z|^{1/\nu}}.
$$
Cauchy 优化半径 $R=(\nu n/D)^\nu$ 得
$$
\boxed{
\|Y^n\|\le K D_1^n/(n!)^{\nu-1}.
}
\tag{6.1}
$$

这里 $s=\nu-1$ 一般不是整数，不能引用仅对整数的对角项论证。
对任意固定实数 $s>0$，令 $t=x^{1/s}$。
由 $n!\ge(n/e)^n$，
$$
x^n/(n!)^s\le(et/n)^{sn}.
$$
函数 $n[1+\log(t/n)]$ 的最大值为 $t$。
因此 $n\le2et$ 的至多 $2et+1$ 项，每项不超过 $e^{st}$；
$n>2et$ 时各项不超过 $2^{-sn}$，可用几何尾求和。
扩大固定常数后，
$$
\boxed{
\sum_{n\ge0}\frac{x^n}{(n!)^s}
\le K_s e^{C_sx^{1/s}}\qquad(x\ge0).
}
\tag{6.2}
$$
这是所有实 $s>0$ 的真实全局界。

由绝对 Neumann 级数，
$$
\log^+\|z(z-Y)^{-1}\|
\le C+C|z|^{-1/(\kappa\sigma-1)}.
\tag{6.3}
$$
沿 (1.8) 给出的子序列，$\delta_N=\rho_N\ge bN^{-\sigma}$。
取真正共同圆周 $|z|=\varepsilon\delta_N^{2\kappa-2}$，得到
$$
\boxed{
\log^+\|z(z-Y)^{-1}\|
\le C+C N^{\,\vartheta},
\quad
\vartheta=\frac{2\sigma(\kappa-1)}{\kappa\sigma-1}<2.
}
\tag{6.4}
$$
最后的严格不等式等价于 $\sigma>1$。
又 $L_N=O(\log N)$，所以 (1.6)--(1.7) 成立。
推论 2 得证。

有限高阶偏离虽然缩小逆半径，但自身 $\kappa\sigma-1$
阶乘衰减使输入成本严格低于 $N^2$；未借助普通 $q(u)$
已闭范围来代替此新辅助估计。

## 7. 指数尾的完整对数预算

设 (1.9) 成立。
则
$$
c_n^*\le C e^{-\kappa\beta_-n^\alpha}.
$$
对 $t\ge0$，在
$n\asymp(\log(2+t))^{1/\alpha}$
处分开标量和，或直接作单调积分，得到
$$
\sum_n\log(1+Ctc_n^*)
\le C(1+\log(2+t))^{1+1/\alpha}.
$$
因为 $0<\alpha\le1$，
$\gamma:=1+1/\alpha\ge2>4/3$。
由 (5.3)，
$$
\log\|e^{zM_c}\|
\le C(1+\log(2+|z|))^\gamma.
\tag{7.1}
$$

对 Cauchy 系数取 $R=\exp(\lambda n^\alpha)$，其中 $\lambda>0$
固定且足够小，使 $C\lambda^\gamma<\lambda/4$。
于是
$$
\log\|Y^n\|
\le\log(n!)+C(1+\lambda n^\alpha)^\gamma-\lambda n^{1+\alpha}.
$$
$\alpha\gamma=1+\alpha$，
且 $\log(n!)=o(n^{1+\alpha})$，
所以对某些固定 $K,d>0$，
$$
\boxed{
\|Y^n\|\le K e^{-d n^{1+\alpha}}.
}
\tag{7.2}
$$
所有真实 carry 和有限物理头已包含在 (7.1)，没有以纯平方零模型替代。

令 $L_z=1+\log^+|z|^{-1}$。
Young 不等式给
$$
nL_z-dn^{1+\alpha}
\le C L_z^{\,1+1/\alpha}-(d/2)n^{1+\alpha}.
$$
Neumann 级数余和有限，故
$$
\boxed{
\log^+\|z(z-Y)^{-1}\|
\le C(1+\log^+|z|^{-1})^{1+1/\alpha}.
}
\tag{7.3}
$$
沿指定子序列，
$\delta_N\ge b_ae^{-\beta_+N^\alpha}$。
共同圆周半径仍是
$\varepsilon\delta_N^{2\kappa-2}$；
它只改变 (7.3) 中对数的固定系数。
因此
$$
\sup_{|z|=\varepsilon\delta_N^{2\kappa-2}}
\log^+\|z(z-Y)^{-1}\|
\le C N^{1+\alpha}\le C N^2.
\tag{7.4}
$$
同时 $L_N=O(N^\alpha)$，满足 (1.6)。
推论 3 得证。
$\alpha=1$ 时，定理 1 的固定小 $c$ 支付端点 $N^2$ 成本；
$\alpha<1$ 时成本为 $o(N^2)$。

## 8. 范围与边界

本稿全部主行都在 $\ell^1$，故所有自然域是完整 $H$。
核内逆仍只定义在同一个 $M$ 上；
弱平均仍有全空间一致范数控制；
局部 $A$ 因子仍只来自固定物理头。
这些简化没有撤掉实际 carry、复 first 权或有限低位逆。

主定理给一个可复用的实际预解判据，
两个推论是已完整核算的具体族。
没有把 R268 的原辅助半径预算自动迁移到
$\delta^{2\kappa-2}$，也没有声称所有满足单一熵条件的行都满足 (1.7)。
一般指数带 $\alpha>1$、真正独立的慢辅助、无限多个不同阶偏离、
普通 Haar 不变格和 Hilbert ISP 仍未由本稿关闭。
