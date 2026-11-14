# 原 M14 真联解的 W14 选择器、纯准备与关闭审计

2026-11-09，`/root/coupled_prefix`。本实现落实已审 `prefix-spectral-true-m14-interface.md`，保留该稿原字节。**本批只准备入口并作静态/元数据检查；实际 coupled 运行由 root 另行持有工具会话。** 未用 M15 的 continuation/最终门冒充 M14 运行，也不翻转 affine 试验的实际性质。各源码与工件的最终 SHA、真实准备退出记录见本批 publication。

## 1. 三个全新文件

| 文件 | 职责与执行边界 |
|---|---|
| `scripts/db6f-prefix-spectral-true-m14.py` | 新实际 selector。仅将原 flat-coupled 模块的 global `solve_bvp` 换成已审 W14 callable；它的 `main` 会运行真实求解，本批不调用。 |
| `scripts/db6f-prefix-prepare-spectral-true-m14.py` | 纯来源/JSON/AST准备器。生成独立 config、launch、preparation 三件小文件；不初始化 candidate、restart、flow，不安装 Newton、不创建 weighted solver 或 tail client。 |
| `scripts/db6f-prefix-audit-spectral-true-m14.py` | 新 M14 身份的只读首包/最终关闭审计。只读 JSON、源码哈希及保存的数组，必要时仅用 PPoly 算保存图端值；不调原 flow/ODE/DN/BVP。 |

原 `db6f-prefix-coupled.py`、flat patch、shared 八源、已审谱权模块、旧 affine runner、M15准备器及审计器全部不改。新文件复用 frozen affine runner 的**通用 metadata/source helper 定义**，绝不调用其 `main`，也不复制它的 affine 结论到新运行。

## 2. 真实基线与完整来源

准备器严格绑定原 affine preparation launch `e45c553e…` 的97来源；这里借用的是已经验证的**原真 M14 输入和源码闭包**，不是其未来 affine 试验结果。实际基线为原 `fixed-m14-d12-p8-s32-q512-outer-from14.json.gz`，初始 tail 为其自己最后 `_tail_0002.json.gz`。原 CP、own tail、原 profile/chart/port、全部系数分片及旧闭运行事实都仍在此来源链中。

新 callback 账本保留原15项，再补原 `main`、`solve_with_actual_tail`、seam、shared solve/close及 `SupportBVP.flow`，共21项。新增 AST闭包扫描把**原 coupled main**与新 selector main纳入运行图；只排除不被本次调用的其它 dependency CLI main。整份被排除函数所在文件仍绑定；未知本地 `f6/curve_/fixed_metric_` 等导入拒绝。这个区别不能继续沿用“affine不运行原coupled main”的旧范围。

准备前对原 own tail 作完整有限 schema检查：它是历史真实已闭响应；没有制造未来成功 packet。检查原616项 Jacobian、17字段 jets、8字段 audit、865×28 staged states及13×28 raw mirror、原残差与参数。准备器不以任何新射击或输出存在代付这些事实。

新运行配置从原 M14完整 config复制，只改 `initialCheckpoint/traceFile/iterationCheckpointFile`；若原来有另两项 trial I/O，才一并改为新路径，保持原键缺席性。当前原 M14没有 trialDiagnosticFile/trialStatePrefix。新 initialCheckpoint 指向原 own `_tail_0002`，不是旧 raw-lift warm。非五 I/O字段 canonical JSON逐类型相同。

原 M14/N512、p8/s32、depth12、36轮、tail tol2e−9、默认floor .05、默认原 boundary correction全部保持。prefix tol2e−9、bc1e−8、physical_bc2e−11、angular512、audit1024、固定 gauge与原自由参数保持；max_nodes6500是明确资源预算。新的物理图和结果尚不存在。

## 3. 唯一数值选择与运行身份

selector加载原 flat wrapper取得 `.m`，不自己构造第二个 BVP对象。实际运行采用

