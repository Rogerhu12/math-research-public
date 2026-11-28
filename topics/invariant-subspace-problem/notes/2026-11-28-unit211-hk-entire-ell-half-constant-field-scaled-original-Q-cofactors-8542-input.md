# 新输入：碰撞图整个 ell=1/2 的二次常数域与缩放原 Gram

日期：2026-11-28（UTC）。这是首次执行前的输入说明，没有新执行回执，不预报整支排除。

唯一源码：2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542.py  
blob：53d57ae6baf7a9fdf3867a95952833a570317797  
SHA256：44b7c44c5e4ba5408a8662e6f2579be23c6bf9effd0d9d2a59993eb827ca79cb  
准确 UTF-8 字节数 21885；已 fetch 精确回读，尚未执行。  
预算：180 秒、4 GiB，建议外层 195 秒。自含，零依赖。

## 1. 原图、单位与新目标

只研究当前正确的原 singleton 值碰撞 $h=k$ 图，其中 $\ell=1/2$ 的整个权支。这里的 $h,k$ 不是 W 权参数。

原值参数为
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad
w=\lambda-1-T,\quad h=k=1+\xi.
$$
本源直接工作在 $\Delta\ne0$ 图。独立刚完成的原 $C_1,C_2,C_4$ 整纤维与两个整谱域有限 DVR 单位返回，已关闭当前正确 $\Delta=0$ 图；本次不重跑它们。

独立终证：
[R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md](../results/R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md)，完整 proof blob c3fe01ac550dfea6d4848063ecfd93a5f6f3245c，实际 receipt f5511465cfa47c9854b26f09cf48d887792cce6e。
即使把本次范围单列为 $\Delta\ne0$，新输入本身也不需要重放该终证。

