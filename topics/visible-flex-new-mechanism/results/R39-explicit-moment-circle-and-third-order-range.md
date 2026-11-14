# R39：全零周期基底上的显式三矩圆与三阶相容通道

日期：2026-11-14。root 全文审读，repo_sources 独立逐项核对通过。独立构造和精确方程。以 [R37](../results/R37-closed-geometry-zero-period-operator.md) 的真实零算子周期浸入带为基底；没有运行新的研究数值。

**已支付。** 给出不依赖数值特征向量的具体 $C^\infty$ profile 圆，它满足全部三个 ruling 总矩；完整二阶周期条件由 R37 自动支付，故真实二阶校正存在。并将下一阶准确化成两个 forcing 通道，证明其中的周期障碍不受任何同 collar 齐次 profile gauge 影响。

**未支付。** 本稿没有证明这两个三阶通道通过，没有给固定非零参数下的精确连续等距族。特别地，线性组合 $X+\varepsilon(\cos\theta\,Y_f+\sin\theta\,Y_g)$ 本身并不保持同一个度量。

## 1. 八个分离 bump 给完全显式的三矩平衡

取 $\delta=1/10$，定义偶的紧支撑光滑函数

$$\eta(x)=
\begin{cases}
\exp\{-1/[1-(x/\delta)^2]\},&|x|<\delta,\\
0,&|x|\ge\delta.
\end{cases}$$

对 $j=1,2,3,4$，令

$$b_j(x)=\eta(x-j)+\eta(x+j).$$

这四个偶函数的支撑互不相交，每个由两个同形 bump 组成。记

