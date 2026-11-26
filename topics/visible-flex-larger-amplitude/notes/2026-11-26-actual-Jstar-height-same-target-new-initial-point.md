# 实际 Jstar 高度字作为同一 g 的完整新初点

日期：2026-11-26。会话：Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：给出完整同目标初点选择与已刊入口的可执行参数；新初根、场、QP 和几何尚未返回。** 本文没有更改 R690 尾、原标量目标、原参考、十八字 Q、原自由量或原完成标准。实际原高度下的全弦长和支撑外必要条件都已经通过；本次不是修复这些不存在的已证障碍，而是改变有限端点控制族面对的竖直目标。

## 1. 采用的真实字与不可混用的积分含义

run45820592817/1 的实际 stage21 完整 R696 报告已经返回如下字：

| 量 | 原报告中的 binary64 hex |
| --- | --- |
| 原 4e reference 的 H | 0x1.f27228dabd944p+0 |
| R696 的 working Istar | 0x1.f27228dabd93ep+0 |
| R696 的 working Jstar | 0x1.ec0bc59b655d2p+0 |

实际来源为 [21/22/25 的完整归因](2026-11-26-actual-R696-angular-unit-direction-21-22-25.md) 与 [公开 part005](2026-11-26-public-actions-45820592817-1-part-005.md)。runner 路径 angular-unit-complete-first/report.json，21086484 B，SHA256 为 399ae8196032bb96a5a3f5f90c565582f8bd222fe838301fee6f8139f379dde9；本次不转存该 raw。该次 source commit 是 4aaa7c1bd5d1f0538aa2a09b6265523354a82f2d，driver 为 7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d，operator 为 d2f8a93c3356fc172e5c6ac365b0bff65660fea2bb3bf8350ab124537a0f4a14。

固定输入仍是 reference0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1 与 profile6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb。实际 Jstar 字来自 latest_operator_metadata.working_definition.Jstar_hex。

R696 的准确高度基底定义见 [R696](../results/R696-angular-unit-tangents-and-exact-closed-sections.md)。令

$$
I_*=\int_0^S c(s)\,ds,\qquad
J_*=\int_0^S c(s)w(s)\,ds,
$$

其中 $\varepsilon=1/20$，$w(s)=S_5(s/\varepsilon)$ 于 $[0,\varepsilon]$，之后为1。这里 $c$ 是准确旋转参考的竖直单位切向分量。

原 4e H 使用其归一化 c 与原完整求和；d2f8 的 working Istar/Jstar 使用原 raw c 与累计积分。两者工作形成路径不同，积分和舍入费用都没有包围。不能把 d93e 换成 d944 称为消除了准确端点残差，也不能把 working Jstar 宣称为准确 $J_*$。

本次明确选择**原报告已经打印的一个有限字**

~~~text
--initial-height 0x1.ec0bc59b655d2p+0
~~~

作为原自由坐标 H 的新初值；其数值本身是精确定义的 binary64 常量，不要求它等于准确积分。这里没有本地积分、浮点转换或新科学读数。

这与修改 Istar 的几个末位有明确区别。由上述字的十六进制展开直接可见，原 H 与 working Istar 相差 $6\cdot2^{-52}$；而新旧 H 字满足

$$
\frac5{256}<H_{\rm old}-H_{\rm new}<\frac7{256}.
$$

证明只需原 H 位于 $[1+242/256,1+243/256)$，新字位于 $[1+236/256,1+237/256)$。这些是字面有理界，不是本地数值实验。新字也严格大于 $1.01$，但这仅核一个输入标量，不能代替完整幅度或几何读取。

## 2. 零旋转初点的准确端点失配

固定同一材料图 $\theta_0(\phi)$，令 $e_r=e_r(\theta_0)$、$e_z=(0,0,1)$。准确轴对称参考是

$$
T_0(s,\phi)=a'(s)e_r+c(s)e_z,\qquad a(0)=1,\quad a(S)=R.
$$

