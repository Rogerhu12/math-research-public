# R314：完整 self 的有序九矩缺陷、零矩后的局部化与忠实 Euler 坐标

日期：2026-11-15。**完整纸面证明；没有新符号程序、profile 求积、矩阵消元、人工检查或科学执行。**

本稿把 [R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md) 的有序平台矩阵与完整 self 函数联系起来。对 $V\in U\cap\ker\pi$，该矩阵恰是 self 对两个有序不交 profile 的加法缺陷。保留真实左尾后，完整 self 可准确分解为
$$
\boxed{\mathfrak q_u(V)=\mathcal N_{\mathbf T(V)}(u)
+\int L_V(x,u,u',u'',u''')\,dx,}
$$
其中 $\mathcal N$ 是本文明确给出的九参数二重积分，$L_V$ 是局部四次 jet 多项式，最高 jet 为三且最高 jet 至多二次。特别，$\mathbf T(V)=0$ 时，完整 self 的所有剩余 Volterra 尾均能化为局部项；不仅是 principal 部分。

证明从 R295 的完整生成成本展开开始，显式保留左锚常数、二重积分的对角边界和全部 $C^2$ 余项，再作两次有限 Euler 最高阶递降。没有借抽象加性直接引用 Peetre 结论。

来源：[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R303](R303-complete-self-degree-nine-and-all-translation-control.md)、[R313](R313-complete-five-dimensional-J-self-module-and-fifteen-dimensional-image.md)。

## 1. 真实函数空间、生成元与线性延拓

沿用
$$
U=\operatorname{span}_{\mathbb R}
\{V_B:B\text{ 为真实同端口、frame I、}M_B=T_B=0\},
\qquad U_{\mathrm p0}=U\cap\ker\pi .
\tag{1}
$$
这是真实成本的线性 span，不是允许实际成本自由取负的半群。实际闭 hook 的归属按 R105 的真倒行论证处理，不在本稿重新假定。

完整 self 定义为
$$
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u^2,0).
\tag{2}
$$
输入 u 始终是同一个合法 I 内的实紧 profile；公共左右零 collar 都保留。所有右原函数使用原同锚正尾。

对每个 (1) 的生成元，在 $\phi=0,F=u^2$ 上原完整第四 forcing 恰为
$$
-H(Z_{u^2},Z_{u^2}),
$$
因为含 $Y_\phi$ 的另一项准确为零。因此
$$
\mathfrak q_u(V_B)
=-\frac14[x^2]_{\rm left}\mathscr P H(Z_{u^2},Z_{u^2}).
\tag{3}
$$
式 (3) 本身不要求该生成元已有 pure 零。R295 用 actual pure 身份将其识别为单包 $Q_{ii}$；本稿以 (2) 为定义时，(3) 对所有上述 canonical 生成元已经成立。

R105 给 U 有限维。任取有限真实生成基后，所有原 profile 多项式、右锚及有限 jet 上界可共同固定。下文先对生成元作准确代数，再对任意有限实线性组合延拓。特别，$V\in U_{\mathrm p0}$ 不需要在其每一个生成元上分别假设 pure 零；只在用到完整 pure 系数身份时对总 V 使用 $\pi V=0$。

## 2. 九矩就是完整 self 的有序加法缺陷

设真实紧 u 的全部支撑在真实紧 w 左方，二者有正间隙。由于 R73 的所有局部交叉乘积和三条尾密度在不交输入上均为零，
$$
Z_{(a u+b w)^2}=a^2Z_{u^2}+b^2Z_{w^2}.
\tag{4}
$$
这是同一几何、同一原初值的真实二阶场恒等式；不删除单场本身的左尾。

