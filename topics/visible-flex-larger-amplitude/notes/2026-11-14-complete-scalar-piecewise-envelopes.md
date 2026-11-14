# 2026-11-14：完整固定标量的原公式、断点与同一 a² 的分片包络

目的：给 [R251：直接相对算子度量证书](../results/R251-direct-relative-operator-metric-certificate.md) 的 operator 正性检查提供**同一个完整标量函数**的上下多项式包络。本文只读既有源码及公开 Actions 元数据，给出解析构造和证明；没有重拟合标量、改变设计参数、启动数值计算或重跑旧 A。

## 1. 当前对象与必须保留的调用链

完整 v3 标量由 `LiftedModesPrefixProfile → PrefixControlsProfile → CompleteProfile` 构造，最后由 `FrozenCompleteProfile` 在全部三个真实设计参数 \(p_*\) 上取值。v4 将同一份 v3 spec 原样嵌入 `frozen_design_scalar_profile`；`active_scalar_parameters=0` 不会删除原三个冻结 bump，也不改变标量函数。

本次读取的具体元数据来自公开 run `43588155190`、artifact `14111735884`，出处见 [M112 preflight note](2026-11-14-M112-complete-preflight-and-BC-response.md)：

| 文件 | SHA256 |
|---|---|
| `preparation112/driver-status.json` | `6ddba15ee29868bf8ed26bde840aec7eb9ab210869163092b7733d5257d072c6` |
| `preparation112/prepared.json.gz` | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |

其 source prefix 为实际接受的 M96、端点 \(S=0.99\)，输入 SHA 为 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`。prepared 内 \(p=(0,0,0)\) 只描述准备场，**不能预先代替未来实际 full-DN 接受的 \(p_*\)**。以下分片结构对全部三个冻结参数成立；实际证书必须绑定真实接受输出中的完整 spec/canonical scalar SHA。

三个不同曲率参数不可混淆：

- 新外转弯 `AngleConnector` 的峰值为 \(K=2.5\)；
- 原有限 terminal bridge 的本次构造峰值为 \(K_b=7.5\)；
- 原物理 tail 的背景设计参数仍为 `curvatureBound=8`。

尤其，spec 中保留的原 `complete_original_port.cut._prefix_bridge.curvature` 是 `8.0`，但 `CompleteProfile` 明确先调用

```
tagged_port(port, loop_radius=.35, loop_speed=.985,
            loop_curvature=7.5, terminal_peak_fraction=.1)
