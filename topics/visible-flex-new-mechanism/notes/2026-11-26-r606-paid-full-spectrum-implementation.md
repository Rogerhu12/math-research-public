# 已付 682q 的全正频率续解与 R606 实际系数观察

本包从 run **45845035304** / job **139996367531** 的自然终态继续。原十一行弱目标降低而完整 metric 略升，实际 D 的 30、40 阶峰已经超过原受约束模式。新包保留同一高度定义，直接改变求解目标；不重新计算任何旧 DtN 口，不把前一轮末 q 或最后试探混淆。

## 1. 完整输入与费用身份

输入实际 q 规范 JSON 为 15,027 bytes，SHA-256 `a752de58142fb20a6c0f8c2a3bcd54523eeef29ad9a4715d2c3cdb0f4c1c4fe1`，682 个参数、H=0.5188901259915873、amplitude=1e-5、global accepted iteration=180、actual next damping=1e-14。它完整嵌入新 request 的 stdin 字段；没有单独 checkpoint 文件。

原 stdout 为 1,580,253 bytes / SHA-256 `71dc64aaa126f6bd62321e8703410fd6b761820def3154703ffd1d2bb9558266`；原 FINAL 为 57,128 bytes / SHA-256 `639fd09d6ffa2763b1d5796907c4efb7bb507348612d6b75456095382d75108f`。来源是公开 commit `4adf950498047e76e4a17b0f81f93d8c4f6b5b0a`，不是私有计算结果。

输入保留原 265q、67 knots、全部十一模有限口及来源；两层更早成本与本次来源的 1426.507060097 s 和所有分层 counters 分开保存。本包重新构造必要 dense、connector、core、H 积分的费用全部新增计入，不假装先前未存的 dense 插值已经免费可用。

新完整 stdin 输入为 31,425 bytes / SHA-256 `14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee`。其中实际 q 保持原 JSON 字节，不经过浮点重新序列化；三个新增口的 13 jets、alpha、z_alpha、display log 和有限 M 身份直接从原终态读入。

## 2. 同一高度，完整正频率残差

高度模型直接继承已发布 R602 主源，完整保留：

- 原 pre-tanh 265q、所有原 bulk knots、固定 post-tanh 四模强迫；
- 固定 canonical 512 的同一个均值函数及其 f/fr/frr 导数；
- 2/4/.../22 的十一种真实有限尾模；
- R602 依赖于整个 q 的从属核心高度修正（频率至 44）；
- 全部六个空间 jets 和对应参数导数，完整 mean turning 与实际重构几何。

新目标为
$$
c_j(r)=2\langle (A_t/M)\cos(j\theta)\rangle_N,
\qquad j=2,4,\ldots,48.
$$
每个半径保留全部 24 行。角行权全部为 1，不再按 1/j² 压小高频；径向权仍为非均匀梯形质量归一后的平方根，最后统一除 amplitude。因此新的 merit 与旧十一行 merit 不具有直接数值可比性；是否改善以新目标的真下降、完整物理读出和末细网共同判断。

每次 trial 仍评价未截断的 At、M、implicit turning 与完整高度，随后才作上述有限投影；没有将原 D 改成低阶多项式、将高模设置为零或增加独立 e 控制。均值由同一 turning 恒等式决定。有限 48 阶目标本身仍不证明无限角方程已解。

主源中的 Jac 逐项复用已付核心链，仅把输出分配改为 nr×24，并让同一投影矩阵含 2cos(jθ)。所有空间、隐式 e、M、At、核心修正与 H 导数保持完整；681 个高度方向和一个 H 方向仍为原 682 列。新增行是同一逐点导数的线性读取，不调用旧方向、restriction 或 physics gate 复跑。

原十一模质量块观察仍明确用原十一种 cos 基，而不是悄悄用 24 个输出频率替代未知空间。a 失号时仍不硬除 a，继续完整残差求解并报告实际块秩。

H 列的核心导数没有省略：原 gain 的 H 系数 B(r)=S((r−.37)/(.48−.37))S((.61−r)/(.61−.48)) 在整个 r≥.61 开领准确为零，背景高度的对应积分也为零；原 core_scale/alpha 不含 H。因此 R602 的 core_k、P、P_r、eR 和从属 cc 对 q[0] 的导数确为零，H 的 dw/dwr 与背景高度链仍保留。

## 3. 18/20/22 模不重做 Riccati

10/12/14/16 直接复用已发布 paid-mouthed evaluator。新类 PaidFactoredFlat 仅重建原 18/20/22 的必要密场：

