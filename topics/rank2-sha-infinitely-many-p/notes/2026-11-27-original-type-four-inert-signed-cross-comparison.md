# 原 type4 惰性 signed 坐标的全精度交叉比较与绝对整周期

2026-11-27 UTC。

本注继续[原负二 Newton / signed 笔记](2026-11-27-original-type-four-inert-negative-two-newton-and-signed-line.md)和[固定 weight5 toric Artin 基](2026-11-27-original-weight-five-toric-artin-basis-and-common-phase.md)。新增的是同一原椭圆单位来源的**完整解析交叉恒等式**：三条 signed 坐标与三条 Newton 平方，只差一个共同解析因子。证明先在合法正整数权使用同一 mixed 显式互反律，逐项保留原有限投影、Artin 基、Gamma、Tate 和惰性 Euler；随后才用解析唯一性。不对任何 $p^{\mathrm{weight}}$ 作解析延拓。

§§1–6 先不预设共同因子的 augmentation 非零。§§7–9 随后用原整 universal Coleman 提升及一个合法正权点，证明在至少一条原 Newton K 为 Tate 单位的范围内，该共同因子本身是 Tate 单位；全 norm 与 CM/Tate 格均显示保留。本注仍不将原固定54图类在全精度下直接认作椭圆单位类。

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
到此的相对比较本身尚不排除共同正阶；§§7–9 将在(18)的范围内补上 $F_p(0)$ 为单位的独立整格证明。
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
到此保留的共同量是 $u_pF_p(0)$；(23)本身没有证明其非零，也没有把模 $p$ 的几何平方提升为全精度 cycle equality。下面通过原 mixed 整格及完整 norm trace 支付 $F_p(0)$ 的单位性，不用共同号或同一个局部表示代替该步骤。


## 7. 固定有限分支上的整 Coleman 提升

本节开始补上(18)中共同因子的绝对端点。仍在本注固定好范围内，
特别删除固定 $c_j$ 的非单位支撑。新增论证只使用一个合法正权
$$
m=p-1=d-2,\qquad v=1,\qquad T(1)=Q-1\in p\mathcal O .
\tag{24}
$$
不在 $m$ 上延拓任何 $p$ 的幂，也不调用另一 tame 分支的参考类。

记 $L=K_p$，$L_\infty=L(E_0[p^\infty])$，
$$
\Delta=\operatorname{Gal}(L(E_0[p])/L)
 \simeq\mathbf F_{p^2}^{\times},\qquad
\operatorname{Gal}(L_\infty/L)=\Delta\times\Gamma_2,\quad
\Gamma_2\simeq\mathbf Z_p^2 .
$$
以下“二变量”始终是**取定原 $\Delta$-等型分支后的 pro-$p$ 塔**。
未经该投影，完整 $L_\infty$ 上的 Tate 表示已经平凡，
不能由此声称其未投影 $H^2_{\rm Iw}$ 消失。

令
$$
T_m=\mathcal O(\widehat\psi_0^{-m}
                    \widehat{\bar\psi}_0^{m+1}) .
$$
以 $\bar\psi_0$ 在剩余域上为 $\widehat\psi_0^p$ 的原惯性规范，
(24)给出
$$
\bar T_m|_\Delta:\;2-p,\qquad
\overline{T_m^*(1)}|_\Delta:\;2p-1
       \pmod{p^2-1}.
\tag{25}
$$
二者均非零。因此选定分支上
$H^0(L,\bar T_m)=H^0(L,\overline{T_m^*(1)})=0$。
同一结论对基层 $T_{\rm CM}$ 成立；
(12)的全部反圆分变权保持这个剩余分支。

取 $R=\mathcal O[[\Gamma_2]]$ 及实际 tautological 逆作用构成的
二变量表示。局部 Galois 上同调的整 perfect complex 在剩余域上
由(25)、Tate 对偶和 Euler 特征仅有 $H^1$，维数为2。
Derived Nakayama 因而将这个 complex 整地化为
$R^2[-1]$。特别对反圆分 quotient 和(24)的权特殊化均有
$$
H^1_{\rm Iw,\,\Delta}(L_\infty/L,T_m)
          \otimes_R R/I
 \;\xrightarrow{\ \sim\ }\;
