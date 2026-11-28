# W 自由 lambda,T,f：新原均值首一二次、纯权 f 头与六条纯值坐标必要式输入

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 新输入与范围

脚本：

- `2026-11-28-unit211-W-lambda-T-f-original-monic-two-pure-weight-head-and-scalars-8542.py`
- SHA256：f6d0afca90813e795bb67c80ba7906d3075e8e44e4875b73302de2f19a14825b
- 首次预算：180 秒、4 GiB 地址空间；零依赖。
- 此处只是未执行输入，不预记成功、次数、因式或排空。

这是当前互异两值、物理 $D\ne0$ 的 W 原权图。沿用
[全图显式首一 f 二次及完整 I4／I6](../results/R150-appendix-unit211-W-lambda-T-f-global-monic-f-two-and-exact-I4-I6.md)
的已完成纸证，真正新目标为自由 $(\lambda,T)$ 上三条原均值一次余式的三对 cofactor 和三个同 f 范数。
新源码从原四行 Gram 直接构造正确四式 $E_1,E_{Be},E_{Bo},N_1$，全程保持 $E_1$ 独立。
不运行旧 alpha/chi、native 动作、旧结式或冻结六维范数门。

本次不加入或重新计算 $N_S,P_S$，不把仅 I4 的运行范围写成完整 I6。
两者在已刊纸面定理中的十行结论仍是独立已成定理。

## 1. 原坐标与真 dual 乘法

权参数为
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},
$$
$$
\delta=1-Q,\quad m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2=4bc\delta .
$$
保持同点原恢复
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t=-\frac{P_f f+P_c}{bcQ\Phi},\quad
V=\frac{Jf-G+bcQt}{Q},\quad W_1=T_0/2+2uf,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
$$
源码逐项返回 $bX+cY=V$、$bpX+cqY=W_1$、$d=(u,2f-V-(1-\ell)u,X,Y)$、$\tau d=2f$，
并从真正原 Gram 返回 $E_0=0$、$N_4(\mathrm{row}_0)=2\lambda P_{02}$ 及
原 $P$ jet 为 $3(\lambda-1-T)P_{02}$。

dual 相乘固定为
$$
(v_0,v_1)(w_0,w_1)=(v_0w_0,v_0w_1+v_1w_0).
$$
因此 singleton B 的完整均值中是 $2pr$。
源码另完整返回
$$
E_B=ap^2+2pr+ct^2
 -2(apu+pd_1+ru+ctY)-2X^2+4fX.
$$
绝不调用曾撤回的 derivative 平方紧凑式。

$N_1$ 固定为真 $N_4$ 在 row0、row1 的极化减 $4\lambda(\lambda-1-T)P_{02}$，
保完整常数、一次及二次项。

## 2. 全图首一 qf 与双向原 I4

令
$$
\beta=2u-J/Q,\qquad u-\beta=-\frac{ue(k+4)}{\overline V}
=\frac{u\Phi}{2e}.
$$
$u-\beta$ 是既有纯权单位。$m$ 仅沿当前互异两值原等权整支排除支付，
不外推值碰撞图。

显式
$$
c_f=\frac{bc}{2u(u-\beta)},\qquad
q_f=c_f(E_{Be}+\ell\delta E_{Bo}/m)
=f^2+q_1f+q_0
$$
使用已付纯权分母，源码返回完整四原式组合及
$$
E_{Be}=c_f^{-1}q_f-\ell\delta E_{Bo}/m.
$$
它还核真二次头等式
$$
b^2c[f^2]E_B-bc^2[f^2]E_C=2u(u-\beta)(b-c).
$$

对 $F_i=E_1,E_{Bo},N_1$，取
$$
h_i=[f^2]F_i,\qquad r_i=F_i-h_iq_f=A_i+B_if .
$$
逐 f 坐标返回正反等式；$\deg_{\lambda,T}A_i\le2$、
$\deg_{\lambda,T}B_i\le1$。
若 $\tau_i$ 是该式的四原来源，则
$$
f r_i-B_iq_f=-q_0B_i+(A_i-q_1B_i)f
$$
的来源正是 $f\tau_i-B_i\tau_q$，也逐坐标完整返回。

