# R150 附录：正确 Phi 的整 ell-half 直接原 z 证书与二十权覆盖

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

**状态：唯一首次实际完整返回。** 在当前正确 $\Phi=0$、distinct-singleton、物理 $D\ne0$ 原图的整个 $\ell=\tfrac12$ 上，六个未作三规则约化的原方程给出

$$
C_{20}(u)\,z\in I_6,\qquad z=Qt,
\tag{1}
$$

其中 $C_{20}$ 是二十次多项式。实际 QQ 因式分解只有一个二十次因子、重数一。因此本图的不同权对 $(u,Q)$ 至多二十个；整个 $C_{20}=0$ 上的 $\lambda$ 和原值纤维仍保留。本文没有宣布整 ell-half、整 Phi 或普通不变子空间问题已解决。

这一结论加强[先前整 ell-half 的 $C_{114}^2z$ 原正目标](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-positive-z-and-114-weight-cover.md)。新输入直接使用十八个低次原列，没有重算旧 $\lambda$ gcd、三十列模块、旧 LCM 或 C114。完整定义见[本次输入](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-direct-raw-degree-three-z-certificate-8542-input.md)、[唯一源码](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-direct-raw-degree-three-z-certificate-8542.py)及[小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-ell-half-direct-raw-degree-three-z-certificate-8542-execution.json)。

## 1. 整条权曲线与合法系数环

令

$$
s=u-1,\qquad Q=4(u-1)(u-2),\qquad
\delta=1-Q,\qquad \ell=\frac12.
\tag{2}
$$

使用可逆常数平移

$$
\epsilon=\lambda-\frac12,\qquad \tau=T+\frac12.
\tag{3}
$$

令 $\mathcal A$ 为在 $\mathbb Q[u]$ 中只反演下列原已付支持所得的系数环：

$$
U=u(u-1)(u-2)\delta(2u-1)
       \bigl(2(u-1)^2-3\bigr).
\tag{4}
$$

$u$ 来自独立的[原零基均值排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)，$2u-1$ 来自当前整等权排除及其[静态来源记录](../notes/2026-11-28-unit211-Phi-corrected-equal-weight-m-unit-static-provenance-8542.md)，最后一个因子来自[正确整个 B 零支排除](R150-appendix-unit211-Phi-zero-true-entire-Bzero-original-exclusion.md)在 (2) 上的拉回。$Q,\delta,P_{02},P_f,bc$ 的其余分母和单位只沿原图支付。没有使用已撤回的错误 compact 均值链。

整曲线上的恢复为

$$
\begin{aligned}
m&=u-\tfrac12,&M&=-2s^2,&bc&=-\frac{s^2}{2\delta},\\
T_0&=-4s^2,&J&=-4s,&P_{02}&=4s^2(u-2),&
P_f&=16s^4,\\
f&=\frac u2-(u-2)\epsilon-\frac{(u-2)^2}{s}\tau.
\end{aligned}
\tag{5}
$$

令 $G=\lambda P_{02}+sT_0$、$P_c=QP_{02}(\ell+T)-GT_0$。源真实返回 $P_ff+P_c=0$。再取

$$
t=z/Q,\quad V=(Jf-G+bcz)/Q,\quad
W_1=T_0/2+2uf,
$$

$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
A_1=2f-2V+2bct.
\tag{6}
$$

此次完整返回的两个中心身份是

$$
V-f=(u-2)\tau+bct,\qquad A_1=-2(u-2)\tau.
\tag{7}
$$

它们是整多项式身份，不施加 $\tau=0$、$A_1=0$ 或 $t=0$。本源也没有反演 $\epsilon,\tau,z$ 或 $D$。

## 2. 六个未约化的完整原式

在 $\rho^2=\delta$ 的整个二次代数中恢复

$$
b=\ell/2+\frac{m\rho}{2\delta},\quad c=\bar b,\quad
p=1+\rho,\quad q=1-\rho,\quad
X=x+\rho y,\quad Y=\bar X,
$$

