# R119 续篇：真实连续 Jacobi 强源、完整 mean 通量与实际二次余项的强尾返回

2026-11-15，visible-exact / tail_connector。

**状态：已证明；独立核对后修正半角宽 Galerkin 半径。** 本篇保持当前同一个
$\mathsf K=2^{128}$、深 $\zeta_j\asymp\delta_j^{131}$ 对象。
新的估计直接作用原固定材料径向坐标中的完整 Jacobi 方程，
不借完整根余核的解析 lag，不把角 $H^{2048}$ 改称指数标签。

已证明的用途是：给定当前真实强尾背景、全部标签方向及一个下文
明定的 ordinary 源，构造含所有 Fourier 模、真实 mean 通量和
唯一高度常数的强尾解。对于实际固定 metric 二次余项，以及两条
实际 $D\Gamma^*$ 在扣除参考高度提升后的源，源 norm 由
$C_j^2$ 的真实消失阶支付；其端点状态回到原强标签空间。
有限外根、long、帽、$\nu$ 及最终全局匹配仍按原真实端口联立，
不包含在下面的局部 Cauchy 乘积内。

依赖：

* [当前 controlled profile 全标签图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)，
  C.2--C.7、C.13--C.35、C.40--C.51，以下记 C；
* [原完整 mean 与连续源](R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md)，
  115.14--115.18、115.25--115.33；本篇重新支付当前 profile 的
  连续源 norm，不沿用其旧 $\delta^{-2890}$ 常数；
* [实际 fixed-$t$ 普通源](R119-supplement-fixed-radial-root-sources-and-complete-ordinary-C2-inverse.md)，
  K.3--K.10；
* [实际非线性源与两 Γ 提升](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md)，
  Q.1--Q.27，以下记 Q；
* [1024阶论文](R119-supplement-complete-1024-angular-Sobolev-network-and-physical-cap-Schur.md)，
  U.7--U.8，只用其当前 $C_j$ 的三段显式数界。

本篇的局部胞元均指 C 中未改变的完整 controlled-profile 胞元。
若实际外接口截断其中一个有限胞元，则只在其实际保留的子段使用
本篇 Cauchy 公式，且该子段的两个真实端口单列。新 finite
simple-root 的物理系统不被重新叫作 C 的旧 quartic 系统。

## 1. 同一角标签空间，重新支付半个局部角宽

物理 Fourier 模为 $m\in4\mathbb Z$。对角宽 $\sigma$ 定义
$$
 \|u\|_{\mathcal A_\sigma}
       =\sum_m e^{\sigma|m|}|u_m|,\qquad
 \|X\|_{\mathcal X_\beta}
       =\sum_{m\ne0}\sup_{j\ge129}
                e^{\beta|m|}\|X_{m,j}\|_\infty.
 \tag{S.1}
$$
$\beta$ 是附加角宽；特别可取原 $\beta=224$。
所有下述 $\mathcal A$ 都是角解析 Wiener 范数，不是微分阶数。

写
$$
 C_j=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \qquad J=j+5,\qquad
 \sigma_j=\tau_{j-1}+\beta+h_j/2 .
 \tag{S.2}
$$
同一个真实局部解可以在 $\mathcal A_{\sigma_j}$ 中读取。
这里不是仅凭原输出较窄就宣称有更宽解析性，而是如下重作 C.18--C.23。

将那里的局部角损 $h_j$ 替换为 $h_j/2$：
C.19 的 $J_j$ 是 C.18 的 Galerkin cutoff，须同时改变。
若 $J_{\rm old}=4\lceil x\rceil$、$J_{\rm new}=4\lceil2x\rceil$，
则 $J_{\rm new}\le2J_{\rm old}$，准确有
$$
 R_{\rm new}
  =2^{-5}(J_{\rm old}/J_{\rm new})^5R_{\rm old}
  \ge2^{-10}R_{\rm old}>2^{-15}R_{\rm old}.
$$
下文统一使用更保守的 $2^{-15}R_{\rm old}$ 下界。
齐次物理四态界乘 $2^5$，二次 endpoint map 费用仍乘 $2^{14}$。
新的投影窗满足
$$
 J_{\rm proj}\le2^{16}(j+5)/h_j
                         <2^{-5}\delta_j^{-3/8}.
 \tag{S.3}
