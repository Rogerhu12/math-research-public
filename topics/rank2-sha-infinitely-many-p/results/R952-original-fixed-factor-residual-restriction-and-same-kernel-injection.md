# R952 — 原固定重因子的实际剩余限制、同核单射与奇偶单位秩

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列同一原矩阵的有限限制式、固定因子分类、完整子核单射及渐近单位秩界已证明。**
本文接 [R950](R950-original-mixed-contact-multiplicity-four-and-forced-fivefold-factor.md) 的全部混合簇和 [R951](R951-original-uniform-diagonal-defect-and-parity-fixed-volume.md) 的完整移动来源。新的输入是把唯一最近的真实重复根同实际商 \(R=\widehat P/F^m\) 在 \(C=(F)\) 上的限制相联；不是再增加一个抽象局部能量常数。

在原自然五块预算、短比 \(x=11/47\) 下，本文证明每个奇或偶子核各自满足
\[
 \limsup\frac{\dim K_\varepsilon}{n_D}
 \le\frac12\left(\frac{31/\sqrt{199}-2}{5}\right)^2
 <\frac1{1250}.
 \tag{A}
\]
所以同一个真实 parity 列块、因而原全矩阵的单位秩满足
\[
 \liminf\frac{\operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})}{n_D}
 \ge\frac12\left[1-\left(\frac{31/\sqrt{199}-2}{5}\right)^2\right]
 >\frac{312}{625}.
 \tag{B}
\]
此结论不相加两个可能有交像的列块，不断言整个原核为奇偶直和；也不把指定仿射 forcing 的成员性或更高整模页认作已付。

## 1. 原来源、有限最近根门及记号

保持 R950/R951 的全部原规范：
\[
 p=6s-1>211,\quad N=s-13,\quad 1\le\ell<N,\quad
 D<p,\quad f_D=\lfloor9D/2\rfloor+4<p.
\]
原 \(P_{134}\)、charge 四十、五十二跨界成本、十九角和全部来源帽不变。
在同一十九角曲面上置
\[
 B=B_D,\quad \beta=B^2>0,\quad
 \mathcal W_D=H^0(X,\mathcal O_X(B)),\quad
 n_D=\dim\mathcal W_D.
\]
\(\tau(t,Y)=(t,-Y)\)，
\[
 K_\varepsilon=\ker\bar M_5^{\rm orig}\cap
 \mathcal W_D^\varepsilon.
\]
这里通过原固定清分母 \(d^{C_D}\) 识别原相对来源与显示的截面空间；保原矩阵及其列识别。所有域扩张都是同一剩余域的几何基变，不更换矩阵。
以下固定一个非零 \(K_\varepsilon\)；若它为零，相应满列单位秩更强。

保原清分母 \(\widehat P=d^{C_D}\bar P\)，垂直阶
\(1\le r\le M_D=5D+4-(D\bmod2)\)。
使用 R950 的同一个函数
\[
 \Phi(S,L)=\min\left\{13S,\ 10S+15L,\
       \max\left(\frac{61S}{5},\frac{15S+47L}{2}\right)\right\}.
\]
本篇的有限最近根门为
\[
 N>M_D,\qquad
 \Delta_D:=2\Phi(N-M_D,(\ell-M_D)_+)-3\beta-248D>0.
 \tag{1}
\]
若在两个物理点 \((0,\pm1)\) 都没有 R950 附录 A 的唯一最近 \(5,6,7,8\) 重根，该篇未补偿能量就给 \(\Delta_D\le0\)。
因此 (1) 迫至少一个这样的根；parity 恒等式迫两个物理点有同一对应类型。
这里可直接取二点轨道，不必假设最大 charge 差公因数恰为二。
单一 charge 的情形已由 \(N>M_D\) 排除。

取 R951 §4 的一般实际成员：其所有重复非垂直分量和准确重数都来自整个 \(K_\varepsilon\) 的共同 gcd \(G\)，剩余非垂直因子全部简单。
而 (1) 迫唯一最近的五至八重根，所以它必在固定 \(G\) 内。
若固定 \(G\) 的最高截止接触有两根并列，则任何一般成员都不可能满足这个坏类型，矛盾；故该最高固定根本身唯一，所属分量及接触已经固定。
继续选择一般成员只排除有限个非零系数条件：截止于 \(s\) 的有限根接触型是有限 Taylor 数据的可构造条件，其有限并覆盖一般成员，故可固定一型的非空 Zariski 开集。
随后使用的 \(F,\psi,h,T,J\) 因此与该开集中的向量无关，§2 的线性消失条件才能延拓到全子核。
所有常数均可在某个有限剩余域扩张中取到。
所用的共同因子原则仍是 R238/R951 已证原则，不重登记为新输入。

