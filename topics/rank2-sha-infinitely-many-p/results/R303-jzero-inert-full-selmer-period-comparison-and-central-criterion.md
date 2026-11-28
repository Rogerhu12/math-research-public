# R303 — 新 j=0 的惰性完整 Selmer 桥、实际周期比较与中央导数

日期：2026-11-13。**状态：以下整模比较、全部同支中央权、准确消失阶及完整初级有限性判据均已证明。主目标仍未完成：尚须在无穷多个素数上证明原中央导数非零。**

固定本课题已经证明精确秩二的
\[
 E^{(0)}:y^2=x^3+17,
 \qquad K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
 \omega=(-1+\delta)/2.
\]
本篇只使用这一固定曲线。参考是 R302 已完整识别的
\(E_1:y^2=x^3+1\)，其原 theta 来源为 \(B=x\sigma^2\)。
记
\[
 p\ge11,\qquad p\equiv5\pmod6,\qquad p\ne17,\qquad
 d=p+1,\quad \Phi=K_p=\mathbf Q_{p^2},\quad
 \mathcal O=\mathbf Z_{p^2},\quad v_p(p)=1.                 \tag{1}
\]
以下没有额外的未知有限例外集。

## 1. 结论与原来源

在 \(E_1\) 的微分 \(dz=dx/(2y)\) 下置
\[
 A(z)=\sigma(z)^{34}
 \left(x^{14}-\frac{53}{7}x^{11}-\frac{12}{7}x^8
                   -\frac{80}{7}x^5-\frac{128}{7}x^2\right)
       =\sum\alpha_m z^m,
 \qquad B(z)=x(z)\sigma(z)^2=\sum\beta_m z^m.               \tag{2}
\]
因此 \(\alpha_6=1,\ \beta_0=1\)，两者仅有六的倍数次幂。
目标曲线的真正来源为 R297 的 \(S=\sum s_mz^m\)，并且
\[
 s_m=17^{m/6-1}\alpha_m\qquad(6\mid m).                   \tag{3}
\]
在当前素数处，这只是明确的单位缩放。

令 \(c=[z^d]\log(\sigma(z)/z)\)，并按 R301 定义
\[
 \begin{split}
 G&=A\exp(-34cz^d),& a_h&=[z^{dh}]G\,(34c)^{-h},\\
 G_0&=B\exp(-2cz^d),&a_h^0&=[z^{dh}]G_0\,(2c)^{-h},\\
 J_p(u)&=\sum_{h\ge0}a_h(u)_h,&
 J_{0,p}(u)&=\sum_{h\ge0}a_h^0(u)_h .
 \end{split}                                             \tag{4}
\]
这里 \((u)_h=u(u-1)\cdots(u-h+1)\)。R301 已证明
\[
 v_p(c)=-1,\qquad
 J_p\in pu\mathbf Z_p\langle u\rangle,\qquad
 J_{0,p}\in1+p\mathbf Z_p\langle u\rangle.                 \tag{5}
\]

**定理。** 存在来自目标曲线标准椭圆单位的非零整 Rubin 系数
\(\mathcal A_p(T)\in\mathcal O[[T]]\)，且 \(J_p\ne0\)。若
\(e=\operatorname{ord}_{u=0}J_p\)、\(j_e=[u^e]J_p\)，则
\[
 \boxed{\operatorname{ord}_{T=0}\mathcal A_p=2e,\qquad
 v_p([T^{2e}]\mathcal A_p)=2v_p(j_e)-2e.}                 \tag{6}
\]
尤其 \(e\ge1,\ v_p(j_e)\ge e\)。完整通常 Selmer 群满足
\[
 \boxed{
 2+\operatorname{corank}_{\mathbf Z_p}
       \Sha(E^{(0)}/\mathbf Q)[p^\infty]
 \le 2\operatorname{ord}_0 J_p.}                         \tag{7}
\]
所以
\[
 \boxed{J_p'(0)\ne0\quad\Longrightarrow\quad
             \Sha(E^{(0)}/\mathbf Q)[p^\infty]\text{有限}.} \tag{8}
\]
这里不主张反向等价；有限性也不等于初级群为零。

