# R133：完整伴随与真实 ν 源的双积分、均值及全部乘积跳跃

**状态。** 下述恒等式及有向消费规则已证明。新
[完整消费程序](../scripts/fourfold_codazzi_signed_nu_adjoint_pairing.py)
在执行环境失联期间写成，**尚未执行**。目前没有实际 M96 response /
adjoint trial，也没有本程序的 native 报告；本篇不声称参数 Schur 非零、
补空间可逆或完整非线性 BVP 存在。

本篇给出恢复 runtime 后可计算的带符号数。它不以有限 QR 的条件数
代替参数横截，也不从一个近似伴随的源积分直接推出真 Schur 的符号。

## 1. 唯一对象和函数空间

使用最终全长 moving 中心，候选完整索引 SHA256 为

ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。

其 $\alpha=6890507429876859/9007199254740992$、
$\nu=-2572625729470897/72057594037927936$、$R=25/8$，
$u=\alpha U,\ v=s_\nu+\alpha V$。中心有完整 32 个 moving 模，
原 $4\mathbb Z$ 反射类为 $u$ 奇、$v$ 偶。每个保存的三次 PPoly
按其准确 dyadic 系数读取；所有实际接缝都保留。

圆周内积为 $\langle f,g\rangle=(2\pi)^{-1}\int f\cdot g$。
$I=\partial_\varphi^{-1}P_\perp$，故 $I^*=-I$。所有均值均是这一
完整圆周均值。控制支集为 $[a,b]=[1/20,9/50]$，

\[
 w(r)=4096t^6(1-t)^6,\qquad t=(r-a)/(b-a).                 \tag{D.1}
\]

区间外 $w=0$。$w,w'$ 在端点为零；$w'$ 始终是原物理 $r$ 导数。
intrinsic provider 含完整 primitive 的无限尾，保留全部
$|\eta|\le10^{-9}$。程序要求它与 full-mean 证书所用原目标缓存
是同一字节输入，并要求真实 type-cover 包含准确 $\nu$。

## 2. 完整物理源及真实径向导数

令 $Q=(u,v)$，$m=\langle v\rangle$，

\[
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 S=u^2+Kv^2,\quad d=-\beta IS,\quad T=\frac{\beta}{2E_\nu}.
\]

完整算子 $\mathcal D h=h_r-\mathcal A_Qh$ 保留
$d\partial_\varphi+\gamma mJ\partial_\varphi$、全部局部项以及

\[
 \mathcal Nh=-2\beta Q_\varphi I(uh_1+Kvh_2)
             +\gamma JQ_\varphi\langle h_2\rangle.         \tag{D.2}
\]

这正是[已发表的完整源与伴随程序](../scripts/fourfold_codazzi_nu_full_adjoint_kernel.py)
所定义的算子。设

\[
 \mathcal W=I(v^2)Q_\varphi+v^2Q,\qquad
 A_\nu=-\beta T\mathcal W+(\gamma mT v_\varphi,0),
\]
\[
 B_\nu=\beta K\mathcal W-
       \frac{\gamma m}{2}(Kv_\varphi,u_\varphi).            \tag{D.3}
\]

在固定**物理** $u,v$ 下 $\gamma_\nu=+w\gamma/2$、
$K_\nu=-wK+Tw'$，于是准确有

