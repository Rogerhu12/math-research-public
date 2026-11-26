# R1042：原 CM 圆盘的真实第二列与完整有限角投影

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
global_route / root；o1_theta 与 o2_high_coefficient 已全文独立纸审通过。

**已证明：在 R1033 的同一个原整圆盘中，次高系数模最高系数，
由一个新的明确 Cauchy 列给出。**
这个结论保留原节点单位、实际参数及整个第 \(7m\) normal 层。
它不是把一个单尾参考多项式的单位系数直接当作全局 Abel 系数。

令 \(n_0=4g-1\)、\(n_1=4g-2\)。在下文的同一原 Lie 基中置
\[
J_0=\sum_{s\in S}\frac{e_s}{(1-s)^2},\qquad
J_1=\sum_{s\in S}\frac{e_s}{(1-s)^3}.
\]
若原规范 Abel-log 的 \(w^n\) 系数向量为 \(V_n\)，则
\[
\boxed{\quad
V_{n_0}=u_0J_0,\qquad
V_{n_1}\equiv u_1J_1\pmod{kJ_0},
\quad}
\tag{1042.1}
\]
其中
\[
u_0=-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}\lambda_0^{-n_0},
\qquad
\boxed{\quad
u_1=\frac{16}{5m}\kappa_1^2A_{\rm tail}^2\lambda_0^{-n_1}.
\quad}
\tag{1042.2}
\]
两者都是实际保留的单位。未指定的 \(J_0\) 倍数没有被设为零。
这证明整个类型块的前两列线性独立；尚未证明指定
Mordell–Weil 消去泛函在任何一列上取单位。

## 1. 原对象和准确限制子空间

只取
\[
p=12g-1>37,\quad m=(p-1)/2=6g-1,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m .
\]
保持 R1023、R1029、R1032、R1033 的原 \(X_1\)、\(c_1\)、
实际整投影 \(e_1\) 及同一个 trace-zero ordinary quotient。
在 \(S=\{A_p=0\}\) 的尾上使用
\[
\omega_s=dX_s/Y_s,\qquad f_s=[z_s^{-m}],\qquad
e_s=\theta_sf_s,\qquad \langle f_s,\omega_t\rangle=-2\delta_{s,t}.
\]
底 Hodge 向量写为 \(L=\sum_sL_s\omega_s\)。R1032 给完整中心首层
\[
\varepsilon R_L(b)\,db,\qquad
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2}.
\tag{1042.3}
\]
原 \(c_1\) 尾是
\[
D:\ y^2=x(x^{2g}+A_{\rm tail}),\quad Q=(0,0),\quad t=\sqrt{x}.
\tag{1042.4}
\]
本文先在准确的余维一子空间
\[
\boxed{\quad R_L(1)=0\quad}
\tag{1042.5}
\]
上计算。取同一个实际权 \(m\) 的整 Hodge 提升
\(\Omega=e_1\Omega_L\)。R1029 保证这种类型一提升模 \(p\) 唯一。
R1032 已证明其 \(D\) 上第 \(4m\) 层为
\(\kappa_1R_L(1)d(x^{2g-1}y)\)，因此 (1042.5) 使这个
**完整层**为零。这里不是只将最高 Laurent 系数置零。

## 2. 到第 \(7m\) 层的全部 normal 输入

### 2.1 CM 尾没有隐藏的更早层

该尾仿射函数和微分的完整惯性角色都是 \(3m\) 的倍数。
权 \(m\) 的整体微分在第 \(n\) 层因而必须满足
\(n\equiv m\bmod 3m\)。
R1032 已排除 \(n<4m\)；(1042.5) 又使 \(4m\) 全层为零。
所以
\[
\Omega|_D\equiv0\pmod{\pi_0^{7m}}.
\tag{1042.6}
\]
尤其在 \(4m<n<7m\) 不能发生一个额外 CM 层。

