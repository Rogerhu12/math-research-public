# 原 type4 惰性 signed 坐标的全精度交叉比较

2026-11-27 UTC。

本注继续[原负二 Newton / signed 笔记](2026-11-27-original-type-four-inert-negative-two-newton-and-signed-line.md)和[固定 weight5 toric Artin 基](2026-11-27-original-weight-five-toric-artin-basis-and-common-phase.md)。新增的是同一原椭圆单位来源的**完整解析交叉恒等式**：三条 signed 坐标与三条 Newton 平方，只差一个共同解析因子。证明先在合法正整数权使用同一 mixed 显式互反律，逐项保留原有限投影、Artin 基、Gamma、Tate 和惰性 Euler；随后才用解析唯一性。不对任何 $p^{\mathrm{weight}}$ 作解析延拓。

共同因子可能在 augmentation 为零。本注不以交叉比较或三个 Newton 单位代替其非零证明，也不将原固定54图类直接认作椭圆单位类。

## 1. 原来源及同一个局部整模块

保持
$$
K=\mathbf Q(\omega),\quad\delta=1+2\omega,\quad
E=\mathbf Q(\zeta_9),\quad
\mathcal J=\{4,10,16\},\quad
\mu=34\delta .
\tag{1}
$$
三个原 $\eta_j$、全 $34\delta$ ray class 单位、$e_{\eta_j}$、辅助 $(5)$、正 Coleman 规范及 $1/30$ 均严格沿 R804、R806。原 norm 和特殊化为
$$
e_{\eta_j}=\frac1{18}\sum_{g\in\operatorname{Gal}(H/K)}
                        \eta_j(g)^{-1}g,\qquad
\boldsymbol z_{j,p}
=\frac1{30}\operatorname{pr}_{\Gamma}
 \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty).
\tag{2}
$$
这里 $\operatorname{pr}_{\Gamma}$ 是同一全局 Iwasawa 类的实际特殊化；不是另选局部类。$H/K$ 为原 cyclic18 域。

取前述 Newton 笔记的好惰性 $p\ge11$，$d=p+1=6s$；需要几何首层时另保 R1049 的全部固定好模型范围及 $p>q_0$。本注纯交叉比较不需要几何的 $q_0$。系数整数环扩大到同时包含所有原基的同一不分歧完成，记为 $\mathcal O$，分式域为 $F$。删去原固定投影分母及下文固定非零常数的零极支撑。

因 $\eta_j((p))=1$，原 $H/K$ 在此惰性素位完全分裂，三个 $\eta_j$ 的本地限制都严格平凡。沿原 CM/Tate 基，有同一个整表示
$$
T_{\rm CM}=\mathcal O(\widehat\psi_0^2
                          \widehat{\bar\psi}_0^{-1})
\tag{3}
$$
和同一个 $M_p^+\simeq\mathcal O[[\Gamma]]$。前述 signed 笔记已通过实际单位的全部偶导子特化证明
$\operatorname{loc}_p\boldsymbol z_{j,p}\in M_{j,p}^+$。

原 Artin 基写为 $a_{j,p}e_j$，其中 $e_j$ 是 R804 的 $\eta_j^{-1}$ étale 基。保持它，不为本注重选。局部整同构明确取
$$
\iota_{j,p}^{a}(e_j\otimes t)=a_{j,p}^{-1}t .
\tag{4}
$$
它将 $a_{j,p}e_j$ 送至1。所有 $a_{j,p}$ 在当前位为单位，所以这是真整同构，且与限制、norm、tensor twist、两指数映射及 signed 分解相容。

固定一个本原基 $e_p^+$，定义真正的整坐标
$$
\iota_{j,p}^{a}(\operatorname{loc}_p\boldsymbol z_{j,p})
      =A_{j,p}^{a}(T)e_p^+,\qquad
A_{j,p}^{a}\in\mathcal O[[T]] .
\tag{5}
$$
不同本原基只同时乘一个 $\mathcal O[[T]]^\times$。下文从不逐 $j$ 另调一个随权周期。

## 2. 先由原有限单位支付 $c_j$ 的 Artin 方向

这一步不能从 $B_j^2=C\,c_j\gamma_j$ 猜出，须回到实际有限投影。

令 $\varpi_0\mathcal O_K$ 为原 $E_0$ 的 CM 格，
$P_\mu=\varpi_0/\mu\bmod\varpi_0\mathcal O_K$，并保持 Kato 的 norm-normalized 有理函数 $\theta_{-5}$。它满足
$$
\operatorname{div}(\theta_{-5})
=25(O)-\sum_{P\in E_0[5]}(P),
\qquad \operatorname{Norm}_{[b]}\theta_{-5}=\theta_{-5}
\quad((b,5)=1).
$$
故其有限 torsion translates 及原全 norm 就是(2)中使用的单位来源；不额外换一个 theta 函数的乘法常数。