$$
对于 $j\le4096$，左端小于 $2^{20}(j+5)$；
在首层与右端已有超过15 bits的余量，此后单调改善。
对于 $j>4096$，只须
$2^{18}(j+5)<\delta_j^{-95/256}$，其首层余量超过1400 bits。
所以 C.12 的真实内部频窗仍适用。强修正中的
$J_{\rm proj}(h_j/2)/4\ge4096(1+|\log\delta_j|)$ 不变。

原 $16e\sup\zeta_j/R_j<1$ 给，在
$\|X\|_{\mathcal X_\beta}\le2^{-24}$ 时，新输入与新半径之比至多
$2^{15}2^{-24}/(16e)<2^{-13}$，仍位于新半径的 $1/8$ 球。原完整强收缩常数即使乘 $2^{14}$ 仍小于
$2^{-38}$。因此新局部构造和原局部构造在共同域具有同一
Cauchy 数据，由完整解唯一性相同；其全局 endpoint map亦相同。
这没有改几何、profile、参数或真解。

C.23 和真局部 map 的一次 Cauchy 估计于是给安全统一界
$$
 \|W\|_{\mathcal A_{\sigma_j}}
       \le2^8 C_j\|X\|_{\mathcal X_\beta},\qquad
 \|Y\|_{\mathcal A_{\sigma_j}}
       \le2^8 C_j Y_* .
 \tag{S.4}
$$
$W=(P,K,P_\theta,K_\theta)$ 是实际背景，
$Y=(p,k,p_\theta,k_\theta)$ 是原强尾 chart 的真实标签或
固定参数 Jacobi 方向；$Y_*$ 是其 canonical 强状态 norm。
这里的全纯 Cauchy 只用于已有局部真 map，不涉及外部完整 FIO 核。
U.7 的三段数界给 $\sup C_j<2^{-11}$。
因此把实际小球收至 $\|X\|+Y_*\le2^{-24}$ 后，
本篇所用完整复角相对状态小于 $2^{-14}$。
当前 $\mathcal X\le2^{-8388608}$ 远在此球内。

## 2. fixed-$t$ 两行的完整复角 principal 预算

先固定一个真实径向参数 $\Pi$，允许背景与源的角 Fourier
系数为复数。令
$$
 A=(\log w)_t,\quad Q=-A,\quad q=w^2,\quad E=1+q,
$$
$$
 \mathcal J=1+K+EU,\quad
 F=\frac{Q(2K+U+K^2+KU+qP^2)+E(V-P)^2}{\mathcal J}.
 \tag{S.5}
$$
此处 $Q$ 是真实径向 scalar；不将它与独立源 charge 同名。
对高度变化 $h$ 定义
$$
 p=\frac{h_\theta}{\rho rw},\qquad
 k=\frac{h_t}{\rho rw}.
$$
准确 Jacobi ordinary 方程是
$$
 p_t=k_\theta-(A+1)p,\qquad
 k_t=F_Pp+F_Kk+F_Up_\theta+F_Vk_\theta+e .
 \tag{S.6}
$$
$e$ 使用 Q 中 $k_t-DF(W)Y$ 的单位；
真实 divergence RHS为
$ f=w^2\mathcal J D^{-3/2}e$，不是裸 $e$。

若 $n=\|W\|_{\mathcal A_\sigma}\le2^{-14}$、$0<q<1$，
对 (S.5) 的分母作同一个 Banach 逆，直接给
$$
 \begin{split}
 \|F_U-Q\|_\sigma,\ \|F_K-2Q\|_\sigma
                  &\le32(1+|Q|)n,\\
 \|F_P\|_\sigma&\le8(1+|Q|)n,\qquad
 \|F_V\|_\sigma\le8n .
 \end{split}                                             \tag{S.7}
$$
例如
$F_U-Q=(-QE U-EF)/\mathcal J$、
$F_K-2Q=(Q(1-2E)U-F)/\mathcal J$，且
$\|F\|_\sigma\le4(1+|Q|)n$。
这些界保留复部分；不要求更新后的 operator 自伴。

取真实正径向权
$$
 \omega(t)=\sqrt{1+|Q(t)|},\qquad z=(\omega p,k)^T .
 \tag{S.8}
