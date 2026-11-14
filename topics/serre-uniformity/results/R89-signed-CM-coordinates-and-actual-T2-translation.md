# R89. 加权 Jacobi 系数确定层 41 的真实 CM 比例及 T₂ 规范平移

日期：2026-11-12。会话：serre-uniformity-resume2；qc_global。

**状态：已证明；全部八个系数域附精确有理证书。** 本文从实际带符号的 Heegner 除子计算 R79、R85 中尚未选择的点比例，进而计算真正的 $G=2F$ 平移。它不把平方根的任选符号当作实际点，也不使用近似复周期来选符号。

写
$$
p=41,\quad N=p^2=1681,\quad X=X_{\rm ns}^+(p),\quad
J=\operatorname{Jac}(X),\quad d=\deg D=20,
$$
其中 $D$ 是全部尖点之和。沿用 R71 的实际项链同源
$$q:J_0(N)\longrightarrow J,\qquad qq^\dagger=\kappa,$$
以及 R79 的实际点 $B_{-4},B_{-8}$、$U_{-3},U_{-7}$。在每个真正的 new、Fricke $+$ 因子 $f$ 上定义
$$
B_{-8,f}=s_f B_{-4,f},\qquad U_{-3,f}=r_{3,f}B_{-4,f},\qquad
U_{-7,f}=r_{7,f}B_{-4,f}.
\tag{0.1}
$$
这些等式在 $J(\mathbb Q)\otimes\mathbb Q$ 中，标量属于实际 Hecke 系数域 $E_f$；$B_{-4,f}\ne0$ 已由 R79 证明。

令 $\phi_f$ 是与 $f$ 对应的权二、指标 $N$ 的 holomorphic Jacobi 特征形式，$c_f(\Delta,r)$ 采用判别式及 $r\bmod2N$ 记号。则
$$
\boxed{
\begin{aligned}
s_f&=\frac{c_f(-8,142)}{2c_f(-4,756)},\\
r_{3,f}&=\frac{30}{\kappa_f}\frac{c_f(-3N,N)}{c_f(-4,756)},\\
r_{7,f}&=\frac{10}{\kappa_f}\frac{c_f(-7N,N)}{c_f(-4,756)}.
\end{aligned}}
\tag{0.2}
$$
这些是实际符号公式。所有分母非零，后面的整数路径计算直接证明这一点；不需要额外假设某个 Jacobi 系数非零。

对 R79 的
$$F=27T_2+4\operatorname{id},\qquad G=2F=54T_2+8\operatorname{id},$$
实际平移在基 $B_{-4,f}$ 下为
$$\boxed{\xi_{G,f}=108r_{7,f}+1080s_f+80+\frac{16}{3}r_{3,f}.}\tag{0.3}$$
全部八域的准确系数存于证书。特别是在
$$E_f=\mathbb Q[h]/(h^2-2h-31),\qquad h=a_2(f)+2a_3(f),$$
有
$$
\boxed{
s_f=\frac{h+5}{4},\qquad r_{3,f}=-\frac{15}{4},\qquad
r_{7,f}=-\frac{5(h+1)}8,\qquad
\xi_{G,f}=\frac{405h+2685}{2}.}
\tag{0.4}
$$
若取 $h=1+4\sqrt2$，最后一项是 $1545+810\sqrt2$。

## 1. 加权除子、次数零基点及已发表的 GKZ 输入

### 1.1 正定形式与粗模权重

