# R139：任意周期入口的准确平坦 coast Gauss–Codazzi 传播

## 1. 命题与位置兼容的区别

本结果给出共同度量

$$
g=d\sigma^2+(a_c+v\sigma)^2du^2,\qquad a_c>0,\quad v>0
\tag{1}
$$

上的准确正交 $l,m,n$ 场。入口只需给足够光滑的 $2\pi$ 周期函数 $n_c(t)>0$、$m_c(t)$；不预先假定它们已经与一条闭合空间曲线及周期标架兼容。

在下面的 $D>0$ 区域，公式产生真正周期的 Gauss–Codazzi 场，并保持初始 $l_c=m_c^2/n_c$。若另有准确兼容的实际周期位置和标架，则 R137 把它实现为真实周期等距曲面；若没有，该公式不自动消除空间 monodromy。当前近似入口的这项缺陷仍由其实际位置/标架后验处理。

## 2. 共同材料图与显式 native II

定义

$$
k(t)=\frac{m_c(t)}{n_c(t)},\qquad
\rho_c=\frac{a_c}{v},\qquad \rho=\rho_c+\sigma,
$$

$$
Q=\sqrt{\rho_c^2+(1+k^2)(\rho^2-\rho_c^2)},
\qquad w=\frac{\rho^2-\rho_c^2}{\rho_c+Q},
$$

$$
B=v(1+k^2)-k_t,\qquad D=a_c+wB.
\tag{2}
$$

注意 $Q=\rho_c+(1+k^2)w$。共同材料角为

$$
u=U(\sigma,t)=t-\frac1v\arctan\frac{wk}{\rho_c+w}.
\tag{3}
$$

由 R137，$U_t=D/(vQ)$。因此只要 $D>0$，(3) 是完整圆周上的度数一微分同胚，记其逆为 $t=t(\sigma,u)$。

在这个逆标签处取所有右端量，令

$$
\boxed{
\widehat k=\frac{k\rho_c}{Q},\qquad
n=\frac{a_c n_c Q^2}{D\rho^2},\qquad
m=n\widehat k,\qquad l=n\widehat k^2.
}
\tag{4}
$$

这就是准确 native 二基本形式传播公式。特别有 $n>0$、$ln-m^2=0$，且 $\sigma=0$ 时恢复 $(m_c^2/n_c,m_c,n_c)$。

## 3. 完整证明：不要求先有全局闭合位置

先在任意入口材料小区间上，任选一个同向正交初标架，解线性角向 ODE

$$
e_{1,t}=v e_2+a_c m_cN,\qquad
e_{2,t}=-v e_1+a_c n_cN,\qquad
N_t=-a_c m_c e_1-a_c n_c e_2.
\tag{5}
$$

其系数矩阵反对称，故保正交性；再积分 $X_{0,t}=a_c e_2$。这在小区间上总存在，不需要另一个径向非线性存在定理，也不要求角向 monodromy 已经为零。

以这些局部实际数据应用 R137 的显式直母线 $X_0+w(e_1-ke_2)$，得到准确诱导 (1) 的局部曲面。其在母线坐标 $(w,t)$ 中的二基本形式仅有

$$
II_{tt}=a_c n_cD
\tag{6}
$$

非零。共同材料坐标的导数为

$$
t_\sigma=\frac{\rho_c k}{\rho D},\qquad
t_u=\frac{vQ}{D}.
\tag{7}
$$

将 (6) 作张量坐标变换，并按目标切向尺度 $1,a_c+v\sigma=v\rho$ 归一，得到

$$
l=a_c n_cD\,t_\sigma^2,
\quad m=\frac{a_c n_cD\,t_\sigma t_u}{v\rho},
\quad n=\frac{a_c n_cD\,t_u^2}{v^2\rho^2},
$$

正是 (4)。所以它们是一个实际局部等距曲面的二基本形式，必满足该度量的 Gauss–Codazzi 恒等式。具体在当前约定中是

$$
ln-m^2=0,
$$

$$
m_\sigma=\frac{l_u}{a_c+v\sigma}-2\frac{v}{a_c+v\sigma}m,
$$

$$
n_\sigma=\frac{m_u}{a_c+v\sigma}
+\frac{v}{a_c+v\sigma}(l-n).
\tag{8}
$$

