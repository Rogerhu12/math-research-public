# R1018：原 CM 点差的完整最早形式层与精确深度

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：对 \(p>37,\ p\equiv11\pmod{12}\)，原
\((p-1)D_0\) 在原良好约化 Jacobian 的形式群中，准确深度为
\(m=(p-1)/2\)，相对于 \(\pi_0^{(p^2-1)/2}=p\)。**
证明使用整个 compact-type 模型的惯性权，以及同一个原 Igusa
主化函数的真实 quotient-isogeny 提升。原 \(a=0\) 参考尾的首类
是一个系数为单位的 Weierstrass gap，因而非零。

这是实际形式点的首层定理，**尚不是形式对数的首层定理**，
也没有声称 R1011 指定半秩商的整投影保留该类。完整 \(p\) 对数项、
实际投影和原候选排除继续开放。

## 1. 原对象、底环和结论

全部保持 R1014：
\[
X_1=\operatorname{Norm}\bigl(
 X_{\rm ns}^+(p)\times_{\mathbf P^1_j}\mathbf P^1_a\bigr),
\quad j=6912a^3(1-a^3),\quad
D_0=2[c_1]-[c_\zeta]-[c_{\zeta^2}].
\tag{1018.1}
\]
取 \(K_{\rm ur}=\widehat{\mathbf Q_p^{\rm ur}}\)，剩余域
\(k=\overline{\mathbf F}_p\)。置
\[
e_0=(p^2-1)/2,\quad \pi_0^{e_0}=p,\quad
R=O_{K_{\rm ur}}[\pi_0],\quad
m=(p-1)/2,\quad h=(p+1)/4,\quad g=(p+1)/12.
\tag{1018.2}
\]
在 full-\(p\) 图上可再取 \(\varpi^2=\pi_0\)，
\(\varpi^{p^2-1}=p\)。
原 Jacobian \(J_1\) 在 \(R\) 上有好模型 \(\mathcal J\)：
这是 R1014 的 compact-type 模型，节点的 tame 商只须正则化有理链，
无需为 Jacobian 加入新的有效惯性。亦可在 full-\(p\) 扩张上检查：
\(u=-1\) 对全部分量和树形图都作用平凡，故对全部
\(\ell\ne p\) 的 Tate 模作用平凡，良好约化下降到 (1018.2)。

定义
\[
F^n\mathcal J(R)=
\ker\bigl(\mathcal J(R)\longrightarrow\mathcal J(R/\pi_0^n)\bigr),
\quad n\ge1,\qquad P_J=(p-1)[D_0].
\]
**定理 1018.1。**
\[
\boxed{\qquad P_J\in F^m\mathcal J(R)\setminus F^{m+1}\mathcal J(R).\qquad}
\tag{1018.3}
\]
相应规范首类属于
\[
F^m/F^{m+1}\simeq
H^1(\mathcal X_k,O_{\mathcal X_k})
 \otimes_k(\pi_0^mR/\pi_0^{m+1}R).
\tag{1018.4}
\]
下面明确计算它在原 \(a=0\) 尾上的投影。

记中心的真正标准 Igusa 参数为 \(b\)。仍是
\[
a=b^p,\qquad
G(b)=\frac{(b-1)^2}{b^2+b+1},\qquad
\operatorname{div}_I G
 =m(2s_1-s_\zeta-s_{\zeta^2}).
\tag{1018.5}
\]
特别不能以 \(G(b)^p=F(a)\) 代换主化函数。
R1014 已证 \(P_J\) 约化为零，本篇不重做该特殊纤维结论。

## 2. 全部惯性权给 \(F^m\) 的真实下界

原辅助六层只有两种有效稳定子。三个 \(a^3=1\) 支保留
\(j=0\) 的有效 \(\mu_3\)，记其阶为 \(e_s=3\)；
其余 supersingular 辅助支的有效稳定子为 \(e_s=1\)。
在 \(a=0\)，到 \(j\) 的分歧为三，故 \(e_s=1\)；
在 \(j=1728\) 的三个支，到 \(j\) 的分歧为二，亦为 \(e_s=1\)。
这使用实际 \(a\)-map，不套用未加六层的粗尾。

