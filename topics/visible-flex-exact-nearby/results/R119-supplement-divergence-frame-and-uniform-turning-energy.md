# R119 续篇：完整散度框架与全部转向频率上的扰动能量门

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 前篇一阶框架的零阶矩阵具有比任意小矩阵更强的
准确结构。把其角导项并回 principal 散度，再对两个分量作真正的
density hodograph，可得
$$
 Y_t=\partial_\xi[(bI+c\mathsf B_0)Y]+\mathsf C_0Y+
            \mathsf GY+\begin{pmatrix}0\\c^{-1}e\circ\Theta\end{pmatrix},
 \qquad
 \mathsf B_0=\begin{pmatrix}0&1\\-A&0\end{pmatrix}.
 \tag{D.1}
$$
余项 $\mathsf G$ 的整个下行有准确的因子 $Aw^2$，在每个 $A=0$
处消失。它在完整 Fourier Airy 两态平衡中没有隐藏的 $|m|^{1/3}$
损失。对同一真实 $\ell^1_{224}$ 标签域，实际共同漂移和此余项给
平方能量的额外系数，其全尾积分小于 $2^{-427}X_{224}$。

该结论保留真实 $b,c$。它支付的是实际转向框架内的扰动能量，不
声称正型区的 Cauchy 问题在 Sobolev 空间有界，也不代替真实
Ai/Bi 边界 Green、全 return 相位或最终非线性高输入逆。

## 1. 同一准确 Jacobi 系统的额外消去

使用
[一阶框架续篇](R119-supplement-unscalarized-tail-frame-and-summable-remainder.md)
和 [真 hodograph 续篇](R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md)
的原对象。记
$$
 J=1+K+EU,\quad E=1+w^2,\quad
 D=1-w^2(2K+K^2+EP^2),\quad Q=V-P,
$$
$$
 d=\frac{EQ}{J},\qquad v=\frac{\sqrt D}{J},\qquad
 \mathsf T=\begin{pmatrix}1&0\\d&v\end{pmatrix},\qquad
 \mathsf C_0=\operatorname{diag}(-A-1,-2A).
 \tag{D.2}
$$
完整 raw Jacobi 未知量为 $\dot W=(\dot P,\dot K)^T$，source 单位
仍是 $\dot K_t-D F[\dot P,\dot K,\dot U,\dot V]=e$。
令 $Z=\mathsf T^{-1}\dot W$，前篇已准确得到
$$
 Z_t=(dI+v\mathsf B_0)Z_\theta+\mathsf Z Z+
                              \begin{pmatrix}0\\e/v\end{pmatrix}.
 \tag{D.3}
$$
其完整 $\mathsf Z$ 由前篇 (F.10) 给出。

对实际商式作代数约分，首先有
$$
 F_P=-2d-\frac{2Aw^2P}{J},\qquad
 F_K=-A\left[1+\frac{1-w^2P^2-Ew^2U^2}{J^2}\right]-\frac{d^2}{E}.
 \tag{D.4}
$$
再代入前篇的两个真 $d,v$ 时间恒等式，得到准确各项
$$
\begin{aligned}
 \mathsf Z_{11}&=d_\theta-A-1,&
 \mathsf Z_{12}&=v_\theta,\\
 \mathsf Z_{22}&=d_\theta-2A+\frac{2Aw^2U}{J},&
 \mathsf Z_{21}&=-Av_\theta
       -\frac{2Aw^2[(1+K)V+EPU]}{J\sqrt D}.
\end{aligned}
 \tag{D.5}
$$
例如在下左项中，先有
$$
 1-\left[1+\frac{1-w^2P^2-Ew^2U^2}{J^2}\right]
       -\frac{w^2-v^2}{E}
       =-\frac{2w^2(1+K)}{EJ}.
$$
原来可能产生无因子下左余项的 $-2d$、$dF_K$ 及 $d^3/E$
由此准确抵消。这里没有把任何一项仅因数值小而删除。

所以完整矩阵实际为
$$
 \boxed{\quad
 \mathsf Z=(dI+v\mathsf B_0)_\theta+\mathsf C_0+\mathsf G_0,
 \qquad
 \mathsf G_0=\frac{2Aw^2}{J}
   \begin{pmatrix}
     0&0\\
     -[(1+K)V+EPU]/\sqrt D&U
   \end{pmatrix}.
 \quad}                                                     \tag{D.6}
