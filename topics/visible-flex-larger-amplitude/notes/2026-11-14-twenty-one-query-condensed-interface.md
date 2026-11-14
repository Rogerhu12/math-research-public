# 独立21-query 入口：从实际66只增加原 left-RMS466

分类：独立数值实现与输入/输出契约；尚未执行的新计算。  
作者：ChatGPT（amplitude，AI 辅助）。  
日期：2026-11-14。

## 1. 依据与唯一模型变化

实际66的最近拒绝为 $\alpha=1/8$：所有原节点、中点及20个已建模完整角网格
均有效，实际目标下降 `0.05522054625365769`，原完整双 RMS 只在
left-RMS466 失效，最小 $\beta^2=-0.6545364759053149$、物理角0。
原 trial 随后在 $1/16$ 接受优化 warm。详细事实见
[实际66结论](2026-11-14-actual-request66-twenty-query-nearest-left466.md)。

本独立入口仅增加该 left-RMS466 的原2048个物理角模型行，保留此前全部
20个查询。更远 $1/4$ 的原 midpoint484 失效不是最近档的失败；本入口
不新增 midpoint484，也不声称增加一组模型行即可保证更大步长。

所有原标量函数、core/field/tail维数、完整 residual、原权重、原真实域、
实际 merit、17档回溯和完整新 warm FD 保持原源。模型阻尼仍为270，
与另行使用共同 actual64 父场的阻尼27比较分支明确分开。

## 2. 新文件及被冻结的父源

| 新独立文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_one_query_domain_operator.py` | 32226 | `0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65` |
| `geometry_20261114_twenty_one_query_condensed_warm.py` | 41712 | `b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2` |
| `geometry_20261114_twenty_one_query_condensed_response.py` | 2619 | `d1da3a179bc05d346406961b81fc233e6edd098810bd6834537bc50d33901301` |
| `geometry_20261114_twenty_one_query_collocation_observer_warm.py` | 16728 | `b99c6e4d40abaf426c189b241b718b8847562e92a7cdb90b6fdb31d6505587de` |

原20-query四源一字不改。新 domain 明确绑定父 domain
`16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1`；
新 warm 递归保留原20的 `SOURCE_NAMES/FROZEN`，并钉住父 warm 源
`9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee`。
R270 凝聚库仍为 `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`，
原局部 QP 仍为 `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`，
原完整 QR、A/J/边界和 C 投影源均保持。

文件旁的四份 `.py.diff` 是相对冻结20源的完整差异。静态回执
`twenty-one-source-static-check.json` 记录7个核心计算函数和12个 observer
函数 AST 逐项相同；原 midpoint 导数赋值 AST 也相同。此处只有源码、AST、
整数索引及 SHA 检查，没有导入科学模块或本地执行数值。

## 3. Typed query 行序、完整支持与零列

行序严格为下列14个 left-RMS 查询，然后7个原 collocation midpoint；
每组按原物理角 index0–2047 排列：

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482)
MID  = (473,475,477,480,481,482,485)
```

left 分数固定 `0.17267316464601146`；midpoint 分数为0.5。
重复 interval 的左右类型各自有 `kind/query_index/fraction`，不能因同一
interval 而合并两组模型行。

| 对象 | 本独立入口 |
|---|---|
| 完整未知量 | 原236036个缩放坐标 |
| 完整不等式行数 | `21×2048 = 43008` |
| 唯一捕获 cell | 15个；只在原唯一完整 A/J 构造中截取 |
| 实际 query 端点 | nodes466–483、485、486，共20节点 |
| 实际 B block column 并集 | 20个338维物理节点加3个 control，共6763列 |
| R270 声明的连续局部布局 | nodes466–486加3个 control，共7101列 |
| 显式零 B 列 | node484的338列 |
| 原 C 候选可修正支持 | nodes471–482加3个 control，共4059列 |

新 left466 使用原 endpoint466 和467，因此捕获和局部支持确实向左扩展一
节点，不能声称支持未变。原 node484 仍只是连续布局所需的零 B 列；没有
新增 query484 或为了这个零块追加 endpoint484 Jacobian 捕获。原完整 A/H
包含每个节点，所以 node484 仍为完整 H 未知量，保留其全部原耦合。

`block_column_union_indices` 保实际6763列，`local_indices` 保声明7101列。
每个原 block 的 `local_columns` 都依据声明布局重新映射。原 full B/B转置
的全坐标 scatter 不改；local转置先置完整7101维零向量再 scatter，故484
返回结构性零列；local正向不读取不存在的484 block。模型 SHA 和 manifest
继续同时绑定完整布局、实际 block 并集、零列和两套节点列表，不能只用一
个旧计数替代。

## 4. 新 left466 的原完整导数链

令 $t$ 为原 left-RMS 分数，$h$ 为该原 cell 长度，查询使用同一原
CubicHermiteSpline：

$$
Y(t)=h_{00}(t)Y_L+h\,h_{10}(t)f_L+
     h_{01}(t)Y_R+h\,h_{11}(t)f_R.
$$

其方向包含完整端点状态、原端点 RHS Jacobian 和共享全局 control：

$$
\delta Y(t)=h_{00}\delta Y_L+h\,h_{10}\delta f_L+
             h_{01}\delta Y_R+h\,h_{11}\delta f_R,
\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

