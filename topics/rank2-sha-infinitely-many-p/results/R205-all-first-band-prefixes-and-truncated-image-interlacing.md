# R205. 任意第一带前缀的末两行控制与模 p³ 有限像交错

日期：2026-11-12。**状态：任意原次数、任意合法第一带前缀上的
末两行控制、真实整化格交错、有限目标像分解及其跨素数代价均已
证明。** 这里不要求 R201 的 $q\ge\lceil r/2\rceil$，因而覆盖
$p>8D$ 中原源可发生 Hermite–Padé 抵消的小 $q$ 范围。结论仅在
所示有限精度成立，不将其当成全部深度的准确 jet 范数。

## 1. 同一原源与合法前缀

取惰性 $p=4r-1\ge19$、$R=r(p-1)$，保留
$$
 \mathcal O=\mathbb Z_p,\qquad
 E_D=\mathcal O[A,C]_{\le D},\qquad C=B-A,\qquad
 A=w+\cdots,\quad C=v_0w^2+\cdots,\quad v_0=-22.
 \tag{1}
$$
$D$ 任意。整轴、原归一行和常数仍为
$$
 A=\Gamma^{17}f(y),\quad C=\Gamma^{17}c(y),\quad
 f=y+\cdots,\quad c=v_0y^2+\cdots,\quad
 a_p=17pu_0\in\mathcal O^\times,\quad a=\bar a_p,
 \tag{2}
$$
$$
 J_n(P)=p^{\lfloor n/r\rfloor}[w^n]P(A(w),C(w)),\qquad
 \mathcal E=A\partial_A+C\partial_C.
$$
取 $k=rq+s$、$0\le s<r$、$0\le q\le p-2$，使用全部 $n<k$
的行。R199 准确给
$$
 J_{rh+l}(P)=
 \sum_{i=0}^h p^{h-i}\frac{a_p^i}{i!}
 [y^{l+r(h-i)}](\mathcal E^iP)(f,c).
 \tag{3}
$$
所有相关阶乘为单位。没有改变原参数或多项式源。

假设原两个完整中央导数同时为零。置
$v_1=(f_r,c_r)$、$v=v_2=(f_{2r},c_{2r})$。R185 给
$$
 v_1\in p\mathcal O^2,\qquad
 v_1-\frac p{a_p}v\in p^2\mathcal O^2.
 \tag{4}
$$
依 R201 在同一 $E_D$ 上删去轴的 $y^r,y^{2r}$ 两项，得到有限
比较矩阵 $J^\circ$。保留同一个 $u_0$，不把比较形式平面称为
原 theta 曲线。R201 §2 的计算仅使用 (3)–(4)，不使用其较强
$q$ 范围，因此对本篇全部前缀准确有
$$
 J-J^\circ\in p^2\operatorname{Hom}(E_D,\mathcal O^k),
 \tag{5}
$$
及
$$
 \frac{J_{rh+l}-J^\circ_{rh+l}}{p^2}(P)
 \equiv\frac{a^{h-2}}{(h-1)!}[y^l]
 D_v\{\mathcal E^{h-1}+(h-1)\mathcal E^{h-2}\}P(f,c)
 \pmod p,\qquad h\ge1.
 \tag{6}
$$
这里 $D_v=v_A\partial_A+v_C\partial_C$。$h=1$ 时第二项省略；
第 $h=0$ 块的差准确为零。式 (6) 保留原全部齐次块。

## 2. 不依赖高权源分裂的两个额外角向零

按原像定义
$$
 \Lambda_t(k;J)=
 \{x\in p^{-t}E_D:J_{<k}x\in\mathcal O^k\}.
 \tag{7}
$$
由 (5)，$J$ 与 $J^\circ$ 在 $t=0,1,2$ 的这些格完全相同。
记共同第二层为 $\Lambda_2(k)$。

取 $x\in\Lambda_2(k)$，置
$$
 P=p^2x\in E_D,\qquad
 \widetilde g_n(y)=(\mathcal E^nP)(f(y),c(y))\in\mathcal O[[y]],
 \qquad g_n=\widetilde g_n\bmod p.
 \tag{8}
$$
于是 $J_{<k}P\in p^2\mathcal O^k$。此处始终使用 $P$ 本身，
**不**把 $\bar P$ 先写成原权至少 $r$ 的多项式；这种写法在小
$q$ 范围通常不成立。