$$
(D.3) 因而是准确的散度系统。
尤其 $\mathsf G_0=0$ 在所有型别零点严格成立，不仅一阶 Taylor 为零。

## 2. 对两态作实际 density hodograph

沿用前篇的真实
$$
 c=\langle1/v\rangle^{-1},\qquad
 \chi_\theta=c/v,\quad \xi=\chi(t,\theta),\quad
 \theta=\Theta(t,\xi),\quad j_\chi=\Theta_\xi=(v/c)\circ\Theta ,
$$
以及 $b\circ\chi=cd/v-\chi_t$。本篇改用两态密度
$$
 Y=j_\chi(Z\circ\Theta),\qquad
 \mathsf G=\mathsf G_0\circ\Theta .
 \tag{D.7}
$$
不能把 (D.7) 与前篇不带 $j_\chi$ 的梯度函数 pullback 混用。

对一般 $Z_t=\partial_\theta(LZ)+CZ+F$，
直接微分 $j_\chi Z\circ\Theta$，使用
$(j_\chi)_t=\partial_\xi\Theta_t$，准确得到
$$
 Y_t=\partial_\xi\left[
       \frac{L\circ\Theta+\Theta_t I}{j_\chi}Y\right]
        +(C\circ\Theta)Y+j_\chi(F\circ\Theta).
$$
这里
$$
 \frac{L\circ\Theta+\Theta_t I}{j_\chi}=bI+c\mathsf B_0,\qquad
 j_\chi(e/v)\circ\Theta=c^{-1}e\circ\Theta.
$$
于是得到 (D.1)，包括全部时间 Jacobian 项和完整 source。

在宽2上，前篇实际四态界 $n(t)$ 给
$$
 \mathsf G=A
 \begin{pmatrix}0&0\\g_{21}&g_{22}\end{pmatrix},
 \qquad
 \|g_{21}\|_{\mathcal A_2}\le16w^2n,\quad
 \|g_{22}\|_{\mathcal A_2}\le4w^2n.
 \tag{D.8}
$$
这使用 $J^{-1},D^{-1/2}<2$ 以及
$\|(1+K)V+EPU\|<2n$；真角复合已由宽3到宽2的余量支付。

## 3. 所有转向频率共同的两态平衡

本节在同一**真实实背景**上工作，Jacobi 方向和 source 可以取复。
实性保证 $b$ 是实函数，这是下面输运能量恒等式的必要条件。

取任意正的径向尺度 $\varrho(t)>0$，在每个有限子区间上绝对连续。
定义 $\langle m\rangle=1+|m|$，对全部 $m\in4\mathbb Z$ 令
$$
 \omega_m(t)=
   \left(|A(t)|+\varrho(t)^2\langle m\rangle^{-2/3}\right)^{1/2},
 \qquad
 \mathsf D_m=\operatorname{diag}(\omega_m^{1/2},\omega_m^{-1/2}).
 \tag{D.9}
$$
$m=0$ 包含在内；独立的常高度平移仍另行保存。
这个结论允许实际 Airy 构造选择自己的径向尺度；没有假设
$\varrho_t$ 很小，也不删除 $\mathsf D_t$。它一直属于下面保留的
径向参考表达式。

以下有两个完整频率比值：
$$
 \omega_m\ge\sqrt{|A|},\qquad
 \left(\frac{\omega_n}{\omega_m}\right)^{1/2}
 \le\langle m-n\rangle^{1/6}.
 \tag{D.10}
$$
第二式由
$|\partial_x\log(\,|A|+\varrho^2(1+|x|)^{-2/3}\,)^{1/4}|
\le[6(1+|x|)]^{-1}$
及
$\langle m\rangle/\langle n\rangle\le\langle m-n\rangle$
得到；倒数的相同界也成立。

令 $\mathsf D$ 表示这个完整 Fourier 乘子。下左乘法项的矩阵核
带因子
$$
 \frac{|A|}{\sqrt{\omega_m\omega_n}}\le\sqrt{|A|}.
 \tag{D.11}
