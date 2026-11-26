# R1046：原 p≡5 mod12 行的全部 CM 系数旗标与真实 MW 消去后非零

日期：2026-11-27（Asia/Taipei；2026-11-26 UTC）。
会话：Astra-serre-24b8836b-20261126；
o1_theta / root；有限求和与接触升阶使用 R1045 已独审的纯代数引理。

**已证明：原 p≡5 mod12 的 Raynaud 最低型，在原有理 CM 圆盘上的
全部模 p 系数构成明确的 Cauchy 旗标；对 R1040 的真实本原
Mordell–Weil 消去泛函，其完整约化多项式在充分大 p 时不恒零。**

这使用实际双中心、双无穷端、图环路及好 BT 因子。
所有环带留数由原 Raynaud 来源准确消去，
不能把 p≡11 mod12 的 compact-type 树直接搬到本行。
完整的 $\bar{\mathcal Q}^2\lambda$ 保留。

非零多项式仍不等于原深盘只有中心零点。最低单位次数、所有更深
子盘的零点排除、原全局覆盖和最终绝对界继续保留原任务。

## 1. 原对象与全部结论

设
$$
p=12g+5\ge41,\qquad N=2g,\qquad
m=6g+2=(p-1)/2,\qquad h=m/2=3g+1,
$$
$$
e_0=m(p+1),\qquad \pi_0^{e_0}=p,\qquad
\varepsilon=\pi_0^m,\qquad \varpi^2=\pi_0.
\tag{1046.1}
$$
全篇保持 R1038–R1040 的原 $X_1,J_1,c_1,D_0$、六标记、
$\kappa_4$ 下降、整 $e_1$、Raynaud 扩张
$0\to T\to G\to B\to0$，以及实际好因子
$$
\mathcal G_1=e_1B[p^\infty]\simeq e_1G[p^\infty].
$$
不声称 whole Jacobian 好约化。

实际超奇异底尾的根集为
$$
S=\{A=0\},\qquad
A=bQ_N(b^3)\text{ 单首},\qquad
\deg A=3N+1=6g+1.
$$
A 的根简单、属于 $\mathbf F_{p^2}$，均避开 $b^3=1$；
本行 j=1728 ordinary，不将它加入 S。
原基和配对为
$$
e_s=\theta_sf_s,\qquad
\omega_s=dX_s/Y_s,\qquad
\langle f_s,\omega_t\rangle=-2\delta_{s,t}.
\tag{1046.2}
$$
两无穷端共同定义 $f_s$，不作单端归一化。

若 $L=\sum_sL_s\omega_s$，R1039 的两个实际中心有同一个首层
$$
\varepsilon R_L(b)\,db,\qquad
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2}.
\tag{1046.3}
$$
原 CM 尾和原盘参数为
$$
D:\quad y^2=x(x^{2g+1}+A_{\rm tail}),\qquad
Q=(0,0),\quad t=\sqrt x,
$$
$$
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varepsilon^3w,\qquad
\lambda_0=(d\bar z/dt)_Q\ne0.
\tag{1046.4}
$$
$\kappa_1,\theta_s,\sqrt{A_{\rm tail}},\lambda_0$ 均为原单位，
不重新归一。

R1039 已证明原 Abel-log 除 $p\varepsilon$ 后为整 Tate 级数，
其完整约化为
$$
\overline{\mathcal H}(w)
 =\sum_{n=1}^{n_0}V_nw^n,\qquad
n_0=(p-2)/3=4g+1=2N+1.
$$
定义
$$
J_i=\sum_{s\in S}\frac{e_s}{(1-s)^{i+2}}\quad(i\ge0).
\tag{1046.5}
$$

**定理 1046.1（原全部旗标）。**
对 $1\le k\le n_0$，令
$$
n_k=(p+1)/3-k=4g+2-k.
$$
则
$$
\boxed{\quad
 V_{n_k}\equiv u_kJ_{k-1}
 \pmod{\langle J_0,\ldots,J_{k-2}\rangle},
\quad}
\tag{1046.6}
$$
其中准确单位为
$$
\boxed{\quad
u_k=
\frac{(-1)^k\kappa_1^k(2\sqrt{A_{\rm tail}})^{3k-2}}
     {m(3k-1)}\lambda_0^{-n_k}.
\quad}
\tag{1046.7}
$$
于是整个实际类型块的系数空间维数准确为 $n_0=4g+1$。

