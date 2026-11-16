# 原同角色有限 Schwartz、单位 CM 伸缩与完整中央 germ

日期：2026-11-16。**状态：已证明。**

本篇支付一种具体的同角色闭包。保持原 Hermitian 类、无穷 Hermite 规范、原有限角色及目标 $p$ 处来源，只改变有限多个辅助处的 Schwartz 向量，再作原角色的紧子群投影。所得实际 theta 来源是原来源的有限个范数一 CM 伸缩之和。普通处的整个单位 Mellin germ 和惰性处的整个 Gaussian–Newton germ 都准确运输。

这个闭包不增加独立的中央标量。在惰性处，它的原 $p+1$ 首行模 $p$ 只读一个原值；全 Gaussian 的下一位与所有 Hurwitz 行也由下文的一个真实下三角矩阵运输。共同有限覆盖上的这些来源仍位于同一个 sigma–椭圆函数域的代数扩张中。本篇不据此排除重新支付整个来源格后可能获得的预算改善，但不把向量数、较高中央零阶或形式伸缩极限计成这种改善。

## 1. 原角色和允许的变动

取原
$$
 K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
 T=\ker(\operatorname{Res}_{K/\mathbf Q}\mathbf G_m\longrightarrow\mathbf G_m).
$$
先以 R290/R757 的原 $S_{34}$ 为来源 $F$。其全权角色必须写为
$$
 \Phi_n=\eta\,\psi_{\rm base}^{\,2n+1},\qquad n\ge0,\quad6\mid n,
 \tag{1}
$$
保原有限 $\eta$，而不是把整个 $\eta\psi_{\rm base}$ 升到 $2n+1$ 次。下证同样适用于已经支付同一模型的其它原 type-zero 纯角色线。

固定 Yang 的原 splitting character $\chi$、Hermitian 类、标准极化与全有限向量 $\varphi^0_f$。令 $\eta_n$ 是对应的环面角色。其在每个有限紧子群上的限制与 $n$ 无关；记为 $\eta_0$。这是 (1) 与 $6\mid n$ 的实际有限角色结论：基础 CM 角色在坏处的有限单位因子被 $2n$ 次幂消掉，而原 $\eta$ 全保。

在 nonsplit 处取紧群 $C_v=T(\mathbf Q_v)$；在 split 处通过
$T(\mathbf Q_\ell)\simeq\mathbf Q_\ell^\times$ 取
$C_\ell=\mathbf Z_\ell^\times$。同角色投影是
$$
 {\cal P}_v\varphi
 =\int_{C_v}\eta_{0,v}(c)\,\omega_{\chi,v}(c)\varphi\,dc,
 \qquad\operatorname{vol}(C_v)=1.
 \tag{2}
$$
因此投影像的 eigencharacter 是 $\overline{\eta_{0,v}}$。这里原 $2,3,17$ 的 splitting、半特征和相位没有换成平凡模型。

允许的 $\varphi_f$ 只在固定有限集 $\Sigma$ 改变；目标 $p\notin\Sigma$ 处仍取原向量。在新 split 辅助处原角色未分歧，参考向量在 Yang 的自然极化中是 $\mathbf1_{\mathbf Z_\ell}$。所有变动先施 (2)。未施 (2) 的任意 Mumford 平移或有限加性扭曲不属于本篇结论。

Schwartz 向量及投影均具有有限定义：紧群作用在该向量上有开稳定子，(2) 是有限商上的平均。有限 Weil 矩阵、Gauss 因子和平均分母均为代数数。

## 2. 局部闭包的准确形状

Yang，*Theta liftings and Hecke L-functions*，Corollary 2.4，给出：在固定 nonsplit Hermitian 模型中，给定合法环面角色的 Schwartz 本征空间恰为一维。因此该处 (2) 的像是原参考向量的一个代数倍数，也允许为零。

在 split 辅助处，Yang Corollary 2.10 的自然极化是
$$
 \omega_\chi(g)f(x)=\chi_\ell(g)|g|_\ell^{1/2}f(xg).
 \tag{3}
$$
从标准极化到 (3) 必须用原文 (2.25)–(2.28) 的实际 intertwiner。它是代数有限 Schwartz 转换，不删 quadratic phase。

