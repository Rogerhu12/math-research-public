# R158：权负二 PSD 秩一边界上的完整 null 曲线判据

日期：2026-11-15。**已证明。** 纯纸面推导，没有新 profile 评价、原式归约或研究计算。

依据 [R141](R141-affine-character-acceleration-covariance-and-J-positivity.md)、[R148](R148-sharp-one-dimensional-highest-action-positivity.md) 和 [R155](R155-complete-highest-action-curve-Sturm-Liouville-equivalence.md)。本稿给出 R141 加速度 PSD 锥的一个**秩一边界**上的准确必要门：完整最高 action 在全部真实 null 方向路径上的非负性，恰等价为一个逐状态四次系数非负。所有面积项和 $\widehat Q_4$ 均保留；没有计算或假定这些未知完整四次系数的符号。

它不处理 $a_0>0$ 的内部，也不证明整个最高 action 或完整实际成本的正性。

## 1. 完整系数与明确的边界假设

令 $\lambda$ 为 R141 的实仿射字符，满足

$$
\lambda(R)=0,\qquad
\lambda\circ\mathsf P_{H,d}=H^{-2}\lambda
\quad(H>0).
\tag{1}
$$

若 $\lambda$ 还非负于真实闭成本锥，R137/R140 已保证它的完整最高层在所有真实开平端路径上非负，并给加速度逐状态 PSD。以下首先只使用 (1) 产生的实系数；对正泛函的应用在第6节说明。

令

$$
S=(h,k,\omega),\quad h>0,\qquad
u=h_s,\ w=k_s,\ a=h_{ss},\ b=k_{ss},\qquad
\omega_s=\frac{w}{2h}.
\tag{2}
$$

R141 的完整加速度与面积系数是

$$
A_{hh}=h^{-4}(a_0+a_2k^2),\qquad
A_{hk}=h^{-3}b_1k,\qquad
A_{kk}=h^{-2}c_0,
\tag{3}
$$

$$
H_1=h^{-4}p_1k,\qquad H_2=h^{-3}q_0.
\tag{4}
$$

其中 $A_{hk}$ 是 action 中 $ab$ 的系数，对称矩阵的非对角项为 $A_{hk}/2$。六常数按 R141 为

$$
(a_0,a_2,b_1,c_0,p_1,q_0)
=(\lambda J_0,\lambda J_1,\lambda J_4,
  \lambda J_6,\lambda J_7,\lambda J_9).
$$

本稿只取以下边界：

$$
\boxed{a_0=0,\qquad c_0>0,\qquad 4a_2c_0=b_1^2.}
\tag{5}
$$

置

$$
\beta=\frac{b_1}{2c_0},\qquad a_2=c_0\beta^2.
\tag{6}
$$

于是加速度二次型准确因式化为

$$
A_{hh}a^2+A_{hk}ab+A_{kk}b^2
=c_0h^{-2}\left(b+\frac{\beta k}{h}a\right)^2.
\tag{7}
$$

它在每个 $h>0$ 状态上恰为秩一 PSD；即使 $k=0$ 也仍有 $c_0h^{-2}>0$ 的一维方向。

完整最高层仍为

$$
L_4^\lambda
=c_0h^{-2}\left(b+\frac{\beta k}{h}a\right)^2
+(H_1u+H_2w)(ub-wa)
+\widehat Q_4^\lambda(S;u,w),
\tag{8}
$$

其中

$$
\widehat Q_4^\lambda
=\lambda\!\left(Q_4^v-D_0P_{3v}-\mathcal B_{m_2}(N_2)\right).
\tag{9}
$$

式 (9) 完整保留未归约 $N_2$、三阶势的真实水平状态导数，以及所有速度四次项。这里 $D_0$ 是 R129 的水平微分算子，不能与 R150/R153 的轴系数 $\mathcal D_0$ 混淆。

## 2. 全部真实 null 方向状态曲线

加速度矩阵的核方向可写成

$$
V_\beta(S)=\left(1,-\frac{\beta k}{h}\right).
\tag{10}
$$

以 $h$ 本身为曲线参数，解

$$
\frac{dk}{dh}=-\frac{\beta k}{h},\qquad
\frac{d\omega}{dh}=\frac1{2h}\frac{dk}{dh}.
\tag{11}
$$

任意给定初始状态 $(h_0,k_0,\omega_0)$，取 $K=k_0h_0^\beta$，则

$$
k(h)=Kh^{-\beta}.
\tag{12}
$$

真实 $\omega$ 原函数必须分两种写法：

