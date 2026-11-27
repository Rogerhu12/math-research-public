# 原 ψ4 权重二候选的完整局部型与零 toric 点

2026-11-27 UTC。

本注检验一个具体的降权候选：以 $\theta(\psi_4)$ 代替原 weight3 形式，使双 theta 槽由 $(n,n+2)$ 变成 $(n,n+1)$，期望在 $n=-1$ 直接读原 canonical $S$ 的零阶。结论有两层：原 GL₂ 模曲线在2、3处均没有所需 toric Hom；改成正确的判别式6四元数曲线后，实际 Gross–Zagier toric 点仍为零。后一结论使用完整 Rankin 因子和原 $\psi_{17}$ 的已证中央零，不把局部 Hom 非零当作全局点非零。

本注是纸笔证明，不新增数值执行，不对任何 $p^{\mathrm{weight}}$ 作解析延拓。这里的 $\lambda_{\mathrm{pt}}$ 是一个新的 type $(1,0)$ 椭圆角色，不是 R806 的三个 type $(3,0)$ 角色。

## 1. 同一个原有限角色

沿 R290、R991 取
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
E_4:\ y^2=x^3+4,\qquad E_{17}:\ y^2=x^3+17.
\tag{1}
$$
$\psi_a$ 是相应原 CM Hecke 角色，$\nu_a$ 是其 unitary 规范。定义
$$
\pi=\operatorname{AI}_{K/\mathbf Q}(\nu_4),\qquad
\chi=\nu_{17}\nu_4^{-1},\qquad
\alpha=\nu_4^2\nu_{17}^{-1},\qquad \beta=\nu_{17}.
\tag{2}
$$
$\pi$ 是 weight2、level108 的 $\theta(\psi_4)$；其中心角色为1。$\chi$ 是有限阶角色，且在 $\mathbf A_{\mathbf Q}^{\times}$ 上平凡。在本文的 toric 约定下取 $\operatorname{Hom}_{K_v^\times}(\pi_v,\chi_v)$；应用 CST 时其字符写作 $\Omega=\chi^{-1}$。

R991(5)与 R290 原表逐项相除给
$$
\begin{array}{c|cc}
 &\chi&\alpha\\ \hline
\mathcal O_{K,2}^{\times}&\epsilon_2^{-1}&1\\
2&1&-1\\
\mu_6\subset\mathcal O_{K,3}^{\times}&u^4&u\\
\delta&-1&-i\\
\mathcal O_{K,17}^{\times}&\vartheta_3&\vartheta_3^{-1}\\
17&1&-1 .
\end{array}
\tag{3}
$$
这里 $\epsilon_2$ 是原 $\mathbf F_4^\times$ Teichmüller 角色，$\vartheta_3(u)=\operatorname{Teich}(u)^{48}$。所有更深主单位上均为平凡，其他有限位保持原未分歧数据。特别每个有限位均有
$$
\chi_v(-1)=1,\qquad
\mathfrak f_\chi=(34\delta^2),\qquad
\mathfrak f_\alpha=(17\delta^2).
\tag{4}
$$
在3处，$\chi(\omega)=\omega$、$\alpha(\omega)=\omega$，所以导子指数确为2，而不是仅由一个模 $\delta$ 值猜测。$\chi$ 是 ring class conductor102 的实际有限角色。

代数角色
$$
\lambda_{\mathrm{pt}}=\psi_4^2/\psi_{17}
\tag{5}
$$
对应真正的 sextic twist $d=16/17$；乘以 $17^6$ 得整数代表
$$
E_{\mathrm{pt}}:\ y^2=x^3+16\cdot17^5
=x^3+22717712 .
\tag{6}
$$
因此其导子是 $3\,\mathrm N(17\delta^2)=7803$。例如在2处作 $x=4x_0,\ y=8y_0+4$，得到整模型 $y_0^2+y_0=x_0^3+354964$；这也与(3)在2处未分歧相容。式(5)保持原 CM 定向，不把另一个共轭角色任意代入。

## 2. 两个有限不匹配处的完整 Gauss 计算

在 $W_K$ 上，
$$
\left.\pi\right|_{W_K}\otimes\chi^{-1}
=\alpha\ \oplus\ \beta^{-1}.
\tag{7}
$$
本节先沿 R991(11)–(14)在3处取 $\Psi_{\mathbf Q_3}(1/3)=\omega$、$\Psi_{K_3}=\Psi_{\mathbf Q_3}\circ\operatorname{Tr}$。对导子指数 $c$ 的角色 $\rho$，
$$
\epsilon(\rho,\Psi_{K_3})
=\rho(\delta^{c+1})\,3^{-c/2}
 \sum_{u\in(\mathcal O_K/\delta^c)^\times}
 \rho(u)^{-1}\Psi_{K_3}(u/\delta^{c+1}).