同一论证也可逐层写成 gluing 归纳。CM 尾的全纯微分角色为
\(3m(2j+1)\)、\(0\le j<g\)；在权 \(m\) 的提升中，
最早可能作为全纯自由项的 normal 次数至少是
\((6g+4)m>7m\)。
所以直到本次精度，指定 polar part 后没有 CM holomorphic 自由项。

### 2.2 中心只有三层，中心自身变形仍保留

中心的惯性角色为 \(p+1\) 的倍数。
在 \(0<n\le7m\) 中只可能有
\[
n=m,\qquad 3m+2,\qquad5m+4 ;
\tag{1042.7}
\]
下一层 \(7m+6\) 已越界。

严格沿用 R1032 §3 的实际节点
\(zw=\rho\pi_0^3\) 及其公式
\[
c\,w^a\,dw\quad\longmapsto\quad
-c\bar\rho^{\,a+1}\pi_0^{\,n+3(a+1)}z^{-a-2}\,dz.
\tag{1042.8}
\]
所有 \(\rho\) 和更高单位项保留。这里只假定当前 \(b=1\) 尾
的早期层为零；其它两个 CM 尾的第 \(4m\) 层可已非零，
并在后续中心层给出返回 principal parts。这些既定极部全部保留，
它们在当前 \(b=1\) 标记正则。
提升中心自身带标记 smooth deformation 的剩余项时，取
\(D_{\rm aux}\) 包含 \(S\) 及其它已规定极点、避开当前标记；
\(H^1(I,\Omega_I^1(D_{\rm aux}))=0\) 保证继续保持当前正则。
这个 vanishing 不删除全纯自由项，也不替代已规定主部的可解性；
桥节点 residue 仍由实际 compact-type 树和 residue 定理逐一迫为零。

因为所有更早 CM 层已为零，(1042.7) 的三个中心层在当前 CM
节点都没有来自该尾的 polar input；中心自身变形也不会凭空造出
这个极点。因此下面使用的是这些层的 **regular** Taylor 项。

- 第 \(m\) 层是 (1042.3)。由 \(R_L(1)=0\)，在 CM 节点
  \(b-1\) 阶为 \(m\) 的参数中，其最小阶是 \(2m-1\)。
  它最早在 \(m+3(2m)=7m\) 传入，最高极阶为 \(2m+1\)。

- 第 \(3m+2\) 层是 \(u^{-2}\) 角色。其 regular Taylor 指数
  从 \(2g-2\) 开始，之后相差 \(m\)。
  最小项本会在第 \(4m\) 层给极阶 \(2g\)。
  此时第 \(m\) 层的输入因 \(R_L(1)=0\) 已为零；
  没有第三个中心层可在 \(4m\) 到达，也没有 CM 全纯自由项。
  因此完整 CM \(4m\) 层为零迫这个最低 Taylor 系数为零，
  并不存在用别层抵消后仍保留它的情形。
  下一个允许指数为 \(2g-2+m=8g-3\)，在 \(7m\) 到达，
  极阶至多 \(8g-1\)。

- 第 \(5m+4\) 层是 \(u^{-4}\) 角色。
  在 CM 点，\(u^{-4}db\) 的原阶为 \(-2g-2\)；
  regularity 至少要求补一个 \(r=1-b^3\)，其阶为 \(m\)。
  所以最小 regular 指数是 \(4g-3\)。
  它最早在 \(5m+4+3(4g-2)=7m\) 到达，
  极阶至多 \(4g-1\)。

其它 supersingular 尾的往返传播可以改变后两层的系数，
但不能改变已确定的第 \(m\) 层。
原节点的高阶单位、中心非齐次变形以及这些往返项，均只改变
后面的较低极部。由此得到完整界
\[
\boxed{\quad
\text{第 }7m\text{ 层的极只在 }\infty,\qquad
\operatorname{pole}\le2m+1=p .
\quad}
\tag{1042.9}
\]

