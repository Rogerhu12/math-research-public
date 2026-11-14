# R309 — 三条真实 j=0 来源的四次像、倍点导子与同一 $q=2$ 有限像

日期：2026-11-13。**状态：以下真实三源环的四次归一化、完整导子、原次数二与原点一阶的最小代价、固定坏集上的 primitive 角向格、倍点 theta 身份、同一原加权前缀的完整矩阵及首次核均已证明。只使用原 $H_1$ 的中央导数零作为待反驳条件；没有给 $H_3,H_5$ 的斜率赋值，也没有将整个三源代数置成中央零。**

## 1. 三原来源及准确的公共 carrier

固定 $b=17$，也保留固定齐次换标到 $b=1$ 的写法。R306/R307 的三个原截面为
$$
H_i=\sigma^{34}x^2P_i(x^3),\qquad i=1,3,5,
$$
其中 $H_1=S=z^6+\cdots$，$H_3(0)=H_5(0)=1$。本篇使用实际线性缩放
$$
X=7bH_1,\qquad Y=H_3,\qquad Z=H_5.
\tag{1}
$$
它不依赖权，且在所用好素数处为单位。令
$$
t=-b/x^3,\qquad F=\Theta^{17}=\sigma^{34}x^{17},\qquad
\rho=F(1+8t)=\sigma^{34}x^{14}(x^3-8b).
\tag{2}
$$
准确有
$$
\boxed{(X,Y,Z)=\rho\,(a(t),b_0(t),c(t)),}
\tag{3}
$$
$$
\begin{aligned}
a&=16t^4-12t^3+3t^2-7t,\\
b_0&=256t^4+1472t^3-1200t^2+200t+1,\\
c&=-128t^4-832t^3+1968t^2-280t+1.
\end{aligned}
\tag{4}
$$
这里 $1+8t$ 是三条**实际**角多项式的完整共同因子；没有把这个因子从原 Mellin 变换中删除。$\rho(0)=1$，三个来源的 theta degree 都是 $34$。

## 2. 四次像及其真正的两个奇点

三个四次齐次形式无共同基点。事实上
$$
\operatorname{Res}_t(a,b_0)=2^{16}3^{18},
\tag{5}
$$
且二者在无穷处的最高系数均非零。原射影像的隐式方程是
$$
\begin{aligned}
\Phi={}&1327104X^4-221184X^3Y-442368X^3Z\\
&-41472X^2Y^2-76032X^2YZ-20736X^2Z^2\\
&-96XY^3-288XY^2Z+288XYZ^2+96XZ^3\\
&+7Y^4-4Y^3Z-9Y^2Z^2+2YZ^3+4Z^4.
\end{aligned}
\tag{6}
$$
下面三个明确的 conic 同时给出归一化的有理逆：
$$
\begin{aligned}
C_0&=\frac{-1152X^2+336XY+432XZ-3Y^2+YZ+2Z^2}{7776},\\
C_1&=\frac{-1152X^2+192XY+288XZ+3Y^2+YZ-4Z^2}{31104},\\
C_2&=\frac{4608X^2+672XY+288XZ+9Y^2-4YZ-5Z^2}{62208}.
\end{aligned}
\tag{7}
$$
置
$$
d(t)=t(t-1)(8t^2+20t-1)^2.
$$
直接代入得到完整多项式恒等式
$$
\boxed{C_j(a,b_0,c)=t^jd(t)\quad(j=0,1,2),\qquad
C_1^2-C_0C_2=\frac{\Phi}{2^{14}3^8}.}
\tag{8}
$$
故 $t=C_1/C_0$ 给泛点处的逆。无基点的四次参数化因此确为四次整曲线的归一化，而不是次数二的多重参数化。这些恒等式在所有特征大于三处同样成立。

原点的射影像 $[0:1:1]$ **不是光滑点**。它的两个归一化原像是 $t=0,1$。在局部坐标 $(X/Y,Z/Y-1)$ 中，两条切向量分别为
$$
(-7,-480),\qquad (1/27,-32/9),
$$
行列式为 $128/3$。所以这里是普通节点，两个分支的导子指数各为一。

