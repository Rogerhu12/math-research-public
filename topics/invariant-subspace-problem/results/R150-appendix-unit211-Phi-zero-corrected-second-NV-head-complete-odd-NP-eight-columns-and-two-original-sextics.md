# R150：正确 Phi 第二个 NV 最高头的完整 odd N/P 八列与两个原六次式

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**已证明的范围。** 在当前正确 $\Phi=0$ 原图的第二个完整 $NV$ 的 $t$ 最高头
$$
\ell(3-2\lambda)+2T+2m\sigma=0
\tag{1}
$$
上，两个完整 singleton $N/P$ 误差的奇部各自给出四条新的同点原列。它们与此前二十列组成准确的 $4\times28$ 原值理想呈示。两个事前固定的四列 cofactor 均完成全部九个原方程的普通多项式回乘，实际得到两个非零的 $\lambda$ 六次必要式，权首项总次分别为 $60,65$。

**本次没有返回单位，没有计算这些标量的共同 gcd，没有排除第二头或整个 $\Phi$。** 全部新权首项零纤维以及其余原值条件继续保留。

唯一首次实际计算为 run **46172445766**、job **141063663909**，内层正常退出。下文只使用该次完整返回，不重跑此前二十列、三个 cofactor 或已经冻结的第一头 gcd。

## 1. 原权环与同一个物理点

置
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
M_n=2uL-L^2-u^2Q,\qquad M=M_n/Q=4bc\delta.
$$
本次身份所在系数环为
$$
\mathcal A=\mathbb Q[u,Q,(Q\delta sK_wLM_n)^{-1}].
\tag{2}
$$
这些权因子在当前正确 $\Phi$、物理 $D_{\rm phys}\ne0$ 原图都已有独立正确来源；本文不把该物理支付迁到此图之外。本次没有添加 $m,u,2\ell-1$、$D$、$\lambda$、$\sigma$、$t$ 或任一新头的逆。

写
$$
a=\lambda-\frac32,\quad T=\ell a-m\sigma,\quad
T_0=-K_w,\quad P_{02}=2sL,\quad J-Q=-4s^2.
$$
由原 $E_0,N_0,P_1$ 同点恢复，
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
V=f+bct-E,
$$
$$
A_1=2E,\quad W_1=T_0/2+2uf,\quad
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M}.
\tag{3}
$$
取
$$
\rho^2=\delta,\quad
b=\frac\ell2+\frac{m\rho}{2\delta},\quad
c=\frac\ell2-\frac{m\rho}{2\delta},\quad
p=1+\rho,\quad q=1-\rho,
$$
$$
X=x+\rho y,\quad Y=x-\rho y,\quad
r=X-(1-\ell)p-ct,\quad
s_G=Y-(1-\ell)q-bt.
$$
真实 Gram 的四行是
$$
v_0=(0,0,p,q),\quad v_1=(0,A_1,r,s_G),\quad
v_B=(p,r,0,t),\quad v_C=(q,s_G,t,0).
\tag{4}
$$
原代数第一块的乘法始终为
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0,
$$
另两坐标逐点相乘，且
$$
\mathbf1=(1,0,1,1),\qquad
\tau(v)=(1-\ell)v_0+v_1+bv_B+cv_C.
$$
在 (1) 中，两个物理 singleton 值为
$$
h=\lambda-\frac12-\rho\sigma,\qquad
k=\lambda-\frac12+\rho\sigma,\qquad
w=\lambda-1-T.
\tag{5}
$$
全过程没有专门化物理 $t=0$。

本节使用的旧原来源是：

- [正确全权 $t$ 参数与原均值](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)；
- [全权首一 $t^2$ 与第二头四元环境](R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)；
- [第二头二十条原列及三个 cofactor](R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-twenty-original-columns-and-three-cofactors.md)。

## 2. 新加入的是完整原误差的奇部