由 (3)，每个生成元的完整 self 只有 $a^4,a^2b^2,b^4$ 三类项，其中交叉系数为
$$
-\frac12[x^2]_{\rm left}\mathscr P H(Z_{u^2},Z_{w^2}).
\tag{5}
$$
在 $V\in U_{\mathrm p0}$ 上，R292 的完整 pure 交叉身份为
$$
Q^Z_{u,w}(V)=-2Q_{u,w}(V).
\tag{6}
$$
该身份来自 universal profile 振幅多项式系数比较，故对总 V 线性成立。生成元具有真实 $M=T=0$，二、三阶历史的周期性也保持；不把一个未付的入历史误作零。

R292 的真实左二次系数给
$$
[x^2]Q_{u,w}(V)=
\mu(u)^{\mathsf T}\mathbf T(V)\mu(w),
\quad
\mu(u)=\left(\int r^2,\int xr^2,
\int[x^2r^2+2v^2]\right),
\tag{7}
$$
其中 $v=u',r=u''$。于是
$$
\boxed{
\mathfrak q_{a u+b w}(V)
=a^4\mathfrak q_u(V)+b^4\mathfrak q_w(V)
+a^2b^2\mu(u)^{\mathsf T}\mathbf T(V)\mu(w).
}
\tag{8}
$$

没有把两槽互换。u 必须在 w 左方，矩阵可非对称。R292 的两组独立真实矩开集又说明：一个矩阵若使 (7) 对所有这种真实有序包为零，就必为零。因此 (8) 也说明 $\mathbf T(V)$ 由完整 self 函数本身唯一决定，与选用哪组成本生成元无关。

特别，
$$
\boxed{
\mathbf T(V)=0
\iff
\mathfrak q_{u+w}(V)=\mathfrak q_u(V)+\mathfrak q_w(V)
\quad\text{对所有真实有序不交 }u,w.
}
\tag{9}
$$
必要性不能仅从一个固定母函数的平移推出；(9) 使用全部允许真实 profiles。

## 3. 一个明确保留全部九矩的非局部项

