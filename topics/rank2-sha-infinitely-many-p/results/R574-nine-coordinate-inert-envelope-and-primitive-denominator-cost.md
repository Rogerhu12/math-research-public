# R574 — 同一九坐标的惰性全 jet 包络与原函数分母成本

日期：2026-11-14。**状态：已证明。**

本篇对 R575 的七个正幂规整原函数与原 $S,T$，使用同一个九坐标
多项式源格，支付所有次数和所有饱和 jet 的无条件惰性估计。
新增积分分母确有成本；它不能由代数独立性或有限阶分布消去。

结果为
$$
\sum_{p\equiv5\ (6)}\log\|\varphi_{D,9}^k\|_p
\le 3k\log k+3k\log\min(D,k)+O(k+D).
$$
常数与 $D,k$ 无关。证明保原系数格和原最高阶乘，
没有对各列另换归一。它尚不提供主目标所需的严格改善。

## 1. 固定的九个整坐标与真正源格

使用 [R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)
同一 $b=17$、$w=z^6$ 的七个固定函数
$$
V_{4,r}=z^{2-r}U_{4,r}\quad(r=1,2),\qquad
V_{1,r}=z^{5-r}U_{1,r}\quad(r=1,\ldots,5),
$$
连同原实际 $S,T$，按此固定次序记为 $\boldsymbol F$。
七个 $U$ 均取固定零初值；这里没有改变任何原函数常数。

每个坐标在 $w=0$ 至少一重零，所有系数有理；
九者代数独立，且均为有限型、阶 $1/3$ 的整函数。
完整来源与复侧证明分别见 R575 和
[R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)。

采用原单项式格
$$
E_{D,9}=\bigoplus_{|\boldsymbol a|\le D}
\mathbf Z\,\boldsymbol X^{\boldsymbol a},\qquad
N_D=\binom{D+9}{9}.
$$
定义
$$
r_k(P)=[w^k]P(\boldsymbol F(w)),\qquad
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_{D,9},
$$
$$
\varphi_{D,9}^k=r_k|_{K_{D,k}\otimes\mathbf Q}.
\tag{1}
$$
局部范数由这个格的系数最大范数诱导；$K_{D,k}$ 是真正饱和前缀。
后面先证明全部原列的系数界，再限制到 (1)，所以没有偷换饱和格。

全部固定小坏素数，包括 $2,3,5,7,17$，先保留为一个固定有限集。
对它们，固定坐标的正收敛半径直接给总成本 $O(k+D)$。
以下惰性好素数满足 $p>71,\ p\equiv5\bmod6$。

## 2. 原高度二圆盘上四个被积来源的准确界

记
$$
c_p=\frac{p}{p^2-1},\qquad \rho_p=p^{-c_p}.
$$
R418 (13)–(15) 给每个 $0<r<\rho_p$ 上
$$
\|\Theta\|_r\le1,\qquad
\|z^2x\|_r=\|(z^2x)^{-1}\|_r=1,\qquad
\|S\|_r,\|T\|_r\le r^6 .
\tag{2}
$$
其真实首 Gaussian、余项圆盘和固定 $b$ 尺度已经保留。
由 $\sigma^2=\Theta/x$，严格得 $\|\sigma\|_r\le r$。
又 $y^2=x^3+b$ 给 $\|y\|_r\le r^{-3}$。
因此原两个被积函数满足
$$
\boxed{\|f_4\|_r\le r^4,\qquad
       \|f_1\|_r\le r,\quad
       f_4=x\sigma^6,\ f_1=-xy\sigma^6.}
\tag{3}
$$
这不是对积分后的函数猜一个相同的 Gauss 范数。

若先在 R418 的 $b=1$ 共同模型使用 (2)，也可作固定尺度运输。
取 $\theta^6=b$，
$x_b(z)=\theta^2x_0(\theta z)$、
$\sigma_b(z)=\theta^{-1}\sigma_0(\theta z)$；
在 $p\nmid b$ 处 $\theta$ 为单位，圆盘及上述范数保持。
特别正幂规整给
$$
V_{\ell,r,b}(w)=b^{-1}V_{\ell,r,0}(bw).
$$
全部这种固定尺度仅改变被保留有限坏位的常数。

