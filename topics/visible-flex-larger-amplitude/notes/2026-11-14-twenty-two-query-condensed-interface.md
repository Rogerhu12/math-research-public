# 独立22-query入口：从实际68只增加原left-RMS484

分类：独立数值实现与输入/输出契约；尚未执行的新计算。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC；代码继续沿用本轮`20261114`源名。

## 1. 实际依据与唯一新增查询

实际68在$\alpha=1/8$接受一个优化warm。最近拒绝档$\alpha=1/4$的全部
原节点、原collocation中点、21个已建模完整角网格均有效，且在该次固定
权重下实际merit下降`0.09253669240028017`。原完整双RMS检查只在
left-RMS484失效，原最小$\beta^2=-0.04104689346427315$、物理角0，原
站点`1.2400832560024813`；right-RMS没有失效查询。依据和原回执范围见
[实际68结论](2026-11-14-actual-request68-twenty-one-query-nearest-left484.md)。

本独立入口只把该left-RMS484的2048个原物理角行加入优化模型，保留
原21个typed查询。更远$\alpha=1/2$同时失败于原中点482、484、486，以及
已建模left466、left480和mid482，尚未执行完整RMS。因此本入口不添加
mid484，不把各档失败归因于同一个遗漏查询，也不保证增大可接受步长。

原完整有限方程、标量profile、338维物理场、112维core/tail、3个全局
control、原权重定义、原实际merit、全部域检查、17档回溯和原FD门保持。
阻尼仍为270；另行从actual66共同父场出发的21-query阻尼27对照是独立
分支，本入口不借其未来结果，也不从该分支的新warm继续。

## 2. 新源及冻结身份

| 新独立文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_two_query_domain_operator.py` | 32106 | `083abbf5e7f6dfede4f717d059192011e2ca4f895ff2f57e2d3760f49d06feb0` |
| `geometry_20261114_twenty_two_query_condensed_warm.py` | 42120 | `2b01d4384f312a435b4e00feb9296c93a15aebe063a29fe9c588ac230aaf867a` |
| `geometry_20261114_twenty_two_query_condensed_response.py` | 2619 | `08f8343b56b1f000ec2439b3d3d949260b26a3da5ad1dc6820788a1fd45be481` |
| `geometry_20261114_twenty_two_query_collocation_observer_warm.py` | 16728 | `240837606d8b98214d25a6c0fe8b5546ce5b4994349bea39af32e96e22241ffa` |

冻结21-query四源一字不改。新domain绑定原21domain
`0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65`；
新warm递归保留原21的`SOURCE_NAMES/FROZEN`，并钉住原21warm
`b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2`。
R270凝聚库仍为`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`，
局部QP仍为`ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`。
原完整QR、A/J、边界、C投影和warm引擎没有改写。

每个新文件旁的`.py.diff`保留相对冻结21源的完整差异。静态回执
`twenty-two-source-static-check.json`为4363B，SHA
`942282ae235657f30790775bc4833cb3eaf42c2d4df625709395f898543d96c7`。
它核实7个核心计算函数、12个只读observer函数的AST逐项相同，原中点
导数赋值AST相同，FD全文仅名称/身份替换可逆。检查只涉及源文本、AST、
整数索引和SHA，没有导入科学模块或执行数值。

## 3. Typed行序、实际支持及node484的身份变化

固定行序为以下15个left-RMS，然后7个原collocation midpoint；每组
包含原物理角index0–2047：

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484)
MID  = (473,475,477,480,481,482,485)
```

left分数仍为`0.17267316464601146`，midpoint分数为0.5。
`kind/query_index/fraction`共同定义查询，重复interval不合并两种查询。
新增left484使原mid查询的typed索引整体后移一位；所有索引从当前
`QUERY_SPECS`重建，不沿用旧21行号。

| 对象 | 新22-query身份 |
|---|---|
| 完整未知量 | 原236036个缩放坐标 |
| 不等式模型行数 | `22×2048 = 45056` |
| 唯一捕获cell | 16个；原唯一完整A/J构造中的只读捕获 |
| 实际查询端点 | nodes466–486，共21节点 |
| 实际B列并集 | 21个338维物理节点及3个control，共7101列 |
| R270声明连续局部布局 | 同nodes466–486及3个control，共7101列 |
| 当前零布局列 | 无；`zero_layout_indices`为空int64数组 |
| 原C可修正支持 | nodes471–482及3个control，共4059列 |