H^1(L,\mathbb T_m\otimes_RR/I).
\tag{26}
$$
这里可用 BKNKO Proposition2.12 的同一个 perfect-complex 证明；
在 $G_L$ 上只用刚显示的两个不变向量空间消失，
并未给任意二变量变形额外加 symplectic 条件。
等价地，可先诱导到 $G_{\mathbf Q_p}$ 再用相同控制论证。

还须核(26)中的整原像真正来自单位。Kummer 扭曲的附加因子为
$$
T_m(-1)=
 \mathcal O(\widehat\psi_0^{-m-1}\widehat{\bar\psi}_0^m),
\qquad
T_m(-1)|_\Delta:\;1-2p .
\tag{27}
$$
局部乘法群的 valuation 商在 $\Delta$ 上平凡，
而 $1-2p\not\equiv0\bmod p^2-1$。
所以在当前实际分支，valuation 商严格为零。
$|\Delta|=p^2-1$ 是单位，整个等型投影没有 $p$ 分母。
因此(26)给每个整局部类，尤其
$e_p^+|_{T(1)}$，一个**整 norm-compatible 单位系统**的原像。
这是 Kummer、原 tensor twist 和原 finite idempotent 的复合；
不以某个已知非零 exponential 的有理逆像代替整原像。

Coleman Theorem2.1 及 Tsuji Proposition2.2 将它表示为
$$
f\in\Gamma(\widehat E_0^{\,\rm univ},\mathcal O^\times),
\qquad \operatorname{Norm}_{\Phi}f=f,
\qquad \left.\Phi\right|_{\rm CM}=[-p]
\tag{28}
$$
的整 universal Coleman 单位。
有限系数扩张仅作外部 $\mathcal O$-线性张量；
若先在有限不分歧系数域写 Coleman 函数，须保其完整 Frobenius，
再沿同一个 $\Delta$ 分支下降。这里可在 $L$ 上作(28)，
故下面没有被省略的未分歧系数角色。

## 8. 原混合微分的整界及完整一层范数

### 8.1 整 PD 格

在 CM 点的整 PD 包络上，Tsuji §1 给
$$
H^1_{\rm dR}(\widehat E_0^{\,\rm univ})
 \simeq \mathcal O_{M^{\rm PD}}\otimes_{\mathcal O_L}
                  H^1_{\rm dR}(E_0/\mathcal O_L).
$$
因 $L/\mathbf Q_p$ 不分歧，两个 CM 幂等元及水平 splitting 都整。
Gauss–Manin connection、Kodaira–Spencer 同构及该 splitting
组成的 $\mathfrak D_p$ 因而保持整 PD 截面。
对(28)，无需先把 $\log f$ 当成整函数：
$$
\partial\log f=f^{-1}\partial f
$$
已经整。定义
$$
R_m(f)=
 \left.\mathfrak D_p^m\partial\log f\right|_O
 \in\mathcal O\,\omega_0^{\,2m+1},
\qquad \omega_0=\frac{dx}{2y}.
\tag{29}
$$
在(24)上 $m!=(p-1)!$ 是单位，所以 $R_m(f)/m!$ 仍整。
这里使用的目标格是 Tsuji Theorem4.1 原本的
$\operatorname{coLie}(E_0)^{\otimes(2p-1)}$，
不是另选一个未定 CM period 的格。

### 8.2 全混合 isogeny 因子

设 $\phi$ 为 degree $q$ 的 CM isogeny，实际微分拉回标量为 $c$。
杯积自然性给
$$
\operatorname{KS}_{\rm src}(\phi^*\omega^2)
   =q\,\phi^*\operatorname{KS}_{\rm tgt}(\omega^2).
$$
水平 CM 投影与 $\phi^*$ 交换，故逐次有
$$
\mathfrak D_{p,\rm src}^{\,m}(\phi^*s)
     =q^{-m}\phi^*(\mathfrak D_{p,\rm tgt}^{\,m}s).
\tag{30}
$$
其中 $\phi^*$ 是**完整张量拉回**，不是只把函数自变量复合。
在当前权 $2m+1$，实际系数是
$$
\frac{c^{\,2m+1}}{q^m}
   =\frac{c^{\,m+1}}{\bar c^{\,m}} .
