# R593 恢复：真实商的迹零线丛、固定 Picard 修正与变化导子的高度支持

日期：2026-11-14。状态：**几何和局部高度规范已证明；对数线性化条件单独列出，由 R596 处理。**

恢复说明：旧 R593 正文及旧清分母符号的字面定义随环境重置丢失。本 v2 副本从同一实际几何重新构造完整可复核的平凡化，并澄清只对完整修正线丛取三次甲板范数，绝不把其 Picard 零次项对称化删去。原已哈希恢复稿保留。以下两整数命名为 \(c_{\rm clear}\)、\(c_{\rm triv}\)，不冒认旧摘要所写的 \(N/M\)，也不移植任何未恢复的旧数值目标集合。所有全局及局部高度均除回同一个明确因子 \(C_h=c_{\rm clear}c_{\rm triv}\)。

## 1. 同一个真实曲线族和 CM 商

设 \(p>37\) 为惰性素数，采用 R575 的实际六层甲板方向。令

\[
 Y=W_p=\operatorname{Norm}\bigl(X_{\rm ns}^+(p)\times_j\mathbb P^1_v\bigr),
 \qquad j=6912v(1-v),
\]
\[
 X_d=\operatorname{Norm}\bigl(Y\times_{v}\mathbb P^1_b\bigr),
 \qquad v=db^3,\qquad\phi_d:X_d\to Y.
\tag{593R.1}
\]

这里 \(d>0\) 立方自由；以下局部支持的统一结论最终限制到 R317 的实际偶分支 \(d\) 奇且 \(d\in\mathbb Q_3^{\times3}\)。\(X_1=Z_p\) 的原变量是 \(a\)，映射 \(v=a^3\)。把原整数关系 \(a^3+db^3=1\) 看作两个曲线上的点时，中间还有 \(Y\) 上 \(v\mapsto1-v\) 的对合；本篇不把它省略为一个商间同态。

在 \(\overline{\mathbb Q}\) 上三次甲板群 \(\mu_3\) 作用为 \(b\mapsto\zeta b\)。其作用作为群概形在 \(\mathbb Q\) 上定义，虽然所选生成元 \(\delta_\zeta\) 只在 \(K=\mathbb Q(\zeta)\) 上定义。

取真实 CM family 中一个 \(\mathbb Q\)-单因子

\[
 q_d:J_d:=J_{X_d}\to A_d,
 \qquad A_d\leftrightarrow
 \operatorname{AI}_{K/\mathbb Q}(\Psi\theta\kappa_4\kappa_d^{-1}).
\tag{593R.2}
\]

\(d\) 的负扭向来自 \(b\mapsto\sqrt[3]d\,b\) 的 cocycle，见本次恢复的 R587；\(\kappa_4\) 正扭向及正 holomorphic CM 型来自已发布 R575。甲板作用在这块上没有不变向量，故

\[
 q_d\phi_d^*=0.
\tag{593R.3}
\]

系数域 \(F\) 全实，\(\operatorname{End}_{\mathbb Q}^0(A_d)=F\)，\(n=[F:\mathbb Q]=\dim A_d\)。在 \(K\) 上的 CM 作用与 \(F\) 交换。可由 CM 诱导表示限制到 \(G_K\) 的两种不同无穷型计算稳定子和自同态，得到这个标准 GL2 型描述；不得把它换成原反向扭曲因子的出现性。

## 2. 有理 CM 基点与粗模参数

在 \(X_{\rm ns}^+(p)\) 上选由 \(E_0\) 的 \(\mu_3\) 保持的实际 CM 项链。非平凡三阶 CM 元的中心化子是唯一的非分裂 Cartan，因此该无向 CM 项链在 Galois 下稳定，是有理点。

其完整三阶椭圆稳定子已包含在取商群内，所以粗模 \(j\) 在这个点的局部零阶为 \(3/3=1\)。\(Y\to X_{\rm ns}^+(p)\) 在 \(j=0\) 的两个 \(v\)-分支 \(v=0,1\) 都 étale，因为 \(d(6912v(1-v))/dv\ne0\)。取 \(v=0\) 的有理点 \(c_{\rm base}\in Y(\mathbb Q)\)。

