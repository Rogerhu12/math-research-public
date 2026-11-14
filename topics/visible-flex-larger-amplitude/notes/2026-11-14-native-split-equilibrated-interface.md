# 原 schedule 下 578 段线性表示的独立消费者

2026-11-14。新文件：

- `../computations/geometry_20261114_native_split_captured_system.py`：绑定原 actual28 与实际四短块探针，构造新的有限线性对象；
- `../computations/geometry_20261114_native_split_equilibrated_correction.py`：对该对象做有明确预算的二进幂行列均衡、带主元带状求解和精确残差修正。

本文写成时，这个新消费者尚未运行。它不能从源码准备完毕推导出短块探针已完成、扩展方向有效或 native 尾已接受。只在公开 Actions 消费指定的真实短块结果；本地仅检查语法。此任务不重解 prefix、尾背景或零 H，不增加原 ODE 步数，不改变 g、原完整 H、far 条件及原 native 容差。

## 1. 输入是两个具有独立身份的实际产物

原 actual28 整个 capture 的 result SHA 固定为：

`ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。

继续使用冻结 `CapturedArrays` 的全部原绑定，核原 29 个完整数组、116 个 chunk、源、原 seed 和负零、全部原 σ、对角 far 图以及原完整 J。原 J 的 SHA 不被重新解释为新矩阵身份。

第二个输入是 [四短块探针](2026-11-14-native-same-schedule-split-probe-interface.md) 实际完成后的整个输出目录，以及显式 `--split-result-sha256`。本接口不预填尚未取得的 result SHA。消费者要求同一冻结 producer：

| 源 | SHA256 |
|---|---|
| split probe Python | `911b8d8a872ec5ba2d1ae45cb83011e4d7b2d1302c1693bded34fc0a8f6c09ae` |
| split probe hook | `34d1bb4f31514425e123e978ccffbc5e2d36bf314a98f53505353743a01c8898` |
| same-schedule window module | `2973c14460de920ba2cc873ef9bcc137bdd264b70799ba9734122f3c610b946f` |

它核结果的 scoped completion、4 个短 J、4 个独立 no-J 窗、两段、完整原输入、计划 STOP、1 次协议请求、worker 正常退出，以及所有列出的实际文件 SHA。原请求 flags 并不被解释为完成了全 J 或 audit。所有短块数组都要有完整 shape/dtype/raw SHA，非有限数组会作为无法组装有限线性系统的实际失败报告，不能被丢弃或截断。

两份输入必须指向同一个完整 H、原 seed、配置、far、原 σ、原 profile 与 live layout。原参考 input、output、guard-mean 和两个旧长 J 都逐字节与 actual28 对应位置核对。历史绝对路径不是身份依据，实际文件 bytes 和 SHA 才是。

## 2. 扩展基点、方程和顺序

仍取 M=112、K=224。原有 576 段、577 个节点。只把原第 43、58 段各拆成两个 shooting 段，新增两个形状节点，得到 578 段、579 个节点。所有旧节点按 `old_to_new` 映射逐位复制，所有 224 个模式坐标都保留。

原段流向是 node n+1 到 node n，因此扩展数组里每个被拆的段依次放：

1. 外半块：原 k=6,...,11，带原出口的 Pi/portRatio；
2. 内半块：原 k=0,...,5，不提前除 portRatio。

新增中点取实际 inner withJac 返回的完整 226 项 state 的前 224 项。探针已经保留了两项完整 mean 积分，消费者不重算中间状态。这里的形状线性系统只增加形状节点；它不声称重新分组 mean 积分或改变最终 reduce 括号仍逐位相同，完整 mean/readout 继续按原 native 对象支付。

写内半形状流为 P、外半含原 port 的形状流为 Q，原入端为 x+、原出端节点为 x−。新基点定义

$$m=P(x_+),\qquad r_i=P(x_+)-m,\qquad r_o=Q(m)-x_-.$$

实际数组中，m 直接复制真实 inner 输出；r_i 由原顺序的二进制减法计算，通常是零。r_o 必须使用实际 split 出口再减旧 outgoing node；即使新旧出口浮点表示不同，也不以旧 residual 替换它。其他 574 段的原 residual 和旧完整 J 原字节复用。

两条线性缺陷式为

$$e_o=J_o\Delta m-\Delta x_-+r_o,$$

$$e_i=J_i\Delta x_+-\Delta m+r_i.$$

这里 J_i、J_o 是探针各自从恒等 tangent 启动得到的两个真实短块。程序不把它们乘回一个新长矩阵。精确代数消去中点会出现 J_o J_i；这个乘积不应自动等同于原 actual28 的浮点长 J。它们来自不同的有限导数传播表示，必须保留各自来源；程序也不把任何 computed J 直接称作原非线性流的精确 Fréchet 导数。

原 cut 和 far 的基态 residual 继续保留原 bytes，原 far 图仍是同一个完整对角向量。方程排列保持

$$112\text{ 个 cut 行};\quad578\times224\text{ 个 stage 行};\quad112\text{ 个 far 行}.$$

变量按 579 个完整节点排列，因此总维数为 129696。far 首行是 `112 + 578*224`。带宽推导不依赖段数：完整 stage J、左侧 −I 和原对角 far 仍给 `kl=112, ku=335`。

## 3. 显式尺度和新矩阵身份

所有旧节点 σ 按 `old_to_new` 原字节保留。新增中点取对应原 parent stage 的 σ。这一规则与探针的 `prospective-split-layout.json` 和显式 579 项尺度文件逐位一致；没有重建新 graphs/gains，也没有用新 gains 重定义原误差范数。

扩展系统的误差规范采用这组明确的新节点权重。最终方向限制到旧节点后，原 nonlinear readback 仍采用原 577 项 σ。新增中点权重不是放宽原科学验收的途径。

`new_matrix_identity_sha256` 同时绑定：

- 原 actual28 result 与完整 capture binding；
- 实际短块 result、producer、窗口 source；
- 全部 `old_to_new`、新段顺序与窗口；
- 578 个矩阵块的原始 SHA 和来源；
- 新基态、全部 residual、完整原 cut/far/H、显式 σ；
- 虚拟连续完整 J 字节流的 SHA。

旧 574 块只读流式访问，4 个新块各自有独立原始 SHA。程序不会再保存一份完整约 232 MB 的拼接 J。输出保完整新基态、residual、σ、边界以及4个小 J，原大 J 继续由已钉实际 artifact 重现。

## 4. 只复用无 depth 依赖的整数核

原 exact-allrows 入口的一些索引写死 576。本消费者不用其 `stage_bytes`、`row_order` 或 `worst_witness`，而由新的 `DynamicExactContext` 明确处理 578 段及新的 far 行。

仍复用原冻结的 `stage_job`、`boundary_job`、binary64 解码和整数有理比较：这些核只操作实际传入的一块 K×K 和对应完整方向，M/K 未变。没有修改原核或伪造原 producer 身份。

行列均衡、直接一次 `ldexp` 形成、有限带状 LAPACK、正确舍入 exact RHS 的算法复用冻结8f5源：

`8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3`。

源以可由 spawn 子进程正常导入的 canonical module name 加载；实际每块整数核仍核自己的冻结来源。没有把私有动态 import 别名发送给子进程后期待一个不存在的 module。

每一轮保全 579×224 的完整恢复方向、binary64 恢复账、全 129696 行 exact 缺陷、正确舍入修正 RHS 及 worst operand bits。最多执行显式 `--refinement-steps` 预算；第一轮不严格改善时保留上一完整方向，不隐瞒失败轮。

沿用的底层实用函数中部分字段含 `original`，在这一新目录中表示**该已绑定 578 段对象的未缩放数组**。所有输出通过 `ScopedWriter` 另加 `matrix_scope`、`new_matrix_identity_sha256` 和 `original576_long_matrix_not_claimed_solved=true`；不能据旧函数名称把结果说成解了 old576 矩阵。

## 5. 方向限制与真正的原方程 readback

最终保两份互不混称的完整 checkpoint：

- `complete-native-split-shooting-direction-v1`：579 个节点，给新系统诊断；
- `complete-original-node-restriction-of-split-direction-v1`：577 个旧节点，取上述方向的 `old_to_new` 项，逐位保负零，明示 producer 是新的 578 段系统。

它们没有使用旧 `complete-original-native-band-direction-v1` schema。原 generic trial 的旧 producer 绑定不能直接把新 restriction 当旧576矩阵的解；未来应以独立薄绑定读取这个新 schema、全部新 J 和同一旧基态，然后调用原完整 evaluate/10trial/guards/merit。

本消费者会在最后保留一次旧长矩阵的浮点全行诊断，以及对应最坏行的精确原始二进制实代数值。它们只解释两种导数表示的关系：**不要求旧长矩阵缺陷必须下降，不据其大小拒绝新方向，也不以它代替原非线性 readback**。

实际下一检查是将 restriction 放入同一个原完整 nonlinear no-J/evaluate/trial，原全部域条件和接受公式不变。本程序不执行这些调用，技术完成也不等于 native 接受。

## 6. 公开 Actions CLI

先用已冻结下载器统一取得原28；短块目录指实际探针的完整目录，不能用只含部分数组的节选：

```bash
python "$C/geometry_20261114_native_split_equilibrated_correction.py" \
  --capture-directory "$CAPTURE28" \
  --split-directory "$ACTUAL_SPLIT/native-same-schedule-split-probe" \
  --split-result-sha256 "$ACTUAL_SPLIT_RESULT_SHA256" \
  --equilibration-passes 3 \
  --refinement-steps 3 \
  --exact-workers 2 \
  --out "$OUT/native-split-equilibrated-correction"
```

这两个实际输入的 bytes 必须保持只读；输出必须是独立新目录。所有 `large-arrays` 和完整 checkpoint 可只留 Actions artifact，Git 保小摘要、清单与 SHA。launcher 不修改原 mathematical worker、原配置、原冷/暖初猜、原验收，也不启动新的 J 或零解。

后续应先读实际 short-probe 及本消费者结果，才决定采用哪个具体 nonlinear trial；本文没有预设均衡、分组或任何有限方向会成功。