\[
 \boxed{F_\nu=w'A_\nu+wB_\nu.}                            \tag{D.4}
\]

这里没有除以 $\alpha$。归一化 $U,V$ 的参数列还含参考 $s_\nu$
的链式项；它不能替换本篇物理源。取真正保存的 $Q_r$，逐项微分
(D.3)，再定义

\[
 G_\nu=B_\nu-\mathcal D A_\nu.                            \tag{D.5}
\]

$A_\nu,B_\nu,(A_\nu)_r$ 的完整 Fourier 支集至 $3M$；
$G_\nu$ 的完整支集至 $5M=160$。均值和非局部原函数都参与这些乘积。
径向微分中使用真实 PPoly 的导数及 intrinsic $s_\nu'$，不把
有限中心代入未成立的非线性 PDE 来替代 $Q_r$。

## 3. 同一个连续伴随均值

有限伴随非均值试函数 $\lambda=(\lambda_1,\lambda_2)$ 必须符合
已发表的 physical trial schema；其第二分量 mean 列在每个
PPoly 系数中准确为零。完整伴随是

\[
 \Psi=\lambda+\mu e_2,\qquad
 \mu'=-c_m\mu-g,\qquad
 g=\langle\mathcal A_Qe_2,\lambda\rangle,                  \tag{D.6}
\]
\[
 c_m=\beta(1-\langle u^2\rangle-K\langle(v-m)^2\rangle-3Km^2).
\]

初值是实际幅度乘子乘以完整腰 mean 列。程序读取
[完整 mean/body 消费器](R133-supplement-mean-completed-head-and-adjoint-body-consumer.md)
围住的同一标量初值问题。$\mu$ 是连续普通标量函数，即使 $Q$ 或
$\lambda$ 在保存的接缝跳跃也如此。分片有界系数给通常的唯一
绝对连续解。

令 $\mathcal R_\Psi=\mathcal D^*\Psi$。其第二分量的完整均值因
(D.6) 准确为零。源码先核原始 interval 包含零，再只把这一
已证明的单个系数设为零；其余全部系数保持。

新报告不会生成另一个独立均值轨迹。它读取原闭盒的 $\mu$
enclosure，重算同一 $c_m,g$ 并与原完整 enclosure 求交。
每个真实接缝处也对左右连续均值 enclosure 求交，不能人为给
$\mu$ 安排点源。

## 4. 带符号的双积分恒等式

在无真实跳跃的开片上，完整圆周分部积分给

\[
 \langle\Psi,\mathcal DA_\nu\rangle
 =\partial_r\langle\Psi,A_\nu\rangle+
             \langle\mathcal D^*\Psi,A_\nu\rangle.
\]

所以

\[
 \langle\Psi,F_\nu\rangle
 =\partial_r\{w\langle\Psi,A_\nu\rangle\}
  +w\{\langle\Psi,G_\nu\rangle+
                    \langle\mathcal R_\Psi,A_\nu\rangle\}. \tag{D.7}
\]

$\Psi$ 不必是真齐次伴随。尤其
$\langle\mathcal R_\Psi,A_\nu\rangle$ 不能删除。令 $\mathcal J$ 为
$a<r_i<b$ 内候选与伴随的全部实际 PPoly 接缝并集，跳跃统一右减左。
由于外端 $w=0$，

\[
 \boxed{\begin{aligned}
 I_\nu&=\int_a^b\langle\Psi,F_\nu\rangle\,dr\\
 &=\int_a^b w\{\langle\Psi,G_\nu\rangle+
                \langle\mathcal R_\Psi,A_\nu\rangle\}\,dr
   -\sum_{r_i\in\mathcal J}w(r_i)
                [\langle\Psi,A_\nu\rangle]_{r_i}.
 \end{aligned}}                                         \tag{D.8}
\]

$w'$ 费用已转成真实径向 $G_\nu$、伴随残差和乘积点源。接缝再小
也不能省掉。直接形式同时保留：

\[
 I_\nu=\int_a^b
 \{w'\langle\Psi,A_\nu\rangle+w\langle\Psi,B_\nu\rangle\}\,dr.
                                                               \tag{D.9}
\]

每个闭盒额外切在 $(a+b)/2$，使 $w'$ 不变号。若 $P_A,P_B$ 是
盒上完整带符号 pairing enclosure，则

\[
 \int_l^r\langle\Psi,F_\nu\rangle
 \in [w(r)-w(l)]P_A+
             \left(\int_l^r w\right)P_B.                 \tag{D.10}
\]

负的 $\Delta w$ 按有向区间乘法处理，不能换成绝对值后仍称带符号
积分。$\int w$ 和 $\Delta w$ 按 (D.1) 的有理多项式准确积分。

## 5. 全部实际乘积跳跃

由于 $\mu$ 连续，

\[
 [\langle\Psi,A_\nu\rangle]
 =\langle[\lambda],A_\nu^-\rangle+
       \langle\lambda^++\mu e_2,[A_\nu]\rangle.           \tag{D.11}
\]

第一项用左 $A_\nu$，第二项用右完整伴随。两种跳跃同时存在时也成立，
无遗漏交叉项。

$\Delta Q$ 从准确 dyadic PPoly 接口差产生；同一 intrinsic
$s_\nu(r_i)$ 因真实目标连续而相消。设
$\Delta v^2=(v^++v^-)\Delta v$，则

\[
 \Delta\mathcal W=
 I(\Delta v^2)Q_\varphi^+
 +I((v^-)^2)(\Delta Q)_\varphi
 +(\Delta v^2)Q^++(v^-)^2\Delta Q,
\]
\[
 \Delta A_\nu=-\beta T\Delta\mathcal W+
 \bigl(\gamma T[
       \Delta m\,v_\varphi^++m^-(\Delta v)_\varphi],0\bigr).
                                                               \tag{D.12}
\]

该式保存真实 mean 跳 $\Delta m$，避免把两个大 interval 直接
相减的费用当作小的真接缝费。伴随 mean 跳准确零，候选 mean 跳
通常非零。其他源变换的 jump 不能与本式互相抵销；本式只处理
当前标量 Green 恒等式产生的乘积 jump。

## 6. 有向全频实施

消费器要求三个已发表源的准确 SHA：

- fourfold_codazzi_final_nu_return_derivative.py：
  33ae536750241497e7ad73b72aedb2be8d7185542b5f71a88f081af005c7ebbe；
- fourfold_codazzi_nu_full_adjoint_kernel.py：
  09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b；
- fourfold_codazzi_mean_completed_head_body_residual.py：
  190291987e288beaa9647afd90b54f16df2c6610d706fee01cac4623e1a4b62f。

原 target germ、mean-flow、候选、adjoint 的全部边界和 bump 中点
构成精确共同分割，可再显式细分。若伴随最高指数为 $N$，
grid 严格大于 $2\max(5M,N+2M)$，容纳算子的全部有限输出。
圆周内积直接算完整 $\sum_j f_jg_{-j}$，不做可能 alias 回 mean
的循环乘积。不以 $N$ 模投影 $G_\nu$ 或伴随残差。

每盒保存四个 pairing、带符号 $\int wG$、伴随残差积分、
直接积分及真实索引；每个 jump 保留 (D.11) 的两个独立项。
最后求交直接全域 enclosure、完整分部积分 enclosure，以及
原 full-body 证书的同一 $\int\langle\Psi,F_\nu\rangle$ enclosure。

任一交集为空即实际失败，已算前缀和错误原样保存。仅同一输入
$\Psi$、同一 mean 初值问题、同一全部 $\eta$ 范围才可求交。

## 7. 复现及范围

恢复准确候选并完成真实 trial 与 mean/body 报告后：

~~~sh
PYTHONPATH=scripts python scripts/fourfold_codazzi_signed_nu_adjoint_pairing.py \
  --candidate ACTUAL_COMPLETE_AC1.json \
  --adjoint ACTUAL_PHYSICAL_NONMEAN_ADJOINT.json \
  --mean ACTUAL_COMPLETE_MEAN.json.gz \
  --body ACTUAL_COMPLETE_MEAN_FILLED_BODY.json.gz \
  --angles 1024 --max-new-rows 64 \
  --out NEW_SIGNED_PREFIX.json.gz
~~~

续算传 --resume OLD_SIGNED_PREFIX.json.gz 和一个新 --out。
仅成功保存的前缀可续；source、全部输入、共同分割和 jump radii
必须相同。最后一盒和所有 jump 完成后才设
complete_actual_source_pairing_proved=true。

即使 $I_\nu$ enclosure 排除零，它仍只是这个完整近似伴随对真
参数源的配对。真正分母还需原始物理 $b_4$、完整外边界转置、
腰行、独立 mean、所有 trial jump 以及
$(b-\Lambda\bar A)\bar A^{-1}r_\nu$ 的全空间误差。
本篇不把这些未付项并入一个未定义的小余项。

独立 $f_B$、真正外尾 regular/label 方程、非线性中心的完整
边界残差也没有被本次 homogeneous $\nu$ 源配对删除。
