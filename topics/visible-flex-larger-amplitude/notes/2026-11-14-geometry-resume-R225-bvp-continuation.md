# 从短转弯 BVP 接至真实转弯末端

作者：geometry_design，AI 辅助，2026-11-14。

**状态：给正在排队的 M48/M64 实际边值问题提供完整续算定义和代码；尚没有它们的成功输出。** 已提交的 `geometry_20261114_r225_high_core_bvp.py` 不改动。新 `geometry_20261114_r225_bvp_continue.py` 读取该程序的结果、保留其自适应网格，并把端点从 `.955` 逐步移至同一转弯的实际末端 `1.2076613485893157`。不把首个短域当作转弯或闭合完成。

## 两端条件的维数

未知有限状态为 $r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M$，共 $3M+2$ 个。核心条件为 $r_0=1$、原 R225 前 32 个 $r_j=c_j$、所有 $t_j=-2jr_j$、所有 $z_j=0$，共 $2M+34$ 个。余下 $M-32$ 个自由核 support 模由末端每个高模的一个条件决定。高核系数改变后，法角表达的 $\rho_0$ 与 $g$ 也改变；各个续算阶段属于设计延拓，不称为同 g 加密。

## 末端条件及它在转弯结束处的极限

对于轴对称背景，记 $v=a'$、$\beta=\sqrt{1-v^2}$，对一个角频 $n=2j$ 的线性扰动定义

$$
\zeta=vr+\beta z,\qquad \eta=-\beta r+vz.
$$

由原 Frenet 方程在圆纬线处线性化，先得

$$
r'=-\frac{v(n^2-1)}a r-\frac{\beta n^2}a z,
\qquad
z'=\frac{v^2(n^2-1)}{a\beta}r+\frac{vn^2}a z.
$$

再微分以上变换，使用 $\beta'=-va''/\beta$，得到完整的二乘二瞬时系统

$$
\begin{pmatrix}\zeta'\\\eta'\end{pmatrix}
=\begin{pmatrix}0&A\\B&d\end{pmatrix}
\begin{pmatrix}\zeta\\\eta\end{pmatrix},\quad
A=-\frac{a''}{\beta},\quad
B=\frac{a''+(n^2-v^2)/a}{\beta},\quad d=\frac va.
$$

本次高模在转弯内部满足 $A,B>0$。正特征值是 $\lambda_+=(d+\sqrt{d^2+4AB})/2$，对应左特征向量可取 $(B/\lambda_+,1)$。程序将其归一化，并对高模施加

$$
\frac B{\lambda_+}\zeta+\eta=0.
$$

这是轴对称线性化的增长方向消除条件，用作大非轴 BVP 的 WKB 边界设计；没有把它宣称为完整非轴系统的精确稳定流形。

到转弯末端，$a''\to0^-$、$v\to-.6<0$。此时 $A\to0^+$，$d<0$，$\lambda_+\sim AB/(-d)$，所以归一化的左特征向量趋于 $(1,0)$。因此条件连续趋于

$$
\zeta=vr+\beta z=0.
$$

新 adapter 在实际转弯末端恰好切换到已有 `--terminal cone`，避免直接计算 $B/0$；没有换原 PDE 或人为滤掉高模。

## warm 格式和实际续算

已提交程序的结果包含 `M,N,mesh,states,rhs,parameters,original_metric_identity,turn`，这就是 adapter 接收的格式。`states` 和 `rhs` 与 `mesh` 一一对应；径向排列是每行完整 $3M+2$ 系数。adapter 从这些值恢复原 collocation 的三次 Hermite 场，保留全部已求出的自适应节点。新增的很短区间用保持纬线形状的同尺度延拓作为初猜，平均高度用给定 $a'$ 积分；该初猜不称为解。它的所有点域以及 collocation 中点域在原 Frenet 根式下实际检查，不使用 clipped 根式。

初始端点增量 `.005`，成功后最多增至 `.015`；不收敛则减半并留下失败结果。每个成功阶段都要求原 solver success、原 collocation 容差和边界残差满足设定、核心采样 $\rho_0>0$、保存站点均在点域。曲率、真实度量误差、G 费用仍随输出保存，不因短 BVP 收敛而被认证。最小步长或本次运行的阶段预算用完时，仅保存可继续的实际状态；不得据此宣称研究完成。

```bash
python computations/geometry_20261114_r225_bvp_continue.py --initial CI_RESULT.json.gz --seed notes/2026-11-14-geometry-resume-R225-full-spectrum-seed.json.gz --out-dir CONTINUATION --initial-step .005 --maximum-step .015 --max-nodes 1600 --tol .000002
```

`CONTINUATION/progress.json` 持续记录每次尝试、每个真正收敛的端点和结果 hash。`--prepare-only` 只构造下一阶段 warm 与 argv，明确记录未执行 BVP。

## 完整闭合仍需后续条件

本转弯末速度是 `-.6`，不能把它接一个很长的 `-.6` coast 就误认为尺寸预算已经保住。下一段需要在真实点域内继续将速度转向接近 `-.98`、进入有限回环、接原尾部并完成全部末端匹配；全部低模匹配与完整核心形状之间也仍有设计自由度问题。真 A 的实际纬线读出显示，进入陡降以前 $a\kappa_{\rm lat,min}$ 已从约 `.90` 增至 `.989`；R225 当前入口约 `.495`，因此圆化必须由真正的场求解完成。全闭 $D$、图像 Hausdorff、逐点固定 H、含反射的 E(3) 及全时连续 reach 沿用 README 原定义。
