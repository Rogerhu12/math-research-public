# 均衡曲率卵形核：冻结输入与强 BVP 接口

2026-11-12，constructive_geometry；完整证明见
`../results/R118-balanced-oval-with-exact-moments.md`。

## 已闭存的输入

准确中央 seed 是 `BalancedOvalCore()`，参数修正 q 初始全零。
脚本：`../scripts/fd2d_balanced_oval_core.py`。
SHA256：`1df75241ec76ae9a28042b72cbb721de61e7283378d82e7dea5ff05c3f84b692`。

它严格保留原 (1.4,.5) 椭圆的周长 `2*pi*a0`，
`a0=1.0040828380214688` 是数值评估值，准确值按原椭圆积分定义。
新的长短轴支持准确为 1.405、.495，三个准确积分矩补偿支付周长与两轴支持，
不靠求根器或近乎零的浮点修正值支付准确性。

独立区间证书 `2026-11-12-fd2d-balanced-oval-moment-certificate.json`
证明参考 `.228<rho<3.17`；
允许有限零均值支撑参数 `sum((4*j*j-1)*abs(q_j))<=.012` 后仍有
`.216<rho<3.182`、`A_q>=1.401`、`B_q<=.499`、`A_q-B_q>=.902`。
这是中央曲线和其圆柱段的结论，完整活动核几何尚未验证。

## 消费接口

```python
import importlib.util
from pathlib import Path
import numpy as np

script = Path('topics/visible-flexible-closed-surface/scripts/fd2d_balanced_oval_core.py')
spec = importlib.util.spec_from_file_location('balanced_core', script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
core = module.BalancedOvalCore()
u = 2*np.pi*np.arange(512)/512
initial = core.gauss_codazzi_initial(u)
# X, X_u, X_uu: material sigma; n=1/rho, m=l=0.
theta_initial = core.gauss_codazzi_initial(u, reference_angle=True)
# X_u/X_uu remain material sigma derivatives sampled at sigma(theta).
# X_theta/X_thetatheta are the distinct reference theta derivatives.
```

法向与 R116 相同：`e1=ez`、`e2=unit tangent`、`N=ez cross e2` 为平面内法向。
所有参数 JVP 和 Hessian 与 R115 一样按固定材料角计算。
`reference_angle=True` 使用**原** (1.4,.5) 椭圆的固定 sigma(theta)，
不是新曲线的法向角或按 1.405/.495 新建的偏心角。
尾 DN 仍使用材料 sigma；连接 cut 时要做固定坐标转换。

旧接口原字节快照 `../scripts/fd2d_balanced_oval_core_aa56_snapshot.py`
保持 SHA256 `aa56c7d69b0d7a855ab8617f68657f25912a6a094704f3c619d22c3834a49c7b`。
该快照用于复现 root 的入口角谱表；新版只澄清 jet 字段并增加接口核对，数学定义不变。

### 已完成的计算坐标选择

root 的 `2026-11-12-fd2d-balanced-inlet-coordinates-01.json` 对同一个准确 seed 做了
三种固定计算角的实际 Fourier 入口比较；它绑定上述 aa56 原版快照。2048 点评估下，
原椭圆偏心角 θ 在 M=255 的实际中央 metric 为 `5.4332e-9`，
材料角 σ 在 M=255 为 `1.76675e-7`；固定 seed 法向角 φ 在 M=191 为 `5.367e-13`，
n 投影误差 `4.054e-12`。φ 在 M=127 仍为 `6.001e-9`，因此不能只因换角就无视角分辨率。

几何曲率更均衡没有自动使任意材料坐标的谱更窄。可采用固定
`sigma=S_seed(phi)/a0`，目标角系数成为 `b(s,phi)=a(s)*rho_seed(phi)/a0`。
此图仍表示相同物理 g；若随后变动中央参数，仍复合**同一个 seed 图**，
不能改用各参数自己的法向角。此表只决定输入图的谱成本，未做径向 ODE、BVP 或连续误差证书。

有限输入检查已通过：弧长逆最大残差 `1.69e-14`，两种角度下速度误差 `<4.45e-16`。
其报告 `2026-11-12-fd2d-balanced-oval-core-check.json` 与区间证书均绑定当前源哈希。
带中央括区保护的 Newton 修复已包含；先前普通在括区内的 Newton 在四个偏心角样本处
会在两端间交替，未改变数学曲线，只修复数值反演收缩。

## profile 与尾接口的冻结范围

中央 seed 的变化不改变 v2 的完整 a(s)。现有 v2 文件保持原样：
`2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json`，
SHA256 `064a7a3bcb7beaaa45bf59e30e0c64be58106a566edfa55d6b3c4bf6480b2ba0`。
新的提前浅回转后缀仍在选取，未冻结前不把它与 v2 混为同一个候选。

闭合尾保持 cuff=.32、cut=.4、w=.1、wr=-1.75；
`a'_cut=-10/sqrt(101)`、`a''_cut=1750/10201`。
有限线性端口、非线性尾 DN 配置和上半面反射约定保持已有记录。
不再采用单调直接收缩所得 v3；其有限 m2 匹配的末端放大约 70，已经排除为当前强几何种子。

## 后续真正需要核验的条件

R118 不替代实际 GC/BVP 的 E/F/G、主曲率、n 图有效性或尾部匹配。
完整活动核还须满足 R113 的 `|y|<=.75`、held 保护曲线、全时 reach、球包、接口高度及两 jet。
若在此 seed 上再使用 R116 §6 的中央曲率参数，需用新的统一 n 区间重付该节的小参数常数。
当前的参数族与新 profile 可各自独立选择；一旦完整 profile 冻结，求解过程中必须保持同一个 a(s)。
