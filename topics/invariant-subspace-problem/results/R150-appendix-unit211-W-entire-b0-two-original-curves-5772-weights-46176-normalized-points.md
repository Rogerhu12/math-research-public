# R150：整个 W 的 b0 零支——两原权曲线、5772 权长度与 46176 个完整规范点

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 已成结论

在当前互异两值、物理 $D\ne0$ 的 W 原图上，整个 $b_0=0$ 支满足两个新的纯权条件
$$
C_{74}(e,k)=D_{78}(e,k)=0,\qquad
\gcd_{\mathbb Q[e,k]}(C_{74},D_{78})=1.
\tag{1}
$$
它们的总次数分别为 $74,78$，完整来源来自同一个原二次 $q_2$、
原六次 $\mathcal R_6$ 与新增完整值条件 $\mathcal N_5$。
所以共同仿射权方案的长度至多
$$
74\cdot78=5772.
\tag{2}
$$
这里的 gcd1 只用于排共同曲线，没有把它解释为二元理想含1。

本篇还给一个完整、保首项零的纸面纤维论证：
每个物理权点的 $\lambda$ 至多2个，$T$ 随之唯一；
原均值给同一个 f 的首一二次，至多2个 f；
$\rho^2=1-Q$ 至多2个，而两个原矩条件使 $\zeta$ 唯一。
因此整个该支的**完整有序规范不同点**至多
$$
5772\cdot2\cdot2\cdot2=\boxed{46176}.
\tag{3}
$$
(3) 是不同点上界，不是完整几何商的方案长度或自由秩。
尚未逐个返回这些有限权纤维，也未宣布该支为空。

## 2. 原值来源与 b0 全图恢复

沿
[纯值六／四／五次全图等价](R150-appendix-unit211-W-pure-lambda-T-six-four-five-entire-value-equivalence.md)，
令
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,
$$
$$
A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,\quad \delta=1-Q,\quad m=u-\ell,
$$
$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*,
$$
$$
b_0=2m\bigl(A_*T+uQ(3-2\lambda)\ell\bigr),
$$
$$
\mathcal C_4=2mDa_\Delta+MKb_0,\qquad
\mathcal R_6=MK^2-4m^2D^3 .
\tag{4}
$$
$M=\ell(2u-\ell Q)-u^2=4bc\delta$。
完整 N4 的 f 独立纯式为
$$
\mathcal N_5=2mD(Z_0^*+Dz_2^*)+MKz_1^*.
\tag{5}
$$
星号只是自由 f 系数中的常数项，没有施加物理 $f=0$。

其准确原来源是
$$
\begin{aligned}
\mathcal N_5={}&2mD\ell^2N_4(V)
 +Mz_1^{\rm full}H-2mDz_2^{\rm full}q
 -\frac{2f}{MQ}\mathcal C_4,\\
q={}&Ms^2-D,\qquad H=K-2mDs .
\end{aligned}
\tag{6}
$$
所以 (5) 是完整原值条件的必要式，尤其在 $b_0=0$ 时仍须保留。
本篇没有以该面上自动消失的 $\mathcal B_{\rm pure}$ 代替它。

在 $b_0=0$ 中，若 $A_*=0$，原式迫使 $3-2\lambda=0$；
这被当前 W 已独立排除的整个 $\lambda=3/2$ 支否定。
更明确地，
$$
A_*T=-uQ\ell(3-2\lambda)
\tag{7}
$$
右侧是已付单位，因此 $A_*$ 在该原支中是真单位。
这项支付仅用于整个 b0 零支。
令
$$
\kappa=\frac{uQ\ell}{A_*},\qquad
T=-\kappa(3-2\lambda).
\tag{8}
$$
$\kappa$ 及其逆 $A_*/(uQ\ell)$ 都只用当前已付单位。

又因物理 $mD\ell\ne0$，在此支
$$
q_2:=\frac{2a_\Delta}{\ell}
=\frac{\mathcal C_4}{mD\ell}=0.
\tag{9}
$$
本次新输入恰为将 (8) 代入同一点的
$$
q_2,\quad\mathcal R_6,\quad\mathcal N_5.
\tag{10}
$$
它们的实际 lambda 次数分别为 $2,6,5$。
其原来源及全部权尺度均已返回；没有倒 q2 的 lambda 首项。

## 3. 两个新标量的完整原组合

先只按既有纯权单位清分母和去支持，记三个归一输入仍为
$q_2,R_6,N_5$；每个归一尺度都乘回未归一 (10)。