- 若 $\beta\ne-1$，
  $$
  \omega(h)=\omega_0+
  \frac{\beta K}{2(\beta+1)}
  \left(h^{-\beta-1}-h_0^{-\beta-1}\right).
  \tag{13}
  $$
- 若 $\beta=-1$，
  $$
  k(h)=Kh,\qquad
  \omega(h)=\omega_0+\frac K2\log\frac h{h_0}.
  \tag{14}
  $$

特别 $\beta=0$ 时 (13) 正好给 $k,\omega$ 同时恒定。任意实 $\beta$ 的幂在 $h>0$ 上光滑；(14) 的 log 是实际水平约束的原函数，不是省略的端口常数。

这些曲线通过每个 $h>0$ 的状态。若固定物理带要求 $\xi+\omega$ 留在同一非零分支，给定状态后只取足够小的紧 $h$ 子区间，其曲线像仍在所选开物理状态域中；后面的重参数不会扩大此像。

更一般，设一条真实路径的速度处处在这个核中：

$$
w=-\frac{\beta k}{h}u.
\tag{15}
$$

则

$$
\frac d{ds}(kh^\beta)
=h^\beta w+\beta kh^{\beta-1}u=0.
$$

因此整条连通路径具有同一个常数 $K$，并由 (12)–(14) 复合其实际 $h(s)$ 得到。这里没有除以 $u$，所以允许 $u=0$、任意多次转向和累积静止点，不存在穿过零速度时更换曲线常数的缺口。

## 3. 完整 action 的逐点约化

沿 (12) 的真实路径，以 $h(s)$ 为任意光滑重参数。直接求导得

$$
w=-\frac{\beta k}{h}u,\qquad
b=-\frac{\beta k}{h}a+
\frac{\beta(\beta+1)k}{h^2}u^2.
\tag{16}
$$

所以加速度平方项是

$$
c_0h^{-2}\left(b+\frac{\beta k}{h}a\right)^2
=c_0\beta^2(\beta+1)^2k^2h^{-6}u^4.
\tag{17}
$$

面积因子没有被删除。式 (16) 给

$$
ub-wa=\frac{\beta(\beta+1)k}{h^2}u^3,
\qquad
H_1u+H_2w=(p_1-\beta q_0)kh^{-4}u.
\tag{18}
$$

因而全部面积贡献为

$$
\beta(\beta+1)(p_1-\beta q_0)k^2h^{-6}u^4.
\tag{19}
$$

最后，$\widehat Q_4^\lambda$ 对 $(u,w)$ 是齐次四次式，因此

$$
\widehat Q_4^\lambda(S;u,w)
=\widehat Q_4^\lambda\!\left(S;1,-\frac{\beta k}{h}\right)u^4.
\tag{20}
$$

定义准确的逐状态量

$$
\boxed{
E_\beta(S)=
\widehat Q_4^\lambda\!\left(S;1,-\frac{\beta k}{h}\right)
+\frac{\beta(\beta+1)k^2}{h^6}
\left[c_0\beta(\beta+1)+p_1-\beta q_0\right].
}
\tag{21}
$$

由 (17)–(20) 得到**逐点**恒等式

$$
\boxed{L_4^\lambda(S(s))=E_\beta(S(s))\,h_s^4.}
\tag{22}
$$

不需要额外分部积分、单调性或端点极限。即使 $h_s=0$，(16)–(22) 仍逐点成立。原正规化边界势已由 R129 的平端条件支付；(22) 没有引入新的边界项。

若把完整 quartic 写为

$$
\widehat Q_4^\lambda(S;u,w)=
\sum_{j=0}^{4}Q_j(S)u^{4-j}w^j,
$$

则 (21) 的第一项就是

$$
\sum_{j=0}^{4}Q_j(S)
\left(-\frac{\beta k}{h}\right)^j.
\tag{23}
$$

(23) 明确保留全部五项；本稿没有给其中任何一项预置符号、常值或零值。

## 4. 受限路径类上的必要充分定理

令 $\mathscr D\subset\{h>0\}$ 为开状态域，全部系数在其中光滑，满足 (3)–(6)。以下两条等价：

1. 对每条有限时间、两个端部开邻域 scalar 常值、像在 $\mathscr D$ 内、满足真实水平约束 (2) 和 null 速度条件 (15) 的光滑路径，
   $$
   \int L_4^\lambda\,ds\ge0.
   \tag{24}
   $$
2. 每个 $S\in\mathscr D$ 都满足
   $$
   \boxed{E_\beta(S)\ge0.}
   \tag{25}
   $$

**充分性。** 由 (22)，被积式为非负状态函数乘 $h_s^4$，直接得到 (24)。不需要把路径分成有限多个单调弧，故任意多次转向和零速度集合也全部覆盖。