记在 \((0,1)\) 真正承担这个唯一最近根的几何整曲线为 \(C\)，其准确重复次数为
\[
 m\in\{5,6,7,8\},\quad
 b=\deg_Y C,\quad \kappa=C^2,\quad d_C=B\cdot C.
\]
它非垂直、非两截面；R680 给 \(C\) nef。
整个子核均被 \(F^m\) 整除，其中 \(F\) 是 \(C\) 的 primitive 方程。
在 \((0,-1)\) 承担唯一最近根的分量准确是 \(\tau C\)，重复次数同为 \(m\)。
因而这里只存在两个可能：

1. \(C=\tau C\)，一个实际固定分量；
2. \(C\ne\tau C\)，一对实际固定分量。

其它重复分量仍在原成员内；没有删除它们、也没有将所有五至八重因子都称为这里的最近分量。

令 \(L_{\rm pole}\) 为 R680(14) 的完整 forcing 极除子，
\[
 \lambda_C=L_{\rm pole}\cdot C,\qquad 0\le\lambda_C\le8b.
 \tag{2}
\]
该除子和十九角模型均被 \(\tau\) 保持。

## 2. 唯一最近根给实际商的准确限制

先在 \((0,1)\) 证明。对截止以外的接触，依 R950 作辅助位移
\(g\mapsto g+u t^s\)，保持两个点的 \(\pm\) 对称。
因为 \(N,\ell<s\)，原有限 jet 条件逐条不变。
这只是有限截断证明，不是加入来源列、延长原 ODE 或改变原中央。
可选常数 \(u\) 避开有限个首系数，使全部截止接触有限。
唯一最近的截止根仍唯一；记它为 \(\psi\)，
\[
 h=v_t(\psi-g),\qquad 0<h\le s.
\]
以下 \(g\) 简记这个辅助形式；所有最终限制在真实 \(C\) 上。

整个局部 tame Galois 群保持该根的接触阶。
唯一性迫 \(\psi\in k((t))\)，且 \(\psi(0)=1\)，所以
\(\psi\in k[[t]]\)，对应正规化 \(\nu:\widetilde C\to C\) 上一个真实点 \(Q_+\)，并且 \(t\) 在 \(Q_+\) 是均匀化参数。
这不要求 \(C\) 在 \((0,1)\) 光滑：它可有其它较远分支。

令 \(C\) 在该物理点的其它真实根为 \(\psi_j\)，记
\[
 T=\sum_{j\ne +}v_t(\psi_j-g).
\]
全部这些接触严格小于 \(h\)。
故
\[
 v_t(\psi-\psi_j)=v_t(\psi_j-g),\qquad
 T=v_t(F_Y(t,\psi))\in\mathbf Z_{\ge0},
 \tag{3}
\]
局部 Weierstrass 外单位的阶为零。

对一般实际成员写
\[
 \widehat P=F^m R,\qquad F\nmid R.
 \tag{4}
\]
\(R\) 是同一个全局截面除去 \(mC\) 后的真实截面：
\[
 R\in H^0(X,\mathcal O_X(B-mC)).
\]
它保全部垂直含量 \(t^r\)、其它重复因子、截面和十九角余量。
特别没有把原 \(r\) 从下面的次数或零阶中删去。