$$
其角 principal 矩阵恰为
$$
 \begin{pmatrix}0&\omega\\F_U/\omega&F_V\end{pmatrix},
$$
完整两行 $\ell^1$ 列和小于 $2\omega$。
零阶矩阵为
$$
 \begin{pmatrix}Q-1+\omega_t/\omega&0\\F_P/\omega&F_K\end{pmatrix},
$$
其列和小于
$3(1+|Q|)+|\omega_t/\omega|$。
因此沿任一实际有向子段，以走过的正长度 $ds=|dt|$ 取
$$
                 \frac{d\sigma}{ds}=-4\omega .
 \tag{S.9}
$$
加权 Fourier 和满足
$$
 \frac{d^+}{ds}\|z\|_{\mathcal A_{\sigma(s)}}
 \le\left(3(1+|Q|)+|\omega_t/\omega|\right)
               \|z\|_{\mathcal A_{\sigma(s)}}+\|e\|_{\mathcal A_{\sigma(s)}}.
 \tag{S.10}
$$
负宽度导数的余量同时支付全部实际非径向、复非自伴 principal。
反向走段时 generator 与源换号，绝对列和相同。
$\omega$ 在真实 $Q=0$ 处连续且局部 Lipschitz，
(S.10) 以几乎处处导数积分，不产生假 jump。

## 3. 真实 profile 的积分、变差及每条根两端费用

C 的九段 profile 总 $y$ 长度是 $3\delta+6\eta$；
下降坡平移保持总长度。四条单调 log 坡的总变差小于
$2\log(2\mathsf K)+6|\log\delta|$，完整 bump / shape 已在
原该式的常数余量内。因为 $Q=7-(\log p_*)_t$，
$$
 \int_{I_j}(1+|Q|)\,dt<512+6|\log\delta_j| .
 \tag{S.11}
$$
这使用绝对值，不从 signed $\int Q$ 偷换得到。

四条真实坡仍各只有一个 $Q$ 峰。
上升坡未改；下降坡控制支集都在 $[3/16,15/32]$，
那里 $S''>7/8$。
原两 bump 的二阶界 $6144,98304$ 与真实系数界
$2^{-16},2^{-30}$，连同 $\|\Xi''\|<2^{-21}$，总干扰小于
$1/8$；而本题每条下降坡的 $\Delta>64$。
所以这些支集不能增加一个反向峰。准确零 $Q$ 最多使
$|Q|$ 的单调段数增加2。由 C.15 的真 $Q$ 上界得到
$$
 {\rm TV}_{I_j}\log(1+|Q|)
       \le16\log(2+Q_{\max,j}),\qquad
 Q_{\max,j}\le2^{12}J\delta_j^{-3/2}.
 \tag{S.12}
$$
所有平台接缝上的 $Q=7$ 连续，没有额外跳量。

把 (S.11)--(S.12) 代入 (S.10)，使用
$e^{1536}<2^{2304}$，完整正逆 Cauchy 费用可取
$$
                 C_j^{\rm CK}=2^{4096}J^8\delta_j^{-30}.
 \tag{S.13}
$$
这里 $\delta^{-18}$ 来自 $3\int(1+|Q|)$，
$\delta^{-12}J^8$ 来自 $\frac12{\rm TV}\log(1+|Q|)$。
没有删除平衡权的径向导数。

角损也由原实际 profile 支付。Cauchy--Schwarz 于四条 log 坡给
$$
 \int_{I_j}\omega\,dt
 \le \sqrt{2/3}(3\delta_j+6\eta_j)
 +12^{-1/4}\sqrt{4\eta_j\,{\rm TV}(\log p_*)}
 \le 2\widetilde\beta_j,
$$
$$
 \widetilde\beta_j=
 3\delta_j+8\eta_j+
 \sqrt{\tfrac{15}{2}\eta_j
      [\,2\log(2\mathsf K)+6|\log\delta_j|\,]} .
 \tag{S.14}
$$
以最大的 $\mathsf K=2^{128}$ 同时包围旧有限前缀。
直接有
$\widetilde\beta_j<8\sqrt{j+47}\delta_j^{3/4}$：
首层 $j=129$ 小于 $2^{-92}$，此前缀单调减小；
$j>4096$ 时与 $h_j=8\delta_j^{1/256}$ 的比在首层已小于
$2^{-3000}$，此后继续减小。因此
$$
                1024\widetilde\beta_j<h_j,\qquad
            \hbox{一次完整角损}<h_j/128.
 \tag{S.15}