在 \(c_{\rm base}\) 上，\(v\) 是局部参数。\(v=db^3\) 的规范化有唯一位于 \(b=0\) 的点，剩余域仍为 \(\mathbb Q\)。记作

\[
 c_{0,d}\in X_d(\mathbb Q),\qquad\phi_d(c_{0,d})=c_{\rm base}.
\tag{593R.4}
\]

它被 \(\mu_3\) 固定。设

\[
 \iota_d(x)=[x-c_{0,d}]\in J_d,\qquad
 j_d=q_d\iota_d,
\]
\[
 \iota_Y(y)=[y-c_{\rm base}]\in J_Y,
 \qquad P_d(x)=\iota_Y(\phi_d(x))=\phi_{d,*}\iota_d(x).
\tag{593R.5}
\]

基点固定性使 \(j_d\) 与甲板作用严格交换，不出现未知平移常数。另一 CM 点差 \(q_d[c_{1,d}-c_{0,d}]\) 可以非挠，本篇没有将其置零。

## 3. 极化给出的准确加权迹

先在 \(d=1\) 上取一个 \(\mathbb Q\) 极化，再对 \(\mu_3\) 的三个几何作用取和，使之甲板不变；Galois 只置换两个非平凡生成元，所以和仍在 \(\mathbb Q\) 上定义。沿同一立方扭曲传递，得到全部 \(A_d\) 的固定极化 \(\lambda_d\)。

令 \(\lambda_{J_d}\) 是 Jacobian 的主极化，定义

\[
 q_d^\dagger=\lambda_{J_d}^{-1}q_d^\vee\lambda_d,
 \qquad\kappa=q_dq_d^\dagger\in F.
\tag{593R.6}
\]

\(\kappa\) 是全正元素，并在几何扭曲识别下与 \(d\) 无关。Rosati 在 \(F\) 上为恒等，故

\[
 \operatorname{NS}(A_d)\otimes\mathbb Q\simeq F.
\]

对 \(h\in F\)，令 \(\mathcal L_{h,d}\) 是原点刚性化的对称有理线丛，满足

\[
 \lambda_{\mathcal L_{h,d}}=\lambda_d h.
\tag{593R.7}
\]

拉回次数为

\[
 \deg j_d^*\mathcal L_{h,d}
 =\frac12\operatorname{Tr}_{H^1(A_d)}(h\kappa)
 =\operatorname{Tr}_{F/\mathbb Q}(\kappa h).
\tag{593R.8}
\]

第一等式是 Jacobian 主极化的标准迹/次数公式；第二等式用 \(H^1(A_d)\) 是秩二的 \(F\)-模。于是准确的次数零空间为

\[
 F^0=\{h\in F:\operatorname{Tr}_{F/\mathbb Q}(\kappa h)=0\}.
\tag{593R.9}
\]

\(\dim F^0=n-1\)。没有把实际 \(\kappa\) 删除后误用普通迹零空间；\(n=1\) 时本构造没有非零 \(h\)。

## 4. 固定 Picard 类的下降及 \(d\) 无关性

对 \(h\in F^0\)，置

\[
 \kappa_{h,d}=j_d^*\mathcal L_{h,d}
       \in\operatorname{Pic}^0(X_d)\otimes\mathbb Q.
\tag{593R.10}
\]

甲板元在 CM 域中，Rosati 把它取逆，且它与 \(h\) 交换。因此 \(\delta_\zeta^*\mathcal L_{h,d}\) 和 \(\mathcal L_{h,d}\) 有相同 NS 类。二者均对称，所以它们的 Picard 零次差至多二挠，在 \(\operatorname{Pic}\otimes\mathbb Q\) 中消失。由 (593R.5) 的严格等变性，\(\kappa_{h,d}\) 甲板不变。

