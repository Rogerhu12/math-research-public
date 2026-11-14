# R153/R155 复合字段的实际 native jets 与准确 cut 作用域

## 1. 精确的组合顺序与保存定义

本 reader 的输入首先是原样保存的 mesh、P1 Fourier correction、物理 bump 参数、完整 seed/tail/frozen-coast lifting 及 R149 atlas。它复用已有读取链，不把样本或另一份投影当作保存字段。

字段先应用 `gauss_l_definition` 声明的 R153 coast 正 n 窗，然后才应用 `positive_trace_definition` 声明的 R155 末段正 trace 窗。两个实际支撑不相交。相同保存参数下的物理目标度量保持
$$g_p=ds^2+a_p(s)^2du^2,$$
本次改变的是形式 II 场；不同物理 bump 参数的候选仍是不同的 $g_p$。

`representation_kind` 必须为
`ruling_atlas_coast_Gauss_l_and_terminal_positive_trace_v1`，末窗 schema 必须为
`fd2d-terminal-positive-trace-Gauss-field-v1`。reader 核对原 coast 和新末窗各自的 provider/algebra SHA、准确窗口公式、固定参数布局、原始 atlas/reference 身份与实际 P1 节点。

末窗为
$$
w(s)=S_5\!\left(\frac{s-s_a}{s_b-s_a}\right),\quad
s_a=S-0.02,\quad s_b=s_{\rm last}+L_{\rm last}/2,
$$
其中 $S_5$ 的参数截断于 $[0,1]$。实际保存的二进制端点为
`start=1.4689731783581288`、`ramp_stop=1.4759731783581287`、
`cut=1.4889731783581288`。v2 直接消费这些值，并核对冻结 provider 使用的同一运算；不另用浮点代数上等价的式子重建端点。权重值直接调用冻结 provider 的稳定 `terminal_window`：令 $z=\min(t,1-t)$，先算 $q=z^3(10-15z+6z^2)$，再按 $t\le1/2$ 取 $q$ 或 $1-q$。它仍是同一 S5，而不在接近 1 时发生直接多项式的浮点越界。

所以在 $s\le s_a$ 准确为零，在 $s\ge s_b$ 到 cut 准确为一。这一整个非零窗口位于固定 protected 末 profile 上，所有物理 bump 都在它之前结束。其支撑也严格位于 R153 coast 窗之后。

末 plateau 的表示冗余由保存的 `inactive_raw_trace_nodes` 明示。只有整片 P1 帽函数支撑位于 $w=1$ 时，原 common trace 才完全消失；其 $n,l$ correction 可按保存定义取相反数来保留同一 $d=n-l$。reader 核对节点支撑，不把仅单个节点在 plateau 当作删除相邻 rim 自由度的依据。

## 2. 字段与完整内部空间导数

以下 $(n,m,l)$ 指已经完成 R153 的实际 background，$x=s$ 是固定计算角 $\xi$ 的物理径向坐标。定义
$$
d=n-l,\qquad T=n+l,\qquad
h=\sqrt{d^2+4m^2+4K},\qquad K=-a''/a,
$$
$$
E=\frac w2(h-T),\qquad n_*=n+E,\quad m_*=m,\quad l_*=l+E.
$$
在 $w=0$ 时不计算平方根。一般活跃内部点按真实定义要求 $K\ge0,h>0$，不附加人为的 $n$ 或 $h$ floor。代码复用冻结的 `fd2d_gc_positive_trace_branch.py::positive_trace_delta` 求值与一阶角 jet，因此所有字段与数值端是同一数学定义。

由于 $K_\xi=0$，
$$
h_\xi=\frac{d d_\xi+4m m_\xi}{h},
$$
$$
h_{\xi\xi}=\frac{d_\xi^2+d d_{\xi\xi}
 +4(m_\xi^2+m m_{\xi\xi})-h_\xi^2}{h}.
$$
因此实际角 jets 为
$$E_\xi=\frac w2(h_\xi-T_\xi),\qquad
E_{\xi\xi}=\frac w2(h_{\xi\xi}-T_{\xi\xi}).$$
它们只需要实际 $K$ 及 background 的角一、二导，不需要 $K_s$。

