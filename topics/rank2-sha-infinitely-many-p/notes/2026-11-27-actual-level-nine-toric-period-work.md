# 实际 full9 周期工作笔记：已接到 R1006

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

完整推导已写入
[R1006](../results/R1006-actual-full-nine-trace-and-original-katz-square.md)。
本笔记只保留探索中必须纠正的方向与已经闭合的接口，避免先前未完成
笔记中的分量、CM 基点及帽号约定被继续当作结论引用。

## 1. full9 需用合成 P h

标准右 adelization 的 compact 角色与经典角色互逆。
$h_\Gamma=f_{27}(\tau/3)$ 对应右 $\theta^{-1}$，不是右 $\theta$。
而且 $3^{3/2}\pi_3(\operatorname{diag}(3,1))W_3^0$ 的整个 adelic
向量并非一个3型，必须先施加真实有限 idempotent
$e_{\theta^{-1}}$，得到 $w^-$；再取 $w^+=\pi_3(h)w^-$。

令
$$
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
h=\operatorname{diag}(-1,1).
$$
标准 torus 下使用 $\pi_3(P)w^+$。相对于固定的 $h_\Gamma$，
实际 finite 点是 $g=P h$，不是单独的 $P$。
$\det g=-2\equiv1\pmod3$，故回到原 $K$ 分量；不再另作一次
$\tau$。

Hsieh 用 row/adjugate：标准行基为 $(\omega,1)$，右 $g$ 的
级作用是乘 $g'=\det(g)g^{-1}$。真实9级基因而是
$$
((1+\omega)u_9,(\omega-1)u_9).
$$
旧笔记用 column 基表示的相反顺序不能与此约定混用。
在这个实际基中 $\delta$ 的矩阵为 $-D$。

## 2. 基 CM 点是光滑无穷纤维

第二个3挠点 $(\omega-1)u_3=-\delta u_3$ 属于
$\ker[\delta]$。故 $X_1(3)$ 点是 $t=\infty$，不是
$t=1/24$ 的另一类非 CM 稳定3子群。

置 $z=v/t,r=1/t$，有 $z^3=r^2-27r$。
在 $x=z^{-2}X,y=z^{-3}Y$ 下，曲面成为
$$
Y^2+zXY+(r-27)Y=X^3.
$$
无穷纤维 $Y^2-27Y=X^3$ 经 $X=9x_E,Y=-27y_E$ 精确是
$E_{27}$。其微分 $\omega_{\rm new}|_E=-\omega_E/3$，且
$$
\Omega_S=-dr/z\wedge\omega_{\rm new}.
$$
由 $r=-z^3/27+O(z^6)$，$\Omega_S$ 在此纤维有一阶零。
不能把这个零当成已经有一个非零的基 weight3 值；R1006 使用
全部54商以及 raised/负二阶值。

## 3. 原 Artin 方向的完整核定

对有限单位 $u$，$\epsilon(u)$ 是 $u_3\bmod3$ 的唯一
$\mu_6$ 提升；$\psi_f(u)=\epsilon(u)$，而主理想值为
$\psi((a))=\epsilon(a)^{-1}a$。
算术 reciprocity 在实际 Tate 模上给
$$
\rho_E(\operatorname{rec}_{\rm ar}(u))=\epsilon(u)u^{-1}.
$$
row/adjugate 的右 torus 作用在级点上的实际乘数是共轭，因此
上述 Galois 作用对应 $a=\epsilon(u)^{-1}\bar u^{-1}$。
整个 $m\equiv-2\pmod6$ 分支上的特征精确抵消为
$\eta_j(u)$；没有反转原 $e_{\eta_j}$。
于是完整 $\operatorname{Cor}_{L/H}$ 留下 $[L:H]$，原
$1/18$ 平均给1。所有54项和重复共轭保留。

## 4. 所有局部常数已经算出

Hsieh 标准全局加性角色给 $\Psi_3(1/3)=\omega^{-1}$。
归一化 Kirillov 函数为
$$
w^-(d(a))=3^{3/2}{\bf1}_{1/3+\mathbf Z_3}(a),\qquad
w^+(d(a))=3^{3/2}{\bf1}_{-1/3+\mathbf Z_3}(a).
$$
对真实 $g=P h$，
$g^{-1}Jg=\iota_-(-\omega)h$，故3处 normalizer 相位是
$\chi_3(-\omega^2)=-\omega$，得到
$$
\mathcal P_3=-6\sqrt3\,\omega.
$$
2、17处的真实商向量是
$q^{3/2}\sum_t\chi_q(t)^{-1}\pi(\iota(t)\operatorname{diag}(q^{-1},1))W_q^0$；
其全部邻点双线性式给 $\mathcal P_q=-q^4$。
无穷因子与 Katz 插值相除给 $-4/\sqrt3$，再除 torus 体积
$(2/(3\sqrt3))^2$ 给 $-9\sqrt3$。完整固定常数为
$C=162\omega34^4$。

## 5. 实际54图的负二阶尺度与原单线

几何商算子满足 $R_{q,k+2}\theta=q\theta R_{q,k}$。
令 $V_j=R_{2,3}R_{17,3}h_\Gamma$；则在负二端点，R997 的
次数34和 $f_{\Omega_S}=-\delta h_\Gamma$ 给完整值
$-[L:H]\delta\,\theta^{-2}V_j^{[p]}/34$。
两个 $p$ Euler 因子先在经典权准确抵消，再在 Igusa 评值上取
$m_n=-2+6(p-1)p^n$ 极限。不能单独延拓 $p^m$ 或
$\Omega_p^{3+2m}$。

若 $\chi_E$ 是 $T_pE$ 的算术正角色，则 $H^1$ 对应线是
$\chi_E^{-1}$。所以 $P_-$ 的 $H^3(2)\eta_j^{-1}$ 恰为
$\eta_j^{-1}\chi_E^3\varepsilon^{-1}$，即 R804 的原 $V_j$。
同嵌入下 $\Omega_S\omega_E\in P_+$，正好检测 $P_-$。
原来源需选 $e_E^-$；其混合线为 $\bar\chi_E\eta_j^{-1}$，
是已由 Kato/R994 消失的 $\beta_j^c$ Tate 中央实现。
不能把 R998 的 cohomological 帽号与 R804 的 Tate 帽号混排。

R1006 给出的实际平方式仍不证明原 Katz 负二值在无限多个不同
素数非零。后继继续推进这一真实门槛；不把新最高图循环冒称为
R854 的旧 canonical 图，也不把复高度非零当作跨素数 AJ 保真。