公式 (4) 与起始局部标架或平移无关。它完全由周期函数 $n_c,m_c$ 及其导数给出，而 (3) 与 $t\mapsto t+2\pi$ 的 deck 移位相容。因此各局部式拼成整个材料环带上的周期 $l,m,n$，(8) 全域成立。

这一步没有偷换为全局周期位置。若把 (5) 沿完整圆周积分，可能得到某个非平凡欧氏 monodromy $(R,b)$。R137 的位置构造满足

$$
F(t+2\pi,w)=R F(t,w)+b,
$$

因为输入的 $k$ 周期而位置与标架具有该 monodromy。共同材料回收不会把 $(R,b)$ 变成恒等。因此已有准确周期位置/标架时可以真实闭合；只有周期 native 场时，仍须独立支付这一兼容条件。

## 4. 曲率、全角正域及对已绑定实例的严格结论

矩阵 $\begin{pmatrix}l&m\\m&n\end{pmatrix}$ 的本征值为 $0$ 与 $n(1+\widehat k^2)$。利用

$$
Q^2+\rho_c^2k^2=(1+k^2)\rho^2,
$$

得到

$$
\boxed{l+n=\frac{a_c n_c(1+k^2)}{D}.}
\tag{9}
$$

对固定入口标签，$w$ 随 $\sigma$ 单调，$D$ 对 $w$ 仿射。因此 $D$ 最小值、(9) 最大值都由入口和目标 coast 末端给出。可对角区间计算端点包后一次覆盖全部径向位置。

针对 R136 新34的实际有限入口，已闭 [Arb 全角包](../notes/2026-11-12-fd2d-k0-ruling-angular-certificate-01.json) 使用准确二进制 Fourier $n_c,m_c$ 和已证明的 balanced 材料坐标区间。$209$ 个自适应角盒证明

$$
n_c>19/100,\qquad D>1/20,\qquad l+n<73/10<125/17
\tag{10}
$$

在完整 coast 全角、全径向成立。对于本稿定义的 native 矩阵，(10) 是严格本征值结论；对于 R137 的另一张近似入口位置曲面，不能跳过其实际兼容缺陷直接移用 (10)。

包还同时覆盖原候选准确 $a_c=a_0+d_*$ 及存储的浮点评估 $a_c$，避免遗漏二者的微小差别。运行身份为 `67753 / 142692`、退出 $0$；源、全部二进制区间端点和版本见 [独立闭 manifest](../notes/2026-11-12-fd2d-k0-ruling-angular-closed-manifest.json)。

## 5. 原生导数与可消费 API

[fd2d_k0_native_gc.py](../scripts/fd2d_k0_native_gc.py) 提供 `native_from_inlet(a_c,v,sigma,data)`，直接返回 $l,m,n$、$n_\sigma,m_\sigma,n_u,m_u,l_u$ 及 (8) 的实际求值残差。它不需要位置或标架输入。

为说明一阶导数的准确含义，记下标 $t$ 为保持 $\sigma$、入口标签的导数，保持入口标签的径向导数记作 $\partial_\sigma|_t$。有

$$
w_\sigma|_t=\frac\rho Q,
\qquad w_t=-\frac{k k_t w^2}{Q},
$$

$$
Q_\sigma|_t=(1+k^2)w_\sigma|_t,
\quad Q_t=2kk_tw+(1+k^2)w_t,
$$

$$
D_\sigma|_t=Bw_\sigma|_t,
\quad D_t=Bw_t+w(2vkk_t-k_{tt}).
$$

对 (4) 直接求导给

$$
\partial_\sigma n|_t=n\left(\frac{2Q_\sigma|_t}{Q}-\frac{D_\sigma|_t}{D}-\frac2\rho\right),
$$

$$
n_t=n\left(\frac{(n_c)_t}{n_c}+\frac{2Q_t}{Q}-\frac{D_t}{D}\right).
$$

再用 (7) 作链式变换 $n_\sigma=\partial_\sigma n|_t+n_t t_\sigma$、$n_u=n_t t_u$。$m=n\widehat k$、$l=n\widehat k^2$ 的导数同理由乘积法则给出。这些是解析导数，不是径向差分或对有限拟合再求导。

`SavedNativeCoast(inlet_path).evaluate(sigma,u)` 读取本轮已闭入口，并以带角 lift 括号的 Newton 方法在给定固定材料 $u$ 上求值。准确图由 (10) 的 $D>0$ 保证单值；数值反解误差单独报告。