这里原单位角色平凡，所以 (2) 在 (3) 中就是单位平均。投影后的 $f$ 径向。若 $r_k$ 是其在 $v_\ell(x)=k$ 上的值，则存在整数 $k_0\le k_1$，使
$r_k=0$ 对 $k<k_0$，且 $r_k=f(0)$ 对 $k\ge k_1$。故有**函数身份**
$$
 f=\sum_{k=k_0}^{k_1}(r_k-r_{k-1})\,\mathbf1_{\ell^k\mathbf Z_\ell}.
 \tag{4}
$$
不是只说一个局部积分商为一维。每个球又准确为
$$
 \mathbf1_{\ell^k\mathbf Z_\ell}
 =\chi_\ell(t_\ell)^k|t_\ell|_\ell^{k/2}
       \omega_\chi(t_\ell^{-k})\mathbf1_{\mathbf Z_\ell},
 \qquad v_\ell(t_\ell)=1.
 \tag{5}
$$

作为交叉核对，原 Mellin functional 为
$$
 Z_n(f)=\int_{\mathbf Q_\ell^\times}
 f(x)(\chi_\ell\eta_{n,\ell})(x)|x|_\ell^{1/2}d^\times x.
$$
若 $T_{\ell,n}=(\chi_\ell\eta_{n,\ell})(t_\ell)\ell^{-1/2}$，则
$$
 (1-T_{\ell,n})Z_n(f)
 =\sum_k(r_k-r_{k-1})T_{\ell,n}^k.
 \tag{6}
$$
先在收敛域中计算，再作有理延拓。后文不以 (6) 的商或一个可能为零的全局值定义归一化；真正使用的是 (4)–(5)。

## 3. 全局线性 theta 身份，保绝对相位

因为 $K$ 类数为一，对每个 split $\ell\in\Sigma$ 选
$(\alpha_\ell)=\mathfrak l$，令
$$
 \kappa_\ell=\alpha_\ell/\bar\alpha_\ell\in K^\times,\qquad
 \operatorname{N}\kappa_\ell=1.
 \tag{7}
$$
固定 split 标识，使 $t_\ell=(\kappa_\ell)_\ell$ 在所选 $\mathfrak l$ 方向赋值一。其它有限处分量属于相应紧群。

使用原 Hermite 参数。Yang 1999，Lemma 1.1，的规范给
$$
 \omega_\infty(t)\varphi_{\infty,n}=t^n\varphi_{\infty,n}
 \quad(t\in T(\mathbf R))
 \tag{8}
$$
在原固定 splitting 下；若把 $T$ 的两坐标交换，则 (7) 和所有 $k$ 同时反向，而不是另改相位。

theta distribution 对有理 $T(\mathbf Q)$ 的完整 Weil 作用不变。在其它有限处，原向量是
$\overline{\eta_{0,v}}$-本征向量。由 (5)、(8) 与主 idèle 的全局角色乘积，球 $k$ 对第 $n$ 个原 Hermite 值的作用准确为
$$
 C_\ell^k\kappa_\ell^{kn},\qquad
 C_\ell=(\chi_\ell\eta_{0,\ell})(t_\ell)|t_\ell|_\ell^{1/2}.
 \tag{9}
$$
例如对 $t=\kappa_\ell^{-k}$，无穷处分量是
$\kappa_\ell^{-kn}$，其它有限处的本征乘积由
$\eta_0(t)=1$ 给出；移到等式另一侧，再乘 (5) 的常数即得 (9)。
所以 (9) 在原 Hermite 值为零时仍成立，未通过除以质量、中心 $L$ 值或任何 theta 值选择符号。

R290/R757 的 Hermite-to-Taylor 常数只依赖 $n$、原 Hermitian 参数和共同周期，完全不依赖这里的有限向量。因此对全部 $6\mid n$，(9) 给同一物理变量的 Taylor 身份。其它角型由原 $\mu_6$ 对称为零。对多个辅助处用 (4) 的有限张量展开，得到
$$
 \boxed{\quad
 F_\varphi(z)=\sum_{\mathbf k}a_{\mathbf k}\,
                  F(\kappa_{\mathbf k}z),\qquad
 \kappa_{\mathbf k}=\prod_{\ell\in\Sigma,\ {\rm split}}
                      \kappa_\ell^{k_\ell},\quad
 \operatorname{N}\kappa_{\mathbf k}=1.
 \quad}
 \tag{10}
