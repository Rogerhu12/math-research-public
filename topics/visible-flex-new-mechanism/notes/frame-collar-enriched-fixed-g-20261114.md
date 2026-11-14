# 固定同一度量的混合角函数暖扩空间

2026-11-14。独立运行器 `../scripts/frame_collar_enriched.py`。它导入已发布的 frame、ellipse port、径向 seed 和分布 audit 实现，没有修改这些基模块。此次改变有限维场空间、取样网格和形状软目标；核心、参考度量、开放端口、S9 基场及局部 Cauchy 修正均保持原定义。

## 1. 选择空间的实际依据

公开 run `43602519926` 的首个固定度量候选没有通过几何条件。随后 run `43603136078` 的[同参数分布审计](actions-43603136078-1-ellipse_audit/frame-ellipse-fixed-distribution.json)与原最细网格的六项摘要逐位相同；其最大积分性残差位于负 K 段 `t=.4275,theta=0`，是 `R_T=-3.5102196878`。主曲率峰在 `t=.4575`，度量峰在后段 `t=.7275`。这不是“入口截止点漏采”已经获得的证据。

峰附近的残差角谱在原自由角模截止频率 10 以上仍有明显分量。因此本轮保留旧空间，加上与准确椭圆参数相适配的少量函数；同时用严格嵌套的径向节点增加局部调整能力。不把一次大网格评价当成连续证书，也不把优化器正常终止称作可行。

## 2. 准确的增广角函数

材料角仍是原来的 \(\theta\)，参考度量仍为 \(dt^2+a(t)^2d\theta^2\)。令 \(\phi(\theta)\) 是同一准确椭圆弧长反解，\(u_{\rm core}(\theta)=\psi(\theta)-\theta\) 是真实入口的完整标量角函数。新角基的顺序为

\[
\begin{aligned}
u:&\quad \sin(2k\theta),\ k=1,\ldots,5;\quad
      \sin(2j\phi(\theta)),\ j=1,2,3;\quad u_{\rm core}(\theta),\\
v:&\quad \sin(2k\theta),\ k=1,\ldots,5;\quad
      \sin(2j\phi(\theta)),\ j=1,2,3,\\
\beta:&\quad \cos(2k\theta),\ k=0,\ldots,5;\quad
      \cos(2j\phi(\theta)),\ j=1,2,3.
\end{aligned}
\]

旧 \(\theta\) 列完整保留且顺序不变。没有重新投影或正交拟合核心；也没有额外添加重复的 \(\phi\) 零模。所有新增函数都有解析角导数：

\[
\phi_\theta=\frac{a_0}{\sqrt{A^2\sin^2\phi+B^2\cos^2\phi}},
\qquad (u_{\rm core})_\theta=\psi_\theta-1.
\]

这里的 \(\phi\) 只用于表示标量函数，不作为新的物理材料坐标。故它没有改变 \(g\)。恒等式
\(\phi(\theta+\pi)=\phi(\theta)+\pi\)、\(\phi(-\theta)=-\phi(\theta)\)，以及 \(u_{\rm core}\) 的奇性和 \(\pi\) 周期性，保证原来的反射与二重旋转对称仍成立。R28 的闭角平均条件仍由对称性准确给出。

取径向自由数 \(J=9\) 后，三个场分别有 \(9\times9,9\times8,9\times9\) 个变量，共 **234** 个。实际开放核心、开平领和所有位置二 jet 仍由原始基场和径向三阶消失条件保留。自由场依然可以改变高阶 Cauchy 系数，本轮没有另加“完整局部解”的假设。

## 3. 准确插结与实际暖参数的舍入分开记录

旧 \(J=4\) 的内结点为活动区间的 \(i/5\)，新 \(J=9\) 为 \(j/10\)，前者是后者的子集。脚本用 **Fraction 有理数的逐次 Boehm 插结** 得到准确五次 B 样条变换矩阵。首末各三个完整控制系数为零的子空间也被准确保留。

因此在实数数学定义中，准确插结后的系数表示完全相同的旧自由函数。新增 \(\phi\) 与 \(u_{\rm core}\) 系数初始全为零。插结权重可能不是二进有理数，所以数值求解前还需舍入到 binary64；两者没有混为一谈。输出保存：

- 旧、新准确结点及准确自由控制变换矩阵；
- 乘以旧准确 binary64 系数后的未舍入有理系数；
- 真正交给求解器的 binary64 系数及其准确有理身份；
- 最大系数舍入误差的准确有理值；
- 在公开 Actions 中，与旧模型使用完全相同径向/角网格和中心积分规则时的 \(X,X_t,X_{tt},R\) 及其他位置 jet、标量 jet 差异。

这个有限回放明确标记不是连续误差上界，也不声称舍入后的两个场准确相同。入口的准确性来自共同定义，不由一张有限对照网格证明。启动时若实际有限差超过 `1e-8`，脚本会停止而不悄悄运行一个未经识别的暖初值；这是实现核验门，不是等距完成门。

