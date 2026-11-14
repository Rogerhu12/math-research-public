# 从真实 .99 到完整物理 cut 的可执行 DN 主线

可信度：**新数值驱动与初猜设计，尚未执行完整 BVP。** 公开 Actions 已接受
的 .99 结果与原始失败日志见
[public-free3-099-accepted](2026-11-14-public-free3-099-accepted.md)。本条没有
重算或修改该接受场。

## 完整实际问题

`geometry_20261114_full_dn_solve.py` 直接消费完整 accepted M96/N1024 文件，
接既有 `AngleConnector`、coast、原 finite bridge，直到原 $r=.3$ 物理 cut。
Scalar 三控制、全材料角非均值 DN、常值 core/control 增广的定义见
[coupling-interface](2026-11-14-full-DN-coupling-interface.md)。初设计为389维，
左293行、右96行；原 separated QR 和原 Newton 源文件逐一核 SHA。

新初猜的已接受部分完整保留。新增区间以显式五次平滑权重走向**材料角
圆的全96模投影**。在原法向角旋转标架中，该圆为

$$
(R,T,Z)=a(s)\bigl(\cos(\Theta_c(\phi)-\phi),
\sin(\Theta_c(\phi)-\phi),0\bigr).
$$

$\Theta_c$ 使用实际 accepted 的全部96个 core 系数。不能用
$(R,T)=(a,0)$ 的 $\phi$ 圆替代；后者具有错误的入口角密度。
投影保留全部96模，并报告投影后相对 $a^2\rho_c^2$ 的角度量样本误差。
材料圆的组成一般也有无限谱；没有声称这一有限投影是准确圆。
新段的 mean height 只是背景积分初猜，其余高度和横向模均继续进入实际
方程。初猜不是等距解，也不是已经匹配的尾。

## 先做有实际对象的 prepare-only

以下在本公开仓库 Actions 中运行。所有路径相对课题目录：

```bash
python computations/geometry_20261114_full_dn_solve.py \
  --accepted notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --out "$RUNNER_TEMP/full-DN-prepared" \
  --work "$RUNNER_TEMP/full-DN-qr" --prepare-only
```

此步逐节点和 Hermite 中点调用原完整有限 Frenet RHS。若仅中点域不合格，
增加真实网格点；节点本身不合格则报告失败，不剪根、不改方程。
成功会留下完整389行 `prepared.json.gz`、原输入哈希、完整 scalar 定义、
所有新增节点和初始 collocation 残差；不会写 `success=True`。

## 原尾 client 与边界导数检查

`exact_20261114_true_tail_client.py::prepare_config` 从公开仓库原 A 配置
产生 M96/N1024 配置，只改变有限分辨率和移除失效旧 I/O 路径。
原78项来源通过公开仓库恢复工具读取；不依赖私有仓库。三处容量上限由
独立 SHA 锁定 Node loader 适配，原方程、分支、Newton、完整 J 和 audit
均在原路径中执行。

`geometry_20261114_full_dn_response.py` 可消费上一步 prepared 文件及同一
真实尾 client/source/config。在真正 scalar cut 上给一个明确未接受的
非零高度 trial，比较完整非局部 BC Jacobian 和389维 separated 增广的
两级有限差分。方向覆盖 core 1/32/96、径向、切向、高低高度模和三个
scalar controls。使用的矩阵是 worker `ready.linearD` 的**原 linear-graph
参考**，仅为实现检查；它不是已计算的非线性有限 DN Jacobian，后者来自
实际 shooting tangent，二者不必逐位相同。

```bash
python computations/geometry_20261114_full_dn_response.py \
  --accepted notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz \
  --prepared "$RUNNER_TEMP/full-DN-prepared/prepared.json.gz" \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --tail-client computations/exact_20261114_true_tail_client.py \
  --tail-config "$RUNNER_TEMP/tail96-config.json" \
  --tail-source-root "$RUNNER_TEMP/public-source/repro/source-root" \
  --out "$RUNNER_TEMP/full-DN-response"
```

`public-source` 应是恢复工具实际生成并带 `source-origin.json` 的目录；
上面占位路径不可以未经恢复直接创建为空目录。

## 真正耦合求解与准确的接受边界

去掉 prepare-only，给 solve 驱动同一 tail client、config、source-root，
即可执行真正全部96非均值 DN。程序逐项核查原 port 的**所有参数**及
cut 的 $r,E,E',w,w'$，不只比较两个偶然相同的 cut 数值。

每轮先求真实非线性尾和完整 $(3T+2)\times T$ J，再求完整 affine-inner
BVP，保存全维 inner 检查点，然后对新的完整材料高度重新求真尾。
RMS $10^{-6}$、BC $10^{-11}$ 原门不变；最终再作一次真 audit。没有把
inner 线性边界或零高参考矩阵的残差作为真实尾接受。

常值增广不会稀释原 RMS：原 SciPy 实现对各状态残差平方**求和**。
另外程序把实际求得的 scalar 向量 $p_*$ 固定为一个常量，重新算物理
290维 Lobatto RMS，并计入任何节点上的常值漂移。该物理 RMS 也必须
通过 $10^{-6}$。最终保存的物理 RHS 使用这一固定 $p_*$。

最终输出还保留：

- 非均值一阶和二阶高度 seam 误差；
- **均值**一阶和二阶 seam 误差，不能从报告中删掉；
- 全部 core 和 control 的常值状态漂移；
- 全部真实尾 audit、source hash、外层历史；
- 正确的固定 scalar profile 定义和完整物理/增广场，供重启与读出。

实际耦合有限解若成功，仍标记 `full_Cartesian_closed_surface=False`。
R239 的连续匹配结论还需要完整分支和谱假设；本条并未自动满足这些假设。

## 后处理与剩余关键问题

`geometry_20261114_full_dn_readout.py` 仅替换 scalar 公式的恢复入口，调用
原 material-quintic 的同一 saved-RHS C² 定义及完整材料角反解；同时记录
新 adapter 和 scalar 源哈希。核心准确证书继续使用原全96系数证书程序。

旧 .984 点的实测材料谱已表明 T96 不能保持完整二阶数据，见
[material-spectrum-accepted-0984](2026-11-14-material-spectrum-accepted-0984.md)。
这个点及新 .99 都不是物理尾 cut。T96 在新驱动中只用于未接受探索；
只有未来真正 cut 上重做角网格/频率精化、全部六 jet 和无限谱余项检查，
才能判断该 cut 所需的 T，不能沿用旧端点的小高度点值误差过关。

一次完整设计成功后，依 R240 冻结整个 $a(s;p_*)$ 与原尾/帽度量，再用
$K=0$、无 scalar 参数、全部 core 自由的共同材料角问题作真正同度量
精化。完整 Cartesian 装配、全部 $t$ 的同度量族、hold、reach、嵌入与
网格导出仍是后续实际任务，当前课题没有完成。