最近根唯一，故 \(R\) 的全部局部根都比 \(\psi\) 更远。
逐根使用超度量不等式，并保外单位，得
\[
 v_t R(t,g)=v_tR(t,\psi)=
 \operatorname{ord}_{Q_+}(\nu^*(R|_C)).
 \tag{5}
\]
记此共同阶为 \(v\)。
对 \(j=0,1,2,3,4\)，唯一最低阶的普通 \(Y\) 导数项，是全部 \(j\) 次导数都落在最近的 \((Y-\psi)^m\) 上。
其系数为 \((m)_j=m(m-1)\cdots(m-j+1)\ne0\)，因为 \(m\le8<p\)。
任何一次导数落在远根上都少减一个严格较小的接触，落在正规外单位上也不能达到这个最低阶。
所以没有同阶相消，准确有
\[
 v_t(\partial_Y^j\widehat P(t,g))
 =(m-j)h+mT+v.
\]
在 Euler 算子 \(\mathcal E=Y\partial_Y\) 的展开中，最高普通导数项前的 \(Y^j\) 是单位；所有较低阶项都高出正的 \(h\) 倍。
因此同样准确有
\[
 \boxed{
 v_t(\mathcal E^j\widehat P(t,g))
 =(m-j)h+mT+v,\quad 0\le j\le4.}
 \tag{6}
\]
尤其第三长行的首系数就是非零的 \(m(m-1)(m-2)\) 乘实际单位。

原四长一短条件于是迫
\[
 v\ge J:=
 \max\{0,\ N-(m-3)h-mT,\ 
                \ell-(m-4)h-mT\}.
 \tag{7}
\]
\(h,T,J\) 都为整数；式 (7) 保第四短行。
在两个物理点的相应分量上完全同理。

式 (6) 只需在所选非空开集上的一般成员证明。
\(F,\psi,h,T,J\) 对这个开集固定，且
“\(R|_{\widetilde C}\) 在 \(Q_+\) 消到 \(J\)”是关于原子核向量的线性条件。
因此 (7) 对**整个同一个 \(K_\varepsilon\)** 成立，包含特殊成员和零向量。
没有将一般成员的精确因子重数错误地强加给每个特殊成员。

## 3. 同一曲线 forcing 支付全部远支

R680 的完整曲线 forcing 在该物理点至少支付
\[
 h+T+6T=h+7T.
\]
理由是每个远支与最近支的相交阶准确为 (3) 中的相应接触；其它远支间的判别式项非负。
所有奇点、tame 共轭和截止外分支仍在完整 forcing 中。
因此若 \(C=\tau C\)，两边对应的 \(h,T\) 相同，并有
\[
 \boxed{2(h+7T)\le3\kappa+\lambda_C.}
 \tag{8}
\]
若 \(C\ne\tau C\)，对各自承担最近根的一个物理点，分别有
\(h+7T\le3\kappa+\lambda_C\)；
它们在其它物理点的非负能量不删作负项。

由于 \(m\ge5\)，
\[
 m\le7(m-3),\qquad
 (m-3)h+mT\le(m-3)(h+7T).
 \tag{9}
\]
这就是同一个 \(F\) 的 forcing 与真实 \(R|_C\) 相接之处。

当 \(C=\tau C\) 时，\(R|_C\) 对一般成员非零，
其正规化拉回线束的次数准确为 \(d_C-m\kappa\)。
两个不同点的零阶之和不超过这个次数。
由 (6)、(8)、(9)：
\[
 \boxed{
 2N\le d_C+(2m-9)\kappa+(m-3)\lambda_C.}
 \tag{10}
\]
这里用的是原长窗 \(N\)，不是 \(N-r\)：全部 \(t^r\) 已在真实 \(R\) 和次数 \(d_C-m\kappa\) 中支付。

当 \(C\ne\tau C\)，对 \(C\) 的一个点同理给
\[
 N\le d_C+(2m-9)\kappa+(m-3)\lambda_C.
 \tag{11}
\]
对 \(\tau C\) 的式子一样。曲线间的其它相交、包括商 \(R\) 中的另一因子，仍被同一个剩余限制次数计入。

## 4. 真非不变因子对的有限排除

若 \(C\ne\tau C\)，实际共同除子
\[
 A=m(C+\tau C)
\]
nef 且 \(B-A\) 有效。
由 \(\tau\) 保交数、Hodge 和有效比较，
\[
 C\cdot\tau C\ge\kappa,\quad
 4m^2\kappa\le A^2\le\beta,\quad
 2m d_C=B\cdot A\le\beta.
 \tag{12}
\]
将 (11) 相加：
\[
 \begin{aligned}
 2N
 &\le2d_C+2(2m-9)\kappa+
                 2(m-3)\lambda_C\\
 &\le\frac{4m-9}{2m^2}\beta+
                 16(m-3)b\\
 &\le\boxed{\frac{11}{50}\beta+5D}.
 \end{aligned}
 \tag{13}
\]
末步用 \(m=5,6,7,8\)、该有理系数在这些整数中以 \(m=5\) 最大，以及真实径向次数 \(2mb\le D\)。
因而有限门
\[
 \boxed{2N>\frac{11}{50}\beta+5D}
 \tag{14}
\]
排除整对可能。

