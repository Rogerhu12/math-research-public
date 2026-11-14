# M15 辅助前缀实际一阶采样独核与 M12 连续界余量定位

作者：独立几何审查岗位 `/root/independent_geometry`，2026-11-09。本岗位未参与本次 M15 辅助前缀或真实 prefix–tail 联解优化。

## 1. 对象、状态及输入绑定

本次只读冻结 CP `2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz`，SHA256 为 `4a13e13223047c995acd855db93007ed57bf0471214229c62adb5d7543425190`。它的两块原 float64 五次系数均按 CP 中的字节数和 SHA256 独立验证后读取。辅助 BVP 的成功状态不等于真实非线性 DN 成功；本 CP 明确保留 `actual_nonlinear_tail=False`、`frozen_affine_dn=True` 和 `UNSOLVED relative to the actual nonlinear DN`。本报告不修改该状态。

与已认证 M12 闭图元数据 `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json` 比较，`frozen_profile`、完整 `chart` 和 `warp_reference_q` 逐字段相等；物理 port 哈希、其全部参数和 cut 数据也相等。轮廓加载器及 flat 实现哈希与 M12 元数据一致。实际支持幅度变化属于图的系数变化；它没有改变冻结的角坐标参考幅度或目标轮廓。本次只评价冻结数值源中的轮廓；将 bridge 的唯一精确根及其坐标缩放误差转入连续度量预算仍须在正式证书中执行，不能从本次浮点采样省略。

独立采样脚本为 `scripts/db6f-audit-prefix-actual-metric-sample.py`，冻结 SHA256 `3b5435d2caef6655421acead3b6bbaa90d482890dc98d1842a34c04aa07c4aa4`。输出为 `2026-11-09-db6f-audit-m15-affine-actual-metric-sample.json`，SHA256 `aa9845c1d849d754d08333beec1b8752c5f225725184d7978cf6cea62953e81c`。正式完整运行真实退出 0；输出另绑定实际加载的冻结源文件闭包。初版曾在计算完成后因 long-double 标量不能直接写 JSON 而拒绝输出；只将输出标量显式转为 Python float 后重新完整运行，所有数学运算不变，未留下可误用的成功报告。

## 2. 独立重算的是保存图的导数

记原材料角为 $\Theta$，数值角为 $\psi$，并写

$$
\Theta(s,\psi)=\psi-\frac{e(s)}3\sin(3\psi),\qquad
\gamma=\Theta-\psi,\qquad
\rho=\Theta_\psi>0,\qquad v=\frac{\Theta_s}{\rho}.
$$

从保存的五次分段多项式，用独立的 long-double Horner 求出其值和**物理 $s$ 导数**。没有调用原 `audit`、`frame`、`values` 或 ODE RHS 来代替这些导数。若保存的三组非均值系数分别为 $y_j^r,y_j^t,y_j^z$，则被评价的位置定义为

$$
X=R e_r(\psi)+T e_\theta(\psi)+(h+Z)e_z,
$$

$$
R=a\cos\gamma+q\left(y_0+\sum_{j=1}^M y_j^r\cos(3j\psi)\right),\qquad
T=a\sin\gamma+q\sum_{j=1}^M y_j^t\sin(3j\psi),\qquad
Z=q\sum_{j=1}^M y_j^z\cos(3j\psi).
$$

旋转基的导数直接进入实际 Cartesian 导数。例如角导数的前两分量为 $(R_\psi-T,T_\psi+R)$，不是把 $R_\psi,T_\psi$ 当作固定 Cartesian 分量。由此独立得到 $d=X_\psi$、$d_\psi$、切向量、曲线法向量和副法向量。源中 mean-height 的定义是

$$
h(0)=0,\qquad
h_s=\frac1{2\pi}\int_0^{2\pi}
\left[\alpha N+\sqrt{1-\alpha^2}B+v d\right]_z\,d\psi,
\qquad \alpha=-\frac{a_s}{a\kappa_{\rm curve}}.
$$

