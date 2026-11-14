# 工作补充：真正核内正密度的截断源具有强算子残量

日期：2026-11-13 UTC。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

本稿只使用真实核 $T\rho=0$，补充既有正密度截断源的实际向量范数预算。
它比正常泛函意义的湮灭余项更强，但不把残量小当作到 $\ker T$ 的距离小，不给有界源或投影预算。

完整推导经 root 核验。[同次规范头源补充](2026-11-13-canonical-head-positive-normal-sources-and-simultaneous-strong-annihilation-central-review.md)给另一个源 $v_p$ 的全部正常湮灭强残量；本稿的 $h_p$ 保留真核支持独有的 $\sqrt{\delta_p}$ 因子。

## 1. 同一个有限头与全部常数

使用原实际 $\mathfrak C=A'$、$\mathcal A$、$\Omega$、$C$、$V_j$ 和准确有限头 $V_j^{[p]}$。
固定 $p\ge1$，令 $\Pi_p$ 为前 $p$ 位 Walsh 柱投影，头外为真空。
有限头代数 $\mathcal A_p$ 中每个算子只作用于该头，头外张量恒等，因此与 $\Pi_p$ 交换。

对 $a\in\operatorname{Ran}\Pi_p$，实际及局部乘子分别是
$$
X_a=\sum_{F\subset[0,p)}\widehat a(F)V_F,\qquad
X_a^{[p]}=\sum_{F\subset[0,p)}\widehat a(F)V_F^{[p]}.
$$
保持既有准确预算
$$
K_p=10^{p/2},\qquad
D_p=6\eta_{p-1}
\left(\sum_{F\subset[0,p)}|F|^2\,9^{|F|}\right)^{1/2}
\le6p\eta_{p-1}K_p.
\tag{1.1}
$$
于是
$$
\|X_a\|,\ \|X_a^{[p]}\|,\ \|X_{Ca}\|,\ \|X_{Ca}^{[p]}\|
\le K_p\|a\|,
$$
$$
\|X_a-X_a^{[p]}\|,\ \|X_{Ca}-X_{Ca}^{[p]}\|
\le D_p\|a\|.
\tag{1.2}
$$
这些是 [R230 正密度截断稿](../results/R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md) §§1、3.1 的真实有限乘子估计。

设 $T\in\mathfrak C$ 有界，取一个准确局部头 $T_p\in\mathcal A_p$，记
$$
d_p=\|T-T_p\|,\qquad
\gamma_p=2K_pd_p+\|T\|D_p.
\tag{1.3}
$$
以下不假设 $\Pi_p$ 与实际 $T$ 交换。

## 2. 真核向量的有限 Walsh 乘子是算子范数近湮灭子

设 $f\in\ker T$，令
$$
a=\Pi_p f,\qquad b=(I-\Pi_p)f,\qquad z=T_pa.
$$
由于 $T_p$ 与 $\Pi_p$ 交换，
$$
\boxed{
z=T_p\Pi_pf
=\Pi_pT_pf
=\Pi_p(T_p-T)f,
\qquad
\|z\|\le d_p\|f\|.
}
\tag{2.1}
$$
特别 $z\in\operatorname{Ran}\Pi_p$。

在同一有限头代数内，真空循环且分离，所以
$$
\boxed{T_pX_a^{[p]}=X_z^{[p]}.}
\tag{2.2}
$$
具体地，两边作用于 $\Omega$ 都等于 $z$，并与全部 $\mathcal A_p$ 元素交换；
有限头循环性使它们在整个头空间相等，再张量恒等扩张。
因此不是把局部乘子关系无证提升到实际代数。

对 $z$ 的实际提升也确有
$$
\|X_z-X_z^{[p]}\|\le D_p\|z\|,
\tag{2.3}
$$
因为 $z$ 仍在同一头空间；无需任何新平滑性。
不过下面直接使用 $\|X_z^{[p]}\|\le K_p\|z\|$，可得到较小常数。

准确分解为
$$
TX_a=
T(X_a-X_a^{[p]})
+(T-T_p)X_a^{[p]}
+X_z^{[p]}.
$$
结合 (1.2)、(2.1)，得到
$$
\boxed{\|TX_{\Pi_pf}\|\le\gamma_p\|f\|
\qquad(f\in\ker T).}
\tag{2.4}
$$
这是真正的全空间算子范数界，不只是某个指定矩或真空列的界。

