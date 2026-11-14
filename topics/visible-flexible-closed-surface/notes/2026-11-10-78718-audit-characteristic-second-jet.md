# 特征接口二阶障碍、共同四矩修正与真实参考条带：全文独审

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
审者未参与本稿的二阶展开、矩条件推导、度量修正或参考条带构造，
也未参与主 M14 数值候选的种子选择、优化或调参。

## 0. 对象、结论与范围

全文对象为
[characteristic-second-jet-v1](2026-11-10-78718-geometry-characteristic-second-jet-v1.md)，
10203 B，SHA256
91901f5ff48055831e216ed5b837ccee2526161b43f33b8489d641b2bc134b8f。

**第 1—6 节全文独审通过，无数学订正。**
以下重新推导每一阶 Gauss–Codazzi、周期分部积分、对全部参数的共同
四矩条件，并补出无参数奇点的显式积分因子与真实测地法坐标构造。

输入曲线和全周期标架已由本审者完成另一份独立全文审查及严格区间重跑：
[有符号种子独审](2026-11-10-78718-audit-signed-torsion-seed.md)，
19390 B，SHA256
f1dfa8d5810172747c5990e2ed1d973a5151792f60447681735ee84592a48751。
故本稿的条件输入已有实际实例，但本稿的每个新推导仍在此独立核查。

三项成立结论应严格区分：

1. 对原直纹度量，明示 \(C^2\) 第二形式类别中的延伸必须有 \(L_0=0\)。
2. 一个固定解析函数 Delta、进而一个固定共同度量，可以同时支付全部
   小参数边界函数的所述有限阶兼容条件。
3. 该度量确实来自一张实际解析参考嵌入条带，其参数是 lambda=0。
   非零 lambda 的二维等距浸入或共同度量族没有在此构造。

第一项不适用于未经证明具有该较高正则性的全部 \(C^2\) 浸入。
第 3 项也不支付帽、固定握持区、全闭面 reach 或有效幅度。

本稿为解析审查，没有新增 ODE/PDE 求解、优化、网格或数值候选运行。
既有种子证书没有不必要地重跑。本审没有把任何静态核查称为实际数值执行。

## 1. 假设与完整二次径向展开

输入为解析闭嵌入曲线及周期正交标架，采用
\[
 \gamma'=T,\qquad d'=\alpha T-N,\qquad
 T'=-\alpha d,\qquad N'=d,
\]
其中 \(\int_0^\ell\alpha=0\)，\(\alpha\not\equiv0\)。
共同测地法度量为
\[
 g=dr^2+a^2du^2,\quad Q=aa_{rr},
\]
且边界数据为
\(a=1,a_r=\alpha,Q=1,Q_r=-2\alpha\)。
固定位置和横向标架使 \(M=-1,C=0\)。
这里 \(L,M,C\) 是第二形式在 \(r,u\) 坐标中的分量；
本轮二次经典微分使用 \(C^2\) 第二形式。\(C^4\) 浸入是充分条件，
不是主问题新增的完成要求。

