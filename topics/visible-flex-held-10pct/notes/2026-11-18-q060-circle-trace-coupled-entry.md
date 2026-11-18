# q060 唯一主矩与两 jet 初猜接原实际尾：M8 联立入口

状态：**源码和单一启动计划准备完成，尚未执行新联立 BVP 或 DN。**
本条承接已完成的
`2026-11-18-q060-m8-circle-trace-initializer-terminal.md`，不重做其有限初猜诊断。
原初猜通过了数值核心与 Frenet 域，完整八项 cut height 与旧实际尾输入逐位一致；
它的初始 RMS 为 $1.4166287468767744$，没有因此成为 BVP 解。

## 1. 唯一新设计与参数含义

固定新主幅值

$$
q=0.05210565550627671,
\qquad q_{\rm old}=0.06,\qquad q=q_{\rm old}/P_{\rm new}
$$

其中 $q$ 是已证明唯一最近 binary64 值；主矩公式及舍入身份沿用已登记的冻结计划。
主核为 $\lambda=1$、$a=.21$、主过渡宽度 $.32$、控制过渡宽度 $.4$，
中心按数学 $\pi/3$ 定义，偶/C3 且锁定均值与 $\cos3\phi$ 支撑矩。
新有限空间固定为

$$
\operatorname{span}(B_2,B_3,B_4,B_5,B_6,T,U),
\qquad T=S_A-S_B,\quad U=S_B.
$$

这是 M8 的七个控制和 25 个状态，没有嵌入 M16，也不是原余弦空间的换坐标。
物理 trace 参数 $(t,u)$ 对应 $(A,B)=(t,u-t)$。
末两项的名义频率标签不被当作频率 21、24 的实际谐波。

新运行以原 q060 最终 `frozen_profile` 为基础：初始
$\delta=0.06104275721220832$、$L_{\rm binary}=1.3602524132788236$，
原角图与 warp reference $.06$ 保持。`fixed=False` 且新 `p0=0`；
旧历史 `p0=-8.84429295772251e-6` 已进入这个最终 profile，不能再加一次。
此后 `p0` 只沿原方程改变 $\delta$ 和相应径向 chart，新 $q$ 固定。
所以这次运行是新设计的真实联立，不能称固定同 $g$ 精化。

完整物理控制仍按原尺度链

$$
c_j=\texttt{pscale}_j\,p_j
$$

计算。原七项尺度不变，没有装预条件或重设参数尺度。
T/U 的导数由实际原函数和支撑 jets 进入
`core.parameter_derivatives`、`exact_lift_parameter_jac`、
`analytic_adaptive_core_jac`，再乘一次对应 `pscale`。
`p0` 列保留原完整 profile/chart 差分。
cut 上的 reference lift 为零且 chart 为恒等，原尾的直接参数列为零。

## 2. 必要重建与真正的首个 DN 锚

已完成初猜没有另存状态数组。新入口因此复用冻结
`q060_circle_trace_design.py` 的同一个 `evaluate_initializer` 函数，
只在首次调用 collocation/RMS 之前插入返回值，取出它已经构造的
$x,y,p,H$ 和实际新对象。没有调用原余弦 restart，也不重跑那份初猜的 RMS 探针。
构造真正 BVP 所需的这次重建必须核对：

| 数组 | 原完整 binary64 SHA-256 |
|---|---|
| $y$ | `900cbfda191554b5642e0246caff0f644444e1e67708c33756c1e18b8eb0dd40` |
| $p$ | `8b5153c3b7609783a7f75e8310a884e5cc5db1770fdf26aa9edbad7305c5eab4` |
| 完整八项 $H$ | `36f201a193e1fd50b764af622d81d0b359e1a1a29e0f2608c2ebb73b06e6b2df` |

七项物理控制与原尺度也逐位核对。初始构造保持旧完整参考的表示部分回投和
共享 C2 入口修补；表示状态不含竖直均值原函数，不能把这称作已经复制完整三维图。
真均值轨迹仍由原 flow 的积分及原实际尾/接缝流程处理。

