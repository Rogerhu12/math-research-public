# 真材料 Haar 固定目标的完整幅度求解与实际 Actions 接口

**状态：完整可执行源码已形成并只做静态源级核验；尚无本新固定目标的求解返回。** 准确角矩 `1d12` 与冻结接口 `c5a` 已由根代理发布于 `e95fea50651bcfe32aad52826caa8a692c2ff741`，首角矩批已接实际 7ebb 父。本文的完整求解器、粗预条件器、启动器、实际读取器及其纯源派生器是独立的后继文件；实际stage71完整moment carrier已返回，见配套实际note；target identity和新final SHA只在真实返回后填写。

本接口保持 R671 的实际物理表示、全部原自由量、完整相对 Gram 行、H² 母范数、几何不等式、两支 held-amplitude 约束和永久位置。它明示选择一个新的准确 Haar 度量。旧 physical-mean 或固定标量目标下的 $\Phi$ 不能作为这个新目标的下降证据。

## 1. 完整来源与断线后恢复

| 新文件 | 字节数 | SHA-256 |
|---|---:|---|
| `derive_frozen_haar_amplitude_solver.py` | 34420 | `af03a9beb98df0d0500f58891b2e6c3c2e7530724d3cfe047d858f8228153f12` |
| `frozen_material_haar_coarse_moments.py` | 22458 | `ee172fd58ec6ad589bb9cc8f7e9980eded83cc9d051bec7329d07bf474bbc80f` |
| `fullclosed_frozen_haar_amplitude_qp.py` | 76558 | `b70bdcd7c9b0e0a8cf101d9a59b229d048359318f8b5289e3513fc96ce79d61f` |
| `launch_frozen_haar_amplitude_actions.py` | 24756 | `991e7d4a4c0f8141f34844e07d2a76b26496ba1d5a74867f25042c5fb47d8cf1` |
| `read_frozen_haar_amplitude_report.py` | 14628 | `d8d48df3597068ca76c9be71e2cd6a585ccb91b2a27b68f5dc29e4ae08e5e91c` |

完整派生输入均为已经发布的真实源码：

- `fullclosed_frozen_metric_amplitude_qp.py`：`859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b`；
- `frozen_metric_coarse_moments.py`：`a531818d75040ff571ad1249eecb3c18f7341284d1cdd86d2032b0f8f4ef9f63`；
- `launch_frozen_metric_amplitude_actions.py`：`d73ec177827fd420153dd95ceafbc3601eeb0af6e3b0c89b7b2d372c021e41e1`；
- `read_frozen_amplitude_report.py`：`f119d9960a0e6de381b6a7ab93581a1dd785db258a6b7cd2a72546ea62c979af`。

派生器先逐字核这四个输入，再进行显式完整 AST 派生。数值主体 b70 与粗算法 ee172 已精确再生为断线前相同字节；当时未发布的启动器、读取器和完整派生器没有冒称原字节恢复，而从完整 d73e/f119 重建，使用表中的新 SHA。旧未发布的 d816/a8ec/912f 不作为本次实际来源。

固定目标接口必须是 `frozen_material_haar_metric.py` 的 c5a 完整字节，准确角矩必须是 `material_haar_moments.py` 的 1d12 完整字节。当前完整求解器只收原 R671 factory `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`、$\lambda=1$、keep-q 模型；没有把 deep 4ae 模型重新标成 2e，也没有偷用有限 physical mean 的 wrapper。深谷固定 $g_n$ 分支继续使用它自己的完整源。

## 2. 准确目标与完整导数

先冻结实际完整场 $F_*$ 及其 $\rho_*=\Theta_*'>0$，定义

$$
g_*=E_*(s)\,ds^2+C_*(s)\,d\theta^2,\qquad
E_*=\frac1{2\pi}\int\rho_*|F_{*,s}|^2\,d\phi,\qquad
C_*=\frac1{2\pi}\int\frac{|F_{*,\phi}|^2}{\rho_*}\,d\phi.
$$

完整角矩 $P,Q,\ell,b$ 及其误差、全部连续径向共享 quintic 和准确 $f,h,k$ 的定义见配套两份完整说明：

