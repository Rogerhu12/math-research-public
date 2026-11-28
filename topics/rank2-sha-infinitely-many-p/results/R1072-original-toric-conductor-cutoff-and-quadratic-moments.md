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

## 2. 原整数 Brandt 行在全部导子上的严格第一位

取 R736 同一个固定的 $f_{\rm int}$、原判别式 $3$ 的定四元数代数、含 $2,3,17$ 的同一整环及 CM 嵌入。公开固定证书 R736 §8 的原 368 个值均在 $\{0,\pm1,\pm2\}$ 及原 $f_{\rm int}(1)=0$。不运行新的变 $p$ 扫描。记 $i\ge1$、$t=2i-1$、$M_i=p^{t-1}$、$D_i=(p-1)M_i$，并置
$$ S_i=\sum_{j=1}^{i-1}(p^{2j}-p^{2j-1})=p\sum_{j<i}D_j .$$
这个 $D_i$ 是旋分次数；上段高层截点的 $D=\varphi(p+1)/2$ 仍单列。

每一层的 ring class 群由 $h_K=1$ 等于 $(\mathcal O_K/p^{2i})^\times/((\mathbf Z/p^{2i})^\times\mu_6)$，其 tame 部分阶 $d/3$，wild 部分 $\mathbf Z/p^t$。固定原 $\gamma$ 所给 $u\in\mathbf Z/p^t$。令 $A_{i,u}$ 为在这个 wild 标签上的全部 $d/3$ 项原整数 $f_{\rm int}(x_{2i}(a))$ 之和，与 R736(30) 的 $i=1$ 读法一致。实际 $[\delta]$ 是群中的非平凡 tame 二阶元：全局 $\delta^2=-3$，且其在 $K_p$ 的约化不在 $\mathbf F_p^\times\mu_6$（若可写 $\delta=c\epsilon$，则 $-1=\delta/\bar\delta=\epsilon^2\in\mu_3$，矛盾）。它在全部层代表同一个原分歧处的 toric class，固定 $f_{\rm int}$。具体可用 idele 只在 $3$ 取 $\delta$ 的代表，移去全局 $\delta$ 后，除 $p,3$ 外是固定 $\mathcal O_{K,q}^\times$；在 $p$ 上留下 $[\delta]^{-1}$，而 $3$ 的原 toric 向量整个 $K_3^\times$ 不变。这一说明不依 $i$。各行遂有
$$ A_{i,u}\in2\mathbf Z,\qquad |A_{i,u}|\le2d/3 .$$
对确切阶 $p^t$ 根 $\xi$，原 Brandt 周期按同一坐标为 $P_i(\xi)=\sum_{u=0}^{p^t-1}A_{i,u}\xi^u$。若因选择 CM 基点另乘一个 $\xi$ 幂，下面有限本征值及同余阶均不变。

先不依赖任何周期比较。按 $u=b+jM_i$ 分组，$0\le b<M_i,0\le j<p$。以 $\Phi_{p^t}(Y)$ 除这个真整多项式，其次数 $<D_i$ 的余式恰为
$$ \sum_{b=0}^{M_i-1}\sum_{j=0}^{p-2}(A_{i,b+jM_i}-A_{i,b+(p-1)M_i})Y^{b+jM_i}.$$
若 $v_p(P_i(\xi))\ge1$，则这些整数系数全被 $p$ 整除，因为 $1,\xi,\ldots,\xi^{D_i-1}$ 是 $\mathbf Z_p[\xi]$ 的整基。另一方面，任两行差均为偶数，绝对值至多 $4d/3<2p$。所以相同模 $p$ 的两行必准确相等，全部余式为零。反之显然。即在**每一层**
$$ \boxed{P_i(\xi)\ne0\ \Longrightarrow\ 0\le v_p(P_i(\xi))<1.}$$
证明保所有 $p$ 个子项；没有设置一个未计算的同步行等于零。

## 3. 指定 Brandt 周期与原 Rubin 系数的准确相对赋值

BHKO §2.3(2.7)、§3.2.2(3.4) 使 $f^\dag=f-\alpha_p^{-1}\pi(\operatorname{diag}(1,p))f$。在 (2.7) 的未分裂局部基上，$\varsigma_p^{(2i)}\operatorname{diag}(1,p)=p\varsigma_p^{(2i-1)}$。中央标量 $p$ 对原 $f$ 作用为1。在从 $\mathrm G_{2i}$ 到 $\mathrm G_{2i-1}$ 的每个纤维中，第二项的 $f$ 值相等；原 $\nu$ 在阶 $p$ 的核上非平凡，该纤维的完整角色和为0。稳定化第一项系数是1，故在此 BHKO 基点和角色下稳定化周期恰是原 $P_i(\xi)$。其它 CM 基点的平移乘一个根单位；下式取 BHKO 基点，估值对所有这样的平移相同。

