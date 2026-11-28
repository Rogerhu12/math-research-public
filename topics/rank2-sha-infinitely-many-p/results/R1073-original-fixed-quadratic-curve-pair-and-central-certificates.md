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

## 3. 两条原曲线的真实 CM descent 与单一范数正支

沿上节 $b=65,8125$、原共同 $E_1$ 及 $p=6s-1>211$。写 $r_b(\nu)=L(1,\psi_b\nu)/L(1,\psi_1\nu)$、$w_b(\nu)=\theta_b r_b(\nu)$，其中 $\theta_b>0$ 是实际正实六次根。对任一 $\nu$ 确切阶 $p^n$、$n$ 为正奇数，将证明
$$ w_b(\nu)\in K(\mu_{p^n})\cap\mathbf R,\qquad
 \sigma w_b(\nu)= w_b(\nu^a) \quad(\sigma\in G_K,\ \sigma(\zeta_{p^n})=\zeta_{p^n}^a). \tag{1}$$
这里要规范同一个带 $p$ 分歧的 L 值；仅写“代数”不足以指定有限系数域。

取 $M=390p^{n+1}$ 作为有理整模数，同时容纳三条 primitive 导子及该 ring-class 角色。对 $k=1,65,8125$ 取本曲线自身 $\Lambda_k=\varpi_k\mathcal O_K$ 及有理 Néron 微分。写 $\psi_k((r))=r\epsilon_k(r)$，其中 $\epsilon_k$ 是实际理想侧的有限角色，故对全局根单位 $u$ 有 $\epsilon_k(u)=u^{-1}$。记 $\nu(r)=\nu((r))$。类数一、每个理想六个生成元及共轭理想变量代换给
$$ \frac{L_M(1,\psi_k\nu)}{\varpi_k}=
 \frac1{6M}\sum_{r\in(\mathcal O_K/M)^\times}
   \epsilon_k(r)^{-1}\nu(r)^{-1}
   \mathcal E_1^*(r\varpi_k/M,\Lambda_k). \tag{2}$$
$L_M$ 是去掉所有 $M$ 素因子的系列。为核方向，先把它改写为 $L_M(1,\bar\psi_k\nu^{-1})$，后在 $\Re(s)>3/2$ 将 $\overline r/|r|^{2s}$ 按剩余类求和。令 $s\to1$ 时对每一陪集取 $H_1(z,s,\Lambda)=\sum_{l\in\Lambda}(\bar z+\bar l)/|z+l|^{2s}$ 的标准解析延拓；尺度给上式 $1/(6M)$，且余类和在所有 $\sigma$ 之前完成。此 Kronecker 值等于 $\zeta(z)-\eta_\Lambda(z)$，其中 $\eta_\Lambda$ 是从格的 zeta 拟周期实线性延拓。也见 R302 原 Kronecker 规范、Bannai–Furusho–Kobayashi 的 *p-adic Eisenstein–Kronecker series for CM elliptic curves and the Kronecker limit formulas*, §§2–3。

这里使用的挠点值确实和 $G_K$ 作用相容。函数 $M\zeta(z)-\zeta(Mz)$ 是有理模型上的椭圆函数：定义 $Q_M(z)=\sigma(Mz)/\sigma(z)^{M^2}$，则函数等于 $-D\log Q_M/M$，$D=d/dz$，且 $Q_M$ 是带固定首项的 division function，定义于该曲线的有理域。在非零 $M$ 挠点 $z_0$ 以 $t$ 为原 invariant formal logarithm 的平移局部坐标；该函数在 $z=z_0+t$ 的 Laurent 常数为 $M\zeta(z_0)-\eta_\Lambda(Mz_0)=M\mathcal E_1^*(z_0,\Lambda)$。形式参数可取短模型的严格 $-x/y=t+O(t^3)$，换元不改简单极的常数。因此每项是实际点 $Q$ 所定义域内的代数数，且对 $\sigma\in G_K$ 变为同函数在 $\sigma Q$ 的值。

设 $s_k(\sigma)\in(\mathcal O_K/M)^\times$ 为 $\sigma$ 在 $E_k[M]$ 的实际 CM 标量。始终有 $\epsilon_k(s_k(\sigma))=1$：在任一不分歧好素理想的算术 Frobenius 上，CM 主定理给 $s_k\equiv\psi_k(\mathfrak l)\bmod M$；取 $\mathfrak l=(r)$，则 $\epsilon_k(r\epsilon_k(r))=1$。有限像和 Chebotarev 将此式给到全部 $\sigma$。另外 $s_b(\sigma)/s_1(\sigma)\in\mu_6$，由 $F_{\sigma\theta_b}F_{\theta_b}^{-1}$ 是六次 CM 自同构得。$\nu$ 是理想角色，杀全部全局单位，故 $\nu(s_b(\sigma))=\nu(s_1(\sigma))$。应用 $\sigma$ 到(2)并重编号 $r\mapsto s_k(\sigma)r$，得到原 $\nu^a$ 的和乘 $\nu(s_k(\sigma))^a$。两曲线取比后该因子准确相消。

目标在 $M$ 的全部素处都已分歧，参考的额外删除素处只有 $(5),\pi_{13},\bar\pi_{13}$。将参考的有限乘积 $\prod_{\mathfrak l}(1-\psi_1(\mathfrak l)\nu(\mathfrak l)/N\mathfrak l)$ 乘回取比结果，恢复 primitive 比。它在 $G_K$ 下恰按 $\nu\mapsto\nu^a$ 变化，且各单项非零，因为 $|\psi_1(\mathfrak l)|=\sqrt{N\mathfrak l}$。原周期比 $\varpi_1/\varpi_b=\theta_b$，故得到(1)的 equivariance 和系数域。实性由对每条 CM Hecke 系列合并共轭理想得到，因 $\psi_b(\bar{\mathfrak a})=\overline{\psi_b(\mathfrak a)}$、$\nu(\bar{\mathfrak a})=\nu(\mathfrak a)^{-1}$。此外每个 $L(1,\psi_b\nu)\ge0$：在单位化的 $\psi_b\nu|\cdot|^{-1/2}$ 上应用 Yang, *Theta liftings and Hecke L-functions*, Theorem 0.1（作者稿 p.26 的证明），它在有理 idèle 上限制为 $\epsilon_K$；$\nu$ 的限制平凡。原参考非零，所以它严格为正。

