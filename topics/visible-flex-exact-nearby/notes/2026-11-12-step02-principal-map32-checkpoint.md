# step02 的 R37 中央主返回：32角冻结检查点

本记录只属于
data/phase_ring_continuation/type_fixed_step02.npz，
SHA256 05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883。
它不使用旧 canonical 或未作 Newton 的 predictor 的返回值。

## 1. 所积分的实际算子

用同一个 Q256 有限原函数的真实二、三 jet，记
$C=F_\theta\times F_x$、$A=|C|$、
$m=C\cdot F_{x\theta}$、$n=C\cdot F_{\theta\theta}<0$。
在当前图取固定径向目标
$g_0=E(x)dx^2+a(x)^2d\theta^2$，
$E=\langle|F_x|^2\rangle$、$a$ 为保存的周长半径。
令 $k=-K_0$、$b=-m/n$、$h=A^2/n$，R37 的两个主速度准确为
$$
c_\sigma=b+\sigma h\sqrt{k},\qquad \sigma\in\{-1,1\}.
$$
因此未归一化判别式确为 $(-K_0)G_{\rm actual}^2$，
其中 $G_{\rm actual}=A^2$，没有预设 $G_{\rm actual}=Ea^2$。

真实求根得到目标正根 $t=.23836991573122465$。
这与此前径向样本线性插值得到的约 $.238475$ 不同；
下列返回从这个重新求出的根出发。
设 $x=t\sin\tau$，则
$$
\theta_\tau=t\cos\tau\,(b+\sigma h\sqrt{k}).
$$
因为目标 $k$ 与角无关，角导数的准确变分方程为
$$
(\log J)_\tau=t\cos\tau\,(b_\theta+\sigma h_\theta\sqrt{k}),
\quad J_{\rm in}=1,
$$
$$
b_\theta=-m_\theta/n+mn_\theta/n^2,\qquad
h_\theta=2AA_\theta/n-A^2n_\theta/n^2.
$$
转折处没有 $\partial_\theta k/\sqrt{k}$ 的不定式。
近端点使用 $k(t\sin\tau)=\cos^2\tau\,\bar k(\tau)$，其中
$$
\bar k=-\frac{t}{1+|\sin\tau|}
\int_0^1 k_x\bigl(t[1-\lambda(1-|\sin\tau|)]\bigr)\,d\lambda.
$$
代码在此采用三点 Gaussian 求积，作为普通浮点诊断；
不是这个端点求积误差的严格包络。
先走 $\sigma=-1$ 的左根到右根，再走 $\sigma=+1$ 的右根到左根。
两段角导数按链式法则相乘。

## 2. 冻结输出与独立核查

完整32角输出：
2026-11-12-phase24-corrected-step02-principal-map32.json，
SHA256 2b0b23bcb733305f34c60b94357f1c3d74fc5e444491d51f310394bd16282d27。
每8条射线完成后即落盘；最后一个块的首分支保存在
data/phase_ring_continuation/type_fixed_step02_principal_branch.npz。

- $R(\theta)-\theta$ 样本范围 $[.58345110,1.15368453]$；
- $R'(\theta)$ 样本范围 $[.22783827,3.73130005]$；
- 实际积分射线上的最大 $N=-.44483628$；
- 径向 $\bar k$ 的最小采样值 $.60132842$；
- DOP853 相对容差 $2\,10^{-7}$，共10348次右端求值，约189秒。

独立轴对称复核把 phase 系数设零而保留同一 mean/radius shift，
直接比较此程序与
$4\int_0^t\sqrt{(a''z'-a'z'')/(az')}\,dx$ 的剖面积分。
三个起始角都给 $J=1$，返回值与512点独立求积相差
$9.61\,10^{-8}$；256与512点求积自身相差 $1.05\,10^{-8}$。
其 ODE 相对容差为 $10^{-9}$。
这核对了所积分的主速度和全往返因子，仍然不是严格误差证书。
完整文件为 2026-11-12-phase-principal-axisymmetric-check.json。

## 3. 旋转数和半周锁频的首次探索

对32角数据分别构造带实际 $R'$ 的周期 Hermite 插值，以及单调
PCHIP lift。各自从8个起点迭代100000步，得到的旋转数估计为
$.5514060290$ 和 $.5516611150$，相差 $2.55086\,10^{-4}$。
这里使用的是长轨道位移除以步数及周期 $\pi/2$，
**不是一步平均位移**。

对一个精确的递增 degree-one lift，$n$ 步平移量除以 $n$ 与其
平移数之差至多周期除以 $n$：因为该 $n$ 次迭代的最大、最小
位移之差至多一个周期，而其平移数落在这两个值之间。
所以文件还列出每个插值内的 $\pm10^{-5}$ 有限时间尺度；
这没有包含 ODE、角插值和浮点迭代误差，不能叫真实映射的区间证书。
两种插值的差大于该尺度，说明需要实际新增射线校正插值。

在8193个角点检查 $R^2(\theta)-\theta-\pi/2$，
两个插值的最小值分别为 $+.06812864$、$+.06927088$，
均未找到符号变化根。当前数据没有半周锁频迹象。
这只是对明确插值的浮点排查，尚不排除未包络的真实映射误差。
完整结果为 2026-11-12-phase24-corrected-step02-rotation32.json。

下一轮已按观察到的插值差，选差异最大的16个区间中点求实际新射线，
而不是不加判断地整体加密。无论后续数据如何，本冻结32角输出保持不改。

## 4. 重做与恢复入口

在仓库根：

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_phase_principal_map.py \
      --checkpoint topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02.npz \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-corrected-step02-principal-map32.json \
      --branch-checkpoint topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_principal_branch.npz \
      --rays 32 --block-size 8 --tolerance 2e-7 --resume

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_circle_map_rotation.py \
      --map topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-corrected-step02-principal-map32.json \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-corrected-step02-rotation32.json \
      --iterations 100000

resume 检查源 NPZ 的 SHA、容差、完整角网格及保存分支的实际起角。
已经完成的32角输出会直接保留。这个主图不包含转折幅度、次主相位、
椭圆 DtN 或完整 PDE 散射，不能据此直接宣布全频逆或本课题完成。
