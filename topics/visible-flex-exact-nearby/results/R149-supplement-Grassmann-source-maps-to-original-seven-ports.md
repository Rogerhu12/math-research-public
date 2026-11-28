# R149 GTP：同一 Grassmann 四源映射到物理七端口和 WPN 两行

**已证明的是转接定理及其程序实现。** 本条不赋予 GG、物理门、PN 或 CXN 任何尚未实际得到的数值。设 [GG](R149-supplement-joint-Grassmann-true-low193-and-whole-source-maps.md) 的两项目标均对同一 selected family 的 WVC hybrid 真正完成。则 GG 四族映射可作为 [TP](R149-supplement-true-flow-to-complete-positive-physical-chain.md) 的输入，依次验证原物理 58、224、32 条；当三次实际验证均成功时，原 PN56 与 CXN6 的正侧先决条件成立。其余各自列明的前提仍须实际满足。

## 同一算子和同一单位

在同一个真实区间 $[r_*,25/8]$，写 $G_c$ 为初端指定 even96、末端指定 $((u_j+13v_j/80)_{j=1}^{96},v_0)$ 的 WVC hybrid 解算子。body 使用物理 $S$ 与普通 $dr$；root 读取 $(u_1,\ldots,u_{96},v_0)$，outer 读取 $(\Theta_jv_j)_{j=1}^{96}$，$\Theta_j=(1+16j^2)^{-5/12}$。GG 每个 $Q_i$ 是已声明有理 Householder 乘积，$Q_i^tQ_i=I$。图表给出的 $L_i,R_i,\ell_i,\rho_i$ 直接在同一原始物理坐标上分解状态，且 $L_i\ell_i+R_i\rho_i=I_{193}$。完成两个端条件以及每一节点横截验证后，齐次问题只有零解，任一给定普通源的变参数解唯一。因此 GG 的 $G_c$ 在此定义下就是 TP.1 的解算子。估计不同不改变解算子的定义。

GG 的 $J_i^W$、$X_i$ 包含全部变系数转移、两同格有序三角、ordinary-$dr$ 时长以及原 $S$。四个 $W$ 依次为 $I_{193},S^{-1},(A_{Lc}-D)S^{-1},C_*$；列数依次为 $193,193,193,128$。其四个接收器 $J$ 为 body $B$、root $R$、outer $O$ 和 joint atoms $A=R\oplus O$。由 GG 的四个 complete-map 定理分别得到 $g_{WJ}\ge\|\mathcal O_J G_cW\|$。分开的 $R,O$ 由各自保存的 HS 平方上界开方；联合 $A$ 使用 GG 同一完整 norm。原两端 mean 读出及独立 mean 输入的 identity 按原定义保留。

## 物理闭合

记 correction 列上界为 $c_J$、raw 列为 $g_{0J}$、centre-return 列为 $g_{CJ}$。对同一个原 $D$ 与 $S$，原参考解和实际解的差满足同边界非齐次方程，按 TP.4 的解算子恒等式得
$$
T_L=I+\mathcal O G_c(A_{Lc}-D)S^{-1}\operatorname{pr}_B .
$$
故原完整低族差 $L_0$ 对 body 的费用为 $\ell_B=(1+c_B)L_0$，对其余接收器为 $\ell_J=\sqrt{1+c_J^2}\,L_0$。把 $C=C_*+\Delta C$ 代入原实际 $CG_HB_{HL}$，由三角不等式得到
$$
 \kappa_J=\ell_J+(g_{CJ}+g_{0J}d_C)H_B ,
$$
其中 $d_C,H_B$ 分别取 TP.3 的整球。$C_*$ 的 128 列只控制第一项，$\Delta C$ 与全 high 的费用另由上述原结果支付。严格 $\kappa_B<1$ 时，以 $1-\kappa_B$ 的正下界反解 body 方程，继以各 $\kappa_J$ 回代。完整原参考边界 lift $d$ 经 $T_L$ 的接收器为 $p_B=(1+c_B)d_B$ 与 $p_J=d_J+c_Jd_B$；随后 TP.7 的 160、288 支集费用与 TP.8 的原 Robin/独立 mean 两行完全相同。故原 B18–21 的物理二块逆估计适用，必须实际通过两正 margin 和 determinant 门；任一充分门未过只保对应已完成分支。

通过时原14输入包含全部七个 source/jump ports、raw low、$S^{-1}$ low、root-even96、charted right97、独立 height、Robin、mean。每个边界数据沿 low right97 和 high affine 图进入的两路都保留。全部16个输出遂给原 $14\cdot16=224$ 个接收器。继而按原 $24480$ 径向投影、$q\ge1/8$ 与原 $H^1$ lift，有限和全正交 tail 两个 WPN 输入各有16个输出。上述步骤和原 TP 的数学公式逐项相同，从而原 PN56 与 CXN6 可使用新实际物理结果及各自其余的合格输入。证毕。

## 可执行的输入链

新入口为 `make_grassmann_physical_chain_manifest.py`、`fourfold_codazzi_grassmann_physical_chain_owner.py` 和 `fourfold_codazzi_grassmann_physical_consumer_math.py`。完整 GG actual、execution 和 manifest 的 size/SHA256/git blob 必须匹配，并且实际执行须包含这份 exact scientific 文件。验证同一 run、checkout、完整21件历史恢复、97件 current（按该 manifest 完整原序）、GG 新 kind、两个新目标、每个原序联合图/节点、全部四族 whole map 以及九份 GG 源码/证明和原 GH5 reference identity。首发旧 TF 的失败及其三个须恢复的 whole SHA 身份原样保留。只有这些成立才创建相应物理 stage 的 manifest/workflow。公式与原 TP 的标量字段相同，原有物理 stage kind 沿用；GG 输入的新 kind 及其 provenance 始终单独验收。

实际运行时每个标量先定向、完整保存并读回再消费；读取旧58或224条时同时检查原 manifest、execution 和全部有序记录。新的 58/224/32、PN56/CXN6 均未在本条执行。signed Newton、$\nu$ defect 和 nonlinear 同态的实际 cut、shell、负窗不由这四组算子范数自动给出。
