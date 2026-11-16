# R923：原两端正规阶中的 272 个目标正常函数与一次共用分母

日期：2026-11-16。状态：本文是以 R917 **实际完成**的两端八阶正规 order 为输入的准确后继证明、精度合同和执行来源。新的目标函数端点坐标尚未计算；本文不把端点 order 帧改称九范数或五个目标线丛的完成标定。

本篇接 [R917 两端实际认证](R917-certified-original-two-endpoint-normal-orders-and-frames.md)、[R917 原证明](R917-original-two-endpoint-normal-orders-and-source-contract.md)、[R912 端点格](R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md) 与 [R885 单左伴随行](R885-original-one-row-adjugate-and-whole-Artin-fibre-norms.md)。新入口先用原 273 阶 primitive 表与已经算出的判别式，求目标 $w$ 的八个正规坐标；再用已成全局伴随行和一个共同八阶分母恢复全部 272 个正常函数。原 272 阶矩阵、273 个插值节点、全部伴随行多项式、两端正规化均不重算。

## 1. 固定真实两端，而不是原普通 $z=0$ 纤维

保持原对应

$$
p=\pi_s:C_7\to Y,\qquad q=\pi_t:C_7\to Y,
\qquad U=q^*z,\qquad V=q^*w.
\tag{923.1}
$$

原 $P(U)=0$、$V=K(U)/P_U(U)$ 及其特征零含义仍来自 R873 的原 2058 列单位解；R882 的同素点 17 列没有换一个对应。原原理想的 Hecke 方向仍是 $\operatorname{Nm}_{\pi_t}(\pi_s^*I)$，当前 $p$ 上的有限代数经原 canonical dual7 输运，分子和分母两个 determinant 都保留。

实际地方固定

$$
k=\mathbf F_{1000000753},\qquad
\zeta=549966761,\qquad s=99932770.
\tag{923.2}
$$

对 $\epsilon=0,1$，令

$$
\rho_0=z-z(P_0),\qquad
\rho_1=\iota^*\rho_0=z-2\beta_{72}-z(P_0),
\quad R_\epsilon=k[[\rho_\epsilon]],\quad F_\epsilon=k((\rho_\epsilon)).
\tag{923.3}
$$

R914 的完整几何 $\iota$ 和原 273 项 jets 已被 R917 消费。这里不把 $\rho_1$ 换成 $z-z(P_1)$，也不把 R885 的普通源纤维 $z=0$ 的目标值移作端点值。

R917 真实 run `43904492746`，source `64228da6693769dcf70fb8bcaec4a72ad0faa445`，配置 SHA

`1d1e0b7e6cd16ad4108e0674c2a9cca73ff1eadf35902269f1673a2199b5fb4b`

给出的两端数据如下。所有数字是原完成证书的字段，不是本篇新运算。

| 量 | $P_0$ | $P_1$ |
|---|---:|---:|
| $v_\rho(\widetilde P_8)$ | 0 | 0 |
| 原 primitive 指数 $h$ | 0 | 0 |
| primitive 精度 | 273 | 273 |
| primitive 判别式阶 | 6 | 6 |
| 正规化累计 index | 1 | 1 |
| 最终 order 精度 | 271 | 271 |
| 最终判别式阶 | 4 | 4 |

特别地，本次 $\Theta=U$。记原幂基 $e=(1,U,\ldots,U^7)$，实际正规基 $b$ 和已成变换为

$$
b=eB_\epsilon,
\qquad b=\left(\frac{v_\epsilon(U)}{\rho_\epsilon},1,U,\ldots,U^6\right),
\qquad [U^7]v_\epsilon=1.
\tag{923.4}
$$

$B_\epsilon$、$B_\epsilon^{-1}$ 的全部 64 项已经保存为有限 Laurent 多项式。此次 $B_\epsilon^{-1}$ 的所有非零项的最低阶均非负；第一行只在原第 7 列有 $\rho_\epsilon$，其余行由常数和标准坐标组成。这是所选真实基的来源属性，不能任意另选有利基后沿用原帧。

