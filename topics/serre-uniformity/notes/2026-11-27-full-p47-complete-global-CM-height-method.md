# 原 full47 完整第一层全局高度：有限计算与真实归一

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明计算方法；尚未得到此完整请求的实际数值。**
[R1100](../results/R1100-certified-original-level47-first-global-CM-height.md)
已经认证 $\Gamma(1)=818$；本请求直接消费该值，不重新计算其范数和。

## 1. 目标、整格与有限输入

取原 $q=4513$、$B=q+1-T_q$、$P_0=Bu_4$，
其中 $u_4=23y_{1728}-C_\infty$。
R1093已证明原完整 Mordell–Weil 整格
$$
M=\mathcal T_{\mathbf Z_q}P_0,\qquad
\log M=q\operatorname{Lie},\qquad
\operatorname{rank}_{\mathbf Z_q}M=73.
$$
这里 $B$ 在原整 $\mathcal T$ 中可逆，所有实际 CM-log 来源保R1093。

R1096给
$$
H=T_3+T_5,\qquad \mathcal T=\mathbf Z_q[H],\qquad
a=(T_2-1)/2\in\mathcal T^\times,\qquad Bu_{16}=aP_0 .
\tag{CH.1}
$$
$q$-local 高度对所有原奇指标
$B u_4,T_nB u_{16}$ 均在 $q^2\mathbf Z_q$；
完整规范泛函是
$$
\Gamma(T)=q^{-1}h(P_0,TaP_0),\qquad
q^{-1}h(SP_0,TP_0)=\Gamma(a^{-1}ST).
\tag{CH.2}
$$
不把第一次移动的 $a$ 漏掉，也不把 $B$ 从实际对数中删除。

新小奇基请求给73个实际 $n_i\le2255$，与$2\cdot47\cdot q$互素，
以及相对 $1,H,\ldots,H^{72}$ 的规范坐标矩阵 $C$。
其方法和公开消费者见
[小奇基方法](2026-11-27-full-p47-small-odd-Hecke-basis-method.md)。
本请求只按成功证书指定的73个指标重建并核全部hash，
不重开贪心搜索，不另选未标定的 Hecke 基。
$n=1$ 的旧值818直接作为输入，其余72个值才是新计算。

## 2. 全部局部项的准确有限展开

对每个新指标$n$，三个实际指标为 $m=n,nq,nq^2$，
权为
$$
c_0=q^2+3q+1,\qquad c_1=-2(q+1),\qquad c_2=1.
\tag{CH.3}
$$
沿 [R1097](../results/R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)，
全部奇好素数的 $G_\ell(m)$ 使用两个不交进程
$A=2209s$ 或 $B=2209s$，$A+B=8m$、$4\nmid s$。
对每项分解 $B$，只有唯一惰性奇赋值素因子$\ell$
才可能贡献；全部 $\ell\equiv1\bmod4$ 的原交数为零。
$\ell=47$交给坏模型，$q$项由R1094/96模$q^2$消失。
原 $\ell\mid n$ 的 quasi 层及一般复合$n$的非循环核，
已经包含在R1097的完整公式中。

对任一素数$\ell\ne q$，令
$$
F_q(\ell)=\frac{(\ell^{q-1}\bmod q^2)-1}{q}\pmod q.
$$
消费者直接累加
$$
W_{\rm odd}(m)=\sum_{\ell\ne2,47,q}G_\ell(m)F_q(\ell)\pmod q.
\tag{CH.4}
$$
这是原有限和的交换求和，不是抽样或漏掉大素数；
每个正范数项都按原$1/16$重数进入，
再乘它自己的$F_q(\ell)$。
因此无需保存长素数交数字典。

2处使用R1099的两个完整二平方和，保整数与半整数Hurwitz格，
得到 $G_2(m)$。
坏47水平使用R1098的
$$
H_{47}(m)=\frac1{16}
\sum_{\substack{0<47^3t<8m\\4\nmid t}}
r_2(t)r_2(8m-47^3t)(2+v_{47}t).
\tag{CH.5}
$$
三个$m$均是原有效Hecke，$\mathcal D_q$完整保$T_{q^2}$的非循环项。

