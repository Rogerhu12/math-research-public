# R117：真实高度两 jet 到 Codazzi 尾端口、参数切线与轴向切口接合

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

**状态：下面的端口恒等式、固定 g 参数切线、C² 切口刚体对应和 D2 轴向结论均已证明。**
代码已消费一个保存的真实非线性旧尾包，核对了其 Fourier、均值和镜像约定。
这不是新强目标尾的求解，也不把有限 DN 包的形式曲率替代实际 Cartesian metric。

## 1. 固定目标、完整高度与定向

固定

$$
g=ds^2+a(s)^2du^2.
$$

在上半尾切口令 $r=a(s)>0$、$v=a'(s)<0$、$A=a''(s)$。
若原径向背景为 $E(r)=1+w(r)^2$，则

$$
v=-E^{-1/2},\qquad A=-\frac{E_r}{2E^2}.
\tag{1}
$$

这些是同一固定 g 的数据；对尾的物理高度系数求参数导数时不改变它们。
材料角是 u。设完整物理高度为 $z=z(r,u)$，取

$$
e_1=X_s,\quad e_2=X_u/r,\quad N=e_1\times e_2.
$$

原正 w worker 的完整高度记为 H；上半图采用 $z=-H+$ 一个常数。
在当前定向和保持平面正定向的竖直图支路上，$N_z<0$。
这是与 R116 的中央 $e_1=e_z,N=e_z\times T,n>0$ 连续相容的上半尾支路。

### 定理 1：高度到第二基本形式

若 X 是这个 g 的 C² 等距浸入，且

$$
D_z=1-v^2z_r^2-z_u^2/r^2>0,
\qquad N_z=-\sqrt{D_z},
$$

则正交标架中的第二基本形式准确为

$$
\boxed{
l=\frac{v^2z_{rr}+Az_r}{N_z},\qquad
m=\frac{(v/r)(z_{ru}-z_u/r)}{N_z},\qquad
n=\frac{z_{uu}/r^2+(v^2/r)z_r}{N_z}.}
\tag{2}
$$

**证明。** 把竖直单位向量在正交标架中分解：

$$
e_z=(vz_r)e_1+(z_u/r)e_2+N_zN.
$$

取范数平方给 $N_z^2=D_z$；负支由定向选定。
Gauss 公式的 z 分量给

$$
\operatorname{Hess}_g z=N_z\,\mathrm{II}.
\tag{3}
$$

非零 Christoffel 符号为
$\Gamma^u_{su}=v/r$、$\Gamma^s_{uu}=-rv$。
又 $z_s=vz_r$，所以

$$
\begin{aligned}
(\operatorname{Hess}_g z)_{ss}&=v^2z_{rr}+Az_r,\\
(\operatorname{Hess}_g z)_{su}&=v(z_{ru}-z_u/r),\\
(\operatorname{Hess}_g z)_{uu}&=z_{uu}+rv^2z_r.
\end{aligned}
$$

分别除以 $N_z,rN_z,r^2N_z$ 就得到 (2)。只用到 C²。证毕。

若只有有限数值尾图，代码仍可计算 (2)，但应称为针对目标 g 的**形式端口值**。
实际诱导度量 h 不等于 g 时，准确公式是

$$
(\operatorname{Hess}_g z)_{ij}
=N_z^{\rm actual}\mathrm{II}^{\rm actual}_{ij}
+(\Gamma(h)^k_{ij}-\Gamma(g)^k_{ij})z_k.
$$

因此不能只凭 (2) 小残差或 Gauss 残差就宣称实际 Cartesian 两 jet 已匹配。
这没有增加新验收门；它保留原来的实际 E、F、G 和接缝检查对象。

## 2. 实际 worker 的 Fourier 与均值排列

`createCompactTailDN` 的 `cutJets` 输出

$$
\begin{aligned}
H(r_c,u)&=H_0+\sum_{j=1}^M h_j\cos(k_ju),\\
H_r(r_c,u)&=\overline H_r+\sum_{j=1}^M p_j\cos(k_ju),\\
H_{rr}(r_c,u)&=\overline H_{rr}+\sum_{j=1}^M q_j\cos(k_ju),
\qquad k_j=\mathrm{spacing}\,j.
\end{aligned}
\tag{4}
$$

实际字段对应为 `height`、`slope`、`second`、`meanSlope`、`meanSecond`。
**完整均值已含背景**：

$$
\overline H_r=w+\mathrm{meanSlopeCorrection},\qquad
\overline H_{rr}=w_r+\mathrm{meanSecondCorrection}.
$$