故本次若全部断言成功，实际构成原 I4 在 $A[f]/q_f$ 中的完整六行两列呈示。
环境自由于 $(1,f)$；实际原理想商不被假设自由。
既不倒 $B_i$，也不倒任何新 lambda、T、f、D 或范数。

## 3. 真正新的纯权 f 一次头

由 $B_i$ 对 $\lambda,T$ 仿射，把其三个系数排成
$$
\mathcal B_i=([1]B_i,[\lambda]B_i,[T]B_i).
$$
后两列给固定三个 cofactor $\mu_i$，满足
$$
\sum_i\mu_i B_i=\det\mathcal B,\qquad
\sum_i\mu_i r_i=(\det\mathcal B)f+\sum_i\mu_i A_i.
$$
所有 $\mu_i$ 和这个 f 头都是纯权函数。
本门真正返回系数矩阵全部三个坐标以及完整四原式乘子；
再只取消四个实际乘子的共同纯权内容，
重新返回同一 f 一次原关系 $h f+a(\lambda,T)$。
整个共同内容零面保留，因为新行直接有约后的原来源。

该头不是零有理函数已有一个首次小精确计算：
在 $e=1,k=3$，原 Gram 加真有理二次扩张及已证总二次界给
$$
\det\mathcal B=\frac{879351616}{1012683}\ne0.
$$
源 blob d95dbf5c3be0b538d61e16b42301141c8a3ef108、
SHA ebe11ef8d8cee3f17064faf3bd40c5efe55d70f2af10158109b3e0ad8af12f7e；
小回执 5952b68095676015666b2171ba6c88ee5872782a。
真实 46550 次有理加乘、65 ms。
这只识别一个有理函数非零；不是物理解抽样，更不是全纤维排空。
本门不重做该计算，而构造完整 QQ 权头并将其整式因式全乘回。

只在实际完整权头剥旧单位后为非零常数时，才作
$$
f=-g(\lambda,T),\qquad g=a/h,
$$
并同时返回
$$
q_f-(f+q_1-g)(f+g)=g^2-q_1g+q_0,
$$
$$
r_i-B_i(f+g)=A_i-B_i g.
$$
这些是同 f 的完整反向消元，给 I4 的精确纯 $(\lambda,T)$ 呈示。
若还有任何未付权因子，则整个零面保持，源码不倒 h；
后续仍是完整六行与以下六必要标量，没有擅自缩小图。

## 4. 六个新的原常数目标

三对行给
$$
C_{ij}=B_jr_i-B_ir_j=A_iB_j-A_jB_i,\qquad \deg_{\lambda,T}C_{ij}\le3.
$$
每个同 f 范数还满足
$$
N_i=(A_i-q_1B_i-B_if)r_i+B_i^2q_f
=A_i^2-q_1A_iB_i+q_0B_i^2,\qquad\deg_{\lambda,T}N_i\le4.
$$
源码分别构造全部四个真实原式乘子，先完整返回目标；
再只对这四个乘子共同清纯权分母、约共同多项式；
最后用约后的四乘子重新组合原式，并逐 f 坐标返回。
因此共同因子为零的整个面仍由新原组合覆盖。
没有将原方程本身除以未付共同因子。

所得纯 $(\lambda,T)$ 标量仅可再剥已付纯权支持，剥前剥后实际乘回。
不剥新几何内容或头，不进行模空性提升。
三个 pair 和三个 norm 的列表本身不宣称足够；
完整相容对象始终是同一个 $q_f$ 下的六行原模。

目标恒零时准确输出恒零，不按不存在 cofactor 推空。
本门没有权投影、首项零排空、全 W 排空或新点数界目标。

## 5. 保存、资源及失败边界

源自含，没有嵌套脚本修改时钟或硬限制。
全部输出只给原定义、次数、项数、字节、SHA、乘回计数和必要小状态；
不输出或保存可重算的大系数、矩阵、编码片。
最终原式乘子仅在该进程内验证。

每个完整新 checkpoint 后才记录该部分已成。
若 180 秒或 4 GiB 触界，只保最后真正完成的原四式／qf／六行／各 scalar；
不得把未返回的后续列、norm、权曲线或排空标记成功。
不延长、换序或重放同门。
