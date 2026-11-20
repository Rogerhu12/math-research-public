# 与现有完整 metric 审计共享物理图的只读 R / Rθ 壳诊断

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：源码已写，尚未执行。** 此入口针对当前完整材料核候选中 projected BVP 已收敛而 full metric 仍有缺口的情形。它不重新求解、不改任何核心/物理参数、不改变现已冻结的 metric 审计或原门。本文没有为当前在跑作业填写未返回阶段。

## 输入和同一个实际图

新源：[audit_full_frenet_residual.py](../scripts/resume_n4/audit_full_frenet_residual.py)。

直接调用以下两个既有接口，不复制或改写它们：

- [audit_full_relative_metric.py](../scripts/resume_m3/audit_full_relative_metric.py) 的 load_physical：读实际 physical.npz 中的物理 quintic PPoly，不读一个拟造的 raw cubic。接入时源码 Git blob 为 5eecadb050e5227b4b6eaaf43878aad5a187f28a。
- [actual_m3_metric_model.py](../scripts/resume_m3/actual_m3_metric_model.py) 的 load_model：按原 run.json 重建同一 geometry、完整 reference lift 和 moving 材料角图，不启动 BVP 或尾。接入时 Git blob 为 fe4d454a9f8b23bccdb5d78aae3c7d85bd31c4c9。

径向点与冻结 metric 审计默认完全相同：151 个均匀物理 s 点、全部真实 quintic 节点、全部相邻中点的并集。默认分批 8 个径向截面。mean_nodes 必须显式传入，本次和原独立审计同为 512；改变评价角点数时仍只用这一条 mean 规则。

## 残差与两个分量

由真实导出场读取
$$
Y=\mathrm{physical.sol}(s),\qquad
Y_s=\mathrm{physical.sol}(s,1).
$$
不以投影 RHS 替代 $Y_s$。每个评价角网格上，
$$
P_s=g[\mathrm{s1}]+q_g\,B Y_s,\qquad
R=P_s+m'e_3-\mathrm{frame}[\mathrm{V}].
$$
其中完整 geo 包含原背景与全部 lift；frame 的 V 是 $V_{\rm normal}+vP_\psi$，所以 convection 没有漏掉。mean 则在固定 mean_nodes 上独立形成，所有角网格共用。

为定位径向表示的影响，源码默认另外评价一次原物理 s RHS，给
$$
R_{\rm radial}=q_gB(Y_s-\mathrm{flow.fun}(s,Y,p)),\qquad
R_{\rm comp}=R-R_{\rm radial}.
$$
这是完整 R 的分解，不是把它改成投影残差。调用的是 physical flow.fun，绝非 normalized obj.fun。comp 包括原有限角投影、其求积及固定 mean 规则的效应；不称它为精确的纯高模尾。命令行可用 --no-native-projection-split 省略这一额外只读分解。

在 N=512 且 mean_nodes=512 时，完整竖直 R 的零 ψ 模应仅有有限状态均值/舍入量。N 改成 1024、mean 仍固定 512 时，零模可以出现 mean512−mean1024。源码同时报告这两个量及二者差，避免将这种规则差异误说成新物理 mean 或高模缺陷。

## 不需第三角 jet 的独立标量核对

新增的一项只读检查直接使用当前 C² jets。令
$
F_{s,\psi}
=g[\mathrm{sp}]+q_g B_1Y_s
 -v_\psi P_\psi-vP_{\psi\psi},\qquad
F_\theta=P_\psi/\rho,\quad T=F_\theta/|F_\theta|.
$
两个 moving-chart 项都保留；mean 只依赖 s，其角导数为零。原 frame 给
$F_\theta\cdot V_\theta=(a_s/a)|F_\theta|^2$，所以
$
\boxed{
T\cdot R_\theta
=T\cdot(F_{s,\psi}/\rho)
 -(a_s/a)|F_\theta|.}
$
这里使用实际 $|F_\theta|$，没有假设 $G=a^2$。该标量除以 a，正是
$\partial_s(|F_\theta|/a)$ 在固定材料角下的导数。它只需当前完整场的一阶 s、二阶角及混合 C² jets，不计算 V 的第三角导数。