对 $R_6,N_5$ 分别作 q2 的正幂伪除。
若 $h=[\lambda^2]q_2$，每步均满足
$$
h\,R-\operatorname{lc}(R)\lambda^j q_2=R_{\rm next}.
$$
同时保存并逐项返回
$$
h^rF=Q_Fq_2+R_F.
\tag{11}
$$
本次共9步，得到两条一次式
$$
R_1=a+b\lambda,\qquad N_1=c+d\lambda.
\tag{12}
$$
本节 $N_1$ 是 (12) 的伪余式标签，不是原极化方程的记号。

每个新组合均清三个实际原乘子的纯权分母，
只取消这三个乘子的共同多项式内容，再用约后的三个乘子重新组合 (10)，
逐 lambda 坐标返回。
因此共同内容为零的整个面保留；没有将原方程除掉该内容。

第一标量来自
$$
dR_1-bN_1=ad-bc .
\tag{13}
$$
第二标量来自固定二次／一次的三阶身份。写
$$
q_2=A\lambda^2+B\lambda+C;
$$
则
$$
d^2q_2-(Ad\lambda+Bd-Ac)(c+d\lambda)
=Ac^2-Bcd+Cd^2.
\tag{14}
$$
(14) 在 $d=0$、$A=0$ 以及两者同时为零时仍是原多项式身份。
两条标量均完整返回全部三个原输入；没有使用临时头的逆。

只剥已经付清的纯权支持后，(13)、(14) 分别给
$C_{74},D_{78}$。实际剥除按 gcd 层数记录：

| 标量 | k | Vbar | M | ell 原分子 | 仅本支的 Astar 原分子 |
|---|---:|---:|---:|---:|---:|
| $C_{74}$ | 3 | 1 | 1 | 1 | 6 |
| $D_{78}$ | 2 | 1 | 1 | 1 | 6 |

这些是脚本反复 gcd 的层数，不把它们冒称各未分解整因子的幂。
所有剥前、剥后与来源尺度均实际乘回。
两条新标量共用的实际乘子内容总次数68、1297项，
仅保其定义与 SHA，不保存40234字节的可重算系数。

## 4. 真实 QQ 结果与权长度

完整实际参数如下；它们唯一由固定新源码及原定义确定。

| 新权式 | e 次数 | k 次数 | 总次数 | 项数 | 定义字节 |
|---|---:|---:|---:|---:|---:|
| $C_{74}$ | 41 | 51 | 74 | 1587 | 59972 |
| $D_{78}$ | 43 | 55 | 78 | 1805 | 68525 |

SHA256：

- $C_{74}$：61f94d2de21fb53f992abded0c670a8f7e529319f38396ac904e77824d80b8b9
- $D_{78}$：59387d311d686962932c2d15325bf139b47d9ad6a19fa566c24cdab1f8e7bd2c
- 三实际乘子的共同内容：6de283dc72a7f7acfb86f07c237b8c30ca0df33da35f762d1709636f4cd14b9c

$D_{78}$ 是本次 q2／N5 新目标，与先行固定八阶结果所定义的
旧 $F_{78}$ 有各自独立的源码及哈希。
本次没有重算旧固定八阶或其因式。

QQ 多变量 gcd 实际返回非零常数1，故两曲线无共同不可约分量。
仿射 Bézout 给
$$
\dim_{\mathbb Q}\mathbb Q[e,k]/(C_{74},D_{78})\le5772.
$$
这一结论含交点重数；随后局部化原纯权单位或取更多原条件，只删减相应零维支持。
它不说二元理想本身等于整个环，也不证明存在任何物理解。

## 5. q2 的全部首项退化：每权至多两个 lambda

这里给新的完整纸面纤维论证，未增设运行门。
先由权定义直接算出
$$
MA_*+C_*=4uQ\delta\ell^2.
\tag{15}
$$
置 $n=2\lambda-1$。将 (7)、(8) 精确代入 (9)，得到
$$
q_2(n)=2M\ell Q(1-2n)+C_*(n^2+1)
 -8uQ\delta\ell\kappa^2(n-2)^2.
\tag{16}
$$
这一步的来源是完整原 q2：
$MA_*T^2+2MuQ(3-2\lambda)\ell T=-MA_*T^2$，
随后 (15) 合并全部 $T^2$ 项；没有遗漏剩余常数项。

