# R951 — 原全部重数的对角缺陷、固定基自交与奇偶子源的真单位秩

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列全有限重数不等式、同一原子核的固定基部分及单位秩界已证明。**
本篇继续 R950 的完整混合簇，在五至八重的四个真正例外上只补实际对角成本，
不改交叉权、不加原来源列。由此得到无需重数上界的统一缺陷式。
对同一个原奇来源或偶来源子核，全部重复因子可在一个一般成员中读成共同固定因子；
R238 的既有共同因子原则在这里用于新的原五块来源，而非重新登记那个原则。

原十九角曲面的完整剩余线性系还允许精确支付截面维数和奇偶差，
从而在自然短窗比 \(11/47\) 时给整个原矩阵至少
\[
 \left(\sqrt{\frac{56}{199}}-\frac{28}{199}-o(1)\right)\dim\mathcal W_D
\]
个单位 Smith 因子。此界来自一个完整的来源限制，不把两块秩相加。
它不判定 \(q=1\) 的全部混合核，也不从五个中央零制造深核或解决主目标。

## 1. 原矩阵与统一实际缺陷

沿 [R950](R950-original-mixed-contact-multiplicity-four-and-forced-fivefold-factor.md)
和 [R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)
的同一个十九角光滑面 \(X\)、原完整格
\[
 \mathcal W_D=H^0(X,\mathcal O_X(B_D)),
 \qquad p=6s-1>211,\quad N=s-13,\quad 1\le\ell<N.
\]
保全部固定坏素数、\(D<p\)、\(f_D=\lfloor9D/2\rfloor+4<p\)、
原 \(P_{134}\)、charge 四十、五十二跨界成本及全部来源帽。
记
\[
 \beta=B_D^2>0,\qquad
 M_D=5D+4-(D\bmod2).
\]
对非零原首核向量仍置
\[
 \widehat P=d^{C_D}\bar P,\quad
 r=\operatorname{ord}_t\widehat P,\quad
 1\le r\le M_D,\quad
 S=N-r,\quad L=(\ell-r)_+.
 \tag{1}
\]
当 \(r<N\) 时，同一个实际多项式在每个由其 charge 支持给出的
\(P_\zeta=(0,\zeta)\) 上有四个深 \(S\) 的普通 \(Y\) 导数及一个深 \(L\) 的第四导数。
只读原低轴至 \(s\)，所有接触取 \(\bar h=\min(h,s)\)。

记 R950 的准确混合函数为
\[
 \Phi(S,L)=
 \min\left\{13S,\ 10S+15L,\
 \max\left(\frac{61S}{5},\frac{15S+47L}{2}\right)\right\}.
 \tag{2}
\]
沿该篇附录 A 取
\[
 c_m=\min(m^2,31m),\qquad \lambda_m=\sqrt{c_m}.
\]
另定义四个**真实对角缺陷**
\[
 \delta_5=1,\quad \delta_6=3,\quad
 \delta_7=3,\quad \delta_8=1,\qquad
 \delta_m=0\quad(m\notin\{5,6,7,8\}),
 \qquad c'_m=c_m+\delta_m.
 \tag{3}
\]
平方根只在实 Néron–Severi 交数中用，不在剩余域中开根。