## 2. 实际整同构与共同反圆分权

取 \(\theta=17^{1/6}\)，在复嵌入选正实根。
因为 \(6\mid p+1\)，循环群 \(\mathbf F_{p^2}^{\times}\) 的六次幂
子群包含 \(\mathbf F_p^\times\)。于是 \(\theta\) 的每个当前嵌入均落在
\(\mathcal O^\times\)，且
\[
 F_\theta:E_1\longrightarrow E^{(0)},\qquad
 (X,Y)\longmapsto(\theta^2X,\theta^3Y),\qquad
 F_\theta^*\omega_{17}=\theta^{-1}\omega_1               \tag{9}
\]
是光滑整模型、形式群以及完整 CM Tate 格的同构。
两条方程在 (1) 的素数均光滑；因此没有仅用有理表示的同构来代替整格。

令 \(\Omega_j>0\) 为原实周期、\(s=(1-\omega)^{-1}\)、
\(\varpi_j=s\Omega_j\)。真实 CM 格是 \(\varpi_j\mathcal O_K\)，且
\[
 \varpi_{17}=\varpi_1/\theta.                             \tag{10}
\]
选择由 (9) 对应的原始 CM Betti 基与 Tate 基；代数同构的比较自然性
给出这种相容选择。若原先的格生成元有不同相位，只差 \(\mu_6\)，
在当前位为单位。所有张量均在秩一 CM 整格上作，不使用带阶乘分母的
对称幂投影。

记实际 Hecke 角色为 \(\psi_j\)，按算术理想采用 type \((1,0)\)。
两者的比是六次有限角色。对 \(d\mid m\)，有同一个全局反圆分角色
\[
 \chi_m=(\psi_{17}/\bar\psi_{17})^m
        =(\psi_1/\bar\psi_1)^m.                          \tag{11}
\]
在 \(p\) 的惯性上，它的 tame 指数为 \((1-p)m\)，恰在
\(p+1\mid m\) 时消失；其余有限角色因 \(6\mid m\) 消失。
故 (11) 确实是同一反圆分 \(\mathbf Z_p\)-扩张 \(K_\infty/K\)
的连续角色，而不是换了 tame 分支的值。

类数为一。局部类域论把其主单位商与范数一主单位格识别，
在反不变 Lie 格上 \(u\mapsto u/\bar u\) 是乘二。
固定生成元 \(\gamma\)，可取
\[
 T=\gamma-1,\qquad q=\kappa_{\rm ac}(\gamma)\in1+p\mathcal O,
 \quad v_p(q-1)=1,\qquad x_m=q^m-1 .
\]
于是
\[
 v_p(x_m)=1+v_p(m),\qquad v_p(x_{dk})=1+v_p(k).           \tag{12}
\]
本文约定在 \(\chi_m\) 处评价对应 \(\chi_m^{-1}\) 的表示扭转。
逆 Artin 规范同时把 \(q\) 换成 \(q^{-1}\)，只作整参数自同构，
不影响赋值或消失阶。

## 3. 原秩零类给出完整 signed 模的整基

令 \(T_j=T_pE_j\)，视为自由秩一 \(\mathcal O\)-模，并置
\[
 M_j=\varprojlim_n H^1(\Psi_n,T_j^{-1}(1)).
\]
BKO21 的局部 Rubin 定理及 BKO24 §2.2.1 的上同调表述给出完整整分解
\[
 M_j=M_j^+\oplus M_j^-,\qquad
 M_j^\pm\simeq\Lambda:=\mathcal O[[T]].                  \tag{13}
\]
这不是略去有限模后的伪同构。signed 子模用有限特征下的 dual
exponential 消失定义。(9) 与其逆均和限制、corestriction、指数映射
相容，因而
\[
 F_\theta^*:M_{17}^\pm\xrightarrow{\sim}M_1^\pm.          \tag{14}
\]

