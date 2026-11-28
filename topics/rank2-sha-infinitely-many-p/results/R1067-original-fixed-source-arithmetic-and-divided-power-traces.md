# R1067（续）：固定原源的素数指标与完整除幂迹

本卷接 [§§98–111](R1067-original-global-derived-classes-and-exact-tate-readers.md)，保持同一原证明编号、固定曲线和完整Tate源。前卷接近100KB，以下按自然论证段续写；不保存可重算数据。主目标尚未完成。

## 112. 原两变量类在有限驯点的三次整除与固定有理序列的素数指标

**已证明。** 沿§§104–105，在物理曲线$E=E_{17}:y^2=x^3+17$上取同一个$M\in\mathbf Q(E)^\times$。记$\mathfrak f=34\delta$、$\mathcal O=\mathbf Z_{p^2}$、$\Phi=\mathbf Q_{p^2}$、$q=p^2$、$b=q-1$。本节取任意$p>211$在$K$惰性，不要求$(17/p)=1$。$\omega:\mathcal O^\times\to\mu_b$为Teichmüller映射，以$\omega_K$区别三次单位根；$\rho$是原CM Tate角色，$\langle x\rangle=x/\omega(x)$。先假设通常全$\Sha(E/\mathbf Q)[p^\infty]$无限。

### 112.1 从系数截断到真实有限驯特化

$\Lambda_2=\mathcal O[[\Gamma_+\times\Gamma_-]]$，$I$为增广理想，$\mathbb W$为§105的普遍两变量系数，$\boldsymbol Z$为原$c=103$平滑的全域Robert类。(BU2)与
$$
 0\longrightarrow I^3\mathbb W\longrightarrow\mathbb W
       \longrightarrow\mathbb W/I^3\mathbb W\longrightarrow0
$$
的长正合列给$\boldsymbol Z$的一个真实$H^1(K,I^3\mathbb W)$提升。按(BU3)的逆群元约定，取
$$
 [g_w]\longmapsto\langle w\rangle^{-1}.
$$
于是$w^{-1}[g_w]^{-1}\mapsto\omega(w)^{-1}$，目标系数为
$W_\tau=\mathcal O(1)\omega(\rho)^{-1}$。$I$每个生成元取值在$p\mathcal O$；限制于$I^3\mathbb W$的系数映射通过$p^3W_\tau$。上同调的自然性因此给实际特化属于$p^3H^1(K,W_\tau)$。这里没有使用或声称$\boldsymbol Z\in I^3H^1(K,\mathbb W)$。

令$L_j=K(\mathfrak f p^j)$、$B_1=\operatorname{Gal}(L_1/K)$、
$$
 u_j=({}_{103}\theta)^{-1}
          \bigl(\varpi_{17}/(\mathfrak f p^j)\bigr),\qquad
 \chi=\omega(\rho).
$$
在$L_1$取原Tate基，有限特化的限制恰为
$\sum_{d\in B_1}\chi(d)^{-1}[d]u_1=|B_1|e_\chi[u_1]$。
在任一上层，主单位权被该特化完全消去，整个相对野迹是
$N_{L_j/L_1}u_j=u_1$，没有$[L_j:L_1]$倍。
$\chi([(t,a)])^{-1}=\varepsilon(t)\omega(a)^{-1}$，所以仍保留全部$\mathfrak f$角色；$|B_1|$为单位。

同步特化(BT5)，整个平滑算子$c^2-c[g_c]$变成
$$
 c^2-\omega(c)\equiv103^2-103\not\equiv0\pmod p,
$$
$\varepsilon(p)(1+\omega_K)/6$也为单位。记
$P_1=[\mathfrak f^{-1}]\varpi_{17}/p$，逆取模$p$，遂有
$$
 \begin{aligned}
 e_\chi[u_1]&\in p^3
    \bigl((L_1^\times)^\wedge_p\otimes_{\mathbf Z_p}\mathcal O\bigr),\\
 W_M:=\sum_{a\in\mathbf F_q^\times}
      \omega(a)^{-1}[M([a]P_1)]
    &\in p^3
    \bigl((L_1^\times)^\wedge_p\otimes_{\mathbf Z_p}\mathcal O\bigr).
 \end{aligned}                                                \tag{CB1}
$$
$[a]P_1$只依赖$a\bmod p$；外部系数始终是真Teichmüller权，特别在模$p^3$时不能换成任意整提升。这是原单位的Kummer张量；在$p$位各点值为单位，故其$p^3$原像也可取在当地单位张量，因离散赋值商无挠。完整的Kummer等式
$H^1(L_1,\mu_{p^3})=L_1^\times/(L_1^\times)^{p^3}$
不要求$\mu_{p^3}\subset L_1$。

### 112.2 物理模型上的严格坐标与固定有理数列

取实际不变微分$\eta=dx/(2y)$、$z=\int_O^P\eta$，以$P_E(z)$表示形式逆。定义与$p$无关的有理数
$$
 A(z)=\log M(P_E(z))=\sum_{n\ge1}m_nz^n\in\mathbf Q[[z]].
                                                               \tag{CB2}
$$
(BT1)给$M(O)=1$、$M(-P)=M(P)^{-1}$，故$A$奇。还有$m_1=0$。确切地，§109已由原102挠除子函数比较证明
$d\log M=-\sum_tI_t\kappa_{T_t}$，无额外全纯差；
$I_t=-\omega_K\varepsilon(t)-\bar\omega_K\overline{\varepsilon(t)}$。
常项$-\sum_tI_tX(T_t)$的$\varepsilon$方向由同一个原$L(E_{17},1)=0$的Kronecker–Hecke分布消失，另一方向由$\mu_6$非平凡权消去。物理周期缩放仅乘共同非零标量。因此$M(P_E(z))=1+O(z^2)$。

以下直接在$E/\mathbf Z_p$构造严格坐标，不经六次扭转。取$t=-x/y$，有$dz/dt(0)=1$。因为$p\equiv2\bmod3$，立方在$\mathbf F_p$为置换，二次特征和为零，所以$a_p=0$；特殊纤维$\operatorname{Frob}_p^2=[-p]$。因此
$$
 f_E(t)=[-p]_E(t),\qquad f_E'(0)=-p,\qquad f_E(t)\equiv t^q\pmod p.
$$
$f(s)=-ps+s^q$与$f_E$是同一$\Phi$的LT级数。有唯一导数一的
$u(s)\in\mathcal O[[s]]$满足$u\circ f=f_E\circ u$。
也可直接逐次证明整性：已有整截断的误差模$p$为零，因为两边分别约化为
$\bar u(s^q)$、$\bar u(s)^q$，系数在$\mathbf F_q$；
加入第$n$项的修正系数乘$(-p)^n-(-p)$，其$p$进赋值恰一，
故可唯一消除误差而保持整。两边系数均在$\mathbf Z_p$，
非分歧Frobenius保持导数一，唯一性再给$u\in\mathbf Z_p[[s]]$。

物理形式群与该LT模律一致，因为其导数一对数在$f_E$下乘$-p$，
此对数唯一；物理CM作用亦由其导数对齐。写
$$
 \ell(s)=z(u(s)),\qquad
 \ell'(0)=1,\qquad \ell(f(s))=-p\ell(s).
$$
则$\ell(s)=s+O(s^q)$，$\omega(a)$作用为$s\mapsto\omega(a)s$。
在固定$p$位全部$p$挠点都落在形式群，$P_1$的真实非零坐标$s_1$满足$s_1^b=p$。固定$\mathfrak f$层只增加未分歧扩张；$L_{1,v}/\Phi$的绝对分歧指数$e\le b$，也直接由第一射线的惰性子群得到。

$M$的零极为素于$p$阶的固定$\mathfrak f$挠点，约化后都与$O$不同；归一$M(O)=1$使$M(u(s))\in1+s\mathbf Z_p[[s]]$，对数导数整。置
$$
 d_n=[s^n]A(\ell(s)).
$$
于是$nd_n\in\mathbf Z_p$，而$m_1=0$及$\ell=s+O(s^q)$给
$d_1=0$、$d_q=m_q$。这些识别在同一个物理模型上完成。

### 112.3 真实局部对数的精度与原Euler因子

约定$v_p(p)=1$。当地任意单位除去剩余Teichmüller单位后为$1+x$，
$v_p(x)\ge1/b$。逐项估计给
$$
 v_p(\log(1+x))
   \ge\min_{r\ge0}\{p^r/b-r\}=1/b-1.
$$
对每个$r=v_p(n)$有$n\ge p^r$；下界在$r=2$达到，此后严格递增。
因此(CB1)给$v_p(\log W_M)\ge2+1/b$，不能把普通单位对数
未经证明地当成$p\mathcal O_{L_{1,v}}$。

直接将完整$\mathbf F_q^\times$迹代入
$\log M(u(\omega(a)s_1))$，由$s_1^b=p$得准确收敛式
$$
 \frac{\log W_M}{b\,s_1}
       =\sum_{j\ge0}d_{1+jb}p^j\in p^2\mathbf Z_p.              \tag{CB3}
$$
左边对Kummer张量取固定复合$\log\otimes\mathcal O\to L_{1,v}$。
右边$j=0$为零，$j=1$为$p\,m_q$。$2\le j\le4$时，
$1+jb\equiv1-j\ne0\bmod p$；$j\ge5$时
$1+jb<p^{j-1}$，由$nd_n$整得全部尾项属于$p^2\mathbf Z_p$。
故
$$
 \boxed{\quad
 \Sha(E_{17}/\mathbf Q)[p^\infty]\text{无限}
        \ \Longrightarrow\ m_{p^2}\in p\mathbf Z_p .
 \quad}                                                       \tag{CB4}
$$

令$U(z)=M(P_E(z))$。$U(\ell(s))=M(u(s))$整，
而$\ell^{-1}(z)=z+O(z^q)$的第$q$次可能不整校正乘$[z]U=0$，
所以$U$至$q$次的全部系数都在$\mathbf Z_p$。逐阶消首项唯一构造
$$
 U(z)\equiv\prod_{n=1}^{q}(1-e_nz^n)\pmod{z^{q+1}},
 \qquad e_n\in\mathbf Z_p,\quad e_1=0.
$$
取形式对数并在素数和素数平方处比较，准确得到
$$
 \boxed{\qquad
 m_p=-e_p,\qquad
 m_{p^2}=\frac{m_p^p}{p}-e_{p^2}.
 \qquad}                                                      \tag{CB5}
$$
若$m_p$为单位，后一式赋值为$-1$，与(CB4)矛盾。
所以坏情形同时有$m_p,m_{p^2},e_{p^2}\in p\mathbf Z_p$。
反之，任一$m_p\notin p\mathbf Z_p$，或任一$v_p(m_{p^2})\le0$，
均已足够推出此$p$的通常全$\Sha[p^\infty]$有限。

### 112.4 同一张量的另一嵌入给联合的一位条件

仅在(CB1)的外部$\mathcal O$系数施Frobenius，
把权换成$\omega(a)^{-p}$，不移动$P_1$或$\mathfrak f$点。
除以$b s_1^p$后的收敛迹为
$$
 \sum_{j\ge0}p^jd_{p+jb}\in\mathbf Q_p.
$$
(CB1)及上述对数界给其赋值至少
$2-(p-1)/b$，而该值在$\mathbf Q_p$，故实际至少二。
各$j\ge2$项同样落在$p^2$：$2\le j\le4$时分母模$p$非零，
其余用$p+jb<p^{j-1}$。若
$$
 \ell_q=[s^q]\ell=\frac1{-p-(-p)^q},
$$
则Teichmüller权使下一次LT对数校正至少为$2q-1$，所以
$$
 d_{q+p-1}=m_{q+p-1}+p\ell_qm_p.
$$
已知$m_p\in p\mathbf Z_p$，且$p\ell_q$为单位，
故最后一项属于$p\mathbf Z_p$。由$d_p=m_p$得到另一条真实联合必要条件
$$
 \boxed{\qquad
  m_p/p+m_{p^2+p-1}\equiv0\pmod p .
 \qquad}                                                      \tag{CB6}
$$

本节得到同一个固定有理函数、同一个有理系数序列的素数指标判据。
它保留真实全域源、两个系数嵌入、原Tate方向与分歧精度。
尚须证明在无限多个惰性素数满足相应的不整除；复数意义下的非零、
逐个有限素数验证和一般性的“应当不消失”都不能替代这一剩余步骤。

### 112.5 当地自由模与三个完整Coates–Wiles权的余秩界

本小节加强(CB4)–(CB6)，仍使用同一个$M$、$m_n$与所有$p>211$惰性素数。置
$
 t_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E_{17}/\mathbf Q)[p^\infty],
 \qquad s=2+t_p,\qquad h=s-1.
$
则无条件有
$
 \boxed{\quad
 t_p\le
 \min\left\{v_p(m_p),\ 
            v_p(m_{p^2+p-1}),\ 
            1+v_p(m_{p^2})\right\}.
 \quad}                                                       \tag{CB7}
$
零值的赋值按$+\infty$理解。由§102的奇偶性，$t_p$是非负偶数，
所以$m_p$或$m_{p^2+p-1}$中任一项的赋值至多一，
或$m_{p^2}$的赋值至多零，都足以推出通常全$\Sha[p^\infty]$有限。
特别全Sha无限时，前两项必须被$p^2$整除。

#### 当地才可加强成理想整除

(BU1)给原全域类在$I^h$系数截断中的像为零。
该整截断的每个模$p$分次仍有非平凡驯标量$-1$，
故$H^0=0$，乘$p$长正合列给$H^1$无$p$挠。
因此(BU1)的有理消失对任意这个有限$h$都提升为整消失。

在唯一$p$位$\Phi$，考虑同一个普遍系数及其外部$\mathcal O$共轭。
两者的残余驯角色分别为$\tau^p,\tau$，
Tate对偶分别有另一非平凡角色。因此当地残余$H^0,H^2$都为零；
局部Euler特征给$H^1$在$\mathbf F_q$上的维数二。