准确有
\[
 \lambda_m\le m,\qquad c'_m\le31m,\qquad
 \frac{\delta_m}{m^2}\le\frac1{12}.
 \tag{4}
\]
最后的最大值恰在 \(m=6\)；这不是一个假设的重数上界。
五至八的 \(c'_m\) 分别为 \(26,39,52,65\)，准确等于 \(13(m-3)\)。

## 2. 对全部重数成立的局部补偿

在每个物理点按真实不同根和原重数写
\[
 f(t,\zeta g+Z)=U(t,Z)\prod_\alpha
 (Z-\alpha_\alpha(t))^{m_\alpha},\qquad U(0,0)\ne0.
\]
保全部较远根、单位外因子、tame 分裂及原截断。
令 \(d_{\alpha\gamma}=v_t(\alpha_\alpha-\alpha_\gamma)\)，定义
\[
 \mathscr E'_\zeta=
 \sum_\alpha c'_{m_\alpha}\bar h_\alpha+
 6\sum_{\alpha<\gamma}
       \lambda_{m_\alpha}\lambda_{m_\gamma}d_{\alpha\gamma}.
 \tag{5}
\]
这里**只改对角项**；不同根的交叉权仍是原 \(\lambda_m\lambda_n\)。

**引理1。** 对全部实际重数，无任何 \(\max m\) 条件，
\[
 \boxed{\mathscr E'_\zeta\ge\Phi(S,L).}
 \tag{6}
\]

**证明。** R950 附录 A 已穷尽全部最近簇，并支付任意高重数的远尾。
除了截断下唯一最近根且其重数为 \(5,6,7,8\) 外，
原未补偿能量已经至少为 (2)，增加非负对角项不会破坏该界。

在唯一未付的四种情形，记该根截断接触为 \(w\)，
全部较远根的真实带重数接触和为 \(H\)。
同篇有限 \(t^s\) 泛位移使所有根差有限且不改变 (5)；
第三个长导数的准确首项给
\[
 S\le(m-3)w+H.
\]
因为 \(\lambda_m=m\ge5\)，任意远根的自项与它同该最近根的交叉项至少支付
\(13m_\alpha h_\alpha\)：未截权用
\(m_\alpha^2+6m m_\alpha\ge13m_\alpha\)，
\(m_\alpha>31\) 时自项 \(31m_\alpha\) 已足够。
再用 \(c'_m=13(m-3)\)，得到
\[
 \mathscr E'_\zeta\ge13(m-3)w+13H\ge13S\ge\Phi(S,L).
\]
所有其它根对均非负。此证明保原有限导数和外单位，
不把除去最近根后的乘子当成一个自由 jet 来源。证毕。

## 3. 同一原全局预算的精确缺陷式

把经过所读 \(q\) 个物理点的实际几何整非垂直因子写为 \(C_i^{m_i}\)，
\(b_i=\deg_YC_i\)。它们仍是同一个 \(\widehat P\) 的因子。
原 R680/R837 的完整 forcing 给
\[
 \sum_{\zeta}\left(\sum_{\alpha\in C_i}\bar h_\alpha+
       6\sum_{\alpha<\gamma,\ \alpha,\gamma\in C_i}
           d_{\alpha\gamma}\right)
 \le3C_i^2+L_{\rm pole}C_i,\qquad
 L_{\rm pole}C_i\le8b_i.
 \tag{7}
\]
所有奇支、切向根、无穷、十九角及原 ODE 截断都包含在此式。
每个 \(C_i\) nef，
\[
 B_D-\sum_i m_iC_i\ \text{有效},\qquad
 \sum_i m_i b_i\le D.
\]

将 (7) 乘 \(c'_{m_i}\)。
它准确支付 (5) 的自项，内部交叉额外多付
\(6\delta_{m_i}d_{\alpha\gamma}\ge0\)；
不同因子仍用真实交数乘
\(6\lambda_{m_i}\lambda_{m_j}\)。
置 \(\mathscr C_\lambda=\sum_i\lambda_{m_i}C_i\)，得到
\[
 \begin{aligned}
 q\Phi(S,L)
 &\le3\mathscr C_\lambda^2+
       3\sum_i\delta_{m_i}C_i^2+
       \sum_i c'_{m_i}L_{\rm pole}C_i\\
 &\le
 \boxed{3B_D^2+3\sum_i\delta_{m_i}C_i^2+248D}.
 \end{aligned}
 \tag{8}
\]
第二步只用 \(\lambda_m\le m\)、同一有效余除子、nef 比较及
\(c'_m\le31m\)。没有把增加的对角权当成原来源中的新幂。

令真正五至八重的活动除子为
\[
 A(P)=\sum_{\substack{i:\ 5\le m_i\le8}}m_iC_i.
 \tag{9}
\]
它 nef，且 \(B_D-A(P)\) 有效。由 (4) 和不同 nef 曲线的非负交数，
\[
 A(P)^2\ge\sum_{5\le m_i\le8}m_i^2C_i^2
 \ge12\sum_i\delta_{m_i}C_i^2.
\]
所以 (8) 给完全有限的必要式
\[
 \boxed{
 A(P)^2\ge
 4\{q\Phi(N-r,(\ell-r)_+)-3B_D^2-248D\}.
 }
 \tag{10}
\]
当右边为负时不主张额外正下界。所有任意高重数因子仍在 (8) 中支付；
没有使用 \(\max m=o(D)\)，也没有用局部纯幂模型替代原来源。

## 4. 整个奇或偶子核的共同固定部分

令 \(k=\overline{\mathbf F}_p\)，并把原矩阵及来源作同一几何基变。
定义实际子空间
\[
 \mathcal W_D^\varepsilon=
 \{P:P(t,-Y)=(-1)^\varepsilon P(t,Y)\},\qquad
 K_\varepsilon=\ker\bar M_5^{\rm orig}\cap\mathcal W_D^\varepsilon,
 \quad\varepsilon=0,1.
 \tag{11}
\]
不声称整个原核对 \(Y\mapsto-Y\) 稳定，
也不声称它等于这两个交核之直和。

假定 \(K_\varepsilon\ne0\) 且 \(N>M_D\)。
在它的一组基 \(\widehat P_i=d^{C_D}P_i\in k[t,Y]\) 中，
取全部非垂直共同因子的 primitive gcd 为 \(G\)。
垂直含量另保；在 \(k(t)[Y]\) 中余系统
\(Q_i=\widehat P_i/G\) 的 gcd 为一。
\(G\) 不依赖这组基。

这里使用 R238 已证的共同因子机制，具体需要如下事实：
可取一个 \(k\)-常数线性组合 \(Q=\sum a_iQ_i\)，
使其所有非垂直因子都简单，且与 \(G\) 的非垂直部分互素。
为免把纯超越常数上的 forcing 当成新输入，给出有限特化的支付：

若全部 \(Q_i\) 只依赖 \(t\)，此事实直接成立。
否则取一个关于 \(Y\) 非恒定的 \(Q_a\)。
因整个余系统 gcd 为一，可以在无限域 \(k\) 中避开有限多个真线性子空间，
选 \(Q_b\) 为常数线性组合，使 \(Q_a,Q_b\) 在 \(k(t)[Y]\) 互素。
约去后的比值 \(Q_a/Q_b\) 非恒定，且其有理映射次数小于 \(p\)；
故其 \(Y\) 导数不为零。
于是
\[
 Q_a+zQ_b
\]
对一般参数 \(z\) 关于 \(Y\) 可分。
这可直接由非零多项式
\(Q_a'Q_b-Q_aQ_b'\) 证明：
重复根使该多项式为零，并使 \(z=-Q_a/Q_b\)；
只有有限多个坏 \(z\)。同样，互素性使与 \(G\) 的 resultant 只在有限多个 \(z\) 处消失。
选一个避开这些坏值的 \(z\in k\)，便得到所需实际成员。
所选有限多个常数都落在某个有限剩余域扩张，原矩阵、低轴和完整 forcing 均保持。
此处没有在本地或程序中求任何数值样本。

故有一个原非零成员 \(P_*\in K_\varepsilon\)，其全部重复非垂直因子，
连同它们的准确重数，恰好来自固定 \(G\)。
对该成员使用 (9)，得到一个固定有效 nef 除子
\[
 A_\varepsilon=A(P_*),
 \qquad
 K_\varepsilon\subset
 s_{A_\varepsilon}H^0(X,\mathcal O_X(B_D-A_\varepsilon)).
 \tag{12}
\]
这是整个同一子核的固定部分，不是随各向量重新选因子。
并不声称右边所有截面都通过原五块矩阵。

因每个基向量都有同一奇偶性，\(Y\mapsto-Y\) 置换 \(G\) 的因子并保准确重数。
所读两个物理点的集合也被保持，
所以 \(A_\varepsilon\) 是该 involution 不变的实际除子。
(12) 依自然线束线性化落在一个确定的奇或偶特征子空间。

每个原成员的 charge 差均被二整除；
只有一个 charge 的情形由 \(N>M_D\) 排除。
因此在 (10) 中至少可取 \(q=2\)，不需要先假设其最大公因数恰为二。
由 (2) 的单调性，令
\[
 \boxed{\Delta_D=
 2\Phi\bigl(N-M_D,(\ell-M_D)_+\bigr)-3\beta-248D.}
 \tag{13}
\]
则当 \(\Delta_D>0\) 时，
\[
 \boxed{A_\varepsilon^2\ge4\Delta_D.}
 \tag{14}
\]
同时 \(A_\varepsilon^2\le\beta\)。
特别，若 \(4\Delta_D>\beta\)，两个子核各自都为零。
这一有限门不删去 \(r\)、固定前缀或线性误差。

## 5. 同一完整剩余线束与无边界移动成员

在原十九角光滑有理曲面 \(X\) 上，令
\[
 B=B_D,\qquad
 A\ge0,\qquad A\text{ nef},\qquad B-A\text{ 有有效代表}.
\]
在本篇应用中 \(A=A_\varepsilon\) 是第4节已实际证明的共同五至八重因子除子。
置 \(L=B-A\)。原 kernel 的相应子空间通过乘同一个 \(A\) 的定义截面，真正包含在 \(H^0(X,\mathcal O_X(L))\) 内；这里不以某个局部商或有限交的全环境空间替代它。

若 \(H^0(L)=0\)，所有界显然。否则在代数闭包上写完整线性系
\[
 |L|=Z+|M|,
\]
其中 \(Z\) 是全部固定除子，\(|M|\) 无固定素分量。
乘 \(Z\) 的定义截面给 \(H^0(L)\simeq H^0(M)\)。
不需要消去孤立基点，也不要求一般成员不可约。

令 \(\mathscr B\) 为固定的有限边界曲线集合：原两截面、十九条严格例外曲线，以及所有特殊严格纤维。
对每条 \(B_0\in\mathscr B\)，由于它不是 \(|M|\) 的固定分量，包含它的截面构成一个真线性子空间。
故可在代数闭包中同时避开这有限多个子空间，选一个有效成员 \(M_0\in|M|\)，使它**不含任何 \(\mathscr B\) 曲线作为素分量**。
没有声称 \(M_0\) 不与边界相交。

\(M_0\) 的每个几何整素分量，要么为非垂直、非两截面的曲线，要么为一般底纤维。
前者由 R680 引理2为 nef 且 \(-K_XC\ge2\deg_YC>0\)；后者同样 nef，且 \(-K_XF=2\)。
因此 \(M\) 是 nef 类。

## 6. 奇曲线、重数均保的完整上同调消失

按真实重数逐个加入 \(M_0\) 的素分量。设当前有效和为 \(D'\)，下一步加入整曲线 \(C\)，记 \(D=D'+C\)。
\(D'\) 是 nef 曲线的非负整数和，故
\[
 (D'-0)\cdot C=D'\cdot C\ge0,\qquad K_X\cdot C<0.
\]
因为 \(C\) 是光滑曲面上的整 Cartier 曲线，它是 Gorenstein，伴随与 Serre 对偶给
\[
 H^1(C,\mathcal O_C(D))^\vee
 =H^0(C,\omega_C\otimes\mathcal O_C(-D)).
\]
右侧线束的准确次数为
\[
 (K_X+C-D)\cdot C=K_X\cdot C-D'\cdot C<0,
\]
故它没有非零截面。因此 \(H^1(C,\mathcal O_C(D))=0\)。

使用完整正合列
\[
 0\longrightarrow\mathcal O_X(D')
 \longrightarrow\mathcal O_X(D)
 \longrightarrow\mathcal O_C(D)\longrightarrow0.
\]
从 \(H^1(X,\mathcal O_X)=H^2(X,\mathcal O_X)=0\) 出发，逐步归纳得
\[
 H^1(X,\mathcal O_X(M))=H^2(X,\mathcal O_X(M))=0.
\]
重复加入同一个 \(C\) 仍成立，因为 \(C^2\ge0\)；奇点、非约化总成员与所有正特征均未被删除。
所以准确有
\[
 \boxed{h^0(L)=h^0(M)
 =1+\frac{M^2-K_X\cdot M}{2}.}
 \tag{C1}
\]

## 7. 原 \(B_\infty\) 给显式统一线性误差

取 R680(9) 的固定有理 nef 类 \(B_\infty\)。
它可由 R680 的非边界式 (10) 与全部边界交数直接看出为 nef，也可由 \(B_D/D\to B_\infty\) 得到。

对任一第1节的非垂直非截面曲线，记 R680 的实际末 Gauss 值为
\(v_0,v_{h_1},v_{h_2},v_1,v_d,v_\infty\)、\(b=\deg_YC\)。
完整公式给
\[
 \begin{aligned}
 -K_XC&=2b-(v_0+v_{h_1}+v_{h_2}+v_1+v_d+v_\infty),\\
 4B_\infty C&=\frac{47}{3}b
 -(v_0+v_{h_1}+v_{h_2})-\frac43v_1-2(v_d+v_\infty).
 \end{aligned}
\]
两者之差是
\[
 \frac{41}{3}b-\frac13v_1-(v_d+v_\infty)\ge0,
\]
因为原 primitive 条件已经给 \(v_1\le0\)、\(v_d+v_\infty\le0\)。
对一般底纤维也有 \(2=-KF\le4B_\infty F=4\)。
逐素分量相加，得
\[
 0\le-K_XM\le4B_\infty M\le4B_\infty B.
 \tag{C2}
\]
最后一步用 \(B-M=A+Z\) 有效及 \(B_\infty\) nef。

原十九角准确类给
\(B_\infty B=(47/12)D+O(1)\)，常数只取决于那十九个固定取整余类。
因此无需 Fujita、Bertini 光滑性、一般限制满射或未付的 \(H^1\) 假设，
(C1)–(C2) 给完整原来源的有限界
\[
 \boxed{h^0(B-A)\le1+\frac12M^2+2B_\infty B.}
 \tag{C3}
\]

## 8. 固定基自交怎样真正减少移动面积

\(A,M\) 均 nef，且 \(B-A-M=Z\ge0\)。
因此
\[
 (A+M)^2\le B^2.
\]
Hodge 指数不等式对两个 nef 类给
\(A\cdot M\ge\sqrt{A^2M^2}\)；任一平方为零时亦直接成立。
所以
\[
 \boxed{M^2\le(\sqrt{B^2}-\sqrt{A^2})^2.}
 \tag{C4}
\]
\(0\le A^2\le B^2\) 也由同一个有效比较得到。
合并 (C3)–(C4)：
\[
 \boxed{
 h^0(B-A)\le
 1+\frac12(\sqrt{B^2}-\sqrt{A^2})^2+2B_\infty B.
 }
 \tag{C5}
\]
这是完整 \(H^0(B-A)\) 的上界；没有把可能不 nef 的 \(B-A\) 的自交直接代入 Riemann–Roch。

## 9. 原乘 \(Y\) 的准确 parity 比较

现在另假设 \(A\) 在原 involution
\(\tau:(t,Y)\mapsto(t,-Y)\) 下不变。它正适用于同 parity 核的完整共同因子除子。
\(L=B-A\) 具有原 \(\tau\)-linearization；\(p>211\) 保 \(\pm\) 分解。
若某个 primitive 方程的符号为负，乘回 \(A\) 只交换两种标签，不影响以下两边统一上界。

令
\[
 T_Y=\operatorname{div}_\infty(Y).
\]
在原 \(\mathbb F_4\) 框中，
\(\operatorname{div}(Y)=S_-+4F_\infty-S_+\)；
吹起后负部分准确为
\[
 T_Y=\pi^*S_+.
\]
原正角图为 \(t-\alpha=x^jz_j,\ Y=x^{-1}\)；
所以 \(T_Y\) 是正截面的严格变换，加三个四步链与一个三步链的全部十五条严格例外，系数都为一。
原 \(d=0\) 与底无穷远两步链在 \(Y\) 的零部，不增加极。
因此 \(T_Y\) 是固定的、几何约化的十六个 \(\mathbf P^1\) 分量。

由于 \(B,A\) 均 nef，对每个 \(C\subset T_Y\)，
\[
 \deg L|_C\le B\cdot C.
\]
一个 \(T_Y\) 截面在全部约化分量上的限制是单射，故
\[
 \begin{aligned}
 h^0(T_Y,\mathcal O_{T_Y}(L))
 &\le\sum_{C\subset T_Y}\max(0,L\cdot C+1)\\
 &\le B\cdot T_Y+16.
 \end{aligned}
\]
按原 R680 类 \(B=D S_0+(u_D+4D)F_0-\sum\mu E^*\)，其中
\(u_D=2\lfloor D/2\rfloor+4\)，准确有
\[
 B\cdot T_Y=u_D+4D.
\]
置
\[
 t_D=4D+u_D+16.
 \tag{C6}
\]

完整限制列的核是 \(H^0(L-T_Y)\)，所以自然包含
\(H^0(L-T_Y)^\pm\subset H^0(L)^\pm\) 的余维均不超过 \(t_D\)。
另一方面，乘原有理函数 \(Y\) 给真注入
\[
 H^0(L-T_Y)^\pm\hookrightarrow H^0(L)^\mp,
\]
因为 \(T_Y\) 恰为其完整极除子，且 \(\tau Y=-Y\)。
由两种符号分别比较，得到
\[
 \boxed{
 |h^0(L)^+-h^0(L)^-|\le t_D,\qquad
 h^0(L)^\pm\le\frac12h^0(L)+\frac12t_D.
 }
 \tag{C7}
\]
未假设该乘法满射，也未把全部原核说成 parity 直和。

## 10. 同一原矩阵中可直接使用的有限秩式

若原某个 parity 子核 \(\mathcal K_\varepsilon\) 的全部来源均含共同 \(A\)，则它真正注入 \(H^0(B-A)\) 的一个 parity 分量。
由 (C5)、(C7)，
\[
 \boxed{
 \dim\mathcal K_\varepsilon
 \le\frac14(\sqrt{B^2}-\sqrt{A^2})^2
      +B_\infty B+\frac{1+t_D}{2}.
 }
 \tag{C8}
\]
即
\[
 \dim\mathcal K_\varepsilon
 \le\frac14(\sqrt{B^2}-\sqrt{A^2})^2
      +B_\infty B+2D+\frac{u_D}{2}+\frac{17}{2}.
\]

对原全来源取 \(A=0\)，同一 (C7) 给
\(\dim\mathcal W_D^\varepsilon\ge(n_D-t_D)/2\)，
\(n_D=\dim\mathcal W_D\)。
因此这个**单一真实 parity 列块**的单位秩至少为
\[
 \boxed{
 \operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})
 \ge
 \max\!\left(
 0,\ \frac{n_D}{2}
 -\frac14(\sqrt{B^2}-\sqrt{A^2})^2
 -B_\infty B-t_D-\frac12
 \right).
 }
 \tag{C9}
\]
两块各自的单位秩不能相加；它们在整个目标中的像可能相交。

特别，若已经实际证明
\[
 \liminf A^2/B^2\ge c>0,\qquad
 n_D=\tfrac12B^2+O(D),
\]
则
\[
 \limsup\frac{\dim\mathcal K_\varepsilon}{n_D}
 \le\frac12(1-\sqrt c)^2,\qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})}{n_D}
 \ge\sqrt c-\frac c2.
\]
用已经支付的固定基下界 \(c=56/199\)，得到根式常数
\[
 \dim\mathcal K_\varepsilon/n_D
 \le\tfrac12(1-\sqrt{56/199})^2+o(1),\qquad
 \operatorname{rank}_{\rm unit}/n_D
 \ge\sqrt{56/199}-28/199-o(1).
\]
此处 \(A\) 的大自交必须由原实际核证明；单有一个抽象五重曲线不能代替此前提。


## 11. 全有限单位秩与最佳显示窗口

将第4节的 \(\Delta_D\) 代入第10节。
若 \(\Delta_D>0\) 且 \(4\Delta_D\le\beta\)，
(14) 与平方根差在 \(0\le A^2\le\beta\) 上的单调性给
\[
 \boxed{\dim K_\varepsilon\le
 \frac14(\sqrt\beta-2\sqrt{\Delta_D})^2+
 B_\infty B_D+\frac{1+t_D}{2}.}
 \tag{15}
\]
因此这个**同一原 parity 来源列块**满足
\[
 \boxed{
 \operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})
 \ge \max\left(0,\ 
 \frac{n_D}{2}
 -\frac14(\sqrt\beta-2\sqrt{\Delta_D})^2
 -B_\infty B_D-t_D-\frac12\right),
 }
 \tag{16}
\]
其中 \(n_D=\dim\mathcal W_D\)、\(t_D=4D+u_D+16\)。
如果该子核本来为零，其满列单位秩直接给更强结论；
如果 \(4\Delta_D>\beta\)，第4节已迫子核为零。
这些式子中的所有交数、取整及线性项都来自原十九角，
没有删去一个未控制的 \(H^1\) 或附加重数代价。

考虑真正满足
\[
 D\longrightarrow\infty,\qquad
 \frac{\ell}{N}\longrightarrow x,\qquad
 4N+\ell=n_D+o(D^2),\qquad
 n_D=\frac12\beta+O(D)
 \tag{17}
\]
的五块预算。因 \(r,M_D=O(D)\)，
\[
 \frac{\Delta_D}{\beta}\longrightarrow
 \gamma(x):=\frac{\Phi(1,x)}{4+x}-3.
 \tag{18}
\]
在 \(9/41<x<1/3\) 中 \(\gamma(x)>0\)。
对两个子核各自，若非零，则其共同固定除子满足
\[
 \liminf\frac{A_\varepsilon^2}{B_D^2}\ge4\gamma(x).
 \tag{19}
\]
这比仅断言存在一个五重因子严格更强：
它给同一个核空间的固定部分的正二次预算，
不允许把重复部分放进自交可忽略的尾项。

例如 \(x=1/4\) 时，\(\Phi(1,x)=13\)，
\[
 \gamma(1/4)=\frac1{17},\qquad
 \liminf A_\varepsilon^2/B_D^2\ge\frac4{17}.
\]
于是
\[
 \limsup\frac{\dim K_\varepsilon}{n_D}
 \le\frac12\left(1-\frac2{\sqrt{17}}\right)^2,\qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})}{n_D}
 \ge\frac2{\sqrt{17}}-\frac2{17}.
 \tag{20}