$$
u=Wy,\quad u'=Wf(x,W^{-1}u,p),\quad
b(W^{-1}u_a,W^{-1}u_b,p)=0,
$$

其中 W是已审模块实际 `power2_weights(14)` 返回的43项二幂对角。调用 `make_solver` 的代码及其返回物理 `y/yp/cubic PPoly` 的逻辑完全复用。每次只传原 `tol/bc_tol/max_nodes/fun_jac/bc_jac`。运行记录分开 weighted RMS 和原 physical RMS；不由 RMS推断新quintic metric。

原main先执行原 `install()`。新BVP callable在每次调用前后核 `_bvp.solve_newton is f6curve_domain_newton.solve_newton`、源码 SHA、实际文件、qualname及11项signature；不会自行再装一个 Newton。运行时核14项可直接取得的物理 callback，包括原对象的 `fixed_flow` 方法、`obj.flow` 选择器、保存函数、seam及临时affine solve。访问 `fixed_flow` **不调用** flow构造或RHS。原 restart/实际shared构造的调用关系由未改的原main、完整源绑定及真实响应八源支付，不冒称准备期已执行这些函数。

原lagged控制流未改：首个true DN/J，最多8次inner solve，每次finally恢复true tail，再按新cut H重求true DN/J及原 `o.bc`；最后原 `seam_audit`另调 `jacobian=True,audit=True`。谱权 callable末尾的physical BC还是当时**临时affine内层**的BC；恢复true tail后的外层检查才支付非线性BC。

新选择器不改tail八源记录，也不把自身SHA冒写成旧driver。它自己的reproduction记录真实wrapper command、传给原parser的argv、完整输入、运行callback与每次谱权记录。原source CP/summary保持原main输出格式；新的来源由独立reproduction绑定。

## 4. 初始请求、程序状态与异常

新argv显式空 `--warmup-scales`。因此原首次true请求是 `_tail_0001`。原true DN返回后、首个inner BVP开始前，selector从原调用收到的物理初猜 `y` 算

$$
H=\sigma q_g y_Z,
$$

并核已关闭首包的真实请求/原config/八源/残差/J。写独立 `-first-request-binding.json`，明确只支付首DN，outer仍未完成。准备器没有预造这个 H，也没有自行执行 restart。该小文件写成后不再修改，首包审计无需读活动trace/reproduction。

原coupled main会捕获某些异常而仍返回，所以selector不会凭函数返回或原exit惯例称成功。main返回后，使用新只读审计的 `check_outputs` 验证原全部成功门；否则写真实错误并请求程序exit2。异常未被恢复为成功，不补原失败response缺失字段。中断或I/O/资源失败可能阻止程序完整封存，仍以root真实工具观察为准。

reproduction运行更新使用小型同目录临时文件后原子replace；写失败向外抛出，不返回正常成功。首次输出用exclusive写，旧prefix/coeff/tail/summary/reproduction拒覆盖。已有stdout日志不被误当数学输出。新selector不新增任何worker退出数值门；原client.close沿原main执行。程序的 `requested_process_exit_code` 与root `actual_exit_code`是不同证据。

## 5. M14关闭审计：完整而不添加几何门

首包模式只验证新固定launch、其实际首请求绑定和同一 `_tail_0001`，不要求主进程结束。最终模式则必须先提供root观察：

```text
status = observed-process-completed
observer = /root
actual_exit_code = 真实工具值
session_id = 真实正整数会话号
tool_receipt = 真实完成回执
stem = 本次实际prefix名称或绝对路径
files = 下述真实关闭文件的path/bytes/SHA256清单
```

guard/child记录不能替代这个观察。非零退出、缺文件、原summary false/error、早期未完成CP都拒绝，不强凑成功schema。root观察需绑定launch、reproduction、原summary、最终CP、首请求绑定/首包、末次outer真包、最终seam真包和全部系数块；可同时带其它真实已闭文件。实际会话号尚未存在，准备期不预填。

