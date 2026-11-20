# 任意点 QP 对第二批父点的恢复尝试（2026-11-20）

维护会话：`/root/geometry_path`。

## 已执行结论

新 v4a 从第二批 v3 的真实输出
`3a3f77c9363ec866c4f8e12d294d226ef2f9d7bbabfbe258819a009177c8477c`
开始，对已知胞内曲率峰作恢复。**3 个真实方向、36 个真实回溯 trial 均未同时满足原加权 Gram SSE 下降与全部已知几何点的 $0.98$ 数值余量**。进程正常结束，状态为 `restoration_failed`；没有接受任何步，也没有把未恢复状态登记为可行后继。

这是具体有限算法尝试失败，不能推出同一 $g$ 无解或本场 reach 已失败。该父点的已知实际点乘积仍小于 1，只超过人为设置的 $0.98$ 余量。按既定后继顺序，后续实际求解已经改接 fullspace 产生的 `def1ccbd…` 父点，并继续使用本次任意点检查与阻尼规则；不继续这条失败恢复分支。

## 实际固定范围

源与公式分别见：

- `scripts/resume_20261120_curvature_qp_v4a.py`；
- `notes/2026-11-20-curvature-qp-arbitrary-formulas.md`；
- 本次输入的前情见 `notes/2026-11-20-curvature-qp-gauss-twelve-step-02-result.md`。

本轮仍为原 1280 列物理粗空间、全部原固定度量/仿射端口、相同 7377 径向观察位置和正 Simpson/Gauss 混合加权 Gram 目标。没有删 Gram 行、改 core 系数或改 $g$。新增任意点只用于几何；它们直接读取真实五次 Hermite 场与完整解析 lift。

初始加权 SSE **0.34559813964253105**，全点 max Gram **0.05470303672415744**，全 Gauss 乘积 **0.9793534901423574**。真实任意点局部优化加上新的真实半径点给初始必要乘积 **0.9936553006038907**；此前使用旧采样半径下界的值是 **0.9936530964723217**。这两个数字对应不同的直径点下界，未改变同一参数化。

方向的线性安全目标为 $0.9798$，实际接受门为 $0.98$。任意曲率记忆容量 12、半径容量 2；保留原固定网格记忆 32/4；最多 4 个曲率局部极值优化及 1 个局部半径优化。所有旧记忆在当前场重新读取，两条主曲率分支均重评。

## 三次实际方向

| 方向 | $\mu$ | 约束行 / 负界行 | 半空间修复次数 | 原尺度 $\max(Qp-b)$ | 满步 SSE | 满步 Gauss 必要乘积 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.001 | 1111 / 27 | 119 | -3.3729625342759917e-10 | 0.168530022807344 | 1.8303762019363845 |
| 2 | 0.01 | 1188 / 27 | 8 | -3.7673662453552303e-10 | 0.174082970311994 | 1.208590906117587 |
| 3 | 0.1 | 1188 / 27 | 7 | -1.1503902917070485e-9 | 0.2161758205505642 | 0.9941519838796201 |

三个线性方向都实际通过了含负界的一般半空间修复。它们没有依赖零方向可行的假设。三个 QP 的双对偶均报告收敛；投影修复后的方向仅称数值可行近似方向，不称已严格证明 QP 最优。

第一方向 $\alpha=1/16$ 的 SSE 为 **0.322606695672082**，Gauss 乘积为 **0.9790256991068755**，但任意点乘积 **0.9927910573805957**，故拒绝。第二方向 $\alpha=1/4$ 的 SSE 为 **0.2759962099059539**，Gauss 乘积 **0.9791775078709992**，任意点乘积 **0.9901889541030058**，故拒绝。第三方向 $\alpha=1/4$ 的 SSE 为 **0.2980039856620884**，Gauss 乘积 **0.9788626557302859**，任意点乘积 **0.9901612859884836**，也拒绝。

更小 $\alpha$ 会留下初始未恢复的胞内峰，不能用趋近零步来恢复负界。第三满步的加权二次模型实际/预测下降比为 **0.996128070473702**，说明该次主要拒绝原因是几何，而不是 Gram 目标模型失真。每条方向全拒后按新规则将 $\mu$ 乘 10，最后为 1。指定 3 次恢复尝试用完即明确结束该分支。

## 身份、终态与复现

- 完整执行源 SHA256:
  `d3ee2f2dce84ba9401f6a993109741564c65f9317356bd2a9431b489d0a633de`。
- 输入与未接受步后的输出 bundle SHA256 相同:
  `3a3f77c9363ec866c4f8e12d294d226ef2f9d7bbabfbe258819a009177c8477c`。
- 完整结果 `curvature-qp-arbitrary-restore-six-step-a.json` SHA256:
  `823f003135f9ca98fcda69cf15142b7866f6c1b4dbf6d27f798c2618391ee1cf`。
- 实际 wall time **135.3472683309992 s**。
- 最终重新读取任意点必要乘积 **0.9936553006038796**；
  `final_known_point_safety_pass=false`。
- 仿射端口检查的三 jet 最大/RMS 差仍为零；冻结 core 字节未变。

