# 真实 R53 M24：完整 λ 列、同一原 J 切线与 δ/logq Schur

本次在真实接受的原 R53 `lambda002_m24` 场上执行完整有限线性化。
源为 $\lambda=.002$、M24、879节点、gauge/warp=.06、实际 mean1168，
实际 $\delta=.06413464112662924$。它已通过全部原线性 Robin 前缀门。
这不是新非线性尾、固定 g 精化、$\lambda=1$ 或闭面接受。

完整实际标量记录原样保存于
[`2026-11-28-analytic-material-tangent-observed.json`](2026-11-28-analytic-material-tangent-observed.json)；
没有将可再生状态或大矩阵放入 Git。
入口是 [`material_lambda_tangent_predictor.py`](../scripts/resume_20261128/analytic/material_lambda_tangent_predictor.py)，
解析列是 [`material_lambda_column.py`](../scripts/resume_20261128/analytic/material_lambda_column.py)。

## 完整原有限问题

令 $Z=(Y,p)$ 为全部 $73\times879$ 个原节点未知量和24个原参数。
$p_0$ 仍是**加性物理 $\delta$ 增量**，其余为原支撑系数坐标。
令 $F(Z;\lambda,q_a)$ 为原 collocation 残差及全部入口/末端行。
计算坐标始终是原 $t$；没有把 $t$ 当成物理 $s$。

动态构造器在切换 $\lambda$ 或实际支撑主系数 $q_a$ 时，清理完整
core、Flow、exact-lift 与解析参数 Jacobian 缓存。只共享已字节绑定的只读
Fourier CSR 表，不共享物理 Flow 或响应。
原节点、中点和两个 RMS 离中点的 Frenet 域样本均保留。

先将源模型重新构造，并与真实保存 cubic 的节点导数核对：最大 RHS 差
$8.673617379884035\cdot10^{-19}$，原完整 $F$ 最大值为
$4.3983177284010555\cdot10^{-11}$。两种参数差分结束后，均恢复原参数并
确认原完整 $F$ **逐位相同**。

## λ 列：中心差分与解析实现的真实全向量比较

在全部 $Y,p$ 不变时，对完整 $F$ 以 $h=10^{-5}$ 和 $h/2=5\cdot10^{-6}$
作中心差分。中点状态依赖也包含在差分内，全部原边界行均保留。
两个完整列的相对 $\ell^2$ 差为
$3.6454628572163515\cdot10^{-10}$，没有域拒。

解析实现逐项微分**当前有限 Gauss 规则**、累计原函数和 real-origin 投影，
没有把有限核心换成另一个真积分对象。写

$$\phi=\phi_0+\lambda C,\qquad \kappa=\kappa_0+\lambda C',\qquad P=2\pi/3.$$

在源码使用的同一积分网格上，以 $\mathcal Q$ 表示该字面 Gauss 求和。
位置原函数的 $\lambda$ 导数使用

$$\mathcal Q[-e^{i\phi}C],\qquad
\Gamma_\lambda(u)=\operatorname{Re}
 \frac{\mathcal Q_{[0,P]}[-e^{i\phi}C]}{e^{iP}-1}
 +\mathcal Q_{[0,u]}[-e^{i\phi}C].$$

跨扇区继续乘原 $e^{ijP}$。其两阶材料 jets 为

