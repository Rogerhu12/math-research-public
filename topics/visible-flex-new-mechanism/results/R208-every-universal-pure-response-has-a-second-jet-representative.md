# R208：全部 universal pure 第四响应都有二阶 profile jet 表示

日期：2026-11-15。**完整纸面证明，继承一项已发表的准确代表上界。** 本稿没有新原式编译、profile 评价、正规化、旧列消元或研究计算。它把既有第三控制空间的覆盖范围，与两个通用的同右锚代数引理接起来。

来源：[R69](R69-pure-fourth-effective-bridge-gamma-and-finite-moment-targets.md)、[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)、[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md)、[R82](R82-exact-pure-P1-endpoint-and-genuine-bridge.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md)、[R179](R179-universal-independence-of-fixed-color-remainder-words.md)。

## 1. 结论及其不包含的断言

沿 R80 记完整实际第三可调空间为

$$
W=W_{71}+V_3+W_1,
\qquad
W_{71}=\operatorname{span}\{[\Phi_i,\Phi_j]:i<j\}.
$$

对 $\tau\in W$，只在本稿取其对角三次函数

$$
\tau_\Delta(q)=\tau(q;q,q).
$$

R83/R105 的完整响应空间为

$$
R=\operatorname{span}\{\mathcal B_E(\tau):E\in E_8,\ \tau\in W\},
\qquad \pi V=V_{-4}.
$$

**定理。** 每个 $F\in\pi R$ 都存在一个准确的 universal 表示，只含

$$
x,\quad q,\quad q',\quad q'',\quad
\text{它们的有限乘积与同一右端锚的有限嵌套原函数}.
\tag{1}
$$

即不需要任何 $q'''$ 或更高 profile jet。所有式子对任意光滑右 collar 零输入、整个查询区间成立，左尾照常保留。

进一步，在 R178/R179 的单色规范余词中，$\pi R$ 只占用 jet 阶至多二的行。因此，若一个已知真实 $F\in\pi U$ 的准确规范余词有非零的 jet 阶至少三的行，则

$$
\boxed{F\notin\pi R.}                                      \tag{2}
$$

这里要求该余词来自 sound 原式转换并满足 R179 的规范语法；不把任意不完备正规化中的某个高 jet 临时项当作 (2)。

本稿不证明全部 $\pi U$ 都有 (1)，不支付局部势、完整动态第四密度的高 jet 系数，也不将结论推广到完整 mixed 响应。它没有计算 $\dim W_\Delta$ 或 $\dim\pi R$。

## 2. 已发表的 151 列为什么覆盖整个 $W_\Delta$

本节使用 R82 同一个公开实际的第三空间部分，**不是只用该实际的 pure 第四目标成功身份**。

来源身份为：

- run `43632772378`，lane `closed_c1_endpoint`，source `31a276f6f4b2361d10bea9a46fea307a951bb639`。
- 脚本 `literature_closed_c1_endpoint.py`，SHA256 `b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1`。
- 原 main `closed-C1-endpoint.json`：13911 B，SHA256 `622cd662e60eed74e58f59bb52981aed6a209eeaf4664bc7304a5e3826b6da86`。
- 原 receipt：24387 B，SHA256 `923d2b509b0680f4ab705c2e2764542bd4f155897db1cc8aa963d3179f9d8f46`。

实际报告的 `reachable_space` 为

| 原对角第三列来源 | 列数 |
|---|---:|
| 全部 R71 二次算子交换子 | 28 |
| R77 面积及四种三次速度的全部几何系数，去已改写零项/重复项 | 56 |
| R79 两个闭 C1 相容函数的全部几何系数，去已改写零项/重复项 | 67 |
| 合计 | 151 |

这里的“全部”可逐项接回定义，而非某个方便的可达子集：

1. R77 把 $V_3$ 定义并证明为面积系数和四个三次速度系数的全部状态值跨度。有限 Laurent/log 几何展开的全部 profile 系数张成同一空间。
2. R79 式 (5) 给 $W_1=\operatorname{span}\{\mathcal H(S),\mathcal K(S)\}$，其中

$$
\mathcal H=\partial_h(h^2R_h),\qquad
\mathcal K=(R+hR_h)_\omega-2(-h^2R_h)_k.
$$

R79 又证明全部几何系数的跨度与这些状态值跨度相同。
3. 该旧脚本的 `profile_labels` 对 `area,cubic` 和 `h_shape_obstruction,contact_closure` 的每一个几何键取原系数；后一对正是上述 $\mathcal H,\mathcal K$。对角投影与几何微分、系数展开及积分线性交换。
4. `independent_labels` 只删 sound 改写后为零或相同的代表，没有按采样秩裁掉不同余项。其后 `raw_columns=commutators+c3+closed` 的次序恰为表中次序。

因此这 151 个原函数的真实跨度就是 $W_\Delta$。完整外槽与内槽没有由这一论证被混同：只有取了对角后才使用这张表。

该次已完成的准确有理消元报告代表秩 18，保留列为

$$
0,1,2,3,4,5,6,7,8,9,10,11,12,14,18,20,21,24.
\tag{3}
$$

它们全部位于最初 28 个 R71 列内。这个事实足以给一个**正向包含**，无须认定代表独立就是函数独立：设 $w_j$ 是这 151 个 sound 词代表，$\mathrm{ev}(w_j)$ 是相应原函数。既有消元已给

$$
\operatorname{span}\{w_j:0\le j<151\}
=\operatorname{span}\{w_j:j\text{ 属于 (3)}\}.
$$

对这一线性恒等施加真实函数解释 $\mathrm{ev}$，得到

$$
\boxed{
W_\Delta=(W_{71})_\Delta.
}                                                            \tag{4}
$$

反向包含原本就由 $W_{71}\subset W$ 成立。这里不需要旧 normalizer 完备，也没有从旧报告推出真实维数恰为 18；只继承其已完成的 sound 上界和保留列均在 R71 中这一事实。没有重跑这 151 列、它们的 pure 响应或任何旧原式身份。

固定不同 scalar 端口所带的 $T_{\rm end}$ 不属于本节要覆盖的可调空间 W；(4) 不将任意开桥端点势擅自删掉。

## 3. 两个 profile 代数与线性最高 jet 的准确消去

令

$$
p=q',\qquad r=q'',\qquad t=q''',\qquad
I(F)(x)=\int_{r_*}^{x}F(y)\,dy,\qquad J=-I.
$$