本次与原采样审计一样，以 1024 个均匀角点的平均评价这一个定义泛函，未认证其连续积分余项。绝对高度的积分常数及 $h$ 本身不影响第一基本形式，故这里只计算 $h_s$，不做无必要的高度积分。非均值经向导数始终来自保存多项式，而不是上式中的 Frenet 速度。

最后在固定材料角下使用精确链式法则

$$
F_s=X_s-vX_\psi,\qquad F_\Theta=X_\psi/\rho,
$$

并重算

$$
e_{ss}=|F_s|^2-1,\qquad
e_{s\theta}=\frac{F_s\cdot F_\Theta}{a},\qquad
e_{\theta\theta}=\frac{|F_\Theta|^2}{a^2}-1.
$$

与原作者一致的有限 FFT 指标，是各 $s$ 及上述三个分量的离散 Fourier 系数绝对值之和的最大值。另行报告实际采样点的对称 $2\times2$ 残差矩阵算子范数；二者不混为一个定义。

## 3. M15 采样结果及限制

使用原 CP 节点、其物理中点及原 151 个均匀径向点，去重后恰为原作者的 5399 个 $s$ 点；角点数为原作者的 1024。以下是浮点诊断值，**不是连续严格上下界**。

| 指标 | 独立结果 |
| --- | ---: |
| 保存图的 metric FFT $\ell^1$ | $1.302458505758324\cdot10^{-9}$ |
| 原作者同网格报告 | $1.3024643295715905\cdot10^{-9}$ |
| 独立值减原作者值 | $-5.823813266511528\cdot10^{-15}$ |
| 采样残差矩阵算子范数最大值 | $1.3024585035167381\cdot10^{-9}$ |
| 保存导数与 Frenet 法向速度的差最大值 | $2.1762127909838206\cdot10^{-9}$ |

最坏 metric 在 $s\approx0.002000715729531439$，由角向对角项给出；采样算子最大值出现在 $\psi=0$。两种独立实现的差远小于所讨论的 $10^{-9}$ 量级，支持原作者对这个冻结辅助前缀的采样报告。它没有证明连续角／径向界，也没有支付真实 DN。

这里评价的是保存的五次**非均值**插值加解析 warped 圆背景和 mean-height 定义；正式闭图还另有有限 Fourier 背景展开、共享两 jet 的 Cartesian Hermite 表示、入口镜像修正、共同 cut 修正、有限尾及帽。它们必须各自在最终同一图上获得连续证书。不能将本次采样数字直接搬到尚未构建的 M15 闭图上。

## 4. M12 的约 2.9 倍估计余量来自哪里

原 M12 源图采样约为 $8.9513\cdot10^{-9}$；已审闭图前缀连续算子界为 binary 端点约 $2.5720856392336185\cdot10^{-8}$。二者不完全是同一个指标／表示，不能仅从这个比值断言数值插值误差。为隔离区间估计方法，本次固定**同一已认证 M12 共享图、同一目标供应包及同一物理区间**进行局部对照。

脚本 `scripts/db6f-audit-prefix-metric-budget.py`，SHA256 `dc5c0a569f291fdd19e77272c4d565c43a2d976d2534dc13cc47d0fb13bb451f`，真实退出 0，输出 `2026-11-09-db6f-audit-m12-prefix-metric-budget.json`，SHA256 `487fa3781de18a58bea2268bfd8fd85ceab5e29a3bc3cb8305d450362a9d1a3b`。本次只检查区间 0 与原全域最坏区间 74，不是新全域证书。二者均位于共同 cut 修正开始之前，脚本按原 common-cut 实现逐槽补零至同一 Fourier 基，不加载或借用其他尾端点；最坏区间 74 的原上界逐位复现。

原最坏区间为

$$
s\in[0.00707621563286909,\ 0.007413178282053332].
$$