令 \(l=L|_0\)、\(h=L_r|_0\)。
由 \(Q=1,a=1\) 得 \(a_{rr}=1\)；
\(a(0,u)\equiv1\) 给 \(a_u=0\) 与 \(a_{ru}=\alpha'\)。
因此对
\(\mu=a_r/a,\nu=a_u/a,B=aa_r\)，逐项有
\[
 \mu=\alpha,\quad
 \mu_r=\frac{a_{rr}a-a_r^2}{a^2}=1-\alpha^2,\quad
 \nu=0,\quad \nu_r=\alpha',
\]
\[
 B=\alpha,\qquad B_r=a_r^2+aa_{rr}=\alpha^2+1.
\]
全部式子都是边界限制，没有把一般 r 处的等式误用于边界。

由已核对符号的完整 Gauss–Codazzi
\[
 LC-M^2=-Q,\quad M_r=L_u-\mu M,\quad
 C_r=M_u+\mu C+BL-\nu M
\]
得到
\[
 M_r=l'+\alpha,\qquad C_r=\alpha l.
\]
再微分一次：
\[
 M_{rr}=h'-\mu_rM-\mu M_r
       =h'+1-2\alpha^2-\alpha l'.
\]
而
\[
 C_{rr}=(M_r)_u+\mu_rC+\mu C_r+B_rL+BL_r-\nu_rM-\nu M_r.
\]
其中 \((M_r)_u=l''+\alpha'\)，\(-\nu_rM=+\alpha'\)，其余非零项为
\(\alpha^2l+(\alpha^2+1)l+\alpha h\)，所以
\[
 C_{rr}=l''+2\alpha'+(2\alpha^2+1)l+\alpha h.
\]
特别地，两份 \(\alpha'\) 都在，没有遗失非径向项。

Gauss 一次微分在 \(C=0,M=-1\) 处给
\[
 lC_r-2MM_r=\alpha l^2+2l'+2\alpha=-Q_r=2\alpha,
\]
即
\[
 2l'+\alpha l^2=0. \tag{A}
\]

Gauss 二次微分为
\[
 2hC_r+lC_{rr}-2(M_r^2+MM_{rr})=-Q_{rr}.
\]
这里 \(L_{rr}C\) 因 \(C=0\) 消失；没有假设 \(L_{rr}=0\)。
代入后左边完整展开为
\[
 2h'+3\alpha lh+ll''-2(l')^2-6\alpha l'
 +2\alpha'l+(2\alpha^2+1)l^2-6\alpha^2+2.
\]
由 (A)，
\[
 l'=-\frac{\alpha l^2}{2},\qquad
 l''=-\frac{\alpha'l^2}{2}+\frac{\alpha^2l^3}{2}.
\]
于是 \(ll''-2(l')^2=-\alpha'l^3/2\)，
\(-6\alpha l'=3\alpha^2l^2\)。
写 \(Q_{rr}=6\alpha^2-2+\Delta\)，消掉相同常数项，最终确为
\[
 \boxed{
 2h'+3\alpha lh+\alpha'l\left(2-\frac{l^2}{2}\right)
 +(5\alpha^2+1)l^2=-\Delta.
 }\tag{B}
\]
每一项的符号和系数均与原稿一致。

## 2. 非零 l 的完整周期条件与原度量障碍

对原直纹度量
\[
 a_0^2=(1+r\alpha)^2+r^2,\qquad Q_0=1/a_0^2,
\]
直接微分倒数得
\[
 (Q_0)_{rr}|_0=2(2\alpha)^2-2(\alpha^2+1)
             =6\alpha^2-2.
\]
因此原度量正是 \(\Delta=0\)。

方程 (A) 的系数光滑，右端对 l 局部 Lipschitz。
任一周期解若在某点为零，则全圈为零；
所以非零周期解在整圈不为零且保持同号。

在此非零类别中，将 (B) 除以 \(2l^3\)，利用
\[
 \left(\frac h{l^3}\right)'
 =\frac{h'+(3/2)\alpha lh}{l^3}
\]
得到
\[
 \left(\frac h{l^3}\right)'
 =-\frac{\Delta}{2l^3}-\frac{\alpha'}{l^2}
   +\frac{\alpha'}4-\frac{5\alpha^2+1}{2l}. \tag{C}
\]
这也直接核对积分因子是 \(l^{-3}\)，不是 \(l^3\) 或其它幂。

周期性给 \(\int\alpha'=0\)。
另一个不可略去的周期分部积分是
\[
 \left(\frac\alpha{l^2}\right)'
 =\frac{\alpha'}{l^2}-\frac{2\alpha l'}{l^3}
 =\frac{\alpha'}{l^2}+\frac{\alpha^2}{l},
\]
故 \(\int\alpha'/l^2=-\int\alpha^2/l\)。
对 (C) 积分，得到周期 h 的必要条件
\[
 \boxed{\int_0^\ell
     \left(\frac{\Delta}{l^3}+\frac{3\alpha^2+1}{l}\right)du=0.}
 \tag{D}
\]

它也是充分条件：若上述积分为零，则 (C) 右端零平均；
对其从 0 到 u 积分、加任意常数，给一个周期的 \(h/l^3\)。
乘以非零周期函数 \(l^3\)，即得周期 h，且直接满足 (B)。
系数平滑或解析时，h 具有相应正则性，全部周期 jets 一致。

当 \(\Delta=0\) 时，
\((3\alpha^2+1)/l\) 严格保持 l 的符号，在整个非空圈上积分不可能为零。
因此原度量不允许非零 l 的这种延伸。结论不声称 l=0 时整块曲面唯一，
也不排除更高阶或全部阶平端变化。

## 3. 同一个 Delta 对全部参数的恰好四个矩

定义
\[
 A(u)=\frac12\int_0^u\alpha(s)\,ds,\qquad
 b(u)=3\alpha(u)^2+1.
\]
零平均给 A 的周期性；解析性随积分保持。
因 \(A'=\alpha/2\not\equiv0\)，A 非恒常。

首阶小参数族
\[
 l_\lambda=\frac{\lambda}{1+\lambda A}
\]
直接满足 (A)。A 在紧圈有界，可一次选定正 \(\lambda_*\)，使
所有 \(|\lambda|\le\lambda_*\) 的分母均大于 1/2。
对非零参数，令 \(z=1/\lambda\)，则 \(1/l_\lambda=z+A\)。
所以同一个 Delta 对全部这些参数满足 (D)，等价于多项式
\[
 P(z)=\int\{\Delta(z+A)^3+b(z+A)\}\,du
\]
恒为零。非零小参数对应的 z 含开区间，故“对全部参数为零”
确实强制多项式的每个系数为零，不能只用有限几个参数代替。

逐项展开得到：

| z 次数 | 系数 |
| --- | --- |
| 3 | \(\int\Delta\) |
| 2 | \(3\int A\Delta\) |
| 1 | \(3\int A^2\Delta+\int b\) |
| 0 | \(\int A^3\Delta+\int Ab\) |

这正是原文四个矩条件。它们是整个参数族的充要条件，
不是为每个参数分别挑一个度量修正。

设
\[
 G_{ij}=\int A^{i+j},\qquad 0\le i,j\le3.
\]
对任意实向量 c，
\[
 c^TGc=\int\left(\sum_{j=0}^3c_jA^j\right)^2\ge0.
\]
若为零，连续非负被积函数处处为零。
A 的像是含非退化区间的连通紧集，因此对应多项式在一个区间恒零，
所有系数只能为零。这证明 G 严格正定，尤其可逆。

于是
\[
 q=\left(0,0,-\frac13\int b,-\int Ab\right)^T,\qquad
 c=G^{-1}q,\qquad \Delta=\sum_{j=0}^3c_jA^j
\]
是一个实际定义的、解析周期的、与 lambda 无关的函数，并精确支付
四个矩。其系数由真实积分定义，无需数值近似矩或浮点可逆性假设。
Delta 不被要求非负；这不妨碍下面真实局部度量的正定性。

## 4. 参数零点无奇性的 h 族及所支付的 jet 范围

对每个参数令 \(h_\lambda(0)=0\)。
原文用光滑 ODE 说明依赖性已经充分；这里补一个显式、无
\(1/\lambda\) 奇点的积分因子，避免误用非零参数公式到零参数。

写
\[
 D_\lambda=1+\lambda A,\qquad l_\lambda=\lambda/D_\lambda.
\]
(B) 除以 2 后的 h 系数为 \((3/2)\alpha l_\lambda\)。
由于 \(D_\lambda'/D_\lambda=\lambda\alpha/(2D_\lambda)\)，
该线性 ODE 的积分因子可取
\[
 E_\lambda=D_\lambda^3,
\]
它在包含 lambda=0 的整个参数区间上解析且不为零。

定义
\[
 R_\lambda=-\frac{\Delta}{2}-\alpha'l_\lambda
       +\frac{\alpha'l_\lambda^3}{4}
       -\frac{(5\alpha^2+1)l_\lambda^2}{2}.
\]
则完整解为
\[
 h_\lambda(u)=D_\lambda(u)^{-3}
       \int_0^uD_\lambda(s)^3R_\lambda(s)\,ds. \tag{E}
\]
而积分内函数恰为
\[
 -\frac{\Delta}{2}D_\lambda^3
 -\alpha'\lambda D_\lambda^2
 +\frac{\alpha'\lambda^3}{4}
 -\frac{5\alpha^2+1}{2}\lambda^2D_\lambda.
\]
它实际上关于 lambda 是三次多项式，系数均为解析周期函数。
因此 (E) 的联合解析依赖没有任何参数零点障碍。

对非零参数，四矩已经由 (D) 支付 \(h_\lambda(\ell)=h_\lambda(0)=0\)。
对零参数，(E) 直接成为
\[
 h_0=-\frac12\int_0^u\Delta(s)\,ds,
\]
由第一个矩条件而周期。
周期系数和端值相等通过原线性方程逐次微分给全部 u jets 匹配；
所以 h 不是仅端值相等的分段函数。

这里能组装的确切数据是
\[
 L|_0=l_\lambda,\quad L_r|_0=h_\lambda,\quad M|_0=-1,\quad C|_0=0,
\]
以及第 1 节给出的 \(M_r,C_r,M_{rr},C_{rr}\)。
它们支付 Gauss 在 r=0 的 0、1、2 次径向导数，以及两条 Codazzi
在 r=0 的值和一次径向导数。二次 Gauss 中的 \(L_{rr}\) 因乘以 C 而
不出现；本稿没有用这些数据决定所有更高法向系数。
因此这确实是有限阶兼容结论，不是完整二维 Gauss–Codazzi 解。

## 5. 真实参考嵌入与精确诱导度量

取上节的实际解析周期函数
\(h_0=-\frac12\int_0^u\Delta\)，并定义
\[
 \overline F(s,u)=\gamma(u)+sd(u)+\frac{s^3}{6}h_0(u)N(u).
\]
它是一个实际解析映射，且在 s=0 有
\(\overline F_s=d,\overline F_u=T\)，两者正交单位。
因此每个边界点附近，某个固定平面投影的二维微分可逆；
解析逆函数定理给局部图和局部单射。紧致性先给统一正的浸入宽度。

为得到全局单射，反设任何缩小宽度都存在不同材料点同像。
可取两列
\((s_j,u_j)\ne(\widetilde s_j,\widetilde u_j)\)，
二者 s 坐标都趋于 0，且像相同。
材料圈紧，取子列使两个 u 分别趋于 u、v；极限满足
\(\gamma(u)=\gamma(v)\)。输入曲线嵌入，故 u=v 为同一材料圈点。
于是两列最终同在该点附近的一个局部图区域，违背局部单射。
所以存在一个统一的正宽，整个双侧条带嵌入。
此论证也覆盖跨周期接缝的参数，因为局部图取在材料圈坐标中。

为核对度量，不以原文给出的结果为假设。利用 \(N'=d\)，直接求导：
\[
 \overline F_s=d+\frac{s^2h_0}{2}N,
\]
\[
 \overline F_u=(1+s\alpha)T
 +\left(-s+\frac{s^3h_0'}6\right)N+\frac{s^3h_0}6d.
\]
对正交标架逐项点乘，得
\[
 \overline E=1+\frac{s^4h_0^2}{4},
\]
\[
 \overline F_{\rm met}
 =\frac{s^3h_0}{6}
  +\frac{s^2h_0}{2}\left(-s+\frac{s^3h_0'}6\right)
 =-\frac{s^3h_0}{3}+\frac{s^5h_0h_0'}{12},
\]
\[
 \overline G=(1+s\alpha)^2+s^2-\frac{s^4h_0'}3
       +\frac{s^6((h_0')^2+h_0^2)}{36}.
\]
特别地，两个混合三次项合并成负的 \(-s^3h_0/3\)，所有系数正确。

## 6. 测地法坐标的真实构造、周期与二阶数据保持

在实际解析正定诱导度量中，从每个 \((s,u)=(0,u_0)\) 出发，
取初速度 \(\partial_s\) 的单位测地线。
此处 \(\overline E=1,\overline F_{\rm met}=0\)，所以初速度既单位又正交
于初始边界曲线。解析测地 ODE 在紧初值圈上有统一正区间的解析解，
记坐标映射为
\[
 (r,u_0)\longmapsto(s(r,u_0),\eta(r,u_0)).
\]
其边界微分是单位矩阵。局部逆函数定理、紧致性及与第 5 节同样的
碰撞序列排除给统一的小双侧解析坐标条带。
系数在材料角变量周期，ODE 唯一性给
\(s(r,u_0+\ell)=s(r,u_0)\)、
\(\eta(r,u_0+\ell)=\eta(r,u_0)+\ell\)，
所以真实坐标下降到材料圈，没有新添一个未支付的角向 monodromy。

r 是单位速度测地参数，故新度量 \(g_{rr}=1\)。
再由无挠和测地方程，
\[
 \partial_r\langle\partial_r,\partial_u\rangle
 =\langle\partial_r,\nabla_u\partial_r\rangle
 =\tfrac12\partial_u|\partial_r|^2=0.
\]
初始混合项为零，故新度量 \(g_{ru}=0\)；其余正系数的正平方根解析，
得到实际 \(g=dr^2+a_*^2du^2\)，并非仅形式换元。

以下仔细核查换元后的 \(L_r\)，这是 Qrr 结论的关键。
在旧坐标边界，
\[
 \overline E_s=\overline E_u=(\overline F_{\rm met})_s=0.
\]
由 Christoffel 公式，两项 \(\overline\Gamma^s_{ss}\) 与
\(\overline\Gamma^\eta_{ss}\) 都为零，因此测地初值给
\[
 s_r=1,\quad\eta_r=0,\quad s_{rr}=\eta_{rr}=0.
\]
又
\(\overline F_{ss}=s h_0N\)，旧法向在 s=0 等于 N，
所以
\[
 \overline L|_0=0,\qquad \overline L_s|_0=h_0,\qquad
 \overline M|_0=-1,\quad\overline C|_0=0.
\]

第二形式作为二次型变换：
\[
 L_*=\overline Ls_r^2
       +2\overline M s_r\eta_r+\overline C\eta_r^2.
\]
在边界微分，所有带 \(\eta_r\)、\(\overline L\)、
\(\overline C\)、\(s_{rr}\) 的附加项消失；唯一可能的其它项
\(2\overline M\eta_{rr}\) 也因零测地加速度而消失。
故
\[
 L_*|_0=0,\quad (L_*)_r|_0=h_0,\quad
 M_*|_0=-1,\quad C_*|_0=0.
\]
坐标在边界保留 \(F_{*,r}=d,F_{*,u}=T\)，正定向法向仍为 N，
没有悄悄翻转第二形式符号。

还需保持 \(a_r=\alpha\)。边界初速度作为 u 的函数恒为 (1,0)，
所以 \(s_{ru}=\eta_{ru}=0\)；由链式求导得
\[
 \partial_rF_{*,u}|_0=d'.
\]
因此
\[
 a_*|_0=1,\qquad
 \tfrac12\partial_r|F_{*,u}|^2|_0=T\cdot d'=\alpha,
\]
即 \((a_*)_r|_0=\alpha\)。

## 7. 从实际嵌入计算 Qrr，而非假设它在换元下不变

Q 是新测地坐标下的 \(a_*a_{*,rr}\)；
不能无证地把旧 s 坐标下某个导数直接当成它。
原稿实际使用新的第二形式和真实 Gauss–Codazzi，方法正确。

由实际边界 \(L=C=0,M=-1\)，
\[
 Q_*=M_*^2-L_*C_*=1.
\]
Codazzi 给 \((M_*)_r=\alpha\)、\((C_*)_r=0\)，所以
\[
 (Q_*)_r=2M_* (M_*)_r-(L_*)_r C_*-L_* (C_*)_r=-2\alpha.
\]
此时再用第 1 节的 Mrr 公式，l=0、h=h0，得到
\[
 (M_*)_{rr}=h_0'+1-2\alpha^2.
\]
对 \(Q_*=M_*^2-L_*C_*\) 再微分。
全部 LC 项因 \(L=C=C_r=0\) 而消失，故
\[
 (Q_*)_{rr}=2\alpha^2-2(h_0'+1-2\alpha^2)
 =6\alpha^2-2-2h_0'
 =6\alpha^2-2+\Delta .
\]
这真实实现了所需的内在度量数据。

因此可以取这张实际参考嵌入的**整个诱导度量**作为一个固定共同度量。
所有 lambda 的有限兼容计算只使用其已支付的低阶数据，
无需为其它参数重新选择 Delta、宽度函数或高阶度量系数。
但这不意味着其它 lambda 已有二维浸入；
实际图仅在 lambda=0 构造，且其 \((l_0,h_0)\) 确与解析族数据一致。

## 8. 固定另一侧的 C² 接合与结论边界

若接口另一侧的参考图完全固定，而欲以共同位置、横向标架作 \(C^2\)
接合，第二基本形式必须连续。
参考侧在该边界的 \(L=\mathrm{II}(d,d)\) 为 0，
故另一侧也必须 \(l=0\)。
这只是 \(C^2\) 接合本身的必要连续性条件，不依靠前文二次 Gauss
微分的较高正则性。

非零小参数的 \(l_\lambda=\lambda/(1+\lambda A)\) 全圈不为零，
所以即使将来能构造其二维延伸，也不能直接与固定参考半片这样接合。
法向选择或把两侧的外向坐标反向都不能把非零二次型值变成零；
这里不存在靠重命名横向变量消去此障碍的空间。

正式可采用本稿的全部三个中间结论，并保留以下未解范围：
非零参数的二维周期解、完整函数或形式级数收敛、位置/标架闭合、
可接的两侧整体几何、帽、固定开握持区、有效幅度和完整闭面 reach，
均未由本文支付。它既非精确非平凡二维等距族，也非 README 的 G5。
