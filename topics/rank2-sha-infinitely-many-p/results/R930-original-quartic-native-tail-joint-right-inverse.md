# R930 — 同一原 quartic 来源的 native 尾联合右逆

日期：2026-11-20。**状态：完整符号推导，尚未执行数学计算。** 本注计算 R872 所留的一个实际联合像；不证明全第二、第三页可解，不证明 R928 的固定全局类非零，也不放宽受限 S。

R868 已在足够 t 松弛时构造一个原首像方向，证明指定 Lambda0 不杀完整首 Bockstein 的像。本注在更强且明确的同源松弛下，构造一整组实际方向，给出 R872 末尾读取的联合三角右逆。R920 的负 fringe 在一个明确的同余因子分支中自动支付这些松弛门。

## 1. 原对象、准确松弛与两个不同的 r

始终保留 R821/R828 的同一个实际矩阵

$$
M:\mathscr L_D\longrightarrow
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3),
\qquad p=6s-1>211,\quad0<\ell<s-13.
\tag{1}
$$

原 P134、公共单位、charge 四十、十九角、全部 normal 行及三个十三行带均保留。相对约化格仍为

$$
\overline{\mathcal W}_D
=\bigoplus_{n=0}^D Y^nq_n(t)\,k[t]_{\le e_{n+1}},
\qquad A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,
\qquad q_n/t^{A_n}\in k[[t]]^\times.
\tag{2}
$$

使用 R868 的精确松弛

$$
\sigma_t(P)=\min_n(\operatorname{ord}_0P_n-A_n),
\qquad P=\sum_nY^nP_n(t).
\tag{3}
$$

R868 已逐 charge 支付全部十九角和无穷帽，给出

$$
t^{-v}P\in\overline{\mathcal W}_D
\quad\Longleftrightarrow\quad0\le v\le\sigma_t(P).
\tag{4}
$$

固定同一个真正存在的 quartic 来源

$$
\overline P=t^{r_{\rm src}}F^4q\in\overline{\mathcal W}_D,
\qquad F(t(w),\bar g(w))=w^hu(w),
\qquad u_0e_0q_0\ne0.
\tag{5}
$$

这里 g 是完整实际轴，e=EF，E=Y∂Y；q0=q(0,1)，e0=e(0,1)。F、q 是 Y 多项式，系数在 t=0 正则，原固定 d 分母在那里为单位。令

$$
t(w)=t_1w+O(w^2),\quad t_1\ne0,\qquad
\tau=r_{\rm src}+2h-s\ge0,
\qquad C_0=c_*U_0(0)t_1^{r_{\rm src}}q_0.
\tag{6}
$$

源指数 r_src 与 R920 返回 qt²H3 中的指数 2 不混用。全篇不从四中央零推断 (5) 存在。

W_i 始终表示 R928(3) 的实际总 charge 矩，未删除 H_Theta B。原来源给

$$
\operatorname{ord}_w\overline W_i(P)\ge r_{\rm src}+(4-i)h
\quad(0\le i\le3),\qquad
[w^{r_{\rm src}+2h}]\overline W_2(P)=12C_0u_0^2e_0^2.
\tag{7}
$$

这是因为 (E+40)²(t^rF⁴q) 的唯一最低 F 次项为 12t^rF²(EF)²q；公共单位和 q 的其余 Euler 项含至少 F³，不进入显示首项。

## 2. 原全首核的实际联合尾像

取整数 m，满足

$$
\boxed{1\le m\le13,\qquad
\sigma_t(P)\ge\tau+m,\qquad
\ell\le s-h-m.}
\tag{8}
$$

对 j=1,...,m 定义

$$
\boxed{Y_j=t^{-(\tau+j)}\overline P.}
\tag{9}
$$

由 (4)、(8)，每个 Y_j 都在原同一 W_D，不扩大次数或列数。E(t)=0，公共来源因子不变，故全部实际矩严格满足

$$
\overline W_i(Y_j)=t(w)^{-(\tau+j)}\overline W_i(P).
\tag{10}
$$

从而

$$
\operatorname{ord}\overline W_i(Y_j)\ge s+(2-i)h-j
\quad(0\le i\le3),
\tag{11}
$$

并且

$$
\boxed{\overline W_2(Y_j)=\mu_jw^{s-j}+O(w^{s-j+1}),
\qquad
\mu_j=12C_0t_1^{-(\tau+j)}u_0^2e_0^2\in k^\times.}
\tag{12}
$$

**定理 1。** 所有 Y_j 都属于原完整首核 K1=ker Mbar，并且