令 $L=uQ\delta\ell\kappa^2$。
(16) 的三个 n 系数准确为
$$
a=C_*-8L,\quad b=-4M\ell Q+32L,\quad
c=2M\ell Q+C_*-32L.
$$
完整回乘给
$$
2c+b-2a=-16L.
\tag{17}
$$
若直接以 lambda 记
$q_2=a_2\lambda^2+a_1\lambda+a_0$，同一身份是
$$
\boxed{\quad a_2+3a_1+4a_0=-32uQ\delta\ell\kappa^2.\quad}
\tag{18}
$$
右侧由 $u,Q,\delta,\ell,\kappa$ 的已付来源是真单位。
所以在任何物理权点，q2 的三个系数不可能同时为零。
无论二次头、一次头怎样降次，q2 都是非零、次数至多2的 lambda 多项式，
因此每权点至多2个不同 lambda。
$T$ 由 (8) 唯一。

这里不倒 q2 的二次头，也不把非首一 q2 商无证称为自由二生成。

## 6. 完整规范点的恢复与界

原四均值／极化条件中两个 singleton 均值满足
[全图显式首一 f 二次](R150-appendix-unit211-W-lambda-T-f-global-monic-f-two-and-exact-I4-I6.md)
的已成纸面身份：
$$
\beta=2u-J/Q,\quad
u-\beta=-\frac{ue(k+4)}{\overline V},\quad
q_f=\frac{bc}{2u(u-\beta)}
 \left(E_{Be}+\frac{\ell\delta}{m}E_{Bo}\right)
=f^2+q_1f+q_0.
\tag{19}
$$
所有分母仅为当前原权单位。对每个允许的同一点 $(e,k,\lambda,T)$，
这个真正首一二次给至多2个 f；没有要求新的纯权 f 一次头非零，
也没有用三条 pair cofactor 代替同 f 相容。

随后 $t,V,W_1,x,y,A_1$ 都由先行 E0/N0/P1 仿射恢复唯一确定：
$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\quad
V=\frac{Jf-G+bcQt}{Q},\quad W_1=T_0/2+2uf,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{20}
$$
取 $\rho^2=\delta$ 至多2个选择后，
$b,c,p,q,X,Y,r,s$ 及完整原 Gram 唯一恢复。

最后，两个完整原值矩条件给
$$
s_{\rm val}=\frac{K}{2mD},\qquad
\zeta=\frac{T+u s_{\rm val}}{\ell}.
\tag{21}
$$
$m,D,\ell$ 在本篇的原范围均已付，故没有额外 $\zeta$ 二选一。
两个有序 singleton 值也由同一 $\rho,\zeta,T$ 唯一恢复。

于是每个物理权点至多 $2\cdot2\cdot2=8$ 个完整有序规范点，
结合 (2) 得 (3)。
可用规范坐标为 $(e,k,\rho,\lambda,T,f,\zeta)$，
也可使用由 (20) 唯一恢复的 $(e,k,\rho,x,y,t,\zeta)$。
这是固定原归一图的不同点上界，不计未经归一的矩阵轨道。

其余原均值、两个 singleton 个别 N/P 以及其他原条件仍须逐点满足；
它们只可能继续削减该有限集合。
本篇没有把必要值子系统当成完整问题的充分系统。

## 7. 唯一实际执行回执

- Actions run：46130465286；job：140934243412。
- 源 commit：6a974eeaaf02646bfdc9a4e2ff85fbfb90a14b34。
- 原源 blob：47281af16fdd0ad7500ecda377c3cb9f9d65e725。
- 源 SHA256：e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。
- 真实驱动时间：5.531909013 秒；子进程 RSS：92796 KiB；退出码：0。
- 数学最后完整 checkpoint：5.464842081 秒。
- stdout：7712 字节；SHA256：24f07c9c89a5f874ddc954359dc06eeff016d67bf20178f03131d2364d24809f。
- 真实 pull：2026-11-28 09:26:24.195267 UTC；前后均为上述源 commit，两 README 无变化。
- 170 次精确多项式除法乘回、12 个原 lambda 坐标返回、9 次伪除步、
  132 个已付支持乘回、2 个完整 QQ gcd 除法返回。

固定首次预算为180秒／4 GiB，正常结束。没有资源失败，没有延时或重跑。
只保存源码、参数定义和小回执；不保存两条大权多项式或任何可重算矩阵缓存。

源码：
[新 b0 的完整 N5 两目标](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)；
[首次输入说明](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542-input.md)；
[实际小回执](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-receipt-8542.json)。

(5)–(14) 的新实际返回已完成；(15)–(21) 是完整纸面纤维与恢复证明。
它们不等待附加计算，也不把当前有限支宣布已排空。
