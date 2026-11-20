# n4：缺失工作场的最短再生入口与新环境 native 源

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。

**状态：工程恢复及新设计入口；没有新增闭曲面或 10% 结论。**

## 旧状态的可知范围

新环境实查 `/workspace/scratch/7322d0dee069` 不存在；当前 scratch 文件检索也未找到原 `n4_work/native-raw-fullH-v1` 或 M24 返回场。因此原 27744 在失联后的终态仍未知，不把当前路径缺失解释成原 BVP 失败。2026-11-18 已提交的 M20 结果仍有效；这里只为继续研究再生必要场，不重复登记旧结论。

`native_raw_fullH_coupled_terminal.json` 保存了全部 20 个参数、19 个控制尺度、原 profile 以及原核定义。新增 `scripts/resume_n4/recover_compact_anchor.py` 直接用这些参数构建原 fixed-profile/raw-core 模型，以两条真实物理 BackwardLine 作初猜，执行原 Frenet BVP。它先保存原返回 cubic，再作物理 C² 插值与完整 metric 审计，避免把后处理的失败混作内解未返回。**恢复时的边界算子明确是原线性尾 DN**；原 M20 非线性尾全场没有被移用或宣称已恢复。

实际新入口：M20、angular1280、初始 615 节点、tol1e-8、bc_tol1e-8、max_nodes6000；初始边界残差 $3.7089357720\times10^{-5}$，完整初猜进入原 Newton。工作输出前缀是 `n4-work/recover-m20-v1/seed`，工具 session18524。入口不等于成功，终态另记。

## 同一实际厚 cut 的重新生成

从原 `mode4_physical_config24.json` 只把物理 `wCut` 改为 `.16`，保留其余物理尾参数；端口使用 spacing4、M24、N512、steps16。首次无共享 engine、parts32 的纯端口启动被主动中止（工具 1526 最终 exit130），未得到 DN/数学终态；它不是 OOM 或不可解证据。

随后安装既有 sparse 线性系统、same-mu engine 共享及 periodic quadrature，在 parts2 的端口构造下成功返回（18201，exit0）。这三项安装均复用已登记代码，不更改原方程/域门/尾接受门。前四个物理线性 DN 为

`31.376146246799383, 60.487854835566694, 74.13386964076182, 75.67782559005828`。

cut 的实际值是 $r=.30000000000000004$、$w=.1599999999999997$、$w_r=-3.7333333333333263$。这与旧记录表示同一物理设计；末位算术差如实保留，不承诺旧端口文件逐字节重生。新端口文件 SHA-256 为 `da2640c7b05cd3902275884ccebda1fb6d1fbb853479bb1b66ecebb4866c0d27`。

## native 入口不再依赖失去的 plan 链

新 `scripts/resume_n4_tail/native_extended/prepare_recovered_native.py` 从当前真实 sparse/shared/periodic 树直接安装原 whole-evaluate native hook，绑定当前源码、CLI 以及实际 M/spacing/N/steps。旧原物理 constructor、边界、残差归一化、Newton、线搜索、$2\times10^{-9}$ 门、cut 和 audit 均保留。并行使用原 `parallel_native_batch.py` 的字节分段/合并，只选 2 个进程；输出次序及逐段浮点 payload 不变。没有把旧 n4 manifest 重命名成新状态证书。

原 `frozen_flow_production.cpp` 用下面的原数值编译选项重新编译，88786 实际 exit0：

```bash
g++ -std=c++17 -O2 -fno-fast-math -ffp-contract=off \
  -fexcess-precision=standard -frounding-math -DVF_BUILD_MAIN \
  frozen_flow_production.cpp -o frozen_flow_batch -lm
```

