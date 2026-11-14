# 偏心双圆领的直接 Cartesian 有限设计试验

日期：2026-11-14。独立推导和公开课题定义；没有使用私有来源的数据、公式或研究摘要。

**状态：实际运行的有限设计搜索；没有得到合格的活动环带，更没有完成闭曲面、reach 或固定度量收敛证书。** 本文件的失败结论仅针对列出的离散空间和初值。两圆领相位机制见 `../results/R1-eccentric-collar-phase-bearing.md`；混模的局部精确依据见 `../results/R2-mixed-modes-local-eccentric-drift.md`。

## 1. 可执行模型

脚本 `../scripts/eccentric_collar_search.py` 采用三分量 Cartesian Fourier × 五次 B 样条。径向未知基函数在两段真正开圆领上恒零，且在活动区两端具有零二阶 jet。左领固定，右领由预先规定的横向偏心 $e$ 和绕 $y$ 轴倾角刚体放置，因此位置、标架及完整位置二阶 jet 是表示本身的约束，不是有限边界点上的罚项。

参考母线定义为

\[
\beta(s)=\pi S(x)+b\sin(2\pi S(x)),\quad
a'=\cos\beta,\quad z'=\sin\beta,
\qquad S(x)=10x^3-15x^4+6x^5,
\]

其中 $S$ 在活动段外截成 $0$ 或 $1$。本轮 $L=2$，初始圆半径 $.45$，每侧开圆领长 $.12$，$b=.9$。该母线中间有 Gauss 曲率改变符号的区域。积分用 96 点 Gauss 求积计算；此处没有给积分舍入误差的严格上界。

`--metric-mode fixed` 固定 $g=ds^2+a(s)^2du^2$。`--metric-mode angular-design` 仅消除 $E,F,G$ 的角依赖，径向三个均值自由。这是设计另一个度量，绝不是同一目标度量的精化。

最新的自由度量目标以径向均值归一化角残差，并在有限配置点惩罚

\[
\bar E-\bar F^2/\bar G<.1,\qquad
\bar G/a_{\rm ref}^2<.1,\qquad
\bar E>4,\qquad \bar G/a_{\rm ref}^2>4.
\]

这些是软约束，不能代替连续区间的非退化或尺度证书。报告另在 65、129、257 个径向点和至少 64 个角点计算相对均值度量的算子范数。采样加密只是独立检查；没有宣称连续误差上界。

解析 Jacobian 用随机方向中心差分核验：固定度量相对差 $1.07\cdot10^{-10}$；自由度量的归一化及激活障碍项分别给 $1.08\cdot10^{-10}$、$4.77\cdot10^{-10}$。零偏心圆母面在相同评估器下的相对度量误差为 $4.80\cdot10^{-16}$。这些只核实现一致性。

## 2. 已运行的有限结果

所有偏心均沿 $x$ 轴，倾角为零。数据文件包含小系数向量、参数、运行源码 SHA-256、求解器状态和独立采样指标，没有大网格。

| 文件（本目录） | 空间与求解 | 偏心 | 257×64 的相对度量误差最大值 | 结果 |
|---|---|---:|---:|---|
| `eccentric-search-fixed-002-small.json` | 固定 $g$；10 个径向控制点、4 阶 Fourier、每段 3 个 Gauss 点；7 次函数评估 | .02 | .0072296714 | 求解器成功停止，但等距残差明显不合格 |
| `eccentric-search-design-002-small.json` | 原始绝对角差目标；10/4/3；100 次评估 | .02 | .96474808 | 被度量退化排除 |
| `eccentric-search-design-002-normalized.json` | 归一化角差、无尺度上界；12/4/4；400 次评估 | .02 | .0059110382 | 被尺寸膨胀和漏采的径向退化排除 |
| `eccentric-search-design-002-bounded.json` | 归一化角差、有上述上下界；12/4/8；300 次评估 | .02 | .0039165293 | 有限设计仍不合格 |
| `eccentric-search-design-020-bounded.json` | 同上，混模初值改为 $.18,-.12$ | .2 | .0211235361 | 有限设计仍不合格 |
| `eccentric-search-design-002-curvature-seed.json` | 固定周长曲率种子；14/6/8、32 角点；151 次评估 | .02 | .0003338331 | 本轮最低真采样误差，仍不合格且曲率过大 |

前四行的径向扰动初值幅度为 $.08,.08$；最后一行如表。原始绝对角差目标虽然使未归一化角差降到 $10^{-3}$ 量级，却使 Schur 补降至 $8.87\cdot10^{-4}$，某些圆周方向的均值度量也接近零，采样主曲率超过 $1.24\cdot10^4$。这是明确的假改善。

第二种假改善出现在无尺度上界的归一化版本：配置点残差最大值约 $1.78\cdot10^{-6}$，内部横向跨度却增至约 $1.246\cdot10^4$。而在 4097×32 的额外检查中，$s=.1337890625$ 附近的相对度量误差达到约 $1.5166$，Schur 补仅约 $3.85\cdot10^{-5}$。不能用配置点精度声称得到候选；也不能通过无限增大整个形状让固定绝对偏心相对消失。