其已相消的 $\psi\psi$ 坐标残差 Fourier／Bernstein 范数约为 $1.0218550481502665\cdot10^{-9}$；统一使用 $\min(a\rho)\approx0.20000525$ 后，仅这一项的归一化上界就约为 $2.554503418951874\cdot10^{-8}$。再加混合项得到原 $2.5720856392336185\cdot10^{-8}$。这一步把残差随角度的变化与 $\rho$ 随角度的变化拆开取最坏值，丢失了二者在同一角度上的关联。

下表列出本次两个局部区间的算子上界；显示十进数仅作紧凑比较，严格端点由 JSON 中的 binary 数及已审向外算术解释。

| 同一物理区间上的估计 | 区间 0 | 区间 74 |
| --- | ---: | ---: |
| 原 Fourier $\ell^1$／统一 $\min\rho$ | $2.56305\cdot10^{-8}$ | $2.57209\cdot10^{-8}$ |
| 只把径向等分为 8 段 | $2.56304\cdot10^{-8}$ | $2.57035\cdot10^{-8}$ |
| 保持原径向区间，64 个角弧 | $1.68816\cdot10^{-8}$ | $1.68850\cdot10^{-8}$ |
| 保持原径向区间，128 个角弧 | $1.16934\cdot10^{-8}$ | $1.17079\cdot10^{-8}$ |
| 保持原径向区间，256 个角弧 | $9.52493\cdot10^{-9}$ | $9.53674\cdot10^{-9}$ |

径向八分只使最坏区间降低约 $0.0673\%$，角弧 256 则降低约 $62.9\%$。此局部证据清楚地把主要估计余量定位到角向归一化，而非缺少径向节点。区间 74 中，坐标 $G$ 残差范数与其系数区间中点范数只差约 $2.37\cdot10^{-12}$，约占该范数的 $0.23\%$；这个中点比较只是舍入余量诊断，不是另一个严格图的证书，也不足以解释原来约 2.9 倍的差距。

角弧改进始终先在系数域计算小残差 $E_r,F_r,G_r$，再在每个角弧上用已有有理三角余项、Bernstein 和向外区间算术包围

$$
\widehat E=E_r-2vF_r+v^2G_r,\qquad
\widehat F=\frac{F_r-vG_r}{a\rho},\qquad
\widehat G=\frac{G_r}{a^2\rho^2}.
$$

保留局部正的 $a,\rho$ 下界，最后以最大绝对行和控制对称矩阵算子范数。它没有对两个量级为 1 的度量矩阵分别取区间再相减，也没有改变目标 $g$、图或物理参数。

## 5. 后续 M15 认证的最小必要细分建议

对最终真正完成的 M15 共同图，先运行原系数相消后台并逐区间保存上界；仅对超过预定前缀预算的区间启用角弧版本。入口附近优先尝试 128 个角弧，再只把未达预算的角弧加至 256 或更细。这个次序由上述 M12 同图对照支持，但不承诺尚未构建的 M15 在固定 128 弧必然通过。

不应仅因原界约为采样量的 2.9 倍就全域加密径向或重导出整个尾。只有新证书某个区间的径向 Bernstein 余量或实际插值误差仍主导时，才对该物理区间增加径向分割。目标 packet 与几何均保持原定义；角弧细分只改验证精度。M15 当前真实 DN、共享图转换、全尾及最终 G5 的作用域仍分别保留。

复现命令：

```sh
python scripts/db6f-audit-prefix-actual-metric-sample.py \
  --checkpoint notes/2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz \
  --linear-port notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
  --source-root repro/source-root \
  --reference-geometry notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json \
  --out notes/2026-11-09-db6f-audit-m15-affine-actual-metric-sample.json

python scripts/db6f-audit-prefix-metric-budget.py \
  --geometry notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json \
  --target notes/2026-11-09-db6f-root-flat17-m12-target.json \
  --certificate notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-metric.json \
  --out notes/2026-11-09-db6f-audit-m12-prefix-metric-budget.json
```