当前完整 core 曲线记为 $\Gamma_c(\phi)$，帽锚点为 $P_H=R e_r+H e_z$。在全部原 omega 系数为零且端点控制也为零时，

$$
\begin{aligned}
C_0(H,\phi)
&=\Gamma_c-P_H+\int_0^S T_0\,ds\\
&=\Gamma_c-e_r+(I_*-H)e_z.
\end{aligned}
\tag{1}
$$

帽半径 R 严格抵消。这是完整准确定义的恒等式；实际载体没有因为写出此式就得到误差认证。

因此，若理想地取 $H=I_*$，只消掉竖直项。原 core 的水平向量

$$
d(\phi)=\Gamma_c(\phi)-e_r(\theta_0(\phi))
\tag{2}
$$

仍然存在。原固定前三 core 系数没有被清零；全材料曲线若处处满足 $\Gamma_c=e_r(\theta_0)$，它就是真圆，正性下其支撑函数恒为1，所有非恒定 Fourier 系数都为零。这与保留该非圆 core 的输入不同。因此改 H 不会把这个非轴对称初点变成零控制的完整解。

理想地取 $H=J_*$ 时，

$$
C_0(J_*,\phi)=d(\phi)+\delta e_z,\qquad
\delta=I_*-J_*=\int_0^\varepsilon c(s)(1-w(s))\,ds.
\tag{3}
$$

由 $0\le c\le1$、原 core 附近 $c>0$，以及 $0<w<1$ 于内部，得到

$$
0<\delta<\varepsilon=\frac1{20}.
\tag{4}
$$

这给出了一个竖直压低的方向尺度：同一单位长度 meridian 可以尝试把一部分原竖直增量用于水平转向。本次实际字选择是这一几何动机的可复现数值实现；它不证明有限双 bubble 控制必可达，也不证明相同根球里的 Newton 必成功。

对任意原完整 omega、core 和固定控制 z，旧 [H-only 完整接口](2026-11-26-explicit-initial-height-fixed-moment-zero-entry.md) 已证明

$$
C(H_2,c,\omega,z;\phi)-C(H_1,c,\omega,z;\phi)
=-(H_2-H_1)e_z.
\tag{5}
$$

本次引用该已登记恒等式，不重做其隐式 J/J*。尤其不增加角度相关 H；所有角度共用原来的单个 H 自由量，后续仍可优化它。

## 3. 原 core 的 metric 缺陷仍须真正求解

对原直接轴对称 hDelta 场，在零 omega 下写 $h(s)=1-S_5(s/S)$、$\Delta=d+(I_*-H)e_z$。于是