定义 $DK(v)_i=\tau(v_i v)$、$d=DK(\mathbf1)$、$F_2=\tau(d)=2f$。完整原式为
$$
\begin{aligned}
N_4(v)={}&2\tau(dv^2)-F_2\tau(v^2)
-4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vDK(v)),\\
P_2(v)={}&\tau\!\left((v-\tau(v)\mathbf1)^3\right).
\end{aligned}
\tag{6}
$$
新输入为
$$
E_N=\bigl[N_4(v_B)-2\lambda P_{02}h^2\bigr]_{\rm odd},
\qquad
E_P=\bigl[P_2(v_B)-P_{02}h^3\bigr]_{\rm odd}.
\tag{7}
$$
odd 是 $\rho$ 的系数。计算同时构造 $v_C,k$ 的两个完整误差，并实际返回
$$
\mathrm{Err}_{N,C}=\overline{\mathrm{Err}_{N,B}},\qquad
\mathrm{Err}_{P,C}=\overline{\mathrm{Err}_{P,B}},
$$
$$
\mathrm{Err}_{N,B}-\mathrm{Err}_{N,C}=2\rho E_N,\qquad
\mathrm{Err}_{P,B}-\mathrm{Err}_{P,C}=2\rho E_P.
\tag{8}
$$
这里横线是原二次代数中 $\rho\mapsto-\rho$ 的共轭，没有选取单个平方根。

(6) 保留所有中心项和实际 dual 乘法；(7) 不是单独的裸 $N/P$ 范数条件。由于 (3) 中的几何量仿射，两式总 $(\lambda,\sigma,t)$ 次数至多三；本次实际核对了此上界。

将九个原方程依次记作
$$
(F_0,\ldots,F_8)=
(E_2,R,E_{Be},E_{Bo},N_1,E_3,NV,E_N,E_P).
\tag{9}
$$
其中
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda,\qquad
E_3=b(h-1)^3+c(k-1)^3-B_\lambda,
$$
$$
NV=N_4(1,w,h,k)
$$
为未乘 $\ell^2$ 的完整原值，$N_1$ 为完整第一 jet 的 $N$ 误差。三个均值 $R,E_{Be},E_{Bo}$ 使用已经纠正的原定义。设 $J_9=(F_0,\ldots,F_8)$。原物理解必满足 $J_9$；本文不声称它已是全部原条件的充分描述。

## 3. 两次首一短除保留全部重数

令
$$
q_\sigma=
\sigma^2-\frac{2ma}{\ell\delta}\sigma
-\frac{A_\lambda-\ell a^2}{\ell\delta},
\qquad E_2=\ell\delta q_\sigma.
$$
令
$$
B_q=Q^2+(2u^2-3)Q+2s(2u-1)(u-2),
$$
$$
\gamma_R=-\frac{B_q}{\ell bc\,sQ},\qquad
\gamma_O=-\frac{8\delta}{\ell},\qquad
q_t=\gamma_RR+\gamma_OE_{Bo}.
\tag{10}
$$
此前已完整证明 $q_t$ 对 $t$ 首一二次，$\gamma_O$ 是 (2) 中的单位。这里的正确原 $R$ 是
$$
R=4(f-u)(V-f)+bc\,t^2+
t\left(4bcu-\ell V+\frac{m(T_0+4uf-2V)}{2\delta}\right).
$$
用唯一普通 $\sigma$ 短除定义
$$
q_t=\widetilde q_t+w_\sigma q_\sigma,\qquad
\deg_\sigma\widetilde q_t<2.
\tag{11}
$$
因此
$$
\mathcal B=\mathcal A[\lambda,\sigma,t]/(q_\sigma,\widetilde q_t)
$$
在 $\mathcal A[\lambda]$ 上自由，基固定为
$$
e=(1,\sigma,t,\sigma t),\qquad d=(0,1,1,2).
\tag{12}
$$
两个首一多项式的重根与所有幂零结构均保留。

对任意待处理原倍数 $G$，先除 $\widetilde q_t$，再除 $q_\sigma$，得
$$
G=r+Q_t\widetilde q_t+Q_\sigma q_\sigma.
$$
故普通原多项式环中有
$$
G=r+
\frac{Q_\sigma-Q_tw_\sigma}{\ell\delta}E_2+
Q_t\gamma_RR+Q_t\gamma_OE_{Bo}.
\tag{13}
$$
本次对 $E_N,E_P$ 各乘 (12) 的四基，实际返回八次 (13) 和全部三十二个余式坐标。

八条新列的实际 $\lambda$ 次数都达到下表记录；每行依次是四坐标 $1,\sigma,t,\sigma t$ 的次数：

