# 原 sigma 的完整 Hurwitz 高块与首 p 矩形的充分性

日期：2026-11-15。状态：**下述高块递推及唯一性已证明；没有证明 critical 或 primitive 共同非零。**

本记录核查一个具体的失败入口：先保留原 $p$-曲率，再把 R782 的双线性恒等式升到 $p^2$ 高块，是否会给 R788 首 $p\times p$ 矩形之外的独立支撑约束。答案是：对于这里同一个原完整加法核，所有高块已由该矩形唯一决定。不能把再次升块当作新的算术条件。

以下 $p=6N+5\ge41$、$\kappa=6B\ne0$，$B$ 始终是 R574/R702 的原单位。写
$$
F=x\sigma^6,\qquad G=-xy\sigma^6,
\qquad a_m=F^{(m)}(0),\quad b_m=G^{(m)}(0).
\tag{H1}
$$
这是**普通导数**，不同于先前 $f_i=[z^{6i+4}]F$、$g_i=[z^{6i+1}]G$。R697 证明所有 $a_m,b_m$ 在 $p$ 处整：在实际非零的两个 CM 类中，它们是原 $A_{m+1}$ 的二的幂倍；其他类严格为零。

## 1. 原六同源上的实际曲率和 tame 点值

使用 R697 §§4--5 已固定的、保 $dz$ 的原六同源
$$
\Lambda'=\Lambda+\mathbf Z\Omega/6,\qquad
\mathcal C_6=\langle\Omega/6\rangle.
$$
其坐标记为 $X,Y$，其完成化权二常数记为 $s$，以免和原 $x,y$ 混淆。R697 (697.19) 给
$$
X(P)=\sum_{T\in\mathcal C_6}x(P+T)
-\sum_{0\ne T\in\mathcal C_6}x(T).
\tag{H2}
$$
由于 $D^p=0$ 于原椭圆函数域，且 $D^{p-1}x=-B$，从这个原函数恒等式直接得到
$$
D^pX=D^pY=0,\qquad D^{p-1}X=-6B=-\kappa.
\tag{H3}
$$
不存在在这一步把同源方向或微分尺度置一的操作。

