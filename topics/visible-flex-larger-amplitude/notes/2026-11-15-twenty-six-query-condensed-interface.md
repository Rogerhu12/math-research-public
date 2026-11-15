# 独立26-query入口：从实际86只加入原collocation MID479

分类：独立数值实现及实际输入、输出、调度契约；本稿冻结时尚未执行新的科学计算。  
作者：ChatGPT（geometry，AI辅助）。日期：2026-11-15 UTC。

## 1. 原件依据和本次唯一模型变化

实际86使用未改的25-query入口，在其真实新父场重新构造完整模型。
第五个原trial，即 $\alpha=1/16$，通过原完整检查并接受一个优化warm步。
同一模型的固定权重merit由`43.48685863012245`变为
`43.46927199458273`，原保存下降`0.017586635539714734`，预测下降
`0.017895041976059296`，原比率`0.9827658165453225`。原全部节点、
中点及左右两RMS族有效；之后原完整affine Rphi FD重跑通过。
`success`及`new_coupled_finite_acceptance`仍为false，没有求新H的native尾。
完整依据见[实际86正式结论](2026-11-15-actual-request86-same-twenty-five-query-mid479-limit.md)。

最近拒绝的原第四档 $\alpha=1/8$ 有以下明确记录：

| 原字段 | 实际86保存值 |
|---|---|
| 原节点域失败数 | 0 |
| 原中点域失败数、位置 | 1；MID479 |
| 已建模25个完整角网格 | 全部有效 |
| MID479原站点 | `1.217222883746318` |
| 原 $\beta^2$ 最小值 | `-0.07269811719200936` |
| 原角index、物理角 | 894；`2.742757648739526` |
| 原负角数量 | 8；2048角全部有限 |
| 原middle输入 | 全有限 |
| 原middle RHS | 338个物理分量非有限 |
| 完整RMS与实际merit | 此拒绝档未执行、未保存实际下降 |

这里没有把预测merit写成实际下降。更远 $\alpha=1/4$ 的MID487失败，
它不是本次新增点。新增MID479仍不能保证下一方向、较大步长或整个
非线性域可行；原节点/中点/两RMS族/merit/边界检查继续决定接受。

本次在真实86完整warm上构造一个新的26-query模型，只把原MID479
的2048个物理角域行加入优化约束。原17个left-RMS、8个中点、固定g、
全部A/H/C计算、原17档试探、阻尼270和全部既定预算不变。

## 2. 四个独立冻结源

