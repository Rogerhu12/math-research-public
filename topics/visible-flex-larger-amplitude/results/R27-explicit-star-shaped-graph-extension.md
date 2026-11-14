# R27：非轴星形边界两阶数据的显式整图延拓

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。
日期：2026-11-12。

**状态：已证明（满足下列坐标、正则性与连续范数假设时）。**

本条为 [R25](R25-entire-graph-curvature-and-reach.md) 提供一个可直接核销的
外圈延拓构造：在真实 Cartesian 平面的极坐标中，匹配有限图的两阶边界数据，
经过一个有限宽度的环带后接到常值平面，并控制整个外环的主曲率。
原有限图内部只需控制主曲率，不要求其全域图 Hessian 小于同一预算。

**正则性条件不可省略。** 一般 $C^2$ 图的二阶径向导数在边界上只保证连续。
下面显式构造要求三组径向边界 trace 都属于 $C^2(S^1)$，并实际使用
二阶径向 trace 的两阶角导数。图在边界邻域 $C^4$ 是一个充分条件；
一般 $C^2$ 图不能无条件套用本条公式及其导数界。

## 1. 数据、坐标及结论

以下 $(r,\phi)$ 始终是真实水平 Cartesian 坐标的极坐标：
$$
 (x,y)=(r\cos\phi,r\sin\phi).
$$
它们不是源 ODE 的内蕴 $(r,\theta)$ 的默认别名。

设 $R\in C^2(S^1)$、$R(\phi)\geq R_*>0$，并令
$$
 \Omega=\{(r,\phi):0\leq r<R(\phi)\}.
$$
设一个真实高度图 $f$ 在 $\overline\Omega$ 的邻域中为 $C^2$。
在星形边界上记
$$
 a_0(\phi)=f(R(\phi),\phi),\quad
 a_1(\phi)=f_r(R(\phi),\phi),\quad
 a_2(\phi)=f_{rr}(R(\phi),\phi),
                                                               \tag{R27.1}
$$
并额外假设 $a_0,a_1,a_2\in C^2(S^1)$。
这里的 $f_r,f_{rr}$ 是固定真实极角 $\phi$ 的径向导数。

给定常数 $c_0,c_1,c_2$ 及外环宽度 $L>0$，下文显式构造
$$
 \widetilde f\in C^2(\mathbb R^2)
$$
满足：

- 在 $\overline\Omega$ 上 $\widetilde f=f$，全部两阶 Cartesian jets 匹配；
- 在 $r\geq R(\phi)+L$ 上 $\widetilde f$ 为同一个常数；
- 外环上的主曲率绝对值不超过一个由已知边界范数给出的显式上界
  $K_{\rm ext}$。

若原有限图的全域主曲率界是 $K_{\rm in}$，则辅助整图有
$$
 |\widetilde\kappa_i|\leq\max(K_{\rm in},K_{\rm ext}).
                                                               \tag{R27.2}
$$
因此可直接使用 R25 的整图 reach 和成对弦长不等式。
这一辅助外环不要求成为最终闭曲面的实际组成部分。

## 2. 显式插值公式

令
$$
 u=a_0-c_0,\qquad v=a_1-c_1,\qquad w=a_2-c_2,
$$
并定义五次基函数
$$
 \begin{aligned}
 H_0(t)&=1-10t^3+15t^4-6t^5,\\
 H_1(t)&=t-6t^3+8t^4-3t^5,\\
 H_2(t)&=\tfrac12t^2-\tfrac32t^3+\tfrac32t^4-\tfrac12t^5.
 \end{aligned}                                                \tag{R27.3}
$$
它们在 $t=0$ 的值、一阶导、二阶导组成单位矩阵：
$$
 H_i^{(j)}(0)=\delta_{ij},\qquad 0\leq i,j\leq2,
$$
并在 $t=1$ 同时满足 $H_i(1)=H_i'(1)=H_i''(1)=0$。

常数背景部分使用一个四次曲线。以 $s$ 为径向外移量、$t=s/L$，设
$$
 B(s)=c_0+
 Lc_1\bigl(t-t^3+\tfrac12t^4\bigr)
 +L^2c_2\bigl(\tfrac12t^2-\tfrac23t^3+\tfrac14t^4\bigr).
                                                               \tag{R27.4}
$$
直接计算：
$$
 \begin{aligned}
 B(0)&=c_0,&B'(0)&=c_1,&B''(0)&=c_2,\\
 B'(L)&=0,&B''(L)&=0,&
 B(L)&=c_0+\tfrac12Lc_1+\tfrac1{12}L^2c_2.
 \end{aligned}