如果 $f$ 只有小残量而非在核中，则同一计算给
$$
\boxed{
\|TX_{\Pi_pf}\|
\le K_p\|Tf\|+\gamma_p\|f\|.
}
\tag{2.5}
$$
这里只将 (2.1) 的上界替换为
$\|z\|\le\|Tf\|+d_p\|f\|$。

## 3. 核内正密度的完整实际截断源

设 $\rho\ge0$ 为迹类，$\tau=\operatorname{Tr}\rho$，并且
$$
T\rho^{1/2}=0.
\tag{3.1}
$$
等价地，$\rho$ 的支持包含于 $\ker T$。
取正平方分解
$$
\rho=\sum_i f_i\otimes f_i,\qquad f_i\in\ker T,\qquad
\sum_i\|f_i\|^2=\tau.
$$
允许可数无穷项。
令
$$
a_i=\Pi_pf_i,\quad b_i=(I-\Pi_p)f_i,\quad
\delta_p=\sum_i\|b_i\|^2,\quad
\sigma_p=(I-\Pi_p)\rho(I-\Pi_p).
$$

既有准确源为
$$
h_p=\sum_i\left(X_{a_i}Ca_i+X_{a_i}Cb_i+X_{Ca_i}b_i\right).
\tag{3.2}
$$
有限 Walsh 乘子的双线性对称性给
$X_{Ca_i}a_i=X_{a_i}Ca_i$。
因此也可准确写成
$$
h_p=\sum_i
\left(X_{a_i}Cf_i+X_{Ca_i}f_i-X_{a_i}Ca_i\right).
\tag{3.3}
$$
这些级数在 $H$ 中绝对收敛，且
$$
\|h_p\|\le2\tau K_p,\qquad
\|\Phi_{h_p}-\varphi_\rho\|_{\mathfrak C_*}=\delta_p,\qquad
\langle h_p,\Omega\rangle=\tau-\delta_p.
\tag{3.4}
$$

$T$ 与全部实际 $X_{Ca_i}$ 交换，且 $Tf_i=0$，所以 (3.3) 给
$$
\boxed{Th_p=\sum_i TX_{a_i}Cb_i.}
\tag{3.5}
$$
由 (2.4) 及 Cauchy--Schwarz，右侧绝对可和，并有
$$
\boxed{
\|Th_p\|
\le\gamma_p\sum_i\|f_i\|\|b_i\|
\le\gamma_p\sqrt{\tau\delta_p}.
}
\tag{3.6}
$$
这是原明确源的强向量范数预算，使用了真实核支持条件。
只知道 $\varphi_\rho(T\mathfrak C)=0$ 时不能删去 (3.3) 中
$X_{Ca_i}Tf_i$ 那一项。

更一般，记 $r_\rho=\|T\rho^{1/2}\|_{\mathrm{HS}}$。
(2.5) 和 (3.3) 直接给
$$
\|Th_p\|
\le
K_p r_\rho\left(\sqrt{\tau-\delta_p}+\sqrt{\delta_p}\right)
+\gamma_p\sqrt{\tau\delta_p}.
\tag{3.7}
$$
原核情形即 $r_\rho=0$。

### 3.1 正尾仍需保留其残量

由 (2.1) 以及
$Ta=(T-T_p)a+T_pa$，还得到
$$
\|T\Pi_pf\|\le2d_p\|f\|\qquad(f\in\ker T).
$$
因此 $Tb_i=-Ta_i$，并有
$$
\boxed{
\|T\sigma_p\|_1
\le2d_p\sqrt{\tau\delta_p},\qquad
\|T\sigma_p^{1/2}\|_{\mathrm{HS}}\le2d_p\sqrt\tau.
}
\tag{3.8}
$$
第一式由每个秩一项的迹范数计算；
第二式由
$\|T\sigma_p^{1/2}\|_{\mathrm{HS}}^2=\sum_i\|Tb_i\|^2$。
这些并不表示 $\sigma_p$ 精确支持于 $\ker T$。
将 $\sigma_p$ 除以其小迹时，必须分别保留
$2d_p\sqrt{\tau/\delta_p}$ 等相应归一费用。

## 4. 当前联合二次核的明确头误差

