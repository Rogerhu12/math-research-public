# R308 — 两个实际秩零参考的完整 p-core、中央质量与全部尺度项

日期：2026-11-13。**状态：以下普通全测度恒等式、各自 Euler 因子、全部 tame/环带、质量补偿及惰性原解析参考均已证明。它们支付 R307 一阶连接所需的真实参考数据，不给未证明的参考中央导数赋值。**

沿用 R306–307，令
\[
 E_k:y^2=x^3+17^k,\qquad k=1,3,5,\qquad
 r_k=17^{(k-1)/6},\quad r_1=1 .
\]
目标是精确秩二的 \(E_1\)；本篇的两个参考是 \(E_3,E_5\)。
本篇的下标 \(1\) 指 \(b=17\)，区别于 R302 的 \(b=1\) 基曲线。

## 1. 同一个实际 sigma frame 及原始周期

在共同 \(E_1:y^2=x^3+b,\ b=17\) frame 中置 \(X=x^3\)，
\[
 \begin{split}
 P_3(X)&=X^5-208bX^4+400b^2X^3+8128b^3X^2
                      +12032b^4X-2048b^5,\\
 P_5(X)&=X^5+272bX^4-272b^2X^3-14912b^3X^2
                      -6784b^4X+1024b^5,\\
 H_k(z)&=\sigma(z)^{34}x(z)^2P_k(x(z)^3)
                          =\sum_{m\ge0}h_{k,m}z^m .
 \end{split}                                               \tag{1}
\]
两条来源均满足 \(H_k(0)=1\)，并在全部 \(\mu_6\) 缩放下不变。
它们是 R306 的实际原 Schwartz 来源，经 R307 完整 CM13
识别的质量一规范，不是任意两个全纯截面。

若写到各自曲线的微分下，其真正来源及周期是
\[
 \widetilde H_k(z)=H_k(r_kz),\qquad
 \Omega_{\infty,k}=\Omega_{\infty,1}/r_k .                 \tag{2}
\]
R307 的原 Kronecker 求和准确给
\[
 \frac{L(E_3,1)}{\Omega_{\infty,3}}=3,\qquad
 \frac{L(E_5,1)}{\Omega_{\infty,5}}=6.                     \tag{3}
\]
记 \(\kappa_3=3,\ \kappa_5=6,\ s=(1-\omega)^{-1}\)，
\(\varpi_k=s\Omega_{\infty,k}\)。其完整 CM 全权公式为
\[
 \frac{(2\pi/\sqrt3)^mL(\psi_k^{2m+1},m+1)}
       {m!\varpi_k^{2m+1}}
   =\kappa_k(1-\omega)34^{-m}(r_k^m h_{k,m})^2,
       \qquad 6\mid m.                                  \tag{4}
\]
这里 \(\psi_k\) 是各自的实际 Hecke 角色，不能统一换成 \(\psi_1\)。

## 2. 普通原参数与整测度

固定 \(p>7,\ p\equiv1\pmod3\)，选择同一个普通嵌入，写
\[
 \pi=\psi_1(\mathfrak p),\quad \bar\pi=\psi_1(\bar{\mathfrak p}),
 \qquad v_p(\pi)=1,\quad v_p(\bar\pi)=0,\quad\pi\bar\pi=p.
\]
六次扭曲的比值给
\[
 c_k=\frac{\psi_k(\mathfrak p)}{\psi_1(\mathfrak p)}
       \in\mu_3,\qquad
 \pi_k=c_k\pi,\quad \bar\pi_k=c_k^{-1}\bar\pi.             \tag{5}
\]
这些是当前位中确定的根单位，\(c_3,c_5\) 一般不等于一。
全部有限相位依 R306，不取任意范数 \(p\) 生成元。

取 R295 的同一个整正式参数
\(\beta_1:\widehat{\mathbf G}_m\to\widehat E_1\)，周期为 \(\Omega_p\)。
在容纳 \(r_k\) 的未分歧整扩张上，实际同构
\(F_{r_k}:E_1\to E_k\) 给
\(\beta_k=F_{r_k}\beta_1\)，所以
\[
 \Omega_{p,k}=\Omega_p/r_k,\qquad
 \widetilde H_k(\Omega_{p,k}\log(1+Z))
             =H_k(\Omega_p\log(1+Z)).                   \tag{6}
\]
这是真正的整形式群同构；没有对 \(\mathbf Z_p\) 上的测度擅作
一个不在 \(\mathbf Z_p^\times\) 内的系数缩放。

