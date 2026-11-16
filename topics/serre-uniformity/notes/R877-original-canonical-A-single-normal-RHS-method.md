# R877 — 原 canonical A 的单个 S5 正规坐标右端

日期：2026-11-16。状态：**执行方法与来源契约；本篇不登记尚未运行的新数值。** 本消费者只取得原 $A/\tau^5$ 在一个已固定剩余域中的完整正规坐标，以及同一向量的特征零单位解表达式。已成的 $B/\tau^5$、S5 矩阵及其模逆均直接消费。它是原全局 $y=A/B$ 与后继五个原极理想的必要输入，不是五个 $\mathscr L_j$ 的128/144维 RR 核已完成的声明。

## 1. 固定原函数，而非选择另一个关系

保持 [GP](R839-original-global-addition-polar-ideals-and-eta-DAG.md) 的原 $f=f_4$、$L=\mathbf Q(b,\zeta)$ 和原关系 $y=A/B$。原积分坐标是 $B_{\mathrm{fld}}=\lambda b$、$s=1+2\zeta$；关系分母截面 $B$ 与 $B_{\mathrm{fld}}$ 是不同对象。原 U.1 的2420阶单位选行解、自由列1186等于1及其余27个自由坐标等于0，唯一确定

$$
\mathbf a=(a_0,\ldots,a_{1233}),\qquad
\mathbf c\in L^{1214},\qquad
\mathbf b=Z\mathbf c,\qquad
A=\sum_i a_iF_i^{(5)},\quad B=\sum_i b_iF_i^{(5)}.
\tag{877.1}
$$

R849 的真实完成 DAG 保存了这条准确定义及全部原叶的文件身份；它没有展开这2420个准确系数。R827 的真实
`R827-canonical-B-original-V5-expansion.json.gz`
虽以 B 命名，同时保存了 (877.1) 的 A、C、B 在原分支0上的完整约化。其来源审计以原单位子式、原完整核维数28及同一自由坐标，证明该模向量确是原特征零解的约化。这里不重新求 Schur 核，不把任意模核向量提升为特征零关系。

本消费者逐项核对 R827 的原 R787 身份、chart、Z、自由坐标与 R849 DAG 的原 A 系数节点。R849 的全局 F 矩阵叶也须与 R827 的 B-normal 阶段保存的1234个原 F 文件规格逐项相同。这样，新右端与已成 B 使用同一个准确全局关系。

## 2. 只增加一个右端

原正规基记为 $\beta_0,\ldots,\beta_{271}$，次数为

$$
(\epsilon_i)=(0,1^{144},2^{127}).
$$

原 S5 的1234列是 $z^j\beta_i$，按 $i$ 外、$j$ 内排列，其中 $0\le j\le5-\epsilon_i$。记 $S$ 为这组截面原前69个 $v$ 系数、每阶20个实圆分坐标的矩阵：

$$
S\in\mathbf Z^{1380\times1234},\qquad
F_{69}\in\mathbf Z^{1380\times1234},\qquad
r_A=F_{69}\mathbf a.
\tag{877.2}
$$

$F_{69}$ 的列从原
`R787-real-power5-row-0000.json.gz` 至 `...-1233.json.gz`
的 `integer_t_coefficients` 直接截取原69阶。这里保留常数块；不能把 B 的常数块为零推广给 A。

两套原列均已含 $82^{10}=13744803133596058624$ 的同一整数尺度。因此 (877.2) 直接使用保存的整数，不另乘或除 $82^{10}$，不插回曾经清除的共同 content，也不再作 $\lambda$ 换基。R827 已经将原 A 系数准确约化到

$$
\ell=1000000753,\qquad \text{原分支 }0,\qquad
\zeta\mapsto549966761,\quad s\mapsto99932770.
\tag{877.3}
$$

原 $b$、$B_{\mathrm{fld}}$ 的根及 $\lambda$ 单位性从同一原 place-audit 逐字段绑定。

R842 已真实保存 $S\bmod\ell$ 的全部1380行。R827 已真实保存一个1234行集合 $I$、单位子式和双边乘回通过的

$$
U=(S_I\bmod\ell)^{-1}.
$$

新数学仅为

$$
\bar r_A=(F_{69}\bmod\ell)\bar{\mathbf a},
\qquad
\bar q_A=U(\bar r_A)_I,
\qquad
(S\bmod\ell)\bar q_A\stackrel{!}{=}\bar r_A
\quad\text{全部1380行}.
\tag{877.4}
$$

不重新约化旧 S5 列，不重新选择 I，不重新计算其行列式或逆，不重新转换 B。前式按64个原 F 列分块保存；每块同时保留新形成的 F69 模列和部分 A 右端，供同一旧源的后继 Galois 右端直接复用。

## 3. 准确含义和全部加权支撑

S5 是原 $V_5$ 的完整基，且 $A\in V_5$。因此存在唯一准确向量 $q_A\in L^{1234}$ 使 $Sq_A=F_{69}\mathbf a$。由原 $\ell$ 单位子式，

$$
q_A=S_I^{-1}(F_{69}\mathbf a)_I
\tag{877.5}
$$

的全部分母在所选原地方为单位；这是与 R849 中原全局 A 相同的准确向量。R849 的准确 DAG 使用的选行集合可以不同：完整基中表达的唯一性严格保证两种单位解定义相同，不要求伪造相同的子式文件。

把 (877.5) 按原 S5 行映射还原，得到

$$
\frac A{\tau^5}
 =\sum_{i=0}^{271}v_{A,i}(z)\beta_i,\qquad
\deg v_{A,i}\le5-\epsilon_i.
\tag{877.6}
$$

输出同时保存：

