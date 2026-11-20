# r17 径向扩展与一次 N8192 纯读诊断（2026-11-20）

维护会话：`/root/geometry_path`。执行源仍为已发布 v4b，未覆盖或修改其字节。

## 结论与实际边界

根据前批真实残差谱，在原 mesh 上把 11 个径向粗中心扩为 17 个，粗维 **1280 → 1964**；保留 12 个非零偶角模、原 N2048 的全部 metric 行与原加权 Gram 目标。六个方向中前五个接受，第六个全部回溯拒绝。

真实终态的加权 SSE 从 **.28981377553494947** 降到 **.2819324923967224**；全观察点 max Gram 从 **.04620001982850197** 降到 **.03569673566390885**。因此增加尾部径向自由度确实降低了当时的统一点误差，而不是只改善加权平方误差。

第六方向发现新的 prefix 窄角峰；将该点重新代入当前真实终态后，必要乘积为 **.9929444020206977**，稍超过本批 **.992** 算法余量。因此最终 `final_known_point_safety_pass=false`。这仍小于真实必要阈值 1，不能据此声称 reach 失败或无解。

随后完成一次 **N8192、零求解方向** 的全 Gauss 密角纯读，确认这个新峰，并把全部新取得的位置与旧位置合成永久重读清单。诊断没有改变原 N2048 优化目标、接受记录或输入场；输出 bundle SHA 与输入完全相同。

## 扩展空间及实际参数

在原 11 个中心之外新增：
**1.077134370991557、2.020292089293148、2.100560831276262、
2.2410311297467116、2.301232686234047、2.321299871729826**。
最后一项是原符号 lift 断点 node 894。实际 17 个中心为：

`0.3,0.6,0.83,1.0570671854957785,1.077134370991557,
1.1975374839662283,1.3580749679324564,1.5587468228902417,
1.759418677848027,1.9400233473100337,2.020292089293148,
2.100560831276262,2.140695202267819,2.2410311297467116,
2.26109831524249,2.301232686234047,2.321299871729826`。

每个中心仍有完整 Y/U/A 三 jet 列；扩大的是原场内的搜索子空间，原标量、mesh、仿射端口和所有 Gram 方程不变。当前 core 形状系数仍在这轮粗空间内冻结，允许的 core 二阶 jet 与全局平滑高度列仍保留。

输入为前批真实终态
`2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453`。
沿其末次阻尼取初始 $\mu=.32$，本轮仍是数据 GN 对角尺度步罚。真实筛选线 .992，线性目标 .9918。增加 cell 879 及其左邻 cell 878 的保护 seed，局部曲率优化预算由 4 改为 6，其余固定点与整方向锁定规则沿用 v4b。

新增粗基的任意点 complex-step 检查在 cell 878、$u=1$、
$\phi=.534121316431557$、分支 1：$d\kappa$ 相对误差
**1.0713120763856163e-15**，$d(2|F|)$ 相对误差
**1.2212453270876722e-15**。该检查实际经过新 1964 维完整粗基到原自由向量的映射。

## 六方向真实记录

| 方向 | $\mu$ | 接受 $\alpha$ | 加权 SSE | 全点 max Gram | 当时已知点乘积 |
|---:|---:|---:|---:|---:|---:|
| 1 | .32 | 1/16 | .28816397732624344 | .04400424541313841 | .9918283396731623 |
| 2 | 1.28 | 1/16 | .2872938879192163 | .04238006629165647 | .9919077309916631 |
| 3 | 5.12 | 1/2 | .28461499054411743 | .03751781492457562 | .9918496507847411 |
| 4 | 5.12 | 1/2 | .28297033046986503 | .03651401563180445 | .9918077556535324 |
| 5 | 5.12 | 1/2 | .2819324923967224 | .03569673566390885 | .9918033312819176 |
| 6 | 5.12 | 无 | 同前 | 同前 | 最终新点重读 .9929444020206977 |

前两小步使阻尼按既定规则各乘 4，后三个中等接受步保持；第六全拒后阻尼为 **51.2**。前五个实际/二次模型下降比分别为
**.9980028867216822、.9989217684402237、.9959358034212655、
.9973403472442677、.9984300087500423**。

最终 all raw SSE **666.0870383289416**，legacy raw SSE **166.6978754467937**，加权 mean **5.805353909232265e-5**；最小相对点度量行列式 **.9719780917798279**，$H=1.9067494611023124$。终态是第五个接受场，第六次没有偷偷修改它。

## 新实际窄角峰

第六次拒绝提供的 prefix 位置，在当前终态实际读取为
$$
\text{cell}=227,\quad u=0,\quad s=.5425,\quad
\phi=.667566753913,
$$
$$
(\kappa_0,\kappa_1)=(-.10213732061003133,8.08715669939561).
$$
实际局部半径点位于 cell 881、
$u=.25004610177344727$、$\phi=.47937024276653356$，给
$D_{\rm lb}=4.092680278656753$。必要乘积为 **.9929444020206977**。

这个点属于新 prefix 角盆，已有两个 cell 821 basin 并没有被淘汰。此次遗漏与 v4a 的 LRU 问题不同：永久点规则已生效，但此前的 N2048 网格及少量动态局部优化尚未取得这个窄角峰。因此本结果按实际最终 false 记录，不能倒填前五步的已知点集合。

