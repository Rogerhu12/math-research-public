# 2026-11-14：v4 同材料度量精化的物理消费入口

## 状态与输入身份

这是实现接线，尚无新的 v4 接受场，也没有在本地执行数值计算。新的独立入口接受
geometry_20261114_same_metric_full_dn.py 实际接受的完整输出，使用
geometry_20261114_same_metric_saved_prefix.py 的验证和物理 SavedPrefix 接口。
prepared、失败状态及父场改标签后的文件不能通过这个入口。

v4 仍保存原始 v3 设计的全部 scalar 公式、支撑、完整参数与源哈希，并用
canonical_scalar_identity_sha256 标识固定的
$g=ds^2+a(s;p_*)^2d\theta^2$。活动 scalar 状态为空；原设计的三个
$p_*$ 通过 frozen_design_parameters 单独保留。完整物理状态为
$3M+2$ 行，另有 $M$ 个常值核心状态，尾维数为 $T=M$。
完整 $z_0$、原保存 RHS 构造的物理 $C^2$ 五次曲线、原有限 ODE 的二阶节点 jet、
完整材料逆角、解析材料均值和所有九 jet 均沿用原实现。

相关求解接线见
[同度量精化执行接口](2026-11-14-same-metric-refinement-executable-interface.md)，
数学身份和计数见 [R240](../results/R240-canonical-material-metric-and-refinement.md)。

## 四个独立消费者

| 入口 | 实际复用的算法 | v4 适配 |
| --- | --- | --- |
| geometry_20261114_same_metric_readout.py | 原完整物理五次场的材料角读出、相对 operator 与分量 metric、主曲率采样 | 改用 SameMetricSavedPrefix；显式写入同度量身份、空活动参数与原三个冻结参数 |
| geometry_20261114_same_metric_material_tail_packet.py | 原材料逆角、六 jet 频谱、完整核心换角导数、网格及模数截断诊断 | 原 scalar 构造改用 v4 重构；原数值循环不变；诊断对象增加 v4 身份，裸 native 请求格式不变 |
| geometry_20261114_same_metric_closed_assembly.py | 原实际尾绑定、全 H/J、单一 SE(2)、完整材料均值、全角九 jet 外接缝修正、有限内 collar 与帽 | 改用 v4 SavedPrefix；读者源账与 full-material-readout 入口准确指向 v4 |
| geometry_20261114_same_metric_after_accept.py | 原接受后物理读出、切口频谱、实际尾径向读出及闭图像流水线 | 三个子进程入口分别映射到上面三个 v4 文件；实际调用命令另记在每个 execution 记录中 |

原 v3 五个入口及其数值源未被修改。新包装明确保留被复用入口的源哈希和实际
v4 读者的源哈希，不把旧文件名当成实际读者。所有操作仍限定在公开仓库自己的
GitHub Actions。

## 直接调用

接受后的整套读出沿用原参数：

    python computations/geometry_20261114_same_metric_after_accept.py \
      --checkpoint "$ACCEPTED_V4/actual.json.gz" \
      --port "$ORIGINAL_PORT" \
      --tail-config "$THIS_V4_TAIL_CONFIG" \
      --tail-response "$ACCEPTED_V4/actual-tail-final-audit.json.gz" \
      --source-topic "$PUBLIC_SOURCE_TOPIC" \
      --angles 2048 4096 \
      --radial-subdivisions 2 4 \
      --readout-levels 1,2,4 \
      --out "$FRESH_V4_READOUT"

其中真实 final response 的 SHA 必须等于这个 v4 场保存的 actual_tail 身份，
输入 config 的 SHA 必须等于该次调用保存的 input_config；不能仅因是同一个
$g$ 就换成父场的实际尾。完整尾模数和完整原 port 仍由原消费者核对。径向尾读出
消费本场已经接受的真实响应，不在这个包装中创造一次新 nonlinear DN 接受。

也可以单独调用 readout，或用 material_tail_packet 的原 --station、
--angles、--tail-modes 参数诊断同一个接受场；closed_assembly 继续使用原
all / plan / render 子命令及原参数。选用更高模数后，应按实际频率相应选择足够的
材料角读出网格，不以显示网格代替物理网格。

## 与入口反射规范形的关系

这里读取的是已接受有限解本身；这四个入口不会悄悄修改入口节点 jet。
原闭读出报告的入口 $z$、水平 $F_s$、竖直 $F_{ss}$ 反射缝残差仍存在其原位置，
并不因 v4 身份而自动为零。R249 的独立入口规范形通过
geometry_20261114_inlet_parity_normal_form.py 的 read_saved / normalize_inlet
接口处理这一项；它已经识别 v3 与 v4，须以自己的构造身份和 metric 成本报告。

全角外接缝修正也保留原先的适用范围：理想函数层面的 Hermite 端点恒等式、
实际浮点端点误差及实际 metric 变化分别记录。有限全 DN 的接受、原始物理读出、
入口规范化和闭图像构造不是一个可互换的状态。

## 未增加的结论

同度量身份只绑定冻结的 scalar 函数和共同材料图。新的核心与物理场仍须重新计算
完整幅度、全部帽与活动面距离、嵌入性和 reach；不能继承父场的数值。两级材料角
和径向采样仍是数值读出，不能单独证明连续上确界或课题 README 第 5 条的同度量
求解精化。这里不增加“全部六 jet 达到机器精度”的完成门，也没有放宽原 RMS、
边界或 native tail 的任何接受门。

## 源身份与本轮核验

仅进行了 Python AST 检查和源级接口核对，没有执行拟造的接受场：

| 文件 | SHA256 |
| --- | --- |
| geometry_20261114_same_metric_saved_prefix.py | 9442814a913c4932b1955d9d91c0e1f27f212cc175f50c10b5dc33f7ac70f2be |
| geometry_20261114_same_metric_readout.py | 99a6869d2adb70ee5eb5e94d754c9b3f6f92d320ac3bae5d1ade6cfb0355c6c8 |
| geometry_20261114_same_metric_material_tail_packet.py | c562d825607331775404f12267a1acb767531ff53b2215665e2b65f450249b3a |
| geometry_20261114_same_metric_closed_assembly.py | 13cebadcaff169c66d0b63420e0c71966fd0d20538ee225bf854c55d99086bc4 |
| geometry_20261114_same_metric_after_accept.py | 5434ac0619e8f848581f9e45e4d27395466496fd70fc28ee543a7bae82bdffb1 |

实际 v4 场出现后，调用以上原参数链即可取得其真实读出；本说明没有宣称这样的
场已经求出，也没有把当前 M112 设计联解与后来冻结设计后的同度量精化混在一起。
