# 同一真实对象上的普通段／转折段标量时间圆接口

本页记录独立实现 `scripts/fourfold_phase_unified_scalar_time_circle.py`。
它不改动已冻结的普通段 scalar-circle、turn Taylor 或任何域证书。
对象是显式径向对称、无限角原函数的 exact affine δ₅ 图；准确参数为

\[
\delta _5=-7789843107295549/4611686018427387904.
\]

本模块只构造已付解析芽的真实场采样。有限二维多项式、全角／全时间补集、
参考残差及真实返回的比较仍由各自证书负责。

## 1. 精确对象、时间和解析芽

构造器读取 retarget descriptor 和一份通过的 whole-angle/complex-time
域报告；支持普通 JSON 和 gzip。逐一核对 descriptor、目标图、真根证书、
准确参数、旧参考的时间网格 manifest、分支符号、segment 和准确 subspan。
时间端点统一表示成

\[
q+p\pi\qquad(q,p\in\mathbf Q),
\]

并核对它们确为保存网格端点的相应仿射组合；从而首末 \(\pm\pi/2\)
没有先变成浮点数。记端点为 \(a,b\)，\(c=(a+b)/2\)、\(h=(b-a)/2\)，
保留 \(h\) 的符号。

`germ` 选择报告里一个已通过的实际 common span。若真实时间区间还穿过
别的 span，接口明确把所选结果标作该芽的解析延拓，不能把它授予整个
实际分段场。相邻芽的完整覆盖／cap 费用须另付。

所需域仅为该叶已经付清的 \(|u|<R\)、物理角 \(|\Im\theta|<S\)。
没有强制要求 \(R=6\)；全支当前使用的 \(R=3\) 足以在 \(|u|=1\)
或 \(5/4\) 上采样。

## 2. 普通段和真实转折使用同一几何场

普通段用

\[
r=t\sin(c+hu),\quad r_\tau=t\cos(c+hu),\quad
f=-r_\tau\frac{M+\sigma\sqrt{-K_0}\,W}{D}.
\tag{1}
\]

其中 \(t\) 是同一实际目标度量的已认证正根。\(D,M,W\) 是冻结
`f_invariants` 的移动 frame 不变量，\(\sigma\) 是该腿保存的符号。
普通段的 square root 采用已证 \(\Re(-K_0)>0\) 的主支。

负、正真实转折分别取 \(s=-1,+1\)，令

\[
\eta=\pi/2-s(c+hu),\quad r=st\cos\eta,\quad r_\tau=t\sin\eta.
\]

正根附近定义

\[
J(\rho)=-\frac{K_0(t-\rho)}{\rho},\qquad
Q(\eta)=\frac{tJ(t(1-\cos\eta))}{1+\cos\eta}.
\tag{2}
\]

准确的 \(K_0(t)=0\) 来自已有真根证书。显式对称性使负根使用同一个
正根函数 \(J\)。物理内侧的恒等式为

\[
\sqrt{-K_0(r)}=\sin\eta\sqrt{Q(\eta)},
\]

故转折采样采用

\[
f=-t\sin\eta\,
       \frac{M+\sigma\sin\eta\sqrt Q\,W}{D}.
\tag{3}
\]

这里必须保留解析的 \(\sin\eta\)，不能换成绝对值，也不能在跨根的
复时间盘重新使用 \(\sqrt{-K_0}\)。已付 \(\Re Q>0\) 给出同一解析支。
若准确有理 \(u\) 满足准确 PiTime \(\eta=0\)，(3) 严格等于零；接口
在这个已认证的无零分母点返回准确 `acb(0)`，而非用浮点 cos(π/2)。

## 3. Q 的有限径向多项式和完整余项

设在 \(|r-t|\le R_K\) 上实际 \(K_0\) 全解析且 \(|K_0|\le M_K\)。
源码重算这个门：真实无限 primitive 给出复平均度量 \(E\)，并检查
实际 \(a\)、\(E\) 均不为零。对真根处的完整 jet 写

\[
K_0(t-R_Kz)=\sum_{m\ge1}a_mz^m.
\]

保留 \(d\) 个 \(J\) 系数得到

\[
J_d(\rho)=-\frac1{R_K}
              \sum_{j=0}^{d-1}a_{j+1}(\rho/R_K)^j.
\]

它是已知有限多项式，采用 Horner 在真实、可能非零的复 \(\rho\)
直接求值，不把截断解析级数平移当成精确运算。Cauchy 界给出

\[
|J(\rho)-J_d(\rho)|
\le\frac{M_K}{R_K}
       \frac{(|\rho|/R_K)^d}{1-|\rho|/R_K}.
\tag{4}
\]

代码要求 \(|\rho|<R_K\)，把 (4) 有向加到复球，再除以真实
\(1+\cos\eta\)，检查 \(\Re Q>0\) 后开根。默认 \(R_K=3/1250\)、
\(d=64\)。所有有限系数已包含真根不确定性、角原函数无限尾及区间
运算误差。缓存键包含对象、根证书、精度、节点数、各半径、阶数和根球，
不会跨目标复用旧图的曲率。

## 4. 一次径向 majorant 支付全部 scalar nodes