用各自 Néron 微分及原始 CM Betti 基，按 BKO24 Proposition 3.1、
Definition 3.13 取标准椭圆单位类的局部像 \(\xi_j\)。
R290 给目标根数 \(+1\)，R302 的非零中央值给参考根数 \(+1\)。
于是 \(\xi_j\in M_j^+\)。这里用到的 BKO 条件是 CM Q-curve、
当前位好约化及 \(p\nmid h_K\)；它们不要求目标导子仅支撑在三处。

R302 由完整六点 Kronecker 和证明
\[
 \frac{L(E_1,1)}{\varpi_1}=\frac{1-\omega}{6}
                                  \in\mathcal O^\times. \tag{15}
\]
BKO24 Corollary 4.11(i) 的证明明确给出：该值为单位时，
标准 Rubin 函数属于 \(\Lambda^\times\)。因此
\(M_1^+=\Lambda\xi_1\)，并有唯一的整系数
\[
 \boxed{F_\theta^*\xi_{17}=\mathcal A_p(T)\xi_1,\qquad
                  \mathcal A_p\in\Lambda.}             \tag{16}
\]
BKO21 Theorem 6.1 的 torsion/特征理想结论给 \(\mathcal A_p\ne0\)。
改用任一其他原始 signed 基只乘 \(\Lambda^\times\)；
这一步实际支付了整周期，未任意指定一个未知局部周期为单位。

## 4. 同一个椭圆单位类的混合权比较

对 \(m>0,\ d\mid m\)，置
\[
 \mathscr E_{j,m}
  =\frac{(2\pi/\sqrt3)^mL(\psi_j^{2m+1},m+1)}
             {m!\varpi_j^{2m+1}}.                       \tag{17}
\]
若参考值非零，则准确的相对赋值式为
\[
 \boxed{
 v_p\mathcal A_p(x_m)
      =v_p\mathscr E_{17,m}-v_p\mathscr E_{1,m}.}          \tag{18}
\]
零的赋值约定为 \(+\infty\)。以下证明保留混合型特化及所有可能非单位因子。

### 4.1 两条特化路径确实给同一个类

实际 primitive 导子是
\(\mathfrak f_1=(2\delta)\)、\(\mathfrak f_{17}=(34\delta)\)。
对每条曲线从其完整射线类塔
\(K(p^\infty\mathfrak f_j)\) 的同一个标准椭圆单位系统
\(\mathbf u_j\) 出发。可用一个整辅助单位系统表示它，再在最终处
除辅助 Euler 算子；无需在整个二变量群环任意求逆。

具体选惰性辅助素数
\(\ell\equiv1\pmod p,\ \ell\nmid6\cdot17p\)。
Dirichlet 定理给这种 \(\ell\)；\((\ell)\) 在反圆分塔作用平凡，
而两曲线均有 \(\psi_j((\ell))=-\ell\)。
辅助算子在下面两条目标路径中的值相同，为
\(\ell^2+\ell\equiv2\pmod p\)。
所以所需的最后除法是实际整单位除法。

更正（2026-11-28，R1067 §100）：本处原写 \(\ell^2+\ell^{-1}\)。
按本文明确的目标角色 (19)，Kato 原 \(\Lambda^\#(1)\) 的特化
\([g]\mapsto\chi_{\rm cyc}(g)/\rho_{j,m}(g)\) 在惰性 \((\ell)\)
准确为 \(-\ell\)，故平滑因子是 \(\ell^2+\ell\)；
亦见 Kato (15.9.1–2)。旧值的精确写法不对，两值均模 \(p\) 为二，
因此此前只使用的单位性和相对赋值式不变；这里不是更换原对象。

令 \(b_j\) 表示 Kato §15.8 中与 \(T_j^{-1}\) 对应的 CM
Betti/étale 基，\(\zeta\) 表示同一个 cyclotomic Tate 基。
两条路径的最终表示都是
\[
 T_j^{-(2m+1)}(1+m),\qquad
 \rho_{j,m}=\psi_j^{-(2m+1)}\chi_{\rm cyc}^{1+m}.          \tag{19}
\]
第一条先构成 \(T_j^{-1}(1)\) 的类，再在反圆分角色处特化。
因为 \(\chi_m^{-1}=\psi_j^{-2m}\chi_{\rm cyc}^{m}\)，其向量为
\(\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}\)。