正确原前置单位的来源为
[Pf 原源静态审计](2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)及
[正确小谱整支排除](../results/R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。
本次只使用当前原图已付 $u,u-1,Q,\delta=1-Q,bc,P_{02},\lambda,2\lambda-1,A,B,P_f$，以及本图的 $\Delta$。

这里没有物理 $D\ne0$ 假设。不得借 W 或正确 Phi 的 distinct-singleton 整 $\ell=1/2$ 排除。$\Phi$、$u-\ell$ 及任何新消元首项都不倒置。

新目标：在整二次常数域先专门化，再构造八条完整原条件；固定 $Q$ Sylvester 原常数目标后，作整个 $K[u]$ 的 Bézout。只在实际原目标为 $1$ 时排本图；非恒定 $g(u)$ 只给必要整 $u$ 覆盖，全部 $Q$ 纤维与首项退化保留。

## 2. 整二次常数域和原单位 u-2

直接恒等式
$$
2A^3-B^2=(2\lambda-1)^2(3\lambda^2-2\lambda+1)
$$
配已付 $2\lambda-1$ 给整个新谱域
$$
K=\mathbb Q[\lambda]/(3\lambda^2-2\lambda+1).
$$
判别式 $-8$，故为二次域。源始终用 $1,\lambda$ 基，不选单个复根或模根。

域中
$$
\lambda^2=(2\lambda-1)/3,\quad
A=(1-2\lambda)/3,\quad B=(1-5\lambda)/9,
$$
$$
\xi=1-\lambda,\quad \ell=\tfrac12,\quad T=(1-\lambda)/2,\quad
h=k=2-\lambda,\quad w=\tfrac32(\lambda-1),
$$
$$
S=5-4\lambda,\qquad \eta=4-3\lambda.
$$
置
$$
m=u-\tfrac12,\quad a=\tfrac12,\quad
M=u-u^2-Q/4=\delta/4-m^2,\quad bc=M/(4\delta).
$$
因此 $M=4bc\delta$ 原已付。沿一般原定义
$$
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3
$$
有完整身份
$$
T_0=J-Q=2M,\qquad P_f=4M^2,\qquad P_{02}=-2M(u-2).
$$
故 $u-2$ 由原 $P_{02},M$ 自动付成单位。所有这些恒等式在源中先于新原 Gram 和投影逐式返回；不把参数整理本身称为排空。

## 3. 同一点 Cramer 和统一尺度 H

完整原值两线为
$$
P_ff+bc\,\Phi z+P_c=0,\qquad
N_Ff+bc\,S\xi z+N_C=0,\qquad z=Qt,
$$
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
N_F=(3-4\lambda)Q+J\xi\eta,\qquad
N_C=\eta(-G\xi+Qwu).
$$
定义
$$
\Delta=\Phi N_F-S\xi P_f,\quad
T_{\rm num}=P_fN_C-P_cN_F,\quad
F_{\rm num}=S\xi P_c-\Phi N_C.
$$
则同一点
$$
f=F_{\rm num}/\Delta,\qquad z=T_{\rm num}/(bc\,\Delta).
$$
源先核
$$
P_fF_{\rm num}+\Phi T_{\rm num}+P_c\Delta=0,\qquad
N_FF_{\rm num}+S\xi T_{\rm num}+N_C\Delta=0.
$$
未倒 $\Phi,N_F$ 或其他斜率，也没有任意配对不同投影根。

为避免形成 $\Delta$ 分式，令原单位 $H=M Q\Delta$，用波浪号表示所有 Gram 坐标统一乘 $H$。置
$$
V_{\rm num}=JF_{\rm num}-G\Delta+T_{\rm num},\qquad
W_{\rm num}=M\Delta+2uF_{\rm num}.
$$
直接定义多项式
$$
\widetilde f=M QF_{\rm num},\quad
\widetilde V=M V_{\rm num},\quad
\widetilde t=4\delta T_{\rm num},
$$
$$
\widetilde x=(u-\ell Q)V_{\rm num}-mQW_{\rm num},\quad
\widetilde y=\ell QW_{\rm num}-uV_{\rm num},
$$
$$
\widetilde A_1=2M[(Q-J)F_{\rm num}+G\Delta].
$$
这些正是原
$$
V=(Jf-G+bc z)/Q,\quad W_1=T_0/2+2uf,\quad
x=((u-\ell Q)V-mW_1)/M,\quad y=(\ell W_1-uV)/M,
$$
$$
A_1=2f-2V+2bc\,t
$$
乘 $H$ 后的式子。源逐项核回 Cramer、$A_1$、$bX+cY$ 与 $bpX+cqY$，没有增加自由几何坐标。

## 4. 真 dual Gram 和八条完整原条件

在 $\rho^2=\delta$ 中置
$$
b=\ell/2+m\rho/(2\delta),\quad c=\ell/2-m\rho/(2\delta),\quad
p=1+\rho,\quad q=1-\rho,
$$
$$
\widetilde X=\widetilde x+\rho\widetilde y,\quad
\widetilde Y=\widetilde x-\rho\widetilde y,
$$
$$
\widetilde r=\widetilde X-aHp-c\widetilde t,\quad
\widetilde s=\widetilde Y-aHq-b\widetilde t.
$$
直接构造 $H$ 倍原对称 Gram
$$
\widetilde K=
\begin{pmatrix}
0&0&Hp&Hq\\
0&\widetilde A_1&\widetilde r&\widetilde s\\
Hp&\widetilde r&0&\widetilde t\\
Hq&\widetilde s&\widetilde t&0
\end{pmatrix}.
$$
头两坐标始终用真 dual germ：
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0.
$$
特别 $(d^2)_1=2d_0d_1$，没有承继已撤错误的 $(d_1)^2$。

令 $\mathbf1=(1,0,1,1)$、
$\tau(v)=av_0+v_1+bv_2+cv_3$、
$D\widetilde K(v)_j=\tau(\widetilde K_jv)$、
$d=D\widetilde K(\mathbf1)$、$F_2=\tau(d)$。
源核
$$
d_0=Hu,\quad d_2=\widetilde X,\quad d_3=\widetilde Y,\quad F_2=2\widetilde f.
$$
未压缩原定义为
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
       +2F_2\tau(v)^2+\tau(vD\widetilde K v),
$$
$$
P_2(v)=\tau[(v-\tau(v)\mathbf1)^3].
$$
设四行是 $g_0,g_1,g_B,g_C$。先完整返回 $E_0=0$，
$P_2(g_0)=H^3P_{02}$，$N_4(g_0)=2\lambda H^3P_{02}$，
第三矩 polar $P_{\rm jet}=3wH^3P_{02}$，
以及完整 $N_4(1,w,h,h)=0$。末式在 $\widetilde K$ 下是 $H$ 倍原 $N_4(V)$，不是只保其一个 $\Phi$ 倍数。

八行固定为
$$
E_1,\ E_{B,e},\ E_{B,o},\ N_1,\
N_{B,e},\ N_{B,o},\ P_{B,e},\ P_{B,o}.
$$
这里
$$
N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wH^3P_{02},
$$
$$
N_B=N_4(g_B)-2\lambda h^2H^3P_{02},\quad
P_B=P_2(g_B)-h^3H^3P_{02}.
$$
C 行由共轭逐式核回，保完整两个符号分量。前三行是 $H^2$ 倍原均值，后五行是 $H^3$ 倍原值条件。$H$ 已付，所以其局部化原理想不变。物理 $D$ 从不取逆。

## 5. 系数运算与严格单位表

底层是 $K[u,Q]$ 的两个 QQ 多项式坐标。$\rho$ 层之下仅 $\delta$ 的正幂为分母；缩放原 Gram 不实际除 $\Delta$ 或 $M$。

对于 $a+b\lambda$，共轭及范数为
$$
\overline{a+b\lambda}=a+\tfrac23b-b\lambda,\qquad
{\rm Nm}(a+b\lambda)=a^2+\tfrac23ab+\tfrac13b^2.
$$
源码只以范数作两件事：

- 非零常数域元素求逆，整个 $K$ 上乘回 $1$；
- 检查多项式精确整除：先乘共轭，两 QQ 分量都精确除范数，再完整乘回原除数。

第二件事是多项式等式，绝不把范数加入物理单位表。不能整除就保留原因子；没有剥掉另一嵌入的范数零面。

八行只清 $\delta$ 分母，再按完整因子整除
$$
u,\quad u-1,\quad u-2,\quad Q,\quad\delta,\quad M,\quad\Delta.
$$
每一步乘回，每行保准确缩放；$u-2$ 由第 2 节原式支付。其余纯权内容、$Q$ 头、结果式因子、$\Phi$、$u-\ell$ 全留。非零常数域系数可归一，因为两个嵌入下都非零。

## 6. 固定 Q cofactor 保全部首项零

事前固定对顺序
$$
(E_1,E_{B,e}),\quad(E_1,E_{B,o}),\quad(E_1,N_1),
\quad(E_{B,e},N_{B,o}),\quad(E_{B,o},P_{B,o}).
$$
先得整 $K[u]$ 单位即停；不换点或素数。

给定原 $Q$ 多项式 $F,G$，在整个 $K[u]$ 上次数 $m,n$，固定 $m+n$ 行
$$
F,QF,\ldots,Q^{n-1}F,\quad G,QG,\ldots,Q^{m-1}G
$$
对 $1,Q,\ldots,Q^{m+n-1}$ 的矩阵 $S$。转置增广 $e_0$，作分数自由消去和精确回代。每个整除均核
$$
\text{new entry}\cdot\text{previous pivot}
=\text{pivot product difference}.
$$
最后实际返回所有列
$$
\mu S=C(u)e_0^{\,t}
$$
和完整二元原身份
$$
\mu_F(Q)F+\mu_G(Q)G=C(u).
$$
临时主元和最终首项都未付为物理单位；这属于整个 $K[u,Q]$，故全部主元零与次数下降纤维保全。固定矩阵恒奇异时准确记录零目标；若一输入原来与 $Q$ 无关，它本身就是原常数目标。

$C(u)$ 只剥 $u,u-1,u-2$ 完整因子及非零常数域倍数，其他所有 $u$ 因子保留。

## 7. 整 K[u] Bézout接回八原源

一元运算仍在整个 $K$ 上。每除法乘回，每次 xgcd 核
$$
s C_{\rm old}+t C_{\rm new}=g
$$
并保累积至所有已得原 scalar 的 Bézout，不选一个 $\lambda$ 嵌入。

设规范化原行
$$
F_i=\delta^{e_i}\widetilde{\mathcal E}_i/r_i,\quad
\widetilde{\mathcal E}_i=H^{d_i}\mathcal E_i,\quad d_i\in\{2,3\},
$$
其中 $r_i$ 都是第 5 节原单位的明确乘积。每 scalar 所剥 $c_j(u)$ 同样是原单位。源码用已记录各因子的最大指数共同倍数 $E,R$，并完整验证全部 $E/c_j,R/r_i$ 多项式精除。

最终真的核
$$
\sum_{i=1}^8\Omega_i\,H^{d_i}\mathcal E_i
=R(u,Q)E(u)g(u).
$$
$R,E,H$ 全为已付原单位。这把固定矩阵、累积 Bézout和起点真 Gram 接到同一个原理想，不靠裸投影根、模秩或无证来源。

若 $g=1$，整个本次 $\ell=1/2,\Delta\ne0$ 图原理想为单位；合独立整个 $\Delta=0$ 排除才得当前碰撞图整 $\ell=1/2$ 排除。

若 $\deg g>0$，只取正倍数
$$
{\rm Nm}_{K/\mathbb Q}g=\overline g\,g
$$
作 QQ 必要 $u$ 覆盖，完整因式乘回。不倒范数、不剥新因子或重数，不声称 $Q$/几何纤维有限，更不宣布排空。

## 8. 执行与输出边界

这是先专门化的新整常数域原输入，不读取或重放已闭 $F_{99}/F_{300}$、旧 QQ joint-u-gcd、固定 17 阶谱覆盖、冻结 Loww 两个 $z$ 结式、W 的任何 $\ell=1/2$ 或 C74/D78 门。

只有一个 180 秒绝对闹钟及 4 GiB 硬界，没有嵌套前缀或扩限。输出只含小参数定义、次数、SHA、完整返回标记和准确成功/未闭范围；可重算系数不存文件、缓存、编码或分片。

只有实际内层断言、数学 checkpoint 和退出码可作回执。外层绿色不代表内层成功；触界后最后完整 checkpoint 以外不计结果。本文件不预记上述任何新执行已经通过。
