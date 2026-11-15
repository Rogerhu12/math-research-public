# R398：完整低层自然通量不能同时为零

日期：2026-11-15。**完整纸面推论；没有执行新的 profile、积分、原根、秩、人工检查或科学运行。**

[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md) 已给完整 Q4 自然像的九维结构和两个仿射字符头。本稿把其中权 $-2$ 的头与 [R188](R188-no-nonzero-positive-affine-character-at-weight-minus2.md) 的原完整正性定理接合，得到一个必须保留的结论：
$$
\boxed{
\text{原 }F_0\text{ 与三个 }\widehat Q_2\text{ 的自然读出，不可能对全部实际状态同时恒零。}}
\tag{1}
$$
这里是实际 $U$ 中正规生成族的存在性结论，不指定哪个状态、哪个速度二次槽非零，也没有计算这些低层的完整 action。它不使用任何尚未证明的增强联合控制。

## 1. 原定义和已付来源

记 $U$ 为原完整 canonical 第四成本的真实实线性空间，$\mathcal R$ 为全部已实现响应空间。共同右锚和真实 histories 均按原定义保留。

令
$$
\mathcal N:U\longrightarrow\{\text{紧 profile 上的五次函数}\},
\qquad
(\mathcal N V)(u)=\Lambda_u(V),
\tag{2}
$$
其中 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的完整读出为
$$
\Lambda_u(V)
=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{3}
$$
$\mathscr G$ 是原 pure 的有序三矩尾映射；中间输出的真实左尾不删。已付
$$
\mathcal N(\mathcal R)=0.
\tag{4}
$$
[R365 第5节](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md) 中独立有效的仿射协变为
$$
\mathcal N(\mathsf P_{a,c}V)(u)
=a^2(\mathcal N V)(C_{a,c}u),
\qquad C_{a,c}u(x)=u((x-c)/a).
\tag{5}
$$
本稿仅使用该协变及真尾输运，不使用后来已更正的旧 H 非零结论。

[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md) 给出完整十四族的真实跨度：
$$
U=\mathcal R+\operatorname{span}_S
\{F_0,\widehat Q_{2,0},\widehat Q_{2,1},\widehat Q_{2,2},
\bar A_{hh},\bar A_{hk},\bar A_{kk},H_1,H_2,
\widehat Q_{4,0},\ldots,\widehat Q_{4,4}\}.
\tag{6}
$$
这里取全部实际状态值；不是把十四个标签当作维数。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 已付三个完整加速度平方族的自然读出为零；[R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md) 已付完整更正后的两个 H 族为零：
$$
\mathcal N(\bar A_{hh})=\mathcal N(\bar A_{hk})
=\mathcal N(\bar A_{kk})=\mathcal N(H_1)=\mathcal N(H_2)=0.
\tag{7}
$$

## 2. Q4 的一个非零真实仿射字符

采用
$$
v=u',\quad r=u'',\quad t=u''',\quad
L=v-xr,\quad d=h\omega-k,\quad
\gamma=h_s,\quad\delta=d_s.
$$
[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md) 的完整公式是
$$
\Lambda_u(\mathcal Q_S[\gamma,\delta])
=-\frac1{32h^8}
\int\{1+(hx+d)^2\}(\gamma L-\delta r)^4t.
\tag{8}
$$
$\mathcal Q_S[\gamma,\delta]$ 是完整正规四次速度成本，而非单个未付 ambient 项。

令 $\mathscr A_4$ 为(8)全部状态及速度值的自然函数跨度。R393 已从完整分部积分和 Euler 自由 jets 证明：它恰九维，仿射稳定，真成本权为 $-7,\ldots,-2$。其中权 $-2$ 只有一个非零函数
$$
K(u)=\int x^2L^4t=\frac15\int L^5.
\tag{9}
$$
权 $-1$ 及以上在 $\mathscr A_4$ 中为零；原平移导子将真权降低一。因此定义
$$
\ell(K)=-1,\qquad
\ell|_{\mathscr A_{4,\sigma}}=0\quad(\sigma\ne-2)
\tag{10}
$$
得到 $\mathscr A_4$ 上良定义、非零的真实线性泛函，满足
$$
\ell\circ\mathsf N=0,\qquad
\ell\circ\mathsf D_a=a^{-2}\ell.
\tag{11}
$$
它不是有限 profile 取值或未检验的 formal 系数。