对 $\Delta<0$、$r^2\equiv\Delta\pmod{4N}$，令
$$
\mathcal Q^+_{N,\Delta,r}=
\{[A,B,C]:A>0,\ N\mid A,\ B\equiv r\bmod2N,\ B^2-4AC=\Delta\}.
$$
允许非本原形式。若 $z_Q\in\mathbb H$ 是 $Q(z,1)=0$ 的根，定义粗模曲线上的有理系数除子
$$
Y_{\Delta,r}=\sum_{Q\in\Gamma_0(N)\backslash\mathcal Q^+_{N,\Delta,r}}
\frac{[z_Q]}{e_Q},\qquad
e_Q=|\operatorname{Stab}_{\Gamma_0(N)}(Q)/\{\pm1\}|.
\tag{1.1}
$$
其次数零类是
$$y_{\Delta,r}=[Y_{\Delta,r}-\deg(Y_{\Delta,r})\,\infty]
\in J_0(N)(\overline{\mathbb Q})\otimes\mathbb Q.\tag{1.2}$$
这里固定真实尖点 $\infty$。紧曲线的 $\operatorname{Pic}$ 有次数商，不能直接当作 Jacobian；(1.2) 正是所需的次数零投影。

### 引理 1：在 Fricke $+$ 商中，(1.2) 的生成级数是权二 Jacobi 尖点形式

这个结论包括 $\Delta$ 与 $N$ 不互素的情形，且 Hecke 特征分量的系数与相应 $\phi_f$ 的系数成同一比例。

**证明。** 使用 Borcherds 1999 Theorem 4.5、Example 5.1，并采用其 2000 年已发表勘误中的有限阶 multiplier 条件。该定理从指标为 $N$ 的三维格给出所有 Heegner 除子的权 $3/2$ 向量值模性，经 theta 分解成为权二、指标 $N$ 的 Jacobi 模性；Example 5.1 明确允许非本原形式，也没有 $(\Delta,N)=1$ 限制。以下交代本题所需的两个规范化。

第一，Borcherds §4 的除子是上半平面的群不变除子，即 orbifold 除子。商映射在稳定子阶 $e_Q$ 的点局部形如 $t\mapsto t^{e_Q}$，故上层单点下到粗模曲线时是 $[z_Q]/e_Q$，正是 (1.1)。Borcherds 同时计入 $A>0$ 和 $A<0$ 的向量。把负向量变号将 $r$ 换为 $-r$；Fricke 将这两个正定除子互换。因此投影到 Fricke $+$ 后，其系数为 $2y_{\Delta,r}$。即使 $r=-r\bmod2N$，正负向量仍各计一次，所以仍是同一个因子 $2$；在任意两个系数的比中它取消。

第二，原构造在非紧模曲线上隐含商掉尖点。映射
$$Z\longmapsto[Z-\deg(Z)\infty]$$
确实下到其有理 Heegner 类群：若一个关系来自有限阶字符的权 $w$ 自守形式，取足够正整数次幂消去字符，再用模判别式 $\Delta_{\rm mod}$ 的适当幂消去权，得到权零函数，其原除子之外只有尖点。Manin–Drinfeld 说明每个次数零尖点除子在 Jacobian 中是挠元，故此关系经 (1.2) 为零。形式权对应的 $y_{0,0}$ 同样被消去，因为 $\Delta_{\rm mod}$ 在上半平面无零点。其他判别式零系数也为零，因此所得 Jacobi 形式是尖点形式。

最后，Hecke 对应与该构造相容。可直接在 (1.1) 中按循环 $\ell$ 同源计数：对奇素数 $\ell\nmid N$，横向、上行和下行的二次序三种情形给通常 Jacobi Hecke 递推。以所有形式（包括非本原形式）计数，并使用 $1/e_Q$，正好保留各自同构轨道的长度。相应的二次形式公式已见 Gross–Kohnen–Zagier 1987，I §1，pp.507–508；它不要求判别式与 $N$ 互素。次数零化产生的尖点修正仍由 Manin–Drinfeld 消去。故对 $f$ 的 Hecke 投影得到一个具有 $f$ 的远离 $N$ 的特征值的 Jacobi 形式。

权二 Jacobi 新形式的相应特征线是一维：Skoruppa–Zagier 的新形式对应，或 Ryan–Sirolli–Skoruppa–Tornaría（下称 RSST）Theorem 3.2 的 injective Hecke 映射，结合经典新形式的 multiplicity one，给出此结论。远离 $2N$ 的特征值已经唯一确定 $f$。因此所有 $e_fy_{\Delta,r}$ 都与同一个 $\phi_f$ 的系数成同一比例。此论证按每个嵌入成立，也等价于在整个 $E_f$ 因子上成立。证毕。

