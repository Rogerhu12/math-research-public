# 当前 W、$b_0=0$、负 $e$ 射线的正 $\mu=2\lambda-3$ 中心：三个完整原必要式的新首次输入

日期：2026-11-29（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127。

## 1. 已付范围与本次目标

只在现有一般 unit211 的当前 W 原物理图、$D_{\rm phys}\ne0$、$b_0=0$ 上工作。沿用该图已证明的原权单位及 $A_*$ 单位；$A_*$ 只在本 $b_0$ 整支支付，不向补图外推。所有原均值、个别 N/P 与完整原值条件仍须在同一点成立。

已完成且不重跑的来源如下：

- [整个 W 的 $\lambda=3/2$ 原排除](../results/R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)，当前树正文 blob df6e590338d43e6fe2dd41023c5dbd3d8e474864。
- [十一原式最低项与 $\lambda=3/2$ 剩余中心](../results/R150-appendix-unit211-W-b0-eleven-original-initials-and-lambda-three-halves-residue-center.md)，唯一 actual run 46162974839 / job 141034199881：在 $p=1009$、$(v(e),v(k))=(-a,0)$、$a>0$ 的全部五个 $t$ 赋值格和 $t=0$ 下，只付 $(2\bar\lambda-3)^2$。该次没有单位返回，没有支付 $\bar k+2$。
- [原奇 N/P 与完整 NV 的低 $D$ 理想压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，完整正文 blob f4e6d79b9956e5a8b39e4a4f88bfbe17eee945f0；这里只沿用原值身份，不引入 $D$ 逆。

因此，任何本射线上的实际特征零原点都满足
$$
\mu=2\lambda-3\ne0,\qquad v(\mu)>0,\qquad
\eta=\frac{v(\mu)}{-v(e)}>0.
$$
$\bar\lambda=3/2$ 仅为剩余中心，绝不令原 $\lambda$ 恒等于 $3/2$。本次对全部 $\eta>0$ 重新构造三个必要式的初始理想；不使用 $t$，不预设 $\bar k=-2$，也不运行十一原式的旧算法。

唯一新目标：在每个新格中用三个实际初始式返回 $1$，或返回真实属于该三式 Laurent 理想的纯 $\bar k$ 中心多项式。失败或未得到的格完整保留。只证明初始必要条件，不把模 $1009$ 的理想结果直接提升为特征零整个 W 排空。

## 2. 唯一小依赖与必要定义边界

新源：

2026-11-28-unit211-W-b0-positive-mu-center-three-original-initials-8542.py

冻结 SHA256：

756fc12c1f328125ae693db0e61ac9fc54dfb76371960e1eaa4b2c926e967136

资源：从新源启动起绝对 180 秒、4 GiB；建议外层 195 秒。不得增限或为未返回格重新执行同门。

唯一依赖放在运行器临时同目录：

2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py

该完整源 blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725，11675 字节，SHA256：

e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8

只读其前 6749 个 ASCII 字节，SHA256：

53a8d55ef6bcc8dd0eb233ef387420f5e2d40c04c0418ff493d82aa605b1eef9

边界恰在 q2,R6,N5=basis 后、def combine(tag) 前。AST 删除旧顶层断言、旧输出、旧统计校验循环及旧时钟/资源设置；保留必要算术、三个原式定义、只按旧付权支持作输入归一的定义。内层不会重置新源的绝对截止或硬内存界。

不进入旧 C74/D78 标量、全 QQ gcd、固定结式、旧 $\lambda$ 首项，或新十一式最低项门。重建这三个已知必要多项式只是新 $\mu$ 初始理想的系数定义，不登记为新的旧结论验证。

## 3. 三个原必要式及同点来源

原权图为
$$
u=e+1,\quad Q=ek,\quad \bar V=(e+1)k+2,\quad
\delta=1-Q,
$$
$$
\ell=\frac{u((k+2)^2-2ek)}{k\bar V},\quad
m=u-\ell,\quad
M=\ell(2u-\ell Q)-u^2,\quad bc=\frac{M}{4\delta}.
$$
沿用
$$
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q,\quad
P_f=T_0(J-Q),\quad \Phi=T_0+4u-4+Q.
$$
令
$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2,\quad
\kappa=\frac{uQ\ell}{A_*},\quad T=\kappa(2\lambda-3).
$$
本次仍在完整 $b_0=0$ 图，因为
$$
b_0=2m\{A_*T+uQ\ell(3-2\lambda)\}=0.
$$
取
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell A_2T+2T^3,
$$
$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQ(3-2\lambda)\ell T+DC_*.
$$
三个必要原式是
$$
q_2=2a_\Delta/\ell,\qquad
R_6=MK^2-4m^2D^3,\qquad N_5.
$$
$N_5$ 是完整原 NV 的准确 $f$ 常数系数输入，不是施加物理 $f=0$。旧源保留的原身份为
$$
N_5=2mD\ell^2NV+M z_{1,\rm full}H
 -2mD z_{2,\rm full}q-\frac{2f}{MQ}C_4,
$$
其中
$$
q=M\sigma^2-D,\quad H=K-2mD\sigma,\quad
C_4=2mDa_\Delta+MKb_0.
$$
所以原值条件及 $q_2=b_0=0$ 确使 $N_5=0$；没有倒 $D$、$q_2$ 的 $\lambda$ 头或新范数。三个输入在同一 $\lambda,T$ 上，不能独立选根。

原输入归一只用该旧源明确列出的旧付权支持：$e,k,u,\delta,\bar V,k+4,P_{02},M,k+2,\ell,m,2\ell-1,A_*$。本次不新增任何权单位。付权归一在特征零原图合法，不要求这些单位的剩余值仍非零；后续只对归一后的真实必要多项式取初始式，不借其剩余值作逆。

## 4. 新上下文运输与整数化

旧 flint 上下文为 $(e,k,\lambda)$，新上下文为 $(e,k,\mu)$。逐单项式明确代入
$$
e^ik^j\lambda^r\longmapsto
e^ik^j\bigl((\mu+3)/2\bigr)^r.
$$
所有纯权分母和归一尺度必须逐项确认旧第三指数为零，再重嵌到新上下文；不把不同上下文对象直接当成同一系数对象。

若旧归一输入满足 $F_i=s_iR_i$，写成分子分母后，新源逐多项式核回
$$
F_i\,s_{i,d}R_{i,d}=s_{i,n}R_{i,n}.
$$
再以有理数分母最小公倍数和整数内容，把 $F_i$ 化成整本原多项式 $\widehat F_i$，保留非零有理常数尺度并核回
$$
\widehat F_i\,c_i=F_i d_i,\qquad
\widehat F_i(s_{i,d}R_{i,d}c_i)=s_{i,n}R_{i,n}d_i.
$$
整数化不是新几何局部化；三式的所有零点及原来源保持。源输出仅次数、项数、字节数、SHA 和小状态，不保存完整系数。

## 5. 全部严格正斜率的精确下包络

对 $\widehat F_i=\sum c_{abr}e^ak^b\mu^r$，定义
$$
w_\eta(a,b,r)=-a+\eta r.
$$
每个固定 $r$ 先取最小 $-a$。全部直线的下包络交点中只保留 $\eta>0$ 的真实最小值重合点；三个输入合并所有有理断点。

分区包含每个正断点、相邻开区间、从 $0$ 到首个正断点的开区间及最后一个无界开区间。开区间仅用有理样本识别恒定最低面，覆盖该整个开区间，不把样本当成唯一赋值。没有 $\eta=0$；原 $\mu=0$ 已由整个 $\lambda=3/2$ 原排除支付。任何非零代数点上的有限正 $\eta$ 均在此分区中。

取代数闭剩余域并一致重标赋值参数，使 $e$ 的首系数为 $1$。$\bar k$ 和 $\mu$ 的首系数 $\bar\mu_{\rm lead}$ 均非零。初始式落在
$$
\mathbb F_{1009}[\bar k^{\pm1},\bar\mu_{\rm lead}^{\pm1}].
$$
这里 $\bar\mu_{\rm lead}$ 不是原 $\mu$ 的零剩余值，而是正阶项的非零首系数。

只有最低几何面包含 $1009$ 单位系数时才据此作模初始约束。若最低面所有整数系数均被 $1009$ 整除，本次完整保留该格，不擅自移动到下一面或断言排空。

## 6. 三源 Laurent 返回与允许结论

每个初始式只除去 $\bar k,\bar\mu_{\rm lead}$ 的共同单项式及非零 $\mathbb F_{1009}$ 常数，完整保留该 Laurent 正规化乘子。新 Buchberger 行使用消去次序 lex$(\bar\mu_{\rm lead},\bar k)$；每次减法、单项式移位、S 对及行正规化都同步运输三源乘子并回乘。互素首单项式仅使用普通乘积判据。

若返回 $1$，必须最终把三源乘子与最初正规化乘子复合，并对三个未正规化初始式完整回乘为 $1$，才排除这个赋值格。

若没有单位返回，源只输出实际出现的纯 $\bar k$ 行 $G_j$ 及其完整三源来源：
$$
G_j(\bar k)=\sum_{i=1}^3\Omega_{ji}
 \operatorname{in}_\eta(\widehat F_i).
$$
这给真实必要中心，不宣称这些 $G_j$ 单独完整呈示整个余理想，不预选其根，不断言有实际剩余点。未得到纯 $\bar k$ 行也只保留该格。

全程不以模 $D$ 幂零、固定目标的非零余式或失败的单位搜索提升 QQ 结论。若所有新格均实际返回单位，才能按已有赋值必要性排除该条剩余射线；这仍不是其它五条射线、全 W 或普通不变子空间问题的结论。若仍有格或中心，则按实际输出另做真正新原输入。

## 7. 首次执行与记录边界

本输入尚未执行。只请求上述冻结源的一次 180 秒 / 4 GiB 实际运行。完整数学记录必须区分：三个新中心多项式已返回、全正斜率分区已返回、各格原来源已返回、是否有单位，以及资源或实现中断发生的位置。

不重跑已成 47281 标量、c55c 十一式格、旧七式格、旧有限权曲线或任何冻结门。若发生资源边界，按最后完整来源记录并更换真正新输入；不能增加时间、换素数或把同目标改序后重播。
