# 同一shared-B有限闭场的R251相对算子metric消费者

日期：2026-11-15。状态：**独立source-only接线，尚无真实已接受场输入，也没有任何已通过的数值上界。** 本文复用R251的算子判据和R248的条件归约，不另立一个相同定理，不新增native求解、六/九jet机器收敛或审批门。

## 1. 具体补足的执行责任

原 `geometry_20261114_full_prefix_operator.py` 已实现完整前缀的R251消费者及原有限Gauss标量表达式。新shared-B有限闭场则还包括完整材料角复合、实际native全FFT、零模式与mean、同一个shared-B背景、完整cut修补、上下反射片和两个原固定帽。不能把原前缀证书或旧renderer的分量最大值直接改标签为这个新闭场的全域算子误差。

新文件 `geometry_20261115_shared_field_relative_metric.py` 直接复用已冻结 `ExactFiniteField` 的完整真实表达式和六jet，按R251四个严格标量条件遍历全部闭格。它把前缀、collar/native尾和两固定帽的责任统一列出，保留所有未解析叶、未访问DFS子格及完整rank后缀。它不复用旧静态网格的worst若干项，不以有限角/时间采样代替连续全域。

当前**不能自动付清的真实缺口**是原stored-tail目标的连续 $E(r)$ 包围生产者。现有节点 `r/w/w2/E`、原height表以及R283有限root-trace的分别给定原数值，并不证明径向区间上同一个 $E(r)$ 的上下界。此消费者默认把所有相应尾格列为 `original_stored_tail_continuous_E_enclosure_not_supplied`；它不会把shared-B的 $1+B'(r)^2$、样本极值或另一R26实积分背景替成原 $g$。

## 2. 同场的精确含义

输入通过原 `geometry_20261114_shared_background_closed_assembly.load_shared_bundle(args)`。它实际核当前shared-B render与其原完整closed bundle、原descriptor、checkpoint/port/config/tail response/complete readout及原source-topic。新消费者不另设accepted旗，原loader的输入范围原样保留；不制造一个当前不存在的成功field。

随后调用同一冻结 `geometry_20261115_shared_active_interval_balls.ExactFiniteField`，而非调用renderer `.jets()`后假设这些标签就是一致导数。被解释的确切有限映射是：

- R249处理后完整物理shared-node quintic，所有 $3M+2$ 分量和每个原节点都保留；保存jet是多项式系数资料，导数由该多项式真正求出。
- 同一记录的完整核心、材料角、一次SE(2)配准与平移，完整mean和零模式。
- 实际native节点的完整有限FFT系数，包括Nyquist；全部原径向Hermite系数、collar和完整material cut差均保留。
- 同一shared-B的精确有理quintic，而原参考metric表保持其原身份。改变几何背景不自动改变参考 $g$。
- 下片使用实际完整反射表达式；所有六jet均由该表达式传播，未用旧法向/kappa字段作为导数。

这仍是一个明示的准确有限实表达式，不是“逐字执行的binary64 renderer在连续自变量上的导数”。普通浮点renderer误差另欠，结果固定 `ordinary_floating_renderer_error_bound_certified=False`。

`same-exact-finite-field-expression.json` 记录已实际生成/绑定的完整FFT节点及 `all_native_nodes_evaluated_and_bound`。没有提供尾目标包围时，本组件可先完成前缀检查并明确跳过尾格；此时不能把未生成的native节点表达式假称已全部复核。原输入完整payload的来源绑定与本次真正求值范围分别保留。

## 3. 正确的共同材料角拉回

全角变量取 $q\in[0,1]$，令

$$
\phi=2\pi q,\qquad
\theta=\Phi(\phi),\qquad
\theta_q=2\pi\rho(\phi),\qquad
\rho(\phi)=1+\sum_{m=1}^{K}(1-4m^2)c_m\cos(2m\phi).
$$

使用实际完整核心的已有严格正界 $\rho\ge\rho_*>0$。`angle_density` 用同一 `material_angle` 的真实jet包围并与该完整正界相交；它没有人为加一个数值floor。$\Phi(\phi+2\pi)=\Phi(\phi)+2\pi$、$\rho>0$保证整材料圆被覆盖。

令当前径向坐标为 $u$，$X=F_u$、$Y=F_q$，