使用 v4a 的完整依赖、原 carrier
`71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`，
输入第二批 v3 bundle 及其 `.memory.json`；两个 `--witness-input` 分别是首 Gauss 六步和第二批十二步的根会话局部曲率 JSON。参数为 `--steps 6 --seconds 1800`，其余默认含 `damping=.001, backtracks=12, restoration-attempts=3`。状态因恢复次数用尽而在第三方向后结束，并非将六步误记为已执行。

任意点导数检查实际成功：$\kappa$ 粗基 complex-step 相对误差 **3.012468273305693e-16**，直径点导数误差 **0**。完整公式 note 已记其实际点与分支。

**当前研究仍继续**。本结果既不是完整闭面解，也没有给出连续度量、全域 reach、握持幅度或全部相位的完成证明。


## 完整公开命令与依赖取得方式

以下命令给出本轮全部参数；源码均从本仓库取得，不依赖只存在于 scratch 的未发布脚本。令 repo 为已经按根 README 部分克隆并更新的 checkout，work 为仓库外新目录，topic="$repo/topics/visible-flex-larger-amplitude"。本次数值环境为 Python 3.12、NumPy 2.3.5、SciPy 1.17.0；不承诺不同 BLAS/平台的时序和 NPZ 容器元数据逐字一致。科学输入需以文内 SHA 和同一重建配方核对。

完整上游由仓库内 scripts/resume_20261120/rebuild_fullclosed.py 与 rebuild_closed_warm.py 生成；其 CLI 均为 --repo "$repo" --work "$work/fullclosed_solver"。随后按 [63维结果](2026-11-20-physical-fit-six-step-result.md)、[H2真实筛选父](2026-11-20-fullclosed-integrated-h2-reach-screen-first-result.md)、[首Gauss六步](2026-11-20-curvature-qp-gauss-six-step-result.md) 的已登记输入/命令生成 2038 父；保留每个驱动旁生的 bounded memory JSON。第二批 3a3 父由 v3 的相同依赖和下面完整参数生成：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/geometry_path/curvature-qp-gauss-six-step.npz" \
 --memory-input "$work/geometry_path/curvature-qp-gauss-six-step.memory.json" \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-gauss-twelve-step-02.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .98 \
 --damping .001 --steps 12 --backtracks 12 --seconds 1800
~~~

如果固定 Gauss carrier 尚未生成，在上述闭合 warm 与 scalar 参数重建完成后执行以下命令。这里 pulse-a5-complete-base.json.gz 的科学内容 SHA 是 826106b40f06ddece0500bd5ac7ea1a14ad4edbb9fab0664e3de46a76a76f196，fullclosed-hold-warm.json 的 SHA 是 fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692；carrier 输出由同一原标量 oracle 查询，不能替换为插值。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/read_gauss_closed_gram.py" \
 --repo "$repo" \
 --bundle "$work/fullclosed_solver/data/fullclosed-mode-damped-warm.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --scalar-input "$work/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
 --outdir "$work/recover_evidence/gauss6-current-three" \
 --order 6 --angles 2048 --stage-block 64 --carrier-only
~~~

两个初始任意 witness 由已发布根读者重建（源 SHA f376c058fd9d931ee4df6dabf68cbabc93e8e6c0b61cb15a1b2c20fd9f135456），没有把大数组上传作输入：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/read_closed_local_extremum_20261120.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-gauss-six-step.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --stage 6772 --angle 208 --angles 2048 \
 --diameter-point-lower 4.087221451205496 \
 --out "$work/root/gauss-six-step-local-curvature.json"

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/read_closed_local_extremum_20261120.py" \
 --repo "$repo" \
 --bundle "$work/geometry_path/curvature-qp-gauss-twelve-step-02.npz" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --stage 1643 --angle 5 --angles 2048 \
 --diameter-point-lower 4.09152646644 \
 --out "$work/root/gauss-twelve-step-02-local-curvature.json"
~~~

本次 v4a 恢复命令（展开所有数值默认值）为：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v4a.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/geometry_path/curvature-qp-gauss-twelve-step-02.npz" \
 --memory-input "$work/geometry_path/curvature-qp-gauss-twelve-step-02.memory.json" \
 --witness-input "$work/root/gauss-twelve-step-02-local-curvature.json" \
 --witness-input "$work/root/gauss-six-step-local-curvature.json" \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-arbitrary-restore-six-step-a.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 4 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .98 \
 --linear-margin .0002 --damping .001 --steps 6 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800
~~~

所有驱动要求新输出路径；先创建外部工作目录。上面完整公开链替代了原先只在本机命令行出现的依赖路径，后继不必访问旧 scratch 报告才能发现参数。

### 早先 v4 边界异常的单独预算

v4 原源 SHA cf5001e76dc83ddef1efb207c07d5ba476c3f569e87d155822493dc03353b4b0 曾单独启动一次；设置同样的 6 外层步、12 回溯、3 次恢复预算。它运行到首方向的真实 trial 任意点读取时，由舍入后的 $\phi=\pi/2$ 键落在闭区间外触发异常，未完成任何外层迭代、未接受任何场、未产生最终 bundle。异常运行未保存每个 trial 的完成计数或 wall time，故不虚构该部分时间/完整 trial 数。它不计入上面 v4a 的 **3 个完成方向 / 36 个完成 trial**。v4a 的修改只修复位置键边界并提前保存初态检查；原执行源未覆盖。
