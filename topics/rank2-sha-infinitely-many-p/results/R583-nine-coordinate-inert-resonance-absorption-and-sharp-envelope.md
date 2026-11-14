# R583 — 九坐标惰性共振分母的逐因子吸收与同格全 jet 包络

日期：2026-11-14。**状态：已证明。**

本篇保持 R574、R575、R579 的同一个九坐标、多项式系数格及真正饱和前缀。
七个原积分的短分母仍然存在，但其一次 $p$ 因子与原被积函数的 Gaussian 分母不能分别取最坏值后相加。
逐因子保留来源至少六阶零的预算，便得到无条件改进
$$
\boxed{
\sum_{\substack{p\ {\rm inert}\\\text{及固定坏位}}}
\log\|\varphi_{D,9}^k\|_p
\le 3k\log k+O(k+D).
}
\tag{1}
$$
常数同时独立于 $D,k$。这把 R574 的额外 $3k\log\min(D,k)$ 降为 $O(k)$，
并没有假设原负矩、中央导数或某个共振系数消失。

## 1. 完全相同的来源与格

沿用
[R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md) 的
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad b=17,\qquad w=z^6,
$$
以及取零初值的 $r$ 次积分 $U_{\ell,r}$。
令
$$
R_4=2,\quad R_1=5,\qquad
V_{\ell,r}=z^{R_\ell-r}U_{\ell,r}\quad(1\le r\le R_\ell).
$$
固定九坐标为
$$
\boldsymbol F=(S,T,V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5}).
$$
每一个坐标至少从 $w$ 起。对所有 $D,k\ge1$ 使用
$$
E_{D,9}=\bigoplus_{|\boldsymbol a|\le D}\mathbf Z\,\boldsymbol X^{\boldsymbol a},
\qquad
r_k(P)=[w^k]P(\boldsymbol F(w)),
$$
$$
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_{D,9},
\qquad
\varphi_{D,9}^k=r_k|_{K_{D,k}\otimes\mathbf Q}.
\tag{2}
$$
局部系数最大范数仍由 (2) 的原单项式格诱导。
没有按 $p$ 改列、改积分常数或除以一个随 $p$ 变化的来源。

固定坏素数保留为有限集；以下取惰性好素数 $p>71$。
设
$$
c_p=\frac{p}{p^2-1}.
$$
[R574](R574-nine-coordinate-inert-envelope-and-primitive-denominator-cost.md)
第 2–3 节已经对原全部来源证明：若
$$
f_\ell=\sum_m a_{\ell,m}z^m,\qquad d_4=4,\quad d_1=1,
$$
则
$$
v_p(a_{\ell,m})\ge-\lfloor(m-d_\ell)c_p\rfloor.
\tag{3}
$$
这里 $d_\ell+R_\ell=6$。七塔的实际系数因此为
$$
\boxed{
[w^j]V_{\ell,r}
=\frac{a_{\ell,6j-R_\ell}}
{(6j-R_\ell+1)\cdots(6j-R_\ell+r)}.
}
\tag{4}
$$
原 $S,T$ 的 $w^j$ 系数同样有下界
$-\lfloor(6j-6)c_p\rfloor$，但它们没有 (4) 的积分分母。

本篇直接使用 (3)–(4) 的完整原系数，尤其保留 $6j-6$ 中的六阶 slack，
直到每个因子的实际短分母已经处理完毕。

## 2. 一次共振吸收的整数量词

**引理 1。** 设 $p>7$ 为整数，$n\ge6$，$0\le h\le4$，
$p\mid n-h$，且 $n<2p^2$。则
$$
\boxed{
\lfloor(n-6)c_p\rfloor+1\le\lfloor nc_p\rfloor.
}
\tag{5}
$$

证明。写 $n=mp+h$。由 $n\ge6>h$ 可知 $m\ge1$；
由 $n<2p^2$ 可知 $m<2p$。准确有
$$
(n-6)c_p
=m+\frac{m+(h-6)p}{p^2-1},
\qquad
nc_p=m+\frac{m+hp}{p^2-1}.
\tag{6}
$$
因为 $h\le4$，第一式的分子小于零；第二式的分子非负。
所以第一式的下取整至多 $m-1$，第二式至少 $m$，即 (5)。
这不使用被积系数本身被 $p$ 整除。证毕。

对 (4) 中的短段记
$$
\Delta_{\ell,r}(n)
=\prod_{i=1}^r(n-R_\ell+i),\qquad n=6j,
$$
$$
\delta_{p,a}(\ell,r,n)
=\#\{\,i:1\le i\le r,\ p^a\mid n-R_\ell+i\,\}.
\tag{7}
$$
所有因子都是正整数，不超过 $n$。
因为 $r\le5<p$，每个 $\delta_{p,a}$ 都至多为一，且
$$
v_p(\Delta_{\ell,r}(n))=\sum_{a\ge1}\delta_{p,a}(\ell,r,n).
$$