## N8192 全 Gauss 纯读

仍用同一 v4b 源，以 `--steps 0 --angles 8192` 读取相同 7377 个径向观察位置；代表角点 2049，总计 **15,115,473** 个代表几何点。没有运行 QP 或产生求解方向，没有使用旧 N2048 grid-memory 的整数角索引；只重用带字面 $\phi$ 的 arbitrary memory。

密角 grid 最大曲率为 **8.086665386800508**，在 stage 454、
cell 227、$u=0$、$\phi=.6672816427302539$；
密角 grid $D_{\rm lb}=4.092672379383897$，乘积
**.992882162096347**。加入先前实际精细点后仍以
$K=8.08715669939561$ 和乘积 **.9929444020206977** 为最大已知见证；
密角网格没有取得比它更高的样本。这仍不是连续上界。

同一密角读出还取得邻近实际高点（共同
$\phi=.66728164273$）：
cell 226、$u=.966234757102$；cell 225、$u=.966234757102$；
cell 227、$u=.966234757102$；cell 226、$u=.380690406958$；
cell 225、$u=0$。它们覆盖这个新角盆的相邻径向位置，不把每一个相邻样本夸称为独立几何机制。

N8192 的诊断加权 SSE 为 **1.1277299695868905**，all raw 为
**2664.3481533157683**，是角总数变为四倍的读出；这些数字不能代替原 N2048 的优化目标来报告增减。相应加权 mean 为
**5.805353909232269e-5**，与原读出一致到浮点精度。
max Gram 仍为 **.03569673566390885**。

全部新实际位置、已有永久位置及原 grid 记忆已合成静态 manifest
`curvature-qp-r17-angular8192-witnesses.json`，
SHA **52723ab1e61df0bb52c23f32d5c9396e54d7ef3e1869f05bc285a45910845f60**，
9977 bytes，包含 45 个任意曲率位置与 7 个任意半径位置。后继必须在自己的当前场重读它们，不能沿用此处的曲率值。该 manifest 已交完整空间后继；在另一个真实父点 13ce 上的读出由该方向另行登记。

## 执行身份

- 完整源：`scripts/resume_20261120_curvature_qp_v4b.py`，
  SHA **f8dee5e090e9353b611598e42c135bd3855d856aafe6e2e80499478eec40933f**。
- 输入：**2b143b5fb1f68c6bb9fe46ccc748755e125629786e072d8eb42e4903e4e4d453**。
- 六方向输出：**1240c633c959a9f1df2c7a78bc25bcb6d2663f23ba8abc1a30e0b1e116a5e4d9**。
- 六方向 JSON：**96b07939f104197c74a2ca7684433f52773736579980c0c2f3c8b242a849ed4f**，
  wall time **197.86451212500106 s**。
- 密角纯读 JSON：**85ae3dda7af14c31cd604817ec1948e4fca2dada09f8d3f770573833f44c05e0**，
  wall time **8.394510011999955 s**。
- 密角纯读的输入/输出 bundle SHA 完全相同，仍为 1240；真正求解方向数为 **0**。

源、父和所有参数均明确分开，N8192 没有回填为六方向优化所用角数。
原初末仿射端口三 jet 差为零，固定 scalar/mesh/core 形状检查通过。

## 完整公开命令

上游 2b143 与其 memory 文件按
[保护点十二步记录](2026-11-20-curvature-qp-protected-992-twelve-step-result.md)
完整命令生成；原 carrier/标量与源依赖取得方法见
[恢复记录](2026-11-20-curvature-qp-arbitrary-restore-result.md)。
令 repo 为 checkout、topic="$repo/topics/visible-flex-larger-amplitude"、work 为仓库外目录。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v4b.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/geometry_path/curvature-qp-protected-992-twelve-step.npz" \
 --memory-input "$work/geometry_path/curvature-qp-protected-992-twelve-step.memory.json" \
 --local-memory-input "$work/geometry_path/curvature-qp-protected-992-twelve-step.local-memory.json" \
 --witness-input "$work/root/gauss-twelve-step-02-local-curvature.json" \
 --witness-input "$work/root/gauss-six-step-local-curvature.json" \
 --protected-point 879,0,.5341213196286112 \
 --protected-point 878,.98,.5341213196286112 \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-protected-992-r17-six-step.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 6 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .992 \
 --linear-margin .0002 --damping .32 --steps 6 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800
~~~

一次密角纯读（不带整数角索引的旧 grid memory）：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v4b.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/geometry_path/curvature-qp-protected-992-r17-six-step.npz" \
 --local-memory-input "$work/geometry_path/curvature-qp-protected-992-r17-six-step.local-memory.json" \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-r17-angular8192-read.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 6 \
 --angles 8192 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .992 \
 --linear-margin .0002 --damping .001 --steps 0 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800
~~~

局部搜索和有限密角读出都不证明连续最大值。当前主线继续在原目标上使用新物理 H² 型正步范数与永久点清单；正权 Lp/IRLS 目标若随后采用会另行声明，不回填本批固定 Jw 结果。