1. `exact_unit_solve_expression`：准确的 (877.5)、原 A 节点、原 F/S5 叶、所选行集合及单位子式来源；
2. `S5_coordinates_mod_prime`：实际1234个约化坐标；
3. `vector_coefficients_mod_prime`：按 $z$ 次数外、正规基指标内排列的 $6\times272$ 数组；
4. 全1380行回代与全部加权支撑断言。

没有准确系数有理重构。模数组的身份明确是 (877.5) 的约化；它本身不冒称已经展开的特征零坐标。

## 4. 与已成 B 及原 y 的接缝

原 B-normal 阶段已有同一结构的 $v_B(z)$，其源尺度、自由坐标和全部1380行证书保持原字节。新阶段仅建立

$$
y=\frac{\sum_i v_{A,i}(z)\beta_i}
        {\sum_i v_{B,i}(z)\beta_i}
\tag{877.7}
$$

与 R849 原 `original_y` 节点的同一性。原 B 非零已由 U.1 的自由坐标及 Z 的单射证明；本分支保存的 B-normal 向量也须实际非零。

(877.7) 没有断言 B 在任意所选纤维可逆。后继有限纤维求值必须使用同一原 W/Krylov 数据，实际检验各分母的单位性，并保留其准确域求值定义。若需微分，可以按 [R872](R872-original-point-jets-and-bounded-two-weight-RR-kernels.md) 已有的原 $g,h$、循环纤维规则形成所需有限 RHS；本消费者不要求等待尚未完成的全部特征零 $\Gamma$ 或 $M_g$ CRT。

五个原 $g_j$ 及真 Galois 范数需要同一 $\zeta$ 地方上七个原 $b$ 分支的完整函数约化。当前单分支 A 不能替代它们。后继可消费 R824 的七个真实 canonical 分支及本次已成 F69 模块，复用原 S5 矩阵/逆，按需形成其余 A/B 右端；必须沿原全局 Galois 作用，不仅共轭常数。此次不计算这些后继右端，不把它们加入成功标志。

## 5. 最小原来源与运输

原数学来源只有四组。运输来源和数学生产来源分别记载，运输不改旧 tag。

| 原来源 | 直接消费的数学数据 | 明确保留的身份 |
|---|---|---|
| R827，run43734420663 | canonical A/C/B 模展开、已成 B-normal、原 p753 S5 逆、place-audit | 原 source400edecf、core d9cf7739、完整原 manifest2609de21、实际失败 checkpoint |
| R842，run43776927742 | 已成1380×1234 S5 模矩阵 | 原 sourceccc94341、core6fe0a0d3、矩阵1c1647ea、成功证书 |
| R787，run43683912711 | B-normal 所列1234个原整数 F 行、chart、Z、selection | 原 sourceeab5e58b、core93d3d72b、manifest613f436b、真实 exit1 |
| R849，run43790410670 | 原全局 U.1/函数/极理想准确 DAG 及小元数据 | 原 source39119159、core544241ac、DAG529822ba、成功证书 |

纯 IO intake 先取原 R827 B-normal，再从其 `source_original_V5_rows` 选出 R787 的恰当1234个文件；每项必须与原 R787 manifest 的 bytes/SHA 一致。它不重新计算旧 F、原 phase 变换、S5 或 B。所选源以一日 tar 保留；原失败来源只要求真实已完成阶段及其原 tag，不能要求其不存在的成功 FINAL。

首次 intake 已查询四个原 artifact 的实际可用性。若运输过期，后继只准改为已核同字节的活跃 carrier；数学 source_commit、core、manifest、file SHA 与 tag 均不改变。请求中不得预填未取得的 B-normal/S5-inverse SHA。

## 6. 核心与断点

核心为 `scripts/R877_original_canonical_A_normal_input.py`，命令行：

~~~text
python scripts/R877_original_canonical_A_normal_input.py \
  --config expanded-job.json --out output --budget-minutes 300
~~~

数学 RESULT 为 `R877-original-canonical-A-normal-input`；
FINAL 为 `p41-original-canonical-A-normal-input-certificate.json`。

输出全部在根目录 `R877-*.json.gz`。完整阶段依次为来源审计、64列 F69/部分右端、完整右端、正规 A、原 y 分式输入、阶段清单。工作 current 单独标 `complete=false`。每个完整阶段绑定新核心、方法/证明、原四组 selected-file fingerprint 及全部实际输入规格。

完整阶段原子写入后续算直接读取。已结束的 false FINAL 是历史终点，不能用它的旧清单约束后来继续增长的 current。成功 FINAL 的全部引用必须存在并逐 SHA 核对。预算或异常保留实际已完成阶段，真实 core receipt 报具体错误，不能把部分右端当作完整 A 坐标。

## 7. 本次唯一成功出口与后继界限

成功必须同时给出：

- `canonical_A_normal_input_certified=true`；
- `all1380_original_short_coordinates_verified=true`；
- `original_global_y_normal_fraction_input_certified=true`；
- 恰一个新右端及全部原身份/尺度/支撑；
- 旧矩阵、旧逆、旧 B 未重算。

下列标志仍为 false：准确正规系数已重构、七分支已完成、五个原 $\mathscr L_j$ 的128/144维 RR 已算、原连接/刚性化/高度已算。后继才把原 y 和真正七分支接到已成 W、[原 GP 极理想 DAG](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)、[原点模及有界核](R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)，形成实际五个原类的截面矩阵。

原证明固定为 GP SHA256
`520bfbd521cadfeff2b519c864217a56258a991a07039ee33e923db7e9be4e0a`
及 R872 SHA256
`bd6ee11af3fbbce8db2767bc327265176992bb3be15395018df6612ab4e2dae2`。