若 $\delta_{p,1}=1$，短段中唯一的 $p$ 倍数具有形状 $n-h$，
其中 $0\le h\le R_\ell-1\le4$。
当 $n<2p^2$ 时应用 (5)。
当 $n\ge2p^2$ 时，暂时保留这一个一次分母。
没有一次分母的情形只用下取整的单调性。
因而对全部 $n=6j$、全部七个原积分，统一有
$$
\boxed{
\lfloor(n-6)c_p\rfloor+v_p(\Delta_{\ell,r}(n))
\le
\lfloor nc_p\rfloor
+\mathbf1_{n\ge2p^2}
+\sum_{a\ge2}\delta_{p,a}(\ell,r,n).
}
\tag{8}
$$
这是每个原系数的真实估计，不是把一阶分母从记账中删除。
二次及更高的 $p$ 幂全部还在右边。

## 3. 全部混合单项式的同一次吸收

取总次数为 $q$ 的一个原单项式，其中 $q_{\rm pr}$ 个因子来自七塔。
其 $w^k$ 系数中的每一项，对应
$$
j_1+\cdots+j_q=k,\qquad j_i\ge1.
$$
令 $n_i=6j_i$，于是
$$
\sum_i n_i=6k=:n,\qquad q_{\rm pr}\le q\le\min(D,k).
\tag{9}
$$
在每个积分因子上先用 (8)；在原 $S,T$ 因子上用
$\lfloor(n_i-6)c_p\rfloor\le\lfloor n_ic_p\rfloor$。
这保留了同一因子的分子与分母之间的预算配合。
之后才对各因子求和。

所有 Gaussian 项满足
$$
\sum_i\lfloor n_i c_p\rfloor\le\lfloor nc_p\rfloor.
$$
未被 (5) 吸收的一次 $p$ 分母，每出现一个都消耗至少 $2p^2$ 的正次数，
故
$$
\sum_{\text{积分因子 }i}\mathbf1_{n_i\ge2p^2}
\le\left\lfloor\frac{n}{2p^2}\right\rfloor.
\tag{10}
$$
对每个 $a\ge2$，短段中的 $p^a$ 倍数不超过对应的 $n_i$；
因此全部高次倍数的个数同时不超过 $q_{\rm pr}$ 和
$\sum_i\lfloor n_i/p^a\rfloor\le\lfloor n/p^a\rfloor$：
$$
\sum_i\delta_{p,a}(\ell_i,r_i,n_i)
\le\min\left(q_{\rm pr},\left\lfloor\frac n{p^a}\right\rfloor\right).
\tag{11}
$$

定义完整保留的高次误差
$$
\mathcal E_p(n,K)=
\left\lfloor\frac n{2p^2}\right\rfloor
+\sum_{a\ge2}\min\left(K,\left\lfloor\frac n{p^a}\right\rfloor\right).
\tag{12}
$$
逐个系数项的结论是
$$
v_p(\text{该原单项式的 }w^k\text{ 系数项})
\ge-\lfloor nc_p\rfloor-\mathcal E_p(n,q_{\rm pr}).
\tag{13}
$$
合并系数项、再取整系数多项式和，都不增加负赋值。
不论各项之间是否另有相消，(13) 已成立。

所以得到原格上的统一定理。

**定理 2。** 对全部 $D,k\ge1$ 及全部好惰性 $p>71$，
令 $K=\min(D,k)$，则
$$
\boxed{
\log\|\varphi_{D,9}^k\|_p
\le
\left\{
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor
+\mathcal E_p(6k,K)
\right\}\log p.
}
\tag{14}
$$

这里先支付了 $E_{D,9}$ 的全部原列，随后限制到真正饱和子格 (2)；
没有将一个有限 jet 或单一来源的整性升级为全部饱和层。
当 $p>6k$ 时右边为零，所以仍覆盖所有惰性位。
常数列在 $k>0$ 的系数为零，不是遗漏的例外。

## 4. 误差的全素数和只有线性成本

(12) 的第一项满足
$$
\sum_p\left\lfloor\frac n{2p^2}\right\rfloor\log p
\le\frac n2\sum_p\frac{\log p}{p^2}=O(n).
\tag{15}
$$
其余所有高次幂满足
$$
\begin{aligned}
\sum_p\sum_{a\ge2}
\min\left(K,\left\lfloor\frac n{p^a}\right\rfloor\right)\log p
&\le n\sum_p\sum_{a\ge2}\frac{\log p}{p^a}\\
&=n\sum_p\frac{\log p}{p(p-1)}
=O(n).
\end{aligned}
\tag{16}
$$
常数与 $K$ 无关。这正是把一次素数共振先逐因子吸收的作用：
R574 中产生 $\log K$ 的 $a=1$ 和已经没有留在误差项里。

