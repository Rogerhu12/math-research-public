# R33 单位切向表示的实际有限幅计算

状态：**浮点探索，不是闭合精确等距族存在证明。**

本记录接续 `2026-11-12-spline-newton.md` 的 M24 位置样条图。
保存的相位函数定义一个真无限 Fourier 的单位切向场；角向闭合与
$g_{\theta\theta}=a(x)^2$ 是解析恒等式。其余两个径向度量方程仍有
下表所示的非零残差，且尚无固定帽、完整无限尾和全局 reach 证书。

## 1. 变量与实际函数

使用 R33 的有限相位多项式

\[
\beta=\sum_{k=1}^M\beta_{4k}(x)\sin(4k\theta),\qquad
\gamma=\sum_{k=1}^M\gamma_{4k}(x)\sin(4k\theta).
\]

$\beta$ 为 $x$ 偶函数，$\gamma$ 为 $x$ 奇函数；它们的系数是带权
实际五次样条，$\beta_{4k}=a_{\rm ref}^3b_k$、
$\gamma_{4k}=a_{\rm ref}^2c_k$。圆柱旋转基中的单位切向为

\[
T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma),
\qquad F=a(x)\mathcal P_\theta T+Z(x)e_z.
\]

这里 $\mathcal P_\theta$ 是笛卡尔向量场的零均值原函数。四重与反射
对称性保证 $\int T\,d\theta=0$，于是 $F$ 真正周期闭合。
$T$ 不是截断的位置多项式；有限相位通过三角函数产生无限频尾。

**本表示的 $a$ 是周长半径，不能直接当成旧图的平均径向坐标。**
初值从旧位置图的 $F_\theta/|F_\theta|$ 提取相位，同时计算
$\langle |F_\theta|\rangle-a_{\rm old}$ 并将其存成一个真实偶五次
样条 `radius_shift`。该样条的 knots、coefficients、degree 全部保存在
NPZ 内；后续不需要重新猜测它。其余三维 mean 参数仍作用在原有
mean 基函数上。新图的 mean 作用量必须另算，不能沿用旧位置图的值。

振幅规范改为固定 **$\beta_4(0)$**，通过线性消元精确施加。
每次另外报告实际 $U_4(0)$ 与真实腰圈径向差，不再给新图贴上旧
“核振幅 $\varepsilon=.06$”或“固定 $U_4=.06$”的标签。

## 2. 原函数、真实导数与角频预算

四分之一周期取 $Q$ 个节点。对 $n=4k$，旋转基中的原函数 Fourier
逆矩阵是

\[
\frac1{1-n^2}\begin{pmatrix}in&1\\-1&in\end{pmatrix},
\qquad (\mathcal P_\theta T)_z^{\widehat{\ }}(n)=\widehat T_z(n)/(in).
\]

零模横向分量按同一矩阵处理，竖向均值置零；丢弃 quarter Nyquist。
保留 $|k|\le Q/2-1$，等价于完整圆周 $N=4Q$ 点 DFT 保留
$|n|\le2Q-3$：横向最高 $4k\pm1$、竖向最高 $4k$。
该对应已与 `fourfold_unit_tangent.py` 的独立笛卡尔实现交叉核查。

solver 中的 $F_x=a'\mathcal P T+a\mathcal P T_x+Z'e_z$ 使用 FFT
原函数；角向公式 $F_\theta=aT$ 保留真无限场定义。后验几何检查则
先构造有限原函数，再对**同一有限函数**求 $F_\theta,F_{x\theta},
F_{\theta\theta}$，报告其与真切向公式的差及解析尾/alias 预算。
不以截断原函数的导数冒充无限 $aT$。

最初的高分辨率独立 helper 比较只能检查公式实现；预算必须使用
当前实际 $Q$ 对应的 $N,K$。在 Q128 的首轮中，角加倍的径向 primitive
二jet样本差约1.36e-7，保守解析预算给 $F_{\theta\theta}$ 约.00262，
因此确有继续角加密的理由。现在保存的是 Q256 状态。

## 3. 加权残差的稳定实现与核查

目标为全部可表示的非均值 $g_{xx}$、$g_{x\theta}$ 系数，径向每个
样条区间用3点 Gauss，采用原固定背景的权重和有限 Robin 行。
由于极端极点的 $a_{\rm ref}^3$ 权重很小，先对整体 $g_{xx}$ 做 FFT
再去均值会放大浮点消减。实现改成相对于轴对称一阶场的增量恒等式：

\[
\Delta g_{xx}=2F_{0,x}\cdot\Delta F_x+|\Delta F_x|^2,
\]

并用 $\cos\gamma\cos\beta-1=-2\sin^2(\gamma/2)-2\sin^2(\beta/2)
+4\sin^2(\gamma/2)\sin^2(\beta/2)$ 保留极小二次项。
修复前方向差分显示约1%的假误差；稳定实现后，在 M4/35、含固定腰
振幅消元的小例中，中心差分最大误差约6.1e-14、相对L2约1.1e-12。
局部 Gram 的随机二次型与实际 JVP 范数平方一致至双精度，梯度方向
差约1.1e-22。以上是有针对性的实现核查，不是无穷维逆证明。

为后续升频，新增 `fourfold_banded_normal.py`。按径向块排序后，局部
五次样条产生有限带宽物理块，三个 mean 列形成小型 Schur 补。
它解同一个列归一化、阻尼正规方程，避免同时保留多个大 CSC/LU 对象。
小例与原稀疏 LU 的缩放步最大差2.94e-15（步最大值.01679），原正规
矩阵中的残差1.14e-17。正规方程仍会损失条件数，故任何接受步都检查
原非线性残差；此线性算法不是验证算术。

