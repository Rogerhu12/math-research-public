# 显式 LU 生命周期版本：true M14/W14 选择、纯准备与关闭审计

状态：**独立备用入口；本稿和准备器不运行求解。**
作者 `db6f / coupled_prefix`，2026-11-09。
原 true-M14 v1、原 3/4 GiB 资源 wrapper 及活动 attempt02 均保持原字节。
本入口不依赖 affine01 或 true01 成功；初值始终来自此前已经真正
完成的 M14/N512 CP 及它自己的最终 `tail_0002`。

## 1. 唯一数值程序变化及来源边界

本组另建三个文件：

- `scripts/db6f-prefix-spectral-true-m14-release-lu.py`；
- `scripts/db6f-prefix-prepare-spectral-true-m14-release-lu.py`；
- `scripts/db6f-prefix-audit-spectral-true-m14-release-lu.py`。

它们从已审对应 v1 副本派生，保留 v1 所用源文件，不改原件或其
SHA 常量来冒充旧运行身份。新的 `schema`、实际命令、来源集合、
程序结果状态、最终审计状态都明确含 `release-lu` 或 `LU_RELEASE`。
数学门仍是原门；程序身份不是原身份。

数值循环唯一改动在另外冻结的
`db6f-prefix-domain-newton-release-lu.py`：原 `solve_newton` 的
refresh 预算检查后、求替换 Jacobian/LU 前，加入 `factor=None`。
删除这行后函数全文逐字等于原定义。全部异常分支、复用分支、
8 次 LU/24 次迭代/21 档内部线搜索和接受式仍是原来的。
完整控制流证明、十类隔离协议及资源限制见
`2026-11-09-db6f-prefix-newton-release-lu-method.md`；该批先已封存，
新准备器把其实际来源与报告一并绑定。

这里没有更换 `splu` 的默认排序或参数，没有改 Jacobian 公式，
没有宣称一个 Python 引用解除必然减少某个指定数量的 RSS。
3 GiB 失败发生在新网格首次分解还是后续 refresh，已有记录不能
判定；首次分解本来没有旧 LU，故本备用版本也不能保证解决内存
不足。资源额度由 root 独立外层决定，准备器没有放宽空间门或
为自己添加资源 wrapper。

## 2. 仍然完全相同的实际问题

仍以旧真 M14/N512 的 frozen affine 输入包作**来源索引**；索引中的
CP 和 `frozen_tail` 经原 metadata 校验确为该 CP 自己的真正最终
DN/J/audit。索引名中的 affine 不把新入口变成 affine，也不允许
使用 affine01 失败输出。

| 项目 | 保留值或原操作 |
|---|---|
| prefix Fourier 模数与维数 | $M=14$，43 states，14 个自由参数，13 个高模 correction scales |
| 正对角谱权 | 原已审 W14，最大权 2048；原物理变量返回及物理 RMS/BC 重算 |
| prefix angular / audit angular | 512 / 1024 |
| 原 BVP 容差 | `tol=2e-9, bc_tol=1e-8, physical_bc_tol=2e-11` |
| 网格预算 | 原 seed 真 mesh；`--preserve-restart-mesh`；`max_nodes=6500` |
| tail | 同 $g$，Nθ512，depth12，parts8，steps32，auditSteps32 |
| 原 shooting 门 | 36 次迭代，`solveTolerance=2e-9`，默认 `projectionFloor=.05` |
| tail 初值 | 旧真 M14 自有最终 `tail_0002`；原默认全模边界修正开启 |
| prefix 外层 | 原 `--lagged-tail`、最多 8 轮；每轮真实 DN/J 和原实际 BC |
| warmup | 原显式空 `--warmup-scales`，不回到其他幅值 |
| Node | 原 `--node-heap 1536` |
| 最终 seam | 原真实 Jac+audit 请求；616 Jacobian entries、17 jets、8 audit fields |

所有六个冻结物理定义字段、gauge、profile、chart、linear port、
参数自由度和边界条件仍由原 v1 的 typed equality 门支付。新 config
仍只把原五个 I/O 键指向新 stem / 原自有 tail warm；任何非 I/O
差异均拒绝。原 shared worker/core 八源也保持不变。

## 3. 何时选择新 Newton

原 coupled `main()` 原样调用原 `install()`，首次 true DN/J 也按
原路径执行。新的谱权 BVP 包装器首次被实际调用时：

1. 核查原 BVP 选项及原 14 个物理 callback 的来源；
2. 确认当时 `_bvp.solve_newton is f6curve_domain_newton.solve_newton`，
   来源/11 参数签名仍是已绑定原件；
3. 由新独立 helper `select_newton()` 显式安装单行版本，并令
   `derived.STATS is original.STATS`，不清零计数；
4. 记录 `newton_selection.before_selection_original_runtime` 和
   `newton_selection.selected` 两套真实身份；
5. 每个实际 BVP 前后均重核新函数指针、完整新源码、原源码仍未改、
   同一 STATS 字典、同一 NumPy 和 `splu`。