R295 的 CM sigma 唯一性及 R300 的完整 \(34\) 维整格适用于 (1)，故
\[
 \mathcal A_{H_k}(Z)=H_k(\Omega_p\log(1+Z))
       =\int_{\mathbf Z_p}(1+Z)^x\,d\nu_k(x)              \tag{7}
\]
是整 Amice 测度。特别
\[
 \nu_k(\mathbf Z_p)=1,\qquad
 M_{k,m}:=\int x^m\,d\nu_k=\Omega_p^m m!h_{k,m}.            \tag{8}
\]
系数可取在同一完整未分歧整环中；以下公式中的
\(\pi,\bar\pi,c_k\) 都在固定普通嵌入的 \(\mathbf Q_p\) 中。

## 3. 完整 p-core 的准确标量

令 \([a]_*\) 表示变量乘 \(a\) 的推前，并记
\[
 \psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbf Z_p}),\qquad
 T_p=\bar\pi[\bar\pi^2]_*\psi_p,\qquad
 \varkappa=p/\bar\pi^2,\qquad b_k=c_k/\bar\pi.             \tag{9}
\]

**定理 1。** 两个原参考的完整测度满足
\[
 \boxed{T_p\nu_k=c_k\nu_k,\qquad
 \nu_k|_{p\mathbf Z_p}=b_k[\varkappa]_*\nu_k.}             \tag{10}
\]
故对每个整数 \(m\ge0\)，
\[
 \boxed{
 \int_{\mathbf Z_p^\times}x^m\,d\nu_k
   =\left(1-c_k\frac{\pi^m}{\bar\pi^{m+1}}\right)
                       \Omega_p^m m!h_{k,m}.}           \tag{11}
\]
对 \(6\mid m\)，括号准确等于
\(1-\pi_k^m/\bar\pi_k^{m+1}\)。其余 \(m\) 的两侧均为零。
式 (11) 包括原点质量，且是由全测度等式推出，而非只由 principal
正权猜测符号。
同一个实际 p-depletion 是
\[H_k^\times(z)=H_k(z)-b_k H_k(\varkappa z).\]

### 3.1 先付真实标量性及整性

R300 在完整空间
\[
 \sigma^{34}L(34O),\qquad
 \mathcal H=\operatorname{span}
             \{\sigma^{34}x^{2+3j}:0\le j\le5\}
\]
上已证明实际整算子
\[
 T_p=\frac{\bar\pi}{p}\mathscr M_\pi,\qquad
 \mathscr M_a(\sigma^{34}f)
   =\sigma^{34}\operatorname{Tr}_{[a]}
       \left[(r_{\bar a}/r_a)^{34}f\circ[\bar a]\right].  \tag{12}
\]
这里 \(r_a=\sigma(az)/\sigma(z)^{Na}\)，保首项常数及全部 Heisenberg
中心。完整根单位平均支付了 \(1/p\)，整个整 theta 格保持。

R307 的原 \(\mathscr M_\gamma\)（\(\gamma=4+\omega\)）本征值是
\[
 H_3:\ -\gamma\omega^2,\qquad H_5:\ -\gamma\omega .
\]
它们在完整六维块中都单重，因为其特征多项式为
\[
 (X^3+\gamma^3)(X^3+\omega^2\gamma^3).
\]
在这三个第一因子的根处，导数范数均为 \(27\cdot13^5\)。
当 \(p\ne13\) 时，R300 的真实互素双纤维交换证明给
\(\mathscr M_\pi\mathscr M_\gamma
 =\mathscr M_\gamma\mathscr M_\pi\)。
所以存在 \(d_k\) 使 \(T_pH_k=d_kH_k\)。
完整整格及 \(H_k(0)=1\) 直接给 \(d_k\) 整。
到此还未认定 \(d_k=c_k\)。

