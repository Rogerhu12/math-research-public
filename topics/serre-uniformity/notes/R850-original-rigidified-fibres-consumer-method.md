# R850：原刚性化纤维、完整截面及两个帧一阶项的来源消费契约

本文件落实已公开的 [原 $c_0$ 刚性化 Poincaré 纤维证明](2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)（下称 RF）。它消费三个已经成功、已经核对来源的 producer；新工作是有限准确表达式图的组合与 RF 中两个帧一阶系数的输出。它不重新计算旧相对 Norm、原点加法、Fourier 系数、CM 响应、Dixon 位数或全局线性解。

## 1. 原对象与输出边界

始终使用原 $C_b:y^2=x^3+b$、原 $f=f_4$、原次数 $1206$、原 $T^7=\zeta^2$ 运输和原实下降 $f_R=[1-\zeta^2]f$。五方向保持

$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134),
\qquad \delta_j=p_j-q_j.
$$

输入点分别是原 $P_0=\phi(c_0)$、$P_1=\phi(c_1)$ 和原 $\gamma=[c_1-c_0]$。二者的 Jacobian、极化和 Abel 映射不混用。原局部参数为 $t=a^3$、$z=a-1$，椭圆原点参数为 $\xi=-x/y$，原微分为 $dx/(2y)$。

输出是五条原线丛及其指定非零纤维、完整 Picard 修正、刚性化比较和截面的准确有限 DAG；它没有把这些对象展开成标准 Jacobian 坐标。原 $C_h=c_{\mathrm{clear}}c_{\mathrm{triv}}$ 在图中保持具名原常数，未被另一个方便的值替换。

以下结论必须继续为 `false`：原 canonical Poincaré logarithm 数值、原高度数值或非零、原 $\eta$ 的标准坐标、CM 短候选的 A.1 接受，以及 all-$p$ 一致性。

## 2. 三个直接来源

| label | 原 producer | 本次保留的原字节 |
|---|---|---|
| `GLOBAL` | 成功 run `43790410670` 的原全局五极理想和比较函数 DAG | manifest/reference、run/core/public 元数据、证书、audit、原 DAG、stage manifest、原 source inventory 和 retained receipt，以及原 $395{,}061{,}658$ 字节载体 |
| `C0` | 成功 run `43790534424` 的原 $c_0$ Hodge 一阶、六个真 Norm 与五个比较首项 | manifest/reference、run/core/public 元数据、证书、audit、stage manifest、六个 `norm-and-trace` 阶段与五个 `comparison-leading-jet` 阶段 |
| `POINTS` | 成功 run `43789012126` 的原比较对数一阶有限精度见证 | manifest/reference、run/core/public 元数据、证书、audit、原 retained receipt 与 $2{,}078{,}830$ 字节原载体 |

直接选取清单是确定的，由原证书和固定文件名得出；每组的 `selected_file_count` 与按文件名排序的 plain spec 列表 SHA 都写入请求。每个 plain spec 是原 `file/bytes/sha256`，不改生产者配置，也不把运输复制登记成新数学结果。

`GLOBAL` 的大载体作为不展开的必要后继输入原样续传。其整体 SHA、原 source inventory、原 receipt、原 public job 和原 manifest 相互绑定；原 receipt 指定的 $2709$ 个原成员清单保留。本 consumer 不为这些成员重新执行旧数学，也不声称已在本次重新逐项展开这个大载体。

`POINTS` 的小载体则按其原 receipt 的 `expanded_sources` 解出并逐 SHA 核验全部 $270$ 件。它们的标签为 `CM,DAG,JETS,NONTORSION,POINTS,R791`；其中嵌套 `POINTS` 才是 R844 的 $529$ 节点原点图，而直接 `POINTS` 是 R847 producer。所有指向嵌套原件的图引用显式带 `nested_in=POINTS`。无需下载或重做 R847 的 $1413$ 个有限精度见证阶段。