$$
\mathcal T_m:K_1\longrightarrow k^m,\qquad
Y\longmapsto
\bigl([w^{s-m}]\overline W_2(Y),\ldots,
[w^{s-1}]\overline W_2(Y)\bigr)
\tag{13}
$$

在同一个实际子空间 U_m=span(Y_m,...,Y_1) 上是同构。

**证明。** 原前三个约化 normal 块要求 W0、W1、W2 的相对阶至少 s-13，式 (11) 和 m≤13 同时支付。末短块要求 W3 的阶至少 ell，由 (8) 支付。最前三个十三行在所有原列上本已含 p。所以是整个 Mbar Y_j=0，不是仅通过一条尾行。

按输入 (Y_m,...,Y_1) 和输出 (w^(s-m),...,w^(s-1)) 排序，(12) 给一个三角矩阵，其主对角是 mu_m,...,mu_1。每个都是单位，所以可逆；它也证明 Y_j 在原源中线性无关。证毕。

右逆须用完整尾矩阵求逆；高于首项的系数一般不为零。没有将其误当成对角矩阵，也未删普通单位、B 或完整卷积。

## 3. 原首 Bockstein 的 native carry 投影

取原整行

$$
\lambda_q=[\epsilon^3w^{13-q}],\qquad1\le q\le13.
\tag{14}
$$

它们杀整个 Mbar，因为全部原约化列含 w^13。对 Y∈K1 及任一原整提升 Ytilde，R928(6) 的实际 carry 合并给

$$
\boxed{\lambda_q\!\left(M\widetilde Y/p\bmod p\right)
=\frac{a^2}{2}[w^{s-q}]\overline W_2(Y).}
\tag{15}
$$

改变提升只加 Mbar 的像，被 lambda_q 杀掉。若改用参考 W_i^circ，(15) 会展开成 H_Theta B 低项与参考高项；这里已准确合并为实际轴，未令 H_Theta B 为零。

所以 (13) 同时给 beta1(K1) 到这 m 条实际 carry 的完整满射。它不是在自由目标格中写出 m 个单位。

若再有 m≤h，则 (11) 使 W0(Y_j)、W1(Y_j) 的阶均至少 s。这组真实首 Bockstein 向量在前两个十三行带上全零；第三带在 w^0,...,w^(12-m) 上也全零。全部三十九 carry 的可能非零响应只在指定的末 m 行。其它 normal 响应仍保留，不能由此宣称整个第二余核有一个自由直和。

特别

$$
\boxed{U_m\cap\ker\beta_1=0.}
\tag{16}
$$

这些方向不属于完整首 Bockstein 核。也没有声称 U_m 在 R920 的较小 jmath(H3) 内。

## 4. 同 P、R、S 的准确页数作用

若固定原 P、R，并已知完整

$$
M(P+pR)\in p^2\Gamma,
\tag{17}
$$

则 R→R+Σc_jYtilde_j 保持整个 (17)，其第二页类准确改变

$$
\sum_j\bar c_j\,\beta_1(Y_j).
\tag{18}
$$

它可以同时指定 (15) 的 m 个 carry 值；normal 行沿同一个真实向量改变。

若固定完整

$$
X=P+pR+p^2S,\qquad MX\in p^3\Gamma,
\tag{19}
$$

则保持 P、R 不变、令

$$
S'=S+\sum_jc_j\widetilde Y_j
\tag{20}
$$

仍保持整个 p³ 提升，因为每个 M Ytilde_j 属于 p Gamma。第三页类的变化仍是 (18)。因此同一个来源组合可同时指定末 m 条 native carry，不必为各标量分别换一组 S。

其它第三页 normal 行必须继续用同一个 S' 检验；最终 p³T 在这些 carry 上不起作用的事实也保持。由于 (16)，不能把 (20) 改称“两个完整 p³ 解之间任意改变 R 并补 S”；后者要求完整 beta1 零，恰被这些单位响应排除。

若 S 只允许在固定陪集 S_b+mathscr S 中变化，只有当这些整提升的约化组合确实属于允许差格时，才能使用 (20)。本注不由 Y_j∈W_D 推断该受限成员性，更不替代 R928(31) 的完整同源检验。

## 5. R872 指定尾的直接实际方向 P/t⁴

在 R872 的 tau∈{1,2,3} 和

$$
\tau<\ell\le r_{\rm src}+h-4
\tag{21}
$$

下，若实际 sigma_t(P)≥4，取 m=4-tau，则 (8) 全成立：第二门是 tau+m=4，第三门就是 (21)。第 m 个真实方向恰为

