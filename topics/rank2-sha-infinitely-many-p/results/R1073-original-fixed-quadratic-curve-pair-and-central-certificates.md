# R1073 — 固定二次扭曲曲线对、原椭圆单位类与中央有限证书

日期：2026-11-28 UTC。

本篇在已证明秩至少二的固定 E65/E8125 上研究原通常全Sha的联合无穷素数非零；曲线不随p改变。复用[R959原E65](R959-original-e65-two-independent-points.md)与[R981原E8125](R981-original-delta-new-e54925-e8125-rank-two-sources.md)已登记的独立点、全部局部标签及原椭圆单位桥；以下保留真正的原类/微分/Betti规范。当前得到有限层等价证书，尚未证明无穷不同p检出，主目标未完成。

## 1. 同一 $E_{65}$ 理想来源按模五范数分为两份

取 $K=\mathbf Q(\omega)$，$p=6s-1>211$，$\Gamma=\operatorname{Gal}(K_\infty/K)$ 为原反圆分群，$T=\gamma-1$ 同时供全部模型使用。取两条已给出独立有理点及完整通常 Selmer 桥的固定曲线 $E_b:y^2=x^3+b$，其中 $b=65,8125$；分别沿 R959 §§1–5,15–16 和 R981 §§2,6.2。因 $8125=5^3\cdot65$，两者是有理二次扭曲，直接运输短 Weierstrass 方程及其 CM 作用给
$$ \psi_{8125}=\psi_{65}\,\eta,\qquad \eta(\mathfrak a)=\left(\frac{N\mathfrak a}{5}\right)\quad((\mathfrak a,390)=1). $$
等价地，在所有好素理想实际六次剩余角色的比为 $(5^3/\mathfrak q)_6^{-1}=(5/\mathfrak q)_2$，这是 $K(\sqrt5)/K$ 的 Artin 角色；$5$ 是有理基本判别式，故为上述范数。R959(17)–(19)、R981(21)–(23) 的两个 primitive 导子均为 $(390)$，射线度10368。实际 degree390 标签依次为 $(\epsilon,a,b;c,\eta_3)=(0,4,4;1,0),(0,1,4;1,1)$。两条单位角色在2、3及双13处相同；5处由 $u^4$ 变为 $u^{16}$，比 $u^{12}$ 正是模5范数二次角色。两模型的 uniformizer 比在 $2,\delta,5,\pi_{13},\bar\pi_{13}$ 依次是 $+1,-1,+1,-1,-1$。特别两个分裂13支的原值也变号。无穷及总根数同为原约定；两模型的全局根数为 $+1$。这用的是两条实际 Hecke 角色，未给任一未经转移的局部 Brandt 测试赋零。

在同一复嵌入取 $\theta_b>0$, $\theta_b^6=b$, $\theta_{8125}=\sqrt5\,\theta_{65}$；固定到 $p$ 进处的相容嵌入。因 $6\mid p+1$，两根在 $\mathcal O=\mathbf Z_{p^2}$ 均为单位。原 Néron 微分和 CM 格满足 $F_{\theta_b}^*\omega_b=\theta_b^{-1}\omega_1,\ \varpi_b=\varpi_1/\theta_b$，取这些相容 primitive Betti、Tate 基。以 R303(15) 的原 $E_1$ 秩零单位类 $\xi_1$ 为两者同一 signed 整基，写
$$F_{\theta_b}^*\xi_b=\mathcal A_b(T)\xi_1,\qquad \mathcal A_b\in\mathcal O[[T]].$$
这正是 R959(62),(66) 与 R981(46)–(50) 的对象。尤其 $\operatorname{ord}_0\mathcal A_b=2\operatorname{ord}_0\widehat J_{b,p}\ge2$，前两项皆零，每条的 $[T^2]\mathcal A_b\ne0$ 都给该固定曲线秩恰为二和通常全 $\Sha(E_b/\mathbf Q)[p^\infty]$ 有限。保留原 $\widehat\kappa_b$ 及分母规范；阶数身份已足够，不以两曲线的具体 leading coefficient 逐项相等代上述命题。