$$
任意实际 source 位置到同胞两端均服从 (S.13)--(S.15)。
若从内端取初宽
$\tau_{j-1}+\beta+3h_j/8$，全程末宽仍大于
$\tau_{j-1}+\beta+h_j/4$。
没有由一个正向耗散估计推断未经支付的反向源列；
本节两向均直接使用同一个 fixed-$t$ generator。

有限 Fourier 投影先给 (S.10)，严格较窄条带的一致 Fourier 尾
和径向积分给完整解。相减使用同一 estimate 给唯一性。
全篇只在角变量使用解析性，未要求径向接缝两侧解析延拓。

## 4. 真 mean 是已知 source charge，不能每胞清零

设
$$
 B=1-w^2P^2,\quad
 D=1-w^2(2K+K^2+EP^2),\quad L=1+K.
$$
当前水平 coframe 的完整 angular holonomy 为
$$
 {\cal M}(W)=
  \left\langle
       (1+w^2LU/B)D^{-1/2}
  \right\rangle .
 \tag{S.16}
$$
它在原实际尾上准确为1。利用
$D+w^2L^2=EB$，其点态 $K$ 导数准确是
$w^2\mathcal J D^{-3/2}$。
再将 $U=P_\theta$ 的变化分部积分，得
$$
 D{\cal M}(W)[p,k]
   =w^2\left\langle\mathcal J D^{-3/2}(k-dp)\right\rangle
   =\langle\pi\rangle,\qquad
             d=E(V-P)/\mathcal J .
 \tag{S.17}
$$
最后一式正是 K 中实际 total conormal
$\pi=\mu(h_t-dh_\theta)$、$\mu=w\mathcal J D^{-3/2}/(\rho r)$
的 mean，没有改成 canonical $m=0$。

记这个真实 charge 为 $\chi(t)$。
由完整 divergence 方程
$$
 \chi_t=
 w^2\left\langle\mathcal J D^{-3/2}e\right\rangle,
 \qquad
 \chi(t)=\int_{t_f}^{t}
 w(s)^2\left\langle\mathcal J D^{-3/2}e(s)\right\rangle ds .
 \tag{S.18}
$$
深端 $\chi(t_f)=0$ 是原物理平端条件。
外端 $\chi$ 是输出，不能另设为0。
由于 $|\langle\mathcal J D^{-3/2}\rangle-1|<1/4$，
在给定非mean Cauchy 数据时，mean 小根关于 $\chi$ 的附加初值满足
$$
                         |k_0^\chi|\le2|\chi|/w^2 .
 \tag{S.19}
$$
原实际非mean数据所诱发的 mean 导数照旧包含在 $D\Phi_j$ 内。
本式只分离新的 charge 源，不将 mean 全部当自由数据。

对任意有固定角宽 (S.2) 的连续 ordinary 源定义
$$
 E_j(e)=\sup_{t\in I_j}\|e(t)\|_{\mathcal A_{\sigma_j}},
 \qquad
 Q_j(e)=2^{261}\sum_{k\ge j}\mu_k^2\delta_k^{-1}E_k(e).
 \tag{S.20}
$$
由 $w\le2\mathsf K\mu_j\delta_j^{-1}$、
$w\ge\mu_j\delta_j/256$、$|I_j|_t<4\delta_j$、
$\|\mathcal J D^{-3/2}\|<2$ 得
$$
 \sup_{I_j}|\chi|\le Q_j(e),\qquad
             |k_0^\chi|\le
                    2^{17}\frac{Q_j(e)}{\mu_j^2\delta_j^2}.
 \tag{S.21}
$$
这包含所有更深源的真实 mean 积分；没有将未来源截成0。

## 5. 原两行 endpoint 转换和明确强源 norm

先以零非mean输入、(S.19) 的真实 mean 输入解每胞 (S.6)。
高度角 primitive 唯一取零mean，实际高度 mean 稍后统一积分。
其原 canonical 两行仍准确为
$$
 V_1=\nu(D_\theta)\frac{h}{\rho r^4},\qquad
 V_2=\frac{p_*}{\sqrt{12}r^4}
                  \left(\frac{h_t}{\rho}
                             -D_{\rm mode}^2\frac h\rho\right),
       \qquad (m\ne0).
 \tag{S.22}
