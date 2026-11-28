# R1072 — 原全导子反圆分平均、整数 Brandt 行与中央二次矩

日期：2026-11-28 UTC。

本篇继续使用固定原 E17、原ψ17、原Γ、原Rubin函数和原几何B34。已证结论按节陈述；以下全导子非消失只排除明确范围内的旋分零，不替代原中央导数跨素数非零。主课题未完成。

依赖：[R724原Mellin平均与完整非实补偿](R724-original-first-wild-analytic-average-and-nonreal-compensation.md)、[R1070原全层绝对比较与整平方](R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。保留每个原Euler、period、tame及wild标签。本文证明为符号推导，不作本地数学计算。

## 1. 原几何边界根及 Rubin 旋分因子的统一截点

设 $p>211$ 惰性于 $K=\mathbf Q(\omega)$，$d=p+1$，令 $D=[K(\mu_d):K]=\varphi(d)/2$；因为 $3\mid d$，两域的交就是 $K$。对任意固定 $\varepsilon>0$，当 $p$ 充分大且 $i\ge(1/2+\varepsilon)D$ 时，所有R1070 中确切阶 $p^{2i-1}$ 的原 Hecke 扭曲均满足
$$
 L(1,\psi_{17}\nu)\ne0,\qquad \Phi_{p^{2i-1}}(1+T)\nmid\mathcal A_p(T),\qquad Q_i(W)\nmid\mathcal B_{34}(W).
$$
这个明确的 $p$ 依赖截点与固有极限 $i\to\infty$ 有区别。证明只用原全导子 Yang 范数给出的真根号及 R724 同一个固定权二原来源；不用此前由 $\mu=0$ 得到的深层非零来反证。

设 $I=2i$，$Q_0=51/\pi$，$X=Q_0p^{I}$。原 $\psi=\psi_{17}$ 导子 $\mathfrak f_0=(2\delta\cdot17)$，每个该层 primitive $\nu$ 分歧导子 $p^I$，其余有限原标记不变，完成因子参数为 $X$。原 Yang 向量给根号 $+1$。R724(13) 的 Mellin 两半在同一原固定 Fricke 点对称，故
$$
 L(1,\psi\nu)=2\!\sum_{(\mathfrak a,\mathfrak f_0p)=1}\frac{\psi(\mathfrak a)\nu(\mathfrak a)}{N\mathfrak a}e^{-N\mathfrak a/X}.
$$
每个 primitive 角色来自原$\lambda$采样，$\nu=\theta_\lambda(\cdot/\overline{\cdot})$。因此对 $s\in\{I,I-1\}$ 定义 $Z_s(X)$ 为上述去掉 $\nu$ 后，仅在生成元 $\alpha$ 满足 $\alpha/\bar\alpha\in\mu_d\bmod p^s$ 的全部整理想上求和。$\mu_6$ 换元不改条件。局部主单位的层 $j$ 对全部 $p^j$ 角色平均，恰是 $\alpha/\bar\alpha\in\mu_d\bmod p^{j+1}$ 的指示；取 primitive 差得到
$$
 \frac1{\varphi(p^{I-1})}\sum_{\operatorname{ord}\nu=p^{I-1}}L(1,\psi\nu)
 =\frac2{p-1}\{p Z_I(X)-Z_{I-1}(X)\}.
$$
两个 $Z$ 使用相同 $X$；后一层是从 primitive 指示扣除的完整项，没有设置为零。

按 R724(B1)–(B3) 在 $Z_s$ 中先分解 $\mathfrak a=(c\alpha)$，其中 $c\ge1$，$\alpha$ 是 primitive 整数标签模 $\mu_6$。保留 $(c,102p)=1$、$(\alpha,\delta)=1$ 及原坏位权 $\psi((\alpha))$。径向因子 $R_{102p}(X/|\alpha|^2)$ 满足统一界
$$
 |R_{102p}(X/|\alpha|^2)|\ll \exp(-|\alpha|^2/X).
$$
确实 $\chi_{-3}(c)\mathbf1_{(c,102)=1}$ 的部分和绝对有界，去掉 $p\mid c$ 只再减其同一部分和乘 $\chi_{-3}(p)$，界不依 $p$；对递减权 $c^{-1}e^{-c^2|\alpha|^2/X}$ 作 Abel 求和即得。又 $|\psi((\alpha))|=|\alpha|$。所以每个 primitive 方向的绝对贡献至多常数乘 $|\alpha|^{-1}\exp(-|\alpha|^2/X)$。单位类全部倍数形成同一个有理主项
$$
 R_{102p}(X)=\frac{9\pi}{17\sqrt3}(1+p^{-1})+O(X^{-1/2}),
$$
只要 $X/p^2\ge1$。这里用 R724(26)–(28) 的一般式 $R_{102p}(X)=R_{102}(X)+p^{-1}R_{102}(X/p^2)$；两误差各为 $O(X^{-1/2})$。

对每个固定 $\zeta\in\mu_d\subset K_p$，令
$$
 \mathcal L_{\zeta,s}=\{\alpha\in\mathcal O_K:\ \alpha-\zeta\bar\alpha\in p^s\mathcal O_{K_p}\}.
$$
这个平面格在 $\mathcal O_K$ 中指数为 $p^s$。事实上 $\alpha\mapsto\zeta\bar\alpha$ 为整 $\mathbf Z_p$ 线性对合，模 $p$ 既非 $+1$ 亦非 $-1$，而 $2$ 是单位，故正负特征部分各为自由秩一；只需约束负特征坐标被 $p^s$ 整除。primitive $\alpha$ 自动为 $p$ 单位，故每个满足条件的 $\alpha$ 只在一个这样的格中。为上界允许数全部六个整数代表。

先设 $\zeta\notin\mu_6$。对任一非零格点 $\alpha$，$\alpha-\zeta\bar\alpha\ne0$，因为 $K$ 的根单位只有 $\mu_6$。取固定 $p$ 进嵌入所对应的 $K(\zeta)$ 的**相对范数**。其中原因子在 $p$ 进估值至少 $s$，所有其他因子均整。其积是非零 $y\in\mathcal O_K$，$v_p(y)\ge s$，故 $y\in p^s\mathcal O_K$；非零 Eisenstein 整数的复模至少1，遂有 $|y|\ge p^s$。每个复因子模长至多 $2|\alpha|$，相对次数 $D_\zeta=[K(\zeta):K]\le D$，因而
$$
 |\alpha|\ge\tfrac12 p^{s/D_\zeta}\ge\tfrac12 p^{s/D}.
$$
在 $\eta=\zeta\in\mu_3$ 的格中有确切原短直线 $u\mathbf Z$（$u\in\mu_6,\ u/\bar u=\zeta$）；primitive 实际只有该单位类，已并入有理主项。对 $\zeta\in-\mu_3$ 相应直线为 $u\delta\mathbf Z$，由原 $(\alpha,\delta)=1$ 全部排除。当 $p$ 充分大时这些固定线给各格最短向量：平行线间距等于格余面积 $\asymp p^s$ 除以该 primitive 向量长度，其余格线距原点远大于固定长度。

给二维格 $L$ 的最短原方向取向量长 $r$。格线平行于它，间距 $h=\operatorname{covol}(L)/r$。选第二基向量并平移到沿第一坐标投影绝对值至多 $r/2$，最短性给 $h\ge\sqrt3r/2$。长度至多 $R$ 的偏离首线点数为零若 $R<h$；否则用 $O(R/h)$ 条非零线、每线上 $O(1+R/r)=O(R/r)$ 个点，得 $O(R^2/\operatorname{covol}(L))$。对 $R^{-1}e^{-R^2/X}$ 分部求和，全部偏离首线的带权点总量 $\ll \sqrt X/\operatorname{covol}(L)$。在首线的 $\mathcal O_K$-primitive 点至多 $\pm$ 两个，合计 $O(1/r)$；若最短向量不是 $\mathcal O_K$-primitive，这条线的实际贡献为零。故非 $\mu_6$ 格使用上段的明确下界，$\mu_6$ 格的首线已经逐一处置后，只需偏离首线的估计。合并全 $p+1$ 个原 tame 方向，得
$$
 |Z_s(X)-R_{102p}(X)|\ll
 (p+1)\left(p^{-s/D}+p^{i-s}\right),\qquad s=2i,\,2i-1.
$$
所有常数只依固定模型与 $Q_0$，不依 $p,i,D$；若需要可把 $p^{-s/D}$ 改成 $d^{-1}\sum_{\zeta\notin\mu_6}p^{-s/D_\zeta}$。因此当 $i\ge(1/2+\varepsilon)D$，$D=\varphi(p+1)/2\to\infty$，两误差对全部此类 $i$ 一致趋于零。原 primitive 完整平均遂趋于 $18\pi/(17\sqrt3)>0$。至少一个实际扭曲非零。一个非平凡原 $p$ 幂阶字符的 Rubin 零由 $\mathcal A_p\in\mathbf Z_{p^2}[[T]]$ 运到全部同阶字符（在未分歧基上旋分多项式 Eisenstein）；R1070 的真实全层等价及参考不零因而给当层全部非零。严格 LT 中 $Q_i$ 的原几何返回亦跟随。这正是对命名 $\mathcal B_{34}$ 在实际 primitive 各层的无根区间。

因 $6\mid d$，$D\le d/6$。此外，对每个固定由小素数组成、含 $6$ 的平方自由整数 $M$，在无穷 $p\equiv-1\bmod M$ 上有 $D/d\le\varphi(M)/(2M)$。逐次取这些原进程中的大素数，可得一列惯性 $p$ 使上述截点与 $p$ 的比趋于零。这一结论仍保留可能的首导子 $p^2$；它给统一可比较的深层根排除，不将任一单导子非零偷换为原中央导数非零。
