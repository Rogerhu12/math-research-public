# 精确圆弧 core 的最小数值接口、有限秩诊断与未收敛尝试

状态：**数值/启发式；没有达到本题完成标准。** 精确 core 的定义、给定方向的参数导数和参考项公式独立于 Fourier 截断。下列成功均只表示有限 Galerkin BVP 的 collocation 达标；全图未投影残差及同 g 精化没有通过。

## 1. 最小接口

`plateau_core.py` 给出三重对称严格凸平面曲线。以法向角 $\phi$ 为参数，曲率半径为 $\rho=h+h''$，周长固定 $2\pi$。在指定圆弧上 $\rho=R$；在补弧上加紧支撑、每周期积分为零的基函数。空间曲线由 $\Gamma_\phi=\rho(-\sin\phi,\cos\phi)$ 和三重对称闭合常数定义，材料角 $u$ 是弧长。所有浮点评估均从这些定义积分获得；没有把有限 Fourier 曲线叫作精确圆弧。

外支撑变化取 $h\mapsto h+c_j f'_j$，$f_j$ 为补弧中的紧支撑函数。固定材料 $u$ 的正确变分为
$$\partial_{c_j}\Gamma\big|_u=f'_j n+\bigl(f_j(0)+f_j''(0)-f_j\bigr)t,$$
不是固定 $\phi$ 的导数。数值中心差分检查的误差约 $10^{-9}$。材料曲率半径导数按
$$\rho_u=\rho_\phi/\rho,\qquad \rho_{uu}=(\rho_{\phi\phi}\rho-\rho_\phi^2)/\rho^3$$
直接解析计算；没有用 FFT 微分代替定义。