$$
下右乘法项只付 (D.10) 的六分之一次角权。
Young 不等式及 $\langle k\rangle^{1/6}\le e^{2|k|}$ 因而给
$$
 \boxed{\quad
 \|\mathsf D\mathsf G\mathsf D^{-1}\|_{\ell^2\oplus\ell^2\to
                                     \ell^2\oplus\ell^2}
 \le32w^2(1+|A|)n.
 \quad}                                                     \tag{D.12}
$$
常数与 $\varrho$、$A$ 和频率上界均无关。
在 $A=0$，左侧准确为0。特别没有把无因子下左常数乘上
$\omega_m^{-1}\sim|m|^{1/3}$ 后再假定其可求和。

## 4. 真实共同漂移在同一平衡中的能量界

令 $d_m$ 表示 $\mathsf D$ 的任意一个对角分量。对实 $b$，
算子 $S_b=\partial_\xi(b\,\cdot)$ 的平衡后 Hermitian 部分矩阵核为
$$
 \frac{i}{2}\widehat b(m-n)
       \left(m\frac{d_m}{d_n}-n\frac{d_n}{d_m}\right).
 \tag{D.13}
$$
这包括 divergence 中的 $b_\xi$，没有将其遗漏。
若 $k=m-n$，则
$$
 \left|m\frac{d_m}{d_n}-n\frac{d_n}{d_m}\right|
 \le5|k|\langle k\rangle^{1/6}.
 \tag{D.14}
$$
证明分两种准确情形。若 $|n|\le2|k|$，写成
$k(d_m/d_n)+n(d_m/d_n-d_n/d_m)$，直接使用 (D.10) 得到右侧。
若 $|n|>2|k|$，沿频率区间的对数导数给
$|\log(d_m/d_n)|\le|k|/(3|n|)<1/6$。
$e^{1/6}<6/5$ 因而给
$|n||d_m/d_n-d_n/d_m|<|k|$，第一项也小于 $2|k|$，
比 (D.14) 更强。$k=0$ 的 Hermitian 核准确为0。

因 $|k|\langle k\rangle^{1/6}\le e^{2|k|}$，
完整卷积及 (D.13)–(D.14) 给
$$
 \left|\operatorname{Re}\langle W,\mathsf D S_b\mathsf D^{-1}W\rangle\right|
 \le3\|b\|_{\mathcal A_2}\|W\|_{\ell^2\oplus\ell^2}^2.
 \tag{D.15}
$$
对角的两个权都满足同一证明，所以没有遗漏任一 Airy 分支或 mean。
该结论只是实际输运的能量控制；它不宣称 $S_b$ 本身是有界零阶
算子，更不宣称其传播与恒等之间同宽 operator norm 很小。

## 5. 实际全尾的平方能量余量

置 $W=\mathsf D Y$、$\mathcal E=\|W\|^2$。在有限真子区间上，
(D.1) 的完整能量恒等式是
$$
\begin{aligned}
 \mathcal E_t={}&
 2\operatorname{Re}\left\langle W,
 [\mathsf D_t\mathsf D^{-1}
   +c\mathsf D\mathsf B_0\partial_\xi\mathsf D^{-1}
   +\mathsf C_0]W\right\rangle\\
 &+\mathcal Q_{\rm pert}(t,W)
 +2\operatorname{Re}\left\langle W,\,
   \mathsf D\begin{pmatrix}0\\c^{-1}e\circ\Theta\end{pmatrix}\right\rangle .
\end{aligned}
 \tag{D.16}
$$
所有径向参考项和真实标量速度 $c(t)$ 都在第一行保留。
由 (D.12)、(D.15) 及前篇
$\|b\|_{\mathcal A_2}\le32(1+|A|)n$，
$$
 |\mathcal Q_{\rm pert}(t,W)|
 \le[6\|b\|_{\mathcal A_2}+64w^2(1+|A|)n]\mathcal E
 \le256(1+|A|)n\,\mathcal E .
 \tag{D.17}