在一个 \(e_s=1\) 尾，取原商坐标
\[
D_s:\quad Y^2=X(X^{2h}+A_s),\quad A_s\in k^\times.
\tag{1018.6}
\]
三个 \(e_s=3\) 尾则为 R1014 的
\(y^2=x(x^{2g}+A_s)\)。

以下算完整惯性生成元，不仅计算固定 Weil 配对的子群。
选 full-\(p\) 基 \((P,Q=sP)\)，其中抽象 Cartan 的
\(s^2=-3\)，\(P\) 生成所选普通 connected line。
在这个基下，稳定该线的 normalizer 为
\[
\{\operatorname{diag}(a,a),\operatorname{diag}(a,-a):
 a\in\mathbf F_p^\times\}.
\tag{1018.7}
\]
因为 \(p\equiv3\pmod4\)，其 determinant 覆盖
\(\mathbf F_p^\times\)，且全部元素保持 \(Q\) 的直线。

令 \(\sigma(\varpi)=u\varpi\)，\(u\) 为原始
\(p^2-1\) 次单位根，置
\[
\xi=u^2,\qquad t=u^{p-1}=\xi^m,\qquad
\sigma(\pi_0)=\xi\pi_0.
\]
用 (1018.7) 的元素调整 Weil 分量后，原 Cartan 坐标
\(U=A_0^{p+1}-c/2,\ V=A_0B_0\) 的变化分别为
\[
(U,V)\longmapsto(U,tV)
\quad\text{或}\quad(-U,-tV).
\]
因此在实际 normalizer 商 \(X=V^2,Y=UV\) 上，两种情形都给
\[
\sigma^*X=t^2X,\qquad \sigma^*Y=tY.
\tag{1018.8}
\]
于是 \(H^0(D_s,\Omega^1)\) 的基 \(X^j\,dX/Y\) 有准确权
\[
\xi^{m(2j+1)},\qquad0\le j<h.
\tag{1018.9}
\]
在 \(e_s=3\) 尾取 \(x=X^3,y=XY\)，相应权为
\[
\xi^{3m(2j+1)},\qquad0\le j<g.
\tag{1018.10}
\]
中心 \(I\) 的惯性经 \(\mathbf F_p^\times/\{\pm1\}\) 作用，
阶整除 \(m\)，故其全部余切权指数是 \(p+1\) 的倍数。
正则化的有理链没有 Jacobian 余切空间。

R1014 的树形乘积分解保留所有这些块。
因为 \(e_0\) 与 \(p\) 互素，可以如 R378 §5 对实际
\(\widehat{\mathcal J}_0\) 的形式参数作 character 平均，
得到整参数 \(Z_i\) 使
\[
\sigma Z_i=\xi^{w_i}Z_i
\]
为整个形式环上的恒等式。取 \(0\le w_i<e_0\)。
(1018.9)–(1018.10) 的指数均已落在这个范围内；
它们的最小值分别为 \(m\)、\(3m\)。
中心的最小正指数至少为 \(p+1>m\)。

点 \(P_J\) 定义于 \(K_{\rm ur}\)，且约化为零。
所以 \(Z_i(P_J)\) 属于 \(\pi_0^{w_i}K_{\rm ur}\cap R\)；
若 \(w_i=0\)，约化为零又迫使它至少含 \(\pi_0^{e_0}=p\)。
因此全部坐标含 \(\pi_0^m\)，证明 \(P_J\in F^m\)。
第 \(m\) 层只可能在 \(e_s=1\) 尾的 \(j=0\) 对偶方向；
中心与三个支持尾在这一层没有分量。这是完整 Jacobian 的结论，
没有假定某个模形式投影整饱和。

