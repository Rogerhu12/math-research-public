# R846 — 原完整 Hom 的三阶特征排除全部 generating genus-four 项

日期：2026-11-16。**状态：下列原来源排除定理已证明。**

本篇接 R841 的实际对称 polarization、R844 的完整域下降，
证明原有限曲线表达中任何生成 $E_0^3$ 的像，其正规化亏格
至少为5。证明读取同一个 $J_0(10404)$ 的**全部**
$K_3$-定义 Hom，包含所有可能的 Galois 诱导来源；
没有只检验某个 CM Fourier eigline。

这不证明原最高 Chow 类为零。亏格至少五的曲线项及其
指定有限线性组合仍保留，原端点到 R814 canonical 类的
比较也未由此完成。

## 1. 固定原实际映射及待排假设

沿 R841 B、R844，固定
$$
K=\mathbf Q(\omega),\quad E_0:y^2=x^3+1,\quad
X=X_0(10404),\quad C=X_0(2601),
$$
$$
\eta=\eta_{10},\quad \mathcal H=H_{34},\quad
K_3=K(17^{1/3}),\quad
\operatorname{Gal}(\mathcal H/K_3)=\langle\tau\rangle\simeq C_6 .
$$
原实际项为
$$
\Phi=(F,a q_0,a q_2):X\longrightarrow E_0^3,
\tag{1}
$$
其中 $F$ 经整个原 $f=\theta(\eta^3\psi_0)$ 因子，
$a$ 经整个原有理 packet
$\{\theta(\eta_j^{-2}\psi_0):j=4,10,16\}$。
保留原 $q_0:z\mapsto z$、$q_2:z\mapsto4z$、
cusp $\infty$ 基点、真实 $R:z\mapsto z+1/3$ 和
$S:z\mapsto z+1/2$。

假设 (1) 的像生成整个目标，正规化 $D$ 的亏格为4。
R844 的完整 Hom 下降已给 $K_3$ 上的
$X_{K_3}\to D_0$、两个自同构 $v,s$ 和模型
$$
D_0:\quad y^3=d\,x(x^4+A x^2+B),\qquad
d,A,B\in K_3,\quad dB(A^2-4B)\ne0,
\tag{2}
$$
$$
v(x,y)=(x,\omega y),\qquad s(x,y)=(-x,-y).
$$
$d$ 是保留的真实 cubic twist。
原目标同时下降为
$$
B_f\times B_g^2,
\tag{3}
$$
其中 $B_f\sim_{K_3}E_{17}$，
$E_{17}:y^2=x^3+17$；$B_g$ 是原 packet 在 $K_3$ 上的
共同 elliptic twist。

为彻底固定逆号，下文始终用**实际 Hom 到 $E_0$**
的 Galois 角色，记为 $\kappa_f,\kappa_g$。
R844 的 (13)–(17) 给
$$
\kappa_f=\eta^{-3}|_{G_{K_3}},\qquad
\kappa_g=\eta^{2}|_{G_{K_3}},\qquad
\kappa_f(\tau)=-1,\quad\kappa_g(\tau)=\omega.
\tag{4}
$$
特别 $\kappa_f^2=1$。目标的 Tate twist 角色是 (4) 的逆，
本篇不在两种约定间省略一个逆号。

## 2. 原属二商的已知 elliptic quotient 和剩余因子

取同一个二阶商
$$
H=D_0/\langle s\rangle .
$$
其真实不变量是
$$
z=y/x,\qquad W=d(x^2-B/x^2),
$$
所以
$$
H:\quad W^2=z^6-2dAz^3+d^2(A^2-4B).
\tag{5}
$$
三阶作用下降为
$$
r(z,W)=(\omega z,W).
\tag{6}
$$
在 $H^0(H,\Omega^1)$ 上，$dz/W$、$z\,dz/W$
的特征分别为 $\omega,\omega^2$。
$H/\langle r\rangle$ 为亏格0，因而
$1+r+r^2=0$ 于真正的 $\operatorname{End}J(H)$。

原 (1) 的 $s$-不变目标方向给一个非零的
$K_3$-同态
$$
Q:J(H)\longrightarrow B_g,\qquad Qr=[\omega]Q.
\tag{7}
$$
这里 $a q_2$ 逐点由 $S$ 固定，故 (7) 来自原实际映射，
不是重新选择一个 genus-two quotient。
令 $B_h=(\ker Q)^0$。它是 $K_3$ 上的 elliptic curve，
$r$ 保持它，并在其全纯微分上作用为 $\omega^2$。
故
$$
j(B_h)=0,\qquad r|_{B_h}=[\omega^2].
\tag{8}
$$
(8) 中的 CM 标号按全纯微分规范确定。

