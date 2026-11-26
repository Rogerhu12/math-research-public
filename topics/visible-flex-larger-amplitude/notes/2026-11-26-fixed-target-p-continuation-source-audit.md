# 固定 g 的 p4→p8 备选：现有完整入口、基线和阻尼来源审查

会话：Astra-larger-e4e2a2bf-20261126；范围：纯源阅读与符号推导。没有本地科学求值、数组读取、fixture、新求解源或新队列。本稿把已有 R664/R687 公式用于当前入口，不申领新定理编号。

## 当前选择

公开运行 45762076394/1 的实际阶段 67/68 已返回固定深谷目标两次 256 步。固定 profile 为 `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d`。从实际 `b788c32879aa5ff5ff3d5f2ed81b92205b54fc0da61a1a2b84ace8345a3f22eb` 到 `8a0509fd3a09ef01aa0cecb98b21f4c06ce0ed56a9ddd9398f1d4bef7ec0d326`，同 p4/epsilon=.001/scale=.05 的 max 从 `0.01426432970666691` 降到 `0.012896410280312631`，Phi 从 `0.00032735551888962906` 降到 `0.00019751382939144711`。两个方向均经完整真读接受 SOC 全步，分别在第 5、第 7 轮。返回 mu=`0.0025`。报告 SHA256 为 `a8cf736f6386a3cd08afb616e7ca1cd151565f64d8aa0519e15415cf7202710b`；公开紧凑证据见 [实际阶段 65–68](2026-11-26-public-actions-45762076394-1-part-007.md)。

因此目前优先同层、同固定 g、同 p4 继续，不把尚在下降的峰值说成停滞。两个 QP 仍为 iteration_limit，Pg/tol 分别 `30298.56046007907`、`27614.98298356061`，末活动面仅 12、16 advances。fine 接口已经备妥，但这两步没有证明粗层已充分求解。下文是遇到实际“平均损失下降而峰值停滞”时的备选操作边界，不是现在排 p8 的指令。

## 完整来源

| 角色 | 完整 SHA256 |
|---|---|
| deep 全体 driver | `329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90` |
| deep launcher | `ca4048343c7ddccfd1662e7c3099d699a4715fe5c101c9cde3be024d0a76c7cc` |
| deep 完整体 deriver | `d80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec` |
| deep 当前 coarse moments | `dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395` |
| Haar 全体 driver | `b70bdcd7c9b0e0a8cf101d9a59b229d048359318f8b5289e3513fc96ce79d61f` |
| Haar launcher | `991e7d4a4c0f8141f34844e07d2a76b26496ba1d5a74867f25042c5fb47d8cf1` |
| Haar 当前 coarse moments | `ee172fd58ec6ad589bb9cc8f7e9980eded83cc9d051bec7329d07bf474bbc80f` |
| R664 原谱残差 Hessian | `29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4` |
| 原谱统计 | `e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91` |
| R687 centered 统计 | `5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01` |

上述六个 driver/launcher/coarse 文件的本地纯字节 SHA 已复核，未改任何锁源。

## deep：现有入口允许显式新损失，禁止跨单位自动继承 mu

`launch_deep_amplitude_separation_soc.py` 现有互斥参数组要求 `--damping <值>` 或 `--damping-from-parent` 二选一。后一分支逐一核真实 completed parent、实际 final bundle、selected scalar key，以及父 `final_statistics.spectral` 的 p/epsilon/scale 与本次参数完全相同；因此 p4 父搭配 `--spectral-p 8 --damping-from-parent` 会被明确拒绝。

显式 `--spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 --damping <新的显式正有限值>` 没有被该继承规则禁止。`complete_current_positions` 仍完整核 d3 或 329e 父来源、同固定 profile/物理 context、真实 bundle/carrier/nodes/scalar、原 amplitude budgets，并保全部永久位置；没有把选 p8 当成改 g。d80 `verify_fixed_target` 比较每份实际报告内部 initial/final 的 p/epsilon/scale/normalization，没有要求一个新独立预算必须与其父采用相同 p。

329e 从当前实际 bundle 重新计算 `problem.residual(x)`，再用当前 `spectral_parameters` 写 `report.initial`。它没有从父报告读取旧 merit；每个 direction 的 `old_merit` 都来自本次新统计。每次新建 R664 `NativeLinearization` 和当前 coarse Gram，并按新的 p/epsilon/scale 外因子建立 A 和 virtual RHS。dcfa 直接用当前 bridge 的参数和 Hessian blocks，且记录它们；没有复用旧 p4 Gram。原完整物理 J/J*、H² 母范数、所有原 C 及幅度行、同父多轮 SOC 和完整真筛保持。

ca40 没有 `--comparison-parent-report` 接口，因此没有一个隐含旧 p4 common-measure 比较需要关闭。若做本次单一 p-continuation，保持同 M/J/N、同观察载体和全部位置，以便将“损失改变”与“网格改变”分开说明。入口本身允许 dyadic angle supergrid；那将同时改变观察测度，不能再把旧 raw Phi 当成本次基线。

## Haar：同一精确目标下可换 p，但旧 p4 comparison 必须省略

991e 的 `--damping` 本来就是必需的显式值，没有自动从父读 mu 的开关。`--spectral-p 8` 通过偶数 p>=2 的参数约束。target manifest/精确 Haar target identity、冻结成员及 working moments 身份与损失指数是独立对象；改 p 不应另做 freeze 或改同一 g。

