# 完整 Cartesian 流式分支：第三次失盘后的文本恢复与实际有限核验

**可信度：严格的有限代数接口加浮点数值核验。没有完整 Cauchy 输入上的 Cartesian 接受步，也没有连续、reach 或闭族完成证书。**

2026-11-26 11:19 UTC 附近执行环境失联，未返回的 cold push 不能视为成功。随后终端恢复，根会话实际确认原 scratch 目录不存在。本文记录这次恢复的真实字节身份，不能把新恢复文件借成旧版本的验证结果。正式运行、全场新基线、LM 接受与观察必须由同一个实际 runner 另行给出。

## 1. 恢复身份

下列路径均相对于本课题。四个 Python 文件分别放在 scripts，配方放在 ci-requests。代码和小配方可公开；数组、完整状态、训练和观察缓存均只放在 Git 外。

| 文件 | 当前字节数 | 当前 SHA-256 | 与失盘前关系 |
|---|---:|---|---|
| scripts/6a65-cartesian-complete-stream.py | 18018 | b8cfd595b535cc33d47e2c0bc3e2b8d6a79c8163a235415115ca42c53416e4a9 | 全文重建的新身份；不继承旧 stream 的哈希或执行回执 |
| scripts/6a65-cartesian-stream-fixture.py | 6481 | 4013823713889d3fe4c0fcdd05f7f5a622f28c7ac7f30083b856292ba3a107a5 | 新验证脚本；本次实际执行 |
| scripts/6a65-cartesian-independent-experiment.py | 23539 | b546504c1cf7c8b46dccd6f86f94def8250528ebfaf037737ce74b81d7a7fe1d | 从独立保留全文恢复，逐字 SHA 与旧 v1 相等 |
| scripts/6a65-cartesian-independent-experiment-v2.py | 25969 | 8959a77106e563174c8233b369472dd0fa3e79aa2ff850e560c88e3a4099b418 | 从已保存 v1 加已核具体差异恢复，逐字 SHA 与旧 v2 相等 |
| ci-requests/6a65-cartesian-independent-recipe-20261126.json | 1935 | 0794c4d61e4307cde3de4a84154d4e27311f96a4f7f7aa48d74d6fa0724841a7 | 显式新恢复配方，不借旧配方 94f618… 的身份 |

完整 13 行点算子没有变化，依赖已公开脚本 scripts/6a65-cartesian-complete-point-operator.py，字节 SHA-256 为 cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f。实际源 adapter 也由其拥有者逐字恢复，6a65-cartesian-oracle-background.py 的字节 SHA 仍为 c57d4d21f85f949f869a2c7d1d7c4e50ede7be948ce541f1b676d589ae4045a5。

失盘前 stream 的 SHA 是 20f5fa17c17d355cd1e0e2539bfa6cbbc01e24b84992df9a0e5e72a8f6c2069f；本次没有声称把那份全文逐字找回。旧 stream fixture 数值仅属于旧文件，不作为本次新文件的回执。

## 2. 保留的数学问题与完整参数空间

冻结真实原 Cauchy checkpoint 的全部 rho、振幅、cut 高度和原角 primitive。目标是它定义的同一个固定物理度量 $ds^2+a(s)^2du^2$。背景所有六个位置 jets 由常驻 Node oracle 直接取实际位置供应器及真实 R205 尾段；不做 Fourier 或 Hermite 拟合。新校正 W 只支撑在实际 [c,S]，积分和观察域则保留完整 [0,S+.48] 到 r=.32 真平 cuff。

径向采用物理 s 上 clamped quintic B-spline，完整 J+6 列删除首末各三列，故 W、Ws、Wss 在两端严格为零；所有含 u 导数的端点 jets 也同时为零。J80 对应 81 个径向 span。两个水平分量各保留全部奇数频率的独立 cos/sin，竖直分量保留常数及全部偶数频率的独立 cos/sin。M32 给 97 个角通道、7760 个参数，不额外加镜面对称限制。

每一点完整保留 3 个放大的 full-Gram 残差、3 个 R191 实际曲率谱残差和 7 个 R219 几何残差。完整 JVP 与 JT 经实际六jets链式求导。归一角求和权重 1/N 与每个物理径向权重都显式进入点算子，不混入其他面积因子。所有原几何参数、metricTau 和 curvatureTau 从实际父输入读取。

预条件器仅是可逆坐标变换。对角频率 k，采用

$$
P_k=\beta_1K_1+(\beta_0+\beta_1 k^2)M+\beta_2(K_2+2k^2K_1+k^4M).
$$

beta0=.01、beta1=1、beta2=.001，M/K1/K2 分别是同物理径向样本的 B、Bs、Bss Gram。五次局部支撑给精确 bandwidth 5；代码检查带外没有非零项，再做带状 Cholesky。JVP 用 $L^{-T}$，JT 用 $L^{-1}$，没有构造稠密参数 normal、逆矩阵或删去物理行。