原21模型为保持R270连续布局而保留了node484的338个零B列。新增
left484使用真实端点484、485，原J/P捕获现在包含node484，因此它的B
列已实际存在。声明局部维数7101没有增大；实际B列并集从6763补齐为
7101，实际捕获端点从20增加至21。不能把这次变化表述为B支持完全未变。

新代码直接声明空`zero_layout_indices`，避免对空列表调用concatenate。
它核对`local_indices`与`block_column_union_indices`相同；每个block的
local索引依据当前声明布局重新映射。full/local正向和转置仍使用同一套
实际行，完整全坐标scatter和共享节点累加保持原实现。模型SHA、manifest、
export及verify同时保存实际和声明布局；当前身份明确
`formerly_zero_layout_node484_now_has_actual_B_columns=True`及
`complete_capture_includes_original_endpoint484=True`。

完整父producer作为历史原样保留。历史21及更早层中的zero484说明仍然
准确描述其旧模型，不能递归篡改；新22当前模型不能继续沿用旧零列声称。

## 4. 新left484的完整原Hermite链

令$t$为原left-RMS分数，$h$为对应原cell长度。新查询与旧left查询相同，
使用冻结的原CubicHermiteSpline：

$$
Y(t)=h_{00}(t)Y_L+h\,h_{10}(t)f_L+
      h_{01}(t)Y_R+h\,h_{11}(t)f_R.
$$

其一阶方向保留两个端点的完整状态和原J/P链：

$$
\delta Y(t)=h_{00}\delta Y_L+h\,h_{10}\delta f_L+
            h_{01}\delta Y_R+h\,h_{11}\delta f_R,
\qquad \delta f_i=J_i\delta Y_i+P_i\delta p.
$$

查询处$a$和原返回$a'$的显式control项保持。新增484的端点J/P来自同一
完整A构造的捕获，不额外构造完整J。共享control、共享端点、入口core注入
及原列缩放$S$均沿原实现，B编译只除一次$S$。

七个原中点继续直接取`state.middle[j]`和`problem.mid[j]`，其方向为
$\frac12(\delta Y_L+\delta Y_R)-\frac h8(\delta f_R-\delta f_L)$；
没有用left-RMS或节点平均替换中点。当前完整B伴随及实际complex链检查
覆盖新typed网格，沿用原实现检查阈值，不增加科学接受门，也不扩写为
连续角、全站点或精确等距证书。

## 5. 原C支持、outside offset与完整H恢复

原C候选只允许修正$S_C=$nodes471–482及3个control，共4059列。完整B
仍作用于236036维，局部C不等式的offset必须包含
$c+B_{\overline{S_C}}z_{0,\overline{S_C}}$。其outside节点仍为
466、467、468、469、470、483、484、485、486，但node484现在有真实B
贡献，不能因旧模型为零而省略。固定支持投影仍可不可行；原备份/径向
路径处理，不新增科学门。

完整R270路径保留7101维局部H-QP、原$g=A^Tb$和外部条件最优响应。
它不把原C固定支持施加到完整H方向。恢复后照旧用完整原A/AT/B/BT
读回实际gdot、全部45056行slack与R267浮点后验；后验不替代原实际
域或BVP验收。最后全向量radial仍同时作用outside部分，不声称最终
outside等于原raw方向。

模型阻尼、原候选预算、dual预算和全部真实回溯保持。新入口仅改变
当前父场和上述一组约束模型行；它没有宣称QP已精确最优，没有预测
实际步长，也没有将优化warm当作完整联解。

## 6. 首次真实父pair与own-schema续接

首次父场严格为实际68原warm/status：

| 字段 | 原身份 |
|---|---|
| science run/source | `43653811809` / `9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14` |
| parent schema | `exact-constraint-twenty-one-query-condensed-complete-H-warm-v1` |
| 原压缩warm | 4827392B，`3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535` |
| 原JSON status | 2007513B，`f4de267f1630201fb077b9d6245016760868f9a20a5b4624db08e780ce2f90e9` |
| 公开status gzip | 242383B，`4ce10967f799b887540049617bfa16b59d171dd0019396906d6dde628450365c` |