由(8)中唯一的权 $-2$ 项，准确有
$$
\boxed{
\ell\bigl(\mathcal N(\mathcal Q_S[\gamma,\delta])\bigr)
=\frac{\gamma^4}{32h^6}\ge0.}
\tag{12}
$$
取 $\gamma\ne0$ 时严格正。这只是 Q4 层的 action；在下节的反证假设之外，不能把 $\ell$ 自动延拓到整个自然像。

## 3. 假定全部低层零将产生 R188 禁止的字符

反设对所有实际状态及每个速度二次槽，
$$
\mathcal N(F_0)=0,\qquad
\mathcal N(\widehat Q_{2,j})=0,\quad j=0,1,2.
\tag{13}
$$
由(4)、(6)、(7)，有
$$
\mathcal N(U)=\mathscr A_4.
\tag{14}
$$
包含 $\mathscr A_4\subseteq\mathcal N(U)$ 用的是 R130 的实际正规系数属于 $U$；反向包含才使用反证假设(13)。

所以此时可以在整个原 $U$ 上定义
$$
\lambda=\ell\circ\mathcal N.
\tag{15}
$$
它良定义且杀 $\mathcal R$。由(5)、(11)，它是权 $-2$ 的真实平移不变仿射字符。由(12)和实际 Q4 系数非零，$\lambda\ne0$。

还须验证它对原真实路径成本非负，不能只看(12)的形式最高项。对任一原有限同常值端口、闭 frame 且 $M=T=0$ 的真实路径 $B$：

- [R109](R109-local-density-of-the-complete-fourth-quotient.md) 的完整局部化把原成本与 $\int(v-\mathcal B_mN)$ 的差准确放在 $\mathcal R$；
- 原八矩归一化减去同一个 $\Gamma m$，其积分为 $\Gamma M_B=0$，没有只删静态矩阵部分；
- [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的全部正导数权边界势在两个常值 germs 准确为零；
- 其余正规项按(7)、(13)被同一个 $\lambda$ 消去。

所以完整实际身份为
$$
\boxed{
\lambda(V_B)
=\int_B\frac{h_s^4}{32h^6}\,ds\ge0.}
\tag{16}
$$
原 $N_0,N_2$、全部 $\Gamma$、真实历史以及边界并未被预先设零；它们通过上述原完整身份进入(16)。

这里覆盖的正是 R188 定理所用的实际成本类。原 $U$ 由固定同端口 $M=T=0$ 成本取实跨度，且 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 已证明真实跨度与 scalar germ 无关。R188 不要求统一的先验长度或窄状态盒；每条有限路径均按原实际约束 $\omega_s=k_s/(2h)$ 取合法共同窗口。本稿没有用实际成本的负数替代一条真实路径。

R188 的完整结论是：任何杀 $\mathcal R$、权 $-2$、平移不变并在全部这些实际成本上非负的线性泛函必须为零。因此(15)–(16)迫使 $\lambda=0$，与(12)矛盾。反证完成，得到(1)。

## 4. 准确的新结论与仍欠的具体值

式(1)说明：至少存在一个实际状态和一个原静态或速度二次正规系数，其自然函数不是零；等价地，对某个真正紧光滑 $u$ 有非零 $\Lambda_u$。这是 R130 中实际 $U$ 系数的存在性，不是任意 ambient 势的存在性。

它不证明该低层函数必在九维 $\mathscr A_4$ 之外。可能的两种情形仍须区分：

1. 低层扩大完整自然像，导致(10)不能在新真实关系下延成整个自然像的仿射字符；
2. 低层仍落在 $\mathscr A_4$，但改变(16)的完整 action。在这种附加假设下，(15)仍是非零真实字符；R188 保证它不可能在全部实际成本上非负，故必有真实有限成本使其为负。

第二条是明确条件性结论，不是已构造的负成本词，也不是任意目标的联合截面。

本稿没有判定 $F_0$ 和三个 $\widehat Q_2$ 各自的准确函数，也没有判定 $\Lambda(U_0)$。下一原式仍是
$$
L_0=v_0-\mathcal B_{m_0}N_0,\qquad
L_2=v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0,
$$
随后保留同一个 $\Gamma m_0,\Gamma m_2$ 和完整水平正规化。Q4 没有零权不能代替这些低层；旧 $E=(\text{whole pure},\text{whole self})$ 的投影等像也不能代替新自然通量关系。

这不改变 R333 的 whole $E$ 实际控制、R390 的两个固定自然通量实际控制或 R392 已保完整基准的响应分量联合截面。它仅严格排除“全部低层自然零，所以只剩 Q4”这一捷径。