若调用方还需要内部径向及混合 jets，则使用真实
$$K_s=-a'''/a+a''a'/a^2$$
以及
$$
h_x=\frac{d d_x+4m m_x+2K_s}{h},
$$
$$
h_{x\xi}=\frac{d_xd_\xi+d d_{x\xi}
 +4(m_xm_\xi+m m_{x\xi})-h_xh_\xi}{h}.
$$
完整窗乘积项是
$$
E_x=\frac12\{w(h_x-T_x)+w_s(h-T)\},
$$
$$
E_{x\xi}=\frac12\{w(h_{x\xi}-T_{x\xi})+w_s(h_\xi-T_\xi)\}.
$$
这四种增量都同时加到 $n$ 和 $l$ 对应的导数上，$m$ 的五组 jets 完整保持。原 $d=n-l$ 的五组 jets 因而在准确算术中不变。

在固定计算角下，background 的 $n_x,m_x,l_x$ 已包含真实 $U_s$ 漂移；$K_x=K_s$ 仍成立，因为目标沿角恒定。所需 $a'''$ 使用已经冻结的 `physical_profile_third`，对实际 phase 片求
$$a'''=\cos(p)p_{ss}-\sin(p)(p_s)^2$$
并加入真实 bump 三导。这里是所请求内部 jet 的计算，不是新增全局 C³ 曲面条件。

实际 Gauss 必须按 R155 的完整恒等式检查：
$$
G_*=(1-w)G_0-\frac{w(1-w)}4(h-T)^2.
$$
不能在这个新 rim 直接使用 R153 的单纯 $(1-w)G_0$ 缩放。

## 3. 正确的物理角接口

固定材料角是 $u=U(s,\xi)$，令 $b=U_\xi>0$。同一实际字段满足
$$
f_u=f_\xi/b,\qquad
f_{uu}=\frac{f_{\xi\xi}-(f_\xi/b)U_{\xi\xi}}{b^2},\qquad
f_s=f_x-(U_s/b)f_\xi.
$$
这些链式关系不改变目标度量，也不省略 atlas 的漂移。内部的 `physical` 保留完整 $s,u,uu$ 结果；`physical_angular` 专门提供只需值和材料角两 jet 的消费路径，不查询不必要的 $K_s$ 或 cut 径向 II 导数。

```python
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField

r = PositiveTraceNativeField(
    field_npz, candidate_json,
    reference_inlet=inlet_npz, reference_cache=cache_npz)

interior = r.evaluate_native(s, xi, side='right')
angular = r.evaluate_angular_native(s, xi, side='right')
material_angular = r.physical_angular(s, material_u, side='right')
definition = r.definition()
restored = PositiveTraceNativeField.from_definition(definition_json)
```

`evaluate_native` 在内部返回值、`_x`、`_xi`、`_xixi`、`_x_xi`。侧限参数共同选择实际 P1 slope 和 atlas 径向侧。`evaluate_angular_native` 不携带已改变字段的 `n_x/l_x/n_x_xi/l_x_xi`，以免调用者误用 background 的陈旧径向数据。

## 4. 准确 cut 的角恒等式不等于径向零

reader 核对 cut 的 correction 全为准确零、tail controls 非负、目标 $K=0$，然后在 $s=S$ 直接沿用完整准确 tail。该尾在既定法向下为
$$
(n,m,l)=\kappa(u)(\cos^2u,-\sin u\cos u,\sin^2u),\qquad\kappa\ge0.
$$
故 $h=n+l=\kappa$，整个角函数上准确有
$$E(S,u)=E_u(S,u)=E_{uu}(S,u)=0,$$
包括 $\kappa=0$ 的开放平直弧和 $n=0$ 的其它角。代码在这些点不通过一般平方根导数去除以 $h=0$；它求的是已经绑定的尾族之准确角迹。

受约束的尾参数方向也有 $DE=0$，但这不意味着 $E_s(S^-,u)=0$。固定某个 $\kappa(u)>0$ 的角，若内部径向导数存在且 $K_s\to0$，仍可能有
$$
E_s(S^-,u)=\frac{d d_s+4m m_s-h T_s}{2h}\ne0.
$$
在 $\kappa=0$ 处，一般三变量平方根不在原点可微，径向极限还依赖真实趋近方式。单纯把 exact-tail mask 的参数偏导零复制到空间径向导数，是不同的问题，不能这样处理。

因此本 reader 对准确 cut 的值与角两 jet 完全可调用，但 `evaluate_native` 的完整径向请求在那里明确拒绝，并指向 `evaluate_angular_native` 或 `physical_angular`。它没有填零，也没有把未付径向正则当作原题不存在。接口的这一范围不增加 C³ 完成门。

准确边界函数的两阶角导数已定义，也不自动证明任意保存 P1 字段的内部角二阶导数都向该值连续收敛。当前定义中 `interior_to_cut_angular_second_trace_continuity_certified` 保持 false；R156 的具体参考或后续实际候选需按其真实表示支付所需接合。这里不凭端点赋值宣布闭曲面完成。

## 5. Body 使用原有公式，不索取无用 cut 径向 jet

`body_rhs` 与 `body_jets` 只是一层薄适配，直接调用原先冻结的
`body_rhs_from_fields` 和 `actual_body_twojet`。24 列固定材料变分系统需要
$$l_*,m_*,(l_*)_u,(m_*)_u,(l_*)_{uu},(m_*)_{uu},$$
不需要 cut 的 $l_s$ 或 $n_s$。新方法从 `physical_angular` 取得这些真实字段，然后调用同一原公式。没有重新实现 body 方程，也没有在本组运行积分。

最终实际位置图、Cartesian 两 jet、seam、metric、reach 和强比例仍应消费同一实体并支付原完成条件。一个可调用 reader 或一次小差分检查不代替这些条件。

## 6. 实际检查记录

正式只读小检查源是 `scripts/fd2d-metric-positive-trace-native-check-v2.py`。它只对新保存实体的 terminal rim/plateau 两个实际内部点与八角、一个 coast 点、窗间点和准确 cut 求值。检查内部五组 jets、固定材料链式、完整 Gauss 窗恒等式、$d,m$ 不变量、真实非零 $K_s$ 项和定义重载；cut 检查只覆盖已声明角迹，另核完整径向请求不会被静默填零。

唯一正式检查输入是 `notes/2026-11-12-fd2d-positive-trace-warm04-warm.npz`，58791 B，SHA256
`a0ebb07b210d373b5a9aced7b79137f28fc5f7ffa6a797ea960113f9ee3980ac`。
这是数值端明确保存的新转换初场，不能冒称它已经改善原残差或完成几何。reader 绑定的 provider SHA256 为
`582e85efb95f3f735b6fd19e47a94182462368c1f16aeb75399fa81729cc6e61`。

正式可用 reader `scripts/fd2d_gc_positive_trace_native_field_v2.py` 为 17344 B，SHA256
`59a7cab1702d20aa27ea299e225b5f3ba5aa1e800d349c09cc70ded5c6b7179d`。
检查源为 10785 B，SHA256
`4d996b554f579c69d6c9317a08abd228f73ed3b28ff507092fc19b7b4eb613b6`。

实际命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fd2d-metric-positive-trace-native-check-v2.py \
  --field notes/2026-11-12-fd2d-positive-trace-warm04-warm.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --inlet notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz \
  --cache notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz \
  --out-prefix notes/2026-11-12-fd2d-metric-positive-trace-native-check-02
```

执行 session **20405**，初始 chunk **621010**，完成 chunk **bd0335**，真实 exit **0**。内部耗时 **8.740315860 s**，RSS 峰 **76636 KiB**。该源拒绝覆盖旧输出，复现应使用另一个新前缀。

有限核验结果：

- 与冻结 helper 的实际值和一阶角导差为零；$m$ 的五组 jets 完整不变。
- $d=n-l$ 五组 jets 的浮点差最大 `1.8189894035458565e-12`，angular-only 与完整接口的值/角两 jet 差为零。
- 完整 Gauss 窗恒等式误差最大 `3.552713678800501e-15`。
- 两个实际内部点的 $x,\xi,\xi\xi,x\xi$ 差分核验，细步最大归一差 `9.988650570723069e-8`。
- 实际 $K_s$ 对增量径向导数的最大贡献 `45.26722985037908`，没有静默删除。rim 点 $K_s\approx-20.44587606$，plateau 点约 $-31.61338091$。
- 原 coast 和两个窗之间的实际五组 jets 与 R153 background 差为零。
- 准确 cut 的值、角两 jet 与原完整 tail 差为零；八角中五个是完整零 II 矩阵，仍可准确求值。完整径向请求明确不赋值。
- 定义保存、重载后的内部五组 jets 差为零；输入及冻结源前后不变。

这个初场的 rim 仍可很坏：本次 rim 点 $s=1.4724731783581286$ 的有限最大 $|G|$ 约为 `13.4547072344`，其中 $l$ 可为负。plateau 点 $s=1.4840981783581289$ 的有限最大 $|G|$ 约为 `8.7430063189e-16`。这正符合 R155 的混合恒等式，不意味着完整有限解或连续几何通过。

真实报告 `2026-11-12-fd2d-metric-positive-trace-native-check-02-report.json` 为 9798 B，SHA256
`e099b7636d8470001c5abde83f26108c15b8b964430c9cee2d7e717cc4ebe614`。同 stem 的 definition、samples 和 exit receipt 完整保存。

## 7. 首次身份拒绝的完整保留

此前首版 reader/checker 使用旧接口说明中的浮点 `S-.013` 计算 ramp stop。实际冻结 provider 已改用末片共享中点 `s0+.5*L`；两种浮点运算相差一个 ulp。首版在 metadata 校验处正确拒绝，尚未询问任何字段。执行 session **65794**，初始 chunk **261d11**，完成 chunk **1d6ba9**，真实 exit **1**，异常为
`ValueError: Changed terminal field definition: ramp_stop`。

这是输入身份实现差异，不是平方根公式、几何或不可解的证据。原 `fd2d_gc_positive_trace_native_field.py`、原 `fd2d-metric-positive-trace-native-check.py` 及 `...native-check-01-exit-receipt.json` 均原样保留；v2 使用另名源，不覆盖或洗掉该失败。v2 还直接复用冻结 provider 的稳定 S5 求值。

完整闭组 manifest 同时登记两份失败源/receipt 和正式 v2 源/实际结果。原 numerical provider、R155 helper、旧 reader 和公共索引均未改动。