`C0` 的旧大输入载体、旧 $V_j/W_j$ 数组与 Norm 算法无需加入本次来源闭包。其已完成六个准确 Norm 阶段及五个准确比较阶段保持为原证书的原子数学结论。

## 3. 实际 schema 与身份检查

每个直接来源均核对实际 artifact/run/source/core/wrapper、原 manifest、原完成证书及配置 SHA；来源 public input 的 driver 必须是该来源真实 driver。新 `public-actions-input.json` 的 driver 必须是本次 `R850_public_original_rigidified_fibres.py` 的 SHA，不能沿用旧包装器的身份。

两个已知 schema 差异必须按原文件处理：

- `GLOBAL` 的配置用 `source_identities.R791`；`C0` 的配置用 `sources.R791`。二者均与嵌套 R791 的实际 run/source/core/manifest 身份核同。
- 直接 `GLOBAL,C0` 的 public input 使用 `driver_sha256`；直接 `POINTS` 使用 `wrapper_sha256`。C0 core receipt 保存 `configuration_sha256`，另两组保存完整 `configuration`。这些字段不得互相假定。

另核 `GLOBAL` 中原 R840 CM 来源与嵌套 `CM` 相同。原 R791 五个 $p_j/q_j$、原 $h_j$ 索引及 eta 输入 spec 必须与 C0、GLOBAL、R844 三侧一致。

R850 数学 tag 精确绑定新 core SHA、RF proof SHA、本 method SHA、三组原数学身份与选取清单 SHA，以及核心的完整 `SCOPE`。绝对目录、运行预算和请求 resume 不改变原数学对象。冻结 R839 core 的 SHA 也在新请求与 public input 中明确绑定；核心仅重用它的 `Source`、`Graph` 和序列化定义，不实例化旧 `Job`。

## 4. 旧 Norm 与新的归一化节点

六个原 Norm 阶段输出

$$
M_j=s\,m_j,\qquad s=1+2\zeta,\quad s^2=-3,\quad m_j\in\mathbf Q^\times.
$$

图的六个输入数值是准确有理坐标 $m_j=M_j/s$，不是完整 $M_j$。相应节点的 `norm_equals_s_times_value=true`，原 full-$K$ 公式节点另指向两个实际 Norm 文件，并写 `inputs_are_rational_coordinates_M_over_s=true`。

RF.24、RF.27 已证明

$$
\nu_j=(3s)^{7\delta_j}\frac{M_0^{p_j}}{M_j^{q_j}}
      =3^{11\delta_j}\frac{m_0^{p_j}}{m_j^{q_j}}\in\mathbf Q^\times.
$$

consumer 建立这两种相等的准确表达式，不展开巨大的整数幂。六个分母非零由原完成 Norm 阶段绑定，$R_j(P_1)\ne0$ 由原 R843 非挠及 R844 Hom 字分离来源绑定，不能用未准确接受的短候选代替。

## 5. 原纤维、正乘比较和完整修正

继续使用函数理想约定 $I_Z=\mathcal O_Y(-Z)$。原来源已经给出

$$
I_{Z_{j,R}}=R_j I_{Z_j}^{\,3}.
$$

在 $P_0$ 的原帧为 $t^{-7\delta_j}$，在 $P_1$ 是支持集之外的单位帧 $1$。正乘 $R_j$ 的未刚性化标量分别为 $\kappa_j$、$R_j(P_1)$；RF.12 的指定刚性化纤维关系为

$$
v_{j,R}=\frac{\kappa_j}{R_j(P_1)}\,v_j^{\otimes3}.
$$

张量三次作用在 Poincaré 第二槽，第一点 $P_Y=[P_1-P_0]$ 固定，不能改写成同一固定扩张中的群乘三。