$$
这里 $D_{\rm mode}^2$ 的 multiplier为 $m^2$；
$\nu_m=m^2(m^2-1)/12$。
由 $h_\perp=\rho rw\,I_\theta p$ 和
$h_t=\rho rw k$，从至少 $h_j/4$ 的剩余角宽支付至多三次角导，
以及真实 $w,p_*,r$ 后，
$$
 \|V_{\rm out}\|_{\mathcal A_{\tau_{j-1}+\beta}}
       <2^{270}\mu_j\delta_j^{-2}h_j^{-3}
                   \sup\|(\omega p,k)\|_{\mathcal A_{\sigma(t)}} .
 \tag{S.23}
$$
因 $\omega\ge1$，恢复 $p$ 无额外放大；
初值 mean 也未乘一个不存在的 $\omega$ 因子。
末端 $c_j$ 换算仍是原准确第二行除以 $c_j$，其 norm不增。
本式保两行，不以 height 单行代替 source port。

定义新的显式连续强源范数
$$
 \boxed{\quad
 \|e\|_{\mathcal T_\beta^\sharp}
 =2^{4400}\sum_{j\ge129}
  \frac{\mu_j}{\zeta_{j-1}}J^8\delta_j^{-32}h_j^{-3}
       \left(\delta_j E_j(e)
                   +\frac{Q_j(e)}{\mu_j^2\delta_j^2}\right).
 \quad}                                                   \tag{S.24}
$$
$\zeta_{128}$ 取原同一规范初值；
若当前物理安装只消费一部分完整胞元，(S.24) 对其实际源作零延拓，
其实际有限外口另保留。
这个范数完全由已知背景/profile 与源给出，不含未知 Green norm。

(S.13)、(S.21)、(S.23) 的最大常数为
$2^{4096+270+17}=2^{4383}$，小于显示的 $2^{4400}$。
所以真实规范 endpoint 源满足
$$
                       \|f_a(e)\|_{\mathcal F_\beta}
                              \le\|e\|_{\mathcal T_\beta^\sharp}.
 \tag{S.25}
$$
这里范数次序必须说明：每个胞元先以真正
$\mathcal A_{\tau_{j-1}+\beta}$ 范数控制该胞的完整输出，
随后使用
$$
 \sum_m\sup_j |f_{m,j}|
                   \le\sum_j\sum_m|f_{m,j}|.
$$
右侧正是 (S.24) 所支付的胞元和。
没有把 $\sup_t\sum_m$ 反向写成 $\sum_m\sup_t$，也没有从
单列 supremum 得到强 source norm。

给全部原标签变化 $b$，完整线性化 endpoint 问题为
$$
 \dot X=\mathcal H_\Pi b+
  \mathcal G_\Pi\big(D\mathscr R_\Pi(X)\dot X+f_a(e)\big).
 \tag{S.26}
$$
同一原强收缩给
$$
 \boxed{\quad
 \|\dot X\|_{\mathcal X_\beta}
      <18\|b\|_{\ell^1_\beta}
                  +2^{17}\|e\|_{\mathcal T_\beta^\sharp}.
 \quad}                                                   \tag{S.27}
$$
每胞重建用刚才的实际 Jacobi response，传入 charge 都是
同一个 (S.18)。所以两行、charge、mean 小根均匹配。
独立高度从
$$
                  h_t=\rho rw\,k,\qquad h(t_f)=\lambda
 \tag{S.28}
$$
统一积分。各胞 $ \int\rho rw\langle k\rangle\,dt$
是实际高度跨度，绝不在每胞重新设为0。
有限外端取得两条完整 source 迹、$\chi$ 和此 mean 高度。
只有与其余外部来源的真实 flux / holonomy 条件联立后，才是全闭问题。

## 6. 实际 $C_j^2$ 源的全部层账

下面给 (S.24) 一个便于直接消费的严格门。
若对某个 $T\ge0$，
$$
            E_j(e)\le
                2^{660}J^5\delta_j^{-8}C_j^2 T
                    \qquad(j\ge129),
 \tag{S.29}
