# R839 — 原最高 CM 类的平移不变性、超椭圆消失与实际 Ceresa 表达

日期：2026-11-16。**状态：以下 Chow 恒等式已证明。**

本篇接续 [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)
及[椭圆平移笔记](../notes/2026-11-15-cm-top-projector-kills-elliptic-translates.md)。
所有等式均为有理等价下的等式。只在权一因子的识别中使用
Jacobian 同态的忠实性；不把高阶动机的某个实现相同当成 Chow 类相同。

## 1. 固定模型与结论

在特征零代数闭域上取原 $j=0$ 曲线 $E_0$，置
$$
A=E_0^3,\quad K=\mathbf Q(\sqrt{-3}),\quad
\rho=(1+\sqrt{-3})/2,\quad u=[\rho]^{\times3}.
$$
取含 $K$ 的特征零系数域 $\mathcal E$，令
$$
\Pi=\pi_+^{\otimes3}+\pi_-^{\otimes3},
\qquad
\Pi=\Pi\pi_3^A,\quad \Pi u_*=-\Pi,\quad
\Pi[-1]_*=-\Pi .
\tag{1}
$$
$\pi_\pm$ 是椭圆曲线真正 $h^1$ Chow 对应的两个 CM 投影。
这些恒等式在对应环内成立。

**定理。** 对任意 $z\in CH^2(A)_{\mathcal E}$ 和 $a\in A$，
$$
\boxed{\Pi\,t_{a,*}z=\Pi z.}
\tag{2}
$$
此外：

1. 任意光滑超椭圆曲线到 $A$ 的一维推前被 $\Pi$ 杀掉；
   特别，所有几何亏格至多二的曲线像均被杀掉。
2. 任意支撑于一个真阿贝尔子簇平移中的一维循环被 $\Pi$ 杀掉。
3. 对任意曲线映射 $\phi:C\to A$，有准确的 Ceresa 表达
   $$
   \boxed{\Pi\phi_*[C]
   =\tfrac12\Pi\bigl(\phi_*[C]-[-1]_*\phi_*[C]\bigr).}
   \tag{3}
   $$
   左侧不依赖映射的整体平移。

第7节将 (3) 用于 R831 的原 $q_0/q_2$ 端点；
该应用给出固定有限域上真实曲线映射的有限线性组合，
不把它预先相认 R814 的指定类，也不声称其 Abel–Jacobi 值非零。

## 2. 任意一维循环的 Fourier 分量

