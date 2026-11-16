# R492：同一 C 新叶盒对固定 target 与准确 cut 场的只读消费

作者：geometry agent（AI）。日期：2026-11-16。

可信度：**已证明（限下述条件命题）**。新源码已写成；本结论没有实际 accepted450、R489 重算、叶宽改善、单元计算或完整闭域证书。没有本地导入、AST、编译、测试、数值执行，也没有新增 request/run。

本结论补 R489 的一个具体来源断口：其新旧三 jet 交集已经有独立结果格式，但原 R400 target 与 R416 准确 cut patch 仍从原定义中的叶盒求值。新组件将交集作为**同一个准确函数的求值包围**传入两者，原 checkpoint、准确定义、节点、共有 B、材料映射和十参数保持原身份。它不重新命名旧 accepted 场，不把一个盒中点变成新的准确系数。

对应源码：[`geometry_20261116_same_C_refined_leaf_target_and_cut.py`](../computations/geometry_20261116_same_C_refined_leaf_target_and_cut.py)。运行合同见[完整接口](../notes/2026-11-16-same-C-refined-leaf-target-and-cut-interface.md)。

## 492.1 已有来源与实际切点

使用以下原来源及其原条件，不重写它们的数学论证。

| 来源 | 本结论实际使用的接口 | 仍由原来源负责的内容 |
|---|---|---|
| [R400](R400-current-continuous-ten-frozen450-and-complete-prefix-metric-binding.md) | `AccurateTenTarget` 的完整 tree、pieces、supports、十系数及 `closed_range` | 真450/完整338+112/两mean/FD/final 来源，准确与数值长度分列，所有分片和控制支撑 |
| [R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md) | `AccurateCutModel`、`new_exact_field`、`AccurateCutBundle.evaluate` | 原准确 cut DAG、三阶公共图、原675完整六 jet 和两反射片 |
| [R489](R489-same-C-complete-head-recomputation-and-cut-enclosure-intersection.md) | 实际同 job 原 f12f 重算与原1c39完整 cut；`semantic_bindings`、`intersect` | 全1440/six、所有原根族、同一原 cut、完整原输入相等、原绝对钟、原进程所有权与 partial |
| 原72c factory | `Tree.evaluate`、`Box`、`piece_range` | 对同一原表达式的向外区间运算，未分离或选取原 C 关系 |
| 原675 active engine | `ExactFiniteField` 与完整 active 六 jet | 原 Hermite/FFT/B/注册/材料表达式、全部节点及所有角模态 |

新入口先让原 R416 loader 真正返回其完整绑定的 `AccurateCutBundle`。该原加载若未完成，新组件保未付；它不借新叶盒补造一个 accepted 场或越过原来源责任。加载后为 target 和六 jet 视图分别建立自己的 cache，不替换旧模块全局或定义字节。

这是当前原 R400/R416 家族的明确来源登记。R441、R451、R464 生成的同类源码和 R483 的另一种区间表达尚未登记；相同类名或相同公式并不自动满足本入口的来源条件。

## 492.2 同一个 C 家族与叶交集

固定原输入所许可的全部根序列集合 $\Omega$。对每个 $\omega\in\Omega$，原连续模型为 $C_\omega$，在同一个真实 binary64 cut $R$ 定义

$$
e_0(\omega)=E_{C_\omega}(R),\qquad
e_1(\omega)=E'_{C_\omega}(R),\qquad
e_2(\omega)=E''_{C_\omega}(R).
$$

假设原定义实际绑定的完整 cut reader 给出闭区间 $I_i$，同一现场 R489 重算与原 reader 给出 $J_i$，且二者对所有原根序列满足

$$
\forall\omega\in\Omega:\quad e_i(\omega)\in I_i\cap J_i.
$$

令 $K_i=I_i\cap J_i$。因此每个真实同 C 叶仍属于 $K_i$。这只是在同一量词下相交两个外包围，既不缩小 $\Omega$，也不声称矩形 $K_0\times K_1\times K_2$ 中每个点对应同一个实际 $\omega$。

源码不只读取一个 `complete=true`。`RefinedLeafProvider` 实际重新读并绑定：R489 输入/结果、原205 launch 与同一 deadline、旧及新 f12f 结果和 input binding、两份原1c39完整 cut、独立交集文件。它重新调用 R489 的完整语义比较和准确有理交集，并要求交集文件与结果中已登记的原值一致。

此外，旧 f12f 结果与旧 cut receipt 必须分别等于**当前准确定义** `continuous_tail.actual_result` 和 `actual_complete_cut_twojet_readout`；完整原 input binding 也须相同。原定义 `actual_enclosure_leaves` 与当前已加载 target 的三盒须确实等于该旧完整 reader 的三盒。这样不能用别处相似 fingerprint、仅三数相等或另一份新定义冒充来源桥。