在 (1)、(14) 下，整个非零 \(K_\varepsilon\) 因而有一个实际共同、\(\tau\) 不变的 \(F^m\)，且其最近根在两物理点各自唯一。
选 primitive \(F\) 时，其非零 \(Y^0\) 系数使 \(\tau F=F\)；即 \(F\) 真为偶多项式。
没有将未知 \(F\) 认成 R948 指定的旧 \(F\)。

## 5. 固定单因子的全部有限预算与下一重数排除

令
\[
 \rho_D=\frac{2N}{\beta},\qquad A=mC,\qquad
 a=\frac{m^2\kappa}{\beta}.
\]
\(B-mC\) 有效及 \(B\) nef 给 \(d_C\le\beta/m\)。
从 (10) 得
\[
 \boxed{
 a\ge
 c_m(\rho_D)-
 \frac{m^2(m-3)\lambda_C}{(2m-9)\beta},
 \qquad
 c_m(\rho)=\frac{m^2\rho-m}{2m-9}.}
 \tag{15}
\]
全部有限误差保原 \(\lambda_C\)。
粗略统一地，因 \(mb\le D\)，误差不超过 \(80D/\beta\)。

若 \(3/13\le\rho\le41/173\)，四个 \(c_m\) 以 \(m=6\) 最小：
\[
 \boxed{c_m(\rho)\ge c_6(\rho)=12\rho-2.}
 \tag{16}
\]
直接相减即可：
\(c_5-c_6=13\rho-3\)，
\(c_7-c_6=(3-11\rho)/5\)，
\(c_8-c_6=(6-20\rho)/7\)。

\(m=8\) 还可更早排除。
(10)、\(d_C\le\beta/8\)、\(\kappa\le\beta/64\) 给
\[
 \boxed{m=8\ \Longrightarrow\
 2N\le\frac{15}{64}\beta+5D.}
 \tag{17}
\]
故反向严格门下只剩 \(5,6,7\)。

更重要的是一个实际全来源单射门：
\[
 \boxed{\kappa>\frac{\beta}{(m+1)^2}
 \ \Longrightarrow\ H^0(X,\mathcal O_X(B-(m+1)C))=0.}
 \tag{18}
\]
确实，若右侧有非零截面，有效性和 \(B\) nef 迫
\(d_C\le\beta/(m+1)\)；
而 Hodge 对 nef \(B,C\) 给
\(d_C\ge\sqrt{\beta\kappa}>\beta/(m+1)\)，矛盾。
没有把 \((B-mC)^2\) 当作未证明的 nef 自交。

自然预算中 (18) 由 (15) 自动严格成立。
在最小极限 \(\rho=3/13\)，四个 \(c_m\) 分别为
\[
 \frac{10}{13},\quad\frac{10}{13},\quad
 \frac{56}{65},\quad\frac{88}{91},
\]
逐个严格大于 \(m^2/(m+1)^2\)。
因此固定短比的正余量吸收 (15) 的 \(O(D)/\beta\)；
不需要统一错误地用四个阈值中的最大值去比较最小 \(c_m\)。

## 6. 整个同核到正规化两点线束的真单射

现在假设 (18)。
在 \(\tau\) 不变的 \(C\) 的正规化上，令 \(Q_-,Q_+\) 为第2节的两个真实点。
它们被 \(\tau\) 交换，且 \(t\) 在两点均为均匀化参数。
置
\[
 \mathscr Q=
 \nu^*\mathcal O_X(B-mC)|_C
 \otimes\mathcal O_{\widetilde C}(-JQ_+-JQ_-),
 \qquad
 e=\deg\mathscr Q=d_C-m\kappa-2J.
 \tag{19}
\]
这里是完整线束的正规化拉回，不假设 \(C\) 光滑，也不用算术 genus 替代正规化 genus。
第2节已经证明每个核向量除去同一个 \(F^m\) 后的真实限制落在 (19)。
该限制的核准确是仍被 \(F\) 整除的来源，故由 (18) 为零。
于是得到
\[
 \boxed{
 K_\varepsilon\hookrightarrow
 H^0(\widetilde C,\mathscr Q)^{\varepsilon}.
 }
 \tag{20}
\]
若线性化的原标签选择不同，只整体交换两个符号；以下两侧界相同。
(20) 是实际子空间的单射，不主张右边整个环境空间都由原核实现。