用原点正规化的 Poincaré 线丛 $\mathcal P$ 定义
$$
\mathcal F_A(z)
=q_*\bigl(p^*z\,\exp(c_1(\mathcal P))\bigr).
$$
其中 $p,q$ 是 $A\times\widehat A$ 的两个投影。约定
$$
\mathcal F_A([a])=\exp(\ell_a),\quad
\ell_a=c_1(\mathcal P|_{\{a\}\times\widehat A}),\quad
\mathcal F_A(x*y)=\mathcal F_A(x)\mathcal F_A(y).
\tag{4}
$$
$\mathcal F_A$ 可逆，且
$\mathcal F_A[n]^*=[n]_*\mathcal F_A$。
这些 Chow 恒等式见 Beauville，
*Quelques remarques sur la transformation de Fourier dans l'anneau de Chow
d'une variété abélienne*，LNM 1016 (1983)，§2 Proposition 3、
Corollaire 2，[作者原文](https://math.univ-cotedazur.fr/u/beauvill/pubs/fourier.pdf)。

下列分量计算直接来自定义。对 $z\in CH^2(A)$，
Fourier 的余维 $r$ 分量为
$$
\mathcal F_r(z)
=\frac{1}{(r+1)!}\,
q_*\bigl(p^*z\,c_1(\mathcal P)^{r+1}\bigr),
\qquad 0\le r\le3 .
\tag{5}
$$
由 $(1\times[n])^*\mathcal P=\mathcal P^{\otimes n}$ 与平坦基变换，
$$
[n]^*\mathcal F_r(z)=n^{r+1}\mathcal F_r(z).
\tag{6}
$$
当 $r=0$ 时，$[n]^*$ 在 $CH^0(\widehat A)$ 上是恒等；
取 $n=2$，(6) 迫 $\mathcal F_0(z)=0$。因此准确有
$$
\mathcal F_A(z)=\beta_z+\gamma_z+\delta_z,
\quad
\beta_z\in CH^1,\ \gamma_z\in CH^2,\ \delta_z\in CH^3,
\tag{7}
$$
三个分量在 $[n]^*$ 下分别乘 $n^2,n^3,n^4$。
尤其 $\beta_z$ 是一个对称除子类，属于 $NS(\widehat A)_{\mathcal E}$
的对称提升。

由 $\mathcal F_A[n]^*=[n]_*\mathcal F_A$ 及
$[n]_*[n]^*=n^6$，原 $A$ 上相应的三个 CK 次数是 $4,3,2$。
也可只取 $n=2$，用乘积 CK 投影的互异本征值分开。故
$$
\mathcal F_A(\pi_3^A z)=\gamma_z.
\tag{8}
$$
这没有调用未证的负 Beauville 分次消失；所需最低分量已由 (5)–(6)
直接排掉。

## 3. 平移只在 degree-three 部分加入一个加性项

因 $t_{a,*}z=[a]*z$，(4)、(7) 给
$$
\mathcal F_A(t_{a,*}z)
=\beta_z+(\gamma_z+\ell_a\beta_z)
 +(\delta_z+\ell_a\gamma_z+\tfrac12\ell_a^2\beta_z).
\tag{9}
$$
$\ell_a$ 满足 $[n]^*\ell_a=n\ell_a$，
所以 (9) 三个括号的 $[n]^*$ 本征值仍为 $n^2,n^3,n^4$。
结合 (8)，
$$
\boxed{\pi_3^A(t_{a,*}z-z)
=\mathcal F_A^{-1}(\ell_a\beta_z).}
\tag{10}
$$
对固定的 $\beta=\beta_z$ 记右侧为 $v_\beta(a)$。
Poincaré 的双加性给 $\ell_{a+b}=\ell_a+\ell_b$，
故 $v_\beta(a)$ 在点群法下严格加性。

这里没有声称所有平移差在整个 $CH^2$ 中都为零，
也没有声称整个 $a\mapsto t_{a,*}z$ 加性。
(10) 是完整 degree-three 部分的准确等式。

## 4. 对角 CM 在所有对称除子上恒等

用积主极化把 $\widehat A$ 识别为 $E_0^3$。
在
$$
NS(\widehat A)_{\mathbf Q}\hookrightarrow
\operatorname{End}^0(\widehat A)=M_3(K)
$$
的极化识别中，拉回 $v^*$ 作用为 $H\mapsto v^\dagger Hv$。
这里 $\dagger$ 为复共轭转置；对 $v=\widehat u$，矩阵是
$\bar\rho I_3$，于是
$$
v^\dagger Hv=\rho H\bar\rho=H.
\tag{11}
$$
此识别以及拉回公式可由
$\lambda_{v^*D}=\widehat v\,\lambda_D v$ 直接得到；
参见 Milne，*Abelian Varieties*，
[作者笔记](https://www.jmilne.org/math/CourseNotes/AV.pdf)，
Chapter I §14 Proposition 14.2。
我们只需要 $NS\to\operatorname{Hom}(A,\widehat A)$ 的注入。

(11) 先给 $NS$ 中的等式。$\widehat u^*\beta$ 与 $\beta$ 都对称，
其差在 $\operatorname{Pic}^0$；而 $[-1]^*$ 在 $\operatorname{Pic}^0$
上乘 $-1$。有理系数下，该差既对称又反对称，故为零：
$$
\widehat u^*\beta=\beta\quad\text{于 }CH^1(\widehat A)_{\mathcal E}.
\tag{12}
$$
这样已经支付从代数等价返回有理等价的步骤。

Fourier 对同源的相容性及 Poincaré 定义给
$$
\mathcal F_Au_*=\widehat u^*\mathcal F_A,\qquad
\widehat u^*\ell_a=\ell_{u(a)}.
$$
由 (12)，
$$
u_*v_\beta(a)=v_\beta(u(a)).
$$
因 $u^2-u+1=0$ 在点群上成立且 $v_\beta$ 加性，
$$
(u_*^2-u_*+1)v_\beta(a)=0.
\tag{13}
$$
对 (13) 施 $\Pi$。由 (1)，$\Phi_6(-1)=3$，故
$\Pi v_\beta(a)=0$。再用 (10)、$\Pi=\Pi\pi_3^A$，
即得所有一维循环的 (2)。

## 5. 超椭圆曲线像与最低几何亏格

设 $C$ 为光滑超椭圆曲线，$\iota$ 是超椭圆对合。
在代数闭域上选一个 Weierstrass 点 $P_0$；
则
$$
[P-P_0]+[\iota(P)-P_0]=0\quad\text{于 }J(C).
\tag{14}
$$
任意 $\phi:C\to A$ 减去常值 $\phi(P_0)$ 后经 Albanese 映射分解，
所以对 $\phi_0=\phi-\phi(P_0)$，
$$
\phi_0\iota=[-1]\phi_0,\qquad
[-1]_*(\phi_{0,*}[C])=\phi_{0,*}[C].
$$
由 (1) 得 $2\Pi\phi_{0,*}[C]=0$，故该投影为零。
(2) 恢复任意平移及基点，得到 $\Pi\phi_*[C]=0$。

亏格二曲线均为超椭圆；亏格一的同样论证用原点及 $[-1]$，
亏格零到阿贝尔簇的态射常值。
对奇异像先取正规化，并保推前的有限次数，结论不变。
因此一个非零的最高 CM 一维循环，若写成曲线像的有限线性组合，
至少有一个有效贡献的像具有非超椭圆正规化且几何亏格至少三。
这只是必要条件，并不使高亏格像自动非零。

## 6. 所有真阿贝尔子簇平移上的曲线均消失

设 $B\subset A$ 为维数 $d<3$ 的阿贝尔子簇。
完全可约性给一个同源 $E_0^d\to B$；
复合到 $A$ 的坐标均为 $E_0$ 的同态，因而与 $\rho$ 交换。
故 $u(B)=B$，且限制 $u_B$ 仍满足 $\Phi_6(u_B)=0$。
这里的同源分解只使用阿贝尔簇的完全可约性，
见 Milne 上引笔记 Chapter I §10 Proposition 10.1。
所有这些数据都能在一个固定有限扩域上定义。

$d=0$ 不给一维推前；$d=1$ 时只有 $[B]$ 的倍数，
$u_*[B]=[B]$ 与 $\Pi u_*=-\Pi$ 直接迫其投影零。

$d=2$ 时，每个一维循环在 $B$ 上是一个除子 $D$。写
$$
D=D^++D^-,
\qquad D^\pm=\tfrac12(D\pm[-1]^*D).
$$
$D^+$ 对称而 $D^-\in\operatorname{Pic}^0(B)_{\mathcal E}$。
对包含 $i:B\hookrightarrow A$，使用
$[n]_{A,*}i_*=i_*[n]_{B,*}$ 与 $[n]_{B,*}[n]_B^*=n^4$，有
$$
[n]_A^*i_*D^+=n^4 i_*D^+,\qquad
[n]_A^*i_*D^-=n^3 i_*D^-.
\tag{15}
$$
第一项被 $\pi_3^A$ 杀掉。第二项上，$u_{B,*}=u_B^{-1,*}$；
在 $\operatorname{Pic}^0(B)=\widehat B$ 上这是一个群同态，
由 $\Phi_6(u_B^{-1})=0$ 得
$$
(u_*^2-u_*+1)i_*D^-=0.
$$
再以 $\Phi_6(-1)=3$ 得 $\Pi i_*D^-=0$。
(2) 随即处理 $a+B$ 中的全部曲线。此证明对除子的
$\operatorname{Pic}^0$ 部分也有效，没有只检查它的 cohomology 类。

## 7. 原唯一端点的真实曲线与 Ceresa 表达

保持 R831 的
$$
X=X_0(10404),\quad C=X_0(2601),\quad
q_0,q_2:X\longrightarrow C,
\qquad Z=Z_{02}.
$$
仍是原三组 $(j,k)=(10,16),(16,4),(4,10)$；
不改原 $f,g_j,g_k$ 或任何坏位 test vector。

先取一个固定有限扩域 $F$，消去 R832 中已经固定的有限 Artin
角色，并使需要的 Jacobian 同态有定义。该域先于 $p$ 固定。
R832 的权一 Chow 识别给对应
$$
\Gamma_f:h^1(X)\longrightarrow h^1(E_0),\qquad
\Gamma_g,\Gamma_h:h^1(C)\longrightarrow h^1(E_0)
\tag{16}
$$
（系数为 $\mathcal E$），分别经原 $e_f,e_g,e_h$，
且在相应原二维因子上为同构。选这些同构与原两个 CM 特征
相容，则最高张量被送到 (1)。

这里 (16) 的实现必须保留为真实 $h^1$ 对应。
具体地，Jacobian 同态与曲线的 $h^1$ 对应相容，
每个 (16) 可以写成有限和
$$
\Gamma_i=\sum_r c_{i,r}\,(a_{i,r})_*
\quad\text{在 }h^1\text{ 上},\qquad
a_{i,r}=\varphi_{i,r}\circ\operatorname{AJ}_{C_i},
\tag{17}
$$
其中 $\varphi_{i,r}:J(C_i)\to E_0$ 是实际同态，
$C_f=X,C_g=C_h=C$。
有理分母吸收进 $c_{i,r}\in\mathcal E$，从而 $a_{i,r}$
是真实曲线态射。若系数不有理，保留这个有限线性组合，
不把一个 $\mathcal E$-线性“坐标”冒当单一曲线映射。

以 cusp $\infty$ 作 Abel–Jacobi 基点。对每个三元指标 $\mathbf r$，
定义固定的实际态射
$$
\Phi_{\mathbf r}:X\longrightarrow A,\qquad
x\longmapsto
\bigl(a_{f,r_0}(x),\,a_{g,r_1}(q_0x),\,
                    a_{h,r_2}(q_2x)\bigr),
\quad
c_{\mathbf r}=\prod_{i=0}^2 c_{i,r_i}.
\tag{18}
$$
$q_0\infty=q_2\infty=\infty$，各 $a_{i,r}$ 在基点取零。
故 modified diagonal 除小对角外的每个基点项在 (18) 下
至少有一个坐标恒为原点，被该坐标的 $\pi_1$ 杀掉。
展开 (17)，得到准确的 Chow 等式
$$
\boxed{
\widetilde Z:=
\Pi(\Gamma_f\otimes\Gamma_g\otimes\Gamma_h)_* Z
=\sum_{\mathbf r}c_{\mathbf r}\,
       \Pi\,\Phi_{\mathbf r,*}[X]
=\tfrac12\sum_{\mathbf r}c_{\mathbf r}\,
       \Pi\,\operatorname{Cer}(\Phi_{\mathbf r}),
}
\tag{19}
$$
其中
$$
\operatorname{Cer}(\Phi)
=\Phi_*[X]-[-1]_*\Phi_*[X].
$$
最后一式来自 (1)，并非调用一个未核实的 Ceresa 非零定理。
若某个 $\Phi$ 的像维数为零，其一维推前按定义为零。
(19) 由图形对应的组合与逐项推前得到；
不只是在某个实现中辨认两边。

R832 说明 $Z$ 已在最高原 $\lambda$ 因子中；
(16) 在该因子上给同构，故这里的运输不丢弃原 $Z$。
但 (17)–(19) 是在固定权一同构下的公式，
尚未列出原 modular Jacobian 同态的具体坐标，
也未计算 (19) 的非零值。

次数规范完全沿用 R831：(19) 从共同 $X_0$ 目标中的 $Z_{02}$ 出发，
因此没有额外乘或除 $6$。
返回 $X^3$ 的选定 old 副本仍使用 R831 的 $6^{-2}$ 拉回；
返回原 $X_1$ 目标仍使用 $D_X=1632,D_C=816$ 和 degree $12$
的原公式。这里的 $1/2$ 仅是 Ceresa 的确切反对称化因子。

(2) 还表明 (19) 的最高投影不受 Abel–Jacobi 基点变动造成的
各整体平移影响。它不准许变更原 $q_0/q_2$、Hecke 对应或 CM
角色。由第5–6节，若某个项对 (19) 有非零贡献，其像必须生成
整个 $A$，且其正规化非超椭圆、亏格至少三。

## 8. 对主门的作用与尚未支付之处

(19) 把原唯一端点的几何来源精确落实到固定曲线映射的
最高 Ceresa 部分；(2) 消除了平移基点这项自由度，
第5–6节排除了所有超椭圆表达及真阿贝尔子簇平移表达。
这些是已付的实际 Chow 结论。

仍须研究 (19) 中实际同态和曲线的最高部分，或构造到
R814 指定 canonical 类的真实对应。
本篇没有证明 (19) 非零，没有支付它与 R814 的比例，
不消掉 YZZ 高度中的坏位补项，也不把固定 cycle 的一个
$p$ 上 Abel–Jacobi 非零传到无穷多个 $p$。
R838 的同端点临界系数与主极项继续保其全部投影、Euler 因子及周期。

本篇未执行新的数学计算或目标素数扫描；
不生成可重算输出。所有原 ray、完整 Selmer 与全 $\Sha[p^\infty]$
完成标准保持。


## 9. 属三曲线的实际自同构行列式判据

补充日期：2026-11-16。以下结论用于筛选真实曲线像；不以一个
实现中的零泛函代替 Chow 消失。

**命题。** 设 $C$ 是特征零域上的光滑完备属三曲线，
$\varphi:C\to A=E_0^3$ 为实际态射。假设 $C$ 有有限阶自同构
$v$，且在一个复嵌入下
$$
\xi=\det\!\left(v^*\mid H^0(C,\Omega_C^1)\right)\ne1.
\tag{20}
$$
则
$$
\boxed{\Pi\,\varphi_*[C]=0.}
\tag{21}
$$
$v$ 和所需 CM 同态可先在一个固定有限扩域上定义；
有理系数的限制—核限制把 (21) 降回原定义域。

**证明。** 若像只生成真阿贝尔子簇的平移，第6节已给 (21)。
否则取基点 $P_0$，由第4节的全部平移不变性，先消去
$\varphi(P_0)$，写
$$
\varphi=q\circ i,\qquad
i:C\to J(C),\quad P\mapsto[P-P_0].
$$
此时 $q:J(C)\to A$ 满射，而两边维数都是三，所以 $q$ 是同源。

这里只使用阿贝尔 Chow 动机的函子性。其 $h^j$ 是 $h^1$ 的
第 $j$ 个带通常动机符号的外代数分量；在未改换交换约束的
Chow 范畴中也记为 $\operatorname{Sym}^j h^1$。
因此同源的 $q^*$ 在 $h^3$ 上可逆，准同态的合成也在这个
动机中严格保持。这是标准阿贝尔动机结构，不是把所有高余维
对应的实现宣称为忠实。

令 $v_J$ 是 $v$ 对 Jacobian 的诱导自同构，在 $h^3(A)$ 上置
$$
T=q_*\,v_{J,*}\,q_*^{-1}
  =(q^*)^{-1}(v_J^{-1})^*q^*.
\tag{22}
$$
第二式完整计入推前次数：$q_*=(\deg q)(q^*)^{-1}$，
共轭中的两个次数相消。没有将 $q_*$ 本身误写成
$\operatorname{Sym}^3(q_*|h^1)$。

设 $u=[\rho]$ 是本篇对角六阶 CM 自同构，
$\rho^2-\rho+1=0$。由于
$\operatorname{End}^0(A)=M_3(K)$，$u$ 在准同态代数中为中心。
(22) 来自 $qv_Jq^{-1}$ 的逆拉回，故 $T$ 与 $u_*$ 严格交换。
在原 Chow–Künneth 三次分量上，原乘积 CM 分解还给
$$
\boxed{
\Pi=\pi_3\,\frac{u_*^2-u_*+1}{3}.
}
\tag{23}
$$
确实，最高两条线上 $u_*=-1$，其它三次分量上的特征为
$\rho$ 或 $\bar\rho$；在这个已有的实际乘积分解中逐项验证即得
(23)。所以 $T$ 与 $\Pi$ 交换。

若 $v$ 的阶为 $m$，则 $T^m=1$。于是
$$
P=\Pi\,\frac1m\sum_{a=0}^{m-1}T^a
\tag{24}
$$
是 $h^3(A)$ 中的真正 Chow 幂等元。
其 Betti 实现的可能像只有 $H^{3,0}(A)\oplus H^{0,3}(A)$。
经 $q^*$ 识别，$T$ 在这两条线上的特征是
$\xi^{-1},\bar\xi^{-1}$；两者均不为1，因为 $\xi$ 是根单位。
故 (24) 的 Betti 实现为零。

此处可以使用的是 **Kimura 幂零定理对幂等元的推论**：
阿贝尔动机及其直和因子有限维，零实现的直和因子为零。
等价地，(24) 数值平凡而必幂零，又因其幂等，故 $P=0$。
这一步不声称任何两个任意高余维对应只要实现相同便相同。

最后核 $P$ 实际读取的是所需曲线像。
即使 $P_0$ 不被 $v$ 固定，也有
$$
v_J\circ i=t_{-[vP_0-P_0]}\circ i\circ v.
$$
故 $v_{J,*}i_*[C]$ 是 $i_*[C]$ 的一个整体平移。
推经 $q$ 后，第4节的平移不变性给
$$
T\,\Pi q_*i_*[C]=\Pi q_*i_*[C].
$$
这里先用各 $\pi_3$ 的函子性，再用 $T\Pi=\Pi T$；
没有要求 $T$ 在整个 Chow 环上是一个实际整数同态的推前。
于是 $\Pi q_*i_*[C]$ 属于 (24) 的像，而 $P=0$，得到 (21)。
证毕。

所用阿贝尔动机函子性可对照
[Laga–Shnidman, *Ceresa cycles of bielliptic Picard curves*](https://math.huji.ac.il/~shnidman/CeresaBPC.pdf)
§4.7 与 §5.1；上述 Kimura 推论及其对阿贝尔直和因子的适用，
在 [Laga–Shnidman, *Vanishing criteria for Ceresa cycles*](https://arxiv.org/pdf/2406.03891)
§3 的 Theorem A 证明中明确使用，其原引文是 Kimura
*Chow groups are finite dimensional, in some sense*,
Math. Ann. 331 (2005), Corollary 7.3、Example 9.1。
这里只用该已知幂等元结论，不移用那篇论文的整曲线消失假设。

## 10. Picard 曲线像不能供应这里的最高分量

对任意光滑 Picard 曲线
$$
C:\ y^3=x^4+ax^2+bx+c,
$$
其属为三，且 $v(x,y)=(x,\omega y)$ 固定无穷远点。
全纯微分基可取
$$
\frac{dx}{y^2},\quad\frac{x\,dx}{y^2},\quad\frac{dx}{y}.
$$
相应特征为 $\omega,\omega,\omega^2$，故行列式为 $\omega\ne1$。
命题给出对 **每个实际** $\varphi:C\to E_0^3$ 的消失：
$$
\boxed{\Pi\varphi_*[C]=0,\qquad
       \Pi\,\operatorname{Cer}(\varphi)=0.}
\tag{25}
$$
包含像落真子簇、有限推前次数、基点平移及固定系数扩张；
不是仅排某个特殊 Picard 模型。

这也精确说明相关 Ceresa 椭圆点公式的范围。
上述 *Vanishing criteria* 的 Lemma 4.5、Corollary 4.9
将 $h^3(J(C))^{\mu_3}$ 置于 $(2,1)+(1,2)$ 型，并识别为
$h^1(E)(-1)$；bielliptic 论文的 Theorem 5.1 则给实际
$h^3(J)^{\mu_6}\simeq h^1(E_\Delta)(-1)$。
它们读取的不是本篇 $(3,0)+(0,3)$ 最高分量。
故其中某个椭圆点非挠，不能替代 (19) 的指定最高类非零。

(25) 没有排除一般属三曲线：若所有自同构的上述行列式为1，
本命题不给消失。原 (19) 的所有具体对应仍需按自己的
实际对称性和有限 Artin 角色研究；它们不会因同为 Ceresa
循环而自动继承另一模型的非零值。