第二条先乘
\(b_j^{\otimes(2m+1)}\otimes\zeta^{-1}\)，投到高权 CM 新形式的
cyclotomic Iwasawa 类。Kato (15.16.1) 将此类识别为对应的
Beilinson–Kato 类。其 Theorem 12.5(1) 取
\[
 k=2m+2,\qquad r_{\rm crit}=m+1
\]
再乘 \(\zeta^{k-r_{\rm crit}}=\zeta^{m+1}\)，仍得到上述同一个向量。

这两条复合都是对同一完整射线类群环上同调类按 (19) 作基变换。
norm、tensor twist、特化及局部化因而交换，随后施同一个 dual
exponential 也交换。故使用的高权值确实是 (16) 的反圆分评价。
单独有限阶角色的插值式并不足以证明本步。

Kato §15.8 的 CM period map 是椭圆曲线自身 period map 在 CM 域
上的张量。Lemma 15.11 的两个定义性图分别规范 étale 与 Betti
比较；已证明的 (15.16.1) 再与 Theorem 12.5(1) 给出共同复 Tate 因子
\((2\pi i)^{k-r_{\rm crit}-1}=(2\pi i)^m\)。
把两个图拉回同一 CM 线时，任意的中间 \(S(\psi)\to S(f)\) 缩放消去。
本论证不使用 Kato 在 §15.11 末尾明确未证明的高权 Betti/étale
motivic 相容性，也不把任意非零 de Rham 向量当作整基。

### 4.2 实际整格与非单位因子

在 (9) 的相容基下，两个 CM tensor 格与 Tate twist 完全对应；
de Rham 微分比较为
\[
 F_\theta^*(\omega_{17}^{\otimes(2m+1)})
                  =\theta^{-(2m+1)}\omega_1^{\otimes(2m+1)}, \tag{20}
\]
其因子是当前位单位。规范的 canonical CM-pair 与原模型间
只产生导子整数幂；导子只含 \(2,3,17\)，也是单位。
若经六次扭转域或完整有限导子域下降，所需有限度数分别整除六、
二百八十八，当前 \(p\) 均不整除。直接在 CM 秩一线作张量
没有对称幂阶乘分母。

Kato 的共同临界 Tate 因子与 (17) 的比包含
\[
 (i\sqrt3)^m\,m!.
\]
其中 \(m!\) 在 \(m\ge p\) 时可能不是单位，但两曲线的因子
完全相同，必须在取比后抵消。任何相同的 Gamma、
Tate 或 dual-exponential 规范因子也作同样的准确抵消。

还须保留 \(p\) Euler 因子。惰性好约化给
\(\psi_j((p))=-p\)，而 \(N(p)=p^2\)，故在此中央点去掉 \(p\) 的因子均为
\[
 1-\frac{(-p)^{2m+1}}{(p^2)^{m+1}}=1+\frac1p.            \tag{21}
\]
它的赋值为 \(-1\)，并非单位；但两个 (21) 完全相同，所以仍抵消。
各自的有限特征在 \(6\mid m\) 时不变，导子仍为各自的
primitive 导子。特别地，参考始终保留它在十七处的原 Euler 因子，
未为了共同层数而人为删掉该因子。

对 (16) 施相同特化与 dual exponential，§4.1 给上述临界值；
(20)、全部下降及导子比较只乘已确定的单位；唯一可能非单位的
共同因子如上抵消。这证明 (18)。参考值非零确保取比合法。
本证明只需要逐权的准确赋值，不假设余下单位因子随权解析。

## 5. 全权平方给准确阶数，保留两侧全部阶乘