\tag{8}
$$
$\alpha$ 的导子指数是2、单位型为 $u$、$\alpha(\delta)=-i$。完整六单位和是
$$
\sum_{u\in\mu_6}u^{-1}\Psi_{K_3}(u/\delta^3)=-3 .
$$
而 $\alpha(\delta^3)=i$，故 $\epsilon(\alpha)=-i$。$\beta^{-1}$ 的导子指数是1、单位型为 $u^3$、$\beta^{-1}(\delta)=i$；和为 $\delta$，给 $\epsilon(\beta^{-1})=-i$。于是
$$
\epsilon(\alpha\oplus\beta^{-1},\Psi_{K_3})=-1 .
\tag{9}
$$
两角色在 $-1$ 上都为 $-1$，所以同时反转加性角色不会改变(9)。

在2处可用全局标准加性角色，其在 $\mathbf Q_2$ 上导子为0。$\alpha_2$ 未分歧，给 epsilon 为1。$\beta_2^{-1}$ 是非平凡 cubic，完整 $\mathbf F_4^\times$ Gauss 和为2，而 uniformizer 值为 $-1$，给 epsilon 为 $-1$。因此
$$
\epsilon(\alpha\oplus\beta^{-1},\Psi_{K_2})=-1 .
\tag{10}
$$
若用原 Yang 的 $\Psi_K/2$，两个单因子分别变成 $-1,+1$，乘积仍为 $-1$。这支付了2处加性规范，不能将“未分歧角色 epsilon=1”与 $\Psi_K/2$ 混用。

在17处，两因子都是原奇指数 $\vartheta_{\pm3}$。沿 trace 纤维求和，
$$
\sum_{u\in\mathbf F_{17^2}^{\times}}
 \vartheta_{\pm3}(u)^{-1}\Psi(u)
=17\,\vartheta_{\pm3}(\delta)=-17 .
$$
再乘 uniformizer $-1$，两者的 epsilon 均为 $+1$。其余有限位的完整乘积为 $+1$。

为同时显示全局根号，取 CST 的全局标准加性角色，即无穷处 $e^{2\pi i x}$、有限处 $e^{-2\pi i\{x\}_q}$，再复合 $K/\mathbf Q$ trace。相对于(8)，3处每个单因子乘 $-1$。得到
$$
\begin{array}{c|rrrr|r}
 &2&3&17&\infty&W\\ \hline
\alpha&+1&+i&+1&+i&-1\\
\beta^{-1}&-1&+i&+1&+i&+1\\
\alpha\oplus\beta^{-1}&-1&-1&+1&-1&-1 .
\end{array}
\tag{11}
$$
反演 $\beta$ 不改变其诱导到 $\mathbf Q$ 后的完整 $L$ 函数或根号；在 CM 线中仍保(7)的方向。

## 3. 正确的四元数代数

CST §3 pp.2554–2555 的 Tunnell–Saito 判据，按(2)的方向是
$$
\dim\operatorname{Hom}_{K_v^\times}(\pi_v,\chi_v)=1
\iff
\epsilon(\left.\pi_v\right|_{W_{K_v}}\otimes\chi_v^{-1})
=\chi_v(-1)
\tag{12}
$$
（GL₂ 一侧）。CST 原文先写 $\epsilon(\pi_v,\Omega_v)=\eta_v(-1)\epsilon(\pi_{K,v}\otimes\Omega_v,\Psi_{K,v})$，其 Hom 判据右侧亦含 $\eta_v(-1)$；两边消去该因子，且 $\Omega_v(-1)=\chi_v(-1)=1$，正给(12)。另一侧给除四元数代数上的 Jacquet–Langlands transfer。由(4)、(9)–(11)，有
$$
\begin{array}{c|ccc}
v&2&3&\text{其余有限位}\\ \hline
\dim\operatorname{Hom}_{K_v^\times}(\pi_v,\chi_v)&0&0&1 .
\end{array}
\tag{13}
$$
这是整个 Hom 为零，不只是旧向量选择不合适。故不能在原 full9 模曲线保留同一图后，只换 weight 或只替换3处向量。

$\pi_2$ 是由非平凡 cubic 诱导的 depth-zero supercuspidal；$\pi_3$ 由 ramified quadratic $K_3/\mathbf Q_3$ 的 conductor2 角色诱导，且其共轭单位型为 $u^{-1}\ne u$，所以也是 supercuspidal。两处均允许 Jacquet–Langlands transfer。取
$$
B/\mathbf Q\quad\text{在且仅在 }\{2,3\}\text{ 分歧}.
\tag{14}
$$
$B$ 在无穷处 split，是判别式6的不定四元数代数。$K$ 在2、3均为域，故嵌入 $B$。有限处 JL transfer 对 $\chi$ 的 Hom 全为1。CST 的 Gross–Zagier 叙述使用在无穷处换成 definite 的 incoherent adelic quaternion；其对应的实际 Shimura 曲线正是(14)，二者不能混淆。

无穷处 weight2 discrete series 的紧型是 $\pm2,\pm4,\ldots$，而 $\chi_\infty=1$。因此这是总根号 $-1$ 的 Gross–Zagier 情形，不是一个处处 Hom 非零的普通 Waldspurger toric period。

## 4. 改到正确曲线后，实际 toric 点仍为零

