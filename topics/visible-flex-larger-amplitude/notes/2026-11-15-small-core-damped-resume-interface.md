# 原 R259 三方程阻尼候选的真实父结果续接接口

日期：2026-11-15。状态：独立源码及源码级核验完成；未运行本次科学计算。拟供第 82 轮使用，实际提交、run、artifact 和未来结果 SHA 均不预填。

## 1. 本次解决的接口

第 80 轮完整原件已经给出八次首试步 $\alpha=1$ 接受，最终参数为

$[0.09071772300091886,-0.13939413969182854,-0.12252606423015384]$。

原三方程仍为 $[206.4299715953469,-176013.15201356995,1950.1545213062855]$，所以此次仍只是候选诊断。完整事实及原件身份见 [actual80 正式读回](2026-11-15-actual80-damped-small-core-eight-full-steps.md)。现有 `geometry_20261115_small_core_damped_search.py` 固定从 actual78 开始，本新入口只把父来源改成显式完整父文件 SHA，并用独立 schema 记录续接。

独立源 `geometry_20261115_small_core_damped_resume.py`：15452 B，SHA256 `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a`。

两层已冻结科学源保持原字节：

| 用途 | 源及 SHA256 |
|---|---|
| 实际 6×3 正阻尼方向 | `geometry_20261115_small_core_damped_search.py`，`1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| 原三方程、Jacobian、域、FD、Arb、圆参考 | `geometry_20261114_small_core_resonance.py`，`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |

新源直接绑定并导入 `1691.damped_direction`，再通过其原 `original_module()` 加载 `3b9`。没有复制或重写方向公式。数值模块只在 public repository Actions 环境条件通过后导入。

## 2. 真实父来源契约

两个必填参数为 `--parent-status` 与 `--parent-status-sha256`。后者必须是真实提供文件的 SHA256；若文件是 gzip，哈希针对原压缩文件。程序按 gzip magic 解码，记录压缩与解码后各自长度/SHA，并将提供的完整文件原字节保存到独立输出目录。

支持的父来源仅为：

1. 冻结 `1691` 输出的 `R259-original-three-equation-column-scaled-LM-candidate-v1`。
2. 本次精确同一新源输出的 `R259-original-three-equation-column-scaled-LM-resume-v1`。其 `source_sha256` 必须等于本 checkout 中本源实际 SHA，`direction_engine_source_sha256` 必须等于冻结 `1691`。

两类父状态均须是完整 `phase=diagnostic-completed`、`diagnostic_completed=true`，并明确 `success=false`、`native_nonlinear_solver_called=false`、`full_nonlinear_nonzero_lambda_solution_computed=false`。这些是候选输出来源契约，不要求父残差已小、不要求父 Arb 结论更强，也不作为原 BVP/native 的新通过条件。

父 `consumed_source_sha256` 的全键集合和每个实际文件 SHA 均核对；第一类为原十件，第二类为加新入口后的十一件。两者共享原全部模型源码。四件数学输入须与原 `EXPECTED` 以及本次提供文件逐项一致。未来同一冻结新源可继续自己的完整输出；源码版本变化时不能把旧 producer 仅改名成新 producer。

只从父 `final.parameters` 读取三个有限 JSON 数值作为初猜。每次重新 `model.evaluate(parameters)`、重新 `description`、重新 Jacobian 与试步。父的状态、Jacobian、merit、FD 和域结果均不冒充本次新算结果；文件完整保留用于来源追溯。

## 3. 第 82 轮的具体已存在父输入

真实第 80 轮：run `43664043053`，source `5a17ad802c28a0a00f2776201cea4cef27f68da7`，job `132659392179`。

公开父文件：

`notes/public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/damped-search-status.json`

其原件 52985 B，SHA256：

`ebe5b50c6af5ec9cfbe201e4d19a1b24dc9357e28ac8fe89354d5c04fd13ee2a`。

原四数学输入不变：

| 输入 | SHA256 |
|---|---|
| accepted96 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112 / 原699节点 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 实际 T112 零尾完整 J | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原尾配置 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

不需要为本入口重新调用 native 或重算零尾。原完整 112×112 slope J 仍由原模型消费；原 diagonal/非零低模 target 适用条件保持，不能用此三方程入口代替高模 Schur 消元。

## 4. 唯一有界下一实验及原数学

建议请求显式选 `--damping 0.1 --candidate-steps 8 --backtracks 20`。该选择依据是第 80 轮全部首试步被接受，但后段弱敏感方程仍有大残差；减小模型正则项是可检验候选，不是已证明的唯一原因，也不保证成功。源码要求 `--damping` 显式给出，不含隐藏默认或自动扫描。

仍逐轮使用实际原三方程 $r$ 与 $J$，列尺度 $D_{jj}=\|J_{:,j}\|_2$；恰零列仅取尺度 1，保留全部三列。设 $A=JD^{-1}$，通过完整六行增广 least-squares 解

$\min_z\frac12\|Az+r\|_2^2+\frac12\eta^2\|z\|_2^2,\qquad d=D^{-1}z$。