R298 与 R302 的真正全权公式分别为
\[
 \mathscr E_{17,m}
       =\kappa_0(1-\omega)34^{-m}s_m^2,\qquad
 \mathscr E_{1,m}=\frac{1-\omega}{6}2^{-m}\beta_m^2,
 \qquad \kappa_0=48940416=2^7\,3^3\,7^2\,17^2.            \tag{22}
\]
在 (1) 下，其固定常数及 \(17\) 幂都是单位。
这里每条曲线用自己的真实 CM 周期；若统一到 \(E^{(0)}\) 的周期，
R302 §7 的额外 \(\theta\) 必须同留，它仍为当前位单位。

R301 对每个整数 \(k\ge0\) 已给准确的有限卷积
\[
 J_p(k)=k!(34c)^{-k}\alpha_{dk},\qquad
 J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.                        \tag{23}
\]
由于 \(J_{0,p}(k)\) 为单位，所有参考系数均非零，且
\[
 v_p(\beta_{dk})=-k-v_p(k!).                             \tag{24}
\]
所以 (18) 可用于每个正整数 \(k\)。代入 (3)、(22)–(24) 得
\[
 \boxed{v_p\mathcal A_p(x_{dk})=2v_p J_p(k).}             \tag{25}
\]
这一步保留了两个 \(k!\) 及两边赋值为 \(-1\) 的指数常数；
没有把它们预先当成单位。

若 \(J_p\) 恒为零，(25) 迫非零 \(\mathcal A_p\) 在
\(x_{dp^n}\to0\) 处有无穷零，矛盾。因此 \(J_p\ne0\)。
令 \(r=\operatorname{ord}_0\mathcal A_p\)、
\(A_r=[T^r]\mathcal A_p\ne0\)、\(e=\operatorname{ord}_0J_p\)。
对充分大 \(n\)，首非零项支配两侧：
\[
 v_p(A_r)+r(n+1)=2v_p(j_e)+2en .
\]
比较 \(n\) 的系数与常数项，得
\[
 r=2e,\qquad v_p(A_{2e})=2v_p(j_e)-2e,
\]
即 (6)。整性给右侧非负，从而 \(v_p(j_e)\ge e\)。

## 6. 通常 Selmer 群与完整 Sha 方向

BKO21 Theorems 6.1–6.2 对这条根数 \(+\) 的 CM 曲线给
\[
 \operatorname{corank}_{\mathcal O}
       \operatorname{Sel}_{p^\infty}(E^{(0)}/K)
                  \le\operatorname{ord}_0\mathcal A_p.  \tag{26}
\]
平凡角色属于 \(\Xi^+\)，所以这里没有相反符号时的加一项。
该定理在基层比较的是完整通常 Selmer 群；没有用 Mordell–Weil
子空间代替 Selmer 群，也没有先假设高度非退化。

\(E^{(0)}\) 的 \(-3\) 二次扭转是 \(y^2=x^3-459\)，R294 已给
它与目标曲线的有理三同源。当前 \(p\ne2,3\)，限制、
corestriction、二次特征投影和三同源均在 \(p^\infty\)-Selmer
余秩上给同构。因此
\[
 \begin{split}
 \operatorname{corank}_{\mathbf Z_p}
       \operatorname{Sel}_{p^\infty}(E^{(0)}/K)
 &=2\operatorname{corank}_{\mathbf Z_p}
       \operatorname{Sel}_{p^\infty}(E^{(0)}/\mathbf Q),\\
 \operatorname{corank}_{\mathcal O}
       \operatorname{Sel}_{p^\infty}(E^{(0)}/K)
 &=2+\operatorname{corank}_{\mathbf Z_p}
                         \Sha(E^{(0)}/\mathbf Q)[p^\infty].
 \end{split}                                             \tag{27}
\]
第二式使用 R294 的精确秩二及完整 Kummer 正合列。
结合 (6)、(26) 得 (7)。

