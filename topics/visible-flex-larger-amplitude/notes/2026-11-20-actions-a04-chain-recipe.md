# 公开 Actions 的 a04 完整父链与下一四方向配方（2026-11-20）

维护会话：`/root/geometry_path`；根会话统一发布与启动 Actions。

## 本条实际完成的工作

新增完整轻量编排源
`scripts/resume_20261120/rebuild_a04_chain.py`，以及一个完整纯位置参数文件
`scripts/resume_20261120/a04_historical_location_seeds.json`。
本条只做源码编写、既有报告读取、位置元数据提取、语法和命令参数检查。
**没有在本地启动新的科学计算，也没有得到新的 a04 数值结果。**
后续科学子进程必须在本仓库公开 GitHub Actions 内执行；脚本同时检查
`GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。
本地 `--print-only` 只读取文件身份并打印命令计划，不导入科学模块、不执行科学子进程。

此前 `reproduce_and_solve.py` 已能完整恢复 warm，但不包含 af89 之后的父链。
本编排调用该既刊入口，不复制或替换其数学生成器；不传 `--implementation`，
因此不会额外执行无关的旧首 fullLM 尝试。

## 一条可执行入口

令 `repo` 为本仓库 checkout，`work` 为仓库外新工作目录。原始数组和完整过程报告
全部写入 `work`，没有把 NPZ、逐 trial 数组或证书缓存塞入 Git。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 \
python "$repo/topics/visible-flex-larger-amplitude/scripts/resume_20261120/rebuild_a04_chain.py" \
  --repo "$repo" --work "$work" --stop-after a04
```

直接连做新的下一四方向时，唯一变化是 `--stop-after continue`。也可以在同一
已经完成的工作目录第二次使用这个选项；脚本只复用**该次工作目录**已经完成且所有
输出/父输入 SHA 仍一致的阶段，接着运行新的四方向。不能凭旧历史 hash 伪造一个阶段已完成。

Git checkout 须能读取历史接受 `.99` 的真实对象：

```sh
git -C "$repo" fetch --filter=blob:none --depth=1 origin \
  60321451c058c6a51da58c37ae5ec6f2d1145f74
```

恢复器随后读取该提交中的
`notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz`，保留它原本的
`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`
字节校验。其后的每个实际场都记录本轮身份。旧恢复器对 Hold 输入及 mode-damped
父文件已经显式记录 historical/reproduced 身份重绑；本编排没有绕过旧原始数据的校验。

完整参数可在任何环境以 `--print-only` 审阅；该计划逐项展开科学源、源文件 SHA、
所有依赖路径、父路径、输出路径和本次参数。编排中 `operator`、`gauss-source`、
`base-source`、`coarse-source`、`norm-source` 各自使用其正确公开角色，不再混用接口。

## 真正的场依赖链

下表中的名称只是**历史配方标签**。不同硬件、浮点库或新的实际回溯分支可能生成
新的 hash 和不同指标，必须登记为新实际父，不能沿用表中历史身份的数值证书。

| 标签 | 实际父输入 | 版本与完整方向预算 | 起始阻尼/目标 |
|---|---|---|---|
| warm | 历史真实 `.99` 接受前缀 | `.991,.992`，M112 精化，`.993,.995`，共同 jet pulse、assembly、Hold、mode damping | 既刊恢复入口逐段原参数 |
| af89 | 本轮 warm | 63 列物理 v1，6 方向、8 回溯、600 s | raw Frobenius SSE，$mu=.001$ |
| e8 | 本轮 af89 | 完整 DoubleIntegrated +1280 粗列，1 方向、LSMR256 | 原节点/中点目标，$mu=.005$，数值筛选 .98 |
| 2038 | 本轮 e8 | 全观察 v3，1280 列、6 方向 | 新正径向加权 $J_w$，$mu=.001$，筛选 .98 |
| def1 | 本轮 2038 | 完整全 Gauss 切向方向，LSMR256、16 活动行 | $J_w$，$mu=.0025$，筛选 .98 |
| 6077 | 本轮 def1 | 任意点 v4a，6 方向，负界恢复上限3 | $J_w$，$mu=.01$，筛选 .98 |
| v4b 十二步 | 本轮 6077 | 1280 列，12 方向、永久双 basin 与整方向固定点 | $J_w$，$mu=.04$，筛选 .992 |
| 13ce | **本轮 v4b 的 accepted-1** | 完整物理高度/永久位置方向，LSMR256、64 活动行 | $J_w$，$mu=.0025$，筛选 .992 |
| e19 | 本轮 13ce | v5 物理 H² 范数，1964 列、1 方向 | $J_w$，$mu=.0025$ |
| 0241 | 本轮 e19 | 同 v5，1964 列、6 方向 | $J_w$，$mu=.0025$ |
| 8d | 本轮 0241 | v6 正谱 p8，1964 列、6 方向 | 真 $Phi$，relative damping .001 |
| ca367 | 本轮 8d | 同 v6，4 方向 | 真 $Phi$，$mu=.015440957971131026$ |
| 077 | 本轮 ca367 | v7 精确残差 E-Hessian，1964 列、4 方向 | 同一真 $Phi$，$mu=.015440957971131026$ |
| bede | 本轮 077 | 同 v7，2534 列、6 方向 | 同一真 $Phi$，$mu=.0019301197463913783$ |
| 35f | 本轮 bede | 同 v7，2534 列、3 方向恢复 | 同一真 $Phi$，$mu=.004825299365978445$ |
| a04 | 本轮 35f | 同 v7，2534 列、6 方向 | 同一真 $Phi$，$mu=.012063248414946114$ |