首次新 Haar target 仍须采用实际冻结成员，禁止旧目标 comparison。对已有同 Haar target 父的 p4→p8 后继，必须省略 `--comparison-parent-report` 与 `--comparison-parent-carrier` 两项。b70 的 comparison 分支不仅核同精确 target 和同 working-moment 文件，还逐一核父 p/epsilon/scale 与本次相同；旧 p4 comparison 配 p8 会按预期拒绝。不能伪改父谱字段让它通过。

b70 无 comparison 时仍从 `problem._state(x)` 完整读取新 initial residual/statistics，之后的 merit 只用本次参数。ee172 用当前 bridge.blocks 与当前 `k/(scale^2*C0)` 重新装配 K00；固定 target diagonal scaling、全部原 mean rows、完整物理 J/H²/C 和幅度真筛不变。Haar 的 b70 仍是其已发表的 ray 全局化，不能因换 p 冒称继承 deep 的多轮 SOC。

Haar 若同时升级 working moments，即使数学 target identity 相同，数值 target 载体也不同；现 comparison 源要求同 working carrier，不能跨载体复用旧 Phi。单一 p 后继应继续同一个实际 working carrier。p8 初始 max 可以与同目标、同网格、同 working carrier 的父 max 比较；p8 Phi 只能与本次重新读取的 p8 initial 比较。

## mu 的符号尺度：p 改变并非乘一个常数

设残差矩阵 E 的特征值为 t，p=2k，epsilon=e>0，scale=c>0。当前谱目标是正权归一化和

$$
\Phi_p=\sum_j\omega_j\operatorname{tr}\bigl((E_j^2+e^2I)/c^2\bigr)^k,
\qquad \sum_j\omega_j=1.
$$

R687 的 centered 值是同一目标减常数 `2(e/c)^p`，不改梯度、Hessian 或 mu 的单位。本次 p4 与 p8 的 centered 值仍是两个不同函数，不能相减作为下降量。

R664 给出 Frobenius 特征方向上的半 Hessian 权

$$
a_p(t)=\frac{k}{c^{2k}}(e^2+t^2)^{k-2}\bigl(e^2+(2k-1)t^2\bigr).
$$

所以

$$
a_4(t)=\frac{2(e^2+3t^2)}{c^4},\qquad
a_8(t)=\frac{4(e^2+t^2)^2(e^2+7t^2)}{c^8},
$$

$$
\frac{a_8(t)}{a_4(t)}=
\frac{2(e^2+t^2)^2(e^2+7t^2)}{c^4(e^2+3t^2)}.
$$

这个比值依赖 t，因此不存在一个全局 mu 倍率能令 p8 QP 与 p4 QP 等价。非对角残差特征方向还使用同一正导数的 divided difference；也不会由一个普遍常数统一缩放。原 QP 为 `.5||Az+v||² + .5 mu²||z||²`，A、v、coarse Gram 全随新残差权改变。只复制 p4 mu 的数值可以成为一个显式的新参数选择，但不能称为同单位自动继承、保持原相对阻尼或保持原 QP。

若之后确有必要并由实际报告选定参考幅度 t*=当前同目标同网格 max，可声明一个“仅在该标量特征方向匹配相对阻尼”的政策

$$
\mu_8=\mu_4\sqrt{a_8(t_*)/a_4(t_*)}.
$$

这只校准一个参考曲率尺度，不是完整 Hessian 等价或步长保证。t*、父 mu 与来源必须来自当时真实报告；该公式的数值求值和实际参数选择仍在公开 Actions。本次没有计算任何新数值 mu，也没有为它新增入口。

另一个不同情形是保持 p/epsilon/E/测度，只把 c 改成 c'。这时确有统一倍率 `alpha=(c/c')^p`：Phi、梯度和残差 Hessian 同乘 alpha，A/v 同乘 sqrt(alpha)。有限 QP 要保持同一数学极小点，须同时 `mu'=sqrt(alpha) mu`；若连数值停止条件也声称同尺度，则绝对梯度 tolerance 必须乘 alpha，rtol 不变。当前 driver 的固定 mu 下限 `1e-8` 并不自动按这个倍率变换，所以不能由前述单步等价推出所有外迭代的逐字相同行为。

## p8 的取舍与接续责任

写 x=|t|/e，半 Hessian 的峰谷权比为

$$
\frac{a_4(t)}{a_4(0)}=1+3x^2,\qquad
\frac{a_8(t)}{a_8(0)}=(1+x^2)^2(1+7x^2).
$$

p8 更强调峰值，也可能放大目前尚未收敛的内层谱跨度；这是从已证公式得到的取舍，不能当成 p8 已更快或已更准确。保全部正权和原均值行，不以截断低残差点改善条件数。新的 R664 块与 coarse 预条件必须随新 p 重建，真 Phi/curvature/amplitude 和永久位置仍逐 trial 全读。

若未来选择 p8，应固定一份真实合格父和同一 g，显式声明新损失及新 mu 来源，用现有完整 launcher 新输出目录运行，并在 report.initial 重新建立该损失基线。先看真实新损失下降、同 g 的 max、QP/活动面与全部真筛；不要跨 Phi 宣称改善，也不要把 finite 试步或 iteration_limit 当成同 g 精化收敛。当前 67/68 已有 max 与 Phi 同降，故没有必要在这次返回后立即切 p 或增加 fine 网格。