这里不用原 GKZ 高度计算中为简化而加的判别式互素条件去覆盖 $-3N,-7N$；允许这两个判别式的模性来自 Borcherds 的已发表定理。也没有把权二情形混同为非 holomorphic 的 skew-Jacobi 空间。

## 2. 两个分裂源点的权重与 $r$ 标号

沿用 R79 的
$$
\widetilde P_{-4}=(E_{-4},\ker((5+4i)^2)),\qquad
\widetilde P_{-8}=(E_{-8},\ker((3+4\sqrt{-2})^2)).
$$
它们分别由正定形式
$$[1681,756,85],\qquad [1681,142,3]$$
表示：两者判别式分别为 $-4,-8$。其对应理想分别是
$$
[1681,-378+i]=((5+4i)^2),\qquad
[1681,-71+\sqrt{-2}]=((3+4\sqrt{-2})^2).
\tag{2.1}
$$
例如商元素依次为 $-2+9i$、$1+\sqrt{-2}$；范数与包含关系给理想等式。源点的选向与 R79 相同；若改取共轭根，则在 Fricke $+$ 中给同一点类。

这两个序均为类数一，而所选水平 $N$ 结构由对应 CM 素理想平方给出。因此给定 $r$ 的正定形式各只有一个类。$-4$ 的点稳定子在除去 $\{\pm1\}$ 后阶为 $2$，$-8$ 的为 $1$，所以
$$
y_{-4,756}=\frac12[\widetilde P_{-4}-\infty],\qquad
y_{-8,142}=[\widetilde P_{-8}-\infty].
\tag{2.2}
$$
对每个 $f$ 投影后，引理 1 与 $B_\delta=q[\widetilde P_\delta-\infty]$ 给出
$$s_f=\frac{c_f(-8,142)}{2c_f(-4,756)},$$
即 (0.2) 第一式。缺少 (2.2) 的 $1/2$ 会使这个点比例错误一倍。

## 3. 惰性 CM 点的实际反向项链迹

令 $\delta=-3,-7$，$K_\delta=\mathbb Q(\sqrt\delta)$，$u_\delta=|\mathcal O_{K_\delta}^\times/\{\pm1\}|$，所以 $u_{-3}=3,u_{-7}=1$。两个域中 $p=41$ 均惰性，且类数均为一。记 $P_\delta\in X(\mathbb Q)$ 为实际 CM Cartan 点，
$$U_\delta=[dP_\delta-D].$$
在 $X_0(N)$ 上置
$$T_\delta=y_{\delta N,N}.
\tag{3.1}$$
下面直接识别其有限点集与重数；不把未核准的跨曲线迹定理当作输入。

### 引理 2：源点集和导子

$Y_{\delta N,N}$ 的全部点恰对应于最大 CM 曲线 $E_\delta$ 上的有序对跖对子
$$ (A,B),\qquad A=\sqrt\delta\,B,$$
模去 $\mathcal O_{K_\delta}^\times/\{\pm1\}$ 的作用。共有 $(p+1)/u_\delta$ 个不同粗模点，每个权重为一。

**证明。** 一个正定形式的系数形如
$$[p^2a,p^2b,c],\qquad p^2b^2-4ac=\delta.$$
模 $p$ 看出 $p\nmid ac$；因为 $\delta$ 是基本判别式，公因子的平方须整除 $\delta p^2$，而公因子又不含 $p$，所以此形式本原。其 CM 序的判别式是 $\delta p^2$、导子是 $p$；该序只有单位 $\{\pm1\}$，因而 $e_Q=1$。

