# R35：无需接近径向基点的真实正组件、角权和 Robin 逆

2026-11-12，visible-exact-astra-f6a2。

**状态：完整证明的局部算子结论，尚未认证当前闭面输入。**
R32 将一个落在开半球内的真实转折组件精确化为散度型方程。本篇对
已经具有下面真实系数比较的正组件，直接构造完整弱解、两端 Poisson、
DN、普通源通量及非实 Robin 逆，并支付一段明确的正角宽。
系数不必是径向系数的小扰动；小量仅用于选择角权宽度。

本篇不跨过负曲率组件，不证明完整传递缺陷的逆，也不供应退化平帽
或极点的零二 jet。特别，两端模型是**法向系数不消失的简单转折**，
不能将它套到两个主系数同时消失的平面片边缘。

## 1. 实际算子、固定域和输入

设 $I=[0,L]$、$L>0$，角变量周期 $2\pi$，积分采用 $d\theta/(2\pi)$。
置
$$
 \chi(x)=x(L-x),\qquad
 A_0(x)=\operatorname{diag}(1,\chi(x)).
 \tag{1.1}
$$
真实实对称密度矩阵写为
$$
 A(x,\theta)=A_0(x)^{1/2}C(x,\theta)A_0(x)^{1/2},
 \qquad mI\le C(x,\theta)\le MI,
 \quad 0<m\le M<\infty.
 \tag{1.2}
$$
该分解在端点按连续的归一系数解释。允许 $C$ 远离恒等矩阵。
实际 cross 项、法向系数和消失 tangential 系数必须全部包含在 (1.2)。
从原曲面坐标得到它所需的 shear、端角图及常数不能省略。

令 $V$ 为光滑周期函数在范数
$$
 \|u\|_V^2=\int_{I\times S^1}
   (|u|^2+|u_x|^2+\chi|u_\theta|^2)
 \tag{1.3}
$$
下的完备化。真实 form 和正号算子为
$$
 \mathfrak e(u,v)=\int A\nabla u\cdot\nabla\overline v,
 \qquad P=-\operatorname{div}(A\nabla).
 \tag{1.4}
$$
复变量的配对按第一变量线性书写。普通源 $f$ 属于整个 $V^*$，
不只零边界测试空间的对偶；后者不足以确定 source contact。

写 $\lambda_n=\sqrt{1+n^2}$，定义两端 trace 空间
$$
 \mathcal T=H^{1/3}(S^1)\oplus H^{1/3}(S^1),\qquad
 \|h\|_{\mathcal T}^2
 =\sum_n\lambda_n^{2/3}(|h_{-,n}|^2+|h_{+,n}|^2).
 \tag{1.5}
$$
本篇所有域固定为 (1.3) 的域及其零 trace 子空间，不作未经证明的
maximal-domain 满射断言。

## 2. 完整 trace 和一个明确的 Fourier 延拓

令 $\ell=L/4$，可取
$$
 C_{\rm tr}=2\ell+\frac4\ell+\frac{64}{3L\ell^2},
 \qquad
 C_E=\frac1\ell+\frac\ell3+\frac{L\ell^2}{12}.
 \tag{2.1}
$$
则真实边界取迹连续并满射，且存在 Fourier 对角的右逆 $E$，满足
$$
 \|\operatorname{Tr}u\|_{\mathcal T}^2
 \le C_{\rm tr}\|u\|_V^2,
 \qquad
 \|Eh\|_V^2\le C_E\|h\|_{\mathcal T}^2.
 \tag{2.2}
$$

**trace 证明。** 对第 $n$ 模置 $t=\ell\lambda_n^{-2/3}\le L/4$。
对 $y\in[t/2,t]$，基本定理和 Cauchy--Schwarz 给
$$
 |u_n(0)|^2\le 2|u_n(y)|^2
       +2t\int_0^t|u_n'|^2.
