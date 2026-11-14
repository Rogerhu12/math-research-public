# 任意复 ℓ² 主行的近共振预解准则与实数偏离阶

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065。
状态：完整证明的统一加强。先行[弱ℓ¹稿](2026-11-13-next-nonzero-order-after-quadratic-resonance-central-next.md)与[可和主行稿](2026-11-13-next-order-resonance-bounded-resolvent-criterion-central-next.md)；本文独立核其自然域及一次联合成本后，去掉统一准则的主行ℓ¹限制，并允许实数偏离阶κ>2。普通 ISP 未完成。

## 1. 统一定理

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),
$$
假设 $a$ 有无限支撑。记非零幅度非增重排为 $\rho_n$。
固定实数 $\kappa>2$，并设
$$
|c_j|\le C_0|a_j|^\kappa\quad(j\ge0),
\tag{1.1}
$$
以及对充分大的物理位 $j$、$a_j\ne0$，
$$
|c_j|\ge c_0|a_j|^\kappa,\qquad c_0>0.
\tag{1.2}
$$
这里只比较绝对值，不定义复数 $a_j^\kappa$。特别 $a_j=0$ 时 $c_j=0$，且 $c\in\ell^1$。

令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
X=X_b,
$$
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2,\qquad
T=X^2+Y-B.
\tag{1.3}
$$
$X$ 为原倾斜闭 first，不能在非可和分支将它定义成范数收敛和。$Y,B\in\mathcal A$ 的和范数绝对收敛，$B\in\mathcal G$。

固定 $0<\varepsilon<c_0^2/64$。假设沿某个无穷整数子序列 $N$，以 $\delta_N=\rho_N$ 有
$$
L_N=1+\log^+(\delta_N^{-1})=O(N^{3/2}),
\tag{1.4}
$$
$$
\sup_{|z|=\varepsilon\delta_N^{\,2\kappa-2}}
\log^+\|z(z-Y)^{-1}\|=O(N^2).
\tag{1.5}
$$
(1.5) 是实际有界预解式的范数条件。