令 $\sigma_p$ 是 $K_p/\mathbf Q_p$ 的非平凡元。无分歧二次扩张与 $\mathbf Q_p(\mu_{p^n})$ 全分歧不交，故可固定全部 $\mu_{p^n}$ 延拓 $\sigma_p$。在 $K(\mu_{p^n})$ 内，此作用等于先作一个固定 $K$ 且将单位根求逆的元素，再作复共轭。后一元素固定(1)中每个 $w_b(\nu^{-1})$。原有限输入 $\theta_b\mathcal A_b(t_\nu)=w_b(\nu)$ 于是给整有界函数恒等式
$$ \boxed{\quad (\theta_b\mathcal A_b)^{\sigma_p}(T)=
   \theta_b\mathcal A_b((1+T)^{-1}-1).\quad} \tag{3}$$
这里左边只对系数作用；全式用全部奇数层 primitive 特化和 Weierstrass 有限零点性。因为原质量、一次项都为零，(3)准确给 $u_b:=\theta_b[T^2]\mathcal A_b\in\mathbf Z_p$，包含为零的可能。

若 $(5/p)=-1$，固定 $\sqrt5=\theta_{8125}/\theta_{65}$ 的约化不在 $\mathbf F_p$。对任一 $u,v\in\mathbf Q_p$ 有 $v_p(u\pm v/\sqrt5)=\min(v_p(u),v_p(v))$；等估值时约化的 $1,1/\sqrt5$ 线性独立。因 $2\theta_{65}$ 单位，两条原范数支满足
$$ \boxed{\quad v_p([T^2]\mathcal P_+)=v_p([T^2]\mathcal P_-)
 =\min_{b=65,8125}v_p([T^2]\mathcal A_b).\quad} \tag{4}$$
因此这整个素数类上，只须检出上节的 $D_{i,+}$；$(5/p)=-1$ 与 $p\equiv5\bmod6$ 同时成立的素数有正密度。加号支的复样值为非负实数，它的理想支撑包含全部与模数互素的有理主理想。此项是在原二阶上排除了等估值抵消，没有从复非负性推出其 $p$ 进中央项非零。

