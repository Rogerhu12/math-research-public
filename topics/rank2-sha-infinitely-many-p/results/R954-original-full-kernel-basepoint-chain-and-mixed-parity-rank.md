# R954 — 原全核的累计基点链、固定因子成本与混合奇偶单位秩

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：本文的有限全核维数界及其单位秩推论已证明。**
本篇直接处理原五块矩阵的整个首核，允许同一个来源同时含奇、偶 charge。
实际五个 jet 在物理点给一条有限基点链；共同固定因子在这条链上消耗的接触，
由原十九角 forcing 的自交与完整极除子支付。
除掉真正固定部分后，对同一个移动系统计算实际吹起重数和截面维数。

在原自然预算与短窗比 \(11/47\) 下，本篇给
\[
 \liminf\frac{\operatorname{rank}_{\rm unit}M_5^{\rm orig}}
                    {\dim\mathcal W_D}
 \ge
 \sqrt{\frac{705}{398}}-\frac{633}{796}>\frac12.
 \tag{0}
\]
这是整个矩阵的一次秩估计，包含全部混合首核。证明不需要 R950、
R952 或 R953 的同 parity 固定因子分类。
它尚未判定整个首余核中的实际 Bockstein 是否单射，
也没有从五条中央零制造同预算深核或证明主课题的无穷性。

## 1. 同一原完整来源、矩阵和有限条件

取 R555/R680 的同一个十九次吹起曲面
\[
 \pi:X\longrightarrow\mathbb F_4,\qquad S_0^2=-4,
\]
以及完整原来源
\[
 \mathcal W_D=\bigoplus_{n=0}^D
 Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad
 \mathcal E=Y\partial_Y.
\]
原 \(q_n,e_{n+1}\)、全部中间角帽和显示整基保持不变。
置
\[
 c_D=\lfloor D/2\rfloor,\quad u_D=2c_D+4,\quad
 B=B_D=
 D S_0+(u_D+4D)F_0-\sum_{\alpha,j}\mu_{\alpha,j}(D)E_{\alpha,j}^*,
\]
\[
 \beta=B^2,\qquad
 n_D=\dim\overline{\mathcal W}_D,\qquad
 M_D=5D+4-(D\bmod2).
 \tag{1}
\]
例外类用各步的全变换，\(\mu_{\alpha,j}(D)\) 为 R555 的准确十九个整数。
沿该篇的多项式平凡化，
\[
 H^0(X,\mathcal O_X(B))=d^{c_D}\overline{\mathcal W}_D,\qquad d=1+8t.
 \tag{2}
\]
R680 已证明 \(B\) nef，且
\[
 \beta=\frac{47}{12}D^2+O(D),\qquad n_D=\frac{\beta}{2}+O(D).
 \tag{3}
\]
有限式始终使用 (1) 的准确交数和真实 \(n_D\)，不以主项替换它们。

保 R943 的实际五块矩阵
\[
 M=M_5^{\rm orig}:\mathcal W_D\longrightarrow
 \Gamma^{(5)}_{4s+\ell+13},\qquad p=6s-1,
\]
以及该篇的全部固定坏素数排除。以下假设
\[
 D\ge3,\quad D<p,\quad f_D=\lfloor9D/2\rfloor+4<p,\quad
 N=s-13,\quad 1\le\ell<N,
\]
\[
 q=\lfloor N/5\rfloor\ge1,\qquad q\le\ell,\qquad q\ge\beta/48.
 \tag{4}
\]
本文的 \(q\) 专指这一条链的长度；不对 charge 差的最大公因数作假设。
特别，支持最大公因数为一的来源也在范围内。
由定义 \(q<s\)，所用低轴未超过原 ODE 的有效截止。