**定理。** 在这些假设下，
$$
\boxed{\ker T=0,\qquad
\overline{\operatorname{Ran}T}=H,}
$$
$$
\boxed{
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{1.6}
$$
$a$ 的相位、物理排列与是否ℓ¹均不受额外限制。

## 2. 原自然域、核与共同求值

[R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md) §§2–5、8、10 给
$$
\operatorname{Dom}T=\operatorname{Dom}X^2,\qquad
T=C_0T^*C_0.
$$
若 $M=\ker T$，则
$$
M\subset\mathcal D_\infty:=\bigcap_{n\ge0}\operatorname{Dom}X^n,
\qquad X_M=X|_M\in B(M).
\tag{2.1}
$$
所有有界 $\mathcal A$ 系数保持 $M$、保持全部自然幂域并完整交换 $X$。在同一个核上准确有
$$
X_M^2=(B-Y)|_M.
\tag{2.2}
$$

R270B 的局部二阶消去给 $B\in\mathcal G$、字符零，故
$$
\log^+\|z(z-B)^{-1}\|
\le C_B(1+\log^+|z|^{-1})^{4/3}.
$$
若 $B=0$，直接用 $z(z-B)^{-1}=I$。
由 (1.4)–(1.5)，对在双闭圆盘
$|z_B|,|z_Y|\le\varepsilon\delta_N^{2\kappa-2}$ 的邻域全纯、边界模不超过 $M_F$ 的函数 $F$，
$$
\boxed{\|F(B,Y)\|\le C M_F e^{K_0N^2}.}
\tag{2.3}
$$
这是整个 $F$ 的一次联合 Cauchy 求值；两个圆周长度分别抵消预解式的逆半径。$K_0$ 不依赖后续选位数，也不依赖后面才选的平均参数。

若选中位 $j$ 满足 $|a_j|\ge\delta_N$ 及 (1.2)，令
$$
\tau_j=\frac{c_j}{2a_j},\qquad
L_j=8a_j(X+\tau_jI).
$$
在两倍双圆盘内，
$$
|z_B-z_Y-\tau_j^2|\ge c_*\delta_N^{2\kappa-2}
\tag{2.4}
$$
对固定 $c_*>0$ 成立。
对 $r$ 元位集 $F$，共同求值整个乘积
$$
G_F(z_B,z_Y)=\prod_{j\in F}(z_B-z_Y-\tau_j^2)^{-1}.
$$
在 $M$ 上定义
$$
\mathfrak R_F=
\left(\prod_{j\in F}(8a_j)^{-1}\right)
\left(\prod_{j\in F}(X_M-\tau_jI)\right)
G_F(B,Y)|_M.
\tag{2.5}
$$
它保持同一 $M$。由 (2.2) 得
$$
\boxed{\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M.}
\tag{2.6}
$$
不声称 $L_j^{-1}$ 在原全空间有界。对下节选位，
$$
\log^+\|\mathfrak R_F\|
\le K_0N^2+(2\kappa-1)rL_N+C_Mr+C.
\tag{2.7}
$$
成本 $K_0N^2$ 只出现一次；分母乘积的模长及分子多项式另外支付 $O(rL_N+r)$。

## 3. ℓ² 选位已足够：不用主行ℓ¹

从最大的 $N$ 个实际非零幅度位中，删去排序前 $\lfloor N/4\rfloor$ 项，再删去物理位置小于 $m_N=\lfloor N/4\rfloor$ 的项。剩余至少 $N/2$ 项；取恰有 $Q_N=\lfloor N/2\rfloor$ 项的 $I_N$。
若 $g=\|a\|_2$，则
$$
\min I_N\ge m_N,\qquad
\delta_N\le|a_j|\le\frac{2g}{\sqrt N}
\quad(j\in I_N).
\tag{3.1}
$$
最大物理位不限。

固定稍后选定的小 $\theta>0$，令
$$
r=\left\lceil\sqrt{N/\theta}\right\rceil.
$$
对全部 $r$ 元 $F\subset I_N$，
$$
\sum_{j\in F}|a_j|
\le\frac{2gr}{\sqrt N}=O_\theta(1),
\tag{3.2}
$$
$$
\sum_{j\in F}|a_j|^2=O_\theta(N^{-1/2}),\qquad
\sum_{j\in F}|c_j|
\le C_0(2g/\sqrt N)^{\kappa-1}\sum_F|a_j|
\longrightarrow0.
\tag{3.3}
$$
尤其 $\max_F|\tau_j|\to0$，从而 (2.7) 中的分子预算成立。

原弱ℓ¹稿使用了更强的 $\sum_F|a_j|\to0$，但其后续自然幂估计实际只需 (3.2) 的统一有界性。常数允许依赖这个固定的 $\theta$；它们不随 $N$ 增长。

## 4. 完整域反射、真实三次余项与输入 jets

令 $J_F=\prod_{j\in F}M_{\chi_j}$、$\gamma_F=\operatorname{Ad}J_F$、$\sigma_j=(-1)^{1_{j\in F}}$，并定义
$$
\widehat R_j=V(\sigma_jt_jN_j),\quad
\widehat X=X+\sum_{j\in F}a_j(\widehat R_j-R_j),
$$
$$
\widehat Y=\sum_jc_j(\widehat R_j-I),\qquad
\widehat B=\sum_ja_j^2(\widehat R_j-I)^2.
$$
[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) §§2–5 的完整域壳层给
$$
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\|\delta_X^s(\gamma_FY-\widehat Y)\|
+\|\delta_X^s(\gamma_FB-\widehat B)\|
\le s!\epsilon_N,
$$
$$
\epsilon_N\le C e^{-385\,16^{m_N-1}}.
\tag{4.1}
$$
原始非零差壳只从最高位 $\ell\ge m_N$ 起；该壳实际局部于前 $\ell+1$ 位。与闭尾交换后，全部导数成本不超过
$e^{C+Cg\sqrt{\ell+1}}$。
对 $X$ 的非可和系数按最高位收集壳，Cauchy–Schwarz 及真实权比给每壳 $C\eta_{\ell-1}$，不使用 $\sum|a_j|$。
$Y$ 用 $c\in\ell^1$，$B$ 用 $a^2\in\ell^1$ 和有序平方差。
真实导子 Banach 代数的完备性支付所有自然域保持与有理逆。
全部常数不含 $\max F$。

$J_F$ 双向保持 $\mathcal D_\infty$。准确有
$$
\widehat B-B=
\sum_{j\in F}16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2}.
\tag{4.2}
$$
因此其符号差没有 Boolean 一次项；$N_j^3=\eta_jN_jN_{j+1}$ 支付余项。另有
$$
\widehat X-X=4\sum_Fa_jt_jN_j+O_\theta(\eta_{m_N}),\qquad
\widehat Y-Y=4\sum_Fc_jt_jN_j+O_\theta(\eta_{m_N}).
\tag{4.3}
$$
(3.2) 使 $\widehat X-X$ 在全空间统一有界。