| 新种子 | 基倍 $1$ | 基倍 $\sigma$ | 基倍 $t$ | 基倍 $\sigma t$ |
|---|---|---|---|---|
| $E_N$ | $(3,2,2,1)$ | $(4,3,3,2)$ | $(4,3,3,2)$ | $(5,4,4,3)$ |
| $E_P$ | $(3,2,2,1)$ | $(4,3,3,2)$ | $(4,3,3,2)$ | $(5,4,4,3)$ |

每条实际坐标也逐项满足 $\deg_\lambda c_{ij}\le3+d_j-d_i$。

## 4. 精确的二十八列呈示与两个固定组合

因为 $\ell\delta,\gamma_O$ 都是 (2) 中的单位，
$$
J_9=(q_\sigma,\widetilde q_t,R,E_{Be},N_1,E_3,NV,E_N,E_P).
\tag{14}
$$
此前五个种子 $R,E_{Be},N_1,E_3,NV$ 已各有四条实际基倍列，准确表示 $J_7$。增加 (13) 的八列后，作为 $\mathcal A[\lambda]$ 模有
$$
\mathcal A[\lambda,\sigma,t]/J_9
\simeq
\operatorname{coker}
\bigl(\mathcal A[\lambda]^{28}\longrightarrow
\mathcal A[\lambda]^4\bigr).
\tag{15}
$$
证明只需四元环境在 (12) 上自由：理想任意元素的每个乘子都是四个基元素的 $\mathcal A[\lambda]$ 线性组合。因此四个基倍已完整生成每个种子的理想。原值商不被假设为自由，(15) 也不是凭某个数值秩推得。

旧列保持编号 $0,\ldots,19$；$E_N$ 的新块是 $20,\ldots,23$，$E_P$ 是 $24,\ldots,27$。本次只再生旧基列 $0,4,8$ 的定义供两个新矩阵使用，不重跑旧二十列循环和旧三个 cofactor。

固定的两个新四列组为
$$
I_A=[0,4,20,24]=[R,E_{Be},E_N,E_P],
$$
$$
I_B=[0,8,20,24]=[R,N_1,E_N,E_P].
\tag{16}
$$
对其四阶矩阵 $B_I$，令
$$
\omega_j=(-1)^j\det(B_I)_{\widehat0,\widehat j}.
$$
实际完整返回
$$
B_I\omega=(\det B_I)e_0.
\tag{17}
$$
没有倒行列式、任何主元或任何几何首项。按列总次数 $(2,2,3,3)$ 与行基权 $(0,1,1,2)$，
$$
\deg_\lambda\det B_I\le6.
\tag{18}
$$
将 (17) 沿每列 (13) 合回，得到全部九个原式的身份；这一步允许某些原乘子为零，但不删除这些原条件。

## 5. 九原共同约消及本次两个实际六次式

写 $F_i=n_i/d_i$，各 $d_i$ 仅含 (2) 的权支持。先把 (17) 得到的真实乘子运输为 $n_i$ 的乘子，统一清分母，完整返回
$$
\sum_{i=0}^{8}\Omega_i n_i=C.
\tag{19}
$$
随后只对全部九个实际 $\Omega_i$ 的共同因子作精确约消，并在同一多项式环中再返 (19)。本次两个共同因子都有总次一、三项，且规范 profile SHA 相同：
9d8ab7335bcfbc1af82c09eedc3891136169e0c0f0da9561274744e9d9e6bd05。
这里只按实际记录说明它的度数与身份，不由 hash 猜其系数。

共同约消后的等式本身在共同因子为零的纤维仍成立；没有把它当作新物理单位。接着只剥除 (2) 的原权因子并运输到九个乘子，再返完整原式。全部十八个最终实际分母均通过原支持检查。

最终得到 $C_A,C_B\in\mathbb Q[u,Q,\lambda]$，且
$$
C_A,\ C_B\in J_9
\quad\text{于 }\mathcal A[\lambda,\sigma,t].
\tag{20}
$$
实际 profile 为：

| 必要式 | 固定组 | $\deg_u$ | $\deg_Q$ | $\deg_\lambda$ | 总次 | 项数 |
|---|---|---:|---:|---:|---:|---:|
| $C_A$ | $[0,4,20,24]$ | 55 | 32 | 6 | 66 | 8012 |
| $C_B$ | $[0,8,20,24]$ | 60 | 34 | 6 | 71 | 9352 |

