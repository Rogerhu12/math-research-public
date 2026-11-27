# 实际第一阶共同正则器的平坦／可逆二分

日期：2026-11-27（台北时间，UTC+8）。作者：literature_deddens / Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

状态：完整短证明。只识别 R128/R143 已构造的同一个正则器在完整兼容喷射理想中的位置；不从平坦性推断未知闭根域或未知限制的分母像。

## 1. 非负第一阶预解式

在任意原尾 $B=B_m$ 上，记 $\mathscr C_m=\{B_m\}'$，
$\mathfrak U_m$ 为实际 UHF 代数，$\mathfrak I_{\infty,m}$ 为全部兼容形式喷射的共同核。
给定 $b_j\ge0$、$b\in\ell^2$，令
$$
Z_b=X_{\sum_jb_j\chi_j},\qquad
R_b(t)=(I+tZ_b)^{-1},\qquad t>0.
\tag{1.1}
$$
R128 已证这是单射收缩交换子，$R_b(t)\to I$ 强收敛，且它的像在 $Z_b$ 的真实域内。

**命题 1.1。**
$$
\boxed{
\begin{array}{ll}
b\in\ell^1:&R_b(t)\in(\mathscr C_m\cap\mathfrak U_m)^\times;\$$2mm]
b\notin\ell^1:&R_b(t)\in\mathfrak I_{\infty,m}\setminus\{0\}.
\end{array}}
\tag{1.2}
$$

若 $b\in\ell^1$，则 $Z_b=\sum b_jV_j$ 按算子范数收敛，属于 $\mathscr C_m\cap\mathfrak U_m$。
$I+tZ_b$ 有界可逆，其逆仍属于这两个代数，证明第一支。
在任何兼容喷射中，$j_\chi(R_b(t))$ 因而是形式单位，不能为零。

现设 $b\notin\ell^1$。固定任意深度 $\ell\ge1$，$d=2^\ell$，作原有限头分解
$H=\mathbb C^d\otimes H_{m+\ell}$。真实高位 Cayley 算子满足
$V_{j+\ell}^{(m)}=I_d\otimes V_j^{(m+\ell)}$。
于是按实际闭算子及完整域有
$$
Z_b=s_\ell I+K_\ell(B)+I_d\otimes Z^{\rm tail}_\ell,
\qquad s_\ell=\sum_{j<\ell}b_j,
\tag{1.3}
$$
其中 $K_\ell(B)=\sum_{j<\ell}b_j(V_j-I)$ 是零常数解析芽，
而 $Z^{\rm tail}_\ell$ 是余下非负、仍非绝对可和的真实第一阶尾乘子。
本式的域是 $I_d\otimes Z^{\rm tail}_\ell$ 的域，因为只加了有界有限头项。

R128 §9 给 $Z^{\rm tail}_\ell$ 空谱。定义
$$
E_\ell=\bigl((1+ts_\ell)I+tZ^{\rm tail}_\ell\bigr)^{-1},
\qquad D_\ell=I_d\otimes E_\ell.
\tag{1.4}
$$
$E_\ell$ 为有界拟幂零交换子：对每个 $\mu\ne0$，预解恒等式给
$$
(I-\mu^{-1}E_\ell)^{-1}
=I+\mu^{-1}\bigl((1+ts_\ell)I+tZ^{\rm tail}_\ell-\mu^{-1}I\bigr)^{-1},
$$
故 $\sigma(E_\ell)\subseteq\{0\}$。非零 Hilbert 空间上的有界算子谱非空，因而谱恰为 $\{0\}$。

$K_\ell(B)$ 与 $D_\ell$ 交换，且前者拟幂零，故 $K_\ell(B)D_\ell$ 拟幂零。
由 (1.3) 的真实闭域分解，直接求逆得到
$$
\boxed{
R_b(t)=\bigl(I+tK_\ell(B)D_\ell\bigr)^{-1}D_\ell.
}
\tag{1.5}
$$
这里只求一个明确有界单位的逆，没有形式除以尾根。

对任意尾交换子字符 $\chi$，由于完整交换子逆封闭、$E_\ell$ 拟幂零，
$\chi(E_\ell)=0$。
因此有限头字符求值 $\rho_{\ell,\chi}$ 满足
$$
\rho_{\ell,\chi}(D_\ell)=0,\qquad
\rho_{\ell,\chi}(R_b(t))=0.
\tag{1.6}
$$
兼容喷射的前 $d$ 个系数恰由这个有限头字符矩阵读出。
$\ell$ 任意，且 (1.6) 对每个尾字符成立，所以每个完整兼容喷射都把 $R_b(t)$ 送到零。
于是 $R_b(t)\in\mathfrak I_{\infty,m}$。
它单射，故不为零，证明第二支。

## 2. 复第一阶行的同一个四正分量正则器

给定原复行 $a\in\ell^2$，按实、虚部正负部分写为四个非负行
$$
a=b^{(1)}-b^{(2)}+i b^{(3)}-i b^{(4)}.
$$
R128/R143 使用的固定共同正则器正是
$$
R_a(t)=\prod_{\nu=1}^4 R_{b^{(\nu)}}(t).
\tag{2.1}
$$
所有因子交换且单射。逐点有
$$
|a_j|\le\sum_\nu b_j^{(\nu)}
=|\operatorname{Re}a_j|+|\operatorname{Im}a_j|
\le\sqrt2|a_j|.
$$
因此 $a\in\ell^1$ 当且仅当四个非负行都属于 $\ell^1$。
(1.2) 及 $\mathfrak I_{\infty,m}$ 的理想性立即给
$$
\boxed{
\begin{array}{ll}
a\in\ell^1:&R_a(t)\in(\mathscr C_m\cap\mathfrak U_m)^\times;\$$2mm]
a\notin\ell^1:&R_a(t)\in\mathfrak I_{\infty,m}\setminus\{0\}.
\end{array}}
\tag{2.2}
$$
加入任意常数项 $a_*$ 不改变这个已选正则器。
有限多个第一阶行的共同乘积同样：全部行绝对可和时可逆；只要一行不是绝对可和，共同乘积便全喷射平坦。

这些正则器的真实第一阶像包含、固定参数图核心和全部不变限制上的参数单位关系仍是 R128/R140/R143/R172 的旧结论。
本稿没有从 (2.2) 新推出它们对另一未知闭算子或另一未知分母的范围性质。
特别，R143 有界头像中的分母 $D=-2Z$ 是另一个算子；它在同一未知 $L$ 上的稠密像与根图的伴随域比较不由 (2.2) 支付。

## 来源

- [R128：正第一阶预解式与非绝对可和空谱](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)，§§6、9；
- [R143：同一四正分量共同正则器](../results/R143-quadratic-gauge-common-regularizers-and-kernel-graphs.md)，§3；
- [完整有限头求值与兼容喷射](../results/R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)，§§1--3。