有限覆盖的 pull–push 恒等式给

\[
 \phi_d^*\phi_{d,*}=1+\delta_\zeta^*+\delta_{\zeta^2}^*
 \quad\text{于 }\operatorname{Pic}^0(X_d)\otimes\mathbb Q.
\]

故定义

\[
 \eta_h=\frac13\phi_{d,*}\kappa_{h,d},
 \qquad\boxed{\kappa_{h,d}=\phi_d^*\eta_h}.
\tag{593R.11}
\]

范数与整个群作用均在 \(\mathbb Q\) 上定义，所以 \(\eta_h\in J_Y(\mathbb Q)\otimes\mathbb Q\)。

在 \(L=\mathbb Q(\sqrt[3]d,\zeta_3)\) 上，\(b\mapsto\sqrt[3]d\,b\) 识别 \(X_d\) 与 \(X_1\)，固定底曲线 \(Y\) 和基点，且按同一 cocycle 识别 \(A_d,q_d,\lambda_d,h\)。于是 (593R.10)–(593R.11) 在这个识别下完全相同，说明 \(\eta_h\) 与 \(d\) 无关。

若把 \(c_{0,d}\) 换成另一个次数一基点，\(\kappa_{h,d}\) 的改变量在 \(q_d^\dagger A_d^\vee\) 中；而 (593R.3) 的对偶给

\[
 \phi_{d,*}q_d^\dagger=0.
\tag{593R.12}
\]

所以规范化的 \(\eta_h\) 也不依赖这个辅助基点变化。这允许 R596 仅在规范模曲线 \(d=4\) 上用 Hodge 基点计算同一固定类。

## 5. 真正拉回平凡的线丛：正号和因子二

令 \(\Theta_Y\) 给 \(J_Y\) 的主极化 \(\lambda_Y\)。使用 convention

\[
 \lambda_Y(Q)=t_Q^*\Theta_Y\otimes\Theta_Y^{-1}.
\]

Abel 映射的 autoduality 在这一 convention 下是

\[
 \iota_Y^*\lambda_Y(Q)=-Q\quad
 \text{于 }\operatorname{Pic}^0(Y).
\tag{593R.13}
\]

因此真正的修正线丛不是单独的 \(q_d^*\mathcal L_{h,d}\)，而是

\[
 \mathscr L_{h,d}
 =q_d^*\mathcal L_{h,d}
       \otimes\phi_{d,*}^*\lambda_Y(\eta_h)
 \quad\text{于 }\operatorname{Pic}(J_d)\otimes\mathbb Q.
\tag{593R.14}
\]

由 (593R.11)、(593R.13)，

\[
 \iota_d^*\mathscr L_{h,d}
 =\kappa_{h,d}-\phi_d^*\eta_h=0
       \quad\text{于 }\operatorname{Pic}(X_d)\otimes\mathbb Q.
\tag{593R.15}
\]

这也解释后文全局高度的 **正号及因子二**。若 \(h_Y(P,Q)\) 是由 theta 高度极化得到的双线性配对，则 Poincaré 对 \(\lambda_Y(Q)\) 的高度为 \(2h_Y(P,Q)\)。所以 (593R.14) 的高度是

\[
 \widehat h_{\mathcal L_{h,d}}(q_dP)
       +2h_Y(\phi_{d,*}P,\eta_h).
\tag{593R.16}
\]

若改用 Poincaré 配对本身命名 \(h_Y\)，必须同时调整这一因子；本稿及 R596 均固定 (593R.16) 的 theta-polarized convention。

## 6. 新的统一清分母和真实截面

现在把 (593R.15) 的有理 Picard 等式变成可供 BMS Lemma 7.1 使用的实际平凡化。

先在 \(d=1\) 选择正整数 \(c_{\rm clear}\)，清除 \(h\)、\(\eta_h\)、对称线丛和有理同态表示所需的有限分母，使

\[
 \mathscr M_{h,1}=\mathscr L_{h,1}^{\otimes c_{\rm clear}}
\]

