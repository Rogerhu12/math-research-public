# R146：已知 lifting 导数的准确端点消元与 quintic 窗求积

**状态：已证明。** 本结论给出同一准确 Gauss–Codazzi 方程的一种有限积分表示；不改变物理度量或实际保存的 P1 场，不把旧离散的结果改记为新离散的结果。实现只对剩余完整 PDE 右端作求积，并保留所有角补余及目标参数变化。

## 1. 已定位的实际误差

这项计算只用真实保存的 122 个径向节点、R139 入口标量与 R144 的明确权重；不求值未知场，不求 BVP，也不据此判定候选几何失败。

输入为 `2026-11-12-fd2d-raw-bump-coast09-b0001-initial.npz`，SHA256
`897ecba1f6eaf69252c12236cffae324058b3aeec5fdee817000245224ba3b56`。

coast 为 $[c,c+L_c]$，$c=0.5919999999999992$、$L_c=0.2755434451024161$。权重

$$
w(s)=S_5((s-c)/r)S_5((c+L_c-s)/r),\qquad r=.12L_c
$$

在两个 rim 外分别平坦，$S_5(t)=10t^3-15t^4+6t^5$ 在 $t\le0$ 延为0、$t\ge1$ 延为1。

两个真实边界单元为

| cell | 左端 | 右端 | 准确端点质量 $w(b)-w(a)$ |
|---:|---:|---:|---:|
| 63 | 0.5919999999999992 | 0.6313633493003443 | $+1$ |
| 71 | 0.8281800958020702 | 0.8675434451024153 | $-1$ |

每格宽约 $0.03936334930034513$，是 rim 宽的 $1.190476190476\ldots$ 倍。已知 rim 片界位于单元内部，而两点 Gauss 节点均位于该 ramp 内。

`fd2d-metric-coast-window-quadrature.py` 将已有 provider 实际生成的 binary `entry`、`exit=entry+length` 与 `rim=length*fraction` 当成准确有理多项式常数。对这个明确的 scalar weight，它给出两边漏失质量的准确外包

