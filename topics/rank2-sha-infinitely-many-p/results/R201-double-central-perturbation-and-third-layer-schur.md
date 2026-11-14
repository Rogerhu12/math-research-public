# R201. 双完整中央条件的第三层扰动与真实前缀 Schur 消去

日期：2026-11-12。**状态：同源有限比较、共享整化格、准确第三层差及其至多两条边界行均已证明。** 始终保留原 $E_D$ 和全部早期真实行。比较矩阵只定位两个原中央条件的有限精度作用，不被当作另一条已付算术性质的全局曲线。

## 1. 原源与两个精确输入

取 $p=4r-1\ge19$，置
$$
\mathcal O=\mathbb Z_p,\quad R=r(p-1),\quad E_D=\mathcal O[A,C]_{\le D},\quad C=B-A.
\tag{1}
$$
这里 $A=A_2$，原 $w=z^4$ 级数满足 $A=w+\cdots$、$C=v_0w^2+\cdots$，$v_0=-22\in\mathcal O^\times$。原整基为 $A^{m-c}C^c$，原次数为 $m$、角向最低权为 $\ell=m+c$。不增加环境坐标作为自由源列。

R185 的同一整截面给
$$
A=\Gamma^{17}f(y),\quad C=\Gamma^{17}c(y),\quad f=y+\cdots,\quad c=v_0y^2+\cdots,\quad f,c\in\mathcal O[[y]].
\tag{2}
$$
记
$$
\pi_0=u_0^{-1}\in p\mathcal O^\times,\quad\tau_p=pu_0\in\mathcal O^\times,\quad\mathcal E=A\partial_A+C\partial_C.
\tag{3}
$$
取完整前缀
$$
k=rq+s,\quad0\le s<r,\quad\lceil r/2\rceil\le q\le p-2.
\tag{4}
$$
真实整行是 $J_n(P)=p^{\lfloor n/r\rfloor}[w^n]P(A(w),C(w))$，$n<k$。R199 的特征零准确式为
$$
J_{rh+l}(P)=\sum_{i=0}^h p^{h-i}\frac{(17\tau_p)^i}{i!}[y^{l+r(h-i)}](\mathcal E^iP)(f,c),\quad0\le l<r,\ rh+l<k.
\tag{5}
$$
所有 $i!$ 是单位；本式不要求 $D<p$ 或 $p\nmid m$。

本篇条件输入仅为原两个完整中央导数同时为零：
$$
J_A'(0)=J_B'(0)=0.
\tag{6}
$$
故 $J_C'(0)=0$。置 $v_1=(f_r,c_r)$、$v_2=(f_{2r},c_{2r})$。R185 (30) 对同一个齐次次数 $17$ 给
$$
\boxed{v_1\in p\mathcal O^2,\qquad v_1-\frac{\pi_0}{17}v_2\in p^2\mathcal O^2.}
\tag{7}
$$
没有把 (6) 传给乘积；下文只用原多项式的整 Hasse 展开。

## 2. 同一源上的有限比较矩阵

定义整轴
$$
f^\circ=f-f_ry^r-f_{2r}y^{2r},\qquad c^\circ=c-c_ry^r-c_{2r}y^{2r}.
\tag{8}
$$
在同一个 $E_D$ 上令 $J^\circ$ 为把 (5) 中 $(f,c)$ 换成 $(f^\circ,c^\circ)$ 得到的矩阵，保留原 $\pi_0,\tau_p$。这是明确的整有限矩阵；也可看成形式平面 $(e^{17u_0w^r}f^\circ(w),e^{17u_0w^r}c^\circ(w))$ 的归一 jet，但不赋予它原 theta 的全局性质。

另记
$$
\Lambda_{h,l}(P)=\pi_0^h[w^{rh+l}]P,\qquad J_{rh+l}=\tau_p^h\Lambda_{h,l}.
\tag{9}
$$
若 $P=\sum_mP_m$ 按原次数分解，$d_m=17m$，则
$$
h!\Lambda_{h,l}(P)=\sum_{a=0}^h\pi_0^a(h)_{\underline a}\sum_m d_m^{h-a}[y^{l+ra}]P_m(f,c).
\tag{10}
$$
这里 $(h)_{\underline a}=h!/(h-a)!$，没有再除以 $a!$。零次幂按一理解，常数部分的方向导数为零。