$$
对 $y$ 平均。如果 $n\ne0$，在该段上
$\chi\ge3Lt/8$，所以
$$
 \lambda_n^{2/3}|u_n(0)|^2
 \le2\ell\int_0^t|u_n'|^2
 +\frac{64}{3L\ell^2}\int_{t/2}^t\chi n^2|u_n|^2.
 \tag{2.3}
$$
这里用了 $\lambda_n^2/n^2\le2$。对 $n=0$，直接用
$(4/\ell)\int_{\ell/2}^\ell|u_0|^2$ 代替后一项。
右端点同理；两端使用的区间不交。对所有模求和即得 (2.2)。

**延拓证明。** 在第 $n$ 模，以左边界值乘
$\phi_{-,n}(x)=(1-x/t)_+$，右边界值乘
$\phi_{+,n}(x)=(1-(L-x)/t)_+$。两者支撑不交，且
$$
 \int\phi_{-,n}^2=t/3,\quad
 \int|\phi_{-,n}'|^2=1/t,\quad
 \int\chi n^2\phi_{-,n}^2\le Ln^2t^2/12.
$$
代入 $t$ 得每一端的 $V$ 范数平方至多
$C_E\lambda_n^{2/3}|h_{\pm,n}|^2$。帐篷函数属于 $V$，可在同一
范数下光滑逼近；所以这给真实有界延拓，而不只是一个形式试函数。
构造按 Fourier 模对角，故与本篇所有纯角 Fourier 权交换。

## 3. 真实零 Dirichlet 逆与完整 Poisson 算子

定义 $V_{00}=\ker\operatorname{Tr}$，并置
$$
 D_L=1+L^2/\pi^2,\qquad g_0=D_L/m.
 \tag{3.1}
$$
每个 $u\in V_{00}$ 的各 Fourier 模有真实零端值，区间 Poincaré
不等式给
$$
 \|u\|_V^2\le D_L\int(|u_x|^2+\chi|u_\theta|^2),
 \qquad
 \mathfrak e(u,u)\ge g_0^{-1}\|u\|_V^2.
 \tag{3.2}
$$
而 $|\mathfrak e(u,v)|\le M\|u\|_V\|v\|_V$。
因此有唯一的真实 Riesz/Lax--Milgram 逆
$$
 G:(V_{00})^*\longrightarrow V_{00},\qquad
 \|G\|\le g_0.
 \tag{3.3}
$$
源来自 $V^*$ 时先限制到 $V_{00}$；这个限制范数至多一。
构造只使用实际 form 的强制性，不要求 $C-I$ 小。

令 $PEh$ 表示 $v\mapsto\mathfrak e(Eh,v)$ 在 $V_{00}$ 上的限制，置
$$
 \mathcal Hh=Eh-GPEh.
 \tag{3.4}
$$
它是同一域上的唯一 $P$-调和延拓，且
$$
 \|\mathcal Hh\|_V\le\sqrt{C_E}(1+Mg_0)\|h\|_{\mathcal T},
 \qquad
 \mathfrak e(\mathcal Hh,\mathcal Hh)
 \le MC_E\|h\|_{\mathcal T}^2.
 \tag{3.5}
$$
第二式来自准确的能量最小性质：$\mathcal Hh-Eh\in V_{00}$，
$\mathfrak e(\mathcal Hh,\mathcal Hh-Eh)=0$。

给定源和边界数据，完整解就是
$$U=\mathcal Hh+Gf.\tag{3.6}$$

## 4. 全 DN、真实 source contact、mean 与普通源界

定义 full DN $\Lambda:\mathcal T\to\mathcal T^*$：
$$
 \langle\Lambda h,k\rangle
 =\mathfrak e(\mathcal Hh,Ek)
 =\mathfrak e(\mathcal Hh,\mathcal Hk).
 \tag{4.1}
$$
它保留两端 cross，不是两个单端 DN 的直和。由 (3.5)，
$$
 \|\Lambda\|\le MC_E,
 \qquad \Lambda=\Lambda^*,\qquad\Lambda\ge0.
 \tag{4.2}
$$
其 kernel 恰是两端的共同物理常数 $(c,c)$：能量零迫使
$U_x=U_\theta=0$ 于内部；反向常数显然调和。