\]

在本篇准确四段函数内，\(\gamma(x)\) 的最大值在
\(x=11/47\) 取得：第三段的比值递增，第四段的比值递减；
前两段不超过这个值。
此时
\[
 \Phi(1,11/47)=13,\quad
 \gamma(11/47)=\frac{14}{199},\quad
 c:=4\gamma(11/47)=\frac{56}{199}.
 \tag{21}
\]
因此两个实际子核各自满足
\[
 \boxed{
 \limsup\frac{\dim K_\varepsilon}{n_D}
 \le\frac12\left(1-\sqrt{\frac{56}{199}}\right)^2,
 \qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})}{n_D}
 \ge\sqrt{\frac{56}{199}}-\frac{28}{199}.
 }
 \tag{22}
\]
原全矩阵的单位秩至少是任意一个真实列块的单位秩，
故它也有 (22) 的后一界。
没有相加两个可能有相交像的列块；
也没有把全部核的混合 \(q=1\) 向量作奇偶分解。

## 12. 保持的算术与下一实际门

这里的固定因子在剩余域内由同一个子核确定。
它不保证任意整提升继续被某个所选整 \(F^m\) 整除；
原 \(P+pR+p^2S+\cdots\) 的修正仍必须遍历其完整原来源。
对给定仿射强迫项的成员性，(16) 只给这个原矩阵的秩，
没有证明该强迫项位于或不位于像中。

同样，唯一最近根不等于整个曲线在物理点光滑。
R948 的指定 \(F\)、零角和相继限制门，R943 的全部 carry，
原有限 away 类及受限 \(S\) 均继续保留。
R947 扩大规范化格的真实返回和 jet 成本没有混入本篇旧十九角来源。

本篇新增的是 (8) 的无重数上界缺陷、(14) 的整个同 parity 核固定基预算，
以及通过完整剩余线性系和实际乘 \(Y\) 得到的 (15)–(22)。
它们不支付原中央同时零到所需深核的算术桥，
不替代无穷不同素数上通常全 Sha 有限的主目标。
没有新增数学程序执行、素数样本或可重算输出。