$$
r=X-(1-\ell)p-ct,\qquad
s_g=Y-(1-\ell)q-bt.
$$

原 Gram 四行为

$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s_g),\quad
g_B=(p,r,0,t),\quad g_C=(q,s_g,t,0).
\tag{8}
$$

所有平方与极化均用真实 dual 乘法

$$
(vw)_1=v_0w_1+v_1w_0.
\tag{9}
$$

特别，$E_1$ 中的项是 $-2(d^2)_1=-4d_0d_1$。源从同一完整 $\operatorname{tr},DK,N_4,P_2$ 定义构造

$$
(F_1,\ldots,F_6)=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{10}
$$

这里

$$
N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)
        -4\lambda wP_{02},\qquad w=\lambda-1-T,
$$

$$
\begin{aligned}
NS&=bN_4(g_B)+cN_4(g_C)
       -2\lambda P_{02}(\ell+2T+A_2),\\
PS&=bP_2(g_B)+cP_2(g_C)
       -P_{02}(\ell+3T+3A_2+B_3).
\end{aligned}
\tag{11}
$

其中 $A_2=2\lambda^2-2\lambda+1$、$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。

原 $E_0=0$、$N_4(g_0)=2\lambda P_{02}$、第一 jet $P_{\rm jet}=3wP_{02}$ 与共轭身份均实际返回。六式奇部及归一完全来自 (8)，不把 weighted N/P 代替个别值条件；其余个别 N/P、完整 $N_4(V)$ 和物理几何约束继续保留。

令 $I_6=(F_1,\ldots,F_6)$ 于 $\mathcal A[\epsilon,\tau,z]$。前四式几何总次数至多二，后二式至多三。这里没有对六式先取三生成元余式。

## 3. 二十普通坐标中的十八个原列

固定容器为全部普通单项式

$$
\epsilon^a\tau^bz^c,\qquad a+b+c\le3.
\tag{12}
$$

这是二十维系数容器，不是商代数。固定十八个原列为

$$
F_i,\ \epsilon F_i,\ \tau F_i,\ zF_i
\quad(1\le i\le4),\qquad F_5,\ F_6.
\tag{13}
$$

每列仅乘其原已付纯 $u$ 分母。把列写成 $m_jD_jF_{i(j)}$，得到 $\mathbb Q[u]$ 上的 $20\times18$ 矩阵 $B_{\rm raw}$。每列全部二十坐标都重新组回原多项式。

唯一固定矩形 Bareiss 输入实际给出：

- $\mathbb Q(u)$ 上秩为十八；
- 原恒零行恰为常数和 $\epsilon$ 两个坐标；
- 目标列 $e_z$ 一致，全部二十行始终保留；
- 完整回代后，二十坐标均返回 $B_{\rm raw}v=e_z$。

本次 2280 个 Bareiss 更新乘积和总计 2333 个精确多项式除法乘回全部完成。未知纯 $u$ 主元只参与产生有理系数；它们没有因此成为物理单位。

## 4. 六个最终原乘子的一次分母清除

先把十八个回代系数真正合并到六个原乘子：

$$
\Omega_i=\sum_{j:\,i(j)=i}v_jD_jm_j.
\tag{14}
$$

每个 $\Omega_i$ 完整约消后，本次直接返回

$$
\sum_{i=1}^6\Omega_iF_i=z
\quad\text{于 }\mathbb Q(u)[\epsilon,\tau,z],
\tag{15}
$$

并另外返回全部二十普通几何系数。这里返回的是完整未约化原多项式。

只取这六个最终乘子的真实分母 LCM，记为 $\Delta_u$。其实际次数为二十六、项数二十七，规范参数 SHA256 为

$$
\texttt{f161edba1f417befd7aca7ab135d4c79ffa31de1c101e14055a0bed029c8cadf}.
$$

源先逐个返回六条 $\Delta_u\Omega_i$ 精确整除，再返回

