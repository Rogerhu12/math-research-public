# 正向环带筛选与平面椭圆柱起点（2026-11-08）

会话：`Astra-visible-flex-effcccee / repo_amplitude`。仅写本题 notes；HANDOFF 和提交由 root 负责。

**可信度：下列新曲面计算均为数值证据，尚无满足本题完成标准的闭曲面。**
末端 Robin 条件不是圆周边界，也不是无限尾部。`D_cyl` 只是在当前前缀的采样半径/高度基础上形成的包围圆柱对角线；不含未来封帽，也未做区间包围。没有计算本题的全刚体商 Hausdorff 下界或 reach 下界。

## 1. 旧 wavy-core 的小批筛选

脚本 `repo_scan_gentle.py` 复用相邻课题的
`f6root_gentle_inner_cycle_scan.screen`、物理线性 ODE 和真实曲线 Frenet frame。
新增检查直接从一阶参数曲面的第一、第二基本形式计算主曲率，避免把 rotational background 的曲率当作实际曲面曲率。

- 初轮 24 个配置：`repo_scan_initial.json.gz`，小摘要 `repo_scan_initial_summary.json`。
- 调宽 bridge、改变末端坡度的 24 个配置：`repo_scan_wideport.json.gz` 及摘要。
- inward-first 16 个配置：`repo_scan_inward.json.gz`。这些配置与继承的末端线匹配时都要求非正 rectifying halfwidth，故未进入振幅筛选。
- 显式选择初始 halfwidth、反算暂定 Robin 线的 18 个配置：`repo_scan_freeport.json.gz`。它们的末端线仅为设计变量，未提供可实现的 compact tail；没有改善有效大振幅。

原最强 wide-m2 的窄 bridge 从半径 1 到 .98 完成近 87 度转向，在线性背景中已产生约 68 的峰值曲率。把 bridge 展宽确实能减少这个峰值，但不能自动解决幅度问题。

较好的旧型线性样本为

```
delta=.6, vu=.8, vd=.95, ramp=.4, cycles=1,
cut_radius=.7, cut_slope=.05, base_mode=2,
q=.0361328125.
```

其第一阶曲面采样结果为 `kappa*D_cyl≈27.80`、`PV/rmax≈.0447`、
`H/rmax≈1.490`。`PV/rmax` 距预筛目标 .2 仍很远；这不是本题的 δ。

一次旧型完整空间 BVP 小试也已保存于 `repo_scan_bvp_wide_summary.json`：
M4、q=.01 与 .025 的 projected collocation 收敛，但 q=.025 的实际度量分量误差约
`.0009953`，q=.04 的继承初值失去 Frenet 根号域。因此停止扩大旧型 q 搜索。

### 几何公式自身的数值核查

`repo_scan_jets_validation.json` 记录了以下独立计算：

- 物理线性 ODE 的解析一阶导数与中心差分差约 `2.47e-10`。
- 二阶导数与中心差分相对差约 `4.37e-8`。
- q=0 时，从两基本形式得到的曲率与旋转曲面公式差 `2.66e-15`。
- q=0 时相对度量分量误差 `4.44e-16`。

这些检查只核实筛选器所用公式的实现，不把一阶曲面提升为等距解。

## 2. 平面椭圆柱为什么是不同的起点

设平面椭圆为

\[
\gamma(\phi)=(R\cos\phi,r\sin\phi,0),\quad R\ge r>0,
\]

以弧长除以平均速度 `a0=length(gamma)/(2*pi)` 参数化为 `gamma(theta)`。
广义柱

\[
F(x,\theta)=\gamma(\theta)+x e_z
\]

具有精确度量 `dx^2+a0^2 dtheta^2`。柱长只改变平移，不改变非均值截面，
所以旧 BVP 的 halfwidth 控制在此退化，不能原样使用其 Jacobian。

本地实现是 `repo_scan_ellipse_core.py:PlanarEllipseCore`。它使用明确的平面
Laurent 多项式曲线、谱弧长积分与单调 Newton 反演，而不是把 φ 当成 θ。
对轴比 2 的无修正椭圆，将 a0 归一为 1 后有