完整 outward flux 是 $\Lambda h+\mathcal Kf$，其中
$$
 \boxed{\quad
 \langle\mathcal Kf,k\rangle
 =\mathfrak e(Gf,Ek)-\langle f,Ek\rangle.
 \quad}
 \tag{4.3}
$$
右边不依赖所选的真实延拓：两个延拓之差在 $V_{00}$ 中，而
$PGf=f$ 在该域中。特别可用常数延拓检查准确 charge：
$$
 \langle\mathcal Kf,(1,1)\rangle=-\langle f,1\rangle.
 \tag{4.4}
$$
并有明确的普通源界
$$
 \|\mathcal Kf\|_{\mathcal T^*}
 \le\sqrt{C_E}(1+Mg_0)\|f\|_{V^*}.
 \tag{4.5}
$$
没有删去 mean、全局常数自由度或 (4.3) 的负 source-contact 项。
用于 R32 的 $P=-\operatorname{div}(Y^2A\nabla)$ 时，源为
$f=-Yf_\rho$；最后应按 R32 的真实 shear 还原原 momentum。

## 5. 无角权的实际非实 Robin 满射

令 $Q=(1-\partial_\theta^2)^{1/6}$，分别作用于两个端点。
则 $Q:\mathcal T\to L^2\oplus L^2$ 为准确等距同构，并且
$$
 B=Q^{-1}\Lambda Q^{-1}
 \tag{5.1}
$$
是整个 $L^2\oplus L^2$ 上的有界自伴算子，$\|B\|\le MC_E$。
允许完整实 normal shear $s_\partial(\theta)$，置
$$
 S=Q^{-1}s_\partial Q^{-1},\qquad L_B=B-S.
 \tag{5.2}
$$
其中 $s_\partial$ 在两端各有一份；它必须来自真实端口变换。
$L_B$ 自伴，但不必非负。

若 $\tau$ 是有界的 Fourier 对角端口算子，满足
$\operatorname{Im}\langle\tau v,v\rangle\ge\gamma\|v\|^2$、$\gamma>0$，则
$$
 \boxed{\quad
 (L_B-\tau)^{-1}:L^2\oplus L^2\to L^2\oplus L^2,
 \qquad\|(L_B-\tau)^{-1}\|\le\gamma^{-1}.
 \quad}
 \tag{5.3}
$$
证明不依赖某个径向 Robin 基点。虚部给
$\|(L_B-\tau)v\|\ge\gamma\|v\|$，所以单射且值域闭。
同一计算对 adjoint 给 kernel 零；值域因而也稠密，即满射。
负虚部的情形完全相同。

特别对 $\tau=i\gamma I$，真实 Cayley
$$
 R=(L_B+i\gamma)(L_B-i\gamma)^{-1}
   =I+2i\gamma(L_B-i\gamma)^{-1}
 \tag{5.4}
$$
是 unitary；这是真实 selfadjoint realization 的谱恒等式。
若选其他 Airy 端口列，须连同列的 Gram、normal shear 和源一起变换，
不能把任意非实 $\tau$ 的未归一矩阵直接称为同一 unitary。

## 6. 小正角宽来自实际系数，不来自小振幅

设归一矩阵和 shear 的 Fourier 系数有某个 $\rho>0$，使
$$
 N_C=\sum_{k\in\mathbb Z}|k|e^{\rho|k|}
       \sup_{x\in I}\|C_k(x)\|_{\rm op}<\infty,
 \qquad
 N_s=\sum_k|k|e^{\rho|k|}\|s_{\partial,k}\|_{\rm op}<\infty.
 \tag{6.1}
$$
这是实际系数的输入。例如更宽角带上的一致解析有界性可付出它；
真实角图和平方根归一化的解析域仍须另行认证。

取 $W_\sigma=e^{\sigma|D_\theta|}$，允许正负 $\sigma$。
在三角多项式上，Fourier 矩阵逐项满足
$$
 \left|e^{\sigma(|n|-|j|)}-1\right|
 \le e^{|\sigma||n-j|}-1.