取原实际
$$
Q_j=V_j-I,\quad
X=\sum_ja_jQ_j,\quad
Y=\sum_jc_jQ_j,\quad
B_0=\sum_ja_j^2Q_j^2,\quad
T=X^2-B_0+Y,
\tag{4.1}
$$
其中 $a,c\in\ell^1$。
在同一个有限头中定义
$$
Q_j^{[p]}=V_j^{[p]}-I\quad(j<p),
$$
$$
X_p=\sum_{j<p}a_jQ_j^{[p]},\quad
Y_p=\sum_{j<p}c_jQ_j^{[p]},\quad
B_p=\sum_{j<p}a_j^2(Q_j^{[p]})^2,
\quad
T_p=X_p^2-B_p+Y_p.
\tag{4.2}
$$
这里 $T_p\in\mathcal A_p$，所以 (2.1)--(2.2) 确实适用。

记
$$
A_1=\sum_j|a_j|,\quad A_2=\sum_j|a_j|^2,\quad
C_1=\sum_j|c_j|.
$$
由 $\|Q_j\|,\|Q_j^{[p]}\|\le4$ 和原头差
$\|Q_j-Q_j^{[p]}\|\le18\eta_{p-1}$，可取
$$
e_a(p)=18A_1\eta_{p-1}+4\sum_{j\ge p}|a_j|,
$$
$$
e_c(p)=18C_1\eta_{p-1}+4\sum_{j\ge p}|c_j|,
$$
$$
e_B(p)=144A_2\eta_{p-1}+16\sum_{j\ge p}|a_j|^2.
\tag{4.3}
$$
于是
$$
\|X-X_p\|\le e_a(p),\quad
\|Y-Y_p\|\le e_c(p),\quad
\|B_0-B_p\|\le e_B(p),
$$
$$
\boxed{
d_p=\|T-T_p\|
\le8A_1e_a(p)+e_B(p)+e_c(p).
}
\tag{4.4}
$$
平方差只用
$X^2-X_p^2=X(X-X_p)+(X-X_p)X_p$；
没有假设实际 $X$ 与局部 $X_p$ 交换。

若对某个 $\alpha>1,\beta_0>0$，
$$
|a_j|+|c_j|\le C e^{-\beta_0j^\alpha},
$$
则凸性给
$$
\sum_{j\ge p}e^{-\beta_0j^\alpha}
\le
\frac{e^{-\beta_0p^\alpha}}
{1-e^{-\beta_0\alpha p^{\alpha-1}}}
\le C_{\alpha,\beta_0}e^{-\beta_0p^\alpha}
\quad(p\ge1).
$$
故
$$
\boxed{
\gamma_p
\le C_T10^{p/2}
\left(e^{-\beta_0p^\alpha}+p\eta_{p-1}\right)
\longrightarrow0.
}
\tag{4.5}
$$
在迟首 $c_j=a_j^\kappa\mathbf1_{j>j_0}$ 情形，取较小的指数包络即可。

## 5. 同一个真实联合见证的结论边界

原联合核构造给 $\rho=h\otimes h$，其中 $h\in\ker T$，
并给全空间单射的实际 $S=X+H_\zeta$，使
$\varphi_\rho(S\mathfrak C)=0$。
因此同一既有截断源同时满足
$$
\|h_p\|\longrightarrow\infty,\qquad
h_p/\|h_p\|\rightharpoonup0,\qquad
\langle h_p,\Omega\rangle\longrightarrow\tau>0,
$$
以及新的强预算
$$
\boxed{
\|Th_p\|\le\gamma_p\sqrt{\tau\delta_p}\longrightarrow0.
}
\tag{5.1}
$$
前一组来自已发表的准确正常泛函源理论；后一组使用 (3.1) 与当前具体头误差。
这里没有要求正常尾 $\delta_p$ 以任何速度衰减。

对于固定 $n\ge1$，还可取
$\|T^nh_p\|\le\|T\|^{n-1}\gamma_p\sqrt{\tau\delta_p}$；
不把它改写成未证的 $\gamma_p^n$。

本稿没有证明 $\|P_{\ker T}h_p-h_p\|$ 小。
小 $Th_p$ 不能在没有右逆或谱间隙预算时替代该距离。
也没有从 $\Phi_{Sh_p}$ 的小正常泛函范数推出 $\|Sh_p\|$ 小；
这个 $h_p$ 上的相应费用仍未支付；[规范头源补充](2026-11-13-canonical-head-positive-normal-sources-and-simultaneous-strong-annihilation-central-review.md)改用同一密度的另一个 $v_p$，已同时支付 $S,T,Z$ 的强残量，不能据此宣称两源的向量范数之差趋零。