$$
F_s=T_0+h'\Delta,\qquad
E-1=2h'\{a'e_r\cdot d+c(I_*-H)\}
+(h')^2\{|d|^2+(I_*-H)^2\}.
\tag{6}
$$

H 只改变这里的竖直项；$d$ 及其角导数仍在全部场、交叉项与曲率里。不能从高度变化的一阶趋势推导整面最大误差下降。

对 R696 的**零 omega、零新增径向 profile** 初点，记它的完整中心化截面为 $C(s,\phi)$。$C$ 一般非圆且 $C_s$ 一般非零。准确公式是

$$
F=aC+\left\{I+\frac J{J_*}(H-I_*)\right\}e_z,
$$

$$
F_s=a'C+aC_s+
c\left\{1+\frac{H-I_*}{J_*}w\right\}e_z,
\qquad F_\phi=a\rho_0 e_\theta(\beta).
\tag{7}
$$

所以此初点的交叉 Gram 残差

$$
\frac{F_s\cdot F_\phi}{a\rho_0}
=(a'C+aC_s)\cdot e_\theta(\beta)
\tag{8}
$$

不随 H 改变。径向残差则为

$$
|a'C+aC_s|^2+
c^2\left\{1+\frac{H-I_*}{J_*}w\right\}^2-1.
\tag{9}
$$

它仍保有完整的角向变化；一个全局 H 不能被当作逐角消残差的变量。式 (8) 的 H 独立性仅针对这里明确的零 omega 水平切向初点，不扩张到任意已扭转的 R696 场。

R696 已证明当 H 大于 $\varepsilon$ 时该零旋转 seed 的竖直导数保持正；本次 H 字满足这个标量范围。但所选新试验使用的是原 44ac 零端点表示，绝不能把 R696 seed 的嵌入性结论转给解出的新 44ac 场。

## 4. 原点验证不会要求失败的旧根先成功

本次完整源码全部已刊：

| 角色 | SHA256 |
| --- | --- |
| launch_zero_moment_height_so3_actions.py | c1d3e0e5da47d3edef42124a8020cba705e99ac4b522c758ee195e8d575a58bd |
| fullclosed_zero_moment_height_so3_qp.py | 34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3 |
| read_zero_moment_height_so3_report.py | 2e5b340d622993af55060f22d1dc26bd1cc451218feb27f8b8ce7b1366de1fe9 |

逐段源码读取确认以下真实顺序：

1. 核实际 4e reference、7f base、scalar/context、原初点和完整固定十八字 Q 的来源与字节。
2. 构造 44ac 算子；此时根缓存为空，构造器没有调用初场、端点求根或 root jets。原坐标范数的建立也不要求端点根。
3. 读取 q.initial() 的原完整数组副本；explicit_height_seed 再核原点 cd530 身份和完整 model/Q，只把末槽 H 设为所选字。
4. 对所有非 H 槽逐 byte 比较，保存原/新整点摘要、前缀摘要、H hex/准确分数以及 model 未变标志。
5. 完整收集历史位置、建立 geometry 和报告后，才开始这个**新初点**的首次 F/root/Gram/几何读取。

所以“先验证原点”是来源、字节和完整结构的验证，不是先要求已失败的原根成功。没有绕过或删掉守卫。若新 H 根仍失败，报告在首次场失败路径保留该真实新点，pure reader 以实存 reference 为 parent，不要求一个尚不存在的 final.npz。

## 5. 完整 Actions 试验与保留责任

完整两步参数见 [Jstar 同 g 初点请求](../computations/resume-20261126-zero-frozen-Q-Jstar-height-first-ready.json)。同实际 stage19 的所有科学预算保留：wide 两支撑、半径 .75、根容差2e-12、24轮、18次回溯、Armijo1e-4，原全变量/全部正权 Gram、jet-sum H2、原192工作集选择、完整幅度和 Phase I，最多1个16步 metric 方向及4个64步恢复方向。没有为了新 H 提高球或放宽残差/几何。

输入 Q 用已刊 df11 完整小参数文件并严格核原05dc定义，不重算新矩。固定 g、reference、chart、模型和所有原自由量保持不变；只有完整 driver/source 的入口身份与实际初点摘要如实区分。未来新点和候选 SHA 尚未预填。

七份完整位置来源为 preparation locations、原 hDelta 首报告、实际 prior-SOC 报告、R696 报告、首 integral 报告、原端点延拓失败报告、以及已经排在前面的 integral-second 报告。最后一项须随前序实际返回消费，不把它的场值当作初值。所有位置在新场真读，新极值继续永久保存。不得因为起点、source 或 schema 改名而丢掉同 g 的历史责任。

只有 rows-* 缓存作为明确清理对象；不请求旧控制器列举删除整个参考缓存。raw 仍留 runner。pure reader 只读真实完整 report 与来源，所有摘要选取都是标量。

这一原05dc入口严格绑定03b的实际参考。如果03b结束，不能将这个旧参考合同贴到05重建输入上；后者必须使用已经明确区分的新参考绑定，并另行声明当前 H 初点。无论在哪个 runner，都要读出自身初场、完整原 C、幅度、永久点和真实接受结果，再继续同 g 求解。此次没有预言成功，也没有以一个 H 试验替代课题 README 的任何完成条件。