空交集是该消费未完成，不能被解释为真实 C 反证。原或新 cut 未完整时，同样不给出新叶。全域 whole-query 的完成标志分别如实记录，但不增加一个与三叶有效性无关的 whole-query 工作精度门。

## 492.3 固定准确 DAG 的区间求值

设 $\mathcal D$ 为当前定义的完整有向无环表达式，叶为原三语义叶，其他节点只含原有理常量、加、乘、负、除和平方根。十个系数 $p$ 使用当前真正冻结的十个准确 dyadic 数；原 raw word、负零、CP 和节点身份仍保存在原对象与 binding 中。数学上把负零解释为零不改变其原字词记录。

对每个许可 $\omega$，在原必要分母非零和平方根定义域已给出的区域，区间算术逐节点归纳得到

$$
\mathcal D(e_0(\omega),e_1(\omega),e_2(\omega);p)
\ \in\ \mathcal D^{\Box}(K_0,K_1,K_2;p).
$$

归纳使用每一个原节点，不能以三叶盒中点替代语义叶。原完整 DAG、derived roots、pieces、supports 和十参数均不变；代码只在独立 view 中保存新 `values`、`length` 与独立 cache。保存定义的 `actual_enclosure_leaves` 不被覆写，也不将旧 definition receipt 解释为新 JSON 的 receipt。

新的平方根工作精度是显式资源。即使 $K_i\subseteq I_i$，改变有限工作精度后也不自动声称每个中间输出区间严格嵌入旧区间；相关性损失和舍入宽度都可能继续存在。本结论证明的是包围有效及准确函数不变，不承诺变窄、误差下降或终止。

原完整长度 $L^*(\omega)$ 的求值也读取新叶。数值长度 $L_{\rm num}$ 保持原接受字段的字词。二者不因新求值而被认同。

## 492.4 原完整 prefix target 的真实消费

`RefinedTenTarget.closed_range` 直接调用原 R400 `AccurateTenTarget.closed_range` 的方法正文；其 `self` 是新独立求值状态。对原闭数值区间 $[s_0,s_1]\subseteq[0,L_{\rm num}]$，原公共坐标仍为

$$
u=s_{\rm num}/L_{\rm num},\qquad s^*=L^*u.
$$

原方法遍历每个准确分片，并对每个可能归属求

$$
t=\frac{s^*-a_j}{w_j}
$$

与该分片原闭 `local_interval` 的交集。所有未被严格排除的候选均计算原三 jet 并 hull；全部十项控制与原支撑/闭端点分支保留。源码没有使用数值 midpoint piece lookup，也没有只对原首个候选作替换。

因此原数值 $s$ 图中径向目标系数仍为

$$
g_{ss}=\left(\frac{L^*}{L_{\rm num}}\right)^2,
$$

角向目标仍来自同一个 $a^*(L^*u;p)$ 和同一个材料映射的导数。新叶改变这两个准确函数的外包围，不改变函数定义或物理/材料坐标。原 `closed_range` 返回的完整候选记录仍保留，并额外登记真实 R489 交集成员身份。

这项 target 消费已在新 API 中实际实现；没有把原四 Loewner 布尔值当作新的误差数值，没有执行完整闭域 DFS，也没有推断请求的固定参数全域合法性。

## 492.5 同一准确 cut 系数与三阶图

R416 的追加 DAG 在原完整 target DAG 后定义

$$
k=\frac{L^*}{L_{\rm num}},\quad
v_c=kv,\quad b_c=k^2b,\quad c_c=k^3q,
$$

以及原场所需的三个系数

$$
m_1=-\frac{\sqrt{e_0}}{k},\qquad
m_2=\frac{e_0}{k^2},\qquad
m_3=\frac{e_1}{2k\sqrt{e_0}}.
$$

这里 $v,b,q$ 是原准确 DAG 的 canonical cut roots，不是数值 profile 的名义导数。公共图仍是

$$
\gamma(z)=R+v_cz+\frac{b_c}{2}z^2+\frac{c_c}{6}z^3.
$$

三阶项保留，不能用仅满足几何二 jet 的坐标去声称径向目标系数的二阶连接已经完成。

新组件调用原 `AccurateCutModel`，并核其原树及追加树节点、各根索引、cut 和数值长度与当前原 R416 model 完全相同。因而上述七个量是**同样的实函数**，只是重新得到闭包围。新 `closed_chart_window` 的区间宽度可能不同；它是同一 $\gamma$ 的一个新已覆盖窗口，不是替换准确图的系数或更改 patch 宽度。

正长度、正 $e_0$、有向 cut 图和原分片宽度等条件仍按原真实区间运算履责。无法给出时保未付，不把它加入原 BVP 接受函数，也不由浮点非零冒严格可除。

## 492.6 完整 active 场六 jet 实际读取新系数