新二进制为 125248 字节，SHA-256
`1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94`，恰与旧已执行生产 CLI 一致。这个身份不是新 DN 接受。新 n4 M20 owned 树 `n4-work/native-tail20` 准备与语法检查实际通过，manifest 为 `317c78663952816ed82479859bf739ef5d2e228d59b6d61e8997d1436e2b4351`。运行必须分别设置其 manifest 路径、SHA 以及新的 `VISIBLE_FLEX_NATIVE_RUN_DIR`。同一 installer 也支持 m3 的独立 M8/spacing3 作用域，不能把两者的结果混同。

## 新材料核心的独立设计路径

几何线新 `material_curvature_core.py` 的参数直接控制单位材料弧长中的曲率，不是旧支撑 Fourier 系数。新 `scripts/resume_n4/material_curvature_prefix.py` 将它接入原完整 n4 Frenet 方程：使用 identity 材料角图，固定 q，放开 delta/vd 两物理轮廓参数与 M−2 个有效曲率控制；首控制槽恒零，仅作为 vd 参数槽。原 exact lift 保留完整积分核心，解析参数 jet 改用新核心自身公式。

首个实际入口为 q=.01、保护材料半宽 .2、过渡 .25、M12、angular512、317 节点，tol1e-7/max_nodes3000；初猜全域 RHS 已实际通过，BC 为 $2.1000896998\times10^{-5}$。session45322、输出 `n4-work/material-q010-m12-v1/seed`；原 Newton 正在运行，未提前记作接受。该设计从一开始具有精确圆弧，但前缀、真正尾、C² 闭合、完整 metric/加密及全时 reach 均须由后续结果支付。它改变物理设计，不能冒称固定 g 的精化。

全部可再生全场、raw/cubic、native wire 和矩阵只留 scratch；Git 保存源、参数、命令和紧凑数值/哈希。

## 可搬迁复现命令

从本仓库根目录执行。`HELD10_WORK` 必须是仓库外的新目录。下面重新取得原 70 文件来源，随后安装本次实际使用的既有 sparse/shared/periodic 层；它不依赖前会话的 scratch。运行期间不要修改 `source`、`loader` 或其他已启动任务的 owned 源。

```bash
HELD10_REPO="$PWD"
HELD10_TOPIC="$HELD10_REPO/topics/visible-flex-held-10pct"
HELD10_WORK="/absolute/new/scratch/n4-work"
mkdir -p "$HELD10_WORK"
python "$HELD10_TOPIC/scripts/nonlinear_tail/m3_coupled_seed_deliverable/recover_m3_source.py" \
  --repo "$HELD10_REPO" --dest "$HELD10_WORK/source"
python "$HELD10_TOPIC/scripts/resume_n4/prepare_scripts.py" --dest "$HELD10_WORK/loader"
python "$HELD10_TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/make_sparse_source.py" \
  --source-recovery "$HELD10_WORK/source" --dest "$HELD10_WORK/sparse"
python "$HELD10_TOPIC/scripts/resume_m3/install_shared_tail_engines.py" \
  --copy-from "$HELD10_WORK/sparse/bundle/topics/visible-flexible-closed-surface" \
  --source-topic "$HELD10_WORK/tail-source" --manifest "$HELD10_WORK/shared-install.json" \
  --export-modules "$HELD10_WORK/shared-modules"
python "$HELD10_TOPIC/scripts/resume_n4_tail/install_periodic_quadrature.py" \
  --source-topic "$HELD10_WORK/tail-source" --manifest "$HELD10_WORK/periodic-install.json"
python - "$HELD10_TOPIC" "$HELD10_WORK" <<'PY'
import json, sys
from pathlib import Path
topic, work = map(Path, sys.argv[1:])
d = json.loads((topic/'scripts/even_circle/double_prefix_first/mode4_physical_config24.json').read_text())
d.update(wCut=.16, steps=16, shootingParts=2)
(work/'w016-port-config.json').write_text(json.dumps(d, indent=2)+'\n')
d['shootingParts'] = 32
(work/'w016-config.json').write_text(json.dumps(d, indent=2)+'\n')
PY
python -u "$HELD10_TOPIC/scripts/even_circle/double_prefix_first/export_original_worker_port.py" \
  --source-topic "$HELD10_WORK/tail-source" --config "$HELD10_WORK/w016-port-config.json" \
  --out "$HELD10_WORK/w016-port24.json"
g++ -std=c++17 -O2 -fno-fast-math -ffp-contract=off \
  -fexcess-precision=standard -frounding-math -DVF_BUILD_MAIN \
  "$HELD10_TOPIC/scripts/resume_n4_tail/native_extended/frozen_flow_production.cpp" \
  -o "$HELD10_WORK/frozen_flow_batch" -lm
python "$HELD10_TOPIC/scripts/resume_n4_tail/native_extended/prepare_recovered_native.py" \
  --source-topic "$HELD10_WORK/tail-source" --dest "$HELD10_WORK/native-tail20" \
  --native-cli "$HELD10_WORK/frozen_flow_batch" --modes 20 --spacing 4 \
  --quadrature 512 --steps 16 --workers 2
```