$$

令
$$
 G(s,\phi)=B(s)+u(\phi)H_0(t)
             +Lv(\phi)H_1(t)+L^2w(\phi)H_2(t).
                                                               \tag{R27.5}
$$
所需延拓为
$$
 \widetilde f(r,\phi)=
 \begin{cases}
 f(r,\phi),&r\leq R(\phi),\\
 G(r-R(\phi),\phi),&R(\phi)\leq r\leq R(\phi)+L,\\
 B(L),&r\geq R(\phi)+L.
 \end{cases}                                                  \tag{R27.6}
$$
常数 $c_0$ 可以用来减少 $u$ 的零阶范数；
角导数范数不受这个常数选择影响。
三个 $c_j$ 只是延拓公式的参考常数，不必等于真实 trace 的角均值。
它们的选取同步进入 $u,v,w$，所以不会改变任何原边界值、mean slope 或 mean second。

### 2.1. 内边界两阶 jets 的匹配

在内边界 $s=0$，有
$$
 G=a_0,\qquad G_s=a_1,\qquad G_{ss}=a_2.
                                                               \tag{R27.7}
$$
写 $F(r,\phi)=G(r-R(\phi),\phi)$。链式法则给出
$$
 \begin{aligned}
 F_r&=G_s,&F_{rr}&=G_{ss},\\
 F_\phi&=G_\phi-R'G_s,&
 F_{r\phi}&=G_{s\phi}-R'G_{ss},\\
 F_{\phi\phi}
 &=G_{\phi\phi}-2R'G_{s\phi}+(R')^2G_{ss}-R''G_s.
 \end{aligned}                                                \tag{R27.8}