$$
0.30816577911923976
\ \le\ |Q_2(w')-(w(b)-w(a))|\
\le\ 0.3081657791192398. \tag{1}
$$

这不是以浮点采样推断的误差：以下多项式公式在这两个实际单元上作有理运算即可得到 (1)。真实原浮点求积与该准确 scalar 计算之差另外记录在报告中。

## 2. 两点 Gauss 的完整准确公式

令

$$
\alpha=\frac12-\frac{\sqrt3}{6},\qquad
\beta=\frac12+\frac{\sqrt3}{6}.
$$

考虑从左 ramp 起点开始、长度 $h$ 的单元，写 $\lambda=h/r$。若 $\lambda\ge1$，单元右端位于平台，且 $\lambda\beta<1$，则两个 Gauss 节点仍在 ramp 内。准确积分由端点差等于1，而 Gauss2 值为

$$
\begin{aligned}
Q_2(w')&=15\lambda\left[(\lambda\alpha)^2(1-\lambda\alpha)^2
                     +(\lambda\beta)^2(1-\lambda\beta)^2\right]\\
&=10\lambda^3-15\lambda^4+\frac{35}{6}\lambda^5. \tag{2}
\end{aligned}
$$

证明只需
$\alpha+\beta=1$、$\alpha\beta=1/6$，从而

$$
\alpha^2+\beta^2=2/3,\quad
\alpha^3+\beta^3=1/2,\quad
\alpha^4+\beta^4=7/18.
$$

右 ramp 由镜像给出相反号。本例对应接近 $\lambda=25/21$；脚本使用真实 binary 网格宽度与 rim 宽度的准确商，没有把它直接替换成 $25/21$。

**只增加 rim 端点但仍在完整 ramp 上用两点 Gauss，误差不会消失。** 在 $\lambda=1$ 时，(2) 是 $5/6$。更一般，若把整条 ramp 等分成 $N$ 段并逐段用 Gauss2，准确质量是

$$
1-\frac{1}{6N^4}. \tag{3}
$$

为证明 (3)，在每个子段上 $w'$ 为四次多项式，其四次系数为 $30/r^5$。单位区间两点 Gauss 对 $t^4$ 的积分误差为 $-1/180$，所以长度 $h=r/N$ 的单元积分误差为 $-h^5/(6r^5)$；求和即得 (3)。

按已知片界分片后，三点 Gauss 对 $w'$ 的每个四次片准确积分，因为其精确次数为五。这只消除明确的 scalar weight 误差；对 $w'(R-L)$ 等非多项式乘积，不可据此声称积分完全准确。

## 3. 更直接的准确消元：不对 lifting 导数求积

令计算坐标为 $(x,\xi)$，完整场写成

$$
f(x,\xi)=B(\xi)y(x)+L(x,\xi;p), \tag{4}
$$

其中 $y$ 是实际保存的连续 P1 correction，$L$ 是明确的全函数 lifting，$p$ 是其参数。令 $f_d=(n,m)$ 为两条微分方程分量，并以 $\mathcal F(f,f_\xi;x,\xi,p)$ 表示完整 Codazzi 右端，已包含当前真实目标与固定角图。

在物理 $x=s$、$u=U(s,\xi)$ 情形中，这个右端明确是

$$
\begin{aligned}
\mathcal F_n&=\frac{m_\xi}{aU_\xi}+\frac{a'}a(l-n)
                           +\frac{U_s}{U_\xi}n_\xi,\\
\mathcal F_m&=\frac{l_\xi}{aU_\xi}-2\frac{a'}a m
                           +\frac{U_s}{U_\xi}m_\xi.
\end{aligned} \tag{5}
$$

所有符号仍用真实当前 $a_\delta$ 与完整独立 $l,m,n$；不借用参考的 base 方程替代目标。

这里一条径向积分线保持的是 **同一个计算角 $\xi$**，并非同一个材料角 $u$。端点 lifting 必须分别取 $L(a,\xi)$、$L(b,\xi)$，其参考部分分别是 $R(a,U(a,\xi))$、$R(b,U(b,\xi))$。因此准确端点差已经包含 $R_s+U_sR_u$ 的积分；(5) 的 $U_s n_\xi/U_\xi$、$U_s m_\xi/U_\xi$ 仍完整保留。若误以同一个 $u$ 取两个端点，又删除 (5) 的漂移项，将得到另一个错误方程。


原 correction 微分方程是

$$
By' = \mathcal F-L_{d,x}. \tag{6}
$$

在任一实际单元 $[a,b]$、$h=b-a$ 上，已知函数的微积分基本定理给出

$$
\frac{1}{h}\int_a^b L_{d,x}\,dx
  =\frac{L_d(b)-L_d(a)}{h}. \tag{7}
$$

所以无需把该项混入任何 Gauss 节点求和。完整的平均积分残差应写成

$$
\mathcal R_{ab}
 =\frac{B(y_b-y_a)+L_d(b)-L_d(a)}{h}
     -\frac1h\int_a^b\mathcal F(f,f_\xi)\,dx. \tag{8}
$$

有限离散只对 (8) 最后一项应用所选求积 $Q$。这样 R144 的 $w'(R-L)$ 项，以及所有其他 seed/tail lifting 的已知径向导数，其积分全部由准确端点差支付。它不需要增加未知节点、修改保存的 P1 场或改变物理度量。端点函数仍须按其定义准确求值或付明确数值误差；这里没有把浮点求值误差宣布为零。

这也是一个新有限求积规则，通常与已运行的“对 (6) 整体求积”不逐位相同。旧求解记录及残差身份必须保留，不能事后改名为新规则的收敛结果。

## 4. 保留角模、高角补余与 Jacobian

设 $P$ 为原低模分析投影、$H=I-BP$ 为完整高角补余。在准确 Fourier correction 空间中 $PB=I$、$HB=0$。于是 (8) 的两类行是

$$
\begin{aligned}
R_{\rm low}&=\frac{y_b-y_a}{h}
       +\frac{P(L_d(b)-L_d(a))}{h}-P Q\mathcal F,\\
R_{\rm high}&=\frac{H(L_d(b)-L_d(a))}{h}-H Q\mathcal F. \tag{9}
\end{aligned}
$$

不能在高角补余中删除 $H(L_d(b)-L_d(a))/h$：全函数 lifting 通常具有超出 correction 空间的真实角模。R142 的 D2 正交压缩仍可在这些完整高行上使用；完整 max 诊断应另保留。

对任意参数 $p_j$，固定实际计算端点求导，端点部分为

$$
\frac{L_{d,p_j}(b)-L_{d,p_j}(a)}{h}. \tag{10}
$$

其余部分为 $-Q\partial_{p_j}\mathcal F$，其中必须包括当前 $a,a',K$、完整字段和全角一导数的所有参数变化。未知节点方向保留 usual P1 左右端差，并在求积点计算真实 $\partial\mathcal F$。这不要求新的 $L_{xp}$ 数值差分，也不删当前目标连接导数。若端点或计算坐标自身随参数改变，须显式加入相应链式项；本次固定保存物理 $x=s$ 网格的 bump 布局没有这种额外项。

## 5. 余项和正则性范围

R143 的分片 $W^{1,\infty}$ / $W^{2,\infty}$ Peano 界可应用于剩余被积函数 $\mathcal F$；不能再把已由 (7) 准确消掉的 $L_x$ 误差重复收费。这里需要的只是在每片内 $L$ 绝对连续并具有一致端点值；R144 的 $C^2$ window 与已定义参考已满足，P1 correction 的导数跳不破坏 (7)。没有增加 $C^3$ 或 $C^4$ 曲面前提。

最终连续误差还要支付 $Q\mathcal F$ 的实际余项与所有函数求值包围。端点消元不自动证明 Gauss2 小等于全域小，也不完成主态、接缝、实际曲率、reach 或强比例。

## 6. 真实运行与闭存

工具 session `31387`、完成 chunk `8f1bbf`，**实际 exit 0**。脚本内部计时 0.53234 秒；只读取已有 scalar 定义与节点，不构造未知场、大矩阵或 body。

准确结果在 `2026-11-12-fd2d-metric-coast-window-quadrature-01-report.json`，SHA256

```
c60bb65f4a019b17b4bf7a92ec571e8f27b008a824852d84773fe6522cae99f4
```

本报告定位了现有限离散的一个明确误差项，并给出同一准确方程的直接修正方式。它既不把旧候选作几何否定，也不把新有限规则称为完整证明。

## 7. 原生 consumer 的明确范围

另名实现 `scripts/fd2d_gc_gauss_cell_codazzi_endpoint_d2.py` 提供

```python
gauss_cell_codazzi_endpoint_d2(problem, vector, order=2,
                               high_weight=1., jacobian=True)
```

它以原 Gauss2/D2 helper 的实际 `op`、`inv`、`adv`、计算角和 P1 插值为基础，只替换已知 lifting 径向积分。原全部 Gauss/边界/gap 行由 caller 保留。返回 low/high 残差与 sparse Jacobian、完整有限角 max 诊断和实际 Gauss 点，与原 16-cell chunk wrapper 的 `consumer=` 接口兼容。这里不要求在支撑 rim 插入未知节点，也不修改任何先前已闭 helper 或活动 solver。

保存的参考源、liftings 及参数列必须与当前 field 绑定。实现使用真正的 `L(b)-L(a)` 和 `L_p(b)-L_p(a)`，不由低角截断重建端点，不把 Nyquist 或非零高模删除。有限角误差、非多项式 PDE 求积误差及实际位置证书仍按原要求独立支付。

## 8. 实际小单元核验与首轮未覆盖项

独立脚本 `fd2d-metric-endpoint-codazzi-cell-check.py` 消费 09 已闭的同一原始初场，只构造两个保存节点的局部视图，并把主目标、固定角图、完整 lifting 与全部参数保持原定义。

第一次实际 cell63 核验（session47283，chunk9bf408）返回 **exit1**，原因是明设的“三类 JVP 全非零”覆盖条件不成立：该处 tail lifting 尚未激活，真实 tail 参数列与其有限差分都准确为浮点零。端点变化恒等式、状态列、物理 bump 列以及原局部 F/field 不变均已通过。该失败报告完整保存，不以之后结果覆盖。

随后仅把同一脚本的实际单元改为 cell71，使用原已闭 Gauss2 节点，未求新场。session84335、chunkcc70b2 **实际 exit0**，3.73178 秒、峰 RSS77640KiB。三类非零方向的相对 L2 JVP 误差为：

| 方向 | 真解析 JVP 的 L2 范数 | 中央差分相对 L2 误差 |
|---|---:|---:|
| 两个实际节点的状态 | 26.9021319053 | 1.78539e-10 |
| 完整尾参数 | .668617224546 | 1.24572e-8 |
| 物理半径参数 | 16.3586580114 | 4.91714e-10 |

三方向均使用明确的随机种子146146和步长1e-6，实际向量定义保存于报告。新状态 Jacobian 与旧 Gauss2 helper 逐项相同；原局部 provider 的 F、fields、mesh、角图和实际输入向量均逐项未变。新旧完整/low/high 行之差恰为 (7) 的端点差减去旧求积 L_x，有限全角投影与 low 行也一致。这里并不宣称新有限残差等于旧有限残差，更不把局部 JVP 核验当成全域证书。

两次报告和真实退出回执均收入同一闭存清单，原 source、原 solver 与首失败报告完整保留。