**定理 1046.2（指定真实消去后的全轮廓）。**
对 R1040 的原本原 MW 消去泛函 $\Lambda_{\mathcal Q}$，
当 p 超过该篇及 R1026 的同一个绝对门槛 $C_*$ 时，
$$
\boxed{\qquad
\overline{\Lambda_{\mathcal Q}(\mathcal H(w))}
\ne0\quad\text{作为 }k[w]\text{ 中的多项式}.
\qquad}
\tag{1046.8}
$$
没有新增计算窗口或另选一个便于非零的泛函。

## 2. 本行整个 normal 精度内的实际几何

### 2.1 准确零留数继续适用于全部层

实际微分先取于 $\omega_B$，再经
$\omega_B\hookrightarrow\omega_G\simeq\omega_{\mathcal J^0}$ 拉回原曲线。
R1039 §2 已用 Coleman–Iovita 的原 $N_X=N_J$ 比较证明：
这些微分的每一条环带留数在泛纤维中准确为零，
并由整格无挠整地为零。
证明用 residue 向量同时属于图的 cycle 和 coboundary 空间，
正定边配对迫交为零。

这不是只在特殊纤维上得到零，也不是把原图当成树。
因此在本篇更高 normal 层的全部节点递推中，
同一个实际 $\Omega=e_1\Omega_L$ 仍无遗漏的 simple residue。
原厚度二、六节点及其单位都保持 R1038–R1039 的来源。

### 2.2 两个中心的角色和一般 regular 阶

两个中心各为原 Igusa 曲线的 $C_4$ 商，写成
$$
u^h=h_p(b),\qquad
h_p=r^{2g+1}A,\quad r=1-b^3,\qquad u=\mathfrak a^4 .
\tag{1046.9}
$$
完整惯性会交换两个中心；其偶次子群固定每一个。
R1039 §3.2 保留了两中心并上的实际惯性扩张。
因此原权 m 的微分在中心的可能 normal 层恰为
$$
n=m+j(p+1),\qquad j\ge0,\quad n<e_0,
\tag{1046.10}
$$
相应的局部角色由 $u^{-j}db$ 表示。
此表述作用于两中心并，不将交换中心的惯性误当成单一中心上的标量。

在任一原 CM 节点，$b-1$、u、db 的阶分别为
$$
h,\qquad 2g+1,\qquad h-1 .
$$
故 $u^{-j}db$ 的阶是 $h-1-(2g+1)j$；
其一个 $r^\ell$ Taylor 项的指数为
$$
a=h-1-(2g+1)j+\ell h.
\tag{1046.11}
$$
这里在 regular 输入中只使用 $a\ge0$ 的项。
若使用另一中心的单位 Hodge frame，这些整数和角色不变，
原首系数单位仍保留。

### 2.3 节点传播与双端最高极部

在原节点 $zw=\rho\pi_0^6$，中心第 n 层的 regular 项
$cw^a\,dw$ 传到尾上的首极部为
$$
-c\,\bar\rho^{\,a+1}
 \pi_0^{n+6(a+1)}z^{-a-2}dz.
\tag{1046.12}
$$
由 (1046.10)–(1046.11)，其到达层准确为
$$
n+6(a+1)=(4+3\ell)m,
\tag{1046.13}
$$
而极阶是
$$
(\ell+1)h+1-(2g+1)j.
\tag{1046.14}
$$
所以在当前 $(3k+1)m$ 层，极阶至多 $kh+1$；
若 $j\ge1$，则严格小于 $kh+1$。
唯一最高极部来自第 m 中心层。

这些结论只使用 regular 输入。
当此前当前 b=1 尾的 CM 全层为零时，两个中心在该尾的两个标记
都没有 incoming polar part；其它两个 CM 尾可能已经返回，
必须保留它们的既定主部。
各中心自身的带标记 smooth deformation 取足够大的有效除子
$D_{\rm aux}$，包含 S 及已经出现的其它极点，但避开当前 b=1
标记。先保留那些已指定的主部，再由
$H^1(I_\pm,\Omega^1(D_{\rm aux}))=0$ 提升自身 smooth 余项，
始终在当前标记正则。这里不宣称整个中心仍只在 S 有极，
也不把 $\mathcal F_j$ 的条件扩张到另外两个 CM 尾。
这个消失式不删除 holomorphic 自由项，
也不替代 §2.1 已另行支付的准确 residue 条件。