对 $v=v_2$ 写 $D_v=v_A\partial_A+v_C\partial_C$。

**命题 1。** 在 (6) 下，
$$
J-J^\circ\in p^2\operatorname{Hom}_{\mathcal O}(E_D,\mathcal O^k).
\tag{11}
$$
第 $h=0$ 块的差准确为零。定义
$$
\mathcal T_1(P)=D_vP/17,\qquad\mathcal T_h(P)=h17^{h-2}D_v\{\mathcal E^{h-1}+(h-1)\mathcal E^{h-2}\}P\quad(h\ge2).
\tag{12}
$$
则
$$
\boxed{h!\{\Lambda_{h,l}-\Lambda^\circ_{h,l}\}(P)\equiv\pi_0^2[y^l]\mathcal T_h(P)(f,c)\pmod{p^3}.}
\tag{13}
$$
直接使用原归一行，令 $a=17\tau\in\mathbb F_p^\times$，等价为
$$
\boxed{\frac{J_{rh+l}-J^\circ_{rh+l}}{p^2}(P)\equiv\frac{a^{h-2}}{(h-1)!}[y^l]D_v\{\mathcal E^{h-1}+(h-1)\mathcal E^{h-2}\}P(f,c)\pmod p.}
\tag{13a}
$$
$h=1$ 时第二项省略，系数 $a^{-1}$ 合法。

**证明。** 每个 $P_m$ 的整 Hasse 展开显示：角向阶小于 $r$ 的部分不变；第 $l+r$ 项的差为 $[y^l]D_{v_1}P_m(f^\circ,c^\circ)$；第 $l+2r$ 项的差为
$$
[y^l]D_vP_m+[y^{l+r}]D_{v_1}P_m+[y^l]\sum_{a+b=2}(v_1)_A^a(v_1)_C^b\partial_A^{[a]}\partial_C^{[b]}P_m,
\tag{14}
$$
均在 $(f^\circ,c^\circ)$ 取值。后两项分别被 $p,p^2$ 整除。式 (10) 的 $a\ge3$ 项本来被 $p^3$ 整除；$a=1$ 使用 (7)，$a=2$ 只保留 (14) 第一项。因此全部差模 $p^3$ 为
$$
\pi_0^2\sum_m\left\{\frac{h d_m^{h-1}}{17}+h(h-1)d_m^{h-2}\right\}[y^l]D_vP_m.
\tag{15}
$$
$h=1$ 第二项省略，不使用负次 $d_m$。角向 $l<r$ 可把轴换回 $(f,c)$。这给 (11)–(13a)。$\square$

## 3. 共享的第二整化格

沿用 R198 的原像定义
$$
\Lambda_t(J)=\{x\in p^{-t}E_D:Jx\in\mathcal O^k\},\qquad I_t(J)=J\Lambda_t(J).
\tag{16}
$$
由 (11) 准确有
$$
\Lambda_t(J)=\Lambda_t(J^\circ)\qquad(t=0,1,2).
\tag{17}
$$
尤其 $x\in p^{-2}E_D$ 时两个整性条件相差一个整向量。比较包含准确有理核，没有分别前缀化各 summand。

记共有第二层为 $\Lambda_2$。对 $x\in\Lambda_2$，置 $P=p^2x$，则 $JP\in p^2\mathcal O^k$。R196 在 (4) 范围的完整模 $p$ 核为原权至少 $r$ 的列空间，故唯一写
$$
P=pF+G,\quad F\in\operatorname{span}\{A^iC^j:i+j\le D,\ i+2j<r\},\quad G\in\operatorname{span}\{A^iC^j:i+j\le D,\ i+2j\ge r\}.
\tag{18}
$$
而 $P/p=F+G/p$ 属真实第一层，其全部 $J$ 行被 $p$ 整除。