原 Gaussian 项的惰性和仍准确为
$$
\sum_{p\equiv5(6)}
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor\log p
=3k\log k+O(k),
\tag{17}
$$
见 R418 (17)，亦在 R574 (9) 保同一规范。
固定坏位由固定九坐标的正收敛半径给总成本 $O(k+D)$。
把 (14)–(17) 合起来，得到 (1)。

特别，九坐标现在确实获得与原两坐标相同的惰性主包络
$$
\boxed{(a_I,b_I)=(0,3).}
\tag{18}
$$
这来自 (3)–(13) 的原来源全次数证明，并非直接套用旧两坐标的界。
(18) 是已付上界，不声称每个素数、每一层都达到它。

## 5. 同格 Euler 基及共振的准确含义

为后续分析保留一个与 (4) 完全等价的固定整基。
设
$$
J_{\ell,j}(z)=\int_0^z t^j f_\ell(t)\,dt.
$$
定义七个实际整函数
$$
W_{4,h}=z^hJ_{4,1-h}\quad(h=0,1),\qquad
W_{1,h}=z^hJ_{1,4-h}\quad(0\le h\le4).
\tag{19}
$$
若 $\theta=6w\,d/dw=z\,d/dz$，则完整函数恒等式是
$$
(\theta-h)W_{4,h}=z^2 f_4,\qquad
(\theta-h)W_{1,h}=z^5 f_1.
\tag{20}
$$
相应系数精确为
$$
[w^k]W_{4,h}=\frac{a_{4,6k-2}}{6k-h},\qquad
[w^k]W_{1,h}=\frac{a_{1,6k-5}}{6k-h}.
\tag{21}
$$
两个右端是两条固定来源，不是七个任意 forcing。

R575 (7) 给固定三角变换
$$
V_{4,1}=W_{4,1},\qquad
V_{4,2}=W_{4,1}-W_{4,0},
$$
$$
V_{1,r}=\frac1{(r-1)!}
\sum_{j=0}^{r-1}(-1)^j\binom{r-1}{j}W_{1,4-j}.
\tag{22}
$$
两块行列式分别为 $1$、$1/288$；逆矩阵也仅有固定小分母。
因此在本篇全部好位，(22) 属于 $GL_7(\mathbf Z_p)$。
加上原 $S,T$ 后，它诱导同一个次数上限的多项式格同构，
保持每个真正饱和前缀；这不是一个依赖 $k$ 的列归一。

(21) 说明确实有共振分母，并不说明对应分子总被 $p$ 整除。
例如写 $p=6s-1$，$h=1$ 的首共振在 $k=s$；
其两个真实分子为
$$
[z^{p-1}]f_4,\qquad [z^{p-4}]f_1.
\tag{23}
$$
它们是原惰性来源的系数，不是普通地点的 $I_4,I_1$，
也未被本篇识别成原 $S/T$ 中央行。
本篇的吸收来自 (6)，与 (23) 是否消失无关。
后续若证明这些分子具有额外整除，仍须给同一完整来源的实际关系。

## 6. 与普通预算及剩余严格门

[R579](R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md)
已在同一个九坐标格上支付全部普通位
$$
\sum_{p\equiv1(6)}\log\|\varphi_{D,9}^k\|_p
\le3k\log D+O(k+D).
$$
R575 的完整独立性与复增长给真实维数九和复侧
$-3k\log k+3k\log D+O(k+D)$。
所以 R579 的严格充分门仍是
$$
a_I+9b_I<21.
\tag{24}
$$
本篇把无条件输入从 $(3,3)$ 改为 $(0,3)$；
其 $9b_I=27$ 仍未小于 $21$。
若未来保持 $a_I=0$，实际需要 $b_I<7/3$ 的全格改善，
本篇没有把该改善赋成。

原全算术中央失败到两个指定负矩的合法桥也仍未付。
不能由 (19) 的两个 forcing、七个普通 core 或一次共振吸收，
删除原 mixed 域及其补项。

## 7. 可复核证书

[check-r583-inert-resonance-absorption.mjs](../scripts/check-r583-inert-resonance-absorption.mjs)
检查全部七个固定积分段、(22) 的有理变换、
一次共振的准确模数表达，以及有限整数网格上所有七种因子和混合分拆的 (8)、(13)。
混合检查用最大加法递推同时覆盖指定总次数内的全部分拆，
没有随机选取单项式。

这些是对完整证明的算术核对；(5)、(8)–(17) 的证明已经保留
所有 $p,D,k$ 量词。证书不进行新的椭圆曲线素数扫描，
也不把有限系数证据当成 (23) 的非消失或主目标的完成。