1. 从各自原 alpha17 的 `[1,z_alpha]` 开始，保留原 M=25、rho26=0 和原浮点初值。
2. 保留旧共同 minimum radius；如果 alpha17 在其外侧，只重新计算已有数学定义要求的短向内传递。
3. 采用原分段 ODE 和每段对数归一，保留剥离 r^(j²) 因子的原 13 jets 公式。
4. display log 固定为原输出值，不重新选择归一；connector 的输入始终是原完整 13 mouth jets。
5. 重新构造的 mouth 与原 mouth 之差只作明确误差观察，不作为重跑旧 gate；core A/C 差也如实输出。

新类中没有 inner_slope 调用。必要 dense/core 数值重建仍可能产生未认证浮点误差，因此文字只称保持同一数学/有限输入定义，不谎称浮点表逐位相同。

## 4. R606 在实际系数上的观察

独立 helper 从已准备的同一场提取两个有限 cosine 系数组：

- V：原四模 pre-tanh 高度的真实 0/1/2 径向系数；
- L：所有新增列、post-tanh 强迫四模、从属核心至 44 阶的真实 0/1/2 系数。

同频贡献先加总，随后才取带 exp(jρ) 的绝对值和。没有用 FFT 网格最大值冒充 Wiener 范数，也没有把不同来源的消去分开浪费。尤其
$$
(Wf_r)_r
$$
使用 Wvrr+W'vr 和 WLrr+W'Lr 的系数组合，再应用 tanh 链式范数；核心近端不会人为引入两个独立发散上界。

helper 在原完整末细网全部 r 上使用固定
$$
\rho\in\{.025,.05,.075,.10,.15,.20,.25,.30,.40,.50,.60\}.
$$
依 R606 逐项计算六 jets 上界、M 正下界、N 与 shift 的复范数；以已有同点 turning 浮点残差和解析 alias 界构造一个 h=0.01(ehat-sρ) 的括区间候选。只有全部明确正性及 d≤h 条件通过，才记录该半径的条件上界。

对正频率2至48，加入 R606 的 Fourier alias 和隐式根位移项；48 后的真正形式 Wiener 尾使用 Gρ exp(-50ρ)。随后按原证明传播到 metric。每个 r 可选预先声明候选中最小的条件上界；输出每个 rho 的覆盖失败数、最坏位置，以及最坏最佳 rho 的完整小型分项收据。没有全部 r 通过时明确输出未覆盖数和首批位置。

**这些计算把当前重构的浮点径向系数当作精确输入，尚未加入有限 DtN/ODE/舍入/core integral 的误差包围。** 输出明确标为条件观察；它不是连续径向证书、全曲面 metric 证书、额外接受 gate 或旧观察复跑。真正连续径向覆盖须另对系数及两阶 jets 作区间包围。新 scope 在实际当前候选上支付这些数值项，避免只继续堆积抽象公式。

## 5. 接受、clock 和末态

继续全 SVD，保全部奇异方向；参数列尺度、函数步长限制和实际/预测下降逻辑保留。只有完整 24 行目标的实际下降超过舍入量级且实际/预测比值大于 .01 才接受；旧的十一行下降不能替它通过。

本次最多 60 个新迭代（180至239），clock 2400 s；预留180 s给末完整细网/位置/R606读出。每个真正接受态保留完整 q、damping、实际 merit、核心、质量块和物理观察。正在评价的 trial 明列为 pending，和 actual retained q 分开。发生 clock 时不会把试探或仅线性预测当作完成态，分层计数与未完成积分的未知额外工作也保留。

细网仍为原全部 r ×512角；原域内四阶中心/单侧实际位置 h 与 h/2 读出不变，所有原 r 保留。完整 D 角谱读到96，core直接端式读出，不挪到R-epsilon。达成采样 metric 门也不自动授予连续曲率/reach或README完成。

## 6. 冻结文件与运行限制

| 文件 | bytes | SHA-256 |
| --- | ---: | --- |
| scripts/r606_paid_full_spectrum_height_20261126.py | 29932 | e13c3709ef8b6c648ff251b24636ff03646b6d0d1cba8f5f8177a98d73e8f541 |
| scripts/r606_weighted_majorant_observation_20261126.py | 9131 | 2042623d08678b3656dae3c9efd23bb682d95c48bfc1b59e8e953ca313176556 |
| .github/workflows/visible-r606-paid-full-spectrum-20261126.yml | 3401 | 1b1df281b24850917dc1cdff4d22ddcbcd1353e1f5375d9b42a197a40b5fd4bd |
| computations/request-r606-paid-full-spectrum-20261126.json | 39097 | 9794af5e625139644d54e95562d75a433d496f292e951538dd9e8c0035b136c6 |

request 绑定主源、helper、完整既有依赖与 workflow，共15项。单个公开 job，45min timeout，与原 height scope 共用串行 concurrency group。runner 先实际 pull 双仓规则、核已读 README/QUEUE，移除凭据后执行科学。只 stdout，不产生 raw table、artifact、Release、Git写入或跨run缓存。没有本地科学执行；本地仅源码纸核、AST/JSON/哈希与原日志身份读取。