## 4. 已保存的 Q256/n201 状态

永久文件：

`data/fourfold_phase_m24n201_q256_checkpoint.npz`，96535 bytes，
SHA256 `63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e`。

同名 JSON 含完整 mean、振幅规范、当前实际原函数预算、评价器源哈希。
参数为 $\mu=4\sqrt2$、M24、201正控制点、graded 网格、Q256、
每单元3点 Gauss、有限端点 $x=3$。从 M24 位置检查点转到 M24/n151/Q128
先做四步，再径向与角向加密做四步；两阶段均使用原 sparse-normal 求解。
末态代价1.6937641820e-11。默认带状求解器用于后续恢复，数值对象相同。

| 同一有限原函数实际二jet，1798径向点、Q256 | 样本值 |
| --- | ---: |
| 完整相对非均值 metric 算子范数 | 3.6569866948257156e-5 |
| 固定 $\beta_4(0)$ | .20747484022400084 |
| 实际 $U_4(0)$ | .06009144027308799 |
| 两倍最大模长（直径代理） | 2.578482278022644 |
| 腰圈径向差 | .132485335453858 |
| 腰差/直径代理 | .051381130901336565 |
| 最大绝对主曲率 | 7.028196676265074 |
| 最小支撑函数 | .9226575034375718 |

腰圈实际二型样本为
$\det II\in[-1.598179,-.952604]$、$N\in[-8.158231,-.423179]$。
mean 参数为 `(.799535158049,-.002082663595,-.060914837771)`。
首阶段的振幅为.20747484245271483；早期重新插值带来约2.3e-9差值，
目前恢复入口已直接继承保存的振幅参数，不再由新网格重新估计。

完整误差峰值在 $x=.2141512354,\theta=0$。径向细化消除了旧第4模
残差峰，当前已表示相位模中最大误差是第96模 xx，约4.08e-6；
超过相位截断的第100模 xt 约4.65e-6。这是继续升M32的依据。

在 $x=0,.1,.25,.5,1$ 五个径向样本，Q256 与完整圆周 helper 的
primitive 差不超过6.67e-16，角加倍的 primitive 径向二jet差不超过
2.86e-15。对应当前 Q 的解析尾+alias 公式最大预算为：

| 几何量 | 五点预算最大值，未含浮点舍入 |
| --- | ---: |
| $F$ | 2.63e-17 |
| $F_x$ | 5.13e-16 |
| $F_\theta$ | 1.32e-14 |
| $F_{xx}$ | 3.05e-13 |
| $F_{x\theta}$ | 2.58e-13 |
| $F_{\theta\theta}$ | 6.70e-12 |

这些不是整个径向区间的统一区间界。独立实际 FFT 导数与真角公式
之间的最大样本差约6.43e-11，包含普通浮点求导误差。任何精确证书
仍需支付径向统一界与舍入误差，不能把上述表直接称作 C² 证书。

## 5. 恢复、继续升频与可见性余量

直接从保存的完整相位函数恢复，不需要重做遗失试验：

```bash
mkdir -p /tmp/visible-exact-phase
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_newton.py \
  --start-phase topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
  --modes 32 --points 201 --mesh graded --gauss 3 --angles 256 \
  --linear-method banded --iterations 4 --regularization 1e-6 \
  --cache /tmp/visible-exact-phase/m32.npz \
  --out /tmp/visible-exact-phase/m32.json
```

若只续原维数，把 `--modes` 改24。若要使用原 sparse-normal 算法，
指定 `--linear-method normal`。每次实际代价改善都会原子保存 NPZ。
本会话当前 M32 工作区是
`/workspace/scratch/f6a2c7886477/newton-experiments/phase-m32n201-q256.npz`，
相应 `.log`、结束后的 `.json` 记录其状态；未另推送的末态不作为永久输入。

在当前径向与角截断误差进一步压下后，可在同一相位图小步增大
$\beta_4(0)$，以争取腰差比约.055的余量。必须同时复算真实
$N,\det II$、曲率、间距以及直径代理，不能靠均值漂移把代价压小而
耗尽可见性余量。当前样本比.05138不等于严格下界 .05 已获证。

## 6. 原位置图的有限 Schur 方向

另有 `fourfold_schur_directions.py`，在已保存 M16/n151 位置图上，
给每个 unit-mean 列补入非均值变分，最小化同一有限线性 metric
残差并保持 $\delta U_4(0)=0$。三个列的加权L2由
`(.04158,.7161,.4058)` 降至 `(.007633,.1162,.0690)`，没有各自消尽。
正规化1e-10的 Schur 谱约
`(1.03e-9,3.41e-6,.01831)`；最软 mean 组合约
`(-.994507,.003204,.104619)`。这些数字提示一项主要兼容条件与近切向
组合，不能把任一裸 mean 列叫作精确等距族的参数方向。

脚本的 `linear_candidate(solver,direction)` 返回不加背景项的同一实际
样条变分二jet，可用于完整转折图灵敏度。当前方向工作区文件
`newton-experiments/schur-m16n151.npz/.json` 已交给独立特征分析使用；
可以从永久位置检查点按脚本完整重做。此有限 Schur 数据不替代
R31/R32 所需的无穷维参数化与实际右逆。