$$
则
$$
                  \boxed{\quad
        \|e\|_{\mathcal T_\beta^\sharp}<2^{393216}T .
                         \quad}                         \tag{S.30}
$$

证明先保真实 mean 求和。准确恒等式
$$
              \mu_j^2 C_j^2
                  =2^{400}h_j^{-10}\zeta_j^2\delta_j^{-4}
$$
给
$$
 \sum_{k\ge j}J_k^5 h_k^{-10}\zeta_k^2\delta_k^{-13}
        <2^{104}J_j^5 h_j^{-10}\zeta_j^2\delta_j^{-13}.
 \tag{S.31}
$$
每个不跨规范接缝的比至少有 $\delta^{6.5-10/256}$ 衰减，
$J^5$ 不改变小于 $2^{-6}$ 的几何门。
4097处唯一可能增大的 $h^{-10}$ 跳小于 $2^{100}$；
8193处 $\zeta$ 的比改为 $2^{-131}$，只会改善。
因此 (S.31) 包含所有未来 mean 源，不是仅深段渐近式。

(S.20)、(S.29)--(S.31) 得
$$
 Q_j(e)<2^{1025}\mu_j^2J^5\delta_j^{-9}C_j^2T.
$$
代 (S.24)，再用
$\mu_j C_j^2/\zeta_j=2^{200}h_j^{-5}\delta_j^{-2}C_j$、
$\zeta_j\le\zeta_{j-1}$，得到
$$
 \|e\|_{\mathcal T_\beta^\sharp}
  <2^{5626}\sum_j J^{13}h_j^{-8}\delta_j^{-45}C_j\,T .
 \tag{S.32}
$$
统一 $h_j^{-8}\le2^{28}\delta_j^{-1/32}$。
原 U.7 三段 $C_j$ 值依次为
$2^{220}\delta^{7/4}$、
$2^{185}\delta_{4096}^{-3/2}\delta^{827/256}$、
$2^{185}\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
\delta^{31867/256}$。
故第一有限前缀总 bits小于200000。
第二前缀中
$45+1/32-827/256<42$、$J<2^{14}$，完整总 bits小于
$$
            5654+182+185+6150+42\cdot8196+13=356416 .
$$
深段首项同样在此界内；其净下降幂大于79，
后续几何和小于2。三段及实际邻端固定计数仍小于
$2^{357000}$，严格小于 (S.30)。
这一证明没有把前8192层当作深渐近，也没有丢
$\delta_{4096}^{-3/2}$ 或 $\delta_{8192}^{-485/4}$。

同一局部 (S.13) 与末端再缩 $h/8$ 的一次角导还给
$$
 \|(\dot p,\dot k,\dot p_\theta,\dot k_\theta)_{\rm part}\|
        _{\mathcal A_{\tau_{j-1}+\beta+h_j/8}}
       <2^{393216}C_j T .
 \tag{S.33}
$$
核算前的逐胞右端可取
$2^{5144}J^{13}\delta_j^{-41}h_j^{-1}C_j^2T$；
与 $C_jT$ 的比用同一个三段账小于 $2^{393216}$。
齐次重建部分另外由 (S.4)、(S.27) 支付。
物理二 jet与唯一 mean 高度按原 C.23、真实方程及 (S.28)
恢复；这些相关源保留趋0的正径向幂。

## 7. 固定 metric 二次余项和两条选定 Γ 源

若 $Y$ 是 (S.4) 中的真实强方向，且
$\|X\|+Y_*\le2^{-24}$，Q.6 的完整 ordinary 二次余项满足
$$
             E_j(\mathscr E_W(Y))
                 \le2^{41}J\delta_j^{-3/2}C_j^2Y_*^2 .
 \tag{S.34}
$$
这直接来自 Q.8 的 $2^{12}(1+|A|)\|Y\|^2$、
$1+|A|<2^{13}J\delta^{-3/2}$ 和 (S.4)。
它是 (S.29) 的严格子类。因此零标签 particular 有
$$
 \|\dot X_{\rm quad}\|_{\mathcal X_\beta}
                        <2^{400000}Y_*^2 .
 \tag{S.35}
$$
完整 mean charge由 (S.18)计算，不因称作二次余项就设为0。