`exact_core_lift.py` 在原 Frenet 参考项中保留精确 core 与其被截断部分，有限 Fourier 仅表示其余修正。入口几何两 jet 因定义而完整保留，内部未投影残差仍须检查。`osculating_core_reference.py` 进一步采用
$$X_{\rm ref,xy}=\Gamma+(a-1)\rho n,\qquad z_s=\sqrt{1-a'^2\rho^2}.$$
在常 $\rho$ 的圆弧上它等于 R5 的显式局部旋转片；全角一般并不等距。去掉参考项的角平均高度后沿用原平均高度恢复。`plateau_patch_audit.py` 单独评估实际入口与局部显式旋转片的两 jet 差。

## 2. 已执行计算

共同旧设计的 profile 来源是 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2` 的 `2026-11-09-db6f-prefix-flat-v17v18-profile.json`，其中 Delta=0.07251477503053651。它不是 R114 的非线性冻结值 0.07254443456654512。线性 m3 根重求得 0.07251477503410932。原物理端口是同一提交中的 weighted-K6 port96-cusp1024。

| 计算 | 有限求解状态 | 实际意义 |
|---|---|---|
| 纯投影、q=.01、宽.4、M4、lambda=.6 | collocation 成功 | 未截断 core 的二阶入口投影误差 2.49，不能用于 R5 |
| 简单 exact lift、q=.01、宽.4、M4、lambda=1 | 758 节点，残差 1.11e-6，BC 1.75e-13 | 全图 metric_l1=.0080471，Frenet 缺陷 .0767632；只得到一个低阶投影根 |
| 同一 Delta=.03894228094576847，M4→M6 fixed-g | 首轮需要的节点超 cap 2000；残差 .43264，BC .05848 | 未取得同 g 加密收敛，不是“不存在”证据 |
| osculating 参考、q=.01、宽.4、M4、lambda=.1 | 407 节点，残差 1.99e-6，BC 2.74e-17 | metric_l1=.0082805；尚没有精确圆弧（lambda<1） |
| 同一参考 lambda=.3 | 1212 节点后超 cap 1600，残差 7.94 | 此次尝试没有收敛 |
| osculating lambda=.1、M4→M6 fixed-g | 出现正根域异常，最小 margin 报 -0.0029393 | 此次启动失败，未完成精化 |
| q=.08、宽1、M4，历史 flat17 warm seed、原 adaptive chart | 1365 节点后超 cap 2400，残差 .013488、BC 1.54e-5 | lambda=0 就未完成校正，未进入精确平顶同伦 |

旧 r=.6 的 q18 M24 作业运行约 37 分钟仍只有 start 日志，因新的 r=.30 分支更有价值被主动取消；取消不算数学失败。与本笔记最后两项不同，它没有留下求解器失败终态。

最后一次会话环境中断后，上表两项旧任务的工具 session 已不可用，但各自 JSON 与日志中已先保存了明确的求解器终态；没有把 unknown session 当作失败证据。

## 3. 两种“秩”不能混写

补弧基函数的低阶 Fourier moment 矩阵只是线性 core 控制矩阵。随保护圆弧加宽、高模数增加，它迅速病态：例如法向宽1.2，列归一化条件数在 M4 约619、M8 约7.59e6、M16 约7.24e13。这不是完整非线性 BVP 的秩。

另外用 `collocation_terminal_rank.py` 在一个已求出的有限根上组装完整 collocation Jacobian，对每个终端 BC 的单位扰动解线性系统，并取参数响应矩阵的逆作为有限 Schur 矩阵。简单 exact-lift lambda=1、M4 fixed-g 根对应 9858 个未知量，列归一化条件数约4.27e8；线性代数方程残差约8.9e-16。osculating lambda=.1、M4 的对应条件数约9.66e5。

这些只是按现有浮点/有限差分参数 Jacobian 得到的数值秩和病态诊断。最小奇异值未给区间下界，不能将它们宣布为无限维满秩定理；尤其不能把 LU 的小残差当作参数导数的精确性证明。

## 4. 可复现闭包与命令

`plateau_recovery_manifest.json` 逐文件固定来源 commit、路径、字节数、SHA-256，合计28个文件、646543字节。使用本题既有 `recover_prefix.py`，从 partial clone 定点恢复到仓库外 scratch：

```bash
python recover_prefix.py --repo REPO --dest SCRATCH --manifest plateau_recovery_manifest.json --endpoints
python core_diagnostics.py --out SCRATCH/core-diagnostics.json
python plateau_prefix.py --source-topic SCRATCH/bundle/topics/visible-flexible-closed-surface --profile SCRATCH/plateau_inputs/flat17-profile.json --port-file SCRATCH/plateau_inputs/flat17-port96.json --out SCRATCH/lift-narrow-q01-m4 --q .01 --modes 4 --halfwidth .2 --transition .1 --lambdas 0 .01 .03 .1 .3 .6 1 --exact-lift
```

成功的低阶根输出物理样条 checkpoint 与 summary。取最后记录的 Delta 写成新的参数 JSON，然后使用 `--fixed --profile FROZEN --restart CHECKPOINT --modes 6` 精化；这一步不能偷偷重求 Delta。`--rank` 添加完整有限 Schur 诊断。`--osculating` 改用第二种参考项，当前要求物理角 chart。

历史 q08 warm seed 的恢复/转换入口为 `restore_flat17_warm.py`：必须明确传入 `--source-topic`、`--input`、`--profile`、`--port-file`、`--out`、`--chart-out`。其输出只是当前求解器的初始猜测，不能称作新 plateau 解。`--constant-chart` 可复现早先的常值 chart 尝试；默认保留历史 adaptive chart。

脚本依赖 Python 3、NumPy、SciPy；本地为 Python3.12.14、NumPy2.3.5、SciPy1.17.0。所有 checkpoint、大数组和再生 summary 均留 scratch，不提交。

## 5. 后续方向已改变

R8的正曲率环带条件引理 给出已证的严格正 K 环带条件引理，并明确保留 K=0 入口的缺口。下一份负曲率追加段的独立profile 已生成一个在 H 后耗尽已知特征保护角窗、同时缩短背景高度的新 metric。当前继续的是这条新 profile 的真实 Frenet 端口求解，不再无目的给旧 flat17 平顶同伦升模。
