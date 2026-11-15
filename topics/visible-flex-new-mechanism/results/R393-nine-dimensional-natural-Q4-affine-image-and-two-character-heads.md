# R393：完整 Q4 自然通量的九维仿射像与两个尚须全层检验的字符头

日期：2026-11-15。**完整纸面原式证明；没有执行新的 profile、积分、符号程序、原根、秩、人工检查或科学运行。**

[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md)
已给完整四次速度正规成本的准确自然通量。本稿把这一整个族的自然函数像归约为九维，
给出真缩放权、完整平移作用与两个字符头，并写出它们在本层的准确 action。

这个结论同时指出增强联合控制必须保留的一项实际义务：
**Q4 自然像没有零权，并不自动消去增强商的负权正字符。**
这里的两个字符头在 Q4 层上都具有非负的四次速度式。
本稿不把它们宣布为整个原 $U$ 的非负字符；原静态与速度二次层仍须用完整密度检验。

## 1. 原成本、自然读出和真正的十四族

固定共同右 collar $r_*$ 与同一个实际 profile 窗口 $I$。
所有 primitive 都是原
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
对实紧 $u\in C_c^\infty(I)$，采用
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)
的原自然读出
$$
\boxed{
\Lambda_u(V)=
\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
}
\tag{1}
$$
其中
$$
\mu(u)=
\left(
\int(u'')^2,\;
\int x(u'')^2,\;
\int\{x^2(u'')^2+2(u')^2\}
\right).
$$
$\mathscr G$ 是原 pure 的有序 $2+2$ 真三矩尾映射。
它不是可自由改变的补偿，也没有把有尾的中间场当成紧场。
式(1)在整个真实 $U$ 上定义，杀掉全部真实响应 $\mathcal R$。

原 [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、
[R134](R134-acceleration-layer-from-complete-local-v4.md) 给
$$
U=\mathcal R+\operatorname{span}
\left\{
F_0,\ \widehat Q_2\text{ 的三个系数},\
\bar A_{hh},\bar A_{hk},\bar A_{kk},\
H_1,H_2,\
\widehat Q_4\text{ 的五个系数}
\right\},
\tag{2}
$$
右边取所有实际状态值。这是十四个函数族，不是十四维断言。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
与 [R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)
已分别支付加速度平方和更正后完整 H 层的自然读出为零。
但式(2)中仍有 $F_0,\widehat Q_2$。
[R109](R109-local-density-of-the-complete-fourth-quotient.md) 的原式明确保留
$$
\begin{aligned}
L_0&=v_0-\mathcal B_{m_0}N_0,\\
L_2&=v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0.
\end{aligned}
\tag{3}
$$
此外 $F_0$ 减去同一个 $\Gamma m_0$，
速度二次正规式减去 $\Gamma m_2$ 并保原水平分部积分。
本稿不删除这些项，不由 Q4 推出 $\Lambda(U_0)=0$。

## 2. 完整 Q4 公式和本稿的函数像

写
$$
v=u',\qquad r=u'',\qquad t=u''',
\qquad e=hx+d,\qquad Q=1+e^2,\qquad d=h\omega-k.
$$
真实水平速度取
$$
\gamma=h_s,\qquad \delta=d_s,\qquad
l=\gamma v-(\gamma x+\delta)r.
$$
R386 已从原 $YC$、$ZZ$、全部 history 导数、完整 $N_2$ 校正和两份有序真尾证明
$$
\boxed{
\Lambda_u\bigl(\mathcal Q_S[\gamma,\delta]\bigr)
=-\frac1{32h^8}\int Q\,l^4t.
}
\tag{4}
$$
$\mathcal Q_S[\gamma,\delta]$ 是原实际 $U$ 内完整正规四次速度系数的值。
式(4)没有未定的 $C^2$ 或尾余项。

令 $\mathscr A_4$ 是所有(4)在 $u$ 上的函数的实线性跨度。
这仅定义一个实际线性像；负系数线性组合未被称为真实路径。

置
$$
L=v-xr,\qquad
D_{j,k}(u)=\int x^kL^{4-j}r^jt,
\qquad 0\leq j\leq4,\quad0\leq k\leq2.
\tag{5}
$$
因为 $l=\gamma L-\delta r$，
$$
\begin{aligned}
\Lambda_u(\mathcal Q_S[\gamma,\delta])
=-\frac1{32h^8}\sum_{j=0}^4
{4\choose j}(-1)^j\gamma^{4-j}\delta^j
\bigl\{(1+d^2)D_{j,0}+2hdD_{j,1}+h^2D_{j,2}\bigr\}.
\end{aligned}
\tag{6}
$$
因此 $\mathscr A_4$ 包含于十五个(5)的跨度。

反向也准确成立。固定任一正 $h$，在一个实际状态开盒内改变 $d$：
$d^2,d,1$ 的三个系数依次给 $D_{j,0},D_{j,1},D_{j,2}$；
再对速度的二元四次多项式取有限线性系数，得到每个 $j$。
这只是有限维多项式系数与有限真实状态值具有相同线性跨度。
可先选 $k$ 与共同窗口，使该小盒始终有 $x+\omega>0$；
没有用非物理状态或改变右锚。故
$$
\mathscr A_4=\operatorname{span}\{D_{j,k}\}.
\tag{7}
$$

## 3. 六条完整分部积分关系

紧 $u$ 给 $L'=-xt$。两 collar 上 $L,r$ 都为零，所以
$$
D_{4,0}=0.
$$
另对 $L^{5-j}r^j$ 作一次普通分部积分，
$$
(5-j)D_{j,1}=jD_{j-1,0}
\qquad(0\leq j\leq4),
\tag{8}
$$
$j=0$ 时右端解释为零。
因此
$$
\boxed{
\begin{aligned}
D_{0,1}&=0,&
D_{1,1}&=D_{0,0}/4,&
D_{2,1}&=2D_{1,0}/3,\\
D_{3,1}&=3D_{2,0}/2,&
D_{4,1}&=4D_{3,0},&
D_{4,0}&=0.
\end{aligned}}
\tag{9}
$$
这些是完整积分身份，没有只比较主项。

选择九个函数
$$
\begin{array}{c|c}
\text{记号}&\text{定义}\\ \hline
A&D_{3,0}\\
B&D_{2,0}\\
C&D_{4,2}\\
D&D_{1,0}\\
E&D_{3,2}\\
F&D_{0,0}\\
G&D_{2,2}\\
H&D_{1,2}\\
K&D_{0,2}
\end{array}
\tag{10}
$$
由(9)，它们张成 $\mathscr A_4$。

## 4. 准确 C2 呈示及真实独立性

定义局部积分记号
$$
J_{i,k}=\int x^kv^ir^{5-i},
\qquad V_5=\int v^5.
$$
下面只是九个完整函数的分部积分呈示：
$$
\begin{array}{c|l}
A&-J_{0,0}/20\\
B&-J_{1,0}/6+J_{0,1}/10\\
C&-2J_{0,1}/5\\
D&-J_{2,0}/2+J_{1,1}/2-3J_{0,2}/20\\
E&-J_{1,1}/2+7J_{0,2}/20\\
F&-2J_{3,0}+2J_{2,1}-J_{1,2}+J_{0,3}/5\\
G&-2J_{2,1}/3+5J_{1,2}/6-3J_{0,3}/10\\
H&-J_{3,1}+3J_{2,2}/2-J_{1,3}+J_{0,4}/4\\
K&2V_5/5+2J_{3,2}-2J_{2,3}+J_{1,4}-J_{0,5}/5 .
\end{array}
\tag{11}
$$
例如 $H=\frac14\int rL^4$、$K=\frac15\int L^5$；
最后一行还用了 $\int xv^4r=-\int v^5/5$。
全部边项由紧 $u$ 的原 jets 支付，不涉及未知左尾。

每行因而是连续 $C^2$ 五次泛函。
证明九行独立时，不能把不同显示单项先当函数独立。
先用第5节的真实缩放区分不同权；
在同权的两行中，取局部密度 $g(x,v,r)$ 的 Euler 导数。
若 $\int g=0$ 对全部紧 $u$ 成立，则最高 $u^{(4)}$ 系数
$g_{rr}$ 必须作为自由 jet 多项式恒零。

对三对同权函数，$g_{rr}$ 分别为
$$
\begin{array}{c|l}
B&-2vr^2+2xr^3\\
C&-8xr^3\\ \hline
D&-3v^2r+6xvr^2-3x^2r^3\\
E&-6xvr^2+7x^2r^3\\ \hline
F&-4v^3+12xv^2r-12x^2vr^2+4x^3r^3\\
G&-4xv^2r+10x^2vr^2-6x^3r^3.
\end{array}
\tag{12}
$$
各对第一行分别含第二行没有的 $vr^2,v^2r,v^3$ 项；
随后第二行也非零，所以两系数都被迫为零。

单行 $A$ 的 $g_{rr}=-r^3$ 非零。
$H$ 的 $g_{rr}$ 含 $-2xv^3$，
$K$ 的 $g_{rr}$ 含 $4x^2v^3$，也非零。
允许窗口含一个非零坐标的开子区间即可作这些紧局部 jet 扰动；
任何非空开窗口都满足这一点。
于是
$$
\boxed{\dim\mathscr A_4=9.}
\tag{13}
$$
这是原完整函数像的维数，既不是十五个标签数，也不是有限采样秩。

## 5. 真缩放权与完整平移作用

这里使用
[R365 第5节](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)
独立成立的自然读出协变：
$$
\Lambda_u(\mathsf P_{a,c}V)
=a^2\Lambda_{C_{a,c}u}(V),
\qquad
C_{a,c}u(x)=u((x-c)/a),\quad a>0.
\tag{14}
$$
该节的协变与真尾输运独立于后来已撤回的旧 H 非零主张；
本稿仅使用(14)。

对 $D_{j,k}$，
$$
a^2D_{j,k}(C_{a,0}u)=a^{\,k-j-4}D_{j,k}(u).
\tag{15}
$$
所以(10)的真实成本权为
$$
\begin{array}{c|c|c}
\sigma&\text{基}&\text{维数}\\ \hline
-7&A&1\\
-6&B,C&2\\
-5&D,E&2\\
-4&F,G&2\\
-3&H&1\\
-2&K&1 .
\end{array}
\tag{16}
$$
缩放只须在共同支撑合法的 $a=1$ 附近开区间比较。
不同有限幂独立，故第4节按权拆分真实关系是合法的。

令 $\mathsf N$ 表示(14)中输入平移 $c$ 在零点的导数。
对 $C_{1,c}u$ 换元后，显式坐标变为 $x+c$，
而 $L$ 变为 $L-cr$，所以
$$
\mathsf N D_{j,k}
=kD_{j,k-1}-(4-j)D_{j+1,k}.
\tag{17}
$$
若另一文献对平移生成元采用相反号，下列像空间与字符条件完全相同；
本稿固定(17)的方向。

使用(9)，完整作用表为
$$
\boxed{
\begin{array}{c|c}
A&0\\
B&-2A\\
C&8A\\
D&-3B\\
E&3B-C\\
F&-4D\\
G&4D/3-2E\\
H&F/2-3G\\
K&-4H.
\end{array}}
\tag{18}
$$
因此 $\mathscr A_4$ 是一个真正有限、仿射稳定的自然函数子空间。
这里没有断言固定两个 profile 评价的核也仿射稳定。

## 6. 只有两个非零字符头

定义本子空间的单权平移头
$$
\mathfrak h_\sigma
=\mathscr A_{4,\sigma}/
\mathsf N\mathscr A_{4,\sigma+1}.
\tag{19}
$$
由(18)，权 $-7,-6,-5,-3$ 的平移像都是满的；
权 $-4$ 的像是 $\operatorname{span}\{F/2-3G\}$；
权 $-2$ 上方没有非零空间。
故
$$
\boxed{
\dim\mathfrak h_{-4}=\dim\mathfrak h_{-2}=1,
\qquad
\mathfrak h_\sigma=0\ \text{其余权}.
}
\tag{20}
$$

特别，权 $-4$ 的字符可写成
$$
\ell_{-4}(F)=c,\qquad
\ell_{-4}(G)=c/6,
\tag{21}
$$
并在其余权为零。
权 $-2$ 的字符由 $\ell_{-2}(K)=b$ 给出。
这两者均是 $\mathscr A_4$ 上良定义的真实线性读出，杀(18)的全部平移像。
本稿没有将它们未经关系检查延拓到整个 $U$ 或全部自然函数像。

## 7. 两个头在 Q4 层上的完整 action

从(6)中按真权提取 $-4$，只有
$$
-\frac1{32h^8}
\left\{
(1+d^2)\gamma^4F
-2hd\gamma^3\delta F
+6h^2\gamma^2\delta^2G
\right\}.
\tag{22}
$$
代(21)，准确得到
$$
\boxed{
\ell_{-4}\!\left(\Lambda_\cdot(\mathcal Q_S[\gamma,\delta])\right)
=-\frac{c}{32h^8}\,
\gamma^2\left\{\gamma^2+(d\gamma-h\delta)^2\right\}.
}
\tag{23}
$$
因此 $c<0$ 时它在全部实际状态与速度上非负，并且不恒零。

权 $-2$ 只来自 $j=0,k=2$，所以
$$
\boxed{
\ell_{-2}\!\left(\Lambda_\cdot(\mathcal Q_S[\gamma,\delta])\right)
=-\frac{b}{32h^6}\gamma^4.
}
\tag{24}
$$
$b<0$ 时同样非负且不恒零。

式(23)(24)是**完整 Q4 系数族的四次速度 action**。
它们不是把 Q4 单项变成一条没有其它成本的实际路径；
也没有证明全部路径成本非负。
实际路径还有(3)及其基准、原型、矩阵和端点势。

## 8. 对 R392 后继联合商的准确影响

[R392](R392-real-joint-control-of-response-E-components-and-two-natural-fluxes.md)
已支付响应 $E$ 分量与固定两个自然通量的实际联合截面，
并明确保留
$$
\mathscr C=E(U)/E(\mathcal R)
$$
中的全部非零基准。下一实际问题是同一条路径上同时控制
$\mathscr C$ 与这些通量。

本稿提供可直接使用的完整事实：

1. Q4 自然函数像恰是(13)，真权恰为(16)，没有零权。
2. 它的仿射结构与平移头由(18)–(21)完全给出。
3. 原 $F_0$ 与三个 $\widehat Q_2$ 仍在(2)中；不能由第1点推出整个自然像没有零权。
4. 即使未来证明全自然像没有零权，增强的负权字符仍须重新检验。
   例如(23)是一个明确的非负最高速度型。
   [R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)
   的 $E(U_{-4})=E(\mathcal R_{-4})$ 只描述旧投影 $E$；
   新自然读出杀 $\mathcal R$，不因该旧等像而被删除。

尤其，式(23)既没有证明原 $U$ 存在新的正字符，
也没有证明实际联合控制不可能。
决定它能否延拓或是否被低层项破坏的下一对象，
是(3)加原 $\Gamma$、原水平正规势后的**完整**静态和速度二次 action。
任何正面实际联合结论还必须保有限正核、同一个有限构造、
非零原型成本、真实倒行、矩阵/端口桥和完整基准。

本稿没有改变已经发表的 whole $E$ 实际控制或 R390 的固定两通量实际控制；
也没有把二者分开可达拼成未经证明的同一路径联合可达。