$$Q=\begin{pmatrix}A&B\\B&C\end{pmatrix},\quad A=|X|^2,\quad B=\langle X,Y\rangle,\quad C=|Y|^2.$$

原前缀以 $u=s$ 计，其目标是

$$g_{sq}=\operatorname{diag}\bigl(1,a(s)^2\theta_q^2\bigr).$$

原tail/collar以 $u=r$ 计，其目标是

$$g_{rq}=\operatorname{diag}\bigl(E(r),r^2\theta_q^2\bigr),\qquad E(r)=1+w(r)^2,$$

这里 $w(r)$ 必须是被原表/source身份绑定的同一个stored来源函数。前缀有限 $\phi$ 带宽与尾部有限 $\theta$ 带宽没有混同；完整 $\theta=\Phi(\phi)$ 的sin/cos复合用Arb包围，不重新投影成有限 $\phi$ Fourier级数。

在两固定帽使用原Cartesian $(x,y)$ 图；不将非线性材料角硬延至极点。两帽全部闭圆盘、极点、标记支撑边界和cuff圈均在其责任内。

## 4. 复用R251四严格条件

固定原请求的 $0<\eta<1$，本组件默认字面 `1/1000000`，不声称该值已经通过。若同一闭格有

$$0<\ell_i\le g_{ii}\le u_i\quad(i=1,2),$$

定义 $g_L=\operatorname{diag}(\ell_1,\ell_2)$、$g_U=\operatorname{diag}(u_1,u_2)$。代码对以下四量分别形成外向Arb包围，并要求下界严格正：

$$
P_{11}=(1+\eta)\ell_1-A,\qquad
\det P=P_{11}\bigl((1+\eta)\ell_2-C\bigr)-B^2,
$$

$$
N_{11}=A-(1-\eta)u_1,\qquad
\det N=N_{11}\bigl(C-(1-\eta)u_2\bigr)-B^2.
$$

这是R251 §2–3的同一Loewner充分判据，允许尾图的第一对角元也用包围：四正量给 $P=(1+\eta)g_L-Q\succ0$ 和 $N=Q-(1-\eta)g_U\succ0$。因 $g_L\preceq g\preceq g_U$、$1\pm\eta>0$，加入相应正半定差即得

$$ (1-\eta)g\prec Q\prec(1+\eta)g,$$

故原目标相对算子范数 $\|g^{-1/2}(Q-g)g^{-1/2}\|_{\rm op}<\eta$。使用较强的上下对角包围不会拟合另一个metric；正定性由 leading principal minor和determinant支付，未把三个分量最大值当算子范数。

下界非正或区间计算不定，都是该格未解析，不能推出存在一个真正超标点。严格等号边界不算通过。已给的粗尾包围在子格上仍可能很宽，固定精度也有舍入宽度；本程序不声称只靠二分一定最终通过。

## 5. 前缀标量仍是原有限Gauss表达式

原 `export_scalar_descriptor` 从当前重建的同checkpoint profile复制全部原48/64 Gauss节点/权重、全部冻结 $p^*$、turn/coast/bridge源常量和原mask/clip约定。`ScalarExpression` 直接解释这些确切二进制有理常量所定义的实有限和，所有径向源分支/clip/控制边界加入初始划分。

每格用内部准确分支包围整个闭径向区间，同时显式并入**原mask规则在两个闭端点实际选中的值**。因此没有以未证明的源接口连续性抹去边界分支。标量只用于目标 $a^2$ 的值，不把返回的 `ap/app` 未经证明当作有限Gauss radius的导数。

可选 `--scalar-descriptor/--scalar-descriptor-sha256` 完整核原文件SHA，再复用原 `descriptor_binding` 比较完整数学表达式。如果sidecar确由实际live profile导出并绑定当前checkpoint，才写 `actual_live_runtime_constants_verified=True`。缺sidecar或只有重建来源时，结论只绑定这次声明的实表达式；不会改标签成旧运行的实际Gauss表来源。

当前原R251 scalar接口支持原完整v3及冻结同 $g$ 的v4规格。这是实际旧入口范围；六控制低维诊断的parameter recipe不是一个该接口的已接受full checkpoint，不能直接冒用。未来若真正接受的完整模型改变标量设计schema，应增加明确同源表达式适配，不能偷偷删除额外控制。

## 6. 尾目标外部premises的精确合同和未付范围