```

然后才创建 `NeckTerminalBridge`。直接使用 port 内的旧 tag 建 bridge 会改变本次标量。应按同一源调用链重建，不能靠字段名称猜测。

## 2. 哪些部分本来就是多项式

### 2.1 保存的 .99 前缀

当前 `base_prefix_geometry` 含 **416 个标量节点、415 个区间**，第一节点为 \(s=0\)，最后为 \(s=0.99\)。原 initial law 参数为

\[
v=0.3,\qquad S_0=0.9,\qquad k_0=0.2.
\]

`FixedProfile` 把每个保存的 binary64 节点位置和 jet 当作有理数，先用 `exact_original_jet` 替换第一个节点的三阶 jet，再在每个区间上取唯一五次 Hermite 多项式。若节点间宽度为 \(h\)，左 jet 为 \((a_0,v_0,q_0)\)、右 jet 为 \((a_1,v_1,q_1)\)，在 \(t=(s-s_j)/h\) 中设

\[
\begin{aligned}
c_0&=a_0,&c_1&=hv_0,&c_2&=h^2q_0/2,\\
A&=a_1-c_0-c_1-c_2,&B&=hv_1-c_1-2c_2,&C&=h^2q_1-2c_2.
\end{aligned}
\]

原精确多项式为

\[
P_j(t)=c_0+c_1t+c_2t^2+(10A-4B+C/2)t^3
          +(-15A+7B-C)t^4+(6A-3B+C/2)t^5. \tag{1}
\]

**不能**把当前 \([0,0.9]\) 换回最初的四次 outward law：`FixedProfile.profile` 仅在 \(s\le\text{first knot}\) 时走该旧 law，而当前 first knot 就是零。这个原 law 在当前场主要负责首节点的精确 jet，后续整个 .99 段已经由保存的 415 个区间定义。

一般情况下，若另一个原输入的 first knot 大于零，旧 law 的真实公式为：令 \(u=s/S_0\)、\(b=k_0S_0\)、\(c=3v-2b\)、\(d=b-2v\)，则在 \(0\le s\le S_0\)

\[
a(s)=1+S_0(bu^2/2+cu^3/3+du^4/4),
\]

为四次；在 \(s\ge S_0\) 为仿射。这里只给出正确备用分支，未将它覆盖到当前保存的前缀上。

### 2.2 三个冻结控制

当前支持区间原件为

\[
[0.0495,0.297],\quad[0.3465,0.594],\quad[0.6435,0.891].
\]

它们互不相交且全在 .99 前缀内部。每个控制在 \([\ell,r]\) 内使用

\[
B(s)=w^2\,64x^3(1-x)^3,
\qquad w=r-\ell,\quad x=(s-\ell)/w, \tag{2}
\]

外部为零。多项式系数顺序是

\[
(0,0,0,64,-192,192,-64),
\]

所以 \(B\) 为六次，端点零、一、二阶 jet 为零。完整函数为

\[
a(s;p_*)=a_{\rm base}(s)+\sum_{i=1}^3p_{*,i}B_i(s). \tag{3}
\]

因此在原标量节点与 bump 端点的共同细分上，当前 prefix 的 \(a\) 次数至多为六，\(a^2\) 次数至多为十二；不在 bump 内时分别至多为五和十。参数取值不会增加次数。

`PrefixControlsProfile` 替换了旧三个控制的支撑，但其 `knots` 保留 `CompleteProfile` 原先加入的辅助节点，如旧 prefix bump 的 \(.15S,.70S\)。这些多余节点可继续作为包络分片端点；它们不表示原旧 turn/coast 控制仍在生效。

### 2.3 两种 coast

新 AngleConnector 后的显式 coast 为

\[
a(s)=a_T-v_c(s-T),\qquad v_c=0.985,
\quad C=(a_T-0.35)/v_c. \tag{4}
\]

这是仿射函数，\(a^2\) 为二次。有限 terminal bridge 内的常相位 coast 也为仿射；若精确保留其原有限求积表达，其斜率是原常正弦乘以原权重总和，仍然是仿射，不能在精确位值证明里默默把一个保存权重总和改成一。

## 3. AngleConnector 的精确分片表达

令来自同一 `FixedProfile` 的 incoming jet 为 \((a_0,v_0,q_0)\)，其中 \(q_0<0\)。源码使用

\[
\phi_0=\arcsin(v_0),\quad
\phi_1=-\arcsin(v_c),\quad
\kappa_0=-q_0/\sqrt{1-v_0^2},\quad
e_i=e_o=0.08,
\]

\[
\overline\kappa=K\bigl(1-(e_i+e_o)/2\bigr)+\kappa_0e_i/2,
\qquad L=(\phi_0-\phi_1)/\overline\kappa. \tag{5}
\]

在 \(u=(s-S)/L\in[0,1]\) 上定义 \(I(u)\)：

\[
I(u)=
\begin{cases}
\kappa_0u+(K-\kappa_0)e_i(t^3-t^4/2),
  &0\le u\le e_i,\quad t=u/e_i,\\
I_1+K(u-e_i),&e_i\le u\le1-e_o,\\
I_2+Ke_o(t-t^3+t^4/2),
  &1-e_o\le u\le1,\quad t=(u-1+e_o)/e_o,
\end{cases} \tag{6}
\]

其中 \(I_1=e_i(\kappa_0+K)/2\)、\(I_2=I_1+K(1-e_o-e_i)\)。于是

\[
\phi(u)=\phi_0-LI(u),\qquad\kappa(u)=I'(u). \tag{7}
\]

相位在三个分片上分别是四次、一次、四次多项式；\(\kappa\) 分别是三次、常数、三次。

理论上的相位积分写法是

\[
a_{\rm int}(s)=a_0+L\int_0^u\sin\phi(v)\,dv,
\quad a'_{\rm int}=\sin\phi(u),\quad
a''_{\rm int}=-\kappa(u)\cos\phi(u). \tag{8}
\]

但是当前 `AngleConnector.profile` 对半径使用固定 **48 点 Gauss** 有限和。设其保存节点、归一化权重为 \(\xi_q,\omega_q\)，三个 panel 为

\[
(\ell_j,h_j)=(0,e_i),(e_i,1-e_o),(1-e_o,1),
\quad d_j(u)=\max\{0,\min(u,h_j)-\ell_j\}.
\]

其直接半径表达是

\[
a_{48}(s)=a_0+L\sum_{j=1}^{3}d_j(u)
       \sum_{q=1}^{48}\omega_q
       \sin\phi\bigl(\ell_j+\xi_qd_j(u)\bigr). \tag{9}
\]

数值返回的第二、第三分量仍直接按 (8) 的 \(\sin\phi\)、\(-\kappa\cos\phi\) 计算。固定求积并非一般精确积分，因此不能未经误差说明就说它们是有限和 (9) 的严格一、二阶导数。**R251 的度量值正性只需要 \(a^2\)**，可以直接包络 (9)，完全不需要改变这个半径表达或先解决该求值差。

将有限和理解为固定常量上的实解析表达时，要保留实际构造器得到的 phase 常量、长度、Gauss 节点和权重的 binary 值及其来源；浮点逐次运算误差则另作外包。若所主张的数学标量是 (8) 的积分函数，须包络 (8)，并把 (9) 作为它的有误差读出。两者不能只因 48→80 数值差很小而被直接视为同一精确函数。

## 4. 原 terminal bridge 的表达

本次标量 bridge 的起始半径为 \(r_b=0.35\)，速度参数为 \(v_c=0.985\)，峰值 \(K_b=7.5\)，terminal peak fraction 为 \(f=0.1\)。对同一原 cut 取背景斜率 \(w_c\) 与径向二导 \(w'_c\)。定义

\[
p_t=-\operatorname{atan2}(1,w_c),\quad
p_s=-w'_c/(1+w_c^2)^{3/2},\quad
\gamma=f(\pi/2+p_t),\quad
p_p=p_t-\gamma. \tag{10}
\]

这里真实原件为

\[
w_c=0.08000000000000027,\quad
w'_c=-1.866666666666673,\quad
r_c=0.30000000000000004.
\]

它们是原 port 打印的 binary 值，不能为了方便直接换成名义的 \(.08,-28/15,.3\)。

### 4.1 平顶 turn

令 \(p_i=-\arcsin(v_c)\)、\(e=0.08\)，长度

\[
L_b=|p_p-p_i|/[K_b(1-e)].
\]

flatturn 的归一化 ramp 原函数为

\[
J_e(u)=
\begin{cases}
e(t^3-t^4/2),&u\le e,\quad t=u/e,\\
u-e/2,&e\le u\le1-e,\\
1-e-e(t^3-t^4/2),&u\ge1-e,\quad t=(1-u)/e.
\end{cases}
\]

相位为

\[
p(u)=p_i+(p_p-p_i)J_e(u)/(1-e). \tag{11}
\]

仍是四次、一次、四次三个分片。半径按 `alternative-neck-flatturn.integral` 的原 **64 点 Gauss** panel 有限和计算；理论积分表达与有限和表达的区别同上。

### 4.2 内部 coast 与 brake

brake 长度和相位为

\[
L_q=2\gamma/p_s,\qquad p_q(u)=p_p+\gamma u^2. \tag{12}
\]

因此 brake 相位二次，半径为正弦二次相位的原 64 点有限求积表达。令这个 brake 的原半径增量为

\[
d_q=L_q\,Q_{64}[\sin p_q](1).
\]

turn 结束半径为 \(a_b\)。内部 coast 的目标半径和长度为

\[
r_{\rm coast}=r_c-d_q,\qquad
C_b=(r_{\rm coast}-a_b)/\sin p_p. \tag{13}
\]

它从 turn 末端到达该半径，随后接 brake。`Pieces.append` 对不足 `1e-14` 的段不添加；当前已完成 prepare 记录的是 turn/coast/brake 三段皆存在的结构。一般消费者须保留实际 segment 列表和跳过规则，不能凭预期强加一个零长分段。

`strong_angle_boost` 的 provider hook 只对带 `strong_angle_boost` 标记的 boost 生效；本 terminal bridge 的 turn/coast/brake 没有该标记。这里没有暗中引入另一种 angle-boost 标量。

## 5. 准确的分片断点

以实际原 spec 和其构造器常量为准，取以下并集并排序去重即可：

1. 全部原保存 prefix 标量节点，以及六个实际 bump 端点；若存在 first-knot 之前的旧 law 分支，还须加入它实际跨过的 \(S_0\)。
2. AngleConnector 的 \(S,S+e_iL,S+(1-e_o)L,S+L\)。
3. 外部 coast 终点 \(B=S+L+C\)。
4. bridge 的
   \[
   B,\ B+eL_b,\ B+(1-e)L_b,\ B+L_b,
   \ B+L_b+C_b,\ B+L_b+C_b+L_q.
   \]
5. 实际 `profile.knots` 中保留的其他辅助节点、物理 Hermite 状态节点。加入这些节点只细分检查区间，不改变函数。

有一个当前原件的数值定位表，以下均为**只读既有公开结果**，不是在本地重新求出的数据：

| 量 | prepare112 已记录值 |
|---|---:|
| prefix end \(S\) | `0.99` |
| incoming \(a_0\) | `1.1666064106120295` |
| incoming \(v_0\) | `0.3579486389103069` |
| incoming \(q_0\) | `-2.0101206107275877` |
| incoming \(\kappa_0\) | `2.15275972133223` |
| AngleConnector length \(L\) | `0.7390454578568767` |
| turn end \(S+L\) | `1.7290454578568766` |
| outside coast length \(C\) | `0.49174749564739106` |
| bridge start \(B\) | `2.220792953504268` |
| whole bridge length | `0.05021108193401754` |
| complete physical end | `2.271004035438285` |

同一 spec 的最后一个保存 prefix 节点写的是 `ap=0.357948638910307`，而 `FixedProfile` 的实际 rounded 系数求值生成的 incoming 是表中的 `0.3579486389103069`。这是一项可见的 1 ulp 求值差，不能把节点原数与后继构造的 incoming 常量不加说明地互换。它不影响“同一原表达式可严格包络”的办法，但说明证书必须声明自己的精确对象和求值误差，不能把打印的接口残差直接当成有理恒等零。

## 6. 多项式段的严格包络

对 (1) 和 (2)，按所绑定的原规范形用有理数直接构造，不需要近似。它们相加后平方，就得到真实 \(a^2\) 的次数至多十二的多项式。任一细分区间上可用精确 de Casteljau/Bernstein 变换求上下凸包，或直接把该精确多项式交给 R251；不必先退化成三个分量误差界。

`FixedProfile` 的 evaluator 把 (1) 的精确系数 \(c_j\) 舍入为 binary 系数 \(\widehat c_j\)。若需要同时外包这层表示差，在单位区间上严格有

\[
|P(t)-\widehat P(t)|\le\sum_{j=0}^5|c_j-\widehat c_j|. \tag{14}
\]

所需更高导数亦有

\[
|\partial_s^i(P-\widehat P)|
\le h^{-i}\sum_{j=i}^5\frac{j!}{(j-i)!}|c_j-\widehat c_j|.
\]

这里只要 \(i=0\) 就足以给 \(a^2\) 的 R251 门。原 bump 的实际 `width=right-left`、系数矩阵乘法及 Horner 求值也可按同一原运算顺序作向外舍入区间计算；不能为了认证方便重新取另一个 width 或回填相同显示小数。

## 7. 非多项式段的同一表达式包络

下面给出一个无需新的拟合、且误差可以指定的构造。先按第 5 节切开所有 phase/clipping 的分支。在每个这样的区间内，(9) 的每个 \(d_j\) 都是零、常数或仿射，正弦里的相位是次数 \(d\le4\) 的多项式（brake 为 \(d\le2\)）。原参数若是 binary 数，可以精确作为有理常量；需要保留的非有理源常量则用有证明的有理区间，不用新自由参数代替。

### 7.1 直接 Taylor 多项式与统一余项

设经原 phase 多项式的 Bernstein 包络得到 \(|\phi|\le B\)。令

\[
S_n(x)=\sum_{k=0}^n\frac{(-1)^kx^{2k+1}}{(2k+1)!}.
\]

对所有实数 \(|x|\le B\)，Taylor 定理给出

\[
|\sin x-S_n(x)|\le R_n(B):=B^{2n+3}/(2n+3)!. \tag{15}
\]

证明是把 \(S_n\) 看成到 \(2n+2\) 次的 Taylor 多项式；偶数次系数恰为零，下一阶导数的模长至多一。因此本界不需要“交错项已经递减”的额外前提。

在原有限和里逐项把 \(\sin\phi\) 暂换为 \(S_n(\phi)\)，得到一个仅用于**包络**的多项式 \(P(s)\)。在当前 partial panel 上其次数至多为

\[
d(2n+1)+1.
\]

旧的完整 panel 只贡献常数。若在该检查区间 \(0\le d_j(u)\le D_j\)，则半径误差严格满足

\[
|a_Q(s)-P(s)|
\le L\sum_jD_j\sum_q|\omega_q|\,R_n(B_j). \tag{16}
\]

所有权重仍是原有限和的权重，不使用它们“恰好和为一”这一未经检查的浮点断言。相位或权重常量本身有区间宽度时，以区间代入同一多项式并将其宽度加入右端。式 (15) 的 factorial 使余项随 \(n\) 任意减小，因而对**指定的同一实表达式**能获得任意给定的正包络宽度；并未把它替换为多项式 metric。

### 7.2 低阶局部展开与细分

若不希望提高到较高次数，可在每个角度表达的有理中心 \(c\) 展开。写 \(\phi=c+z\)，并用有理区间核定 \(\sin c,\cos c\)。其 \(m\) 次 Taylor 多项式的余项不超过

\[
|z|^{m+1}/(m+1)!.
\]

各 Taylor 系数的核定误差另加 \(\sum_{k=0}^m\delta_k|z|^k/k!\)。固定一阶或更高阶后，把径向检查区间二等分；phase 多项式连续且有界导数，所以该区间的 \(|z|\) 可以趋于零，常量核定精度也可独立提高。有限条原 panel 的历史常数项只需核定一次。这样同样能实现给定误差，且不更改原标量、原断点或原求积规则。

如果只需一个最简单的常数区间包络，也可以直接对有限和的正弦函数作向外舍入区间求值并细分。为证明其收敛性，在一个活动 partial panel 内，设 \(q_q=\ell+\xi_qd\)，则有限和半径的**真实导数**为

\[
\frac{da_Q}{ds}=
\sum_q\omega_q\bigl[\sin\phi(q_q)
  +d\xi_q\phi'(q_q)\cos\phi(q_q)\bigr]. \tag{17}
\]

由相位多项式的导数 Bernstein 界可得它的有限 Lipschitz 常数。不能在这一步直接拿源码另行返回的 `ap=sin phase` 当作 (9) 的严格导数；(17) 避开了该问题。

### 7.3 原解析积分的对照误差，不能替换本次有限和

本次有限 Gauss 表达应直接使用 (16)；本小节不授权把目标换成 (8)。仅为解释与已有解析积分对象的关系：对 (8) 可在每个原 panel 上直接积分 \(S_n(\phi(v))\)。被积函数是多项式，积分可精确完成；其半径误差为

\[
L\sum_jD_j R_n(B_j).
\]

这仍是对**同一个积分公式**的包络，而不是重新设计半径。此时数值代码的 48/64 点读出与这个目标之间的求积及浮点差须显式保留。

也可说明理想精确 Gauss 规则的积分误差：48 点 Gauss 对次数至多 95 的多项式精确，所以 quartic phase 时取 \(n=11\) 可使 \(\deg S_n(\phi)\le92\)；积分与正权重求积各自对余项的作用至多为 panel 长度乘 \(R_n\)，故差至多为两倍此量。64 点时可取 \(n=15\)，次数至多 124，低于其 127 次精确门。该论证本身不证明 binary Legendre 节点/权重等于理想节点/权重；若用这条路线，节点和权重扰动须另作区间包络，例如对 Legendre 多项式作有理根隔离，再使用原权重公式。**直接包络实际有限和 (16) 不需要引入这项额外工作。**

## 8. 从 a 的包络转成 a² 的包络

若已得

\[
|a(s)-P(s)|\le\varepsilon,
\qquad |P(s)|\le A
\]

其中 \(A\) 可由 \(P\) 的精确 Bernstein 凸包得到，则

\[
\boxed{\quad
P(s)^2-(2A\varepsilon+\varepsilon^2)
\ \le a(s)^2\ \le
P(s)^2+(2A\varepsilon+\varepsilon^2).
\quad} \tag{18}
\]

证明为 \(a^2-P^2=2P(a-P)+(a-P)^2\) 和三角不等式。这是一对真实的多项式上下界。若另有 \(P-\varepsilon\ge0\)，还可以直接使用更贴近函数的

\[
(P-\varepsilon)^2\le a^2\le(P+\varepsilon)^2. \tag{19}
\]

给定所需绝对平方误差 \(\delta>0\)，例如选

\[
\varepsilon\le\min\{1,\delta/(2A+1)\}
\]

便使 (18) 的误差半宽不超过 \(\delta\)。若下包络暂为负，仍是合法下界，只是未必足以让正性检查通过；继续细分或提高同一表达式的核定精度即可。在原 \(a\) 有正下界的紧区间上，这个障碍会随误差缩小消失。

R251 在 \((s,\phi)\) 坐标中使用 \(g=\operatorname{diag}(1,a^2\rho^2)\)。把 (18) 或 (19) 原样代入其单调上下界即可；不必把 metric 换成 \(P^2\)，也不必先以三个分量界损失一个因子二。

## 9. 原数值求值与数学标量之间的边界

本办法不把原报告中约 \(10^{-15}\) 的 join 误差写成精确 C² 恒等式，也不把某个 rounded evaluator 的 jet 自动认作另一种解析半径的导数。两种问题要分开：

- R251 的值证书只需真实点值 \(a(s)^2\) 的包络，以上可直接覆盖同一完整半径表达；
- 关于连续 metric、标量接口的精确正则性、或者原 Frenet 返回 `a,ap,app` 是否为同一精确函数的完整 jet，需要按照已有的数学标量定义与数值求值误差分别说明。该说明不允许未经证明更换 \(g\)，也不构成额外的人为机器精度完成门。

对 `Pieces.profile` 的端点容差 `s0-1e-13`、`s1+1e-12` 以及 `clip`，若核定的是可执行数值求值，应在这些小带中同时外包所有可能选中的原分支，并包含其原浮点运算误差。若核定的是原分片解析定义，则按准确分片端点取式 (11)—(13)，另外记数值 branch/clipping 的偏差。两者都无需重新拟合或替换半径。

后续公开 Actions 的最小证据包可以只保存：真实 scalar spec/canonical SHA、原重建器 SHA、从同一对象导出的原常量与求积数组、原分片标识、每片 \(P\) 与 \(\varepsilon\)、由 (18)/(19) 得到的上下多项式、以及原函数身份不变的声明。这里只说明证明办法，没有创建新的数值结果。

## 10. 本次核对的原源

| 源文件 | SHA256 |
|---|---|
| [FixedProfile](../computations/geometry_20261114_r225_fixed_profile.py) | `478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c` |
| [完整 scalar](../computations/geometry_20261114_full_scalar_profile.py) | `8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b` |
| [三个 prefix 控制](../computations/geometry_20261114_prefix_controls_profile.py) | `f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24` |
| [v3 独立维数 scalar](../computations/geometry_20261114_lifted_modes_profile.py) | `13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5` |
| [v4 同一 scalar 冻结](../computations/geometry_20261114_same_metric_profile.py) | `651fd91fcf8d34be6cf2054f79728b417149ae4a07e0830915821f32ccf9cd89` |
| [AngleConnector](../computations/strong_20261114_scaled_core_tail_connector.py) | `661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08` |
| [NeckTerminalBridge](../computations/alternative-neck-provider.py) | `84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2` |
| [flatturn phase/求积](../computations/alternative-neck-flatturn.py) | `c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd` |
| [原 64 点规则/brake phase](../computations/alternative-neck-excursion.py) | `f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c` |

可选 `strong_angle_boost.py` 的核对 SHA 为 `ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be`；它未改变上述 terminal bridge 三段。