交付目录：`/tmp/visible-larger-twenty-six-source/`。各`.py.diff`是相对
原25同类源码的完整差异；旧源码未修改。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_six_query_domain_operator.py` | 32954 | `b5b72fde97ece27c034a5f1ae3c81f0c0288b4092050f63e96296f764e7068c8` |
| `geometry_20261114_twenty_six_query_condensed_warm.py` | 43689 | `b9954eb5caffca7e3e001e66b07b0628a8275a22139ca3000cf527e258023197` |
| `geometry_20261114_twenty_six_query_condensed_response.py` | 2619 | `17908d4cb301f2073ce6539a8fcdc218a434529586722f013202c69378933b01` |
| `geometry_20261114_twenty_six_query_collocation_observer_warm.py` | 16728 | `e10055b6e6d5604d247ecfbe637f8ca01b2b1337a7a528da8e25cbe48e6b8b25` |

新domain锁原25domain：
`55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260`。
新warm锁原25warm：
`5dbd5948f815a1fcf4eaf2a08f7d130407ce52c96b25240738d26c6476b48b0c`，
并递归继承其全部`FROZEN`和`SOURCE_NAMES`。实际86父producer的60项
数学源身份逐文件SHA核对，26的数学producer集合在其基础上增加新warm
和新domain，共62项。独立FD及只读observer有自己的来源记录，不冒充
父场的数学producer。每一层`resume_producer`保持原样。

复用的R270库为
`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`；
local-QP为
`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`。
本次不更换这些实现、原完整A、原same-f选择器或原QR算法。

新optimizer schema：
`exact-constraint-twenty-six-query-condensed-complete-H-warm-v1`。
新B schema：
`captured-twenty-six-query-original-RMS-and-collocation-midpoint-domain-v1`。

## 3. 行序、捕获和局部列身份

```text
LEFT = (465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485)
MID  = (473,475,477,479,480,481,482,484,485)
```

先17个原left-RMS，再9个原collocation midpoint；每query保原物理角
index0至2047。left分数仍`0.17267316464601146`；mid分数为0.5。
新MID479是query20，对应当前B行40960至43007。其后的原MID480/481/
482/484/485顺序索引移一位；历史25-query记录仍按其原行序解释。
全部block、梯度、query-readout、模型身份和导出均保`kind`与各自分数。

| 对象 | 26-query源定义 |
|---|---|
| 完整缩放未知量 | 原236036 |
| B约束行数 | `26×2048 = 53248` |
| 唯一捕获cell | 原17个，即LEFT集合 |
| 实际查询端点集合 | 原nodes465至486，共22个 |
| 声明局部布局 | 原22个节点的338物理分量及3个global p |
| 局部列数 | `22×338+3 = 7439` |
| zero-layout | 空int64数组 |
| 原C允许修正支持 | nodes471至482及3个global p，共4059列 |

MID479所需两个端点479/480已经由原left-RMS479及其他查询捕获。
新增query没有新增cell或node。这个集合结论由源码字面配置检查；运行时
仍按全部真实block拼出global列并集，再核其与声明布局完全相等。
本稿没有把尚未生成的26-query B数值、hash或实际运行结果预先写成已核。

全部node J/P仍从唯一一次原完整A/J构造取得。没有第二次全Jacobian。
正向与转置使用同一套完整global列和共享节点scatter-add，新增中点没有
删去任一既有查询、任一物理模态、全局control或core入口链。

## 4. MID479保持原完整非线性中点和导数链

当前查询基点明确读取原一次evaluate的`state.middle[479]`和
`problem.mid[479]`。它不是左右节点的线性插值，也不是left-RMS站点。
令 $h=s_R-s_L$，原完整collocation中点为

$$
Y_m=\frac12(Y_L+Y_R)-\frac h8(f_R-f_L).
$$

其变分使用真正原节点RHS的全部链：

$$
\delta Y_m=\frac12(\delta Y_L+\delta Y_R)
 -\frac h8(\delta f_R-\delta f_L),\qquad
\delta f_i=J_i\delta Y_i+P_i\delta p.
$$

对同一有限物理角域函数的原查询梯度 $\Gamma$ 和查询处直接标量项
$\Pi$，完整块为

$$
B_L=\tfrac12\Gamma+\tfrac h8\Gamma J_L,\qquad
B_R=\tfrac12\Gamma-\tfrac h8\Gamma J_R,
$$

$$
B_p=\tfrac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

原列尺度只除一次。全部338物理分量及3个global控制通过原完整链保留；
通用原inlet/core分支也继续存在，当前MID479在内部不需要重构入口。
源码中这段构造的AST与原25完全相同，唯一新增计算是让既有循环同时
处理新MID479。17个left查询仍采用原`CubicHermiteSpline`。

原复杂方向检查对mid仍直接形成
`.5*(augmentedL+augmentedR)-h*(actual_rhsR-actual_rhsL)/8`，
不使用另一个spline来替代中点链。它保完整实际global-p/RHS及原实现
阈值。有限phi查询不声称给连续角域、场外Nyquist或全几何的证明。

## 5. 完整H、原C offset和原非线性检查

完整H候选仍由原R270仿射消元保全部core、pure-global、外部节点及
$g=A^Tb$。原C只是候选之一；其可修正支持仍nodes471至482+p，
有效offset仍 $c+B_{\overline{S_C}}z_{0,\overline{S_C}}$。outside节点
465、466、467、468、469、470、483、484、485、486全部保留。
不把C支持施加到完整H，不冻结H的外部仿射响应。

原same-f完整比较、全向量径向可行修复、backup和同模型线段选择保留。
实际所选方向仍重新读取完整A/AT/B/BT、gdot、全部53248行slack与浮点
后验；后验值不升级成原问题的新验收条件。径向或组合后不称其仍为
精确外部条件最优。阻尼不计入真实merit。

原所有699节点、698中点、完整左右RMS族、uniform-phi rho、完整边界、
固定权重merit与17档回溯继续原样运行。26个优化查询不是这些完整
非线性检查的替代。参数化标量profile、固定g、所有p与core常量状态的
来源约束不变，没有把共享背景或任何新的 $g$ 定义引入此入口。

## 6. 第一父件必须是真实86；后续才是新own-schema

第一步输入目录为
`notes/public-actions-43668743515-1-condensedqp/twenty-five-condensed-warm/`。

| 原父件 | 字节数 | SHA256 |
|---|---:|---|
| `warm-001.json.gz` | 4891299 | `d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e` |
| 原decoded `driver-status.json` | 2870978 | `7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235` |
| 公开 `driver-status.json.gz` | 334831 | `610e287259236ce996683bfaacdf02045cd0c4256c7ce10a2a33122c623a1464` |

第一父schema是25。新源码同时硬锁warm及decoded status两SHA，检查
其确为完成一个优化步、仍未科学接受的实际父件，嵌套producer及其
完整来源集合、field、mesh、profile、constant core/p均交原validator。
后续同新26-schema可以按同一已存在的own-schema契约接续真正新父件，
没有预造未来SHA或把原84场冒充86。

工作流允许公开status采用原JSON或原gzip别名；若存在两种别名，必须
解码为逐字相同原JSON。gzip本身也锁上表字节数及SHA。实际保存到
`parent86/driver-status.json`的是原decoded bytes，不重新序列化。
旧25源码里最初actual79/actual84的历史字段继续在原producer树中，不
改写为89的来源。

四个原问题输入保持：

| 对象 | 原SHA256 |
|---|---|
| accepted96原场 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| M112完整prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 真实zero-H T112完整J锚 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| T112配置 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

## 7. Actions-only CLI及全部既定预算

以下变量及原source恢复由工作流设置。这里只提供调用模板，没有本地执行。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_six_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT86/warm-001.json.gz" \
  --expected-resume-sha d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e \
  --parent-status "$VISIBLE_PARENT86/driver-status.json" \
  --expected-parent-status-sha 7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235 \
  --out "$VISIBLE_OUT/twenty-six-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

warm完成后，以实际status中真正新warm路径和SHA运行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_six_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

边界FD继续使用原完整方向、原步长、Richardson及`5e-5`门。它明确是
原真实zero-H J提供的affine边界代码核；不称为新warm H处的非线性尾解
或真实native导数。没有复用旧FD pass替代新计算。

## 8. 实际输出及来源范围

新的优化结果位于`twenty-six-condensed-warm/`，包括真实status、warm、
全model/trials、完整B及endpoint导出、完整condensation/QP阵与历史、
same-f比较、local阶段、原中点observer、collocation-location observer。
固定B输出保全部26组的Γ/Π/完整global列、全部9中点原输入和原endpoint
J/P。完整大数组继续artifact保存，compact summary不冒完整数组认证。

新identity键为`twenty_six_query_projection_entry`；FD来源键为
`twenty_six_query_condensed_QP_response_entry`。只读observer仍只对原
evaluate/weights返回作记录，原调用各一次，额外RHS/J/profile/边界/
model/trial均为0。observer异常被标为诊断失败，原科学结果仍由原返回
决定，不把观察器成功当接受，也不因观察器报错改写原数组。

即使有新的warm与FD pass，`nonlinear_native_solved`及完整BVP接受范围
仍未完成。完整native/fullDN、后续同g精化与闭场的责任保持原任务定义。

## 9. 唯一request89工作流草稿

草稿目录：`/tmp/visible-larger-request89/`。沿用现有
`.github/workflows/visible-larger-public-condensed-qp.yml`及唯一
`topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`
push触发。只请求`condensedqp`，保持原concurrency组、单lane/单model；
没有另加workflow或并发重复请求。

| 草稿 | 字节数 | SHA256 |
|---|---:|---|
| `visible-larger-public-condensed-qp.yml` | 26180 | `45e881d6e78755418ccfb797bb87819ca83e6a61eae22fe6e1d14eff17ff8e24` |
| `public-condensed-qp-request.json` | 19585 | `a1a5bcd0a523d0903a0223c2b670eb4289e9d889bea95ff6b1c749f82aaba844` |
| `request89-static-check.json` | 15086 | `0dd0e0bfbe5f738b003eb85ed49d96edeee5160269052dcf0c650f77387c4642` |

该草稿从实际86已核工作流改造，完整diff另附。原55个source pins逐字
保持，增加四个新26源，共59个request pins。publisher仍是原
`22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`；
规则/普通rebase/README检查和always artifact保留。

Python`3.12.14`、NumPy`2.3.5`、SciPy`1.17.0`与原单线程环境不变。
原公开78源恢复、accepted96/prepared112/zero-anchor/config恢复保持；
只把父目录改为真实86，当前执行入口/输出改为26。warm step35分钟、
FD step25分钟、job80分钟原样；内部各科学预算见第7节。科学step没有
token；原publisher独立step使用原权限。没有因此改科学预算或门。

## 10. 已完成的静态检查与尚未发生的事实

`twenty-six-source-static-check.json`为6600B，SHA
`7bb5142018de533266ed2bc1694b6786dc7ae784f54ee1950da7bf8528b8733d`。
它包含18项函数或完整类AST等同检查：原模型证据、同一A捕获、完整
H/C选择、只读中点及collocation观察器等。domain构造器全部科学AST
同25，仅错误文字query名称变化；verify/export仅范围标签变化。
完整FD文本及observer文本在反向替换名称和已核entry pin后逐字等同旧源。
所有新源经过AST及不执行的`compile`语法检查，重复keyword检查通过。

查询集合字面检查确认只加入MID479、原left集合不变、17cell/22node/
7439布局不变、zero为空，row-order包括479。父实际warm/status/gzip
逐字SHA、status嵌套于warm producer、60项实际父数学源逐字SHA也已核。
这不等同26-query数值矩阵或下一方向已生成。

工作流静态检查涵盖59source pins、11个`bash -n`脚本、6个inline Python
AST、唯一trigger/concurrency、全部原数值CLI参数/预算、FD正文及实际
86双父件和gzip。只操作源码、原JSON、哈希及字节；没有导入科学模块，
没有构造数值fixture，没有模型、RHS、Jacobian、FD或精确算术运行。
没有Git写入、workflow dispatch或未来结果SHA；发布和唯一调度由主控执行。

## 主控发布路径

四科学源、workflow45e881d6及requesta1a5bcd0均保持冻结原字节。草稿泛名回执在本notes保存为[源码静态核对](2026-11-15-twenty-six-source-static-check.json)、[工作流静态核对](2026-11-15-request89-static-check.json)；四份`.py.diff`亦按原basename保留。主控已全文读四源差异、全部接口及工作流／请求两差异，独立119项、59源、11shell和6inline检查记于[主控回执](2026-11-15-request89-root-static-check.json)，不执行本地科学。[源码草稿清单](2026-11-15-twenty-six-source-draft-frozen-files.json)及[工作流草稿清单](2026-11-15-request89-draft-frozen-files.json)保原接口SHA，本节仅作保存路径映射。