将 (2)–(3) 从圆盘内部取极限，若
$f_\ell=\sum_m a_{\ell,m}z^m$，并记 $d_4=4,d_1=1$，有
$$
v_p(a_{\ell,m})\ge
-\left\lfloor (m-d_\ell)c_p\right\rfloor.
\tag{4}
$$
相同地，$S,T$ 的 $z^n$ 系数下界为
$-\lfloor(n-6)c_p\rfloor$。
这些式只在相应非零系数的次数上使用。

## 3. 七个固定积分的所有真实分母

置 $R_4=2,R_1=5$，则 $d_\ell+R_\ell=6$。
由固定积分的定义，
$$
[z^{m+r}]U_{\ell,r}
=\frac{a_{\ell,m}}{(m+1)(m+2)\cdots(m+r)}.
$$
正幂规整后的次数是 $n=m+R_\ell=6j$，$j\ge1$。
所以
$$
\boxed{
[w^j]V_{\ell,r}
=\frac{a_{\ell,6j-R_\ell}}
 {(6j-R_\ell+1)\cdots(6j-R_\ell+r)} .
}
\tag{5}
$$
分母是一个长度至多五的真实连续整数段，
其中每个整数为正且不超过 $6j$。
未将此段改成另一个阶乘，也没有除以形式 $\log$。

现在取任何一个原单项式，设总次数为 $q$，
其中七个新坐标共出现 $q_{\rm pr}$ 次。
其 $w^k$ 系数逐项由正整数
$j_1+\cdots+j_q=k$ 给出。
故 $q_{\rm pr}\le q\le\min(D,k)$。

对任何 $p^a$，因 $p>5$，每个 (5) 的分母段至多含一个
$p^a$ 的倍数；同时这个整数不超过对应的 $6j_i$。
因此全部分母中的 $p^a$ 倍数个数同时不超过
$q_{\rm pr}$ 和
$\sum_i\lfloor6j_i/p^a\rfloor\le\lfloor6k/p^a\rfloor$。
定义
$$
\Gamma_p(n,K)=\sum_{a\ge1}
\min\left(K,\left\lfloor n/p^a\right\rfloor\right).
$$
便严格有
$$
\boxed{v_p(\text{该系数项的全部积分分母})
       \le\Gamma_p(6k,q_{\rm pr}).}
\tag{6}
$$
这支付所有混合乘积和重复因子；
合并同类项的整数多项式系数不会增加负赋值。

原分子按 (4) 及 (2) 的总成本至多
$$
\sum_i\lfloor(6j_i-6)c_p\rfloor
\le\lfloor(6k-6q)c_p\rfloor.
$$
所以每个实际单项式都有较精确的界
$$
v_p(r_k(\boldsymbol X^{\boldsymbol a}))
\ge-\lfloor(6k-6q)c_p\rfloor
   -\Gamma_p(6k,q_{\rm pr}).
\tag{7}
$$
(7) 中 $q,q_{\rm pr}$ 属于该单项式本身；
原 $S,T$ 的因子没有被计入积分分母。

## 4. 同一九坐标的全部饱和 jet

令 $K=\min(D,k)$、$n=6k$。
由 (7)、非阿基米德三角不等式及真正子格 (1)，得到

**定理 1。** 对所有 $D,k\ge1$ 和上述惰性好素数，
$$
\boxed{
\log\|\varphi_{D,9}^k\|_p
\le
\left\{
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor
+\Gamma_p(6k,K)
\right\}\log p .
}
\tag{8}
$$
该层若不增加秩，评价为零，仍满足此界。
当 $p>6k$ 时右边为零；未留下一个无限的未估计素数集。

这里不需要把“单独坐标整”升级为任意乘积的饱和整性：
(5)–(7) 已逐个支付全部混合单项式的同一个系数行。
(8) 只是上界；它没有声称这个包络在每个 $p$ 或每一层取到。

## 5. 对全部惰性素数求和