对 $f_F=\mathfrak R_Ff\in M$，由 (2.1)
$\|X^kf_F\|\le\|X_M\|^k\|f_F\|$。将
$X^kJ_Ff_F=J_F(\gamma_FX)^kf_F$
按 $XD=DX+\delta_XD$ 正规排序。
无误差项由 (3.2) 控制；任何误差词保留一个 (4.1) 的误差导数。
至多 $O(r)$ 字母、至多 $4r$ 个 $X$ 的排序成本为
$\epsilon_Ne^{C_\theta r\log(r+2)}$，因为导数阶乘乘积不超过 $(4r)!$。
于是有固定 $R_{M,\theta}$，使充分大 $N$ 时
$$
\boxed{
\|X^kJ_Ff_F\|
\le2R_{M,\theta}^k\|f_F\|,
\qquad 0\le k\le4r.
}
\tag{4.4}
$$
对任一固定物理头 $h$，
$Z_h=X-a_*I-\sum_{j<h}a_jR_j$
具有相同阶数的 jets，常数可依赖固定 $h$。
没有把 $X$ 当成全空间有界算子。

## 5. 正确一次系数与共同弱平均

置 $\widehat T=\widehat X^2+\widehat Y-\widehat B$。
(4.1)、(4.4) 给
$$
\|[(\gamma_FT)^r-\widehat T^r]f_F\|
\le\epsilon_Ne^{C_\theta r\log(r+2)}\|f_F\|.
$$
在同一 $M$ 上，$\widehat T-T$ 保持 $M$，且可由 (4.2)–(4.3) 换成
$$
\widetilde A_F=
8X\sum_Fa_jt_jN_j+
16\left(\sum_Fa_jt_jN_j\right)^2+
4\sum_Fc_jt_jN_j.
$$
替换误差有真实 $\eta_{m_N}$ 因子。其全部系数绝对范数和在 $M$ 上一致受控，依赖固定 $\theta$ 是允许的。

该多项式无零次项、关于选中 $N_j$ 的一次系数准确为 $t_jL_j$。所以
$$
\widetilde A_F^r
\equiv r!t_FN_F\prod_FL_j
\pmod{(N_j^2:j\in F)}.
$$
每个弃项至少重复一位，通过 $N_j^2=\eta_jN_{j+1}$ 支付，全部弃项不超过 $\eta_{m_N}C_{M,\theta}^r$。
左反射的正确顺序为
$$
T^rJ_Ff_F=J_F(\gamma_FT)^rf_F.
$$
先在 $M$ 内用 (2.6)，再施 $J_F$；从不将 $\mathfrak R_F$ 移过反射。因此
$$
T^rJ_F\mathfrak R_Ff
=(-1)^rr!t_FE_Ff+\mathcal E_Ff,
\tag{5.1}
$$
$$
\|\mathcal E_Ff\|
\le\epsilon_Ne^{C_\theta r\log(r+2)}
\|\mathfrak R_F\|\|f\|
+r!|t_F|r\eta_{m_N}\|f\|.
$$

令
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F:M\longrightarrow H.
$$
其像在 $\mathcal D_\infty$。若
$$
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|,
\quad L_b=\max(1,\sup_j|t_j|^{-1}),
$$
则 $\|\mathcal V_N\|\le A_N$，且
$$
\log A_N\le K_0N^2+K_1rL_N+C_Mr+C.
\tag{5.2}
$$
组合数已由 $\binom{Q_N}{r}\le Q_N^r/r!$ 支付。
对 $C_{I_N}=(2/Q_N)\sum_{j\in I_N}E_j$，(5.1) 求和给
$$
\|T^r\mathcal V_Nf-C_{I_N}^rf\|
\le[\epsilon_Ne^{C_\theta r\log(r+2)}A_N+
2^rr\eta_{m_N}]\|f\|\to0.
\tag{5.3}
$$
这里 $m_N\asymp N$，超快物理进位压过全部 $O(N^2+rL_N+r\log r)$ 成本。

纯提升有 $\|C_{I_N}^r\|\le(1+1/Q_N)^r$；在固定有限柱上，其矩阵元系数准确为 $(Q_N)_r/Q_N^r$。
$Q_N\sim N/2$、$r^2\sim N/\theta$ 给
$$
\boxed{T^r\mathcal V_Nf\rightharpoonup e^{-1/\theta}f.}
\tag{5.4}
$$
极限是固定非零倍数。没有使用未知核向量的尾速率，也没有将其改称强收敛。

## 6. 固定局部 A 因子及全部深域配对

