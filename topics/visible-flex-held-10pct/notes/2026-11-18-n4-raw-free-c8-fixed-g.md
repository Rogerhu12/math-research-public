# n4 raw 控制：显式释放 c8 的固定 g 精化入口

维护：Astra-held10-7322d0de-20261118；2026-11-18（UTC+8）。

## 参数选择

双物理设计使用 $\delta,v_d$ 与 $M-2$ 个互补控制，共 $M$ 个未知。固定设计所得的整个物理 $g$ 后，沿用已有固定度量方法：保持 $\eta=0.1$，让实际主幅度 $q$ 与全部 $M-1$ 个 mean-zero 控制成为未知，并**显式释放 $c_8$**。这是固定 $g$ 分支的参数声明；不再声称设计分支的 $c_8=0$ 条件贯穿新的求解。

新入口 [`refine_fixed_raw_n4.py`](../scripts/resume_n4/refine_fixed_raw_n4.py) 复用原 `build_seed` 的完整物理 profile、实际 port、材料图投影、入口修复、原解析参数 jets、BVP 方程和所有接受门。仅替换 raw 核心工厂及其严格嵌套方式。核心与控制源码为 [`raw_fixed_core.py`](../scripts/resume_n4/raw_fixed_core.py) 和 [`raw_n4_free_complementary.py`](../scripts/resume_n4/raw_n4_free_complementary.py)。

## 新增的一个控制列

沿用 [raw mean/c8 定义](2026-11-18-n4-raw-mean-c8-controls.md) 的 $W$ 和加权 Gram 矩阵 $G$。所有 $j\ge3$ 列仍取对 $\{1,\cos(8\phi)\}$ 投影后的 $R_j$，均值及物理 $c_8$ 矩都为零。第一列改为

$$
U_2(\phi)=W(\phi)\left[\cos(8\phi)-\frac{G_{02}}{G_{00}}\right].
$$

它的均值为零，而物理 $\cos(8\phi)$ support 系数为

$$
a_2=2\left(G_{22}-\frac{G_{02}^2}{G_{00}}\right)>0.
$$

严格正性来自 $1,\cos(8\phi)$ 的加权 Gram 正定性。定义中所有矩都有原有理区间包围。本组参数的 $a_2$ 约为 $0.68114793751065$；独立分段 Gauss 审计给出所有列均值残量不超过 $4.79\times10^{-15}$、其余列的 $c_8$ 残量不超过 $8.09\times10^{-15}$。正式记录保存了向外舍入的 $a_2$ 上下界。

写 $V_j=W[\cos(jn\phi)-G_{0j}/G_{00}]$。因为 $U_2=V_2$，且每个 $R_j$ 只是从 $V_j$ 减去一个 $V_2$ 的倍数，$\{U_2,R_3,\ldots,R_M\}$ 与 $\{V_2,\ldots,V_M\}$ 张成的 mean-zero raw 空间完全同 span。高矩 canonical 逆没有重新引入。

新增第一列的 $\lambda=0$ 端仍为冻结原 $J=16$ 的

$$
L_2^{(J)}=\cos(8\phi)+\ell_2^{(J)}\cos(4\phi),
$$

并取 $(1-\lambda)L_2^{(J)}+\lambda U_2$。设计初值中该列系数为零，所以释放它不改变旧核心。其物理 $c_8$ 系数沿同伦为 $(1-\lambda)+\lambda a_2>0$，不会在 $\lambda=1$ 消失。其余列保持原冻结 $J$ 的 raw 同伦。

所有 endpoint 列仍在保护弧外紧支，故在 $\lambda=1$ 不改变圆弧。$\eta$ 保持 0.1，圆弧半径依然按实际求解幅度 $q$ 计算，而不是另行改变 bimodal 比例。

## 有限核心坐标的非退化性

按照物理 support 的 $2n,3n,\ldots,Mn$ 矩排列，endpoint 的列矩阵具有块下三角形式

$$
A=\begin{pmatrix}a_2&0\\ b&D\end{pmatrix},
$$

其中 $a_2>0$，$D$ 是对低块 $\{1,\cos(8\phi)\}$ 作 Schur 补后的严格正定 Gram 矩阵的两倍。原低端矩阵为单位阵；$\cos(4\phi)$ 漏量不影响这些高矩。因此整个控制同伦的高矩矩阵为 $(1-\lambda)I+\lambda A$，其对角块保持严格正定，有限核心坐标在 $0\le\lambda\le1$ 均线性独立。这是控制坐标的结论，并不保证非线性 BVP 的 Jacobian 可逆或完整误差收敛。

## 实际 λ=0.02 的 M16→M20 初值身份

本入口已从 [raw $\lambda=0.02$ 终态](2026-11-18-n4-raw-lambda002.md) 实际构建固定 $g$ 的 M20 初值。冻结值为

$$
\delta=0.030158202455449618,\qquad v_d=0.25018727173023186,
$$

以及整个实际物理 profile 与新 $w_{\mathrm{cut}}=0.16$ port。$J=16$ 与旧漏量定义保持；全控制补零后旧 $c_8=0$ 不变。`parameters + central_correction_scales` 定义核心，显示摘要只作一致性诊断。

| 真正执行的初值检查 | 最大误差 |
|---|---:|
| 完整 $F$ | $2.77556\times10^{-17}$ |
| 完整 $F_u,F_{uu}$ | 0 |
| 完整材料图投影 | $4.44089\times10^{-16}$ |
| 输入 763 点的覆盖 | $1.11022\times10^{-16}$ |
| 入口系数修复 | $4.31252\times10^{-15}$ |

这里 $u$ 是弧长材料角；记录键 `Ft/Ftt` 不表示法角导数。加入分段点后初值为 766 点。

原解析全参数 Jacobian 的独立方向差分误差随步长 $0.003,0.001,0.0003$ 由 $2.93\times10^{-7}$、$3.23\times10^{-8}$ 降至 $4.87\times10^{-9}$；BC 参数 Jacobian 最大比较误差约 $2.82\times10^{-10}$。实际边值求解随后使用原容差 $10^{-8}$、M20、角求积 1280 和网格上限 5000；本条不预支其最终成功。

[`raw_free_fixed_seed_checks.json`](../scripts/resume_n4/raw_free_fixed_seed_checks.json) 由 [`diagnose_raw_free_fixed.py`](../scripts/resume_n4/diagnose_raw_free_fixed.py) 从真实入口日志和独立低矩检查生成，只保留标量、参数及来源 hash。完整求解终态另行登记。