设源参数为 $\tau$，则在 R71 的同构 $X_0(p^2)\simeq X_{\rm sp}(p)$ 下，中间椭圆曲线参数为 $\tau_0=p\tau$，并带有两条不同的 $p$ 阶线
$$ A=\langle\tau_0/p\rangle,\qquad B=\langle1/p\rangle.$$
$\tau_0$ 满足 $[a,pb,c]$，判别式为 $\delta$，所以中间曲线具有最大 CM。由
$$\sqrt\delta=2a\tau_0+pb$$
及 $p\nmid2a$，可见 $\sqrt\delta\,B=A$。射影作用中的 $\sqrt\delta$ 是该非分裂 Cartan 唯一的对合，故恰为项链的对跖映射。

反过来，给定最大 CM 曲线上的 $A=\sqrt\delta B$，选择与这两条线相容的格基。最大 CM 对应的本原形式 $[a,b_0,c]$ 满足 $p\mid b_0$；写 $b_0=pb$，回到源参数 $\tau_0/p$ 即得 $[p^2a,p^2b,c]$。此过程与 $\Gamma_0(p^2)$ 等价及中间格基变换相容，给出所述双射。

有序对由 $B\in\mathbb P^1(\mathbb F_p)$ 决定，共 $p+1=42$ 个。非平凡 CM 单位在惰性 $p$ 处没有固定射影线，故单位商自由作用；商后分别有 $14$、$42$ 个点。全部源序导子为 $p$，所以每个点的粗模权重确为一。证毕。

例如
$$[N,N,(N-\delta)/4],\qquad
\tau_{\delta,p}=-\frac12+\frac{\sqrt\delta}{2p}$$
给出其中一个点。由 CM 互反律，这个有限点和也可记成导子 $p$ 的环类域到 $K_\delta$ 的迹；以下等式只需要已经证明的有限除子解释。

### 命题 3：带实际重数的反向迹公式

在 $J_0(N)(\overline{\mathbb Q})\otimes\mathbb Q$ 中有
$$\boxed{q^\dagger U_\delta=d\,u_\delta\,T_\delta.}\tag{3.2}$$

**证明。** R71 的 $q^\dagger=r_C^*\lambda$ 是真正反向 incidence 对应。$\lambda$ 把一个项链送到其 $(p+1)/2=21$ 个无序对跖对子，$r_C^*$ 再恢复两种次序，泛纤维次数总计为 $p+1=42$。

在 $P_{-7}$，没有非标量自同构，故得到引理 2 的 $42$ 个点，各一次。在 $P_{-3}$，源项链的粗模稳定子阶为 $3$，而每个带有指定对跖对子的 incidence 对象稳定子为一：阶三元素不能固定一条线，也不能只交换两条线。因此 incidence 到该源点的粗模映射局部形如 $t\mapsto t^3$。这给 $14$ 个有序粗模点各重数 $3$，而非 $14$ 个各一次。两个情形统一为
$$\mathfrak q^\dagger(P_\delta)=u_\delta Y_{\delta N,N}.$$
反向对应保持尖点，所以 $\mathfrak q^\dagger(D)$ 是次数 $d(p+1)$ 的尖点除子。Manin–Drinfeld 消去
$$\mathfrak q^\dagger(D)-d(p+1)\infty,$$
结合 $\deg Y_{\delta N,N}=(p+1)/u_\delta$，得到 (3.2)。证毕。

此证明同时说明 $T_\delta$ 在有理同源范畴已经属于实际 new、Fricke $+$ 部分；这来自实际对应，不是按维数猜测。

在 $f$ 因子记
$$T_{\delta,f}=t_{\delta,f}[\widetilde P_{-4}-\infty]_f.$$
用 R71 的 $q^\dagger q=\kappa e_0$ 作用于 (0.1)，(3.2) 给出
$$\kappa_f r_{\delta,f}=d u_\delta t_{\delta,f}.$$
另一方面，(2.2) 和引理 1 给
$$t_{\delta,f}=\frac{c_f(\delta N,N)}{2c_f(-4,756)}.$$
代入 $d=20,u_{-3}=3,u_{-7}=1$，即为 (0.2) 的后两式。这里同时保留了度数 $d$、单位重数、真正极化标量 $\kappa$，没有把项链同源当作主极化同构。