没有形成法方程，没有重加权原方程，阻尼没有加到原非线性残差或 merit。$\eta$ 是尺度后六行系统的显式罚系数，实际罚矩阵为 $\eta I$；这里的 0.1 不是残差阈值。

理想精确增广解满足 $r^T Jd=-\|Az\|_2^2-\eta^2\|z\|_2^2$。实际 floating 解不借此恒等式免除检查：仍直接算保存的 $r^T(Jd)$，只在有限且严格负时进入原回溯。全部 rank、singular values、列尺度、完整增广阵和恢复方向原样记录，rank/SVD 不变成收敛证书。

原非线性试步正文逐 AST 保持：$\alpha=2^{-j}$，$j=0,\ldots,19$；用实际原 `model.evaluate(p+alpha*d)` 和未加权 $\frac12 r^Tr$，接受条件仍为原 `.2` Armijo。原域异常捕获和实际参数更新顺序完全相同。没有新增参数 box、投影、截频、根路径或范数阈值。

完整末端保持原 low-mode 实差分三档、原返回 scalar 的 Arb 分片、完整零 core 圆参考及 112 right residual 读出。`1e-8` 只是已有该候选读出标志，绝非原 BVP/native 接受门。参数在搜索中改变，不能宣称整个搜索保持单一固定 metric；原有限 Gauss 的 `a/ap` 含义也未改写。

## 5. CLI 与预算

```bash
python computations/geometry_20261115_small_core_damped_resume.py \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED112" \
  --tail-anchor "$TRUE_T112_ZERO_J" \
  --tail-config "$TAIL_CONFIG" \
  --parent-status "$ACTUAL80_STATUS" \
  --parent-status-sha256 ebe5b50c6af5ec9cfbe201e4d19a1b24dc9357e28ac8fe89354d5c04fd13ee2a \
  --damping 0.1 \
  --candidate-steps 8 --backtracks 20 \
  --candidate-resonance-tolerance 1e-8 \
  --interval-bits 160 --interval-depth 14 \
  --out "$VISIBLE_OUT/small-core-damped-resume"
```

原 allowed bounded count 沿 1691：candidate steps 0–12，backtracks 1–20。本次建议只用 8/20；Arb160/depth14 与候选标志1e-8均保持既有参数。原 workflow 的四输入、Python/NumPy/SciPy/python-flint 版本、恢复公开源及 publisher 路径沿实际80；source closure 只在原69件上加入本新源，原3b9和1691均保留供导入。

八轮预算最多八次6×3 least-squares、160次 trial evaluate。沿原 Jacobian 三 complex-step 和初末 description 的三档实差分，模型 evaluate 上界仍为既有227次；不增加 native/RHS大系统求解或完整尾 Jacobian。Arb/circle 是原完整最终读出，不裁减。若实际域拒/早停，真实次数由新 status 记录。

## 6. 新输出与失败保全

独立输出目录必须为空；此检查先于父文件复制。主要文件：

| 文件 | 语义 |
|---|---|
| `damped-resume-status.json` | 新 `R259-original-three-equation-column-scaled-LM-resume-v1`；完整初末诊断、全部方向和试步、实际阻尼文本/数值、producer/source/input身份 |
| `parent-damped-status.json` 或 `.json.gz` | CLI 给定父完整原字节；SHA、解码SHA和实际 producer 写入 `parent_status` |
| `complete-scalar-domain.json.gz` | 原函数完整输出，格式不变 |
| `circle-reference.json.gz` | 原完整圆参考输出；若原函数出现域失败则按其原输出范围保存 |

新增 `source_sha256` 指本新入口，`direction_engine_source_sha256` 指1691，`original_diagnostic_source_sha256` 指3b9。`parent_status` 包真实文件哈希、schema、producer、literal final parameters 和父阻尼信息，禁止只换旧标签。

`diagnostic_completed=true` 只表完整候选计算完成。`success` 始终 false；不声明非零 native、全 BVP、闭场、完整 metric、reach 或 $\delta_E$ 已通过。原 try/except/finally 保存中途 exception/traceback/status；科学前的来源或目录错误仍由原 CLI 日志保留，不伪造搜索行。

## 7. 本地验证范围

本地没有导入数值模块、没有调用候选或原模型函数。22项源码/字节检查已通过，包括：

- 整个数值 `try/except/finally` 与1691逐 AST相同，唯一允许差异是 status 文件名。
- 原完整 trial 正文与3b9逐 AST相同；五条原输入/model setup语句与1691相同。
- 新入口直接绑定冻结方向函数；Actions条件在数值模块导入之前。
- actual80完整52985B父件、其十个共用模型源码和原四input metadata逐项核对。
- 新 own-schema 所需 producer/source 字段由实际 status 构造输出；父gzip原bytes及解码身份都保留。

完整差异为 `resume-relative-to-frozen1691.diff`，核验记录为 `source-only-check.json`，可复现读源脚本为 `check_resume_source_only.py`。这些是源码及已存原件证据，未执行第82轮、未产生其参数/残差/FD/Arb/circle结果。