这里可以直接证明所需的自由性及全部系数基变换。
记$\mathfrak m=(p,I)$。对任何有限长$\Lambda_2$系数商$A$，
用$\mathfrak m$分次逐次扩张，$H^0,H^2$始终为零。
每一步的$H^1$短正合列，其核为
$H^1(\Phi,\bar W)\otimes_{\mathbf F_q}\operatorname{gr}_{\mathfrak m}A$。
在$A=\Lambda_2/\mathfrak m^r$逐级相容提升残余$H^1$的一组二元基；
这些提升乘以$\operatorname{gr}_{\mathfrak m}A$恰好生成上述核。
归纳得到$A^2\to H^1(\Phi,\mathbb W\otimes A)$满射。
两边长度均为$2\operatorname{length}A$，故为同构。
取逆极限，再对$A=\Lambda_2/(p^k,I^h)$取极限，得到
$
 H^1_{\rm loc}\simeq\Lambda_2^2,\qquad
 H^1_{\rm loc}/I^hH^1_{\rm loc}
   \simeq H^1\bigl(\Phi,\mathbb W/I^h\mathbb W\bigr).
$
过渡映射均满，因而这里无额外$\varprojlim^1$项。
所以原系数截断像零在当地准确加强为
$
                     \operatorname{loc}\boldsymbol Z
                          \in I^hH^1_{\rm loc}.                \tag{CB8}
$
这只用于当地自由模，未把非主$I$的全域上同调误作自由模。

#### 原源严格回到$\Phi$的LT范数系统

令
$
 Q_j=(-1)^j[\mathfrak f^{-1}]\varpi_{17}/p^j,\qquad
 \Phi_j=\Phi(E[p^j]).
$
$\psi_{17}((p))=-p$给$\varepsilon(p)=-1$，
$[-p]Q_{j+1}=Q_j$。
由$M(-P)=M(P)^{-1}$，(BT5)中的$\varepsilon(p)^j$
正好把原$M(P_j)$变为$M(Q_j)$的加法Kummer类。
(BT6)的真实$[-p]$函数范数因此使
$(M(Q_j))_j$严格Norm相容，Coleman函数就是
$M(u(s))\in\mathbf Z_p[[s]]^\times$。

不在额外未分歧层上直接套用错误的LT底域。
设$F_{j,v}$为原$K(\mathfrak f p^j)$的一个完成。
原CM角色给$\Phi_j\subset F_{j,v}$；
$
 |(\mathcal O_K/\mathfrak f)^\times|
      =(4-1)(289-1)(3-1)=1728
$
及对角六次单位商给
$[F_{j,v}:\Phi_j]\mid288$，为$p$单位。
(BT5)在$F_{j,v}$是实际限制的等式，而其中全部
$M([w]Q_j)$本已在$\Phi_j$。
对两边同时corestrict仅乘相同的这个单位次数；
$\operatorname{cor}\operatorname{res}=[F_{j,v}:\Phi_j]$
因此把等式准确降到$\Phi_j$，不产生额外Frobenius相位或局部迹常数。

外部$\mathcal O$共轭后，完整源在有限Shapiro识别中写为
$
 \Theta(u)=\sum_w\bar w^{-1}[g_w]^{-1}[w]u,\qquad
             u=(M(Q_j))_j.
$
主单位$d$的真实重标给
$\Theta([d]u)=\bar d[g_d]\Theta(u)$。
所以$\Lambda_2$的$[g_d]$在未扭的范数单位模上作用为
$\bar d^{-1}[d]$；驯分量是$e_{\tau^p}$。
取群环$[1]$系数只产生$|\Delta|e_{\tau^p}$，
$|\Delta|=p^2-1$是单位，绝不除野群阶。
原常数$(1+\bar\omega_K)/6$及整个
$103^2-103[g_{103}]$仍保留。
原嵌入同理给$e_\tau$及$d^{-1}[d]$。