## 4. 从有限整数和计算带符号的 Jacobi 系数

### 4.1 已发表的权二公式及同调符号

取辅助 admissible pair
$$\Delta_0=-43,\qquad r_0=1219,\qquad r_0^2\equiv-43\pmod{4N}.$$
RSST Theorem 4.15、Remark 4.19 给：对 cuspidal modular symbol $\sigma$，若 $\Delta$ 与 $\Delta\Delta_0$ 均非平方，则一个固定的 Jacobi 形式具有系数
$$
j_{\Delta,r}(\sigma)=
\sum_{Q\in\mathcal Q_N(\Delta\Delta_0,rr_0)}
\chi_{N,\Delta_0}(Q)\,C_Q\cdot\sigma,
\tag{4.1}
$$
其中
$$C_Q\cdot\{\alpha,\beta\}=\frac12(\operatorname{sgn}Q(\alpha)-\operatorname{sgn}Q(\beta)).\tag{4.2}$$
同一个与 $\Delta$ 无关的整体非零归一化在所有比例中取消。文献的权二特例要求 $\partial\sigma=0$；本计算严格在下述实际 cuspidal new 投影上使用它。

RSST §4.2 的 $\varepsilon$ 同调部分要求 $\operatorname{diag}(-1,1)$ 作用为 $(-1)^{k-1}\varepsilon$。此处 $k=2$、holomorphic 对应 $\varepsilon=-1$，故为 **star $+$**。因此不能直接拿 R74 的 star $-$ 二次扭曲行当作这里的同调类。

### 4.2 有限枚举及其完备性

PARI 的每条生成路径都是 $\{g0,g\infty\}$，其中 $g\in\mathrm{SL}_2(\mathbb Z)$。将 $Q$ 变成
$$\widetilde Q=g^{-1}\cdot Q=[a,b,c],\qquad \mathcal D=\Delta\Delta_0>0.$$
由 (4.2)，贡献只可能发生在 $ac<0$。先列 $a>0,c<0$，则
$$|b|<\sqrt{\mathcal D},\qquad n=(\mathcal D-b^2)/4\in\mathbb Z_{>0},\qquad
a\mid n,\quad c=-n/a.\tag{4.3}$$
这给全部正 $a$ 贡献，范围有限且完全。负 $a$ 形式由取负得到。

写 $g=\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)$。恢复 $Q=g\cdot\widetilde Q$ 时
$$
\begin{aligned}
A&=\delta^2a-\delta\gamma b+\gamma^2c,\\
B&=-2\delta\beta a+(\delta\alpha+\beta\gamma)b-2\gamma\alpha c.
\end{aligned}\tag{4.4}
$$
筛选 $N\mid A$ 与 $B\equiv rr_0\bmod2N$ 即得到 (4.1) 的索引。

在这里广义 genus character 化为普通的 $-43$ genus character。确切地，Gross–Kohnen–Zagier I §2 Proposition 1 的定义允许用 $Q=[Na,B,C]$ 所表示的素于 $43$ 的整数；$N=41^2$ 是平方，且 $(43,N)=1$，零值条件也等价于普通的 $(A,B,C,43)>1$。因此这个字符具有全 $\mathrm{SL}_2(\mathbb Z)$ 不变性，可以在 $\widetilde Q$ 上计算：若 $43\nmid a$，值是 $\left(\frac a{43}\right)$，否则取 $\left(\frac c{43}\right)$；若两者都被 $43$ 整除，判别式关系还迫 $43\mid b$，值为零。

正 $a$ 的交数为 $-1$。取负时，交数与 genus character 同时变号；故每个 (4.3) 对路径行贡献
$$
-\chi_{-43}(\widetilde Q)
\left(\mathbf1_{B\equiv rr_0}+
\mathbf1_{B\equiv-rr_0}\right).
\tag{4.5}
$$
当 $r=N$ 时这两个余数相同，仍要计两次，因为它们来自不同的向量 $Q,-Q$。把它们合成一个集合会把两个惰性坐标错误减半。