## 3. 原最高极部来自指定 \(R_L'(1)\)

R1021 的同一个实际 target fine 参数满足
\(u'=\varepsilon(c_Q\psi+pR_Q)\)；coarse \(b-1\) 在该 fine
CM 参数处恰为三次零。R1032 因而固定了原单位 \(\kappa_1\)，使
\[
b_{\rm lift}-1=\kappa_1\varepsilon^3\psi_3+\text{更高层},
\qquad
\psi_3=\beta^{3(p-1)}
=z^{-m}+\text{较低极阶项}.
\tag{1042.10}
\]
这是同一个 ordinary node 的局部式；不声称 \(\psi_3\) 是
整个 \(D\) 上的正则函数。

在 \(R_L(1)=0\) 下，
\[
R_L(b)\,db
=R_L'(1)(b-1)d(b-1)+O((b-1)^2d(b-1)).
\]
所以第 \(7m\) 层的唯一最高 polar part 准确为
\[
\boxed{\quad
\frac{\kappa_1^2}{2}R_L'(1)\,d(\psi_3^2).
\quad}
\tag{1042.11}
\]
其 \(z^{-2m-1}dz\) 系数为
\(-m\kappa_1^2R_L'(1)\)。
任何 \(b_{\rm lift}\) 的更高非线性项，要么乘已为零的
\(R_L(1)\)，要么将 (1042.11) 的 normal 次数提高。
对中心更高层的影响已包含在 §2 的较低极部中。

第 \(7m\) 层在尾上的角色为 \(-6m\)。
全部仿射正则微分按 \(x^jdx/y\) 和 \(x^jdx\) 分解。
前者的角色是奇数倍 \(3m\)，不可能等于 \(-6m\)；
后者恰要求
\[
j\equiv2g-2\bmod2g,\qquad 0\le j\le6g-2
\]
（最后一个界来自 (1042.9)）。
因此完整所需空间正是
\[
d\langle x^{6g-1},\,A_{\rm tail}x^{4g-1},
                    \,A_{\rm tail}^2x^{2g-1}\rangle .
\tag{1042.12}
\]
三个 primitive 指数都小于 \(p\)，没有不可见的 \(p\) 次函数项。
(1042.11) 与 \(x^{6g-1}\) 的最高系数比较，给出
\[
\overline{\varepsilon^{-7}\Omega|_D}
=\frac{\kappa_1^2}{2}R_L'(1)d(x^{6g-1})
 +a_Ld(A_{\rm tail}x^{4g-1})
 +b_Ld(A_{\rm tail}^2x^{2g-1}).
\tag{1042.13}
\]
这里 \(a_L,b_L\) 保留完整的未知反馈，尚未删除。

## 4. 整有限角杀掉的准确多项式子空间

### 4.1 哪些简单模能被 \(E\) 看见

保持 R1030 的 \(G=\operatorname{PGL}_2(\mathbf F_p)\)、
\(N\)、真正整幂等元 \(E\in e_N\mathbf Z_p[G]e_N\)。
R434 的独立有效有限格和 R1030 给
\(k[G]E\) 的 Jordan–Hölder 因子恰为
\[
1,\quad1,\quad
S_0=\operatorname{Sym}^{p-3}(k^2)\otimes\det .
\tag{1042.14}
\]
这是从特征零的 \(1\oplus V_{\theta_1}\) 稳定格约化得到；
没有再消费 R434 已撤回的全局 CM 商。

\(S_0\) 的 nonsplit Cartan 不变量为零。
确切地，Cartan 特征在 \(S_0\) 的各权上为
\(\alpha^{(p-1)j}\)、\(2\le j\le p-1\)，
没有平凡权。因此 \(ES_0=0\)。
若简单模 \(M\) 满足 \(EM\ne0\)，由
\(\operatorname{Hom}_{k[G]}(k[G]E,M)=EM\)，
它必须是 (1042.14) 中的简单商；故只可能是平凡模。
幂等元作用是 exact functor，从而
\[
\boxed{\quad
\text{没有平凡 Jordan–Hölder 因子的模均被 }E\text{ 杀掉}.
\quad}
\tag{1042.15}
\]

### 4.2 完整 \(C\)-过滤，包括终端

在原二维 \(\mathbf F_p\) 向量坐标中令
\[
C=X^pY-XY^p.
\]
对齐次次数 \(D\ge p\)，评价于全部非零
\((X,Y)\in\mathbf F_p^2\) 的核恰为
\(C\operatorname{Sym}^{D-p-1}\)：在每条 \(\mathbf F_p\) 直线上
恒零的齐次多项式被其线性因子整除，所有这些不同因子的乘积就是 \(C\)。
评价像为相应的 homogeneous function space \(W_r\)，
\(r=D\bmod(p-1)\)，其维数为 \(p+1\)。
这里评价点是二维 \(\mathbf F_p\) 向量，绝不是扩域中的全部点。

取 \(0\le r\le p-2\)。标准多项式子模和其商的
Jordan–Hölder 因子是
\[
W_r:\quad
\operatorname{Sym}^{r},\qquad
\operatorname{Sym}^{p-1-r}\otimes\det^r.
\tag{1042.16}
\]
可直接在 scalar、split semisimple 和 nonsplit semisimple 的
\(p\)-regular 类上核 Brauer character：
split 两特征值不同的时候两项之和为 \(\lambda^r+\mu^r\)，
正是两条固定直线的值；nonsplit 时为零；
scalar 时为 \((p+1)\lambda^r\)。
两项所用的次数介于 \(0\) 与 \(p-1\)，均是标准简单模。
这也保留 \(r=0\) 时的平凡模与 Steinberg，未把它们合并。

现令 \(D\) 是 \(p-1\) 的倍数且 \(D<p^2-1\)。
反复取上述评价核，\(C\)-过滤的第 \(j\) 层为
\[
\det^j W_{r_j},\qquad
r_j\equiv-2j\bmod(p-1),
\]
直到剩下次数 \(n<p\) 的最终简单模
\(\operatorname{Sym}^{n}\otimes\det^j\)。
次数始终为偶数，所以不会在次数 \(p\) 终止。
在整个非首层中 \(1\le j<p-1\)。
若 \(r_j\ne0\)，(1042.16) 的两个简单模维数都大于一；
若 \(r_j=0\)，唯一一维因子是非平凡的 \(\det^j\)。
最终简单模也不可能平凡：那必须同时 \(n=0\) 和
\(j\equiv0\bmod(p-1)\)。
因此
\[
\boxed{\quad
E\bigl(C\operatorname{Sym}^{D-p-1}\bigr)=0
\quad\text{若 }(p-1)\mid D,\ D<p^2-1.
\quad}
\tag{1042.17}
\]
这里 (1042.15) 已逐层应用到完整过滤，终端不是额外加入的
虚拟 \(W_r\) 层。

## 5. 在同一个 full-\(p\) 源上求出投影

用 R1030 的原 Cartan eigenvariables \(A_0,B_0\)：
\[
c=A_0^{p+1}-B_0^{p+1},\quad
U=(A_0^{p+1}+B_0^{p+1})/2,\quad V=A_0B_0,
\]
\[
A_{\rm tail}=c^2/4,\qquad
U^2=V^{p+1}+A_{\rm tail},\qquad x=V^6,\quad y=UV^3.
\tag{1042.18}
\]
原 \(c\) 是 \(C\) 的一个固定非零倍数，所以
\(A_{\rm tail}\) 是固定非零常数乘 \(C^2\)。

定义真正 \(\operatorname{GL}_2(\mathbf F_p)\)-equivariant derivation
\[
\Theta=X^p\partial_X+Y^p\partial_Y .
\tag{1042.19}
\]
因换基矩阵的系数在 \(\mathbf F_p\)，链式法则直接给
\(\Theta g=g\Theta\)。在原共轭 Cartan 坐标中
\[
\Theta A_0=B_0^p,\quad\Theta B_0=A_0^p,\qquad
\Theta V=2U,\quad\Theta U=V^p,\quad\Theta A_{\rm tail}=0 .
\]
R1030 已证明
\[
F=UV^{p-2}=x^{2g-1}y,\qquad EF=F.
\]
逐次微分得到完整恒等式
\[
\begin{aligned}
\Theta F&=-3V^{2p-2}-4A_{\rm tail}V^{p-3},\\
\Theta^2F&=12U(V^{2p-3}+2A_{\rm tail}V^{p-4}),\\
\Theta^3F&=-60V^{3p-3}
 -240A_{\rm tail}V^{2p-4}
 -192A_{\rm tail}^2V^{p-5}.
\end{aligned}
\tag{1042.20}
\]
三项都是齐次次数 \(6(p-1)<p^2-1\)。
后两项分别被 \(C^2\)、\(C^4\) 整除，所以 (1042.17) 杀掉它们。
又 \(\Theta\) 与 \(E\) 交换，故
\[
\boxed{\begin{aligned}
E(x^{6g-1})&=H_2,\\
H_2&=x^{6g-1}
       +4A_{\rm tail}x^{4g-1}
       +\frac{16}{5}A_{\rm tail}^2x^{2g-1},\\
E(A_{\rm tail}x^{4g-1})&=
E(A_{\rm tail}^2x^{2g-1})=0 .
\end{aligned}}
\tag{1042.21}
\]
这是一条全配对分支的多项式恒等式，不从单个 \(A_{\rm tail}\)
固定的分支外推。它也保留了 \(\Theta^3F\) 的准确常数 \(-60\)。

为把它合法用于 (1042.13)，仍须核分支尺度。
R1030 的 norm \(d\in\mathbf F_p^\times\) 作用为
\[
c\mapsto dc,\quad U\mapsto dU,\quad V\mapsto dV,\quad
x\mapsto d^6x,\quad A_{\rm tail}\mapsto d^2A_{\rm tail}.
\]
(1042.13) 的三个 primitives 分别乘
\(d^{3p-3}\)、\(d^{2p-2}\)、\(d^{p-1}\)，全部为一。
原 full-\(p\) 拉回是 \(N\)-不变，且这些 \(c\) 分支是 norm 的
单一非零轨道。因此三个系数在同一 CM 来源的分支并上是常数。
Frobenius normalizer 元 \(c\mapsto-c\) 亦相容。
这证明应投影的是整个 (1042.13)，不能把 \(A_{\rm tail}\)
提前从 \(E\) 中提出。

R1021/R1030 的换基在整个 \(R/(p)\) 仿射模型上为常线性作用，
固定 \(\pi_0\)，故它逐 normal 层相容，不会把更早层回灌。
\(E=e_1\) 在实际整 Hodge 格上成立，所以应用 (1042.21) 得
\[
\boxed{\quad
\overline{\varepsilon^{-7}\Omega|_D}
=\frac{\kappa_1^2}{2}R_L'(1)\,dH_2
\quad\text{在 }R_L(1)=0\text{ 时}.
\quad}
\tag{1042.22}
\]

## 6. 同一个原 \(z,t,w\) 参数下的第二列

在 \(Q\) 使用原 \(t=\sqrt x\)。由 (1042.21)
\[
H_2(t)=\frac{16}{5}A_{\rm tail}^2t^{4g-2}
          +4A_{\rm tail}t^{8g-2}+t^{12g-2}.
\tag{1042.23}
\]
原完成参数仍为 R1033 的
\[
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varepsilon^3w,
\qquad
\lambda_0=\left.\frac{d\bar z}{dt}\right|_Q\ne0.
\]
这里不重选 \(z\)，不将 \(\lambda_0\) 设为一。

因为在 (1042.5) 上所有小于 \(7m\) 的 CM normal 层均为零，
当前层只需使用特殊纤维的 \(\bar z(t)=\lambda_0t+O(t^2)\)。
任何混合特征的更高参数项只乘这些已为零的较早层，
或提高当前 normal 次数；而 \(\bar z\) 的非线性项不能降低
(1042.23) 的最低 Taylor 次数。
所以其 \(z^{n_1}\) primitive 系数准确乘
\(\lambda_0^{-n_1}\)，不含未支付的低阶坐标项。

R1033 已付清完整积分分母与所有更高尾项，且
\[
7m+3mn_1=e_0+m,\qquad n_1=4g-2<p.
\]
因此对同一个原
\(H_\Omega(w)=(p\varepsilon)^{-1}\int_{c_1}^{P(w)}\Omega\)，
\[
\boxed{\quad
[w^{n_1}]\overline{H_\Omega}
=\frac85\kappa_1^2A_{\rm tail}^2
      \lambda_0^{-n_1}R_L'(1)
=-\frac{32}{5m}\kappa_1^2A_{\rm tail}^2
      \lambda_0^{-n_1}
       \sum_s\frac{L_s\theta_s}{(1-s)^3},
\quad}
\tag{1042.24}
\]
仍限于 \(R_L(1)=0\)。

R1033 的最高列泛函正是非零单位乘 \(R_L(1)\)。
两个线性泛函在其核上的相等，等价于它们在整个底空间上只差
最高列的一个倍数。再用原 Serre 配对 \(-2\)，
(1042.24) 正是 (1042.1)–(1042.2) 的向量同余。
没有在整个空间上将可能存在的那个倍数删掉。

## 7. 真正得到的秩与仍未完成的事项

\(S\) 至少有两个不同的点，且都不等于 \(1\)；
\(e_s\) 是原底 Lie 的基。因此
\[
\frac{(1-s)^{-3}}{(1-s)^{-2}}=\frac1{1-s}
\]
在 \(S\) 上不是常数，\(J_0,J_1\) 线性独立。
由 (1042.1) 原整个类型块的 \(w^{n_0},w^{n_1}\) 两列秩准确为二。

但这不是 R1037 的
\(\Lambda_{\mathcal Q}(J_0)\) 或 \(\Lambda_{\mathcal Q}(J_1)\)
非零定理。若 \(\Lambda_{\mathcal Q}(J_0)=0\)，第二个实际
系数确为 \(u_1\Lambda_{\mathcal Q}(J_1)\)；
仍须证明后一个指定配对为单位，或者继续支付更低的原列。
全类型秩二也不能替代真实 Mordell–Weil 饱和空间的横截性。
没有声称原圆盘只有 CM 零点，也没有解除 O0 的全局覆盖条件。

## 来源与计算范围

- [R434](R434-primitive-cartan-trace-and-scalar-invariant-cm-logarithm.md)，
  只取未被 R575 撤回的有限群稳定格和约化因子。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)、
  [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：
  同一 ordinary quotient、原 full-\(p\) 仿射模型与完整换基作用。
- [R1028](R1028-original-Igusa-Kummer-model-and-same-order-CM-jet-correction.md)：
  原 Igusa Kummer、\(u^{-2}\) 的 CM 阶和节点厚度三。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)、
  [R1030](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md)：
  真实整类型、有限角、全分支原 \(U,V,F,A_{\rm tail}\) 及 norm 运输。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)：
  原 \(R_L,\theta_s,\kappa_1\)、完整第 \(4m\) 层、中心变形与 gluing。
- [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)：
  原 \(z,w,\lambda_0\)、准确共同尺度和完整积分尾界。

全部新计算是上述原对象上的纸面代数、角色、有限格及逐层 gluing。
没有数学程序执行，也没有重扫有限素数窗口。