以 $Q$ 的极化对偶选取 $K_3$-定义的同源补，
可以在有理同态范畴写
$$
J(H)\sim_{K_3}B_g\times B_h.
\tag{9}
$$
两份 $j=0$ 曲线的 CM endomorphism 都在 $K_3$ 定义。
在第一份取 $[\omega]=r$，在第二份取
$[\omega]=r^{-1}$，得到 $J(H)$ 上的中心 CM endomorphism
$u$，全纯微分上为标量 $\omega$。
它确实是几何 $\operatorname{End}^0J(H)\simeq M_2(K)$
的中心：任一 elliptic Hom 在特征零下与两端这个相同
微分标号的 CM 单位交换。

因此原两个 rational projectors 可写成
$$
e_g=\frac{r-u^2}{u-u^2},\qquad e_h=1-e_g.
\tag{10}
$$
它们在 $K_3$ 定义，像分别为 (9) 的两份同源因子。
在该式中 $u-u^2$ 是可逆的中心 endomorphism；
没有把 $r$ 自身误称为整个 $J(H)$ 的中心 CM 作用。

## 3. 原归一根的准确 Kummer 角色

R844 已付 $\beta=\sqrt B\in K_3$，以及两个实际 $j=0$
Prym 商
$$
\mathcal E_\pm:\quad Y_\pm^2=X_\pm^3+c_\pm,\qquad
c_\pm=d^4(-A\pm2\beta).
\tag{11}
$$
它们在 $K_3$ 上的两份同源类型，准确为
$B_f,B_g$，允许交换。

对 $E_c:y^2=x^3+c$，选择 $s_c^6=c$，
真实同构
$$
\iota_c:E_c\to E_0,\qquad
(x,y)\longmapsto(x/s_c^2,y/s_c^3)
$$
在微分上满足 $\iota_c^*\omega_0=s_c\omega_c$。
故对 $\gamma$，
$$
\boxed{
\iota_c^\gamma=
[s_c^\gamma/s_c]\,\iota_c.}
\tag{12}
$$
右侧 $[\zeta]$ 用微分特征 $\zeta$ 定义 CM 单位。
(12) 明确表明 sextic Kummer 角色就是
$\operatorname{Hom}(E_c,E_0)$ 的角色；
它是相对于 $E_0$ 的 Tate twist 角色的逆。

选择
$$
c^6=d^2(A^2-4B).
\tag{13}
$$
因为
$$
c_+c_-=d^8(A^2-4B)=d^6c^6,
$$
(11)、(12) 给出对全部 $G_{K_3}$ 的准确等式
$$
\boxed{\kappa_c(\gamma):=c^\gamma/c
=\kappa_f(\gamma)\kappa_g(\gamma).}
\tag{14}
$$
若交换 $\mathcal E_+$、$\mathcal E_-$，乘积不变。
没有删掉 $d$，也没有用一个只在17惯性上的等式替代
完整 (14)。由 (4)，
$\kappa_c(\tau)=-\omega$，它有准确阶6，
并切出原 $\mathcal H/K_3$。

## 4. 真实 reciprocal involution 的非零交叉 Hom

在 (5) 上定义
$$
t_c(z,W)=(c^2/z,\ c^3W/z^3).
\tag{15}
$$
由 (13) 可直接代入检查，它是延拓到光滑曲线的
involution；它在 Jacobian 上仍记为 $t_c$。
有
$$
t_c^2=1,\qquad t_c r t_c=r^{-1}.
\tag{16}
$$
在曲线上的 hyperelliptic involution 记为 $\iota$；
其 Jacobian 作用是 $[-1]$。

固定 $\zeta_6=-\omega^2$，故 $\zeta_6^2=\omega$、
$\zeta_6^3=-1$。
若 $\gamma(c)=\zeta_6^k c$，则在原 (5) 坐标上准确有
$$
t_c^\gamma=\iota^k r^k t_c,\qquad
(t_c)_*^\gamma=(-1)^k r^k(t_c)_*.
\tag{17}
$$
这是同一个 $K_3$ 模型上的式子，已包括
$c^3$ 的符号和完整二次 twist，不能只保留 $r^k$。

