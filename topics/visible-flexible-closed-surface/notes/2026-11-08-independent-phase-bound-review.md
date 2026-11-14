# 2026-11-08 独立审查：全相位配准与窄帽标记乘积上界

审查会话：Astra-visible-flex-effcccee / audit_phase_bound；GPT-6 Astra Pro，AI-assisted。审查者未参与被审笔记、脚本或源模型的编写与计算。

## 结论与可信度

**核心数学结论：PASS。** 以下结论均有完整证明，适用范围在下文逐项限定：

1. 当前 wide-m2 的整个活动带在像集意义下可用一个轴旋转完全配准。因此对任意相位，包含反射的完整欧氏群商 Hausdorff 距离均不超过固定上帽高度范围 $B_*$。
2. 采用当前数学定义的精确 binary64 输入 $r_e=.86$、$\sigma=.94$，有 $B_*=\sigma/20000$、$D\ge2r_e$，从而严格有 $\delta/D<2.7325581396\times10^{-5}$。这个上界不使用报告的长经线、帽间距、tail 曲率或等距残差。
3. 保持相同窄支撑、同一 bump 形状与同一整体相位机制，只改变四个非负高度，则对任何仍为 $C^2$ 闭嵌入的族，$\delta\,\inf_t\operatorname{reach}(F_t(M))/D^2\le1/3200$。这排除了该模板同时达到 $\delta/D\ge.05$ 与全部 $t$ 的 reach$/D\ge.03$。

**严格输出端点的标注：需作小修正。** 被审脚本中的 Fraction 计算正确；JSON 的若干 `float(...)` 数字只能作为近似显示，不能自动当作精确十进制的有向端点。下文给出应补充的精确分数及向外舍入端点。这不阻断上述结论，也不需要重新求解任何 PDE。

**本审查不意味着本题完成。** 本题 README 明列任何障碍结果只算中间进展。本审查没有产生满足七项完成标准的正例，也没有认证一条新的精确等距族。

## 1. 审查对象、来源与独立复算

被审文件的 SHA-256：

| 本题文件 | SHA-256 |
|---|---|
| `notes/2026-11-08-repo-amplitude-review.md` | `36a47f99e5eba5a002359b6fd59ffdeda4b32a6ecb4e395ab147ceaefba05bf8` |
| `notes/repo_review_phase_shape_bound.py` | `57c8efd676b73602a8a58e60ea192f1f5c76af5d74226c11d8689dff3a439bfb` |
| `README.md` | `843a592657166b450163e412c3fc8de0c6b017162fccb9dadf96283f03af9649` |

我直接从 GitHub main 读取实际闭模型、实际帽公式、模型定义与 R35；随后对本地缓存计算 Git blob SHA，确认本地读取的完整源码与远端返回的 blob 相同。没有从其他会话的结论代替公式核对，没有读取网格或大系数数组。

