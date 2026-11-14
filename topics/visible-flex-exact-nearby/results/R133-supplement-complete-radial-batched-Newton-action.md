# R133 续篇：完整 Newton 作用的径向分批与实际帽边界

2026-11-13，visible-exact / root。

**状态：已证明的有限算子恒等式及已完成的小型完整矩阵核对；不是非线性 PDE 存在证书。**
本次改变的是独立径向列的系数存取，不改变任何角频率、耦合项、参数列、边界行或反代验收门。

## 1. 同一个完整有限算子

设 $y_j$ 包含全部互逆 $U,V$ Fourier 系数和 $V$ 均值，公共度量参数为 $\nu$。
原完整非线性有限方程的导数在固定节点处是

$$
 df_j=J(r_j,y_j,\nu)v_j+f_\nu(r_j,y_j,\nu)\,d\nu.
 \tag{B.1}
$$

对任意径向节点集合的划分，把各列分别送入同一个 `system.full_action` 再按原序拼接，
得到的就是 (B.1)。理由是每个径向节点的函数值只依赖该节点完整角场和同一个 $\nu$；
所有角卷积、全部有限 Fourier 模和参数导数仍在该列内部完整计算。
这不是沿角频率分块近似，也没有设置任何 Fourier 元为零。

原三次 collocation 的完整线性作用为

$$
 v_{j+1/2}=\tfrac12(v_j+v_{j+1})-\tfrac18h_j(df_{j+1}-df_j),
$$
$$
 (\mathcal Lv)_j=v_{j+1}-v_j-
 \tfrac16h_j(df_j+df_{j+1}+4df_{j+1/2}).
 \tag{B.2}
$$

在 (B.2) 的节点和中点分别使用 (B.1) 的径向分批恒等式，整个矩阵仍准确相同。
右端真实帽切口使用
$b_m+\widetilde q_m c_m$ 的完整物理商导数，逐行乘各自的 $\widetilde q_m$；
两端的均值、第四模幅度和公共 $\nu$ 列都保留。
边界作用仍为 $L v_0+R v_N+P\,d\nu$。

新 `chunked_full_action` 只保留不可变的完整节点数据、参数和节点位置。
每次算子应用以16个径向点为一批重新计算全部系数和完整作用，拼接原节点次序。
它不常驻整段节点及中点的全部角系数数组。内存中的这部分系数规模因而只随批大小增加，
不再随整个径向网格长度增加；输出、原完整节点数据和 QR 检查点仍全部保留。

完整 QR 分解、短段精确重算、三次 collocation、原物理可行域检查与 Newton 接受门
均沿用[完整非线性边界 QR](R133-supplement-reciprocal-complete-nonlinear-boundary-QR.md)。
独立反代检查仍用上述完整 FFT 作用，原相对残差门仍为 $5\cdot10^{-8}$。

同样的径向列恒等式适用于完整非线性 RHS 及物理 $B,C$ 场。
`ReciprocalCapCutBatched` 将这两种调用也分成16列，分别拼接全部归一化状态和全部实际角场。
这避免在初始可行域与 collocation 调用中同时创建全径向网格的中间角数组；所有最终输出仍完整。

## 2. 必要的实际完整矩阵核对

在真实新度量、真实 $r=3/2$ 逐模帽向量、全部非线性边界行与 $\nu$ 列上，
取仅用于线性实现核对的 $M=8$、22个径向节点、375维完整系统。
它由完整旧候选投影产生，不作为新的继续候选，也不当作任何无限维截断证明。

独立 SciPy 完整 collocation Jacobian 和完整 LU 为参照；新完整 checkpoint QR
对实际残差及一个固定随机右端分别求解。两次的最大结果为

$$
 \frac{\|Jx-b\|_2}{\|b\|_2}<7.714\cdot10^{-13},\qquad
 \frac{\|x-x_{\rm full\ LU}\|_2}{\|x_{\rm full\ LU}\|_2}
 <2.324\cdot10^{-14},
$$
$$
 \frac{\|\mathcal L_{\rm full\ FFT}z-Jz\|_2}{\|Jz\|_2}
 <3.918\cdot10^{-16}.
 \tag{B.3}
$$

所有原门通过。非线性场也分批后的完整系统又在同一375维实际矩阵上消费了两右端，得到同样的(B.3)，新增原生文件为 `notes/2026-11-13-R133-reciprocal-capcut-complete-radially-batched-system-audit.json`。这次核对针对第二个新增路径，不改变数值门。

完整源和原生结果为
`fourfold_codazzi_reciprocal_chunked_action_audit.py` 与
`notes/2026-11-13-R133-reciprocal-capcut-radially-batched-full-action-audit.json`。
这是针对新径向存取和真实帽边界的具体实现核对，没有追加不必要的重复完整大求解。

## 3. 原退出与当前接续的精确范围

此前真切口 M256 会话84317在完整1343节点 QR 因子分解之后、独立完整线性解完成之前，
实际被 `Killed`、退出码137。该运行没有新已接受检查点，也没有最终 floating 报告。
其原 process 仍是 `started/complete=false`，不改写成内存不足或任何数学失败结论。
原日志和明确观察记录已保留：
`notes/2026-11-13-R133-reciprocal-capcut-m256-alpha075-step01-exit137.json`。

只分批线性作用的 v3 会话35049也实际返回137；仅保存完整 warm-start 读入记录，
没有 QR 块或新接受步，原因仍未知。该原 process、原日志及退出观察另存；
读取内核日志被本环境拒绝，因此没有据此添加原因推断。

新的 `fourfold_codazzi_reciprocal_cap_cut_refine_probe_v4.py` 同时分批非线性场与完整线性作用，
从早先已实际保存的全 M256 状态继续。地址空间限额1280 MiB，
原 `tol=2e-6`、全部角模、物理边界和 QR 反代门未改。
每个完整接受步之后仍保存全部状态与三次系数，并把主动暂停明确记成
`finite_BVP_success=false`。结果须读取自己的真实报告；
本篇不提前授予有限成功，更不授予全频主体、闭面或可见振幅结论。