设 $q\ge1$。第零块包含原行 $0,1$，故 $P$ 的常数项及原
单项式 $A$ 的系数都属于 $p^2\mathcal O$。因此对每个 $h\ge1$，
$\widetilde g_h$ 的角向零次、一次系数都在 $p^2\mathcal O$ 中。

另一方面，(3) 的模 $p$ 先给
$$
 g_n\in y^r\mathbb F_p[[y]]\quad(n<q),\qquad
 g_q\in y^s\mathbb F_p[[y]].
 \tag{9}
$$
使用真实行 $h=n+1$、$l=0,1$ 到模 $p^2$，其首项已被上面的
常数、线性结论消去；余下为
$$
 J_{r(n+1)+l}(P)
 \equiv p\,\frac{a_p^n}{n!}
           [y^{r+l}]\widetilde g_n
                                  \pmod{p^2}.
 \tag{10}
$$
只要这一行属于前缀，除以所示单位和一个 $p$ 即得该系数模 $p$
为零。结合 (9)，准确有
$$
 \boxed{\begin{aligned}
 g_n&\in y^{r+2}\mathbb F_p[[y]]
                       &&(0\le n\le q-2),\\
 g_{q-1}&\in y^{r+\min(s,2)}\mathbb F_p[[y]],\\
 g_q&\in y^s\mathbb F_p[[y]].
 \end{aligned}}
 \tag{11}
$$
$q=1$ 时第一行的范围为空。这里每一个新增零都由原完整前缀的
现有行支付，无须使用 R196 最终的高权理想描述。

## 3. 任意 q 的末两行定理

设
$$
 W=fc'-cf'=v_0y^2+\cdots,\qquad
 K_v=\frac{v_Ac'-v_Cf'}W,\qquad
 L_v=\frac{v_Cf-v_Ac}W.
 \tag{12}
$$
准确的原平面 Jacobian 反演给
$$
 (D_v\mathcal E^nP)(f,c)=K_v\widetilde g_{n+1}
                               +L_v\widetilde g_n',
 \qquad
 \operatorname{ord}K_v\ge-2,\quad\operatorname{ord}L_v\ge-1.
 \tag{13}
$$
虽用 Laurent 乘子，左侧仍是原多项式的正则轴值。

**定理 1。** 对任意合法 $k$ 和每个共同 $x\in\Lambda_2(k)$，
$$
 \boxed{\quad
 (J_{<k}-J^\circ_{<k})x\bmod p
 \text{ 只可能支撑在 }k-2,k-1\text{ 两行。}
 \quad}
 \tag{14}
$$
不存在的负行号省略。若 $q=0$，两个矩阵准确相同。

**证明。** 在 (6) 中代入 $P=p^2x$，其模 $p$ 差由 (11)–(13)
计算。完整块 $1\le h\le q-2$ 的两个方向导数均被 $y^r$ 整除，
故全块差为零。最后完整块 $h=q-1\ge1$ 的差阶至少
$r+\min(s,2)-2$，因而只可能留最后 $(2-s)_+$ 条。

对于部分块 $h=q$，主项 $K_vg_q$ 的阶至少 $s-2$，其余项的
阶至少 $s$ 或更高。因此只可能留该部分块最后 $\min(s,2)$ 条。
若 $s=0$ 没有部分块；若 $s=1$，一条位于最后完整块末尾，一条
位于当前部分块；若 $s\ge2$，两条都位于当前部分块末尾。这些
行恰为 $k-2,k-1$。

$q=1$ 时，最后完整块是 $h=0$，其差本来准确为零；只需保留
上述部分块论证。$h=1$ 的负 Euler 次数项始终省略。
$q=0$ 只读角向阶小于 $r$ 的原轴，所以差准确为零。$\square$

R201 的较强范围还给 $g_q\in y^r$，故那里可以进一步得到除数
支撑。本定理不使用这一步，因而真正适用于 $p>8D$ 的小 $q$。

## 4. 真实格与模 p³ 有限像的双向交错

定义
$$
 K_3(k;J)=
 \{P\in E_D:J_{<k}P\in p^3\mathcal O^k\}
                    =p^3\Lambda_3(k;J).
 \tag{15}
$$