| 来源 | 读取时 Git blob SHA |
|---|---|
| [根 README](https://github.com/Rogerhu12/math-research/blob/main/README.md) | `f28db43754eef3b9f96d3981a6829f3574d461b9` |
| [实际闭模型](https://github.com/Rogerhu12/math-research/blob/main/topics/large-amplitude-twist-flex/scripts/f6root_closed_wide_m2_model.py) | `d6af93b9b226bfe268286383ec2c6bef949369f4` |
| [实际帽公式](https://github.com/Rogerhu12/math-research/blob/main/topics/large-amplitude-twist-flex/scripts/f6root_inward_caps.py) | `64fc6398c3512a0b95df53232c496d907628ada4` |
| [模型数学定义](https://github.com/Rogerhu12/math-research/blob/main/topics/large-amplitude-twist-flex/notes/f6root_closed_wide_m2_definition.md) | `86102c7650fb3bb7ea174bfb7abda385cc9f8857` |
| [R35](https://github.com/Rogerhu12/math-research/blob/main/topics/large-amplitude-twist-flex/results/R35-closed-wide-m2-geometric-certificate.md) | `d507a4e347b73047809f892c2bb447f2ceb9de26` |
| [所选 M12 帽参数报告](https://github.com/Rogerhu12/math-research/blob/main/topics/large-amplitude-twist-flex/notes/f6root_closed_wide_m2_m12_cusp_p128_model.json) | `4711c8fb206244b98cf83094eaf5a0a20b2ddfb8` |

运行 `python notes/repo_review_phase_shape_bound.py` 成功；我另外用 Fraction 从实际 `MarkedFlatCap` 对象提取初始化后的 binary64 参数，核对精确定义与执行舍入的差异。只复算了标量、四个帽中心及其局部 jets。本审查覆盖被审笔记第 2–3 节与相关标量脚本；第 4 节列举的其他课题求解器、残差表和大数据独立重跑不属于本次认证范围。

## 2. 实际源码确实是一条可整体对齐的带

记 $R_\alpha$ 为绕 $z$ 轴旋转，$B_\alpha$ 为完整 band 的像，包括 core、两个 prefix、两个 tail 与两个平面环领。

`ClosedWideM2.core` 先将角变量替换为 $\theta+\alpha$，再左乘 $R_{-\alpha}$。`prefix_half` 与 `tail_half` 对上半带采用同样操作；下半带还具有固定的 $\pi/2$ 角平移、关于水平面的反射及固定轴旋转。这些固定操作已包含在下半带的 $F_0$ 中。因此直接从函数表达式可得，下半带也满足同一个关系

$$F_\alpha(s,\theta)=R_{-\alpha}F_0(s,\theta+\alpha).$$

这里没有把下半带的相位误写成相反方向。`flat_collar` 本身轴对称，虽不接收 `phase` 参数，仍满足 $R_{-\alpha}F_0(r,\theta+\alpha)=F_0(r,\theta)$。接缝修补只改变 $F_0$ 的角函数，不引入另一套相位。

角变量遍历整个 $S^1$，预合成 $\theta\mapsto\theta+\alpha$ 不改变像集，所以

$$B_\alpha=R_{-\alpha}B_0\qquad\text{对每个实数 }\alpha.$$

`cap_graph` 的上帽始终调用同一个 `MarkedFlatCap`；下帽始终是 $z=-H$ 的完整圆盘，均无相位参数。令 $C_+$、$C_-$ 为两帽，则全曲面像为

$$S_\alpha=R_{-\alpha}B_0\cup C_+\cup C_-.$$

这一结论来自实际公式，不依赖求解器误差趋零或 R35 的全局区间证书是否已扩展到后续 M16 模型。任何后来替换的带，只要仍严格使用这一整体相位操作和同一固定帽，均满足相同像集等式。

## 3. 固定图帽的全相位 Hausdorff 上界

设 $K=\{x\in\mathbb R^2:|x|\le r_e\}$，上帽为

$$C_+=\{(x,H+h(x)):x\in K\},\qquad 0\le h(x)\le B_*.$$

下帽 $C_-=\{(x,-H):x\in K\}$ 旋转不变。对任意 $\alpha$，选用具体允许的刚体运动 $A_\alpha=R_\alpha$，便有

$$A_\alpha S_\alpha=B_0\cup R_\alpha C_+\cup C_-.$$

由于 $K$ 旋转不变，$R_\alpha C_+$ 仍是同一底盘上的图，其高度函数为 $H+h(R_{-\alpha}x)$。将两图上具有相同 $x$ 的点配对，得

$$|h(R_{-\alpha}x)-h(x)|\le B_*.$$

此配对同时控制两个有向 Hausdorff 距离。给两个集合加入共同的 $B_0\cup C_-$ 不会增大已有上界，因而

$$d_H(A_\alpha S_\alpha,S_0)\le B_*.$$

对完整欧氏群取最小值不会增大这个具体候选值：

$$\min_{A\in E(3)}d_H(AS_\alpha,S_0)\le B_*.$$

允许平移、其他旋转与反射均不影响这个方向的不等号，因为我们只需展示一个 admissible 对齐。没有假定最优刚体唯一，也没有用有限角度网格代替 $E(3)$。

因此对任何相位范围、任何 $t\mapsto\alpha(t)$，每个 $t$ 均有上述上界，特别是本题的最大值满足 $\delta\le B_*$。如果仅讨论任意参数集合，改写为上确界仍成立。本题的连续紧族不存在此量词问题；对非空紧像，欧氏配准的平移参数可限制在有界集合，故最小值可取到。

高度范围为何是 $B_*$ 而非 $2B_*$：两个高度都在同一个区间 $[0,B_*]$。若以后允许正负标记，则必须改用整个高度振荡 $\sup h-\inf h$，不能无条件沿用最大绝对振幅。

## 4. 实际 bump 的支撑、最大值和 $C^2$ 性

实际上帽使用四个中心

$$x_j\in\{(-r_e/3,0),(r_e/3,0),(0,r_e/3),(0,-r_e/3)\},$$

共同半径 $b=\min(r_e/10,\sigma/20)$ 与非负高度 $a_j$。当前 $(a_1,a_2,a_3,a_4)=(A,A,A,2A)$、$A=b^2/(100\sigma)$，指数为 $.2,.4,.6,.8$。帽函数是四个 bump 的和：

$$h(x)=\sum_{j=1}^4 a_j\phi_{\beta_j}(|x-x_j|/b),$$

$$\phi_\beta(t)=\begin{cases}(1-t^2)^4(1+t^{2+\beta}),&0\le t<1,\\0,&t\ge1,\end{cases}\qquad0<\beta<1.$$

最小中心间距为 $\sqrt2r_e/3>r_e/5\ge2b$，因此四个闭支撑两两分离。每个支撑位于 $|x|\le r_e/3+b\le13r_e/30<r_e$，所以帽边界附近恰为平面。

对 $0\le t\le1$，令 $u=t^2$，则 $t^{2+\beta}\le t^2$，从而

$$0\le\phi_\beta(t)\le(1-u)^4(1+u).$$

右端的导数为 $-(1-u)^3(3+5u)\le0$，起点值为 1，所以 $0\le\phi_\beta\le1$ 且 $\phi_\beta(0)=1$。非负高度与不重叠支撑给出

$$\max h=\max_j a_j=:B_*.$$

关于正则性，中心附近有 $\phi_\beta(t)=1-4t^2+t^{2+\beta}+O(t^4)$。更直接地，对 $p=2+\beta>2$，

$$\partial_{ij}|y|^p=p|y|^{p-2}\delta_{ij}+p(p-2)|y|^{p-4}y_i y_j,$$

其范数为 $O(|y|^\beta)$，趋向零。因此中心的二阶导数存在且连续；不能只用一个函数值渐近式跳过此项。支撑边缘有四阶因子 $(1-t)^4$，其余因子在 $t=1$ 附近光滑，故向外延零至少为 $C^3$。整个图函数为 $C^2$。

在高度为 $B_*$ 的某个中心 $x_*$，其他 bump 在邻域中恒零，故

$$\nabla h(x_*)=0,\qquad D^2h(x_*)=-\frac{8B_*}{b^2}I_2.$$

源码中 `gpp=8*(1-r*r)**2*(7*r*r-1)`、中心 `tangential=-8` 与径向 Hessian 公式确实给出这一值；我在四个实际中心复算了零梯度与 Hessian。不同指数用于原构造的标记识别，但本上界仅需 $\beta>0$，不使用指数互异或非全等证明。

## 5. 从中心实际曲率到 reach 上界

以下论证的方向不能颠倒。我们掌握一个点处主曲率的**确切非零值**；不是从形如 $|\kappa|\le95.103$ 的全局上界推导 reach 上界。

设 $S$ 是 $C^2$ 闭嵌入曲面，$p\in S$，$n$ 为单位法向。取 $0<r<\operatorname{reach}(S)$。根据 reach 的法向管刻画，即本题 README 所用的法向单射半径，$p\pm rn$ 的最近点为 $p$：任何最近点 $q$ 都满足法向条件，且距离至多 $r$，否则同一管内点将有两种法向表示。故对每个 $q\in S$，

$$|q-(p\pm rn)|^2\ge r^2,$$

展开得到法向二次支撑不等式

$$|n\cdot(q-p)|\le\frac{|q-p|^2}{2r}.$$

在某主方向取单位切向 $v$ 和局部法截面参数，有

$$q(s)-p=sv+\tfrac12\kappa s^2n+o(s^2).$$

代入、除以 $s^2$、令 $s\to0$，得 $|\kappa|\le1/r$。再令 $r\uparrow\operatorname{reach}(S)$，对非零曲率即得

$$\operatorname{reach}(S)\le\frac1{|\kappa|}.$$

在最大 bump 中心，图面第一基本形式为 $I_2$，取向上的法向时第二基本形式为 $D^2h$，所以两个主曲率均为 $-8B_*/b^2$。取绝对值后不依赖法向约定。每个相位保留同一个上帽，因此只要对应全曲面是 $C^2$ 嵌入，均有

$$\operatorname{reach}(S_\alpha)\le\frac{b^2}{8B_*}\qquad(B_*>0).$$

远处自接近只可能进一步减小 reach，不会破坏这一局部上界。若某次改高后不再嵌入，则已经不满足本题，不能把该失败当作上述条件结论的反例。

## 6. 乘积障碍：全部不等号及量词

初始像含完整半径 $r_e$ 的帽边界圆。取其两个对径点，得精确 $D\ge2r_e>0$。令

$$\rho_*=\inf_{t\in[0,1]}\operatorname{reach}(S_{\alpha(t)}).$$

使用下确界可以避免额外援引 reach 最小值的取到性；若最小值取到，即为被审笔记所写的 $\min_t$。我们已经证明了每一个 $t$ 的上界，故不依赖哪个时刻达到 $\delta$ 或最小 reach。

当 $B_*>0$ 时，所有被乘项都非负，故

$$\frac{\delta\rho_*}{D^2}
\le\frac{B_*}{D^2}\frac{b^2}{8B_*}
=\frac{b^2}{8D^2}
\le\frac{(r_e/10)^2}{8(2r_e)^2}
=\frac1{3200}.$$

当 $B_*=0$ 时两帽均轴对称，整个像族可整体配准，$\delta=0$，同一结论直接成立。本题需要 $\delta\rho_*/D^2\ge(1/20)(3/100)=3/2000$，而 $3/2000>1/3200$，矛盾。

若仅保留全部 $t$ 的 reach$\ge3D/100$，则

$$\delta/D\le(1/3200)/(3/100)=1/96.$$

保持同一种二阶中心系数的 bump 而放宽支撑半径时，要满足两个门槛至少需要 $b/D\ge\sqrt{3/250}=\sqrt{.012}\simeq.1095445115$。这是该局部形状模板的必要条件，不是任意“宽帽锚”的一般必要条件，更不是可行构造。

## 7. 当前具体常数与打印舍入

R35 明确将 $.86,.94$ 解释为精确 binary64 输入。记其精确实数为 $r_e,\sigma$，则

$$r_e=\frac{7746191359077253}{9007199254740992},\qquad
\sigma=\frac{2116691824864133}{2251799813685248}.$$

按数学定义作精确代数计算：

$$b=\sigma/20,\qquad B_*=2A=\sigma/20000
=\frac{2116691824864133}{45035996273704960000},$$

$$2r_e=\frac{7746191359077253}{4503599627370496},\qquad
\frac{B_*}{2r_e}=\frac{2116691824864133}{77461913590772530000}
<2.7325581396\times10^{-5}.$$

这些是脚本的 Fraction 路径实际核对的参数。当前数学模型定义第 3 节明确用 $\sigma/20$ 和 $\sigma/20000$，故这一精确解释有来源，不是审查者自行改写几何。

实际 Python 初始化则会在中间步骤舍入。独立从 `MarkedFlatCap(.86,.94,0,True,(.2,.4,.6,.8))` 提取 binary64 常数，得到

$$b_{\rm stored}-\sigma/20=\frac1{360287970189639680},$$

$$2A_{\rm stored}-\sigma/20000=-\frac9{92233720368547758080000}.$$

因此数学公式中的等号不能逐字解释为每一步机器运算都无舍入。但对执行参数冻结后解释成解析图面的版本，实际存储最大高度反而更小，且直接 Fraction 核对仍有 $b_{\rm stored}<r_e/10$；两项上界都保持有效。把浮点求值的输出表本身误当成逐点精确定义的光滑曲面没有意义，所审对象始终是解析表达式及其明确常数。

有两处显示精度值得明确：

- 精确 $2r_e$ 略小于十进制实数 $1.72$。被审笔记写 $D\ge2r_e\simeq1.72$ 是正确的；若改写成严格 $D\ge1.72$ 则不成立。可用上面的精确分数，或保守地写 $D>1.7199999999999999$。
- JSON 输出 `2.7325581395348836e-05` 是浮点近似；若把该打印字符串当作精确十进制数，它比精确分数上界略小。`1/96` 输出为 `0.010416666666666666` 也同样是内向近似。被审 Markdown 中采用 `2.7325581396e-5` 及精确 `1/96` 已经安全。

### 建议的精确修改

无需改数学定理，只需给脚本及笔记增加可复核的端点语义：

1. 在脚本中增加 `diameter_lower_exact=str(D_collar_lower)`、`delta_over_D_bound_exact=str(cap_height/D_collar_lower)`、`delta_over_D_upper_outward_decimal="2.7325581396e-5"`，并断言该精确分数小于对应 `Fraction`。
2. 增加 `delta_over_D_upper_if_reach_at_least_003D_exact="1/96"`；现有浮点字段改名带 `_approx` 或在脚本说明中统一标注为近似显示。无需用向外舍入的浮点替代精确分数。
3. 在笔记具体帽参数后补一句：“这里的等式按数学定义用精确输入作实数运算；执行时舍入常数另有下述差异，现有上界仍向安全方向成立。”也可直接引用本审查。
4. 将“支撑宏观宽度 $b/D\ge.109545$ 的锚定几何”限定为“仍保持本节 bump 二阶中心系数及高度配准界的锚定几何”。不同宽帽曲率形状可能有不同常数，不应把 $\sqrt{.012}$ 扩展成普适定理。
5. 若不想证明 reach 最小值取到，把乘积公式中的 $\min_t$ 写为 $\inf_t$；矛盾论证及全部 $t$ 的条件原封不动。此项只简化形式逻辑，不更改排除范围。

被审脚本正确将 $H=4.1965850822557265$ 和 sampled curvature 标为报告数值。它们未参与上述严格上界。没有据 $\kappa\le95.102735$ 推出 reach$\le1/95$ 的错误；该反向推论绝不能在后续引用时加入。若将 sampled curvature 升级为严格 reach 上界，仍需一个确切位置的实际主曲率下界及明确的区间求值。

## 8. 可以引用的范围与不能据此声称的事

可引用：一个可整体轴旋转配准的 band、固定平面下帽、固定非负图上帽的 $\delta\le B_*$；对于内部不重叠的上述 bump、共同半径 $b\le r_e/10$，可引用任意非负高度的 $1/3200$ 乘积障碍。当前模型的精确 cap 参数及后续保持同样结构的离散细化都在此范围内。

不可扩展为：任意闭曲面、任意上帽、符号任意的标记、互相重叠的 bump、具有不同二阶峰顶形状的标记，或多个无法被同一刚体同时配准的活动分量的普遍不可能性。也不能据本报告宣称精确等距、整个模型的 $C^2$ 嵌入区间证书、固定几何收敛门或 README 正例已经完成。

审查最终状态：**核心结论 PASS；严格标量输出需上述端点与适用范围说明；本题继续研究。**