坏47的五维Brandt模块只重建R1100已固定的$H_q,M_2$，
核原矩阵hash、weights和实际$E_4,E_{16}$标定。
令row向量
$$
v=v_{16}\bigl((q+1)I-H_q\bigr)^2.
$$
对各实际$n$读
$$
b_{\rm moved}(n)=(vH_n)_4.
\tag{CH.6}
$$
$H_n$和$H_q$交换且$(n,q)=1$，所以(6)准确等于
$\mathcal D_qb(n)$。核每个$H_n$的行和$\sigma_1(n)$、
原weighted自伴及交换；不枚举$q^2n$全部核。

完整新值为
$$
\boxed{
\Gamma(T_n)=
23^2\sum_{j=0}^2c_jW_{\rm odd}(nq^j)
+23^2\!\left(\sum_{j=0}^2c_jG_2(nq^j)\right)F_q(2)
+\left\{23^2\sum_{j=0}^2c_jH_{47}(nq^j)
       +23b_{\rm moved}(n)\right\}F_q(47)
\pmod q .
}
\tag{CH.7}
$$
这是原全局高度，符号沿$\chi_\ell(\ell)=-\log_q\ell$；
不能把其中的坏47交数强制改为正值。

## 3. 流式计算的完整性和空间界

小整数界固定为
$$
S_{\max}=\left\lfloor
\frac{8(\max n_i)q^2-1}{2209}\right\rfloor .
$$
parent只建立一次4-byte最小素因子表，fork后的四个worker只读共享。
素数按升序遍历至$\sqrt{S_{\max}}$，
从$p^2$起给仍为空的倍数赋$p$；
所以每个合数被其最小素因子赋值，
仍为空且大于1的整数必为素数。
表分解以整除循环完成，并核全部因子乘积。
更大的整数用官方Sage/PARI精确分解、`proof=True`。
没有随机素性替代或浮点等于零判断。

每worker的分解缓存和Fermat缓存都限65536条，
每完成一个$n$就释放其对象。
不保存范数项数组、完整局部字典或Fourier长级数。
范数贡献逐行用compact JSON更新SHA-256：
起始 `[`，相邻项插入逗号，结束 `]`，
所以其hash严格等于同一完整JSON列表的hash。
这是传输与内存优化，数学枚举范围未变。

四个worker只计算各自的新$n$；
按$n$由大到小分配，parent逐个接收成功值，
同一指标不重算。完整receipt要求全部73个指标出现且无重复。
超时或失败时只报告完成集合，不把剩余项设为零。

## 4. 从实际小Hecke基恢复完整高度泛函

令 $k=\mathbf F_q$，
$P(X)=\chi_H(X)\in k[X]$，$\deg P=73$，
原已认证判别式为2650。
原坐标矩阵$C$的第$i$行是$T_{n_i}$的升幂坐标。
写
$$
g_i=\Gamma(T_{n_i}),\qquad
\gamma_j=\Gamma(H^j).
$$
准确线性方程为
$$
C(\gamma_0,\ldots,\gamma_{72})^{\mathsf t}
=(g_i)^{\mathsf t}.
\tag{CH.8}
$$
这里的行/列由新消费者的实际$T_1,T_2,T_3,T_5$
与原Hodge矩阵逐项核过，未猜转置。

$\mathcal T/q\simeq k[X]/P$的迹配对完美，故存在唯一$\bar\kappa$使
$$
\Gamma(T)=\operatorname{Tr}(\bar\kappa T).
\tag{CH.9}
$$
用$P$的Newton identities精确算
$s_r=\operatorname{Tr}(H^r)$，$0\le r\le144$，
$s_0=73$。设 $G=(s_{i+j})_{0\le i,j\le72}$，
则$\det G=\operatorname{disc}(P)=2650$。
解
$$
G(\kappa_0,\ldots,\kappa_{72})^{\mathsf t}
=(\gamma_j)^{\mathsf t}
$$
便得$\bar\kappa=\sum\kappa_iX^i$。