保原函数 \(Y\)。
令 \(\mathfrak t=(Y|_{\widetilde C})_\infty\)，\(t_C=\deg\mathfrak t\)。
R951 的原极除子 \(T_Y=\pi^*S_+\) 是 nef，故
\[
 t_C\le C\cdot T_Y\le
 \frac{B\cdot T_Y}{m}=
 \frac{4D+u_D}{m},\quad
 u_D=2\lfloor D/2\rfloor+4.
 \tag{21}
\]
\(Y\) 在 \(\widetilde C\) 上非零且 \(\tau Y=-Y\)；
\(\mathscr Q\) 具有原自然 \(\tau\)-linearization。
包含 \(H^0(\mathscr Q-\mathfrak t)^\pm\subset H^0(\mathscr Q)^\pm\)
的余维至多 \(t_C\)，乘 \(Y\) 又真注入相反符号。
所以
\[
 |h^0(\mathscr Q)^+-h^0(\mathscr Q)^-|\le t_C.
\]
任意光滑整曲线上的次数 \(e\ge0\) 线束都有 \(h^0\le e+1\)：
在 \(e+1\) 个不同点取值的核为零即证。
当 \(e<0\) 时无非零截面。
因此不假设 Clifford 区间或任何 genus 下界，(20) 给
\[
 \boxed{
 \dim K_\varepsilon\le\frac{e+1+t_C}{2}.}
 \tag{22}
\]
非零子核已经保证这里 \(e\ge0\)。

由 (7)–(9)，还有完整有限上界
\[
 \boxed{
 e\le d_C+(2m-9)\kappa-2N+(m-3)\lambda_C.}
 \tag{23}
\]
这是同一共同因子之后的实际有限 jet 限制，保第四短行于 (7)、两点、全部远支、垂直含量和原 forcing 极成本。

## 7. 同一个移动部联合限制；不加两个秩

在同一完整剩余线性系中写
\[
 |B-mC|=Z+|M|.
\]
R951 §§5–9 已完整证明 \(M\) nef、
\(h^0(B-mC)=1+(M^2-K_XM)/2\)，以及原 parity 差。
因而对 (20) 的同一个子核，
\[
 \boxed{
 \dim K_\varepsilon\le
 \frac14M^2+
 H_D,\quad
 H_D:=B_\infty B+\frac{1+t_D}{2},\
 t_D=4D+u_D+16.}
 \tag{24}
\]
这是原完整移动来源的界，不是另一块矩阵的独立秩。

置
\[
 u=\sqrt{\frac{M^2}{\beta}}\in[0,1].
\]
\(mC,M\) nef，\(B-mC-M=Z\) 有效。
Hodge 和同一有效比较给两个同时成立的精确式：
\[
 \boxed{
 m^2\kappa\le\beta(1-u)^2,\qquad
 d_C\le\frac{\beta(1-u)}m.}
 \tag{25}
\]
第一式来自
\((m\sqrt\kappa+\sqrt{M^2})^2\le(mC+M)^2\le\beta\)；
第二式来自
\(m d_C=B(B-M-Z)\le\beta-BM\le\beta(1-u)\)。

定义
\[
 F_m(u,\rho)=
 \frac{1-u}{m}+
 \frac{(2m-9)(1-u)^2}{m^2}-\rho.
\]
由 (22)–(25)，得到完全有限的同核联合式
\[
 \boxed{
 \frac{\dim K_\varepsilon}{\beta}
 \le
 \min\left\{
 \frac{u^2}{4}+\frac{H_D}{\beta},\
 \frac12F_m(u,\rho_D)+
 \frac{(m-3)\lambda_C+1+t_C}{2\beta}
 \right\}.}
 \tag{26}
\]
全部未知曲线量在前面都有真实来源和边界成本；两项是同一核的两个上界，取最小值，不作不合法的秩相加。

## 8. 原自然预算中的统一显式秩界