公开路径为
`notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/`。
工作流透明解压status并核原JSON字节SHA，不重新序列化；压缩warm原字节
直接复制。两种status别名同时存在时必须解码为相同原字节。原完整父
`optimization_warm`子树、源账、标量、mesh、常数core/control与原validator
保持，状态仍明确`success=False`、`new_coupled_finite_acceptance=False`。

新schema为`exact-constraint-twenty-two-query-condensed-complete-H-warm-v1`。
首次21-schema父必须匹配上述实际68双SHA；未来真实完成的22-schema
warm/status可用明确新双SHA一次调用继续，仍按原完整producer验证。
不会把初猜或pending状态冒作完成父场。observer的独立执行源身份进入
当前输出账，数学producer是新的22warm源，不冒称旧21产生新45056行。

## 7. 精确CLI及不变预算

公开Actions恢复原accepted96、699-node prepared112、T112配置与真零H
响应后，执行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_two_query_collocation_observer_warm.py" \
  --accepted "$VISIBLE_ACCEPTED" \
  --prepared "$VISIBLE_OUT/preparation112/prepared.json.gz" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --resume "$VISIBLE_PARENT68/warm-001.json.gz" \
  --expected-resume-sha 3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535 \
  --parent-status "$VISIBLE_PARENT68/driver-status.json" \
  --expected-parent-status-sha f4de267f1630201fb077b9d6245016760868f9a20a5b4624db08e780ce2f90e9 \
  --out "$VISIBLE_OUT/twenty-two-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512 \
  --condensed-dual-sweeps 200 --condensed-store-root
```

`T112_TRUE_ZERO_ANCHOR`仍为原`e788a28d…`完整真响应，公开路径
`public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`。
全部准备输入pin与实际68相同。新的实际下降warm保存后执行：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_twenty_two_query_condensed_response.py" \
  --accepted "$VISIBLE_ACCEPTED" --prepared "$VISIBLE_CONDENSED_WARM" \
  --tail-anchor "$T112_TRUE_ZERO_ANCHOR" \
  --tail-config "$VISIBLE_OUT/T112-config.json" \
  --out "$VISIBLE_OUT/physical-response" --angles 4096
```

该FD在实际新warm上重跑原完整方向、两阶Richardson和`5e-5`门。它使用
真零H全J的明确affine图，不把非零当前H叫作已有新native响应。本入口
没有额外native求解、全DN联解或最终闭面验收。原全部node/mid、两套
完整RMS、rho、实际merit和17档回溯保留，新选定网格不替代这些门。

## 8. 输出、静态回执及唯一调度草稿

输出保留完整原model/trials、所有typed角读数、原midpoint与col只读
observer、B/Gamma/Pi/原J捕获、R270局部root/affine/recovery、QP数组、
同一固定模型中的C/H选择、完整原残差后验和新warm/FD来源。observer
只读取原返回数组和原一次权重；异常记报告，不改原finite/merit或决定。

交付草稿仅更新原`visible-larger-public-condensed-qp.yml`及唯一触发文件
`public-condensed-qp-request.json`。本地文件为：

- `/tmp/visible-larger-request72-workflow.yml`，23090B，SHA
  `c139ecacdbd7338b1e18e284cf49fb0ea1c68069cd64ed07938789bb1a8eb6ec`。
- `/tmp/visible-larger-request72-request.json`，12795B，SHA
  `bdeed8cf973e1c9d09462044d89dcb582da4cdd8231521359658e80eba22d5b9`。
- 每个文件旁的`.diff`为相对实际68草稿的完整差异。
- `/tmp/visible-larger-request72-static-check.json`，8975B，SHA
  `ec6908e42af132401f72e7c8f1dc84fddd7020690dc9c907b8d56712ed4e4751`。

43个请求源pin逐字匹配；原39个加新22四源，publisher仍钉
`627393d1ba77b5e13dcf34da64204d0554a7c009770a2d80a1353c3f16b007fe`。
43源AST、11段bash语法及6段内联Python AST通过；所有预算字面值与68
一致。父21与输出22两个schema门分别保留，没有把父字段一并改名。
只有已有工作流的一次新请求，不创建第二条重复dispatch入口。

以上均为源码/字节/语法核，不代表72已经执行。实际运行后仍须先读全部
原试步、最近失败的真实阶段和完整查询范围，再决定下一步；不同轮次
重冻结权重的merit不能直接相减。root负责普通Git、实际pull/README
检查、推送和唯一调度。
