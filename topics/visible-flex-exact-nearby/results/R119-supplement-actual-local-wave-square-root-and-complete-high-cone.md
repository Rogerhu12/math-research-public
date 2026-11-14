# R119 续篇：真实局部波动平方根、完整高锥与切口边界项

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇先把当前非径向 Jacobi 方程在真实
内部特征图上的高度、密度、全部源和两物理端口写准，再在其中
一个真正的 canonical 矩形上构造完整有界高锥系统。
其精确平方根和 canonical 两行平衡表明：bulk 对角相位没有
order \(-2\) 项。这来自真实标量波动结构，并非由实性或酉性猜测。

硬 Fourier 切口的 chronological commutator 仍有一个准确的
order \(-2\) 边界列。本篇将它保留；只有把两边端口置于
明确 buffer 之后，才另付其增益。所有低模、另一角锥及两个
mean 都继续参加完整耦合。

这不是整个负分量的同宽 WKB 结论。局部特征图的两个物理
径向端点一般是不同的图面；其真实图、circle-return 和端角
FIO 仍须进入全网络，不能以一个方便的局部 \(s\)-切口代替。

## 1. 当前实际 raw 方程与局部真实特征图

采用[第61束完整 canonical/profile 方程](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
的同一个当前 \(\Gamma\)、同一个非零标签背景。
为免与第一主剪切混淆，写原判别式为 \(\mathcal D\)、
完整 \(J\) 为 \(\mathcal J\)。其真实散度矩阵是
\[
 G=\mu
 \begin{pmatrix}1&-d\\-d&d^2-\nu^2\end{pmatrix},
 \qquad
 \nu=qv,\quad q=\sqrt Q,\quad
 \mu=(w/r)\mathcal J\mathcal D^{-3/2},\quad
 v=\sqrt{\mathcal D}/\mathcal J ,
 \tag{C.1}
\]
\[
 \operatorname{div}(G\nabla h)=f-\operatorname{div}F,\qquad
 \pi_{\rm phys}=\mu(h_t-dh_\theta)+F^t.
 \tag{C.2}
\]
在真正未使用的 quartic 严格区间内，系数及当前解有本篇
所需的有限径向导数：原四态方程的分母是
\(\mathcal J\)，不是 \(Q\)，每次径向微分由该方程及一个明确
角余宽给出。此处不越过只有 \(C^2\) 的原径向接缝。

以同一个物理初始圆为两个逆特征标签的起点，
\[
 (\partial_t-d\partial_\theta)S_\pm
                              =\pm\nu\,\partial_\theta S_\pm,
 \qquad
        s=(S_+-S_-)/2,\quad \phi=(S_++S_-)/2.
 \tag{C.3}
\]
在足够小的真实内部邻域中，两个角导为正。
其 Jacobian 准确为
\[
 J_\Psi=s_t\phi_\theta-s_\theta\phi_t
                         =\nu S_{+,\theta}S_{-,\theta}>0.
 \tag{C.4}
\]
这就是原双特征图的局部版本，不需要把右端 return 假设为平移。
在其像中取任意闭 canonical 矩形；以下算子在这个真实矩形上
定义。若需将矩形端口送回原固定 \(t\) 圆，必须使用 §8 的图面
公式。

二维 divergence density 的行列式不变，给
\[
 \frac{D\Psi\,G\,D\Psi^T}{J_\Psi}
                         =\Lambda\operatorname{diag}(1,-1),
 \qquad
 \Lambda=\sqrt{-\det G}=\mu\nu
                              =\frac wr\,\frac q{\mathcal D},
 \tag{C.5}
\]
其中右端按 \(\Psi^{-1}\) 复合。最后的
\(\mathcal J\) 准确抵消，不能再独立收费或漏掉
\(\mathcal D^{-1}\)。

置 \(U=\sqrt\Lambda\,h\)、\(m=\Lambda^{-1/2}\)，得到准确的
非径向 scalar wave
\[
                 U_{ss}-U_{\phi\phi}+V(s,\phi)U
                         =f_c-\partial_s Z^s-\partial_\phi Z^\phi,
 \tag{C.6}
\]
\[
 V=-\tfrac12L_{ss}-\tfrac14L_s^2
                  +\tfrac12L_{\phi\phi}+\tfrac14L_\phi^2,
 \qquad L=\log\Lambda .
 \tag{C.7}
\]
等价地，若先用原严格密度篇的准确 \(\kappa\)，则
\[
                         V=(\kappa/J_\Psi)\circ\Psi^{-1}.
 \tag{C.8}
\]
径向时 \(J_\Psi=q\)，(C.8) 恰为第65束的完整 \(V\)，
并非只剩 principal 部分。

## 2. 全部 ordinary/weak 源：高度共轭的额外列

先作真实 Piola 变换
\[
 \widetilde f=(f/J_\Psi)\circ\Psi^{-1},\qquad
 \widetilde F=(D\Psi\,F/J_\Psi)\circ\Psi^{-1}.
 \tag{C.9}
\]
高度共轭后的准确源是
\[
 \boxed{\quad
 Z=m\widetilde F,\qquad
 f_c=m\widetilde f+\nabla m\cdot\widetilde F .
 \quad} \tag{C.10}
\]
最后一项来自
\(-m\operatorname{div}\widetilde F
 =-\operatorname{div}(m\widetilde F)+\nabla m\cdot\widetilde F\)，
不能从 weak 源中删除。没有对 \(F^t\) 作径向微分。

以下任何 high-cone 源都指 (C.10) 的完整源。
仅有弱 \(L^2\) 范数并不免费授予 \(Z^s\) 的端点迹；
恢复 bare flux 时仍须它的真实 trace 合同。

## 3. 一个真实完整高锥及保留的互补空间

周期仍为 \(\pi/2\)，频率 \(m\in4\mathbb Z\)。
令 \(P=P_N\) 是所有 \(m\ge N>0\) 的正角锥，
\(Q_N=I-P_N\) 保留其完整互补空间，包含有限正 head、
零模和全部负角锥。令 \(D\) 在 \(P\) 上为对角乘 \(m\)，
\[
             W=P M_VP,\qquad U_H=PU,\quad U_C=Q_NU.
 \tag{C.11}
\]
这里 \(P\) 没有有限 Fourier 上界。当前 \(V\) 实值，
所以 \(W\) 自伴。

以下给完全可核的门。取 \(r\ge0\)，令
\[
 R=1+\max_{0\le q\le2}
          \|\partial_s^q V\|_{L^\infty_s\mathcal A^{r+8}},
 \qquad N^2\ge64R,\qquad
 \|g\|_{\mathcal A^a}=\sum_k(1+|k|)^a|\widehat g(k)|.
 \tag{C.12}
\]
这对当前光滑内部矩形是真正有限数；
本篇没有把它假定成整尾统一常数。
该式也明确给后续实际 potential 预算的消费者。

定义核范数
\[
 \mathfrak n_{p,a}(T)
 =\sum_k(1+|k|)^a
     \sup_{\substack{m,n\ge N\\m-n=k}}
                       \min(m,n)^p|T_{mn}|.
 \tag{C.13}
\]
空集的 supremum 取0。它控制全高锥，且
\[
 \mathfrak n_{p+q,a}(AB)
       \le\mathfrak n_{p,a+q}(A)\mathfrak n_{q,a+p}(B),
 \quad
 \mathfrak n_{p+\alpha,a}(\mathscr L_{D^\alpha}^{-1}A)
                         \le\tfrac12\mathfrak n_{p,a}(A),
 \tag{C.14}
\]
\[
      (\mathscr L_{D^\alpha}^{-1}A)_{mn}
                    =A_{mn}/(m^\alpha+n^\alpha).
 \tag{C.15}
\]
第一式逐项使用
\(\min(m,n)\le\min(m,\ell)+|\ell-n|\)
及其对称式；第二式是
\(m^\alpha+n^\alpha\ge2\min(m,n)^\alpha\)。
所有中间 \(\ell\ge N\) 均实际求和，没有把压缩乘法换成
未压缩乘法。
例如 \(\mathfrak n_{p,|s_0|+p}(A)\) 界住
\(A:H^{s_0}\to H^{s_0+p}\)，所以它是完整算子门。

## 4. 实际正平方根：无 order \(-2\) 的精确原因

记 \(\mathscr L_D T=DT+TD\)，并置
\[
                A_1=\mathscr L_D^{-1}W.
 \tag{C.16}
\]
真实 \(\Omega=(D^2+W)^{1/2}\) 可以由收缩直接构造：
\[
       \Omega=D+T,\qquad
       T=A_1-\mathscr L_D^{-1}(T^2).                         \tag{C.17}
\]
在 \(\mathfrak n_{1,a}\le R\) 的球上，第一项至多 \(R/2\)。
这里同阶二次项还有更强的准确界
\[
 \mathfrak n_{1,a}(\mathscr L_D^{-1}(T_1T_2))
       \le(2N^2)^{-1}\mathfrak n_{1,a}(T_1)\mathfrak n_{1,a}(T_2).
 \tag{C.18}
\]
因此映射入球且 Lipschitz 常数至多 \(R/N^2\le1/64\)。
迭代保自伴，且 \(\|T\|<R/N<N/64\)；
\(D+T\) 真正正、自伴，并由平方恒等式识别为正平方根。
这不是形式取根。

由 (C.14)，实际余项满足
\[
 \Omega=D+A_1-\mathscr L_D^{-1}(A_1^2)+E_5,
 \qquad
            \mathfrak n_{5,r}(E_5)\le R^3.
 \tag{C.19}
\]
具体地 \(T-A_1=-\mathscr L_D^{-1}(T^2)\) 的
\(\mathfrak n_{3,r+3}\le R^2/2\)；
再在 \(T^2-A_1^2=(T-A_1)T+A_1(T-A_1)\) 中用 (C.14)，
即得 (C.19)。所需角阶严格包含在 (C.12) 的 \(r+8\) 内。

特别
\[
 (A_1)_{mn}=\frac{\widehat V(m-n)}{m+n}.                      \tag{C.20}
\]
这是准确的 Weyl order \(-1\) 核；它并没有另一个隐藏的
order \(-2\) 展开项。下一项
\(-\mathscr L_D^{-1}(A_1^2)\) 是完整 order \(-3\)，
包含全部真实中间频率，而不只 \(V^2/(8D^3)\) 的主项。

## 5. 真 canonical 两行平衡及首个非径向 connection

令 \(B_0=\Omega^{1/2}\)、\(A=(B_0)_sB_0^{-1}\)。
第二次正平方根同样可以由完整核收缩构造。
其前项为
\[
 B_0=D^{1/2}+P_1+E_{7/2},\qquad
 P_1=\mathscr L_{D^{1/2}}^{-1}A_1,\qquad
       \mathfrak n_{7/2,r+2}(E_{7/2})\le4R^2.
 \tag{C.21}
\]
一个自足构造是先在
\(\mathfrak n_{1/2,r+6}\le R/N\) 的球解
\[
 B_0-D^{1/2}
   =\mathscr L_{D^{1/2}}^{-1}
       [T-(B_0-D^{1/2})^2].
 \tag{C.22}
\]
同阶二次常数为 \(1/(2N)\)，仍有 \(R/N^2\) 收缩。
再用 (C.14) 提升到 order \(-3/2\)，以及
\(T-A_1\) 的 order \(-3\)，便给 (C.21)。
对 \(s\) 求导的线性方程有同一收缩常数；
\(B_0^{-1}-D^{-1/2}\) 为 order \(-5/2\)，由完整
Neumann 级数给 \(\mathfrak n_{5/2,r+2}\le2R\)。
这些构造包含真实 \(V_s\)，没有假定平方根与它可交换。

于是
\[
 A=(P_1)_sD^{-1/2}+E_4^A,\qquad
                   \mathfrak n_{4,r}(E_4^A)\le64R^2.
 \tag{C.23}
\]
定义
\[
       K=(A-A^*)/2,\qquad B_s^{\rm off}=(A+A^*)/2.
 \tag{C.24}
\]
两者的准确首核分别为
\[
 (K_3)_{mn}
  =\frac{(m-n)\widehat {V_s}(m-n)}
    {2\sqrt{mn}(m+n)(\sqrt m+\sqrt n)^2},                    \tag{C.25}
\]
\[
 (B_2)_{mn}
                 =\frac{\widehat {V_s}(m-n)}
                              {2\sqrt{mn}(m+n)}.            \tag{C.26}
\]
并有
\[
 \mathfrak n_{3,r}(K_3)\le R,\quad
 \mathfrak n_{2,r}(B_2)\le R,\quad
 \mathfrak n_{4,r}(K-K_3),\
 \mathfrak n_{4,r}(B_s^{\rm off}-B_2)\le64R^2.
 \tag{C.27}
\]
\(K\) 真正反自伴，\(B_s^{\rm off}\) 真正自伴。
首核中的 \(m-n\) 是实际 commutator 的准确因子；
不是从“非径向很小”猜测出的一导增益。

引入高锥**总通量**
\[
        p_H=(U_H)_s+PZ^s,\qquad
        Y=B_0U_H,\quad Z_H=B_0^{-1}p_H,\qquad
        a_\pm=(Y\pm iZ_H)/\sqrt2.
 \tag{C.28}
\]
则完整有源系统准确为
\[
 \partial_s\binom{a_+}{a_-}
 =
 \begin{pmatrix}
 -i\Omega+K&B_s^{\rm off}\\
 B_s^{\rm off}&i\Omega+K
 \end{pmatrix}
 \binom{a_+}{a_-}
 +\binom{\mathcal S_+}{\mathcal S_-},                       \tag{C.29}
\]
\[
 g_H=P f_c-PM_VU_C-iD(PZ^\phi),\qquad
 \mathcal S_\pm=
       [-B_0(PZ^s)\pm iB_0^{-1}g_H]/\sqrt2.                 \tag{C.30}
\]
因此 bulk 对角 Hamiltonian
\(\Omega+iK\) 从 \(D+A_1\) 直接进入 order \(-3\)；
off-diagonal 的首项是 order \(-2\)。
若再用两支 gap 的 Sylvester 方程消它，需要一个 order
\(-3\) 的真实两态变换，而不是把它删去。
本篇 (C.29) 保留这个完整交叉项，尚未把它免费压成 phase。

## 6. chronological commutator 的真实硬切口列

设 \(V,W\) 为两个时刻经真实 principal 平移拉回的实系数，
并令 \(A(V)=\mathscr L_D^{-1}(PM_VP)\)。
完整 commutator 的核是
\[
 [A(V),A(W)]_{mn}
 =\sum_{\ell\ge N}
 \frac{\widehat V(m-\ell)\widehat W(\ell-n)
      -\widehat W(m-\ell)\widehat V(\ell-n)}
                  {(m+\ell)(\ell+n)}.
 \tag{C.31}
\]
准确分解成
\[
 [A(V),A(W)]_{mn}
    =\frac{E_{mn}}{(m+n)^2}+R_{mn},\qquad
 E=PM_WQ_NM_VP-PM_VQ_NM_WP.                                \tag{C.32}
\]
这是完整 \(M_VM_W=M_WM_V\) 后的投影恒等式。
\(E\) 包含真正 finite head、mean 和整个另一角锥；
它一般不为0。不能把所有 \(P\) 和乘法互换。

bulk 余项满足
\[
 \mathfrak n_{3,r}(R)
       \le16\|V\|_{\mathcal A^{r+1}}\|W\|_{\mathcal A^{r+1}}.
 \tag{C.33}
\]
逐项证明只需
\[
 \left|\frac1{(m+\ell)(\ell+n)}-\frac1{(m+n)^2}\right|
 \le8\,\frac{|m-\ell|+|\ell-n|}{\min(m,n)^3}.
 \tag{C.34}
\]
若右端的 lag 和至少 \(\min(m,n)/2\)，原两个分母直接给该界；
否则三频率可比较，展开分母差得到同一界。
故 (C.33) 包含所有高输出，不是只对有限保留模成立。

切口项本身只先有 order \(-2\)。
若明确把其两端都放在 \(P_{2N}\)，则每个
\(\ell<N\) 满足
\(|m-\ell|\ge m/2,\ |\ell-n|\ge n/2\)。
因此另外有真实 buffer 门
\[
 \mathfrak n_{4,r}
 \left(P_{2N}\frac{E_{mn}}{(m+n)^2}P_{2N}\right)
 \le2\|V\|_{\mathcal A^{r+1}}\|W\|_{\mathcal A^{r+1}}.
 \tag{C.35}
\]
其中
\(\min(m,n)^4/(m+n)^2\le |m-\ell|\,|\ell-n|\)
逐项支付了两导增益。
没有满足此 buffer 的端口仍保留 (C.32)，不是丢弃。
特别，本篇没有在整个硬高锥上宣称所有 chronological
order \(-2\) 项消失。

## 7. 参数导数、完整互补历史和两个 mean

对真实 profile/label 参数求导时，(C.17)、(C.22) 的
线性化具有同一个可逆收缩方程；因此 \(\dot\Omega,\dot B_0\)
由实际 \(\dot V\) 定义。
在 (C.30) 中必须同时保留
\[
             -PM_{\dot V}U_C-PM_V\dot U_C
 \tag{C.36}
\]
和两个源、密度以及图的全部参数变化。
\(U_C\) 是整个方程的真实互补状态；在全逆问题中它不是
可以任意置零的外源。

zero Fourier mode 的 \(U_0,p_0\) 均在 \(Q_N\) 内。
而物理高度/通量 mean 与 canonical mean 之间还有真实
\(\sqrt\Lambda\) 和角图；两者不能混同。
第61束的自由 holonomy 线性化仍是原 bare flux mean，
并不因非线性背景固定 \(M=1\) 就要求任意 Jacobi 输入的
该 mean 为0。互补方程及 (C.36) 完整保留这些列。

## 8. 回到两个真实物理端口：图面项仍存在

一个原 \(t=t_e\) 圆在本图中一般为
\[
                       s=\chi_e(\phi),\qquad \phi=H_e(\theta).
 \tag{C.37}
\]
这里的两个 \(H_e,\chi_e\) 通常不同，不是从局部 Lorentz
坐标自动得到同一对 \(s\)-常数圆。
令
\[
 p_{\rm gr}=U_s+\chi_e' U_\phi+Z^s-\chi_e'Z^\phi .
 \tag{C.38}
\]
真正的物理两迹满足
\[
 \boxed{\quad
 h_e=\Lambda^{-1/2}U\big|_{\rm gr}\circ H_e,\qquad
 \pi_e=H_e'\sqrt\Lambda
   \left[p_{\rm gr}
          -\tfrac12(L_s+\chi_e'L_\phi)U\right]_{\rm gr}\circ H_e .
 \quad} \tag{C.39}
\]
这是包含真实 normal shear 与两 weak 电荷的完整 Piola 公式。
其 mean 准确为
\[
 \int\pi_e\,d\theta
   =\int\sqrt\Lambda
       [p_{\rm gr}-\tfrac12(L_s+\chi_e'L_\phi)U]_{\rm gr}\,d\phi.
 \tag{C.40}
\]
这也说明不能清零 canonical mean 来代替物理 mean 条件。

沿参数求导，(C.39) 中 \(H_e,\chi_e,\Lambda,Z\) 的所有
变化均存在；已有实际 ray 响应门可以消费它们，但本篇没有
把这些变化宣布为同阶 operator-norm 小量。
两端图通过完整 circle-return/KAM 以及相邻正型块接回全网络，
仍是下一道实门。

新增结论的范围因而精确：当前实际 scalar wave 允许
(C.17)--(C.30) 的真正无频率上截断平方根和平衡，bulk
order \(-2\) 相位不存在；hard-cutoff 边界列 (C.32)、
互补历史、两个 mean 和全部 source/physical 端口均原样保留。
这些公式为第65束共同高频方向的非径向 paired 比较提供
具体输入，尚不是整个非线性 \(\mathcal F=0\) 的逆。

[必要准确核代数与有理门](../scripts/fourfold_actual_local_wave_high_cone_20261114.py)
及[实际执行记录](../notes/2026-11-14-R119-actual-local-wave-high-cone-budget.json)
保存两行、commutator、source 和 norm 常数的有限核验。