原两个 ordinary quotient germs 为
$$
b_{{\rm lift},\pm}-1
 =\kappa_1\varepsilon^3\psi_{3,\pm}+\cdots,\qquad
\psi_{3,\pm}
 =\pm z_D^{-h}+\text{较低极阶项},\quad z_D=1/x.
\tag{1046.15}
$$
这是 R1039 的同一个原单位 $\kappa_1$；
惯性交换两端，同时使 $\varepsilon$ 反号，
故这两个首符号不能独立选择。
取第 k 次幂后，双端最高 primitive 符号准确为 $(\pm1)^k$。

## 3. 原 full-Dickson 源和两个无穷端

### 3.1 同一个参考多项式及全部两端常数

保持 R1039 的 full-$p$ 原坐标
$$
C=X^pY-XY^p,\quad
c=A_0^{p+1}-B_0^{p+1},\quad
U=(A_0^{p+1}+B_0^{p+1})/2,\quad V=A_0B_0,
$$
$$
A_{\rm tail}=c^2/4,\qquad
U^2=V^{p+1}+A_{\rm tail},\qquad
x=V^6,\quad y=UV^3,\quad
F=UV^{p-2}=x^{2g}y .
\tag{1046.16}
$$
原整有限角 E 等于 R1038 的真实 $e_1$，包括本行新增的
quadratic principal-series / quadratic Steinberg spectrum；
R1039 §3 已证明 E 在那些新增型上为零，且 $EF=F$。
不恢复任何已撤回的旧 CM 商身份。