是 \(J_1\) 上沿原点刚性化的真实线丛。再对这个**完整修正线丛**取 \(\mu_3\) 范数 \(\mathscr M\otimes\delta^*\mathscr M\otimes(\delta^2)^*\mathscr M\)，并将 \(c_{\rm clear}\) 相应乘上三。因为其完整有理 Picard 类在甲板下不变，范数的类正好是原类的三倍；同时循环置换三个因子给真正的 \(\mu_3\)-线性化，Galois 置换 \(\delta,\delta^2\) 给 Q 下降。沿原点的刚性化使三次复合为恒等，不留下标量 cocycle。这里不对整个 \(\mathscr L_{h,1}\) 作 \([-1]\) 对称化：那会消去关键的 Picard 零次修正项并破坏曲线拉回平凡性。若另外需要消除原对称 \(q_1^*\mathcal L_{h,1}\) 的二挠代表差，只能对该对称部分取偶次幂，并将完整修正一起按相同倍数缩放；上述完整范数构造已经足够，无须这一步。

由 (593R.15)，\(\iota_1^*\mathscr M_{h,1}\) 是一个有限阶 Picard 类。选其有限阶的一个正倍数 \(c_{\rm triv}\)，于是

\[
 \mathscr N_{h,1}=\mathscr M_{h,1}^{\otimes c_{\rm triv}},
 \qquad C_h=c_{\rm clear}c_{\rm triv},
\]
\[
 \iota_1^*\mathscr N_{h,1}\simeq\mathcal O_{X_1}
 \quad\text{作为真实线丛}.
\tag{593R.17}
\]

在拉回线上选无零截面 \(s_{h,1}\)，并按固定的基点刚性化归一为

\[
 s_{h,1}(c_{0,1})=1.
\tag{593R.18}
\]

它是唯一的。因为甲板固定 \(c_{0,1}\) 且保持同一刚性化，\(\delta^*s_{h,1}\) 具有同样归一，故等于 \(s_{h,1}\)。因此整套 \(\mathscr N_{h,1},s_{h,1}\) 可以沿实际立方 cocycle 扭曲下降到每个 \(d\)，给

\[
 \mathscr N_{h,d},\qquad
 \iota_d^*\mathscr N_{h,d}\simeq\mathcal O_{X_d},\qquad
 s_{h,d}(c_{0,d})=1,
\tag{593R.19}
\]

并使用 **同一个** \(c_{\rm clear},c_{\rm triv},C_h\)。此结论来自固定几何数据、线性化和基点唯一性，不来自任意局部选取一个不同截面。

旧环境未保留原文所写的 \(N/M\) 的字面定义及任何整数值。本次恢复使用 (593R.17) 的新命名，不声称这些整数与旧稿相同，也不把旧局部数值集合套到新截面。

## 7. 局部规范高度、潜在好约化与统一支持

固定一个非零 \(\mathbb Q_p\)-值全局 idèle 类角色 \(\chi\)，以及 Poincaré 双扩张的 purely mixed curvature/splitting 数据。先在 \(d=1\) 选择与甲板作用相容的数据：对有限 \(\mu_3\) 作用取平均即可，且 Galois 置换生成元保证下降。之后沿同一扭曲传递到所有 \(d\)。

赋予 \(\mathscr N_{h,d}\) 按原点刚性化得到的规范 adelic 度量。对 \(q\ne p\)，定义归一化局部值

\[
 \lambda_{q,h,d}(x)=\frac1{C_h}\,
       v_{\mathscr N_{h,d},q}(s_{h,d}(x)).
\tag{593R.20}
\]

对 \(p\) 处，同样定义

\[
 \lambda_{p,h,d}(x)=\frac1{C_h}
       \log_{\mathscr N_{h,d},p}(s_{h,d}(x)).
\tag{593R.21}
\]

全部值按 (593R.18) 在基点为零。全局高度也除以同一个 \(C_h\)，所以 (593R.16) 不多出缩放因子。

