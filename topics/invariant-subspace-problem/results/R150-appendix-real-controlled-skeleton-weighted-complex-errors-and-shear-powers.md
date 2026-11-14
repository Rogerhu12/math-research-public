# R150 附录：实受控辅助骨架的复加权扰动与全部剪切点态幂

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根完整核验原 Bell 仿射替换、共同图核心、局部相伴单位和两支排核输入；独立说明新原始系数范围，不重复登记两条旧排核预算。

## 1. 定理与范围扣除

固定
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
b_j\in\mathbb R,\qquad |b_j|\le C_0a_j,
\tag{1.1}
$$
其中 $C_0<\infty$ 任意。
再取复数 $\gamma,u_*,v_*$、复行 $e_0,e_1\in\ell^1$，
以及复行 $d$ 满足
$$
d_j=0\quad(a_j=0),\qquad
\|d\|_a^2:=\sum_{a_j>0}\frac{|d_j|^2}{a_j}<\infty.
\tag{1.2}
$$
定义原始点态模式
$$
u=u_*+\sum_j(a_j+e_{0j})\chi_j,
$$
$$
v=v_*+\sum_j(b_j+\gamma a_j+d_j+e_{1j})\chi_j.
\tag{1.3}
$$

设
$$
G(x,z)=z^m+\sum_{\substack{i+j\le m\\j<m}}g_{ij}x^iz^j,
\qquad m\ge1,\quad g_{ij}\in\mathbb C.
\tag{1.4}
$$
则对全部 $\lambda\in\mathbb C$、整数 $r\ge1$
及任意复 $\ell^2$ first 指数权 $w$，
$$
\boxed{[G(u,v-u^2)-\lambda]^re^w
\text{ 是实际 }A\text{ 的循环向量}.}
\tag{1.5}
$$
没有主行增长、尾比或排序正则性要求。

当 $d=0$ 时，这是已推
[计数/柱预算二分](R150-appendix-counting-column-budget-dichotomy-and-all-real-controlled-shears.md)
的实骨架、复线性项和复 $\ell^1$ 余项范围。
当整个辅助行都属于复仿射主行加加权余项时，则由
[加权相对域稿](R150-appendix-weighted-first-relative-domains-local-ratios-and-leading-homogeneous-cyclicity.md)
已有更广的最高齐次结论。
本稿新增允许同时存在独立、不可和的实受控骨架 $b$，
以及不可和的复加权误差 $d$；
通常原始 $X_vX_a^{-1}$ 并不由此有界。

主行在本稿仍只允许 $a$ 加复 $\ell^1$ 余项。
没有把加权主行扰动免费带进下面的两个正 first 论证。

## 2. 实际参考行及有界加权比率

始终以未倾斜的实际参考算子
$$
X=X_{\sum a_j\chi_j},\qquad
Y=X_{\sum b_j\chi_j},\qquad L=X^{-1}
\tag{2.1}
$$
工作。
$X$ 最大增生且空谱，$L\in A'$ 有界拟幂零；
$Y$ 是实 first，但不假定它的任何预解点。

加权相对域稿的完整二次型和图核心证明给
$$
\operatorname{Dom}X\subseteq\operatorname{Dom}X_d,\qquad
B_d=X_dL\in\mathcal B
:=\overline{\operatorname{alg}}(I,\mathcal A,L),\qquad
\phi(B_d)=0,
\tag{2.2}
$$
其中 $\mathcal B$ 是有唯一字符 $\phi$ 的实际交换 Banach 代数。
(2.2) 来自有限 $d$ 截断乘 $L$ 的算子范数极限，
不来自“无界算子乘拟幂零算子”的形式推断。

令 $D_0=X_{e_0}\in\mathcal A$、$E_1=X_{e_1}\in\mathcal A$，
并置
$$
R=\gamma I+B_d+E_1L\in\mathcal B,\qquad \phi(R)=\gamma.
\tag{2.3}
$$
在 $\operatorname{Dom}X\cap\operatorname{Dom}Y$ 上，
原始未倾斜 first 满足
$$
X_u=X+D_0+u_*I,\qquad
X_v=Y+RX+v_*I.
\tag{2.4}
$$

