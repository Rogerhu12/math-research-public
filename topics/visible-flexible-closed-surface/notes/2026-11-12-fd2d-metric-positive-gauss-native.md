# R153 实际正 n 窗字段：原生读取、准确角 jets 与真实 K_s

## 1. 本组已完成与未宣称的内容

本组把 [R153](../results/R153-positive-n-local-Gauss-parameterization.md) 的新有限场定义接到已有 R149 原生读取器。消费者读取真实保存的 P1 correction、物理 bump 参数及完整 atlas/lifting 定义；它没有重新求解 BVP，也没有把原三场中的独立 $l_0$ 误当作新实际 $l_*$。

唯一实际检查输入是
`2026-11-12-fd2d-positive-gauss-warm01-warm.npz`，56874 B，SHA256
`4a3737df628b837143cf3237624656fb7e7c7721495e8df6f0199c5301e6c2a2`。
检查只询问三个径向内部点、八个固定计算角，另加窗外和准确切口。它支付下文列出的有限接口和差分核验；它不是正域、残差、曲率、闭曲面或强目标的连续证书。

正式源：

- `scripts/fd2d_gc_positive_gauss_l_native_field.py`，14983 B，SHA256 `d48399b351fa818f3b3be1359f34a504c4e7f832d201c2d528216590fb9efc7d`。
- `scripts/fd2d-metric-positive-gauss-native-check.py`，12218 B，SHA256 `c0761152a9be152c2507cdf0d864908ea3f5e365e05c100c83fd25186a385718`。

新读取器绑定数值端已经冻结的 provider `fd2d_gc_raw_bump_positive_gauss.py`（SHA256 `7f80d5caf02e46f92bbb32cf96cedad3754aea6f6511ead1d8c5387814b2e0bb`）与 algebra `fd2d_gc_positive_gauss_l.py`（SHA256 `161389ae9ab106bb2ad62ab64d91bb875eaf07996b088f20115f87259c80b6be`）。这些源、旧 R149 reader 和旧 reference 源均未由本组修改。

## 2. 绑定的实际函数，而不是样本插值

物理坐标为 $s=x$，计算角为 R149 中准确声明的 $u=U(s,\xi)$。在固定这一份保存参数 $p$ 后，目标是同一
$$g_p=ds^2+a_p(s)^2du^2,\qquad K_p=-a_p''/a_p.$$
表示替换不再改变这一份 $g_p$；这不把不同 bump 参数的候选误说成同一个物理度量。

先由原 R149 完整函数读取 $(n,m,l_0)$。其 correction 按保存的 123 个节点作准确 P1，角方向按保存 Fourier 系数求值；完整 seed、tail、frozen coast lifting 和真实 angular atlas 不作新的低模截断。字段不是从本组八个角样本定义的，也没有重建或清洗保存节点。

保存的 `gauss_l_definition` 必须明确给出 schema
`fd2d-positive-n-local-Gauss-l-field-v1`、两个原源 SHA、物理支撑 $[e,f]$、rim 比例、同一个 S5 窗、平台及真正无效 P1 帽函数节点。本 reader 核对这些字段及保存 mesh。当前
$$
e=0.5919999999999992,\quad f=0.8675434451024153,\quad
\text{rim fraction}=0.12.
$$
准确平台由同一保存二进制端点计算为
$$[0.6250652134122892,\ 0.8344782316901254].$$
声明的有限求值 floor 是 $0.05$。它只在 $w>0$ 时用于有限求值拒绝，既不是连续正域证明，也不是原连续问题的必要条件。

新场定义为
$$
H=\frac{K+m^2}{n},\qquad l_*=(1-w)l_0+wH\quad(w>0),
$$
在 $w=0$ 时直接沿用 $l_0$，不进行除法。$n,m$ 的五组已提供 jets 原样保留。真实 Gauss 缺陷准确满足
$$n l_*-m^2-K=(1-w)(n l_0-m^2-K).$$
当前 six inactive $l_0$ 节点为 65–70；它们的整片 P1 帽函数支撑均在 $w=1$。reader 只核对该声明与实际 mesh，并不把 rim 邻接的自由度删掉，也不改保存数组。

## 3. 两种接口及所需正则性