全部维数可先扩张到代数闭剩余域 \(k\) 计算；核、秩和交数不变。
记真正的全核为
\[
 \mathcal K=\ker(\bar M:\overline{\mathcal W}_D\to\bar\Gamma).
 \tag{5}
\]
原 \(P_{134}\)、公共单位、charge 四十及四条十三行跨界带仍在 \(M\) 中。
R943 的五十二固定 Smith 成本没有删去。

## 2. 五个实际 jet 给出的累计接触

对 \(\bar P\in\mathcal K\) 置
\[
 \widehat P=d^{c_D}\bar P.
\]
按 R943 (67)、(71)，保实际 \(w^{13}\) 后，四条长行的相对长度恰为
\(N=s-13\)，第五条为 \(\ell\)。
原 charge 的单位缩放、公共 charge 四十的三角换基及公共单位的可逆乘法，
将这些条件准确写成
\[
 (\mathcal E^j\widehat P)(t,g(t))\in t^Nk[[t]]
       \quad(0\le j\le3),\qquad
 (\mathcal E^4\widehat P)(t,g(t))\in t^\ell k[[t]].
 \tag{6}
\]
这里 \(g\equiv(1+8t)\Theta^{17}\pmod{t^s}\)，
\(t\) 与原 \(w\) 相差整单位参数。
第五条换基产生的低阶导数项已在 \(t^N\) 内，因为 \(\ell<N\)。
所有换基对角及 \(1!,\ldots,4!\) 均为当前素数处单位。

物理点 \(P_0=(0,1)\) 避开十九个原中心。
在其完成局部环取
\[
 X_{\rm loc}=Y-g(t).
\]
因 \(g(0)=1\)，Euler 导数和普通 \(Y\) 导数在前五行之间是单位三角变换。
故 (6) 等价于
\[
 \widehat P\in
 I_{N,\ell}:=(t^N,\ t^\ell X_{\rm loc}^4,\ X_{\rm loc}^5)
 \subset k[[t,X_{\rm loc}]].
 \tag{7}
\]
原清分母多项式的 \(\deg_Y\) 小于 \(p\)，所以所用有限 Taylor 系数准确。

对局部函数 \(f\ne0\) 定义 Gauss 估值
\[
 \nu_j(f)=
 \operatorname{ord}_t f(t,g(t)+t^jZ)
 :=\min_i\operatorname{ord}_t[Z^i]f(t,g(t)+t^jZ).
 \tag{8}
\]
它对乘法可加；系数可在 \(k[[t]]\) 中计算。
由 (4)、(7)，每个非零 \(\widehat P\) 满足
\[
 \boxed{\nu_q(\widehat P)\ge
 \min(N,\ell+4q,5q)=5q.}
 \tag{9}
\]

沿形式图 \(Y=g(t)\) 连续作 \(q\) 次普通吹起，中心依次为其严格变换与最新例外的交点。
只需 \(g\) 的有限 \(q\)-jet，故这是实际有限个代数点的吹起，不是假设形式图代数化。
这些中心构成自由链；旧十九角与这条链不相交。

(9) 是累计条件，不能改写成每个严格变换中心的重数至少五。
最初的较大重数可以支付后面的低重数，固定因子也可以在不同阶段退出该链。
因此本篇不把固定重数逐点截成五，再从五中扣掉截帽值；
后文始终使用 (8) 和实际严格变换的累计重数。

## 3. 原 forcing 支付真实链平方成本

令 \(C\) 为一个非垂直、非两原截面、非例外的几何整曲线，
在原多项式图中的 primitive 方程为 \(F(t,Y)\)，
\(b=\deg_YF\ge1\)。R680 引理2给 \(C\) nef。
置
\[
 \kappa_C=C^2,\qquad \lambda_C=\Lambda\cdot C,
\]
其中 \(\Lambda\) 是 R680 (14) 的完整固定极除子。该篇 (16)、(19)、(20) 给
\[
 0\le\lambda_C\le8b,\qquad
 \sum_i\bar h_i+6\sum_{i<l}d_{il}\le3\kappa_C+\lambda_C.
 \tag{10}
\]
这里只取 \(P_0\) 处完整 Hensel 因子的全部根，
\[
 h_i=v_t(\psi_i-g)>0,\quad
 \bar h_i=\min(h_i,s),\quad d_{il}=v_t(\psi_i-\psi_l).
\]
若 \(C\) 不经过 \(P_0\)，所有局部和为零。
\(b\le D<p\) 保这些根 tame；奇点、分数接触阶和完整判别式均由 (10) 覆盖。
该式没有把 \(F_Y\) 当单位。其极成本包括底无穷远及全部十九个中间中心。