在 R697 的两个原初始 tame 点 $Q_+,Q_2$，令
$$
e_Q=\zeta_{\Lambda'}(Q)-sQ-\overline Q/\mathcal A'.
$$
原 zeta 六同源公式，连同 $\mathcal A'=\mathcal A/6$，给
$$
e_Q=\sum_{T\in\mathcal C_6}E^*_{1,\Lambda}(Q+T)
-\sum_{0\ne T\in\mathcal C_6}E^*_{1,\Lambda}(T).
\tag{H4}
$$
第二个和为零：$T$ 与 $-T$ 抵消，非零二挠点的 completed zeta 值为零。这里的 $Q$ 以 R697 原复坐标选取；$Q+T$ 全是素于 $p$ 的原 tame 挠点。应用 R574 的原恒等式
$E^*_{1,\Lambda}(R)^p=D^{p-2}x(R)$，再用特征 $p$ 的 Frobenius 与 (H2)，得到
$$
\boxed{e_Q^p=D^{p-2}X(Q).}
\tag{H5}
$$
(H4) 中的 $sQ$ 正是 R697 Gaussian 所保留的项；不能省去 $s$ 后仍使用 (H5)。所有相关点值及原 Bell 初始数据在 $p$ 处整，见 R697 (697.18)、(697.21)、(697.23)。

## 2. Jacobson 公式在原 Bell 代数中的准确应用

在特征 $p$ 多项式扩展 $k(E')[e]$ 上取
$$
DX=2Y,\quad DY=3X^2+a,\quad De=-X-s,
\qquad \mathscr D=D+e.
\tag{H6}
$$
$e$ 此处是扩展变量，不是把完整非整 sigma 或 zeta Taylor 级数强行约化所得的元素。由 (H3)，
$$
D^p=\kappa\partial_e.
\tag{H7}
$$
对任意导子 $D$ 和乘法算子 $e$，特征 $p$ 中
$$
(D+e)^p=D^p+e^p+D^{p-1}e.
\tag{H8}
$$
一个直接证明是：左边与 $D^p$ 的差和所有乘法算子交换，因此本身是乘法算子；其作用于 $1$ 的值为第 $p$ 个完整 Bell 多项式。按 $\sum j m_j=p$ 的分拆展开，除 $m_1=p$ 或 $m_p=1$ 两项外，各系数
$p!/(\prod m_j!(j!)^{m_j})$ 都被 $p$ 整除。留下的正是 $e^p+D^{p-1}e$。

置
$$
W'=e^p-D^{p-2}X.
$$
(H6)--(H8) 给
$$
\boxed{\mathscr D^p=\kappa\partial_e+W',
\qquad DW'=\kappa,\quad\partial_eW'=0.}
\tag{H9}
$$
特别 $W'$ 沿 $D$ 不是常数，更不能在整个扩展中设为零；(H5) 只说明在原指定点求值时 $W'(Q,e_Q)=0$。

令 $\mathcal B_m=\mathscr D^m1$。因 $[\partial_e,\mathscr D]=1$，
$$
\partial_e\mathcal B_n=n\mathcal B_{n-1}.
\tag{H10}
$$
这里 $\mathcal B_{-1}=0$。于是对于**每个**整数 $n\ge0$，先在扩展代数中使用 (H9)，然后才在原点值求值，可得
$$
\mathcal B_{p+n}(Q,e_Q)
=\kappa n\mathcal B_{n-1}(Q,e_Q).
\tag{H11}
$$
这既没有对 $n!$ 除 $p$，也没有把 $W'=0$ 当成 $D$ 稳定的商关系。

R697 的原 theta 导数归一把 $F$ 支（$m\equiv4\bmod6$）识别为 $24\mathcal B_m(Q_+,0)/f_4^+$，把 $G$ 支（$m\equiv1\bmod6$）识别为 $\mathcal B_m(Q_2,e_2)/f_1$；两个分母都已证明是 $p$ 单位。由于 $p+1$ 被六整除，(H11) 保持这两条 CM 类；其余类两边均为零。故
$$
\boxed{
 a_{p+n}=\kappa n a_{n-1},\qquad
 b_{p+n}=\kappa n b_{n-1}\quad\text{于 }\mathbf F_p,
 \quad n\ge0.
}
\tag{H12}
$$
对 $1\le n\le p-1$，这准确复现 R702 (702.17) 的原首 pole 块；这里的证明将其扩到所有普通导数阶。

## 3. 高块的完整三角公式：没有新的自由种子

任取满足 (H12) 的序列 $c_m$，写 $m=qp+r$、$0\le r<p$。逐次减去 $p+1$ 得
$$
\boxed{
 c_{qp+r}=
 \begin{cases}
 \kappa^q(r)_q\,c_{r-q},&q\le r,\\
 0,&q>r,
 \end{cases}
}
\tag{H13}
$$
其中 $(r)_q=r(r-1)\cdots(r-q+1)$。若 $q>r$，在递推到种子区之前必遇到乘数零；这包括全部 $m\ge p^2$。
因此完整序列由 $c_0,\ldots,c_{p-1}$ 唯一决定。高处的已知单位都来自这些低处种子，并不是一个可以倒推未知 critical 项的新条件。

尤其不能把原 theta 的 $\mathcal B_0=1$ 误放到投影后的 $F$ 或 $G$ 上：后两者的第零普通导数均为零，其已知单位种子分别在阶四和阶一。R702 的两个移位单位正来自这两个种子。

也可从 (H9) 直接看出
$$
\mathscr D^{p^2}=(W')^p,
\tag{H14}
$$
因为 $\partial_e$ 与 $W'$ 交换且 $\partial_e^p=0$。在原点求值 $(W')^p=0$，与 (H13) 一致。稳定的是中心条件 $(W')^p=0$，不是 $W'=0$。

## 4. 正确的系数环：Hurwitz 级数而非普通 Taylor 约化

记 $\mathscr H(k)$ 为 Hurwitz 级数环，具有形式基 $\gamma_m(z)$，乘法及导子为
$$
\gamma_i\gamma_j=\binom{i+j}{i}\gamma_{i+j},
\qquad D\gamma_m=\gamma_{m-1},\qquad z=\gamma_1.
\tag{H15}
$$
$\gamma_m$ 可记作 $z^m/m!$，但在特征 $p$ 这只是记号，并不执行不可逆阶乘的除法。原普通导数在此给合法元素
$$
\mathbf F=\sum a_m\gamma_m,\qquad
\mathbf G=\sum b_m\gamma_m.
$$
(H12) 等价于
$$
D^p\mathbf F=\kappa z\mathbf F,\qquad
D^p\mathbf G=\kappa z\mathbf G.
\tag{H16}
$$
一般地，$D^pH=\lambda zH$ 的解空间由前 $p$ 个 Hurwitz 系数唯一参数化。这个断言对任意 $\lambda\in k$ 都成立；证明就是同一逐项递推，不依赖对无限普通 Taylor 级数的约化。

## 5. 原完整双变量核由首 p×p 矩形唯一决定

Hurwitz 代入使用
$$
\gamma_n(z+t)=\sum_{i+j=n}\gamma_i(z)\gamma_j(t),
$$
并定义同一原核
$$
\mathbf K(z,t)=\mathbf F(z+t)\mathbf G(z-t).
$$
特征 $p$ 下 $D^p$ 对乘法仍是导子。由 (H16)，分别沿 $z,t$ 微分得
$$
\boxed{
D_z^p\mathbf K=2\kappa z\mathbf K,
\qquad D_t^p\mathbf K=2\kappa t\mathbf K.
}
\tag{H17}
$$
第二式保留 $p$ 为奇数所产生的负号：两项是
$\kappa(z+t)\mathbf K-\kappa(z-t)\mathbf K$。

所以 (H17) 的全部解由
$$
[\gamma_a(z)\gamma_b(t)]\mathbf K,\qquad0\le a,b<p
\tag{H18}
$$
唯一决定：先对每列递推 $a$，再对每行递推 $b$，两递推交换。
首矩形中的普通多项式系数 $M_{ab}$ 与 (H18) 相差 $a!b!$；这里两个阶乘都是单位。因此 R788 的首 $p\times p$ 矩形及其 $\Phi_p$ 修正，正是 (H18) 的同一输入，而不是另一个截断。

R784 的六原截面也分别满足 $D^pS=2\kappa zS$。不必再猜一个度十二同源的规范来证明：首六列的原 $6\times6$ 子式行列式为 $36$，Hurwitz 换基只再乘单位阶乘，所以可把这六截面逐个写成 $\mathbf K$ 首六列的单位线性组合；(H17) 立即给断言及其 Hurwitz 整性。

因而三 wedge 表达的右边和 $\mathbf K$ 满足同一个双变量系统。它们在首矩形一致，就在所有 Hurwitz 系数上一致。

**精确边界。** 在原 R788 全部首矩形等式已经保留之后，再查看这个同一加法恒等式的更高 pole 块、$p^2$ 块或更高 Hirota 阶，不产生独立矩阵条件。例如 $t$ 方向的高阶导数恒按
$$
\left.D_t^{p+n}\mathbf K\right|_{t=0}
=2\kappa n\left.D_t^{n-1}\mathbf K\right|_{t=0}
\tag{H19}
$$
归回较低列，而各列的高 $z$ 系数也由 (H17) 唯一延拓。把 D12 恒等式反复升块以求出额外可消高带的方程，不能越过这一唯一性。

这不排除利用原曲线的其他独立几何关系，也不声称首矩形条件对任意种子都自动成立。R788 的秩六和完整 Schur 约束是实质条件；本记录只是证明同一个核在更高层重复它们不会增强这些条件。

### 5.1 首矩形的修正恰是 Hurwitz 加法余项

这一唯一性还有一个显式版本，直接复现 R788 的原系数与符号。
在 Hurwitz 环的前两个基 $p$ 数位中置
$$
z_0=\gamma_1(z),\qquad z_1=\gamma_p(z).
$$
它们生成 $k[z_0,z_1]/(z_0^p,z_1^p)$，且 $D^p=\partial_{z_1}$。
于是 (H16) 的全部解可唯一写成
$$
\mathbf F=\exp_{<p}(\kappa z_0z_1)P(z_0),\qquad
P(z_0)=\sum_{m=0}^{p-1}\frac{a_m}{m!}z_0^m,
\tag{H20}
$$
其中 $\exp_{<p}(u)=\sum_{j=0}^{p-1}u^j/j!$；$G$ 使用同一个规范及 $Q$。
验证 (H20) 时，指数导数最后缺少的项含 $z_0^p$，所以恰为零。
这也逐项给出 (H13)。此处只有 $m<p$ 的可逆阶乘。

在加法 $z\mapsto z\pm t$ 下，第一个数位照常相加，第二个数位为
$$
\gamma_p(z+t)=z_1+t_1+C_+(z_0,t_0),\qquad
\gamma_p(z-t)=z_1-t_1+C_-(z_0,t_0),
$$
$$
C_+(z,t)=\sum_{r=1}^{p-1}\frac{z^{p-r}t^r}{(p-r)!r!},
\qquad C_-(z,t)=C_+(z,-t).
\tag{H21}
$$
把完整核投到首矩形就是令 $z_1=t_1=0$；注意 (H21) 的混合余项仍然存在。
两个指数参数 $\kappa(z\pm t)C_\pm$ 的总次数为 $p+1$，
其任意两个之积在 $k[z,t]/(z^p,t^p)$ 中都为零。因此只在这个首矩形内，
指数乘积准确化为
$$
1+\kappa\{(z+t)C_+(z,t)+(z-t)C_-(z,t)\}.
$$
Wilson 定理给 $1/((p-r)!r!)=(-1)^r/r$。奇数 $r$ 的项及边界 $r=1,p$ 抵消，
偶数 $2\le r\le p-1$ 的系数则是
$2/r-2/(r-1)=-2/(r(r-1))$。于是首矩形正是
$$
\left(1-2\kappa\sum_{\substack{2\le r\le p-1\\r\ \mathrm{even}}}
\frac{z^{p+1-r}t^r}{r(r-1)}\right)P(z+t)Q(z-t),
\tag{H22}
$$
逐字复现 R788 的 $\Phi_p$。这说明首 pole 的跨 $p$ 修正与原 Bell 曲率是同一来源。
完整秩六仍是原六截面的额外几何信息；(H20)--(H22) 并未宣称任意 $P,Q$ 都有秩六。
也没有在一般多变量截断环里滥用 $\exp_{<p}(A+B)=\exp_{<p}(A)\exp_{<p}(B)$；
上面的相乘只依赖所显示的参数两两乘积为零。

## 6. 留下的同标签问题

原 critical 量仍是
$$
f_i g_{N-1-i},\quad0\le i<N,
$$
以及真正筛
$$
\mathbf1_{\gcd(6i+7,p+1)=1}P_{6i+6}(1/\varsigma),\qquad\varsigma^2=-3.
$$
这里 $\varsigma$ 是原 Legendre 规范的根，与 §1 的完成化权二常数 $s$ 不同。
(H12)--(H19) 没有迫这些种子乘积的任一项非零，更没有允许把不同本原标签的单位拼接。未筛全零推出的六零行仍仅是 R788 的必要后果。后续必须在首矩形中使用原函数额外结构，或找到独立的原 Cartier/几何配对；这里不以已知高阶单位替代未知种子。

## 依赖

- [R574](../results/R574-completed-zeta-Cartier-input.md)：原 $D^p=0$、$D^{p-1}x=-B$ 及全部 prime-to-$p$ tame 点的 completed-zeta 恒等式。
- [R697](../results/R697-original-sigma-six-sections-and-integral-square-roots.md)，§§4--6：原六同源、Gaussian 常数 $s$、两个原点值、全部普通导数的整性及单位归一。
- [R702](../results/R702-first-pole-block-and-uniform-shifted-units.md)：首 pole 块与原规范；(H12) 在其原范围逐项一致。
- [R784](../results/R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md)：同一个完整加法核及原六截面。
- [R788](../results/R788-original-cross-p-Cartier-correction-and-rank-six-coupling.md)：准确首矩形、$\Phi_p$ 与单位低子式。