中心 $u$ 与 $t_c$ 交换，(16) 因而使 (10) 两个
projectors 交换：
$$
t_c e_g=e_h t_c.
$$
所以
$$
T=e_h t_c e_g
\tag{18}
$$
是一个**非零**的 $B_g\to B_h$ 有理 Hom。
确实 $t_c$ 可逆，$e_g$ 的像维数1；
若 (18) 为零，就与上述交换式和 $t_c e_g\ne0$ 矛盾。

由于 $e_g,e_h$ 均在 $K_3$ 定义，(17)、(18) 给
$$
T^\gamma=(-1)^k r^kT
=(-1)^k[\omega^{2k}]T
=[\zeta_6^k]T
=\kappa_c(\gamma)T.
\tag{19}
$$
这里第二式使用的是**目标 $B_h$** 上的 (8)。
这是符号与角色的关键位置。

令 $\kappa_h$ 为 $\operatorname{Hom}(B_h,E_0)$ 的实际
sextic 角色。选择两条几何同构到 $E_0$ 后，
$\operatorname{Hom}^0(B_g,B_h)$ 是一维 $K$-空间，
其 Galois 角色为 $\kappa_g\kappa_h^{-1}$。
由 (18) 的非零和 (19)，
$$
\kappa_g\kappa_h^{-1}=\kappa_c=\kappa_f\kappa_g .
$$
故
$$
\boxed{
\kappa_h=\kappa_f^{-1}=\kappa_f,\qquad
B_h\sim_{K_3}E_{17}.
}
\tag{20}
$$
最后一步也可由 (12) 的 Kummer 分类得到一个
$K_3$-同构；本篇只需非零同源。
(20) 是原整个 Galois 角色结论，不只由 $j=0$ 或
某个有限 Frobenius 值推出。

## 5. 原曲线强迫的“错误三阶特征”Hom

原非恒定 $X_{K_3}\to D_0$ 给满的 Jacobian norm，
再经 $D_0\to H$ 及 (10) 的 $B_h$ 投影，得到非零
$K_3$-有理同态。将其与 (20) 的一个 $K_3$-同源复合，
得到
$$
\varphi:J_0(10404)\longrightarrow E_{17},
\qquad \varphi\ne0.
$$
全部映射保原 $R$，而 (8) 在 $B_h$ 上读取
$\omega^2$，所以
$$
\boxed{\varphi R=[\omega^2]\varphi.}
\tag{21}
$$
特征零 elliptic Hom 与两端按全纯微分规范定义的 CM 单位
相容，故 (20) 的同源不改变这个标号。

下面证明原完整 Hom 空间实际上只允许 $\omega$。
这一步必须包含所有来源，不能只看原三个选定形式。

## 6. 全部 $K_3$-定义 Hom 的精确三份下降

写 $t=17^{1/3}$，取
$\gamma\in\operatorname{Gal}(K_3/K)$ 使 $\gamma(t)=\omega t$。
对于任何 $K$-定义阿贝尔簇 $A$，空间
$\operatorname{Hom}_{K_3}^0(A,E_{17})$ 是带后复合 CM
$K$-标量的向量空间。
有限三阶 Galois 作用可准确分为三个本征部分：
$$
\varphi=\varphi_0+\varphi_1+\varphi_2,\qquad
\varphi_i^\gamma=[\omega^i]\varphi_i,
$$
$$
\varphi_i=\frac13\sum_{a=0}^2
 [\omega^{-ia}]\varphi^{\gamma^a}.
\tag{22}
$$

对 $i=0,1,2$ 取原有理曲线
$$
E_i:\quad y^2=x^3+17^{2i+1}
$$
和真实 $K_3$-同构
$$
\iota_i:E_i\longrightarrow E_{17},\qquad
(x,y)\longmapsto(x/t^{2i},y/t^{3i}).
\tag{23}
$$
直接代入曲线方程及 (12) 给
$$
\iota_i^\gamma=[\omega^i]\iota_i.
$$
所以
$$
\psi_i=\iota_i^{-1}\varphi_i\in\operatorname{Hom}_K^0(A,E_i).
$$
准确得到
$$
\boxed{
\operatorname{Hom}_{K_3}^0(A,E_{17})
=\sum_{i=0}^2
 \iota_i\,\operatorname{Hom}_K^0(A,E_{17^{\,2i+1}}).
}
\tag{24}
$$
这是对任意 $A/K$ 的整个 Hom 空间成立的实际下降，
并非假定 $A$ 只有 CM 因子。
在 Tate 语言中它正是 Frobenius reciprocity 的三份
$\eta^{3+6i}\psi_0$；(22)、(23) 已把它直接实现，
没有漏掉一个可能由非 CM 或诱导表示产生的 Hom。