**必要性及真实有限平端实现。** 若 $E_\beta(S_0)<0$，通过 $S_0$ 取第2节的真实曲线。由连续性可选紧区间 $[\alpha,\gamma]$，其曲线像在 $\mathscr D$ 内且全部满足 $E_\beta\le-\varepsilon<0$。

取标准光滑非负函数

$$
\eta(s)=
\begin{cases}
\exp[-1/(s(1-s))],&0<s<1,\\
0,&\text{其余},
\end{cases}
$$

并在 $0\le s\le1$ 设

$$
h(s)=\alpha+(\gamma-\alpha)
\frac{\int_0^s\eta(t)\,dt}{\int_0^1\eta(t)\,dt}.
\tag{26}
$$

再于 $s\le0$、$s\ge1$ 分别延拓成常数。它是 $C^\infty$，在两个端点全平。若要求端部是**开区间**常值而不只是全平，将参数区间取为 $[-1,2]$ 即可；曲线在 $[-1,0]$ 和 $[1,2]$ 分别恒定。

令 $k,\omega$ 严格按 (12)–(14) 与 (26) 复合。得到真实有限总时长3的水平平端路径。其状态像仍为已选紧曲线段，且 $h_s>0$ 在 $(0,1)$。于是

$$
\int L_4^\lambda\,ds
=\int E_\beta(S(s))h_s^4\,ds
\le-\varepsilon\int_0^1h_s^4\,ds<0,
$$

矛盾。这里没有无限时间逼近、未支付的 end cap 或把 $\omega$ 重新固定。

## 5. 与 R155 的一致性及特殊参数

沿以 $h$ 为参数的曲线，

$$
V=\left(1,-\frac{\beta k}{h}\right),\qquad
A=\left(0,\frac{\beta(\beta+1)k}{h^2}\right).
$$

因为 $\mathsf A V=0$，R155 的两个导数系数准确为

$$
a_\Gamma=V^T\mathsf A V=0,\qquad
b_\Gamma=2V^T\mathsf A A=0.
$$

因此其完整 Sturm 势为

$$
e_\Gamma=c_\Gamma=E_\beta(\Gamma(h)).
$$

R155 的二次型退化为 $\int e_\Gamma\psi^2\,dh$；其非负性恰等价于 (25)。第4节同时给出了不借助一般 Sturm 逼近的直接有限平端实现。

两种特殊参数进一步核对全部面积项：

- $\beta=0$：null 曲线 $k,\omega$ 恒定，$\beta(\beta+1)=0$，所以条件为
  $$
  \widehat Q_4^\lambda(S;1,0)\ge0.
  \tag{27}
  $$
- $\beta=-1$：null 曲线 $k=Kh$，$\omega$ 为 (14) 的真实 log；虽然 $\omega$ 一般不恒定，曲线在 $(h,k)$ 平面为直线，仍有 $\beta(\beta+1)=0$。条件为
  $$
  \widehat Q_4^\lambda(S;1,k/h)\ge0.
  \tag{28}
  $$

任意 $\beta$ 在 $k=0$ 上也退化为 (27)。由于本稿假设 $a_0=\lambda J=0$，这与 R148 在该轴给出的必要条件 $\lambda\mathcal D_0\ge0$ 一致；一致性不是 D0 原式已归零或成本可调的证明。

## 6. 对真实正性障碍的范围

若 $\lambda$ 是真实闭成本锥的权 $-2$ 正字符，R137/R140 已经通过真实补偿与时间缩放支付了全部开平端路径的最高层非负。因此只要其加速度常数落在 (5)，它必须满足 (21)、(25)。

第4节使用的开路径本身未被宣称有 $M=T=0$、frame 闭合或空间位置闭合；从真实闭成本正性到这些开路径最高层必要门，正是 R137/R140 的已证步骤。不能跳过该步骤直接把一段 null 曲线当成已构造的完整闭成本。

反向只证明 **null 速度路径类** 的最高 action 非负；它不保证非 null 路径、全部最高层、$L_0,L_2$ 和统一矩阵乘子组成的完整 action 非负。

尤其：

- (5) 是 PSD 锥的特定秩一边界；没有证明每个正字符必须落在这里。
- $a_0>0$、$4a_2c_0>b_1^2$ 或 $c_0=0$ 等其他情形不由本稿覆盖。
- 未知 $\widehat Q_4$ 必须完整出现于 (21)，不能仅凭加速度退化把它或面积项删掉。
- 没有新增响应成员、真实商维数、lineality 或实际多查询控制，也没有解决完整周期/ruling 与有限等距族。