**推论 2。** 当两端的前缀合法时，准确有
$$
 \boxed{\begin{aligned}
 \Lambda_3(k;J)&\subset
       \Lambda_3(\max(k-2,0);J^\circ),\\
 \Lambda_3(k;J^\circ)&\subset
       \Lambda_3(\max(k-2,0);J).
 \end{aligned}}
 \tag{16}
$$
相同包含对 $K_3$ 成立。

**证明。** 若 $x\in\Lambda_3(k;J)$，则
$px\in\Lambda_2(k)$。定理 1 使
$(J-J^\circ)px$ 的前 $k-2$ 个分量被 $p$ 整除，所以
$J^\circ x$ 的这些分量整。反方向使用同一个共有 $\Lambda_2$；
不必把 $J^\circ$ 当成另一条满足独立中央假设的实际曲线。$\square$

因此存在自然满射
$$
 E_D/K_3(k+2;J)\longrightarrow E_D/K_3(k;J^\circ),
 \tag{17}
$$
以及交换两矩阵的同类满射。它们是原目标模 $p^3$ 的真实有限像
之间的映射，不只是维数比较。这里 $k+2$ 也须处于已付第一带。

还能把它写成有限目标行算子。置 $\mathscr R=\mathcal O/p^3$。
由 (17)，每条 $J^\circ_n$ 在 $\mathscr R$ 上经
$J_0,\ldots,J_{n+2}$ 的共同像因子化。这个像上的线性泛函可以
延拓到整个自由目标 $\mathscr R^{n+3}$：在整 Smith 基下，其
各个源 summand 是 $p^a\mathscr R$；其像必须被 $p^{3-a}$ 杀死，
所以属于 $p^a\mathscr R$，即可选择一个自由坐标系数作延拓。
故存在 $\mathscr R$ 上的矩阵 $T_k$，每条第 $n$ 行只使用列
$0,\ldots,n+2$，满足
$$
 \boxed{\quad
 J^\circ_{<k}=T_kJ_{<k+2}\pmod{p^3}.
 \quad}
 \tag{18}
$$
反向同样成立。这是实际有限像上的整分解，但没有证明
$T_k$ 可取为 $I+p^2S$，也没有把它提升为全精度的统一算子。

## 5. 同一 k 的截断 Smith 代价

设
$$
 r_t(k;J)=\dim_{\mathbb F_p}
      \bigl(J_{<k}\Lambda_t(k;J)\bmod p\mathcal O^k\bigr).
$$
由 (5) 及共有的第一、二层，
$$
 r_0(k;J)=r_0(k;J^\circ),\qquad
 r_1(k;J)=r_1(k;J^\circ).
$$
在共有 $\Lambda_2(k)$ 上，定理 1 使两个模 $p$ 映射的差像至多
二维。因此
$$
 \boxed{|r_2(k;J)-r_2(k;J^\circ)|\le2.}
 \tag{19}
$$
R198 的准确源层公式给
$$
 \left|
 \operatorname{length}\frac{\Lambda_3(k;J)}{\Lambda_2(k)}
 -
 \operatorname{length}\frac{\Lambda_3(k;J^\circ)}{\Lambda_2(k)}
 \right|\le2.
 \tag{20}
$$
因为第二层相同，这也控制
$\operatorname{length}(\Lambda_3/E_D)$ 的差。等价地，两个真实
有限像 $E_D/K_3(k)$ 的长度差至多二。

这些表述都允许不同的特征零核和有理秩。若要把源层指数直接
转成 R198 的目标整像指数，还必须另证两边有理秩相同。
即使有理秩相同，(19)–(20) 也只控制前三层的截断信息，未控制
全部 Smith 指数或特征零准确前缀的逐行值理想。

## 6. 大素数范围的已付代价

固定 $D,k$，对本篇合法且满足双中央零条件的素数求和。
$q=0$ 时没有差；$q\ge1$ 时 $r\le k$，故 $p\le4k-1$。
令 $d_{3,p}$ 表示 (20) 中第三层的源增量，则
$$
 \boxed{\quad
 \sum_p|d_{3,p}(D,k;J)-d_{3,p}(D,k;J^\circ)|\log p
 \le2\sum_{p\le4k}\log p=O(k).
 \quad}
 \tag{21}
$$
这里只使用初等 Chebyshev 上界。可由
$\binom{2n}{n}\le4^n$ 控制区间 $(n,2n]$ 中的素数乘积，再按
二进尺度求和得到所需常数。限制到 $p>8D$ 后不等式仍成立。