- `2026-11-26-true-material-Haar-angular-moment-input.md`；
- `2026-11-26-frozen-true-material-Haar-target-interface.md`。

目标身份绑定实际冻结 bundle、全部五项输入、完整 canonical/angular definition、全部源、物理域和闭面 cap recipe。工作角矩的 $Q,p$ 和 carrier SHA 不定义目标；合法地收紧同一准确积分的盒不会改 $g_*$。当前 $q,H$、非固定 core、$M,N$ 及准确嵌套径向网格可以改变，但不能以这些当前量重做目标均值。

原 full operator 返回

$$
r_0=(G_{ss}-1,\ G_{s\theta}/a,\ G_{\theta\theta}/a^2-1).
$$

对当前径向点置 $A=E_*(s)$、$D=C_*(s)/a(s)^2$，固定目标的完整相对残差为

$$
r_*=\left((1+r_{0,1})/A-1,\ r_{0,2}/\sqrt{AD},\
(1+r_{0,3})/D-1\right).
$$

因此完整导数是

$$
J_* = S_*J_0,\qquad J_*^*=J_0^*S_*,
\qquad
S_*=\operatorname{diag}(A^{-1},(AD)^{-1/2},D^{-1}).
$$

`FrozenHaarOperator` 在当前全部观察点求同一冻结目标，保留所有原行及完整 quarter orbit multiplicity，固定正缩放数组设为 readonly。它没有移动均值投影，也不删除三个残差分量的平均行。所有原 core/$\rho$、$q,H$ 的导数仍来自原完整 J/J*。冻结目标在新点由实际冻结共享 quintic 和准确 scalar/lift 公式求值，不插值旧 mean 数组。

数值工作使用准确角矩合法盒的中点矩阵和普通浮点径向求值。矩阵的普通浮点二次型不自动成为向外区间，因此源码明确保留 `numeric_matrix_and_radial_arithmetic_certified=false`。连续目标、完整尾与归一化界仍由严格同场消费者负责。

## 3. 原完整 QP、母范数、幅度与全部均值行

b70 主方向循环及每一次潜在可接受试点的全场真实读取，与完整 859c 的对应 AST 相同。以下十二个物理/坐标/筛选函数保留同一 AST：

`point_geometry`、`load_witnesses`、`coarse_lift`、`coarse_transpose`、`lift`、`transpose`、`objective_value`、`curvature_filter`、`geometry`、`add_actual_location`、`remember_amplitude`、`compact_geometry`。

完整原自由空间未删减。DoubleIntegrated/physical-height/coarse 坐标和 H² 母范数保持原定义；真实原空间 cotangent 仍经过完整 $T^*$。目标谱 Hessian 使用新的完整固定目标残差和 $J_*$。p=4、epsilon=.001、scale=.05、centered 常数减法只定义数值谱目标；不能把 centered 与 uncentered $\Phi$ 混算。

粗 K00 源 ee172 保留 a531 完整数值收缩循环和实际预条件器构造函数的 AST。改变的是明确 wrapper 来源 guard 与准确 Haar 身份元数据。`full_angles=None` 是准确积分目标的语义；工作 moment $Q$ 单独记录。粗 Gram 中全部固定目标均值行保留，原完整 v5/v3 的外层预条件器和 damping 语义不变。

所有原几何行继续存在。额外幅度行使用已纠正的 v2 两支原空间导数和真值筛，固定预算为

$$
\bar D=4.2,\quad B=\bar D-.002=4.198,\quad
\bar L=.9,\quad H_{\min}=1.01.
$$

每个真实试点重读全部当前网格和永久任意位置；距离约束同时保留 $\sigma=\pm1$，$p=(0,r_0,0)$ 中 $r_0=1+\sum c_j$ 使用当前所有自由 core 变化，不能固定旧 witness。原曲率乘直径必要筛照常完整运行。选定少数地点加入工作 QP 不删除任何永久真筛地点；cap 与 height 两条标量行始终存在。

这套预算是同场 whole-image 见证的选定充分保护，不是所有可能大幅度路径的必要条件。有限网格和全部已知位置通过仍不是连续 $D/L/K$、embedding 或 reach 证书。后继实际候选发生变化后，旧场 first 的数值不能跨场继承。