令 \(\mu_{C,j}\) 是 \(C\) 在链第 \(j\) 个中心的实际严格变换重数，
\(0\le j<q\)；不经过该中心时置零。
Weierstrass 分解的单位因子在 (8) 下估值为零，故
\[
 \nu_j(F)=\sum_i\min(h_i,j),\qquad
 \mu_{C,j}=\nu_{j+1}(F)-\nu_j(F).
 \tag{11}
\]
第二式也可逐次在图 \(X_{\rm loc}=t^jZ\) 上验证：
先除去此前所有实际例外重数，新中心的最低总次数恰为两次 Gauss 值之差。
它计算严格重数，不是固定减五后的弱变换重数。

设 \(n_C(x)=\#\{i:h_i>x\}\)。由 (11)，
\[
 \mu_{C,j}=\int_j^{j+1}n_C(x)\,dx.
\]
对每个单位区间用 Cauchy，得到
\[
 \begin{aligned}
 \sum_{j=0}^{q-1}\mu_{C,j}^2
 &\le\int_0^q n_C(x)^2\,dx\\
 &=\sum_i\min(h_i,q)+
     2\sum_{i<l}\min(h_i,h_l,q)\\
 &\le\sum_i\bar h_i+6\sum_{i<l}d_{il}\\
 &\le3C^2+\lambda_C.
 \end{aligned}
 \tag{12}
\]
这里用 \(q\le s\) 及
\(d_{il}\ge\min(h_i,h_l)\)。即使某个 \(h_i\ge s\)，也只读取已付截断。
根的全部 tame 共轭求和保证 (11) 给整数重数；未对单个分支的分数阶取整。

对不同的两条几何整曲线 \(C,C'\)，连续吹起的交数公式给
\[
 \boxed{\sum_{j=0}^{q-1}\mu_{C,j}\mu_{C',j}\le C\cdot C'.}
 \tag{13}
\]
理由是每一步从交数扣掉该中心两个真实重数的乘积；
最后两个不同严格变换的剩余交数非负。
(12)、(13) 因而支付任意真正共同固定除子在这条链上的平方成本。

## 4. 整个核的共同固定部分及边界

若 \(\mathcal K=0\)，单位秩已经等于 \(n_D\)。
以下取 \(\mathcal K\ne0\)，将其视为 (2) 内的线性系统。
除去它的**完整共同固定除子**，写
\[
 B\sim A+Z+M.
 \tag{14}
\]
其中
\[
 A=\sum_i m_iC_i
\]
包含全部非垂直、非两原截面、非例外的共同固定几何整曲线及其真实重数；
\(Z\) 包含余下固定边界和垂直部分；
除去 \(A+Z\) 后的生成系统
\[
 V\subseteq H^0(X,\mathcal O_X(M))
\]
没有固定素分量，且 \(\dim V=\dim\mathcal K\)。
这里未将 \(V\) 认作完整 \(H^0(M)\)。

每个 \(C_i\) nef，因此 \(A\) nef。
无固定分量的 \(M\) 也 nef：对任一整曲线可选一个不含它的系统成员，交数非负。
从同一有效余除子 \(Z\) 及 \(B,A,M\) nef，
\[
 (A+M)^2\le B^2.
\]
Hodge 指数不等式遂给
\[
 \boxed{0\le A^2\le\beta,\qquad
 M^2\le(\sqrt\beta-\sqrt{A^2})^2.}
 \tag{15}
\]
这些比较只用同一个完整核，不依赖成员的奇偶性、因子次数上界或通用成员的重复因子分类。

在 \(P_0\) 附近，\(Z\) 的非单位部分只能是底纤维 \(t=0\)。
两原截面及旧例外均避开该点，其余垂直纤维也是单位。
记该固定纤维的重数为 \(r\)。原完整来源的次数帽给
\[
 0\le r\le M_D.
 \tag{16}
\]
原总因子 \(\sum m_i b_i\le D\)，因为与一般底纤维相交。
取 \(V\) 的一个一般成员 \(f\)，使它在有限条链各中心同时具有系统的最小实际重数，
且不新增固定素分量。Gauss 估值的可加性及 (9) 给
\[
 \nu_q(f)\ge5q-\nu_q(A)-r.
 \tag{17}
\]
固定垂直因子 \(t^r\) 贡献的是一份累计 \(r\)，已经保留在此式中。

## 5. 全部固定重数的线性极成本

将真实固定重数分为
\[
 A_{\rm lo}=\sum_{m_i\le11}m_iC_i,\qquad
 A_{\rm hi}=\sum_{m_i\ge12}m_iC_i.
 \tag{18}
\]
这是成本估计的分组，没有改变固定除子，也没有删掉任何重复因子。

由 (12)、(13)，
\[
 \begin{aligned}
 \sum_{j<q}\mu_{A_{\rm lo},j}^2
 &\le\sum_{\rm lo}m_i^2(3C_i^2+\lambda_i)
      +2\sum_{\substack{i<l\\{\rm lo}}}m_im_l C_iC_l\\
 &\le3A_{\rm lo}^2+\sum_{\rm lo}m_i^2\lambda_i\\
 &\le3A_{\rm lo}^2+88D.
 \end{aligned}
 \tag{19}
\]
最后一步用
\(\lambda_i\le8b_i\)、\(m_i^2\le11m_i\) 及 \(\sum m_ib_i\le D\)。
因此
\[
 \nu_q(A_{\rm lo})\le
 \sqrt q\sqrt{3A_{\rm lo}^2+88D}
 \le\sqrt{3q}\sqrt{A_{\rm lo}^2}+\sqrt{88qD}.
 \tag{20}
\]

高重数部分使用 (10) 的线性接触项：
\[
 \begin{aligned}
 \nu_q(A_{\rm hi})
 &\le\sum_{\rm hi}m_i(3C_i^2+\lambda_i)\\
 &\le\frac14A_{\rm hi}^2+8D.
 \end{aligned}
 \tag{21}
\]
确实 \(m_i\ge12\) 给
\(\sum m_iC_i^2\le\sum m_i^2C_i^2/12\le A_{\rm hi}^2/12\)，
不同 nef 曲线的交数均非负。
又 \(A_{\rm hi}^2\le\beta\)，所以 (4) 给
\[
 \frac14A_{\rm hi}^2\le
 \sqrt{3q}\sqrt{A_{\rm hi}^2}.
 \tag{22}
\]
Hodge 对 \(A_{\rm lo},A_{\rm hi}\) 给
\(\sqrt{A_{\rm lo}^2}+\sqrt{A_{\rm hi}^2}\le\sqrt{A^2}\)。
合并 (20)–(22)，得到对全部重数统一的有限式
\[
 \boxed{\nu_q(A)\le
 \sqrt{3qA^2}+\sqrt{88qD}+8D.}
 \tag{23}
\]
这里没有 \(\max m_i=o(D)\) 或任何先验重数上界。

## 6. 真正移动系统的吹起与有限平方损失

令 \(\mu_j\) 为 \(V\) 在上述链第 \(j\) 个中心的实际系统重数。
一般成员同时取这些最小值。
因为 \(V\) 无固定垂直纤维，它的一般成员满足 \(\nu_0(f)=0\)；
逐次严格变换给
\[
 \sum_{j=0}^{q-1}\mu_j=\nu_q(f).
 \tag{24}
\]
由 (16)、(17)、(23) 及 Cauchy，
\[
 \sum_{j<q}\mu_j^2\ge
 \left[
  5\sqrt q-\sqrt{3A^2}-E_D
 \right]_+^2,\qquad
 E_D:=\sqrt{88D}+\frac{8D+M_D}{\sqrt q}.
 \tag{25}
\]
记 \([x]_+=\max(x,0)\)。
这一步只从真实累计和推出平方和，不假设每个中心还有固定数量的独立 jet。

设 \(\sigma:X_q\to X\) 为该有限链的吹起，减去实际重数后的类为
\[
 M_q=\sigma^*M-\sum_{j<q}\mu_jE_j^*.
\]
其生成系统仍无固定素分量：每个新例外的共同最低阶已经准确除去，
其上至少一个系统成员不再消失；旧非固定分量不会由吹起变成固定分量。
因此 \(M_q\) nef，并且
\[
 \boxed{
 M_q^2=M^2-\sum_{j<q}\mu_j^2
 \le
 (\sqrt\beta-\sqrt{A^2})^2
 -[5\sqrt q-\sqrt{3A^2}-E_D]_+^2.
 }
 \tag{26}
\]
所得右边对这个实际 \(A\) 必须非负。

还可消去该生成系统其余所有基点。
曲面上无固定分量的有限系统只需有限次普通点吹起；
每个非平凡步骤减少两个一般成员的有限交数至少一，故过程终止。
记最后光滑有理面为 \(\widetilde X\)，无基点类为 \(L\)。
同一个 \(V\) 的严格变换生成 \(L\)，并且
\[
 \dim\mathcal K=\dim V\le h^0(\widetilde X,L),\qquad
 0\le L^2\le M_q^2.
 \tag{27}
\]
后续消基点不增加来源或目标，也不把 \(V\) 扩大为原核之外的自由修正。

## 7. 随链长增长的曲面上仍统一的截面上界

本节支付 \(h^0(\widetilde X,L)\)，不把未控制的 \(H^1\) 隐藏在线性误差中。
令 \(B_\infty\) 为 R680 (9) 的固定 nef 类，
\[
 \mathcal H=\pi^*(S_0+5F_0).
\]
\(\mathcal H\) 是原 \(\mathbb F_4\) 上 ample 类的拉回，故 nef。
准确有
\[
 \mathcal H B=u_D+5D,\qquad B_\infty B=\frac{47}{12}D+O(1).
 \tag{28}
\]

### 7.1 原移动部分的 canonical 项及吹起后的方向

选择 \(|V|\) 的一个成员避开两截面、十九例外及原有限特殊纤维。
这是有限个真线性子空间的补集，因为 \(V\) 无固定素分量。
其非垂直素分量 \(C\) 用 R680 的末 Gauss 值公式：
\[
 \begin{aligned}
 -K_XC&=2b-(v_0+v_{h_1}+v_{h_2}+v_1+v_d+v_\infty),\\
 4B_\infty C-(-K_XC)
 &=\frac{41}{3}b-\frac13v_1-(v_d+v_\infty)\ge0.
 \end{aligned}
\]
这里原 primitive 条件给 \(v_1\le0\)、\(v_d+v_\infty\le0\)。
一般底纤维也满足 \(-K_XF_0=2\le4B_\infty F_0\)。
按实际重数相加，得到
\[
 -K_XM\le4B_\infty M\le4B_\infty B.
 \tag{29}
\]
第二步用 \(B-M=A+Z\) 有效及 \(B_\infty\) nef。
后者也可直接从 R680 的非边界公式及其固定边界交数核验。

一次以实际重数 \(\mu\) 消基点时，
\[
 K_{\rm new}\cdot L_{\rm new}=K_{\rm old}\cdot L_{\rm old}+\mu.
\]
所以无论链长或其余基点数如何，
\[
 \boxed{K_{\widetilde X}L\ge-4B_\infty B.}
 \tag{30}
\]
这里只需要此下界；不能把新增重数误写成相反符号。

### 7.2 非 pencil 情形：积分 Cartier 曲线与 Hopf 证明

完整 \(|L|\) 也无基点，因为它含生成 \(L\) 的 \(V\)。
若其映射像维数为二，任意特征下的 Bertini 几何不可约性
适用：可取两一般超平面的有限交中一点，再取第三超平面避开该点，
支付 Stacks Project Lemma 37.32.3 的条件 (3)；空基点集支付条件 (4)。

这里只需要参数函数域代数闭包上的一个积分成员。
通用 incidence 是 \(\widetilde X\) 上的 projective bundle，故积分；
其通用纤维在参数函数域上积分，几何通用纤维的支持由上述定理不可约。
可能的几何通用重数是纯不可分的 \(p\) 幂。
若记其支持为 \(C\)，一般支持不能是原底纤维或例外曲线。
更直接地，若 \(L\cdot F_0=0\)，无基点系统在一般原底纤维上的线束
度为零，故其映射在这些纤维上常值，像维数至多一；这与当前情形矛盾。
因此 \(L\cdot F_0>0\)，而 \(L=p^eC\) 给

\[
 1\le C\cdot F_0,\qquad
 p^e(C\cdot F_0)=L\cdot F_0\le B\cdot F_0=D<p.
\]
故 \(e=0\)。作为光滑面上的 Cartier 除子，它没有嵌入分量，
因此几何通用成员 \(C\in|L|\) 积分。
以下可在该代数闭参数域上计算，截面维数、交数与 (30) 保持不变。
没有使用正特征中不成立的一般光滑性断言。

设 \(\mathscr L=\mathcal O_C(L)\)，\(\deg\mathscr L=L^2\)。
\(C\) 是积分 Cartier 曲线，故 Gorenstein，
\[
 p_a(C)=1+\frac{L^2+K_{\widetilde X}L}{2}.
\]
从 \(0\to\mathcal O_{\widetilde X}\to\mathcal O_{\widetilde X}(L)
\to\mathscr L\to0\) 得
\[
 h^0(\widetilde X,L)\le1+h^0(C,\mathscr L).
 \tag{31}
\]

若 \(h^1(C,\mathscr L)=0\)，曲线 Riemann–Roch 及 (30) 给
\[
 h^0(C,\mathscr L)
 =\frac{L^2-K_{\widetilde X}L}{2}
 \le\frac{L^2}{2}+2B_\infty B.
 \tag{32}
\]
若 \(h^1(C,\mathscr L)>0\)，令
\(a=h^0(\mathscr L)\)、\(b=h^0(\omega_C\otimes\mathscr L^{-1})>0\)。
在一个光滑点取消失阶互异的基。
两组基的乘积包含至少 \(a+b-1\) 个消失阶互异的非零截面，
而全部乘积属于 \(H^0(\omega_C)\)。故
\[
 a+b-1\le p_a(C).
\]
与 \(a-b=L^2+1-p_a(C)\) 合并得到
\[
 2a\le L^2+2.
 \tag{33}
\]
这是此处所需的 Clifford 界，证明对积分奇异 Gorenstein 曲线同样成立。
(31)–(33) 给
\[
 h^0(\widetilde X,L)\le
 \frac{L^2}{2}+2B_\infty B+2.
 \tag{34}
\]

### 7.3 Pencil 与零维像

若完整 \(|L|\) 的映射像为曲线，对其作 Stein 分解
\(f:\widetilde X\to T\)。
\(\widetilde X\) 是有理光滑面，\(H^1(\mathcal O_{\widetilde X})=0\)；
由 \(f_*\mathcal O_{\widetilde X}=\mathcal O_T\)，
Leray 使 \(H^1(\mathcal O_T)\) 注入零空间，所以光滑正规底曲线 \(T\cong\mathbf P^1\)。
有 \(L=f^*\mathcal O_{\mathbf P^1}(a)\)，因而
\[
 h^0(\widetilde X,L)=a+1.
\]
一般纤维 \(F\) 为移动有效除子，不可能全由原底面上的有限例外曲线组成；
故 \(\mathcal H F\ge1\)，并且
\[
 a\le\mathcal H L\le\mathcal H B,\qquad
 h^0(\widetilde X,L)\le u_D+5D+1.
 \tag{35}
\]
若像为一点，则生成的线束平凡，\(h^0=1\)，也满足此界。

结合两种情形，定义明确线性项
\[
 C_D:=2B_\infty B+\mathcal H B+2.
 \tag{36}
\]
由于 \(L^2\ge0\)，统一有
\[
 \boxed{h^0(\widetilde X,L)\le\frac12L^2+C_D.}
 \tag{37}
\]
这对不完整原系统 \(V\) 给上界，未将它等同于完整 \(|L|\)。
常数只读原十九角的固定类，和新增基点个数无关。

## 8. 有限全核定理

**定理。** 在 (1)–(5) 的同一实际五块矩阵中，若 \(\mathcal K\ne0\)，
取其完整固定除子的非边界部分 \(A\)，则
\[
 \boxed{
 \dim\mathcal K\le
 \frac12\left\{
  (\sqrt\beta-\sqrt{A^2})^2
  -[5\sqrt q-\sqrt{3A^2}-E_D]_+^2
 \right\}+C_D.
 }
 \tag{38}
\]
其中 \(E_D,C_D\) 分别是 (25)、(36) 的显示有限量。
原全矩阵的单位秩准确为 \(n_D-\dim\mathcal K\)，故 (38) 立即给它的下界。

**证明。** (15)、(25) 给同一个移动系统的 (26)；
(27) 的后续消基点只进一步减少自交。
最后用 (37)。全部固定分量、垂直 \(r\)、高重数和额外基点均已在同一个不等式内支付。证毕。

无需预先识别 \(A\) 时，可对 \(0\le a\le\beta\) 取
(38) 右边的最大值，得到完全由 \(D,N,\ell\) 决定的有限数值上界。
这一取最大不声称任意 \(a\) 可由原核实现。

在 \(q\asymp D^2\) 时，
\[
 E_D=O(\sqrt D),\qquad C_D=O(D).
\]
因此展开 (38) 的平方时出现的统一误差为 \(O(D^{3/2})\)，是 \(o(D^2)\)；
不能将它写成未经支付的 \(O(D)\)。
有限结论本身仍用完整 \(E_D\)，没有舍弃这项。

## 9. 同一全核的优化及越过一半的单位秩

考虑真实参数序列
\[
 D\to\infty,\qquad
 \ell/N\to x,\qquad
 4N+\ell=n_D+o(D^2).
 \tag{39}
\]
例如任意固定 \(1/5<x<4/5\) 均使 (4) 的两个额外链条件最终成立：
\[
 \ell/q\to5x>1,\qquad
 q/\beta\to\frac1{10(4+x)}>\frac1{48}.
\]
实际物理目标仍是 \(4s+\ell+13\)；其与这里相对长度的差为固定常数，
从未通过非整逆删掉十三行带。

置
\[
 c_D'=\frac{25q}{\beta}\longrightarrow
 c=\frac5{2(4+x)},\qquad z=\sqrt{A^2/\beta}\in[0,1].
\]
(3)、(38) 及上一节的统一误差给
\[
 \frac{\dim\mathcal K}{n_D}
 \le
 (1-z)^2-(\sqrt c-\sqrt3\,z)_+^2+o(1),
 \tag{40}
\]
误差对实际 \(z\) 一致。

当 \(1/3\le c\le3\) 时，右边的主项在
\(0\le z\le\sqrt{c/3}\) 上为
\[
 1-c+2(\sqrt{3c}-1)z-2z^2,
\]
其最大点是 \(z=(\sqrt{3c}-1)/2\)，属于该区间。
在余下区间主项为 \((1-z)^2\)，其最大不超过前一抛物线的最大值。
故
\[
 \boxed{
 \limsup\frac{\dim\mathcal K}{n_D}
 \le\frac32+\frac c2-\sqrt{3c},\qquad
 \liminf\frac{\operatorname{rank}_{\rm unit}M}{n_D}
 \ge\sqrt{3c}-\frac{1+c}{2}.
 }
 \tag{41}
\]

采用原已使用的自然短窗比 \(x=11/47\)，
\[
 c=\frac{235}{398},\qquad
 \boxed{
 \liminf\frac{\operatorname{rank}_{\rm unit}M_5^{\rm orig}}{n_D}
 \ge\sqrt{\frac{705}{398}}-\frac{633}{796}>\frac12.
 }
 \tag{42}
\]
最后的严格不等式可不用小数核验：
\(235/398>4/7\)，函数 \(\sqrt{3c}-(1+c)/2\) 在 \(c<3\) 递增，
而在 \(c=4/7\) 时
\(\sqrt{12/7}>9/7\)，因为 \(84>81\)。
因此该处单位秩比例严格大于 \(1/2\)。

(42) 同时处理 charge 最大公因数为一、混合奇偶、
任意真实重复次数和边界含量。
没有先证明两个子块各自的秩，再将可能相交的像相加。

## 10. 此结果真正支付与继续保留的门

本篇新增输入是同一个原首核的固定部分与移动部分的联合面积预算。
(23) 控制固定因子消耗的累计接触；(25) 将剩余累计接触变成移动系统的真实平方损失；
(37) 在链长随 \(D\) 增长时仍支付统一截面维数。
三步共同给全核的 (38)，而非仅给一个已指定因子的限制接口。

对原整矩阵，单位 Smith 因子之外的层仍需要同一个
\[
 \beta_1:\ker\bar M\longrightarrow\operatorname{coker}\bar M
\]
及其实际原来源修正。
(42) 不证明此映射单射，不把
\(\operatorname{coker}(\bar M|_{\mathcal W_D^\varepsilon})\)
代替全余核，也不自动产生某个指定 \(c_1\) 或最高正面 forcing 的非零。
R943 的原参数、完整公共单位、所有 carry 和下一页尾项继续保持。

五条原中央联合非零的跨素数结论、与通常全 Selmer 的原算术桥的最终合成、
以及无穷不同素数上的 Sha 初级有限，均不能从一个单位秩比例直接推出。
本篇没有新增数学程序执行、素数扫描、低项数据或可重算输出。

## 依赖与标准几何来源

- [R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)，
  §10 的同一实际五块矩阵、完整公共单位、真实十三行带及 (67)、(71)。
- [R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)，
  §2 的原 nef 类、§§3–4 的完整固定极除子、非零 Euler forcing、
  tame 根、截断及完整判别式能量，尤其 (19)、(20)。
- [R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)，
  §2 的整个原来源识别、十九个准确重数、显示整格和次数帽。
- The Stacks Project，
  [Lemma 37.32.3，tag 0G4F](https://stacks.math.columbia.edu/tag/0G4F)；
  [证明所在 §37.32，tag 0G4C](https://stacks.math.columbia.edu/tag/0G4C)。
  本文仅用其任意特征的几何不可约性，已在 §7.2 逐项支付条件；
  积分性另由通用 incidence 和 \(D<p\) 排除纯不可分重数。
  曲线维数所需的奇异 Gorenstein 情形在 §7.2 用伴随、Riemann–Roch、
  Serre 对偶及 Hopf 的消失阶证明完整写出。