所有当前 coarse 命令仍用 M160 的完整场、2048 全圆角点/513 正重数代表、7377 径向
观察位置、`.5 Simpson + .5 Gauss6`。每次 coarse 真实接受保全部原场/原 $g$/端口，
但当次搜索子空间的 core 形状系数固定；完整空间的 e8、def1、13ce 没有将其冻结。
谱目标前的 raw 与 $J_w$、谱目标后的真 $Phi$ 与 $J_w$ 分别记录，不互相相减冒充进步。

原三个径向中心列表在源码逐字给出。特别地，e8 完整方向第三/第九请求中心是
`.8275` / `1.9600905328058122`；def1、13ce 是 `.8300000000000001` /
`1.9400233473100337`。不能因为其余中心相同就替换为另一次运行的列表。
R17 是有已记录实际残差依据的 17 中心，R22 再加 `.99,.995,1.0,1.02,1.097`。
原场和观察网格均不因增加搜索中心而改变。

除表中 warm、af89、完整空间驱动的专门预算外，coarse 源都明确
`backtracks=12, seconds=1800, repair_iterations=40000, restoration_attempts=3`。
任意点版本的线性余量为 `.0002`；.992 只是一条算法筛选线，不是课题阈值，也不是 reach 证书。

本轮重建使用历史命令的字面起始阻尼；跨硬件不声称每次目标、回溯或最终阻尼仍同旧结果。
若某一新版场恢复失败，报告原样保留 false/失败值，不能为了走完标签链而改写接受语义。

## 历史旁支的纯位置输入

父场和方向不能省略；只为固定位置输入而存在的旧失败旁支，可以用完整、可审查的
纯位置参数替代重新计算。根会话明确采用了这一方式。新增完整 JSON
逐项保留来源路径、旧文件 SHA、上游报告/清单 SHA、公开 note 和提取方法。
没有残差、曲率、半径、主方向、旧符号或安全判定值。

| 输入责任 | 保留的纯位置参数 | 来源与处理 |
|---|---|---|
| 2038 初始 grid memory | 32 κ /4 radius，原顺序/容量/计数 | 原 c71 旧阶段记忆；实际新 Gauss 读出重新计算全部值 |
| 6077 初始记忆 | 失败恢复留下的 grid32/4、任意点12/2 | 原 3a3 恢复报告与两个 memory SHA；不重跑未改变父场的失败方向 |
| 6077、v4b 的已知两个 basin | cell821 的低角/正分支两个精确位置 | 原两个根局部读出 JSON 的最终位置；不带原曲率值 |
| 13ce 初始永久位置 | 57 κ /13 radius | 已公开的 accepted-1 小清单加已付出的历史 prefix/双 basin/半径位置 |
| e19、0241 的 r17 责任 | r17 的 grid32/4、任意点12/2、5个保护种子，另加固定45κ/7radius和完整历史grid位置 | 原2b/r17/N8192分支对应的完整清单，只保位置；没有用 r17 失败场作父 |
| 可选下一四方向 | 1107 κ /180 radius /18保护种子的历史完整并集 | 含完整空间最终局部读出的新增位置；同时合并**本轮**a04完整位置导出，新旧位置逐个实际重读 |