第二个式子的域需要说明：
有限柱上它是实际 first 的逐项恒等式；
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §6 的式 (6.5) 给全部共同词域的有限柱图核心；这里取 $p=1$，故有限柱是 $X,Y$ 的共同一阶图核心。
在这个共同图范数下逼近任意输入，
$X_d=B_dX$ 的相对域结论同时控制加权行；
原 $X_v$ 闭性给 (2.4)。
其后由各有界系数的完整域交换作有限词归纳。
没有宣称 $\operatorname{Dom}X_v$ 等于这个交域。

## 3. 保留原完整 Bell 后的平衡次数

令 $\xi=e^w$，使用原始两行 (1.3) 与原 $w$ 的完整混合 Bell 变换；
所有混合 cumulant 均原样保留。
其真实倾斜 first 可以在共同自然域上写成
$$
U=X+H,\qquad V=Y+RX+K,
\qquad H,K\in\mathcal A.
\tag{3.1}
$$
$H,K$ 包括原常数、主行 $\ell^1$ 项和各自实际指数倾斜；
辅助 $\ell^1$ 项已经完整保留在 (2.3) 中。

置参考剪切坐标 $z=y-x^2$。
原剪切坐标在 (3.1) 下准确变成
$$
x\mapsto x+H,\qquad
z\mapsto z+(R-2H)x+K-H^2.
\tag{3.2}
$$
这是 $\mathcal B$ 系数的真正仿射替换。

写 $D=mr$。
对原标量符号
$[G(x,y-x^2)-\lambda]^r$，
完整 Bell 各混合导数使用
$$
\partial_x|_y=\partial_x|_z-2x\partial_z,\qquad
\partial_y=\partial_z.
$$
所以原 Bell 在 $(x,z)$ 总次数至多 $D$，
最高 $z^D$ 系数准确为 $I$；
任何正阶微分的 $z$ 次数至多 $D-1$。
(3.2) 不改变这两条性质。

因此原指定向量的实际多项式可以在参考 $X,Y$ 上写为
$$
P(X,Y)=(Y-X^2)^D+
\sum_{\substack{i+j\le D\\j<D}}
C_{ij}X^i(Y-X^2)^j,\qquad C_{ij}\in\mathcal B.
\tag{3.3}
$$
不是 $G$ 的 Bell 实现的自然 $r$ 次幂。

为识别原规范闭图，参考 $X,Y$ 与原 $X_u,X_v$ 一起纳入 R186 的共同正则器。
(2.4) 和所有有限词等式先在足够深的共同域上验证。
此外 $\xi=e^w$ 位于原/参考全部有限混合域，
(3.3) 在它上的值就是原 (1.5) 的指定向量。
R186 §4 允许任意有界 $A'$ 系数，本稿的 $\mathcal B\subset A'$ 符合；§6 的式 (6.1) 给两个规范实现共同的图核心 $\mathbb C[A]\xi$；
它们在这个核心上同值，故闭图相等。
下面将这一共同规范实现记作 $\mathsf P$。
这样没有用自然交域上的形式等式代替最大闭包识别。

## 4. 同一个参考 Z 的真实相伴图

令
$$
T=(Y-X^2)_{\rm can},\qquad Z=TL.
$$
$Z$ 是闭算子，所有 $A'$ 保其域并作域交换。
在充分深的共同自然域上，(3.3) 给
$$
L^DP=Q(Z),\qquad
Q(z)=z^D+\sum_{j<D}A_jz^j,
$$
$$
A_j=\sum_{i\le D-j}C_{ij}L^{D-i-j}\in\mathcal B.
\tag{4.1}
$$
最高系数是真正的 $I$。

若 $M=\ker\mathsf P\ne0$，
采用已推
[相伴图附录](R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)
§§4—5 的完整闭包论证。
令 $\mathcal D_k$ 为参考 $X,Y$ 的全部长度至多 $k$ 的自然词共同域，
$k_0=4D+4$ 足够。
所有 $C_{ij},A_j,L$ 都属于 $A'$，保持这些域。
$Z$ 至多消耗两层，所以在足深核内可验证 $PZ^jf=0$。
共同正则幂说明
$$
\mathcal M=
\overline{\{(f,Zf,\ldots,Z^{D-1}f):f\in M\cap\mathcal D_k\}}
\subset H^D
\tag{4.2}
$$
对 $k\ge k_0$ 不依赖 $k$，非零，并保持所有对角 $A'$。