```
R = 1.2970467848202847
r = 0.6485233924101423
kappa_min = 0.38549110629751004
kappa_max = 3.0839288503800804.
```

椭圆的精确曲率公式为

\[
\kappa(\phi)=\frac{Rr}{(R^2\sin^2\phi+r^2\cos^2\phi)^{3/2}},
\quad \kappa_{\min}=r/R^2,\quad \kappa_{\max}=R/r^2.
\]

空间 Frenet 方程使用

\[
F_s=\alpha N+\sqrt{1-\alpha^2}\,B,
\qquad \alpha=-\frac{a'}{a\kappa}.
\]

因此在截面仍为给定椭圆时必须有 `abs(a')<a0*kappa_min`。上述 2:1 椭圆的
初始限制是约 `.3854911`。这不是后续所有位置的速度上界：截面改变后要按其
实际曲率重算。慢启动、随后加速的可能性尚需实际非线性解检验。

精确未投影方程自动给出 `|F_s|=1`、`<F_s,F_theta>=0`，且
`d_s |F_theta|=(a'/a)|F_theta|`。若存在满足相应初值的精确解，其度量即为
`ds^2+a(s)^2 dtheta^2`。下面的有限 Fourier 数值解仍有投影缺陷，均另行计算。

### 初始椭圆也必须加密

`repo_scan_ellipse_core_data.json.gz` 保存各轴比、M=2/4/8/12/16 的投影检查。
精确弧长参数曲线本身的度量误差约 `4.4e-16`，不等于它的有限 Fourier 投影误差：

| 轴比 | M16 坐标投影误差 | M16 初值度量投影误差 |
|---:|---:|---:|
| 1.2 | 3.68e-15 | 1.44e-14 |
| 1.5 | 8.08e-11 | 4.96e-9 |
| 2 | 2.60e-7 | 1.62e-5 |
| 10/3 | 1.80e-4 | .01141 |

大轴比下不能因为 collocation 解收敛便跳过这个入口误差。

## 3. 纯平面 m2 回传方向确实能对准

在完整物理 m2 线性变量 `(f,g)` 中，平面椭圆的一阶初值为 `(1,0)`。
这与旧 wavy-core 的 `g/f<0` 不同。`repo_scan_ellipse_line.py` 以一个有限
cycle 的径向幅度 delta 为控制，令末端 Robin 线回传后的 `rho=g(0)/f(0)=0`。
数据：`repo_scan_ellipse_line.json.gz`，小摘要 `repo_scan_ellipse_line_summary.json`。

保留的低曲率根为

```
direction=outward
vu=.35, vd=.5, ramp=.4, cycles=1
cut_radius=.6, cut_slope=.5
delta=.19146251660025568
```

在本次线性计算中，单侧背景高度约 `1.88146333`，经线长约 `2.18878288`，
背景最大曲率约 `4.17399356`，端点高度模态相对初始 radial 模态的增益约 `.0409945053`。
使用独立前向 RK45，从 `(1,0)` 再积分，终端直线的归一化行列式残差约 `1.70e-7`。
后者才是这次独立线性验证的实测精度；不能把反向求根产生的 rho≈3e-17 当成严格精度。

更短的一条根为 `vu=.5,vd=.7,delta=.17569425606328523`，其背景高度约 1.30948、
曲率约 7.09684。当前首选较缓根，不因为高度 1.88 就排除它；宏观固定帽布局
可能有不同的全局直径预算，尚待 root 构造与认证。

末端线来自旧数值 port 的显式缩放并改变 wCut；这里只把它作为有限 Robin
边界条件。没有声称已有与它相容的低曲率无限尾部。

## 4. 新非线性 ellipse-core BVP

源码：`repo_scan_ellipse_bvp.py`。未知量数目与边界条件匹配：

1. p0 改变 cycle 的 delta；在求解过程中它是度量设计变量。
2. 其余 M-1 个参数改变中央**平面**曲线的高阶径向项。
3. 高阶修正分别使用 `cos(2j phi)-1`（j 偶）或 `cos(2j phi)-cos(2phi)`（j 奇），
   因而在两个主轴顶点都为零。统一周长归一后长短轴比例保持指定值。

因此修正后的中央曲线是具有指定两轴比例的平面凸曲线，一般不再是严格椭圆。

为处理 p0 导致的端点移动，BVP 在固定 `t in [0,1]` 上解：
`s=L(p0)*t`，右端含完整的 `L(p0)` 因子和参数依赖的 `a(s;p0)`。
求解后冻结该 profile，把网格转换回物理 s，再构造实际 C² piecewise-quintic
映射。独立 audit 读取实际多项式的一、二阶导数，未用 formal ODE jets 冒充
这些导数。平均高度另用逐网格段正权 Gauss 积分；其径向误差未做区间包围。

### 已完成的 M4 延拓

配置文件 `repo_scan_ellipse_gentle_candidate.json`；结果在
`repo_scan_ellipse_gentle_summary.json` 以及逐点压缩 checkpoint。

| 指定轴比 | 实际度量分量 l1 最大值 | actual flow defect | 采样 κ | `D_cyl` | 末端非圆系数最大值 |
|---:|---:|---:|---:|---:|---:|
| 1.02 | 3.4613e-9 | 6.1931e-9 | 4.18113 | 4.45844 | .000405889 |
| 1.05 | 3.2254e-7 | 5.5690e-7 | 4.19143 | 4.46505 | .000999915 |
| 1.1 | 9.3427e-6 | 1.5319e-5 | 4.20760 | 4.47549 | .00195250 |
| 1.2 | 2.2554e-4 | 3.4915e-4 | 4.23665 | 4.49420 | .00372987 |

`metric_l1` 在此版本指三个相对度量分量 `(E-1,F/a,G/a^2-1)` 的 Fourier-l1
上界之最大值，不能直接写成相对算子范数。后续需要存下三个分量并给出
`sqrt(e^2+2*f^2+g^2)` 上界。独立审查正在检查这一点及 core 投影/mean-height。

### M8 的结果与停止升轴比的理由

在轴比 1.2，M8 使实际分量误差由 `2.2554e-4` 降为 `2.87549e-6`，
约降 78 倍；`kappa*D_cyl≈19.0406`、高度 1.88270、最大半径 1.22685 基本稳定。
但 delta 从 `.19150268766` 变为 `.19151068478`，仍属同一设计问题的数值
分辨率改变，**尚非冻结度量后按本题第 5 条得到的完整加密证据**。

M8 的轴比 1.5 虽然 collocation 收敛，实际分量误差却达 `.0080883`，最高
平面修正异常；1.7 的继承初值失域。因此没有把它们称为可用大幅解，而是回到
轴比 1.2 做 M12 加密及高模态横截性检查。

本作者自身的方向差分检查在 `repo_scan_ellipse_jacobian_check.json`：
包括 p0 链式项，fun Jacobian 相对差约 `4e-10`、BC Jacobian 相对差约 `2e-11`。
这不是未参与者独审。另一个 agent 已在独立前缀 `independent_ellipse_*` 下
从头重跑 M4 的 1.02→1.05。

## 5. 当前复现入口与缺口

在本题目录运行：

```sh
python notes/repo_scan_ellipse_bvp.py \
  --source-root /workspace/scratch/f6f33987b45e/math-research \
  --config notes/repo_scan_ellipse_gentle_candidate.json \
  --out-prefix notes/<自己的前缀> \
  --modes 4 --aspects 1.02 1.05 --tol 2e-7 --bc-tol 2e-8
```

该 source-root 是只读的相邻课题缓存；用完整当前仓库 checkout 可替换它。
输出含 source hash 和所有 checkpoint。所有原始数值明细压缩为 `.json.gz`，
系数使用原有 `.npy.gz` 分块；小 `_summary.json` 只保留标量。

仍缺：更大轴比的真实频谱收敛；冻结几何后的加密；低曲率且真实圆化的末端；
完整 closed embedding；全部相位的 reach；包含未来宏观帽的完整 D 与全刚体
Hausdorff 下界。当前工作的正向价值是：已建立平面非径向中央柱与完整空间
Frenet BVP 之间的可运行接口，并找到了具有小实际误差的非线性小椭圆支。