固定前 $h$ 位的任意局部全矩阵 $D_0$。记
$$
s_h=a_*+\sum_{j<h}a_j,\qquad
L_h=\sum_{j<h}a_j(R_j-I)=AU_h,
$$
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j.
$$
这里只出现有限标量和。
闭尾
$$
T_{{\rm tail},h}=(Z_h+s_h)^2+Y_{\ge h}-B_{\ge h}
$$
与 $D_0$ 完整交换。而
$$
T-T_{{\rm tail},h}
=2L_h(Z_h+s_h)+L_h^2+Y_{<h}-B_{<h}
=A W_h(Z_h),
$$
其中 $W_h$ 是一次多项式、系数在 $\mathcal A$。只对有限固定头提出真实有界 $A$ 因子，没有给整个 $B$ 除以 $A$。

在 $\mathcal D_\infty$ 上，
$$
\operatorname{ad}_T^rD_0
=\sum_{s=0}^r(-1)^s\binom rs
[AW_h(Z_h)]^{r-s}D_0[AW_h(Z_h)]^s.
$$
$Z_h$ 与 $D_0$ 交换。展开只消耗至多 $r$ 阶 $Z_h$ jets。
[R109](../results/R109-invariant-restriction-exact-quartic-type.md) 给
$$
\|A^{r-s}\|\|A^s\|
\le e^{-(5/6)r^4+105r^3}.
$$
保持 $A$ 在 $D_0$ 两侧，(4.4) 逐项求和遂给
$$
\|(\operatorname{ad}_T^rD_0)\mathcal V_Nf\|
\le 2\|D_0\| A_N C_{h,M,\theta}^r
e^{-(5/6)r^4+105r^3}\|f\|.
\tag{6.1}
$$
不声称此交换子在全 $H$ 有界。

由 $L_N\le C_LN^{3/2}$ 和 (5.2)，
$$
\limsup\frac{\log A_N}{r^4}
\le K_0\theta^2+K_1C_L\theta^{3/2}.
$$
先选固定 $\theta>0$ 使右侧小于 $1/4$；选择不依赖局部测试 $h,D_0$。
虽然 $C_{h,M,\theta}$ 可以依赖 $\theta$，其 $r$ 次成本除以 $r^4$ 仍趋零。故 (6.1) 趋零。

对 $f,g\in M$，全部有限词都在 $\mathcal D_\infty$ 上，$C_0$ 对称及有限 Leibniz 展开给
$$
\mathcal B(D_0T^r\mathcal V_Nf,g)
=(-1)^r
\mathcal B((\operatorname{ad}_T^rD_0)\mathcal V_Nf,g).
$$
结合 (5.4)、(6.1)，得 $\mathcal B(D_0f,g)=0$ 对所有局部全矩阵成立。
局部矩阵代数不可约，非零向量的局部轨道稠密，故 $M=0$。
这未假设 $C_0M=M$。
完整 $C_0$ 自伴给稠密值域；R176 的循环域向量图核心用于 $e^w$，由准确 Bell 恒等式得到 (1.6)。

## 7. 实数 κ>2 的三类具体支付

### 7.1 所有 σ≥1 的排序幂行

假设某个实数 $\sigma\ge1$ 满足
$$
0<\limsup_{n\to\infty}n^\sigma\rho_n
\le\sup_{n\ge1}n^\sigma\rho_n<\infty.
$$
$\sigma=1$ 是临界弱ℓ¹类；$\sigma>1$ 自动主行可和。

令 $\nu=\kappa\sigma>2$。函数非负锥上的实际主控为
$$
M_c=\sum_j|c_j|\frac{2L N_j}{1-LN_j},
\qquad L=\max(1,\sup|t_j|).
$$
既有物理头/真实尾证明只使用标量上界
$c_n^*\le Cn^{-\nu}$，因而对实数 $\nu>1$ 同样给
$$
\|e^{zM_c}\|\le K e^{D|z|^{1/\nu}},
\qquad
\|Y^n\|\le K D_1^n/(n!)^{\nu-1}.
\tag{7.1}
$$
这里 Cauchy 取半径 $(\nu n/D)^\nu$，只用 $(n!)^\nu\le n^{\nu n}$，没有要求 $\nu$ 整数。