$$
卷积 Young/Schur 界因此给
$$
 \|W_\sigma C W_\sigma^{-1}-C\|_{L^2\to L^2}
 \le\varepsilon_\sigma
 :=\sum_k(e^{|\sigma||k|}-1)\sup_x\|C_k(x)\|
 \le |\sigma|N_C\quad (|\sigma|\le\rho).
 \tag{6.2}
$$
相同结论用于 $s_\partial$，上界为 $|\sigma|N_s$。
由于 $A_0$、径向导数、角导数和 trace/延拓都与 $W$ 交换，
实际共轭 form $P_\sigma=W_\sigma P W_\sigma^{-1}$ 满足
$$
 \|P_\sigma-P\|_{V\to V^*}\le\varepsilon_\sigma.
 \tag{6.3}
$$
这里是固定域之间的 conjugated source 空间；它不是把
$(W_\sigma^{-1}V)^*$ 错当成 $W_\sigma^{-1}V^*$。
负权使用 Fourier-Hilbert 完备化和对偶，不把所有负权元素称为通常分布。

如果 $g_0\varepsilon_\sigma\le1/2$，真实 zero-Dirichlet 逆的共轭
由实际 $G$ 上的 Neumann 级数得到：
$$
 G_\sigma=(I+G(P_\sigma-P))^{-1}G,
 \quad\|G_\sigma\|\le2g_0,
 \quad\|G_\sigma-G\|\le2g_0^2\varepsilon_\sigma.
 \tag{6.4}
$$
它先在共同有限 Fourier 源上与原弱解由唯一性识别，再按同一域完备化。
这没有以 weighted conjugate 的“自伴性”作不存在的论证。

同一构造给
$$
 \|\mathcal H_\sigma\|\le
 \sqrt{C_E}[1+2g_0(M+\varepsilon_\sigma)],
 \qquad
 \|\mathcal K_\sigma\|\le
 \sqrt{C_E}[1+2g_0(M+\varepsilon_\sigma)].
 \tag{6.5}
$$
第二个算子从同一完整普通源空间到真实两端通量空间。

## 7. 完整 DN/Robin 的正角宽明确门

记
$$
 C_\Lambda=C_E[1+2g_0(M+1)]^2.
 \tag{7.1}
$$
在 $\varepsilon_\sigma\le\min(1,(2g_0)^{-1})$ 时，
$$
 \|W_\sigma B W_\sigma^{-1}-B\|
 \le C_\Lambda\varepsilon_\sigma.
 \tag{7.2}
$$
为核对这个界，用固定延拓写 Schur 公式
$\Lambda=E^*PE-E^*PGPE$，中间的 $P$ 按相应 full/zero-domain
限制解释。共轭后所有 $E$ 不变。第二项的差展开为
$$
 (P_\sigma-P)G_\sigma P_\sigma
 +P(G_\sigma-G)P_\sigma+PG(P_\sigma-P).
$$
由 (6.3)--(6.4)，其连同第一项的范数至多
$$
 C_E\varepsilon_\sigma
 [1+2g_0(M+\varepsilon_\sigma)
      +2g_0^2M(M+\varepsilon_\sigma)+g_0M],
$$
这被 (7.1) 控制。$Q$ 与 $W$ 交换，给 (7.2)。

因而若
$$
 0<\sigma_*\le\rho,\quad
 \sigma_*N_C\le\min(1,(2g_0)^{-1}),\quad
 \sigma_*(C_\Lambda N_C+N_s)\le\gamma/2,
 \tag{7.3}
$$
则所有 $|\sigma|\le\sigma_*$ 都有真正的 signed-weight Robin 逆，
$$
 \boxed{\quad
 \|W_\sigma(L_B-\tau)^{-1}W_\sigma^{-1}\|
 \le2/\gamma.
 \quad}
 \tag{7.4}
