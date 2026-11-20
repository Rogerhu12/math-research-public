# 2026-11-20：完整物理变量的实际余量不等式 QP

## 当前状态与动机

此节保留启动前准备的实际时点；首完整方向现已返回，详见[实际终态](2026-11-20-fullspace-inequality-first-result.md)。本页小模型及该首方向都是已发生的本地诊断；[执行地点纠正](2026-11-20-public-actions-execution-correction.md)后不再启动新的本地科学计算。

这是一份新求解接口与已完成小凸模型验证的记录，写作时尚未运行完整场的新 QP。前一真实角 H² 方向 `5b1e426a…` 只接受 α=1/32；实际满步新峰的净一阶 κ 增量约 66% 来自 m≤12，约 35% 来自 m≥33。因而没有证据支持继续只加重高模惩罚。

原完整方向把选中的所有几何行同时设为等式 `Cz=0`，会阻止旧峰向内移动。本版本保持同一完整坐标映射和全部永久非线性检查，只把本次线性约束改成有真实余量的不等式。没有删去任何原 field 变量，也没有把旧场的模式冻结。

## 完整二次模型

令 T 为已刊的物理高度可逆三角变换、完整 DI、νc=24 正角向过渡范数和按同范数白化的粗列所组成的完整增量映射。求解

$$
\min_z\ \frac12\|Az+v\|^2+\frac{\mu^2}{2}\|z\|^2,
\qquad C_i z\le b_i.
$$

每一个选中的真实 κ 点与真实直径点给出

$$
r_i=\eta D_i|\kappa_i|,\qquad
g_i=\eta\left(D_i\operatorname{sgn}(\kappa_i)\,d\kappa_i
+|\kappa_i|\,dD_i\right)T,
$$

$$
C_i=g_i/\|g_i\|,\qquad
b_i=(.992-r_i)/\|g_i\|,\qquad \eta=.03.
$$

不另减 .0002 的线性余量，因此不会把已经通过 .992、但高于 .9918 的父偷偷当成零初猜可行。程序明确检查 `z=0` 是否满足全部实际归一化界；若原父不通过，需要另做明确 Phase I/restoration。本版没有声称实现 Phase I，不能把失败父当成零可行父。

protected 表示必须保留于线性工作集合，不表示必须维持等式。其余候选按当前 near-active 产品和最强直径伙伴排序。两条 κ 分支只要有近活动依据均可入候选。工作集合可有界；未入工作集合的历史位置仍永久保留于每个真正非线性试步。后继产生的拒绝峰也继续永久保存。

## 原 Jw 与 p8 模型的区别

driver 支持显式 `--objective jw` 或 `--objective spectral`，不能把不同目标数值相减。

Jw 分支保持原 .5 Simpson + .5 Gauss 径向积分、完整原/新增观察行和精确角轨道 multiplicity。p8 分支接已经独立验证的 exact residual-Hessian 桥：设 k=p/2，C0=sum(w_s)N，

$$
A=\sqrt{k/(s_0^2 C_0)}\,\sqrt{w_s}\,B\,J_{\rm native}T,
\qquad B^TB=T_{\rm raw}^*Dh(E)T_{\rm raw}.
$$

虚拟右端为

$$
v=\sqrt{k/(s_0^2 C_0)}\sqrt{w_s m_\alpha}\,
B^{-T}T_{\rm raw}^*h(E).
$$

因此 `Aᵀv` 是真正归一化 Φ 的半梯度；不能用 `B*r` 代替此虚拟右端。cross 的 Frobenius 因子已在 B 内，角轨道也只计算一次，不另外乘 sqrt(2)。p=8、ε=.001、s0=.05 时外侧 half-Hessian 系数为 `1600/C0`；当前 C0=4856.422137302683。

`||v||²` 不是实际 Φ，报告不会这样标记。非线性试步必须直接重算同一固定参数的 Φ，并同步记录 Jw、全部 raw 与 legacy raw、最大相对 Gram。实际 Φ 的二阶模型为 `Φ0+2<v,Az>+||Az||²`；此 residual-Hessian 不是完整 x-Hessian，也不是 p>2 的 MM 上界。

正则项 `µ²||z||²` 已在平均 Φ 单位内，不再乘除 C0 或 1600。本完整 T 使用新的 νc24 范数，且联加粗列的商范数在母范数约 1/2–1 之间；不能宣称与 geometry 的旧粗 G 在相同 µ 下完全相同。

## 可行 active-set CG