$$
另一方面，对实际 trace (R27.1) 沿边界微分，
$$
 \begin{aligned}
 f_\phi&=a_0'-R'a_1,\\
 f_{r\phi}&=a_1'-R'a_2,\\
 f_{\phi\phi}&=a_0''-2R'a_1'+(R')^2a_2-R''a_1.
 \end{aligned}                                                \tag{R27.9}
$$
将 (R27.7) 代入 (R27.8)，正好得到 (R27.9)，所以全部二阶极坐标 jets 匹配。
因为该边界 $r\geq R_*>0$，极坐标到 Cartesian 坐标的变换光滑且可逆，
故全部二阶 Cartesian jets 也匹配。

### 2.2. 外边界及原点

在 $s=L$，所有非轴项的值、径向一阶、径向二阶都为零。
其角导数及混合导数也相应为零，而 $B'(L)=B''(L)=0$。
由 (R27.8)，在变半径外边界 $r=R(\phi)+L$ 上，
全部一阶和二阶 Cartesian 导数都为零，值为同一个常数 $B(L)$。
故可以 $C^2$ 接到整片常值平面。

原点包含在原有限图的内部，仍使用原来的 Cartesian $C^2$ 函数 $f$；
新增公式只在 $r\geq R_*$ 的外环使用，不产生极坐标原点奇性。
这证明 (R27.6) 是整个 $\mathbb R^2$ 上的 $C^2$ 图。

## 3. 可核销的全外环导数上界

设
$$
 \rho_1\geq\|R'\|_\infty,\qquad
 \rho_2\geq\|R''\|_\infty,
$$
并有对 $j=0,1,2$ 的实际连续范数界
$$
 U_j\geq\|u^{(j)}\|_\infty,\quad
 V_j\geq\|v^{(j)}\|_\infty,\quad
 W_j\geq\|w^{(j)}\|_\infty.                                  \tag{R27.10}
$$
它们必须是整个实际边界上的上界，不能只填有限角网格的最大值。

### 3.1. 基函数的有理上界

下表是 $[0,1]$ 上的有效上界：

| 基函数 | $\|H_i\|_\infty$ | $\|H_i'\|_\infty$ | $\|H_i''\|_\infty$ |
|---|---:|---:|---:|
| $H_0$ | $1$ | $5$ | $20$ |
| $H_1$ | $2/5$ | $2$ | $12$ |
| $H_2$ | $1/20$ | $1/4$ | $2$ |

这些上界可在有理数中直接核对。若
$P(t)=\sum_{i=0}^n a_i t^i$，其 Bernstein 系数为
$$
 b_k=\sum_{i=0}^k a_i\frac{\binom{k}{i}}{\binom{n}{i}}.
$$
Bernstein 基函数非负、和为一，故
$\|P\|_\infty\leq\max_k|b_k|$。
对 (R27.3) 及其两阶导数使用此式即得上表。
全部系数和端点恒等式由
[有理账本脚本](../computations/tail_entire_extension_bounds.py) 逐项输出。

### 3.2. 背景部分

一般地，(R27.4) 满足
$$
 \|B'\|_\infty\leq
 b_{\rm mean}:=|c_1|+\frac4{27}L|c_2|,\qquad
 \|B''\|_\infty\leq
 a_{\rm mean}:=\frac3{2L}|c_1|+|c_2|.                                \tag{R27.11}
$$
这里使用 $0\leq1-3t^2+2t^3\leq1$、
$0\leq t(1-t)^2\leq4/27$，以及相应一阶导的上界 $3/2$ 和 $1$。

在本题外 cut 典型的 $c_1>0,c_2<0$ 情形，还可使用更直接的界。
若
$$
 \frac32\leq\alpha:=-\frac{Lc_2}{c_1}\leq3,
$$
则
$$
 B'=c_1(1-t)^2[1+(2-\alpha)t],\qquad
 B''=-\frac{c_1}{L}(1-t)[\alpha+(6-3\alpha)t].
 \tag{R27.12}
$$
括号满足
$$
 0\leq (1-t)[\alpha+(6-3\alpha)t]\leq\alpha.
$$
后一上界可分别在 $\alpha\leq2$ 和 $\alpha\geq2$ 时由二次式的
单调性或凸性直接验证。因此
$$
 0\leq B'\leq c_1,\qquad c_2\leq B''\leq0,
$$
可在下文取 $b_{\rm mean}=c_1,\ a_{\rm mean}=|c_2|$。
这一改进需要明确核对 $\alpha$ 区间；否则使用 (R27.11)。

### 3.3. 五个辅助导数界

由上表和 (R27.10)，可取
$$
 \begin{aligned}
 A&:=a_{\rm mean}+\frac{20U_0}{L^2}+\frac{12V_0}{L}+2W_0
       &&\geq\|G_{ss}\|_\infty,\\
 B&:=b_{\rm mean}+\frac{5U_0}{L}+2V_0+\frac{LW_0}{4}
       &&\geq\|G_s\|_\infty,\\
 C&:=U_1+\frac{2LV_1}{5}+\frac{L^2W_1}{20}
       &&\geq\|G_\phi\|_\infty,\\
 D&:=\frac{5U_1}{L}+2V_1+\frac{LW_1}{4}
       &&\geq\|G_{s\phi}\|_\infty,\\
 E&:=U_2+\frac{2LV_2}{5}+\frac{L^2W_2}{20}
       &&\geq\|G_{\phi\phi}\|_\infty.
 \end{aligned}                                               \tag{R27.13}
$$
本节 $A,\ldots,E$ 是外环的 Cartesian 极坐标导数上界，
其中 $E$ 不表示源 ODE 度量系数。

真实 Euclidean 水平平面中的 Hessian 在正交极坐标基下为
$$
 \nabla^2F=
 \begin{pmatrix}
 F_{rr}&F_{r\phi}/r-F_\phi/r^2\\
 F_{r\phi}/r-F_\phi/r^2&F_{\phi\phi}/r^2+F_r/r
 \end{pmatrix}.
                                                               \tag{R27.14}
$$
由 (R27.8)、$r\geq R_*$，可取
$$
 \begin{aligned}
 C_\times&=\frac{D+\rho_1A}{R_*}
              +\frac{C+\rho_1B}{R_*^2},\\
 T&=\frac{E+2\rho_1D+\rho_1^2A+\rho_2B}{R_*^2}
              +\frac B{R_*}.
 \end{aligned}
$$
于是
$$
 |(\nabla^2F)_{rr}|\leq A,\qquad
 |(\nabla^2F)_{r\phi}|\leq C_\times,\qquad
 |(\nabla^2F)_{\phi\phi}|\leq T
$$
（后两个下标在这里表示正交基的矩阵分量），从而
$$
 \boxed{\|\nabla^2F\|_{\rm op}\leq
 K_{\rm ext}:=\max(A,T)+C_\times.}                            \tag{R27.15}
$$
最后一步是对称 $2\times2$ 矩阵的最大绝对行和界，完全不需数值求特征值。

一个 Euclidean 图的对称形状算子矩阵为
$$
 (I+\nabla F\nabla F^T)^{-1/2}
 \frac{\nabla^2F}{\sqrt{1+|\nabla F|^2}}
 (I+\nabla F\nabla F^T)^{-1/2}.
$$
两侧因子的算子范数都不超过一，故 (R27.15) 同时控制外环的主曲率。
这证明 (R27.2)。图 Hessian 粗界只用于新增外环，原有限尾内部继续使用
其真实主曲率界 $K_{\rm in}$。

## 4. 一个完全有理的充分数据盒

以下是一个**条件性实例数据盒**，用于展示预算大小。
它不是把当前源 ODE trace 当作已经验证的 Cartesian trace。

取
$$
 \begin{gathered}
 R_*\geq0.29,\quad L=0.1,\quad
 \rho_1\leq0.001,\quad\rho_2\leq0.01,\\
 c_1\in[0.079,0.081],\qquad c_2\in[-1.9,-1.83],
 \end{gathered}
$$
并要求下列全角范数上界：

| 导数阶 $j$ | $U_j$ | $V_j$ | $W_j$ |
|---|---:|---:|---:|
| $0$ | $0.00013$ | $0.0015$ | $0.005$ |
| $1$ | $0.00027$ | $0.0031$ | $0.011$ |
| $2$ | $0.00058$ | $0.0065$ | $0.025$ |

全部小数均按所写有限小数理解为精确有理数。
这时
$$
 \alpha\in[61/27,190/79]\subset[3/2,3],
$$
所以 (R27.12) 的背景改进成立。
由 (R27.13) 可得
$$
 A=2.35,\quad B=0.090625,\quad C=0.0003995,\quad
 D=0.019975,\quad E=0.0008525.
$$
精确有理计算给出
$$
 \boxed{K_{\rm ext}\leq
 \frac{327359}{134560}=2.432810642\ldots<\frac52.}             \tag{R27.16}
$$
对应账本是
[2026-11-12-tail-entire-extension-bounds.json](../notes/2026-11-12-tail-entire-extension-bounds.json)。
其中标明 actual_cartesian_certificate 为 false；只有上面的坐标、trace 和
全域范数假设真的验证后，才可以把此数值上界用于实际候选。

例如，若同一个真实有限图内部已经证明
$K_{\rm in}\leq33/4$，则延拓整图满足主曲率界 $33/4$，R25 给出
$$
 \operatorname{reach}(\widetilde\Gamma)\geq\frac4{33}
 =0.121212\ldots.
$$
相对于 $\tau=3/25=0.12$，余量精确为
$$
 \frac4{33}-\frac3{25}=\frac1{825}>0.
$$
这可为 R24 的弱标记保持提供一个条件性起始余量。
它没有验证当前闭曲面所有跨图块的点对，也没有替代原图内部的曲率证明。

## 5. 内 cuff 的平面填充条件

若真实图在一个有界 $C^2$ 内边界外侧定义，并且在该边界上
$$
 f\to c,\qquad \nabla_{\!xy}f\to0,\qquad
 \nabla^2_{\!xy}f\to0
$$
以连续 Cartesian jets 的意义成立，则把内侧填为常值 $c$ 得到 $C^2$ 图，
且填充区主曲率为零。局部把内边界展平后，两侧全部二阶偏导的连续匹配
直接证明这一结论；不需要在接缝增加高曲率端盖。

用于本课题时，这些极限必须来自真正的无限尾与实际坐标变换。
有限深节点的极小 $Q,\pi$，或者源 profile 参数中的某个二阶导数，
不能单独替代上述 Cartesian 两阶极限。
该几何填充也不独立证明填充区与给定固定度量相容；
平盘度量和整族固定材料参数仍由实际闭合构造确定。

## 6. 当前研究接口与剩余验证

R27 的可执行输入是实际水平投影下的
$$
 R(\phi),\quad a_0(\phi),\quad a_1(\phi),\quad a_2(\phi),
$$
及其在 (R27.10) 中出现的连续导数范数。
对于已建立的 Cartesian 浸入，可先证明边界对选定原点星形，
再用实际极角把边界及其两阶高度 jets 转写成上述输入。
真实角变换、径向导数方向及两阶链式法则都应列入核销。

当前 M24/M32 同 H/g 结果提供了有限源 ODE 响应、原 cut Fourier 向量及全尾取样
审计；它们没有直接提供本条所需的全域 Cartesian 图、精确内 cuff 平面极限，
或上述实际极角 trace 范数。后续可使用更光滑的精确浅头/解析边界完成转换，
但其高正则性和投影可逆性必须分别验证。

若这些输入界及 $K_{\rm in}$ 对整族参数一致，则本构造的外环界、
R25 的整图 reach 下界也一致。辅助外环在原图以外无须保持原度量；
它只负责为实际有限图内部的全部有序点对提供 R25 不等式。
最终闭曲面的其他点对仍按 R11/R16/R21 及 R24 的路线处理。