此具体读者绑定 `7c3f31de…` 新34基准物理度量和 $\delta=0$。它不能作为非零 radial-bump 改 $g$ 后的准确传播；若只拿作另一个方程的初猜，也必须明示其原物理身份。

## 6. 真实导出、输入缺陷与舍入范围

实际运行 `41355 / 88d891` 自然退出 $0$，耗时 $100.49913619299969$ 秒。它在 $9$ 个物理 coast 位置、$768$ 个固定 seed-normal $\phi$ 点上求值，材料坐标是同一非均匀函数 $u=U_{\rm seed}(\phi)$。

- [native field](../notes/2026-11-12-fd2d-k0-native-gc-01-field.npz)，SHA256 `5f260eff2719cb48174dd51c85c3b3eca1e9c33e6806695ad165e776e01070ae`；
- [完整实际报告](../notes/2026-11-12-fd2d-k0-native-gc-01-report.json)，SHA256 `23fc2ce14bcf861df247ad106435de366206a3a627809fa2da86b978a37294c7`。

解析字段使用本机 `numpy.longdouble` 求值，保存的 NPZ 数组另舍入为 binary64。报告所示 Gauss 残差不超过 $1.085\times10^{-19}$，两条解析 Codazzi 残差不超过 $1.069\times10^{-14}$；这些是求值误差诊断，不是把已保存 binary64 表称为准确函数定义。准确函数定义仍是有限入口 Fourier 数据、固定材料图和公式 (2)–(4)。

末端 native 场与 R137 真实 Cartesian 位置计算出的二形式分量之差约为

$$
(2.015,1.982,1.611)\times10^{-7}
$$

（按 $l,m,n$ 顺序）。它忠实反映两种数据对象之间未支付的兼容差别，没有通过正交化或覆盖位置数据把它抹掉。

## 7. 角频率约定及真实截断困难

导出表中的投影使用均匀 fixed-seed $\phi$ 网格的普通 Fourier 整数波数 $j$。它不是均匀材料 $u$ 网格上的 Fourier 投影。对当前 D2 场，$l,n$ 为偶函数，$m$ 为奇函数，且全部以 $\pi$ 为周期。

报告的“最高波数 $M$”表示保留 $|j|\le M$。所以 $M=15$ 对应 $\cos(2k\phi)$ 中 $k\le7$，而不是 $k\le15$；$k\le15$ 对应下表的 $M=31$。

| 最高整数波数 $M$ | 最高偶波数 | $\cos(2k\phi)$ 的最大 $k$ | 同 $768$ 节点的最大字段值投影误差 |
| --- | --- | --- | --- |
| $15$ | $14$ | $7$ | $.9797199796070265$ |
| $31$ | $30$ | $15$ | $.7000300863349449$ |
| $63$ | $62$ | $31$ | $.5398318081261$ |
| $95$ | $94$ | $47$ | $.3966050369581364$ |
| $191$ | $190$ | $95$ | $.17313870580377322$ |

这是有限值投影诊断，没有被称为连续无限尾界。它表明准确平坦传播在该固定计算角中会产生难以低阶截断的结构，不能把“准确公式存在”直接变成“低阶 BVP 初猜已经良好”。

[角表示核查脚本](../scripts/fd2d_native_coast_chart_audit.py) 与 [实际核查报告](../notes/2026-11-12-fd2d-native-coast-chart-audit-01.json) 直接核对保存表：全部 $9$ 圈的 $\pi$ 周期、$\phi\mapsto-\phi$ 和 $\phi\mapsto\pi-\phi$ 奇偶误差不超过 $4.45\times10^{-16}$。原数值材料反解残差不超过 $1.94\times10^{-13}$，入口 $U_{\rm seed}$ 数值反解误差不超过 $6.08\times10^{-18}$；加上准确 $D>0$ 的唯一性，可排除把这些大截断误差归因于重复周期分支的解释。

最陡变化出现在 $\phi\approx\pi/2\pm.03$ 附近。实际空间曲率仍有 R137 的有限约 $4.25$ 上界及本稿 native 矩阵的严格包；角截断困难不等于几何曲率发散。后续可以比较入口母线标签作为计算角的表示，而不改变共同物理 $g$。在非零外设计下，该图若使用也必须作为明示固定参考坐标处理。