加入尺度上界后，两个 bounded 输出的 Schur 最小采样值均约 $1$，最大 $\bar E$ 约 $4.036$ 和 $4.004$（软约束有少量越界），采样主曲率最大值约 $3.73$ 和 $4.30$。没有计算全域嵌入、闭帽、固定握持像位移或 reach，因此这些数不构成几何达标。

固定周长曲率种子把误差进一步降到 $3.34\cdot10^{-4}$。`eccentric-search-design-002-curvature-dense-audit.json` 对同一系数做 4097×128 检查，最大相对误差为 $.0003348938814$，Schur 最小值约 $.12413$，最大主曲率约 $75.0416$，横向跨度至少 $2.51245$。因此即使随后修好等距残差，这个形状仍有明显的曲率/reach 必要条件瓶颈：采样估计的 $1/(D\,\max|\kappa|)$ 仅约 $.00530$，低于目标 $.03$。这里不是 reach 下界，也没有用它宣称连续证书。

## 3. 圆母面的一阶 $m=1$ 锁死是可证明的

设圆母面为

\[
X(s,u)=a(s)e_r(u)+z(s)e_z,\qquad a'^2+z'^2=1,
\]

且活动段内部 $z'>0$。取余弦型一阶角模的无穷小变形

\[
V=F(s)\cos u\,e_r-F(s)\sin u\,e_\theta+H(s)\cos u\,e_z.
\]

这里横向两个系数由线性化的 $\delta G=0$ 约束联系。其余线性等距方程准确为

\[
a'F'+z'H'=0,\qquad aF'+z'H=0.
\]

在 $z'>0$ 的连通区间代入第二式得到

\[
F''=\frac{z''}{z'}F',\qquad
F'=Cz',\qquad F=Cz+D,\qquad H=-Ca.
\]

故

\[
V=D e_x+C(e_y\times X),
\]

恰好是全局刚体平移和转动。正弦型有相同结论。连续接到已固定的开圆领时，因为该领半径正，必须 $C=D=0$。所以不能从该圆母面通过一个一阶等距 $m=1$ 分支产生相对偏心。

这一结论也适用于一阶允许径向均值度量改变的设计：基点的 $m=1$ 度量变化只有 $m=1$ 角频率，不能由角无关的目标度量变化吸收。它**没有**排除更高阶非线性分支、非圆 seed、曲率退化引出的特殊延拓或允许不同端姿态的其他构造。

## 4. 当前加入的非圆 seed

脚本的 `--seed-kind curvature` 使用

\[
\rho=a(1+A\cos2\varphi+B\cos3\varphi),\quad
h=a(1-\tfrac A3\cos2\varphi-\tfrac B8\cos3\varphi),\quad
\Gamma=hn+h't,
\]

以及材料角

\[
u=\varphi+\tfrac A2\sin2\varphi+\tfrac B3\sin3\varphi.
\]

只要 $|A|+|B|<1$，该变换单调，截面严格凸、准确闭合，且 $|\Gamma_u|=a$。种子的径向 $A,B$ 以零二阶 jet 的 bump 衰减到零；$B$ 额外乘非对称因子，避免强制上下镜像。每个截面的材料平均中心原样保留；没有逐层置中。然后把这个解析截面族投影进有限 Fourier/B 样条空间；**投影后的种子及其经向度量仍然只是近似设计数据**。

后续若某输出达到有希望的角不变性，须冻结其完整角平均度量、几何端口、相位和物理尺度后再建立真正精化链。目前尚未进行这一步，因为上表没有合格候选。

## 5. 复现入口

从公开仓库根目录运行，例如 bounded 的小偏心试验：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/eccentric_collar_search.py \
  --controls 12 --modes 4 --radial-order 8 --angles 24 --offset .02 \
  --seed2 .08 --seed3 .08 --max-nfev 300 --metric-mode angular-design \
  --out topics/visible-flex-new-mechanism/notes/eccentric-search-design-002-bounded.json
```

固定度量试验改为 `--metric-mode fixed --controls 10 --radial-order 3 --max-nfev 100 --linear-spectrum`。大偏心 bounded 试验改 `--offset .2 --seed2 .18 --seed3 -.12`。

旧绝对角差退化诊断可用 `--design-objective absolute --controls 10 --radial-order 3 --max-nfev 100` 重放；此选项刻意关闭障碍项，仅保留旧诊断目标。旧无限放大诊断使用 `--design-objective relative --design-ceiling 1e300 --controls 12 --radial-order 4 --max-nfev 400`。旧诊断的源码哈希与当前脚本不同，但对应目标作为显式选项保留；不将浮点迭代轨迹的逐位一致作为保证。

非圆种子试验入口为 `--seed-kind curvature --seed2 .35 --seed3 .25 --seed-asymmetry .3 --controls 14 --modes 6 --radial-order 8 --angles 32 --offset .02 --metric-mode angular-design --max-nfev 350`。上述小运行是实现及设计筛查；需要更大计算时可直接把同一命令放进公开仓库自己的 GitHub Actions。