记 $\partial$ 为原不变微分的导数，$\mathfrak D$ 为 CM Hodge splitting 定义的 Katz–Gauss–Manin 提升。对 $m\equiv4\bmod6$，在原完整 torsion 域先作实际 norm 到 $H$，再取 $e_{\eta_j}$。由此得到代数微分的系数
$$
\mathcal R_{j,m}
=\frac1{30}\,e_{\eta_j}
 \operatorname{Tr}\!\left[
 \mathfrak D^{m}\partial\log\theta_{-5}(P_\mu)
 \right].
\tag{6}
$$
$\operatorname{Tr}$ 中保全部原有限共轭；微分系数以
$\omega_0^{\,2m+1}$ 读取。若为书写 universal level 先取整数102，须先用相同 norm/distribution 回到 $\mu$；$\delta$ 已在导子内，不在此新增一枚坏处 Euler。下面也可直接在 $\mu$ 的原格 coset 上计算。

Tsuji 的 Theorem1.4、Proposition1.7 给完整 partial-$L$ 恒等式。其格核为
$$
m!\,A(\Lambda)^{-m}
 \frac{\overline{z+\lambda}^{\,m}}
      {(z+\lambda)^{m+1}},\qquad
A(\Lambda)=\frac{\sqrt3}{2\pi}|\varpi_0|^2 .
$$
在 $z=\varpi_0/\mu$ 代入 $z+\lambda=\varpi_0 a/\mu$，全部周期因子准确为
$$
\frac{\mu^{m+1}}{\bar\mu^m}
  \frac{(2\pi/\sqrt3)^m}{\varpi_0^{\,2m+1}}.
\tag{7}
$$
这是整数 level 公式的原理想版本，直接由显示的格核得到；
没有把 $\mu$ 当成一个有理正整数。
由于 $\mu/\bar\mu=-1$，在当前偶 $m$ 上该首因子就是 $\mu$。

完整 $e_{\eta_j}$ 和 norm 的系数是
$18^{-1}\sum_g\eta_j(g)^{-1}$，没有替成
$|\operatorname{Gal}(K(E[\mu])/K)|^{-1}$。
相应 $L$-值为
$$
\begin{split}
L(\eta_j^{-1}\psi_0^{-m-1}\bar\psi_0^m,0)
 &=L(\eta_j^{-1}\bar\psi_0^{\,2m+1},m+1)\\
 &=L(\eta_j\psi_0^{\,2m+1},m+1).
\end{split}
\tag{8}
$$
第一步只用 $\psi_0\bar\psi_0=\mathrm N$；第二步是全部理想的复共轭重排，因为 $\eta_j^c=\eta_j^{-1}$。这里没有 functional equation、额外 Gauss 选择或未定的根数。

辅助项也必须实际相消：
$\eta_j((5))=1$，$\psi_0((5))=\bar\psi_0((5))=-5$，
故 Theorem1.4 的两个项给
$25-\psi_0^{m+1}\bar\psi_0^{-m}((5))=30$。
因此(6)在固定 torsion 嵌入的原平均规范下准确是
$$
\boxed{
\mathcal R_{j,m}
=\frac{\mu}{18}(m!)^2\,
 \mathscr E_{j,m},\qquad
\mathscr E_{j,m}
=\frac{(2\pi/\sqrt3)^m
 L(\eta_j\psi_0^{\,2m+1},m+1)}
 {m!\varpi_0^{\,2m+1}} .
}
\tag{9}
$$
若把这个固定嵌入的平均改写为 R804 的 induced/étale 特殊化，
仍须用其 $\nu(e_{\eta_j})=1$ 的同一规范。此处不把显示的18
另乘进(2)，也不改变原 $a_{j,p}$。

所有 $\mathfrak D,\partial$、norm 与原曲线的 CM splitting 定义于 $K$。
由(6)直接有
$$
\sigma\mathcal R_{j,m}=\eta_j(\sigma)\mathcal R_{j,m}.
$$
R806 给
$\mathscr E_{j,4}=34^{-4}c_j$，且 $d_{j,4}=1$。
由(9)即严格得到
$$
\boxed{
c_j\in(HE)^{\eta_j},\qquad
\frac{c_j}{B_j}\in E,\qquad
\frac{c_j}{a_{j,p}}\in F .
}
\tag{10}
$$
第一式先在 $H\otimes_KE$ 中解释，再用 $H\cap E=K$。
这支付了所需 Artin 方向，而非只支付一个 $p$-进赋值。
同时由已付的 $B_j^2=Cc_j\gamma_j$ 可得
$\gamma_j\in(HE)^{\eta_j}$；本注不需要另选 $\gamma_j$ 的平方根。