以下约化到 $\mathbb F_p$，写
$$
g_n(y)=(\mathcal E^nG)(f(y),c(y)).
\tag{19}
$$
原权条件给全部 $g_n\in y^r\mathbb F_p[[y]]$。

**引理 2。** 真实 pair 核进一步给
$$
\boxed{g_n\in y^{r+2}\mathbb F_p[[y]]\ (0\le n\le q-2),\qquad g_{q-1}\in y^{r+\min(s,2)}\mathbb F_p[[y]].}
\tag{20}
$$
**证明。** R199 对同一个 $F+G/p$ 在 $h\ge1$ 块读取
$$
(\mathcal E^hF)(f,c)+\frac h{17\tau}y^{-r}g_{h-1}(y).
\tag{21}
$$
第零块已使 $F(f,c)\in y^r$，因此杀掉 $F$ 常数和原单项式 $A$ 的系数。故每个 $h\ge1$ 的 $(\mathcal E^hF)(f,c)$ 的角向零、一次系数都为零。完整块 $1\le h<q$ 的前两行遂杀 $g_{h-1}$ 的 $y^r,y^{r+1}$ 项；末块杀前 $\min(s,2)$ 项。所有 $h,17\tau$ 是单位。$\square$

只使用同一真实前缀已有行，不要求 $F,G$ 各自满足完整核，也不要求核非零。

## 4. 原方向导数的准确轴式

置
$$
W(y)=f(y)c'(y)-c(y)f'(y)=v_0y^2+\cdots,
$$
$$
K_v=\frac{v_Ac'-v_Cf'}W,\qquad L_v=\frac{v_Cf-v_Ac}W.
\tag{22}
$$
于是 $\operatorname{ord}K_v\ge-2$、$\operatorname{ord}L_v\ge-1$。方向分量为零只会改善这些界。