$$
所有 $a_{\mathbf k}\in\overline{\mathbf Q}$ 是 (2)、(4)、(9) 的实际有限系数。原 nonsplit 标量、split 模因子 $C_\ell$、半特征和周期均在其中。

(10) 是原线性 theta distribution 的源身份。它没有从 Yang 的平方范数公式选平方根，也没有从单个经典点的局部 multiplicity one 推导 $p$-adic germ。

## 4. 普通处：同一测度的整个 germ

固定好普通 $p\notin\Sigma$，并避开 (10) 的有限系数分母。由 (7)，每个
$\kappa_{\mathbf k}$ 在所选 $K\hookrightarrow\mathbf Q_p$ 下属于
$\mathbf Z_p^\times$。使用原共同 $p$-adic 周期，(10) 精确给
$$
 \nu_\varphi=\sum_{\mathbf k}a_{\mathbf k}
                    [\kappa_{\mathbf k}]_*\nu_F.
 \tag{11}
$$
右侧是实际有界测度；其 Amice/Fourier 展开与 (10) 相同，故由唯一性即为原来源的测度。

按原 principal 分支写
$$
 J_{F,p}(u)=\int_{\mathbf Z_p^\times}
       \langle x\rangle^{d_pu}\,d\nu_F(x).
$$
整个实际单位切割保持，于是
$$
 \boxed{\quad
 J_{\varphi,p}(u)=Q_{\varphi,p}(u)J_{F,p}(u),\qquad
 Q_{\varphi,p}(u)=
   \sum_{\mathbf k}a_{\mathbf k}
       \langle\kappa_{\mathbf k}\rangle^{d_pu}.
 \quad}
 \tag{12}
$$
这是收敛圆盘上的整解析恒等式，不只在正整数权上成立。若写
$d_p=p-1$，就使用原 $p-1$ 规范；本式没有另调权变量。

完整一阶式为
$$
 J_{\varphi,p}'(0)=
 \Big(\sum a_{\mathbf k}\Big)J_{F,p}'(0)
 +d_p\Big(\sum a_{\mathbf k}\log\langle\kappa_{\mathbf k}\rangle\Big)
    J_{F,p}(0).
 \tag{13}
$$
原 $F=S$ 的单位域质量为 $J_{F,p}(0)=0$。因此原中央失败给
$J_{\varphi,p}'(0)=0$，但 (13) 中的 scale-log 项是由原质量消去，不能在其它质量非零的参考线上删除。

## 5. 惰性处：全部 Newton 和真实 Gaussian 修正

令 $p\equiv5\bmod6$，$d=p+1$，使用 R598 的同一原规范
$$
 X=z^d,\quad \alpha=mc,\quad a=p\alpha\in{\cal O}^{\times},\quad
 G=F e^{-\alpha X},\quad
 G_0=\Pi_0G=\sum_{h\ge0}g_hX^h.
$$
原 $F(0)=0$，故 $g_0=0$。完整原函数为
$$
 J_{F,p}(u)=\sum_{h\ge0}g_h\alpha^{-h}(u)_h.
 \tag{14}
$$
每个 $\kappa=\kappa_{\mathbf k}$ 是惰性局部单位且 Norm 一，所以
$$
 b_\kappa=\kappa^{p+1}=1+pq_\kappa,\qquad q_\kappa\in{\cal O}.
 \tag{15}
$$
Norm 一保证伸缩来源仍用同一个 Gaussian charge $m$。其**实际**余项为
$$
 \boxed{
 G_{\kappa,0}(X)=
   e^{a q_\kappa X}G_0(b_\kappa X),\qquad
 g_{\kappa,h}=
 \sum_{j=0}^h
 \frac{(a q_\kappa)^{h-j}}{(h-j)!}\,b_\kappa^j g_j .
 }
 \tag{16}