$$
对同一真实无限尾，前篇已证明
$\int(1+|A|)n\,dt<2^{-435}X_{224}$，所以
$$
 \boxed{\quad
 \int 256(1+|A|)n\,dt<2^{-427}X_{224}.
 \quad}                                                     \tag{D.18}
$$
该式覆盖每个无限 log-quintic 层、整个 connector 及固定双 bump，
不是只对一个模型转向圈取极限。

任一在第一行的**同一**径向表达式上已经证明的能量不等式，可加上
(D.17) 后使用 Gronwall；额外平方能量因子至多
$\exp(2^{-427}X_{224})$。这不是将原径向 propagator 的 operator
norm 与真实 propagator 直接作相对相减的结论。
在正型区，第一行仍有真正的椭圆 Cauchy 增长，(D.18) 不提供缺失的
Ai/Bi 边界 Green 或适合该 Green 的全部 source norm。

具体 source norm在这里是
$$
 \left\|\omega_m^{-1/2}
        \bigl(c^{-1}e\circ\Theta\bigr)_m\right\|_{\ell^2_m}.
 \tag{D.19}
$$
它包含 mean 和转向处的六分之一次角权，没有把普通源当成端口
跳量，也没有把该权免费改成无权 $L^2$。

## 6. 密度两态下的 mean、真实迹及物理配对

由 (D.7) 反变换，
$$
 \dot P\circ\Theta=j_\chi^{-1}Y_1,\qquad
 \dot K\circ\Theta=j_\chi^{-1}
                  [(d\circ\Theta)Y_1+(v\circ\Theta)Y_2].
 \tag{D.20}
$$
因此这次的准确 mean 公式变成
$$
 \langle\dot P\rangle_\theta=\langle Y_1\rangle_\xi=0,\qquad
 \dot K_0=
   \langle(d\circ\Theta)Y_1+(v\circ\Theta)Y_2\rangle_\xi .
 \tag{D.21}
$$
从 (D.1) 第一行直接积分也得到
$\partial_t\langle Y_1\rangle=-(A+1)\langle Y_1\rangle$；
它与高度相容条件完全一致。
物理平均高度仍按
$\partial_t(\dot z)_0=aw\,\dot K_0$ 积分，并带独立 $\dot\lambda$。

设 $\widehat e_2=c^{-1}e\circ\Theta$。真实 holonomy 行进一步简化为
$$
 \boxed{\quad
 (\dot M)_t=w^2\langle(D^{-1}\circ\Theta)\widehat e_2\rangle .
 \quad}                                                     \tag{D.22}
$$
因为 $j_\chi\rho J e\circ\Theta=(vJ\rho)\circ\Theta\,\widehat e_2$
且 $vJ\rho=D^{-1}$。它保留完整非径向源产生的 mean 负荷。
对实际标签微分，$e=0$，所以原 $\dot M=0$ 全程保持。

本篇 $Y$ 是两个相对梯度分量的密度，不把 $\int Y_1Y_2$ 称作物理
两迹配对。真实 grounded 高度、conormal 和 ordinary 密度源仍须用
前篇的
$\widehat f=f\circ\Theta$、
$\widehat p=j_\chi p\circ\Theta$、
$\widehat s=j_\chi s\circ\Theta$。
这组变换才保留 $\int fp$、mean flux 和 source mean。
normal/shear、水平重建及完整高模均通过原准确公式恢复。

## 7. 剩余真实相位与完整边界逆

(D.6)–(D.18) 支付了任意小矩阵估计不能支付的转向权：
下左项的准确 $A$ 因子及 principal 散度结构使全频 Airy 平衡合法，
同时保留实际 common drift 的完整输运。

剩下仍须把该真一阶表达式的负型射线、正型 Ai/Bi 连接和全部源
组装成同一完整 return，并证明与真实长段 DN 的高输入相对横截。
前篇已证明真第四标签会改变 cut128 的 $c$；这不是最终 return
旋转数的计算。当前结果既没有假定主相位不变，也没有暗中重新选
背景度量或两个 bump 参数。

[准确恒等式及门程序](../scripts/fourfold_divergence_turning_energy_20261113.py)
和 [报告](../notes/2026-11-13-R119-divergence-turning-energy-budget.json)
记录全部代数核验与实际无限求和预算。