从已核实可行的 z=0 出发，初始活动面为空。每一个真正 CG 前进只使用一次 A 与一次 A*，与 matrix-free LSMR 的每轮场乘积同阶。

1. 在当前活动面上投影负梯度，并以 CG 共轭方向推进。
2. 取二次目标一维极小步长与全部线性不等式允许的最大步长之较小者；碰到新的边界就加入该行并重新开始当前面的 CG。
3. 活动行采用增量两次 Gram–Schmidt 正交，实际 `C_active=RQ`，不先把整个 192 行集合变成等式。
4. 到当前面的驻点时解 `R^T λ=-Q∇q`；若存在负乘子就释放对应行。这样允许原先临界的曲率峰向内下降。
5. 每 32 次真正前进刷新梯度和 literal Cz；最后另外读一次精确梯度、Cz、乘子、互补性和投影驻点残差。达到内迭代数量时只能称截断数值方向，不能冒称 QP 精确最优。

线性可行性、活动行数值独立性或有限算术出现问题都会留下明确状态和当前真实方向，不伪报收敛。一般 QP 只生成方向；真正场的 metric、所有 Gauss 点、全部永久 κ/半径点和后继局部复读决定最终接受。

## 内存与代价

literal C 存在 scratch 的 float64 memmap，Cz 按 32768 列分块读取；活动 Q 只触碰实际活动行。没有构造每个几何行的 `H^-1`，也不需要针对 192 行分别运行 192 次完整 LSMR。

与旧 row builder 相比，半径的完整 1,332,245 维余向量改为按被选中的伙伴惰性生成。137 个永久半径位置只先保存标量和 18 维物理场，不会预先占用约 1.4GB 的全部 full-free 余向量。完整数值峰内存必须由真实运行的 `ru_maxrss` 报告，不能把估算称为实测。

## 唯一必要小模型核验

源 `fullspace_feasible_active_cg.py` 对独立随机 32 变量、28 个单位范数不等式、85 行数据和 µ=.03 的严格凸 QP 作一次检查；seed=2026112007。对照直接在原小模型上调用的 SciPy SLSQP：

- 实际 CG 前进 86 次，发生 3 次负乘子释放；最大活动秩 12，最终活动行 9。
- 最终目标相对差 1.5142488651740485e-15；向量相对差 1.2668339523628394e-7。
- literal 最大约束违背 5.134781488891349e-16。
- 最终面内梯度范数 1.0188910733323891e-9；最小乘子非负；互补残差 3.9062148536429745e-16。
- 活动 Q 正交误差 3.3306690738754696e-16。

这是新 active-set 逻辑的独立凸模型核验，不是再次支付旧 Gram/cotangent 的证明，也不是完整场数值结果。

## 源身份

- `fullspace_feasible_active_cg.py`：15699 B，SHA-256 `5d08f84eb787efc6a754b1d2f3e6974582b5bcb408e524bedfaaf9d01a0aacac`。
- `fullclosed_point_inequalities.py`：8858 B，SHA-256 `5395db01e7c1553c626aafebec8f26cdbe54416b2a16fe58684ad650d823657f`。
- `fullclosed_gauss_inequality_qp.py`：38630 B，SHA-256 `5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a`。
- 小模型实际输出 `feasible-active-cg-small-check.json`：1250 B，SHA-256 `1824b41ec77f2f48f9068fd51e17bb696d1360fefd2d539921206abf5166a453`，仅存 scratch。
- 小模型完整可复现入口 `check_feasible_active_cg.py`：3019 B，SHA-256 `fa70b072dc3e6a458e4ababb72b93f412f6f659c6509a60c8fcbb3bd76513a3a`；它保存已用的精确 RNG 调用顺序，没有另跑一次旧检查。
- exact E-Hessian 桥 `positive_spectral_gram_hessian.py`：SHA-256 `29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4`。
- 原正谱目标 `positive_spectral_gram_weights.py`：SHA-256 `e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91`。

真正父、完整纯位置输入、完整 CLI 和实际方向终态另作同批运行记录；这里不虚构尚未发生的完整预算。

小模型的可复现命令为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/check_feasible_active_cg.py --source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullspace_feasible_active_cg.py --out work/fullclosed_solver/feasible-active-cg-small-check-reproduction.json
```

公开源码路径均对应实际执行的同SHA字节；临时数组沿原输入链再生。纯位置输入若替代原诊断清单，计算语义保持，文件路径与输入清单SHA不冒称原raw报告逐字相同。