对任意实数 $s>0$、$x\ge0$，令 $t=x^{1/s}$。由 $n!\ge(n/e)^n$，前 $2et$ 项每项不超过 $e^{st}$，其后由 $2^{-sn}$ 的几何尾控制；扩大固定常数得
$$
\sum_{n\ge0}\frac{x^n}{(n!)^s}
\le K_s e^{C_sx^{1/s}}.
\tag{7.2}
$$
所以实际 Neumann 级数给
$$
\log^+\|z(z-Y)^{-1}\|
\le C+C|z|^{-1/(\kappa\sigma-1)}.
$$
沿 $\rho_N\ge bN^{-\sigma}$ 的子序列，在 (1.5) 的真实半径上有
$$
\log^+\|z(z-Y)^{-1}\|
\le C+C N^{\,2\sigma(\kappa-1)/(\kappa\sigma-1)}.
\tag{7.3}
$$
指数在 $\sigma=1$ 时等于2，在 $\sigma>1$ 时严格小于2；且 $L_N=O(\log N)$。统一定理因此覆盖全部 $\sigma\ge1$，并允许任意实数 $\kappa>2$。

### 7.2 0<α≤1 的指数上界及子序列下界

若
$$
\rho_n\le B_ae^{-\beta_-n^\alpha},\qquad
\rho_N\ge b_ae^{-\beta_+N^\alpha}
\quad\text{沿无穷子序列},
$$
其中 $0<\alpha\le1$、$0<\beta_-\le\beta_+$，则同一正主控的真实头/尾估计给
$$
\log\|e^{zM_c}\|\le C(1+\log(2+|z|))^{1+1/\alpha}.
$$
固定实数 $\kappa$ 只改变标量尾中的常数。
Cauchy 半径 $e^{\lambda n^\alpha}$ 与真实 Neumann 级数遂给
$$
\|Y^n\|\le K e^{-dn^{1+\alpha}},\qquad
\log^+\|z(z-Y)^{-1}\|
\le C(1+\log^+|z|^{-1})^{1+1/\alpha}.
$$
在 (1.5) 的半径上，后者为 $O(N^{1+\alpha})=O(N^2)$；且 $L_N=O(N^\alpha)$。定理适用。

上述实际正主控的低物理头始终保真 $A$ 因子，指数成本为 $O(\log^{4/3}(2+|z|))$；真实尾 carry 已付，不将物理位重排为一个算子置换。这两项原文证明见先行两源及 [R236分阶预算](../results/R236-appendix-factorial-cumulant-powers-and-joint-resolvent-budgets.md)。

### 7.3 解析偏离仍保整数阶

若辅助为 $a_j^2h(a_j)(\chi_j-1)$，$h$ 为零点附近解析芽、$h(0)=2$ 且不恒等于2，则
$$
h(z)-2=\gamma z^m+O(z^{m+1}),\quad
c_j=\gamma a_j^{m+2}+O(|a_j|^{m+3}),
$$
其中 $m\ge1$，所以对应 $\kappa=m+2$ 是整数。
本稿允许实数 $\kappa$ 的主结论依赖绝对值比较，不能据此将复 $a_j^\kappa$ 当成一个全局解析芽。

## 8. 有限低头例外与准确剩余范围

正式定理采用 (1.1) 的全局版本。若有限低物理头有额外任意辅助，取包含全部例外的固定头 $J$，令
$$
Y_{\rm exc}=\sum_{j\in J}c_j(R_j-I)\in\mathcal G,\qquad
Y'=Y-Y_{\rm exc},\qquad B'=B-Y_{\rm exc}.
$$
则 $T=X^2+Y'-B'$。对高位主行用修改后的 $c'$，并将准则 (1.5) 作用于 $Y'$。
选中 $F$ 最终避开 $J$，所以
$\widehat B'-B'=\widehat B-B$；
实际 $\gamma_FY_{\rm exc}-Y_{\rm exc}$ 仍由 R260 的有限低位高壳支付。
$B'\in\mathcal G$ 且字符零（允许 $B'=0$），固定局部 $A$ 因子仍只来自有限头。
因此有限例外可这样完整吸收，而不是靠抽象的“有限扰动不影响循环性”。

精确 $c=0$ 不满足本稿下界，另由 R270C 闭合。
[R270 第五附录](../results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md) 已覆盖任意ℓ²主行的 $F_2+z_c$，只要辅助 $c$ 的非零排序满足 $-\log c_n^*/n^3\to\infty$（或有限支撑）。所以排序指数 $\alpha>3$ 的相关特例早已闭合，不应把全部 $\alpha>1$ 写成开放。

本稿不从单一 R268 熵条件免费推出更小半径 (1.5)，也未处理任意慢 $c$、所有剩余 $1<\alpha\le3$ 情形、多个独立慢模式、正正常湮灭者、无权边界 $N=M$ 或普通 Hilbert ISP。
