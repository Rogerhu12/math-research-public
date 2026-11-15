# R416：准确 C cut 图与独立几何补丁接口

作者：geometry agent（AI）。日期：2026-11-15。

## 1. 交付、状态与冻结身份

本项接在真实 R400 continuous-ten frozen450 与完整 R409 current-C 径向/shared-B结果之后，独立构造同一准确目标的 cut 图及准确几何补丁。它没有创建、删行或重标 accepted450，没有改193运行件，也没有拿有限 Gauss 的185／189参数当连续 C 父场。

完整证明在 [R416](../results/R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md)。当前源码和证明只经过源阅读、纸面推导与文本身份核对；没有本地 import、AST、编译或科学运行，也没有实际 field、实际 cut 包围结果或新的成功证书。没有新增工作流、科学请求或 fixture 前门。

| 件 | bytes | SHA256 |
|---|---:|---|
| [geometry_20261115_current_C_accurate_cut_patch.py](../computations/geometry_20261115_current_C_accurate_cut_patch.py) | 26041 | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| [R416 完整证明](../results/R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md) | 17093 | `3aac8f522649a1375adf937d6be411038aab216e0e2e4bbb71a2cea4816ce7f7` |

独立顶层 schema：

`R416-current-C-ten450-accurate-cut-atlas-field-v1`

准确表达 schema：上项加 `-real-expression`。

唯一新几何入口：

`geometry_20261115_current_C_accurate_cut_patch.load_accurate_cut_field`

接口只新增一个 source 文件。原 R400、R409、R413、193及所有原科学源保持字节不变；本项不承担 root 的 R417 固定帽适配。

## 2. 为什么必须独立

设准确长度 $L_*$、真实数值长度字词 $L_n$、$k=L_*/L_n$。同一准确目标在数值 $t$ 中是

$$
k^2dt^2+a_*(kt;p)^2d\Theta^2,
$$

尾仍是原 $E_C(r)dr^2+r^2d\Theta^2$。原 R409 用数值返回 $v_n,b_n$ 声明图；新的准确图须用

$$
v_c=k(-E_0^{-1/2}),\qquad
b_c=k^2\left(-\frac{E_1}{2E_0^2}\right),
$$

$$
c_c=k^3\left(\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}}\right).
$$

前两个系数支付几何两 jet，第三个还必须进入 $C^2$ 目标张量的公共图。原数值字词没有准确恒等保证，不能仅换图名；本源也不声称已经证出某个 actual450 的严格不相容。

这些系数一般是实表达，不能写回原 Fraction节点冒 dyadic。故新入口保原数据，另定义完整角函数补丁。新场可能与旧场不同，原 metric／reach／held证书不自动继承。

## 3. 四个直接 source 与原完整依赖

源码逐文件核以下直接源：