原 `main()` 已导入的 STATS 引用因此仍有效，最终 CP 的
`newton_domain_audit` 没有被替换成旧零计数。成功调用的谱权层仍
把物理坐标三次插值返回给原 runner；原 chart 与物理五次
`c2_interpolant` 链完全保留。

这里选择的是本独立进程中的新运行函数，之后直到进程结束保持
该显式选择；不在旧 v1 的原函数门外偷偷安装又恢复以隐藏身份。
如果原 `install()` 意外再次覆盖指针，新的每轮身份门会拒绝。
这也不是把 `original.solve_newton` 本身改写成新函数。

第一次 BVP 之前的 DN 成功，只支付首个 DN。内层谱权回调的
physical BC 在该阶段仍对应原 affine DN；真实 nonlinear BC
必须由原 `finally` 恢复 tail 后的新真 DN 与原 outer 检查支付。

## 4. 纯准备器及依赖闭包

准备器只读取真实闭 seed 的 JSON/压缩 JSON、哈希和 Python AST，
核其自有最终 tail 的实际616/17/8、shape 和原残差。它导入的
runner/helper 都仅定义函数，既不调用新 `select_newton()`，也不
调用旧 `install()` 或任何候选对象、restart、flow、RHS、solver
factory、BVP、DN。

准备器绑定原 97 来源、新三源、冻结原 true 三源、单行 Newton
两源与纯协议来源，并递归核实际本地 Python import 闭包。原
21 个 callback 定义保留，另外登记3个：新 Newton 函数、显式
选择函数和运行身份检查函数。动态加载的两个新源码都显式绑定，
不能因文件名带连字符而漏出 AST import 扫描。

它仅在完全未使用的新 topic-notes stem 生成：

- `-tail-config.json`；
- `-launch.json`；
- `-preparation.json`。

输出不含新 CP、PPoly、数学成功响应或未来 root 观察。真实纯准备
回执、实际绑定数与新文件 SHA 随后写在独立 observed/publication
中；不向已经绑定的本稿追加虚构的完成字段。

## 5. 两个关闭入口仍分别支付原门

`--mode first` 不要求进程退出：只读已关闭 `_tail_0001` 和本进程
首次绑定文件，核原请求的精确物理高度、原 config/八源、原残差、
616 Jacobian、17 jets、865×28 staged states 和13×28 raw mirror。
它不读活动 trace，不把首包当 outer 或最终图成功。

`--mode final` 仍先要求 root 独立实际工具观察，状态
`observed-process-completed`、正确新 stem、真实 session/receipt 和
exit0；guard-child 的记录不能代替这一观察。它再核原 reproduction、
summary、CP、所有压缩系数、最终 outer 和自有 final seam 的全部
原门。原 main 捕获异常后 exit0、缺 CP、`solver_success=False`、
只有首 DN 或只有文件存在，均不得放行。

相对 v1 的额外检查只说明**哪段源码真实运行**：
launch/reproduction 的 `newton_lifetime_definitions` 必须同一，
原→新的身份转换必须完整，每个实际谱权调用的 before/after
记录都须匹配新函数来源，并真记 `original_STATS_alias=true`。
不能只把原 source hash 字符串改名后绕过原来源验证。

以下数值/数据门没有删减或增加无关阈值：原物理 RMS≤2e−9，
原 actual outer BC≤1e−8，最后真 shooting residual<2e−9，
完整43维五次有限系数，14个参数/13个scales，原实际高度末端
roundtrip，真实616/17/8最终包、896角度 seam、全部原固定物理字段。
history末基点不被误设成必须等于最后 shooting residual；节点解
outer 的高度也不被误设成必须逐位等于随后五次表示的末端。

## 6. 具体命令及尚未运行的部分

在 repo 根目录，纯准备（实际新 stem 必须未使用）：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-prepare-spectral-true-m14-release-lu.py \
  --out-prefix /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-true-m14q512-release-lu-01
```

完成纯准备后可核真实负门，零输出文件、零求解：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-audit-spectral-true-m14-release-lu.py \
  --launch /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-true-m14q512-release-lu-01-launch.json \
  --mode final --check-current-gate
```

在缺少 root 实际完成观察时必须 exit2。纯准备已经执行后，不能
重跑该 stem 的准备命令；独立重放需新的未用 stem。

未来真正运行的唯一内层命令写在 launch 的 `command` 中，形如
`python .../db6f-prefix-spectral-true-m14-release-lu.py --launch ...`。
**本批不执行这一命令。** root 如选择该备用分支，还需单独绑定
其真实资源/空间 guard 和实际工具观察；当前原 attempt02 与它
不混用身份，不并行自动启动两个 BVP。

即使这一有限联解真成功，新的完整XYZ、公共C²接缝、全域连续
metric/κ、whole budget、2e−9终门、G5和独立最终复跑仍未由本入口
支付。它只使数学不变的资源生命周期分支成为可核、可运行的
明确备用入口。