$$
对于(28)的 $\Phi=[-p]$，$c=-p,\ q=p^2$，所以
$$
\frac{c^{\,2m+1}}{q^m}=-p
\quad\text{对所有 }m.
\tag{31}
$$
这里 $\Phi$ 是 Tsuji Proposition2.2 的实际 universal 延伸；只在 CM 纤维读取 $c=-p$。式(30)保留其 base map、Gauss–Manin 和全部张量，不把 universal Frobenius 的 base map 先当成恒等，也不需要任意延伸一个非有理 CM 自同源。

现在对(28)的全 norm 恒等式
$$
\prod_{\xi\in\ker\Phi} f(P+\xi)=\Phi^*f(P)
$$
先施 $\partial\log$，再施完整 $\mathfrak D_p^m$。
在特征零有限 étale $p$-torsion cover 上微分与全 trace 交换；
(30)保持 moving torsion 的所有项。因此在同一个 CM 点
$$
\sum_{\xi\in E_0[p]}
 \left.\mathfrak D_p^m\partial\log f\right|_\xi
   =-p\,R_m(f).
\tag{32}
$$
去掉 $\xi=O$ 后，完整非零 $p$-torsion 和为
$(-p-1)R_m(f)$。这一步保留了全部 $p^2-1$ 个点，
没有用单个 primitive 点的整性代替迹的整性。


为核定 tame 度数，设
$$
x_{f,1}=\operatorname{pr}_{L_1}
  \operatorname{tw}_{m+1,m}(f),\qquad
x_f:=\operatorname{cor}_{L_1/L}(x_{f,1}),
\quad L_1=L(E_0[p]).
\tag{32a}
$$
这是 Tsuji Theorem4.1 在 inverse-limit 类上的实际第一层特殊化，
其后接**未归一化 corestriction**；norm compatibility 使它也等于
从任一更高层 corestrict 回 $L$ 的类。
所以 $\exp^*(x_f)=\operatorname{Tr}_{L_1/L}\exp^*(x_{f,1})$，
而 $\operatorname{Gal}(L_1/L)=\Delta$ 把所选原始点遍历非零
$p$-torsion，恰好一次。迹中共有 $p^2-1$ 项，没有再除该数。

(26)在 pro-$p$ 分支与 full LT 写法之间的整同构采用这同一个
corestriction。若反方向用 restriction 来选 full LT 原像，
须先乘 $(p^2-1)^{-1}$，因为
$\operatorname{cor}\circ\operatorname{res}=p^2-1$。
这枚整单位已经包含在该原像 Coleman 函数的选择中，
不能在下面(33)外再乘或再除一次。
原 R804 的 $\operatorname{pr}_K$ 本来就是实际
Iwasawa corestriction；它的指定椭圆单位因此使用原函数和原全迹，
没有在此被改成一个 normalized tame average。

Tsuji Theorem4.1 在第1层的系数准确是
$$
\frac{(-1)^m}{m!}
 \pi^{-(m+1)}\bar\pi^m
 =\frac{(-1)^m}{m!(-p)} .
$$
corestriction 与 dual exponential 交换。
把(32)的非零点迹代入，得到底层的**完整**公式
$$
\boxed{
\exp^*_{T_m}(x_f)
 =\frac{(-1)^m}{m!}
      \left(1+\frac1p\right)R_m(f).
}
\tag{33}
$$
若先在不分歧 $H/L$ 写原函数，则中间式是
$R_m(f)-\pi^{-1}\sigma^{-1}R_m(f)$；
下降到本节的实际 $L$-单位后正是(33)。
不把 $1+p^{-1}$ 改成单位或删去其 $-1$ 赋值。

由(26)–(29)，(33)不仅适用于一个特殊椭圆单位：
它给原整局部格的上界
$$
\boxed{
\exp^*_{T_m}\bigl(H^1(L,T_m)\bigr)
 \subseteq p^{-1}\mathcal O\,\omega_0^{\,2p-1},
 \qquad m=p-1 .
}
\tag{34}
$$
若某个类在 exponential 的核中，其值为0，仍包括在(34)内。
本结论没有先假设 signed 生成元的 exponential 是单位。