## 3. 只有一个真正的解析权映射

令
$$
\rho_d=(\widehat\psi_0/\widehat{\bar\psi}_0)^d .
$$
$d=p+1$ 杀掉惰性 $p$ 的有限范数一 torus，$6\mid d$ 杀掉原2、3处有限部分，且其有理 uniformizer 值为1。因此 $\rho_d$ 是同一个原反圆分 $\mathbf Z_p$-扩张的连续角色。

取原生成元 $\gamma\in\Gamma$，置
$$
Q=\rho_d(\gamma)\in1+p\mathcal O,\qquad
v_p(Q-1)=1,\qquad
\boxed{T(v)=Q^v-1=\exp(v\log Q)-1.}
\tag{11}
$$
这是真正的单一解析映射，三个 $j$ 完全相同。
若沿 R303 写 $q=\kappa_{\rm ac}(\gamma)$，则 $Q=q^d$。
反 Artin 约定只把 $Q$ 共同换成 $Q^{-1}$。

对 $k\ge1$，取 $m=dk-2$。在 $T(k)$ 处，(2)的最终表示是
$$
\eta_j^{-1}\widehat\psi_0^{\,2-dk}
                \widehat{\bar\psi}_0^{\,dk-1}
=\eta_j^{-1}\widehat\psi_0^{-m}
                \widehat{\bar\psi}_0^{\,m+1}.
\tag{12}
$$
所以这确实是原类的 mixed 正权特化，不是同一形式的另一 tame 支。
尤其
$v_p(T(p^n))=n+1$，这些点在原坐标中趋于 augmentation。

Iwasawa 级数 $A_{j,p}^a(T)$ 与(11)复合后属于
$\mathcal O\langle v\rangle$：在闭单位圆盘上
$\|T(v)\|\le p^{-1}$，故原 $T$-级数逐项收敛。
这一步不把任何临界 Gamma 或 $p^m$ 声称为 $v$ 的解析函数。

## 4. 同一 mixed reciprocity 的共同因子可以合法消去

对 $m=dk-2$，令 $\ell_{p,m}$ 是在(12)的共同 CM/Tate 基中，
先作真实 dual exponential、再读原正 Hodge 坐标的线性泛函。
它作用在同一个局部特化模块上，且对三个 $j$ 都用同一(4)。
原 R1049§8 标记2是基层 $D_{\rm dR}/\operatorname{Fil}^0$ 所在的 CM 嵌入；
从基层 $(2,-1)$ 到(12)的 $(-m,m+1)$ 后，正权的
$\operatorname{Fil}^0$ 正在这一相同标记上。
所以此处继续读取原 $a_{j,p}$，不把它换成另一标记的共轭基。
在 Iwasawa 模上先施(4)，再作任何权特化，正是保持这一点的方式。

由 Tsuji Theorem4.1 和原单位的 tensor/norm 特化，
存在一个**与 $j$ 无关的非零数** $\Xi_{p,m}$ 使
$$
\boxed{
\ell_{p,m}\!\left(
 \iota_{j,p}^{a}\boldsymbol z_{j,p}\big|_{T(k)}
 \right)
=\Xi_{p,m}\frac{\mathscr E_{j,m}}{a_{j,p}} .
}
\tag{13}
$$
这里的 $\Xi_{p,m}$ 不是从某条非零 $L$-值反解出来：
它由同一个 mixed reciprocity 图的共同映射定义。
下面逐项说明为何该图中没有未付的 $j$-因子。

Tsuji 的参数准确是 $(k_{\rm Ts},j_{\rm Ts})=(m+1,m)$。
其原算子为
$(-1)^m(m!)^{-1}\mathfrak D_p^m\partial$；
CM splitting 的代数性给 $\mathfrak D_p$ 与(6)的
$\mathfrak D$ 在同一个 CM 点上一致。
在第 $n$ 个 Lubin–Tate 层，全部原
$\pi^{-n(m+1)}\bar\pi^{nm}$ 均保留；
$\pi=\bar\pi=-p$ 时这就是 $(-p)^{-n}$。
回到底层的全部 norm 与原 étale/Tate 比较也是共同的。
(9)中的 $\mu$、原18、$(m!)^2$ 及辅助30按同一图处理，
不是为各 $j$ 单独取一个非零 period。