R191 已付原所有真实跳阶的全局界
$k\le(1+o(1))D^2$。因此当 $D$ 足够大、$p>8D$ 时，这些跳阶
都远小于 $R=(p^2-1)/4$，属于本篇使用的完整第一带范围。
这里没有把前缀核为空当作范数收益；只说明若该原真实跳存在，
本篇的有限精度比较适用。

式 (21) 给出这一次中央删项的第三层源代价，不等于已经把
$p>D$ 的全部实际 jet 范数降到 $O(k+D)$。仍需分析比较矩阵的
真实像及第四层以上的同源 Schur，或另得原中央非零输入。

## 7. 全精度 Laurent 表达及尚未支付的接口

以下准确恒等式有助于继续更高层，同时明确非规范角向条目
不能免费当成已观测行。对 $P\in E_D$，仍写
$\widetilde g_h=(\mathcal E^hP)(f,c)$，并置
$$
 \mu=\frac p{a_p y^r},\qquad
 \mathcal R_h(P)=\sum_{t=0}^h(h)_{\underline t}\mu^t
                                      \widetilde g_{h-t}(y).
 \tag{22}
$$
这是整 Laurent 级数的有限和，且特征零中准确有
$$
 \boxed{\quad
 J_{rh+l}(P)=\frac{a_p^h}{h!}[y^l]\mathcal R_h(P),\qquad
 \mathcal R_h=\widetilde g_h+h\mu\mathcal R_{h-1}.
 \quad}
 \tag{23}
$$
相应的指数生成式为
$$
 \sum_{h\ge0}\mathcal R_h(P)\frac{z^h}{h!}
   =\frac{P(e^zf(y),e^zc(y))}{1-\mu z}.
 \tag{24}
$$
所需第一带只取 $h<p$，故这些行归一不损失阶乘的单位性。

若真实完整前缀的行均在 $p^N$，则归纳使用 (23) 可知：
完整块的 $\mathcal R_h$ 模 $p^N$ 被 $y^r$ 整除，当前部分块
被 $y^s$ 整除。特别，负幂也已支付——其来源只可能是
$h\mu\mathcal R_{h-1}$，而前一完整块已被 $y^r$ 整除。
实际上，负幂系数比该前缀精度还多一个 $p$。
这一步允许在已付范围内合法使用 (13) 的 Laurent 乘子。

但是 $[y^{l+r}]\mathcal R_{h-1}$ 不是规范的第 $(h-1)$ 块
角向行。式 (23) 本身没有从唯一的
$J_{rh+l}$ 分离出全部同总权的潜在系数。
所以 (24) 尚未给出任意精度 $N$ 下、统一有限向未来带宽的
目标算子。该可观测性及真实高层像正是下一步需支付的内容，
不能由环境 core 读取或核的位置单独替代。

R204 还给一个必须保留范围的校准。在其
$D\ge2r-1$、$q=\lceil r/2\rceil$、$2\le s\le r-2$ 的实际构造中，
若 $t_1=v_1/p$ 模 $p$ 非零，则存在原 $P=pY\in E_D$，满足
$J_{<k}P=0$，但 $J^\circ P$ 在原 $r$ 或 $r+1$ 行的赋值准确为三。
因此一般 $D$ 下不能把本篇三层的两位置交错自动迭代到第四层。
这是带明确单位假设的构造，不是已经验证存在某个实际双中央
失败素数；若 $t_1$ 有更高赋值，所示两行只在更深层给见证。
R204 两矩阵的全部已付 Smith 与值理想仍相同，不能把核方向
变化误记成净范数变化。其宽源构造不适用于当前重点
$p>8D$ 的小次数范围。

依赖：

- [R185：同一整轴及完整中央条件](R185-integral-axis-stokes-functional-and-complete-central-tests.md)。
- [R191：原源的真实跳阶界](R191-first-band-source-divisibility-and-global-multiplicity.md)。
- [R198：真实原像格与共同像指数](R198-joint-image-saturation-and-complete-prefix-smith.md)。
- [R199：准确完整第一带指数公式](R199-exact-first-band-exponential-and-complete-divided-image.md)。
- [R201：第三层的准确双中央扰动](R201-double-central-perturbation-and-third-layer-schur.md)。
