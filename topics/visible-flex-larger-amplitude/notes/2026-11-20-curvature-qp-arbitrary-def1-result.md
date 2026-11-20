# v4a 从 def1 的六方向结果与记忆淘汰诊断（2026-11-20）

维护会话：`/root/geometry_path`。

## 本次实际终态

以完整空间产生的真实父点
`def1ccbded6c463a014a71a39f259c59501412d5c84afec07ce7253c9dc34f5d`
为输入，v4a 实际执行六个方向、34 个回溯 trial，程序前四方向接受、后两方向全部拒绝，正常结束。终态 bundle 为

`607732377449f07611553ebc1ad1e7f2aa20e835d3f613a3018ae56957dd6941`。

加权 Gram SSE **0.9812955395142278 → 0.3691614454297028**；全部保留和新增观察点的 max Gram **0.10186568199218482 → 0.04536288807497124**。终态重新搜索已知胞内曲率 basin 后，实际点必要乘积为 **0.9892286455516983**，因此 `final_known_point_safety_pass=false`，这里的安全线专指该次命令的 **0.98 自定数值余量**。

该值仍小于真实必要阈值 1；本结果不证明 reach 失败，更不证明无解。后继在取得独立连续局部界之后，另以明确的 0.992 数值余量继续同一数学问题。改变的只是算法余量；README 的 reach ≥ 0.03D、连续度量与其他完成要求没有改变。

## 比旧单一峰多出的实际 basin

输入 def1 的旧正主曲率峰位于 cell 821、$u\simeq0.11023$、$\phi\simeq0.63723$。本次复用了此前低角位置的种子，发现同一 def1 输入另有：
$$
u=0.49328845288451884,\qquad
\phi=0.016515079958009635,
$$
$$
\kappa_0=-8.012674660258932,\qquad
\kappa_1=-1.391599747602466.
$$
配合实际局部半径点的 $D_{\rm lb}=4.090098939220911$，必要乘积为 **0.98317896384742**。这说明只跟踪旧正分支 basin 会漏掉另一处已知几何约束。

本次任意点粗基导数实际 complex-step 检查，$d\kappa$ 相对误差 **2.911274696987841e-15**，$d(2|F|)$ 误差 **0**；加权基目标与真实算子的初始差 **3.3306690738754696e-16**。

## 六方向真实记录

表中“当时乘积”只表示该次有限、可能已淘汰旧点的记忆/局部搜索集合；不是最后独立复查的结论。

| 方向 | $\mu$ | 程序接受 $\alpha$ | 加权 SSE | max Gram | 当时乘积 | trial 数 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | .01 | 1/8 | .8396676092653425 | .092526944826413 | .9755024143841893 | 4 |
| 2 | .04 | 1/2 | .5374584140205168 | .06657790688067267 | .979947193767281 | 2 |
| 3 | .04 | 1/2 | .4218755963752003 | .05072124519423227 | .9796182280624289 | 2 |
| 4 | .04 | 1/2 | .3691614454297028 | .04536288807497124 | .9796434958375734 | 2 |
| 5 | .04 | 无 | 同前 | 同前 | 最终重新发现旧 basin | 12 |
| 6 | .4 | 无 | 同前 | 同前 | .9892286455 | 12 |

前四程序接受步的实际/二次模型下降比分别为
**0.9982551558465138、0.9982811091216691、0.9996493915517941、1.000292610276334**。
第一步因 $\alpha<1/4$ 将 $\mu$ 从 .01 乘四至 .04；接着中等步保持；两次全拒后为 .4、4。新阻尼策略按记录实际执行，没有再在小步接受后自动减半。

最终 all raw SSE **702.7803051365498**，legacy raw SSE **175.871262561833**，加权 mean **7.601510638750602e-5**，最小相对点度量行列式 **0.9692034837027235**。共同高度由 **1.9112007287168216** 变为 **1.9084457083780124**。

全 Gauss 终态的 $K_{\max}=$ **7.979175591824195**，$D_{\rm lb}=$ **4.091119389129324**，必要乘积 **0.9793127991893824**。其采样最大曲率在 stage 7266、$s=2.3453481457124297$、$\phi=\pi/2$。

