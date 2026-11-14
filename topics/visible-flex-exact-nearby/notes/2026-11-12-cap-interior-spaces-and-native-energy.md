# 物理 N4 帽端口的内部空间与首批真实能量积分

2026-11-12，reproduce-newton；接 R88。对象始终是准确显式对称仿射
\(\delta_5=-7789843107295549/4611686018427387904\)。本记录不将
canonical 剪切角的低指标与物理 \(\theta\) 的 Fourier 指标等同。

**已完成：** 固定物理边界 \(|k|\le4\) 和 regular 均值端口，比较了
更丰富的内部 trial/flux 空间；保存了 N16/P2 的实际有限函数；给第一个
真实共同 body span 付清无限 primitive、角混叠、径向积分与舍入误差。
全帽积分、全部低高交叉及最终无限维逆仍未完成。

## 1. 一次几何积分，多种有限内部空间

`fourfold_phase_cap_moment_space.py` 将原真实 body、自然 C4 graft 与
R74 无限尾保持分开。一次浮点几何遍历保存 \(\mathsf B\) 和
\(\mathsf B^{-1}\) 的全部 lag \(|l|\le32\)、每个 FE 单元归一径向
幂次 0 至 6 的矩。每个实际共同样条 span 都单独积分；这份矩缓存
仍是浮点探索，不能单独给真实能量的上下界。

在同一 72 元网格上，仅改变内部空间；边界始终为物理 N4，加上
regular 端的真实均值 \(\xi\)。

| 内部角指标 | 径向 degree | 浮点 upper−lower 的谱范数 |
|---:|---:|---:|
| 4 | 1 | 0.08882033568727661 |
| 4 | 2 | 0.06871112357039849 |
| 8 | 1 | 0.030822544975777563 |
| 8 | 2 | 0.005862046652668079 |
| 8 | 3 | 0.005606247475412695 |
| 16 | 2 | 0.0013340250327668862 |