## 3. 同一个原 \(b\) 的惯性不变实际提升

在原 ordinary 管状邻域，connected line 由有限平坦群决定。
用同一实际 Cartan 取 \(Q=sP\)，令
\[
\phi:E\longrightarrow E'=E/\langle Q\rangle.
\tag{1018.11}
\]
这指定了真正的辅助 \(p\)-同源，不是换一个抽象同型椭圆曲线。
(1018.7) 在调整 Weil 分量时保持 \(\langle Q\rangle\)，故
\(E'\) 和沿 \(\phi\) 运输的六标记在惯性下不变。
由此得到实际辅助参数 \(b_{\rm lift}\)。

必须核其约化恰为 (1018.5) 的 \(b\)。
标准 Igusa 对象为 \((E_b,\alpha_b,Q)\)，原 exotic 对象是
\((E_b^{(p)},F_{E_b}\alpha_b,(0,Q))\)。
在普通特殊纤维上 (1018.11) 为 \(V_{E_b}\)，而
\[
V_{E_b}F_{E_b}=[p].
\]
这里 \(p\equiv-1\pmod6\)，运输的六标记与原标记只差
\(-I_6=(I_2,-I_3)\)。该元素属于实际
\(H_6\)，因为 \(-I_3\in Q_8=\ker\vartheta\)。
所以在原 \(H_6\) 商上标记相同，
\[
\overline{b_{\rm lift}}=b.
\tag{1018.12}
\]
实际 \(\sqrt[3]4\) 的 \(p\)-局部扭曲已平凡，且其剩余值在
\(\mathbf F_p\) 中；这个比较也保持原 \(a\) 的规范。
没有未核的 Möbius 变换。

于是 \(G(b_{\rm lift})^2\) 是同一个
Igusa 主函数 \(G^2\) 的真正惯性不变提升。
选择 trace-zero \(Q\) 并不改变原 Cartan 子代数、项链、
\(a\) 或三个 \(c_\xi\)。它与另一合法 ordinary
quotient-isogeny 在泛纤维可以不同，不能混写其高阶展开；
本篇始终使用 (1018.11)。

## 4. 原 quotient-isogeny 的准确首项

本节在 full-\(p\) Drinfeld 图的平坦整环 \(\mathcal A\) 上进行；
为取得尾上的有理首项，可以先局部化使
\(\beta_Q=\overline{T(Q)/\varpi}\ne0\)。
\(C=\langle Q\rangle\) 是实际 rank-\(p\) 有限平坦子群，
\(E'=E/C\) 为椭圆 scheme。
选择 quotient 的 norm 参数
\[
S(T)=\prod_{a\in\mathbf F_p}
 \mathcal F(T,[-1]_{\mathcal F}(T(aQ))),
\]
其中 \(\mathcal F\) 是原形式群加法。
其模 \(\varpi\) 为 \(T^p\)。在不变微分的原整规范中，
Wilson 乘积给
\[
d\phi=\varpi^{p-1}
 \bigl(-\beta_Q^{p-1}+O(\varpi)\bigr)
 \cdot\text{常数单位}.
\tag{1018.13}
\]
更换到指定原椭圆模型的参数只改变一个约化为常数的单位；
它不将 \(\beta_Q^{p-1}\) 删除。

由 \(d\phi\,d\phi^\vee=p\)，在当前局部化上
\[
(d\phi^\vee)=(\varpi^{p(p-1)}).
\]
令 \(S_0=\operatorname{Spec}\mathcal A/
(\varpi^{p(p-1)})\)；因 \(p=\varpi^{p^2-1}\)，这是特征 \(p\) 的底。
在 \(S_0\) 上 \(\phi^\vee\) 拉回全部相对微分为零。
其形式幂级数只有 \(p\) 倍次数，所以
\(\ker F_{E'/S_0}\subset\ker\phi^\vee\)。
两者皆为 rank-\(p\) 有限平坦群，故相等，从而
\[
\phi^\vee=h_0\circ F_{E'/S_0},\qquad
h_0:E'^{(p)}\xrightarrow{\sim}E.
\]
在
\(\phi\phi^\vee=[p]=V_{E'}F_{E'}\) 中消去 faithfully-flat
的 \(F_{E'}\)，得到 \(\phi h_0=V_{E'}\)。
于是
\[
\operatorname{Ha}(E')=d\phi\,dh_0
 \pmod{\varpi^{p(p-1)}}.
\tag{1018.14}
\]

这里 \(dh_0\) 的约化确为常数单位。特殊尾上原 \(E\) 是固定
supersingular \(E_s\)；\(C\) 约化为 \(E_s\) 的唯一 rank-\(p\)
\(\alpha_p\) 子群。因此 \(E'_k=E_s^{(p)}\)，norm 参数已使
\(\phi_k=F_{E_s}\)。相应 \(h_{0,k}:E_s^{(p^2)}\to E_s\)
是固定同构，不随尾上点变化。也可用 \(p>3\) 时固定椭圆曲线的
自同构群有限 étale 和尾的连通性核准这一点。

在 \(e_s=1\) 的实际辅助支，\(b-b_s\) 是 fine 变形参数，
Hasse 在 supersingular 点有简单零。因此 (1018.13)–(1018.14) 给
\[
\boxed{\quad
\overline{\frac{b_{\rm lift}-b_s}{\varepsilon_1}}
 =\kappa_s\beta_Q^{p-1},\qquad
\varepsilon_1=\varpi^{p-1}=\pi_0^m,\quad
\kappa_s\in k^\times.
\quad}
\tag{1018.15}
\]
在原 \(b_s=0\) 支，简单零是 R378 (378.18) 的原单位 Hasse
一次项，且 \(a=0\) 支保留 fine 参数，不能将它误作 \(j\) 的三次尺度。
对一般 \(e_s=1\) 支，亦可由 Legendre Hasse 多项式
\(\sum_{i=0}^{(p-1)/2}\binom{(p-1)/2}{i}^2\lambda^i\)
的标准二阶方程直接证明简单性：在 \(0,1\) 外若有重根，
合法次数 \(<p\) 的 Taylor 递推迫整个多项式为零；而在 \(0,1\)
的值分别为 \(1\)、\(\binom{p-1}{(p-1)/2}\ne0\)。
prime-to-\(p\) 的 fine 层不改变简单零。

(1018.15) 是实际同源的首项；误差在更高 \(\varpi\) 层。
普通节点的局部扩张中同样成立，故可读取其在尾的附着点的
Laurent 主部。它不是由一个抽象 special-fibre 同构猜出的提升。

## 5. Trace-zero 坐标给参考尾上的准确 gap

仍保持 (1018.11) 的 \(Q=sP\)，令
\(\alpha=\overline{T(P)/\varpi}\)、\(\beta=\overline{T(Q)/\varpi}\)，
并取
\[
A_0=\beta+s\alpha,\quad B_0=\beta-s\alpha,\quad
A_0^{p+1}-B_0^{p+1}=c,\quad
U=A_0^{p+1}-c/2,\quad V=A_0B_0.
\tag{1018.16}
\]
这里 \(c=-2s(\alpha^p\beta-\alpha\beta^p)\ne0\)。
所选 ordinary 节点对应 connected line \(\alpha=0\)，故
\(A_0/B_0=1\) 于该无穷支，且 \(\beta\) 为真正的 étale 方向。

置 \(a_*=c/2,\ A_s=a_*^2\)。在 (1018.6) 的唯一无穷点选参数
\[
X=V^2=z^{-2},\quad Y=UV=z^{-(2h+1)}S,\qquad
S=\sqrt{1+A_s z^{4h}},\quad S(0)=1.
\tag{1018.17}
\]
令 \(w=z^{2h}\)、\(r_0=A_0/B_0\)、
\(t_0=(1-r_0)/(1+r_0)\)。
由 (1018.16) 可得
\[
r_0^{(p+1)/2}=S+a_*w,\qquad
r_0^{p+1}=(S+a_*w)^2.
\]
因 \(r_0(0)=1\)，在所需次数 \(<p\) 的 \(w\)-截断内，
\(r_0^p=1\)，所以
\[
r_0=(S+a_*w)^2+O(w^p),\qquad
t_0=-a_*w/S+O(w^p).
\tag{1018.18}
\]
只使用这个有限截断；没有在特征 \(p\) 中随意定义无限分数幂。

另一方面，\(\beta=(A_0+B_0)/2\) 给精确恒等式
\[
\beta^{p-1}=\frac{U+a_*t_0}{V}.
\]
结合 \(U=z^{-2h}S\)，得到
\[
\beta^{p-1}
 =z^{-(2h-1)}(S+a_*t_0w)
 =z^{-(2h-1)}S^{-1}
   +O\bigl(z^{-(2h-1)}w^p\bigr).
\tag{1018.19}
\]
其唯一负次项就是 \(z^{-(2h-1)}\)。而
\[
\omega_j=X^j\,dX/Y
 =-2z^{2h-2j-2}S^{-1}\,dz,\qquad0\le j<h.
\]
故
\[
\boxed{\quad
[\beta^{p-1}]=[z^{-(2h-1)}]\ne0
 \quad\text{于 }H^1(D_s,O_{D_s}),\quad
\operatorname{Res}_\infty(\beta^{p-1}\omega_0)=-2.
\quad}
\tag{1018.20}
\]
对其它 \(\omega_j\) 的配对为零。这是一个具体原 gap 类。

惯性分支符号也须保留。由 (1018.8) 及 (1018.17) 的
\(Y\)-规范，完整生成元作用为
\(\sigma z=t^{2h-1}z=-t^{-1}z\)，不是简单的 \(t^{-1}z\)。
由于 \((2h-1)^2\equiv1\pmod{4h}\)，
(1018.20) 的类具有权 \(t^{-1}\)，恰与
\(\varepsilon_1\) 的权 \(t\) 配平，亦与 Serre 对偶相容。

## 6. 完整 Čech 首类：同一 frame 与全部较早层

令 \(\mathscr L\) 为
\(O_{\mathcal X}((p-1)D_0)\) 经树上的 vertical twister 调整后的
零多度线丛，它给实际点 \(P_J\)。
先把中心 \(I\) 的 twister 系数定为零。
在正则化的树上，每条边的相邻系数差是该边外侧子树的 divisor
degree，即该边的 flux。
因此在任何无 \(D_0\) 支撑的 \(e_s=1\) 尾及其整条附着有理链上，
flux 为零，所有系数都与 \(I\) 相同。
所以在“该尾、节点、相邻 ordinary 中心”这一整片上，
\(\mathscr L\) 没有 horizontal 或 vertical divisor：
**canonical rational section \(1\) 是同一个非消失 frame。**
此处不是拼接两个任意选取的局部 frame。

R1014 的特殊平凡化在中心由 \(G^{-2}\) 给出，在三个支持尾由
相应 \(x_\xi^{-m a_\xi}\) 给出，其它尾取匹配节点值的常数。
这里使用 \(O(D)\) 的约定，所以实际无零 section 是主函数的逆。
特殊平凡化在中心的 character 为一：canonical frame 与
\(G(b)\) 均惯性不变，因而其全局 character 也为一。

§2 已证明 \(\mathscr L\) 模 \(\pi_0^m\) 平凡。
取一个全局平凡化并对整个 tame 群作平均。
其约化仍是上述指定特殊平凡化；由 Nakayama，它仍是一个平凡化，
并且在惯性下不变。
在 ordinary 中心，把它与真正的
\(G(b_{\rm lift})^{-2}\) 比较。
若最早差为 \(\pi_0^n f\)，其中 \(0<n<m\)，
不变性要求
\[
\sigma_I^*f=\xi^{-n}f.
\]
但 \(\sigma_I\) 的阶整除 \(m\)，故必须 \(p+1\mid n\)，不可能。
所以两者在模 \(\pi_0^m\) 时相同。
在无支撑 \(e_s=1\) 尾，原 canonical frame 和常数提升同理：
函数角色皆为 \(m\) 的倍数，亦没有 \(0<n<m\) 的隐藏修正。
这证明用以下实际过渡读取的确是原线丛的第一个可能非零层。

在无支撑尾处，将尾的 section 常数取成 \(G(b_s)^{-2}\)。
按“从 \(e_D/e_I=1+\varepsilon_1 f\) 读取 \([f]\)”的
Čech 边界约定，其节点过渡为
\[
\frac{G(b_s)^{-2}}{G(b_{\rm lift})^{-2}}
 =1+2\frac{G'(b_s)}{G(b_s)}
       (b_{\rm lift}-b_s)
   +O((b_{\rm lift}-b_s)^2).
\]
由 (1018.15)、(1018.20)，首类在这一尾的准确投影为
\[
\boxed{\quad
2\frac{G'(b_s)}{G(b_s)}\kappa_s
 [z_s^{-(2h-1)}].
\quad}
\tag{1018.21}
\]
改用相反的 Čech 约定会同时改变所有边界符号，不改变 (1018.3)。

其它局部平凡化在第 \(m\) 层的更改只添 coboundary。
中心和三个支持尾不可能有同层 cohomology 分量，已由 §2 的全部
惯性权排除。其它无支撑尾虽也可能贡献，但 R1014 的树形
\(H^1(O)\) 直和使它们不能抵消 (1018.21) 在给定尾上的分量。
因而内在变形、节点和其它尾没有被省略为未知同层误差。

现在使用原 \(a=0\) 参考尾。它无 \(D_0\) 支撑，
其标准参数 \(b_s=0\)，而
\[
G(b)^2=1-6b+O(b^2),\qquad
2G'(0)/G(0)=-6.
\]
所以 (1018.21) 为
\[
\boxed{\quad -6\kappa_0[z_0^{-(2h-1)}]\ne0.\quad}
\tag{1018.22}
\]
\(p>37\) 保证 \(-6\) 为单位，\(\kappa_0\) 已由实际同源证明为单位。
这与 §2 的下界合起来完成 (1018.3)。

## 7. 同一 trace-zero 提升在三次商尾上的全部 gap

为后续高层比较，记录同一实际同源的另一个完整局部恒等式。
这里返回三个 \(e_s=3\) 尾，仍保持 (1018.16)，而取
\[
x=V^6=z^{-2},\quad y=UV^3
 =z^{-(2g+1)}\sqrt{1+A_s z^{4g}},\qquad
\psi=\beta^{3(p-1)}.
\]
在相同普通无穷支，§5 的有限截断计算变为
\[
\psi=z^{-(6g-1)}(1+A_s z^{4g})^{-3/2}
 +O\bigl(z^{-(6g-1)}(z^{2g})^p\bigr).
\tag{1018.23}
\]
这也是实际 coarse 参数提升的首项：
\[
(j(E')-0)/\varpi^{3(p-1)}
 =\kappa\,\psi\pmod{\varpi},\qquad \kappa\in k^\times,
\]
因为此支的粗 \(j\) 在 Hasse fine 参数处恰为三次零。
具体辅助 \(b-b_s\) 只多原单位。

对每个 \(0\le j<g\)，置
\(k_j=2j+1\)、\(n_j=3j+1=(3k_j-1)/2\)。
取原 \(\omega_j=x^j\,dx/y\)，有
\[
\operatorname{Res}_\infty(\psi^{k_j}\omega_j)
=-2(-1)^{n_j}\binom{2n_j}{n_j}A_s^{n_j},
\]
对其它 \(\omega_\ell,\ \ell\ne j\) 的 residue 均为零。
确切地，乘积是
\[
-2z^{\,2g(1-3k_j)-1}
 (1+A_s z^{4g})^{-(3k_j+1)/2}\,dz.
\]
读取 \(z^{-1}\) 正好取第 \(n_j\) 项；
其它 \(\ell\) 的指数差不被 \(2g\) 整除，不能贡献。
所有所需 \(z^{2g}\) 次数
\(3k_j-1=6j+2\le(p-7)/2<p\)，
所以 (1018.23) 的合法截断足够。

原 gap basis 与 \(\omega_j\) 的 Serre 配对为 \(-2\)，故
\[
\boxed{\quad
[\psi^{\,2j+1}]
=(-1)^{3j+1}\binom{6j+2}{3j+1}A_s^{3j+1}
 [z^{-(2g-2j-1)}].
\quad}
\tag{1018.24}
\]
因 \(6j+2<p\)，右侧系数在每个所述 \(p\) 上都是单位。
这给这个**指定原 node 的实际 quotient-isogeny 过渡**在全部
\(g\) 个 gap 上的读数；它并不把这些局部类自动变成原全局
\(P_J\) 在更高层的类。
更高层还会有中心变形、其它尾和较早过渡的乘积项，
不能沿用 §6 仅适用于最早层的排除。

## 8. 形式点、对数与非 CM 商的不同后继

(1018.3) 给出的实际深度为
\[
v_p(\pi_0^m)=\frac1{p+1}.
\]
这个尺度低于 \(1/(p-1)\)；因此整形式坐标的首项不能自动认作
形式对数的首项。对数中次数 \(p\) 的项带有分母 \(p\)，
其实际 Hasse/Frobenius 系数及同阶抵消尚需计算。
本篇没有把形式点非零当作非挠，也没有以一个低阶局部单位代替
\(\log P_J\) 的完整读数。

同样，虽然所有实际商延拓到良好模型，(1018.22) 在某个
Q-simple 半秩商中可能被整微分映射杀掉。
R1011 的真实 MW 对数横截性仍有效；要将这里的新输入用于它，
须保留实际整投影、log 的完整首层与原 \(c_1\) 的 Abel jet。
有限辅助群的半单性或某个 Hecke 对应的次数是单位，均不能代替
上述投影核准。\(p\equiv5\pmod{12}\) 的双中心/图同调也未被本篇覆盖。
**Serre 主目标仍 OPEN。**

## 9. 依赖与全文核准

- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md)：原 compact-type 模型、全部中心/尾类、真实 \(a=b^p\) 及 \(G^2\) 主化；本篇在其基础上计算完整最早提升。
- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md)：实际六层稳定子、原 Cartan 商坐标和标记；只用仍有效的几何部分，不恢复 R575 撤回的旧 CM 秩零商。
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md)：原 Hasse 单位一次项与实际好模型的 tame character 平均。本篇对整个 \(J_1\) 重新列出全部惯性权，未移用旧商的角色限制。
- B. Edixhoven and P. Parent, [Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf), Documenta Mathematica 26 (2021)：§2.1 的 exotic Igusa、§2.2 的 full-\(p\) Drinfeld 坐标及 Theorem 3.3 的 fine 辅助层模型。原文与 R1014 的相关位置已实际读取。
- [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md)、[R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：原非 CM 点的非挠和半秩商，保留各自范围；本篇未以形式首层替代它们。

global_route 与 root 独立核准完整惯性生成元的 determinant 调整、
全部 Hodge 权和准确底环、同一 exotic \(b\) 的六标记方向、
dual derivative 的 Frobenius 因子化及常数单位、trace-zero 主部、
无支撑尾的 zero-flux 同一 frame、全局 character 平均、
所有较早层与其它分量、无穷分支符号及全部 gap 二项式。
无数学程序执行，无既有素数窗口或局部数据重算。