对于真实选定 $\Gamma^*(a,\Omega)$，先使用 Q.19 的参考高度提升
$$
      (h_\psi)_t=\rho rw\psi,\qquad
      h_\psi(t_f)=0,\qquad
      h=h_\psi+h_{\rm rem}.
$$
只对提升后普通源使用本篇。Q.21 准确给
$$
 \|e_{\rm rem}\|_\sigma
    \le2^{12}\big(n_j|\psi_t|
                         +(1+|A|)n_j^2|\psi|\big).
 \tag{S.36}
$$
两条 bump 的原物理导数仍有
$|\psi_t|<2^{13}\delta_j^{-3/2}g_j$。
Q.26 已包含真实六邻胞的 $2^{132}$ 费和全部耦合参数导数，
所以
$$
 g_j(D\Gamma^*b)
  \le2^{480}J^4\delta_j^{-6}(C_j)^\#\|b\|_{\ell^1_\beta}
  <2^{608}J^4\delta_j^{-6}C_j\|b\|_{\ell^1_\beta}.
 \tag{S.37}
$$
这里可取 $\beta=224$，或更强输入标签后再限制到224；
没有把一个未证明的其它参数导数冒作此式。

代 $n_j\le2^8C_j\mathcal X$，并用
$\sup_j J C_j\mathcal X<1$，得到
$$
 E_j(e_{\rm rem}(D\Gamma^*b))
   <2^{660}J^5\delta_j^{-8}C_j^2
                                \mathcal X\|b\|_{\ell^1_\beta}.
 \tag{S.38}
$$
因此
$$
 \boxed{\quad
  \|\dot X_{\Gamma,\rm rem}\|_{\mathcal X_\beta}
       <2^{400000}\mathcal X\|b\|_{\ell^1_\beta}.
 \quad}                                                   \tag{S.39}
$$
$C_j^2$ 在这里来自实际背景与真实选参导数各一份；
若 $\psi$ 只是任意有界径向方向，不能使用 (S.38)。

参考提升本身仍保留其跨胞常高度
$\int\rho rw\psi\,dt$、原 total flux
$w^2\mathcal J D^{-3/2}\psi$ 及两个实际端列。
它们不计入 (S.39) 的“小余源”，也不在每胞重置。
两条 $\Gamma$ 进入原同一个 joint fixed point，未将其中一条冻结。
原 $\Omega$、材料切口、停止尺度与 $\nu$ 列也没有因本篇而消失；
其准确单位仍按 Q/C/K 的独立公式消费。

## 8. 这给出了哪一个真实迭代入口

在固定 metric 的原强尾 chart 上更新标签，
或按已付 $\Gamma^*(a,\Omega)$ 同步更新真实 profile，
每次重建的无限尾本身仍是完整零 Darboux residual。
原强 contraction和 C.31 已给该 chart 的同一
$\ell^1_\beta\to\mathcal X_\beta$ 全纯导数与二次余项；
本篇进一步将实际连续 ordinary 源、真正 mean charge及
选参参考提升接入同一强 endpoint 空间。
这些连续源不再被要求落入旧 $\delta^{2900}$ 量级的过强空间。

这允许在全局 Newton 联立中使用真实 tail chart，
并把 (S.35)、(S.39) 的完整 source / mean / endpoint 费用登记。
原强标签不能由一个普通 $C^2$ 更新替换：
(S.33) 的输出余宽是 $h/8$，本篇并未据此声称任意连续
强迫更新可以无限次重复使用输入的 $h/2$ 余宽。
如直接迭代胞内 forced fields，仍须构造相容的径向移动角宽域；
使用已存在的精确 tail chart则没有这项人为内部 body residual。

特别，本篇不补造下述尚缺命题：
一个只由完整有限 Sobolev 闭网络取得的外解，
自动具有 $\ell^1_{224}$ 的原标签。
其闭 external matching、真正相位/mean荷、帽反馈和 $\nu$
必须在同一准确强标签 domain 中取得 inverse或有效 tame 入口。
实际角余核的不同 canonical 图不能仅由系数角解析性变成
指数 lag 核。本篇闭合的是此前实际 $C_j^2$ 与两 Γ 普通源
返回原强尾域的连续源步骤；下一项继续该外部同空间接口。