若 \(J_p'(0)\ne0\)，则 \(e=1\)，(7) 迫 Sha 初级余秩为零。
通常 Selmer 群余有限生成，因而其 Sha 商余有限生成；
余秩零的 \(p\)-primary 群遂有限。这证明 (8)，不需要另加
\(p\)-parity 或 regulator 假设。

## 7. 原首权及完整有限证书

写 \(p+1=6s\)。R301 已统一证明
\[
 pc\equiv-(-1)^s4^{-s}\binom{2s}{s}\in\mathbf F_p^\times,
 \qquad
 \frac{J_p'(0)}p\equiv\frac{\alpha_{p+1}}{34pc}\pmod p.   \tag{28}
\]
所以
\[
 \boxed{s_{p+1}\in\mathbf Z_p^\times
 \ \Longleftrightarrow\ J_p'(0)/p\in\mathbf Z_p^\times
 \ \Longrightarrow\ \Sha(E^{(0)}/\mathbf Q)[p^\infty]
                       \text{有限}.}                   \tag{29}
\]
若该单位条件成立，(6) 还给
\(\mathcal A_p=T^2U_p,\ U_p\in\Lambda^\times\)。
这里仍不从特征理想主项单独声称基层 Sha 初级群为零。

首层失效时，完整导数仍可非零。具体令
\[
 L_{p,H}=\sum_{h=1}^H(-1)^{h-1}(h-1)!\,a_h,\qquad
 M_{p,H}
 =\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).
\]
R301 的真实余项圆盘给
\(v_p(J_p'(0)-L_{p,H})\ge M_{p,H}\)，故
\[
 \boxed{J_p'(0)\ne0
 \quad\Longleftrightarrow\quad
 \exists H\ge1:\ v_p(L_{p,H})<M_{p,H}.}                  \tag{30}
\]
(30) 与 (8) 是保完整深度的有限初级有限性证书。
没有把首层失败当成完整导数消失。

例如原系数
\(s_{12}=-988\cdot17/105\) 是十一进单位，
所以本篇给 \(\Sha(E^{(0)}/\mathbf Q)[11^\infty]\) 有限。
这是一个准确单素数应用；无穷性仍需证明无穷多 \(p\) 满足 (30)，
或其中较强的 (29)。R295 已付普通素数的完整中央桥，
本篇支付了同一新曲线的惰性桥；两侧均尚未给跨素数非零。

## 8. 证明依赖与一手来源

本篇是统一的整模及解析比较证明，没有以有限素数扫描代替任一全称步骤。
所有原来源、周期常数及解析界分别由以下已完成证明支付：

- [R294：目标的完整有理三同源下降](R294-jzero-exact-rank-two-by-rational-three-isogeny.md)。
- [R298：原全权平方的准确常数](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)。
- [R301：原惰性解析半因子与全部尾界](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)。
- [R302：原 degree 2 参考与准确全权平方](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)。
- [R295：同一曲线的普通完整中央桥](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)。

所用已发表输入及本篇使用位置：

1. A. Burungale, S. Kobayashi, K. Ota, *Rubin's conjecture on local
   units in the anticyclotomic tower at inert primes*, Annals of
   Mathematics **194** (2021), 943–966，Theorems 2.1、6.1、6.2：
   [原文](https://par.nsf.gov/servlets/purl/10336626)，
   [出版页](https://doi.org/10.4007/annals.2021.194.3.8)。
   用于 §3 的完整整分解、非零及 §6 的通常 Selmer 控制。
2. 同三位作者，*p-adic L-functions and rational points on CM elliptic
   curves at inert primes*, JIMJ **23** (2024), 1417–1460，
   §2.2.1、§3.1.1、Proposition 3.1、Definition 3.13、
   Corollary 4.11(i) 的证明：
   [出版全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)，
   [DOI](https://doi.org/10.1017/S147474802300021X)。
   用于实际类、其符号及参考类为整基。
3. K. Kato, *p-adic Hodge theory and values of zeta functions of modular
   forms*, Astérisque **295** (2004), 117–290，
   Theorem 12.5(1)、§15.8、Proposition 15.9、Lemma 15.11、
   (15.16.1)：
   [原文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。
   §4 使用实际同类特化及两张定义性 period 图；不添加其未证明的
   高权 motivic 相容性。

