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