```python
from fd2d_gc_positive_gauss_l_native_field import PositiveGaussLNativeField

r = PositiveGaussLNativeField(
    field_npz, candidate_json,
    reference_inlet=inlet_npz, reference_cache=reference_cache_npz)

q = r.evaluate_native(s, xi, side='right')
angular = r.evaluate_angular_native(s, xi, side='right')
physical = r.physical(s, material_u, side='right')
definition = r.definition()
restored = PositiveGaussLNativeField.from_definition(definition_json)
```

`evaluate_native` 返回实际字段值、$x,\xi,\xi\xi,x\xi$ jets。`side` 同时选择真实 P1 slope 和实际 atlas 的径向侧；在界面不假设 $U_s$ 或 II 径向导数两侧一致。返回键使用 `l_x`、`l_xi`、`l_xixi`、`l_x_xi`，最后一项是一阶 $x$ 与一阶 $\xi$ 混合导数。

`evaluate_angular_native` 只改动实际 $l$ 的值、$\xi$ 和 $\xi\xi$ jets，不查询 $a'''$ 或 $K_s$；它删除 `l_x` 与 `l_x_xi` 键，避免调用方错用原 $l_0$ 的径向导数。Codazzi 和固定材料角的一、二导数只需要这一层数据。原完整 reader 给出的其它坐标和 $n,m$ 数据仍可使用。

通用的径向及混合 jet 接口额外消费实际 $K_s$，仅在支撑内部查询明确 profile 的片式第三导。这是所请求 jet 的实际计算，不把闭曲面的完成标准提升为全局 C³；在片界采用真实侧限。

## 4. 完整商法则与链式公式

以下下标 $x$ 表示固定计算角 $\xi$ 的物理径向导数；原 reader 的 $n_x,m_x$ 已经包含真实的 $U_s$ 漂移。由于 $K=K(s)$，仍有 $K_x=K_s$ 与 $K_\xi=0$。从恒等式 $nH=K+m^2$ 一次、两次求导，得
$$
H_x=\frac{K_s+2m m_x-Hn_x}{n},\qquad
H_\xi=\frac{2m m_\xi-Hn_\xi}{n},
$$
$$
H_{\xi\xi}=
\frac{2(m_\xi^2+m m_{\xi\xi})-Hn_{\xi\xi}-2H_\xi n_\xi}{n},
$$
$$
H_{x\xi}=
\frac{2(m_xm_\xi+m m_{x\xi})-H_xn_\xi-H_\xi n_x-Hn_{x\xi}}{n}.
$$
然后对径向窗作准确乘积求导：
$$
(l_*)_x=(1-w)(l_0)_x+wH_x+w_s(H-l_0),
$$
$$
(l_*)_\xi=(1-w)(l_0)_\xi+wH_\xi,\quad
(l_*)_{\xi\xi}=(1-w)(l_0)_{\xi\xi}+wH_{\xi\xi},
$$
$$
(l_*)_{x\xi}=(1-w)(l_0)_{x\xi}+wH_{x\xi}
 +w_s(H_\xi-(l_0)_\xi).
$$
这些公式保留独立的原 $l_0$、其所有实际 jets、完整 $K$ 和未知场的真实角依赖。不存在把平台 $l$ 值改掉但借用旧导数的混合表示。

记 $h=U_\xi>0$，则继承的 `physical` 消费同一实际场，准确关系为
$$
f_u=f_\xi/h,\qquad
f_{uu}=\frac{f_{\xi\xi}-(f_\xi/h)U_{\xi\xi}}{h^2},\qquad
f_s=f_x-\frac{U_s}{h}f_\xi.
$$
如另需固定材料 $f_{su}$，可由
$$
f_{su}=\frac{f_{x\xi}}h-
\frac{U_{s\xi}h-U_sU_{\xi\xi}}{h^3}f_\xi-
\frac{U_s}{h^2}f_{\xi\xi}
$$
直接得到。此式不把径向 atlas 的跳当作字段值或角迹的跳。

## 5. 真实 K_s 的来源

只有径向及混合接口使用
$$K_s=-\frac{a'''}a+\frac{a''a'}{a^2}.$$
新函数 `physical_profile_third` 读取实际 base profile 的当前片：

- Hermite 半径片：保存多项式的三阶导，除以该片真实长度的三次方。
- 显式 phase 片：$a'=\sin p$、$a''=\cos p\,p_s$，所以
  $$a'''=\cos p\,p_{ss}-\sin p\,(p_s)^2.$$
  turn 的两个 ramp、二次 brake 和 cubic phase bridge 均对实际保存多项式求 $p_{ss}$；coast 的常 phase 两个导数均零。
- 所有片最后加入实际保存 bump 参数的贡献 $\sum_j\delta_j\psi_j'''(s)$。

当前窗口全在明确的 base K0 coast；因 base phase 实际恒定，其第三导确实为零，随后仍须加入非零 bump 第三导。程序使用一般实际片公式，不是把整个 profile 的 $K_s$ 静默置零。

本次三处检查中实际 $K_s$ 依次约为 $-7.75229755558$、$23.6773433589$、$-44.8446735596$。$wK_s/n$ 对 $l_x$ 的最大贡献约为 $89.1522647348$。省略这一项会产生实质错误，即使求解器本身的 Codazzi 不需要 $K_s$。

## 6. 连续性和准确 cut 的作用域

在正域内，$n,m,l_0$ 是完整已定义函数。若 $n\ge\nu>0$ 在闭窗的邻域成立，连续的 $K$ 与原共同角 jets 经上述商法则给出连续的 $l_*$ 和实际角导数。S5 窗在外端的零 jets 把它接回原 $l_0$；中央、cut 开放邻域完全不变。对真实 P1 径向表示，径向 II jets 可以逐片有不同迹，这不妨碍按 R119/R141 的固定材料 frame/位置 ODE 定义 C² 图。

reader 继承的 24 列固定材料 body RHS 动态调用这份实际 `physical` 数据，因此未来使用的是 $l_*,(l_*)_u,(l_*)_{uu}$。本组没有运行 body ODE，不从这一接口自动推出位置、metric 或 reach。仍须由后续实际场支付完整连续正域和原完成条件。

尤其是尾部可能 $n=0$ 的平直角段不属于正窗。实现先判断 $w>0$ 再除法。本次准确 cut 的八角中有四个 $n=0$，原五组 jets 完整返回且有限。

## 7. 本次真实小核结果与复现

```bash
python3 scripts/fd2d-metric-positive-gauss-native-check.py \
  --field notes/2026-11-12-fd2d-positive-gauss-warm01-warm.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --inlet notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz \
  --cache notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz \
  --out-prefix notes/2026-11-12-fd2d-metric-positive-gauss-native-check-01
```

上述唯一正式调用为 exec session **74450**，初始 chunk **5ef7a7**，完成 chunk **7c9cda**，真实 exit **0**。报告内部耗时 **5.550646765 s**，峰值 RSS **76520 KiB**。若复现须另用新输出前缀；程序拒绝覆盖既有结果。

八个计算角来自原 256 点网格的索引 `[0,5,17,31,53,71,89,123]`。表中所有数值均是这次有限取样，不能升格为区间全域结论。

| 真实点 | s | w | 样本 min n | 样本 max abs G_actual |
| --- | ---: | ---: | ---: | ---: |
| entry rim | .6085326067061442 | .5000000000000008 | .26328768756 | .37095373304 |
| plateau | .7297717225512073 | 1 | .26558319555 | 5.55111512313e-17 |
| exit rim | .8510108383962703 | .5000000000000008 | .45307399122 | .32284452830 |

主要已实核结果：

- 原 $n,m$ 的五组 jets 与 affine background 逐位相同。
- angular-only 与完整接口的值/两角导数逐位相同；前者不返回陈旧径向 $l$ jet。
- 与冻结 numerical algebra 的值/一阶角导差最大 `7.993605777301127e-15`。
- 准确 Gauss 缩放恒等的浮点差最大 `2.220446049250313e-16`。
- $x,\xi,\xi\xi,x\xi$ 的两种混合差分和 $K_s$ 差分，细步最大归一误差 `6.416081627164514e-7`；这是有限差分接口证据，不是微分函数的严格误差界。
- 窗外及准确 cut 的五组 jets 与原场逐位相同；cut 四个零 $n$ 样本均未发生除法。
- 保存 definition 后重载三处五组 jets，差为零。额外 scalar 调用与向量调用的差为 `6.661338147750939e-16`。
- 输入及所核源 SHA 前后不变；无 BVP/大 Jacobian/body 积分。

实体输出为同 stem 的 `-report.json`、`-definition.json`、`-samples.npz`、`-exit-receipt.json`。报告 SHA256 为 `5b02b4bf912253c02bd50d1fa5ec259aedad29c93c182fd02cfca5c3888c6613`。完整逐件身份见本组 closed manifest。
