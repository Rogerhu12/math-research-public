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

## 8. 三个原权一来源与同一整 Morava 盘的完整恒等式

保留前述(A)–(I)，写 $E=E_1$、$c=390$。全水平结构 $\alpha:\mathcal O_K/c\buildrel\sim\over\to E[c]$ 取 $a\mapsto[a]Q_c$，参考 $c_1=6$ 由同一水平结构下推。对任何具此水平结构的椭圆曲线、非零不变微分 $\kappa$，定义
$$ f_k(E',\alpha',\kappa)=
 \sum_{a\in(\mathcal O_K/c_k)^\times}\epsilon_k(a)^{-1}
 F_{7,(E',\kappa)}(\alpha'_{c_k}(a)),\qquad k=1,65,8125.\tag{P1}$$
这里不要求 $E'$ 有 CM，$a$ 用固定水平结构标记。七除点函数的对数导数随微分换基 $\kappa\mapsto u\kappa$ 乘 $u^{-1}$。因此这是真正的权一模形式在非尖点模空间上的正则截面：可在通用椭圆曲线局部微分框架中使用七除法多项式的有理对数导数；其水平极在七挠点，而所有被评价点阶为 $c_k$，互素。由固定有限呈示清除固定有限集后，在每个好特征及正规通用族上均正则。其在本文的完整形式邻域的整有界性只用这个结论，无需尖点增长估计。原三个 $G_k(0)=f_k(E,\alpha,\omega_E)$。

取循环子群 $C\subset E[p^s]$，$|C|=p^s$，$q_C:E\to E_C=E/C$。先取唯一 $q_C^*\kappa_C=\omega_E$ 的代数微分。七乘法有理函数在任意该同源下满足
$$\sum_{R\in C}F_{7,E}(P+R)=F_{7,(E_C,\kappa_C)}(q_CP).\tag{P2}$$
两边的极集相同。对每个 $q_C(P)\in E_C[7]$，有且仅有一个 $R\in C$ 使 $P+R\in E[7]$；$q_C$ 在七挠点上是同构，零与非零留数分别匹配，归一微分使留数相等。差是奇常数，所以为零。记 $F_{k,C}=f_k(E_C,q_C\alpha,\kappa_C)$，则逐项平移给 $\sum_{R\in C}G_k(R)=F_{k,C}$。

对 $g\in\Gamma_{s-1}$，所有 $z$ 满足 $\ell_s(z)=g$ 的点 $[z]Q_{p^s}$，按其生成的循环子群分为恰 $p+1$ 份。确因全几何原点参数为 $(\mathcal O_K/p^s)^\times$，同一生成子群的轨道为 $(\mathbf Z/p^s)^\times$；该核在 $\ker\ell_s$ 中的商等于 $\mu_{p^2-1}/\mu_{p-1}$。令 $Y_{k,s}(g)$ 为此 $p+1$ 个 $F_{k,C}$ 的全和。对 $s\ge2$，取父 $C\mapsto pC$ 逐个双射到 $g$ 之父的 $p+1$ 个子群（相同的 Teich 代表模有理标量在各层不同）。因 $C$ 的生成元集合为 $C\setminus pC$，故 (G) 中 $[g^{-1}]$ 的未除系数为
$$ H_{k,s}(g)=Y_{k,s}(g)-Y_{k,s-1}(g\bmod\Gamma_{s-2}).\tag{P3}$$
$s=1$ 的父重复 $p+1$ 次，得 $H_{k,1}=Y_{k,1}-(p+1)G_k(0)=(-p-1)G_k(0)$，故三个 $Y_{k,1}=0$。若 $s\ge3$ 奇，(B)及 Li–Xu 的负根号使 (G) 在所有新 primitive 角色上为零。其完整 Fourier 逆与层间推前于是给每个 $g$ 的 $(-p)^{-s}H_{k,s}(g)=p^{-1}(-p)^{-(s-1)}H_{k,s-1}(\bar g)$。代入(P3)得到 $Y_{k,s}(g)=Y_{k,s-2}(\bar{\bar g})$。所以
$$ Y_{k,s}(g)=0\ (s\text{ 奇}),\qquad H_{k,s}(g)=Y_{k,s}(g)\ (s\text{ 偶}).\tag{P4}$$
全体真参考也满足此式，其平凡处仍是(H)的 $1+p^{-1}$。

### 在同一整变形盘正面比较两个原 Rubin 元素

在包含固定水平结构和 $K_p$ 的有限非分歧整数扩张 $W$ 上工作，必要时扩大剩余域以定义全部特殊纤维标记。偶数 $s$ 时循环子群在好模型的有限平坦闭包有连通特殊纤维（$E$ 超奇异），因此原商同源约化为相对 Frobenius $\operatorname{Fr}^s$ 后接唯一同构。用该同构标记目标曲线的约化为 $E^{(p^s)}=E$ 的特殊纤维。实际 $E/\mathbf F_p$ 的 Frobenius 满足 $\operatorname{Fr}^2=[-p]$，故 $q_C\alpha$ 的约化为 $[(-p)^{s/2}]\alpha$。把水平结构改为
$\alpha'_C=q_C\alpha\circ[(-p)^{-s/2}\bmod c]$，其约化即固定 $\bar\alpha$。这不改变任何 $F_{k,C}$：$\epsilon_k(-p)=\epsilon_k(-1)\epsilon_k(p)=1$。所有偶层的三个曲线来源由此全落在同一带全水平结构的光滑形式邻域。$\bar\alpha$ 含完整至少三级水平，故没有模堆叠的自同构歧义。

由 Serre–Tate 变形等价，该邻域亦为带标记的一维高度二 $p$-可除群 $X=\widehat E$ 的变形盘 $\operatorname{Spf}W[[u]]$；选原 canonical 提升为 $u=0$。令 $\Omega$ 为通用不变微分的任一整自由基，使其在 $0$ 等于原 $\omega_E$。把 (P1) 记为此框架中的 $f_k(u)\in W[[u]]$。此有界性来自整通用椭圆曲线的七除点式和固定水平，绝不在全盘使用水平 Gauss–Manin 坐标。实际点记为 $u_C$，定义 $a_C$ 由
$$q_C^*\Omega(u_C)=a_C\omega_E,\qquad F_{k,C}=a_C f_k(u_C).\tag{P5}$$
$|a_C|$ 不能删除。其准确赋值为
$$ v_p(a_C)=\sum_{j=1}^{s}\frac{(p-1)p^{j-1}}{(p^2-1)p^{2(j-1)}}=
\frac{p}{p^2-1}(1-p^{-s}).\tag{P6}$$
确实整形式同源在任何整参数上 Weierstrass 的秩就是 $p^s$（特殊纤维纯不可分），其 distinguished 核多项式根为 $v_R$、$R\in C$，且余下是整单位；原点导数的赋值是全体 $R\ne0$ 的 $v_p(v_R)$ 之和。准确阶 $p^j$ 的每个点的赋值是上一节 $r_j$ 给出的 $1/((p^2-1)p^{2(j-1)})$。

每个 $t\in\mathcal O_{K_p}^\times$ 在 $\bar X$ 上有 CM 自同构。改变标记的通用性质给变形盘自同构 $\Phi_t$ 和唯一相容的通用 $p$-可除群同构
$U_t:X_u\to X_{\Phi_t(u)}$，其特殊纤维是 $[t]$；可逐 Artin 整层取通用标记再取逆极限，形式群同态的刚性保证相容。它们固定原 canonical 点，那里 $U_t=[t]$。写
$$ U_t^*\Omega(\Phi_t(u))=d_t(u)\Omega(u),\qquad
 \mathcal T_t f=(d_t(u)/t) f(\Phi_t(u)).\tag{P7}$$
$d_t\in W[[u]]^\times,d_t(0)=t$，这给有界的群作用；有理 $t\in\mathbf Z_p^\times$ 在所有变形上本就为标量，故 $\mathcal T_t=I$。准典提升上的 $q_{tC}\circ[t]$ 正好经 $q_C$ 下降为 $p$-可除群同构 $X_C\to X_{tC}$；其约化与 $\operatorname{Fr}^s$ 交换，因为偶数 $s$ 的 $\operatorname{Fr}^s$ 是标量，故其约化恰为 $[t]$。于是它就是 (P7) 在 $u_C$ 的同构。特别
$$ \Phi_t(u_C)=u_{tC},\quad t a_{tC}=a_C d_t(u_C),\quad
 F_{k,tC}=a_C\,(\mathcal T_t f_k)(u_C).\tag{P8}$$
这同时支付了点标记和全部同源微分比；没有把随 $C$ 的 Hodge 基逐条设一。

记 $P_\Delta=(p+1)^{-1}\sum_{t\in\mu_{p^2-1}/\mu_{p-1}}\mathcal T_t$，有理标量作恒等使陪集代表无关。取 $\ell(\eta)=\gamma$、$\eta\in1+p\mathcal O_{K_p}$，依此前群环取向。$\Phi_\eta$ 固定零；其切线乘子模 $p$ 为1，因为单位作用连续，pro-$p$ 群到有限剩余域乘法群的连续特征平凡（亦见下节特征零的准确乘子）。$d_\eta(0)/\eta=1$。因此在每个严格闭 $r<1$ 有 $\|\mathcal T_\eta-I\|_r<1$：对 $f\circ\Phi-f$ 用 $r^{-1}\|\Phi-u\|_r$，乘法框架用 $\|d_\eta/\eta-1\|_r$，整高阶尾各至多 $r$。$\mathcal A_b(\mathcal T_\eta-I)$ 在每个此盘收敛；因全部系数和作用的整界为一，结果在整个开盘仍是 $W[[u]]$。

由(P4),(P5),(P8)，(I)在每个偶层每个 $C$ 除去同一个非零 $(p+1)a_C$ 给出下式在 $u_C$ 的准确等式。它有无穷不同的该类点：$X_C$ 的有理自同态代数是 $K_p$，因为它与原群同源，且形式对数导数嵌入交换域、$T_p$ 嵌入 $M_2(\mathbf Q_p)$，含 $K_p$ 的交换代数即 $K_p$。相对原有理 Tate 空间，$X_C$ 的格为 $\mathcal O_{K_p}+p^{-s}v\mathbf Z_p$，$v$ 是单位。其乘子环为 $\mathbf Z_p+p^s\mathcal O_{K_p}$（乘 $v^{-1}$ 定标后直接算）；反向包含也成立，因为 $m+p^s a$ 保存 $C$，可从原整群下降。故不同 $s$ 的整自同态环判别式不同。所有点都在开盘。离散赋值整数环的非零有界幂级数只有有限个开盘零，遂得
$$\boxed{P_\Delta f_b=65\,\mathcal A_b(\mathcal T_\eta-I)P_\Delta f_1
\quad\text{在 }W[[u]],\quad b=65,8125.}\tag{P9}$$
它比较同一原全模形式来源及同一 $\Gamma$ 的有界函数。R1065/R1066 的 Hall–Katz 第一挠层负二测试没有这个同源变形盘恒等式。此前物理 $E_1$ 盘中沿有理单位的 Volkenborn 算子含 $z h_b$；在(P9)有理单位从循环子群的定义已整除，所余 $p+1$ 是同源轨道而本来可逆，故无需该误差。

## 9. 同一个固定 de Rham 来源在任意中央精度的准确系数

保留(P9)。在特征零的原模曲线中央形式邻域工作；这些操作仅作逐 Taylor 系数比较。记 $e_0,e_1$ 为通用 $H^1_{\rm dR}$ 中水平延拓的中央向量 $\omega_E,x\omega_E$。在 $y^2=x^3+1$ 上二者的 CM 特征是 $t,\bar t$：先对六根单位验不变微分与第二类微分，再由 $K$ 作用及局部连续性延到 $\mathcal O_{K_p}$。GM 常微分方程在特征零形式盘上有唯一水平解。写实际 Hodge 线的任一框架
$$ \Omega=h(u)(e_0+w(u)e_1),\qquad h(0)=1,w(0)=0.\tag{Q1}$$
Kodaira–Spencer 同构给 $w'(0)\ne0$，故 $w$ 是特征零**中央形式**参数。对权一形式定义中央数列
$$ c_k(n)=[w^n]h(u) f_k(u).\tag{Q2}$$
这里 $f_k(u)$ 是用 $\Omega$ 评价的(P1)，所以 $h f_k$ 与临时框架无关。也可完全在固定数域上构造(Q1),(Q2)：在 $y^2=x^3+v x+1$ 的中央光滑族延拓全水平结构，有限 étale 性使标记唯一；$v$ 是带水平结构的中央局部参数（在带标记椭圆曲线形变中 $a_4$ 的变化与保 $a_6=1$ 的微分尺度独立）。代数 GM 连接及上述初值供同一 $w,e_0,e_1$。故所有 $c_k(n)$ 属固定数域、无 $p$ 参数。沿(J)的 Galois 作用，水平结构在整个中央形式邻域由其中央标记唯一决定；$e_0,e_1$ 初值有理且水平延拓自然。逐同样的 $a$ 重标给
$$ \theta_k c_k(n)/(1-\omega)\in\mathbf Q\qquad(n\ge0).\tag{Q3}$$

通用 $p$-可除群同态对其滤过有理 Dieudonné 晶体作用保连接；在椭圆曲线的 Serre–Tate 形式族上这是通用椭圆曲线的带 Hodge 线的 $H^1_{\rm dR}$（可具体用通用向量扩张）。相容性仅在中央完成后、特征零逐阶使用。具体可参 Gross–Hopkins, *The rigid analytic period mapping, Lubin–Tate space and stable homotopy theory*, §1，变形空间上有理周期映射的等变性、étale性及通用向量扩张的构造；这里直接用两条水平解写出的局部式。由水平性及原点处 $[t]$，有 $U_t^*e_0=t e_0$、$U_t^*e_1=\bar t e_1$（两式左边先在 $\Phi_t(u)$ 取基）。比较(P7),(Q1)，得到准确方向和框架
$$ w(\Phi_t(u))=(t/\bar t)w(u),\qquad
 d_t(u)/t=h(\Phi_t(u))/h(u).\tag{Q4}$$
所以(P9)已在整盘确立以后，才在这个形式参数内取系数，得
$$\boxed{c_b(n)=65\mathcal A_b(\rho^n-1)c_1(n)\qquad((p+1)\mid n),\quad
  \rho=\eta/\bar\eta.}\tag{Q5}$$
因 $t/\bar t$ 在 $\mu_{p^2-1}$ 上的像阶为 $p+1$，全 tame 投影恰取这些次数。对 $n$ 次系数可先在 (P9) 中用 $\mathcal A_b$ 的多项式截断，再按此前严格盘收敛取极限；这给标量特化 $\mathcal A_b(\rho^n-1)$，完全无需把 (Q1) 的形式参数延到准典点。$\eta$ 映至原 $\Gamma$ 的拓扑生成元且有理方向已除，故 $v_p(\rho-1)=1$。

### 全部所需同余类都有无限多个真实非零参考项

对任意 $6\mid N$ 与 $6\mid r$，在 $n\equiv r\pmod N$ 有无穷个正 $n$ 满足 $c_1(n)\ne0$。下面支付这个无需假定中央泰勒序列所有项非零的断言。

在复嵌入中 $w$ 正比于 $w_0=(\tau-\tau_0)/(\tau-\bar\tau_0)$，$\tau_0\in K\cap\mathfrak H$ 为原 CM 点。事实上在常 Betti 基中 Hodge 线由 $(1,\tau)$ 参数，$e_0,e_1$ 分别沿 $\tau_0,\bar\tau_0$ 的线，故解其线性分式关系即得此式。权一形式的同一 $h f_k$ 在 $w_0$ 里是固定非零常数乘 $\mathcal F_k(w_0)=f_k^{\rm an}(\tau(w_0))/(1-w_0)$（常 Betti 基中沿 $e_0$ 的分量正比于 $\tau-\bar\tau_0$）。故两种变量的非零指标相同。(P1)确是 holomorphic 权一 Eisenstein 的有限和：$F_7(Q)=7E_1^*(Q)-E_1^*([7]Q)$，代入逐一非零固定挠点即为 Hecke 正则化的权一 Eisenstein，参 Khuri-Makdisi, *Moduli interpretation of Eisenstein series*, §2 (2.1)–(2.7)；固定有理 slash 拉回后仍为有限同余级 Eisenstein。后一点也可在绝对收敛正则化域将有理变换后的子格分成一固定倍格的有限余类，再在同一 Hecke 参数解析延拓。

先作 $\mu_6$ 旋转的全平均 $\mathcal F^{[6]}=6^{-1}\sum_{t\in\mu_6}\mathcal F_1(t w_0)$，它在零等于 $\mathcal F_1(0)\ne0$。这些旋转对应 $\mathrm{PGL}_2^+(\mathbf Q)$ 中固定 $\tau_0$ 的有理矩阵：对每个 $t\in\mu_6\subset K^1$ 取 $a\in K^\times$ 使 $a/\bar a=t$，在 $1,\tau_0$ 格基中为有理乘法矩阵。$t w_0$ 这一变换的权一 slash 与上述横截面间只差固定非零常数。故 $\mathcal F^{[6]}$ 是一个非零权一 Eisenstein 形式的圆盘表示，有某个有理尖点常数非零。为核后一句，在共同小同余群上把这些 Hecke 正则化格和同逐尖点原始向量的 Eisenstein 家族比较（缩放公因子产生 Dirichlet 系数）。在绝对收敛域与任一 cusp form 的 Petersson 配对展开首行，其常数 Fourier 项零，遂在解析延拓后仍为零；残数或有限 Laurent 系数也为零。各有限组合因而与 cusp 空间正交。若各尖点常数全零，该非零 holomorphic 形式自己为 cusp，和自身配对严格正，矛盾。

选上述一个有理尖点 $r_0$，用圆盘边界点 $z_0=w_0(r_0)$ 表示。它在 $K$ 且 $|z_0|=1$。沿 $w_0=\lambda z_0,\ \lambda\uparrow1$，有 $(1-\lambda)\mathcal F^{[6]}(\lambda z_0)$ 趋于非零常数，由该尖点的 Fourier 常数及权一变换律直接得到；可取同余群等价的有限有理尖点避开 $\infty$。反之对 $\xi\in\mu_N\setminus\mu_6$，$\xi z_0\notin K$（$K$ 中全部单位根即 $\mu_6$），不能是任何有理尖点的边界像。对这些边界点的有限实横坐标 $x$，
$ (1-\lambda)\mathcal F_1(\lambda\xi z_0)\to0$。确实设 $z=x'+iy\to x$，圆盘径向给 $y\asymp1-\lambda$。选 $A=\left(\begin{smallmatrix}*&*\\ c&d\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbf Z)$ 将 $z$ 送经典基本域。有限个 slash 形式在该域都一致有界（在每尖点 holomorphic），故 $y|f_1^{\rm an}(z)|\le C y/|cz+d|$；大 $|c|$ 上此界至多 $C/|c|$，固定有界 $|c|$ 时因 $x$ 无理，$|cx'+d|$ 一致远离零。两步取极限即结论。

于是 $N^{-1}\sum_{\xi\in\mu_N}\xi^{-r}\mathcal F_1(\xi w_0)$ 在此径向仍有非零简单极型增长：$r$ 是6的倍数保证六个有理旋转的权皆一，所有其他项经 $1-\lambda$ 后消失。该全平均不为多项式，其 Taylor 展开恰选所求同余类，证明无限非零。

### 固定代数来源的中央二阶准确读者

给每个 $a\ge0$，可取 $n_a>0$ 为 $(p+1)p^a$ 的倍数且 $c_1(n_a)\ne0$。置 $t_a=\rho^{n_a}-1$，$v_p(t_a)=1+v_p(n_a)\ge a+1$。由于真 $\mathcal A_b\in T^2\mathcal O_{K_p}[[T]]$，(Q5)给
$$\boxed{\frac{c_b(n_a)}{65 c_1(n_a)t_a^2}\in\mathcal O_{K_p},\qquad
 \frac{c_b(n_a)}{65 c_1(n_a)t_a^2}\equiv[T^2]\mathcal A_b\pmod{p^{1+v_p(n_a)}}.}\tag{Q6}$$
这同时给 $[T^2]$ 的真正无误差极限；各 $a$ 只需一个真实非零参考系数。更可强制准确 $v_p(n_a)=a$：在 $N=(p+1)p^{a+1}$ 的同余类 $r=(p+1)p^a$ 应用刚证结论即可。若两中央均坏，原整平方阶偶性使每个 $\mathcal A_b\in T^4\mathcal O[[T]]$，故全部这些固定的有理比满足
$$ v_p\left(\theta_b c_b(n)/(65 c_1(n))\right)\ge4(1+v_p(n))
 \quad((p+1)\mid n,\ c_1(n)\ne0).\tag{Q7}$$
反向若对某一所述 $n,b$ 严格小于这一下界，则该固定 $p$ 已有原 $[T^2]\mathcal A_b\ne0$。这里只付了真实全部精度及跨 $p$ 统一候选的固定代数来源，尚未找到使(Q7)违背的无穷多个不同 $p$。

原文：Gross–Hopkins, Bull. Amer. Math. Soc. 30 (1994), 76–86, https://arxiv.org/abs/math/9401220 ；Khuri-Makdisi, *Moduli interpretation of Eisenstein series*, §2, https://arxiv.org/abs/0903.1439 。

## 10. 固定 Picard–Fuchs 解在每层指定权的非零参考

在 (Q1) 的代数族 $E_v:y^2=x^3+vx+1$ 取 $\omega=dx/(2y),\ \eta=x\omega$，$D=4v^3+27$；固定水平形式仍记为 $e_0,e_1$。写
$$ \omega=P(v)e_0+\frac v6 Q(v)e_1,\qquad P(0)=Q(0)=1.\tag{R1}$$
精确 Gauss–Manin 导数为
$$ \nabla_v\omega=\frac{-v^2\omega+(9/2)\eta}{D},\qquad
 \nabla_v\eta=\frac{(3v/2)\omega+v^2\eta}{D}.\tag{R2}$$
例如在相对 de Rham 余类中令 $J_m=x^m dx/y^3, I_m=x^m dx/y$。由 $d(x^j/y)$ ($j=0,1,2$) 及三次方程直接得到 $3J_2+vJ_0=0, I_0=2vJ_1+3J_0,-I_1=2vJ_2+3J_1$，故 $J_1=(2v^2I_0-9I_1)/D, J_2=(-3vI_0-2v^2I_1)/D$，而原导数恰为 $-J_1/4,-J_2/4$。于是 $H=P$ 和 $H=vQ/6$ 同满足
$$D H''+12v^2 H'+\tfrac74 v H=0,\quad
108(j+3)(j+2)H_{j+3}=-(4j+1)(4j+7)H_j,\quad H_2=0.\tag{R3}$$
$P$ 仅有次数 $0\bmod3$，$vQ/6$ 仅有次数 $1\bmod3$。Wronskian $P(vQ/6)'-(vQ/6)P'=9/(2D)$，可用 (R2) 的迹、或 (R3) 的 Abel 恒等式和原初值 $1/6$ 检验。在这个实际微分中 $h=P$、$w=vQ/(6P)$。故对每个 $n\ge0$，取 $[w^n]P f_k$ 的形式留数并用上述 Wronskian 得
$$\boxed{6^{-n}c_k(n)=[v^n]\;f_k(v)\,\frac{27}{D}\,P(v)^n Q(v)^{-n-1}.}\tag{R4}$$
$f_k(v)$ 逐一使用 (P1) 的固定全水平代数来源。其系数对所有充分大 $p$ 属一个固定非分歧扩域的整数环；特别 $f_1(0)=G_1(0)$ 为单位，$f_{65}(0)=f_{8125}(0)=0$。

### 原半径上的全系数控制

设 $p>211$ 惰性，$d_0=p+1$，取 $\pi^{d_0}=p$，只用于本次系数缩放。则在其整数环的限制幂级数中，准确的剩余式为
$$\boxed{
 P(\pi X)\equiv1+\kappa X^{d_0},\quad Q(\pi X)\equiv1\pmod{\mathfrak m},
 \qquad \kappa=p[v^{d_0}]P\in\mathbf Z_p^\times.}\tag{R5}$$
双源证明分三窗。在(R3)迭代至 $H_N$ 时，除固定单位外的分母是 $1,\ldots,N$ 中两个模三余类的子集，且每个整数最多出现一次：$P$ 是 $2,0\bmod3$，$vQ/6$ 是 $0,1\bmod3$。对 $p^j$ 的倍数计数时乘 $p^j$ 置换模三余类，故分母的总赋值至多
$$ \frac{2N}{3(p-1)}+\frac23\lfloor\log_p N\rfloor. $$
若 $N\ge p^2$，$\lfloor\log_p N\rfloor\le2N/p^2$，这个界严格小于 $(N-1)/(p+1)$，且留线性增长余量。若 $3p\le N<p^2$，仅 $p$ 的一次倍数贡献，至多 $2N/(3p)+2/3<(N-1)/(p+1)$。两窗均比两函数的 $\pi$ 次幂严格小，亦保证受限收敛。

最后 $N<3p$。$P$ 的分母能遇 $p$，遇不到 $2p$，首次在 $N=p+1$ 正好遇 $p$（$N=0\bmod3$）。其此项的分子无 $p$：各因子为 $12j+1,12j+7$，$0\le j<(p+1)/3$，若它等于 $mp$ 则 $1\le m\le4$；$p\bmod12=5$ 或11时，$mp\bmod12$ 对这样的 $m$ 不能为1或7。因此 $[v^{p+1}]P$ 的赋值为 $-1$。其他正 $N$ 在该窗经 $\pi^N$ 缩放后赋值严格正。对 $vQ/6$，分母的第一个可能 $2p$，$p$ 不入，其在 $Q$ 的相应次数 $N-1\ge2p-1>p+1$ 已超过代价。初值皆按(R1)。三窗给(R5)，并保住原首次单位 $\kappa$。

### 每级只需固定的一项

代 $n=m(p+1)$，$m\ge1$，在(R4)施 $v=\pi X$ 并约化。(R5)、$Q(\pi X)^{-1}\equiv1$、$27/D\equiv1$、$f_k(\pi X)\equiv f_k(0)$ 给出
$$p^m6^{-n}c_k(n)\equiv f_k(0)\,\kappa^m\binom{(p+1)m}{m}
\pmod {\mathfrak m}.\tag{R6}$$
因此 $m=p^a$ ($a\ge0$) 时二项式模 $p$ 为1（$((1+Z)^{p^a(p+1)})\bmod p=(1+Z^{p^{a+1}})(1+Z^{p^a})$）。原固定参考有逐层**准确**值
$$\boxed{v_p(c_1((p+1)p^a))=-p^a.}\tag{R7}$$
更一般当 $m$ 与 $pm$ 的基 $p$ 相加无进位时亦有 $v_p(c_1(m(p+1)))=-m$。

令 $n_a=(p+1)p^a$, $t_a=\rho^{n_a}-1$。于是原 (Q6) 在整条完全指定数列上成立，$v_p(t_a)=a+1$；对 $b=65,8125$，
$$ \frac{c_b(n_a)}{65c_1(n_a)t_a^2}\equiv[T^2]\mathcal A_b\pmod{p^{a+1}}.\tag{R8}$$
特别每个原中央坏迫使每个 $a$ 的固定权一几何系数满足
$$ v_p(c_b((p+1)p^a))\ge4(a+1)-p^a.\tag{R9}$$
$a=0$ 给确切阈值 $3$；只要两目标之一的 $c_b(p+1)$ 赋值小于3，该固定 $p$ 便已有一条原曲线通过。这里从(R4)直接取得有限中央读者的唯一指定离散权，$1/p$ 的参考因子准确保留，尚无证明 (R9) 在无穷 $p$ 上违背。

## 11. 真正固定代数模曲线上的整三位截取

保持(R1)–(R9)。设 $p=6s-1>211$ 惰性，$k=(p+1)/3=2s$, $t=v^3$。在原 $\mu_6$ 标记下 $f_b(v)=F_b(t)$。确实 $E_v\to E_{u^2v}$ 的 $(x,y)\mapsto(u^{-2}x,u^{-3}y)$ 拉回微分乘 $u$，中央是 $[u]$；新水平由原水平先乘 $u^{-1}$ 再经此同构得到（中心相等，整个局部族的有限 étale 延拓唯一）。(P1)中 $\epsilon_b(u^{-1})=u$ 正抵消权一，故 $f_b(u^2v)=f_b(v)$。两目标 $F_b(0)=0$，(J),(Q3)的常数下降也给 $\theta_bF_b/(1-\omega)\in\mathbf Q[[t]]$；它是该固定代数模曲线上的代数局部支。

记
$$ U(t)=P(v),\quad V(t)=Q(v),\quad H=U/V,\quad
 B=\frac{27U}{(4t+27)V^2},\quad D_t=t\frac d{dt}.$$
来自(R3)的两组**精确有理数**系数是
$$ [t^j]U=\left.\frac{(2r)_{\underline j}(r)_{\underline{2j}}}{(3j)!}\right|_{r=-1/6},\quad
 [t^j]V=\left.\frac{(2r-1)_{\underline j}(r-1)_{\underline{2j}}}{(3j+1)!}\right|_{r=1/6}.\tag{S1}$$
下降幂采用 $x_{\underline m}=x(x-1)\cdots(x-m+1)$。前式相邻比的 $(2r-j)$ 消去 $3j+1$，余 $(12j+1)(12j+7)$；后式的 $2r-1-j$ 消去 $3j+2$，余 $(12j+5)(12j+11)$，正是 (R3)。

对正整数 $r$，将右边保留该整数所得的有限多项式记 $A_r(t),B_r(t)$。它们确是实际三次方程多项式的系数，而非从 mod $p$ 猜的 lift：
$$\begin{aligned}
 [x^{6r}](x^3+vx+1)^{3r}&=\frac{(3r)!}{(2r)!r!}A_r(v^3),\\
 [x^{6r-2}](x^3+vx+1)^{3r-1}&=
 \frac{(3r-1)!}{(2r-1)!(r-1)!}v B_r(v^3).
\end{aligned}\tag{S2}$$
逐三项式展开的指数分别为 $(2r-j,3j,r-2j)$ 与 $(2r-1-j,3j+1,r-1-2j)$；负指数项按零。特别 $B_s$ 是**本特征**通常 Hasse 多项式除首 $v$ 和首单位。其余插值点是整数幂的同系列真实系数，无须其 $6r\pm1$ 为素数。

对 $i=0,1,2$ 的 Lagrange 基多项式写 $L_i(x)=\prod_{h\ne i}(x-h)/(i-h)$。定义截掉 $t^k$ 及以后项的两个整多项式
$$ U_* = \left(\sum_{i=0}^2 L_i(-5/6)A_{5s-1+ip}\right)_{<k},
\quad V_* = \left(\sum_{i=0}^2 L_i(-1/6)B_{s+ip}\right)_{<k}.\tag{S3}$$
对每个 $j<k$，(S1)分母 $(3j)!$ 或 $(3j+1)!$ 都是 $p$ 单位，故相应系数作为 $r$ 的多项式在 $\mathbf Z_p[r]$。对这多项式除以对应三个整数节点的首一三次多项式，余式在目标 $r=\mp1/6$ 差一个 $p^3$ 倍数（每个节点和目标差都在 $p\mathbf Z_p$）。余式值就是(S3)，因为 $(-1/6-(5s-1))/p=-5/6$、$(1/6-s)/p=-1/6$。从而 $U_*,V_*$ 同时准确到 $(p^3,t^k)$，且都以一为常数，截断分母整。

现在以原代数 $F_b$ 精确给
$$ 6^{-(p+1)}c_b(p+1)\equiv [t^k]F_b(t)\frac{27}{4t+27}
                 \frac{U_*(t)^{p+1}}{V_*(t)^{p+2}}\pmod{p^3}.\tag{S4}$$
上述少掉的 $t^k$ 项确实与零 $F_b(0)$ 相乘；若用同式对参考项直接少掉这一位会错，参考仍须保留(R5)的 $1/p$。在 $v$ 参数里(S4)就是以下固定模曲线（整数模型参数 $v$）上的原代数微分，经指定局部 Cartier 读数所得的常数：
$$\mathfrak C_{p,v}\left(
 \frac{27 f_b(v)\,U_*(v^3)^{p+1}}{v^2(4v^3+27)V_*(v^3)^{p+2}}\,dv\right)(0),
\quad
\mathfrak C_{p,v}\left(\sum a_i v^i\,dv\right)=\sum a_{pj+p-1}v^j\,dv .
\tag{S5}$$
因 $f_b(v)\in v^3W[[v^3]]$，原微分正则。末式将微分系数用原 $dv$ 读为标量；在固定参数中对 $W/p^3$ 定义，模 $p$ 与通常 Cartier 相差系数 Frobenius 的约定。没有对模 $p^3$ 声称不依参数的几何 Cartier，也无须在其他超奇异点倒 Hasse。

此外同一检验可以只用一个不依 $p$ 的特征零级数。置
$$ \mathscr H_b=F_b B+
    (3D_t-1)(F_b B\log H)
    +(3D_t-1)^2\big(F_b B(\log H)^2/2\big).\tag{S6}$$
则
$$ 6^{-(p+1)}c_b(p+1)\equiv [t^{(p+1)/3}]\mathscr H_b\pmod{p^3}.\tag{S7}$$
确因(R4)正取 $[t^k]F_b B H^p$。$log H$ 到 $t^{k-1}$ 的全部分母均为 $p$ 单位（$k<p$, $H(0)=1$）；截取 $\exp(p\log H)$ 到二次，其余项对全部有关次数均在 $p^3$。在 $t^k$ 上 $3D_t-1$ 的特征值恰为 $p$，故得到(S7)。两目标的(S4)/(S7)仍要违背 $p^3$ 整除才给(R9)首层的跨素数结论。这里清除了原 PF 超越解在三位成本附近的待算窗口，只给出原来源的准确代数截取。

## 12. 原三位系数在两个单独的五同源类上

固定 $c_*=78$，$\epsilon_*$ 是原 $\epsilon_b$ 在 $2,3,\pi_{13},\bar\pi_{13}$ 的四个分量的乘积，取一贯使用的理想生成元方向。由两原曲线的单位表它对 $b=65,8125$ 相同；把实际五单位分量写 $\xi_b$，故 $\epsilon_b=\epsilon_*\xi_b$。$\epsilon_*(5)=-1$：二处是1，三处是 $-1$，双十三分量在有理单位上的乘积是1。$\xi_b(78)=1$，两条 $\xi_b$ 都在 $\mathbf F_5^\times$ 上平凡。两条在 $\mu_3$ 上相同，在 $\delta=\sqrt{-3}\bmod5$ 上分别是 $-1,+1$，因为 $\delta^2=-3$、$\delta^4=-1\bmod5$，单位表给 $u^4,u^{16}$ 或其逆（此处两符号不变）。

对(P1)的带全水平390的通用椭圆曲线，分别取 $\alpha_{78},\alpha_5$。定义实际78级权一截面及其每个五循环商的值
$$ f_*(E',\alpha',\kappa)=\sum_{a\in(\mathcal O_K/78)^\times}
\epsilon_*(a)^{-1} F_{7,(E',\kappa)}(\alpha'(a)),\qquad
F_C=f_*(E'/C,q_C\alpha_{78},\kappa_C),\quad q_C^*\kappa_C=\kappa.\tag{Y1}$$
这里 $\alpha_{78},\alpha_5$ 取从原复基 $Q_{390}$ 经 $[5],[78]$ 得到的相容结构。在 CRT 代表 $r=5a+78z$ 下，$\alpha_{390}(r)=\alpha_{78}(a)+\alpha_5(z)$，并有 $\epsilon_b(r)=-\epsilon_*(a)\xi_b(z)$。相同 $\mathbf F_5^\times$ 轨道对应同一循环 $C$ 的四个非零点。采用(P2)的 $5$ 次同源完整生成元迹，因 $5\ne7$，恰给 $F_C-f_*(E',\alpha_{78},\kappa)$。$\xi_b$ 均为非平凡角色，故六条的父项全和零。准确得到
$$\boxed{f_b=-\sum_{C\in\mathbf F_{25}^\times/\mathbf F_5^\times}
                 \xi_b(C)^{-1} F_C.}\tag{Y2}$$

现在取原 $E_v$ 族（原 $f_b(v)$ 的全部标记），且令 $c_C(n)=[w^n]P(v) F_C(v)$，使用(R1),(Q2)的同一 $w,P$。每个 $u\in\mu_3$ 的 $E_v\to E_{u^2v}$ 同构将第 $C$ 支送第 $uC$ 支，拉回两条商的相容微分也乘 $u$。原78级水平结构在目标等于源结构先乘 $u^{-1}$ 再随该同构运输。由于 $\epsilon_*(u)\xi_b(u)=u^{-1}$，从(Y1)直接得到
$$F_{uC}(u^2v)=\xi_b(u) F_C(v),\qquad
c_{uC}(n)=\xi_b(u)u^{-2n}c_C(n).\tag{Y3}$$
两条的 $\xi_b(u)$ 确实相同。置 $C_+=\mathbf F_5$、$C_-=\delta\mathbf F_5$，标签都是实际 $E[5]$ 中原 $\alpha_5$ 像的循环子群。$N\delta=3$ 是模五非平方，$\mu_3$ 在六个线标签上给两个三元轨道，正负轨道各一。于每个 $3\mid n$，(Y2),(Y3)便准确拆为
$$\boxed{c_{65}(n)=-3(c_{C_+}(n)-c_{C_-}(n)),\qquad
c_{8125}(n)=-3(c_{C_+}(n)+c_{C_-}(n)).}\tag{Y4}$$
特别 $F_{C_+}(0)=F_{C_-}(0)=0$ 已由两条固定秩二来源的中央零共同推出。两商的 CM 阶皆为 $\mathbf Z+5\mathcal O_K$：其复格为 $\mathcal O_K+5^{-1}v\mathbf Z$ 的尺度；乘子环直接计算如(P9)。理想类数公式给 $h(-75)=2$，且两个 $\mu_3$ 轨道即两类：两个五次超格相似时，若 $z$ 为相似倍数，其范数一且 $5z$ 整、$N(5z)=25$，惰性五迫 $5z$ 为5的单位倍数，故相似已来自 $\mu_6$。因此(Y4)保留的是两个单独的原五同源 CM 类。

对三位读数要保留(Y3)而不能任取五线的裸 Taylor 项。对 $C=C_\pm$ 把 $F_C(v)$ 取其 $v^3$ 成分
$$ Q_C^0(v^3)=\tfrac13\sum_{u\in\mu_3}F_C(u^2 v).\tag{Y5}$$
这是该单个78级源的实际有限投影。$P,Q,w/v$ 均只含 $v^3$，故 $3\mid n$ 时截取 $Q_C^0$ 与原 $F_C$ 的 $c_C(n)$ 相同，且 $Q_C^0(0)=0$。在(S4)以 $Q_C^0$ 代 $F_b$ 定义各自三位数 $J_{+,p},J_{-,p}\in W/p^3$。则
$$ 6^{-(p+1)}c_{65}(p+1)=-3(J_{+,p}-J_{-,p}),\quad
6^{-(p+1)}c_{8125}(p+1)=-3(J_{+,p}+J_{-,p})\pmod{p^3}.\tag{Y6}$$
两个固定五商的死亡同时发生才会使这两个三位测试都为零。余下全部 $2,3$ 与双 $13$ 的原 $\epsilon_*$ 已在(Y1)中，不等价于随意把某条辅助5伙伴测度赋零。

## 13. 原390级两个角色的三级祖源与216条实际循环同源

令 $\epsilon_0:(\mathcal O_K/3)^\times\longrightarrow\mu_6$ 把六个单位余类提升为全局单位后取逆。此识别成立，因为模3的六个单位互异。原两条 $\epsilon_b$ 的三处分量正是 $\epsilon_0$（有限理想生成元方向）。写 $\epsilon_b=\epsilon_0\chi_b$，则 $\chi_b$ 的全部 2、5、双13分量仍取原表；它在有理局部标量上平凡，在对角 $\mu_6$ 上平凡，在三个局部射影环面上各非平凡。它是 $\mathrm{Pic}(\mathcal O_{130})$ 的有限角色，$\mathcal O_h=\mathbf Z+h\mathcal O_K$。$\psi_0((a))=a\epsilon_0(a)$ 是模3同余于1的唯一生成元；它正是 Fermat 曲线 $y^2+y=x^3$ 的 CM 角色（短模型 $E_{16}$，最小判别式 $-27$）。也可从其好于3外、椭圆曲线导子27所给 Hecke 导子范数9、模3六个单位全体和 Weil 权一确定。这里 $\psi_0$ 比较的是理想角色；随后的全部物理取值在原 $E_1$ 的微分上。

在原带水平椭圆曲线 $(E',\alpha,\kappa)$ 上设
$$
 f_3(E',\alpha_3,\kappa)=\sum_{a\in(\mathcal O_K/3)^\times}
       \epsilon_0(a)^{-1}F_{7,(E',\kappa)}(\alpha_3(a)). \tag{Z1}
$$
用 $[195],[130],[78],[30]$ 从 $\alpha_{390}$ 取得 $2,3,5,13$ 水平。CRT 写成 $r=195a_2+130a_3+78a_5+30a_{13}$；这四个有理系数在相应权下的值分别为1（三级 $130\equiv1$，其余三个取射影标量）。三套标签是
$$
\mathcal C=\mathbf F_4^\times/\mathbf F_2^\times
 \ \times\ \mathbf F_{25}^\times/\mathbf F_5^\times
 \ \times\ (\mathbf F_{13}^\times\times\mathbf F_{13}^\times)/
                        \mathbf F_{13}^\times .
$$
十三处有12条线，不包括任一坐标轴。每个 $C$ 表示相应 $C_2\oplus C_5\oplus C_{13}\subset E'[130]$。记
$$G_C=f_3(E'/C,q_C\alpha_3,\kappa_C),\qquad q_C^*\kappa_C=\kappa.$$
在每个局部射影线内遍历所有非零向量；三处完整和等于全部核点和，减去各个真子积的和（容斥）。任何真子积均至少遗漏一处，该处 $\chi_b$ 非平凡，故加权总和消掉其全部父项。对全循环采用(P2)的原 $F_7$ 同源迹，得到
$$\boxed{f_b=\sum_{C\in\mathcal C}\chi_b(C)^{-1}G_C.}\tag{Z2}$$
无除130或归一化的射影迹。中央复格把 \(E_1\) 按其 CM 周期伸缩到 $\mathcal O_K$，商格为 $L_C=\mathcal O_K+\mathbf Z v_C/130$，$v_C$ 模130是单位。其乘子环为 $\mathcal O_{130}$，因为各 $\ell\mid130$ 处保持原线的 $\mathcal O_K$ 元素正是模 $\ell$ 的标量（十三的线两坐标皆非零）。任一乘子先必在 $\mathcal O_K$，由扩成最大序后格皆为 $(1/130)\mathcal O_K$ 得到。相似的两格亦因相同扩格只能差全局单位，故类数为 $3\cdot6\cdot12/3=72$。等价地，环类的标准理想正合列把 $\mathrm{Pic}(\mathcal O_{130})$ 识别为此局部环面除对角 $\mu_3$，因 $h_K=1$。在中央 $G_{aC}=G_C$ 对 $a\in\mu_6$ 成立：CM 同构、三级重标和微分的权恰相消。

在原标记 $Q_3=\varpi_1/3$，六项都是单位轨道，$F_7(uQ)=u^{-1}F_7(Q)$ 及 $\epsilon_0(u)^{-1}=u$ 给出 $f_3(0)=6F_7(Q_3)$。$[7]Q_3=Q_3$，故 $F_7(Q_3)=6E_1^*(Q_3)$，其中 $E_1^*$ 是以原格取值的周期修正 Weierstrass zeta。倍点恒等式 $E_1^*(2Q)=2E_1^*(Q)+\wp''(Q)/(2\wp'(Q))$ 中 $2Q=-Q$。用 $\wp=x,\wp'=2y$ 且 $x^3=-4,y^2=-3$（$Q_3$ 是自由 $\mathcal O_K/3$ 生成元，非 $E[\delta]$），得到
$$ f_3(0)=36E_1^*(Q_3)=-18x(Q_3)^2/y(Q_3),\qquad
 f_3(0)^{24}=2^{56}3^{36}.\tag{Z3}$$

在与原 $\alpha_3$ 相同 Weil 配对的 $X(3)$ 连通分量，$f_3$ 是全纯权一形式。确实 \(F_7=7E_1^*(P)-E_1^*(7P)\)，每条非零三级标记点上等于 $6E_1^*(P)$，这是权一 Eisenstein 级数，任何 cusp 的标准 Tate 展开无负幂。有效指数12、四个尖点宽皆3、无椭圆稳定子给 $X(3)$ 亏格0及 $\deg\omega=1$（$\Delta$ 权12）。标签乘 $\omega$ 的 deck 对称是 $\mathrm{PSL}_2(\mathbf F_3)$ 中非平凡幺幂阶3；由(Z1)重标为特征向量。它固定原 CM 点和唯一尖点 $c_0$，后者的乘法退化线是 $\mathbf F_3\delta,\ \delta=\sqrt{-3}$。在 $\mathbf P^1$ 的非恒等自同构至多两个固定点；(Z3)非零，故 $f_3$ 唯一零为 $c_0$，重数一。整个结论限原 Weil 配对分量；原130商和所有合法偶 $p^s$ 商的次数均模3为1，故实际使用点都在其中。

置 $D_\delta=\alpha_3(\mathbf F_3\delta)$，并规定 $q_\delta^*\kappa_\delta=\kappa$。$f_3^{12}/\Delta$ 在 $c_0$ 阶9，在另三尖点阶$-3$。$X_0(3)$ 上实际商鉴别式比 $\Delta(E'/D_\delta,\kappa_\delta)/\Delta(E',\kappa)$ 在乘法核尖点阶2，在对面尖点阶$-2$，由 Tate 格或 $\Delta(3\tau)/\Delta(\tau)$ 的积展开及 Fricke 对称得到。拉回到 $X(3)$，$c_0$ 处指数3，其余处指数1。平方前一个单位与立方后一个单位除子一致，故比为常数。以 $E_1,\kappa=dx/(2y)$ 标定：$\Delta_E=-432$，$[\delta]$ 微分为 $\delta$，归一商鉴别式为 $\delta^{12}\Delta_E$。由(Z3)得
$$
 \boxed{f_3(E',\alpha_3,\kappa)^{24}
 =2^{48}3^{12}\frac{\Delta(E'/D_\delta,\kappa_\delta)^3}{\Delta(E',\kappa)}.}\tag{Z4}
$$

令 $D_C=\Delta(E_1/C,\kappa_C)/\Delta_E$，$u_C=G_C(0)/f_3(0)$。$\delta:E_C\to E_{\delta C}$ 核为 $q_C(E_1[\delta])$，拉回 $\kappa_{\delta C}$ 为 $\delta\kappa_C$。在(Z4)除以原基点的值：
$$\boxed{u_C^{24}=D_{\delta C}^{\,3}/D_C,\qquad
       \sum_{C\in\mathcal C}\chi_b(C)^{-1}u_C=0.}\tag{Z5}$$
第二式是原两条中央秩二零在(Z2)的原216个非零代数数上的取值。其各项在同源商的所有好约化处为单位（分母只须排固定有限集），并均在72类的纤维上常数。

## 14. 全部72个真实单位及两条单位权一的单零

沿(Z1)–(Z5)。$\mathcal C$ 为216条原开循环，$H=\mathcal C/\mu_3$ 有72个元素。各 $D_C,u_C$ 仅依赖 $\bar C\in H$。以下求和凡标 $\mathcal C$ 保留每一条物理循环，标 $H$ 才除3。

### 包含非本原角色和平凡角色的完整 Epstein 和

对 $\rho\in\widehat H$，令 $\lambda$ 为从 $\rho^{-1}$ 在其本原导子给出的有限理想角色，约定理想 $(a)$ 取剩余类 $a$ 的值。对 $\operatorname{Re}s>1$，
$$
 \sum_{C\in\mathcal C}\rho(C)^{-1} Z_{L_C}(s)
 =6\cdot130^{2s}P_\rho(s)L(s,\lambda),\qquad
 Z_L(s)=\sum_{z\in L\setminus0}|z|^{-2s}.\tag{U1}
$$
$P_\rho$ 仅在 $\rho$ 的局部单位角色平凡的地方有因子。惰性 $\ell=2,5$ 给 $1+\ell^{1-2s}$，分裂13 给 $1-(u+u^{-1})13^{-s}+13\cdot13^{-2s}$，其中 $u=\lambda(\pi_{13})$，共轭理想值 $u^{-1}$。验式时令 $a=130z$。在任一非平凡局部角色处 $a\equiv0\bmod\ell$ 即因该处全环面和而消去；在十三处任一单轴也不属于开放线。单位余类只在唯一射影线上。在平凡惰性处，非零余类权1，可被 $\ell$ 整除时权 $\ell+1$，故修正本原 Euler 为 $1+\ell\cdot\ell^{-2s}$。平凡分裂处按两个坐标皆非零、单零、双零计权 $1,0,12$，相应 Euler 乘子为
$(1-u13^{-s})(1-u^{-1}13^{-s})+12\cdot13^{-2s}$。对所有有理主理想的 $\lambda$ 值都是1。六个全局单位给首因子6。各 $P_\rho(0)>0$，分裂13的候选值为 $14-2\operatorname{Re}(u)$。

所需第一 Kronecker 极限公式的常数也可在此直接核对。记
$E(\tau,s)=\sum' y^s/|m+n\tau|^{2s}$，$\tau=x+iy$。对 $m$ 作一维 Poisson 求和，零频前两项为
$2\zeta(2s)y^s+2\sqrt\pi\,\Gamma(s-\tfrac12)\zeta(2s-1)y^{1-s}/\Gamma(s)$，
其余是
$$
 \frac{8\pi^s\sqrt y}{\Gamma(s)}
 \sum_{n,k\ge1}(k/n)^{s-1/2}\cos(2\pi knx)K_{s-1/2}(2\pi kny).
$$
利用 $K_{-1/2}(t)=\sqrt{\pi/(2t)}e^{-t}$ 得 $E(\tau,0)=-1$，导数为
$-2\log(2\pi)-\log y+\pi y/3
 -4\sum_{n\ge1}\log|1-e^{2\pi i n\tau}|$。
因 $Z_{\beta(\mathbf Z+\mathbf Z\tau)}=(|\beta|^2y)^{-s}E$，且与 $dz$ 相容的鉴别式
$\Delta(L)=(2\pi)^{12}\beta^{-12}\eta(\tau)^{24}$，有
$$ Z_L(0)=-1,\qquad Z_L'(0)=-\tfrac16\log|\Delta(L)|.\tag{U2}$$
原物理格多一个共同尺度 $\varpi_1$，(Z5)的 $D_C$ 是准确比值 $\Delta(L_C)/\Delta(\mathcal O_K)$，故此尺度全消。

若 $\rho\ne1$，本原有限虚二次 Hecke $L(s,\lambda)$ 在0单零。其无穷因子为 $\Gamma(s)$，函数方程联到 $L(1,\bar\lambda)$；后者非零亦可由相应有限阿贝尔类域的 Dedekind zeta 分解推出：除平凡角色外各因子在1全纯，两个 Dedekind zeta 的单极留数非零。于是(U1),(U2)给
$$\sum_{C\in\mathcal C}\rho(C)^{-1}\log|D_C|
 =-36P_\rho(0)L'(0,\lambda)\ne0. \tag{U3}$$
因 $C\mapsto\delta C$ 是 $H$ 的平移，(Z5)进一步给
$$ \sum_C\rho(C)^{-1}\log|u_C|
 =\frac{3\rho(\delta)-1}{24}\sum_C\rho(C)^{-1}\log|D_C|\ne0.\tag{U4}$$
上述 $C$ 可同时取 $\mathcal C$ 或 $H$。$\delta^2=-3$ 是有理标量，故 $\rho(\delta)=\pm1$。

若 $\rho=1$，(U1)为 $130^{2s}P_1(s)Z_{\mathcal O_K}(s)$，$P_1(0)=216$。由三项完整 Euler 乘子直接得到
$$ 2\log130+P_1'(0)/P_1(0)
   =\tfrac23\log2+\tfrac13\log5.$$
其中分裂13项给 $-2\log13$，与尺度中的 $+2\log13$ 相消。微分(U1)并减去 $216Z'_{\mathcal O_K}(0)$，使用 $Z_{\mathcal O_K}(0)=-1$；再把216项除3及使用(Z5)，得
$$
 \prod_{C\in H}|D_C|=2^{288}5^{144},\qquad
 \prod_{C\in H}|u_C|=2^{24}5^{12}=20^{12}.\tag{U5}
$$

### 从原环类的正则作用到每个好处的完整线性无关

对固定 $\sigma\in G_K$，在有全 $\mathcal O_K$ 乘法的 $E_1$ 上，其 prime-to-characteristic Tate 作用是 $\mathcal O_\ell$ 单位。故 $\sigma$ 把 $D_C$ 移到 $D_{sC}$。对 $G_C(0)$ 尚有三级水平重标 $\alpha_3\mapsto\alpha_3s_3$；在(Z1)中重新编号，分子和 $f_3(0)$ 的常数同乘 $\epsilon_0(s_3)$，微分与系数都定义于 $K$，于是 $u_C^\sigma=u_{sC}$。所得对 $H$ 的平移遍取全群。确实任给模130单位 $a$，由 CRT 选非零 $\beta\equiv a\bmod130$ 且 $\beta\equiv1\bmod3$。理想 $(\beta)$ 与 $130\mathfrak f_1$ 互素，其 CM reciprocity 给各素于130 Frobenius 的乘积在130挠上由 $\psi_1((\beta))=\beta\epsilon_1(\beta)$ 作用（取相反 Artin 约定则为其逆）。$\epsilon_1(\beta)\in\mu_6$，在 $H$ 中消失。此处无需模2挠的 Galois 像满整个 $\mathbf F_4^\times$。

记 $A=\langle u_C:C\in H\rangle$ 并除其有限挠子群，指数映射
$\mathbf Q[H]\to A\otimes\mathbf Q$ 的核在纯标签平移下不变。扩标量到 $\mathbf C$ 后，核是正则表示中若干一维角色直和。若某角色线在核中，则经实际同态 $A\to\mathbf R,\ u\mapsto\log|u|$ 的线性延拓，其傅里叶和必须为零。每个非平凡模式已由(U3),(U4)排除，平凡模式由(U5)排除。因此72个单位模挠子群乘法独立。相同论证也适用于72个 $D_C$。

在每个足够大的 $p$ 处及任意相容代数嵌入，全部 $u_C,D_C$ 是 $p$ 进单位。单位的 $p$ 进对数核为根单位，因此它们各自72个对数对 $\mathbf Q$ 线性无关。把每个单位取同一整数幂进入对数指数互逆的小圆盘，由 Brumer, *On the units of algebraic number fields*, Mathematika 14 (1967), 121–124, Theorem 1；同一命题可直接查阅 Fuchs–Pham [Theorem 2.1](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)，得到
$$\boxed{\{\log_p u_C:C\in H\}\ \text{对 }\overline{\mathbf Q}\ \text{线性无关。}}\tag{U6}$$
$\log_pD_C$ 亦满足同一命题。在(p)好约化、$p\nmid 2\cdot3\cdot5\cdot13$ 处两同源的微分与鉴别式皆为单位，足以应用于本题所有允许惰性素数。

对原两条 $\chi_b$，取同一实际单位权一行的局部参数
$$ V_{b,p}(z)=\sum_{C\in H}\chi_b(C)^{-1}u_C\exp(z\log_pu_C) \tag{U7}$$
在零的小邻域解析。它在相应剩余类的整次幂上等同原 $u_C$ 的幂和：取一个共同倍数 $M$ 消掉全部 Teichmüller 单位，整 $z=Mn$ 足够接近0时取得电荷 $1+Mn$。实际质量零 (Z5) 给 $V_{b,p}(0)=0$，而
$$\boxed{ V'_{b,p}(0)=\sum_{C\in H}\chi_b(C)^{-1}u_C\log_p u_C\ne0. }\tag{U8}$$
系数是给定嵌入下的非零代数数，故直接用(U6)。原电荷一在各自参数上都是单零。原 canonical 读数 (Q6),(R9) 对 $w^{(p+1)p^a}$ 水平变形取极限；(U8)已固定同一点、同一微分及原两角色，但其导数参数仍是单位幂。

## 15. 原中央二阶的完整首层端点与过收敛二次积分

设 $d=p+1$，$\pi^d=p$，$\kappa=p[v^d]P\in\mathbf Z_p^\times$。沿(R1)–(R8)，设 $H(X)=P(\pi X)/Q(\pi X)$。由(R5)的线性余量 $P(\pi X),Q(\pi X)$ 在某个严格大于1的闭盘收敛，在单位盘 $Q\equiv1$、$H\equiv1+\kappa X^d$ 模极大理想。每一原 $g=f_1,f_{65},f_{8125}$ 或(Z2)的单支 $G_C$ 在 $v$ 开单位盘整有界，故 $g(\pi X)$ 同样过收敛。

令 $Y(X)$ 是下式中模极大理想等于 $X$ 的解：
$$ YH(X)=X(1+\kappa Y^d). \tag{W1}$$
在 $Y=X$ 处误差范数小于1，偏导 $H-d\kappa XY^{d-1}$ 约化为1。Tate 代数的 Hensel 迭代给唯一所需解。它及逆 $X(Y)$ 均过收敛：在半径 $R>1$ 足够接近1仍有原误差小于1、导数减1小于1，所有高阶导出系数在 $R\downarrow1$ 时有界，取一个固定小于1的收缩球作 Newton 迭代即可。同样对 $Y=X+\varepsilon(X)$ 其中 $\|\varepsilon\|_1<1$ 迭代反解，并在较小的 $R>1$ 保收缩。$Y(0)=0,Y'(0)=1$。于是精确有
$$ \frac{6w}{\pi}=\frac{Y}{1+\kappa Y^d},\qquad
 G_g(Y)=\frac{X(Y)}Y Q(\pi X(Y))g(\pi X(Y))(1-p\kappa Y^d).\tag{W2}$$
$G_g$ 是过收敛函数，$G_g(0)=g(0)$。把实际 $c_g(n)=[w^n]P(v)g(v)$ 写成形式留数：$P(\pi X)=(X/Y)(1+\kappa Y^d)Q(\pi X)$，且 $d\log(Y/(1+\kappa Y^d))=(1-p\kappa Y^d)dY/[Y(1+\kappa Y^d)]$。因子严格相消，得
$$ (\pi/6)^n c_g(n)=[Y^n]G_g(Y)(1+\kappa Y^d)^n,\qquad
 G_g(Y)\,\frac{dY}{Y}=\frac{27g(v)}{(4v^3+27)Q(v)}\,\frac{dv}{v}.\tag{W3}$$
第二式由(R4)的 Wronskian 得到。

取 $k=p^a,n=dk$，将(W3)除以 $\kappa^k\binom{dk}k$，记结果为 $S_g(k)$。置 $g_j=\kappa^{-j}[Y^{dj}]G_g$，$H_j=\sum_{h=1}^j1/h,\ H_0=0$。有
$$ S_g(k)=\sum_{j=0}^k g_j B_j(k),\qquad
 B_j(k)=\frac{\binom{dk}{k-j}}{\binom{dk}k}
       =\frac{\prod_{h=0}^{j-1}(k-h)}{\prod_{h=1}^j(pk+h)}.\tag{W4}$$
$j=0$ 给1。沿此固定数列 $k\to0$（$p$ 进），
$$ S_g(k)=g(0)+k\,s_1(g)+k^2s_2(g)+o(k^2),$$
$$ s_1(g)=\sum_{j\ge1}\frac{(-1)^{j-1}g_j}j,\qquad
 s_2(g)=\sum_{j\ge1}\frac{(-1)^j g_j}j(H_{j-1}+pH_j).\tag{W5}$$
具体控制如下。$1\le j\le k$ 时 $v_p(pk+h)=v_p(h)$ 且 $h<j\le k$ 时 $v_p(k-h)=v_p(h)$，所以 $v_p(B_j(k))=a-v_p(j)$。把 $B_j(k)$ 写为 $(-1)^{j-1}(k/j)$ 乘
$\prod_{h<j}(1-k/h)\prod_{h\le j}(1+pk/h)^{-1}$（第一积从1起）。乘积减1的赋值至少 $a-\lfloor\log_p j\rfloor$，因每个因子与1之差至少此赋值、每个因子为单位。故减去一次项再除 $k^2$ 的大小至多 $p^{v_p(j)+\lfloor\log_pj\rfloor}$。对固定 $j$ 逐因子展开，极限为(W5)二次系数。$g_j$ 指数衰减，故可支配收敛；对 $j>k$ 被补上的一次项除 $k^2$ 的尾也趋零，因为 $p^a=k<j$（通常绝对值意义）且指数衰减胜过多项式。相同估计先给一次极限。这里无需每个 $B_j(z)$ 的极点都避开同一 $p$ 进权盘。

(Q5)的规范比在同一数列给 $S_b(k)=65\,\mathcal A_b(\rho^{dk}-1) S_1(k)$。$S_1(k)\to f_1(0)$，而 $\mathcal A_b\in T^2\mathcal O[[T]]$，故原两目标准确满足
$$f_b(0)=s_1(f_b)=0,\qquad
 \boxed{65 f_1(0)(d\log_p\rho)^2[T^2]\mathcal A_b=s_2(f_b).}\tag{W6}$$
特别，(Z2)每个目标单支变形从头保留在 $G_g(Y)$ 中。单支标准化零阶确为 $G_C(0)=u_C f_3(0)$。

令 $F_g(s)=\sum_{j\ge0}(-1)^jg_j s^j$，这是 $G_g(Y)$ 在 $Y^d=-s/\kappa$ 上的全 $d$ 项平均，过收敛。对 $g=f_b$，取
$$ I_g(s)=\int_0^s F_g(t)\frac{dt}{t}.\tag{W7}$$
$F_g(0)=0$，且(W5),(W6)给 $I_g(0)=I_g(1)=0$。用逐项恒等式 $\int_0^1(1-s^j)ds/(1-s)=H_j$，以及 $H_{j-1}+pH_j=dH_j-1/j$，得
$$ \boxed{
 65 f_1(0)(d\log_p\rho)^2[T^2]\mathcal A_b
   =-\int_0^1 I_g(s)\left(\frac{ds}{s}+d\,\frac{ds}{1-s}\right).}\tag{W8}$$
积分是过收敛函数的原函数差。在0与1的表面极点均因完整的 $I_g$ 消除。证明也可先写 $d\int_0^1 (I_g(1)-I_g(s))ds/(1-s)-\int_0^1 I_g(s)ds/s$，两次积分的逐项式都收敛。设 $s=-\kappa Y^d$，则括号中的微分为 $d\cdot d\log(Y/(1+\kappa Y^d))$。而 $I_g(1)$ 正是(W3)的原微分从0到 $Y^d=-1/\kappa$ 所有根的原函数值的完整和。消去 $s=1$ 的极点只在该全和上进行；各单支没有被赋零。

### 首个圆周上所有端点的原同源解释

这些端点在 $v$ 盘恰是 $P(v)=0$ 且 $v_p(v)=1/d$ 的 $d$ 个简单零。由(W1)和 $Q(\pi X)$ 无零即得；亦可由(R5)直接 Hensel 逐根。现取原 $E_1[p]$ 上任一循环线 $D$，在 $E_D=E_1/D$ 上用 $q_D$ 特殊纤维的相对 Frobenius 给 $E_D$ 的特殊标记。若以原全水平参数 $v$ 表示，先在 $E_1[390]$ 的标签上复合该 Frobenius 的逆，使约化的水平结构回到原标记。这个操作只给变形盘选坐标；实际(W3),(W8)的 $g$ 始终以原盘固定水平运算，不能不经重标就用奇层未归一的单个 $F_{b,D}$ 替换 $g(v_D)$。

此商 Tate 格为 $\mathcal O_{K_p}+p^{-1}u\mathbf Z_p$，乘子环 $\mathbf Z_p+p\mathcal O_{K_p}$，是 Gross 准典提升的第一层。Wewers, *Canonical and quasi-canonical liftings*, Th. 3.2、Cor. 4.7，证明该层的通用形变模量是全分歧度 $[\mathcal O_{K_p}^\times:(\mathbf Z_p+p\mathcal O_{K_p})^\times]=p+1$ 扩张的 uniformizer。换为当前整光滑参数 $v$ 不改赋值：线性系数为单位，常数属于 $pW$，其余项赋值更大。Gross–Hopkins 的等变刚性周期映射把通用 Hodge 线映到特殊纤维等晶体的射影线；在本首闭盘它具体由 $(P(v):vQ(v)/6)$ 给出，因为(R2)的水平基解逐项收敛且 Wronskian 可逆。两种标记下 $q_D$ 在等晶体上是特殊 $\mathrm{Fr}$，它满足 $\mathrm{Fr}\,t=\bar t\,\mathrm{Fr}$ 对 $t\in K$；故其拉回交换 $e_0$、$e_1$ 两轴。又 $q_D^*$ 把目标 Hodge 线映回原 Hodge 线 $\langle e_0\rangle$，于是目标线为 $\langle e_1\rangle$，即 $P(v_D)=0$。这些 $d$ 个点彼此不同：若带上述全水平标记的商同构，复格超格 $\mathcal O_K+p^{-1}u\mathbf Z$ 扩到最大序都为 $p^{-1}\mathcal O_K$，相似只能为全局单位；在公共 prime-to-$p$ 水平上该单位还须恒等，只能为1，故两核相同。由首圈零的数目已尽，这给全部端点的几何识别。

原文 https://smf.emath.fr/download/pdf/42655 （Wewers, Cor. 4.7）；https://arxiv.org/abs/math/9401220 （Gross–Hopkins, §1）。

## 16. 同一三级规范微分的目标一阶与完整二阶返回

保留(Z1)–(Z5),(U1)–(U8),(W1)–(W8)。对每个130商 $E_C$ 在中心取 $\omega_C^*=u_C\kappa_C$，故 $f_3(E_C,q_C\alpha_3,\omega_C^*)=f_3(0)$。令 $\eta_C^*$ 为互补 CM 特征轴上唯一向量，使其与 $\omega_C^*$ 的 de Rham cup 等于原 $\omega,\eta=x\omega$ 的 cup。相对于(Q1)的原两条水平基，$q_C^*$ 在中心的两轴及其水平延拓为
$$ q_C^* e_{0,C}^*=u_C e_0,\qquad q_C^* e_{1,C}^*=130u_C^{-1}e_1. \tag{V1}$$
第二项的130由 $\langle q_C^*\xi,q_C^*\zeta\rangle=130\langle\xi,\zeta\rangle$ 得到。$q_C$ 在中央同源变形的整邻域延拓，因130素于$p$。对于该族中 $q_C^*\kappa_C(v)=\omega(v)$ 的微分，写 $\kappa_C=h_C(e_{0,C}^*+w_C e_{1,C}^*)$，即
$$ h_C=P/u_C,\qquad w_C=\tau_C w,\qquad \tau_C=u_C^2/130. \tag{V2}$$
故若 $\widetilde c_C(n)=[w_C^n]h_C G_C$ 是真正由该三级规范微分出发的水平系数，则
$$c_C(n)=u_C\tau_C^n\widetilde c_C(n).\tag{V3}$$

取 $k=p^a$，令 $a$ 遍历固定公倍数的倍数使每个 $p$ 进单位 $\tau_C$ 的 Teichmüller 部分满足 $\omega_p(\tau_C)^{p^a}=\omega_p(\tau_C)$。因仅有72个固定代数数，一个固定剩余域次数的倍数足够。写 $\zeta_C=\omega_p(\tau_C)^d,\ l_C=\log_p\tau_C=2\log_pu_C-\log_p130$。用(W4)的同一标量规范，令
$$ \widetilde S_C(k)=\zeta_C
 \frac{(\pi/6)^{dk}\widetilde c_C(dk)}
 {\kappa^k\binom{dk}k} .
$$
于是 $S_C(k)=u_C e^{dk l_C}\widetilde S_C(k)$ 对 $a$ 大准确成立，$S_C$ 是(W4)对单个 $g=G_C$ 的真实返回。由(W5)逐项得到
$$ \widetilde S_C(k)=f_3(0)+k\,T_{1,C}+k^2T_{2,C}+o(k^2). \tag{V4}$$
这里分子已用同一三级规范框计算，两个 $T_{i,C}$ 由相同极限唯一决定。具体
$$ T_{1,C}=s_1(G_C)/u_C-d l_C f_3(0),\qquad
 T_{2,C}=s_2(G_C)/u_C-dl_C\,s_1(G_C)/u_C+
                 (d l_C)^2 f_3(0)/2.$$

对 $n=dk$，$6\mid n$。实际 $G_{aC}(v)$ 和 $G_C(v)$ 用 $\mu_6$ 在 $v$ 上的转动、原三级重标和微分权一相消，故 $c_{aC}(n)=c_C(n)$（与(Y3)同样逐项；此处 $\epsilon_0(a)=a^{-1}$）。故216物理行在本数列确为三份72类。由(W6)的 $s_1(f_b)=0$ 与(Z5)得
$$\boxed{\sum_{C\in H}\chi_b(C)^{-1}u_C T_{1,C}
             =-2d f_3(0)\sum_{C\in H}\chi_b(C)^{-1}u_C\log_p u_C\ne0.}\tag{V5}$$
因 (U6)右边确实非零。这将权一单位导数认作同一个目标水平变化的一阶加权值。然后用(V4)的二次项可精确写
$$\boxed{
65 f_1(0)(d\log_p\rho)^2[T^2]\mathcal A_b
 =3\sum_{C\in H}\chi_b(C)^{-1}u_C
 \left(T_{2,C}+d l_C T_{1,C}
       +\tfrac12(d l_C)^2 f_3(0)\right).}\tag{V6}$$
右边是全部目标二阶、水平一阶与移动规范以及中心二次对数。对每条曲线，删去目标变化将已经破坏(V5)。其二阶的剩余结论仍由(W8)的同一真实定端点积分决定。