默认不提供包围时，所有尾/collar根格直接记录 `missing_target_premise=True`，不为不存在的连续 $E$ 数据制造数值。程序仍可支付同场前缀及固定帽的独立责任。

可选输入必须成对给 `--tail-target-envelopes`、`--tail-target-envelopes-sha256`。JSON或gzip schema：

```text
same-original-stored-tail-closed-E-envelope-premises-v1
```

必需字段：

| 字段 | 真实含义 |
|---|---|
| `target_definition` | 原stored $E=1+w^2$ 字面定义，禁止B′替代 |
| `original_target_identity` | 与本次 `required-original-tail-target-identity.json` 完整字典相同 |
| `enclosure_provenance` | 非空、明确列生产源码/证明或其他来源的对象；其真假不由schema证明 |
| `closed_radial_envelopes` | 按顺序覆盖整个原 `[cuff,cut]` 的闭有理区间 |
| 每行 `closed_radial_interval` | 两个有理文本/整数端点，连续覆盖无缺口 |
| 每行 `E_lower/E_upper` | 精确有理文本/整数，满足 $0<E_{lower}\le E_{upper}$ |
| 每行 `proof_reference` | 对该行真正连续包围的外部证明定位；原样保存 |

`original_target_identity`绑定同完整field、config、实际tail response及complete readout、原reference table的全部字节SHA、原profile fingerprint、原target-background SHA、原source adapter/revision、完整径向域、原scalar数学identity、完整材料核心和正密度界。路径来自原loader的 `paths['background']`，不误用不存在的 `paths['heights']`。

这些核查只证明身份、正性和有限区间覆盖，**不证明** $E_{lower}\le E(r)\le E_{upper}$。程序始终输出 `original_continuous_E_bounds_proved_by_this_consumer=False`、`missing_original_stored_g_interval_producer=True`；外部文件即使自带true旗也不能将它们改为true。尾格通过只给一个明确依赖这些premises的条件结论。

源级缺口具体是：原stored径向来源使用已记录cum值、原有限Gauss与自适应部分积分、实际分支/原warp参数；返回 `drdx` 也不能无证明等同于该完整finite-evaluator表达式的导数。现有R26 real-integral `OuterCell` 明示另一个实积分口径。仅有节点表或分别给定的R283 `r/drdx/w/w2/E`不能自动形成同一连续 $E(r)$。后续生产者须先明确原 $g$ 的连续函数口径、原径向逆/单调定位以及全部分支覆盖，再输出上述真包围；不能用“表SHA正确”代替这项数学。

## 7. 两个原固定帽

复用冻结 `fixed_cap_rational_balls.bind_geometry` 核同plan/assembly/shared-B/所有标记和原R14设计。原帽实际准确图为

$$F_+(x,y)=(x,y,H+b_+(x,y)),\qquad F_-(x,y)=(x,y,-H-b_-(x,y)),$$

其中每个 $b_\pm$ 是对应帽所有原 $A_j\max(0,1-|xy-c_j|^2/R_j^2)^4$ 的和。R14 §2与R248 §4已在原设计中把该固定图的诱导度量固定为帽上的目标。因此这里 $g_{cap}=Q_{cap}=I+Db_\pm\otimes Db_\pm$，整Cartesian闭圆盘的相对算子误差准确为0；无需从极角采样推出极点值，也未把旧平面metric当作带标记metric。

该恒等式不需要 $H>0$；原绑定仍要求真实有限 $H$ 和正cuff。它不证明两帽与活动片的全局C²/metric兼容、不证明上下帽不相交，也不证明marker非全等见证、reach或held。

## 8. 完整闭格、资源停止与输出

初始划分保全部prefix共享节点和scalar分支边界；tail保完整native/shared-B径向节点、cuff/inner/cut-patch端点，以及所有外部target包围边界。每块保上下两片和全部闭角格 $[j/2^d,(j+1)/2^d]$，$j=0,\ldots,2^d-1$，$q=0,1$均保留。

`planned-closed-roots.json`用完整径向块列表加准确角格生成公式保存不可变全覆盖；rank恰为 `block_index*angular_count+angular_index`。它不预分配一个可能巨大的全角网格列表，也不裁掉空间。每个失败但可细分格按原两坐标中点分成四个闭子格；没有只取最坏若干格。