$$\Gamma'_{\lambda}=-e^{i\phi}C,\qquad
\Gamma''_{\lambda}=-e^{i\phi}(C'+i\kappa C).$$

入口投影使用原 $\max(2048,128M)$ 网格。设 $I_\lambda$ 为原规范化入口
系数的导数；在 RHS 的实际角网格上，将上述三 jet 转到原 $\psi$ 后，
减去 $qB_jI_\lambda$，得到完整参考差的 $H_0,H_1,H_2$。
令 $h=a\chi$、$h_s=a'\chi+a\chi_s$，则原 RHS 的偏导为

$$\partial_\lambda f=
 \frac{s_t}{q}\Pi\left[
 D_{(d,d_\psi)}V_{\mathrm{normal}}(hH_1,hH_2)
 +v hH_1-h_sH_0\right].$$

这里的 $v$ 是原角图 convection 系数，不是另设的速度。
这同时保留完整 lift、原入口投影及原角图链。

对区间长度 $\Delta t_i$，原中点为

$$Y_{i+1/2}=\frac{Y_i+Y_{i+1}}2
 -\frac{\Delta t_i}{8}(f_{i+1}-f_i).$$

解析列另外使用
$\partial_\lambda Y_{i+1/2}=-\Delta t_i(f_{\lambda,i+1}-f_{\lambda,i})/8$
和中点完整状态 JVP，故没有漏掉这个链项。入口列为 $-I_\lambda$；
完整 lift 在真实短桥 cut 之前已经连同 radial jets 消零，故本固定参数偏导的
Robin 末端列为零。

这个完整解析 $F_\lambda$ 与细中心差分的实际比较：

| 比较量 | 实际值 |
|---|---:|
| 全向量相对 $\ell^2$ 差 | $3.231331383610089\cdot10^{-10}$ |
| 全向量最大绝对差 | $1.6412138315047287\cdot10^{-10}$ |
| 解析完整列本次用时 | 约6.26秒 |

本次最终切线仍使用**完整中心差分列**；解析列只作独立同场核对。
四次完整 $\lambda$ 残差及恢复约耗180秒，因此该已核对的解析列可供后续实际方向计算使用。

## 同一个完整原 J 的 λ 切线

原 $J_{\mathrm{design}}=D_ZF$ 为 $64191\times64191$，包含
10,912,470个非零元。只组装一次；用完整 block QR 消元保留全部状态、参数和边界行。
QR 分解本次耗约.851秒，存储因子162,613,340字节。
没有按小奇异值截掉任何方向。

解

$$J_{\mathrm{design}}Z_\lambda=-F_\lambda.$$

| 实际观测量 | 值 |
|---|---:|
| $d\delta/d\lambda$ | $-3.920492099326574\cdot10^{-5}$ |
| 原完整 $JZ_\lambda+F_\lambda$ 最大绝对值 | $8.355358610786112\cdot10^{-16}$ |
| 相对原 RHS 的完整 $\ell^2$ 线性残差 | $2.4538143050430792\cdot10^{-15}$ |
| 两差分步长所得整个方向相对差 | $7.04628417425203\cdot10^{-8}$ |
| 最大原状态导数 | 1.5757751160892064 |
| 最大规范化参数导数 | 187119.42191747247 |
| 最大实际高阶支撑系数导数 | .01852602833061597 |

较大的原参数坐标含 $10^{-9}$ 的既定 `pscale`，没有将它误称成同样大的物理形变。
完整因子日志中的最大 componentwise backward-error 统计值1也保留在原 JSON；
不能单靠带大参数尺度的极小 normwise 数字声称逆界。上表列出的则是直接对**原完整 J**
重新计算的绝对及相对 RHS 残差。以上均为 binary64 实测，不是区间逆证书。

## 同一因子的 δ ↔ logq 完整兼容标量

这次只令实际支撑主系数
$q_a=q_{\mathrm{source}}e^\eta$。固定 gauge=.06、warp=.06、原 $p$、
所有高阶**实际物理**支撑系数、$\delta$ 及完整 $g$，以相同的两个步长差分
整个 $F$，得到 $v_q=\partial_\eta F$。
它不是把原 $p_0$ 偷换成 $\eta$，也不是只换 core key 而沿用旧 lift。
实际两完整列相对差为 $6.217328342495664\cdot10^{-10}$。

复用同一个 $J_{\mathrm{design}}$ 与同一个因子，解

$$J_{\mathrm{design}}w=v_q,\qquad S=w_{p_0}.$$

若该完整 $J_{\mathrm{design}}$ 可逆，将它的 $\delta$ 列替为 $v_q$ 后，
新矩阵的行列式与旧矩阵行列式之比准确为 $S$：这是按被替换列展开或
矩阵行列式引理的有限维恒等式，包含原全部边界行。

| 实际观测量 | 值 |
|---|---:|
| 细步长 $S$ | $2.4696192160526124\cdot10^{-5}$ |
| 粗步长 $S$ | $2.4696202174156057\cdot10^{-5}$ |
| 标量相对步长差 | $4.054726278458446\cdot10^{-7}$ |
| 整个 $w$ 的相对步长差 | $3.148277546826878\cdot10^{-7}$ |
| 原完整 $Jw-v_q$ 最大绝对值 | $2.9346259328175067\cdot10^{-16}$ |
| 相对原 RHS 的完整 $\ell^2$ 残差 | $1.9086532647443288\cdot10^{-15}$ |

这是当前实际非线性有限场上的非零数值 Schur，具有两步长稳定性检查，
不是旋转背景二维模型的外推，也尚不是严格非零区间证明。
可据此直接尝试已有原 support `fixed=True` 族的同 $\lambda$/同 $g$ 精化；
本次线性检查本身没有执行该精化，也没有支付 full DN。

## λ=.004 的未接受预测与来源

以 $\Delta\lambda=.002$ 形成全部 $Y,p$ 的切线初猜，原节点、中点、
两个 RMS 离中点域检查全部通过。预测实际 $\delta=.06413456271678726$，
完整残差最大值 $1.73538684578034\cdot10^{-6}$，主要在入口行。
该包没有调用 BVP，没有全 metric 接受，未替换 design 代理正在运行的原 .004 场。

本次总实际用时573.256549147秒；一个 J/因子供四个方向使用。
执行源为
`held10-design-work/design-material-recovery-20261128/lambda002_m24/run.json`；
输出为 `held10-analytic-work/lambda002-m24-tangent-v1/`。

| 对象 | SHA-256 |
|---|---|
| 源 run.json | `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891` |
| 源完整 raw | `4f5033800dab66e46125d8e88fc4d0eb4dbacfc5dd6d1bd8f7808a74f9193616` |
| 源完整 physical | `b9a61ae87a80f550daf98417e0cf2c39d12e3150a974fb8c904aa3d21cc7d1b0` |
| 实际标量 JSON（上方原样副本） | `ca7960d4f01cb4727a716cbfe1c7f6b0fc66fec8fd1838713c611d27edf8add8` |
| 切线入口源码 | `acd94b154e2e0e6422e626af6e80a820d50e7c1f8dca1e1f793d79378c7dc14f` |
| 解析 λ 列源码 | `b748fc592ab3a4b46697f9e15354efa2c991eb279f976d3f428ade44c139aece` |
| QR 源码 | `ad93895f46ca1acfca45a1e43245513d7d4bbedc43c3526c764584ffc2ce9bb5` |
| 完整方向文件 | `2022a844765a9557b2347334563cab6e6030bc95bb337e1cff5597353ddf2791` |
| 未接受的 .004 初猜 | `ad439b68799a21872bec9023168699698a3a4c018018e4575c48218d55fe6f8e` |

复现入口参数为 `--target-lambda .004 --rhs-block 32 --jac-block 32
--compare-analytic-lambda --compare-q-schur`，另外传入本会话 repo、上述真实 source-run
与一个新的 outdir。执行入口与所记录依赖的哈希、恢复逐位核对及所有统计均在原样 JSON 中。
