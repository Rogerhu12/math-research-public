# 实际特征场的单 span 时间 Taylor 层与首个严格小模型

2026-11-12。**本文件的局部时间级数与小模型误差门已实际运行通过。**
这不是全初值圆周、完整一条腿或实际共轭残差证书；下一步将同一
接口应用于已保存的全初值 Bernstein 参考函数。

## 1. 对象、坐标与符号

采用准确仿射第二步对象
`type_fixed_step02_d5_exact_affine_step2_object.json`，SHA256
`aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1`，
$\delta=-15291006546051/9007199254740992$。原点与方向保持
`0d17500a...`、`8db5d57d...` 的准确实数仿射定义，不先舍入控制值。
根证书为 `type_fixed_step02_d5_exact_affine_step2_root_tight.json`，
SHA256 `c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb`。

正则时间为 $r=t_*\sin\tau$。本接口保存的 sign 与
`fourfold_phase_exact_affine_nodes.py` 的 DOP853 数据严格一致：

$$
f(\tau,\theta)=t_*\cos\tau
 \left\{-\frac m n+\mathrm{sign}\frac G n\sqrt{-K_0}\right\}.
\tag{1}
$$

若另用 $-(m+\sigma\sqrt{-K_0}G)/n$ 记号，则
$\sigma=-\mathrm{sign}$。不能只按“正向腿”猜测标签。
$n,m$ 均为原始二型系数，$G$ 是实际面积平方，$K_0$ 来自
真实无限原函数的目标 $E=\langle F_r\cdot F_r\rangle$。

在移动正交标架中记
$P=1+\beta_\theta,u=\gamma_\theta,p=\beta_r,q=\gamma_r$，
$c=\cos\gamma,s=\sin\gamma$，$X=F_r$，
$Q=cX_z-s(X\cdot U)$、$v=X\cdot V$。那么

$$
D=PcQ-uv,\quad M=pcQ-qv,\quad W=Q^2+v^2,
\qquad n=-a^2D,\ m=-a^2M,\ G=a^2W,
$$

故式 (1) 等于 $-t_*\cos\tau(M+\mathrm{sign}\sqrt{-K_0}W)/D$。
源码直接给 f、$f_\theta$、$f_{\theta\theta}$。求状态角导数时
使用准确 $X_\theta=a_rT+aT_r$；没有对有限 primitive 求角导数
然后当成准确无限对象。第一、二阶标架恒等式与 R59 相同。

## 2. 先提取径向 germ，再复合时间与角函数

令 $\tau=\tau_0+hu$，给定有限参考角多项式 $Y(u)$ 和有限
对数权多项式 $L(u)$。先用全部原始与反射 knots 的准确 Fraction
选择一个共同闭 span，并检查整个实际实 $|u|\le1$ 的
$t_*\sin\tau$ 都落在这个 span 内。

`AffineBulkTarget` 的显式 span 选择先在 Arb 中组合 $c_0+\delta v$
与 $\alpha_0+\delta w$。背景权重乘积后的物理相位最高为20次，
因此至少保留21个径向系数，取得完整标量多项式。半径、高度和
相位都作同一明确反射；高度仍是准确斜率积分。

径向 Fourier primitive 与 $E,C,K_0$ 取更高阶 jet，再复合

$$
v_r=-\frac{t_*\sin(\tau_0+hu)-r_0}{R_E},\qquad
r_0:=t_*\sin\tau_0.
$$

这里常项准确为零是**定义上的同一锚点恒等式**，不是忽略根
区间误差；germ 的中心仍包含整个已证根区间。若调用者另给一个
近似 $r_0$，则无权把常项误差删掉。

角函数在有限相位的 sin/cos 与有限 Fourier primitive 求和层
复合 $\theta=Y(u)$。$\beta_r,\gamma_r$ 是先在固定角下求径向
导数，再沿时间曲线评价；它们不是总时间导数除以 $r_\tau$。

## 3. 无穷 Fourier 与目标 E 的误差

底层 native Arb 引擎对有限 DFT、三角函数、平方根及所有级数
四则直接给包含区间。无穷 primitive 的误差另由 R33 解析带预算
支付；有限 FFT 加密差不用于认证。

设外径向盘半径 $R_0$，内径向盘半径 $R_E<R_0$。
在外径向盘乘所需角带上，若每个 primitive 分量的误差为
$\epsilon_F$，Cauchy 给整个内径向盘上的

$$
\epsilon_X\le\epsilon_F/(R_0-R_E).
$$

时间外盘为 $|u|\le R>1$。通过

$$
|r(u)-r_0|\le |t_*|\{e^{|h|R}-1\}<R_E
$$

及参考有限多项式的完整模和，确认该盘的全部 r、$Y(u)$ 像落在
已付径向盘和角带内。于是复合后的每个无限 X 误差系数至多
$\epsilon_X/R^j$，逐系数插入区间后才形成 D、M、W 与残差。
对实参考，真实系数为实数；对复角系数保留完整复矩形误差。

目标 E 用有限 primitive 的准确 Parseval 二次平均，再加
$3\epsilon_1(2M_1+\epsilon_1)$ 的无穷修正，其中
$\epsilon_1$、$M_1$ 分别包每个 $F_r$ 分量误差与有限分量界。
这个误差在复径向盘上成立，再按径向 Cauchy 逐系数支付，随后才
组合 $C=a_rE_r-2a_{rr}E$ 与 $K_0=C/(2aE^2)$。因此真实 E 的
尾误差及其径向导数没有遗漏。