$$
\boxed{Y_m=t^{-4}\overline P.}
\tag{22}
$$

因此 R872(32) 的指定原泛函确实非零，准确值是

$$
\boxed{[w^{s+\tau-4}]\overline W_2(t^{-4}P)
=12C_0t_1^{-4}u_0^2e_0^2\ne0.}
\tag{23}
$$

乘原 a²/2 后，得到 R872 第二／第三页基准的单位变化。这支付其实际调整口，未把三个中央轴作为自由参数。sigma≥4 不能由 r_src≥4 单独推出。

对全部末三尾的联合满射，可在 (8) 直接取 m=3；这要求 sigma_t(P)≥tau+3 和 ell≤s-h-3。

## 6. 负 fringe 中自动支付的同余因子分支

额外假设 R920 的全部原强窗及几何门，且返回

$$
q\,t^2\mathcal H_3\subset\overline{\mathcal W}_D,
\qquad \mathcal H_3=H^0(X,\mathcal O_X(3C))
\tag{24}
$$

使用的确实是 (5) 中同一个 q。这是本节的额外实际假设，不能把任意不同返回因子认作它。

令

$$
C.f_0=3,\qquad
\delta=2+2h-s=-d,\quad1\le d\le13,\qquad
\ell=2+L,\quad L\le h,\quad h>21.
\tag{25}
$$

R815 的原四步零角公式给

$$
v_0(F)=-C.f_0=-3,\qquad
v_0(A)=\min_n(4\operatorname{ord}_0A_n-n).
\tag{26}
$$

F³ 本身在 H3，故 (24) 给 qt²F³∈W_D。原零角门 v0≥-2 遂给

$$
8-9+v_0(q)\ge-2,\qquad v_0(q)\ge-1.
\tag{27}
$$

又 q(0,1) 非零，至少一个 q 的 Y 系数在 t=0 为单位，因此 v0(q)≤0。

对任一非零原 Y 多项式，有精确整数等式

$$
\boxed{\sigma_t(A)=
\left\lfloor\frac{v_0(A)+2}{4}\right\rfloor.}
\tag{28}
$$

这是 (3) 的逐 charge 改写：ord-A_n=floor((4ord-n+2)/4)，有限个项取最小与 floor 相容；不是只读最低 charge。

Gauss 值对乘积严格相加，所以 (5)、(26)–(28) 给

$$
\boxed{\sigma_t(P)=r_{\rm src}-3,\qquad
r_{\rm src}=\tau+d+2,\qquad
\sigma_t(P)=\tau+d-1.}
\tag{29}
$$

故对每个 1≤m≤d-1，(8) 的来源门自动成立。短门也自动成立，因为

$$
s-h-m=h+2+d-m\ge h+3>\ell,
\tag{30}
$$

其中最后只用 ell≤h+2。又 m≤12<h，前两个十三带的零响应也已支付。

| 同一个负 fringe | 自动认证的原 K1 尾像 |
|---|---|
| delta=-1 | 本节不新增尾方向 |
| delta=-2 | 最后一尾满射 |
| delta=-3 | 最后两尾联合满射 |
| -13≤delta≤-4 | 全部末三尾联合满射；更一般末 m 尾对 m≤-delta-1 满射 |

表最后一行给出 R872 所需整个末三尾向量的同源右逆。它不是 R920 对 K' 的维数界，也不能改变两个完整 p³ 解之间的差空间；所构造方向的 beta1 投影恰可逆。

在 tau∈{1,2,3} 的指定 R872 行中，只要本节同 q 条件成立且 r_src≥7，(29) 又使 sigma≥4，故 (22)–(23) 自动适用。

## 7. 尚未支付的真实问题

本注付清实际来源中的完整尾联合像及准确页数作用。它没有计算固定 R928 类，也没有证明四中央与全部 normal 行的同源联合解不存在。全 p³ 解内改变 R 仍须属于完整首 Bockstein 核；受限 S 仍须付允许差格中的真实成员性。

在同 q 的负 fringe 子支中，不能再把“末三尾也许完全不可调”当作 delta≤-4 的独立障碍。新的检验须保三角解引入的完整 normal 响应；delta=-1,-2,-3 的缺失尾，以及不同 q 或更小 S 差格，仍按原完整对象继续。

依赖：R868 的全源 t 松弛；R815 的原零角／严格零纤维公式；R821 四块窗口；R828 三条 carry；R872(29)–(32)；R928(6) 的实际矩合并。全部为符号证明，无本地数学实验。