R418 已付
$$
\sum_{p\equiv5(6)}
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor\log p
=3k\log k+O(k).
\tag{9}
$$
为完整计算新增项，先取 $a=1$，在 $p=n/K$ 处分段。
小素数部分至多
$K\vartheta(n/K)=O(n)$。
大素数部分由固定模六的 Mertens 公式给
$$
n\sum_{\substack{n/K<p\le n\\p\equiv5(6)}}\frac{\log p}{p}
\le \frac n2\log K+O(n).
$$
所有 $a\ge2$ 的项合计至多
$$
n\sum_p\frac{\log p}{p(p-1)}=O(n).
$$
以上常数同时独立于 $D,k$，因为 $K\le k$、$n/K\ge6$。
因此
$$
\sum_{p\equiv5(6)}\Gamma_p(6k,K)\log p
\le3k\log K+O(k).
$$
结合固定坏位，得到

**定理 2。**
$$
\boxed{
\sum_{\text{惰性位及固定坏位}}
\log\|\varphi_{D,9}^k\|_p
\le3k\log k+3k\log\min(D,k)+O(k+D).
}
\tag{10}
$$
没有为每条列、每个次数或每个素数改用不同的源格。
原两条中央是否失败、两负矩是否为零，都未用于 (8)–(10)。

## 6. 复侧及严格剩余门

九个固定坐标的共同有限型界给同一原格上
$$
\log\|\varphi_{D,9}^k\|_\infty
\le-3k\log k+3k\log D+O(k+D).
\tag{11}
$$
它对所有 $D,k$ 成立，而非先代入 $k\asymp D^9$。
真实维数为九来自 R575 的完整独立性。

为准确说明还需要什么，若同一个普通饱和格已支付
$$
\sum_{p\equiv1(6)}\log\|\varphi_{D,9}^k\|_p
\le3k\log D+O(k+D),
\tag{12}
$$
且原算术条件进一步给同一个惰性格的改善
$$
\sum_{p\equiv5(6)}\log\|\varphi_{D,9}^k\|_p
\le a_I k\log D+b_I k\log k+O(k+D),
$$
那么 R159/R418 的整个饱和旗标乘积公式给严格充分门
$$
\boxed{a_I+9b_I<21.}
\tag{13}
$$
确切地，$b_I<3$ 时原维数会满足
$9\le(6+a_I)/(3-b_I)$；(13) 正是其严格反面。
普通项 (12) 必须对实际有限阶分布用完整差商论证，
不能仅因阶至多 $5D$ 就沿用有界测度的零成本。

本篇已付的惰性包络是 $(a_I,b_I)=(3,3)$，
没有跨过 (13)。它比把旧两坐标 $(0,3)$ 免费搬到新九坐标更弱，
因为 (5) 的积分分母确实还在。
(10) 不把它们归为固定 $O(k)$ 开销。

还可给一个保持全部量词的条件性 cutoff 后果：
假如在同一九坐标格上，原算术条件能证明对所有
$p>cD^\theta$ 的惰性位有
$\|\varphi_{D,9}^k\|_p\le1$，其余位仍按 (8) 使用，
则 (9) 的截断至多为
$3\theta k\log D+O(k)$，而新增项仍由
$3k\log D+O(k)$ 控制。
故一个已明确支付成本的严格充分范围是
$$
\theta<6
\quad\Longrightarrow\quad
(a_I,b_I)=(3\theta+3,0)\text{ 满足 (13)}.
\tag{14}
$$
这只是条件性充分范围，不声称 cutoff 已存在或该范围最优。
特别不能把原三块 $M$ 的有限低行结果当成上述九坐标的全饱和整性。

## 7. 保留的算术接口

R575 的五个自动 scalar core 和两个原 $I_4,I_1$ Dirac 缺陷
是准确的普通分布身份；它们本身没有给 (13) 的惰性改善。
原完整 $S/T$ 中央失败到两个负矩的合法桥也仍未完成。

R577/578 的实际同预算临界因子、两条剩余 jet 像和同一个修正的
carry/d2 继续作用在其原来源，不能在未付格比较时扩大为本篇所有列。
R571/576 的完整算术补项也不能由辅助九坐标的独立性删除。

本文新增的是 (5)–(10) 的真正九坐标惰性包络。
无穷素数目标尚未完成，后续需要同一全格的实际严格增益。