直接取 BHKO Theorem 3.12 的双线性平方公式。该定理的完整左侧是 $p^{-s}P(\varsigma^{(n)},f^\dag,\nu)^2$，这里 $s=n=2i$。在本题由 $\epsilon(\pi)=+1$, $p$ 为未分歧好素数使 $\epsilon(\pi_p)=1$，且 $N^+=1$；因 $s\ge1$，定理的最后分支因子为1。$N_{\rm r}$ 仅支持在 $3$。$\pi_K=\psi_{17}\boxplus\psi_{17}^{c}$ 按酉归一及 $s=1/2$ 对应动机归一 $s=1$，又由理想共轭有 $L(1,\psi_{17}^c\nu)=L(1,\psi_{17}\nu^{-1})$。两条扭曲 Hecke 角色在 $p$ 已分歧，在 $3$ 均保留 $\psi_{17}$ 的原分歧（$\nu$ 在 $3$ 未分歧）。所以定理去掉的 $p,3$ 的 Euler 因子原为1；$2,17$ 均保留原分量。从而精确有
$$p^{-2i}P_i(\xi)^2=C\,
\frac{L(1,\psi_{17}\nu)}{\Omega_{\mathbf R,17}}
\frac{L(1,\psi_{17}\nu^{-1})}{\Omega_{\mathbf R,17}},\qquad
C=\frac{2^{\#\Sigma_D}\langle f_{\rm int},f_{\rm int}\rangle\sqrt{|D_K|}\,\Omega_{\mathbf R,17}^2}{8\pi^2(\phi,\phi)}.$$
这里 $\langle\ ,\ \rangle$ 取 Theorem 3.12 的固定双线性配对、$(\phi,\phi)$ 是固定权二新形式的 Petersson 范数。$f_{\rm int}$ 为 BHKO Definition 3.10 中同一原整向量，选其固定全局缩放后，缩放同时在 $P_i^2$ 与双线性范数中出现；在每个 $p\nmid N$ 本向量均同一，故没有 $p$ 变常数。这个等式仅取自 Theorem 3.12 的定理陈述。本段只使用 Theorem 3.12 的双线性定理陈述，不借式(3.7)改变周期尺度。

$C$ 是固定的非零代数常数。任选上节已经由原复平均证明非零的一对 $(p,i)$ 与任一 $\nu$；Galois 共轭保证 $\nu^{-1}$ 的值也非零。定理左侧是非零代数数。按原 Yang 公式，两条 $L/\Omega_{\mathbf R,17}$ 都是非零代数 Klein 和的绝对平方乘原有理系数。反解一次即取到同一个 $C\in\overline{\mathbf Q}^{\times}$，故排除固定有限个有理素数后，在任何 $p$ 进嵌入下 $v_p(C)=0$。$\Omega_{\mathbf R,17}/\varpi_{17}=1-\omega$ 是 $p$ 单位。

固定允许的充分大 $p$。$t=2i-1$ 为奇，BHKO Theorem 4.15 的 $\varepsilon=(-1)^{t-1}=+1$；其中 $1\le k\le t-1$ 且 $(-1)^k=1$ 的项正是 $k=2,4,\ldots,2i-2$，故 $v_p(\delta_\nu(v_+))=-i+S_i/D_i$。Theorem 4.14 和 R303 的原整基比较遂给
$$v_p(L(1,\psi_{17}\nu)/\varpi_{17})
=v_p(\mathcal A_p(t_\nu))-i+S_i/D_i.$$
交换 $\nu,\nu^{-1}$ 时两输入在未分歧基 $K_p$ 上共轭，$\mathcal A_p$ 的估值不变。代入双线性等式后，左侧为 $-2i+2v_p(P_i)$，右侧为 $2v_p(\mathcal A_p(t_\nu))-2i+2S_i/D_i$，故
$$ \boxed{ v_p(P_i(\xi))=v_p(\mathcal A_p(t_\nu))+S_i/D_i .}$$
两端容许同时无穷。$\mu(\mathcal A_p)=0$。因此若 $P_i\ne0$，严格第一位界迫 $v_p(\mathcal A_p(t_\nu))<1$；若 $\lambda_p\ge D_i$，低于 $D_i$ 的项系数皆含 $p$、其余幂次估值亦至少1，矛盾。遂有 $\lambda_p<D_i$，且在这个点首单位项严格主导，故
$$ \boxed{P_i(\xi)\ne0\quad\Longleftrightarrow\quad \lambda_p<D_i-S_i,
\qquad P_i(\xi)\ne0\ \Longrightarrow\ D_i v_p(P_i(\xi))=\lambda_p+S_i.}$$
反向因 $\lambda_p<D_i$ 已保证原 $\mathcal A_p(t_\nu)\ne0$。$D_i-S_i$ 在 $i$ 上严格增加，由此允许导子中所有旋分零组成一个**初始段**。若有前 $r$ 层，前述整平方使 $T^{2e_{\rm cent}}\prod_{j\le r}\Phi_{p^{2j-1}}(1+T)^2\mid\mathcal A_p$，故还须 $\lambda_p\ge2e_{\rm cent}+2\sum_{j\le r}D_j$。

特别，首层非零时 $\lambda_p<p-1$ 且为偶数，故 $\lambda_p\le p-3$；首层零时实际 $\lambda_p\ge 2p$。无条件地，在上一节 $i_0=\lceil(1/2+\varepsilon)\varphi(p+1)/2\rceil$ 处用已经证明的原非消失，得到
$$ \boxed{\lambda_p\le D_{i_0}-S_{i_0}-1,\qquad
 \operatorname{ord}_W\overline{\mathcal B}_{34}=\lambda_p/2-1.}$$
这是对同一个固定原几何来源的有限上界。它不要求另有首层非消失。截点很大，仍未使 $\lambda_p=2$ 对无穷多个 $p$ 成立。

## 4. 原整行的有限域插值次数及二次矩

在非零层置 $H_i(X)=\sum_u A_{i,u}(1+X)^u$。因 $v_p(H_i(\xi-1))<1$ 且系数整，有 $\operatorname{ord}_X\bar H_i=D_i v_p(P_i(\xi))=\lambda_p+S_i$：必须存在小于 $D_i$ 的首单位项，其估值独特最小。对首层 $i=1$，令 $G_p(Z)\in\mathbf F_p[Z]$ 为次数 $<p$、$G_p(u)=A_{1,u}/2\bmod p$ 的插值。$\bar H_1$ 首非零 $k$ 次项为 $2\sum_uG_p(u)\binom uk$。对 $k<p-1-\deg G_p$，被积多项式次数小于 $p-1$，和为0；等于时准确为 $-2[Z^{\deg G_p}]G_p/k!\ne0$。非零层 $G_p$ 非恒（恒时全部行同模 $p$ 即准确同值，primitive 投影为零）。故
$$\boxed{\lambda_p=p-1-\deg G_p.}$$
原强制 $\lambda_p\ge2$。因此对充分大的允许 $p$，包括可能零层，
$$ \boxed{\lambda_p=2\quad\Longleftrightarrow\quad \sum_{u\in\mathbf F_p}u^2 A_{1,u}\ne0\pmod p.}$$
零层时所有 $A_{1,u}$ 相等，且 R736(37) 使其全零；非零层低于二次的前矩必为零，$2!$ 为单位。原 $2,3,17$ 和每个局部第二位都保留，特别 R736(30) 允许直接把右端写为原 $\operatorname{nrd}(\beta)=p^2$ 的全部 $\ell_p(\alpha_\beta)^2 f_{\rm int}(\bar\beta\cdot1)/36$ 之和。通过 R303 原通常 Selmer 不等式，该二次矩非零已经足以给 $\Sha(E_{17}/\mathbf Q)[p^\infty]$ 有限。

可进一步统一排除接近阈值的次数。对任一非恒 $G\in\mathbf F_p[Z]$、$k=\deg G<p$，若其每个值有整数代表 $|z|\le d/3$，令 $H(\theta)=(1-\cos\theta)^8$。在这些 $\theta=2\pi z/p$ 上，对 $p>211$ 有 $\cos\theta\ge-1/2-2\pi/(3p)>-3/5$，故 $H(\theta)\le(8/5)^8<44$。完整圆均值为 $\binom{16}{8}/2^8>50$，非零 Fourier 系数绝对值和至多 $2^8$（由三项式系数的 $\ell^1$ 范数直接给出）。各非零频率 $1\le |h|\le8$ 用一元 Weil 界 $|\sum_{u\in\mathbf F_p}\exp(2\pi ihG(u)/p)|\le(k-1)\sqrt p$；其假设 $p\nmid k$, $p\nmid h$ 已满。两边比较得
$$ k\ge1+\tfrac3{128}\sqrt p. $$
原一元界见 Deligne, *La conjecture de Weil I*, Théorème 8.4，$n=1$，亦见 [Katz 作者稿开头的公式](https://web.math.princeton.edu/~nmk/charsum15.pdf)。首层因此还有 $\lambda_p\le p-2-3\sqrt p/128$。

在任一非零层，固定 $b<M_i$，将整数 $A_{i,b+jM_i}/2$ 在 $j\in\mathbf F_p$ 上插值。至少一个这样的多项式非恒，否则所有块内行准确相等而 $P_i=0$。设最大次数为 $k_*$，上述界给 $k_*\ge1+3\sqrt p/128$。模 $p$ 下 $(1+X)^{jM_i}=(1+X^{M_i})^j$；若在 $X^{M_i}$ 方向的最浅非零次为 $r$，同一有限域矩和给 $r=p-1-k_*$。该层系数在 $X$ 中恰是 $\sum_{b<M_i}c_b(1+X)^b$，至少一个 $c_b\ne0$；独立性使其非零且次数小于 $M_i$，不能被更高块抵消。故实际 $\lambda_p+S_i=\operatorname{ord}_X\bar H_i\le(r+1)M_i-1$。以 $i=i_0$ 得进一步的无条件界
$$ \lambda_p\le\bigl(p-1-3\sqrt p/128\bigr)M_{i_0}-S_{i_0}-1 .$$
此界不把整平方给出的所有高层估值当相互独立的零条件。

外部主文：[BHKO 原文](https://arxiv.org/pdf/2408.13932)，§2.3(2.7)、§3.2.2(3.4)、Thm.3.12 的双线性定理陈述、§4.4.1 Thms.4.14–4.15。原固定 Brandt 值、绝对基点及第一完整 incidence 行见 R736 §§3–8 与公开运行 43705223442。

## 5. 原反圆分平均的分裂素理想格与 Poisson 正下界

保留§1原显式非零段的 $I=2i$、$X=(51/\pi)p^{2i}$、$s\in\{I,I-1\}$、$Z_s(X)$、原理想角色 $\psi=\psi_{17}$ 与 $R_{102p}$。在该段的完整 Mellin 差中可把统一截点大幅缩短：对充分大的惰性 $p$，只要
$$i\ge 100\,\frac{\log p}{\log\log p},$$
该层所有确切阶 $p^{2i-1}$ 的原扭曲均非零。对该截点至无穷的整段一致。下文所有对数为自然对数。

沿用 R724(B1) 的实际 primitive 射线，保留 $(\alpha,\delta)=1$，并模原 $\mu_6$。$2,17,p$ 在 $K$ 中皆惰性。在每个分裂有理素数 $\ell$ 上固定上方一侧 $\pi_\ell$（指素理想）。给每条方向记
$$h_\ell=v_{\pi_\ell}((\alpha))-v_{\bar\pi_\ell}((\alpha)).$$
因子 $(\alpha)$ 在每个这样的共轭对中至多包含一侧，且无惰性或分歧素因子。反之任意有限支撑整数向量 $h$ 给唯一这样的 primitive 理想；$h_K=1$ 给唯一模 $\mu_6$ 的 primitive 生成元。相乘后去掉的有理因子均由分裂素数组成，其有限字符 $\chi_{-3}$ 在这些因子上为1。于是确切相位在自由交换群 $\mathcal D=\bigoplus_{\ell\,\mathrm{split}}\mathbf Z$ 上是一个角色 $u$：
$$ |\alpha|=B(h)=\prod_\ell \ell^{|h_\ell|/2},\quad
w(h)=B(h)^{-1},\quad
\frac{\psi((\alpha))}{N(\alpha)}=w(h)u(h),\quad
u(h)=\prod_\ell\left(\frac{\psi(\pi_\ell)}{\sqrt\ell}\right)^{h_\ell}.$$
最后一个式子用 $\psi(\pi_\ell)\psi(\bar\pi_\ell)=\psi((\ell))=\ell$ 与 $|\psi(\pi_\ell)|=\sqrt\ell$。特别原十七处及其它有限标记始终在 $u$ 内。$h\mapsto[\alpha/\bar\alpha]$ 到模 $p^s$ 范数一群除以 $\mu_3$ 是群同态，原同步即像落在 $\mu_d/\mu_3$（$d=p+1$）；故全同步方向构成子群 $K_s$。目标 tame 有至多 $p+1$ 个元素。

令 $B=p^4$，$H_s\subset K_s$ 为所有 $B(h)\le B$ 的同步方向生成的子群；这些生成元有限。设 $k=\mathrm{rank}(H_s)$。取其中 $k$ 个线性独立短生成元。若任两积的每一边至多由 $r$ 个这样的生成元相乘，则有 integral 生成元复模各至多 $B^r$。若其 projective 像相等，适当乘 $\mu_6$ 后有 $\alpha\bar\beta-\bar\alpha\beta\in p^s\mathcal O_K$。其复模至多 $2B^{2r}$，故在 $2B^{2r}<p^s$ 时只能为零；两积在 $\mathcal D$ 中相等。于是 $r\le k$ 且 $8r+\log_p2<s$ 时，由每个含 $r$ 个不同生成元的子集作积，得
$$ \binom kr\le p+1. $$
这个注入只涉及完整同步群的有限 tame 像；辅助积的两个原 $\mu_3$ 相位已按全局六次单位校正。

记 $L=\log p$、$l=\log L$，取 $r=\lfloor 20L/l\rfloor$。在所述 $i$ 范围有 $s\ge 200L/l-1$，故 $8r+\log_p2<s$。若 $k<r$ 已有 $k\ll L/l$；否则 $\binom kr\ge(k/r)^r$ 使 $k\le r(p+1)^{1/r}\ll L^{1+1/16}$（因 $(\log(p+1))/r\le l/16$ 对充分大的 $p$）。故
$$k^{3/4}=o(\log p)$$
且界对 $i$ 一致。没有要求 $H_s$ 饱和或是直和因子。

选择 $k$ 个不同的分裂素坐标 $J$ 使投影 $H_s\to\mathbf Z^J$ 单射；这由有限支撑有秩 $k$ 的整数矩阵的非零子式给出。$H_s$ 的生成元合共只涉及有限多个坐标 $S$。对 $0<t<1$，圆上的 Poisson 概率密度 $P_t(\theta)=(1-t^2)/|1-te^{i\theta}|^2$ 有 Fourier 系数 $t^{|n|}$，最小值 $(1-t)/(1+t)$。先在 $J$ 坐标取 $t_\ell=\ell^{-1/2}$ 的乘积。$\widehat{\mathbf Z^J}\to\widehat H_s$ 的限制映射满射，因满秩整数矩阵可用 Smith 型化为各 $z\mapsto z^{n_j}$；Haar 概率测度的推前是 Haar 概率。故乘积密度限制后的推前至少
$$ c_J=\prod_{\ell\in J}\frac{1-\ell^{-1/2}}{1+\ell^{-1/2}} $$
乘目标 Haar 概率。$S\setminus J$ 的坐标 Poisson 概率也推前到同一对偶群，两概率卷积仍有此下界，全部 Fourier 系数正是 $w(h)$。因 $J$ 投影单射，$\sum_{H_s} w(h)^\gamma\le\prod_{\ell\in J}(1+\ell^{-\gamma/2})/(1-\ell^{-\gamma/2})$ 对任意 $\gamma>0$；故 Fourier 密度一致绝对收敛。代入原 $u$（或其逆）得实值
$$ c_J\le P(H_s):=\sum_{h\in H_s}w(h)u(h)\le c_J^{-1}. $$
$k=0$ 时两端同为1。把 $J$ 的不同素数排序，第 $j$ 个至少 $j+1$ 且全部至少7，遂 $\log c_J^{-1}=O(\sqrt{k})$、$\log\sum_{H_s}w(h)^{1/2}=O(1+k^{3/4})$。两界对实际素因子及 $H_s$ 统一，故 $P(H_s)\ge p^{-o(1)}$、$\sum w^{1/2}\le p^{o(1)}$。

最后返回原 $Z_s$。$B(h)\le B$ 的全同步集合恰是 $H_s$ 中同一截断，因此在这段可用 R724(B3)。原径向在每条短方向上为
$$R_{102p}(X/B(h)^2)=C_p+O(B/\sqrt X),\qquad C_p=\frac{9\pi}{17\sqrt3}(1+p^{-1}).$$
它来自相同 $X$ 的两个 R724(26)–(28) 项；在所述范围 $X/B^2p^2\to\infty$。总误差 $\ll B X^{-1/2}\sum_{H_s}w(h)$。$H_s$ 的无穷尾满足 $\sum_{B(h)>B}w(h)\le B^{-1/2}\sum_{H_s}w(h)^{1/2}$。原 $K_s$ 中的全部长射线（包括不在 $H_s$ 的）按相对范数段同一 $p+1$ 个格和首线区分；在长首线至多两个 primitive 点，各 $\ll1/B$，偏离首线的带权总量仍每格 $\ll\sqrt X/p^s$。于是
$$Z_s(X)=C_p P(H_s)+O\!\left(
 B X^{-1/2}p^{o(1)}+ B^{-1/2}p^{o(1)}+\frac{p+1}{B}
 +(p+1)\frac{\sqrt X}{p^s}\right).$$
$B=p^4$ 且 $s=2i,2i-1$ 使总误差 $O(p^{-2+o(1)})$。无导子混用：两个子群 $H_{2i}$、$H_{2i-1}$ 分别估计，未令其相等。故 $Z_{2i}\ge p^{-o(1)}$、$|Z_{2i-1}|\le p^{o(1)}$，原 primitive 差的实部严格为正。实性亦由全理想和配共轭给出。先得某一 $L\ne0$，再由原 Rubin 函数在未分歧基上的同层 Galois 轨道性，得该层每个 primitive $L\ne0$。由已证原整行桥，取 $i_*=\lceil100\log p/\log\log p\rceil$ 可在无条件 $\lambda_p<D_{i_*}-S_{i_*}$ 中使用这个新截点；$\log(1+\lambda_p)\ll (\log p)^2/\log\log p$。这段控制未给首层的原二次矩赋非零值。

## 6. 原 primitive 族的固定绝对导子截点

对充分大的惰性好 $p$ 和**每个 $i\ge1000$**，原确切导子 $p^{2i}$ 的每个 $\nu$ 均有 $L(1,\psi_{17}\nu)\ne0$。以下证明不依赖原 signed 或 Rubin 函数的 $\mu,\lambda$；在此前原全层比较下，它给 $\lambda_p<D_{1000}-S_{1000}<p^{1999}$。固定常数 $1000$ 不是最小截点。

保留原 $I=2i$、$s=I,I-1$、$X=(51/\pi)p^{I}$、$\psi=\psi_{17}$、原 $2,3,17$ 有限权以及全 Gaussian。令 $L=\log p$, $Y=L^8$, $A=512$, $B=p^4$。令 $\mathcal P$ 为所有分裂有理素数 $\ell\le Y$ 上方两个素理想的无平方乘积。$2,3,17,p$ 均不在其中。取有限 Dirichlet 多项式
$$D(\nu)=\sum_{\mathfrak d\mid\mathcal P,\ N\mathfrak d\le p^A}
 \mu_K(\mathfrak d)\,\frac{\psi(\mathfrak d)\nu(\mathfrak d)}{N\mathfrak d}.$$
这里只需：若原层所有 $L(1,\psi\nu)$ 均为零，则按 $D(\nu)$ 加权的平均必为零。不需 $D(\nu)$ 为正或为单位。将此有限多项式乘进原 Mellin 公式并保持 $s=I,I-1$ 的准确 primitive 差。合并整理想 $\mathfrak n=\mathfrak a\mathfrak d$ 后，角色恰为 $\nu(\mathfrak n)$，指数为 $e^{-N\mathfrak n/(X N\mathfrak d)}$。按 R724(B1)–(B3) 写 $\mathfrak n=(c\alpha)$，以先前的 $h$、$u(h)$、$b=B(h)=|\alpha|$ 标记坏处互素的 primitive 射线，$K_s$ 为其全部同步子群。对每一 $\mathfrak d\mid\mathcal P$，令 $m_{\mathfrak d}(h)$ 是如下有理素数 $\ell$ 的乘积：$\mathfrak d$ 请求了一个上方素理想，而它没有出现在 $(\alpha)$ 中。每个 $\ell$ 最多乘一次；即使两侧均请求，缺少的一侧由 $\ell\mid c$ 同时补足。因此 $\mathfrak d\mid(c\alpha)$ 当且仅当 $m_{\mathfrak d}(h)\mid c$。所有这些有理素数分裂，$\chi_{-3}(m_{\mathfrak d})=1$。记 $R=R_{102p}$，所得精确等式为
$$ \frac{1}{\varphi(p^{I-1})}\sum_{\mathrm{ord}\nu=p^{I-1}}D(\nu)L(1,\psi\nu)
 =\frac{2}{p-1}(p Z_{I,D}-Z_{I-1,D}),$$
$$ Z_{s,D}=\sum_{h\in K_s}\frac{u(h)}b
 \sum_{\substack{\mathfrak d\mid\mathcal P\\N\mathfrak d\le p^A}}
 \frac{\mu_K(\mathfrak d)}{m_{\mathfrak d}(h)}
 R\left(\frac{X N\mathfrak d}{b^2m_{\mathfrak d}(h)^2}\right).$$
两个 $Z$ 中 $X,D$ 完全相同。这只用原全收敛和与有限算子；$D$ 的辅助因子没有成为新 $L$ 函数或新跳层假设。

**原乘子的两条绝对估计。** 当 $h_\ell=0$ 时，$\mathfrak d$ 在 $\ell$ 处选空、单侧（两种）、双侧的 $m_{\mathfrak d}$ 费用分别为 $1,\ell,\ell$。若 $h_\ell\ne0$，选四项的费用分别为 $1,1,\ell,\ell$，其中两种单侧分别列出。故
$$ \sum_{\mathfrak d\mid\mathcal P}m_{\mathfrak d}(h)^{-1}
 \le 4^{\omega(N\alpha)}\prod_{\ell\le Y}(1+3/\ell)
 \ll 4^{\omega(N\alpha)}(\log(2Y))^C.$$
最后的初等界可取 $\sigma=1+1/\log Y$，于是 $\sum_{\ell\le Y}1/\ell\le e\log\zeta(\sigma)\ll\log\log(2Y)$。又令 $\gamma=1/32$。在 $h_\ell=0$ 处，$\sum(N\mathfrak d)^\gamma/m_{\mathfrak d}$ 的局部因子为 $1+2\ell^{\gamma-1}+\ell^{2\gamma-1}$。在 $h_\ell\ne0$ 处至多 $4\ell^\gamma$。从而
$$ \sum_{\mathfrak d\mid\mathcal P}\frac{(N\mathfrak d)^\gamma}{m_{\mathfrak d}(h)}
 \le \exp(C_\gamma Y^{2\gamma})\,4^{\omega(N\alpha)} b^{2\gamma}.$$
这里 $Y^{2\gamma}=L^{1/2}$。$n$ 有 $k$ 个不同素因子便有 $n\ge(k+1)!$，故 $4^{\omega(n)}=n^{o(1)}$，也有 $\sup_{n\le p^8}4^{\omega(n)}=p^{o(1)}$。不需使用素数定理。

**全部短方向的准确取消。** 对 $b\le B$，$m_{\mathfrak d}\le N\mathfrak d\le p^A$，故其径向参数 $U=X N\mathfrak d/(b^2m_{\mathfrak d}^2)\ge X/(B^2p^A)$。由 R724 的实际有理主项 $R(U)=C_p+O(U^{-1/2})$，$C_p=9\pi(1+p^{-1})/(17\sqrt3)$，误差一致为 $O(p^{4+A/2-i})$；$U/p^2\ge1$ 已满。每个 tame 格在半径 $B$ 内的 primitive 点至多同一直线上的两个：任两独立向量张成的面积至少固定正数乘 $p^s$，而此处 $B^2=p^8\ll p^s$。所以总共 $O(p)$ 个短点。由第一绝对估计，径向替换在全部短点上的误差 $\ll p^{5+A/2-i+o(1)}$。再就这些短点把常数项的 $\mathfrak d$ 补全，尾每点至多
$$p^{-A\gamma}\exp(C_\gamma Y^{2\gamma})4^{\omega(N\alpha)}b^{2\gamma}
 \le p^{-(A-8)\gamma+o(1)}.$$
其总误差 $O(p^{-10})$。完整有限 Euler 和逐坐标给
$$\sum_{\mathfrak d\mid\mathcal P}\frac{\mu_K(\mathfrak d)}{m_{\mathfrak d}(h)}
 =\begin{cases}
 K_Y=\displaystyle\prod_{\ell\le Y,\,\ell\ \mathrm{split}}(1-1/\ell),& h_\ell=0\ \text{对所有这些 }\ell,\\
 0,&\text{其余情形}.
 \end{cases}$$
这是带原理性因子的完整取消，不是把任何单独同步短方向的原角色认成零。$K_Y\ge(\log(2Y))^{-C}>0$，由同一素数倒数和界即得。

**余下无小素因子的同步方向。** 对 $R_0\ge\sqrt Y/2$, $R_0\le B$，记 $S$ 为 $R_0<b\le 2R_0$ 且所有坐标素因子 $\ell>Y$ 的同步 primitive 理想。为每一分裂素数独立随机选一侧，只保留各非零坐标都在所选一侧的理想。每个理想保留概率至少 $2^{-\omega(N\alpha)}\ge(2R_0)^{-o(1)}$，其中 $o(1)$ 在所述整个窗一致，因为 $Y\to\infty$。故存在同一取向的子集 $S'$，$|S|\le(2R_0)^{o(1)}|S'|$；任意 $r$ 个该子集理想相乘后仍 primitive，包括重复选项。

取 $r=\lceil8L/\log(2R_0)\rceil$。每个乘积生成元复模最多 $(2R_0)^r$；$2(2R_0)^{2r}\le2p^{16}(2B)^2<p^s$。如果两个乘积有相同 projective 像（允许全局 $\mu_3$），乘单位后 $\alpha\bar\beta-\bar\alpha\beta$ 属 $p^s\mathcal O_K$，其复模小于 $p^s$，故为零。两个 **primitive** 整理想方向于是准确相等。同步 tame 像至多 $p+1$ 个，所以不同理想乘积也至多 $p+1$。
对定乘积 $\mathfrak b$，其带重素因子数至多 $2r\log(2R_0)/\log Y$。把每一个素因子分派到 $r$ 个有序端点至多 $r^{\Omega_K(\mathfrak b)}$ 种，给原有序分解数上界。因此
$$ |S'|^r\le (p+1) (2R_0)^{2r\log r/\log Y}.$$
现在 $(p+1)^{1/r}\le (2R_0)^{1/8+o(1)}$、$r\ll L$、$2\log r/\log Y\le1/4+o(1)$。故充分大 $p$ 时 $|S|\ll (2R_0)^{1/2}$。除单位方向，所有余下 $b$ 至少 $\sqrt Y$。由 dyadic 求和得它们在 $b\le B$ 的全部绝对权至多 $O(Y^{-1/4})$。此估计不取决于哪些固定非实素数为原 anti-Fermat 同步方向；它们的原贡献早已由真实 $D$ 处理。

**原未取消长部分。** 在 $b>B$ 直接使用原截断 $N\mathfrak d\le p^A$，不补全 Euler 乘积。R724 的 $|R(U)|\ll e^{-1/U}$ 和第一绝对估计使每点的绝对权
$$\ll (\log(2Y))^C b^{-1+1/8}\exp[-b^2/(Xp^A)]$$
对充分大 $p$ 成立。每个 $\mathcal L_{\zeta,s}$ 格的最短方向只有至多两个 primitive 格点，若 $b>B$，合并 $p+1$ 格给 $O((\log(2Y))^CpB^{-7/8})$。偏离首线的点在半径 $R_0$ 内仍每格 $O(R_0^2/p^s)$；对上式单调径向权分部求和，全部偏首线误差
$$ \ll (\log(2Y))^C(p+1)(Xp^A)^{9/16}/p^s .$$
当 $i\ge1000$, $s=2i$ 或 $2i-1$ 时，此界一致 $\ll p^{-2}$，因指数至多 $2-2i+(2i+A)9/16$。长首线也为 $O(p^{-2})$。至此没有删去任何原长质点或有限坏位。

合并得一致的实主项（实性也由共轭成对可见）
$$ Z_{s,D}=C_pK_Y\bigl(1+O(Y^{-1/4})\bigr)+O(p^{-2}),
 \qquad s=2i,2i-1.$$
其 primitive 差为 $2C_pK_Y(1+o(1))$，严格非零。因此该层至少一个原 $L(1,\psi\nu)$ 非零。R1070 实际 Rubin 比值及参考单位在未分歧基上把同一个原零沿整层 Galois 轨道传递，故此层全部 primitive 扭曲非零。上述论证同时给固定 $s$ 中无小分裂素因子的真射线数界；结论仍未把 $i=1$ 的二次矩或特征零中央导数赋非零。