## 7. 从 $K$ 到 $\mathbf Q$ 的全部 Hom，以及原精确 level

现在令 $A=J_0(10404)$。每个 $E_i$ 在 $\mathbf Q$ 定义，
在 $K$ 上有 CM endomorphism $[\delta]$，
$\delta=\sqrt{-3}$，且 $[\delta]^c=-[\delta]$、
$[\delta]^2=[-3]$。

对任意 $\psi\in\operatorname{Hom}_K^0(A,E_i)$，置
$\psi_\pm=(\psi\pm\psi^c)/2$。
$\psi_+$ 在 $\mathbf Q$ 定义，
$[\delta]\psi_-$ 也在 $\mathbf Q$ 定义。因此
$$
\boxed{
\operatorname{Hom}_K^0(A,E_i)
=\operatorname{Hom}_{\mathbf Q}^0(A,E_i)
 +[\delta]\operatorname{Hom}_{\mathbf Q}^0(A,E_i).
}
\tag{25}
$$
这包含所有二次 base-change 的可能性；
没有假设某个随意选择的 Hom 已经在 $\mathbf Q$ 定义。

还须核 (25) 中全部有理 Hom 的原 level。
$E_i$ 的 CM 角色准确为
$$
\psi_i^{\rm CM}=\eta^{3+6i}\psi_0
=\psi_{17^{2i+1}}.
\tag{26}
$$
R806/R826 的全局有限表逐处给：

- 在2处，$\eta^{3+6i}$ 的 cubic 单位角色平凡，
  所以保留 $\psi_0$ 的非平凡 cubic 单位角色，导子恰 $(2)$；
- 在3处，$\eta$ 不分歧，保留原 $\psi_0$ 的导子 $(\delta)$；
- 在17处，三条有限角色的单位阶分别为 $6,2,6$，
  均真正分歧且导子恰 $(17)$；
- 其它有限位不分歧。

因此三条都是导子恰 $(34\delta)$ 的原 type-$(1,0)$
CM 角色，其 rational weight-two newforms
$$
f_i=\theta(\eta^{3+6i}\psi_0)
$$
的**最小 level** 均为
$$
\boxed{|D_K|\mathrm N(34\delta)=10404.}
\tag{27}
$$
这也是三条 $E_i/\mathbf Q$ 的导子。
特别它们在本篇 $J_0(10404)$ 中都位于 new 部分，
没有来自更低 level 的 $Q^2$ 或其它 old 副本。

标准 newform decomposition 与 multiplicity one
说明每个 rational newform $f_i$ 在这个最小 level
只出现一次。配合权一同态定理，
$\operatorname{Hom}_{\mathbf Q}^0(J_0(10404),E_i)$
由其原 modular quotient 生成，维数为1。
其余非 CM 新因子、不同 CM 新因子与所有 old 因子
对 $E_i$ 的有理 Hom 都为零：
一个非零 Hom 将使 $E_i$ 成为该因子的有理同源因子，
由全部好素数的 Tate/Hecke 特征及 multiplicity one
必须给同一个 $f_i$；old 因子的更低最小导子又与 (27) 冲突。
这给出 (25) 所需的**完整**排除，不只是列出三个可见形式。

## 8. $R$ 在原全部 Hom 上只具有 $\omega$ 特征

对素于3的每个 $K$-整理想，其范数为 $1\bmod3$：
split 素理想的范数是 $1\bmod3$，
inert 素理想的范数是有理素数的平方，
三处 ramified 理想已由 primitive 导子排除。
所以 (26) 的完整 ideal series 满足
$$
f_i(Q)=\sum_{n\equiv1\ (3)}a_nQ^n.
\tag{28}
$$
R841 已在原 $X_0(10404)$ 上支付
$R^*Q=\omega Q$。因此
$$
R^*(f_i(Q)\,dQ/Q)=\omega\,f_i(Q)\,dQ/Q.
\tag{29}
$$