$$
不得删掉 $q_\kappa$。它是原完整 Fermat 商，不由 $p$ 的固定 ray 类决定。

(16) 仍满足原 Newton 收敛条件：单位伸缩保原闭盘，$a q_\kappa$ 整，新增指数在原严格内盘收敛。对非负整数 $u=N$，下降阶乘只到 $h=N$，所以有限二项式计算给
$$
 \begin{aligned}
 \sum_{h=0}^N\alpha^{-h}(N)_h g_{\kappa,h}
 &=\sum_{j=0}^N\alpha^{-j}(N)_j b_\kappa^j g_j
   \sum_{l=0}^{N-j}
       \frac{(b_\kappa-1)^l}{l!}(N-j)_l\\
 &=b_\kappa^N J_{F,p}(N).
 \end{aligned}
$$
两边都是原收敛解析 germ，非负整数在 $\mathbf Z_p$ 稠密，故
$$
 \boxed{
 J_{\kappa,p}(u)=b_\kappa^uJ_{F,p}(u),\qquad
 J_{\varphi,p}(u)=
   \Big(\sum_{\mathbf k}a_{\mathbf k}b_{\kappa_{\mathbf k}}^u\Big)
     J_{F,p}(u).
 }
 \tag{17}
$$
证明没有交换未经控制的无限双和，也没有只证明前三权。

因此在两类好素数上，原 $J(0)=0$ 都给
$$
 \boxed{
 j_{\varphi,p}=
 \Big(\sum_{\mathbf k}a_{\mathbf k}\Big)j_{F,p}.
 }
 \tag{18}
$$
中央标量在这个实际轨道上只有一条；每个 $\kappa$ 不是新的独立零条件。

## 6. 实际首行、下一位与全 Hurwitz 运输

记原实际首系数 $A_p(F)=[z^{p+1}]F$。由 (10) 逐系数，
$$
 \boxed{
 A_p(F_\varphi)=
   \Big(\sum_{\mathbf k}a_{\mathbf k}b_{\kappa_{\mathbf k}}\Big)A_p(F).
 }
 \tag{19}
$$
于是对整系数，
$$
 A_p(F_\varphi)\equiv
   \Big(\sum a_{\mathbf k}\Big)A_p(F)\pmod p.
 \tag{20}
$$
即使先有 $A_p(F)\in p{\cal O}$，再把这一首行除 $p$ 后约化，
仍只乘 $\sum a_{\mathbf k}$；不能据此得到第二个原 forcing。

(16) 的前两行是
$$
 g_{\kappa,1}=b_\kappa g_1,\qquad
 g_{\kappa,2}=b_\kappa^2g_2+
                  a q_\kappa b_\kappa g_1.
 \tag{21}
$$
先用形式 $X$-Hurwitz 坐标 $\gamma_h=h!g_h$ 可将(16)简写为
$$
\gamma_{\kappa,h}
=\sum_{j=0}^h
 \binom hj(aq_\kappa)^{h-j}b_\kappa^j\gamma_j.
\tag{22}
$$
(22)的矩阵整且主对角为单位，但这本身没有断言原实际
$\gamma_h$ 全部整。原来源的实际整格是
[R602](../results/R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)
在 $w=z^6$ 变量上支付的 Hurwitz 格。
因 $F(0)=g_0=0$ 且原 $F$ 从 $w$ 起始，它准确给
$$
\Gamma_h=(hs-1)!\,g_h\in\mathcal O,\qquad h\ge1.
$$
将(16)乘这个实际阶乘，得到全部 $h\ge1$ 的原整运输
$$
\boxed{
\Gamma_{\kappa,h}
=\sum_{j=1}^h
 \frac{(hs-1)!}{(js-1)!(h-j)!}
 (aq_\kappa)^{h-j}b_\kappa^j\Gamma_j.
}
\tag{22a}
$$
令 $L=s(h-j)$，括号中的整数准确为
$$
\binom{hs-1}{L}\frac{L!}{(h-j)!}\in\mathbf Z.
$$
其主对角仍是 $b_\kappa^h$；逆运输用 $b_\kappa^{-1}$、
$q_{\kappa^{-1}}=-q_\kappa/b_\kappa$ 的同一个式子，也是整矩阵。
因此(22a)真正保存每个原 $w$-Hurwitz 前缀整格，且无 $h$ 上界。
单位伸缩与整指数乘法也直接由 R602 的整代数闭性保证这些伸缩来源处于同一格。

