# 同Hold标量的完整M160边值问题准备

**仅准备，不是新解。** 固定ed6 HoldProfile，终点1.04，M160/N2048，保留全部482个Frenet方程。左端325行由R0=1、原d644前三core、全部160行T_j+2jR_j=0及161行Z_j=0组成。右端157行保留非零外推参考目标。左右行严格分离；本次没有运行完整QR或Newton。

## 固定warm与边界定义

原d644的498个胞元用原M112/N2048二jet，真a425接口前的全部实际0/1/2jet用R637首32胞桥接，再线性下投影到M160。新warm保原499节点，并以81点读局部参考，加桥端点和标量分段点；κ=0界面以后仅用保存的真实二jet明确二阶外推到1.04，长度.01165036710272438。此下投影、重采样与外推不冒充精化、真解或可接受父。

记该明确末端参考为y_ref。以完整482维RHS的A=∂f/∂y及实际移动标架T、T_s构造B=(TA+T_s)T⁻¹，取B的最快157维完整实Schur左子空间L_B，冻结L=L_BT。右边界为 **L y(1.04)=L y_ref**。标架速度和加速度由该参考点的完整有限ODE给出，所有行和目标在参考上一次冻结；不在Newton中重选子空间，不把高模置零，不称非线性DN。

## 有限网格准备门

初603节点的声明quintic本身采样域正，但由完整真实RHS构造的collocation中点有12个坏尾胞。严格按同一规则只二分坏尾胞，保g、参考函数、外推jet和目标不变，原预算1800节点内记录：

|层|节点|坏中点胞|中点H最小值|
|---|---:|---:|---:|
|0|603|12|−.00294876635|
|1|615|23|−.00122605553|
|2|638|39|−.000243855776|
|3|677|73|−.0000320574282|
|4|750|77|−.00000493795170|
|5|827|0|6.54548881e−9|

每层全部节点都保持采样域正，完整节点ODE系数缺陷最大均为.327039521615、相对分量最大.246458477348、相对向量RMS最大.0279365261883。该大缺陷没有因网格准备被冒称消除。

最终827节点，全部warm胞4sub/8192角及全部实际collocation中点检查无坏点；Qmin=.0275621194198、Wmin=8.35801956853e−6、Hmin仅6.54548880588e−9。此H余量很小，且仍为角/径向采样诊断，不是区间证明。完整collocation缺陷有限，max per-length .326496333910。左矩阵rank325，边界残差6.94e−18，不能由边界小残差推出ODE已解。

## 末端完整Schur与费用

实际选择恰为157个完整实Schur维数，未劈开共轭块。分界两侧real=.424741086231/.434876509483，gap=.0101354232524。T条件数2.23573、L条件数1.39558；非零右target norm1.08004782948，max .44545439818。Schur不变性相对残差3.24e−15，但subspace sep估计仅.000291792976，相对矩阵范数4.61e−11；**不声称稳定性已解决**。

只测原前缀一个实际cell的三个完整Jacobian、局部块和一次磁盘QR append，没有完整全段factor或Newton。由此次单线程实测外推：827节点一次全QR factor约113秒、磁盘6.14GB，persistent QR数组约.668GB，另chunk32 Jacobian数组约.121GB；这些是费用估计而非已执行全QR或全局条件数。预留原tol1e−8、bc_tol1e−11、max_nodes1800；本项没有启动求解。

## 复现与冻结身份

T为题目录，S=$T/scripts：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_bvp_prepare.py" --topic "$T" --parent parallel-continue0995-m112.json.gz --interface parallel-negative-hold-type-interface.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --warm parallel-hold-m160-bvp-adaptive-warm.json.gz --arrays parallel-hold-m160-bvp-adaptive-arrays.npz --out parallel-hold-m160-bvp-adaptive-prepare.json
```

SHA256：

- 准备源：`fe6bbefb8cc0411ab6018376b6fde6c957acbe4f57bb24c4a10ce7acecdc9104`。
- 真左父：`d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`；真接口：`a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8`。
- 正确HoldProfile：`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
- 完整warm：`7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74`。
- 冻结BA/BB/target/末参考及完整矩阵：`54ee88a8d6d44307431e3ee35dabbc8c907631cfb62512b9bd8b5f59a94260ba`。
- report：`8a95f0ecb9c313c767a9df11a77d70aff78d610b78cc26b1f6585dee3785bde9`，同时保留每层全部坏胞编号、每层域下读数、完整方程缺陷及依赖源SHA。

所有raw/矩阵仅scratch；warm数据明确`success=false`、`preparation_only=true`。最后的`preparation_gates_passed=true`仅表示该有限准备门通过，不是BVP或几何结论。

## 同一冻结问题的单次执行入口（2026-11-17 16:51 UTC）

本准备完成后已实际启动一次完整BVP，未预填结果。[执行源](../scripts/parallel_20261117_hold_full_bvp_once.py) SHA256 `f93d74382ac83bee08079759ca17cace95b3e99cb765e706e6d1ef67c7861d81`；硬核原warm/BA/BB/target、标量、Frenet、fresh-J Newton及DiskQR全部来源。仍为482/325/157、tol1e−8、bc_tol1e−11、max_nodes1800；准备场不是接受父。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_full_bvp_once.py" --topic "$T" --warm parallel-hold-m160-bvp-adaptive-warm.json.gz --arrays parallel-hold-m160-bvp-adaptive-arrays.npz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --out parallel-hold-m160-bvp-once.json.gz
```

磁盘QR/chunk/source checkpoint都只在scratch；最终状态、原完整数学门与真实全场读出后续分别登记。这里的执行记录不更改上文“准备未求解”的历史结论。

实际终态已见[首次完整BVP失败与RMS域缺口](2026-11-17-parallel-numerical-hold-m160-first-bvp-failure.md)：没有Newton步被接受；17步皆因残差非有限拒绝，第二Jac未装配，失败场不是新父。