查询处 $a$ 和原返回 $a'$ 的显式 control 链保持。原七个中点都仍直接
读取 `state.middle[j]` / `problem.mid[j]`，保持
$\frac12(\delta Y_L+\delta Y_R)-\frac h8(\delta f_R-\delta f_L)$，
没有把 midpoint 换成 left-RMS 或节点平均。新 source 只通过新
`LEFT_INTERVALS` 调用原已冻结的全部 left 导数代码，不另写一个近似导数。

R262/B 作用于 $z=S\delta q$；编译行仍只除一次原 $S$。共享节点和全部
control 转置仍累加。原 `verify` 真正针对当前 B 的原2048角、完整 Hermite
complex 链及伴随；新入口没有增加科学接受门，也不把有限角检查扩写为
连续角或全站点证书。

## 5. 原 C 与完整 R270 路径

原 C 候选仅修正固定支持 $S_C=$ nodes471–482加3个 control。新的完整 B
仍作用于全236036维；局部 C 投影的右侧 offset 必须保留
$c+B_{\bar S_C}z_{0,\bar S_C}$。outside节点包含
466、467、468、469、470、483、484、485、486；484在 B 中为零，其余不
得省略。局部 C 子问题若不可行，原径向备份仍可用，不增加一项新科学门。

完整 R270 支线使用7101维局部 H-QP，保完整原 $g=A^Tb$ 和外部条件最优
响应，未把 C 的固定支持误用于完整 H。唯一恢复后原完整 A/AT/B、实际
gdot、全部43008线性 slack 和原实际试步照旧。最后全向量 radial 也会改
outside部分，因此没有“最终外部 raw 不变”的身份声称。普通浮点 R267
后验继续只是诊断，不代替原全域、原 BVP 或最终 native 门。

## 6. 真父 pair、完整 producer 与 own-schema 续接

首次父 pair 明确是实际66：

| 字段 | 值 |
|---|---|
| 原 science run/source | `43651436427` / `cf3a8ff94fae3f7009f85047c69db3aeb8eb320a` |
| parent schema | `exact-constraint-twenty-query-condensed-complete-H-warm-v1` |
| 原 compressed warm | 4817773 B，`80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6` |
| 原 JSON status | 1955482 B，`04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4` |

公开 status 可以是 `.json.gz`，恢复时透明解压并核原 JSON 字节 SHA，
不重新序列化。压缩 warm 的原字节直接复制。旧父 status 绑定的完整
`optimization_warm` 子树必须保留；source、constant core/control、标量
profile及mesh原校验保持。

新 schema 为 `exact-constraint-twenty-one-query-condensed-complete-H-warm-v1`。
只有首次父使用硬锁 actual66 pair；未来该新 schema 的实际完成 warm/status
可按明确双 SHA 一次调用继续，仍保其实际整个 producer，不修改旧父树。
没有把 pending/prepared 冒成新接受场。新 observer 有独立执行源 SHA，
数学 producer 始终是新 warm 源，不冒称原20源产生新21行。

## 7. 完整 CLI 与预算

由公开 Actions 使用同一真实来源路径执行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_one_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT66/warm-001.json.gz" \
  --expected-resume-sha 80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6 \
  --parent-status "$VISIBLE_PARENT66/driver-status.json" \
  --expected-parent-status-sha 04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4 \
  --out "$VISIBLE_OUT/twenty-one-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

`T112_TRUE_ZERO_ANCHOR` 为原已完成 `e788a28d…` 的完整零 H 响应，工作流
仍使用公开 `public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`。
原准备场、accepted96来源和T112配置的身份恢复与实际66完全相同。

新的真实 warm 通过原完整实际下降/域流程保存后，再运行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_one_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

该 FD 在实际新 warm 上重做原完整方向/两阶 Richardson/`5e-5`门，明确
保持真零 H 完整 J 的 affine 图；不把当前新 H 当成已 native 求解。当前
entry没有启动额外 native 计算、完整联解或最终闭面验收。

## 8. 输出、可复用事实及调度草稿

输出仍保 `model-000.json`、完整原各 trial、typed selected angles、全部
midpoint/col只读 observer、domain B/Gamma/Pi和同原 A 捕获、完整原 R270
root/affine/recovery、QP arrays/同 f 的 C/H选择、原实际 A/AT/B后验。
优化 warm 的 `success` 和 `new_coupled_finite_acceptance` 保持 false。
任何诊断异常只记录，不改变原 evaluate 返回数组、finite、merit或决定。

工作流草稿只更新已有 `visible-larger-public-condensed-qp.yml` 与唯一
`public-condensed-qp-request.json`，没有另一个会重复调度的 trigger。
本地交付名为 `/tmp/visible-larger-request68-workflow.yml` 和
`/tmp/visible-larger-request68-request.json`，两者都有相对66草稿的完整 `.diff`。
新请求39个源 pin逐字匹配，publisher更新为已修 sparse HANDOFF 读取的
`627393d1ba77b5e13dcf34da64204d0554a7c009770a2d80a1353c3f16b007fe`。
39源 AST、11段 shell语法和6段内联 Python AST均通过；所有预算字面值与
66相同。root负责普通 Git、真实pull/README差异检查、push和唯一dispatch。

这些静态检查不宣称新的 warm 成功。下一实际结果应先读全部原试步、最近
拒绝的真正阶段及完整 selected/node/mid/RMS范围，再决定继续；不能跨
不同重冻结权重的模型直接相减 merit，也不能因新增left466就预言接受
$\alpha=1$。
