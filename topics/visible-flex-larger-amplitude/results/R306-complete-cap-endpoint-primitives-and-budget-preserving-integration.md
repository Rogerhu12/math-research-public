# R306：完整 cap 的三项端点 primitive 与保留真实余责的积分路径

- 作者：AI
- 日期：2026-11-15 UTC
- 状态：下述实函数恒等式、闭区间包含与程序责任命题已证明；独立 v3 的实际科学结果尚未产生。
- 范围：[R286](R286-original-stored-continuous-integral-and-metric-bridge.md) 明确约定 C 的同一连续对象；承接 [R297](R297-continuous-E-unit-panel-and-piecewise-enclosure.md) 的单位面板包含以及 [R304](R304-actual136-cap-callback-budget-and-unpaid-domain.md) 的真实未完成结果。
- 对应独立源：`geometry_20261115_stored_continuous_E_cover_v3.py`。旧原 producer 9aa0 与 v2 0040 均保持原字节。

## 306.1 问题、对象与结论范围

实际136没有完成1440个有限原 pieces，也没有得到自然外半径或一个完整径向 query。原日志中 cap 的非解析 callback 次数很大；末面板的完整 $w_x$ 包围不含零，却仍跨可能的 raw／transition-low 边界。这为改进提供了具体切点，但不是单一根因证明，亦不保证下次运行成功。

这里没有将 cap 删除、将 slope 还原成 raw、把有限 selector 改称连续目标，或重新选择冻结常数。$w$ 始终是原连续解释下经过 cap、valley、flat 与 cut-preserving 后写入的同一个正函数。记

$$
E=1+w^2,\qquad q=w_x,\qquad K>0.
$$

源的六项函数依次为

$$
(A,B,\sqrt E A,\sqrt E B,wA,wB).
\tag{306.1}
$$

本结论只简化其中第0、2、4项在 $\chi\equiv1$ 且完整闭面板已证 $q$ 同号时的求积。其余三项不省略；两个原 $\chi$ 过渡 pieces 不用这个简化；同号未能证明也保原积分／细分与完整未付责任。原所有工作精度、预算及几何验收条件不变。

## 306.2 原 cap 的精确实函数

固定 $L>0$，定义原多项式

$$
H(t)=t^5\left(7-14t+10t^2-\frac52t^3\right).
\tag{306.2}
$$

直接按多项式恒等式微分，

$$
H'(t)=35t^4-84t^5+70t^6-20t^7,\qquad
H''(t)=140t^3(1-t)^3.
\tag{306.3}
$$

从而端点二 jet 为

