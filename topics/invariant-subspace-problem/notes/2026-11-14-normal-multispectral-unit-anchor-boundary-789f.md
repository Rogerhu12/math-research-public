# 多谱压缩的后继检查：仅凭正性、正常近真空及原有限秩不能给通用头矩单位锚

2026-11-14，normal-annihilator / 789f。接续记录，不登记新的主编号。用途是保留 R291 最大单谱压缩之后已经核清的一个边界，避免把该单位锚未经证明推广到任意多谱压缩。

## 1. 本轮已完成而应从正式结果继续的内容

R291 主体给实际正常头矩在 $\mathbb C(z)$ 上的独立性、算子 Schmidt 秩和同一正链的指数支撑秩。

后继附录依次给：[固定头有限矩距离](../results/R291-appendix-fixed-head-finite-moment-distance-and-spectral-mass.md)、[固定次数归一化矩](../results/R291-appendix-normalized-tail-moments-and-explicit-spectral-mass.md)，以及[最大尾谱压缩的正头常数项锚和完整尾理想距离界](../results/R291-appendix-positive-spectral-compression-and-full-tail-quotient-cost.md)。最后一份用同一原正态推出

$$
\epsilon_{j+1}=1-\lambda_{\max}(\nu_{j+1})
\ge[128(1+m_j)]^{-2}
$$

（所有充分深 $j$），其中 $m_j$ 是真实 $Z_j$ 到同一完整下一尾理想的距离，并给 $\liminf m_j\sqrt{\epsilon_{j+1}}\ge1/16$。旧 $r_j$ 是本位 Walsh-minus 质量，二者不混同。

## 2. 一个原普通秩一、任意近真空的头矩边界

固定真实头维数 $q=2^M\ge8$，保留 R291 的实际循环加权矩阵 $J(z)$。它的每个 $1\le j<q$ 次幂对角全为零，因为走不足 $q$ 步不能回到同一个物理坐标：

$$
\langle J(z)^j e_0,e_0\rangle=0\quad(1\le j<q).
\tag{2.1}
$$

取远尾单位向量 $v_1=\Omega_{\rm far}$、$v_2\perp v_1$，并置

$$
f_p=\sqrt p\,\Omega_{\rm head}\otimes v_1
+\sqrt{1-p}\,e_0\otimes v_2,
\qquad0<p<1,
\qquad \sigma_p=|f_p\rangle\langle f_p|.
\tag{2.2}
$$

这里 $v_2$ 可以取任意一个真实尾 Walsh 向量。两条尾向量正交，故 $\|f_p\|=1$，而

$$
\|\sigma_p-|\Omega\rangle\langle\Omega|\|_1=2\sqrt{1-p}\longrightarrow0.
\tag{2.3}
$$

$\sigma_p$ 的普通秩为一。头向量 $\Omega_{\rm head}$ 与 $e_0$ 线性独立，因此其 Schmidt 秩为二，尾边缘秩为二，算子 Schmidt 秩为四，小于 $q$。

在尾矩阵单位 $|v_a\rangle\langle v_b|$ 中展开 $\sigma_p$。其 $(2,2)$ 尾系数对应的头矩阵为 $(1-p)|e_0\rangle\langle e_0|$。因此，任何多项式行

$$
a(z)=(a_0(z),\ldots,a_{q-1}(z))
$$

若同时消去这四个真实头矩列，即对每个尾系数头矩阵 $H_{ab}$ 都满足

$$
\sum_{j=0}^{q-1}a_j(z)\operatorname{Tr}(H_{ab}J(z)^j)=0,
\tag{2.4}
$$

则由 (2.1) 在 $(a,b)=(2,2)$ 一列上立刻得到

$$
\boxed{a_0(z)\equiv0.}
\tag{2.5}
$$

这样的非零行确实存在，因为只有四列而 $q>4$。但每个由这种头矩消元获得的

$$
P(t)=\sum_{j=0}^{q-1}t^ja_j(t^q)
$$

都满足 $P(0)=0$。对应 $p(z)=\det P(C_q)$ 的常数项也为零，所以不能直接使用 $p(z)^{-1}$ 的真实单位锚。

这保留了实际头权和整个 $z$ 多项式，而非只在切掉 carry 后构造一个反例。

## 3. 结论的范围与下一缺口

该例表明：即使比较密度正、普通秩一、尾秩二且任意接近完整真空，R291 中**仅依头矩、同时消去各头列的通用多项式关系**仍可能全部丢失常数项。因此最大单谱压缩使用的正头相干锚不能仅凭这几项条件扩成任意多谱压缩。

这里没有排除另一种使用这些具体尾向量的实际泛函关系所构造的证书。例如有限 Walsh 尾向量会带来额外的原代数关系，必须另外计算其来源与费用，不能由 (2.5) 一并排除。

$\sigma_p$ 不是实际湮灭者：其算子 Schmidt 秩四小于 $q$，R291 已排除这一点。它也没有被声称属于某个实际湮灭链的谱压缩。本记录只阻止从正性、有限原秩和近真空这三个独立条件直接推出多谱单位锚。

继续的实质问题是同一真实 $\nu_j$ 的不同尾谱分量之间，原右零式还给出哪些可支付的关联；或者能否控制完整尾理想距离 $m_j$。现有支撑秩、熵 $o(j)$ 与单谱非纯质量界还未给这种控制。