完整枚举的可复算计数如下。“命中”按 (4.5) 的两个指标分别累计。

| $\Delta$ | $r$ | $\mathcal D$ | 正 $a$ 形式数 | 命中数 | 非零生成路径数 |
|---:|---:|---:|---:|---:|---:|
| $-4$ | $756$ | $172$ | $58$ | $18$ | $18$ |
| $-8$ | $142$ | $344$ | $76$ | $32$ | $32$ |
| $-5043=-3N$ | $1681$ | $216849$ | $6848$ | $2114$ | $196$ |
| $-11767=-7N$ | $1681$ | $505981$ | $6960$ | $2146$ | $192$ |

惰性点必须使用 $r=N$，这是 §3 的真实模结构标号；取同余方程的另一个任意平方根不能替代它。

### 4.3 实际相对上同调到 new 同调的投影

PARI/GP 2.19.0 的
$$M=\operatorname{msinit}(1681,2,+1)$$
维数为 $144$。`mspathgens(M)` 给 $289$ 条群模生成路径：$287$ 条自由 $E_1$ 路径，另两条有椭圆二阶关系，在权二有理系数中值零。四个 (4.5) 行在后两条上都为零。

令 $E$ 为 PARI 实际 $144$ 个基符号在前 $287$ 条路径上的取值矩阵。脚本从头解
$$E v_{\Delta,r}=j_{\Delta,r}$$
并逐项核对等式，故得到真实相对上同调功能，而非任意 $289$ 维向量。

用 `msnew(M)` 取维数 $117$ 的实际 new 子空间，再用
$$\ker(w_{1681}-1)$$
得到维数 $54$ 的实际子空间 $P$。脚本核对 star 与 Fricke 均为 $+$。在全空间及 $P$ 上分别构造
$$H_{\rm full}=T_2+2T_3,\qquad H=H_{\rm full}|_P.$$
$H$ 的分母为 $2$。令 $F_H$ 为其特征多项式，则
$$\gcd\left(F_H,\frac{\operatorname{charpoly}(H_{\rm full})}{F_H}\right)=1.$$
因而 $Q=\operatorname{im}F_H(H_{\rm full})$ 是维数 $90$ 的真实不变补空间，$[P\ Q]$ 可逆；前 $54$ 个坐标给所需实际投影。

为什么这里可以去掉 (4.1) 的边界修正？模符号的 cuspidal 同调是边界映射之核，所有 new cuspidal 特征成分都在其中。上同调上的 Hecke 投影是该同调投影的对偶，所以把相对功能投到 $P$，等价于先把输入同调投到这个边界为零的子空间。RSST Remark 4.19 因而逐个适用；未对一般非 cuspidal 路径错误宣称边界修正为零。

记得到的四个列为 $v_4,v_8,v_{3N},v_{7N}$。令
$$K=[v_4,Hv_4,\ldots,H^{53}v_4].$$
它的有理秩为 $54$。将四列乘同一个共同分母，所得整数 $v_4$ 的 Krylov 行列式满足
$$\boxed{\det K\equiv109\pmod{1009}.}\tag{4.6}$$
这证明辅助 Jacobi 构造在全部 $54$ 条特征线上参考系数都非零。

精确求解 $K^{-1}[v_4\ v_8\ v_{3N}\ v_{7N}]$，把每列写成 $H$ 的多项式后，便得到各系数相对 $c_f(-4,756)$ 的比。Hecke 等变性和引理 1 的一维特征线说明这些正是 (0.2) 所需的比例；整体周期或 $\Sigma^*$ 的整体标量自动消去。

## 5. 全部实际符号及真实平移

系数域顺序与 R79、R85 相同，按 $H$ 的特征多项式因子排序，次数为
$$2,3,3,4,4,8,12,18.$$
R85 为 $r_3,r_7$、R79 为 $s$ 各保存了一个未选符号的代数平方根。以下表中符号是**真实点比例相对这些已存根**的比；不是对某个实嵌入的数值正负性作断言。