首个实际尾锚是原 q060 已接受的
`closed_work/q060-saved-inner-resume-v1/seed_tail_0003.json.gz`，SHA-256
`ae01f13ad7b28b82481a3417471c4fd5511b145bb50bd2be73a4386897a0db1e`。
它包含相同完整 $H$、原停止残差 $1.8339313038213144\times10^{-9}$、
208 项有限 Jacobian 和完整有限尾审计。
新入口仅在全部 $H$ 逐位相同、原八个 native 源身份相同的条件下，
把该真实响应放入原 client 的已有缓存；这不登记一次未执行的新 native 求解。
原 worker 仍以该实际 checkpoint 初始化，初始 warmup 列表为空。

尾配置只改 `initialCheckpoint` 与 `traceFile` 两条路径。
原 M8、spacing 3、depth 8、steps 16、quadrature 128、parts 16、
linearFar 48、maxIterations 36 以及 $2\times10^{-9}$ 停止门保持。
没有替换 shared 引擎或邻数候选算法。

## 3. 原控制流和恢复记录

入口直接提取原 `db6f-prefix-coupled.py` 的 `main` 与
`solve_with_actual_tail`。原外层最多八次内解保持：
每个 inner 临时使用实际尾响应的原 affine DN，返回后恢复实际尾对象；
inner 未成功时仍按原代码返回失败；inner 成功后用新的完整 $H$ 调真正的原尾，
再检查原 BC，必要时进入下一轮。

外层函数唯一字面改动是将新 candidate 的尾请求由 `audit=False`
改为 `audit=True`，使每个新 $H$ 都留下完整实际 solve/Jac/audit。
它不改变残差公式、停止阈值、原 BC 判断或外层预算。
原核心数值正性 floor $10^{-5}$、32768 网格上限、Frenet/Newton/merit 门保持。
BVP 参数为 angular 256、audit angular 512、初始 271 节点、max_nodes 6000、
tol $10^{-6}$、bc_tol $10^{-7}$、physical_bc_tol $2\times10^{-9}$。

新增记录钩子只传递原求解参数和返回对象：

- 每次 inner 开始前保存完整原 $x,y,p$，并绑定当前实际 DN 响应文件和完整 $H$。
- 每次 `solve_bvp` 返回后，在任何新尾请求前立即保存原 $x,y,p$、
  全部 cubic 系数、breaks、axis、extrapolate、原 success/status/message/niter 和全 RMS 数组。
- 即使 inner 返回失败也保存这些原值；若调用抛异常而未返回，则明确只保留入口状态和 traceback。
- 原 physical C2 导出、完整 prefix 审计和实际 seam 审计保持。新 CP 显式记录
  积分核心、T/U 有限空间、窗口、完整物理控制与来源，避免被旧纯 Fourier reader 误读。
- 外部独立 observer 保留合并 stdout/stderr、资源与真实 child exit；worker 退出码只记录实际可观察值。

这是实际求解前的恢复能力，不把原 raw cubic 自动称作已接受物理 C2 checkpoint。

## 4. 本次已执行范围与复现

实际已执行命令仅为元数据准备：

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/run_q060_circle_trace_coupled.py \
  --prepare /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-coupled-v1
```

工具 chunk `034734` 返回真实 exit 0；读取和核对 66 项来源/输入，并对三个派生函数作语法编译。
没有调用新核心、初猜重建、BVP、DN 或数值 Jacobian 探针。
该目录的 `launch-command.json` 固定后续唯一实际运行及独立 observer 的完整命令。
重现准备时应使用新的输出目录，不能覆盖已冻结计划。

可入库三件为本 note、`run_q060_circle_trace_coupled.py`、
`q060_circle_trace_coupled_entry_record.json`。
完整启动计划 SHA-256 为
`8b9de60b551deccd8ceb4bb2f88ee6f406b3b24e6abc35158f54ebeae0c54da4`。
原数据、以后产生的完整 inner/尾状态和资源记录只留 scratch。
本条没有新增 BVP/DN 接受结论、完整 metric 界、握持比例或 reach，
也没有继承 R38/R40/R41 的具体几何数值门。