同原物理 raw 支的场再生入口（实际已经启动，终态另记）：

```bash
python -u "$HELD10_TOPIC/scripts/resume_n4/recover_compact_anchor.py" \
  --source-topic "$HELD10_WORK/source/bundle/topics/visible-flexible-closed-surface" \
  --loader "$HELD10_WORK/loader" \
  --definition "$HELD10_TOPIC/scripts/resume_n4_tail/native_raw_fullH_coupled_terminal.json" \
  --port "$HELD10_WORK/w016-port24.json" --out "$HELD10_WORK/recover-m20-v1/seed" \
  --modes 20 --nodes 601 --tol 1e-8 --max-nodes 6000 \
  > "$HELD10_WORK/recover-m20-v1.log" 2>&1
```

新材料曲率设计的独立入口（实际已经启动，不读上面的场）：

```bash
mkdir -p "$HELD10_WORK/material-source"
cp "$HELD10_TOPIC/scripts/resume_transfer/material_curvature_core.py" \
  "$HELD10_WORK/material-source/material_curvature_core.py"
python -u "$HELD10_TOPIC/scripts/resume_n4/material_curvature_prefix.py" \
  --source-topic "$HELD10_WORK/source/bundle/topics/visible-flexible-closed-surface" \
  --loader "$HELD10_WORK/loader" \
  --core-source "$HELD10_WORK/material-source/material_curvature_core.py" \
  --definition "$HELD10_TOPIC/scripts/resume_n4_tail/native_raw_fullH_coupled_terminal.json" \
  --port "$HELD10_WORK/w016-port24.json" --out "$HELD10_WORK/material-q010-m12-v1/seed" \
  --q .01 --modes 12 --nodes 301 --tol 1e-7 --max-nodes 3000 \
  > "$HELD10_WORK/material-q010-m12-v1.log" 2>&1
```

native 实际调用时（不是本条已完成的准备动作），使用上述 fresh owned 源及以下环境绑定；每个新 worker 的 run 目录也必须重新命名。

```bash
export VISIBLE_FLEX_NATIVE_MANIFEST="$HELD10_WORK/native-tail20/native-manifest.json"
export VISIBLE_FLEX_NATIVE_MANIFEST_SHA256="$(sha256sum "$VISIBLE_FLEX_NATIVE_MANIFEST" | cut -d' ' -f1)"
export VISIBLE_FLEX_NATIVE_RUN_DIR="$HELD10_WORK/new-actual-native-batches"
export VISIBLE_FLEX_SPARSE_LINEAR_HELPER="$HELD10_TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py"
export VISIBLE_FLEX_SPARSE_PYTHON="$(command -v python)"
```

三份新入口使用同一个实际厚 cut 来源，但旧 raw 支的幅度、控制与新材料曲率核参数意义不同，不能互用其配置/结论。
