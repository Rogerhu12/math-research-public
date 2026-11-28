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