所有输入及原函数在同一右 collar 为零。

定义 $\mathscr A_2$ 为由 $x,q,p,r$ 出发，经有限加、乘及 I 生成的代数。每个原函数 integrand 有正 profile 次数。定义其子代数

$$
\mathscr B=\mathbb R[x,q,p,\{I(F):F\in\mathscr A_2\}],
\tag{5}
$$

即 $\mathscr B$ 的**原函数外局部因子**不需要 r，原函数内部仍允许 r 及嵌套尾。这不是声称其函数值与 r 无关。

对 $F\in\mathscr A_2$，把外局部 r 看作一个多项式变量，把已有原函数节点暂作系数。真实 x 导数可唯一按语法写为

$$
DF=t\,\partial_r^{\rm out}F+D_0F,
\qquad D_0F\in\mathscr A_2.
\tag{6}
$$

原因是 $DI(H)=H$，不会对 H 再多求一次导数。特别

$$
D\mathscr B\subset\mathscr A_2,
\qquad D^2\mathscr B\subset\mathscr A_2+t\mathscr A_2.
\tag{7}
$$

**线性最高 jet 引理。** 对任意 $F\in\mathscr A_2$，有

$$
\boxed{I(tF)\in\mathscr A_2.}                              \tag{8}
$$

证明：对外局部 r 取多项式原函数 G，使 $\partial_r^{\rm out}G=F$，积分常数取零。G 在右 collar 为零，故由 (6)

$$
I(tF)=G-I(D_0G).
$$

两项均在 $\mathscr A_2$。这一步保留真实原函数常数；它没有将 $I(t^2F)$ 也宣布可如此降阶。

## 4. 任意 E8 对角第三交换子都属于 $\mathscr B$

按 R69，任意 $E\in E_8$ 的双线性算子为

$$
\Phi_E(a,b)=A_0ab+\frac{A_1}{2}(ab'+a'b)+A_2a'b'
+B_0J(a''b'')+B_1J(xa''b'')
+B_2J(x^2a''b''+2a'b').
\tag{9}
$$

所有 A、B 系数是 x 的多项式。令

$$
X_E(q)=\Phi_E(q,q),\qquad
S_E=A_1q+2A_2p,\qquad C_E=B_0+xB_1+x^2B_2.
$$

由 (9)，$X_E\in\mathscr B$，其真实导数具有

$$
X_E'=S_Er-C_Er^2+U_E,\qquad U_E\in\mathscr B,
\tag{10}
$$

$$
X_E''=(S_E-2C_Er)t+V_E,\qquad V_E\in\mathscr A_2.
\tag{11}
$$

考虑两个算子 E、F 的有序复合 $\Phi_E(q,X_F)$。局部导数项中，可能含外局部 r 的部分为

$$
\frac{S_E}{2}(S_Fr-C_Fr^2).
$$

尾项中仅 (11) 的 t 部分需要处理。对每个 $j=0,1,2$，同右锚分部积分给

$$
J(x^jS_Fr t)=-\frac{x^jS_F r^2}{2}
+\text{一个 }I(\mathscr A_2)\text{ 项},
$$

$$
J(-2x^jC_Fr^2t)=\frac{2x^jC_Fr^3}{3}
+\text{一个 }I(\mathscr A_2)\text{ 项}.
$$