定义真实二次密度列
$$
j_u(x)=
\begin{pmatrix}
(u'')^2\\
x(u'')^2\\
x^2(u'')^2+2(u')^2
\end{pmatrix},
\qquad\mu(u)=\int j_u.
\tag{10}
$$
对任意实 $3\times3$ 矩阵 A，定义
$$
\boxed{
\mathcal N_A(u)=
\int_{\ell<x<y<r_*}j_u(x)^{\mathsf T}A\,j_u(y)\,dx\,dy .
}
\tag{11}
$$
共同端点位于空 collar 内，真实密度在 collar 为零，故扩大空 collar 不改变 (11)。

若 u 在 w 左方，则
$$
\mathcal N_A(a u+b w)
=a^4\mathcal N_A(u)+b^4\mathcal N_A(w)
+a^2b^2\mu(u)^{\mathsf T}A\mu(w).
\tag{12}
$$
因此
$$
\mathcal F_V(u):=\mathfrak q_u(V)-\mathcal N_{\mathbf T(V)}(u)
\tag{13}
$$
满足准确的不交加性。下面证明在本题原有限 Volterra 类中，(13) 必须有局部 jet 表示；不是只给一个抽象函数命名。

顺便，A 的六个对称和三个反对称参数在 (11) 中有准确解释。若 $A=A_{\rm s}+A_{\rm a}$，则
$$
\mathcal N_{A_{\rm s}}(u)
=\frac12\mu(u)^{\mathsf T}A_{\rm s}\mu(u),
\tag{14}
$$
而反对称部分是三个真实有序面积
$$
\mathcal N_{A_{\rm a}}(u)
=\sum_{i<j}(A_{\rm a})_{ij}
\int_{x<y}\bigl(j_{u,i}(x)j_{u,j}(y)
-j_{u,j}(x)j_{u,i}(y)\bigr)\,dx\,dy.
\tag{15}
$$
没有把这些密度或矩视为独立几何参数。其九个参数在模局部泛函的商中确独立，后文由 (8) 和真实矩开集支付。

## 4. 从完整二阶场到有限双积分类

### 4.1 原输入范围

R73/R295 对一个真实生成元的二阶量给
$$
W_2=\Phi_{m(s)}(u,u),
\quad m(s_0)=m(s_1)=0,
$$
$$
\eta_0=
-\frac{e_s(1+e^2)}{16h^2}r^2
+\frac{h_s(1+e^2)}{8h^2}vr
-\frac{h_se}{8h}v^2
-\frac1{16}\partial_s(J_e/h),
\tag{16}
$$
以及
$$
V_Z=(A,zP+B,eA-hW_2),\qquad
A=(W_2)_x/2+\eta_0/h .
$$
三条 profile 原尾是
$$
J_i(u)(x)=\int_x^{r_*}j_{u,i}(y)\,dy,\quad i=0,1,2.
$$
所有 x 系数是有限多项式。几何及真实累计 m 只进入 s 系数，不是新 profile 参数。

R295 已完整提取
$$
V_{Z,x}=(1,0,e)\Lambda(s,x;u,v,r)u'''
+\mathcal Z_{\le2},
\tag{17}
$$
其中 $\Lambda$ 对 $(u,v,r)$ 线性；$\mathcal Z_{\le2}$ 是局部二次 jet 多项式加三个 $J_i$ 的线性组合，不含更高嵌套的 profile 原函数。

若左分子为 $xU+V$，完整 self 的原来源是
$$
-\frac14\int_B\left\{
\frac{k}{2h}\int_\ell^{r_*}|V_{Z,x}|^2dx
+k\left[\frac{\ell-\omega}{2h}|U|^2+\frac{U\cdot V}{h}\right]
+\frac{|\nabla_sU|^2}{2h^2}\right\}ds.
\tag{18}
$$
U、V 均线性依赖三个真实总矩，故最后两类是这些矩的二次型。式 (18) 显式保留 $\ell$；不能仅把能量内积分留下。

### 4.2 线性三阶 jet 的真实积分处理

展开 (17) 的平方。最高平方项为
$$
(1+e^2)\Lambda^2(u''')^2.
$$
其余所有 $u'''$ 项都只线性出现，形如
$$
H(x,u,v,r,J_0,J_1,J_2)\,r',
$$
其中 H 为有限多项式且至多线性含原尾。

对 r 取从0起的多项式原函数
$$
A(x,u,v,r,J)=\int_0^rH(x,u,v,\rho,J)\,d\rho.
$$
链式求导时使用真实 $J_i'=-j_{u,i}$，得到
$$
Hr'=D_xA-A_x-A_uv-A_vr+\sum_iA_{J_i}j_{u,i}.
\tag{19}
$$
两 collar 上 r=0，故 A 的边项为零，即使某个 $J_i$ 在左 collar 非零也不影响这个事实。余项只含至多二阶 jets、至多一个 J。这样不改变最高平方项，也不隐藏任何低阶余项。

### 4.3 两个尾相乘和真实左常数

剩余非局部项仅有局部二次密度乘一个 $J_i$，两个 $J_i$ 相乘，以及总矩的二次型。

前一种直接写成 $x<y$ 上的双积分。对第二种，若原 x 系数为多项式 $p(x)$，置
$$
P_\ell(t)=\int_\ell^tp(x)\,dx.
$$
真实 Fubini 恒等为
$$
\int_\ell^{r_*}p(x)J_i(x)J_j(x)\,dx
=
\int_{\ell<x<y<r_*}P_\ell(x)
\bigl(j_{u,i}(x)j_{u,j}(y)+j_{u,j}(x)j_{u,i}(y)\bigr)\,dx\,dy.
\tag{20}
$$
特别 $P_\ell$ 的常数项仍在。它和 (18) 的 $\ell$ 项共同保留，不将下限擅自移到0或删去。

总矩乘积同理：
$$
\mu_i\mu_j=
\int_{x<y}\bigl(j_{u,i}(x)j_{u,j}(y)
+j_{u,j}(x)j_{u,i}(y)\bigr)\,dx\,dy.
\tag{21}
$$
对角集合为二维积分的零测集，没有把一条 distribution 边界从已微分表达式中忽略；此时 (20)–(21) 只是普通光滑密度的 Fubini。

因此对每个生成元、再对整个 U，完整 self 都属于如下明确类：
$$
\boxed{
q(u)=\int L(x,u,u',u'',u''')dx+
\int_{x<y}\sum_{a,b,c,d=0}^2
C_{abcd}(x,y)
u^{(a)}(x)u^{(b)}(x)
u^{(c)}(y)u^{(d)}(y)\,dx\,dy.
}
\tag{22}
$$
C 是有限多项式；L 为四次局部多项式，三阶 jet 至多二次。所有 s 积分只是这些有限系数的真实实数。减去 (11) 后仍在同一类。