它们的完整规范 SHA-256 分别是：

- $C_A$：4941535e2268d2c4631e45829063130f2acc5c34ea237c82d5269f0c3e27958e；
- $C_B$：bb8766f41e9e7aa3c6868cc4d146231c550c14e0730841276ad4e853c7f7c72a。

两个实际 $\lambda^6$ 系数同样是纯权多项式：

| 首项 | $\deg_u$ | $\deg_Q$ | 总次 | 项数 | 规范 SHA-256 |
|---|---:|---:|---:|---:|---|
| $[\lambda^6]C_A$ | 55 | 32 | 60 | 1142 | 6d17bbe6606e7dadb59e06a30b9f9665cd4729b3ef4c838a976b4f98eb560f7b |
| $[\lambda^6]C_B$ | 59 | 34 | 65 | 1280 | b45665b949d8c3a1a3802d4452669a14fd1e8051405b11aeb67bf3258e007d07 |

这两个头均未证明为单位，未作 QQ 因式分解。所有头零纤维仍在 (20) 的必要支持中，不能用表中六次把它们直接视为全权首一模型。

## 6. 唯一实际执行与可重现来源

源码：

[完整 odd N/P 八原列源](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-complete-odd-NP-eight-original-columns-8542.py)

- source blob：1de19854c20cbe5e915d77c7887ae4f6958770ea；
- 完整 SHA-256：39a56877bf4a1ccb73432b9d70dc73c840c22c3415b9bd6cbc3de6c3e3834252；
- [首次输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-complete-odd-NP-eight-original-columns-8542-input.md)，blob e24c18bbdff167ce813104fe1ec4d1af52b478f5；
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-complete-odd-NP-eight-original-columns-8542-execution.json)。

唯一直接依赖为此前 d20 原定义源，完整 SHA-256 为
c7141ce12424d916ee415c0ac0121ea938ff206d20b5a8c12193bb3a1cdcdaa1。
仅使用其前 10519 字节，前缀 SHA-256 为
67c407b2bd4a611a90a1094403546860459dfbb3bad6676a990dca6773343255。
AST 不进入旧二十列或旧三个 cofactor，并省去旧顶层时钟、输出和证明断言；内部精确短除仍返回。外层唯一绝对预算为 120 秒、1 GiB，外层驱动 135 秒。

实际 run [46172445766](https://github.com/Rogerhu12/math-research-public/actions/runs/46172445766)，job 141063663909，首次 attempt 1：

- 源提交：22ca9049ebd082513149c453f56818521228443f；
- 实际拉取后提交：6ad9f9132c197496df8f9ee8759c57cef4c72b2c；
- 规则读取：2026-11-28T17:48:47.290242+00:00，两份 README 均未变；
- 内层时间 21.923922683 秒，峰值子进程 RSS 105724 KiB，exit 0；
- 最后数学阶段时间 21.861471112 秒；
- stdout 20567 字节，SHA-256
  9a4041c5b65bc8cdf0ef40117cd4b9c432e2521dd629406baefc27a2ee8e8fda。

完整六条数学记录均已读取，并按原行重建 stdout 的长度和 SHA 与驱动回执一致。新目标统计为：四条完整奇部/共轭身份，八条新列、三十二坐标，二十二次新目标所需的首一短除，八个 cofactor 坐标，十次九原反传/约消阶段返回，十八个最终分母检查，8241 次精确乘积返回。三个旧基列只作唯一必要参数定义；本次没有重复旧二十列证明。

## 7. 保留范围

(15)、(20) 是本次新结论。它们严格保留同一 $(\lambda,\sigma,t)$，不把不同范数根拼为同一个原点；也保留两个首一二次的全部幂零结构。

本次没有完成新的共同 gcd、权头单位、有限权点界或排空。原完整 singleton even 条件、加权 $NS/PS$ 以及其他原值继续保留；第二头仍开放。第一头已经冻结的三标量泛域 gcd、旧 Q 主分量资源边界和整个正确 $\Phi$ 的已有范围均不因本次 exit 0 而改变。