令 $g_2=8t^2+20t-1$。它的两个根都映到 $[-1:24:-24]$。
在此点的坐标
$$
\xi=X/Y+1/24,\qquad \eta=Z/Y+1
$$
下，模 $g_2$ 准确有
$$
\xi'=-\frac{8t+19}{54},\qquad \eta'=0,\qquad
\frac{\eta''}{2(\xi')^2}=\frac{128(8t+19)}3.
\tag{9}
$$
两条分支均光滑；其切线相同、二次项不同，因此该点是普通 tacnode，两条分支的接触重数为二。这里不是两个 cusp。$g_2$ 判别式为 $432$，且 $\operatorname N(8t+19)=-27$，所以这些断言也在所有特征大于三处保持。

节点的 $\delta$ 不变量为一，tacnode 为二；它们已用尽平面四次曲线的算术亏格三，故没有其他奇点。局部节点的导子阶为 $(1,1)$；两条接触二次的光滑分支的局部环可写成
$k[[\xi,\eta]]/((\eta-f_1(\xi))(\eta-f_2(\xi)))$，其中 $f_1-f_2$ 为 $\xi^2$ 乘单位，故导子阶为 $(2,2)$。因此归一化上的完整导子除子准确是
$$
\boxed{\mathfrak D=(0)+(1)+2(g_2=0),\qquad \deg\mathfrak D=6.}
\tag{10}
$$
特别，次数一的非零导子截面不存在；次数二时 (7) 给出完整三维导子空间。任何导子都必须在原点分支至少消失一次，(7) 的 $C_0$ 恰消失一次。

## 3. 固定坏集上的真实 primitive 角向格

令 $\mathcal R=\mathbf Z[1/(42b)]$，并令
$$
\mathcal A=\mathcal R[X,Y,Z]/(\Phi),\qquad
\mathcal B=\bigoplus_{m\ge0}H^0(\mathbf P^1,\mathcal O(4m)).
\tag{11}
$$
其实际参数化为 (3)。$\mathcal B_m$ 中的元素在原函数域中表示为
$\rho^m q(t)$、$\deg q\le4m$。

有理函数 $t$ 与 $\rho$ 代数独立。若 $\rho$ 在 $\mathbf C(t)$ 上代数，则沿椭圆曲线的周期平移只能有有限多个代数分支；而原 sigma 自动因子使非零 $\rho$ 乘上
$\exp(34\eta_\lambda z+\text{常数})$。取准周期 $\eta_\lambda\ne0$ 的周期并迭代，会给无限多个不同分支，矛盾。因此 (11) 的源环没有漏掉一个额外解析关系。

以下包含对**所有**非负次数成立：
$$
\boxed{C_0\mathcal B_m\subset\mathcal A_{m+2}.}
\tag{12}
$$
这里有不依赖抽象导子定理的整数证书。证书给出五个齐次三次多项式 $Q_j$，满足
$$
d(t)t^j=Q_j(a(t),b_0(t),c(t)),\qquad 0\le j\le4.
\tag{13}
$$
其全部系数分母的最小公倍数为 $2^{12}3^{11}$；精确五行十列系数随脚本保存。
又由 (5)，四次齐次形式 $a,b_0$ 在 $\mathcal R$ 上构成无基点 pencil。
二元多项式的 Koszul 序列说明
$a\mathcal B_m+b_0\mathcal B_m=\mathcal B_{m+1}$ 对 $m\ge1$ 成立；等价地，$\mathcal B$ 作为 $\mathcal A$ 模由 $\mathcal B_0,\mathcal B_1$ 生成。于是 (13) 与 $C_0\in\mathcal A_2$ 立即递推得到 (12)。没有为不同 $m$ 分别删去新素数。

乘 $d(t)$ 的像在每个二元多项式格中都是 primitive：$d(t)$ 的一次系数为 $-1$，所以它模任意素数都不是零多项式；在剩余域多项式整环中乘它是单射。因而 (12) 的每个有限 graded 截断在原 $\mathcal A$ 中亦 primitive。

现在取真正首项一的导子函数和角参数
$$
\boxed{\mathcal D=\frac{C_0(X,Y,Z)}b
=\frac{\rho^2d(t)}b=z^6+\cdots,\qquad q=-t/b=x^{-3}=z^6+\cdots.}
\tag{14}
$$
则以下全部列都在原整数源中：
$$
\boxed{\Omega_{m,j}=\mathcal D\rho^m q^j\in\mathcal A_{m+2},
\qquad 0\le j\le4m.}
\tag{15}
$$
其来源次数为 $m+2$，theta degree 和公共 sigma 指数均为 $34(m+2)$。原 Euler 质量是 $m+2$，不能先改成 $m$。

令 $n=D-2$，使用 (15) 的全部 $0\le m\le n$ 列，秩准确为
$$
2n^2+3n+1=2D^2-5D+3.
\tag{16}
$$
完整四次源 $\mathcal A_{\le D}$ 在 $D\ge2$ 时秩为 $2D^2+2$，所以这份真实 primitive 子格只损失 $5D-1$ 维。
由 (13) 及上述固定 Koszul 表示，也可为所有列选取分母与系数范数至多指数增长于 $m$ 的原多项式代表。这保留了全局 theta 来源的线性高度成本；没有把单独的有极 $q$ 当成全局整函数。

## 4. 导子的真实倍点来源

原倍点式给
$$
\tau(t):=t(2z)=\frac{64t(1-t)^3}{(1+8t)^3},
$$
$$
\boxed{\tau(t)-1=-\frac{g_2(t)^2}{(1+8t)^3},\qquad
\tau'(t)=-\frac{64(t-1)^2g_2(t)}{(1+8t)^4}.}
\tag{17}
$$
故节点的 $t=0,1$ 分别是 $O$ 与非零二挠类，均在 $[2]$ 下映到零；tacnode 的两个归一化原像是映到非零二挠类的四挠类。这里是实际倍点 $[2]$（次数四），没有假定存在范数二的最大整环 CM 元素。

更强地，(14) 是完整 theta 乘积：
$$
\boxed{\mathcal D=
\frac1{16}\sigma(z)^4\sigma(4z)^2\Theta(z)^8\Theta(2z)^2.}
\tag{18}
$$
证明用准确的
$$
\sigma(2z)=-2y\sigma^4,\quad
\sigma(4z)=-4y(x^6+20bx^3-8b^2)\sigma^{16},
$$
$$
\Theta(2z)=x(x^3-8b)\sigma^8.
$$
两边均为
$\sigma^{68}x^{10}y^2(x^3-8b)^2(x^6+20bx^3-8b^2)^2$。
总 degree 是 $4+32+16+16=68$，原点首项是 $z^6$，全体零都由显示的固定挠点给出。

物理倍点尺度不能在下一位中省略。若 $d=p+1$、
$c_p=[z^d]\log(\sigma/z)$，则 (18) 中 sigma 的首坏部分与公共 degree-$68$ frame 的差含准确整项
$$
\boxed{\left(4(2^d-4)+2(4^d-16)\right)c_p\in\mathbf Z_p.}
\tag{19}
$$
其整性来自 $2^d\equiv4$、$4^d\equiv16\pmod p$ 及 $pc_p$ 整。
其余 $\log(xz^2)$ 部分同样整，必须一起保留在真实整轴里。
式 (19) 并不为完整 Mellin 变换新增一个倍点等变性；它只支付 (18) 在下面同一有限目标中的原尺度。

## 5. 同一原 $q=2$ 目标上的完整矩阵

取惰性好素数
$$
p=6s-1>7,\quad p\ne17,\qquad k=2s+\ell,\quad0\le\ell<s,
\qquad w=z^6.
\tag{20}
$$
记 $c_p=[w^s]\log(\sigma/z)$、$\kappa=34c_p$、$a_p=p\kappa$。
R301 已证明 $a_p$ 是单位。原椭圆对数 (2) 到次数 $<3s$ 整；在
$6n(6n-1)$ 中，$n<3s$ 只有 $n=s$ 出现 $p$。因此真实有限轴
$$
g(w)=e^{-\kappa w^s}\rho(w)\pmod {w^k},\qquad q(w)=x(z)^{-3}\pmod {w^k}
\tag{21}
$$
全部整，且 $g(0)=1,q(w)=w+\cdots$。这里 $g$ 包含原高轴全部整系数，不是任意选择的低对数提升。$k<p$，所用指数阶乘都是单位。

置
$$
T_k=\mathbf Z_p[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad e_2(x)=1+x+x^2/2.
\tag{22}
$$
它的整数基是 $w^j,\epsilon w^j$（$0\le j<s$）和
$\epsilon^2w^j$（$0\le j<\ell$），对应原权
$e_r=\lfloor r/s\rfloor$。在同一个实际有限格
$$
V_n=\bigoplus_{0\le m\le n,\,0\le j\le4m}\mathbf Z_p R^mQ^j
$$
上定义
$$
\boxed{J(P)=P\bigl(g(w)e_2(a_p\epsilon),q(w)\bigr).}
\tag{23}
$$
这就是 $\rho,q$ 的原加权前缀评价。令 $\mathcal M=R\partial_R$，
$W_i=(\mathcal M^iP)(g(w),q(w))$，并写
$\mathscr S(H)=w^{-s}(H-[H]_{<s})$。三个完整整数块为
$$
\boxed{\begin{aligned}
J_0&=[W_0]_{<s},\\
J_1&=[a_pW_1+p\mathscr S(W_0)]_{<s},\\
J_2&=[a_p^2W_2/2+pa_p\mathscr S(W_1)+p^2\mathscr S^2(W_0)]_{<\ell}.
\end{aligned}}
\tag{24}
$$
这保留了真实 $a_p$ 的下一位、全部原轴系数和两次进位；$\mathscr S$ 只是普通系数移块，不是在零因子环中除以 $w^s$。

## 6. 只支付一阶导子移位，Smith 代价至多二

由 (14)、(21)，原导子在 (22) 中准确为
$$
J(\mathcal D)=w\,U_k,\qquad
U_k=g(w)^2\frac{d(t(w))}{bw}\,e_2(2a_p\epsilon)\in T_k^\times.
\tag{25}
$$
其常数为一。(18)、(19) 的全部尺度与整修正都包含在这个真实单位中。
故 (15) 的整个原矩阵经**同一个**整数单位行操作，成为
$P\mapsto wJ(P)$。没有按列另选 gauge，也没有删去原点的一阶零。

将输入评价缩到长度 $k-1$，这个乘法准确是先移一行，再在
$$
r=s-1,\quad r=2s-1\qquad(0\le r<k-1)
\tag{26}
$$
各乘一次 $p$；其他行不乘 $p$。因此对每个精度 $N\ge1$，
若 $B_N$ 表示全部 Smith 指数的截断和，则
$$
\boxed{0\le B_N(J_{\Omega,<k})-B_N(J_{V,<k-1})
\le\left\lfloor\frac{k-1}{s}\right\rfloor\le2.}
\tag{27}
$$
证明是两个目标整数格相差至多两条指数为 $p$ 的对角行；乘法在特征零上单射，零 Smith 方向数不变。相同格的指数为 $p^e$ 时，任意截断的 Smith 长度差都在 $0,e$ 之间。

这里来源次数二和原点一阶分别付出，不能把二者混成零成本。另一方面，这个代价也没有被扩大为每条来源一次：是整个同一矩阵的至多两条边界行。

## 7. 原首次核的明确 Hermite–Padé 形式

置 $r=s-1$、$h=\max(\ell-1,0)$。由 (24)–(26)，原 (15) 的模 $p$ 核准确为
$$
\boxed{\begin{aligned}
P(g,q)&=0\pmod {w^r},\\
(\mathcal MP)(g,q)&=0\pmod {w^r},\\
(\mathcal M^2P)(g,q)&=0\pmod {w^h}.
\end{aligned}}
\tag{28}
$$
$h=0$ 时最后一行为空。原首两块的末行因 (26) 恰不参加模 $p$ 核；高精度时仍必须回到 (24)，不能继续把它们删除。

由于 $q(w)$ 首系数为一，可仅为读取 (28) 作同一个整的角向换参。
在 $\mathbf F_p[q]/(q^r)$ 内，所需单位准确为
$$
\boxed{f(q)=(1-8bq)\exp\left(
\sum_{1\le j<r}\frac{17}{3j}
\frac{(1/3)_j}{(5/6)_j}(-bq)^j\right).}
\tag{29}
$$
首坏项从 $q^s$ 才开始，所以 (29) 的系数就是原 $\rho(q)$ 的真实低系数。
式 (28) 可等价地在 $R=f(q)$ 处读出。

如果在**完整**目标中也改成角变量 $q$，必须同时将
$\epsilon$ 乘以 $(q/w)^s$；径向指数相应变成
$a_p h(-bq)^{p+1}$，其中 $h$ 是 R305 的原椭圆对数。
这一完整因子在模 $p^2$ 带有 $h^p$ 的真正下一位，不能从 (29) 的首次核公式推成任意精度的免费换参。

还有一个保留全部有限次数预算的多项式写法。先对整个矩阵乘同一个单位 $R^{-n}$，令 $U=R^{-1}$。原 $V_n$ 准确变成
$$
\mathcal W_n=\operatorname{span}\{q^jU^i:j+4i\le4n\}.
\tag{30}
$$
这是一次共同目标单位操作后的原列，不是加入负 charge 来源。
原实际单位 $\rho^{-1}$ 的前五项是
$$
\begin{aligned}
T_4(q)={}&1+\frac{154}{15}bq+
\frac{207598}{2475}b^2q^2+
\frac{74793772}{111375}b^3q^3\\
&+\frac{2270761219726}{422668125}b^4q^4,
\end{aligned}
$$
$$
\rho^{-1}-T_4
=\frac{39511246126891196}{919303171875}b^5q^5+O(q^6).
\tag{31}
$$
这些是固定特征零系数。删去其有限分母及第五系数分子的素数后，记
$\varphi(q)=f(q)^{-1}-T_4(q)$，则 $\operatorname{ord}_q\varphi=5$ 且首系数为单位。

因为 $\deg T_4\le4$，代换 $V=U-T_4(q)$ 在 (30) 上是一个真正的整数多项式自同构。于是原首次核又准确等价于
$$
\boxed{
Q(q,\varphi)=0\pmod {q^r},\qquad
Q_V(q,\varphi)=0\pmod {q^r},\qquad
Q_{VV}(q,\varphi)=0\pmod {q^h},
\quad \deg_q+4\deg_V\le4n.
}
\tag{32}
$$
Euler 导数换成普通 $V$ 导数只用了 $f(0)=1$ 和前面两条零条件，未假定任意 Hasse 偏导已具备原高精度。

这一写法至少给出一个明确的原单位 Schur 块。$q^jV^i$ 的首阶是 $j+5i$；可选择 $i=0,0\le j\le4n$，再选择
$q^{4(n-i)}V^i$（$1\le i\le n$），得到连续首阶 $0,1,\ldots,5n$。
若 $5n+1<s$，将导子乘回后仍全部处于零权带，给原矩阵的 $5n+1$ 阶单位 minor。其余 $2n(n-1)$ 个方向的真实核由 (32) 决定；本篇没有宣称这个剩余 Padé 矩阵正常，也没有从该单位 Schur 块推出新的深 Smith 比例。

## 8. 完整中央条件仍只按已付范围使用

R301/R303 给的是原 $H_1$ 的完整中央判据。R308 已支付 $H_3,H_5$ 的普通全部 $p$-core、单位质量及环带；惰性参考的质量为一，但两条完整斜率仍未被确定。故本篇的原格
$\mathcal A_{\le D}$ 是一份真实、成本明确的来源代数，不是已知全体满足中央零的代数。

后续可以在 (24)、(28) 或 (32) 中寻找由原完整中央失败**真正强迫**的低次数 primitive 深关系。不能直接把 (15) 的全角带置零，也不能把 (18) 当作 Mellin 的乘法商。节点和 tacnode 的倍点来源、真实一次行移位、两条边界的 $p$ 以及所有原 charge 都已在上述公式中保留。

## 9. 精确证书

- [check-jzero-three-source-quartic-conductor-and-q2.py](../scripts/check-jzero-three-source-quartic-conductor-and-q2.py)
- [check-jzero-three-source-quartic-conductor-and-q2.json](../scripts/check-jzero-three-source-quartic-conductor-and-q2.json)

证书核 (3)–(10)、五个完整三次代表 (13)、固定分母、真正倍点式与 theta 乘积、(24) 的三块系数恒等式及 (31) 的固定五阶逆源。所有素数的断言由显示的统一整数格和阶数证明；没有目标素数扫描。