从 (4) 求 $H_u,H_{ru},H_{uu}$ 后，所有高度 jet 一起乘 −1，得到上半 z 的 jet。
`height` 直接乘 $\cos(k_ju)$，**没有额外 $\sqrt2$**。
worker 在内部归一化动量转回 `slope/second` 时已使用自己的 $\sqrt2$ 因子；外部不能再乘。
这由本题 `fd2d-bounded-tail-stage-core.mjs::cutJets` 和已保存的
`f6tail_relative_spatial_jets.mjs` 直接读出。
后者的 V 是相对旋转背景的扰动；如果改用它的相对 V jet，必须另加背景。
本文 consumer 用完整 `cutJets` 均值，避免把相对 jet 当完整 jet。

高度常数 $H_0$ 不出现在 (2)。它只控制最后的竖直平移，不能帮助消掉 n,m 的失配。
代码重新计算 $D_z$；worker 自己叫作 `minD` 的归一化动量量不是这里的 $D_z$。

## 3. 固定 g 的准确参数 JVP

以点表示参数方向导数，所有 $r,v,A$ 固定。
由 $N_z^2=D_z$ 得

$$
\boxed{\dot N_z=-\frac{v^2z_r\dot z_r+z_u\dot z_u/r^2}{N_z}.}
\tag{5}
$$

于是

$$
\begin{aligned}
\dot l&=\frac{v^2\dot z_{rr}+A\dot z_r}{N_z}-l\frac{\dot N_z}{N_z},\\
\dot m&=\frac{(v/r)(\dot z_{ru}-\dot z_u/r)}{N_z}-m\frac{\dot N_z}{N_z},\\
\dot n&=\frac{\dot z_{uu}/r^2+(v^2/r)\dot z_r}{N_z}-n\frac{\dot N_z}{N_z}.
\end{aligned}
\tag{6}
$$

这些是 (2) 的直接链式求导。
对应的 Gauss 残差导数是
$\dot l\,n+l\dot n-2m\dot m$；$K=-A/r$ 的导数为零。

worker 的 `heightJetJacobian` 按行主序 reshape 为 $(3M+2)\times M$。
列是**物理切口高度 Fourier 系数** $h_j$，不是内部 $h_j/r_c^4$。
行顺序为

| 行 | 导数对象 |
|---|---|
| $0,\ldots,M-1$ | slope |
| $M,\ldots,2M-1$ | second |
| $2M$ | meanSlopeCorrection |
| $2M+1$ | meanSecondCorrection |
| $2M+2,\ldots,3M+1$ | height |

因为背景不变，两个 mean correction 的导数也就是完整均值的导数。
把这个矩阵乘方向，再按 (4) 和 (5)–(6) 计算，即得尾 n,m 的方向导数。
当前 worker 的高度 jet Jacobian 最后一步采用有限差分；本文证明的是后续代数链，
不会把上游有限差分自动变成准确无限维 DN 导数。

若 $R=(n_{\rm prefix}-n_{\rm tail},m_{\rm prefix}-m_{\rm tail})$，则

$$
\dot R=(\dot n_{\rm prefix}-\dot n_{\rm tail},
         \dot m_{\rm prefix}-\dot m_{\rm tail}).
$$

prefix 切线由 R116(10) 推进；尾切线用 (5)–(6)。
无须为这一边界残差改变 g 或数值微分中央参数所对应的目标度量。

## 4. 共用计算角与镜像符号

允许任何固定、与未知参数无关的正向计算角 $u=U(\xi)$，记 $\chi=U'>0$。
则 $b=a\chi$，并且 $e_2=X_\xi/b=X_u/a$。
因此 l,m,n 是同一正交标架的标量：**只复合 $u=U(\xi)$，不再乘 $\chi$**。
原始坐标第二基本形式则是
$\mathrm{II}_{s\xi}=bm$、$\mathrm{II}_{\xi\xi}=b^2n$。
PDE 用 $b^{-1}\partial_\xi$；尾 Fourier 仍是材料 u 的 Fourier。

若拿到的是 $z_\xi,z_{r\xi},z_{\xi\xi}$ 而非 worker 材料 jet，须先变为

$$
z_u=z_\xi/\chi,\quad z_{ru}=z_{r\xi}/\chi,\quad
z_{uu}=z_{\xi\xi}/\chi^2-z_\xi\chi'/\chi^3.
$$

换计算角不改变物理目标，也不允许把 $\cos(k_ju)$ 直接改成 $\cos(k_j\xi)$。
原椭圆 θ、固定 balanced seed 法向角 φ 等，只要 U 固定都适用。

### 两种镜像约定不能混同

设 $J_z=\operatorname{diag}(1,1,-1)$。
若保持同一个向外走的半图参数 s，反射为 $\widetilde X(s,u)=J_zX(s,u)$，则

$$
\widetilde N=\det(J_z)J_zN=-J_zN,
\qquad \widetilde N_z=N_z,
\qquad (\widetilde l,\widetilde m,\widetilde n)=(-l,-m,-n).
\tag{7}
$$