Yang原文：[Theta liftings and Hecke L-functions, Theorem 0.1](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。

## 4. 同一二阶检测的固定实二次域数值

保持前节 $w_b(\nu)=\theta_b L(1,\psi_b\nu)/L(1,\psi_1\nu)$ 的全部 $G_K$ 等变及实性。令 $\iota T=(1+T)^{-1}-1$，取原倒数不变参数
$$ S=(1+T)+(1+T)^{-1}-2=T^2/(1+T). $$
在 $p>2$ 的情形，$\mathcal O[[T]]^{\iota}=\mathcal O[[S]]$。实际证明可按首次数逐次消元：不变非零级数的最低项阶必为偶数 $2h$（一次参数首为 $-T$），减去其首系数乘 $S^h$ 后升阶；完备性给唯一表示。原整函数 $\theta_b(\mathcal A_b(T)+\mathcal A_b(\iota T))/2$ 是倒数不变，且系数共轭不变，故准确属于 $S\mathbf Z_p[[S]]$。用 $SH_b(S)$ 记它，则 $H_b(0)=u_b=\theta_b[T^2]\mathcal A_b$。对 $x_\nu=\xi+\xi^{-1}-2<0$、$\xi=\nu(\gamma)\ne1$，
$$ H_b(x_\nu)=\frac{w_b(\nu)+w_b(\nu^{-1})}{2x_\nu}
 \in\mathbf Q(\xi+\xi^{-1}),\qquad H_b(x_\nu)\le0. $$
场的断言来自前节(1)：将 $\nu,\nu^{-1}$ 成对后，$K$ 的共轭若固定 $\xi$，则交换两项；固定 $K$ 且求逆 $\xi$ 的元素亦交换两项。其余 $\xi\mapsto\xi^a$ 则将整式准确送到同一公式的 $\nu^a$。特别所有实共轭均非正。

令 $C_{j}^{\rm re}(S)=\prod_{\{\nu,\nu^{-1}\},\,\operatorname{ord}\nu=p^{2j-1}}(S-x_\nu)$，$B_i^{\rm re}=\prod_{j=1}^iC_{j}^{\rm re}$。各多项式 monic、整、所有非首系数可被 $p$ 整除，并有 $C_{j}^{\rm re}(0)=p$：将 $\Phi_{p^{2j-1}}(1)$ 的共轭根成对即得 $\prod(-x_\nu)=p$，所有 $x_\nu$ 在 $p$ 位归约为零。对 $H_b$ 作整 Weierstrass 除法，余式次数小于 $\deg B_i^{\rm re}$。用上述模 $p$ 不变的完整实节点并在零点作 Lagrange 插值，给一个**有理数**
$$ R_{b,i}:=-p^i\sum_{x=x_\nu:\ B_i^{\rm re}(x)=0}
 \frac{w_b(\nu)+w_b(\nu^{-1})}{2x^2(B_i^{\rm re})'(x)}
 \in \mathbf Q\cap\mathbf Z_p,\qquad R_{b,i}\equiv u_b\pmod{p^i}. $$
求和每一无序对仅计一次。精确有理性由全部 $\mathbf Q$-共轭置换求和项；$p$ 整性属于整个余式。得到固定二次域而非变层数域里的实检测
$$ R_{+,i}=(R_{65,i}+R_{8125,i}/\sqrt5)/2\in\mathbf Q(\sqrt5),\qquad R_{+,i}\equiv\theta_{65}[T^2]\mathcal P_+\pmod{p^i}. $$
在 $(5/p)=-1$ 时，$R_{+,i}$ 的两实共轭有相同 $p$ 估值；若此处原中央皆坏，则 $v_p(N_{\mathbf Q(\sqrt5)/\mathbf Q}R_{+,i})\ge2i$ 对每个 $i$ 成立。反过来只须其中一层严格小于 $2i$。这是真实固定数域的范数而非高层角相位的任意平均；没有给 $R_{b,i}$ 的其他素数分母设单位。

首层另可把 Lagrange 符号全部移除。设 $d=(p-1)/2$ 并令
$$ V_{b,p}:=-\sum_{\{\nu,\nu^{-1}\},\ \operatorname{ord}\nu=p}
 \frac{w_b(\nu)+w_b(\nu^{-1})}{2x_\nu}\in\mathbf Q_{\ge0}\cap\mathbf Z_p. $$
在 $p$ 分歧扩张中，每个 $H_b(x_\nu)\equiv H_b(0)$ 模最大理想。全和为有理数，故落回未分歧基域时该同余精确加强成
$$ V_{b,p}\equiv-d u_b\pmod p. $$
故 $(5/p)=-1$ 时，$v_p(V_{65,p}+V_{8125,p}/\sqrt5)=0$ 当且仅当至少一条原中央二阶为单位。陈述只对首层作此模 $p$ 检测；高层未经付费的除 $p^{2j-2}$ 不是单位。分母原 $L(1,\psi_1\nu)$ 未删除。非负和恰在有某个原分子非零时为正，此复实严格正性仍允许它可被 $p$ 整除。

## 5. 用原秩零 signed 参考清除所有变层 $L$ 分母

保持 $b=65,8125$、$\theta_b>0$、$w_b(\nu)=\theta_b L(1,\psi_b\nu)/L(1,\psi_1\nu)$、$x_\nu=\xi+\xi^{-1}-2$、$\xi=\nu(\gamma)$。沿 R1072 §§7–9 的原 $E_1$ 有理整 toric 向量 $f_1$。具体可在 $N_1=36$ 的有限 Shimura 集上取有理值：好 Hecke 本征值有理、坏位的平凡 toric 不变性是有理置换方程，已付的一维 toric 本征线故为有理线；固定其 primitive 整生成元。令
$$ U(T)=\Theta_1^-(T)\Theta_1^-((1+T)^{-1}-1)\in\mathbf Z_p[[T]]^\times .$$
这里以及下文只需所有充分大允许 $p$。BHKO Rem.4.10(i) 给 $U(0)=((p+1)f_1(x_0(1))/3)^2$，$x_0(1)$ 的原固定值非零。$U$ 倒数不变，故亦属于 $\mathbf Z_p[[S]]^\times$、$S=T^2/(1+T)$。原有限 signed 值为有理整系数有限 Brandt 和除半旋分，故 $U(t_\nu)=|\Theta_1^-(\xi-1)|^2$ 是所取复嵌入下的实际绝对平方。固定 $n=2j-1$，记 $C_j(\xi)=\prod_{k<j}\Phi_{p^{2k}}(\xi)$。BHKO Thm.4.9(b) 的平方式取通常复绝对值，注意 $|z^2|=|z|^2$，原 $N^+_1=1$、$p,3$ 都有原分歧因子一。得
$$ U(t_\nu)=c_*\,\frac{p^{2j}}{|C_j(\xi)|^2}
 \frac{L(1,\psi_1\nu)L(1,\psi_1\nu^{-1})}{\Omega_{\mathbf R,1}^2},\qquad
 c_*=|C(\pi_1,K)/\Omega_{\pi_1}|\,\Omega_{\mathbf R,1}^2>0. \tag{1} $$
所有 $L$ 非负，参考非零；$C(\pi_1,K)$ 中惰性好 $p$ 的局部 epsilon 为一，故 $c_*$ 是全局固定实数。它也是代数数：固定一组允许 $p,\nu$，(1)的左侧与旋分因子代数，两个 $L/\Omega_{\mathbf R,1}$ 的代数性由下段真 Kronecker 式给出；非零即可反解同一个 $c_*$。因此存在一固定正整数将 $c_*$ 清成代数整数；不必把双线性范数未经核对地指定为一。

$E_b$ 的实周期满足 $\Omega_{\mathbf R,b}=\Omega_{\mathbf R,1}/\theta_b$。于是相乘后**没有变层参考 $L$ 分母**：
$$ U(t_\nu) w_b(\nu)=c_*\,\frac{p^{2j}}{|C_j(\xi)|^2}
 \frac{L(1,\psi_b\nu)}{\Omega_{\mathbf R,b}}
 \frac{L(1,\psi_1\nu^{-1})}{\Omega_{\mathbf R,1}} . \tag{2} $$
参考 5、双 13 的 primitive Euler 因子现位于真正的 $L(1,\psi_1\nu^{-1})$ 内。$U$ 乘同一有界函数的中央首项只乘 $U(0)$ 这个单位。

### 固定七乘法对全部层统一清分母

在 $k=1,65,8125$ 的各自模型与 Néron 微分上，取固定有理函数
$$ F_{7,k}(z)=7\zeta_k(z)-\zeta_k(7z)=-\tfrac17 D\log Q_{7,k}(z),\qquad Q_{7,k}=\sigma_k(7z)/\sigma_k(z)^{49}. $$
其水平极只在 $E_k[7]$。因 $\mathcal E_1^*(z,\Lambda_k)=\zeta_k(z)-\eta_{\Lambda_k}(z)$，其中拟周期项实线性，故 $7\mathcal E_1^*(Q)-\mathcal E_1^*(7Q)=F_{7,k}(Q)$。分别用有理整数模数
$$ M_1=6p^{2j},\qquad M_b=390p^{2j}\quad(b=65,8125). $$
各自模数的素支撑就是对应 primitive 角色的全部坏支撑，故前节式(2)无需共同 Euler 删补。乘 $r\mapsto7r$ 双射；$7$ 分裂，原 CM 角色在有理主理想 $(7)$ 的值为7，且 $\nu((7))=1$。前节 $\epsilon_k(7)=1$。所以在各自完整导子和中，真确有
$$ \frac{36 M_k L(1,\psi_k\nu)}{\varpi_k}
 =\sum_{r\in(\mathcal O_K/M_k)^\times}
 \epsilon_k(r)^{-1}\nu(r)^{-1}F_{7,k}(r\varpi_k/M_k). \tag{3}$$
原两个6分别是根单位计数及 $7-1$，二者均已保留。

存在不依 $p,j$ 的正整数 $D_F$，使(3)的全部 $D_F F_{7,k}(Q)$ 都是代数整数。证明如下。所列 $Q$ 的准确有理整数阶为 $M_k$，因为 $r$ 模 $M_k$ 可逆。在任何剩余特征 $\ell$，$M_k$ 的 prime-to-$\ell$ 部分不整除7：若 $\ell=p$ 有固定模数6或390的部分；若 $\ell\ne p$ 则有 $p^{2j}$。所有模型 $j(E)=0$ 均潜在良约化；固定一个数域使它们在原有限坏集上同时良约化，或者逐个该有限集局部扩张。固定良约化模型上 prime-to-$\ell$ 挠点约化单射，故 $[7]Q$ 在特殊纤维不是原点。于是它所在的整截面落在 $\mathscr E_k\setminus\ker[7]$。固定 $F_{7,k}$ 在此开集上无水平极；垂直极的阶由原固定函数和固定模型决定，有限统一有界。在几乎全部素数处固定扩展直接在整数模型上正则（对固定开集上有限呈示的有理函数清一次全局分母）。余下有限个素数各乘固定有理素数幂。正规光滑模型上取消全部余维一极即得正则函数，并且可在所有这些截面逐一评价。经有限扩张得出的全整性对代数数本身仍成立。这给所称 $D_F$，含真实坏位和7，且不声称每个 $F_{7,k}(Q)$ 是单位。$\varpi_k/\Omega_{\mathbf R,k}=(1-\omega)^{-1}$ 是固定代数数，故(3)证明某个固定 $D_0$ 使 $D_0M_k L(1,\psi_k\nu)/\Omega_{\mathbf R,k}$ 是代数整数。

置 $H_b^U(S)=U(S)H_b(S)$，其中 $SH_b=\theta_b\operatorname{sym}\mathcal A_b$，沿前节 $H_b^U\in\mathbf Z_p[[S]],\ H_b^U(0)=U(0)u_b$。每个 $x=x_\nu$ 的值在 $\mathbf Q(\xi+\xi^{-1})$、全部共轭非正。由(2),(3)，有一固定正整数 $D$ 使所有 $D H_b^U(x)$ 在 $p$ 以外处都整：$M_k$ 的变部只有 $p$，且 $x$ 和 $|C_j(\xi)|^2$ 的非单位素因子只在 $p$ 上。后者逐因子用非零 $1-\xi^r$ 的 cyclotomic 范数；$x=(\xi-1)^2/\xi$ 同理。因 $H_b^U$ 整幂级数，该值在惟一的 $p$ 位亦整。于是所有 $D H_b^U(x)$ 都是原实旋分域的代数整数。

### 可取实正的固定分母整数检测

保持 $B_i^{\rm re}$、各无序对节点 $x$，记 $\ell_x=-p^i/(x(B_i^{\rm re})'(x))$。每个 $\ell_x$ 亦在 $p$ 外整，因为不同节点之差为 $(\xi-\xi')(1-(\xi\xi')^{-1})$，涉及的二单位根既非相等亦非互逆。故
$$ D\sum_x\ell_x H_b^U(x)\in\mathbf Z . \tag{4} $$
有理性及 $p$ 整性来自此前严格整余式；$D$ 可 enlarge 一次覆盖三条模型的固定因子。

全部这些实 cardinal 权都有一致界 $|\ell_x|\le2$。先取 $N=p^{2i-1}$ 的所有非平凡根（包括排除的偶层）并作实配对，其完整多项式为 $\xi^{-(N-1)/2}(\xi^N-1)/(\xi-1)$ 写成 $x$ 的 monic 多项式，常数 $N$。逐根微分得其零点评价 cardinal 权为 $-\xi^{(N-1)/2}(1+\xi)$，实绝对值至多2。恢复仅奇层的原权时，须乘所有被删偶层实旋分值与其在零处值的商；每个值是单位根的 $p$ 项几何和乘单位根，绝对值至多 $p$，常数项等于 $p$。故同一界成立。

第 $j$ 层 $t=2j-1$ 的 $H_b^U(x)$ 全共轭迹落在 $p^{t-1}\mathbf Z_p$。因它在实旋分域的 $p$ 处整，亦在完整局部旋分整数环 $\mathbf Z_p[\xi]$ 中；对每个整数幂 $\xi^m$，全部 primitive 共轭和是 $0,-p^{t-1}$ 或 $\varphi(p^t)$。完整旋分迹等于实迹的两倍，2 为单位。于是把第 $j$ 层每一权改为
$$ W_{i,x}=\ell_x+3p^{\max(0,i-2j+2)} $$
得到严格正权，并对全节点精确满足
$$ V^U_{b,i}:=-\sum_x W_{i,x}H_b^U(x)\in D^{-1}\mathbf Z_{\ge0},\qquad
  V^U_{b,i}\equiv-U(0)u_b\pmod {p^i}. \tag{5}$$
合计使用的是完整迹；没有把单列提升到同一精度。所有大于半层的修正已为固定整数3。对每个固定 $p$，两条原非零有界 $\mathcal A_b$ 各最多有限个开盘零，而 $U$ 是单位，其余高导子节点均有非零分子，故充分大 $i$ 两个(5)都是严格正的。$D$ 与 $p,i$ 无关。

对 $(5/p)=-1$、$p\nmid 10D$，于是有普通有理整数
$$ I_{b,i}=D V^U_{b,i},\qquad
 N_i=5 I_{65,i}^2-I_{8125,i}^2\in\mathbf Z .$$
$N_i$ 对所有充分大 $i$ 非零，因为两 $I$ 为严格正整数而 $\sqrt5$ 无理。实际
$$ \boxed{\quad \exists i:\ v_p(N_i)<2i\quad\Longleftrightarrow\quad
 [T^2]\mathcal A_{65}\ne0\ \hbox{或}\ [T^2]\mathcal A_{8125}\ne0 .\quad} \tag{6}$$
在 $\mathbf F_p$ 的5非平方给 $v_p(N_i)=2\min_b v_p(I_{b,i})$（零用无限估值），然后用(5)。严格正以及普通整数化只保证 $N_i\ne0$ 于充分大层，未给 $p^i$ 费用以外的估值。

### 该整数现有的普通绝对值界

可取一个仅依两曲线的常数 $C$ 使 $I_{b,i}\le C p^{10i}$。固定 weight-one Hecke 系列在该中央点的标准 Mellin 完备式，正负两半均绝对受 $\sum_\mathfrak a(N\mathfrak a)^{-1/2}e^{-N\mathfrak a/X}$ 的固定倍数控制，$X\asymp p^{2j}$ 来自单复 Gamma 和 conductor 的平方根（同 R724/R1072 首平均）。$K$ 固定，范数理想计数 $O(x)$，故该和 $O(p^j)$。对原 $\psi_b\nu$、$\psi_1\nu^{-1}$ 均成立；其余导子固定。令 $\xi$ 阶 $p^{2j-1}$。包含全部较低层的几何和绝对值为 $|\xi^{p^{2j-2}}-1|/|\xi-1|\gg1/p$，除以漏掉的 $j-1$ 个奇层因子（各 $\le p$）得到 $|C_j(\xi)|\gg p^{-j}$。因此(2)与逆角色各给 $|U(t_\nu)w_b(\nu)|\ll p^{6j}$。整层 $\sum 1/|x_\nu|\ll p^{4j-2}$，由 $|x|=4\sin^2(\pi a/p^{2j-1})$、用完整整数 $1\le a\le p^{2j-1}/2$ 的平方倒数上界即得。第 $j$ 层权 $\ll p^{\max(0,i-2j+2)}$；把 $p^{10j-2+\max(0,i-2j+2)}$ 加总为 $O(p^{10i})$，常数可与 $i,p$ 无关。由此 $|N_i|\ll p^{20i}$，该全局估计尚未低于(6)的 $p^{2i}$。

原文：[BHKO §4.3, Thm.4.9(b), Rem.4.10(i)](https://arxiv.org/html/2408.13932v3)，[Yang Thm.0.1](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。

## 6. 三个固定七乘法有理函数给原两支及参考的全部层

取 $k=1,65,8125$， $c_1=6,c_{65}=c_{8125}=390$，仍用前文
$\psi_k((r))=r\epsilon_k(r)$，$\theta_1=1$，
$\theta_k^6=k,\ \varpi_k=\varpi_1/\theta_k$。在同一 $E_1$ 固定
$Q_m=\varpi_1/m\bmod\varpi_1\mathcal O_K$；其相容复、$p$ 进嵌入沿前文。写 $F_7=7\zeta_1(z)-\zeta_1(7z)$ 及
$$G_k(P)=\sum_{a\in(\mathcal O_K/c_k)^\times}
 \epsilon_k(a)^{-1}F_7(P+[a]Q_{c_k}) .\tag{A}$$
三个函数均在固定数域上；对两个目标，$(G_{65}+e G_{8125})/2$ 确实只取 $(Na/5)=e$ 的原带权平移点。$F_7$ 在零的留数 $48/7$、在其余 $7$ 挠点的留数 $-1/7$（各用对应不变微分）。不同 $a$ 的极集合不交，因为 $(c_k,7)=1$，$[a-a']Q_{c_k}\in E_1[7]$ 意味 $a=a'\pmod{c_k}$。各函数在原点及整个好惰性 $p$ 进形式开盘正则且积分，对于此处和下文的积分性只需除去一个固定有限素集：固定水平极为准确的非零 $c_k$ 挠点与七挠点之差，约化仍不为零；固定系数的垂直分母有限。$G_k([u]P)=G_k(P)$ 对 $u\in\mu_6$ 成立，因为 $F_7([u]P)=u^{-1}F_7(P)$ 及 $\epsilon_k(u)=u^{-1}$。

固定 $p\equiv5\bmod6$ 充分大，$p$ 不除 $7c_k$。$\psi_k((p))=-p$，故 $\epsilon_k(p)=-1$。若非平凡反圆分 $\nu$ 的确切导子为 $p^s$，分别用原两个模数 $M_k=c_kp^s$，Kronecker 七乘法公式（前文式(3)的证明对每个 $s\ge1$ 相同）和 CRT 代表 $r=c_kz+p^sa$ 给
$$\frac{L(1,\psi_k\nu)}{\varpi_1}
=\frac{(-1)^s}{36c_kp^s}
 \sum_{z\in(\mathcal O_K/p^s)^\times}\nu(z)^{-1}G_k([z]Q_{p^s}).\tag{B}$$
这里 $\nu(r)=\nu(z)$ 由于 $c_k$ 有理，$\epsilon_k(r)=(-1)^s\epsilon_k(a)$；原复点分解在 $Q_m$ 的固定相容选择上逐项有效。$F_{7,k}(z/\theta_k)=\theta_k F_7(z)$ 正与 $\varpi_k/\varpi_1$ 相消。无须将参考的 $5$、双 $13$ 好 Euler 因子删去。$s=0$ 直接用原固定模数得 $G_k(0)=36c_k L(1,\psi_k)/\varpi_1$；故目标两者为零，参考非零。即使导子奇数时 (B) 两边为零，仍保留 $(-1)^s$。

### 原严格 Lubin–Tate 上的全核迹及保留精度的 Katz 回返

有全曲线有理函数等式
$$\sum_{R\in E_1[p]}F_7(P+R)=pF_7([p]P).$$
两边的极都是 $E_1[7p]$；因 $[p]$ 置换 $E_1[7]$ 且固定原点，每个极左边仅一项，右边的 $p$ 正抵消拉回微分的 $p$，故留数相同。常数差为奇函数故为零。在(A)送 $a\mapsto pa$ 后得
$$\sum_{R\in E_1[p]}G_k(P+R)=-p G_k([p]P),\quad
 \psi G_k=-G_k/p,\quad g_{k,p}=pG_k+G_k\circ[p],\quad\psi g_{k,p}=0.\tag{C}$$
归一 $\psi$ 包含 $p^{-2}$ 和零点。原 $E_1$ 的 R663/R1065 严格整形式坐标及 $\phi H=H\circ[p]$ 给 $g_{k,p}=p(1-\phi\psi)G_k$。把包含固定挠点的有限局部扩域 $F$ 的整数环分解于 $\mathcal O_{K_p}$ 的有限自由基；(C) 与 $\psi$ 的原分解式 R1065(K7) 在每个分量上成立。R1065(K9)–(K12) 的 Berger Theorem A 因此给唯一整 Galois–Katz 测度（各分量的同一基扩张）$\mu_{k,p}$，支撑 $\mathbb T^\times$，且 $\mu_{k,p}(c_n)=[v^n]g_{k,p}$。对每个实际点 $Q$ 在更大有限扩域的完成张量中取 $\mathbf e_Q=\sum v_Q^n\otimes c_n$；实际 $\mu_{k,p}(\mathbf e_Q)=g_{k,p}(Q)$。

定义完整带权点测试
$$\mathcal G_{\nu,s}=\sum_{z\in(\mathcal O_K/p^s)^\times}\nu(z)^{-1}\mathbf e_{[z]Q_{p^s}}.$$
有限角色系数亦在同一张量标量扩张中。对 $s\ge2$ 的 primitive，$G_k([p][z]Q_{p^s})$ 经模 $p^{s-1}$ 下降而 $\nu$ 在末纤维非平凡，完整加和为零。于是
$$\mu_{k,p}(\mathcal G_{\nu,s})=36c_k(-1)^s p^{s+1}\,L(1,\psi_k\nu)/\varpi_1.\tag{D}$$
对允许 $s=2j$ 参考值非零；用原 BKO (3.3) 的 coLie/Betti 运输（前节）以及
$\mu_{e,p}=(\mu_{65,p}+e\mu_{8125,p})/2$ 得
$$ \mathcal P_e(t_\nu)=\frac{c_1}{390}
\frac{\mu_{e,p}(\mathcal G_{\nu,s})}{\mu_{1,p}(\mathcal G_{\nu,s})} .\tag{E} $$
R1065、R1066 原两 $H_{34},H_{102}$ 使用 $p$ 变的物理 Hall 来源和第一挠层负二测试。本式使用固定的 (A) 及全部导子的原角色测试。对任意 $i\ge1$，精确的直接读者是
$$-\frac{c_1p^i}{390}\sum_{j=1}^i\sum_{y=t_\nu:\ \operatorname{ord}\nu=p^{2j-1}}
\frac{\mu_{e,p}(\mathcal G_{\nu,2j})}
 {y^3 B_i'(y)\mu_{1,p}(\mathcal G_{\nu,2j})}
\ \equiv [T^2]\mathcal P_e\pmod{p^i}.\tag{F}$$
这里 $B_i=\prod_{j\le i}\Phi_{p^{2j-1}}(1+T)$。证明是 $\mathcal P_e/T^2$ 的整 Weierstrass 余式在零处的 Lagrange 式，$B_i(0)=p^i$；(E)只是逐节点的真实转换。亦可先对各 $k$ 使用相同的 (D)，代回原 $U$ 插值的 $U(t_\nu)w_k(\nu)$，保留 $U(0)=((p+1)f_1(x_0(1))/3)^2$ 和前节正权整数的全部精度。没有将任一有限普通 Taylor 项指定为上述导子测试。

### 全部有限群环的原来源等式

类数一且 $p$ 惰性。局部单位映射 $\ell_s:(\mathcal O_K/p^s)^\times\twoheadrightarrow\Gamma_{s-1}$，$\Gamma_{s-1}=\Gamma/\Gamma^{p^{s-1}}$；核为 $\mu_{p^2-1}$ 和 $1+p\mathbf Z_p$ 的像。取与 (B) 同侧的互反约定 $\nu(z)=\nu(\ell_s z)$。在含全部挠点的局部数域群环定义
$$D_{k,s}=(-p)^{-s}\sum_{z\in(\mathcal O_K/p^s)^\times}G_k([z]Q_{p^s})[\ell_s(z)^{-1}],\qquad s\ge1.\tag{G}$$
从 $s+1$ 投影至 $s$，每个原有单位 $z$ 的全部 $p^2$ 个提升正给 $[z]Q_{p^s}$ 的全 $[p]$ 逆像；(C)的 $-p$ 抵消一次规范化，故 (G) 严格相容。在平凡角色上，
$$D_{k,s}(1)=(-p)^{-1}\sum_{0\ne R\in E_1[p]}G_k(R)
=(1+p^{-1})G_k(0).\tag{H}$$
在每个非平凡角色、确切导子 $p^a$（$2\le a\le s$）上，由相容性和 (B) 得 $D_{k,s}(\nu)=36c_k L(1,\psi_k\nu)/\varpi_1$。若 $a$ 偶，逐点以原 BKO 比值比较；若 $a$ 奇，则三条 $W(\psi_k\nu)=-1$，两侧 L-值皆零。这里用 Li–Xu, *On the Mordell–Weil rank of certain CM abelian varieties over anticyclotomic towers*, 出版 Theorem 3.12(ii)：本题 $j=0,f(\psi_{k,p})=0,W(\psi_k)=+1$，非平凡角色序指数 $n=a-1$，故符号 $(-1)^{n+1}=(-1)^a$。在平凡处用(H)及 $\mathcal A_b(0)=0$。所有特征零角色已尽，有限 Fourier 单射证明逐群环的准确等式
$$\boxed{D_{b,s}=\frac{390}{c_1}\mathcal A_b(\gamma-1)D_{1,s}\quad(b=65,8125;\ s\ge1).}\tag{I}$$
这里的 $\gamma$ 取有限层像，整幂级数在 $p$ 进群环中收敛。$(-p)^{-s}$、原参考、反号零层和初次 $(1+p^{-1})$ 均保留。若 $[T^2]\mathcal A_b=0$，已证 $\operatorname{ord}_0\mathcal A_b=2\operatorname{ord}_0\widehat J_{b,p}$ 遂给 $\mathcal A_b=T^4K_b$, $K_b\in\mathcal O[[T]]$；(I)要求每一层的同一完整有理点轨道为 $(\gamma-1)^4$ 作用于 $(390/c_1)K_bD_{1,s}$。这些关系没有给出某一充分大 $p$ 的 (F) 首次非零精度。

Li–Xu [作者原版Th.3.11(ii)](https://arxiv.org/html/2502.12648v1#S3.SS3.SSS1.Thmtheorem3)，相应[期刊Th.3.12(ii)](https://doi.org/10.1016/j.jnt.2026.06.001)。Berger 模块、$\mathbf e_Q$ 与严格形式坐标按 R1065 §§2–3；BKO、BHKO 及 Néron 周期按前文归一。

## 7. 三原有理函数的共同有理下降与整 Volkenborn 误差

保留固定来源(A)–(I)。置 $\omega=(-1+\sqrt{-3})/2$、$u_0=\bar\varpi_1/\varpi_1=(1-\omega)/(1-\bar\omega)=-\omega$。有
$$ \frac{\theta_k G_k}{1-\omega}\in\mathbf Q(E_1).\tag{J} $$
确实，$\sigma\in G_K$ 在 $E_1[c_k]$ 及 $E_k[c_k]$ 的 CM 作用分别记 $s_1,s_k\in(\mathcal O_K/c_k)^\times$。前文的 CM 射线有限角色关系 $\epsilon_k(s_k)=1$ 来自好位 Frobenius 的 $\psi_k(\mathfrak q)$ 生成元及 Chebotarev。令 $u_\sigma=\theta_k^\sigma/\theta_k\in\mu_6$。因 $(x,y)\mapsto(u_\sigma^2x,u_\sigma^3y)$ 在不变微分上乘 $u_\sigma^{-1}$，比较实际 $F_{\theta_k}$ 共轭得 $s_k=u_\sigma^{-1}s_1$，故 $\epsilon_k(s_1)=u_\sigma^{-1}$。直接在(A)重标得 $G_k^\sigma=\epsilon_k(s_1)G_k$。复共轭使 $Q_c\mapsto[u_0]Q_c$，且 $\epsilon_k(\bar a)=\overline{\epsilon_k(a)}$ 由有理曲线的 Hecke 角色得来；$F_7$ 是实际有理除点对数导数。故 $\overline{G_k}=u_0^{-1}G_k$；$\overline{1-\omega}=u_0^{-1}(1-\omega)$ 证明(J)。

### 原核轨道的开盘延拓及恰当的整误差

记 $q=p^2,d=q-1,r_j=p^{-1/(d q^{j-1})}$，取 R1065 的 $E_1$ 严格坐标 $[p]v=pv-v^q$，$z(v)=\log_E(v)$ 以不变微分定标。对 $a\in\mathcal O_{K_p}^\times$ 写 $S_af(P)=f([a]P)$。选实际 $\ell(a)=\gamma$ 的 $\eta\in1+p\mathcal O_{K_p}$，取 $\beta=1+p$。置
$$B_k=d^{-1}\sum_{t\in\mu_d} S_tG_k,\qquad
 V_k=\lim_{m\to\infty}p^{-m}\sum_{j=0}^{p^m-1} S_\beta^j B_k.\tag{K}$$
平凡及所有反号源均已经(G)–(I)单独检验。此处(K)系数域可取 $K_p(E_1[c_k])$（有限非分歧，因为好约化和 $p\nmid c_k$），并合先前 $\theta_k\in K_p$。所有 $B_k$ 系数整，且 $\psi$ 与各单位拉回交换。

给第 $s$ 挠半径的 Tate 算子范数 $\|\cdot\|_{r_s}$。$\|[p^s]v\|_{r_s}=p^{-1}r_1$，因为 $[p]$ 将各 $r_i$ ($i>1$) 送 $r_{i-1}$，恰在 $r_1$ 时两项同范数，Gauss 范数取最大值。等式可逐次用 $[p]$ 的盘满射，或用缩放化简后非常数多项式之复合仍非常数。形式群加法的整估计和 $v_p(\beta^{p^{s-1}}-1)=s$ 给
$$\|S_\beta^{p^{s-1}}-I\|_{r_s}\le r_s^{-1}\|[p^s]v\|_{r_s}
\le p^{-1}r_1/r_s.$$
对一般幂级数用幂差分解得同一算子范数。先作 $p^{s-1}$ 项平均，代价至多 $p^{s-1}$；余下平均按 R1070 §6 的 $\sum_{j\ge0}(-1)^j D^j/(j+1)$，其中 $D=S_\beta^{p^{s-1}}-I$ 的上界足以使整个尾算子范数至多一。因此(K)在每个 $r_s$ 收敛，$\|V_k\|_{r_s}\le p^{s-1}$。同样 $\|S_\eta-I\|_{r_s}\le r_s^{-1}\|[p]v\|_{r_s}<1$，故全部整 Rubin 系数的 $\mathcal A_b(S_\eta-I)$ 在每个这样的盘上收敛且范数至多一。

在任一准确 $p^s$ 挠点 $P$，$B_k$ 后的 $\beta$ 平均在 $p^{s-1}$ 次后稳定；$V_k(P)$ 正是 $((q-1)p^{s-1})^{-1}$ 乘以 $\ker\ell_s$ 的完整原轨道和。(I) 用 $[\ell_s(z)^{-1}]$ 这一选向，乘 $[\gamma]$ 遂对应 $S_\eta$，得
$$\Delta_b:=V_b-65\mathcal A_b(S_\eta-I)V_1=0\quad\text{于全部 } E_1[p^\infty].$$
原点由 $V_b(0)=\mathcal A_b(0)=0$ 单验。$z$ 的所有零恰为这些简单挠点：$[p^m]v$ 最终进入 $z$ 的等距小盘，且不变微分处处非零。故商 $h_b=\Delta_b/z$ 在每个 $r_s$ 盘解析（可在有限扩域逐零 Weierstrass 整除再下降）。通过 $z([p^s]v)=p^s z(v)$ 与小盘内 $z$ 等距得 $\|z\|_{r_s}=p^{s-1}r_1$。Gauss 范数乘性于是给
$$\boxed{\Delta_b=z h_b,\quad \|h_b\|_{r_s}\le r_1^{-1},\quad h_b\in\mathcal O_{K_p(E[c_b])}[[v]],\quad \psi h_b=-h_b.}\tag{L}$$
整性用 $s\to\infty$、非分歧系数和 $r_1^{-1}<p$。末式来自 $\psi G_k=-G_k/p$ 和 $\psi(zh)=z\psi(h)/p$；在任一所需较小盘对有限核迹取连续极限即可。$h_b$ 也是 $\psi$-integral，故 R1065 的 Berger 对偶给实际整 Galois–Katz 泛函；此处没有断言它支撑于单位。$h_b([t]P)=t^{-1}h_b(P)$ 对 $t\in\mu_d$。

### 原不变导数的全权等式

记 $M_N(f)=\partial_{\omega_1}^N f(0)$。对每个 $N>0$、$d\mid N$，在 $z$ 的收敛小盘逐项求导即得
$$b_N\{M_N(G_b)-65\mathcal A_b(\eta^N-1)M_N(G_1)\}
  =N M_{N-1}(h_b),\qquad b_N=\frac{N\log\beta}{\beta^N-1}\in\mathbf Z_p^\times.\tag{M}$$
平均的特征值由有限等比和除 $p^m$ 真取极限，$S_\eta$ 对 $z^N$ 的特征值是 $\eta^N$。因此 (M) 的右侧保留了(L)式可能出现的一阶误差。更具体，由 $h_b$ 的整 Katz 泛函，$M_{N-1}(h_b)=\mu_{h_b}(X^{N-1})$，其中 $X(\xi)=\mathbf t'_\xi(0)$；这是在对数坐标用 $\mathbf t_\xi=\exp(X(\xi)z)$ 回到实际有限 Taylor 系数。$v_p(X(\xi))\ge\tau=p/(p^2-1)$ 给
$$v_p(M_{N-1}(h_b))\ge\lfloor(N-1)\tau\rfloor=N\tau-1.$$
对 $N=d p^a$、$a$ 充分大，实际 $v_p(M_N(G_1))=N\tau-1$：$\mu_{g_1}$ 支撑于单位，且 $g_1(0)=(p+1)G_1(0)$ 为单位。取任一 primitive $\xi_0$。$Y=X(\xi)^d/p^p$ 的单位剩余类在 $\mathbb T^\times$ 上恒定，因为 $X(u\xi_0)=uX(\xi_0)$ 且 $u^d\equiv1\bmod p$；由 Galois 等变其剩余类在 $\mathbf F_{p^2}^\times$。$Y^{p^a}$ 在单位上一致趋近其剩余 Teichmüller 提举的 $p^a$ 次方（该提举可随 $a$ 在有限两值中交替）；这是固定 $Y(\xi_0)$ 与所有 $u^d\in1+p\mathcal O$ 的一致估计。在单位外用零延拓，调用支撑及整 Galois 对偶，得 $\mu_{g_1}(X^N)/p^{N\tau}$ 在大 $a$ 时为单位。由 $M_N(g_1)=(p+p^N)M_N(G_1)$ 得上式。因而
$$\frac{M_N(G_b)}{65 M_N(G_1)}\equiv\mathcal A_b(\eta^N-1)\pmod{p^a}\qquad(N=d p^a,\ a\text{ 充分大}).\tag{N}$$
(M)中 $v_p(N)=a$ 只支付了一阶。二阶系数仍由上一节全(F)精度读出；(N)自身不能把 $\eta^N-1$ 的二次项和有界误差分开。
