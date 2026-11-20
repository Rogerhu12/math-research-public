# m3：q=.006 实际 max_nodes 返回、保场重采样与 Hermite 残差定位

维护会话：Astra-held10-1b6d88ec-20261120。

## 1. 实际返回与保留源

同 runner 的命令 held10-H1-regenerate-20261120-01 在首个 q=.006
返回失败：原 tol=1e-6、max_nodes=6000，实际节点 4675、
RMS=1.173712930211244e-6，status=1，外层 returncode=2。
尚无这次场的完整 metric 通过结果，也没有新真尾。不能把接近旧
成功参数当作本次成功。

原记录与场保留在 runner：

    $WORK/height-path-00-q0.0060000/run.json
    $WORK/height-path-00-q0.0060000/inner-00.npz

run.json SHA256：

    281883f93e260d4f100a497f32d7d9129ddb2397e049f48ec2aac280f4f8f577

raw SHA256：

    a7abf71cf17dcab0324594f6107d2ce94946e4ae1a5566742d09335bcb446754

该次公开的小记录可在提交 e98fa2c6728cc9c9e498d34baae0633eeeb82350
的 ci/live-material-result.json 读取。实际 p[0] 为
.00001454550957463652，物理 c2 为 .000004538900758262289；
它们接近前次成功初始化值，不消除本次 RMS 未过门事实。

## 2. 已执行的一次只读诊断

新增并已实际 exit 0 的脚本：

    scripts/resume_m3/diagnose_and_remesh_prefix_raw.py

源码 SHA256：

    187a0b97555968dc9a24d7924e81d0cbba738d903287b75a12ff8ce52032423f

调用为：

    python -u "$TOPIC/scripts/resume_m3/diagnose_and_remesh_prefix_raw.py" \
      --source-run "$WORK/height-path-00-q0.0060000/run.json" \
      --nodes 401 --outdir "$WORK/q006-rms-remesh-01"

模型由 actual_m3_metric_model.py 按原 run 的 profile/chart/q/warp/
core 复建；这里只需要原 RHS，H1 的末端替代不改变该 RHS。
使用 SciPy 1.17.0 原 collocation_fun、estimate_rms_residuals、
create_spline，没有修改求解器或任何验收阈值。

实际诊断：

- 重算原 collocation RMS 与已存 RMS 最大差 4.235164736271502e-22。
- 直接用已存 cubic 的导数减原 F 所算 RMS 最大值
  1.173712930210802e-6，也与已存值一致。
- 4096 个区间超过原 tol。全网格 h_min 与 h_median 都约为
  1.271565755207e-8。
- 最坏区间索引 901，t 在
  [.0008447138468424479, .0008447265625]，
  物理 s 中点 .0011493064930041524。
- 该点 a=1.0000001003178314、a'=.00033926600367535425、
  a''=.8426101719308919，归一化 midpoint collocation 残差
  L2 为 1.6071726197689955e-6。
- eps*(|Y_left|+|Y_right|)/h/(1+|F_mid|) 的 L2 尺度估计
  3.669167154575234e-8。它只是启发尺度，既不是向外舍入误差界，
  也不能据此排除或确认全部浮点条件数效应。
- cubic 在原节点的最大重建误差 5.293955920339377e-23。

所以这里确实存在原规则下的未消除残差；并非打印了旧 RMS，
也不是仅有 solver 标志的假失败。目前不能把它直接称作舍入底。

## 3. Hermite 形状给出的数学定位

对小区间，若端点导数使用原 F，而节点间平均斜率仍有未修正的
近常量差 delta，则 Hermite cubic 的主残差形状是

    r(xi)=6 xi(1-xi) delta,  0<=xi<=1.

故中点残差为 3 delta/2，区间 RMS 为 sqrt(6/5)|delta|，
两者之比为 sqrt(8/15)。

实际最坏区间给出

    RMS / midpoint_norm = .7302967433454323,
    sqrt(8/15)          = .7302967433402214,