在同一原平面写 $A=u f(y),C=u c(y)$，$\mathcal E=u\partial_u$。反演准确 Jacobian，在 $u=1$ 处得
$$
\boxed{(D_v\mathcal E^nG)(f,c)=K_v g_{n+1}+L_v g_n'.}
\tag{23}
$$
这是原多项式的链式法则；两个带极点乘子最终给正则轴值，没有增加 $u,y$ 自由源列。

由 (20)、(23)：

- 若 $h\le q-2$，则 $\mathcal T_h(G)(f,c)$ 被 $y^r$ 整除；
- 若 $h=q-1$，其阶至少 $r+\min(s,2)-2$；
- 对部分块 $h=q$，仅用原权条件也有阶至少 $r-2$。

第一条同时使用 $g_{h-1},g_h\in y^{r+2}$，$h=1$ 直接按 $\mathcal T_1$ 处理。第二条用 $g_{q-2}\in y^{r+2}$ 与末块的 $g_{q-1}$ 界；较低的 $D_v\mathcal E^{q-3}G$ 项仍被 $y^r$ 整除。第三条由 $g_n\in y^r$ 和 (22) 直接成立。这里 $q\ge\lceil r/2\rceil\ge3$，没有负下标端点。

## 5. 第三层差只剩至多两条前缀边界行

令 $\mathscr B(k)$ 包含以下真实行号：
$$
\begin{aligned}
&r(q-1)+l,\quad r-2+\min(s,2)\le l<r,\\
&rq+l,\quad r-2\le l<s.
\end{aligned}
\tag{24}
$$
空区间不给行，大小准确为
$$
\boxed{b(k)=\max(2-s,0)+\max(s-r+2,0)\le2.}
\tag{25}
$$

**定理 3。** 在 (6) 下，对每个共有 $x\in\Lambda_2$，
$$
(J-J^\circ)x\bmod p\text{ 只支撑在 }\mathscr B(k).
\tag{26}
$$
特别，当
$$
2\le s\le r-2
\tag{27}
$$
时，准确有
$$
\boxed{(J-J^\circ)\Lambda_2\subset p\mathcal O^k,\qquad\Lambda_3(J)=\Lambda_3(J^\circ).}
\tag{28}
$$

**证明。** 对 $x$ 使用 (18)。由 (13) 除以 $p^2$ 后的模 $p$ 差只读 $\bar P=\bar G$；其余逐行因子 $\tau_p^h(\pi_0/p)^2/h!$ 是单位。第四节说明所有 $h\le q-2$ 整块差消失；第 $q-1$ 块只留 (24) 第一行；部分第 $q$ 块只留第二行。第零块原本准确没有差。因此 (26) 成立。

在 (27) 两区间均为空，得到 (28) 第一式。R198 的准确原像递推为 $\Lambda_3=p^{-1}\Lambda_2\cap J^{-1}(\mathcal O^k)$。对 $x\in p^{-1}\Lambda_2$，第一式使两个整性条件相差整向量，故完全等价。这没有假设矩阵满行秩或源核为零。$\square$

第三层的向后两格角向导数，在绝大多数块中已由同一个真实 pair 的零、一次角向行支付。只有前缀尾端可能留下有限 Schur 差；这里没有把低权、高权部分分别要求为零。

## 6. 准确像秩与源格指数

仍按 R198 定义目标约化秩
$$
r_t(J)=\dim_{\mathbb F_p}\bigl(J\Lambda_t(J)\bmod p\mathcal O^k\bigr).
\tag{29}
$$
由 (11)、(17)，$r_0,r_1$ 对两矩阵相同。在共有 $\Lambda_2$ 上两个模 $p$ 映射之差像包含于 (24) 的至多二维子空间，故
$$
\boxed{|r_2(J)-r_2(J^\circ)|\le b(k).}
\tag{30}
$$
若 $M_D=\operatorname{rank}E_D$，R198 给
$$
\operatorname{length}(\Lambda_3/\Lambda_2)=M_D-r_2.
\tag{31}
$$
所以两矩阵第三源整化增量差至多 $b(k)$，在 (27) 时格本身相同。

目标像增量则是 $\operatorname{rank}_{\mathbb Q_p}J-r_2$。只有另证两矩阵有理秩相同，才可把 (30) 直接转为目标像指数差。本文不假定这一步，也不把源核增长全部计作 jet 范数收益。

## 7. 边界的未来 pair 行、四行重置与跨素数支撑

### 7.1. 剩余边界对应准确的下一块前两行

继续取 $x\in\Lambda_2$，令 $P=p^2x=pF+G$、$X=P/p=F+G/p$。原第一整化格的这些列在整个第一带都给整行，所以即使以下某行尚未进入当前前缀，其值也有定义并且整。

记 $a=17\tau$，并写
$$
K_{-2}=-\frac{v_C}{v_0},\qquad K_{-1}=2v_A-\frac{2f_2v_C}{v_0}+\frac{2c_3v_C}{v_0^2}.
\tag{32}
$$
这正是 (22) 的 $y^{-2},y^{-1}$ 系数。在最后完整块 $h=q-1$，(20) 使 $g_{h-1}$ 的前两项为零。将 (23) 代入 (13a)，准确得到
$$
\begin{aligned}
\overline{(J-J^\circ)x}_{rh+r-2}
 &=\frac h{a^2}K_{-2}\,\overline J_{r(h+1)}(X),\\
\overline{(J-J^\circ)x}_{rh+r-1}
 &=\frac h{a^2}\{K_{-2}\,\overline J_{r(h+1)+1}(X)
                    +K_{-1}\,\overline J_{r(h+1)}(X)\}.
\end{aligned}
\tag{33}
$$
在部分块 $s=r-1$，唯一可留的行同样满足第一式，取 $h=q$。
当 $q=p-2$ 时，这只使用下一块的零次行 $r(p-1)=R$，是 R199 已支付的准确端点，不使用 $R+1$ 之后的行。

式 (33) 的系数可直接核：未来 pair 行为 $a^h g_h/h!$，而当前差的系数为 $a^{h-2}/(h-1)!$，比值是 $h/a^2$。这说明剩余差来自原下一块前两行；不能把这些尚未进入前缀的值视为当前已经支付的观测。

### 7.2. 四行区间的有限源旗标重置

定义同一原源中的有限精度核
$$
K_3(k;J)=\{P\in E_D:J_{<k}P\in p^3\mathcal O^k\}
                         =p^3\Lambda_3(k;J).
\tag{34}
$$
在所有 (27) 的锚点，(28) 给 $K_3(k;J)=K_3(k;J^\circ)$。
若 $\lceil r/2\rceil\le q\le p-3$，取
$$
k_-=rq+r-2,\qquad k_+=r(q+1)+2,\qquad k_+-k_-=4.
\tag{35}
$$
两个端点都处于 (27)。故从 $k_-$ 到 $k_+$ 的累计源旗标商
$K_3(k_-)/K_3(k_+)$ 对两矩阵准确相同，四行间的累计源长度差归零。

同理，在每个这样的锚点，抽象有限像商 $E_D/K_3(k)$ 相同，亦即模 $p^3$ 的截断 Smith 信息一致。这里不声称目标中嵌入的 $I_3$ 格相同，更不把这个有限精度源旗标代作特征零准确前缀的逐行值理想。

### 7.3. 固定 D,k 的跨素数加权支撑

令 $d_{3,p}(D,k;J)=\operatorname{length}(\Lambda_3/\Lambda_2)$。
式 (25) 准确为
$$
b(k)=\begin{cases}
2,&r\mid k,\\
1,&r\mid k-1\text{ 或 }r\mid k+1,\\
0,&\text{其他情形},
\end{cases}
\tag{36}
$$
其中各条件按 $0\le s<r$ 理解，$r\ge5$ 时不重叠。因此固定 $D,k$，对满足本篇范围且满足双中央零条件的素数求和，有
$$
\boxed{\sum_p|d_{3,p}(D,k;J)-d_{3,p}(D,k;J^\circ)|\log p
 \le\{2d(k)+d(k-1)+d(k+1)\}\log(4k+3)=k^{o(1)}.}
\tag{37}
$$
这里 $d(n)$ 是正整数除数个数。因为 $p=4r-1$ 由 $r$ 唯一决定，边界素数分别注入 $k,k-1,k+1$ 的除数集合；所需 $p\le4k+3$ 即得不等式。

最后的估计不需额外解析数论输入：对任意 $\epsilon>0$，大素数 $\ell$ 满足 $a+1\le\ell^{\epsilon a}$；有限个小素数的比值上确界有限，所以 $d(n)\le C_\epsilon n^\epsilon$，再吸收一个对数即可。

式 (37) 只控制这一层的**源指数差**，且只对定理的 admissible 素数求和。它不把 $J^\circ$ 的未知真实范数预算当成已付，也不把同源指数自动转成目标像或准确 jump 的收益。

## 8. 已付信息与下一步

本篇真正使用两个完整中央零条件的第二位，即 (7) 中 $v_1\equiv\pi_0v_2/17\bmod p^2$。它们在原全部次数列上产生 (13) 的同一个方向扰动；原次数可以任意大，且始终不传递“乘积中央零”的假设。

结论 (28) 说明，不能把这两个低中央轴项的第三层出现直接再计作整块独立条件收益：在 (27) 的完整前缀中，实际第三层整化格对此有限扰动完全不变。边界已由 (33) 表达为未来两条 pair 行；它们在当前前缀中未必已观测。更高轴项与更高精度未被删去。

与此同时，$J^\circ$ 的共同像、更高整化及原第一带之外的前缀仍须实际分析。本文没有取得 R159 所需的严格全次数预算，也没有从辅助矩阵的形式定义推断原中央导数非零。

依赖：

- [R185：完整整轴 Stokes 泛函与多层中央条件](R185-integral-axis-stokes-functional-and-complete-central-tests.md)，尤其 (30)。
- [R196：原源的完整第一带核](R196-continuous-first-band-euler-pade-kernel.md)。
- [R198：同一原像格、共同像及准确层指数](R198-joint-image-saturation-and-complete-prefix-smith.md)。
- [R199：特征零准确第一带与全部耦合除幂像](R199-exact-first-band-exponential-and-complete-divided-image.md)。