### 3.2 各自 Katz 插值与独立平方确定标量

令 \(G_k(T)\) 为 (7) 在单位区间的 principal Mellin，设
\(t_m=(1+p)^m-1,\ e_m=\pi^m/\bar\pi^{m+1}\)。
R295 同一个 Katz 正权插值定理用于实际 \(E_k\)，(4)、(6) 给
\[
 \mathcal K_k(t_m)
 =\frac{\kappa_k}{r_k}(1-\omega)\Omega_p
               34^{-m}(1-c_ke_m)^2M_{k,m}^2,
 \qquad m>0,\quad p-1\mid m.                            \tag{13}
\]
两侧的 \(m!\) 都已保留在 \(M_{k,m}\) 中。
(13) 的 Euler 使用 \(\pi_k,\bar\pi_k\)，而不是目标曲线的角色。

不预设 (10)，只用整测度中非单位矩赋值至少 \(m\)，以及正权
\(m_n=m_0+(p-1)p^n\) 同时满足实值趋于无穷、\(p\) 进趋于 \(m_0\)，
R295 的密集权论证逐字给
\[
 \mathcal K_k(T)
 =\frac{\kappa_k}{r_k}(1-\omega)\Omega_p
       (1+T)^{-\log_p\langle34\rangle/\log_p(1+p)}
                                      G_k(T)^2 .        \tag{14}
\]
(14) 的证明只用 (7)、(13)，没有使用所求 p-core。
特别，在正权处
\[
 G_k(t_m)^2=(1-c_ke_m)^2M_{k,m}^2.                        \tag{15}
\]

另一方面，已经付清的 \(T_pH_k=d_kH_k\) 给
\(G_k(t_m)=(1-d_ke_m)M_{k,m}\)。
\(\mathcal K_k\) 非零：例如其中心原插值由 (3) 及非零
\(1-\bar\pi_k^{-1}\) 给非零值。故 (14) 给 \(G_k\ne0\)，可在
趋于中心的正权序列中选 \(M_{k,m}\ne0\)。
在该权代入 (15)，得
\[
 (d_k-c_k)e_m\bigl(2-(d_k+c_k)e_m\bigr)=0 .
\]
\(d_k,c_k\) 均整，\(v_p(e_m)=m>0\)，最后因子是单位，
所以 \(d_k=c_k\)。这同时支付了平方根的符号，不允许逐权另选。

当 \(p=13\) 时，R300 的原相位给 \(\pi=-\gamma\)，
R306 给 \(\pi_3=-\gamma\omega^2,\ \pi_5=-\gamma\omega\)；
偶性使 \(\mathscr M_{-\gamma}=\mathscr M_\gamma\)。
(12) 遂直接给 \(d_3=\omega^2=c_3,\ d_5=\omega=c_5\)。
共轭普通嵌入同理。因此 (10) 对全部所述普通素数成立。

## 4. 参考质量、全部环带以及归一导数

由 (8)、(10) 有
\[
 \boxed{
 \nu_k(p^n\mathbf Z_p)=b_k^n,\qquad
 \nu_k(p^n\mathbf Z_p^\times)=b_k^n(1-b_k),\qquad
 G_k(0)=1-b_k=1-\bar\pi_k^{-1}.}                         \tag{16}
\]
因为 \(N\bar\pi_k=p\ne1\)，中心质量在特征零中总非零。
但积分性还须区别两个参考。