这正是代码将完整高度 jet 乘 −1、保持相同 v 和 $N_z$ 支路时的变化。
若改用从下半经中央到上半的**统一有符号材料坐标 σ**，下半还须把半图 s 反向。
此时

$$
X(-\sigma,u)=J_zX(\sigma,u),\quad
N(-\sigma,u)=J_zN(\sigma,u),
$$

故 l,n 为偶，m 为奇：

$$
l(-\sigma,u)=l(\sigma,u),\quad
m(-\sigma,u)=-m(\sigma,u),\quad
n(-\sigma,u)=n(\sigma,u).
\tag{8}
$$

两次定向变化的 determinant 因子都已计入。不能只翻高度后沿用错误的 N 号。

## 5. 同 n,m 的切口究竟匹配了什么

### 定理 2：同 g、n,m 给完整切口两 jet 的一个 proper 刚体对应

设两个 C² 等距片在同一切口 $s=s_c$ 使用同一材料 u、同一 g、同一定向标架。
假设两者的 n,m 沿整圈相同，且 n 不为零。
则存在一个与 u 无关的 $Q\in SO(3)$ 和 $c\in\mathbb R^3$，使两片在切口的
位置、全部一 jet 和全部二 jet 都由 $X_1=QX_2+c$ 对应。

**证明。** 令 $F_i=(e_{1,i},e_{2,i},N_i)$。
两者的角向结构方程为

$$
(F_i)_u=F_iB,\qquad
B=\begin{pmatrix}
0&-v&-rm\\v&0&-rn\\rm&rn&0
\end{pmatrix}.
\tag{9}
$$

在一点 $u_0$ 取 $Q=F_1(u_0)F_2(u_0)^T$。
两标架均正定向正交，故 $Q\in SO(3)$。
$F_1-QF_2$ 满足齐次线性 ODE $D_u=DB$，且在 $u_0$ 为零，故整圈为零。
$X_{1,u}-QX_{2,u}=r(e_{2,1}-Qe_{2,2})=0$，因此位置只差常量 c。
再由

$$
X_s=e_1,\quad X_{su}=ve_2+rmN,\quad
X_{uu}=-rve_1+r^2nN,\quad X_{ss}=lN
\tag{10}
$$

以及共同 Gauss 式 $l=(m^2+K)/n$，得到全部两 jet 的对应。证毕。

这里不要求曲线非平面；一点完整定向标架已唯一确定 Q。
C² 情形的 Gauss 式也不需要追加 C³：C¹ 标架的混合偏导在分布意义交换，
平坦性方程给出的 Gauss 分量只含连续的 $a'',ln,m^2$，所以该等式逐点成立。

定理没有说 Q 自动保持固定帽的轴。没有轴向对称时，Q 可以把圆 cuff 倾斜；
这正是下一条对本问题的作用。

### 定理 3：共同半周对称排除 cuff 的倾斜

再假设两片在同一角标签下准确满足

$$
X_i(u+\pi)=SX_i(u),\qquad F_i(u+\pi)=SF_i(u),\qquad
S=\operatorname{diag}(-1,-1,1).
\tag{11}
$$

则定理 2 中 $QS=SQ$，$c=Sc$。因此 c 只能竖直，且 $Qe_z=\pm e_z$。

**证明。** 用 $F_1=QF_2$ 分别在 u 和 $u+\pi$ 代入 (11)，得
$QSF_2=SQF_2$。F2 可逆，故 Q 与 S 交换。
再把位置等式代入 (11)，立刻得到 $c=Sc$。
S 的一维 +1 特征空间是竖直轴，Q 保持它，故 $Qe_z=\pm e_z$。证毕。

若在一个切口点两侧 $N_z$ 同为非零负数，则负号被排除，$Qe_z=e_z$。
所以 Q 只绕竖直轴旋转，接入同轴圆 cuff 与固定帽不会产生倾斜。
若还共同满足 $P=\operatorname{diag}(1,-1,1)$ 的反射
$X(-u)=PX(u)$，其正确 frame 关系是

$$
F(-u)=PF(u)\operatorname{diag}(1,-1,1).
$$

同理可得 $QP=PQ$。此时在已选上半分支，Q 只能为 I 或 S。
这剩余的固定离散轴向规范可由一个切口点的 x 朝向选定。
以上只处理一次固定候选的刚体规范，没有让帽随时间旋转。

高度常数、整体平移和 proper 整体转动不改变 l,m,n；
但高度表达式中的 $N_z$ 必须仍按该图实际定向取支。
切口的竖直平移最后由一个实际位置对齐，不能以它代替边界的 n,m 方程。

## 6. 有限失配的直接切口估计

这是一维角向接缝误差的可用预算，不是假设数值残差为零。
设两条真实定向切口标架使用同一 r,v，