$$
(H,H',H'')(0)=(0,0,0),\qquad
(H,H',H'')(1)=\left(\frac12,1,0\right).
\tag{306.4}
$$

此外，

$$
H'(t)+H'(1-t)=1,\qquad
H(1-t)=H(t)-t+\frac12.
\tag{306.5}
$$

证明：第一式左端导数为 $H''(t)-H''(1-t)=0$，在 $t=0$ 的值为1；再对第二式两侧的差求导得零，在 $t=0$ 核其常数即得。此处是对整个实变量的多项式恒等式，不依赖取样或浮点近似。

设原 raw log-slope 为 $a(x)$，可变 log-cap 为 $c(x)$，两者在所讨论的原闭 piece 上均为 $C^2$；令 $z=a-c$。源的四个分支是

$$
G(a,c)=
\begin{cases}
a,&z\le -L,\\
a-2L\,H\!\left(\dfrac{z+L}{2L}\right),&-L\le z\le0,\\
c-2L\,H\!\left(\dfrac{L-z}{2L}\right),&0\le z\le L,\\
c,&z\ge L.
\end{cases}
\tag{306.6}
$$

在 $z=0$，两个 transition 分支不只是二 jet 相同：由(306.5)，它们是同一个关于 $(a,c)$ 的多项式表达。于是可统一写成

$$
G(a,c)=c+\psi(a-c),\qquad
\psi(z)=
\begin{cases}
z,&z\le-L,\\
z-2L\,H\!\left(\dfrac{z+L}{2L}\right),&-L\le z\le L,\\
0,&z\ge L.
\end{cases}
\tag{306.7}
$$

在 $z=-L$，中段的 $(\psi,\psi',\psi'')$ 为 $(-L,1,0)$；在 $z=L$，它为 $(0,0,0)$。因此 $\psi$ 是全实轴上的 $C^2$ 函数，$G(a(x),c(x))$ 为 $C^2$，即使 $z(x)$ 在阈值处切触、往返或具有非孤立零点，也不需要逐个定位 crossing。

这同时支付了 $-L,0,L$ 的完整接缝，且允许 $a,c$ 都随 $x$ 变化。把 $c$ 当常数后才成立的推导不能替代本式；本式通过复合 $c+\psi(a-c)$ 直接包含 $c',c''$ 的全部项。

## 306.3 原 valley、flat、cut 覆写后的同一个 $w$

源的平滑阶跃是

$$
S(x)=x^3(10-15x+6x^2),\qquad
S(0)=0,\ S(1)=1,\ S'(0)=S'(1)=S''(0)=S''(1)=0.
\tag{306.8}
$$

在每个原 piece 内，raw log-slope 由真实常数、仿射项和 $S$ 多项式组成。valley 在相邻原段的增加项依次为 $\beta S,\beta,\beta(1-S)$，故各段内部均为 $C^2$；端口两阶相容沿原同一 $\beta$ 与(306.8)检查。可变 cap 的 log 值由同一 $S$ 在原相邻层级间插值，同样是准确函数，不把标签中的导数当作另一个函数的导数。

完成(306.6)之后，源仍按原次序执行：

1. full-flat：$g=\ell_{\rm flat}$；
2. flat-transition：$g=(1-S)G+S\ell_{\rm flat}$；
3. 最后一个 cut-preserving 原段：$g=a$；
4. 其前一个 cut-preserving 原段：$g=a+(1-S)(G-a)$，其中 $G$ 在这里包括实际先前的 flat 覆写。

每项在一个原闭 piece 上均为 $C^2$，覆盖分支边界的乘积／复合使用真实求导规则。最后

$$
w(x)=e^{g(x)}
\tag{306.9}
$$

正且为 $C^2$，$q=w_x=e^g g_x$ 正是源完整 Jet2 表达的第一导数。

本节并不从一个 schema 自动推全1440片连接成功。不同原 piece 端口仍需 R286 的真实共享层级、实数 port 关系、合法 flat 过渡索引与 protected join 条件；源仍输出这些实际条件及未付标记。下面的端点公式只需每一个被积闭 piece 内的 $C^1$，因此既不越过未付 seam，也不通过改变端口来制造相容性。

## 306.4 三项端点恒等式

**命题306.A。** 在闭面板 $I=[a,b]$、$a<b$ 上，设完整 $w\in C^1(I)$、$w>0$、$K>0$、$\chi\equiv1$。若存在 $\sigma\in\{-1,1\}$ 使 $\sigma q(x)\ge0$ 对所有 $x\in I$ 成立，则

$$
\begin{aligned}
\int_a^b A\,dx
 &=\frac{\sigma}{K}
 \left[\frac{w}{\sqrt{1+w^2}}\right]_a^b,\\
\int_a^b \sqrt E A\,dx
 &=\frac{\sigma}{K}[\arctan w]_a^b,\\
\int_a^b wA\,dx
 &=\frac{\sigma}{K}
 \left[-\frac1{\sqrt{1+w^2}}\right]_a^b .
\end{aligned}
\tag{306.10}
$$

证明。原完整表达是

$$
A=r_xj_0(1-\chi)+
  \frac{\chi |q|}{K(1+w^2)^{3/2}}.
\tag{306.11}
$$

因此 $\chi=1$ 后，第一项准确为零，且 $|q|=\sigma q$。三个一元原函数的导数分别为

$$
\frac{d}{dw}\frac{w}{\sqrt{1+w^2}}
 =\frac1{(1+w^2)^{3/2}},\qquad
\frac{d}{dw}\arctan w=\frac1{1+w^2},\qquad
\frac{d}{dw}\left(-\frac1{\sqrt{1+w^2}}\right)
 =\frac{w}{(1+w^2)^{3/2}}.
\tag{306.12}
$$

对实际 $C^1$ 函数 $w(x)$ 使用实链式规则与微积分基本定理即得三式。证明不要求 $q$ 严格非零；若完整面板已证 $q\equiv0$，三积分均准确为零。证毕。

特别地，(306.10)允许 $w$ 穿过任意多个 cap 分支。积分恒等式属于完整实函数，并不要求该函数在跨 cap 的复邻域上解析。源不能因这一实恒等式成立，就将剩余 Acb callback 的 `analytic=True` 合同放松。

以下均不充分：仅端点 $q$ 同号、面板中心 $q$ 同号、有限采样同号、某一可能分支同号、仅 raw 导数同号。本算法只用已包含全部原可能分支的完整闭面板 $q$ 区间作证明。

## 306.5 所有原可能端点分支的包含

在精确有理端点 $x_0$，由 `possible_branches(x0,x0)` 生成所有没有被严格区间比较排除的原分支。它可以因常数包围而包含多个分支；此时不得擅选 midpoint 或首项。

令 $\mathcal B(x_0)$ 为该集合，$W_\beta(x_0)$ 是对分支 $\beta$ 执行完整 cap/flat/cut 原次序后得到的 $e^g$ 球。定义

$$
W(x_0)=\operatorname{hull}_{\beta\in\mathcal B(x_0)}W_\beta(x_0).
\tag{306.13}
$$

真实分支必在 $\mathcal B(x_0)$ 内；阈值上(306.6)的值一致。因此真实 $w(x_0)\in W(x_0)$。多包含一个无法排除的多项式延拓只会放宽包围，不会丢真实值。对 $W(a),W(b)$ 分别用严格实球运算计算(306.10)，正平方根的真值由 $1+w^2>0$ 保证。

区间实现若因 dependency 把正性或有限性暂时丢失，只能放弃该次端点候选并保原求积／细分；不能取绝对值改写 $w$、取平方根实部或缩小为方便的假区间。所有 endpoint 计算产生的舍入误差都在球内，未将打印中心当准确数。

对两个端点分别包围会丢失一些相关性，但所得差仍包含实际差。即使它较宽，也不影响包含命题；不能据此宣称达到工作精度。

## 306.6 与原六分量包含及工作目标的组合

记原完整实范围 $F_k(I)$，其长度乘积

$$
C_k=(b-a)F_k(I)
\tag{306.14}
$$

包含第 $k$ 项真实积分。对 $k\in\{0,2,4\}$，在命题306.A前提已证时，端点式给另一个包含 $T_k$。于是

$$
I_k\in C_k\cap T_k.
\tag{306.15}
$$

交集若空，必须显式登记包含不一致。若实现回退独立已证有效的原实范围，必须写明该次收紧失败；不能把空交当作成功收紧或静默选择方便的数。未启用端点式的项始终保原 $C_k$；以后 Acb 若给出严格 $J_k$，再与已有包含相交。不存在缺失或默认为零的分量。

原完整全宽工作目标仍逐项为

$$
\operatorname{upper}(I_k)-\operatorname{lower}(I_k)
 \le
 \varepsilon_A(b-a)+
 \varepsilon_R\max\!\left(
 |\operatorname{lower}(I_k)|,\,
 |\operatorname{upper}(I_k)|
 \right).
\tag{306.16}
$$

已有严格包含达到(306.16)时，该项无需再调用 Acb；这是同一个积分已有足够包围，不是额外近似或科学验收门。未达到时仍允许原 Acb 收紧，恢复原单位后复核(306.16)。两个 $\chi$ 过渡 pieces、同号未证的面板，以及第1、3、5项均保这种完整路径。

沿 R297，Acb 的误差半径与最终球全宽是不同量。缩放及 guard bits 只是工作配置；最终判断仍是(306.16)。到既定最大深度时，原有效 coarse 包围仍可保留并明确工作分辨率未付。不能将一个有限粗界冒成任意小误差，也不删除它覆盖的闭区间。

## 306.7 cap 成本的实际边界

这一优化消去的是满足前提的三个原绝对导数积分所需的数值求积。它不会强称三项 $B,\sqrt E B,wB$ 在跨 cap 处解析，也不抹除它们的分支成本。它不保证所有面板都能证明 $q$ 同号，不保证端点差宽度足够窄，不保证同预算完成全部 query。

实际136末面板的原记录为 $\chi=1$ 所在原 cell5/segment5，且完整 $q$ 区间正；可能 branches 仍是 raw／transition-low。因而端点规则的适用性可由已存字段与原表达位置判断。这不等于已经计算本次三端点值，也不把该面板的事实推广为全部全域。新的具体结果必须由独立139实际执行产生。

## 306.8 预算 callback 的受支持传输

原 python-flint0.9.0 的 [acb.pyx](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb.pyx) 中，C callback 对 `TypeError,ValueError` 才显式保存并在调用返回后重抛；原全局 `ResourceStop` 直接继承 `Exception`。R304已准确保留136的真实 `SystemError`，没有事后改写原异常。

新路径保全局异常类别，只作以下局部操作：

1. 在本次 callback 内确切捕获真正抛出的 `ResourceStop`，保存其原对象、类型、原因与当前分量身份。
2. 仅为跨 C callback 传输，改抛带专用标识的 `ValueError`。
3. 只有本次调用的已保存原 `ResourceStop` 存在，且收到对应支持通道返回时，才恢复原 `ResourceStop`。
4. 未登记的 `ValueError` 沿原有效实范围 fallback；未登记的 `SystemError` 或其它未知异常保持真实错误，不靠 elapsed 猜测。
5. callback 若在登记后被库再次请求，不再执行新的科学函数，继续通过同一专用通道返回停止。

这项修改不把所有异常都归为资源，不修改数学函数，也不延长原声明预算。C 库返回到 Python 的时刻仍决定实际记录的 elapsed；不能承诺外部库恰在预算秒数内中止。

## 306.9 完整 pending、已付 prefix 与未付后缀

原积分 DFS 使用闭有理面板，每次细分为 $[a,m]$ 与 $[m,b]$，保持共同端点；栈先处理左子面板。因此，在第一次停止时：

- 所有 accepted 面板构成已访问原区间的连续左前缀；
- 当前面板及尚未访问的栈仍保原完整闭区间；
- 不允许跨过缺口把后面的增量加到当前径向位置；
- 当前 piece 后的全部原 piece 由完整 index 与连续后缀表示；
- query plan 全部保留，未证明源完整时不给自然域的已付标记。

恢复后的真实 `ResourceStop` 交原 `integrate` 的 pending 收尾，使 `build_head` 正常返回其实际完成 piece 数、已付前缀、当前 piece 的剩余面板和完整后缀。已付前缀六 primitive 与前缀半径单独命名，不叫完整有限头，也不叫 $R_{\rm out}$。

精确 ResourceStop 以外的未知错误仍保原 generic failure，并明确它未完成的范围；本命题不保证任意未知错误后都能重建所有中间对象。尤其不能据日志的计数恢复未保存的全六累计量。

只有原全部1440 pieces、深尾及所请求域已完成时，才能沿既有定义形成真实自然外半径和完整查询责任。任一预算失败、值域不足或 model/seam 条件未付都不构成几何不存在证明。

## 306.10 对象、代码与执行责任

本结论保持同一 R286 约定 C、原冻结参数、原根族、六 primitive、真实 cut/cuff/weight/flat/valley 和自然 $R_{\rm out}$。它不把旧有限 selector 的误差自动付清，不把名义 cut 等同自然外半径，不在外域补 $E=1$。

源只改积分实现与真实中断记录；原实表达定义和其它 query／深尾数学仍由已发表源承接。没有实际 accepted field，没有新的 C 零响应／native J，没有相对 metric 阈值、全曲面 reach、held 或 BVP 完成声明。局部 source-only AST／身份检查不是科学验证；139将按原输入和原预算直接公开执行，不以另一个合成 fixture 作为前置门。

实现所用实球 `atan/sqrt/union/lower/upper` 的语义见 [python-flint0.9.0 arb文档](https://python-flint.readthedocs.io/en/stable/arb.html)。它们仅提供所调用严格区间操作；整个闭覆盖、端点函数前提、模型身份和余责仍由本文及源的实际分支保持支付。
