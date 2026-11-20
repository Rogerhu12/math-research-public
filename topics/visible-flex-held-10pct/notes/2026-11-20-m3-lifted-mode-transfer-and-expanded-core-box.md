# m3：精确 lift 的升 M 传递与实际控制的扩大正性盒

维护会话：Astra-held10-1b6d88ec-20261120。

## 已观察入口及范围

Actions run 44718341266 / job 136227357046 中，H1 与高七条原线性
DN 的幅度初始化从 q=.006 到 .06 的七步成功。q=.06 的有限前缀
metric_l1 为 3.45348243e-8。其后材料曲率同伦 lambda=.02 的八条
原线性 DN 边值问题也返回成功，605 节点、RMS 9.99095868e-7，
但原完整审计 metric_l1=2.3928678465e-5、
darboux_l1=.01876956，未支付 metric<=1e-6，更没有新的真尾。
这些是实际有限计算结果，不是严格存在或已完成曲面。

本条新增的是可用的初始化传递恒等式，以及覆盖该次控制的条件
几何盒。不得以它们替换以上未通过的 metric 门。

## 1. 精确 lift 的 M 依赖不能忽略

令 V_M 表示原三个 R/T/Z Fourier 块到向量场的线性重建，q 固定。
原 exact_core_lift.py 实际使用

    X_M(s,psi) = B(s,psi) + h(s) H_M(psi) + q V_M(Y_M(s),psi),
    H_M = C(theta_0(psi)) - B(0,psi) - q V_M(I_M,psi),
    h(s)=a(s) chi(s),  I_M=initial_M(p).

这里 B 的 core 处半径为一。chi 为脚本原 .5 到 .9 prefix_end
的二阶平滑 cutoff。核心同伦 lambda 只进入 C；lift 自己的系数
恒等于一，不能再乘 lambda。

设 E 把旧 R/T/Z 三个块按各自的频率位置嵌入新 M，保留 R 的均值。
对相同 q、物理 profile、角坐标和实际核心，严格的连续参考传递为

    Y_new(s) = E Y_old(s) + h(s) [ I_new - E I_old ].

因为 H_old-H_new=q V_new(I_new-E I_old)，代入立即得到同一完整
X(s,psi)。其计算一、二阶导数的传递分别加 h' 和 h'' 倍的相同
投影差。因此只把旧 Y 补零，同时重建新 H，会改变真实向量场。
若改变了 q、profile、角 warp 或核心，这个恒等式不适用。

实际参数须保留物理尺度：

    p_new[0] = p_old[0],
    p_new[j] = p_old[j] * pscale_old[j-1] / pscale_new[j-1].

原 p[0] 在此是 delta 增量。新增加的实际支持控制初始化为零，
并不把归一化大 p 数值叫作大物理控制。

同一角平均算子下，角场和其 s 导数相同也保持原重建的平均高度及
其导数。换角求积点数后仍须重新检查数值均值误差；这里没有把
有限 FFT 平均升级为连续或向外舍入证书。

## 2. 可执行接口及诚实的存储范围

新增脚本：

    scripts/resume_m3/prepare_lifted_mode_restart.py

例（路径随实际 live runner 中的输出目录取值）：

    python -u "$TOPIC/scripts/resume_m3/prepare_lifted_mode_restart.py" \
      --source-run "$WORK/material-lam002-linear/run.json" \
      --modes 12 --tail-config "$WORK/inputs/q060-tail.json" \
      --outdir "$WORK/material-lam002-m12-transfer"

它由原 run.json 的完整调用恢复同一输入，核对原 raw 的记录 hash，
保留原 q/delta/warp/实际核心控制，构造上述传递。若原 physical.npz
在，使用它的 C2 PPoly，检查 pos、psi、psi-psi、s、s-psi、s-s 六个
计算 jet；默认至少 2048 角点和约百个 s 点。它保存所有检查值，
有限重建差超过 1e-7 时拒绝生成初始化。这个阈值只检查传递实现，
完全不是新的等距验收阈值。

原 bootstrap 的 port 只有八个 linearSlope。若升到 M=12，脚本用
--tail-config 指定的完整原设置，只修改数值 modes，调用原 exporter
真实生成新高模 DN，并要求 physical parameters/cut 与旧记录相同。
也可 --port 直接提供已导出的同物理较大 port；不补零 DN。
后续必须使用 transfer.json 中 result.port 指出的该 port。

输出 initial.npz 可交未改的 portable_prefix_continue.py
--raw-restart；此时目标 M 与 pscale 已匹配。transfer.json 的
diagnostics/result 是 live worker 可投影的紧凑记录。没有提交场数组。

**initial.npz 保存的是节点初猜。** 上述连续参考有精确传递公式，
但新的 SciPy 插值或重新求出的 C2 前缀不因此自动等于旧连续参考。
后续 Newton 必须重新付全部原域、边界和完整 metric 门。
该准备脚本截至本条记录尚未执行；不能把源码存在写成传递已通过。
若后续允许 delta 或 c 自由改变，这仍不是固定全部 g/q/c 的收敛检验。

## 3. 覆盖实际 lambda=.02 控制的较大正性盒

此前 R53 小盒不包含本次高模控制。可以独立改用下面的有理盒，
且不撤回“原小盒已越界”这一实际观察：

    .0599 <= q <= .0601,
    |c2| <= .000473,       |c3| <= .0000386,
    |c4| <= .000000158,    |c5| <= .000000817,
    |c6| <= .000000915,    |c7| <= .000000116,
    |c8| <= .000001003.

这些上界包含本次公布的 c 值：
[.0004725400447,-.00003852143913,-.0000001579567783,
 .0000008168052457,-.0000009145049582,.0000001153796938,
 -.000001002261729]。后续求解仍须用实际完整控制重新检验留盒，
不得假定它们一直留盒。

记 b_j 为上列上界，w_j=9j^2-1。按分母 10^12 作整数求和：

    sum w_j b_j = 20771912000 / 10^12 = .020771912,
    sum j^2 w_j b_j = 148999684000 / 10^12 = .148999684
                     < 8*.0599 = .4792.

原支持曲率半径是

    rho(phi)=1-8q cos(3phi)-sum_{j=2}^8 w_j c_j cos(3j phi).

在 0<3phi<pi 上，|sin(jx)|<=j sin(x) 给
rho_phi >= 3 [8q-sum j^2 w_j b_j] sin(3phi)>0。
所以中心 phi=pi/3 仍是 rho 的全局最大、kappa_old 的全局最小，
而全角范围满足

    .498428088 <= rho <= 1.501571912,
    0 < kappa_old < 2.01.

将材料同伦目标 k 从中心 kappa 向 .2 下调，则
k<=min kappa_old，原补偿 beta 非负。R53 的凸组合表达式因此仍给
每个 lambda in [0,1] 的 kappa_lambda>=k>=.2，只要控制留在本盒内。
这是整个 lambda 区间的核心正性结论，绝非 BVP 的连续可解性。

新的二阶半径导数界为

    |rho_{phi phi}| <= 9(.4808+.148999684) = 5.668197156.

因此 R53 原来以 5.2 为前提的较锐形变预算不能原样搬到新盒；
可使用 5.67 重新计算。此条不改变 R52 对 n3 完整像采用 sqrt(3)
系数的 Hausdorff 见证，也不把圆心两倍平移尺度误用为整像距离。