非平凡驯分量消去离散赋值商，因此这里完整当地模中的所有
$I^h$原像都属于范数单位张量。
所用Coleman定理只在真正的$\Phi$、原$[-p]$-LT塔上应用：
P. Schneider、O. Venjakob，
*Coates–Wiles homomorphisms and Iwasawa cohomology for Lubin–Tate extensions*
(2015)，Theorem 2.2、Remark 2.3及§8；
[原文](https://arxiv.org/pdf/1511.04922)。
其Theorem 2.2的Laurent级数在单位分量上为整幂级数；
本节采用正次对数系数，所以常数对数的选择不影响读取。

#### 三个整读者和准确的Tate权

对任意原范数单位的Coleman函数$F(s)\in\mathcal O[[s]]^\times$，
写$d_j=[s^j]\log F(s)$；则$jd_j$整。
物理对数的逆为
$
 \ell^{-1}(z)=z-\ell_qz^q+O(z^{2q-1}),\qquad
              \ell_q=(p^q-p)^{-1}.
$
以下三个在整个单位格上的连续加法读者均整：
$
 \begin{aligned}
 \mathcal W_p(F)&=p[z^p]\log F(\ell^{-1}(z))=p\,d_p,\\
 \mathcal W_q(F)&=q[z^q]\log F(\ell^{-1}(z))
                                      =q(d_q-\ell_qd_1),\\
 \mathcal W_n(F)&=pn[z^n]\log F(\ell^{-1}(z))
                       =pn(d_n-p\ell_qd_p),\qquad n=q+p-1.
 \end{aligned}
$
第一式由$p<q$；第二式用$q\ell_q\in p\mathcal O$；
第三式用$n$为$p$单位、$p\ell_q$为单位及$pd_p$整。
它们向$\mathcal O$张量连续延拓。

未扭的$[d]$对第$r$个对数系数作用为$d^r$，
因为$\ell([d]s)=d\ell(s)$。
所以$p,n$两权在实际共轭Tate分量上的$\Gamma$特征为
$d^p/\bar d$、$d^n/\bar d$；
$q$权在原分量上为$d^q/d$。
每个$[g_d]-1$的读者特征均属于$p\mathcal O$。
这里$p,n\equiv p\bmod(q-1)$而$q\equiv1\bmod(q-1)$，
正好与上述两个真实驯幂等一致。

原平滑算子在第$r$权取值$103^2-103^r$，
模$p$为$103^2-103$，因$r=p,q,n$均$\equiv1\bmod(p-1)$，
所以仍为单位。其余固定常数和有限Shapiro归一也为单位。
(CB8)遂准确给
$
 p\,m_p\in p^h\mathcal O,\qquad
 q\,m_q\in p^h\mathcal O,\qquad
 pn\,m_n\in p^h\mathcal O.
$
全部$m_r$是原(CB2)的有理数；除去所示的$p$次幂与单位，
即得(CB7)。这项加强读取同一个完整源，既未更换曲线，
也未借有限素数测试外推无穷素数；余下仍是跨素数的实际不整除。

### 112.6 全域首齐次项的互反律再给一位整除

上述三个界可以再同时提高一位。沿用$t_p,s,h$和固定有理数列$m_n$，有
$
 \boxed{\qquad
 t_p\le
 \min\{v_p(m_p)-1,\ v_p(m_{p^2+p-1})-1,\ v_p(m_{p^2})\}.
 \qquad}                                                       \tag{CB9}
$
因$t_p$为偶数，$m_p$或$m_{p^2+p-1}$的赋值至多二，
或$m_{p^2}$的赋值至多一，均充分推出通常全$\Sha[p^\infty]$有限。
全Sha无限时，前两项必须被$p^3$整除，第三项必须被$p^2$整除。

#### 同一全域提升的首项，不能用任意当地原像替换

由(BU1)的整提升及系数短正合列，存在
$
 \widetilde{\boldsymbol Z}\in H^1(K,I^h\mathbb W)
$
映到原$\boldsymbol Z$。将它投到$I^h/I^{h+1}$，
按$U_+^aU_-^{h-a}$取系数，得到真实全域类
$\eta_a\in H^1(K,W_0)$，$0\le a\le h$。

置$P=H^1_{\rm loc}$，这是112.5已证的自由$\Lambda_2$模。
任取分解
$
 \operatorname{loc}\boldsymbol Z
     =\sum_{a=0}^h U_+^aU_-^{h-a}u_a,\qquad u_a\in P .
$
模$I^{h+1}P$后各单项式独立，系数基变换给
$
                 u_a\bmod IP=\operatorname{loc}\eta_a.          \tag{CB10}
$
也可直接用$H^0(\Phi,\mathbb W/I^h)=0$，说明首分次在相应
$H^1$长正合列中注入，从而核定这个身份。没有断言
$\boldsymbol Z\in I^hH^1(K,\mathbb W)$，也没有要求当地分解唯一。

§105的互反律适用于每个$\eta_a\otimes\Phi$：
固定非挠有理点及其$\mathcal O_K$倍在唯一$p$位的非零对数
张满对偶表示的一维Kummer线。非$p$位的有理Kummer像为零；
全局Tate互反因而使$\operatorname{loc}\eta_a$正交于这条线。
当地正交补就是$H^1_f(\Phi,W)$。

在原未共轭的范数单位模型上，$\Gamma$的作用是$d^{-1}[d]$。
第一Coates–Wiles读者
$
 \operatorname{CW}_1(F)
       =[z]\log F(\ell^{-1}(z))=F'(0)/F(0)
$
在这个扭转下的特征为$d/d=1$，所以准确通过$P/IP$。
Schneider–Venjakob原文
[Corollary 8.8](https://arxiv.org/pdf/1511.04922)，取$r=1$、
$\pi_L=-p$，给
$
 \exp^*\bigl(\operatorname{cores} u_a\bigr)
       =(1-\pi_L^{-1})\operatorname{CW}_1(u_a)\,d_1^{\rm dR}.
$
这里$d_1^{\rm dR}$为其固定非零de Rham基，勿与对数系数$d_1$混用。
由(CB10)左边为零，而$1-\pi_L^{-1}\ne0$，故
$
                         \operatorname{CW}_1(u_a)=0             \tag{CB11}
$
是精确零。此处不需要该Euler因子为整单位。

#### 在整个范数单位格上的三条ghost同余

对任意$F(s)\in\mathcal O[[s]]^\times$，令
$d_j=[s^j]\log F(s)$；常数项的对数不影响正次系数。
逐阶Euler乘积
$F(s)/F(0)=\prod_{r\ge1}(1-e_rs^r)$给
$
 p d_p\equiv d_1^p,\qquad q d_q\equiv d_1^q
                       \pmod p.                               \tag{CB12}
$
确实$p d_p=-e_1^p-pe_p$，
$q d_q=-e_1^q-pe_p^p-qe_q$，而$d_1=-e_1$。
以112.5的同三个整读者及$n=q+p-1$，由
$q\ell_q\in p\mathcal O$、$n\equiv-1$、
$p\ell_q\equiv-1\bmod p$得
$
 \mathcal W_p(F)\equiv d_1^p,\qquad
 \mathcal W_q(F)\equiv d_1^q,\qquad
 \mathcal W_n(F)\equiv-d_1^p\pmod p.                             \tag{CB13}
$
最后一式是
$pn d_n-n(p\ell_q)(pd_p)\equiv-pd_p$；
第一项为$p$倍，因为$n$为$p$单位。

这些同余对外部$\mathcal O$张量必须保留正确的半线性。
若$u=\sum_i a_i[F_i]$，则$q$读者约化为
$\sum_i\bar a_i\bar d_{1,i}^{\,q}
 =\overline{\operatorname{CW}_1(u)}$，因为剩余域为$\mathbf F_q$。
$p,n$读者用于外部系数Frobenius后的$\bar u$，
约化分别为
$
 \sum_i\bar a_i^{\,p}\bar d_{1,i}^{\,p}
       =\overline{\operatorname{CW}_1(u)}^{\,p},
 \qquad
       -\overline{\operatorname{CW}_1(u)}^{\,p}.
$
因此(CB11)使每个首项原像的三个实际读者都落在$p\mathcal O$。
用连续性将有限和推广到完整范数单位张量；未把
外部系数Frobenius误当成点或Coleman参数的变换。

每个$I$因子的三个实际特征值差仍在$p\mathcal O$。
对上面齐次次数$h$的分解应用读者，遂得到
$
 p m_p,\quad q m_q,\quad pn m_n\quad\in p^{h+1}\mathcal O .
$
原整个$103^2-103[g_{103}]$、有限Shapiro及固定常数
仍按112.5给相同的单位因子。除去左边已显示的$p$次幂，
再用$h=t_p+1$，即得(CB9)。

这个加强也澄清原搜索门：仅凭已知rank$=2$，
对本节全部惰性$p>211$已经有
$m_p,m_{p^2+p-1}\in p\mathbf Z_p$及$m_{p^2}\in\mathbf Z_p$。
因此先前“找$m_p\bmod p$非零”的充分条件实际不会出现；
后续应检验上述更高位的真实不整除。
(CB4)–(CB7)作为必要条件仍正确，但(CB9)给当前较强的有效门。
尚未由此证明存在无穷多个满足该门的素数。

### 112.7 普通双位的真实下降与同一素数指标的一致余秩界

**已证明。** 仍用(CB2)的物理曲线$E_{17}$、同一个$M$和同一个有理数列$m_n$。设$p>211$在$K$分裂，$a_p(E_{17})\ne1$。则
$
 \boxed{\qquad
 t_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E_{17}/\mathbf Q)[p^\infty]
       \le v_p(m_p)-1 .
 \qquad}                                                       \tag{CB14}
$
因此$v_p(m_p)\le2$足以推出该通常全$p$初级部分有限；若它无限，则$m_p\in p^3\mathbf Z_p$。本节不要求$p$在固定标记域或六次扭转域完全分裂。

#### 两个普通位的方向和全域首项

写$p=\mathfrak p\bar{\mathfrak p}$，取实际Hecke Frobenius
$
 \pi=\psi_{17}(\mathfrak p),\qquad
 \alpha=\bar\pi,\qquad \pi\alpha=p.
$
在$\mathfrak p$完成$\Phi=\mathbf Q_p$，$\pi$为均匀化元，$\alpha$为单位，
$\alpha\bmod p=a_p\bmod p$。由Hasse界及$p>211$，
$\alpha\equiv1\bmod p$等价于$a_p=1$，故$\alpha-1$为单位。
固定$\rho=\rho_{\mathfrak p}$。原系数在增广处为
$W_0=\rho^{-1}(1)=\rho_{\bar{\mathfrak p}}$；
它在$\mathfrak p$是Frobenius值$\alpha$的未分歧权零表示。
Tate对偶$V=\rho_{\mathfrak p}$在该位是形式群分量。
不要把$W_0$在另一位的一维有限条件误置于本位。

令$s=2+t_p$、$h=s-1$。§105及112.5已经给真实全域提升
$
 \widetilde{\boldsymbol Z}\in H^1(K,I^h\mathbb W)
$
和首齐次全域类$\eta_a\in H^1(K,W_0)$。
本位残余$H^0(W_0)=0$，因为$\alpha-1$为单位；
残余$H^2(W_0)=0$，因为对偶$V$的惯性具有满的非平凡驯角色。
局部Euler特征给残余$H^1$维数一。
对每个有限长$\Lambda_2$商重复112.5的分次提升、长度比较，
得到实际当地模及全部整系数基变换
$
 P=H^1(\Phi,\mathbb W)\simeq\Lambda_2,\qquad
 P/IP=H^1(\Phi,W_0).
$
特别$P/IP$无$p$挠。

对每个$\eta_a$，与原非挠有理点的$V$-Kummer类应用全域Tate互反。
非$p$位的有理局部上同调为零；在$\bar{\mathfrak p}$，
$V$为非平凡未分歧权零分量，其有限Kummer像为零。
在$\mathfrak p$，该点的非零形式对数张满$H^1_f(\Phi,V)$。
故$\operatorname{loc}_{\mathfrak p}\eta_a$属于其正交补
$H^1_f(\Phi,W_0)$；后者是零，因为$W_0$未分歧且$\alpha\ne1$。
这先给有理零，再由$P/IP$无$p$挠给整零。
按(CB10)的同一首分次识别，得到额外的一次真实当地理想整除
$
                 \operatorname{loc}_{\mathfrak p}\boldsymbol Z
                     \in I^{h+1}P=I^sP .                      \tag{CB15}
$
这一步只在已证自由的当地模上进行，没有将全域$H^1$误作自由模。
将另一变量投为一后，像属于真实一变量模的$T^s$。

#### 保住另一普通位的全范数，再下降到真实LT塔

§109的(BY1)先在完整双位射线层做真实范数。
以$P_j$记其原$\pi^j$形式坐标，原单位张量精确为
$
 \Theta_j\!\left(M([\alpha^j]P_j)\right)
       -\Theta_j\!\left(M([\alpha^{j-1}]P_j)\right).             \tag{CB16}
$
这里$\Theta_j$含原全部角向权$w^{-1}[g_w]^{-1}$；
公式先保留整个未分歧层，未预先删除另一普通位。
取$Q_j=[\alpha^j]P_j$，则$[\pi]Q_{j+1}=Q_j$。
实际$\varepsilon(\pi)=1$，(BT6)给
$\operatorname{Norm}_{[\pi]}M=M$，
所以$(M(Q_j))_j$是真正的$\pi$-LT范数相容系统。
以$\Theta([d]u)=d[g_d]\Theta(u)$重标(CB16)，得到完整算子
$
                (1-\alpha^{-1}[g_\alpha]^{-1})
                    \Theta_j(M(Q_j)).                        \tag{CB17}
$
其增广为$1-\alpha^{-1}$，是整群环单位。
固定辅助算子$103^2-103[g_{103}]$及原常数也始终保留。

须特别核清从全射线完成到
$\Phi_j=\Phi(E[\pi^j])$的下降。
$\Phi_j/\Phi$是完全分歧的真实LT塔。
固定$\mathfrak f$层只产生次数除$288$的未分歧扩张，
此部分可用两边同时res/corestr并消去单位次数。
但是另一支$\alpha^j$挠点可以再产生含$p$幂次数的未分歧扩张；
**整个全射线完成相对$\Phi_j$的次数不一定是$p$单位。**

这里改用精确的限制单射，不除该次数。
固定$k$并取$j\ge k$。在$\Phi_j$上，
$\rho_{\mathfrak p}\bmod p^k$平凡，而
$\chi_{\mathrm{cyc}}=\rho_{\mathfrak p}\rho_{\bar{\mathfrak p}}$，
所以$\mu_{p^k}$是未分歧模块，其算术Frobenius为$\alpha$。
于是
$
 H^1_{\mathrm{unr}}(\Phi_j,\mu_{p^k})
       =\mu_{p^k}/(\alpha-1)\mu_{p^k}=0.
$
对任意有限未分歧扩张$L/\Phi_j$，
限制核由inflation包含在这个未分歧上同调群中，故
$
 H^1(\Phi_j,\mu_{p^k})
       \longrightarrow H^1(L,\mu_{p^k})
       \quad\hbox{单射}.                                     \tag{CB18}
$
(CB16)–(CB17)的右边本已定义于$\Phi_j$。
在共同全层比较实际Shapiro等式后，(CB18)对每个$k$
把等式和相应的模$p^k$消失降回$\Phi_j$；
取相容极限恢复真实LT模中的身份。
取群环恒等系数只除驯群阶$p-1$，绝不除野群阶或未分歧$p$次数。
这同时保住(CB15)的一变量$T^s$整除。

#### 物理坐标的一项完整Coates–Wiles读者

物理参数$t=-x/y$的$[\pi]$级数模$p$为$t^p$。
真实LT级数$\pi s+s^p$与之有唯一导数一整严格同构$u(s)$。
如112.2的逐阶论证，分母$\pi^n-\pi$赋值一，
模$p$的误差由$\mathbf F_p$ Frobenius相容性保证可除；
因此$u(s)\in\mathbf Z_p[[s]]$，没有额外周期尺度。
物理不变对数为
$
 \ell(s)=z(u(s))
      =s+\ell_1s^p+O(s^{2p-1}),\qquad
             \ell_1=(\pi-\pi^p)^{-1}.
$
对任意真正范数单位的Coleman函数$F(s)\in\mathbf Z_p[[s]]^\times$，
记$\beta_n=n[s^n]\log F(s)$。全部$\beta_n$整，故
$
 \mathcal W_p(F)
   :=p[z^p]\log F(\ell^{-1}(z))
     =\beta_p-p\ell_1\beta_1\in\mathbf Z_p                    \tag{CB19}
$
是整个单位格上的整连续读者；这里$p\ell_1$是单位。
范数单位与Coleman级数的识别仍取112.5所引
Schneider–Venjakob，Theorem 2.2、Remark 2.3，
只在真正的$\Phi$及其$\pi$-LT塔应用。

原Tate扭转使$\Lambda$的$[g_d]$在未扭范数单位上作$d^{-1}[d]$。
所以(CB19)的实际权为$d^{p-1}$；
对主单位$d$，$d^{p-1}-1\in p\mathbf Z_p$。
原驯分量是$e_\tau$，而$p\equiv1\bmod(p-1)$，
故该读者准确落在原源上。
(CB17)在此权取值$1-\alpha^{-p}$，模$p$仍为$1-\alpha^{-1}$；
完整平滑算子取值$103^2-103^p$，模$p$为$103^2-103$。
两者及原固定$(1+\omega_K)/6$、有限驯Shapiro次数均为单位。

真实源的Coleman函数就是$M(u(s))$。
代回物理对数，(CB19)读数准确为$p\,m_p$，
没有CM周期、Frobenius错位或人为删去的$\beta_1$。
因此(CB15)给
$
                     p\,m_p\in p^s\mathbf Z_p.
$
除去这个明确的$p$并用$s=t_p+2$，即得(CB14)。

#### 两种分裂型合用的范围

结合(CB9)，同一个充分条件$v_p(m_p)\le2$
适用于全部$p>211$惰性素数以及所有$a_p\ne1$的普通素数。
普通例外$a_p=1$满足CM范数等式
$
                         4p=1+3b^2,\qquad b\in\mathbf Z.
$
故$p\le X$的例外数为$O(\sqrt X)$，在素数中密度为零。
若主目标失败而通常全$\Sha[p^\infty]$只对有限多个$p$有限，
那么固定序列必须在密度一的素数集合满足$m_p\in p^3\mathbf Z_p$。
这是一条准确的剩余必要条件；本节尚未排除它，
也未把密度一的必要条件当成无穷非零的证明。

## 113. 原第五深槽的椭圆核与第二个整Artin–Hasse算子

**已证明。** 沿§§110–111记$\mathcal H=D_E-xJ$、$J=\partial_Z$、
$F_2=Z^2-x$、$F_3=Z^3-3xZ-2y$，原规范挠抬升为
$\widetilde P_t=(P_t,X_t)$；$c=c_p$、$q=p^2$。
本节保持(BD1)唯一需要$q$次精度的原深槽，不以浅窗替换它。

### 113.1 通用向量扩张的真实椭圆核

在特殊纤维记$G=L_p$，定义
$$
 \iota(P)=(\operatorname{Fr}_pP,G(P)),\qquad
 \chi(P,Z)=Z^p-G(P).
$$
(AZ1)与原斜率群律同时证明二者可加。在$O$上方的$V=Z+y/x$图，
$G+(y/x)^p=cs+O(s^{5p})$，故两个映射均正则。它们组成真代数群正合列
$$
 0\longrightarrow E_1\xrightarrow{\ \iota\ }E_1^\natural
             \xrightarrow{\ \chi\ }\mathbf G_a\longrightarrow0. \tag{CC0}
$$
确实，$d\iota=cJ\ne0$；$\ker\iota\subset\ker\operatorname{Fr}_p$
为连通有限群概形，而其切空间为零，所以核平凡。
$d\chi=-c\omega\ne0$。每个$\chi=0$的几何点，其基坐标有唯一Frobenius根，
垂直坐标也由$p$次根唯一决定；光滑核因此为$\iota(E_1)$。
$\iota$是从真射影曲线来的闭嵌入，且$\chi$为光滑满同态。
原$p'$挠抬升都在此核中，并有
$$
 \iota(P_t^{1/p})=\widetilde P_t.
$$
这里没有新选挠基。

还有
$$
 \iota^*F_2=G^2-x^p=2cL_{p-1},\qquad
 \iota^*F_3=G^3-3Gx^p-2y^p=3c^2L_{p-2}.
$$
$G=s^{-p}+cs+O(s^{5p})$、$x=s^{-2}+O(s^4)$、
$y=-s^{-3}+O(s^3)$给其唯一主部；减去显示项后只可能为常数，
由$\mu_6$非平凡权消去。

记$Q(s)$为原$E_1$严格形式点，$H_0$为BF2的原形式函数。
实际形式弧
$$
 a(s)=(Q(s),cH_0(s))
$$
在$V$图中主部相消。由$G=c(s+H_0^p)$，
$$
 \chi(a(s))=-cs,\qquad
 \iota(Q(s))=a(s^p)+(O,cs),\qquad
 [-p]a(s)=a(s^q)+(O,cs^p).
$$
第二式的基坐标使用严格参数的整$\mathbf F_p$下降；
第三式也可由$[-p]$落入(CC0)的核及基上的$\operatorname{Fr}_p^2$
确定。

对相应开集上正则的有理函数$U$，定义真实平移Hasse算子
$$
 h_nU(X)=[s^n]U(X+a(s)).
$$
其整提升在113.3给出。若$\deg_ZU\le3$，则对$0\le j\le3$，
$$
 \frac{c^j}{j!}h_mJ^jU(\iota P)
       =[s^{pm+j}](\iota^*U)(P+Q(s)).
$$
因为$\iota(Q(s))=a(s^p)+(O,cs)$，右边恰好只选垂直次数$j$；
$p>3$保证没有另一个同余次数。这是在实际紧椭圆核上的真标记读取，
并非纯形式的换元对象。

### 113.2 保留完整Frobenius的深槽公式

置$N=q+2p-2$、$w_t=\overline{\varepsilon(t)}$。完整原槽满足
$$
 \boxed{\quad
 (B'_{p+2})^p=-\frac1{2c}\sum_t w_t
 \left[h_NF_2-2Z\,h_NZ
       -c^{-1}Z\bigl(h_{p+1}F_2\bigr)^p\right](-\widetilde P_t).
 \quad}                                                       \tag{CC1}
$$
$h_NF_2-2Zh_NZ$对任意竖平移不变，故来自基$E_1$的有理函数。
最后一项保留原点坐标$Z=-X_t$，且在核上有$Z^p=G(P)$。
括号中$p$次幂是真系数及评价的Frobenius，不单独删去。

证明从(BD1)原式
$$
 B'_{p+2}=R_{p+2}
     \bigl(\nu_{11}-H_0\nu_{01}-C(sH_0\nu_0)\bigr)
$$
开始。$\nu_{11}-H_0\nu_{01}$除去不贡献本系数的原$\kappa\omega$项后，
除以$\omega$准确为
$$
 c^{-2}\sum_t\varepsilon(t)X_t^{1/p}
       \bigl(Z(a(s))-X_t\bigr)k_t(Q(s)).
$$
应用§110平方斜率式。$\sum\varepsilon(t)X_t^{1/p}=0$
由单位权$u^2$消失，常数不贡献正次$p+1$，故直接读者为
$$
 -\frac1{2c^2}\sum_t\varepsilon(t)X_t^{1/p}
              h_{p+1}F_2(-\widetilde P_t).
$$
取$p$次幂得$-(2c^2)^{-1}\sum_t w_tX_t(h_{p+1}F_2)^p(-\widetilde P_t)$。

深读者则准确为
$$
 \bigl(R_{p+2}C(sH_0\nu_0)\bigr)^p=[s^N]H_0f,\qquad f=\nu_0/\omega.
$$
§110已经逐点证明
$2Zf=\sum_t w_t\tau_t^*F_2+2\sum_t w_tX_t\tau_t^*Z$。
代入$cH_0=Z(a(s))$给出(CC1)前两项，再以
$X_t=-Z(-\widetilde P_t)$写回直接项，即得全式。
这里$s$及$H_0$的高位全部保留。

### 113.3 Artin–Hasse整算子支付真正$q$窗

置
$$
 \lambda_q=(p^q-p)^{-1}.
$$
$[-p]s=-ps+s^q$的严格对数由Teichmüller对称只含
$1\bmod(q-1)$次项，函数方程给
$\ell(s)=s+\lambda_qs^q+O(s^{2q-1})$。
特征零中的实际形式弧提升为
$$
 \exp\bigl(\ell(s)\mathcal H-\mu\ell(s^p)J/p\bigr).
$$
水平流的$Z$坐标为$\zeta$，BF2的完整整提升保证这个表达在$V$图整，
故每个真实$h_n$保持整函数。

记Artin–Hasse级数
$$
 \mathcal E(T)=\exp\left(\sum_{r\ge0}\frac{T^{p^r}}{p^r}\right)
            =\sum_{i\ge0}e_iT^i.
$$
它的Euler积
$\prod_{p\nmid m}(1-T^m)^{-\mu_{\rm Mob}(m)/m}$
证明全部$e_i$为$p$整。这里$e_i$是本节Artin–Hasse系数，
与§112依赖$M$的Euler因子系数不同。定义
$$
 \mathcal K=\frac{-\mu J-\mathcal H^p}{p},\qquad
 \mathcal L=\lambda_q\mathcal H-\frac{\mathcal H^q}{q}
                              -\frac{\mathcal K^p}{p}.
$$
这些算子彼此交换，也与$\mathcal H,J$交换。至次数$N$有
$$
 \sum_{n\ge0}h_ns^n
    =\mathcal E(s\mathcal H)\,
       \mathcal E(s^p\mathcal K)\,
       \mathcal E(s^q\mathcal L)\pmod{s^{N+1}}.
$$
对数的逐次比较证明此式；先比较$p$格、再比较$q$格，
并用已付的真实整$h_n$，顺次得到$\mathcal K,\mathcal L$
均为整算子，包括各固定标记点的整开集。

对竖次数至多三的函数，$J^p$在特征零已经严格为零，
$\mathcal H,\mathcal K$保竖次数，所以
$$
 \mathcal H^q=(-\mu J-p\mathcal K)^p\equiv0\pmod{p^3}.
$$
$\mathcal L$整便给
$\mathcal K^p\equiv p\lambda_q\mathcal H=-\mathcal H\bmod p$。
对$U=F_2,Z$，更一般地对竖次数至多二且$J^2U$为常数者，
准确的两窗约化为
$$
 \boxed{\begin{aligned}
 h_{p+1}U={}&\mathcal H
              (\mathcal K-ce_{p+1}J)U,\\
 h_NU={}&\mathcal H^{p-2}\mathcal L
                (\mathcal K-ce_{2p-2}J)U
       -e_{p+1}\mathcal H^{p-1}\mathcal KU
       +ce_{2p-2}e_p\mathcal H^{p-1}JU .
 \end{aligned}}                                                \tag{CC2}
$$
没有$\mathcal L$时，$\mathcal E(s\mathcal H)\mathcal E(s^p\mathcal K)$
的$N$格只有$i=p-2,2p-2,3p-2$可能贡献：
$\mathcal H^p=-cJ$及$J^3U=0$杀其余项。
最后一格含$\mathcal H^{p-2}J^2U=0$；
前两格以$\mathcal K^p=-\mathcal H$归并。
带$\mathcal L$的格满足$i+pj=2p-2$，仅$i=p-2,2p-2$，
再用$e_{p-2}=1/(p-2)!\equiv1\bmod p$，即得(CC2)。

(CC1)–(CC2)把唯一$q$窗化为第二个真实整算子$\mathcal L$。
与§§110–111同读，原五条分离系数已有同一个固定通用扩张上的完整表达；
这些恒等式本身仍不证明五条全迹在无限多个素数不同时为零。

## 114. 同一完整Kummer源在十二个固定真扭点盘上的精确分布

本节不是形式参数的任意平移。沿原真实六次扭转
$\theta^6=17$将$M$从$E_{17}$运至$E_1$，记为$M_\theta$；
记$F=K(\theta)$、$\delta^2=-3$、$\omega=(-1+\delta)/2$。
在乘法函数群的加法张量记号中置
$$
 U=e_+M_\theta,\qquad
 e_+=\frac16\sum_{u\in\mu_6}u^{-1}[u]^* .
$$
这里$U\in F(E_1)^\times\otimes_{\mathbf Z}\mathcal O$，
不是擅自给单个有理函数赋予一个它原本没有的$\mu_6$特征。
其准确性质为
$$
 [u]^*U=uU,\qquad
 \operatorname{div}U=-\omega\sum_t\varepsilon(t)[T_t].            \tag{CD1}
$$
本节$T_t$均指从物理$E_{17}$按上述同构运来的原标记。
(CD1)由$I_t=-\omega\varepsilon(t)-\bar\omega\bar\varepsilon(t)$
逐项投影得到；若使用§110的$P_t=-T_t$，需同步重标，不能只改一处符号。

### 十二个盘及真实有限群环

令$j=k+1$，保持(BT5)的
$A_j=(\mathcal O_K/p^j)^\times$、
$G_j=(1+p\mathcal O)/(1+p^j\mathcal O)$、
$g_w=\langle w\rangle$及原$P_w$的真实尺度。
对$R\in E_1[2\delta](K)$定义
$$
 Y_{j,R}=\sum_{w\in A_j}
       w^{-1}[g_w]^{-1}\,U(R+P_w)                              \tag{CD2}
$$
于实际$L_jF$的模$p^k$ Kummer张量及完整
$\mathcal O/p^k[G_j]$群环中。点$P_w$也已按$\theta$运至$E_1$。
原零极都含非零十七分量，而$R$仅有二、三分量，
所以所有这些评价均有定义。

在$R=O$处，(CD2)的$U$可准确换回$M_\theta$：
重标$w\mapsto uw$使逆Tate权乘$u$，$g_{uw}=g_w$，
恰好执行$e_+$投影。因此
$$
 \frac{\varepsilon(p)^j(1+\omega)}6
       (103^2-103[g_{103}])\,Y_{j,O}                           \tag{CD3}
$$
仍是(BT5)原完整源的限制，没有换成新来源。
另有$[103]R=R$，故同一个完整平滑算子也与这些盘的真实重标相容。
$[F:K]\mid6$，故在当前$p>211$范围，
限制后用corestriction乘该单位次数即可退回；此扩域不丢精度。

同一个换标及$U(uX)=uU(X)$给
$$
                            Y_{j,uR}=Y_{j,R}.                 \tag{CD4}
$$
十二点分为四个真实$\mu_6$轨道：原点一个、
非零二挠点三个、非零$\delta$挠点两个、
primitive $2\delta$挠点六个。

### 二、三处原导子给的完整范数关系

[R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)
的(12)、(16)将原完整导子逐项写成
$$
  T_t=[c]P-[u]Q,\qquad
  \varepsilon(t)=-u\chi_{17}(c),\quad
  c\in\mathbf F_{289}^\times,\quad u\in\mu_6 .
$$
固定同一十七分量，把$\operatorname{div}U$沿$[2]$推前，
每个纤维都求和掉原非平凡三次$\chi_2$；
沿$[\delta]$推前则求和掉原非平凡二次$\chi_3$。
故
$$
 [2]_*\operatorname{div}U=0,\qquad
 [\delta]_*\operatorname{div}U=0 .
$$
于是对$\alpha=2,\delta,2\delta$，确有
$$
       \sum_{S\in E_1[\alpha]}\tau_S^*U
                  \in F^\times\otimes\mathcal O.              \tag{CD5}
$$
这只是某个常数，不未经核定地说它为一。

在(CD2)中，每个固定主单位纤维里的常数贡献都含
$\sum_{d\in\mathbf F_q^\times}\omega(d)^{-1}=0$，
所以(CD5)的常数在完整有限群环中精确消失。
用(CD4)先按真实轨道合并，依次得到
$$
 Y_{j,O}+3Y_{j,2}=0,\qquad
 Y_{j,O}+2Y_{j,\delta}=0,\qquad
 Y_{j,O}+3Y_{j,2}+2Y_{j,\delta}+6Y_{j,2\delta}=0 .
$$
因此对全部$j=k+1$、全部$k\ge1$，
$$
 \boxed{\qquad
      Y_{j,R}=\lambda_R Y_{j,O},\qquad
 \lambda_R=
 \begin{cases}
  1,&R=O,\\
  -1/3,&R\in E_1[2]\setminus\{O\},\\
  -1/2,&R\in E_1[\delta]\setminus\{O\},\\
  1/6,&R\text{ primitive }2\delta .
 \end{cases}
 \qquad}                                                      \tag{CD6}
$$
分母全部为$p$单位。这是在两个变量的整个群环中成立的身份，
所以每个$I$截断、每个混合系数及其整$p^k$精度都同步运输。
特别原全Sha坏所迫的六个全域jet，准确在这十二个真盘上消失。

### 当地Coleman范数与未分歧Frobenius也相容

$p\equiv5\bmod6$时，$p+1$被六整除，
所以$\mathbf F_p^\times$的每个元素都是$\mathbf F_q^\times$中的六次方。
Hensel提升给所选$\theta\in\Phi=K_p$；
$U$的系数及$E_1[2\delta](K)$也都在$\Phi$。
因而此处Coleman底域仍是真正的$\Phi$，
不在额外未分歧扩域上错误地略去$\sigma_q$。

(BT6)的真正$[-p]$函数范数与$e_+$交换，给
$[-p]_*U=U$。又$[-p]R=R$，
于是
$$
                     [-p]_*\tau_R^*U=\tau_R^*U .               \tag{CD7}
$$
因此$(\tau_R^*U)(Q_j)$是同一LT塔上的严格范数单位张量，
其Coleman函数就是原固定$\tau_R^*U$在物理形式群上的展开。
不把它除以$U(R)$：任意这种归一会改变范数常数，
而本节所有正次读者本来就不需要这一除法。

若为检验除子临时把所有$\mathfrak f$点分裂，
$\sigma_q$对标记的作用是$T_t\mapsto[-p]T_t$；
$\varepsilon(-p)=1$使完整和逐项重排后仍固定。
这说明准确下降来自完整原和，不是将每个标记点假定为$\Phi$有理。

最后，在$R=O$及两个非零$\delta$点，可把(CD2)中的$U$
直接换成整个$M_\theta$。确实剩余成分$U_-=e_-M_\theta$
在$u\in\mu_3$下特征为$u^{-1}$；
$uR=R$和同一换标使其完整逆Tate投影满足
$Y_{j,R}^{-}=u^{-2}Y_{j,R}^{-}$。
取$u\ne1$，$1-u^{-2}$为单位，故这个投影精确为零。
在其它九点不作这一未经允许的替换。

(CD6)付出了原固定源的全精度平移关系。
它本身尚未把不同Teichmüller权之间的倒数曲率读者识别；
这仍须使用真实固定函数及后续完整算子比较。

## 115. 真实δ平移的协变导子与完整倒数曲率的固定短窗

本节继续§§110–114，在同一$E_1:y^2=x^3+1$及其通用向量扩张上工作。
置
$$
 \mathcal H=D-xJ,\quad J=\partial_Z,\quad
 F_2=Z^2-x,\quad F_3=Z^3-3xZ-2y,\quad
 g=y/x,\quad \mathcal B=\mathcal H-g .
$$
在固定双覆盖$\lambda^2=x$上，
$\mathcal B=\lambda\mathcal H\lambda^{-1}$。
这是同一个固定平方根联络的协变导子，非另选形式乘子。

### 两个真δ平移的完整函数身份

取$R=(0,1)$、$-R=(0,-1)$。
两点的规范向量扩张抬升分别为$(R,0)$、$(-R,0)$；
这正是原代数完成$\zeta$值$X(R)=X(-R)=0$。
其群律斜率为$m_\pm=(y\mp1)/x$，故
$$
 \tau_{\pm R}^*F_2-F_2=2Zm_\pm+2x,
 \qquad
 \tau_{\pm R}^*F_3-F_3
       =3Z^2m_\pm+6xZ+3y\pm1.                                \tag{CE1}
$$
这是特征零的有理函数身份。直接把
$Z'=Z+m_\pm$、$x'=m_\pm^2-x$、
$y'=-y+m_\pm(2x-m_\pm^2)$代入即可核对，所有常数都保留。

定义真实标记泛函
$$
 \mathscr L(V)=\sum_t\varepsilon(t)V(\widetilde P_t),
 \qquad P_t=-T_t,\quad \widetilde P_t=(P_t,X_t).
$$
原文中在$-\widetilde P_t$评价的同权全和等于
$-\mathscr L(V)$，由$t\mapsto-t$重标得到；不影响以下消失关系。
§114的真实$[\delta]$推除子为零给
$$
       \mathscr L(V+\tau_R^*V+\tau_{-R}^*V)=0                 \tag{CE2}
$$
对在所需标记处正则的每个有理$V$成立。
这也在规范挠抬升上成立，因为该抬升与挠点群法相容。

$\mathcal BZ=-x-gZ$、$\mathcal BF_2=\mathcal B(Z^2)-y$，
所以(CE1)–(CE2)给
$$
 \boxed{\qquad
 \mathscr L\!\left(\mathcal O\mathcal BZ\right)
       =\frac34\mathscr L(\mathcal O F_2),\qquad
 \mathscr L\!\left(\mathcal O\mathcal BF_2\right)
       =\frac12\mathscr L(\mathcal O F_3).
 \qquad}                                                     \tag{CE3}
$$
这里$\mathcal O$是任何与这两个真平移交换的算子，
特别包括前节所有$\mathcal H,J,\Xi,\mathcal K,\mathcal L$
的实际整组合；先在特征零取身份，再按已付整性约化。
对于$\bar\varepsilon$全和同理。
因此原$F_2,F_3$的完整迹确实接到了这个固定协变导子；
没有把一个$\mu_6$权直接冒充另一个权。

### 同一个倒数函数在两个δ点的全部留数

取惰性$p=6n-1>211$、$h=(p-1)/2=3n-1$。
沿(BG2)记
$$
 S_{n-1}(v)=\sum_{j=0}^{n-1}\binom{-1/2}{j}v^j,\qquad
 G=D^{p-2}x,\qquad DG=c .
$$
在同一固定双覆盖上令
$Q(P)=(x(P)^{-1},y(P)/\lambda(P)^3)$，则
$$
 J_p(P):=\lambda(P)G(Q(P))
          =-y\,x^{-h}S_{n-1}(x^3)                            \tag{CE4}
$$
是真正$E_1$上的有理函数；同时改$\lambda$的号会改$Q$为$-Q$，
所以乘积不变。除两个非零$\delta$点外它无极；
在$O$处它为正阶正则函数。
两商不变微分给$D_Q=-\lambda D$，于是
$$
                         (D-g)J_p=-c.                        \tag{CE5}
$$
这里$G$是在倒数点的真实值，未套用原挠点的固定性。

用相同的原$P_t,X_t,\varepsilon(t)$定义
$$
 \eta_X=-\sum_t\varepsilon(t)X_t^2\kappa_{P_t}
       =\varphi_X(x)\,\omega,\qquad
 \varphi_X(x)=\sum_t\frac{\varepsilon(t)X_t^2y_t}{x-x_t}.
                                                                    \tag{CE6}
$$
原$\kappa_{P_t}$在$P_t$的留数为$-1$，故$\eta_X$留数为
$+\varepsilon(t)X_t^2$。全常数
$\sum_t\varepsilon(t)X_t^3$由$\mu_6$权消失；
带$y(P)$的部分由$t,-t$配对消失，所以(CE6)没有遗漏全纯项。
$\eta_X$在$O$和$\pm R$都正则。
此外$\mu_6$重标准确给
$$
                       \varphi_X(x)=x\,R_X(x^3),              \tag{CE7}
$$
其中$R_X$是特征零中已固定的有理函数，
系数属于一个固定数域，不依赖$p$。
它在$x^3$的原$\mu_6$轨道标记处只有简单极。
(CE6)中先合并同轨六项即可构造它，未新增随$p$变化的输入。

完整倒数曲率标量为
$$
              r_p=\sum_t\varepsilon(t)X_t^2J_p(P_t).
$$
它正是$J_p\eta_X$在全部原标记处的留数和。
在$R$及$-R$以$x$为真实局参，(CE4)和
$\omega=dx/(2y)$使
$$
       J_p\eta_X=-\tfrac12 x^{-h}S_{n-1}(x^3)\varphi_X(x)\,dx .
$$
两处留数相同，且$O$没有留数。因此全局留数定理准确给
$$
 \begin{aligned}
 r_p
  &=[x^{h-1}]S_{n-1}(x^3)\varphi_X(x)\\
  &=[v^{n-1}]S_{n-1}(v)R_X(v)
   =\boxed{\ [v^{(p-5)/6}]\frac{R_X(v)}{\sqrt{1+v}}\ }\pmod p .
 \end{aligned}                                                \tag{CE8}
$$
最后一项取常数为一的平方根；只读至$n-1$，
所以截断$S_{n-1}$与完整$(1+v)^{-1/2}$恰好一致。
这些分母的指标均小于$p$，约化合法。
两个δ留数的因子$1/2$已经合并，式中没有遗漏倍数或总号。

(CE3)是原完整来源的真平移身份，(CE8)是原完整带权曲率和的真短窗。
它们尚未证明全Sha坏会使(CE8)为零：
$\mathcal B$的原整除幂算子及全部混项仍须接合，
而AQ密度应用还须保持其全Galois分量与普通处的真实权。

## 116. 原倒数母量是两个固定二步联络的真实曲率子式

以下联络均固定在第二个$E_1:y^2=x^3+1$上，
不随素数改变；最后才把其坐标取为原$Q(P_t)$。
置$g=y/x$、$\omega=dx/(2y)$、$D=\omega^{-1}d$。
对$b=1,x$定义
$$
 \nabla_b=d+
 \begin{pmatrix}
  0&-g\omega&0\\
  0&0&-b\omega\\
  0&0&0
 \end{pmatrix},
 \qquad -g\omega=-\tfrac12d\log x.                            \tag{CF1}
$$
它们在去掉$O,(0,1),(0,-1)$的同一固定开曲线上为平坦连接。
本节用$d+A$号；这与(BI3)的$d-\theta$号须按所示矩阵转换。

### 两型素数的全部曲率项

在$p>3$好约化处写
$$
 D^p=aD,\qquad
 G=D^{p-2}x,\qquad DG=D^{p-1}x=ax+c .
$$
这里$a=a_p\bmod p$是Hasse标量；
普通$p\equiv1\bmod6$时$c=0$，
惰性$p\equiv-1\bmod6$时$a=0$、$c=c_p\ne0$。
第二个等式可以从
$D(D^{p-1}x-ax)=0$直接证明：
其为$p$次幂，且唯一极在$O$、阶小于$2p$，
取$p$次根后至多一个简单极，椭圆曲线上只能为常数。
$\mu_6$权再给普通处$c=0$；惰性处为原(BG2)。

记
$$
 \Psi_b=\psi_{\nabla_b}(D)=\nabla_{b,D}^{\,p}-a\nabla_{b,D}.
$$
因为$g\omega=\tfrac12d\log x$经Cartier不变，
$D^{p-1}g=ag-g^p$，所以两条连接的共同上格为
$$
                  (\Psi_b)_{12}=g^p .
$$
另外
$$
 (\Psi_1)_{23}=a,\qquad
 (\Psi_x)_{23}=-c,\qquad
 (\Psi_b)_{13}=k_b
     :=\sum_{r=0}^{p-2}D^{p-2-r}\!\left(gD^r b\right).          \tag{CF2}
$$
最后一式直接把$\nabla_D^p$作用到第三基向量：
两次严格上三角跃迁必须依次经过$-b,-g$，故乘积为正号，
余下各次为真实$D$。$\nabla_D$的右上格为零，
因此减$a\nabla_D$不改变该项。

曲率与连接交换，给
$$
                      Dk_b=g(\Psi_b)_{23}-b g^p.              \tag{CF3}
$$
也可以逐项微分(CF2)并使用$D^p=aD$核定。

### 全局极与μ₆权唯一确定那个子式

置
$$
 w=k_1(\Psi_x)_{23}-k_x(\Psi_1)_{23}
    =-c k_1-a k_x .
$$
(CF3)给$Dw=(c+ax)g^p=D(g^pG)$，
所以$w-g^pG$为有理函数域中的$p$次幂。

在$R_\pm=(0,\pm1)$，$g$只有一个简单极，
而$k_b$的极阶至多$p-1$。
$G(R_\pm)=0$：这两点被$\mu_3$固定，
$G$的权为$u^{-p}\ne1$，且在那里正则。
故$g^pG$在两点的极阶也至多$p-1$。
一个$p$次幂不能有这样的非零极阶，因而$w-g^pG$在两点正则。

在$O$取原物理切线参数$z$。
$g=-z^{-1}+\cdots$、$G=z^{-p}+\cdots$，
后一个首系数是$-(p-1)!\equiv1$；
$w$的极阶至多$p+1<2p$。
所以$w-g^pG$的首极为$+z^{-2p}$。
减去$x^p$后，仍是$p$次幂，唯一可能极在$O$且阶小于$2p$。
其$p$次根至多一个简单极，故只能是常数。
普通时所有剩余项具有$\mu_6$权$u^{-2}$，
惰性时具有权$u^2$；两者非平凡，常数为零。

于是对普通和惰性好素数同时有精确身份
$$
 \boxed{\quad
   (\Psi_1)_{13}(\Psi_x)_{23}
     -(\Psi_x)_{13}(\Psi_1)_{23}-x^p
                       =g^pG .
 \quad}                                                       \tag{CF4}
$$
普通的$G$准确等于(BI4)的$\overline{K_\pi}$。
为付极阶，规范$\psi_\pi=\sigma(\pi z)/\sigma(z)^p$
是$x$的次数$(p-1)/2$多项式，首系数$\pi$；
非零$\pi$挠点的$x$赋值均为$-2/(p-1)$。
于是常数项为单位，其余系数均在$\pi\mathcal O$。
因此$K_\pi=\pi^{-1}D\log\psi_\pi$约化为
仅在$O$有极、极阶至多$p$的有理函数。
其导数为$ax$，与$G$相同。
差为$p$次幂，取根后至多一个简单极，故常数；
奇性又消去该常数。惰性则为原$G$。
所以(CF4)保留两型实际曲率，未把普通标量替成惰性值。

### 原完整源确实使用这个固定对数微分

在物理模型$E_{17}$上，先将其$\delta$点相应运输，
或者等价地始终在$E_1$使用$M_\theta$。
保留(BT1)的$T_t,I_t$标签。
完整原质量在$[\delta]$推前为零，
因为$\varepsilon$和$\bar\varepsilon$两部分在三处的非平凡
二次角色都被真正纤维求和消去。
而
$$
 \operatorname{div}x(P-T_t)
    =[T_t+R]+[T_t-R]-2[T_t].
$$
故比较真实除子，再在$P=O$归一，得到
$$
 \boxed{\qquad
 M_\theta(P)^{-3}
     =\prod_t
       \left(\frac{x(P-T_t)}{x(-T_t)}\right)^{I_t}.
 \qquad}                                                      \tag{CF5}
$$
每个$x(-T_t)$都非零，因原标记有非零十七分量。
这里是有理函数的精确身份，不只是对数导数同余。
若改写$P_t=-T_t$而仍保持原$I_t$，
右边成为$M_\theta(P)^3$，不能保留左边的负三次方。

因此(CF1)的第一个对数因子确实来自原M的固定平移组成。
但是该来源识别仍不能把完整曲率矩阵说成全零：
例如(CF2)中$g^p$一般从来不为零，
原$f(O)=D\log M(O)=0$只消掉相应加权组合在原点的值，
不是整个开曲线上的函数。
(CF4)是曲率的一个二次子式，也不是新的线性$p$曲率。
应用固定联络代数性或AQ密度之前，仍须证明
原全Sha坏输入确实消掉所需的完整带权子式、补偿项及所有Galois分量。

## 117. 真实邻曲线的两次变形分离第五深槽的一项

**已证明。** 取全部$p>211$惰性素数，仍用原固定$E_{17}$、
完整$M$、两变量Tate源及§113的$\mathcal H,J,\mathcal K,\mathcal L,h_n$。
若通常全$\Sha(E_{17}/\mathbf Q)[p^\infty]$无限，还有以下必要条件（§118已进一步证明第一式正是旧第五槽的全局简式，不能视为额外独立条件）
$$
 \boxed{\quad
       h_{q+2p-2}U_2(e)=0,\qquad
       \mathcal H^{p-1}\mathcal L U_2(e)=0 ,
       \quad}                                                 \tag{CG1}
$$
其中$q=p^2$，$e$为通用向量扩张的恒等点，
$$
 U_j=\sum_t I_t\,\tau_{-\widetilde T_t}^{\,*}F_j,\qquad
 F_2=Z^2-x,\quad F_3=Z^3-3xZ-2y .
$$
这里先保物理整数$I_t=-\omega_K\varepsilon(t)
-\bar\omega_K\bar\varepsilon(t)$，再按真实$\mu_6$权分支。
第一条准确选择$\bar\varepsilon$支，第二条选择$\varepsilon$支。
所有点、外部系数及Frobenius一起运输。

特别第一条与(CC1)的第五槽合用给
$$
 \sum_t\bar\varepsilon(t)\,
 Z\left[2h_{q+2p-2}Z+
              c^{-1}\bigl(h_{p+1}F_2\bigr)^p\right]
             (-\widetilde P_t)=0 .                            \tag{CG2}
$$
(CG1)中的第一式不是只由五槽的形式联立所得：
以下使用原$M$在真实循环邻商上的有限变形。
(CG2)仍保两个项的总和；本节没有把任一项单独置零，
也未证明AQ全部曲率或主目标。

### 117.1 保留Tate扭转的绝对微分多给一个边界系数

先在物理$E_{17}$使用112.5的真实$[-p]$-LT塔。
写$\Phi=\mathbf Q_{p^2}$，$Q_j$为原范数相容本原点，
$z=s(Q_2)$、$t=s(Q_1)=[-p]z=-pz+z^q$。
由(CB8)，坏情形的完整当地类属于$I^3P$。
整个$103^2-103[g_{103}]$在$(p,I)$处为单位，
所以去除此实际算子后仍保$I^3$；有限Shapiro只除驯群阶。
令$r_2$为原$e_\tau[M(Q_2)]$，或仅在外部系数施Frobenius后的
$e_{\tau^p}[M(Q_2)]$。

在模$p^2$的第二层，真野群为$C_p^2$。
其未扭增广理想记$\mathfrak J$。
原扭转生成元是$d^{-1}[d]-1$或$\bar d^{-1}[d]-1$；
因$d\in1+p\mathcal O$，它们均属于$\mathfrak J+p$。
$d\equiv1\bmod p^2$在本层及系数中同时为一。因此
$$
 r_2\in(\mathfrak J^3+p\mathfrak J^2)P_2\pmod{p^2},           \tag{CG3}
$$
$P_2$为实际单位Kummer张量；非平凡驯分量已消去赋值商。

取两个独立方向$h,l\in\mathbf F_q$，其实际野元记$G_h,G_l$。
置
$$
 N_h=\sum_{i=0}^{p-1}G_h^i,\quad T_l=G_l-1,\quad
 L_l=\sum_{i=1}^{p-1}\frac{(-1)^{i-1}}iT_l^i .
$$
这些分母全为$p$单位。
$N_h(G_h-1)=0$，而
$T_l^p=-\sum_{i=1}^{p-1}\binom piT_l^i\in p\mathfrak J$。
所以对$r\ge p-3$，(CG3)严格给
$$
                    N_hL_l^r r_2\in p\mathfrak J P_2
                                      \pmod{p^2}.             \tag{CG4}
$$
这里没有把原Tate扭转先模$p$丢掉。

真实Eisenstein方程为$t(z)^{q-1}-p=0$，
其分歧指数和different分别有
$$
 e=v_z(p)=q(q-1),\qquad
 v_z(\mathfrak D)=e+q(q-2)>e+1 .
$$
故绝对微分$\Omega_{\mathcal O_{\Phi_2}/\mathcal O_\Phi}$
再模$pz$是自由的一元
$(\mathcal O_{\Phi_2}/(pz))\,dz$。
野元固定未分歧系数且$gz=z+O(z^2)$。
对任意整单位$V$，
$gV/V\in1+z^2\mathcal O_{\Phi_2}$，
故$d\log(gV/V)\in z\Omega$。
(CG4)于是给实际绝对$d\log$属于$pz\Omega$；
模$p^2$的Kummer误差同样落在$pz\Omega$。
允许固定未分歧扩域以分裂全部标记时，
different及这一结论均不改变。

还须将此绝对微分准确改为邻商的固定$t$微分。
若$L_l^r=\sum_j b_jG_l^j$，用独立变量$z,t$书写原全源
$$
 \mathscr F(z,t)=
 \sum_{a\in\mathbf F_q^\times}\sum_{i,j}
 \omega(a)^{-\chi}b_j
 \log M_\theta\!\left(
     [\omega(a)]Q(z)-[\omega(a)(ih+jl)]Q(t)\right),
 \quad \chi=1\ \text{或}\ p .                                \tag{CG5}
$$
$\theta^6=17$，原CRT的固定可逆标量始终随$Q_j$运输。
对数本身仅作求导，两偏导皆整。
$t=[-p]z$时，(CG5)恰为(CG4)的实际单位张量，
因为$G_h^iG_l^j$在$p^2$挠点上为$1+p(ih+jl)$。
原$m_1=0$给$\partial_t\mathscr F(0,0)=0$，
故$\partial_t\mathscr F(z,t(z))\in z\mathcal O_{\Phi_2}$。
又$t'(z)=-p+qz^{q-1}\in p\mathcal O_{\Phi_2}$，所以
$$
       \partial_z\mathscr F(z,t(z))\in pz\mathcal O_{\Phi_2}.
                                                               \tag{CG6}
$$
这一额外的$z$来自绝对微分和原首对数零；
不能由相对$\Omega_{\Phi_2/\Phi_1}$的不同理想擅自取得。

### 117.2 真循环邻商及截断对数的全部精度

在$E_1:y^2=x^3+1$工作。对惰性$p$，
$17$在$\mathbf F_{p^2}$有六次根，因为$(p+1)/6$为整数；
Hensel提升给$\theta\in\mathcal O_\Phi^\times$。
故六次模型运输只乘共同单位，未另加$(17/p)=1$限制。

令$S=Q(t)$、$C_a=\langle[ah]S\rangle$，
$\phi_a:E_1\to E_{C_a}$为真循环商，
$c_{\phi,a}$由$\phi_a^*\omega_a=c_{\phi,a}\omega$定义。
其赋值为$v_t(c_{\phi,a})=p-1$。
置$u_a=s_a(\phi_a([-al]S))$，
则$v_t(u_a)=p$，它生成双对偶核。
令$M_a=\operatorname{Norm}_{\phi_a}M_\theta$、
$f_a=D_a\log M_a$。范数在$O$取值为一：
原$M_\theta(-P)=M_\theta(P)^{-1}$使非零核点两两相消。

对任意整函数，平移$u_a$的小于$p$次Taylor项均整，
且$1/n!$在$n<p$为单位。
实际截断群环对数因而满足
$$
 \frac{L_l}{u_a}
   \equiv \frac{\ell_{a,<p}(u_a)}{u_a}\,D_a
                  \pmod{u_a^{p-1}\operatorname{End}},
                                                               \tag{CG7}
$$
其中$\ell_{a,<p}$是实际不变对数的小于$p$次截断，
绝非整个挠点对数（后者为零）。
两边均整，取任意$r\le p-1$次方不再损失这个相对精度。
先做原$N_h$范数，再应用(CG7)，(CG6)成为
$$
 \sum_a\omega(a)^{1-\chi}c_{\phi,a}
      \ell_{a,<p}(u_a)^r
       (D_a^r f_a)(\phi_a([\omega(a)]Q(z)))
                          \in pz\mathcal O_{\Phi_2}.           \tag{CG8}
$$
省去的误差至少有$t$阶$p-1+pr+p(p-1)$，
对$r\ge p-3$严格高于$e+1$换算成$t$的界，故不污染以下窗口。

取$r=p-1-j$，$j=0,1,2$。
(CG8)的共同首因子为$t^{p-1+pr}$。
除去它和已展示的单位后，
$e-q(p-1+pr)=jpq$，因此可读到$z^{jpq}$，包括边界。
所有剩余系数在这个窗口可约到特征$p$，
并可取$t=z^q$：被消去的$p$项均带正$z$次幂。
保留完整Teichmüller和后，许可原指数恰为
$$
 \begin{array}{ll}
 \chi=1:& n=jp+d(q-1),\quad 0\le n\le jpq,\\
 \chi=p:& n=jp+p-1+d(q-1),\quad 0\le n\le jpq,
 \end{array}\qquad d\ge0 .                                    \tag{CG9}
$$
后续只使用这些实际界内的系数。

### 117.3 邻曲线的外标量在所需两级没有未知补偿

标号核$C_a$在$t\mapsto nt$、$n\in\mathbf F_p^\times$下不变，
故其商及所有素于$p$标记定义于$t^{p-1}$的整环。
选特殊纤维与原相对Frobenius一致的短模型，
再以唯一$1\bmod t$的六次根归一为
$$
                         E_A:y^2=x^3+Ax+1 .
$$
在模$t^{2p+1}$的范围，$p=0$且对偶微分为零。
光滑相对曲线中微分为零的映射经相对Frobenius分解；
余下为度一同构。由特殊纤维及归一，准确有
$\widehat\phi=-\operatorname{Fr}$、$\phi=-V_A$，
其源为$E_{A^p}=E_1$，因为这里$A^p=0$。
于是
$$
 c_\phi=-H(A),\qquad
 H(A)=[x^{p-1}](x^3+Ax+1)^{(p-1)/2}.
$$
写$p=6n_0-1$，则
$$
 H(A)=H_1A+O(A^4),\qquad
 H_1=\frac{(3n_0-1)!}{(2n_0-1)!(n_0-1)!}\ne0\bmod p .
$$

原$\zeta\in\mu_6$把$C_a$送到$C_{\zeta a}$，
在商模型上由特殊Frobenius决定其标量为$\zeta^p$；
$B=1$的归一使这一标量没有未知连续单位。
故$A$和$c_\phi$随$t\mapsto\zeta t$的权为$\zeta^{p-1}$。
结合$\mathbf F_p^\times$不变性，
其$t$指数必须是$k(p-1)$且$k\equiv1\bmod3$。
核多项式首项及$v_t(c_\phi)=p-1$遂给固定$\kappa\ne0$使
$$
 A_a=\kappa(ah)^{p-1}t^{p-1}+O(t^{4(p-1)}).                    \tag{CG10}
$$
同样，$\ell_{a,<p}(u_a)$在$\mathbf F_p^\times$下权一、
在$\mu_6$下权$p$。其首项为
$$
 c_0a^p(l^p-h^{p-1}l)t^p,\qquad c_0\ne0 ,
$$
下一许可相对指数为$3(p-1)>2p$。
$h,l$独立保证括号非零。因此在(CG9)的$j=2$窗口，
外部$c_\phi,\ell^r$只贡献已知非零首项；
实际变形仅需保$A,A^2$。

用$M_A$表示除子为真实$\phi_A(T_t)$、
$O$值为一的函数。素于$p$的挠截面唯一提升，
而$\sum I_tT_t=0$也唯一提升，故此函数存在且唯一；
它恰为上述实际范数，未另选同除子源。
将
$$
 \mathscr V_A(P)=
   (\mathcal H_A^r f_A)(-V_A^\natural P)
           =F^{(0)}(P)+AF^{(1)}(P)+A^2F^{(2)}(P)+\cdots
$$
代回(CG8)。
每个$k=0,1,2$的外部$a$指数由
$A_a^k$与$z$系数相加，恰给(CG9)同一许可总指数；
其贡献为
$$
 \kappa^k(h^{p-1})^k
         [z^{\,n-qk(p-1)}]F^{(k)}(Q(z)).
$$
$h^{p-1}$遍历$\mu_{p+1}$，$p+1>2$，
所以Vandermonde分离使三个$k$各自为零。
这一步保完整角向和，仅分离真实的邻商参数。


### 117.4 通用扩张上的实际Gauss–Manin抬升

以下把两个变形系数完整算出。本段$f,U_j$先取实际初始$\operatorname{Fr}_pT_t$标记，117.7再统一搬回。置
$$
 \Delta=4A^3+27,\quad \omega=dx/(2y),\quad
 \eta=dZ+x\omega,\quad \mathcal H=D-xJ .
$$
令$\partial_A^0$固定$x,Z$，并令
$\partial_A^0y=x/(2y)$。逐项微分给
$$
 \begin{pmatrix}\partial_A^0\omega\\
                 \partial_A^0(x\omega)\end{pmatrix}
 =
 C\begin{pmatrix}\omega\\x\omega\end{pmatrix}
       +d\begin{pmatrix}R_\omega\\R_\eta\end{pmatrix},
\quad
 C=\frac1\Delta
       \begin{pmatrix}-A^2&9/2\\3A/2&A^2\end{pmatrix},
$$
其中
$$
 R_\omega=\frac{-3A-A^2x-\tfrac92x^2}{\Delta y},
 \qquad
 R_\eta=\frac{\tfrac92+\tfrac32Ax-A^2x^2}{\Delta y}.
$$
定义实际基方向抬升
$$
 \mathcal T=\partial_A^0+
       (C_{01}Z-R_\omega)\mathcal H+
       (C_{11}Z-R_\eta)J .                                    \tag{CG11}
$$
Cartan公式给
$$
 \mathcal L_{\mathcal T}\omega=C_{00}\omega+C_{01}\eta,\quad
 \mathcal L_{\mathcal T}\eta=C_{10}\omega+C_{11}\eta,
$$
以及
$$
 [\mathcal T,\mathcal H]=-C_{00}\mathcal H-C_{10}J,\qquad
 [\mathcal T,J]=-C_{01}\mathcal H-C_{11}J.                      \tag{CG12}
$$
$\mathcal T$是抬升$\partial_A$的群型导子，
不是纤维内的平移不变向量场。

这里可直接检查正则性和群型，毋须猜测一个形式热算子。
在有限图有
$$
 \begin{aligned}
 \mathcal T x&=2C_{01}yZ+(6A+2A^2x+9x^2)/\Delta,\\
 \mathcal T y&=C_{01}(3x^2+A)Z+
                       (\tfrac{27}2x+3A^2)y/\Delta,\\
 \mathcal T Z&=(C_{11}-xC_{01})Z-C_{01}y .
 \end{aligned}
$$
故$y=0$处没有极。在$O$图
$t=-x/y,\ V=Z-1/t$，有$1/t-xt=O(t^3)$，而
$$
 C_{01}Z-R_\omega
   =C_{01}V+C_{01}(1/t-xt)-A^2t/\Delta-3At/(\Delta x)
$$
正则，$\mathcal Tt|_{t=0}=C_{01}V$；代入$\mathcal TV$
也正则并在$e$为零。
特征零中，两真不变形式的群律与上述Lie导数说明：
两因子上$\mathcal T$之和与乘法后$\mathcal T$之差，
其两个不变坐标的相对微分为零，且在$e$为零，
故差为零。该恒等式在$\mathbf Z[1/(6\Delta)]$的整有理式中成立，
所以可在每个本节$p$约化。

还需付出与实际$-V_A^\natural$的自然性。
在特征$p$，其源$E_{A^p}^\natural$的基方向为固定坐标的$\partial_A$；
所有群律系数为$p$次方，故它同样群型。
此导子与目标$\mathcal T$沿$-V_A^\natural$之差，
是到目标Lie代数的群同态，其两个坐标为全局正则函数，
且竖次数至多一。

所需的常数结论在特征$p$有明确次数限制：
非平凡$\mathbf G_a$扩张的全局正则函数，若竖次数$d<p$，
则最高系数是底椭圆曲线上的常数$c$；
下一系数的粘合差给$d\,c$倍的非零扩张类。
$d$可逆，故$c=0$，降次即只剩常数。
因此上述差为常数，并由恒等点处零而消失。
相同论证或素于$p$的挠阶可逆性，
说明全部规范挠截面对$\mathcal T$水平。
这给真实$V_A^\natural$和全部移动标记的自然性。
求导先在完整特征$p$通用族中进行，再在$A=0$取值；
没有把$\partial_A$错误定义在商环$k[A]/A^3$上。

### 117.5 原范数函数的两条完整热方程

在每个移动挠点$\widetilde T_t(A)$附近，
群型$\mathcal T$与其平移相容。
$M_A$的阶为$I_t$，而$\mathcal Tt=C_{01}V+O(t)$，
故$\mathcal T\log M_A$的极部为$I_tC_{01}V/t$。
同一图中$F_2=Z^2-x$的唯一极部为$2V/t$。
逐物理标记相减后，
$$
 \mathcal T\log M_A-\frac{C_{01}}2
             \sum_t I_t\tau_{-\widetilde T_t(A)}^*F_2
$$
全局正则，竖次数至多二。
上面的次数引理使它为常数；
在$e$，$M_A(O)=1$给左首项零，
而$I_{-t}=-I_t$、$F_2$偶使全迹零。
故有准确恒等式
$$
                 \mathcal T\log M_A=(C_{01}/2)U_2(A).          \tag{CG13}
$$

在$A=0$，
$C_{00}=C_{10}=C_{00}'=C_{01}'=0$，
$C_{01}=1/6$，但$C_{10}'=1/18$不能删去。
又$J\log M=Jf=0$，其中$f=D\log M$。
直接由(CG11)得到
$$
 \mathcal T_0=\partial_A^0+
       \frac{Z+x^2/y}{6}\mathcal H-\frac1{6y}J,\qquad
 \mathcal T_0F_2
     =-\frac{xZ^2+2yZ+x^2}{3}
     =\frac19\mathcal H F_3 .
$$
因此
$$
 \mathcal T f|_0=\frac1{12}\mathcal H U_2,\qquad
 \mathcal T^2f|_0=\frac1{108}\mathcal H^2 U_3 .
$$
对任意$r$，二次交换中可能留下的项为
$-rC_{10}'\mathcal H^{r-1}Jf$，确因$Jf=0$而消失。
真实范数拉回的三个系数遂准确为
$$
 \boxed{\begin{aligned}
 F^{(0)}&=\iota^*(\mathcal H^r f),\\
 F^{(1)}&=\frac1{12}\iota^*(\mathcal H^{r+1}U_2),\\
 F^{(2)}&=\frac1{216}\iota^*(\mathcal H^{r+2}U_3).
 \end{aligned}}                                                \tag{CG14}
$$
$216$包含Taylor二次系数的$2$。
初始$M_A$的标记其实为$\operatorname{Fr}_pT_t$，
故这些式子先用于整套Frobenius后的$U_j$；
117.7统一搬回原标记。

这也校正一个容易误判的中间项：
$xZ^2+2yZ+x^2=-\mathcal HF_3/3$，
并非独立的新第四权函数。
二次变形自身不能据此宣称给出AQ倒数曲率。

### 117.6 边界内的两条一次变形准确分离裸深项

取$j=2$、$r=p-3$、原外嵌入$\chi=1$。
在(CG9)中取
$$
 n_1=(2p-1)q+1=2p+(2p-1)(q-1),\qquad
 n_2=2pq=2p+2p(q-1).
$$
两者确在已付的边界内。
一次变形减去$q(p-1)$后，其真实指数分别为
$m_1=pq+1$、$m_2=q(p+1)$。
由(CC0)的紧椭圆核读者及(CG14)，得到
$$
 \begin{aligned}
 \mathcal H^{p-2}(\mathcal L-e_p\mathcal H)J U_2(e)&=0,\\
 h_{q+p}\mathcal H^{p-2}U_2(e)&=0 .
 \end{aligned}                                                \tag{CG15}
$$
第一式用$h_qJ U_2=(\mathcal L-e_p\mathcal H)J U_2$：
$J^2U_2=2\sum I_t=0$，所以$JU_2$为底函数，
其$\mathcal H^p$为零，而$\mathcal K^p=-\mathcal H$。

现在逐项核完整Artin–Hasse分解，不能只取形式最高幂。
为简记写$H=\mathcal H,K=\mathcal K,L=\mathcal L$，
$N=q+2p-2$。
在$H^{p-2}U_2$上，$h_{q+p}$的不含$L$部分由
$(i,j)=(0,p+1),(p,p),(2p,p-1)$贡献：
$$
       -e_{p+1}HK+c e_p^2JH+0 .
$$
第三项含$J^2U_2$，以后各项亦为零；
含$L$部分为$LK-ce_pLJ$。
而(CC2)给完整$h_NU_2$。
两者相减准确为
$$
 \left(h_{q+p}H^{p-2}-h_N\right)U_2
   =c(e_{2p-2}-e_p)H^{p-2}(L-e_pH)J U_2 .                    \tag{CG16}
$$
(CG15)同时杀右边与左边第一项，
故$h_NU_2(e)=0$，即(CG1)第一式。
没有要求$e_{2p-2}-e_p$为单位。

### 117.7 另一真实系数嵌入给单独的第二AH迹

在同一个(CG3)–(CG9)证明中改取$\chi=p$。
仍取$j=2,k=1$，一次变形的三个许可指数为
$$
 m_0=2p,\qquad m_1=(p-1)q+p+1,\qquad m_2=pq+p .
$$
对应原指数均为$m_i+q(p-1)\le2pq$，
且模$q-1$为$3p-1$，与(CG9)完全一致。
(CC0)和Artin–Hasse逐项分解分别给
$$
 \begin{aligned}
 h_2H^{p-2}U_2&=-cJU_2/2,\\
 c h_{q-p+1}H^{p-2}JU_2
       &=c e_{p-1}H^{p-1}K^{p-1}JU_2,\\
 h_{q+1}H^{p-2}U_2
       &=H^{p-1}LU_2+c e_pJU_2
          -c e_{p+1}e_{p-1}H^{p-1}K^{p-1}JU_2 .
 \end{aligned}
$$
三个真实值均为零，且$c,e_{p-1}$为单位，
所以先消前两项，再得$H^{p-1}LU_2(e)=0$。

最后核标记和外系数相位。
先在包含所有素于$p$标记的未分歧整环计算，
始终使用有理整数$I_t$。
绝对剩余Frobenius$\sigma$将每个$T_t,X_t$一起送到
$\operatorname{Fr}_pT_t,X_t^p$，
故初始完整$U_j^F=\sigma(U_j)$。
$E_1,H,J,K,L,h_n$均在$\mathbf F_p$下降，
因而可对整个真实等式施$\sigma^{-1}$，将全部标记同时搬回。
即使单个标记不在$\mathbf F_{p^2}$，这一论证仍成立。
$\theta$也一起运输；其特殊纤维$\sigma\theta/\theta\in\mu_6$，
不是擅设物理周期为实数。

此后才分$I_t$。
$h_NF_2$的$\mu_6$权为$u^{-N-2}=u$，
故只留$I_t$的$\bar\varepsilon$支；
$H^{p-1}LF_2$的权为$u^{-(p-1+q+2)}=u^{-1}$，
故只留$\varepsilon$支。
共同非零常数$-\omega_K,-\bar\omega_K$可消。
§113取$P_t=-T_t$；$F_2$偶且$N$奇，所以$h_NF_2$奇，
将全部$T_t$同时换成$P_t$只给共同负号，零条件不变。
第一式因此与原(CC1)确切合并为(CG2)。
这里没有取得任意改权的独立消失，
尤其没有付出R1073 §34所需的全部$\sigma$曲率条件。

## 118. 第五槽余项在真椭圆核逐点相消

**已证明。** §117的第一条裸深迹必要零是原第五槽的准确全局简式，
不是额外独立的第六个约束。沿§113置$N=q+2p-2$，则在真实椭圆核
$\iota(E_1)\subset E_1^\natural$上有
$$
 \boxed{\qquad
       \bigl(h_{p+1}F_2\bigr)^p=-2c\,h_NZ .
       \qquad}                                                \tag{CH1}
$$
所以原完整(CC1)无条件简化为
$$
 \boxed{\qquad
 (B'_{p+2})^p=-\frac1{2c}
         \sum_t\bar\varepsilon(t)h_NF_2(-\widetilde P_t).
       \qquad}                                                \tag{CH2}
$$
(CG2)的两项逐点相反，不能各自作为新的非零门。
这项简化使用同一紧椭圆核及全局有理函数，
不声称任意满足五槽的纯形式输入也有此额外几何身份。

### 118.1 实际严格群律的对角正则性

令$\mathcal F(t,s)$为原严格坐标下的特殊纤维群律。
§85已证不变微分在这个坐标准确为$ds$，
所以
$$
       \partial_t\mathcal F=\partial_s\mathcal F=1.
$$
$[-1]s=-s$，故$\mathcal F(-s,s)=0$。
在完备正则环$k[[t,s]]$中，
$\mathcal F-t-s\in k[[t^p,s^p]]$；
换元$u=t+s$后，在$u=0$消失迫它被$u^p$整除。
因此存在整形式级数$E(t,s)$使
$$
       \mathcal F(t,s)
        =(t+s)\bigl(1+(t+s)^{p-1}E(t,s)\bigr).
                                                               \tag{CH3}
$$
对$1\le m\le p-1$，
$$
                 \mathcal F(t,s)^{-m}-(t+s)^{-m}
                                  \in k[[t,s]].               \tag{CH4}
$$
确实二项展开的第一差项具有非负指数$p-1-m$，
其余项更高。$m=p$也成立，因为它是$m=1$差式的$p$次方。
这不是把形式群当成加法群；只说明特定低极阶的差为正则函数。

记$L_m$为原§§83–85的有理函数，其唯一极主部为$s^{-m}$。
对$2\le m\le p$，取真正椭圆平移Hasse算子
$$
 h_n^{\mathrm{ell}}L_m(P)
       =[s^n]L_m(P+Q(s)).
$$
其可能的极只在$O$；由(CH4)，唯一主部为
$$
 (-1)^n\binom{m+n-1}{n}\,s^{-(m+n)}.
$$
所以它与相应倍数的$L_{m+n}$之差仅为常数。
若总$\mu_6$权$u^{-(m+n)}$非平凡，该常数准确为零：
$$
 h_n^{\mathrm{ell}}L_m
      =(-1)^n\binom{m+n-1}{n}L_{m+n}.
                                                               \tag{CH5}
$$
此式是全局有理函数身份，不仅是一个局部首项。

### 118.2 两个实际函数的全主部

先取$m=p-1$、$n=q+p$。$n$为偶数，
$m+n=q+2p-1\equiv4\bmod6$，所以常数为零。
Lucas逐位给
$$
 \binom{q+2p-2}{q+p}\equiv1\pmod p
$$
（上数的$p$进数字为$(p-2,1,1)$，下数为$(0,1,1)$）。
因此
$$
                  h_{q+p}^{\mathrm{ell}}L_{p-1}
                           =L_{q+2p-1}.                      \tag{CH6}
$$
这个证明包含所有形式群校正，不截掉可能的第二极项。

还需识别$h_NZ$。
通用扩张的真群律为
$Z(P+Q)=Z(P)+Z(Q)+m(P,Q)$，在$O$图$Z=V-y/x$。
对$n>0$，$h_nZ$不含原竖坐标，故来自底$E_1$。
它的Cauchy极部是$[s^n]\mathcal F(t,s)^{-1}$；
(CH4)的$m=1$情形准确给唯一主部
$(-1)^n t^{-n-1}$。
只要$u^{-(n+1)}$非平凡，全局常数亦为零。
对$n=N$，$N$奇且$N+1\equiv4\bmod6$，遂有
$$
                         h_NZ=-L_{q+2p-1}.                   \tag{CH7}
$$
真实弧$a(s)$的竖坐标高项只能影响这里的常数；
上述单位权已经将它完整消去，没有另选准周期。

### 118.3 CC0上的真正Frobenius运输

§113已证明
$$
              \iota^*F_2=2cL_{p-1},\qquad
       \iota(Q(s))=a(s^p)+(O,cs).
$$
取$F_2$的竖次数零同余格，得到
$$
 (h_{p+1}F_2)(\iota P')
      =2c\,h_{q+p}^{\mathrm{ell}}L_{p-1}(P')
      =2cL_{q+2p-1}(P').
$$
所有这些固定函数都在$\mathbf F_p$下降。
令$P=\operatorname{Fr}_pP'$，取真正$p$次幂则为
$$
 (h_{p+1}F_2)^p(\iota P')
                    =2cL_{q+2p-1}(P).
$$
另一方面，$h_NZ$来自底，故(CH7)给
$h_NZ(\iota P')=-L_{q+2p-1}(P)$。
这逐点证明(CH1)；在所有原$p'$挠抬升上当然成立，
因为它们属于这个真实椭圆核。

将(CH1)原样代回(CC1)，其中两个带$Z$的项完整相消，
即得(CH2)。不改变任何原$\bar\varepsilon$权、Tate源或周期。
§117的邻商推导仍正确，但第一式没有增加独立约束；
其另一外嵌入的$\mathcal H^{p-1}\mathcal L U_2$读者
仍须按真实全局身份继续归并，不能仅凭写法不同断言独立。
主目标和AQ全部共轭曲率接口仍未完成。

## 119. 原二、三挠分布的完整Belyi源与反δ输入

**已证明。** 原完整标记的两个真推除子零，
不仅给§115的$\delta$平移式，也使三个固定Kronecker函数的全迹
准确化为同一个有理对数微分。以下先在
$E_b:y^2=x^3+b$写式，原$E_1$取$b=1$。
令
$$
 g=y/x,\quad \widehat g=x^2/y,\quad
 \mathfrak h=x^3/y^2,\quad
 D=\omega^{-1}d,\quad \mathcal H=D-xJ .
$$
以$\mathscr L$表示原$\varepsilon$、$\bar\varepsilon$或整数$I_t$
的完整标记平移和；可随后在任一实际点评价。
若$\mathcal O$与真二挠、$\delta$挠平移交换，
则对$k=1,2,3$有
$$
 \boxed{\quad
 \mathscr L(\mathcal O F_k)
   =-6kb\,\mathscr L\!\left(
              \mathcal O\frac{Z^{k-1}}{xy}\right)
   =-k\,\mathscr L\!\left(
              \mathcal O\bigl(Z^{k-1}D\log\mathfrak h\bigr)\right).
 \quad}                                                       \tag{CI1}
$$
$F_1=Z$，$F_2,F_3$仍取原规范。
这是保全部标记及算子次序的身份；
没有把$\mathcal H-g$的幂误作平移不变算子。

### 119.1 两个真实分布及三行代数

原R298、§114已付
$[2]_*(\sum_t I_t[T_t])=[\delta]_*(\sum_t I_t[T_t])=0$；
两个原角色分量分别也如此。
规范素于$p$的挠抬升使这些同一除子关系在通用扩张上给
$$
 \begin{aligned}
 \mathscr L\left(V+\sum_{c^3=-b}\tau_{(c,0)}^*V\right)&=0,\\
 \mathscr L\left(V+\tau_R^*V+\tau_{-R}^*V\right)&=0,
             \qquad R=(0,\sqrt b).
 \end{aligned}                                                \tag{CI2}
$$
先在分裂域作这些恒等式，再按全标记和下降；
没有挑选其中一个父点或删去$I_t=0$的份。

二挠点的规范$Z$坐标为零。若
$m_c=y/(x-c)$，真实平移给
$$
 \begin{aligned}
 x'&=m_c^2-x-c,&
 y'&=-y+m_c(2x+c-m_c^2),&
 Z'&=Z+m_c .
 \end{aligned}
$$
且$\sum_c m_c=3x^2/y=3\widehat g$、$\sum_c c=0$。
逐项代入得到
$$
 \begin{aligned}
 \tau_c^*Z-Z&=m_c,\\
 \tau_c^*F_2-F_2&=2Zm_c+2x+c,\\
 \tau_c^*F_3-F_3&=3Z^2m_c+3Z(2x+c)+3y .
 \end{aligned}                                                \tag{CI3}
$$
最后一行的常数为$(c-x)m_c+4y=3y$，不能另加一个极项。

$\delta$两点则有$m_\pm=(y\mp\sqrt b)/x$，
$$
 \begin{aligned}
 \tau_{\pm R}^*F_2-F_2&=2Zm_\pm+2x,\\
 \tau_{\pm R}^*F_3-F_3&=3Z^2m_\pm+6xZ+3y\pm\sqrt b .
 \end{aligned}                                                \tag{CI4}
$$
把(CI3)–(CI4)送入(CI2)，保持$\mathcal O$作用在整个括号上，
即得二挠的三式
$$
 \begin{aligned}
 \mathscr L(\mathcal O\widehat g)
                  &=-\tfrac43\mathscr L(\mathcal OZ),\\
 \mathscr L(\mathcal O(\mathcal H-\widehat g)Z)
                  &=\tfrac23\mathscr L(\mathcal OF_2),\\
 \mathscr L(\mathcal O(\mathcal H-\widehat g)F_2)
                  &=\tfrac49\mathscr L(\mathcal OF_3)
                       -b\,\mathscr L(\mathcal O(1/y)).
 \end{aligned}                                                \tag{CI5}
$$
末式使用$x\widehat g=y-b/y$。
同样，$\delta$分布准确给
$$
 \begin{aligned}
 \mathscr L(\mathcal Og)&=-\tfrac32\mathscr L(\mathcal OZ),\\
 \mathscr L(\mathcal O(\mathcal H-g)Z)
                  &=\tfrac34\mathscr L(\mathcal OF_2),\\
 \mathscr L(\mathcal O(\mathcal H-g)F_2)
                  &=\tfrac12\mathscr L(\mathcal OF_3).
 \end{aligned}                                                \tag{CI6}
$$
现在$g-\widehat g=b/(xy)$。
第一行相减给$-1/6$，第二行相减给$-1/12$；
第三行中
$F_2/(xy)=Z^2/(xy)-1/y$，
所以两个$-b/y$项必须相消，剩系数$-1/18$。
又$D\log\mathfrak h=6(g-\widehat g)=6b/(xy)$，
于是得到(CI1)的全部三个准确常数。

这些式子对原$h_n,\mathcal H,J,\mathcal K,\mathcal L,\Xi$
及其已证整组合均可使用，因为它们与真实固定挠平移交换。
在普通反位的完整混合阶轨道上，
规范$(P,\mathcal E(P))-\widetilde T_t$也是真群平移，
所以同一式子保住全部轨道权；不能据此将任何单点迹置零。

### 119.2 同一个M的两条全Kummer乘积

这里必须仍用物理$T_t$而非不改$I_t$地换成$-T_t$。
§116已付
$$
 \prod_t\left(\frac{x(P-T_t)}{x(-T_t)}\right)^{I_t}=M(P)^{-3}.
$$
另由
$\operatorname{div}y=\sum_{R\in E[2]\setminus\{O\}}[R]-3[O]$
及(CI2)的真实二挠推零，乘积的除子为$-4\operatorname{div}M$。
在$O$归一，得到
$$
 \prod_t\left(\frac{y(P-T_t)}{y(-T_t)}\right)^{I_t}=M(P)^{-4}.
                                                               \tag{CI7}
$$
所有分母都是原标记的实际非零值。
在$E_1$，$1-\mathfrak h=1/y^2$；
故这两式完整给
$$
 \boxed{\begin{aligned}
 \prod_t\left(\frac{\mathfrak h(P-T_t)}
                  {\mathfrak h(-T_t)}\right)^{I_t}
        &=M(P)^{-1},\\
 \prod_t\left(\frac{1-\mathfrak h(P-T_t)}
                  {1-\mathfrak h(-T_t)}\right)^{I_t}
        &=M(P)^8 .
 \end{aligned}}                                                \tag{CI8}
$$
这些是特征零有理函数恒等式，故在每个允许点的所有$p^k$
Kummer张量中也精确成立。
它们比只比较$d\log$强，但没有增加额外独立的坏条件。

在实际双覆盖$\lambda^2=x$上，第二椭圆投影为
$$
                      Q(P)=(x^{-1},y/\lambda^3).
$$
逐式计算给
$$
                  \mathfrak h(Q(P))=1-\mathfrak h(P).           \tag{CI9}
$$
所以(CI8)确实把原两个全Kummer幂连接到第二投影的同一对函数。
这个投影不是$E_1$上的群同态，
不能把$Q(P-T_t)$换成$Q(P)-Q(T_t)$。

### 119.3 反δ差分显出真实的1/x输入

令$\mathscr D_\delta=\tau_R^*-\tau_{-R}^*$、$C=\sqrt b$。
$R$的阶为三，故
$$
 \mathscr D_\delta^2=\tau_R^*+\tau_{-R}^*-2,\qquad
 \mathscr L\mathcal O\mathscr D_\delta^2=-3\mathscr L\mathcal O .
$$
由(CI4)以及$Z$的群律逐项得到
$$
 \begin{aligned}
 \mathscr D_\delta Z&=-2C/x,\\
 \mathscr D_\delta F_2&=-4CZ/x,\\
 \mathscr D_\delta F_3&=-6CZ^2/x+2C .
 \end{aligned}
$$
再作一次$\mathscr D_\delta$，末行常数消去，因而
$$
 \boxed{\qquad
 \mathscr L(\mathcal O F_k)
    =\frac{2kC}{3}\,
        \mathscr L\left(\mathscr D_\delta\,
               \mathcal O\frac{Z^{k-1}}x\right),
       \qquad k=1,2,3 .
 \qquad}                                                       \tag{CI10}
$$
右边是原完整标记经过反$\delta$平移后的真实泛函。
在原三份父轨上，其偶分量保留$(-2,1,1)$型权；
不能删去父点，将它冒作裸$1/x$读者。
单独一次$\mathscr L\mathscr D_\delta F_k$的某些零由总奇偶自动产生，
与(CI10)的两次真实差分不可混淆。

### 119.4 普通倒数曲率的同一固定输入

为说明(CI10)确实出现所需固定函数，取普通$p=6n+1$，
$a=a_p(E_1)\ne0$，$\mathcal B=D-y/x$，并令
$\mathcal J_p(P)=\lambda(P)G(Q(P))$，
其中$G=D^{p-2}x$为§116的实际曲率函数。
$G$为奇函数，改变$\lambda$的符号也同时将$Q$变为$-Q$，
故$\mathcal J_p$确实下降为底$E_1$的有理函数。
由$DG=ax$及真实第二投影，
$\mathcal B\mathcal J_p=-a/x$。
在$\lambda^2=x$的函数域上，
$\mathcal B=\lambda D\lambda^{-1}$，故$\mathcal B^p=a\mathcal B$。
因此
$$
               \mathcal J_p+\mathcal B^{p-2}(1/x)\in\ker\mathcal B .
$$
写$h=(p-1)/2$。
$\ker\mathcal B=x^{-h}k(E_1)^p$，
因为$D(x^{-h})=(y/x)x^{-h}$。
在两个$\delta$点，上式两项极阶均至多$p-1$；
$\mathcal J_p$的极阶至多$h$，由实际$G(Q)$的$O$主部可见。
在$O$，$\lambda\sim\pm z^{-1}$，
而$\lambda^{-1}/x$正则且至少三阶，
所以$\lambda D^{p-2}(\lambda^{-1}/x)$至多简单极；
$\mathcal J_p$在$O$正则。
其它点均无极。

若上式为$x^{-h}F^p$，这些界迫$F$只可能在$O$有至多简单极。
椭圆曲线没有这样的非恒定函数，故$F$为常数。
两项均奇，而$x^{-h}$偶，所以常数为零，准确得到
$$
             \boxed{\quad
             \mathcal J_p=-\mathcal B^{p-2}(1/x).
             \quad}                                          \tag{CI11}
$$
没有先假设$\delta$的高阶极自动消失；
其消失是这个全局等式的结论。

(CI10)与(CI11)展示同一个固定$1/x$输入，
但原读者仍含全部反$\delta$标记、$Z^{k-1}$及平移不变算子，
而曲率用的是$\mathcal B^{p-2}$。
从这些完整原迹到AQ全部共轭曲率的转换仍须证明；
本节不把两个算子的输入相同当成该转换已经完成。

## 120. 真实邻商的倒数双覆盖与二阶位移

**已证明。** 原邻商的真实二阶位移确实含倒数点曲率，
但将它放回原完整椭圆单位时，这一项逐标记相消。
本节付出两个复合的实际差，不把它们误作相同，
也不从相消表达中另取一条不存在的独立坏条件。

### 120.1 移动三挠点与第二真投影

沿§117取任一好惰性$p>211$，在原六次同构后的
$E_0:y^2=x^3+1$上工作。先在特征$p$全族
$E_A:y^2=x^3+Ax+1$取导数，再截断至$A^3=0$。
此窗口中源$E_A^{(p)}=E_0$，
原邻商$\phi_A=-V_A$在$A=0$为真正相对Frobenius。

令$R_A=(r,e_A)$为原$R=(0,1)$的真三挠提升，
置$b=3r^2+A$、$L=e_A^2=r^3+Ar+1$。
三挠切线的三重相交给
$$
 b^2=12rL,\qquad
 3r^4+6Ar^2+12r-A^2=0,\qquad
 r=A^2/12+O(A^5).                                             \tag{CJ1}
$$
取$e_A\equiv1$。原完整点$T_t(A)=\phi_A(T_t)$
及整数权$I_t$作同一运输。
原除子$D_M=\operatorname{div}M$的三点分布
$D_M+\tau_RD_M+\tau_{-R}D_M=0$在整驯标记上成立，
推入真实邻商后仍成立。
因为
$\operatorname{div}(x-r)=[R_A]+[-R_A]-2[O]$，
比较除子和$O$值准确得
$$
 M_A(P)^{-3}=
 \prod_t
 \left(\frac{x(P-T_t(A))-r}{x(-T_t(A))-r}\right)^{I_t}.         \tag{CJ2}
$$
这里沿(BT1)的正$T_t$约定，不能只反转单个标记。
尤其二阶不能把$x-r$换回固定$x$。

在泛点取$\lambda_A^2=x-r$，写$X=\lambda_A^{-2}$、
$Y=y/\lambda_A^3$。实际第二商为
$$
 Y^2=LX^3+bX^2+3rX+1.
$$
置$X'=LX+b/3$、$Y'=LY$后得到短三次式，
其线性系数为
$3rL-b^2/3=-rL$，常数为
$B'=L^2-brL+2b^3/27=1+O(A^3)$。
用唯一$u=(B')^{1/6}\equiv1$规范
$(X',Y')\mapsto(X'/u^2,Y'/u^3)$，
真投影$Q_A$落在$E_{A^\vee}$，其中
$$
                   A^\vee=-rL/u^4=-A^2/12+O(A^5).             \tag{CJ3}
$$
至$A^2$时$u=L=1$、$b=A$，
但$r$的$A^2$项仍必须保留。
以上是在真实双覆盖函数域中的计算；
到$\lambda_A=0$处，下面的两复合不能未经核对就说成正则。

### 120.2 两复合的实际二阶群差

取源非分歧泛点$P=(x_0,y_0)$、
$\lambda_0^2=x_0$和
$Q=Q_0(P)=(x_0^{-1},y_0/\lambda_0^3)$。
记
$$
 x=x_0^p,\quad y=y_0^p,\quad\lambda=\lambda_0^p,\quad
 y'=y/\lambda^3,\quad Z=G_p(P).
$$
选择$\lambda_A$的泛点根使其在$A=0$为$\lambda$。
在$E_{A^\vee}$上取真正点差
$$
        D_A=Q_A(\phi_AP)-\phi_{A^\vee}(Q),
            \qquad D_0=O.
$$
不变微分给其唯一二阶形式群对数
$\log D_A=d_1A+d_2A^2$。

由(CG11)及§117对真实$V_A$已付的自然性，
在$A=0$有
$$
 Tx=(yZ+x^2)/3,\quad
 Ty=(x^2Z+xy)/2,\quad
 TZ=-(xZ+y)/6.
$$
求$T^2x$时还须对(CG11)的显式$A$系数求偏导；
这一项在$A=0$为$2/9$。
将其计入后准确得
$$
                 T^2x=(xZ+y)^2/6.
$$
设$u_1=(yZ+x^2)/3$、$v_1=(xZ+y)^2/12$，
于是$x_\phi=x+Au_1+A^2v_1$。
两个复合的横坐标分别为
$$
 X_C=x_\phi^{-1}+A/3+A^2/(12x^2),\qquad
 X_B=x^{-1}-A^2(y'G_p(Q)+x^{-2})/36 .
$$
若$\Delta_i=[A^i](X_C-X_B)$，直接展开给
$$
 \Delta_1=-yZ/(3x^2),\qquad
 \Delta_2=u_1^2/x^3-v_1/x^2+1/(9x^2)+y'G_p(Q)/36 .
$$
第二点$\phi_{A^\vee}(Q)$至$A^1$常值。
短Weierstrass群沿不变参数的横坐标展开因而给
$$
 d_1=\Delta_1/(2y'),\qquad
 d_2=\Delta_2/(2y')-\frac{3x^{-2}\Delta_1^2}{8y'^3}.
$$
用$y^2=x^3+1$、$\lambda^2=x$逐项归并，得到完整恒等式
$$
 \boxed{\quad
 \log D_A=-\frac{Z}{6\lambda}A
       +\frac{G_p(Q)+y'Z^2+2\lambda Z+y/\lambda}{72}A^2
          \pmod{A^3}.
 \quad}                                                       \tag{CJ4}
$$
特别在原真驯点$P_t$，有$G_p(P_t)=X(P_t)^p$。
若$\lambda_t^2=x(P_t)$、$Q_t=Q_0(P_t)$，则
$$
 72d_2(P_t)=G_p(Q_t)+
       \left(y(Q_t)X(P_t)^2
                   +2\lambda_tX(P_t)+y(P_t)/\lambda_t\right)^p.
                                                                  \tag{CJ5}
$$
所有系数都在原标记域及实际位取约化。
$\lambda_t$改号时$Q_t$和整条等式同时改号；
外部系数Frobenius也没有略去。

### 120.3 真分歧点的极与曲率逐项抵消

在原$\delta$两支$R_e=(0,e)$、$e=\pm1$，
$\lambda_0$是双覆盖局参，$G_p(R_e)=0$，
$dG_p=c_p\omega$且$\omega=\lambda_0d\lambda_0/y_0$。
所以
$$
 Z=\frac{c_p}{2e}\lambda_0^2+O(\lambda_0^3),\qquad
 d_1=-\frac{c_p}{12e}\lambda_0^{2-p}
                 +\text{较低极阶项}.
$$
在$Q=O$，规范严格坐标给
$G_p(Q)=s^{-p}+c_ps+O(s^{5p})$，
$x_Q^2/y_Q=-s^{-1}+O(s^5)$；
故$G_p(Q)+(x_Q^2/y_Q)^p$正则。
又
$$
          y/\lambda-(x_Q^2/y_Q)^p
                         =(\lambda_0^5/y_0)^p
$$
正则。因此(CJ4)的$d_2$真正最高极来自$y'Z^2/72$，即
$$
 d_2=\frac{e^p c_p^2}{288e^2}\lambda_0^{4-3p}
                       +\text{较低极阶项}.                  \tag{CJ6}
$$
这具体排除将整个双覆盖上的两次拉回之差
当作全局正则加法常数的做法。

最后必须把(CJ4)放回原(CJ2)。
去掉$A$常数后可对单位使用截断对数。
至二阶准确有
$$
                x_\phi-r=L/(X_C-b/3).
$$
将$\log(X_C-b/3)$拆为$\log(X_B-b/3)$与实际位移贡献。
从$X_B$的公式，前一项的$G_p(Q)$系数为
$-xy'G_p(Q)/36$；
从平移$2y'd_2$及$X_B(0)=1/x$，
后一项的相应系数为$+xy'G_p(Q)/36$。
二者在每个真实$P$处相消，且$xy'=g(Q)^p$，$g=y_Q/x_Q$。
固定原点归一和其它全部二阶项仍随(CJ2)的完整乘积运输，
不会恢复一个独立的倒数曲率项。

因此真实邻商位移确实含$G_p(Q)$，
却不能单靠(CJ2)就从原坏条件另推出这条曲率
或其标记全和为零。
这与§118的旧第五槽抵消是两个具体位置的核对；
两者均不得再次记作新的独立坏约束。