### 8.3 原 Tate 基不带隐藏的非单位 period

保持 R804 的 $\xi_{\rm LT},\xi_{\rm cyc}$。
以原整 Weil/CM tensor 同构定义
$$
\mathrm W(\xi_{\rm LT}\otimes\bar\xi_{\rm LT})
       =\epsilon_{{\rm T},p}\xi_{\rm cyc},
       \qquad \epsilon_{{\rm T},p}\in\mathcal O^\times .
\tag{35}
$$
整性和单位性来自原 Tate 格上的完美 Weil pairing；
$2\delta$ 的 trace-dual 基变换在当前位为单位。
这里 $\epsilon_{{\rm T},p}$ 是这两个**已经选定的整基**的比，
不是 $\mathbf C_p$ 中可任意选取的 CM period。

Tsuji 的扭曲向量
$\xi_{\rm LT}^{-m-1}\bar\xi_{\rm LT}^{m}$
与 R804/R303 的
$\xi_{\rm LT}^{-(2m+1)}\xi_{\rm cyc}^{m}$
准确相差 $\epsilon_{{\rm T},p}^{m}$。
所以按原基读取(33)时，同乘
$\epsilon_{{\rm T},p}^{-m}$。
它使(34)保持不变，并且须在下面实际值中同留。
原 Artin 方向仍是(4)的 $a_{j,p}^{-1}$。
因而整界与实际椭圆单位值是在**同一**
$\omega_0^{2p-1}$ 格里比较，没有把一个非单位周期藏进
$\Xi_{p,m}$ 后再宣称它是单位。

## 9. 实际椭圆单位取到整界，故共同因子为单位

对原(2)的 norm-compatible 单位，(6)就是(29)在同一全 ray norm、
同一 $e_{\eta_j}$ 和 $1/30$ 后的系数。
$\eta_j((p))=1$ 使该不分歧有限来源在所选惰性位的 norm
回到(33)中的同一支；没有另取一个共轭类。

因此在固定嵌入、完整原平均的写法下，(9)、(33)、(35)给
$$
\begin{split}
\ell_{p,m}\bigl(\iota_{j,p}^a
              \boldsymbol z_{j,p}|_{T(1)}\bigr)
 &=
 \epsilon_{{\rm T},p}^{-m}
 \frac{(-1)^m}{m!}\left(1+\frac1p\right)
       \frac{\mathcal R_{j,m}}{a_{j,p}}\\
 &=
 \epsilon_{{\rm T},p}^{-m}(-1)^m
 \frac{\mu}{18}\,m!
 \left(1+\frac1p\right)
       \frac{\mathscr E_{j,m}}{a_{j,p}},
 \qquad m=p-1 .
\end{split}
\tag{36}
$$
本式的18仍是(6)中原 $e_\eta$ 的18。
若沿 R804 用 induced 特殊化写法，则按
$\nu(e_\eta)=1$ 同步表示同一 finite trace；
不得在(36)之外再乘或再除18。
无论使用哪一同构写法，(34)与(36)采用完全相同的坐标。
本处所需赋值由显示的原常数决定：
$\mu,18,(p-1)!,a_{j,p},\epsilon_{{\rm T},p}$ 全为单位，
而唯一显示的 $p$ Euler 赋值是 $-1$。

假定存在原 $j=*$ 使 $K_{*,p}$ 为 Tate 单位。
由原 Newton 首层等价及(15)，
$$
d_{*,p-1}\in\mathcal O^\times,\qquad
\mathscr E_{*,p-1}
 =c_*34^{-(p-1)}d_{*,p-1}^{\,2}\in\mathcal O^\times .
$$
所以实际原类满足
$$
v_p\,\ell_{p,p-1}\bigl(
 \iota_{*,p}^a\boldsymbol z_{*,p}|_{T(1)}\bigr)=-1.
\tag{37}
$$
令 $e=e_p^+|_{T(1)}$。它是整局部类，故(34)给
$v_p\ell_{p,p-1}(e)\ge-1$。
再用真正的 signed 等式
$$
\iota_{*,p}^a\boldsymbol z_{*,p}|_{T(1)}
             =A_{*,p}^a(T(1))\,e