这只是目标整格的准确运输，不将新增全局来源列免费加入旧原单项式格，
也不支付任意原有序核的 Schur 提升。
对质量非零的其它参考线，必须保留(13)的质量项和(16)的 $j=0$ 项；
本段 $h,j\ge1$ 的真实格与(18)的单行结论限于已指明的零质量来源。

有限差 $F(\kappa z)-F(z)$ 给
$$
 J_{\rm diff}(u)=(b_\kappa^u-1)J_F(u).
$$
其较高中央零阶是 (17) 的准确结果；它不提供额外的原 $j_F$ 条件。无限 $\kappa\to1$ 后除小参数、换成 $zF'$ 的操作不在这里的固定有限整格中。

## 7. 固定覆盖和真正的来源成本

对 (10) 的有限集合，取一个固定 $\beta\in{\cal O}_K\setminus\{0\}$，使
$\alpha_i=\beta\kappa_i\in{\cal O}_K$。所有 $\alpha_i$ 与 $\beta$ 的 Norm 相等。若需消 half-character，进一步作共同固定二倍覆盖。

在 $z=\beta w$ 上，同次数的两个 sigma 拉回之比是代数椭圆函数：
$$
 \frac{\sigma(\alpha_iw)}{\sigma(\beta w)}
 \in\overline{\mathbf Q}(E_{\rm cover}).
 \tag{23}
$$
理由是其线丛 pullback degree 相等，CM 准周期的二次项按
$\alpha_i\bar\alpha_i=\beta\bar\beta$ 准确抵消；可能的二挠 flat 因子由刚才固定二倍覆盖消掉。归一常数由原 sigma 首项固定。其余 $x(\alpha_iw),y(\alpha_iw)$ 是真实 isogeny 有理函数。

所以所有 $F(\kappa_i z)$ 在共同固定覆盖上属于同一个
sigma–椭圆函数域，并对原 $\overline{\mathbf Q}(\sigma,x,y)$ 代数。
这没有产生新的代数独立第五坐标。覆盖次数、拉回线丛 degree、各真实除子和全部单项式格必须重新计入；本篇没有把它们与旧 R365/R821 的原 carrier 相认。

另一方面，它们可以是线性独立的整 theta 截面。本篇不凭“代数相关”否定任何未来的完整旗标改善。当前精确已付的是：同一角色的辅助 Schwartz 闭包给 (10)、完整 germ 给 (12)/(17)，原首中央行给 (19)，全 Gaussian 系数运输给 (22)，原实际整格运输给 (22a)。若要用于严格预算，尚需这个**实际有限覆盖来源格**的完整成本与原中央假设下的新有效估计。

## 8. 资料和范围

无新数值计算或目标素数扫描。本篇的局部函数展开、全局线性身份和 Newton 运输均为符号证明。

- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. 485 (1997), 25–53；Corollary 2.4、Corollary 2.10、(2.12)、(2.25)–(2.28)：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*, Compositio Math.117 (1999),337–359，Lemma1.1 的同一 Hermite 特征：
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- [R757](../results/R757-original-type-zero-six-spectrum-and-order-nine-lines.md)：原完整 finite role、Hermite/Taylor 与 period，尤其全权角色不能换成裸幂。
- [R598](../results/R598-original-full-newton-derivatives-and-central-euler-stokes.md)：原完整 Newton、Gaussian 和中央投影。
- [R812](../results/R812-original-same-charge-cancellation-and-complete-source-budget.md)：原倍点完整运输、固定来源格与主预算的区别。

本篇不包含改变目标 $p$ 处 Schwartz、改变全局 Hecke 角色、未作 (2) 的原物理平移、任意正多项式乘子，或无限伸缩极限。那些操作若要传播原中央，仍须给各自的实际完整来源和整 germ。