另以resolvent独立固定同一迹归一：
若$P(X)=\sum_{k=0}^{73}p_kX^k$，令
$$
R(X)=\sum_{j=0}^{72}\gamma_j
          \sum_{k=j+1}^{73}p_kX^{k-1-j}.
$$
在$z=\infty$展开
$\operatorname{Tr}(\bar\kappa/(z-H))
=\sum_{j\ge0}\gamma_jz^{-j-1}$，
乘$P(z)$取多项式部分，得到$R(z)$。
在每个根$\alpha$处比较简单极的留数，得
$$
\bar\kappa\equiv R(P')^{-1}\pmod P.
\tag{CH.10}
$$
$P$平方自由，故$P'$可逆。
消费者要求(10)与Newton迹Gram的解完全相同；
这个核对直接针对高度坐标和迹归一。

## 5. 全73维高度矩阵的整单位条件

由(CH.2)，实际 $q^{-1}h$ 在基
$P_0,HP_0,\ldots,H^{72}P_0$上的乘数为
$$
w=\bar\kappa\,a^{-1}\in k[X]/P,\qquad a=(p_2(X)-1)/2.
$$
$a$已为原整单位，故完整高度配对为单位等价于
$$
\gcd(\bar\kappa,P)=1.
\tag{CH.11}
$$
原$P$有28个不可约因子：16次一次、6次二次、4次三次，以及11和22。
消费者逐因子读取$\bar\kappa$的余类和field norm，
不从16个一次块或$\operatorname{Tr}(\bar\kappa)=818$推断其余块。

准确的归一高度Gram行列式为
$$
\det(q^{-1}h)=\operatorname{disc}(P)\,
             \operatorname{Res}_X(P,w)\in k.
\tag{CH.12}
$$
理由是高度Gram等于trace Gram复合$w$的乘法矩阵，
而其行列式为$w$的代数norm。
(CH.11)、每个块的norm非零和(12)非零必须给同一判断。
若全部非零，原73维高度在这个真实MW整基中的行列式赋值恰73。
若某块为零，这也是合法完整结果，不更换完结标准。

## 6. 原16个一次块的实际log坐标

为了后续原QC函数的系数归一，另读取16个一次块。
若$H$的一个一次根为$r$，
$$
r_2=(p_2+2p_3+4p_5)(r)
$$
是原$H_2$标签。它匹配R1093公开的原规范eigenform：
第一个非零Hodge坐标为1，坐标hash在旧请求中固定。
记该实际标量
$$
\lambda_r=q^{-1}\log(P_0)(\omega_r)\pmod q.
$$
全部$\lambda_r$已为单位；直接消费原16个值与hash，不重算2208点级数。

若$x_r(P)=q^{-1}\log(P)(\omega_r)$，则$P=TP_0$给
$x_r(P)=\lambda_r\,T(r)$。因此原第一层全局双线性高度在这个
实际log坐标上，$q^{-1}h$ 的系数准确为
$$
\boxed{\quad\mu_r=\frac{\bar\kappa(r)}
                          {a(r)\lambda_r^2}.\quad}
\tag{CH.13}
$$
若改用未除$q$的原 $\log(P)(\omega_r)$ 作变量，$h$ 本身的系数是 $\mu_r/q$。这保留移动$a$、原$B$、实际微分规范和log平方。
本次输出这16个小派生系数及原$H_2$标签，
不把它们外推为28个块的全部性质。

## 7. 执行、存储与后继

仅本公开仓库Actions，原官方SageMath10.6 digest；
parent四核，单job数学18000秒、reserve120秒。
这是有限计算预算；到限不标完成，继续剩余指标或其它已授权方向。
请求固定实际基证书、已成$\Gamma(1)$、原输入hash、代码和方法，
每次输出都含真实checkout/run。

只提交脚本、参数、run/job、hash与小派生结论。
完整矩阵、Fourier和范数数组不入库、不上传artifact或Release。
成功只支付完整第一层高度及(CH.13)；
原八个CM管内的local-height排点和所有充分大$p$的Serre目标继续。