选定 N16/P2 继续积分，未盲目扩大边界矩阵。所存
`cap-space-boundary4-interior16-P2.npz`（文件全名见相邻 manifest）
中的二进制数解释为**准确 dyadic 系数**，因此它们定义具体有限函数，
不要求浮点线性求解本身准确。主 trial 连续 P2；非零模通量 \(p_k\)
连续 P2，\(q_k=-p_k'/(4ik)\)；\(p_0\) 是一个全区间常数，
\(q_0\) 在每元线性。故散度及法向通量连续性都是准确恒等式。
主 trial 在两端准确满足保留端口的迹条件。

源码注释中 “exact constant trial” 的说法只对所意图的代数组合准确，
不能免费授给已经舍入的两个保存列。逐个准确二进制分数检查表明，
N16/P2 两个均值输入列在 38 个内部径向节点相加与 1 相差最多
\(2^{-54}\)。边界条件不受影响；dual 两列互为准确相反数。下面
始终按**所存实际 trial** 积分，因此 R88 对任意 admissible trial 的
互补能量恒等式仍原样适用。此处不声称主有限矩阵具有准确常数核。

重放浮点空间选择：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_moment_space.py build \
  --out notes/2026-11-12-actual-cap-Fourier-moment-cache.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_moment_space.py solve \
  --cache notes/2026-11-12-actual-cap-Fourier-moment-cache.json \
  --boundary-modes 4 --interior-modes 16 --radial-degree 2 \
  --out notes/2026-11-12-cap-space-boundary4-interior16-P2.json
```

严格积分只需要已保存 trial NPZ、对应 trial/cache JSON 以及真几何输入。
可重建的 2.65 MB 浮点矩缓存 NPZ 不是严格积分的数学输入。

## 2. 首个真实共同 span 的有向能量矩阵

`fourfold_phase_cap_energy_interval.py` 用原真实区间几何，完整覆盖
\[
 [1/4,\,4528886369647159/18014398509481984].                 \tag{1}
\]
四个 dyadic 子区间均通过，未越过共同样条 span 或 FE 边界。
实际 P2 主 trial 与准确散度自由 flux 的能量矩阵都完整保留 10 个
输入列。没有以个别基向量的抽样代替矩阵算子范数误差。

对每个积分区间中心 \(c\)、半宽 \(h\)，在同一真实 scalar germ 的
复盘 \(|r-c|\le R\) 证明有限角梯形能量矩阵解析且模数不超过 \(M\)。
径向上的有限 trial 系数共轭多项式取其解析延拓；不把复杂变量本身
共轭后仍称全纯。真 n 点 Gauss–Legendre 的根、正权与常数矩均由
Arb 支付。由于它准确积分 degree \(2n-1\)，径向完整误差为
\[
 \varepsilon_r\le4hM\frac{(h/R)^{2n}}{1-h/R}.             \tag{2}
\]
这里同时支付真积分与正权求积的完整无限 Taylor 尾。

另在真实实径向区间、归一角 \(x=4\theta\) 的完整复带宽 \(s\) 上
支付每个 form 系数的模数。内部指标 N16 只需 lag \(|l|\le32\)，
Q=1024 角梯形规则的完整系数 alias 不超过
\[
 M_\theta\frac{e^{-s(Q-32)}+e^{-s(Q+32)}}{1-e^{-sQ}}.       \tag{3}
\]
每个实际无限 primitive 的尾先进入径向节点、径向外盘和角带的
系数球，故 (2)、(3) 都没有换成有限 primitive 的误差。最终准确
Hermitian dyadic 中心与有向矩阵的距离用完整 Frobenius 上界支付。

首版使用 n=10、R/h=4、s=1/32、primitive Q=512、160 bits；CPU
18.05 秒。报告保留所有失败父盒、细分区间、真节点/权、两个能量
矩阵及每一项误差。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_energy_interval.py --gauss-order 10 \
  --out notes/2026-11-12-cap-true-energy-first-span.json
```

## 3. 准确消去公共半径幂

`fourfold_phase_cap_scaled_body.py` 保持同一图，只将单位切向差的原函数
\(P=\mathcal P(T-T_{\rm circle})\) 先算出，再用
\[
 F=(a(1+P_1),aP_2,Z+aP_3),\quad
 L=a'/a,\quad C=Z'/a^2,
\]
\[
 u=LP+P',\qquad u'=L'P+LP'+P''.
\]
令 \(e=2L\langle u_1\rangle+\langle u\cdot u\rangle\)，则
\[
 E=a^2\overline E,\quad \overline E=L^2+a^2C^2+e,
\]
\[
 K=\frac{C^2(L^2-L')+LCC'+(Le'-2L'e)/(2a^2)}{\overline E^2}.
                                                                    \tag{4}
\]
相应几何 moving-frame 量准确满足
\(D=a^2D_2, M=a^2M_2, W=a^2W_2, H=aH_1\)。因此真实 form 仍是
\[
 \alpha=F_z^2D_2/H_1^2,\quad q=-M_2/D_2,\quad
 \kappa=F_z^2W_2^2K/(D_2H_1^2),\qquad
 \mathsf B=\begin{pmatrix}\alpha&\alpha q\\
                    \alpha q&\alpha q^2+\kappa\end{pmatrix}.        \tag{5}
\]
没有额外缩放算子或丢掉原来的密度。

\(L,C\) 通过固定 dyadic 常数加准确多项式余项求值；\(L',C'\)
先将分子多项式乘开，再有向除以同一半径。单位原函数的全部 R33
Fourier 尾去掉的是原先的公共 \(|a|\) 因子，其余真尾不变；(4)
中的 e,e′ 另付完整零、一次、二次径向原函数误差。换到下一个真实
共同 span 时清理旧 scalar/raw-germ 缓存，不跨全体区间累计大缓存。

三个真点 \(r=1/4,1,3\) 的 K 以及 B、B⁻¹ 六个分量均与首版真实
native 球相交。这是实现交叉检查，不是跨点覆盖证书。随后同 (1)
的完整四区间积分也实际通过：主能量矩阵的总误差小于
\(6.68\,10^{-11}\)，dual 能量总误差小于 \(5.38\,10^{-9}\)，
CPU 14.86 秒。首版输入与报告未覆盖修改。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_scaled_body.py \
  --out notes/2026-11-12-cap-scaled-body-point-comparison.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_scaled_body.py --energy-element 0 \
  --energy-span 0 --gauss-order 10 \
  --out notes/2026-11-12-cap-scaled-true-energy-first-span.json
```

## 4. 互补能量与后续完整帽的合同

对所选准确 trial/flux，R88 给真帽 S 的 Loewner 包络
\[
  T+T^*-D\le S\le E.
\]
若完整主/dual 能量的选定中心为 \(\widehat E,\widehat D\)，其真算子
误差分别是 \(\epsilon_E,\epsilon_D\)，可选
\[
 C_*=(\widehat E+T+T^*-\widehat D)/2,
\]
\[
 \|S-C_*\|\le\tfrac12\|\widehat E-T-T^*+\widehat D\|
                   +\max(\epsilon_E,\epsilon_D).                   \tag{6}
\]
这里 T 由准确 finite flux 的边界迹定义，含保留均值端口。当前只有
(1) 的积分完成，不能把浮点表的 0.001334 直接放入 (6) 宣称真帽已证。
仍须逐一支付其余 body、真实自然 graft、真 \(\Gamma_H\) 与逆的尾端
能量、全部矩阵相加舍入。完整双通道核心/低高反馈也另有其预算。