## 2. 为什么目标正常函数在这个正规阶中整

原 R805/R806 正常环及基严格为

$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,
\qquad \beta_0=1,\quad \beta_1=w,
\qquad \varepsilon=(0,1^{144},2^{127}).
\tag{923.5}
$$

它是原 $\tau\ne0$ 图的正规整环，并有限于 $K[z]$。$\tau,\sigma$ 是原无基点铅笔；因而 $z=\sigma/\tau$ 的有限图就是该 $\tau$ 图。原正常函数、原 good reduction 与同一辅助地方均不更换。

在 R917 的真实八维 generic 代数

$$
E_\epsilon=F_\epsilon[U]/(m_\epsilon(U)),
\qquad m_\epsilon=\widetilde P/\widetilde P_8,
\tag{923.6}
$$

$U$ 已为整元素。原 $q$ 映射在每个正规分支上延拓；若目标落在 $\tau=0$，无基点条件迫 $U=\sigma/\tau$ 有极，与整性矛盾。因此所有目标分支落在原 $\tau$ 图。等价地，(923.5) 中每个 $\beta_i$ 整于 $k[U]$；拉回后整于 $R_\epsilon$，所以

$$
\gamma_i=q^*\beta_i\in\mathcal O_\epsilon,
\qquad V=\gamma_1\in\mathcal O_\epsilon,
\tag{923.7}
$$

其中 $\mathcal O_\epsilon$ 是 R917 已认证的完整正规 order。

这个论证使用原正常环和原对应的整个好约化，不是仅凭 $P(U)$ 首一就把任意 $K/P_U$ 商认作整函数。执行时仍须将下文所有可能的低阶分子逐项验证为零；来源理论和实际整除证书分别保存。特纤维的两个长度 3 部分全部保留，不能在约化商上检查整性。

## 3. 有整性时，共同分母只损一次判别式阶

**引理 923.1。** 设 $R=k[[\rho]]$，$A$ 是一个给定基的有限自由整 $R$-代数，秩为 $r$。$a,b_j\in A$，乘 $a$ 的列矩阵为 $M_a$，$\Delta_a=\det M_a\ne0$，$d=v_\rho\Delta_a$。若原系数、乘法表和输入均已知模 $\rho^N$，且 $d<N$，则

$$
n_j=\operatorname{adj}(M_a)[b_j],\qquad
[a^{-1}b_j]=\frac{n_j}{\Delta_a}.
\tag{923.8}
$$

若商整，则 $n_j$ 的每个坐标都可被 $\rho^d$ 整除。先将分子和分母同时除 $\rho^d$，再求剩余单位的逆，得到商的全部坐标模

$$
\rho^{N-d}.
\tag{923.9}
$$

对一个固定 $a$，所有右端共用同一个 $M_a$、伴随矩阵、$\Delta_a$ 和单位逆；不存在每列重新求逆的必要。

证明。伴随恒等式给出 (923.8)。所有 determinant/adjugate 系数都是原矩阵条目的整多项式，故已知模 $\rho^N$。如果商整，准确恒等式 $n_j=\Delta_a[a^{-1}b_j]$ 给坐标整除。将已知分子和分母除 $\rho^d$ 后均有精度 $N-d$；单位求逆和整乘法不再损精度。没有先构造一个只剩 $N-2d$ 精度的任意 Laurent 逆。

执行上，检查全部坐标的第 $0,\ldots,d-1$ 系数为零即足以验证这里的整除；因 $d<N$，这些都是确切已知系数。若实际 determinant 在已知范围内没有非零项，只能记录 $v_\rho\Delta_a\ge N$ 并返回 NeedPrecision。若出现应为零的低阶非零系数，则应停为来源/相容性失败，不能自动丢掉该项或宣称目标函数无定义。

