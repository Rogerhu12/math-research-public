# 重建后重新通过的实际根 collar 有向有限部

状态：**本笔记的根 collar 界已由完整有向计算证明；全 beta 的 bulk 积分尚在计算。**
本轮执行环境重置后，未推送的旧脚本和完整报告均不可恢复。本笔记使用重建源码从头运行，
不把旧输出哈希转授给新源码。一般证明机制见 [R52](../results/R52-root-taylor-finite-part-and-directed-budget.md)。

## 1. 同一实际对象与本轮文件

冻结输入为 type_fixed_step02_analytic_smoothing_inputs.npz，SHA256：

    bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532

它定义原 sym step02 的无限 R33 primitive；radius、beta 显式取偶，gamma 和冻结 slope 的
准确积分 height 显式取奇。使用 R37 的全 ell 口径，负核心内 chi=1。没有把 Gaussian 近似、
旧 Greville 图、附近 D5 图或有限 Fourier 曲面替换进来。

本轮源 scripts/fourfold_phase_beta_interval.py 的 SHA256 为：

    ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f

完整报告 notes/2026-11-12-beta-recovered-full-collar-enclosure.json 的 SHA256 为：

    7a1687cc304cc29334de3e078c4ce427486f76183a517ed3b465c915802a0200

它使用已推送的 tight root 证书，SHA256：

    3d6018b0a17e1ea5ec1b21fd28d886bc7454a91973fbcfd0cfaa3d7ee4ecc66b

代码核对输入和根证书哈希；此入口目前只接收这个原图。换 D5 对象必须另付同一对象的根与全部积分。

## 2. 重新取得的完整有向界

固定物理切口为准确有理数

$$
b=\frac{1072423152036779}{4503599627370496}.
$$

从原 tight root 证书出发，先修正完整无限角均值 E，再做三次区间 Newton，得到

$$
0.23836991573146337267349149754020
<t<
0.23836991573146337267349149759844.
$$

取 rho=t-r、eta=t-b。每一个正负 scalar knot 都以准确 binary rational 检查；
物理区间 [b,t] 不跨任何 knot。主结果是

$$
\boxed{1305.4032588697<I_{\rm collar}<1305.4032591712.}
$$

这里 $I_{\rm collar}$ 是同一实际无限对象、同一 R37 零阶选择下的正侧 collar 有限部，
已经包括精确根宽度、全部 primitive tail/alias、完整 E 修正、Arb 舍入、径向余项和角求积误差。

这次输出的多项式有限部中心仍约为 1305.403259020484338；严格误差预算为

| 项目 | 本轮有向上界 |
|---|---:|
| 径向 Taylor 余项 | 1.5070392e-7 |
| 完整角均值余项 | 1.3345362e-13 |
| 合成积分球半径 | 1.5070405e-7 |

根展开前两项重新包住旧高精度诊断值：

$$
g_0=-0.0064282775012557264568\ldots,
\qquad g_1=-1.3731448371519669985\ldots.
$$

以上小数用于识别本轮对象；后续程序使用完整报告中的有向球。

## 3. 重建后的复域证明

所有 scalar 都先由其本地样条段生成完整多项式，再组成解析 primitive。只把这个本地多项式
解析延拓用于 Cauchy 估计，不声称有限 C4 样条穿过其他 knot 后整体解析。
NativeSpline 的缓存建立时强制 precision cap 至少 degree+1，避免低阶调用截断缓存多项式。

外部 Cauchy 半径为 R0=.003、RE=.0025，源归一化角宽为 .32，primitive quarter 网格为512。
native 径向 series precision 为72。真正连续复域是

$$
|\rho|\le R=.0006,\qquad |\operatorname{Im}(4\theta)|\le\sigma=.02.
$$

2048 个实际角单元连同准确半格 pi/2048 覆盖全实圆，故系数费用使用
sigma+pi/2048。有限 Taylor 多项式在整圆盘上由系数绝对值和包住；
有限多项式之外的完整解析尾用 R52 的显式 Cauchy 导数余项支付，
无限 primitive 的 omitted/alias 误差另用更大复域支付。

在目标曲率层，有限 E 在 RE 圆盘上的界取

$$
M_E^{\rm fin}=3\bigl(M_F^{\rm fin}/(R_0-R_E)\bigr)^2.
$$

E 的前四个导数都分别加上有限 Taylor 尾和无限 E 的 Cauchy 导数误差。
由实际 scalar a 和这些 E jets 直接形成 K0、K0'、K0'' 的完整复圆盘包络。
真根 deflation 使用准确恒等式

$$
\kappa_0^2(\rho)=\int_0^1K_0'(t-u\rho)\,du,
\qquad
(\kappa_0^2)_\rho=-\int_0^1uK_0''(t-u\rho)\,du.
$$

第二式的包络为 -K0''/2；没有在含 rho=0 的区间上除以 rho。
程序严格检查 Re(kappa0 squared)>0，随后使用同一解析平方根支。

几何计算始终在旋转柱坐标基内进行，点积和叉积保持准确双线性。
设 C=Ftheta cross Fr、A2=C dot C、R2=F dot F、h=C dot F，
原 R32/R37 主系数同时乘 zeta squared 后为

$$
\widetilde a=-n/A^2,\quad\widetilde b=m/A^2,\quad\widetilde c=-l/A^2,
\qquad
\widetilde\omega=(K_F-K_0)/\widetilde a.
$$

同样消去零阶分母中的共同 zeta 因子后，所有剩余除法都使用实际 A2、R2、h、atilde、Fz。
连续复域上全部通过的实部下界可安全缩写为

$$
\operatorname{Re}A^2>1.793,\quad
\operatorname{Re}R^2>1.182,\quad
\operatorname{Re}h>1.206,\quad
\operatorname{Re}\widetilde a>.1388,\quad
\operatorname{Re}F_z>.2677.
$$

这些是整圆盘、整复角条带的包络结果，不是节点符号检查。

R52 的 regularized 角密度为 G(rho,theta)=A+rho B+rho squared C。
本次直接用 |A|+R|B|+R squared|C| 包住它，得到

$$
\sup|G|\le0.046404445251342356204986572265625<.047.
$$

真实角均值与积分分部后的这个 regularized 密度均值相同。
其径向24阶多项式按每个幂的准确有限部积分；Taylor 尾和角梯形求积尾分别用 R52 公式支付。
整个过程没有拿两个不同的数值 collar 相减来外推有限部。

## 4. 重放

```bash
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_interval.py \
  --frozen-inputs data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_symmetric_root_tight_interval.json \
  --infinite-tail --bits 192 --quarter-nodes 512 --angles 2048 \
  --degree 24 --precision 72 --collar-domain \
  --fixed-cut 1072423152036779/4503599627370496 \
  --out notes/2026-11-12-beta-recovered-full-collar-enclosure.json
```

本次用时约159秒。后续汇总必须解析报告中的 lower/upper 字符串，
因为 ball 字符串为了可读性可能比实际有向球额外放宽；二者都安全，但前者保留预算精度。

## 5. 仍未完成的工作

本笔记不宣称全 beta 区间。还要按所有准确正负 binary knots 覆盖 [0,b] 的实际 bulk，
再用 beta=(Ibulk+Icollar)/2 合成，继而检查 R34 的危险格。
原图与 D5 exact-affine 图的 beta 已知在诊断层就明显不同，不能互换。
真实 PDE 完整网络、低频块、非线性闭合和本题 README 的有限幅结论仍须继续支付。