假定真正的五块预算满足
\[
 D\to\infty,\quad
 \frac{\ell}{N}\to x\in(9/41,1/3),\quad
 4N+\ell=n_D+o(D^2),\quad
 n_D=\frac12\beta+O(D).
 \tag{27}
\]
则
\[
 \rho_D\to\rho=\frac1{4+x}
 \in(3/13,41/173).
\]
R950/R951 已付 (1)；因为 \(3/13>11/50\)，(14) 也严格成立。
(15)–(18) 给上文的同核单射。
若 \(x<4/15\)，(17) 另排 \(m=8\)；无需此额外排除也能得到下面统一式。

边界量 \(H_D,\lambda_C,t_C\) 均为 \(O(D)\)，\(\beta\asymp D^2\)。
由 (15)–(16)、(25)，
\[
 u\le1-\sqrt{12\rho-2}+o(1)<3/13.
\]
对这个实际范围，六重的 \(F_6\) 大于其它三种：
\[
 \begin{aligned}
 F_6-F_5&=(1-u)(3-13u)/300\ge0,\\
 F_6-F_7&=(1-u)(3+11u)/588\ge0,\\
 F_6-F_8&=(1-u)(3+5u)/192\ge0.
 \end{aligned}
\]
故可在 (26) 统一用
\[
 F_6(u,\rho)=\frac{3-4u+u^2}{12}-\rho.
\]
在 \(0\le u\le1\) 上，\(u^2/4\) 递增、\(F_6/2\) 递减；
二者的唯一交点由
\[
 5u_x^2+4u_x=3-12\rho
\]
给出，即
\[
 \boxed{
 u_x=\frac{\sqrt{19-60/(4+x)}-2}{5}.}
 \tag{28}
\]
因此取同一个 \(u\) 的最小上界，再对实际 \(u\) 比较，得到
\[
 \boxed{
 \limsup\frac{\dim K_\varepsilon}{n_D}
 \le\frac{u_x^2}{2},\qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}
 (M_5^{\rm orig}|_{\mathcal W_D^\varepsilon})}{n_D}
 \ge\frac{1-u_x^2}{2}.}
 \tag{29}
\]
末步使用原 \(\dim\mathcal W_D^\varepsilon=n_D/2+O(D)\)。
原全矩阵的单位秩至少为任意一个该真实列块的单位秩。

同 R951 的 \(x=11/47\) 比较时，
\[
 \rho=\frac{47}{199},\quad
 a\ge\frac{166}{199}-o(1),\quad
 u_x=\frac{31/\sqrt{199}-2}{5}.
\]
\(m=8\) 已由 (17) 排除。
又 \(155^2<121\cdot199\)，所以 \(u_x<1/25\)，给出 (A)–(B)。

另一便利取值 \(x=2/9\) 给
\[
 \rho=\frac9{38},\quad
 a\ge\frac{16}{19}-o(1),\quad
 u_x=\frac{\sqrt{91/19}-2}{5}.
\]
这些都是对同一实际来源、实际有限窗和全部边界误差的结论，不是只比较抽象 Hilbert 主项。

## 9. 精确推进与仍须支付的整模后页

本文把 R950 的“某个一般成员有坏最近重根”推进为：

- 全部同 parity 核共享的真实 \(F^m\)，且非不变因子对被有限式 (13) 排除；
- 同一个原 \(F\) 的完整 forcing 与 \(P/F^m\) 限制联接的有限式 (10)；
- 在明确下一重数门 (18) 下，整个核到正规化两点线束的实际单射 (20)；
- 对同一剩余来源同时使用 (22)、(24)，给有限式 (26) 和单位秩 (29)。

没有声称原整提升 \(P+pR+p^2S+\cdots\) 仍被某个选择的整 \(F^m\) 整除。
指定仿射 forcing 必须在 (20) 的**实际像**中判定，环境 \(H^0(\widetilde C,\mathscr Q)\) 不自动是满像。
同样，不把未知共同 \(F\) 套成 R948 原指定 \(F\)，不将曲线奇点删除，
不把 \(q=1\) 混合核拆成两个 parity 核。
原高页、真实 carry、有限 away 类及受限 \(S\) 继续保持；
本文未证明原中央非零的无穷性或主目标。

本篇没有新增数学程序执行、素数样本或可重算输出。
