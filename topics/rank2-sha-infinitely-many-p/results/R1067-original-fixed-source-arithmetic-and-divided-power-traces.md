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
