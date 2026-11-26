# 独立 polar 输入的全 5292 列、双网格 q=2 全 H 入口

可信度：**代码接口与有限身份核验**。此条尚无新的实际 polar 全目标值、LM 接受、连续域 metric/reach 结论。旧 gap、Cauchy、v5 的接受数与指标均不借入本入口。

## 明确的新来源和目标

`6a65-geometry-nonfold-polar-q2-full-normal.py` 直接消费新
`6a65-geometry-nonfold-cartesian-prepare.py` 的独立 prepared。后者绑定实际 positive-height polar 六个位置 jet、单独冻结的目标 $g$、整段 prefix、真 R205 tail/cuff，以及两次自然退出的直接缓存。定义 $g$ 所用零参数文件的历史身份仍为 probe-only/target-definition-only；它没有被改标签成旧 Cauchy 位置或旧完整 value。本次 polar 位置是另外明确的新完整函数。

新 basis 已由 prepared 构成全部 5292 列；入口不再次细化，也不接收旧 refined/q1/q2 checkpoint。新采样为同 97 个实际径向节点的 128 与 192 全角两组，均参与目标，各乘 $1/2$。这是另一个有限 quadrature 的实际 baseline，不能引用旧 514/343 径向网格的积分值、接受数或第三观察结果。原 13 行全部保留，并在两组各追加 $q=2$ 倒面积罚项。所有 Cartesian 自由系数仅支撑于 prepared 指定的连接区间，整个 prefix 与真 tail 的两端二阶 jet 保持。

没有 `--state` 时真正创建零自由系数向量，完整求值后才写 `-initial.json`，own 接受数与尝试数均为 0。`--steps 0` 只产生这个完整 baseline 和报告，不构造 LM 接受。其 `-initial.json` 可作为 `--state` 的下一次输入。只有本入口自身 schema、实际 prepared/source/$g$/basis/pointConfig/算子 epoch/源码 hash 全相同的 checkpoint 才能续算；5292 个实际非零系数原样保留。Actions prepared 若声明实际 run ID，必须和当前进程的 `GITHUB_RUN_ID` 相同。每次使用新输出 prefix，数组与完整报告只留当前执行目录。

## 完整物理方程及诊断

冻结 helper 仍对双网格全部原 13 行与 $q=2$ 行组装完整 $H=J^TJ$，包括跨 Cartesian 分量和跨角频项。默认 $\eta=\lambda$，以 R244 的完整带因子作右预条件；实际 LSMR 消费

$$
\begin{bmatrix}JT\\\sqrt{\lambda}L_S^TT\end{bmatrix},\qquad
\begin{bmatrix}-r\\0\end{bmatrix},\qquad
\operatorname{damp}=0.
$$

原共同 Sobolev 二次型 $\lambda\,\Delta z^TS\Delta z$、全部列、完整 value 和 Armijo 判据不变。有限方向核验仍实际检查完整 J/JT 与两侧残差差商；保存了未接受试步与域拒绝，不能将其计作 value 或接受。每次实际尝试后再次求两组完整值；两组都是训练目标，报告明确没有第三独立观察。

令 $g_0=J^Tr$，$n=J^T(J\Delta z+r)+\lambda S\Delta z$。新入口同时记录

- `originalPhysicalNormalAbsoluteResidual`：$\|n\|$；
- `originalPhysicalInitialGradientNorm`：$\|g_0\|$，其定义明确为 $J^Tr$；
- `originalPhysicalNormalRelativeResidual`：$\|n\|/\max(\mathrm{float64.tiny},\|g_0\|)$；
- `originalPhysicalNormalMaxOneScaledResidual`：$\|n\|/\max(1,\|g_0\|)$。

因此小梯度阶段不会把后一缩放值冒称为真实相对 normal 收敛。LSMR 停机、有限 normal 残差和精确代数谱界均不构成非线性/连续域完成结论。

## 已实际执行的有限接口检查

`6a65-geometry-nonfold-polar-q2-entry-fixture.py` 对入口中独立的身份接收函数执行明确标识为 synthetic 的小 metadata 检查。实际 OS exit 0，外部 0.41387301999202464 秒；不调用真实 polar provider、完整 5292 列 normal 或任何 LM。