| 因子 | 次数 | $r_3$/R85 根 | $r_7$/R85 根 | $s$/R79 根 |
|---:|---:|:---:|:---:|:---:|
| 1 | 2 | $+$ | $+$ | $-$ |
| 2 | 3 | $-$ | $+$ | $-$ |
| 3 | 3 | $+$ | $+$ | $-$ |
| 4 | 4 | $+$ | $-$ | $+$ |
| 5 | 4 | $-$ | $-$ | $-$ |
| 6 | 8 | $+$ | $+$ | $-$ |
| 7 | 12 | $+$ | $+$ | $+$ |
| 8 | 18 | $-$ | $+$ | $-$ |

前五个域的 Jacobi 比可短列为：

| $f_H(h)$ | $c(-8,142)/c(-4,756)$ | $c(-3N,N)/c(-4,756)$ | $c(-7N,N)/c(-4,756)$ |
|---|---|---|---|
| $h^2-2h-31$ | $(h+5)/2$ | $-8$ | $-4h-4$ |
| $h^3+h^2-33h-85$ | $(h^2-2h-21)/2$ | $4h^2-12h-92$ | $-6h^2+16h+146$ |
| $h^3+h^2-30h+41$ | $(7h^2+19h-165)/29$ | $(-40h^2-150h+860)/29$ | $(-30h^2-40h+790)/29$ |
| $h^4-3h^3+4h-1$ | $-h^3+h^2+h$ | $-12h^3+12h^2+24h-12$ | $12h-12$ |
| $h^4+9h^3-108h-81$ | $h^3/27+h^2/9-h$ | $20h^3/27+28h^2/9-16h-12$ | $16h^3/27+8h^2/3-12h-12$ |

其余三域以及全部 $s,r_3,r_7,\xi_G$ 使用系数降幂整数向量和正分母保存在 JSON 中。标准库验证程序逐项证明：
$$
2s=c_8/c_4,\qquad \kappa r_3=30c_{3N}/c_4,\qquad
\kappa r_7=10c_{7N}/c_4,
$$
并核对全部平方严格等于 R79、R85 从实际 Gross–Zagier 和项链极化独立求出的平方。平方一致是归一化的反向检查；选择真实符号的证明是 §§1–4 的带符号除子和 Jacobi 系数计算。

由 R79 的完整除子等式，$G=2F$ 的平移就是 (0.3)。代入后全部八域的 $\xi_G$ 都非零；这也与 R85 对全部八种候选符号的非零性相符。现在这些候选已经被选择成唯一的实际坐标。

## 6. 与 R47 的真实 QC 方程的接口

若以 $B_{-4,f}$ 为 Mordell–Weil 的 $E_f$ 基，并以其非零 $47$ 进对数归一化相应微分坐标，则 $z_f(x)$ 仍来自实际
$$u_D(x)=[20x-D],$$
而平移坐标就是本文 (0.3)。这时 R47 的全局部分成为
$$\sum_f\operatorname{Tr}_{E_f\otimes\mathbb Q_{47}/\mathbb Q_{47}}
\left(c_f z_f(x)\bigl((54a_2(f)+8)z_f(x)-\xi_{G,f}\bigr)\right).
\tag{6.1}$$
$c_f\ne0$ 由 R75、R77 已证明。若保留原先未归一化的微分，本文的 $\xi_{G,f}$ 应再乘 $\log_f(B_{-4,f})$，并按 R68 同时变换二次高度系数；不能只改平移一个项。$d=20$ 已在 $u_D$ 和 §3 的迹公式中保留，$2F$ 也只使用一次。

本文确定了 (6.1) 的真实线性平移输入。要排除非 CM 共同根，还须把它与同一规范的完整辅助局部高度 $H_{D,G,47}(x)$ 及 R54 的有限坏高度靶值联合。Jacobi 的带符号全局坐标不会自动给出这个局部迭代积分，也不推出 CM 根的导数非零或层 41 的全部有理点已求出。