在代数中心坐标中，完整 Rankin 函数的因子为
$$
L(s,E_4/K,\chi^{-1})
=L(\lambda_{\mathrm{pt}},s)\,L(\psi_{17},s).
\tag{15}
$$
第二因子的 CM 定向来自(7)的 $\beta^{-1}$；在诱导 $L$ 函数中它与 $\psi_{17}$ 给同一个函数。

R290(36)、(39)已经由原算术 rank 下界支付
$$
L(\psi_{17},1)=0.
$$
(11)又给其根号 $+1$。完成函数的其他因子在 $s=1$ 正则且非零，故
$$
\operatorname{ord}_{s=1}L(\psi_{17},s)\ge2.
\tag{16}
$$
另一方面 $W(\lambda_{\mathrm{pt}})=-1$，所以它在 $s=1$ 至少一阶零。于是
$$
\operatorname{ord}_{s=1}L(s,E_4/K,\chi^{-1})\ge3,\qquad
L'(1,E_4/K,\chi^{-1})=0 .
\tag{17}
$$
此处不需要假设 $E_{17}$ 的解析秩恰为2，也不需要新计算 $E_{\mathrm{pt}}$ 的导数。

对(14)取实际 JL modular parametrization $f:X_U\to E_4$，以规范 Hodge 类为基点。$\chi$ 有限且中心相容；局部符号已逐处由(11)支付。CST §2 pp.2550–2551 的一般 Gross–Zagier 式(2-4)，以及 Proposition2.5 的(2-5)，适用于任意实际 pure tensor $f_1,f_2$：
$$
\frac{\langle P_{\chi^{-1}}(f_1),P_{\chi}(f_2)\rangle}
     {\operatorname{Vol}(X_U)^{-1}(f_1,f_2)_U}
=
\frac{L'(1/2,\pi,\chi^{-1})}
     {L(1,\pi,\operatorname{ad})L(2,1_{\mathbf Q})^{-1}}
 \prod_v\beta_v(f_{1,v},f_{2,v}).
\tag{18}
$$
这里 unitary 中央 $1/2$ 与(17)的代数中央1对应；全部局部 toric 积分、Haar、有限 trace 与 dual 向量都留在原式。

由(17)，(18)右边为零。用 Rosati 与复共轭取 $f_2$ 为 $f_1$ 的正定 dual，左边是实际 $\chi$-等型点的 Hermitian Néron–Tate 高度。其正定性给
$$
\boxed{P_{\chi^{-1}}(f)=0
       \quad\text{于 }E_4(H)\otimes_{\mathbf Z}\mathbf C
       \text{ 的该有限等型分量。}}
\tag{19}
$$
$H$ 可取定义该 level 与字符的有限 ring class extension。对有限线性组合由线性得到同式。特别所有相应 $p$-adic elliptic logarithm 均为0。无需为了该零结论逐一算出新的非零 test-vector 常数；任意局部向量的完整 GZ 式都已有零的全局因子。不能反过来把(19)说成 $E_{\mathrm{pt}}$ 的全部有理点均为挠点。

## 5. 剩余一阶问题的准确范围

拟议双核的两个槽是 $(n,n+1)$。在 $n=-1$，正槽是原 $\psi_{17}$ 来源的真空，而原 canonical $S$ 的真空是0。式(19)证明，即使完成正确的四元数几何替换，该零阶点也不能提供一个新的非零负一读者。这与原 canonical 中央零相容，并没有消掉完整连接、Gaussian 或 Euler 费用。

若要继续使用此候选，至少须构造同一 $B$ 上实际变化权/导子的整来源，付清两个有限向量、全部局部相位和真实权参数，随后计算其第一个非零 derived toric point 或正则化读数。复变量的至少三阶零(17)不说明任何 $p$-adic 权导数非零；同样，不允许对单个 CM 点的(19)在模参数中直接微分。BDP good-pair 的非零辅助 $\beta$ 条件在本候选恰失败，不能以它除去 $L(\psi_{17},1)$。

因此本注排除的是“降为 weight2 后直接获得新的非零点输入”这一具体方案。它不证明原 rank2 中央导数为零或非零，也不排除另一个已付 derived construction。

## 文献与原结论

- R290，§§1、6–8，特别(30)–(41)：原 $\psi_{17}$ finite Schwartz、全权平方及 canonical 真空零。
- R991，§§1、3、5、9，特别(5)、(11)–(16)、(39)：$\psi_4$ 全角色、含 uniformizer 的3处 Gauss 和、全局加性规范。
- R297(14)–(16)：原 canonical $S$ 的唯一完整 CM13 质量核及其真实 degree34 来源。
- Li Cai, Jie Shu, Ye Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory **8** (2014), 2523–2572；§2 pp.2550–2551 式(2-4)、Proposition2.5 式(2-5)，§3 pp.2554–2555 的 Tunnell–Saito 判据。[原刊完整 PDF](https://msp.org/ant/2014/8-10/ant-v8-n10-p.pdf)。本注用的是实际 weight2 公式，未将它套到旧 weight3 循环。
