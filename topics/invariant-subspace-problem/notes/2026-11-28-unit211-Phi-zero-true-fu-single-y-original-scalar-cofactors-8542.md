# 新输入：正确 Phi 的 f=u 单一原坐标与固定原 cofactor

日期：2026-11-28（Asia/Taipei）。未执行，不预记成功。

唯一源 SHA256 9d591ab41ed41cc7dbee8ac3e9ce326ef68348455751ae9ad1cea954a7d463cb。120 秒、1 GiB，全部必要前缀共享最初绝对截止。仅需正确 f62 算术源，不执行其四头或其后任何旧消元。本输入与整 B 原两列正幂目标分工不同：这里处理整个 $f=u$ 的二维权参数图，不施加 B=0。

## 1. 完整原参数图

当前保持正确 Phi、原 $Q(1-Q)P_fP_{02}bcD\ne0$，并令 $f=u$。已有[正确整 t=0 排除](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)给 $t\ne0$；新[整 u=3/2 原分支排除](../results/R150-appendix-unit211-Phi-zero-fu-entire-u-three-half-original-exclusion.md)仅在本 $f=u$ 支支付 $h=2u-3$。

记
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2)=\ell Q,\quad K=Q+4s,\quad A=4s^2-Q,
$$
$$
\theta=u-L,\qquad
M_n=2uL-L^2-u^2Q=4bcQ\delta.
$$
实际原单位为
$$
Q\delta sKLM_nh\ne0.
\tag{1}
$$
不假 $u$、A、B、旧第一头、$u-\ell$ 或 $u+Q-1$ 非零。

选择新原坐标
$$
y=A+2L\lambda.
$$
原 $E_0/N_0/P_1$ 及正确 R 的完整恢复是
$$
\lambda=\frac{y-A}{2L},\qquad
A_1=\frac{2sy}{Q},\qquad
T=-\frac LQ-\frac{Ky}{2QL},
$$
$$
t=\frac{2\delta(2\theta y+LA)}{M_nh},\qquad
V=u-\frac{sy}{Q}+bc\,t,\qquad W=\frac{4u^2-K}{2}.
\tag{2}
$$
该坐标全域覆盖当前 $f=u$ 原点，因为 L、h 均由 (1) 支付。

为保真正同点来源，在自由 t 下先令 $v_n=uQ-sy+bcQt,\ z=Qt$。正确 germ 组合精确为
$$
R=\frac{sz}{\delta}
 \left[-bc\,h\,z+\theta y+\frac{LA}{2}\right].
\tag{3}
$$
原点上 R=0，$sz/\delta$ 非零，所以 (3) 与 (2) 的 t 等价。源完整返回 (3) 的自由 t 恒等式、代入后的 R=0 以及原 P1；不存在只在泛型权成立的分母逆。

## 2. 完整原 Gram

令 $m=u-\ell,\ M=M_n/Q$，
$$
x_0=\frac{\theta V-mW}{M},\qquad
y_0=\frac{\ell W-uV}{M},\quad
X=x_0+\rho y_0,\quad Y=x_0-\rho y_0,\quad \rho^2=\delta,
$$
$$
b=\ell/2+\rho\,m/(2\delta),\quad c=\bar b,\quad
p=1+\rho,\quad q=1-\rho,\quad a=1-\ell.
$$
$X,Y$ 与权均保两个 $\rho$ 嵌入。原行
$$
(0,0,p,q),\quad(0,A_1,r,s_1),\quad(p,r,0,t),\quad(q,s_1,t,0)
$$
使用 $r=X-ap-ct,\ s_1=Y-aq-bt$ 与真 dual 乘法。源从该原 Gram 构造
$$
E_{\rm e},\quad E_{\rm o},\quad N_1,\quad NS,\quad PS.
\tag{4}
$$
原 $E_0,N_0,P_1$、$E_1=bE_B+cE_C$ 以及完整值全部逐式返回；不使用错误 Rbad，也不把 weighted 原值替为乘过 D 的条件。

(4) 前三式对 y 至多二次，后两式至多三次。每行只清 (1) 的实际分母及剥其所有系数的已付内容，逐次乘回。未付内容完整保留。记得到的多项式行为 $E,O,N,S,P$。

## 3. 真正新原标量输入

固定以下三个原系数矩阵：
$$
(E,O,N)\quad\hbox{在 }(1,y,y^2)\hbox{ 上},
$$
$$
(E,yE,O,S),\qquad(E,yE,O,P)
\quad\hbox{在 }(1,y,y^2,y^3)\hbox{ 上}.
\tag{5}
$$
只取固定三阶、四阶多项式 cofactor，不倒任何 y 首项。每个矩阵以 adjugate 第一行完整返回
$$
\sum_i\Omega_i(E,O,N,S,P)_i=D(u,Q).
\tag{6}
$$
重复 E 的两项先合成实际乘子。然后仅除全部五个真实原乘子的共同因子，并同步除 D，再把 (6) 全式乘回；这种取消在共同因子的整个零集仍成立，不是约掉原方程。最终只剥 (1) 的已付权因子，并返回相对于未约原式 (4) 的完整五项身份。

因此每个非零最终 D 都是整个当前原 $f=u$ 图的必要权多项式。若 D 为非零常数，才给整支排除；否则保全部 D 零曲线，仍不从泛型结式推无根。

## 4. 后继范围与停止边界

源最后只计算这些新必要权多项式的实际 QQ[u,Q] pair gcd。若某对确实互素，可由固定平面 Bézout 得其不同复权点数不超过总次数乘积；这只涉及权坐标。即使权点有限，也不假设每个固定权处至少有一条 y 多项式非零，所有整 y 纤维与首项退化仍保留。

本输入不进行新的 Buchberger、旧 t0/fu 的被冻结 GB、旧三头 cofactor 或旧错误紧凑式重放。不输出或存入可重算大系数；只保源定义、完整原返回的小摘要和实际资源边界。

唯一依赖：

- 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7；仅取 R 算术定义前缀。