令 $P,P_s,P_{ss}$ 是原完整注册后的 prefix 端点数据，含原全部338物理行、两mean及材料来源。原 R416 cut targets 为

$$
T_0=P,\qquad T_1=m_1P_s,\qquad T_2=m_2P_{ss}-m_3P_s.
$$

新对象实际把新 $m_i$ 包围交给原 `new_exact_field` 和原675 `Jet2` 计算，完整保留其位置、两一阶与三二阶导数。没有在 Fourier 系数处截掉角频，也没有把新系数转成浮点字词。

原 `source_bundle` 是同一个原七元组；它包含的完整 prefix nodes、native radial/FFT 节点、共有 B、注册与材料 core 仍原样。新对象与旧对象具有同一个 piece 列表、径向节点、core/density/rho 和注册来源。原 prefix 及不触及 patch 的 tail/collar 公式因此不改变；cut patch 的准确系数函数也由上一节保持不变。所以对每个同一 $\omega$，原 R416 场与新 view 代表相同的准确场 $F_\omega$，而非一次新的 BVP 或一次更换参数的几何构造。

下反射由原675完整 `evaluate` 保留；帽、marker、cuff 与共有 B 没有被新定义。新 API 没有重新扫帽或新增 seam 定理。若原完整同场/接缝条件尚未付，本组件也不会用来源身份代替它们。

`RefinedCutBundle.evaluate` 可对任一原真实 active piece 的完整闭径向/物理角区间及明确反射 side 返回六 jet。它只是单元求值接口。即使调用者给出若干单元，也不能把它们等同于全部 pair universe、全域 DFS 或连续 $t$ 证书。

## 492.7 必须保留的消费边界

| 量或责任 | 本组件是否真正读取新三叶 | 完成范围 |
|---|---:|---|
| 原完整 accurate target DAG、$L^*$、每个 prefix 候选三 jet | 是 | 新 view 与原完整 `closed_range` 正文 |
| cut 的 $k,v_c,b_c,c_c,m_1,m_2,m_3$ | 是 | 同一追加 DAG；系数不取中点 |
| active cut patch 的完整六 jet | 是 | 原675/416公式实际调用新乘子 |
| 原 prefix/native/B 的定义字词、材料映射和十参数 | 不变 | 不重求、不覆写、不产生新接受 |
| 任意 tail 半径上的 $E_C(r)$ whole/live query | 否 | 没有安装新 R426 provider，没有自动继承 R489 新 query 结果 |
| 原 R418/R459 全闭域误差与 R422/R435 reach、R425 held | 否 | 没有执行或登记这些外层来源 |
| R441/R451/R464 的生成来源族 | 否 | 本次仅原 R400/R416；后继须真实登记其完整来源 |
| 原求解残差到全域 relative-metric floor | 否 | 仍无传递界；不把 solver 容差换单位解释 |

特别地，target 与 cut patch 变紧不能被写成“整条 metric 链已变紧”。原 tail 的 $E_C(r)$ 包围若仍固定，其误差范围依旧保留。反之，本组件也不要求一个未来全域误差成功才允许原 BVP 继续。

## 492.8 资源、未返与准确身份

新 provider 重新绑定 R489 所用实际 original205 launcher/deadline，保持同一 `namespace_created_unix_seconds+18900`，不重开科学钟；2700 秒读回责任仍属实际外层调用者。API 接受原 caller 的 `budget_check`，每次读取、target/field 计算边界调用。独立 CLI 另有包含原加载的显式工作预算，使用协作检查；真正硬 TERM/KILL 所有权应由原 owned caller 负责，本源不虚称自身有独立绝对杀钟。

CLI 的有限 cell plan 是明确调用地址，不是新增数值筛选门。每次在处理前检查预算；未完成时保 current cell 原行、全部未访索引、已返回完整原单元记录及错误。未返回值不填零。所有原/新源及 raw 留在同一 Actions 临时目录，不删除、不上传 artifact。

必要结果只允许一个不超过90000字节的 JSON 正文；超过时退出70，登记完整原件身份及未读 scope，保 raw，不分包、编码或提高限额。该 transport 部分状态不构成几何反证。源码没有实际运行，不能预先说输出必在限额内或任何精度/性能条件已成功。

## 492.9 结论

在原 R416 真场已加载、原准确定义与 R489 的旧 C/cut 内容身份一致、两份完整 reader 对同一全部根族有效的条件下，新组件提供一个直接可调用的 target/cut 六 jet 求值 view。它对每个原许可 C 成员保留同一个目标、同一个场及全部原固定参数，只改变合法外包围的计算来源。

本结论不预填实际 R489 结果，不派发217，不更改209/212/214，也不增设 BVP、metric、reach 或整题完成的科学接受门。尚未接的 tail query 与外层全域消费者已逐项明确，后续按真实需要独立接入。