在 primitive 正权中唯一的 $p$ Euler 为
$$
1-\frac{\eta_j((p))(-p)^{2m+1}}{(p^2)^{m+1}}
=1+\frac1p .
\tag{14}
$$
它的赋值为 $-1$，不能当单位；但它非零而且三个值完全相同。
原2、3、17都在同一实际 primitive 导子中；其完整有限 Gauss
及 Haar 已包含在 R806 的 $c_j$，没有再删除一个参考 Euler。
原 $m!$、复 Tate 因子、$p$-adic CM tensor period、以及
induced 与固定嵌入平均之间的同一个 finite trace 标量，均保留在
$\Xi_{p,m}$ 内。它们每一项都与 $j$ 无关。
**唯一有限 Artin 基变换就是显示的 $a_{j,p}^{-1}$，
其方向已由(6)–(10)支付。**
因此(13)是准确等式，不只是相差未控制的逐权单位。
本注不要求、更不宣称 $\Xi_{p,m}$ 随 $m$ 解析。

将前述 Newton 笔记的全整数权式代入：
$$
\mathscr E_{j,dk-2}
=U_p(k)c_jK_{j,p}(k)^2,\qquad
U_p(k)=34^2
 (34^{\,1-p}c_\sigma^2)^k
 \frac{p^2}{((k-1)!)^2}.
\tag{15}
$$
$U_p(k)$ 对每个整数 $k\ge1$ 都非零；其可能的非单位幂与阶乘
仍原样在式中。定义
$$
t_{j,p}=\frac{c_j}{a_{j,p}},\qquad
L_p(k)=\ell_{p,dk-2}(e_p^+|_{T(k)}).
$$
由(5)、(13)–(15)，同一个合法整数点上准确有
$$
L_p(k)A_{j,p}^a(T(k))
 =\Xi_{p,dk-2}U_p(k)\,t_{j,p}K_{j,p}(k)^2 .
\tag{16}
$$

消去时不假设 $L_p(k)$ 永远非零：
若至少一条 $K_{j,p}(k)$ 非零，则(16)迫 $L_p(k)\ne0$，
可以除以同一个数；若三条 $K_{j,p}(k)$ 均为零，
所需交叉式两边本来都为零。
所以任何 signed/Hodge 特化的零方向都已包含，
没有跨过一个未付的 exp* 零点作除法。

## 5. 全精度解析交叉恒等式

对任意 $j,\ell\in\mathcal J$，由(16)得到每个整数 $k\ge1$ 上的
交叉式。取 $k=p^n$，这些是真正的合法正权，而非形式负权值。
由(11)和 Newton 的过收敛性，两个交叉乘积均为闭单位圆盘上的
解析函数；它们在 $v=p^n\to0$ 的无穷多个不同点相等。
解析唯一性给
$$
\boxed{
 A_{j,p}^{a}(T(v))\,t_{\ell,p}K_{\ell,p}(v)^2
 =
 A_{\ell,p}^{a}(T(v))\,t_{j,p}K_{j,p}(v)^2 .
}
\tag{17}
$$
这是原三条 signed 坐标之间的全 $p$-精度恒等式。
证明只消去了整数点上明确相同的非零因子；
没有将 $\Xi_{p,m}$ 或 $U_p(k)$ 本身延拓到 $v=0$。

若某一实际 $K_{*,p}$ 是 Tate 单位，则定义
$$
\boxed{
F_p(v)=
 \frac{A_{*,p}^a(T(v))}
      {t_{*,p}K_{*,p}(v)^2}\in\mathcal O\langle v\rangle .
}
\tag{18}
$$
这里只在删掉固定 $c_*$ 的非单位支撑后宣称整；
不需要该删集时同式属于 $F\langle v\rangle$。
(17)给所有三条的准确表示
$$
\boxed{
 A_{j,p}^a(T(v))=F_p(v)t_{j,p}K_{j,p}(v)^2 .
}
\tag{19}
$$
$F_p$ 非零：$K_{*,p}(k)$ 对所有整数 $k\ge1$ 非零，
故(16)使 $A_{*,p}^a(T(k))$ 非零。
定义不依赖选择哪条 Tate 单位 $K_*$；
改变共同 signed 本原基只乘一个共同解析单位。

特别，
$$
\operatorname{ord}_{T=0}A_{j,p}^a
 =\operatorname{ord}_{v=0}F_p
   +2\operatorname{ord}_{v=0}K_{j,p},