令 $\mathcal C$ 为 (4.1) 的有界相伴矩阵。
它把足深图移成 $(Zf,\ldots,Z^Df)$；
从深度 $k+2$ 出发保证移位图仍在 $\mathcal V_k$。
因此 $\mathcal C\mathcal M\subseteq\mathcal M$。
对角 $\mathbf Z$ 闭，遂给整个闭图上的真实有界限制
$$
\boxed{
\mathcal M\subseteq\operatorname{Dom}\mathbf Z,\qquad
\mathbf Z|_{\mathcal M}=J:=\mathcal C|_{\mathcal M}\in B(\mathcal M).
}
\tag{4.3}
$$
此处没有使用 $Z$ 自然高幂的闭性。

## 5. 相伴系数放大到 B 后仍只有有限谱

这是使用谐和条带支路前需要另付的一项。
置
$$
h(z)=\phi(Q(z))\in\mathbb C[z],
$$
它是 $D$ 次首一多项式。

如果 $h(\zeta)\ne0$，则 $Q(\zeta)$ 是 $\mathcal B$ 的实际单位。
有限相伴矩阵的伴随矩阵恒等式给
$(\mathcal C-\zeta I)^{-1}$，
而这个逆可写成 $\mathcal C$ 的有限次多项式，
其系数为对角的 $\mathcal B$ 元素（包含 $Q(\zeta)^{-1}$）。
这些系数以及 $\mathcal C$ 都保持 $\mathcal M$，
所以该逆真正保持 $\mathcal M$，并是 $J-\zeta I$ 的双边逆。
故
$$
\boxed{\sigma(J)\subseteq h^{-1}(0).}
\tag{5.1}
$$
没有把完整矩阵交换子代数不变性赠送给 $\mathcal M$。
唯一使用的是对角 $A'$ 不变性和相伴矩阵本身的不变性。

## 6. 两条已有排核预算的输入逐项保持

令
$$
\Theta_a(t)=\sum_j\lfloor ta_j\rfloor,\qquad
\Lambda_a=\limsup_{t\to\infty}\frac{\Theta_a(t)}{t\log t}.
$$

### 6.1 有限计数比的柱支路

若 $\Lambda_a<\infty$，
已推排序二分给主行幅度重排 $r_n$ 满足
$$
\liminf_n
\frac{n\sum_{k>n}r_k^2}{(\sum_{k\le n}r_k)^2}=0.
\tag{6.1}
$$
对参考辅助 $b$ 有 $|b_j|\le C_0a_j$。
因而
[归一化全柱稿](R150-appendix-normalized-column-root-bounds-complex-controlled-auxiliaries-and-shear-powers.md)
§6 的有界放大限制排除引理适用于原参考
$Z=(Y-X^2)_{\rm can}L$ 和 (4.3)。

该引理的假设只是：
同一非零闭 $\mathcal M$ 保持对角 $A'$，
包含于 $\mathbf Z$ 的真实域，
并且 $\mathbf Z|_{\mathcal M}$ 有界。
它不要求产生该闭图的系数仍在 $\mathcal A$，
也不要求这些系数为标量或 $J$ 有限谱。
所需全柱测试仅使用参考正行 $a$ 与实受控行 $b$。
因此 (4.3) 被直接排除。

### 6.2 无限计数比的真实正 first 支路

若 $\Lambda_a=\infty$，可使用已推
[谐和/好时间条带稿](R150-appendix-harmonic-positive-anchor-sharp-strip-budget-and-all-shear-powers.md)
中有限谱相伴图的排除证明。
为明确它仍适用，列出完整算子输入。

对角 $A'$ 不变性使 $\mathbf X$ 在 $\mathcal M$ 的实际部分为空谱最大增生算子；
全部原预解和半群限制到同一空间，范数预算不增加。
(4.3) 在共同深域给
$$
\mathbf Yf=\mathbf X^2f+J\mathbf Xf.
\tag{6.2}
$$
$J$ 与 $\mathbf X$ 的全部预解交换。
$L_{\mathcal M}$ 拟幂零，故
$I+JL_{\mathcal M}$ 为实际单位；
因此右侧在 $\operatorname{Dom}\mathbf X_{\mathcal M}^2$ 上闭。
R186 共同正则器在 (6.2) 两边作双向图逼近，得到准确域
$$
\operatorname{Dom}\mathbf Y_{\mathcal M}
=\operatorname{Dom}\mathbf X_{\mathcal M}^2.
\tag{6.3}
$$