每次完成的判据与全部六jet写入临时gzip逐record journal。正常的显式cell数/时间预算停止会保存当前root剩余**全部**DFS格、已完成root结果，以及未触碰rank后缀 `[start,planned_roots)`。最大depth仍未解析的叶也留在完整ledger，绝不从总覆盖消失。若进程被外部强杀，只能认已落盘的partial journal/不可变计划；不能冒正常footer或完整覆盖。

主要临时输出都在 `large-arrays/`，结果描述器采用相对当前 `--out` 的完整路径：

- `input-binding.json`、`same-scalar-expression.json`、`same-exact-finite-field-expression.json`；
- `required-original-tail-target-identity.json`、`original-fixed-cap-target-identity.json`；
- `planned-closed-roots.json`、`relative-metric-cells.jsonl.gz`、`coverage-and-pending.json`。

顶层 `result.json` schema为 `same-shared-field-R251-complete-relative-metric-consumer-v1`。`completed`仅表示计划遍历完成；可以同时含未付或未解析格。分别给前缀声明实表达式通过、原live scalar来源通过、显式尾premises下活动全格通过、两帽准确零误差，以及全部未访问/未解析计数。

全局原目标接口兼容、C² seam和原stored-tail包围证明仍有各自false/unpaid字段，`whole_original_g_closed_surface_standard4_certified`固定false。没有实际完整这些责任时，不能从独立chart范围的条件通过升级为README第4项。

## 9. 全相位和其他原任务边界

准确family/source身份由原field解释器核：活动片为 $F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha)$，固定帽不动，同轴和完整反射保留。R248 §4于是给活动metric误差在材料圈上平移；帽误差为0。只有实际共同C²和原目标图册接口兼容已付时，才将完整空间结论提升到全部 $t$；本消费者没有生成该缺失证据，也没有时间采样。

它不选择或重选 $\tau$、不改变 $D=\operatorname{diam}F_0(M)$，不付reach/embedding/held/$\delta_E$，不改变原native/RMS/BC门，不把当前有限相对误差当同 $g$ 非线性精化序列已经完成。R279曲率/D消费者、R281/R282完整点对责任仍使用其各自准确范围。

## 10. CLI、依赖和真实输入

```text
python geometry_20261115_shared_field_relative_metric.py
  --directory CURRENT_SHARED_B_RENDER --basename surface
  --source-directory ORIGINAL_COMPLETE_CLOSED_BUNDLE --source-basename surface
  --descriptor ACTUAL_SHARED_BACKGROUND_DESCRIPTOR
  --checkpoint ACTUAL_ACCEPTED_COMPLETE_CHECKPOINT --port ACTUAL_PORT
  --config ORIGINAL_TAIL_CONFIG --tail-response ACTUAL_NATIVE_RESPONSE
  --complete ACTUAL_COMPLETE_NATIVE_READOUT --source-topic ORIGINAL_SOURCE_TOPIC
  --code-directory PINNED_COMPUTATIONS --out NEW_TEMP_DIRECTORY
  [--scalar-descriptor LIVE_SCALAR_SIDECAR --scalar-descriptor-sha256 ACTUAL_SHA]
  [--tail-target-envelopes SAME_G_EXTERNAL_PREMISES --tail-target-envelopes-sha256 ACTUAL_SHA]
  --eta 1/1000000 --precision-bits 192 --initial-angular-depth 3
  --max-depth 10 --max-visited-cells 1000000 --budget-seconds 3600
```

所有field及数值原loader在 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public` 之后才导入/运行。直接四source pins：

| 依赖 | SHA256 |
|---|---|
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| `geometry_20261115_fixed_cap_rational_balls.py` | `a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e` |
| `geometry_20261114_full_prefix_operator.py` | `a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703` |
| `geometry_20261114_direct_operator_cell.py` | `1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce` |

此外复用active模块原9项依赖核、原full-prefix的10项源核以及旧完整loader自己的来源核，运行件须沿已付source闭包提供它们，不只拷上述四文件。Arb来自原python-flint运行环境，NumPy负责原FFT/loader，原closed/source链其余runtime照旧。当前没有实际field可派，没有新fixture或workflow请求；所有重新生成的cell/证书payload只临时读取后按Rule15处置，不上传Git/Release。

本地仅读既有源码、证明和metadata，并做AST/字段/依赖SHA核，不import数值模块、不执行模型。实现使用已有R251/R248证明，不借本接口声称一个新数值证书已成立。
