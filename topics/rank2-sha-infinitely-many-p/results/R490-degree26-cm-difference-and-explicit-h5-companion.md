# R490 — 原 degree26 因子的显式 CM 差、两输出与实际 H5 伴随

日期：2026-11-14。**状态：已证明。** 本篇在原
\(E_{17}:y^2=x^3+17\) 的同一个 sigma、周期和测度格中，把
\(S_{34}\) 的一个 degree26 因子完全识别为两个原 degree2
参考的 CM 缩放之差。它自己的中央导数由一个非零的固定代数数
\(p\)-adic 对数准确给出。

与剩余 degree8 因子联合后，原 \(S\) 的条件行有一个 degree442
伴随。本篇不把它留作未知截面：它准确是原秩零 \(H_5\) 的两个
norm13 缩放的明确线性组合。全部两态核心、输入限制和反卷积
移动的单位条件均保留。因此辅助中央非零没有被直接当成原
\(S\) 中央非零，主目标尚未完成。

## 1. 同一原规范及完整低 degree 因子

沿用 R295、R302、R308、R483 的
\[
 b=17,\quad \delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
 X=x^3,\quad t=-b/X,\quad \Theta=x\sigma^2,
\]
\[
 a(t)=t(t-1)(7+4t+16t^2),\qquad d(t)=1+8t .
\tag{1}
\]
原 \(S\) 的首项为 \(z^6\)，其实际因式为
\[
 \boxed{\begin{aligned}
 C(z)&=\frac{\Theta(z)^{13}a(t(z))}{7b}\\
 &=\sigma(z)^{26}x(z)
 \left(X^3+\frac{3b}{7}X^2+\frac{12b^2}{7}X+\frac{16b^3}{7}\right),\\
 \Theta(2z)&=\sigma(z)^8x(z)(X-8b)=\Theta(z)^4d(t(z)),\\
 S(z)&=C(z)\Theta(2z).
 \end{aligned}}
\tag{2}
\]
故 \(C\in\mathcal S_{26}\)、\(C(0)=0\)、\([z^6]C=1\)；
它是整个全纯来源，未在原点删极后改变 theta 乘子。

置
\[
 \gamma=\gamma_{13}=(7+\delta)/2,\qquad \gamma\bar\gamma=13.
\]
在 \(b=1\) 时，实际 norm13 division polynomial 是
\[
 q_{13}(x)=x^6+(2+6\delta)x^3+(40+24\delta)/13.
\]
保完整 sigma 乘子，R466 的同源公式给
\[
 \Theta(\gamma z)=\sigma(z)^{26}x(z)
 \left[
 X^4+(-32-168\delta)X^3+(-1128-72\delta)X^2
 +(-1184-288\delta)X+640-384\delta
 \right].
\tag{3}
\]
这是有限除子空间中的整个多项式身份；附脚本从同一个
\(q_{13}\) 的全同源分子重新得到所有系数。一般 \(b\) 的 \(X^j\)
系数乘以 \(b^{4-j}\)，没有省掉 \(b\) 的尺度。

取 (3) 与共轭之差，与 (2) 逐项比较即得
\[
 \boxed{C(z)=
 \frac{\Theta(\bar\gamma z)-\Theta(\gamma z)}{336b\delta}.}
\tag{4}
\]
这不是新的秩二曲线来源：它是同一个秩零 degree2 来源的两个
实际单位推前之差。

## 2. 完整 ordinary 核与一个已知非零的中央导数

保原固定普通 ray
\[
 \pi_0\equiv1428552127+2161889730\omega
       \pmod{2793510720},\quad
 \lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
 \kappa=p/\bar\pi_0^2,\quad d_p=p-1 .
\tag{5}
\]
\(p>19,\ p\equiv7\pmod{64},\ p\equiv1\pmod3\)，原全部有限坏集
和实际 Euler 规范均保留。R416/R483 已付 \(1-\lambda\)、
\(1+\lambda\) 在这条 ray 上为单位。

原 \(\Theta\) 的整个测度关系是
\[
 \nu_\Theta|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_\Theta,
 \qquad \nu_\Theta(\mathbf Z_p)=1 .
\tag{6}
\]
\(\gamma,\bar\gamma\) 都是当前位的单位，所以其尺度与同一深度
限制交换。(4) 因而直接给 \(C\) 的同一个 scalar core \(\beta\)。