检查支付了新 zero 初始化、非零 own 向量及 2 次接受/3 次尝试的原样传承。21 个被拒变更包括旧 schema、错误 prepared/$g$/源/basis/支撑/pointConfig、model 与 entry 字节、错误或布尔计数、缺列/多列/非有限列；4 个 run 身份异常也均被拒。另取 $\|n\|=10^{-10}$、$\|g_0\|=5\cdot10^{-9}$，实算真相对值 $0.02$，max-one 缩放值 $10^{-10}$；全零与非有限输入边界也核过。此 metadata 测试中的 6 维向量不冒充真实 5292 维科学计算。

可复算命令，`$SCRATCH` 为 Git 外新目录：

```sh
python "$SCRIPTS/6a65-geometry-nonfold-polar-q2-entry-fixture.py" \
  --entry "$SCRIPTS/6a65-geometry-nonfold-polar-q2-full-normal.py" \
  --output "$SCRATCH/polar-q2-entry-fixture-report.json"
```

完整新输入的实际入口用法：

```sh
python "$SCRIPTS/6a65-geometry-nonfold-polar-q2-full-normal.py" \
  --scripts "$SCRIPTS" --prepared "$SCRATCH/polar-prepared.json" \
  --prefix "$SCRATCH/polar-baseline" --steps 0
python "$SCRIPTS/6a65-geometry-nonfold-polar-q2-full-normal.py" \
  --scripts "$SCRIPTS" --prepared "$SCRATCH/polar-prepared.json" \
  --state "$SCRATCH/polar-baseline-initial.json" \
  --prefix "$SCRATCH/polar-step01" --steps 1
```

上面的完整 baseline/LM 命令在本条发表时尚未由本核验运行；它们消费实际 prepared，不能用 fixture 替代。若设置 `--operator-epoch`，以后自身续态必须保持同一实际源码提交身份。

## 冻结字节与实际回执

| 文件或输出 | SHA-256 |
|---|---|
| 新 polar 全 H 入口 | `1acca77721dc06cb1ac00f369e96a6f9b36da7976162b696def98f0766865c20` |
| 有限身份/诊断核脚本 | `3bd5716b971387ab6ec8f809951da1cd20f9cc42450a61848e3ea0ba35878f3f` |
| 新 prepared 入口 | `497f7e7220003ec0b80ecb97e170b7e68009dcbab63ec06cefedcaf41e15588a` |
| 新 polar background | `39adb88c1d7b9aa6c43b8851e20d7d7ff2c48734fca14e68178532a636601cdb` |
| 不变的双网格 q=2 全 H helper | `8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084` |
| 此次有限完整报告，仅 scratch | `3e4d5d01bf08386d57180acd9c09d0d899efd878d5914a1bc4336b3cc6fb09e1` |
| 此次外部退出回执，仅 scratch | `0db5df066936bf340f3e8a55de8fb1c7225068d32c66487549d43605c9129873` |
| 此次 stdout，仅 scratch | `0feb9354b28a16745e529d8e844aa515bd5afa4f35a53126ea51ba7914064ce4` |

只发布源码、参数、此结论和输出 hash；不把完整可重算报告或 cache 存入 Git。当前新入口自身实际科学接受数仍为 0；具体 polar baseline 和后续接受须另付实际退出与数据身份。

## 稳定反参的显式 v2 生产入口

后继 `6a65-geometry-nonfold-polar-q2-full-normal-v2.py` SHA `18ba78db845473cfeef6125cde41e733b36ce096963e01ab1fec43041dadc37a` 只更换显式schema、base/background绑定和缺省文件名，绑定新的prepare `4e6aaee2178c621e1207f6d5b06d58d075aea1c0566f84c8b506cfd588db0ddd` 与background `58e7080d51c0c0a7d584e688c9ec1b995fdffb72c0c0a21eec9a8f23f178c3fd`。实际compile/--help均自然0；所有run/guard函数AST与上面的v1逐项相同，不重跑无关数学核。

[v2实际完整新基线](2026-11-26-6a65-geometry-polar-v2-actual-complete-baseline.md)已实际消费该v2入口：两个全新直接缓存及assemble自然0，全部5292列/434560行的新完整baseline自然0，总R²97.05124504890188、metric.9394005187239691、曲率104.97845760048854，接受0。此处的0仅指baseline调用；后续真实LM另行登记，不能将首版metadata fixture当作该生产值。