## 4. 实际父、永久位置和旧目标 $\Phi$ 的边界

第一条 Haar 分支选择 run `45762076394/1` 的实际 stage 63/65/66：

| 真实对象 | SHA-256 |
|---|---|
| 实际 final bundle | `7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b` |
| 实际完整 report | `749fc0a31661e111f2621619b45da25bf25fe0a53a6feca348c831aa1e221821` |
| own reference carrier | `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8` |
| 实际 own first | `449a672f86253f14e8866d98464a8a0704b4dc0d2edb5f6bf89bc1dcf96fb364` |

旧场为 M=160、J=923、N=2048、eta-start-node=885、$\lambda=1$。其旧目标完整方向实际有接受；相对 Gram 最大值与 $\Phi$ 是不同统计，不能声称最大误差改善，更不能把旧 $\Phi$ 当成 Haar $\Phi$。其实际末 damping=.005；本次新目标的初始 damping=.01 是明确新选择，不冒称继续旧值。

首启动器要求实际 parent report 已完成且 final SHA 与所给 bundle 相同，并要求该 bundle 正是 frozen manifest 的实际冻结 member。若以后继续这个目标，父报告必须明确携带同一准确 Haar target identity。另一个旧固定目标即便用了同一物理表示，也不能默认为本目标的后继。

永久位置继续调用原完整 history collector，保留全部真实祖先、试点、活动行和末场位置；R676 transfer 分支的 `transfer_positions` AST 原样保持，只读取实际已精确重映射的当前坐标数组，绝不从 provenance 重新走出旧 cell 坐标。新目标不会丢掉原永久位置。

初次进入 Haar 不传 `--comparison-parent-report`。所有初始残差、谱 $\Phi$、完整几何和幅度由新目标下的实际初始场重新读取。之后若比较保存的父 $\Phi$，b70 还要求同一准确 Haar identity、同一实际 working moment SHA、同一 p/epsilon/scale 和准确保留的父观察测度。若工作 moments 收紧而改变普通浮点中点，旧保存 $\Phi$ 不能直接相减；必须在新的工作矩阵下重新读父量。准确数学目标不因此变化。

## 5. 四个实际入口与完整参数

`geometry_ready_Haar_7ebb_chain.json` 给出四步完整 controller argv、所有小 summary 字段和输出。它只预留未来科学 SHA 为 null，不能把参数计划写成已完成返回。

1. 准确 moments：Q=8192、p=12、请求 1e-14、900 秒 admission、最多 4096 个新完整 quarter orbits，runner journal 续接。每个批次只在自然完整 orbit 后退出；若 partial，使用同 bundle/core/Q/p/source/run/journal 和新的小 report 路径继续。完整合法盒但请求精度未达仍如实报告实际宽度，没有额外 fixture 门。
2. 真正 complete 后才调用 c5a，消费实际 7ebb report/bundle 与实际 moment carrier，冻结全部连续目标。
3. 对真实冻结目标运行完整固定 Haar 求解，首批 1 个方向 × 256 个 QP advances，参数如下。
4. 对实际完成的新报告调用独立读取器，只核真实源和报告，不重跑 F/J。

完整首求解命令；其中 REPO/WORK 是当前公开 Actions 的实际路径：

```sh
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_frozen_haar_amplitude_actions.py" \
  --repo "$REPO" --work "$WORK" \
  --bundle "$WORK/mean-metric-design-amplitude-separated-SOC-v2-first/final.npz" \
  --parent-report "$WORK/mean-metric-design-amplitude-separated-SOC-v2-first/report.json" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --manifest "$WORK/mean-metric-design-amplitude-protected-first/report.json" \
  --eta-start-node 885 --lambda-value 1 --angles 2048 --stage-block 64 \
  --frozen-target-manifest "$WORK/haar-7ebb-fixed-target/frozen-target.json" \
  --target-moments "$WORK/haar-7ebb-fixed-target/moments.json" \
  --marked-diameter-budget 4.2 --witness-lower-budget .9 --amplitude-height-floor 1.01 \
  --amplitude-top-radius 2 --amplitude-top-distance 4 --amplitude-active-band .025 \
  --amplitude-budget-evidence "$WORK/mean-metric-design-amplitude-separated-SOC-v2-first-geometry/first.json" \
  --coarse-preconditioner coarse --coarse-moment-stage-block 8 \
  --spectral-p 4 --spectral-epsilon .001 --spectral-scale .05 \
  --damping .01 --directions 1 --maxiter 256 --active-rows 192 \
  --qp-atol 0 --qp-rtol 1e-6 --reach-safety-factor .992 --active-band .025 \
  --target 5e-7 --outdir "$WORK/frozen-true-Haar-7ebb-amplitude-p4-first"
```