相对差约 7.14e-12。这支持当前残差主要是未纠正的 collocation
斜率缺陷，而非通常随进一步细分迅速衰减的高阶插值尾。该判断
针对观测到的残差形状；没有把有限精度的近常量假设升级为严格
全区间方程证书，也尚未观察到最终网格的 no_step 确证。

原 SciPy 外层在 1*tol<RMS<100*tol 时二分该区间，再以原 cubic
重采样作为下一网格初值。如果内层 Newton 仍未修改这个平均
斜率差，单独继续二分就不会消除其归一化 RMS。因此此次观察
不给增加 max_nodes 或放宽 tol 的理由。

## 4. 原 domainNewton 的退出逻辑

已读原 frozen source：

    repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py

它要求每分量

    |cr_i| < h*(tol/30)*(1+|F_mid,i|)

才走正常内层残差停止。M=8 时 n=25；由
r_mid=1.5*cr/h，此条件必推出归一化 midpoint 残差 L2
小于 sqrt(25)*tol/20=2.5e-7。实际 1.6071726197689955e-6
远大于这个上界，因此最终网格不是按这一正常残差条件完成。

在没有 singular 返回的情况下，原源码还允许以下停止原因：
21 次回溯没有满足严格 affine-invariant merit 下降（计 no_step）；
8 次 Jacobian 分解预算已用；24 次迭代预算已用。
完整步 alpha=1 被接受时还会沿用旧 factor 作 modified Newton。
这些返回没有自动改成 singular，外层仍会按 RMS 做网格细分。

现有公开小记录没有导出该原 run 的 domain_newton_stats，所以
尚不能在这几种原因中选定一种。后续只读原 run.json 的已有
计数即可，不必重跑 Newton，也不据此改算法或发新验收门。

## 5. 已生成但尚须实际求解的保场初猜

脚本以原 merge_profile_mesh(401, chart_breaks) 得到 415 个点，
在每点采样原 raw cubic 的全部 25 个状态分量，原 p 和 pscale
逐位保留，没有重建 cold 场，也没有只复制低模幅度。

输出：

    $WORK/q006-rms-remesh-01/initial.npz

SHA256：

    5f08c33c4f5050c1d9fa2abc253fd9e9906c88be37665276111e044fe35abc6c

实际原 frame 最小 margin=.003891741691174011。以这些节点与
原 F 生成的下一 solver cubic，其初始 RMS=.0010630764399725422；
与源完整 cubic 的状态最大差 1.061783029054908e-6，
t 导数最大差 .0016071897009829147。节点保场采样不表示两条
新旧插值曲线全段相同，更不表示此重采样已满足原方程或 metric。

因此下一步只把它交原 H1 边值问题暖解，保留原 tol=1e-6、
max_nodes=6000、域/边界/完整 metric 检查。暖解命令已发出；
本条写作时终态仍待实际返回，不能预记成功。

另备 resume_height_amplitude_path.py：只有已接受的 H1 前缀和
真实完整 checkpoint 才能续接剩余 q 序列，输出独立目录和摘要，
不覆盖上述失败源或重启 cold 入口。

## 6. 原门下暖解的实际返回

命令 held10-q006-warm-remesh-01 已 returncode=0，实际 pull 至 1fdbc1e0337313137be3bed19b35d9643100e059，双 README 无变化。579 节点、RMS=9.947402870695902e-7、原 metric_l1=2.5223305069605293e-9；5 次内层调用共接受5个全步，no_step、域拒绝、merit拒绝均0。raw SHA256=9763fb14879c17f3011bf0ec92a1a68402124f58083512636dedeb4ba6911975；physical SHA256=889fca11fd3d36e617bf5104200ab75d3e1b8276c217c0de057aa80c6d2dbd9b。完整紧凑返回见同日 q006-warm-remesh-return.json。

同一原方程与阈值通过说明这次小区间停滞可以由完整场重采样暖解绕过；没有修改tol/maxnodes/p scales，也不由此选择旧失败的具体停止原因。此成功仍为H1+高7原linearDN初始化；首原linearDN欠5.024514865270223e-7，所有原非线性DN及完整闭面仍未付。接续命令只从该真实完整checkpoint推进其余幅度，不回到cold入口。