更一般地，若只有商的真实极阶上界 $k_0\ge0$，则同一算法先保 $\rho^{k_0}a^{-1}b$ 的整性；未经额外精度输入，商的保守绝对精度为 $N-d-k_0$。下文的 272 个正常函数使用的是已证明的 $k_0=0$；未来 $\Phi$、连接或指定分式函数不能默认沿用这一界。

## 4. 先求原 $V=K/P_U$：实际可用精度 267

固定一个端点，省略 $\epsilon$。R917 已保存全部共同清分母列、$a=\widetilde P_8$ 的单位逆和首一多项式 $m$。令

$$
d(U)=m'(U),\qquad
b(U)=\widetilde K(U)/a,
\qquad V=d(U)^{-1}b(U).
\tag{923.10}
$$

这里没有重求 $a^{-1}$；直接引用 R917 `deflated_leading_unit_inverse`，并保原共同清分母恒等式

$$
P_U(U)V=K(U)
\quad\Longleftrightarrow\quad
\widetilde P_U(U)V=\widetilde K(U).
\tag{923.11}
$$

**先在旧 primitive 表中计算。** 该表有精度 273；用它构造 $M_d^{(e)}$、$b$ 的幂基坐标。由于 $m$ 为次数 8 的首一多项式，

$$
\det M_d^{(e)}=\operatorname{Nm}_{E/F}(m'(U))
=(-1)^{8\cdot7/2}\operatorname{Disc}(m)
=\operatorname{Disc}(m).
\tag{923.12}
$$

右端是 R917 **primitive** 判别式原 series，阶为 6；不能误用正规基的判别式阶 4。它已在同一次 R917 计算中完成，消费者不新增一份相同判别式计算。只需新伴随矩阵并核两侧乘回到这个旧判别式。

定义

$$
n=B^{-1}\operatorname{adj}(M_d^{(e)})[b]_e.
\tag{923.13}
$$

乘 $B^{-1}$ 必须在整除之前。由 (923.4) 的实际非负阶性质，(923.13) 仍有 273 阶精度。由 (923.7)，

$$
n=\operatorname{Disc}(m)[V]_b\in\rho^6 R^8.
\tag{923.14}
$$

逐项核八个坐标的前六项为零，然后除 $\rho^6$、乘旧判别式单位部分的真逆，得到

$$
\boxed{\ [V]_b\pmod{\rho^{267}}\ }.
\tag{923.15}
$$

本式没有重新执行 R917 的 idealizer，也没有将正规表精度 271 反过来充作 primitive 表精度 273。$B^{-1}$ 是旧准确有限 Laurent 表，不重新解矩阵；它的真实非负阶是此次 267 界中的必要条件。

必须保存并核：两侧伴随乘回、全部 48 个低阶消失、原未首一式 (923.11) 在完整八维正规表中的乘回。后者在实际共有精度 267 上成立；不能因原式在精度 273 给出来源便给新商虚报 273 项。

## 5. 原单左伴随行给全部目标正常坐标

保持 [R860](../notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md) 的原列输入约定

$$
W(z)=M_w,\qquad
\chi(z,T)=\det(TI_{272}-W(z)),\qquad
r(z,T)=e_0^t\operatorname{adj}(TI_{272}-W(z)).
\tag{923.16}
$$

原准确函数恒等式是

$$
r_i(z,w)=r_0(z,w)\beta_i,\qquad r_0(z,w)\ne0,
\qquad \deg_{z,T}r_i\le271+\varepsilon_i.
\tag{923.17}
$$

R885 已在同一辅助地方完整计算全部多项式行，不仅有 $z=0$ 的值。其实际 row-level $k$ 给

$$
r_i(z,T)=\sum_{k=0}^{271} b_{k,i}(z)T^{271-k},
\qquad \deg_z b_{k,i}\le k+\varepsilon_i.
\tag{923.18}
$$

原 $b_{k,i}$ 的系数、全部原行索引和 weighted support 必须直接读取；不再作 273 节点插值、Berkowitz 大矩阵或全伴随矩阵。

取共同精度 $N_*=267$。在 R917 正规表截到 $N_*$ 后，$U,V$ 均为整坐标，故以 (923.18) 作 Horner 求值

$$
R_i=r_i(U,V)\in\mathcal O/\rho^{N_*},\qquad0\le i\le271
\tag{923.19}
$$

不因多项式的 273 次总次数反复损精度。此前每次 Laurent 除法的实际损失已由 (923.15) 统一记入。

令 $M_0$ 是在同一正规基中乘 $R_0$ 的完整八阶矩阵，

$$
\Delta_0=\det M_0,\qquad d_0=v_\rho\Delta_0.
\tag{923.20}
$$

$r_0$ 不是预先假定的端点单位。原特征零非零性来自 R860；同辅助地方的整个原 $z=0$ 对应代数中，[R885 实际完整纤维证书](R885-certified-original-whole-Artin-target-coordinates-and-nine-reference-norms.md) 已证它为单位。原有限平坦对应的每个 generic 分量都支配源曲线并经过该完整源纤维，故这也排除了本次模函数在某个 generic 分量上恒等为零。端点仍可有正的 $d_0$，实际值必须新算。

若实际看到 $d_0<N_*$，由 (923.7)、(923.17) 与引理 923.1，所有

$$
n_i=\operatorname{adj}(M_0)[R_i]_b
\tag{923.21}
$$

均被 $\rho^{d_0}$ 整除。全部 272 个右端只需这一次共同八阶伴随矩阵和 determinant 单位逆。逐坐标核低阶、同时整除，得到

$$
\boxed{\ [\gamma_i]_b=[q^*\beta_i]_b
\pmod{\rho^{267-d_0}},\qquad0\le i\le271.\ }
\tag{923.22}
$$

若 $d_0$ 在 267 项内没有显露，则保已成 $U,V,R_i$ 和实际下界，返回 NeedPrecision。本文不预填 $d_0$，不声称旧 273 项必然足以完成所有目标坐标，也不把零截断用于 Picard inactive 或函数零判。

### 5.1 必须保留的原完整方程

新的成功终点需包含：

$$
\chi(U,V)=0,\qquad \gamma_0=1,\qquad\gamma_1=V,
\qquad \sum_{i=0}^{271}\gamma_iW_{ij}(U)=V\gamma_j
\quad(0\le j\le271).
\tag{923.23}
$$

最后是全部 272 条、每条全部八个 series 坐标、在实际共同精度上的乘回。另保 $R_0\gamma_i=R_i$ 和 (923.11)。这些核验来自原四个 $W$ 多项式系数块，不重新构造原 $W$。

该有限域核验不产生新的特征零坐标系数。特征零函数身份仍是原 (923.10)、(923.17) 的 source-bound 准确表达式；数组字段明确标成辅助地方的模 $\rho^N$ 值。

## 6. 可执行的小矩阵和可续接阶段

矩阵均至多 $8\times8$；大的部分只是在这些八维整代数中评价已成 272 个多项式。可以用无除法递推计算 determinant/adjugate，或在本次 $\ell>16$ 下使用 $1,\ldots,8$ 的明确常数单位；不允许对尚未为单位的 series pivot 作除法。

固定阶段顺序如下。

1. `source-audit`：原 P/K、两端 order/precision、旧幂基与逆、全部 row-level 和同地方 $W$；保持每个 source 的原 result/tag/SHA。
2. 每端 `primitive-derivative-adjugate`：只新 $M_d$ 和伴随；旧 primitive discriminant 作为原输入，双侧乘回。
3. 每端 `target-w-normal-coordinates`：原 $B^{-1}$ 运输、前六项消失、真实 267 阶商和原式乘回。
4. 每端 `integral-target-powers`：实际 $U$ 与 $V$ 的已需幂/乘法矩阵，完整八维，按需保存；不建立 272 维新乘法表。
5. 每端、每 16 个正常列的完整 Horner 阶段：按原 row-level 区块原子保存；预算终止后只续未成区块。
6. 每端 `shared-r0-adjugate`：真实 determinant 阶、共同伴随与单位逆；不足时返回 NeedPrecision 并保所有已成 Horner 块。
7. 每 16 列新正常坐标及低阶整除；完整四个 $W$ 系数块乘回，生成端点证书。
8. 总证书仅在两个端点实际完成时为 `complete=true`；分别保每端实际精度和未完成原因。

所有阶段保存原子 plain-spec 引用。预算、输出目录和运输路线不进数学身份；固定算法、分块、源码 SHA、原输入身份和 requested precision 进身份。旧已成 stage 不经改 tag 移入新输出；它们始终是外部原来源。

若最终要求 $T$ 项而已见 $d_0$，这一算法的统一原 jet 精度需求为至少 $T+6+d_0$；若仅知 $d_0\ge267$，只能给相应下界，不能填一个猜测的充分精度。增加输入精度必须来自新的真实 R914/R917 producer；旧 273 项文件及其原身份不改写。

## 7. 原帧、两个范数方向及尚未给出的目标理想

R923 不改变正规基。原 R917 determinant 是

$$
\det B_\epsilon=-\rho_\epsilon^{-1},\qquad
t_\epsilon=c_\epsilon\rho_\epsilon+\cdots,
\quad (c_0,c_1)=(354813668,645187085).
\tag{923.24}
$$

原 $t_\epsilon$ 首项和完整八维特纤维直接引用旧 frame/special-fibre stage；不重新选符号或把相同基改成一个归一到 1 的 determinant 帧。新 $V,\gamma_i$ 的坐标均相对于这同一个基。

保持

$$
\nu=82\tau\,dq_Y/q_Y,\qquad \iota^*\nu=\nu.
\tag{923.25}
$$

本次只给原正常函数的目标评价。$\nu/d\rho$、靶到源微分的比例、某个连接分母的逆，都不是本次旗标。原 dual7 精确表达式、scalar7/diamond/$-3$ 相位及两个 determinant 的输运同时保留。

未来如给出真实 $\Phi$ 或目标生成元

$$
f=\frac{\sum_i a_i(U)\gamma_i}{\sum_i b_i(U)\gamma_i},
\tag{923.26}
$$

本次坐标可直接装配其完整八维分子、分母；分母仍须按真实 determinant、极阶与精度求商。不能由于 $\gamma_i$ 整就假定任意 $f$ 整，更不能仅把其模 $\rho$ 值代入 line-bundle 的标记格。

R912/R907 的目标仍需 $\operatorname{Nm}(q^*\Phi)\det U$、参考 $M_0$ 和两端原帧。R903/R907 五个目标输入在本 scope 中继续为 `null`；目标理想格、九范数端点标定、Hecke Picard 活跃支持和高度的完成旗标全部为 false。

## 8. 新消费者的精确原输入，不取旧大矩阵逆

### 8.1 R917 真原件

R917 原 FINAL：`p41-original-two-endpoint-normal-orders-certificate.json`，13981 B，SHA

`cf539a58a7ab8212bb0e0d56c9621c2c6916ca25c2cbc3b50ce7be3890c15349`。

原 manifest：32468 B、184 项、SHA

`d8bac1cf2d29e385afd7222d87805506732e2dfecc440980b187e6112bb2af2b`。

每端只按完整证书引用选：共同清分母 17 jets、primitive order、`order-000-discriminant`、`order-001-complete-table`、最终 discriminant、idealizer 小核、完整特纤维、primitive/t 帧，以及该端证书。原 173 个 stage 的其他部分不要求重算或重新装载。需要精确 P/K 与 dual7 的原 DAG 时，从 R917 已续存的 40 件 carrier 按原 inventory 抽出原 R873 DAG/单位解及最小原 metadata；不重标签、不访问新的替代 producer。

### 8.2 R885 全局多项式，绝不是 $z=0$ 的目标数组

原 polynomial producer：run `43842694142`，source

`0210f90f1ac7d2c89e948cae0cdc5f64f775dc07`，

core SHA `dd4ef0d445e7c90caf568d7aa87951166d6730cc86da0a44be11b664742d3035`，配置

`f4a4973d93b328bd76f93d41b668e70a0817c1510012b9824370a18858ed634a`。

原 manifest SHA 为 `51dff64343665bf629603f42e43cc21ecc10aaf17912df5cc6f20bb7b8973154`。所需数学原件严格是：

| 原件 | 字节 | SHA256 |
|---|---:|---|
| `R885-adjugate-full-polynomial-adjugate-certificate.json.gz` | 17474 | `b49becb6df241cdb0e075c810f7e25865255de1389d62475c3f6db082517a106` |
| `R885-adjugate-polynomial-characteristic-relation.json.gz` | 194378 | `fb8dbdd0a97eef2cd10a08f61afc55865203267c157d7e64c78c9a311a73486b` |
| `R885-adjugate-row-level-000.json.gz` | 2169 | `b6f92cbcda282bd05872c97541e3c04d26dfe2b2bc683e1db22b2df8f14145d1` |
| `R885-adjugate-row-level-271.json.gz` | 331029 | `9b5196f171e4b3eee5401e85e7d75b2496444db9f1230f3460c6249c7967a51f` |

中间全部 270 个 level 按已成 index 的 `adjugate_row_T_terms` 逐 spec 读取。第 $k$ 件的 `row_level=k`、`shape=[k+3,272]`、`coefficient_rows_ascending_z` 及 `T_power=271-k` 逐项绑定。不需要原 273 个 charpoly 节点或新的多项式重构。

### 8.3 原 $W$ 与同地方身份

原 `R827-original-W-g-h-reductions.json.gz` 为 763994 B、SHA

`5bcbadf437c2ac91431771b6d9818b99436008e9a5db4caa185dfac8aca5f841`。

它的 `W_coefficients_mod_prime` 是原四块 $[4][272][272]$，`original_rational_denominators_all_units=true`。来源仍是原 R827，不能将其预算结束的 producer 改称完整成功。这里只取实际已成 W、place audit 及原 metadata；无 Krylov 逆、无 $M_g$、无 $\Gamma$、无新 272 列求解。

若为了固定模函数的 generic 非零证额外引用 R885 whole-Artin 已成的 $r_0$ 单位小证书，只作为原来源保留；其 $z=0$ 的 $\gamma_i$ 数组不进入两端坐标计算。

## 9. 实际成功旗标和诚实的精度停止

后继消费者可给以下新的正面量：两个端点原 $V$ 的完整八维值、全部 272 个 $q^*\beta_i$ 的八维 series、各自实际绝对精度、真正原方程乘回，以及对 R917 原基/参数/dual7 帧的逐字引用。这些是下一端点理想和 determinant 消费者需要的真实函数叶。

R917 已有的正规 order、判别式、幂零特纤维和原帧不重新计为本次新数学。若输入 273 项对某个新分母不足，只冻结已完成部分并输出该分母实际阶下界、缺失的原输入精度及未完成列；不得以零模值删掉因子、声明 inactive，或用特征零函数存在性替代尚未求出的系数。

本篇证明不把任意剩余类提升成原特征零准确系数；也不把原 272 正常函数端点叶、九范数相对坐标、完整 $\operatorname{Nm}(\Phi)\det U$、原 Picard/高度之间的区别消去。