系数 $D(x^jS_F)$ 只含 q、p、r，不产生 t，故所余 integrand 确在 $\mathscr A_2$。式 (9) 的其余尾项本就属于 $I(\mathscr A_2)\subset\mathscr B$。

于是整个有序复合的全部外局部 r 贡献，模 $\mathscr B$ 恰为

$$
\boxed{
\frac12S_ES_F r
-\frac12(S_EC_F+C_ES_F)r^2
+\frac23C_EC_F r^3.
}                                                            \tag{12}
$$

它关于 E、F 完全对称。因此

$$
\boxed{
\Phi_E(q,\Phi_F(q,q))-\Phi_F(q,\Phi_E(q,q))\in\mathscr B.
}                                                            \tag{13}
$$

这是全部 28 个 R71 对角第三交换子的同一个原式证明，没有逐列计算。结合 (4)，所有 $\tau_\Delta$，$\tau\in W$，均有一个 $\mathscr B$ 表示。

## 5. 这种第三函数经任意纯第四响应仍不产生三阶 jet

设 $\tau_\Delta\in\mathscr B$，令 $X_E=\Phi_E(q,q)$。纯响应准确为

$$
\pi\mathcal B_E(\tau)
=\frac{D\tau_\Delta(q)[X_E(q)]
-2\Phi_E(q,\tau_\Delta(q))}{8}.
\tag{14}
$$

第一项是真正固定右锚的 Fréchet 导数。它只依赖 $\tau_\Delta$ 的真实三次函数；不同完整第三提升若对角相同，(14) 相同。

先看第二项。由 (7)，$\tau_\Delta'$ 在 $\mathscr A_2$，$\tau_\Delta''$ 在 $\mathscr A_2+t\mathscr A_2$。式 (9) 的局部部分因而在 $\mathscr A_2$，尾中所有 t 都线性出现，可由 (8) 消去。所以

$$
\Phi_E(q,\tau_\Delta)\in\mathscr A_2.
\tag{15}
$$

再看第一项。变分规则为

$$
\delta q=X_E\in\mathscr B,\qquad
\delta p=X_E'\in\mathscr A_2,\qquad
\delta r=X_E''\in\mathscr A_2+t\mathscr A_2,
\qquad \delta I(F)=I(\delta F).
$$

按原函数嵌套深度归纳：对 $F\in\mathscr A_2$，其变分在 $\mathscr A_2+t\mathscr A_2$；原函数内部的线性 t 由 (8) 支付。因此 $\delta I(F)\in\mathscr A_2$。而 $\tau_\Delta$ 的外局部因子只含 q、p，它的外变分也在 $\mathscr A_2$，故

$$
D\tau_\Delta(q)[X_E(q)]\in\mathscr A_2.
\tag{16}
$$

(14)–(16) 证明每个原 pure 响应都在 $\mathscr A_2$，实线性组合给第 1 节的定理。证明从未假设几何 h、k、omega 常值；使用的是已经覆盖全部真实 W 的 universal 响应接口。

## 6. 高 jet 规范余词为何不能被 $\pi R$ 隐藏

本节只使用 pure 的单色语法。把一个 $\mathscr A_2$ 表达式送入 R178 的有声余词转换：

- shuffle 不改变字母的 jet 阶；
- 对一个最高 jet 阶至多二、该最高 jet 只出现一次的单色局部单项分部积分时，先把该阶降低一阶，微分其余因子只会恢复到原最高阶，不会产生三阶 jet；
- 移动迭代词上的导数只取其首字母，不再微分这个字母；
- 零 profile 次数的坐标因子处理也不提高 profile jet 阶。

因此存在一个全部 jet 阶至多二的规范余词表示。由 R179 的 universal 单射性，它是相应真实函数的唯一规范坐标。

故任何具有非零三阶或更高 jet 规范坐标的真实 pure 算子，都不可能等于 $\pi R$ 中的元素，得到 (2)。这是一条函数非成员判别，仍须先支付该对象属于 $\pi U$ 以及其规范转换的准确性。

它也说明后续完整动态 pure 消费不能以“模掉 R 便可去高 jet”为默认步骤：R 自身没有这些规范坐标。若高 jet 真能消去，必须是原式内部身份，或额外空间的已证明作用；不能靠遗漏它们得到一个假的成员关系。

## 7. 保留边界

本稿没有将 $W_\Delta=(W_{71})_\Delta$ 升成完整 $W=W_{71}$；外槽信息仍可有非零核。也没有把 pure 二阶 jet 表示当作其真实维数、正性、实际负成本或第四 ruling 的结论。

已发单根 $\bar A_{hh}$ 的权 −6 化简是一个完整成本系数自身降到二阶 jet 的例子；它不是本稿全响应定理的前提，也不能据此推全部 $\pi U$ 已降阶。各权的完整局部势与动态项仍按原式保留，由各自准确证明或公共消费者处理；一项具体整权的成员证书不替代其他权的这种支付。