$$
\epsilon=\sup_u\sqrt{(m_1-m_2)^2+(n_1-n_2)^2}.
$$

仍在一点对齐 Q,c。因为 (9) 的 B 反对称，角向齐次传播的算子范数为 1，
且 $\|B_1-B_2\|_{\rm op}=r\sqrt{(m_1-m_2)^2+(n_1-n_2)^2}$。
沿长度为 t 的角弧积分，得到

$$
\|F_1-QF_2\|\le rt\epsilon,\qquad
|X_1-QX_2-c|\le\tfrac12r^2t^2\epsilon.
\tag{12}
$$

若两片都真实闭合，可对每点选较短弧，取 $t\le\pi$。
没有指数放大因子。
记 $D=rt\epsilon$、$\delta m=m_1-m_2$、$\delta n=n_1-n_2$，由 (10) 又得

$$
\begin{aligned}
|\Delta X_s|&\le D,\\
|\Delta X_{su}|&\le(|v|+r|m_1|)D+r|\delta m|,\\
|\Delta X_{uu}|&\le(r|v|+r^2|n_1|)D+r^2|\delta n|,\\
|\Delta X_{ss}|&\le|l_1|D+|\delta l|.
\end{aligned}
$$

若 $n_1\ne0$，共同 Gauss 方程还给

$$
|\delta l|\le
\frac{(|m_1|+|m_2|)|\delta m|+|l_2||\delta n|}{|n_1|}.
$$

这只控制切口值和两 jet；它不自动修正非零接缝，也不替代两片内部的 metric 或 reach。

## 7. 已交付代码和真实小核验

`scripts/fd2d_metric_tail_gc_port.py`，SHA256
`2c9476d79db0260ddc423774b1f29b9176019851f35252b511b3c3c4d725fc95`，提供

```python
port = TailGCJetPort.from_worker_record(record)
tail = port.evaluate(material_u)
tail_direction = port.jvp(material_u, physical_height_direction)
```

`evaluate_in_chart`、`jvp_in_chart` 只复合一个固定 $u=U(\xi)$。
`target_jet=(r,v,A)` 可显式指定 prefix 的固定切口 jet，返回对象另保留它与 worker 背景的差；
不能把这项差静默当作零。
没有 DN Jacobian 的包不会伪造它；可用 `jvp_from_jet_direction` 消费明确的 jet 方向。

检查源码 `scripts/fd2d-metric-tail-gc-port-check.py`，SHA256
`38cd2064ef09debadb461859043cfdf771a1a9fd6fdf79ed19aad47b382b02bb`。
实际报告 `2026-11-12-fd2d-metric-tail-gc-port-check-01.json`，SHA256
`595b48e9680cc8e33c693d6aba9b35712fd8781244e86522d46adf22e430028a`。
真实运行自然 exit 0，未另起 tail worker 或重做 BVP。

1. 非零 m 的准确局部检查取 catenoid–helicoid 关联片。
   令 $r^2=s^2+c^2,s<0$，高度
   $z=\cos\alpha\,c\operatorname{arsinh}(s/c)+\sin\alpha\,cu$。
   准确 $l=-c\cos\alpha/r^2,m=-c\sin\alpha/r^2,n=c\cos\alpha/r^2$。
   (2) 的最大误差小于 $1.1\times10^{-19}$，两种镜像规范的符号差均为零。
   这是一个局部代数核验，不称闭曲面。
2. 把半径 2 的球片作 proper 倾斜旋转，再平移高度 17。
   (2) 仍给 $l=n=1/2,m=0$，最大误差 $2.17\times10^{-19}$，平移不变性误差为零。
3. 直接消费保存的真实旧包
   `2026-11-10-78718-numerical-m15-w22-fast-07_tail_0009.json.gz`，
   其 SHA256 为 `2cc67a7a0cd1652df817aff62770ca20c6b3804bd3e38af581032f787bb2ad52`。
   它是旧 g 的 M=22、spacing=3 已收敛响应，不是新强尾。
   在 513 角点，重新计算的 $D_z\ge.7947893137887561$，
   形式 Gauss 残差最大 $6.297263058230307\times10^{-15}$；
   $n\in[.7406409457868028,.7509963926618465]$，$|m|\le.0279750393398254$。
4. 保存旧包没有高度 Jacobian。检查显式另造了一个**仅用于行布局**的完整测试矩阵，
   保留该身份，没有冒称旧 DN 导数。
   (5)–(6) 的参数中心差分由步长 .001 降到 .0003 时，n 导数差由
   $2.81\times10^{-11}$ 降到 $2.53\times10^{-12}$，其余分量也呈相同二阶比例。

这些有限核验确认代码约定；准确结论由 §1–6 的证明给出。
新强目标仍需实际求解共同固定 g 的完整非线性 BVP 和尾响应，并检验最终实际图。