$$m_0=2\int_{\mathbb R}(\eta'')^2\,dx>0,\qquad
m_2=2\int_{\mathbb R}x^2(\eta'')^2\,dx
+4\int_{\mathbb R}(\eta')^2\,dx.$$

使用当前 range 的三个准确总矩

$$I_0(\phi)=\int(\phi'')^2,\qquad
I_1(\phi)=\int x(\phi'')^2,$$

$$I_2^*(\phi)=\int x^2(\phi'')^2+2\int(\phi')^2.\tag{1}$$

平方不带复共轭；本节 $b_j,f,g$ 为实函数。直接平移积分给

$$I_0(b_j)=m_0,\qquad I_1(b_j)=0,\qquad
I_2^*(b_j)=m_2+j^2m_0.\tag{2}$$

不同 $b_i,b_j$ 的三个交叉矩全部为零，因为其导数支撑也不交。

现在准确取

$$\boxed{\quad
f=\sqrt{\frac{19}{30}}\,b_1+\sqrt{\frac{11}{30}}\,b_4,\qquad
g=\frac{b_2+b_3}{\sqrt2}.
\quad}\tag{3}$$

由

$$\frac{19}{30}+\frac{11}{30}=1,\qquad
\frac{19\cdot1+11\cdot16}{30}=\frac{4+9}{2}=\frac{13}{2},$$

可得

$$I_0(f)=I_0(g)=m_0,\qquad I_1(f)=I_1(g)=0,$$

$$I_2^*(f)=I_2^*(g)=m_2+\frac{13}{2}m_0.\tag{4}$$

$f,g$ 的交叉三矩也全为零。因此

$$\phi_\theta=\cos\theta\,f+\sin\theta\,g$$

在全部 $\theta$ 上保持三个总矩。等价地，复 profile $q=f+ig$ 的三复总矩全部严格为零。

只用两个平移的相同 bump 再乘相对相位 $i$，一般不能同时抵消 (1)：$I_1$、$I_2^*$ 含坐标权重。这里的四对配置明确支付了这些权重。

## 2. 可放入任意紧活动物理区间

设 $\phi(\xi)=a_*\psi((\xi-\xi_*)/\sigma)$，其中 $\sigma>0$。准确变换律为

$$I_0(\phi)=\frac{a_*^2}{\sigma^3}I_0(\psi),$$

$$I_1(\phi)=\frac{a_*^2}{\sigma^3}
\{\xi_*I_0(\psi)+\sigma I_1(\psi)\},$$

$$I_2^*(\phi)=\frac{a_*^2}{\sigma^3}
\{\xi_*^2I_0(\psi)+2\xi_*\sigma I_1(\psi)
+\sigma^2I_2^*(\psi)\}.\tag{5}$$

交叉矩遵循同一线性变换。故可共同平移、缩放 (3)，把全部支撑放入 R37 的任意更小物理活动区间，两侧均留开放零 collar；(4) 和交叉零矩仍严格成立。以下沿用 $f,g$ 表示已经完成这次共同变换的 profile。

## 3. 真正可解的二阶固定度量方程

记公开无穷小场为

$$Y_\phi=U\phi+V\phi',\qquad
U=uB,\quad V=-\frac{uT+wB}{2h}.$$

定义线性化度量算子及对称双线性张量

$$\mathcal L_X Z=(DX)^T DZ+(DZ)^T DX,$$

$$\mathcal S(Y,Z)=(DY)^T DZ+(DZ)^T DY.$$

令 $H_f=(DY_f)^TDY_f$、$H_g=(DY_g)^TDY_g$。由于 (3) 中 $f,g$ 的支撑互不相交，逐点都有

$$\mathcal S(Y_f,Y_g)=0.\tag{6}$$

这比交叉总矩为零更强，但不表示 $H_f=H_g$；二者恰在不同活动子区出现。

R37 的全零算子使每个 profile 的完整周期函数障碍为零。对

$$H_d=H_f-H_g,$$

三个 ruling 总矩由 (4) 支付，所以 [完整 range 定理](../notes/literature-second-order-moments-20261114.md) 给一个真实 $C^\infty$、周期、两 collar 为零的向量场 $Z_d$，满足

$$\mathcal L_X Z_d=H_d.\tag{7}$$

可取同一锚点和同一齐次 gauge 的具体积分恢复。

于是准确取

$$Y_\theta=\cos\theta\,Y_f+\sin\theta\,Y_g,\qquad
Z_\theta=\sin^2\theta\,Z_d.\tag{8}$$

由 (6)–(7)，

$$\mathcal L_X Z_\theta+(DY_\theta)^TDY_\theta=H_f.$$

对固定参考度量

$$g_\varepsilon=(X+\varepsilon Y_f)^*e
=g_X+\varepsilon^2H_f$$

而言，真正定义的二阶路径

$$F^{[2]}_{\varepsilon,\theta}
=X+\varepsilon Y_\theta+\varepsilon^2Z_\theta
$$

满足准确展开

$$\begin{aligned}
(F^{[2]}_{\varepsilon,\theta})^*e-g_\varepsilon
={}&\varepsilon^3\mathcal S(Y_\theta,Z_\theta)\\
&+\varepsilon^4(DZ_\theta)^TDZ_\theta.
\end{aligned}\tag{9}$$

所以在固定紧带上误差为一致的 $O(\varepsilon^3)$，不是零。$\theta=0,\pi$ 两个端点的 $Z_\theta=0$，给熟悉的两个准确等距像 $X\pm\varepsilon Y_f$；中间相位仍须解后续方程。

本节的 $g_\varepsilon$ 只随一次选定的 $\varepsilon$ 而定，在比较不同 $\theta$ 时未改动。

## 4. 三阶准确地只剩两个 forcing 通道

继续写

$$F_{\varepsilon,\theta}
=X+\varepsilon Y_\theta+\varepsilon^2Z_\theta
+\varepsilon^3W_\theta+\cdots .
$$

与同一个 $g_\varepsilon$ 比较，$\varepsilon^3$ 系数要求

$$\mathcal L_X W_\theta
=-\mathcal S(Y_\theta,Z_\theta).\tag{10}$$

定义两个具体 forcing 张量

$$H_f^{[3]}=-\mathcal S(Y_f,Z_d),\qquad
H_g^{[3]}=-\mathcal S(Y_g,Z_d).$$

由 (8)，右侧准确为

$$\sin^2\theta\{
\cos\theta\,H_f^{[3]}+\sin\theta\,H_g^{[3]}\}.\tag{11}$$

因此对当前固定的 $Z_d$，完整三阶可解当且仅当这两个通道都通过同一完整 range 条件。若解得
$\mathcal L_X W_f=H_f^{[3]}$、
$\mathcal L_X W_g=H_g^{[3]}$，便可取

$$W_\theta=\sin^2\theta(\cos\theta\,W_f+\sin\theta\,W_g).$$

必要性也直接成立：$\theta=\pi/2$ 单独取出 $H_g^{[3]}$，再用任一 $\sin\theta\cos\theta\ne0$ 的相位即可取出另一通道。

这没有把所有三阶误差误算成三个总矩。对一般 $H$，准确的两个条件仍是：

1. 对每条固定 $s$ 的完整 ruling，$\int H_{uu}\,du=0$；
2. 从同一 collar 积分得到 $2r_u=H_{uu}$ 后，对每条固定 $\xi$ 的闭叶，
   $$\mathscr P(H)(\xi):=
   \oint\frac{\frac12H(D_s,D_s)+(wk-u)r-cD_sr}{u^2}\,ds=0,$$
   其中 $D_s=\partial_s|_\xi$、$c=D_su$。

第二条是整个函数为零。第三阶 forcing 一般不再是两个无穷小 profile 场的平方差，不能仅以 $M=0$ 跳过它。

## 5. 三阶周期障碍不受齐次 profile gauge 影响

固定相同两 collar 条件，若另取一个二阶解 $\widetilde Z_d$，则完整齐次 range 分类给

$$\widetilde Z_d-Z_d=Y_\psi$$

对某个两侧为零的光滑 profile $\psi$ 成立。理由是齐次方程首先给 $r_u=0$，collar 条件迫 $r=0$；随后
$D_s(\zeta/u^2)=0$，剩余自由度恰为一个 $\xi$ 函数，恢复成上述 profile 场。

周期泛函 $\mathscr P$ 是 forcing 的线性泛函，并且它可在未先支付另一侧 collar 条件时，仍按同一侧锚定的 $r$ 定义。对任意紧支撑 profile $\phi,\psi$，极化 R37 的恒等式 $\mathcal O_\phi\equiv0$ 给

$$\mathscr P\{\mathcal S(Y_\phi,Y_\psi)\}=0.\tag{12}$$

故两条三阶周期函数满足

$$\mathscr P(\widetilde H_f^{[3]})
=\mathscr P(H_f^{[3]}),\qquad
\mathscr P(\widetilde H_g^{[3]})
=\mathscr P(H_g^{[3]}).\tag{13}$$

同样，若在每个 $\theta$ 加入任意允许的齐次 profile gauge，(10) 的周期障碍仍不改变。调整二阶 gauge 可以改变第三阶 ruling 条件，但不能靠这一自由度消去一个非零的三阶周期函数。

因此 (13) 给出了准确的下一研究对象：两个由实际零算子几何和显式 $f,g$ 决定的三阶周期障碍类。它们若非零，就必须改变几何或 profile，而不是把残差吸收到一个虚假的 gauge 修正中。

## 6. 对完成标准的边界

本稿完成了完整二阶相容的显式 profile 圆，并给出真正三阶方程、两个必要充分通道及周期障碍的 gauge 不变性。没有证明这些三阶周期函数为零，也没有把有限阶误差随 $\varepsilon$ 变小当成固定参数的精确等距族。

基底目前仍是 R37 的周期浸入带。闭面嵌入、固定握持区的宏观位移和统一 reach 尚未支付；这些条件不能由二阶矩平衡或有限阶 Taylor 路径自动推出。