令 $\psi:J_0(10404)\to E_i$ 是一个有理 modular quotient。
其微分拉回是 (28) 的非零常数倍。
由 (29) 以及 $[\omega]^*\omega_{E_i}=\omega\omega_{E_i}$，
两条真实 Hom $\psi R$、$[\omega]\psi$ 的微分相同。
特征零下阿贝尔簇到 elliptic curve 的 Hom
若微分为零则是零，故
$$
\psi R=[\omega]\psi.
$$
由第7节的全部 Hom 描述、$[\delta]$ 与 $[\omega]$
交换，再用 (23) 也与 CM 单位交换，严格得到
$$
\boxed{
\varphi R=[\omega]\varphi
\quad\text{对所有 }\ 
\varphi\in\operatorname{Hom}_{K_3}^0
 \bigl(J_0(10404),E_{17}\bigr).
}
\tag{30}
$$
因此 (30) 是原整个 Hom 的等式。
它没有把某个 Fourier 系数恒等式无条件推广到未知映射；
所需全空间已经由 (22)–(27) 逐层支付。

## 9. 矛盾与原有限曲线表达的准确后果

由属四假设构造的非零 Hom 满足 (21)，
而整个原空间必须满足 (30)。相减得到
$$
[\omega-\omega^2]\varphi=0.
$$
$[\omega-\omega^2]$ 是 elliptic curve 的非零同源，
有理 Hom 群无挠，故 $\varphi=0$，与第5节矛盾。

于是：
$$
\boxed{
\text{R841 B 的每个生成 }E_0^3\text{ 的实际曲线像，
其正规化亏格均至少为5。}
}
\tag{31}
$$
R841 A 已排亏格至多3，本篇排的是其余全部亏格4项。
范围包括 polarization 中的所有 $a$、
$a+b$ 和全部实际 Galois-Artin 系数；
没有只排某个选定的 $\eta_j$ eigline。

R843/R844 的商、CM order17、邻点 order34 等条件性
几何结论保持有效；本篇进一步说明这些必要条件不能在
**当前原 modular Hom 表达**的 genus-four 分支实现。
一般具有这些 CM 性质的属四曲线不被本篇排除，
也不能将它们倒装为原来源的实际项。

原最高类仍是 R839/R841 的有限曲线像和，
其可能非零的 generating 项现在只剩亏格至少5。
本篇未证明它们的总和为零或非零，
未改变原 $q_0/q_2$、原 finite test vector 或 critical projector，
未产生 R814 canonical 比例，未给新的跨 $p$ AJ 非消失。
全部 $\deg(X\to D)$、平均/polarization 系数、
$6^{-2}$、$X_1$ 的 $1632/816$ 和 $12^{-2}$ 原样保留。

## 10. 依赖与证明范围

全文没有新增数值计算或素数扫描。
关键非零对象 (18) 是可逆曲线 involution 的实际交叉分量；
最终矛盾来自 (30) 的完整原 Hom 空间。

- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)
  附录 A、B：原完整 Hom、真实 $R,S$、最低亏格与 genus-four 模型。
- [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)
  §§2–7：$H_{34}/K_3$、全 Hom 的 $\tau$、
  真下降、$\sqrt B\in K_3$ 和两个实际 Prym 因子。
- [R843](R843-actual-genus-four-quotient-and-cm-three-isogeny.md)
  正文及附录 A：同一个属二商、$r,t$、
  真实 $j=0$ quotient 与 norm/pullback。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、
  [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)：
  完整 $\eta$、$\psi_0$ 坏位及
  $\eta^{3},\eta^{9},\eta^{15}$ 的原 rational CM 曲线。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原层级与 old 副本的实际区别。
- A. O. L. Atkin and J. Lehner,
  *Hecke operators on $\Gamma_0(m)$*, Math. Ann. **185**
  (1970), 134–160：
  <https://doi.org/10.1007/BF01359701>。
  所用为 new/old 分解和最小 level 上 normalized newform
  的 multiplicity one；并未使用其 normalizer 分类，
  本篇 $R$ 已由 R841 在原层级自含证明。
- G. Faltings, *Endlichkeitssätze für abelsche Varietäten über
  Zahlkörpern*, Invent. Math. **73** (1983), 349–366：
  第7节仅用权一 Hom/同源定理把同一原 newform 因子与实际
  abelian-variety Hom 相认；不调用高余维 cycle 的实现忠实性。