最终检查保留原门：

- 原CP与summary（扣除各自存储字段/时间）一致，`solver_success=True`，physical RMS≤2e−9，配置是真M14固定g，原自由参数14、中央scale13有限；mesh完整严增、43个物理槽由全部已核SHA的finite float64 quintic块连续覆盖。
- 每个原outer row都是真inner成功；最后原scaled BC≤1e−8，其own真DN残差<2e−9，定位该真实call包。**不**强求inner节点H与随后quintic端值逐位一致。
- 最后seam必须在outer以后另有真实audit请求；按实际保存PPoly端值和同一outward桥的σ=−1核H。保留616Jac、17jets（14标量+3×14）、8audit、865×28/13×28、rawNode映射、真实八源与精确config。last history基点norm不被强制等于最终residual；chartCondition在收敛break时缺席合法。
- seam mean/nonmean一二jet、source metric/fullD等仅要求原有限诊断如实存在，没有添加新的二jet阈值。source/audit的 `actualMetric`不当作保存XYZ的连续证书。
- 每个谱权call的原参数、weighted/physical成功、round-trip、原physical残差与runtime来源保持；call数量与原成功outer数量一致。其最后physical RMS必须是原CP所存值。依旧分开inner affine BC与outer true BC。

保存PPoly求端值是只读多项式计算，不调用原flow。final审计不生成新packet，不运行任何solver，也不验证连续闭图；其成功仅表示本次有限原联解按原门完整关闭。

## 6. 准备、启动和只读审计命令

本批纯准备使用全新stem `2026-11-09-db6f-prefix-spectral-true-m14q512-01`。在仓库根：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-prepare-spectral-true-m14.py \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-true-m14q512-01
```

准备后再运行上述命令会拒绝已用stem。生成launch中的 `command` 是未来真实selector入口，不能直接把它的 `delegated_parser_argv`当成谱权命令（后者只是未改原parser的参数）。实际root启动应使用该真实command并独立记录guard/工具观察；本批未执行。

准备关闭后的安全负门检查：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-audit-spectral-true-m14.py \
  --launch topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-spectral-true-m14q512-01-launch.json \
  --mode final --check-current-gate
```

目前应真实返回2/NOT_READY，0写0solver，不构造假的正分支。
未来首包使用 `--mode first --out <新绝对审计路径>`；最终添加
`--mode final --observed-execution <root真实观察绝对路径> --out <新绝对审计路径>`。
审计输出拒覆盖，原输入/trace不改。

## 7. 1.5 GiB RLIMIT_DATA的窄评估

Linux手册的RLIMIT_DATA约束进程数据段/heap，并从Linux4.7起也可令mmap以ENOMEM失败；这是每进程资源限额，fork继承且exec保留。见 [getrlimit(2)](https://man7.org/linux/man-pages/man2/getrlimit.2.html) 的 RLIMIT_DATA 与 NOTES。它不是总RSS或整个cgroup的内存承诺。

因此可以将1.5GiB作为**允许触限失败的affine单进程pilot上限**，但没有证据保证容纳6500节点时的稀疏Jacobian/LU与临时数组峰值。触限应记资源失败，不能解释为原数学问题无解；异常可能也妨碍程序封存，真实工具观察仍不可缺。未通过证明此限额适合带Node子进程的true coupled，不能直接移植。成功时数学门仍是原门，限额不加入任何数学假设。本批未设置资源限制、未改已有guard。

## 8. 尚待实际工作

只有纯prepare/只读检查的真实退出可在本批记录；实现全文审、root实际资源安排和真实coupled计算另行进行。即使未来有限M14成功，保存XYZ/共同cut/全时几何/原g连续metric与未参与者独立重跑仍必须按既有流程取得新证据。现实现没有给出新的M14 metric、reach或README完成结论。