## 7. 可复算文件

在课题目录运行：

```text
python -B scripts/p41_jacobi_cm_coordinates.py --gp /tmp/pari-2.19.0/gp
python -B scripts/verify_p41_jacobi_cm_coordinates.py
```

文件：

- `scripts/p41_jacobi_cm_coordinates.py`：四个有限整数交数和，调用真实 GP 空间并组装证书。
- `scripts/p41_jacobi_cm_coordinates.gp`：从头构造 star $+$、new、Fricke $+$ 空间，精确相对功能转换、Hecke 投影和符号比例。
- `scripts/verify_p41_jacobi_cm_coordinates.py`：标准库整数/有理数复核全部有限和、Krylov 非消失、54 维多项式恒等式、真实符号及平移。
- `scripts/data/p41_jacobi_cm_certificate.json`：289 个路径矩阵、四个整数行、$2H$、四个投影列及全部八域系数；不保存巨大的中间群结构。

证书 SHA256：

```text
f472bf8d7389cd8face0998431517c74af2e56a10dbc290dda31fde2b2ea7224
```

生成器保存实际投影的共同分母，所有四列使用同一个尺度；mod $1009$ 判据对相应整数列计算。验证器还在 $\mathbb Q$ 上验证每个因子的全部比例恒等式，不把一次模素数一致代替系数恒等式。

## 8. 原始来源及准确适用点

1. R. E. Borcherds, **The Gross–Kohnen–Zagier theorem in higher dimensions**, *Duke Mathematical Journal* **97** (1999), 219–233；**Correction**, **105** (2000), 183–184。[作者合并勘误版](https://math.berkeley.edu/~reb/papers/gkz/gkz.pdf)，日期 2000-03-04：§4 的 orbifold 除子定义及有限阶字符条件在 PDF pp.6–7，Theorem 4.5 在 p.9，Example 5.1 与尖点商在 pp.10–11（以页面所印页码计）。这里用其允许全部判别式的模性，不假定导子与 $N$ 互素。
2. B. Gross, W. Kohnen and D. Zagier, **Heegner points and derivatives of L-series. II**, *Mathematische Annalen* **278** (1987), 497–562。[原文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01458081/fulltext.pdf)。I §1 pp.507–508 是二次形式的 Hecke 作用；I §2 Proposition 1 pp.508–509 是广义 genus character；IV §1 pp.541–542 明确给 $1/e$ 权重。原文引言 p.500 也记录新 Jacobi 特征线的一维性。
3. N. C. Ryan, N. Sirolli, N.-P. Skoruppa and G. Tornaría, **Computing Jacobi forms**, *LMS Journal of Computation and Mathematics* **19**, Special Issue A (2016), 205–219，DOI [10.1112/S1461157016000346](https://doi.org/10.1112/S1461157016000346)。[已发表全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B9816899D93044A71CF095492887893D/S1461157016000346a.pdf/computing-jacobi-forms.pdf)。Theorem 3.2 p.207、§4.2 p.209、§4.3 的 dual kernel p.210、Theorem 4.15 与 Remark 4.19 p.212，分别用于一维特征线、star 符号、对偶 Hecke 作用和有效的权二 cuspidal 公式。
4. M. Rebolledo and C. Wuthrich, **A moduli interpretation for the non-split Cartan modular curve**, *Glasgow Mathematical Journal* **60** (2018), 411–434。[作者原稿](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。§4.1 的两项链对应及 Lemma 22 与 R71 所用 $q,q^\dagger$ 相同。
5. 仓库 R71、R79、R85：实际项链同源、粗模重数、真实 $T_2$ 平移及独立比例平方；R47、R68、R75、R77：QC 坐标、极化/微分标量与 $47$ 进高度非退化。

研究过程中核对了 Kohen–Sirolli 的非分裂 Cartan GKZ 论文，但不直接使用其中将紧化 Picard 群与 Jacobian 混同的简写，也不使用未加单位权重的版本。§1 和 §3 已在这里给出所需的准确基点与重数证明。