$$
及 $A_{*,p}^a(T(1))\in\mathcal O$，(37)迫
$$
\boxed{
A_{*,p}^a(T(1))\in\mathcal O^\times,
\qquad v_p\ell_{p,p-1}(e)=-1.
}
\tag{38}
$$
这里没有先知道 $e$ 的具体 exponential，也没有用其“非零”
代替赋值；其准确赋值是由整界与实际原类一起迫出的。

因 $T(1)\in p\mathcal O$，真正的 Iwasawa 整性立即给
$$
A_{*,p}^a(0)\equiv A_{*,p}^a(T(1))\not\equiv0\pmod p .
$$
于是 $A_{*,p}^a(T(v))$ 是闭单位圆盘上的 Tate 单位。
代入(18)，得到本注的绝对强化：
$$
\boxed{
F_p(v)\in\mathcal O\langle v\rangle^\times .
}
\tag{39}
$$
它的前提恰是(18)定义该共同因子时的原范围：
至少一条 $K_*$ 为 Tate 单位，且固定非零 $c_*$ 在当前位为单位。
不是在没有这些前提时单凭交叉式宣称所有共同因子单位。

现在(19)在该范围内有完整赋值和端点结论：
$$
\boxed{
v_p A_{j,p}^a(0)=2v_p K_{j,p}(0),\qquad
h_{j,p}^{\rm EU}
 =u_pF_p(0)\frac{c_j}{a_{j,p}}K_{j,p}(0)^2 .
}
\tag{40}
$$
零值允许无穷赋值。特别
$$
K_{j,p}(0)\ne0
 \quad\Longleftrightarrow\quad
\operatorname{loc}_p z_j\ne0 ,
\tag{41}
$$
因为原 augmentation 位于整 $H_f^1$，其实际
Bloch–Kato 对数是 $p h/(p+1)$，由 R1049§8 已付为同构。
这是真实 R804 全局类的指定局部化，非另造一个对数逆像。

若 $K_j$ 在 $v=0$ 的首非零项为 $k_{j,e}v^e$，则还准确有
$$
\operatorname{ord}_{T=0}A_j^a=2e,\qquad
v_p([T^{2e}]A_j^a)=2v_p(k_{j,e})-2e .
\tag{42}
$$
这只用 $\log Q$ 赋值1和(39)。
它不是将 $p^{\mathrm{weight}}$ 或逐权 period 解析延拓后的结论。

## 10. 对原几何首层的准确消费范围

完整未平方 toric 源已经把 §6 的共同剩余号锁定，
但本节只需要其平方恒等式。结合(23)、(39)，得到
$$
\boxed{
\overline{h^{\rm EU}_{j,p}}\ne0
 \quad\Longleftrightarrow\quad
\overline{h^{\rm geom}_{j,p}}\ne0
 \quad\Longleftrightarrow\quad
\overline{K_{j,p}(0)}\ne0
}
\tag{43}
$$
于原几何好模型、$p>q_0$、全部固定常数为单位且至少一条
$K_*$ 为 Tate 单位的范围。
最后一个“至少一条”在欲使用某个非零几何首层时由该首层自己支付；
并非增加一个独立的非零假设。

(43)仍保持原 $B_j/a_{j,p}$、$[L:H]$ 和
$C=-972\omega34^4\epsilon_{\rm per}^{-3}$ 的尺度。
它并未把两类在全 $p$ 精度下直接认作同一个 cycle，
也未证明有无穷多个 $p$ 使这些首层非零。
原固定 $p=29$ 的三个 $K_j$ 单位属于纯 Newton 已验结论；
若要在29直接使用(39)–(43)，仍须另外保留这里列出的
固定 $c_j$、几何常数和整模型好范围，不能以纯 Newton 检查替代。

本强化没有新增数学执行。所需原文位置是
Tsuji §1 的整 PD splitting、Proposition2.2 的整 universal
Coleman lift、Theorem4.1 的原 mixed reciprocity，
以及 BKNKO Proposition2.12 的整上同调 base change 证明。

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