还可支付整个 \(\mathcal S_{26}\) 的绝对核心。精确计算
\[
 g=\pi_0/\bar\pi_0\equiv27=1+26\pmod{52}.
\tag{7}
\]
它在 canonical 两个 Heisenberg 生成元上分别只增加平行整周期；
degree26 的标准偶半特征使这两个相位均为一。故整个 \(K_{26}\)
与这两个生成元交换，是一个标量。实际非零锚
\(\Theta(\gamma z)\in\mathcal S_{26}\) 的 core 为 (6)，从而
\[
 \boxed{K_{26}=-I\quad\hbox{在整个 }\mathcal S_{26}\hbox{ 上}.}
\tag{8}
\]
这里采用原归一 \(\nu_F|_p=\lambda[\kappa]_*\nu_{K_NF}\)，
不是从 projective 交织任意选择负号。

对任意这些实际来源，记
\[
 J_F(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{d_pu}\,d\nu_F(x).
\tag{9}
\]
由 (4)、(6)，整个 \(u\) 的恒等式为
\[
 J_C(u)=
 \frac{\langle\bar\gamma\rangle^{d_pu}
       -\langle\gamma\rangle^{d_pu}}{336b\delta}J_\Theta(u),
 \qquad J_\Theta(0)=1+\lambda.
\tag{10}
\]
因此
\[
 \boxed{J_C'(0)=
 \frac{d_p\log\langle\bar\gamma/\gamma\rangle(1+\lambda)}
      {336b\delta}\ne0 .}
\tag{11}
\]
非零性完全明确：\(\gamma,\bar\gamma\) 是不同的 norm13 素元，
二者公因子只能除 \(\gamma-\bar\gamma=\delta\)，故互素。
\(\bar\gamma/\gamma\) 在这两个素理想上的赋值为 \(1,-1\)，不可能
是全局根单位。如果它在普通局部嵌入的单位对数为零，则为局部
根单位，同一个代数数满足相应 \(X^n-1=0\)，与上述赋值矛盾。
本篇只使用非零，不假定该对数有统一的赋值上界。

## 3. 保原两输入的完整 degree34/442 联合

令物理输入 \(A,D\) 分别携带 \(\nu_C,\nu_\Theta\)，定义
\[
 W=A+2D,\qquad V=2A-13D,\qquad
 T=\begin{pmatrix}1&2\\2&-13\end{pmatrix},\qquad \det T=-17.
\tag{12}
\]
它在当前处是整自同构，且
\[
 T\operatorname{diag}(26,2)T^t=\operatorname{diag}(34,442).
\]
对偶生成函数为
\[
 \boxed{\Phi(w,v)=C(w+2v)\Theta(2w-13v)
     \in\mathcal S_{34}\otimes\mathcal S_{442}.}
\tag{13}
\]
两轴交叉 Gaussian 为零，所有 sigma 次数均偶，故确是标准
完整张量格，没有隐藏平坦特征。

写
\[
 \Psi(w,v)=\Phi(-w,v)=\Phi(w,-v).
\tag{14}
\]
R416/R483 的 whole \(K_{34}\) 是第一轴反射，故
\(K_W\Phi=\Psi,\ K_W\Psi=\Phi\)。
原 \(A,D\) 同时深与 \(W,V\) 同时深等价，原两 scalar core
给 \(\beta^2=\lambda^2\)。由于两个输出核心独立且交换，得到
\[
 K_V\Phi=\Psi,\qquad K_V\Psi=\Phi.
\tag{15}
\]
这里只断言 \(K_{442}\) 在这两个实际来源上的作用，不把
whole \(\mathcal S_{442}\) 错写成一个反射。

设 \(\Phi_0=\Phi,\Phi_1=\Psi\)。全部双深度严格为
\[
 \boxed{\nu_{\Phi_i}|_{\{W\in p^n,\ V\in p^m\}}
 =\lambda^{n+m}[\kappa^n,\kappa^m]_*
       \nu_{\Phi_{\,i+n+m\pmod2}}.}
\tag{16}
\]
任意原输入事件都须同时转置。两状态的完整边际相同：
\[
 W_*\nu_{\Phi_i}=\nu_S,\qquad
 V_*\nu_{\Phi_i}=\nu_B,\quad
 B(z)=C(2z)\Theta(13z).
\tag{17}
\]
因此 \(B\) 质量为零、core 为 \(\lambda\)，但这里没有给它
赋一条已识别的秩二算术曲线。

对未反射的实际乘积 \(\Phi\)，原独立输入还给
\[
 \nu_\Phi|_{\{A\in p^n,D\in p^m\}}
 =\beta^{n+m}(T_A^nT_D^m)_*\nu_\Phi ,
\tag{18}
\]
\[
 \begin{aligned}
 T_A&=I+(\kappa-1)(1,2)^t(13,2)/17,\\
 T_D&=I+(\kappa-1)(2,-13)^t(2,-1)/17.
 \end{aligned}
\tag{19}
\]
(18) 不被未经证明地套给 \(\Psi\)。第一输出反射写回原输入是
\[
 T^{-1}\operatorname{diag}(-1,1)T
 =\frac1{17}\begin{pmatrix}-9&-52\\-4&9\end{pmatrix}.
\tag{20}
\]
所以保 \(V\) 的输出反射并不保原 \(A,D\) 的各自单位条件。

一个完整补域也可准确写出。令
\(\Gamma_n=\{W\in p^n\}\setminus\{A,D\in p^n\}\)，后一个域确实
包含在前者中，则 (16)、(18) 给整个测度身份
\[
 \boxed{(W/\kappa^n)_*
       ({\bf1}_{\Gamma_n}\nu_\Phi)
       =(\lambda^n-\lambda^{2n})\nu_S.}
\tag{21}
\]
(21) 保留整个差域，未把它拆成两个未支付的输入独立深度。
若 \(J_S'(0)=0\)，该完整 \(W\) 中央观察为零；这不等于
\(\Gamma_n\) 上的 \(A\) 中央观察为零。

## 4. 全 CM7 纤维与第一轴准确秩一投影

记 \(N_7=M_{\gamma_7}/\gamma_7\)，
\(\gamma_7=(5+\delta)/2\)，采用 R464 的完整 pull/trace 规范。
附脚本对以下全部基分别计算所有七点纤维：
\[
 \mathcal H_{26}^+
  =\sigma^{26}xK[X]_{\le4},\quad
 \mathcal H_2^+=K\Theta,\quad
 \mathcal H_{34}^+=\sigma^{34}x^2K[X]_{\le5}.
\tag{22}
\]
得到完整 \(5\times5,1\times1,6\times6\) 矩阵，并准确核得
\[
 N_7C=\omega C,\quad N_7\Theta=\omega\Theta,\quad
 N_7^{18}=I\ \hbox{在 }\mathcal H_{34}^+.
\tag{23}
\]
第一轴投影
\[
 \mathcal P_S=\frac1{18}\sum_{j=0}^{17}(-1)^jN_7^j\Pi_0
\tag{24}
\]
准确为 rank one，像是原 \(KS\)。这里 \(\Pi_0\) 是完整
\(\mu_6\) 平均，不是只取某些有限 Taylor 行。

在 (22) 的整个六维空间还有
\(N_{\bar\gamma_7}=N_{\gamma_7}^{-1}\)，精确矩阵乘积为一。
这亦是整个 \(\mathcal S_{34}\) 的真实 inverse：完整 Heisenberg
交织使两者乘积为一个标量，而非零原 \(S\) 锚定该标量为一。
以下只将这一事实用在原 \(\mathcal S_{34}\) 及其实际 CM 拉回上。

## 5. 实际伴随完全下降到 H5 的两个缩放

定义两个完整二变量来源
\[
 G_+(w,v)=\Theta(\gamma(w+2v))\Theta(2w-13v),\qquad
 G_-(w,v)=\Theta(\bar\gamma(w+2v))\Theta(2w-13v).
\tag{25}
\]
由 (4)，\(\Phi=(G_--G_+)/(336b\delta)\)。

在 \(G_+\) 中令 \(u=\gamma v\)，则
\[
 G_+(w,v)=H_+(w,\gamma v),\qquad
 H_+(w,u)=\Theta(\gamma w+2u)\Theta(2w-\bar\gamma u).
\tag{26}
\]
这是一个**实际 degree34/34 下降**，因为
\[
 B_+=\begin{pmatrix}\gamma&2\\2&-\bar\gamma\end{pmatrix},
 \quad B_+B_+^*=17I,\quad \det B_+=-17.
\tag{27}
\]
所有系数都在原 CM 整环中，交叉 Gaussian 精确为零，偶半特征
为标准。\(H_-\) 是将 \(\gamma,\bar\gamma\) 互换的同样来源。
没有从相同次数猜测下降或伴随。

\(\det B_\pm=-17\) 与 \(7\) 互素，所以完整双七点纤维在 (27)
下双射，全部 canonical 相位由 Gram 身份保持。由原两个
\(\Theta\) 的 (23)，
\[
 N_{7,w}N_{7,u}H_\pm=\omega^2H_\pm .
\tag{28}
\]
联合 \(\mu_6\) 类型为零，所以投到第一 principal 轴后，第二轴
也在 (22) 的 principal 六维空间。

第一轴取 \(N_7=-1\) 的 (24) 后，(28) 强迫第二轴特征为
\(-\omega^2\)。完整六维矩阵精确给这条特征线为 rank one，
其质量一生成元就是 R308 的实际秩零来源
\[
 \boxed{H_5=\sigma^{34}x^2
  (X^5+272bX^4-272b^2X^3-14912b^3X^2
            -6784b^4X+1024b^5).}
\tag{29}
\]
它对应 R308 的 \(y^2=x^3+17^5\) 参考，未换曲线或周期。
因此 (24) 在 \(H_\pm\) 上必为 \(S(w)H_5(u)\) 的标量倍。

该标量也已完整计算。将 (3) 乘 \(\Theta(2w)\) 的全部多项式，
再乘 (24) 的完整 \(6\times6\) 矩阵，得到
\[
 \mathcal P_S G_+(w,0)=168b(1-\delta)S(w),\qquad
 \mathcal P_S G_-(w,0)=168b(1+\delta)S(w).
\tag{30}
\]
一般 \(b\) 由原同次性恢复，系数恰为一次 \(b\)。
结合 (26)–(30) 得到完整张量身份
\[
 \boxed{\mathcal P_{S,W}\Phi
   =\mathcal P_{S,W}\Psi=S(W)\Lambda(V),}
\tag{31}
\]
\[
 \boxed{\Lambda(z)=
 \frac{(1+\delta)H_5(\bar\gamma z)
       -(1-\delta)H_5(\gamma z)}{2\delta}.}
\tag{32}
\]
\(\Psi\) 的投影相同，是因为 \(S\) 在第一轴反射下为偶。
这是整个伴随函数，而不只是它的质量或前几个矩。

特别
\[
 \Lambda(0)=1,\quad
 \nu_\Lambda|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_\Lambda,
 \quad J_\Lambda(0)=1-\lambda.
\tag{33}
\]
核心也可由 (15)、(31) 得到；(32) 则以两个原参考的单位尺度
再次给同一个实际来源解释。所有系数在当前位整。
\(\nu_\Lambda\) 和其单位限制的 Amice 常数分别为 \(1,1-\lambda\)，
所以二者都是原整测度卷积环中的单位。

## 6. 原条件行、伴随 transfer 与反卷积的真实测试

(23)、(27)、(28) 的完整纤维也将 (24) 转到伴随：
\[
 \boxed{\mathcal D_S\Phi=\mathcal D_S\Psi=S(W)\Lambda(V),\qquad
 \mathcal D_S=
 \frac1{18}\sum_{j=0}^{17}(-\omega^2)^j
       N_{\bar\gamma_7,V}^j\Pi_{0,V}.}
\tag{34}
\]
这里先在两个实际 \(H_\pm\in\mathcal S_{34}^{\otimes2}\) 上使用
(28) 与上一节已付的 inverse，再按 \(u=\gamma v,\bar\gamma v\)
拉回；这些拉回与完整 norm7 trace 交换，因为 \(13,7\) 互素。
故 (34) 不要求一个未经证明的 whole degree442 特征表。

若反证输入为原 \(J_S'(0)=0\)，则 \(J_S(0)=0\) 及 (31) 给任意
独立伴随连续测试 \(h(V)\) 的实际中央行
\[
 \int_{W\in\mathbf Z_p^\times}
       d_p\log\langle W\rangle h(V)\,
               d\nu_{\mathcal D_S\Phi}=0.
\tag{35}
\]
可用 (16) 保所有第一环带及实际伴随深度。若测试依赖 Mellin
参数，质量项也按 \(J_S(0)=0\) 在这个独立张量身份中消失；
没有对未投影来源或移动的 \(W\) 条件赋零。

由于 (32) 给真实整卷积逆，可以在第二轴反卷积 (31)。
其对原输入的转置必须保留：
\[
 A=(13W+2V)/17,\quad D=(2W-V)/17,\qquad
 V\mapsto V+t
 \Longrightarrow
 (A,D)\mapsto(A+2t/17,D-t/17).
\tag{36}
\]
因此 (11) 中的 \(A\) 单位条件及 \(\log\langle A\rangle\)，
在反卷积下都是随 \(t\) 移动的实际测试。不能由 (35) 把它们
当成一个只依赖 \(V\) 的独立条件。

为记录全部参考尺度，(32) 还直接给
\[
 \begin{aligned}
 J_\Lambda'(0)=J_{H_5}'(0)
 +\frac{d_p(1-\lambda)}{2\delta}
 \bigl((1+\delta)\log\langle\bar\gamma\rangle
       -(1-\delta)\log\langle\gamma\rangle\bigr).
 \end{aligned}
\tag{37}
\]
未知 \(J_{H_5}'(0)\) 没有因质量为一而被删去。

## 7. 第二边际的完整非齐次中央关系

记 \(G_\pm(z)=G_\pm(z,0)\)。实际函数恒等式为
\[
 G_--G_+=336b\delta\, S,\qquad G_\pm(0)=1.
\tag{38}
\]
它们位于标准 \(\mathcal S_{34}\) 且为偶，因此 whole
\(K_{34}=R\) 给 \(J_{G_\pm}(0)=1-\lambda\)。

交换两个相同 \(\Theta\) 因子，严格得到
\[
 \boxed{B(z)=
 \frac{G_+(\bar\gamma z)-G_-(\gamma z)}{336b\delta}.}
\tag{39}
\]
所以整个 Mellin 函数有
\[
 \boxed{
 J_B(u)+\langle\gamma\rangle^{d_pu}J_S(u)
 =\frac{\langle\bar\gamma\rangle^{d_pu}
        -\langle\gamma\rangle^{d_pu}}{336b\delta}J_{G_+}(u).}
\tag{40}
\]
\(J_S(0)=0\)，微分后准确为
\[
 \boxed{J_B'(0)+J_S'(0)=
 \frac{d_p\log\langle\bar\gamma/\gamma\rangle(1-\lambda)}
      {336b\delta}\ne0.}
\tag{41}
\]
这是两个实际边际之间的非齐次身份，非零理由与 (11) 完全相同。
(11)、(41) 还给
\[
 (1+\lambda)(J_B'(0)+J_S'(0))=(1-\lambda)J_C'(0).
\tag{42}
\]

原 \(J_S'(0)=0\) 会迫 \(J_B'(0)\ne0\)，但 \(B\) 是已经明说的
degree442 辅助来源，不是一条新识别的 rank-two 曲线。
同样，(32) 的显式参考伴随没有使 (36) 的混合单位条件消失。
下一接口是利用这些整个来源身份，在同一个原条件域中将 (41)
的非齐次项接回 (35)；本篇没有预付这一消元。

## 8. 精确证书与依赖

- [全部低 degree 来源、完整 CM7 纤维、两个 rank-one 投影及真实下降矩阵](../scripts/check-r490-degree26-factor-and-cm7.py)；
  [精确矩阵与系数](../scripts/check-r490-degree26-factor-and-cm7.json)。
- [R302：实际 degree2 参考及原周期](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)。
- [R308：原 H3/H5 的完整算术身份及 core](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)。
- [R416：原 ray 的完整 theta 核与中心相位](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R464：完整 CM 纤维的有限除子空间算法](R464-fixed-delta-division-source-full-arithmetic-projection-and-core.md)。
- [R466：真实 norm13 division 及固定来源规范](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R483：原 CM transfer 与完整单位条件](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。