对每个实 $c>C_0$，原行 $ca\pm b$ 非负且不可和。
对应正 first 的实际部分最大增生。
将这两条 first 也纳入共同正则器，
在共同深域上使用 (6.2)，再按相同的两向闭图论证，
得到它们的准确实现
$$
\pm\mathbf X_{\mathcal M}^2+(cI\pm J)\mathbf X_{\mathcal M},
\qquad
\operatorname{Dom}=\operatorname{Dom}\mathbf X_{\mathcal M}^2.
\tag{6.4}
$$
二次式闭性分别由实际单位
$I+(cI+J)L_{\mathcal M}$、
$I+(J-cI)L_{\mathcal M}$ 支付。

§5 给 $J$ 有限谱。
在一个非零 Riesz 分支上写 $J=\omega I+N$，$N$ 拟幂零。
其 Riesz 投影是已识别的限制预解演算，保持全部正 first 域及正则器。
与旧条带证明相同，等价 Hilbert 范数
$$
\|f\|_\epsilon^2=\sum_{k\ge0}\epsilon^{-2k}\|N^kf\|^2
$$
使 $\|N\|_\epsilon\le\epsilon$，
且不增加任何与 $N$ 交换的原收缩半群/预解预算。

因为 $\Lambda_a=\infty$，
可以选任意充分大的有限 $k$，使好时间半群预算满足旧稿的条带阈值
$C_0<2\pi k$。
(6.3)—(6.4) 正好给其两二次因式；
有限谱分支、原空谱预解及好时间远边界矩形全部保留。
旧稿的窄半条带最大模与 Liouville 矛盾遂排除这个非零分支，
从而排除 $\mathcal M$。
这里实际正性全部来自 $a$、$ca\pm b$；
没有把复原辅助行的系数误认成非负。

## 7. 回到原指定向量

两个支路穷尽 $\Lambda_a\in[0,\infty]$，
所以 (4.3) 的非零闭图不可能存在。
因此 $\ker\mathsf P=0$。
原 $H$ 上 R186 的完整 $C$ 自伴给其像稠密；
§3 已核准原指定 $\xi=e^w$ 的共同图核心，故
$$
[[G(u,v-u^2)-\lambda]^re^w]_A
=\overline{\operatorname{Ran}\mathsf P}=H.
$$
证明 (1.5)。

## 8. 一个不属于两个旧单独范围的复同阶例

令
$$
a_j=(j+1)^{-3/5},\qquad
b_j=(-1)^ja_j,\qquad
d_j=i(j+1)^{-9/10},\qquad
u=\sum a_j\chi_j,\quad v=\sum(b_j+d_j)\chi_j.
\tag{8.1}
$$
则 $b$ 为实受控不可和骨架，$d$ 为不可和复行，并有
$$
\sum_j|d_j|^2/a_j=\sum_j(j+1)^{-6/5}<\infty.
$$
$v$ 的行不是实行加 $\ell^1$ 误差；
其比值 $v_j/a_j=(-1)^j+i(j+1)^{-3/10}$
也不落在某条固定仿射复直线上。
正、负两个骨架子列都具有无穷 $a$ 质量，
故不存在一个复 $\gamma$ 把整个辅助剩余变为加权行加 $\ell^1$。
于是不能只引用全实骨架稿或整个辅助都相对有界的加权稿。

本稿仍给
$$
[(v-u^2)^2-\beta u^2-\lambda]^re^w
$$
对所有 $\beta,\lambda\in\mathbb C$、$r\ge1$ 及复 first $w$ 循环。
全部其它 (1.4) 也同样成立。

固定非实仿射线方向的旧范围应引用
[R150 跨最高根簇附录](R150-appendix-disjoint-leading-roots-cross-kernel-exclusion-and-real-structure.md)
§2；这里不把它重做为新条带定理。
一般无加权小量的复受控辅助、加权主行扰动加实独立骨架、
更高退化剪切及完整 ISP 仍保持开放。