新恢复配方固定训练 N512、每个真实物理分段与新基结点并集上的 G2；曲率和几何的 nodeShare 沿用实际输入。完整背景还含非有限带宽成分，N>8M 只避免纯校正四次项的已知角别名，不能据此声称连续积分精确。观察使用 N1024 和每段二等分，独立记录有限峰值。

## 3. 本次真实有限核验

在恢复后的终端实际运行：

    python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-cartesian-stream-fixture.py --output /tmp/visible-flex-6a65e705/solver-work/cartesian-restored-stream-fixture01-report.json

该进程真实 OS exit 0；程序内计时 0.32438990200171247 秒。小报告字节 SHA-256 为 da8983928d34390c05b39540b8114af42ca4a5e76a45f24d3001f1d2d730cd89。本次只做这次新有限验证，没有重复完整科学求解。

| 核验 | 实际结果 |
|---|---|
| 小型完整线性化 | J7/M8，175 列，19 个径向点 × N64 × 13 行 = 15808 行 |
| 三阶角接口的双线性伴随 | 导数阶 0/1/2 相对差 6.418512668977942e-16 / 1.1485163869317907e-16 / 3.7080754825662613e-16 |
| 完整预条件 J/JT 双线性值 | -44.59079012679438 与 -44.59079012679448 |
| 完整 J/JT 相对差 | 2.230863878472501e-15 |
| point cache 开/关 JVP、JT 最大差 | 均为 0 |
| 全部残差平方和与完整 nonlinear observer 差 | 0 |
| 中心有限差分 epsilon=1e-5 / 1e-6 / 1e-7 | 相对误差 4.738208195566269e-7 / 4.7382103331061e-9 / 6.16879245497887e-11 |
| J80/M32 真 7760 列两端六jets | 最大绝对值 0 |
| 同一完整 7760 列 proper-half-turn 六jets | 最大差 0 |

另实际执行 v2 的 --help 返回 OS exit 0，验证新 stream、已公开点算子及恢复的实际源 adapter 可以共同导入。上述小 fixture 的背景是脚本内明确给定的解析曲面，不是当前 CI 的实际 checkpoint，没有产生 Cauchy/Cartesian 历史接受步。

## 4. 真实实验入口与接受规则

入口固定使用 v2：

    python scripts/6a65-cartesian-independent-experiment-v2.py \
      --scripts ABS_TOPIC_SCRIPTS \
      --candidate ACTUAL_CANDIDATE \
      --source ACTUAL_CAUCHY_INITIAL_OR_CHECKPOINT \
      --observer ACTUALLY_EXECUTED_MATCHING_CAUCHY_OBSERVER \
      --prefix FRESH_GIT_EXTERNAL_PREFIX \
      --recipe ci-requests/6a65-cartesian-independent-recipe-20261126.json \
      --source-epoch ACTUAL_40_HEX_COMMIT \
      --run-id ACTUAL_RUN_ID

生产入口拒绝 interface probe；验证实际源文件、参数向量、候选、源码 epoch 与原 observer 的字节绑定。新模型 baseline 必须完整实际求值，之后才执行一个完整 LM 尝试。配方的 LM lambda=.001，最多三个 damping 值、各最多 80 次 LSMR；线搜索 alpha=1,.5,.25,.125，Armijo 系数 1e-4。原曲率放大 tau 不为触发新分支而更改。

LSMR 迭代上限本身不构成接受。只有方向有限、全矩阵梯度斜率严格负、未阻尼预测下降严格正，并且真实完整 13 行目标严格下降且满足 Armijo，才记本模型一个接受。若不接受，保留零校正和 ownAcceptedSteps=0，并照常密观察；原 Cauchy 文件和计数始终不改。

完整状态分别写 prefix-initial.json、prefix-state.json、prefix-observer.json、prefix-report.json；它们只留在同 runner 临时区。只有小标量报告和哈希可由父控制器发布。程序不读凭据、不 push、不改原 Cauchy 的计数或模型 schema。

## 5. v2 的内禀曲率诊断

v2 在两个真实缓存上分别取 $K_g(s)=-a_{ss}(s)/a(s)$，记录最大绝对值、符号、物理 s、实际 a/as/ass 与输入状态 SHA。该诊断不改任何残差、方程、预条件器或 LM 门槛。

若未来得到真正等距曲面且 reach≥.097，则主曲率绝对值不超过 1/.097，Gauss 方程给必要条件 $|K_g|\le1/.097^2$。采样超过这个必要值是检查当前固定 g 的线索；只有有限浮点样本不能自动提升为连续严格排除。代码明确 finiteSamplingOnly=true、continuousBound=false、isAcceptanceGate=false。

冷新输入与优化过 rho 的当前 CI 输入必须各自实际测量；不能把冷输入的 K_g 移借为当前状态的数值。本文截至发布准备时两者均没有由本入口给出完整实际 Cartesian baseline 或接受。