$$
这是把 (7.2) 及完整 shear 差接到实际 (5.3) 上的一次 Neumann；
$\tau$ 为 Fourier 对角，故与权交换。
若 $N_C$ 或 $N_s$ 为零，相应 (7.3) 条件自动成立。
一般有限输入下，总存在一个可明确选取的正 $\sigma_*$。
例如把各分母中的 $N_C$、$C_\Lambda N_C+N_s$ 分别换为
$1+N_C$、$1+C_\Lambda N_C+N_s$ 后取这些上界的最小值即可。

对 (5.4) 的完整 Cayley，(7.4) 还给
$$\|W_\sigma R W_\sigma^{-1}\|\le5.\tag{7.5}$$
ordinary offset 必须使用 (4.3)、(6.5) 的同一通量，再经过同一
Robin 逆；没有从 unitary 一词免费获得带权源界。

### 7.1 只有直接 log 宽时的同一个真实结论

上述解析宽不是从 $C^\infty$ 正则性或源题的 log 宽自动推出的。
如果实际输入仅给直接 log 权，可改用
$$
 \omega(t)=\log(e+t)^{3/2}-1,\qquad
 W_\sigma=e^{\sigma\omega(|D_\theta|)}.
 \tag{7.6}
$$
这里 $\omega(0)=0$、递增且凹，因为
$$
 \omega''(t)=\frac{3[1-2\log(e+t)]}
                   {4(e+t)^2\sqrt{\log(e+t)}}<0.
$$
凹性及零端值给次可加性，从而
$|\omega(|n|)-\omega(|j|)|\le\omega(|n-j|)$。
于是 (6.2) 的证明逐字成立，只须将其中的 $|k|$ 换成 $\omega(|k|)$，
并实际供应
$$
 N_C^{\omega}=\sum_k\omega(|k|)e^{\rho\omega(|k|)}
              \sup_x\|C_k(x)\|,
 \qquad
 N_s^{\omega}=\sum_k\omega(|k|)e^{\rho\omega(|k|)}
              \|s_{\partial,k}\|.
 \tag{7.7}
$$
常数项 $-1$ 不改变任何共轭；它使次可加的差值恒等式准确。
以 (7.7) 替换 $N_C,N_s$ 后，(6.3)--(7.5) 及同一个正宽门全成立。
这给直接 log 权中的真实正组件逆，没有声称获得不存在的解析带。

## 8. 真实两几何差与后续使用

对于同一 $A_0$ 和同一弱域下的两组实际系数，零 Dirichlet inverse
始终有准确 resolvent identity
$$G_1-G_0=-G_1(P_1-P_0)G_0.\tag{8.1}$$
Poisson、DN、source contact 和 Robin 的差按上述固定域公式展开，
每项都含一次真实系数差。若 (1.2)、(6.1)、(7.3) 对整个邻域有共同
常数，所有上述门在同一个正角宽上保持。这不需要每轮把几何重新
假定为径向基点的小扰动。

对本题的准确限制如下：

1. R32 的 ground-state 变换可供应完整散度型算子和 source/shear，
   但需实际证明该正组件存在满足 (1.2) 的坐标及比较常数。
2. 本文付清的是正组件的弱域、full DN/Robin 最大性和一段带权预算。
   两端 simple root 到严格双曲切口的真实 Airy/Cauchy 接线、强输出
   jets、完整负组件反馈和所有低阶相位仍须另付。
3. 一次球谐 $Y$ 的下界、从 $U$ 到原 $w$ 的范数、端口角图复合、
   多帽相对 Killing 条件及最终 Cartesian 零二 jet 均仍在原问题中。
4. 本篇选择的角宽可能很小。没有给出当前有限振幅候选的实际常数，
   就不能据此宣称其非线性残差已经满足收敛门。

结构对照为 [R513 §§4–6](../../continuous-flexibility-swarm/results/R513-direct-log-physical-local.md)：
该源用径向基点小扰动构造 full cap form、源 contact 和真实 Robin。
本文直接从当前 form 的强制性及其 Fourier 角权交换差重新证明以上门，
未使用源的原 profile、小量或尚未适配的高阶输出作为免费输入。