| basename | SHA256 | 实际使用 |
|---|---|---|
| `geometry_20261115_current_C_ten450_shared_field.py` | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` | 原 `exact_field`／`load_shared_bundle`，完整新径向、B、同场七元组绑定 |
| `geometry_20261115_continuous_ten_frozen450_prefix_metric.py` | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` | 原 `AccurateTenTarget` 的全十DAG、全piece／support及公共u绑定 |
| `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` | 原 `Tree`、`Expression`、闭有理 `Box`，不调用新的factory搜索 |
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` | 原完整338／112材料映射、全部径向模态、六jet与piece分割 |

R416 proof的完整 SHA 也由 source 固定。原 Shared loader继续按自身 source闭包核 R400 checkpoint／SavedPrefix、原物理kernel、R249、共享背景、完整Node径向源等；没有删原source pin或新增另一套数学接受规则。

本源仅导入上述前缀metric模块中的准确目标类，不调用旧 finite-tail／旧 shared-B 初始化器，也不借原 a601 的旧 schema构造当前尾。这里没有重跑原BVP、RHS、FD或native；实际父的原验收由原loader继续负责。

## 4. 输入文件与来源链

程序接受一个已经真实完成的 R409目录及其原 `result.json` SHA。原loader从该结果读取checkpoint目录（或允许显式提供同一实际目录）并重新按其原合同验证：

- 同一实际全部十词冻结450；
- 完整338物理节点012、全112材料系数、两个均值及同一SE(2)；
- R409全部径向节点与模态、共享B及完整plan／assembly／target；
- 原完整C输入、原cut、准确family和数值编译身份；
- 原结果/成员descriptor、同场guard及完整源。

R416继而通过原 `AccurateTenTarget` 绑定当前父的实际十个dyadic参数。它不强制factory最初参数等于末参数；准确DAG与support定义保原参数族，当前点由实际checkpoint给出。原 `complete_original_C_input_binding` 与 `chosen_root_scope` 原样保留。

自然长度的表达root、实际 $L_n$ 字词、R409末节点坐标必须相符。原准确 cut radius必须等于完整径向实际cut。没有移动cut、调整warp或以nominalcut替naturalRout；原完整径向域责任仍保。

**当前不存在本项可用actual父目录或结果SHA。** 文中路径占位只说明接口，不能当输入或已付运行。193本次不执行R409，清理后的摘要/SHA不能恢复R409所需raw；将来须同job真实再生并明确接入。

## 5. DAG 扩展与闭区间计算

`AccurateCutModel` 复制原完整有序DAG，原节点逐对象不变，只追加七个root：

| root | 准确表达 |
|---|---|
| `k` | 原准确长度／实际数值长度 |
| `radial_first` | $kv_*$ |
| `radial_second` | $k^2b_*$ |
| `radial_third` | $k^3c_*$ |
| `target_first_multiplier` | $-\sqrt{E_0}/k$ |
| `target_second_multiplier` | $E_0/k^2$ |
| `target_first_in_second_multiplier` | $E_1/(2k\sqrt{E_0})$ |

三个语义叶不复制或增加，原选择根scope不改。准确对象由上述共享实函数定义；`actual_enclosures` 只是一次向外包围，不是新的实际系数或可任意精化real-name。

原闭有理 `Box` 开方保正外包端点。除法在有理端点层处理，只用严格同号分母；然后才把三个最终乘数盒转换为Arb乘数。新代码没有让宽Arb球再充当分母，也没有向原 `Jet2.__truediv__` 传非有理实系数。所有六jet由完整乘法法则传播。

若当前粗包围不足以支付正长度、正开方分母或负图导数，直接API抛出明确错误，CLI保存未完成定义。没有给原BVP新增拒绝门，没有用中点越过责任，也没有把区间不足称为实际几何失败。

## 6. 真实闭窗及完整三阶图

`closed_chart_window` 使用原准确collar宽度、实际前缀最后Hermite单元、原patch宽度、原C真实rCuff和七个root包围，按R416式(416.15)取最小正有理 $\delta$。

输出保全部最小项、$[-\delta,\delta]$、严格负导数上界、实际cut／cuff／width、准确collar包围。正侧全部落在原尾内侧及补丁，负侧全部落在准确collar和前缀末单元。它支付完整闭段，不是只验端点或采样角。

第三图jet明确存入同DAG。几何补丁虽只用两个jet，输出不因此丢掉目标 $g_{tt,tt}$ 所需的三阶坐标。

本源没有在原naturalRout外延拓E。原R409 plan若尚未用R413绑定cuff，R416不会暗改它或声称整个collar目标已付；这里的原rCuff只用于合法cut局部窗口。

## 7. 完整六jet补丁与独立API

新 `AccurateCutField` 继承已绑定的675解释器。只覆盖 `cut_targets` 和新表达身份：

$$
J_0^*=P,\quad J_1^*=M_1P_t,\quad
J_2^*=M_2P_{tt}-M_3P_t.
$$

仍是全部338字段形成的完整角函数，保零模态、两个平面均值、原竖直均值、完整材料 $\Phi$ 和单次SE(2)。原 `tail` 动态调用这个新函数，原三权Hermite/完整1025模态/B及混合链式全部保留，不做有限θ或φ截断。

公共函数返回 **`AccurateCutBundle`**，有：

- `schema`、`required_geometry_loader`：独立R416身份；
- `field`：新675派生六jet场；
- `target`：完整原准确十族目标上下文；
- `model`：准确扩展DAG、七root包围和闭窗；
- `binding`：完整来源与未付范围；
- `pieces`：原全部活动闭片；
- `evaluate(piece, radial, angular, lower=False)`；
- `expression_identity()`。

`evaluate` 接受完整闭径向区间及归一化物理角 $q\in[0,1]$，返回三坐标各六个Arb导数。径向坐标在prefix是实际 $t$，在tail/collar是实际 $r$；caller必须从该对象的完整 `pieces` 取片。反射侧保原规则。

`source_bundle` 只是原R409七元组的来源／数据，不是新准确场的替身。特别是其中旧 `A` 的数值renderer仍有旧cut补丁，不能用它绘制或取jet后称为R416。新API故意不实现旧七元组迭代协议；未来消费者必须显式绑定新loader。新 `field.binding` 也换成R416绑定，原七元组文件、guard和metadata未被改写。

本项不调用所有片、不给显示mesh、不自动执行R279/R281/R282。全帽仍须root独立R417；不能把活动pieces列表冒全帽覆盖。

## 8. 可直接接入的调用合同

未来真实同job源可构造参数对象，调用：

~~~python
handle = R416.load_accurate_cut_field(args)
jets = handle.evaluate(
    piece=handle.pieces[index],
    radial=(actual_left, actual_right),
    angular=(actual_q_left, actual_q_right),
    lower=actual_side)
~~~

参数字段：

| 字段 | 要求 |
|---|---|
| `computations` | 本job真实完整源目录 |
| `directory` | 完整R409实际输出目录 |
| `result_sha256` | 上述目录原result实际SHA |
| `checkpoint_directory` | 可省，原R409结果自带；如提供仍需原loader匹配 |
| `proof_directory` | 可省，默认computations相邻results；需完整R416原文 |
| `sqrt_bits` | 调用方明确的正整数工作精度，不是准确系数 |
| `interval_bits` | 调用方明确的Arb工作精度，至少2bit；不作为数学目标 |

没有预选参数、阈值、根成员或执行run。完整目标比较可继续用原R251四Loewner式，但必须同时使用此新准确场及原完整target，在正确坐标中支付所有闭片。原a601/旧nine schema不能重标成当前结果。

## 9. CLI与输出

定义/绑定CLI是：

~~~bash
python computations/geometry_20261115_current_C_accurate_cut_patch.py \
  --computations ACTUAL_CODE_DIRECTORY \
  --directory ACTUAL_R409_DIRECTORY \
  --result-sha256 ACTUAL_R409_RESULT_SHA \
  --checkpoint-directory ACTUAL_MATCHING_450_DIRECTORY \
  --proof-directory ACTUAL_RESULTS_SOURCE_DIRECTORY \
  --sqrt-bits ACTUAL_WORKING_PRECISION \
  --interval-bits ACTUAL_WORKING_PRECISION \
  --out FRESH_OWNED_RUNNER_TEMP_DIRECTORY
~~~

上述所有ACTUAL是来源占位，不是shell环境变量或可运行假配方。程序只在 `GITHUB_ACTIONS=true` 且正确公开仓库中执行。原输出/输入目录不得覆盖。

新临时目录包含：

| 文件 | 原范围 |
|---|---|
| `accurate-cut-expression.json` | 原全部DAG+新增节点/七root、全原C及目标绑定、当前完整包围和闭窗 |
| `complete-original-target-binding.json` | 原准确十族与完整目标上下文 |
| `binding.json` | 四直接源、完整祖先绑定identity、原父和新表达身份 |
| `new-exact-field-identity.json` | 新场身份，旧数值图明确只作为来源，未访native节点按原解释器实报 |
| `result.json` | 本定义阶段完整/未完整、成员identity、所有未付范围 |
| `necessary-summary.json` | 单份不超过90000B必要回传，不内联完整DAG或原raw |

`completed=true` 仅表示表达与API成功构造；`explicit_closed_cell_evaluations_performed=0`，全帽覆盖和新field几何接受均false。没有将定义成功称为BVP/native/metric成功。

异常保具体type/message和整个未付scope，exit2；成功定义exit0；必要摘要超90KB是exit70，保临时结果，不拆分/编码大数据。输出标记是 `BEGIN_R416_ACCURATE_C_CUT_ATLAS_SUMMARY` 与对应END，另给原必要JSON完整bytes/SHA。接口没有上传artifact或Git数据步骤，也不在本源删除旧输入或未读输出。运行级外部超时/进程停止/必要读回后清理由未来同jobowner负责；本模块不冒绝对硬杀钟。

## 10. 几何变化与保留责任

新旧准确差完整为 $h_1D_1+h_2D_2$，R416给全部系数及Gram扰动界。可在同一准确目标、同坐标中的原片证据确实存在时转移严格余量，或者重新对新场直接运行原四Loewner。没有任何实际旧误差数值或新增余量在本次被填入。

保留并明确未付：

- 原native/RK/finite shadow到准确连续对象误差；
- 实际全十点的完整半径/速度域与当前完整径向目标域；
- 新准确场的全metric、正则性、曲率、全pair/reach、held及终任务；
- 全帽interval sixjet与coverage；
- 原完整450及full338+112/mean/FD/final责任，原R400/R409来源要求；
- 未经R413绑定的cuff责任。

准确target始终是既定连续十族与原C尾目标，绝非 $1+B'^2$ 或新场诱导metric。新cut补丁支付结构兼容，不使未生成的actual场、未来共同根选择或数值终门成为已完成。