## 5. 二重密度的准确正规化，保三角边界

关键不是假设 (22) 的原 C 逐个为零。它们可以有分部积分冗余，必须先正规化。

对任一单变量二次 jet 密度
$$
a u^2+buu'+c(u')^2+d u u''+e u'u''+f(u'')^2,
$$
直接乘法求导给
$$
=A_0u^2+A_1(u')^2+A_2(u'')^2+D_xB,
\tag{23}
$$
其中
$$
A_0=a-\frac12b'+\frac12d'',\quad
A_1=c-d-\frac12e',\quad A_2=f,
$$
$$
B=\frac b2u^2+d uu'-\frac{d'}2u^2+\frac e2(u')^2.
\tag{24}
$$
系数可依赖另一个独立变量，但这里的撇号只作用当前变量。

在 (22) 中先按 x 使用 (23)。x 的真实积分区间为 $(\ell,y)$：$\ell$ 端因 u 与所需 jets 为零而消；$x=y$ 的 B 不删，准确回收到一个局部四次、至多二阶 jet 的积分。

对剩余项按 y 再用 (23)。y 的真实积分区间为 $(x,r_*)$：右端同样为零；$y=x$ 的边项同样准确回收到局部 $C^2$ 项。

如此只作有限次纸面分部积分，得到
$$
\boxed{
q(u)=\int\widetilde L(x,u,u',u'',u''')dx+
\int_{x<y}\sum_{i,j=0}^2
P_{ij}(x,y)(u^{(i)}(x))^2(u^{(j)}(y))^2dx\,dy.
}
\tag{25}
$$
P 仍为多项式，三角对角产生的局部项都已并入 $\widetilde L$；最高 $u'''$ 平方项仍是 (17) 给出的原项。

(23) 不是声称任意高阶密度有这种形式；它只用于本题已经付清的二次、二阶双核。这里的有限阶输入恰使两个三角边界都是可控的局部 $C^2$ 项。

## 6. 不交加性强迫全部九个双核为零

设 (25) 满足
$$
q(u+w)=q(u)+q(w)
$$
对任意真实有序不交紧 u、w 成立。固定两个有正间隙的开包络 $I_L<I_R$，分别放 u、w。局部项没有交叉，故
$$
\int_{I_L}\int_{I_R}\sum_{i,j=0}^2
P_{ij}(x,y)(u^{(i)}(x))^2(w^{(j)}(y))^2dy\,dx=0
\tag{26}
$$
对全部真实紧 u、w 成立。

### 6.1 第一轮 Euler 最高阶递降

固定 w，令
$$
A_i[w](x)=\int_{I_R}\sum_{j=0}^2
P_{ij}(x,y)(w^{(j)}(y))^2dy.
$$
式 (26) 是
$$
\int_{I_L}\sum_{i=0}^2A_i[w](x)(u^{(i)}(x))^2dx=0
$$
对全部真实紧 u 成立。其一阶变分给局部算子恒等
$$
A_0[w]-D_x(A_1[w]D_x)+D_x^2(A_2[w]D_x^2)=0.
\tag{27}
$$
这里是作用于任意真实紧测试函数的算子等号。最高四阶系数先迫 $A_2[w]=0$；再看二阶系数迫 $A_1[w]=0$；最后迫 $A_0[w]=0$。不用随机 profiles 或正性推断。

### 6.2 第二轮 Euler 最高阶递降

对每个固定 x 和每个 i，已有
$$
\int_{I_R}\sum_{j=0}^2P_{ij}(x,y)(w^{(j)}(y))^2dy=0
$$
对全部紧 w 成立。重复上一轮，在 y 上先取四阶、再二阶、再零阶，准确得到
$$
P_{i2}(x,y)=P_{i1}(x,y)=P_{i0}(x,y)=0
\quad(x,y)\in I_L\times I_R.
\tag{28}
$$
任意 $x<y$ 都可被这样两个真实小开包络覆盖，所以全部 P 在整个开三角上为零。它们原本是多项式，不存在另一个被忽略的对角 distribution；对角边项已在第5节逐次收回。

因此 (25) 完整退为局部积分。这一证明没有把普通加性直接当作一个未检查前提的局部性定理。

## 7. 完整局部化定理及 principal 保留

对 $V\in U_{\mathrm p0}$，将第6节用于 (13)。由 (8)、(12) 它确实满足不交加性；由第4–5节它确实属于 (22)。因此存在一个四次局部 jet 多项式 $L_V$，使
$$
\boxed{
\mathfrak q_u(V)
=\mathcal N_{\mathbf T(V)}(u)
+\int L_V(x,u,u',u'',u''')dx.
}
\tag{29}
$$
其系数可线性依赖 V；选取固定顺序执行上述有限积分步骤即可得到一个线性选择。