定义完整 $\operatorname{GL}_2(\mathbf F_p)$-equivariant derivation
$$
\Theta=X^p\partial_X+Y^p\partial_Y,\qquad
\Theta V=2U,\quad \Theta U=V^p,\quad\Theta A_{\rm tail}=0.
$$
对 $1\le k\le n_0$，置
$$
n'_k=3k-3,\qquad a_k=\frac{(-1)^{n'_k}(n'_k+2)!}{2},
\qquad H_k=a_k^{-1}\Theta^{n'_k}F.
\tag{1046.17}
$$
这与 R1044 的纯 full-source 构造相同；$EH_k=H_k$。

本行每个 CM 无穷端的 x 是 simple pole，$z_D=V^{-6}$。
在 plus 端 $U\sim V^{(p+1)/2}$，每次 $\Theta$ 对最高项的新因子
仍为 $2(j+3)m=-(j+3)$。
在 minus 端每次额外乘 −1；连同 F 自身的负号，共为
$(-1)^{n'_k+1}=(-1)^k$。
因此准确地
$$
\boxed{\quad
H_k|_{\infty_\pm}
 =(\pm1)^k z_D^{-kh}+\text{较低极阶项}.
\quad}
\tag{1046.18}
$$

在原 Q，$t=V^3$、$U(Q)=\sqrt{A_{\rm tail}}$。
唯一最低 V 次项来自每次使用 $2U\partial_V$，给
$$
\boxed{\quad
H_k(t)=
\frac{(2\sqrt{A_{\rm tail}})^{3k-2}}{3k-1}
 t^{n_k}+\text{更高 }t\text{ 次项}.
\quad}
\tag{1046.19}
$$
因为 $p-2-n'_k=3n_k$，该次数准确为
$n_k=(p+1)/3-k$。
整个范围有 $n'_k\le p-5$、$3k-1\le p-3$、$k<p$；
所有显示阶乘与分母均为单位。

### 3.2 真实 full 分歧指数为十二

本行不能使用 p11 的无穷分歧六。
在 full 平面光滑曲线
$$
X^pY-XY^p=c_0Z^{p+1},\qquad c_0\ne0,
$$
每个无穷点的 V 极阶为二，所以原 $x=V^6$ 极阶为十二。
在 (1046.4) 的每个无穷端，x 的极阶为一。
因此实际 full→CM 的每个无穷分歧指数准确为
$$
e=12 .
\tag{1046.20}
$$
它是 tame，且把全部 full 无穷点运输到这两个真实节点。

原 invariant differential
$$
\eta=\frac{dX}{X^p}=\frac{dY}{Y^p}
$$
在仿射无零无极，每个 full 无穷点的零阶是 p−2；
R1044 §3.1 的直接局部计算与 p mod12 无关。
一条当前 CM 微分的双端极阶若至多 kh+1，拉回 full 后至多
$$
12kh+1=6km+1.
$$
所以写成 $f_k\eta$ 后，f_k 在每个 full 无穷点的极阶至多
$$
D_k=6km+p-1=(3k+1)(p-1).
\tag{1046.21}
$$

### 3.3 原全分支齐次化与完整有限角

无穷除子为平面曲线的超平面截面。
由平面 hypersurface 的 exact sequence 及
$H^1(\mathbf P^2,O(a))=0$，f_k 有 degree≤D_k 的多项式代表。
这里用的是 P² 的 H¹，不能换成曲线自身的 H¹ 消失。

原惯性满足
$$
\sigma(\varpi)=\upsilon\varpi,\quad
\sigma(X,Y)=\upsilon^{-1}(X,Y),\quad
\upsilon\in\mu_{p^2-1}.
$$
权 m 的实际 $\Omega$ 在第 $(3k+1)m$ 层的权为
$\upsilon^{-3k(p-1)}$，而 η 的权为 $\upsilon^{p-1}$。
故 f_k 的准确权为 $\upsilon^{-D_k}$。
固定 $C=c_0$ 后，对稳定子 $\mu_{p+1}$ 平均，
仅留下次数 $D_k-j(p+1)$ 的项。
将每项乘 $(C/c_0)^j$，其中 j≥0，便取得 degree D_k 的齐次代表。
全 $\mu_{p^2-1}$ 将全部实际 C 分支传递，
同一个准确惯性权证明这一个多项式在全部分支同时代表原 f_k。
没有给每个分支独立选择相位。

由
$$
D_k\le(p-1)^2<p^2-1,
$$
R1042 的完整 C-过滤与 R1044 的 finite-corner 结论给
$$
\dim E\operatorname{Sym}^{D_k}(k^2)=1.
\tag{1046.22}
$$
这部分只依赖 $p>3$、$(p-1)\mid D_k$ 和实际 E，
本行的 E 已在 §3.1 支付。
非零生成元正是 $\Theta H_k$，因为
$dH_k=(\Theta H_k)\eta$，其 plus 端最高系数为 $-kh\ne0$。

因此当前层的全部实际 E-固定微分，包括未知低极部和
可能出现的 holomorphic 自由项，必是 $dH_k$ 的唯一标量倍。
即使最初齐次代表未先选成 E-固定，也可用
$(E P_k)\eta$ 表示原 E-固定微分，故无需另假设代表的唯一性。
原 full 换基到整个 R/(p) 为常线性，E 逐 normal 层相容。
最大 normal 次数为 $(p-1)m<e_0$，始终没有越过其实际精度。

## 4. 两中心全部 normal 层的归纳

定义
$$
\mathcal F_j
 =\{L:R_L(1)=R_L'(1)=\cdots=R_L^{(j-1)}(1)=0\}.
$$
我们证明，对 $L\in\mathcal F_{k-1}$，
$$
\Omega|_D\equiv0\pmod{\pi_0^{(3k+1)m}},
$$
$$
\boxed{\quad
\overline{\varepsilon^{-(3k+1)}\Omega|_D}
 =\frac{\kappa_1^k R_L^{(k-1)}(1)}{k!}\,dH_k .
\quad}
\tag{1046.23}
$$

k=1 已由 R1039 的完整双节点、自由中心修正与真实 E 证明。
假设此前各层断言已证；在 $\mathcal F_{k-1}$ 上，
所有此前的整个 CM 层为零。
CM 仿射函数和微分的角色都是 3m 的倍数，
故相邻 $(3j+1)m$ 层之间不存在额外层。

两个中心的实际更早输入在 CM 标记正则，理由为 §2.1–2.3。
(1046.13)–(1046.14) 给当前双端极阶≤kh+1，
唯一最高项来自同一个第 m 层 (1046.3)。
本行两中心相同的 $R_L$ 及 (1046.15) 因而准确给
$$
\frac{\kappa_1^kR_L^{(k-1)}(1)}{k!}\,d(\psi_{3,\pm}^k)
\tag{1046.24}
$$
的双端最高部分。
它的 $(\pm1)^k$ 与 (1046.18) 完全相同。
高阶单位和坐标项或者乘此前已经为零的 Taylor 系数，
或者提高 normal 次数、降低当前极阶。

原层在整个 affine CM 尾正则。
任何此时允许的 CM holomorphic 自由项也满足该双端极阶界；
不再以首层时的角色界把它们删除。
§3.3 的真实一维图像遂给 (1046.23)。
若 L 又在 $\mathcal F_k$，该整个层为零，完成归纳。

此证明在两个中心、两个无穷端及所有配对分支同时进行。
没有先在单端固定一个参考 primitive 再冒作全局来源。

## 5. 原 $w$ 盘的准确系数

在 $\mathcal F_{k-1}$ 上，更早 CM 全层都为零。
因此代入原 $\bar z(t)=\lambda_0t+O(t^2)$ 时，
(1046.19) 的最低 primitive 次数 n_k 只乘
$\lambda_0^{-n_k}$。
混合特征坐标的更高 normal 项只作用于以前的零层，
或提高当前 normal 次数。
由于
$$
(3k+1)m+3mn_k=e_0+m,
$$
该项在除去 $p\varepsilon$ 后正好处于单位尺度。
n_k<p，积分分母为单位。
固定 n_k 的更高同角色项相差整 e₀，不再改变模 p 系数；
所有其它次数、包括 p 倍积分次数，继续由 R1039 §8 的完整尾界控制。

所以
$$
[w^{n_k}]\overline{H_\Omega}
 =
 \frac{\kappa_1^kR_L^{(k-1)}(1)}{k!}
 \frac{(2\sqrt{A_{\rm tail}})^{3k-2}}{3k-1}
 \lambda_0^{-n_k}.
\tag{1046.25}
$$
又
$$
R_L^{(k-1)}(1)
 =\frac2m(-1)^{k-1}k!
 \sum_s\frac{L_s\theta_s}{(1-s)^{k+1}}.
$$
使用原 Serre 配对 −2，得到 (1046.6)–(1046.7)。
在整个底空间上只取模前列的同余；
未定的前列倍数没有被置零。

$J_0,\ldots,J_{n_0-1}$ 线性独立：
取 $t_s=(1-s)^{-1}$，这些点两两不同且非零，
任取 n₀ 个根得到 t_s² 乘通常 Vandermonde 矩阵。
故
$$
\boxed{\quad
\langle V_1,\ldots,V_{n_0}\rangle
 =\langle J_0,\ldots,J_{n_0-1}\rangle,\qquad\dim=n_0.
\quad}
\tag{1046.26}
$$
整个底 Hodge 上原轮廓的核维数是
$(6g+1)-(4g+1)=2g=N$。
不把这个核未经比较地命名为旧 deck 空间。

## 6. 指定真实泛函与全部接触条件

全部符号现在取自 R1040 的实际 p5 good BT 因子。
令
$$
r=1-b^3,\quad f=r^{4N+2},\qquad
\bar{\mathcal Q}(a)=\operatorname{quo}(f\,a(b^p),A^2)\bmod A,
$$
$$
\lambda=-6(b+1)/r,\qquad
\bar v=(1-\bar{\mathcal Q})\lambda .
\tag{1046.27}
$$
$a(b^p)$ 保持外部系数不变。
原 $\bar v$ 是实际完整首 log，不是首 formal 项 λ 的替代记号。
同一原对称型为
$$
q_s=-r_s^{4N+2}/A'(s)^2\in\mathbf F_p^\times,\qquad
B(e_s,e_t)=\frac{q_s}{2}\mathbf1_{t=s^p}.
\tag{1046.28}
$$

令 $D=(\delta_*-\delta_*^{-1})/(\zeta-\zeta^2)$
是 R1040 的原非平凡 deck 符号算子，并置
$$
c=D\bar{\mathcal Q}\bar v .
\tag{1046.29}
$$
R1040 已证明：在 p>C_* 时，原负 deck 首 log 非零，
$\bar{\mathcal Q}$ 在该方向单射，所以 c≠0；
c 属于实际 new 部分。
同时 D 与 $\bar{\mathcal Q}$ 在 B 下均自伴、彼此反交换，
故 $D\bar{\mathcal Q}$ 为反自伴，
$$
B(c,\bar v)=0.
\tag{1046.30}
$$
这不是从 B 完美推指定配对非零，而是该特殊真实 c 的额外零关系。
原 MW 消去泛函的约化准确为 $B(c,\cdot)$，因为
$B(\bar v,\bar{\mathcal Q}D\,\cdot)
 =B(D\bar{\mathcal Q}\bar v,\cdot)$。
原 complete MW saturation 的消去和本原性仍直接使用 R1040，
不重新选泛函。

对任意 c，定义唯一次数 <d 的 $T_c$：
$$
T_c\equiv\frac{f\,c(b^p)}{A'}\pmod A.
\tag{1046.31}
$$
完整根集部分分式给
$$
2B(c,J_i)
 =\frac{(-1)^i}{(i+1)!}
   \left(\frac{T_c}{A}\right)^{(i+1)}(1),
 \qquad0\le i\le n_0-1.
\tag{1046.32}
$$
因 $A(1)\ne0$、$n_0+1<p$，若原指定泛函在完整轮廓上为零，
(1046.26)–(1046.32) 准确等价于存在 $\gamma\in k$ 使
$$
(b-1)^\ell\mid T_c-\gamma A,\qquad
\ell=n_0+1=2N+2=(p+1)/3.
\tag{1046.33}
$$

## 7. R1045 的纯代数引理为何适用于原 p5 来源

R1045 的接触升阶与 Euler 排除是纯有限域引理，其完整假设为：
$p=6N+5$、$A=bQ_N(b^3)$ 是上述实际 Hasse、
$\mathcal LA=0$、$f=r^{4N+2}$、λ 与 $\bar{\mathcal Q}$ 为
(1046.27)、$\bar v=(1-\bar{\mathcal Q})\lambda$，以及
c 是非零 new 向量且 $B(c,\bar v)=0$。
这里每一项已由 R1038–R1040 与 §6 实际支付。

特别地：

- $\ell=2N+2$ 始终为偶数，不要求 N 奇。
- $Q_N(1-z)^2=Q_N(z)^2$ 消除了 reflection 中的 $(-1)^N$，
  所以其全部留数与 polynomial part 计算也适用于 N=2g。
- 原 new $T_c$ 的指数准确为
  $
  E=\{0,3,\ldots,3N\}\cup\{2,5,\ldots,3N-1\},
  $
  共 $2N+1=\ell-1$ 个。具体地，
  $\delta_*a(b)=\zeta a(\zeta b)$ 使 new c 的指数为 0、1 mod3；
  保系数的 $c(b^p)$ 将这两类送到 0、2，而 $f/A'$ 为零角色，
  模 A 取唯一代表保持角色。这是实际运输，不由维数相同代替。
- 真正 Hasse、KS、q_s 和首 log 都是本行的原来源，
  不把某个同型的抽象有限根集放进去。

该纯代数引理因而把 (1046.33) 升为
$$
(b-1)^{\ell+1}\mid T_c-\gamma A.
\tag{1046.34}
$$
它完整使用 (1046.30) 及 $\bar v=(1-\bar{\mathcal Q})\lambda$；
不会把 $\bar{\mathcal Q}^2\lambda$ 从 c 中略去。
若 $\gamma=0$，new 指数集 E 的前 $\ell-1$ 阶 jet 矩阵为
一个非零 Vandermonde 乘单位，因全部指数互异且小于 p；
(1046.34) 就迫 $T_c=0$，进而 c=0。
故当前 $\gamma\ne0$。

为明确核准最后排除，令
$$
P_E(\theta_b)=\prod_{e\in E}(\theta_b-e),\qquad
\theta_b=b\partial_b .
$$
它的 order 是 $\ell-1$，且 $P_E(\theta_b)T_c=0$。
(1046.34) 因而迫 $P_E(\theta_b)A$ 在 b=1 至少二阶消失。

原 Hasse 方程给
$$
\frac{Q_N(x)}{Q_N(0)}
 =\sum_{i=0}^N
  \frac{(-N)_i^2}{(2N+3)_i\,i!}x^i.
$$
若 $P_i=P_E(3i+1)$，直接乘积给
$$
\frac{P_i}{P_0}
 =\frac{(4/3)_i(2/3)_i}
        {(1/3-N)_i(2/3-N)_i}.
$$
由于 $2N+3\equiv4/3\bmod p$，有
$$
P_E(\theta_b)A=Q_N(0)P_0\,b\,G(b^3),
$$
$$
G(x)={}_3F_2\!\left(
 \begin{matrix}-N,-N,2/3\\1/3-N,2/3-N\end{matrix};x\right).
\tag{1046.35}
$$
这里表示到 i=N 的有限多项式；G(0)=1、degree N，
全部 Pochhammer 分母及 $Q_N(0)P_0$ 都是单位。
于是 G(1)=G′(1)=0。

写 $b_1=1/3-N,b_2=2/3-N$、$\theta=x\partial_x$。
有限系数逐项满足
$$
\bigl[
\theta(\theta+b_1-1)(\theta+b_2-1)
-x(\theta-N)^2(\theta+2/3)
\bigr]G=0.
\tag{1046.36}
$$
在 x=1+t 处，普通三阶导数的首系数为 −t，
二阶导数的常数系数为 −5/3。
若 $G=a_jt^j+\cdots$、j≥2，
最低 $t^{j-2}$ 系数准确是
$$
-a_jj(j-1)(j-1/3)
=-a_jj(j-1)(j-\ell),
\tag{1046.37}
$$
因为 $3\ell=p+1$。
但 $2\le j\le N<\ell<p$，每个因子均非零，矛盾。

因此 (1046.33) 不可能，证明 (1046.8)。
不需要、也没有单独断言有限和 G(1) 总是单位；
实际 c 的反自伴零关系提供了不可省去的额外一阶接触。

## 8. 原任务中的准确后继范围

两个 p mod12 行现在都有同一个原最低型圆盘的完整 Cauchy
系数旗标，且各自实际 MW 消去泛函的约化轮廓在充分大 p 非零。
本行的证明通过实际 Raynaud 好 BT 因子完成，
没有声称全 Jacobian 好约化，也没有越过本行新的局部类型。

原所有系数已由 R1039 证明整；(1046.8) 又给至少一个系数为单位。
因此实际 MW 消去后的共同尺度也准确为
$$
\boxed{\quad
\min_{n\ge1}v_p\!\left(
 [w^n]\frac{\Lambda_{\mathcal Q}
       (\log\operatorname{Abel}(P(w)-c_1))}{\varepsilon}
\right)=1 .
\quad}
\tag{1046.38}
$$
这里的 $M=1$ 是经过实际 MW 消去之后的结论，
不是从整个类型块的 $M=1$ 自动继承。

这仍只给原 $(p\varepsilon)^{-1}$ 轮廓为非零多项式，
不自动给它在 $v_p(w)>0$ 上的最低单位次数、
低项 Newton 斜率或中心以外的零点。
一般全型秩、指定泛函的全轮廓非零与原深盘排点是三个不同结论。
原课题的全局覆盖、准确有效深度与 Serre 完成标准继续保留。

## 来源与审核范围

- [R1038](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)：
  本行双中心、generic 双节点、原 Hasse/KS、好 BT 因子和完整首 log。
- [R1039](R1039-original-p5-complete-CM-normal-jet-and-rational-disc-scale.md)：
  全环带准确零 residue、实际中心 $u=\mathfrak a^4$、CM 厚度六、
  同一 $\kappa_1,R_L$、真实有限角和原有理盘的无限尾界。
- [R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：
  本行实际 B、$\bar{\mathcal Q}$、deck、CM 谱排除、
  原负首 log 单位及真实 MW 饱和消去。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：
  原 full-$p$ 仿射模型到整个 R/(p) 的常线性 level 作用。
- [R1042](R1042-original-CM-disc-second-column-and-finite-corner.md)：
  完整 C-过滤、终端因子和实际整 E。
- [R1044](R1044-original-CM-disc-complete-coefficient-flag.md)：
  p11 的完整旗标以及与 p mod12 无关的 $\Theta$、η、
  平面齐次化和 finite-corner 证明；本篇重新支付 p5 的全部几何变化。
- [R1045](R1045-original-MW-annihilator-nonzero-reduction.md)：
  原特殊 c 的接触升阶与 Euler 排除；
  本篇 §7 逐条核准其纯代数假设及无 N 奇偶限制的理由。
- [R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)：
  同一个绝对门槛 $C_*$ 与本行已实际接通的负 deck 非零来源。

全部新证明是上述实际原对象上的纸面角色、节点传播、
多项式恒等式和准确源比较。没有数学程序执行，没有重扫旧窗口。