新目标下原全部变量、原均值行和幅度约束保持。`--target 5e-7` 只是一条明确数值阈值，不代替课题要求的完整连续精度或求解容差极限。初批有限 advances 耗尽不是 stationary、收敛或完成证据。

创建出来的 command plan 同时 SHA 绑定当前所有源、全部 frozen input/source、实际工作 moments、真实 parent report 和完整位置 manifest。旧源绝对路径消失时只允许同字节的 repo-relative 恢复或显式 override。模板命令准备若失败，会先保留真实 stdout/stderr 再报错，不用报错遮蔽具体失败原因。

## 6. 实际报告读取与小公开返回

求解报告 schema 为 `complete-fixed-true-material-Haar-with-held-amplitude-budgets-v1`。实际读取 schema 为 `complete-fixed-true-material-Haar-held-amplitude-actual-summary-v1`。它们不冒用 finite-physical-mean 的报告绑定器。

读取器保留 f119 的每个真实方向、完整真线筛接受判定、原/新增工作行数和同测度谱统计检查。另逐项核 b70/c5a/ee172 与原 amplitude v2/v5 源，核 exact-Haar contract、工作 moment SHA/Q、真实 physical 2e/$\lambda=1$，并检查 initial、final、current 和每个 finite trial 都是同一冻结 target identity。通过读取器只表示归属及实际报告内部一致，不额外宣称连续证书。

公开小 summary 至少给出：

- 实际 parent/final/report/source commit 与 target/angular/moment identity；
- initial/final 完整最大相对 Gram、$\Phi$、centered $\Phi$ 及同测度差；
- 实际方向数、接受数、QP 状态及预算、末 damping；
- 原自由量和全部 Gram 行数；
- 选定幅度预算、完整真筛覆盖与末 gmax；
- 必要 reach-product 真筛与全部永久位置计数；
- 各 continuous/refinement/reach/topic-complete 旗标的真实 false 状态。

raw bundle、角矩向量/journal、稠密工作行、solver 大报告只留 runner scratch。公开的是必要源、完整推导、实际 command/source identity 和小 summary；不为可重算数据创建仓库 raw 备份。

## 7. 静态核验的精确边界与后继责任

已经完成的本地工作只有：完整源 byte hash、AST/compile、字面 dict key/keyword 无重复、完整派生输入 SHA、上述保留算法 AST 等同，以及 parser 的纯源提取。新 driver 和 launcher 相比原完整版本没有删除 CLI，只各增加 `--target-moments` 和 `--target-source-overrides`；ready 首求解 74 个 argv token 已通过纯 parser 检查。没有在本地读候选数组、计算 moments、求 F/J、跑 QP 或做科学 fixture。

实际stage71完整moments已返回，请求1e-14尚未达到且有效包围保留；详见[实际note](2026-11-26-actual-complete-material-Haar-moments.md)。尚未产生：冻结 manifest/target identity、完整 Haar 方向与最终 bundle、固定同 $g_*$ 的网格/M/N 精化下降和求解容差极限、完整连续误差、完整同场 K/reach 或课题完成证据。后续根据真实返回继续方向、工作积分精度和固定目标精化，不以这份源码说明代替研究完成。

严格连续消费者仍须对 current/frozen 的准确共同分割支付全部径向/角向/高模及准确无限尾误差。在同 scalar/$\lambda,\eta,$物理宽度的条件下，只能抵消准确共同的 $f_s^2,f^2$；含 $h_sH$ 的项须保留当前与 frozen 的差。只有实际新候选接近所需精度后才投入昂贵的完整 metric/K 上界，避免在已经明显失败的百分之一场重算同类失败证书。