输入原报告仍须经过原分布审计器的完整身份核验：三个定义几何的实现 SHA256 必须与原报告一致，场系数逐位回转，核心和参考度量的准确身份及完整数学字典一致。新问题的 \(a,a',a''\) 在同网格必须逐位一致，数学 metric hash 必须相同。**本轮是固定同一 \(g\) 的场空间扩展，没有径向 metric 设计变量。**

## 4. 新形状目标采用足够的支持域

本轮主配置为 `--envelope disk-strip --strip-half-width .33`。只需完整初始面满足

\[
X_x^2+X_y^2\le1,\qquad |X_y|\le33/100,
\qquad |X_z|\le9/20.
\]

在其他组装条件同时成立时，R33 的同一支持见证给

\[
D\le\sqrt{481}/10,\qquad \delta_{\rm hold}\ge67/100,
\qquad \delta_{\rm hold}/D\ge\frac{67}{10\sqrt{481}}>0.305.
\]

半径 `rc=.22` 的固定盘仍有直径 `.44`，原握持预算不变。这个支持域比要求全投影留在 `A=1,B=.28` 的填充椭圆宽裕；它不改变核心或 \(g\)。当前只有软取样目标，尚未支付完整曲面的包含条件或 reach。

每个网格点的形状残差为下列五项的原有平滑正部：

\[
X_x^2+X_y^2-1,\quad X_y/.33-1,\quad -X_y/.33-1,
\quad X_z/.45-1,\quad -X_z/.45-1.
\]

例如圆盘项的参数导数为 \(2X_x\,dX_x+2X_y\,dX_y\)，条带项为 \(\pm dX_y/.33\)。完整位置 Jacobian 包含角原函数和中心积分，仍使用原 frame 实现；新增层没有用目标切向代替真实位置。

每项使用原 `shape_weight=2` 和同一个 `1/sqrt(Nr*Nt)` 归一化。主积分性残差仍为三个 \(R\) 分量，因此总共是每点八个分量。**新形状目标和网格下的 cost 不能与旧 cost 直接当作同一函数的下降来比较。** 输出明确记录新目标的初值 cost、shape 身份，以及旧椭圆包络只是 legacy 诊断。可选 `--envelope ellipse` 才启用原椭圆项；输出列出真正活动的残差，不把未选择的条带当成硬约束。

## 5. 计算预算、检查点与审计

建议仅运行一个 case：`J=9,phi_modes=3,Nr=61,Ntheta=192,max_nfev=250`，场系数界 `6`。它沿用原 `least_squares(method='trf',x_scale='jac')` 及解析 Jacobian。默认不会改变原基场、入口截止长度或尾部函数来制造更优初值。

该配置的 dense residual Jacobian 有 `61*192*8` 行、234 列，仅此数组约 **167.3 MiB**。连同参数位置导数、径向积分及优化器中间数组，预估峰值为数 GiB；这是静态尺寸估计，真实峰值另以 Linux `ru_maxrss` 记录，不把估计写成实测。

每十次目标评价或六十秒更新一次当前最优 checkpoint，最终保存完整准确系数和定义。最终同一参数另做 `121*384` 与 `121*768` 审计、独立 Gauss 原函数有限对照，并保存径向残差分布。新 disk/strip 极值和位置单独记录，旧 ellipse 极值明确只是诊断。所有连续度量、嵌入、整面 reach、闭面构造和任务完成标志仍为 false。

## 6. 已实际执行的人工开发检查

文件：`frame-collar-enriched-check-20261114.json`。只使用 `A=.9,B=.72` 的两个侧号；旧 `J2,theta2` 精确嵌入新 `J5,theta2,phi1,u_core`，共55变量。形状界在人工检查中收紧以覆盖非零条带和高度残差，没有优化研究候选。

最终人工检查得到：

| 项目 | 结果 |
| --- | --- |
| 完整方向 Jacobian，相对差 | 两侧约 `4.02e-9`、`5.57e-9` |
| 新角函数解析导数与差分 | 最大绝对差 `5.17e-10` 以下 |
| 暖转后同网格位置/残差 jet 差 | 最大 `4.45e-16` 以下 |
| 准确 metric hash 及 `a,a',a''` 评价 | 保持相同；评价逐位一致 |
| 核心位置完整二 jet | 最大 `2.71e-14` 以下 |
| 平领位置完整二 jet | 最大 `7.55e-16` 以下 |
| 非嵌套的径向结点请求 | 正确拒绝 |

`repo_sources` 独立只读核验了父类构造与新 slices 的时序、角链式、完整旧列保留、Boehm 索引和分母、零二 jet 子空间裁剪、准确与舍入身份、disk/strip/height Jacobian 以及同 g 回放；未进行额外研究计算。这些实现检查不证明本次真实强椭圆连接器可解。

## 7. 单 case 的公开 Actions 命令

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_enriched.py \
  --check-only --out "$RUN_DIR/frame-enriched-development-check.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/frame_collar_enriched.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43602519926-1-ellipse_frame/frame-ellipse-positive-fixed.json \
  --radial-free 9 --phi-modes 3 --radial-nodes 61 --angular-nodes 192 \
  --quadrature-order 4 --max-nfev 250 --field-bound 6 \
  --envelope disk-strip --strip-half-width .33 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --checkpoint-every 10 --checkpoint-seconds 60 \
  --out "$RUN_DIR/frame-ellipse-enriched-fixed.json"
```

后续结论须依据该次实际输出，包括启动的暖转同网格差、全场积分性/度量、细网格曲率及真正支持域，而不能把新增自由度或一个正常退出码当作改善证据。