对数组身份重新绑定前，编排严格校验本轮 node report 的923个精确符号节点定义与
历史同一清单一致，并校验原固定 scalar profile、analytic origin、cut/ramp/pulse
定义参数一致。它不把派生的浮点 end/height/radius 载体值混作定义参数。
这些检查通过后，才把纯位置输入的 carrier 身份显式重绑到**本轮实际 carrier SHA**；
历史/本轮两个身份以及验证依据一起写入 `binding-manifest.json`。
若精确符号网格或 scalar 定义不同，脚本明确停止，不能把旧索引解释成新位置。

上述替换保留历史输入参数；它不声称在新硬件上重新运行被省略的失败支线一定产生相同位置。
后续每个真接受/拒绝 trial 的新位置由本轮报告重新导出，并用于下一方向。

## 可选的新四方向

`--stop-after continue` 先生成 a04 全历史位置清单，再并历史完整空间位置责任。
下一四方向使用 v7、R22/2534列、相同真 p8 $Phi$、相同物理 H² 范数和 .992 数值筛选；
起始阻尼取**本轮 a04 报告的实际 `final_damping`**。

另外永久保护两个已经付出的实际位置：

- cell821，$u=.557082202638, phi=.01647875344$；
- cell113，$u=.17836061753131477, phi=.11275230115214022$。

完整空间最新增量还永久保护 cell113 的原新 Gauss 点和 cell230 的原新 Gauss 点；
它的全部7个曲率位置/1个半径位置均已作纯位置合并。
`local_refine=21` 可容纳该历史并集与上述两个指定点合并后的19个保护种子及动态名额。
命令仍保 grid32/4、moving-local12/2、top32/4、12次真实回溯、负界修复40000和恢复上限3。
没有为拼接代码先启动新的本地四方向；它是明确的下一 Actions 计算预算。
若本轮 a04 的 `final_known_point_safety_pass` 不是 true，编排不直接冒称可行父进入该可选段。

## 状态、日志与可恢复性

`work/status.json` 使用 schema `public-actions-a04-status-v1`：

- 稳定字段 `stage`、`state`（`running/completed/failed`）、`completed`；
- 每个完成条目的 `name, seconds, returncode, scope`；
- 实际父、输出 bundle、完整 report 的路径及 SHA；
- 若报告提供，抽取真 `Phi`、`max_gram`、`weighted_sse`、`raw_sse`、`product`、最终 finite flag/damping；
- `historical_bundle_sha256` 只是对照，`historical_bytes_match` 如实记录；不继承历史证书。

每次状态更新用临时文件原子替换，并打印一行紧凑 JSON，根发布器可监看并逐条登记。
完整命令、所有源身份和阶段表写入 `work/recipe-manifest.json`；完整 stdout/stderr 在
`work/recipe-logs/`。本编排不含 git commit/push/API逻辑。

重启时，只复用本轮 journal 已完成、源/seed字节、所有输出字节及父输入字节均一致的
阶段。没有 journal 身份的旧输出不会被自动覆盖。中途失败的科学日志保留，须据实检查后
决定下一次实际预算，不会把异常当作旧阶段成功。

## 预算与已经支付的程序检查

读取既有各阶段 `seconds/elapsed_seconds` 后，主父链旧科学运行时间合计
**3736.639817604秒，即62.2773302934分钟**，已含 .99→.995 的五段 BVP、warm生成、
carrier、三个完整空间方向和所有列出的 coarse 方向。不含没有改变主父而已替换成纯位置
输入的失败旁支，也不含新四方向。这个量级支持以6小时公开 Actions job 作为本次初始
预算；不同 runner 的速度和非线性轨迹可能改变耗时，不把估计当完成保证。

本条实际只做了：Python AST 语法检查；源码角色 SHA/文件存在检查；完整 `--print-only`
计划（a04为25阶段，含continue为28阶段）；对27条外部命令以源码 AST 核对必需参数与
允许开关，全部通过。没有重跑旧数值探针、旧连续证书或任何新的科学方向。

## 输出约定与完成范围

当前 a04 本轮输出为
`work/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz`；
其 `-witnesses.json` 是本轮新生成的全历史位置输入。0241、node report、原 pulse scalar、
Gauss carrier 继续使用既有目录布局，后处理入口可以直接消费，无须扫描仓库寻找 raw。

这些输出只是后续科学计算的实际父与可复现输入。统一 $10^{-6}$ 度量、全域 reach、
全部相位、握持幅度和最终固定 $g$ 精化是否成立，仍由本轮实际结果与对应严格证明判断。
结束一个 materialization job 不是结束课题。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