对 $\nu$ 确切阶 $p^{2j-1}$ ($j\ge1$)，置 $t_\nu=\nu(\gamma)-1$。用 BKO, *p-adic L-functions and rational points on CM elliptic curves at inert primes*, §3.1.1、Prop. 3.1 (3.2),(3.3)（出版页1431）及 Def. 3.13 (3.14)。其加权全 Galois 和在 $\chi=\nu^{-1}$ 给 $L_{p\mathfrak f_b}(1,\bar\psi_b\nu^{-1})\omega_b/\varpi_b$，群环元素于 $\nu$ 特化。理想共轭把此 $L$ 变成 $L_{p\mathfrak f_b}(1,\psi_b\nu)$。当前 $p$ 由 $\nu$ 分歧，其余导子处由原 $\psi_b$ 分歧；在 split 13 的 $\nu$ 虽可在 uniformizer 上非平凡，却未分歧，不能抵消原分歧。参考 $\mathfrak f_1=(2\delta)$，故其好位5和两个13的原 Euler 因子都完整保留。参考 primitive 有限值非零，由原单位 signed 参考及各第 $2j-1$ 层非零局部 resolvent（亦见 R1070 §§15–17,23）。共同全和没有不同的 $p$ 幂。coLie 中的 $\theta_b^{-1}$ 与周期比准确相消，给
$$ \mathcal A_b(t_\nu)=\theta_b^{-1}\,\frac{L(1,\psi_b\nu)/\varpi_b}{L(1,\psi_1\nu)/\varpi_1}=\frac{L(1,\psi_b\nu)}{L(1,\psi_1\nu)}. $$
使用上一项同一代数值的固定 $p$ 进嵌入读取后一项；没有对一般复数选择 $p$ 进绝对值。

对 $e=+1,-1$，定义 $L_e(s,\nu)$ 为 $\sum_{(\mathfrak a,390p)=1,\ (N\mathfrak a/5)=e}\psi_{65}(\mathfrak a)\nu(\mathfrak a)/(N\mathfrak a)^s$ 的解析延拓。在 $\Re(s)>3/2$ 它绝对收敛。逐理想采用 $(1+e\eta)/2$ 并沿同一延拓给 $L_e=(L(\psi_{65}\nu)+eL(\psi_{8125}\nu))/2$。于是两个真正有界整函数为
$$ \mathcal P_e=\frac{\mathcal A_{65}+e\mathcal A_{8125}}{2}\in T^2\mathcal O[[T]],\qquad
 \boxed{\ \mathcal P_e(t_\nu)=L_e(1,\nu)/L(1,\psi_1\nu).\ } $$
由整有界级数的有限零点性，这些 primitive 特化各自唯一确定 $\mathcal P_e$。全集上的两个正交范数指示函数保住了同一 primitive Dirichlet 来源。两分支相加为 $\mathcal A_{65}$，相减为 $\mathcal A_{8125}$，所以两条真实原中央同时坏当且仅当 $[T^2]\mathcal P_+=[T^2]\mathcal P_-=0$。

## 2. 全有限 $L$-值直接读二阶系数

对 $i\ge1$ 取 $B_i(T)=\prod_{j=1}^i\Phi_{p^{2j-1}}(1+T)$，并令 $\mathcal Y_i$ 为其全部根 $y=t_\nu$。该多项式 monic distinguished、无重根且 $B_i(0)=p^i$。对 $H_e(T)=\mathcal P_e(T)/T^2$ 取其除 $B_i$ 的整 Weierstrass 余式 $R_{i,e}$。以所有非平凡原根的完整 Lagrange 插值在零处评价准确得到
$$\boxed{\quad D_{i,e}:=-p^i\sum_{y=t_\nu\in\mathcal Y_i}
 \frac{ L_e(1,\nu)}{y^3 B_i'(y)\,L(1,\psi_1\nu)}
 =R_{i,e}(0)\in\mathcal O,\qquad
 D_{i,e}\equiv [T^2]\mathcal P_e\pmod{p^i}.\quad}$$
单项可有分母；整性属于整余式的完整和。此式包含直至 $p^{2i-1}$ 的每一合法奇层、每个 primitive 角色及全部5和双13参考因子。于是对每个允许惰性 $p$，存在一条原中央非零，当且仅当存在 $i,e$ 使 $v_p(D_{i,e})<i$。若此检测在无穷不同 $p$ 上成立，固定两曲线中至少一条满足本课题结论。原导子投影本身不决定 $D_{i,e}$ 的首次检出层或跨素数非零。

BKO 出版本：[JIMJ 23 (2024), 1417–1460](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