\(E_3\) 有真实有理二挠点 \((-17,0)\)。所以对每个当前 \(p\)，
\(\#E_3(\mathbf F_p)\) 为偶数，\(a_p(E_3)\) 为偶数。
当 \(p>7\) 时 Hasse 界排除除 \(a_p=1\) 外的
\(a_p\equiv1\pmod p\) 可能性；偶性又排除 \(a_p=1\)。
因此
\[
 \boxed{G_3(0)\in\mathcal O^\times
             \quad\text{对全部当前普通 }p>7.}           \tag{17}
\]
没有额外加入“非异常”假设。

对 \(E_5\)，同一范数恒等式给
\[
 \begin{split}
 N(1-\bar\pi_5)&=\#E_5(\mathbf F_p),\\
 v_pG_5(0)&=
 \begin{cases}
 1,&a_p(E_5)=1,\\
 0,&a_p(E_5)\ne1 .
 \end{cases}                                            \tag{18}
 \end{split}
\]
因 \(1-\pi_5\) 为单位，且 Hasse 界使群阶的正 \(p\) 倍只能为 \(p\)，
(18) 准确保留可能的一个 \(p\) 损失。

对每个 \(j\in\mathbf Z/(p-1)\)、\(u\in\mathbf Z_p\)，定义
\[
 \begin{split}
 \mathcal M_{k,j}(u)
 &=\int_{\mathbf Z_p^\times}\tau(x)^j\langle x\rangle^u\,d\nu_k,\\
 \mathcal M_{k,j}^{[n]}(u)
 &=\int_{p^n\mathbf Z_p^\times}
             \tau(x/p^n)^j\langle x/p^n\rangle^u\,d\nu_k .
 \end{split}
\]
完整测度式给
\[
 \boxed{
 \mathcal M_{k,j}^{[n]}(u)
  =b_k^n\tau(\bar\pi)^{-2nj}
            \langle\bar\pi\rangle^{-2nu}\mathcal M_{k,j}(u).} \tag{19}
\]
当 \(6\nmid j\) 时，原 \(\mu_6\) 对称使两侧恒为零。
其余分支的中心导数必须保留
\[
 \boxed{
 \mathcal M_{k,j}^{[n]\prime}(0)
 =b_k^n\tau(\bar\pi)^{-2nj}
   \bigl(\mathcal M_{k,j}'(0)
       -2n\log_p\bar\pi\,\mathcal M_{k,j}(0)\bigr).}       \tag{20}
\]
特别，两参考的 principal 质量非零，(20) 的第二项不能删除。
目标 \(S\) 的对应质量为零，正是 R300 中那一项消失的原因。

在质量非零的 principal 分支记
\[
 \ell_k=\mathcal M_{k,0}'(0)/\mathcal M_{k,0}(0).
\]
则 \(\ell_k^{[n]}=\ell_k-2n\log_p\bar\pi\)。
这只比较同一个未定斜率在各环带的变化；并没有确定 \(\ell_k\) 本身。
若采用变量 \(u\mapsto(p-1)u\)，对数项亦须乘 \(p-1\)。

另外，若真正允许的坐标缩放是 \(a\in\mathbf Z_p^\times\)，
\[
 \mathcal M_{[a]_*\nu,j}(u)
       =\tau(a)^j\langle a\rangle^u\mathcal M_{\nu,j}(u),
\]
因此它的中心导数增加
\(\log_p\langle a\rangle\) 乘中心质量。
(2)、(6) 中实际周期已相互抵消；不可在别处遗漏这类尺度项，
也不可把一个不在 \(\mathbf Z_p^\times\) 中的 \(r_k\)
擅当作 \(\mathbf Z_p\) 的坐标自同构。

## 5. 非零质量的完整收敛重构

目标 \(S\) 的单位环带级数在 R300 中利用总质量零直接收敛。
两个参考总质量为一，不能照抄那一条未补偿的无穷和。

令 \(\nu_k^\times=\nu_k|_{\mathbf Z_p^\times}\)、\(m_k=1-b_k\)，
\(\delta_0\) 为原点 Dirac 测度。准确的完整式为
\[
 \boxed{
 \nu_k=\delta_0+\sum_{n\ge0}b_k^n[\varkappa^n]_*
                     \bigl(\nu_k^\times-m_k\delta_0\bigr).} \tag{21}
\]
这里括号总质量为零，级数按对每个连续函数积分的意义收敛。
它是明确的质量补偿公式，不声称原测度本来就有质量一的原点原子。

证明先在有限 \(N\) 使用 (10)：
\[
 \nu_k=\sum_{n=0}^{N-1}b_k^n[\varkappa^n]_*\nu_k^\times
                     +b_k^N[\varkappa^N]_*\nu_k .
\]
多项式恒等式
\((1-b_k)\sum_{n=0}^{N-1}b_k^n=1-b_k^N\) 给 (21) 的有限和，
余项准确为
\[
 b_k^N[\varkappa^N]_*(\nu_k-\delta_0).
\]
对任意连续 \(f\)，其积分的绝对值由
\(\sup_x|f(\varkappa^Nx)-f(0)|\) 乘固定测度范数控制，趋于零。
这证明 (21)，同时没有要求不成立的 \(b_k^N\to0\)。

## 6. 惰性时真正的质量一解析参考

现在固定 \(p\ge11,\ p\equiv5\pmod6,\ p\ne17,\ d=p+1\)。
把 (1) 齐次缩回 \(y^2=x^3+1\)，令 \(H_k^\circ\) 表示
同一个多项式取 \(b=1\) 的来源，\(H_k^\circ(0)=1\)。
准确尺度是
\[
 H_k(z)=H_k^\circ(17^{1/6}z).
\]
若同时使用共同曲线的首分母 \(c_{17}=17^{d/6}c_1\)，则其 \(h\) 次缩放与 \([z^{dh}]\) 的缩放完全抵消，所得原 Newton 函数与下面的 \(b=1\) 函数相同。若只比较系数而不换 \(c\)，则只能先使用单位赋值，不能把残留根单位幂无证延拓为解析函数。

令 \(c=[z^d]\log(\sigma/z)\) 如 R301，定义
\[
 G_k^\circ(z)=H_k^\circ(z)e^{-34cz^d},\qquad
 J_{k,p}^\circ(u)
   =\sum_{h\ge0}[z^{dh}]G_k^\circ\,(34c)^{-h}(u)_h.       \tag{22}
\]
R301 的同一个半径 \(R=p^{-1/(2p)}\) 上，
\(z^2x\) 整且范数至多一，余下 sigma 指数可收敛取值。
(1) 的每一单项在 \(O\) 阶非负，系数整，所以
\[
 \|G_k^\circ\|_R\le1,\qquad
 v_p\bigl([z^{dh}]G_k^\circ(34c)^{-h}\bigr)
          \ge\left\lceil\frac{h(p-1)}{2p}\right\rceil
              \quad(h\ge1).
\]
因此
\[
 \boxed{
 J_{k,p}^\circ\in1+p\mathbf Z_p\langle u\rangle,\qquad
 J_{k,p}^\circ(n)=n!(34c)^{-n}[z^{dn}]H_k^\circ,\qquad
 v_p([z^{dn}]H_k^\circ)=-n-v_p(n!)}                    \tag{23}
\]
对每个整数 \(n\ge0\) 成立。
这给 R307 两实际参考在整个同支正权序列上的准确赋值，
而不仅是复中央值非零。

但 (23) 只使其中心值为一、导数属于 \(p\mathbf Z_p\)；
它不计算导数。反圆分的对偶后共轭功能方程逐点固定原角色，
没有由此得到 \(u\mapsto-u\) 的奇偶性。
原一阶连接转置时，两个参考的完整导数仍须保留。

## 7. 当前可直接使用的输入

R307 的实际一阶关系可现在使用以下已付数据：
共同整 Amice frame、各自 \(c_k\) 及单 Euler、完整非零质量、
全部 tame/环带的尺度导数、普通 \(H_3\) 的单位质量，
以及惰性两个原解析参考为单位。原点质量一和中央复值 \(3,6\)
不自动确定其中任何一个 Mellin 斜率。

本篇不改变完成标准；仍须证明原秩二来源的中央导数在无穷多个
素数上非零。所有统一证明都由真实迹、整格、原插值及解析界完成，
没有以目标素数样本代替。

### 依赖

- [R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)：普通原 sigma、Katz 规范及密集正权平方证明。
- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)：完整 \(34\) 维真实迹、整 p-core、CM13 单重性和全 Heisenberg 相位。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：惰性 sigma 首分母与实际余项圆盘。
- [R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)：三个真实 Hecke 角色、局部向量、范数、周期及 CM13 相位。
- [R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)：两原多项式、质量一规范、准确中央常数 \(3,6\) 与全部权。