\tag{20}
$$
零函数按无穷阶解释。若三条 $K_j$ 都是 Tate 单位，
三条原 signed 坐标有同一个 augmentation 消失阶。
其共同阶仍可能为正；(18)未证明 $F_p(0)\ne0$。
已验证的 $p=29$ 可用于纯 Newton 和相对式(17)；
若要同时宣称(18)中的固定系数为整单位，仍须核其固定常数格，
不能凭 $d_{j,28}$ 的单位性删掉这项。

## 6. 原 $B_j/a_{j,p}$ 与真实基层对数

固定 toric note 给
$$
B_j^2=Cc_j\gamma_j,\qquad
C=-972\omega34^4\epsilon_{\rm per}^{-3}.
$$
若改用原真实 $B_j e_j$ 作为 Artin 基，
$$
A_{j,p}^{B}=\frac{a_{j,p}}{B_j}A_{j,p}^{a},\qquad
t_{j,p}^{B}=\frac{c_j}{B_j}.
$$
所以(17)–(19)逐项改为
$$
\boxed{
A_{j,p}^{B}(T(v))
 =F_p(v)\frac{c_j}{B_j}K_{j,p}(v)^2 .
}
\tag{21}
$$
这没有把既有 $a_{j,p}$ 悄悄改成 $B_j$；
它把全部基变换写在了原式上。

R1049§8已给同一个整局部表示的正规形：
$\log_{\rm BK}=p h/(p+1)$，且 $h$ 是整 $H_f^1$ 的本原坐标。
signed 分解与 augmentation 为真正整 base change，
故可写
$$
\log_{\rm BK}(e_p^+|_{T=0})
=\frac p{p+1}u_p,\qquad u_p\in\mathcal O^\times .
$$
这里 $u_p$ 完全来自已经选定的同一个本原基，
不为了本注重调到1。
原椭圆单位类的基层参数因此准确为
$$
\boxed{
h^{\rm EU}_{j,p}
=u_p\,A_{j,p}^{a}(0)
=u_pF_p(0)\frac{c_j}{a_{j,p}}K_{j,p}(0)^2 .
}
\tag{22}
$$
本式中的 $h^{\rm EU}$ 与原54图的 $h^{\rm geom}$ 是两个不同的实际类；
前者已由(2)固定，后者已由原循环固定。

在全部固定好范围内，现有几何首层为
$$
\frac{a_{j,p}}{B_j}\bar h^{\rm geom}_{j,p}
 =s_p[L:H]\bar K_{j,p}(0),\qquad s_p^2=1 .
$$
故在(18)整的范围内，(22)还给一个保全部实际基的相对首层：
$$
\boxed{
\overline{h^{\rm EU}_{j,p}}
=
\overline{\frac{u_pF_p(0)a_{j,p}}
 {C\gamma_j[L:H]^2}}\,
 \bigl(\overline{h^{\rm geom}_{j,p}}\bigr)^2 .
}
\tag{23}
$$
共同的未知量只有 $u_pF_p(0)$；
(23)没有证明它非零，也没有把模 $p$ 的几何平方提升为全精度的
cycle equality。若要证明 $F_p(0)$ 非零或为单位，
仍须原 mixed signed period 的实际归一或一条真正的全局 cycle 比较。
这项费用不能由三条线分别为单位、共同号、或同一个局部表示来代替。

## 来源与验证范围

- 原 R804、R806：同一 $34\delta$ ray 单位、正 Coleman、18幂等元、30平滑、三个完整角色、实际 $D_j$ 与全权平方。
- T. Tsuji, *Explicit reciprocity law for Lubin–Tate groups*，USC seminar notes（2001），Theorem1.4、Proposition1.7、Theorem4.1：
  <https://swc-math.github.io/notes/files/DLSTsuji1.pdf>。
  正式版本为 *Explicit reciprocity law and formal moduli for Lubin–Tate formal groups*，J. reine angew. Math.569 (2004),103–173：
  <https://doi.org/10.1515/crll.2004.022>。
  这里 $k_{\rm Ts}-j_{\rm Ts}=1$，不是文中另需有限角色条件的差2情形。
- Kato 原 (15.16.1)、Theorem12.5(1) 及 R303§4：同一个单位的两 tensor 特化路径；本注不用 R303 的 HT$(1,0)$ 本原参考类。
- 原负二 Newton / signed 笔记：$K_j$ 的全尾、整数权恒等式、$M^+$ 的原单位归属。
- 固定 weight5 toric Artin 基 note及 R1049§8：$B_j$ 的真实有限 Galois 线、共同相位和原整 BK 参数。

本注没有新增数学执行或数值扫描。