源码在同一组节点上比较这个直接标量与 DFT 角导数的 T 投影，记录两者尺度、差的最大值、相应 s/ψ/θ 位置及带符号值。它是当前节点上的独立分辨率诊断；该点值差不能被当作未采样连续导数误差的上界。此项不改变现有 R、固定 mean 或任何 metric gate，也不触发额外 frame、BVP 或尾求解。

## 输出如何读

每个角网格的 compact JSON 保留：

1. 实际三个 Cartesian 分量的 R 节点最大值、位置、全向量；原 Frenet margin 与角图 rho 的节点最小值。
2. 全 Cartesian ψ-DFT 的分壳质量与 $|k|$ 加权质量，最高值所在 s 及少量主频。默认壳包含 0、1 到 base_mode、到 base_mode*M+1，以及其两倍、四倍、八倍尺度。
3. 真实材料角中的所有整数 $-K,\ldots,K$ 系数，按原 $d\theta=\rho\,d\psi$ 规则做有限求积。没有把水平分量限制为标量的 3j 或 4j：水平 $\pm1+n j$ 模也在其中。对应的 Rθ 壳由估计系数乘 $|k|$ 得到。
4. ψ 三角插值的节点导数除以真实节点 rho 的 Rθ proxy；偶 N 的 Nyquist cosine 在这些节点上的导数取 0。加权壳仍保留 Nyquist 质量，不能由节点导数为零宣布该频率没有影响。
5. 固定 mean 下不同角网格的共同节点 R 差及相同材料 Fourier 系数差。
6. C² 直接标量 T·Rθ 与 DFT 同投影的点值最大、差及主导尺度；不额外假定实际角向度量已等于目标。
7. 在同一实际物理 s 点并集上，对两个 Rθ proxy/a 作梯形积分。该积分只是有限诊断，不是本日 [连续残差界](2026-11-20-n4-full-frenet-residual-metric-bound.md) 的已认证输入。

任何输出都不能代替已有完整 metric/真尾/mean 与非mean 两 jet 验收。DFT 有混叠，材料 Fourier 只到明确 K，rho 目前只报告节点最小，梯形积分没有径向余项；源始终把 continuous_angle_certified 与 continuous_radial_certified 设为 false，不发物理“通过”标志。实际 mean 的连续积分/导数误差也没有在这个入口被默认支付。

## 同一个当前 runner 的调用

以下 RUN 应指向本次工作目录中已经真实返回 physical.npz 和 run.json 的那个候选。只对其现有图做读操作，不启动新的恢复/BVP。

~~~bash
python "$TOPIC/scripts/resume_n4/audit_full_frenet_residual.py" \
  --model-adapter "$TOPIC/scripts/resume_m3/actual_m3_metric_model.py" \
  --metric-loader "$TOPIC/scripts/resume_m3/audit_full_relative_metric.py" \
  --model-config "$RUN/run.json" \
  --physical "$RUN/physical.npz" \
  --out "$RUN/full-frenet-residual-shells.json" \
  --angular 512 1024 \
  --mean-nodes 512 \
  --physical-cutoff 96 \
  --batch 8
~~~

这里固定 mean_nodes=512 与冻结审计一致。提高 --angular 时不随之改变 mean；--physical-cutoff 必须严格小于最小角点数的一半。所有材料整数频率都求积，所以 cutoff=96 是 193 条系数，不能把它解释为只有 96 条或只取 24 个谐波。

对 S 个径向点，以上配置评价一套固定 mean 512 点、一套原 native 投影 RHS（可选），以及 512/1024 两套实际 frame。材料系数按 16 个频率一组生成临时 phase，不保存完整全场或大矩阵。输出只有参数、命令、来源散列、极值、壳统计和少量系数，原 physical.npz 与内部数组继续只留在临时运行目录。

此文件与新源在执行环境失联期间写成，环境恢复后仅完成语法编译，尚未实际读取λ场或运行诊断。后续实际命令的终态、完整统计和任何错误由真实 runner 记录；当前没有数值结论可以预填。