最终独立重新搜索低角 basin 得：
$$
\text{cell}=821,\quad u=0.5528648040420315,\quad
\phi=0.016477979189500086,
$$
$$
K=8.059957974514708,\quad
D_{\rm lb}=4.0911240839369265,
$$
故必要乘积为 **0.9892286455516983**。$D$ 是另一实际最远点提供的下界，不是用曲率点自身半径替代全体直径。

## 已定位的具体算法缺陷及后继修复

v4a 在回溯中将被拒的大步新峰加入容量有限的 LRU 记忆。它们可能挤出本方向 QP 已使用的低角 basin；随后只有四个局部优化名额，起点也可能被其他 trial 的新峰占满。因此程序前四次接受时显示的“当前任意点乘积”没有保证旧已知 basin 仍被跟踪。最终重新读取暴露了这个遗漏，源的最终标志据实为 false。

v4b 使用新的完整源文件，不覆盖本次 v4a：

1. 两个已知 cell 821 basin 种子永久保护，始终优先进行局部极值搜索；
2. 整条 line search 锁定本方向 QP 实际使用的所有任意曲率点和半径点，被拒 trial 不能淘汰它们；
3. 原全部 Gauss 观察点仍每次完整读取，原固定网格点无需依赖 LRU 保留；
4. 每个实际接受场保存独立 NPZ，后继可以直接复读具体场；
5. 最终仍独立重读已知点，不因中途程序接受就假定连续证书成立。

v4b 的确切 source SHA 是
`f8dee5e090e9353b611598e42c135bd3855d856aafe6e2e80499478eec40933f`；
它从本次真实 6077 场继续，数值筛选线明确为 .992。该后继的实际结果另行登记，不能倒改本次 .98 运行的接受语义。

## 执行身份和完整命令

本次执行源 `scripts/resume_20261120_curvature_qp_v4a.py` SHA256：
`d3ee2f2dce84ba9401f6a993109741564c65f9317356bd2a9431b489d0a633de`。

完整 JSON `curvature-qp-arbitrary-def1-six-step.json` SHA256：
`cb239edf00f54ec0e58121987207d59c1983e391744e6f1d2648f1cff6aeb7fd`。

实际 wall time **202.6216773190008 s**；同一 scalar/mesh/core 形状字节不变，初末仿射端口三 jet 差均为零。

源码依赖都在仓库内。输入 def1 的完整重建命令见
[全Gauss完整空间首方向](2026-11-20-gauss-fullspace-projected-first-result.md)；
固定 carrier、原始闭合 warm、v3 父链和两个 witness JSON 的完整取得命令见
[任意点恢复记录](2026-11-20-curvature-qp-arbitrary-restore-result.md)。
本次两个 memory 输入正是该恢复运行实际旁生的 JSON，不储存旧曲率值；所有点均在新 def1 输入重评。

令 repo 为 checkout、topic="$repo/topics/visible-flex-larger-amplitude"、work 为仓库外重建目录。展开全部本次科学参数如下：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v4a.py" \
 --gauss-source "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
 --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
 --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
 --observed-source "$topic/scripts/resume_20261120/gauss_observed_closed_gram.py" \
 --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
 --bundle "$work/fullclosed_solver/gauss-h2-projected-first-fixed/final.npz" \
 --memory-input "$work/geometry_path/curvature-qp-arbitrary-restore-six-step-a.memory.json" \
 --local-memory-input "$work/geometry_path/curvature-qp-arbitrary-restore-six-step-a.local-memory.json" \
 --witness-input "$work/root/gauss-twelve-step-02-local-curvature.json" \
 --witness-input "$work/root/gauss-six-step-local-curvature.json" \
 --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
 --batch-source "$topic/scripts/resume_20261120_batched_closed_gram.py" \
 --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
 --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
 --out "$work/geometry_path/curvature-qp-arbitrary-def1-six-step.json" \
 --legacy-fraction .5 --memory-curvature 32 --memory-radius 4 \
 --local-curvature 12 --local-radius 2 --local-refine 4 \
 --angles 2048 --stage-block 64 --low-modes 12 \
 --centers .30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26 \
 --top-curvature 32 --top-radius 4 --reach-ratio .03 --safety .98 \
 --linear-margin .0002 --damping .01 --steps 6 --backtracks 12 \
 --repair-iterations 40000 --restoration-attempts 3 --seconds 1800
~~~

这些是有限数值记录。没有取得连续 $10^{-6}$ 度量、全域嵌入/ reach、固定握持幅度或全部相位的完成证明。