$$
\sum_i(\Delta_u\Omega_i)F_i=\Delta_u z.
\tag{16}
$$

只沿 (4) 剥去已付部分，得到

$$
\Delta_u=P_{\rm paid}C_{20},\qquad P_{\rm paid}\in\mathcal A^\times.
$$

最后六个原乘子再次完整合并，实际返回

$$
\boxed{\ \sum_i\frac{\Delta_u\Omega_i}{P_{\rm paid}}F_i
          =C_{20}(u)z.\ }
\tag{17}
$$

所以这是 $\mathcal A[\epsilon,\tau,z]$ 中的原一次理想身份。清分母指数是 **一**。临时主元若已在最终六个乘子中取消，(17) 自身延拓到其零点；未取消的新纯 $u$ 极点全部保留在 $C_{20}=0$。

最后六个原乘子的分母次数依次为 $5,5,5,6,4,4$，这些分母全部通过 (4) 的旧单位核对。未引入新几何逆或 $D$ 逆。

## 5. 实际二十次因子与二十权覆盖

$C_{20}$ 的次数恰为二十，共二十一项，其规范参数 SHA256 为

$$
\texttt{01e360b988892d68755864adae1520933535e6c79faf79bb667f1eec33eeb3cb}.
$$

在先完成 (17) 的 checkpoint 后，同一首次运行继续作 QQ 因式分解。结果只有一个二十次因子、重数一，完整乘回成立；该原始因子规范 SHA256 为

$$
\texttt{9034b6927e4b9097da053a88284bf004a5f0771c3339efdf14a4562af2b9bb5c}.
$$

两个 SHA 对应首一覆盖与因式分解采用的因子归一，不能混用成同一字节串。本次不保存可再生系数载荷或数据分片。

由[正确整个 $t=0$ 原排除](R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)，当前物理原点的 $z=Qt$ 非零。因此 (17) 给

$$
C_{20}(u)=0.
\tag{18}
$$

因为 $Q$ 在 (2) 中由 $u$ 唯一确定，当前整个 ell-half 原图至多有二十个不同的 $(u,Q)$ 权对。这是对原 C114 覆盖的真实缩小，且新覆盖为一次、QQ 平方自由。

**此处不把二十权点提升为二十个完整规范原点。** 在全部 $C_{20}=0$ 上，$\lambda,\epsilon,\tau,z$ 及其余完整原值条件仍保留。二十次因子不可约只决定后继可以使用完整 $\mathbb Q[u]/C_{20}$ 常数域，不将它支付为非零单位，也不选择某个复嵌入代替整个原支。

## 6. 唯一实际执行与准确边界

本次唯一实际 [run 46141521771 / job 140968304419](https://github.com/Rogerhu12/math-research-public/actions/runs/46141521771/job/140968304419)：

- 原数学阶段 0.863918801 秒；driver 0.938861547 秒。
- driver 峰值 40544 KiB，源码退出码 0；120 秒、1 GiB 的原预算未改变。
- 源 blob 6ee987687964a48e1d4ffec6abf1230018de5263；源 SHA256 为 32e949c11469da6350c0403e2aead13d3558fce80f64b78021e3f1f65d87b15e。
- 源提交 1d259ac3f394c6288c770b8dd1bac733358cd418；真实 pull 后为 4a01d17a28a5f2397674999692752ad6839b4966，两份规则未变。
- 原 stdout 8124 字节，SHA256 为 951f7f8fd2321c3b9b208f310c6cc0843f8b8f74da91d43e23f863898d13d83c。
- 二十矩阵坐标、二十原多项式坐标、六个终端分母乘积及 QQ 因子乘回全成。

没有重放旧 C114 门，没有运行增加次数后的矩阵，没有隐藏任何 $C_{20}=0$ 纤维。后继目标必须从整个二十次常数域或不同的新原条件继续；本次已完成的原 $z$ 证书无需重跑。