原 theta 源 $S_j$ 保持其原 Hom、原极化和原刚性化代表。先取原 $u_j^{\otimes3}$ 的实际 $\mathbf Q$ 下降纤维，再用 canonical square 取 $u_j^{\otimes6}$，形成

$$
z_j^{(3)}\in\mathcal P_{J_X}(\gamma,3\lambda_{S_j}\gamma)^\times.
$$

完整 Picard 修正与可能的 theta 二挠代表一起运输。图保留 RF.28 的原唯一刚性化比较，并用正乘 $\nu_j$ 归一化原 $c_0$ 截面；不把 theta 代表的二挠差单独置为平凡。

最终 local-height 节点只是未求值的原式

$$
\frac{\chi_v(\nu_j\kappa_j/R_j(P_1))
      +\frac12\tau_{J,v}(z_j^{(3)})
      +3\tau_{Y,v}(v_j)}{3q_j}.
$$

原所有地方与原 R724 splitting 都保留。该节点的 `canonical_periods_evaluated=false`；构造这个节点不构成高度数值或高度非零证书。

## 6. 两个帧的一阶系数

设原 C0 producer 已经准确给出比较单位的一阶对数导数 $d_j\in\mathbf Q$。本次仅按 RF 的已证公式输出

$$
-\frac{d_j}{2},\qquad -\frac{3d_j}{2}.
$$

它们分别属于原实下降帧及较小理想三次帧。它们是代数帧系数，不是原高度的一阶导数。这里只发生新的小有理组合，不重新求 Norm、trace 或比较函数的旧一阶数据。

## 7. 标准库 runner、断点与一日载体

runner 只做 HTTP Range/ZIP64 传输、来源 SHA/schema 检查、tar 续传与子进程调用；它不 import 数学 core。Range 运输核对 GitHub 实际 artifact 平台 digest，并逐选取成员核原 manifest SHA；若未全取 ZIP，回执不声称重新核了整个 ZIP 字节 digest。

新载体以 `GLOBAL/…`、`C0/…`、`POINTS/…` 三目录保存全部原选取文件；GLOBAL 与 POINTS 的旧 tar 本身保持原字节。续算先从本次一日载体恢复全部直接来源，再恢复同新 core/tag 的已完成 R850 阶段，不依赖届时已过期的旧 artifact。

核心 CLI：

```text
R850_original_rigidified_fibres.py --config EXPANDED_JOB --out OUTPUT --budget-minutes BUDGET
```

只有两个原子数学阶段：

1. `R850-rigidified-fibres-source-audit.json.gz`；
2. `R850-rigidified-fibres-five-original-fibres-and-sections-DAG.json.gz`。

独立 stage manifest 的键是 `stages`，排除自身。所有数学阶段均保存原 `complete=true` 与精确数学 tag。阶段已完成则直接读回；未完成的临时文件不冒充阶段。外层 runner 在预算加 $900$ 秒到达时终止 core，保留全部已经原子提交的阶段并写真实退出状态。若外层超时造成 core receipt 缺失，只有 `run.core_receipt_sha256=null` 的失败状态可以记录该缺失，不补造 core 成功回执。

verify 核完整本次输出 manifest、全部恢复载体成员、两个阶段和新图拓扑/内容 SHA；旧图节点只是来源引用，不能重写。成功要求五方向各自原指定纤维及完整截面结论全部为真，而所有未求值或未展开的边界旗标仍为假。

公开 workflow 仅监听专属请求，权限为 `contents: read`、`actions: read`，checkout 使用 `blob:none` 与明确 sparse paths。独立 rules job 实际 `git pull --rebase origin main`，比较请求所绑定的根及本专题 README。输出只上传一日 active artifact；没有发布 Git/Release 数据的步骤。

源码、参数、纸面证明及简明运行/SHA 登记可入 Git；机器回执与图、坐标、向量或载体只在一日 active artifact/carrier 中续传。本契约没有预填本次尚未运行的节点数、证书 SHA 或成功结果。