外复盘不要求其所有 r 值仍位于实 span 内：使用的是该准确
多项式 germ 的解析延拓。实际实时间轨迹留在所选 span 内的门
已单独检查；不能因此把相邻 span 当作同一个多项式。

## 4. 时间截断尾与连续残差

在更大时间盘，把 r、$Y$ 的完整像作一次粗 Arb 盒评价，包含
无穷 primitive/E 修正，并证明 $D\ne0$ 和
$\operatorname{Re}(-K_0)>0$。后者固定与实轴正平方根一致的
解析分支。这个粗盒只用于解析域和场的上界，不用于直接相减
$Y_\tau-f(Y)$。

设外盘上 $|f|\le M_f$、$|f_\theta|\le M_1$，保留
$j=0,\ldots,N-1$ 的真实时间系数。参考导数是已知有限多项式，
若其次数小于 N，则在实 $|u|\le1$ 上

$$
\|e_0\|_\infty\le
\sum_{j<N}|[Y_u/h-f]_j|+
\frac{M_fR^{-N}}{1-R^{-1}},
$$

$$
\|e_1\|_\infty\le
\sum_{j<N}|[L_u/h-f_\theta]_j|+
\frac{M_1R^{-N}}{1-R^{-1}}.
$$

这保留时间依赖后相减，避免宽时间盒中的低阶依赖损失。
外盘的状态角盒还包含严格正的额外半径 d，因此同一次场评价
给 $B_2\ge|f_{\theta\theta}|$，可接 R60。q 的模由整个有限
L 的实部界给出。时间正反向都采用 $2|h|$ 积分长度，并按 R61
统一改变场与参考导数的方向。

## 5. 实际小模型与结果

本次取 $\tau_0=1/2$、$h=1/16384$、外盘 R=8、
$R_0=3/1000$、$R_E=1/400$、原函数归一角带宽 $8/25$。
参考为7次多项式，$Y(0)=3/10$、$L(0)=0$。通过逐项选择
binary64 中点生成其余系数，**这些选定的准确有理系数本身**
定义最终参考；没有声称生成算法准确求解方程。
完整系数与准确实共同 span 均保存在报告中。

选择 N=17（0至16阶），状态管半径 $d=1/65536$。初值定义为
这个参考在 $u=-1$ 的准确有理值，因此本小模型的初始误差为零。
它不是当前全局 H 初值或整条已保存射线。

| 原函数 quarter 节点 | E 无穷误差上界 | 连续 $|e_0|$ 上界 | 连续 $|e_1|$ 上界 | R60 实际流误差上界 |
|---|---:|---:|---:|---:|
| 256 | $1.083\cdot10^{-9}$ | $8.310\cdot10^{-9}$ | $4.137\cdot10^{-9}$ | $1.015\cdot10^{-12}$ |
| 512 | $8.743\cdot10^{-28}$ | $5.503\cdot10^{-14}$ | $5.479\cdot10^{-13}$ | $6.718\cdot10^{-18}$ |

256点的瓶颈明确是已支付但很松的 E 无穷尾；因此只把原函数
节点数加倍，未改变 Newton 网格或给出新的几何候选。512点下
时间 Cauchy 尾分别小于 $5.100\cdot10^{-17}$ 和
$1.168\cdot10^{-16}$，X 无穷差小于 $1.706\cdot10^{-33}$。
q 约在 $[.99999360,1.00000640]$，R60 管余量远大于所需误差。

独立轴对称模型 $X=(2,0,3),K_0=-1,a=1,r_\tau=1$ 给
$f=-13/3,f_\theta=f_{\theta\theta}=0$，源码每次运行都检验。
另与独立浮点非径向 evaluator 比较 $\tau=.5,\theta=.3$，
f 与 $f_\theta$ 差约 $2.15\cdot10^{-12}$、$1.06\cdot10^{-12}$。
此比较只用于定位符号/坐标错误；严格界来自 Arb 和上述完整
误差预算，不把浮点差当作认证误差。

## 6. 冻结与重放

源码 `scripts/fourfold_phase_field_time_taylor.py` SHA256：
`5f8b0294bc3cc6f19444ebf2d8e5106bdabaecab44576a77593890b2c42c312a`。

两份报告位于 `data/phase_ring_continuation/`：

- `type_fixed_step02_d5_exact_affine_step2_field_time_pilot_q256.json`：
  `6109df95237a2004630c287337184880acd3b2acae7c01474c9265bf09ed9ff0`。
- `type_fixed_step02_d5_exact_affine_step2_field_time_pilot_q512.json`：
  `b37d1ac92647cb58627d8b7374172303ae9b646af965cb6132e78f3a964f6b8d`。

native 四个依赖源码 hash 及全部准确输入身份均在报告内。
从仓库根目录：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_field_time_taylor.py \
  --object topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --quarter-nodes 512 --out /tmp/visible-field-time-pilot-q512.json
```

用 `--quarter-nodes 256` 可复现第一列对照。报告保存运行耗时，
独立重放的字节 hash 可不同，但科学区间与源码/输入身份须对应。
API `FieldTimeModel.time_field()` 与 `residual_bound()` 接受明确
有限参考系数；实际 Bernstein 参考的准确变换将由独立适配器处理。
