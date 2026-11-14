# 2026-11-14：同一实际接受输出的入口反射规范形接口

完整证明为 [R249](../results/R249-shared-node-inlet-parity-normal-form.md)。新源码是 [`geometry_20261114_inlet_parity_normal_form.py`](../computations/geometry_20261114_inlet_parity_normal_form.py)。这是尚待实际成功场消费的接口；本 note 不登记任何尚未返回的数值结果。

## 修改范围和身份

输入必须先由原 reader 验证为真正接受的完整 full-DN 输出。v3 设计场使用 `LiftedModesSavedPrefix`；v4 同一度量精化场使用 `SameMetricSavedPrefix`，保留其空 active 参数向量、原三个冻结设计参数、完整 `z0` 和实际 field/tail 维数。

`normalize_inlet(saved)` 只投影首个共享节点的三个分量块：高度值全部为零、水平径向一导全部为零、高度径向二导全部为零。其余节点及所有后续单元不变。它保留原 `saved.rec` 和 `saved.original_quintic`，另定义精确共享 binary 节点的唯一实 Hermite 有限场；原接受 checkpoint 不改，后处理场不被标成新的 BVP 接受。

在该实多项式规范形中，入口反射严格满足 R248 的三项 C² 条件；其 rounded 系数与浮点读出仍是数值表示。原 prefix 的一次配准只改变 XY，反射面仍是 `z=0`。切口完整九 jet、材料均值 0/1/2 导、actual H/DN 输入、单次 SE2 拟合输入、外切口整函数修补及帽高数据都未改变。

`saved.definition["inlet_normalization"]` 是所有后续消费者的共同身份，至少含：

- `enabled`, `normal_form_schema`, `source_sha256`, `original_input_sha256`；
- 真正 v3/v4 reader 的类名、源 SHA 和 `mode_identity`；
- 原/新三份完整共享节点数组 SHA，以及实际首单元 `[0,h]`；
- 精确端点恒等式数、修补多项式系数 SHA；
- 不改变标量函数、材料角、切口、实际尾输入的声明；
- 精确有理 Bernstein/Fourier/材料角链式法则产生的九 jet 连续差界。

网格、法向 packet、空间覆盖必须使用同一个 `enabled` 值和同一份规范形身份。不能用旧未修补网格作新规范形的中心，再只在覆盖计算中改真实求值器。

## 公共 Actions 最小命令

下面 `ACTUAL` 是原 full-DN 或 v4 精化的真实成功 `actual.json.gz`；`PORT`、`CONFIG`、`RESPONSE`、`SOURCE_TOPIC` 均为该 actual 已绑定的原件；`COMP` 为本题 computations。`OUT` 使用新输出目录。

先对第一单元作局部前后读出：

```bash
python -u "$COMP/geometry_20261114_inlet_parity_normal_form.py" audit \
  --checkpoint "$ACTUAL" \
  --angles 2048 4096 \
  --radial-subdivisions 16 32 \
  --out "$OUT/inlet-audit.json"
```

该命令从相同六 jet 直接计算旧/新 operator、三个分量最大值、实际主曲率与 Gram 最小行列式，另记录首圈三项奇偶残差、六 jet 变化。全部是实际样点结果。它同时输出 R249 的精确连续修补差界；若首单元在所有设计控制之前，可直接从原标量 quintic 的 Bernstein 凸包给出正 `a_lower`，不拟合新标量。

可选 `--old-metric-bound` 只接受一个由其他证据给出的连续旧 operator 界，用 R249 公式输出条件新界。默认无需该参数，且不会把旧样点最大值自动用作这个前提。

需要完整规范化 prefix 读出时：

```bash
python -u "$COMP/geometry_20261114_inlet_parity_normal_form.py" readout \
  --input "$ACTUAL" \
  --angles 2048 4096 \
  --radial-subdivisions 2 4 \
  --out "$OUT/physical-material-prefix.json"
```

若原 after-accept 已完成实际尾的径向读出，令 `COMPLETE` 指向其原 `complete-4.json`，即可重建规范化闭面而**不重新求 DN，也不重复实际尾径向读出**：

```bash
python -u "$COMP/geometry_20261114_inlet_parity_normal_form.py" closed all \
  --checkpoint "$ACTUAL" \
  --port "$PORT" \
  --config "$CONFIG" \
  --tail-response "$RESPONSE" \
  --source-topic "$SOURCE_TOPIC" \
  --complete "$COMPLETE" \
  --out-prefix "$OUT/closed/surface"
```

原 after-accept 默认路径为 `accepted-112-physical-closed/closed/surface-actual-tail-readout/complete-4.json`。使用 `all --complete` 会生成本规范形的新 plan，并按该 plan 的真实 SHA 生成配套 source background，然后 render。虽然径向 background 的数学输入与旧 plan 相同，旧 heights 文件仍绑定旧 plan 的 SHA；不得直接把它传给新 plan 来绕过原身份检查。

所有原 actual H/config/response/public-source SHA 检查、完整 tail 模数、非线性审计、单 SE2、全角九 jet 切口差、显示网格预算及相位整除规则仍由冻结的原消费者执行。新 wrapper 不改这些五个已有源文件。

## 后续覆盖器的对象 API

```python
from geometry_20261114_inlet_parity_normal_form import read_saved

saved = read_saved(checkpoint, normalize=normalization_enabled)
# The mesh/assembly must record this same choice and the same definition.
# saved.nine_jets / material_jets / mean_jets / profile / core retain their API.
```

也可在已有实际对象上调用 `normalize_inlet(saved)`，避免重复构造。若以后直接恢复 assembly 已记录的 SE2，则继续使用原 `rotation_angle`、`prefix_translation_to_subtract` 与其 cos/sin 定义；本 wrapper 完整保留这些字段。

首单元修补的二阶成本可能分别含 `h^-2` 倍位置残差、`h^-1` 倍一导残差；必须消费真实输出后判断代价。它本身不建立全局嵌入、reach、真实 Hausdorff 幅度或同一度量精化收敛，也不把本题标准提高为所有六 jet 差必须达到机器精度。

本次本地操作只包含源码编辑、静态 AST 检查和证明书写。新的几何数值消费仍由公开仓库 Actions 执行。