Besser–Müller–Srinivasan，*p-adic adelic metrics and Quadratic Chabauty I*，Lemma 7.1，精确适用于这样的 **曲线拉回已平凡、已有真实无零截面、按基点刚性化** 的线丛：\(\lambda_q\) 的值域有限，且曲线在 \(q\) 潜在好约化时该函数恒为零。

原文：<https://arxiv.org/pdf/2112.03873>，Lemma 7.1 及其前面的 (7.1)–(7.4)。本稿没有把只在 \(\operatorname{Pic}^0\) 中与 \(\phi_d^*\eta_h\) 相等、却未平凡的 \(\mathcal L_{h,d}\) 直接代入该引理。

规范 \(X_4\) 是六水平与 \(p\) 水平的模曲线，在 \(q\nmid6p\) 好约化。每个 \(X_d\) 在有限三次扩张后与它同构。因此

\[
 X_d\text{ 在每个 }q\notin\{2,3,p\}\text{ 潜在好约化},
\]
\[
 \boxed{\lambda_{q,h,d}\equiv0\qquad(q\notin\{2,3,p\}).}
\tag{593R.22}
\]

这包括所有新增 \(q\mid D\)：原曲线可在这些地方坏约化，但扭曲后的曲线具有潜在好约化，正是引理所需的假设。

对实际偶分支，\(d\in\mathbb Q_2^{\times3}\cap\mathbb Q_3^{\times3}\)。在这两个局部域中 \(b\mapsto\sqrt[3]d\,b\) 识别全部曲线、商、极化、线丛和基点。按 (593R.18) 的唯一截面归一和规范度量的函子性，局部函数的值域正好等于 \(d=1\) 的值域：

\[
 \Lambda_{q,h}:=\lambda_{q,h,1}(X_1(\mathbb Q_q))
 =\lambda_{q,h,d}(X_d(\mathbb Q_q)),\qquad q=2,3.
\tag{593R.23}
\]

这两个集合有限。定义本次实际截面对应的新有限集合

\[
 \Omega_h=\{u_2\chi_2(2)+u_3\chi_3(3):
                   u_2\in\Lambda_{2,h},\ u_3\in\Lambda_{3,h}\}.
\tag{593R.24}
\]

没有擅自决定 \(\chi_q(q)\) 与 \(\log_pq\) 的正负 convention；统一保留同一个已选 \(\chi\)。也没有声称计算出了这两个有限集合的数值。\(\Omega_h\) 与 \(d\) 无关，但依赖本次固定的实际截面和归一。

## 8. 对有理点的准确高度关系

假设所选同一个真实 \(A_d\) 满足

\[
 \operatorname{rank}A_d(\mathbb Q)=\dim A_d,
 \qquad\log_p:A_d(\mathbb Q)\otimes\mathbb Q_p
       \xrightarrow{\sim}\operatorname{Lie}(A_d)(\mathbb Q_p).
\tag{593R.25}
\]

则其全局对称高度在有理点上通过实际对数写成一个二次型 \(Q_{h,d}\)。把 (593R.16) 的高度按全局—局部分解，并用 (593R.22)–(593R.24)，对所有 \(x\in X_d(\mathbb Q)\) 得

\[
 Q_{h,d}(\log_pj_d(x))
 +2h_Y(P_d(x),\eta_h)-\lambda_{p,h,d}(x)
 \in\Omega_h.
\tag{593R.26}
\]

这是一条关于真实商的公式，不把整个 \(J_d\) 的秩判据误套到商。此时没有假定 \(h_Y(P,\eta_h)\) 已经通过 \(\log P\) 因子化。

其准确剩余条件是

\[
 \log_pP=0\quad\Longrightarrow\quad h_Y(P,\eta_h)=0
 \quad(P\in J_Y(\mathbb Q)\otimes\mathbb Q_p).
\tag{593R.27}
\]

在此条件下，固定线性高度项在有理对数的像上给线性泛函；延拓到 Lie 空间记为 \(\ell_h\)，于是