特别，
$$
\boxed{
\mathbf T(V)=0
\Longrightarrow
\mathfrak q_u(V)=\int L_V(x,u,u',u'',u''')dx
\quad\text{对所有真实紧 }u.
}
\tag{30}
$$
反过来，局部积分自动具有不交加性，再由 (9) 得 $\mathbf T(V)=0$。所以这是完整 self 在本题上的准确局部性判据。

因为第4.2、5节只给最高 jet 的线性项和双核增加局部 $C^2$ 项，R295 的主式保持：
$$
L_V=-\frac18\mathcal K_V(x;u,u',u'')(u''')^2
+\mathcal L_{V,\le2}(x;u,u',u'').
\tag{31}
$$
$\mathcal K_V$ 是原生成式 (23) 的真实线性组合，$\mathcal L_{V,\le2}$ 现在是**局部**四次多项式，而非未解析的 Volterra $C^2$ 余项。M=0 已付的 $u^2$ 主系数仍为零；其他主系数没有由 (30) 自动消去。

因此 T=0 并不意味完整 self 为零、principal 为零或只剩低阶。R298、R310、R313 的非零零矩响应都与 (30) 一致，且给了具体局部实例。

## 8. 九矩是准确的非局部商，不冒实际负成本

令 $\mathscr Q=\mathcal Q_{\rm all}(U_{\mathrm p0})$，令
$\mathscr Q_{\rm loc}$ 为其中可由局部三阶 quartic 密度表示的子空间。
(8) 表明 $\mathbf T$ 只依赖 q，不依赖成本代表。第7节给
$$
\ker(\mathbf T:\mathscr Q\to{\rm Mat}_3)=\mathscr Q_{\rm loc}.
$$
R297 的九个真实 pure-zero 响应已使 $\mathbf T$ 满射。因此
$$
\boxed{0\longrightarrow\mathscr Q_{\rm loc}
\longrightarrow\mathscr Q
\xrightarrow{\ \mathbf T\ }{\rm Mat}_3(\mathbb R)
\longrightarrow0}
\tag{32}
$$
是准确的有限维实向量空间序列。

(11) 是在较大 quartic 函数类中的一个明确商代表，不先断言每个 $\mathcal N_A$ 单独就是某个 canonical 成本的 self。若需要在真实响应空间内选代表，可用 R297 九列：它们具有给定 T，同时保留其自己的局部项；那些局部项不得丢弃。

式 (32) 是完整函数像与真实响应的线性结论，不等于一个任意符号路径可直接实现。实际控制仍使用 R222/R297 的保基准有限复制与全 pure 校正。

## 9. 局部 self 的忠实有限 Euler 坐标

第7节允许后继用局部多项式，而不再重新编完整 Volterra forcing。对
$$
L(x,u_0,u_1,u_2,u_3),
\quad u_j=D^ju,
$$
定义
$$
\mathcal E(L)=
\frac{\partial L}{\partial u_0}
-D\frac{\partial L}{\partial u_1}
+D^2\frac{\partial L}{\partial u_2}
-D^3\frac{\partial L}{\partial u_3}.
\tag{33}
$$
它是关于 $u_0,\ldots,u_6$ 的三次多项式，x 系数仍有限多项式。将全部字面系数作为一个有限向量。

对本题四次齐次、紧端的 L，有准确等价
$$
\boxed{\int L(u)=0\text{ 对所有真实紧 }u
\iff \mathcal E(L)=0\text{ 为字面多项式}.}
\tag{34}
$$
必要性由真实紧变分和任意局部 jets 的实现得出。充分性可直接用齐次恒等：将
$\sum_{j=0}^3u_jL_{u_j}=4L$ 逐项分部积分，得到
$$
4L=u\,\mathcal E(L)+D\mathcal B_L.
$$
紧端使边项准确为零。故 (34) 不依赖一个可能不完备的 NF。

两种局部 L 若代表同一个完整 self，它们的 Euler 多项式相同。因此一份完整的忠实 self 坐标可以取为
$$
\boxed{\left(\mathbf T(V),\ 
\text{全部 }\mathcal E(L_V)\text{ 的字面系数}\right).}
\tag{35}
$$
零坐标准确等价于完整 self 函数零；T 和 Euler 两部分都必须检查。对未知新目标，不能只凭 principal 矩阵或已付九矩宣零。

U 有限维及原递推有限保证实际使用的 x 次数与单项集合有限。这里未把一个尚未展开的保守次数上界或单项个数冒成真实维数。下一消费者应从已绑定原生成公式输出实际有限支撑，并据 (34) 做准确有理关系和独立原差核验。

## 10. 后继最小原式工作的边界

新结论把可消费问题缩为：

1. 从 R295 的完整二阶原表达、真实左矩项和有限 s 系数表示生成 (22)，保 (20) 的左常数；
2. 采用固定的 (23)–(24) 顺序，输出九个双核及完整局部密度；
3. 对真 $\mathbf T=0$ 的目标，使用本文已证身份消掉正规双核，再输出全部 Euler 坐标；
4. 对响应，优先消费 R261 已存的全 Z 局部 c 与原 E8；其完整 self 为 $-\frac14\int c_{\tau,u}\Phi_E(u,u)$，不重新恢复八 χ 或 3974 个旧 forcing；
5. 若声称已覆盖整个 $\mathcal R_{\mathrm p0}$，还须保 R247 分解中的其他完整 pure 核分支，不能把 $Z18\times E8$ 自动当成全部响应。

本稿不报告任何新矩阵秩，不宣称 $\mathscr Q_{\rm loc}$ 已由现有十五方向覆盖，也不从局部化推出 fixed-circle 的全部 period/ruling 相容。它给的是一个完整、可核、有限且忠实的原式接口：所有非局部 self 信息恰由原有序九矩承载，其余真实缺口可以在局部四次 Lagrangian 的 Euler 坐标中比较。

作者责任：所有边界、Fubini 和 Euler 步骤均在文中显示；没有新的实际消元、原根恢复或研究运行。