普通段的同一中心是 \(r_c=t\sin c\)。\(|u|\le R\) 上

\[
|r-r_c|\le |t|\{ |\sin c|(\cosh H-1)+|\cos c|\sinh H\},
\quad H=|h|R.
\tag{5}
\]

转折用相同恒等式的 cosine 版本、中心 \(r_c=st\cos\eta_0\)：

\[
|r-r_c|\le |t|\{ |\cos\eta_0|(\cosh H-1)+|\sin\eta_0|\sinh H\}.
\tag{6}
\]

若此上界为 \(d_r\)，每个节点处半径 \(R_0\) 的圆盘均含于中心
\(R_0+d_r\) 圆盘；\(R_E\) 也同理。扩大两个半径不改变
\(R_0-R_E\)，所以一次中心预算可以支付全部节点的 primitive 和
\(E\) 无限尾。每个节点的 \(E\) 导数依旧使用节点的 \(R_E\)
Cauchy 分母；不会把较大中心半径偷换为节点的合法半径。

节点几何由 `complete_data` 在复 \(r\) 直接重算，保持复 \(E\)；
不调用会在实径向 jet 口径下取实部的 `target` 来求复节点的平均度量。
有限 Fourier 系数通过 native Arb FFT 在整角网格求值，再单付真实
primitive 径向导数的无限尾。每个采样点都检查实际 \(D\) 的模下界。

## 5. 对外接口与后续使用

```python
model = UnifiedScalarTimeCircleField(
    descriptor_path, domain_path, germ=-1, nodes=1024,
    root_nodes=None, radial_degree=64,
    curvature_radius=Fraction(3, 1250))
values, timing = model.sample(u, angles)
```

`values[j]` 是物理角 \(\theta_j=\pi j/(2N)\) 上真实 \(f\) 的复球。
它没有乘时间尺度 \(h\)。保留的属性包括 `outer`, `strip`, `modulus`,
`sign`, `center`（径向中心）, `tau0`（物理时间中心）, `h`, `cell`,
`root`, `root_package`, `object_path`, `root_path`, `target`。
`time_endpoints`, `exact_tau0`, `exact_h` 为准确 PiTime 对象。
`identity()` 返回对应哈希、准确时间、模式和单芽范围。

此类满足已冻结 `circle_coefficients` 和 `time_alias_bounds` 的采样契约。
准确实系数、同一主平方根支及 (3) 使
\(f(\bar u,\theta)=\overline{f(u,\theta)}\)（实 \(\theta\)），
因此可以只算半个时间圆，再用准确共轭恢复另半圆。

## 6. 实际完成的独立核验

入口命令保留在 frozen manifest。已对真实 forward 0、1 的域分别完成：

- 在 \(u=\frac54\{1,i,e^{i\pi/4},-1,-i\}\) 计算完整 512 角节点；
- 用已冻结、独立构造的 `TurnCollarTimeModel` 得到 64 阶真实时间 jet，
  在四个角核对新 scalar 值；
- 不直接比较两个截断值，而对旧时间 jet 添加完整尾
  \(M(|u|/R)^{65}/(1-|u|/R)\)；
- 对 forward 0 的准确首端点检验所有角严格为零。

实际设置为 Q=512、N=512、256 bits、径向阶数64；两段、五个时间点、
每点四角的独立核验全部通过。整批耗时198.99秒、CPU26.32秒。
以下数值仅概括报告保存的有向区间，严格口径以 JSON 的端点为准：

| 实际段 | scalar复球分量半径最大值 | 采样D模下界 | 完整J径向尾最大值 |
|---|---:|---:|---:|
| forward0 | <9.495×10⁻²⁹ | >.65565 | <1.760×10⁻⁸⁶ |
| forward1 | <2.303×10⁻²⁸ | >.65429 | <4.421×10⁻⁵¹ |

对应报告为
`data/phase_ring_continuation/type_fixed_step02_d5_step5_unified_scalar_turn01_pilot.json.gz`。
首端点u=−1在全部512角得到严格零。

普通419另由 `fourfold_phase_unified_scalar_ordinary_probe.py` 对同五个
时间点、完整512角与冻结 `SharedBudgetScalarField` 交叉检查，所有复球
重合，耗时40.32秒、CPU5.50秒。报告为
`data/phase_ring_continuation/type_fixed_step02_d5_step5_unified_scalar_ordinary419_probe.json.gz`。
这份回归故意保留原三germ外包的身份，所以接口把其所选main germ
标作解析延拓；它没有借用后来的sharp单芽结论来改变输入报告的范围。

此处的球半径不能转授后续转折段。越靠近root芽另一端，
\(|\rho|/R_K\)可能增大；调用者可提高 `radial_degree` 或改用时间圆半径1，
但必须保留逐节点完整J尾。无需为此把所有叶提升到R6。

报告中的逐点重合是实现交叉核验；该接口的全时间/全角数学依据是输入的
真实域、(2)–(6)、有向 primitive 尾和节点区间运算，不能把有限个重合
点单独解释为连续域证明。全 field Fourier package 仍须支付角 alias、
遗漏角模、时间 alias 和遗漏时间项；全真实 flow 则另须支付完整残差。