\[
 \rho_{h,d}(x)=Q_{h,d}(\log_pj_d(x))
 +2\ell_h(\log_pP_d(x))-\lambda_{p,h,d}(x)
\tag{593R.28}
\]

是实际 \(p\) 进局部解析/Vologodsky 高度函数，且有理点满足 \(\rho_{h,d}(x)\in\Omega_h\)。R596 独立证明 (593R.27) 并给一个规范的 \(\ell_h\) 构造，故本篇几何不是循环依赖于该结论。

## 9. 指定 \(c_{0,d}\) 盘上的形状和限制

在 \(c_{0,d}\) 附近，细参数是 \(b\)，甲板为 \(b\mapsto\zeta b\)。R575 的正 holomorphic CM 型在全部系数域嵌入上给 \(\delta_\zeta^*\omega=\zeta\omega\)。因此每个实际商微分及其基点积分形如

\[
 j_d^*\omega_i=f_i(b^3)\,db,\qquad
 L_i(b)=b\,U_i(b^3).
\tag{593R.29}
\]

二次型项于是为 \(b^2U(b^3)\)。固定底曲线的对数线性项通过 \(v=db^3\)；所选甲板不变 curvature、真实截面和刚性化使规范局部高度项也甲板不变，并在 \(a'=\sqrt[3]d\,b\) 的识别下等于 \(d=1\) 的同一函数。因此 (593R.28) 保持

\[
 \rho_{h,d}(b)=b^2U(b^3)+V(db^3)
\tag{593R.30}
\]

的形状。这里没有认为全局二次型在所有扩域点上都等于一个 \(K_p\)-双线性延拓的高度；(593R.29)–(593R.30) 只用有理点高度得到的二次型及真实局部积分。

若 \(h\ne0\)，\(q_d^*\mathcal L_{h,d}\) 的 NS 类非零，而 Picard 修正不改变它。这里直接采用 BMS Theorem 7.2 的证明，而不把其某个商版本备注不加核对地套到含 Y 修正项的本线丛：对全纯积分的二次型与线性项，\(\partial d\) 的值属于 \(F^1\otimes F^1\)；另一方面，非零 NS 类的 Chern 类为非零 \((1,1)\) 类，不属于 \(F^2H^2\)，其相应曲率部分不能落在 \(F^1\otimes F^1\) 中。Picard 零次修正不改变 Chern 类，Abel 映射在 \(H^1\) 上的同构也不消去这一差异。因此局部高度项不能被全纯二次与线性项抵消，(593R.28) 非恒定。这个论证不计算其最低系数或 \(\Omega_h\) 的距离，也不自动排除某个有理点。

特别，单个 primitive Abel 积分的首项为单位，不能直接当作 (593R.30) 的首项为单位；它还含 \(Q_{h,d}\)、\(\ell_h\) 及局部度量。一般 \(d\) 的秩/对数条件 (593R.25) 也必须由同一个实际家族另外证明。

## 10. 恢复范围和可接续结果

本稿完整恢复：实际甲板不变极化与加权迹；固定 \(\eta_h\) 的 Q 下降及 \(d\) 无关性；真正拉回平凡的线丛和基点截面；跨 \(d\) 统一的新清分母因子；所有新增坏素数处的零局部项；以及实际偶分支独立于 \(d\) 的有限高度目标集合。

R596 用该固定 \(\eta_h\) 完成 (593R.27)。R598/R600 在明确解析范围内给 (593R.25)。原候选在 \(X_1\) 的 \(c_1\) 与 \(X_d\) 的 \(c_0\) 之间是否可运输商值，必须按 R597 的真实图式处理，不能由六水平标记变化直接断言。

旧 \(N/M\) 的字面数值及旧数值 \(\Omega_h\) 未恢复。本稿已提供一套重新选定、统一且完整可复核的规范；后续任何实际数值高度计算须明确使用本稿的 \(c_{\rm clear},c_{\rm triv},C_h,s_{h,d}\)，不得混用旧未验证数据。
