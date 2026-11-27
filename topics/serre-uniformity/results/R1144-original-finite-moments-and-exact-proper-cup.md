# R1144：原有限 theta 矩、完整上同调比较与指定 proper 杯积

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 对每个 $p>37$，本文直接在实际非零 $p$-挠点上取有限 theta 矩，求出原 $\chi_1=\omega^{-2}$、$\chi_2=\omega^{-4}$ 两角色的完整 proper 杯积。没有除以 level $p$，也没有添加 Bernoulli 单位假设。关键是次数 $4,8,12$ 的完整几何上同调与实际尖点留数：这里不是仅从一维几何来源猜测绝对 $H^2$。

全文保持 R1070、R1138 的原函数与根相位。本文不构造四阶覆盖，不从一个杯积恒等式推断原有理点不存在。

## 1. 原对象和主等式

置
$$
p>37,\quad K=\mathbb Q(\zeta_p),\quad m=(p-1)/2,\quad
X=X_{\rm ns}^{+}(p),\quad
N(x,y)=x^2-\delta y^2,
\tag{1144.1}
$$
其中 $\delta\in\mathbb F_p^\times$ 是原固定非平方。令
$$
\chi_1=\omega^{-2},\qquad \chi_2=\omega^{-4},\qquad
\theta=\chi_1\chi_2=\omega^{-6}.
$$
$F_1=F_{\chi_1}$、$F_2=F_{\chi_2}$ 始终是 R1070 原 leading-normalized 函数类；其 divisor 是 $p$ 倍，故有原 proper Kummer 类
$$
A_i=\kappa(F_i)\in H^1(X_K,\mu_p).
$$
这两个角色均在原 forced 家族中；不另假设它们的 Bernoulli 数为单位。

使用 R1140 §§13–14 的实际圆单位类
$$
\epsilon_4=\sum_{b\in\mathbb F_p^\times}
 b^4\,\kappa(1-\zeta_p^b)\in H^1(K,\mu_p).
\tag{1144.2}
$$
指数解释于模 $p$ 类；需要实际函数时取整数提升。它的 $\Delta=\operatorname{Gal}(K/\mathbb Q)$ 角色是 $\omega^{-4}$。本文证明
$$
\boxed{\quad
 A_1\cup A_2
 =-\frac{8\delta^2}{11}\,A_1\cup\epsilon_4
 \quad\text{in }H^2(X_K,\mu_p^{\otimes2}).
 \quad}
\tag{1144.3}
$$
右边把常数类沿 $X_K\to\operatorname{Spec}K$ 拉回。

同一等式成立于 [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md) 的原 smooth proper 模型
$\mathscr X/\mathcal O_K[1/p]$。因此这是真正的 proper 等式，先于任何 Picard 商；不是只在函数域中相等。特别
$$
A_1\cup\left(A_2+\frac{8\delta^2}{11}\epsilon_4\right)=0.
\tag{1144.4}
$$
若 $a$ 是原圆单位所用的奇生成元，则 R1140 的原规范给
$$
\epsilon_4=\frac{\beta_{\chi_2}}{1-a^{-4}}.
\tag{1144.5}
$$
分母非零。式 (1144.3) 因而确定原第二槽所需的具体常数修正，而非只证明存在某个未定标量。

## 2. 完全有限的原 theta 矩

令 $\mathcal M=\mathcal M_{1,1,\mathbb Q}$，$\mathcal E/\mathcal M$ 为 universal elliptic curve，$\mathcal H=\mathcal E[p]$。记 $\mathbb F_p(t)=\mu_p^{\otimes t}$。在任一几何纤维上，Weil pairing 给
$\bigwedge^2\mathcal H\simeq\mathbb F_p(1)$。

选素数 $c>3$，使 $c\bmod p$ 为生成元。对 $d=4,8,12$，
$$
k_d(c)=c^2-c^{-d}\ne0.
\tag{1144.6}
$$
因为 $p-1>14$，不可能有 $c^{d+2}=1$。此处只用 Dirichlet 选素的存在性，未声称 $c<p$。

取 R1138 的同一 trace-fixed theta 类
$$
\operatorname{div}(\theta_c)=c^2[O]-[\mathcal E[c]].
$$
其 $\mathbb Z[1/30]$ 系数合法映入 $\mathbb Z_{(p)}$。若使用局部 Weierstrass/Hodge frame，单项的共同 frame 因子在以下有限矩中消去；不把有权的单个 division polynomial 叫作全局 weight-zero 单位。

令 $\pi:\mathcal E[p]\setminus O\to\mathcal M$，$P$ 为其 tautological point，定义
$$
\mathsf M_d=
 \frac1{k_d(c)}
 \operatorname{Cor}_{\pi}
 \bigl(P^d\otimes\kappa(\theta_c(P))\bigr)
 \in H^1(\mathcal M,\operatorname{Sym}^d\mathcal H(1)).
\tag{1144.7}
$$
这是所有有序非零 $p$-点的真 finite-étale corestriction。没有取除以 $p$ 的平均；局部 degree-$p$ orbit 也只作 transfer。纯幂采用通常 symmetric-power convention，所需 factorial 在 $p>37$ 时全为单位。

局部共同 base 类的系数是 $\sum_{P\ne0}P^d=0$：逐单项式求和即得，因 $0<d<p-1$。所以 (1144.7) 与原 theta 的无 frame 解释相合，也不会留下额外常数。

在原 full-level curve 上，R1138 (1138.2)、(1138.5) 精确给
$$
\boxed{\qquad
 \langle N^2,\mathsf M_4\rangle=2A_1,\qquad
 \langle N^4,\mathsf M_8\rangle=2A_2.
 \qquad}
\tag{1144.8}
$$
这里 $\langle N^{d/2},v^d\rangle=N(v)^{d/2}$。例如第一槽的原权是
$m^{-1}N(v)^2$，其 theta 和为 $2k_4(c)F_1/m$；乘回 $m/k_4(c)$ 正好得到 $2F_1$。另一槽相同。因此 (1144.8) 没有再多一个 $m$、$p-1$ 或半向量因子。

## 3. Tate 基与全部局部 transfer

### 3.1 惯性不变量与 coinvariant 分开

在 $K((q))$ 的 Tate curve 上取 $t^p=q$，令
$$
e_1=[t],\qquad e_2=[\zeta_p].
\tag{1144.9}
$$
$e_2$ 是 $\mu_p$ 方向，惯性不变；$e_1$ 是 $q$ 方向，其像生成 coinvariant。取几何惯性生成元 $u$：
$$
u(e_1)=e_1+e_2,\qquad u(e_2)=e_2.
$$
固定兼容的 $q$ 根后，$G_K$ 的 splitting 固定两者模 $p$，而在完整惯性上
$gug^{-1}=u^{\chi_{\rm cyc}(g)}$。因而
$$
H^1(I,\operatorname{Sym}^d\mathcal H(t))
 \simeq\mathbb F_p(t-1)\,[e_1^d].
\tag{1144.10}
$$
$e_1^d$ 本身的算术角色平凡；$-1$ Tate twist 来自惯性。这正是后文使用的 Galois 规范。

以标准 Tate pairing $e_p(e_2,e_1)=\zeta_p$ 固定相位。即使把基顺序交换，本文只用的偶数次 contraction $0,2,4$ 也不改变符号；尤其第四 contraction 的值为 $+\zeta_p^{\otimes4}$。

### 3.2 $\mu_p$ 线的共同 q 阶必须先消去

固定点为 $b e_2$，$b\ne0$。单个 $\theta_c(\zeta_p^b)$ **并非** $q$-单位：它有共同 $q$ 阶 $(c^2-1)/12$。此外 leading 中可以有共同 base/model 因子和 $\zeta_p^{A_cb}$ 相位。原 Tate product 给
$$
\operatorname{lc}\theta_c(\zeta_p^b)
 =C_c\,\zeta_p^{A_cb}
  \frac{(1-\zeta_p^b)^{c^2}}{1-\zeta_p^{cb}}.
\tag{1144.11}
$$
在 $b^d$ 加权和中，
$$
\sum_{b\ne0}b^d=0,\qquad \sum_{b\ne0}b^{d+1}=0
\quad(d=4,8,12).
$$
第一式分别杀共同 $q$ 阶和共同 leading；第二式杀实际 $\mu_p$ 相位。不能只用 augmentation 代替第二步。

重指标 $b\mapsto cb$ 后，这一整条固定线的贡献是
$$
\epsilon_d\,e_2^d,\qquad
\epsilon_d=\sum_{b\ne0}b^d\kappa(1-\zeta_p^b).
\tag{1144.12}
$$
所除的系数恰为 $k_d(c)$。特别 $d=4$ 时就是 (1144.2)，没有换圆单位规范。

### 3.3 非零 q 坐标的 degree-p orbit

其余点按 $a=1,\ldots,p-1$ 分成 orbit
$\{u^i(ae_1):0\le i<p\}$。代表是 $P_a=[t^a]$，定义于 $K((t))$。写
$$
ca=pr_a+s_a,\qquad 1\le s_a\le p-1.
$$
原 Tate theta product 给
$$
\theta_c(P_a)=C_a\,t^{k_c(a)}(1+t\,K[[t]]),
$$
其中
$$
\begin{aligned}
k_c(a)
 &=\frac p2\left(c^2B_2(a/p)-B_2(s_a/p)\right)\\
 &=ca r_a+\frac{c-c^2}{2}a
   -\frac p2(r_a^2+r_a)+\frac p{12}(c^2-1).
\end{aligned}
\tag{1144.13}
$$
所有指数均为整数；$c$ 奇且 prime to $6$。最后的共同项仍保留于公式，未在单个 orbit 上删去。

$1+t\cdots$ 在 $K((t))$ 中唯一 $p$-可除。常数 $C_a$ 的 transfer 系数是
$$
\sum_{i=0}^{p-1}u^i(ae_1)^d=0,
\tag{1144.14}
$$
因为每坐标是 $i$ 的次数至多 $d<p-1$ 的多项式。因此常数 Kummer 类，包括其中可能的 $\mu_p$ 相位，全部严格消去。

还须核算 arithmetic transfer，而不能只算惯性 residue。对 coset representatives $u^i$，$g\in G_K$ 的实际项为
$$
\frac{\chi_{\rm cyc}(g)-1}{p}
 \sum_{i=0}^{p-1}i\,u^i(ae_1)^d=0.
\tag{1144.15}
$$
该 prefactor 是 $\mathbb Z_p$ 整数；求和的次数至多 $d+1<p-1$，故模 $p$ 为零。这个式子来自 $g$ 对 $u^i$ 的共轭重指标，不是假设 $G_K$ 与完整惯性交换。

在 $u$ 上 transfer 先给 $u^{p-1}(ae_1)^d$。它与 $(ae_1)^d$ 的差属于 $(u-1)\operatorname{Sym}^d\mathcal H$，可减去一个在 $G_K$ 上为零的 coboundary。于是局部类具有表示
$$
\mathsf M_d=\mathsf R_d+\mathsf U_d,\qquad
\begin{cases}
\mathsf R_d(u)=v_d e_1^d,\quad \mathsf R_d(G_K)=0,\\
\mathsf U_d(g)=\epsilon_d(g)e_2^d,\quad \mathsf U_d(u)=0,
\end{cases}
\tag{1144.16}
$$
其中
$$
v_d=k_d(c)^{-1}\sum_{a=1}^{p-1}a^d k_c(a).
$$
$\mathsf R_d$ 真正从 $C_p$ quotient inflation 而来，因为 (1144.14) 也使 $u^p$ 上的 cocycle 值为零。这将排除下一节可能的 arithmetic ramified-cup 余项。

### 3.4 三个准确 residue 单位

令 $k=d+2\in\{6,10,14\}$。由 $s_a=ca-pr_a$，
$$
(c^k-1)\sum_{a=1}^{p-1}a^k
 \equiv kp\,c^{k-1}\sum_{a=1}^{p-1}a^{k-1}r_a
 \pmod {p^2}.
$$
Faulhaber 在这三个小次数上给
$\sum a^k\equiv pB_k\pmod{p^2}$。所有显示分母均为 $p$ 单位。代入 (1144.13)，其它项在加权后模 $p$ 消去，得到
$$
\sum_a a^d k_c(a)
 =(c^2-c^{-d})\frac{B_{d+2}}{d+2}\pmod p.
$$
故
$$
\boxed{\qquad
v_4=\frac1{252},\qquad
v_8=\frac1{132},\qquad
v_{12}=\frac1{12}.
\qquad}
\tag{1144.17}
$$
三个值对所有 $p>37$ 都非零。这是有限 degree-$p$ transfer 的 residue，未反除 transfer degree。

## 4. 几何 H¹ 与完整绝对 H² 的同构

设 $d=4,8,12$。对几何系数 $\operatorname{Sym}^d\mathcal H$，$-I$ 平凡作用，故可使用
$\operatorname{PSL}_2(\mathbb Z)=C_2*C_3$ 的有限系数 cohomology。两个非平凡 unipotents 的共同不变量为零：因 $d<p-1$，一个的 invariant 仅是一条纯幂线，另一个给另一条，交为零。因此 $H^0_{\rm geom}=0$。

对标准 $S$ 与 order-three $U$，固定空间维数如下：
$$
\begin{array}{c|ccc}
d&4&8&12\\ \hline
\dim(\operatorname{Sym}^d)^S&3&5&7\\
\dim(\operatorname{Sym}^d)^U&1&3&5
\end{array}
$$
$p\nmid6$，有限群的高 cohomology 为零。自由积的 Mayer–Vietoris 序列遂给
$$
\dim H^1(\overline{\mathcal M},\operatorname{Sym}^d\mathcal H)
 =(d+1)-\dim M^S-\dim M^U=1.
\tag{1144.18}
$$
这里是实际模 $p$ 计算，不从 characteristic-zero modular-form dimension 直接约模 $p$。

此外 $H^j_{\rm geom}=0$ 对全部 $j\ge2$ 成立。可直接用自由积，也可取 level $4$ 的 prime-to-$p$ étale cover：其几何底为 affine curve，$p$-cohomological dimension 为 $1$，degree 的素因子只有 $2,3$，有限群 descent 不添高 cohomology。复解析比较将上述有限系数计算识别为几何 étale cohomology。

实际 $\mathsf M_d$ 在几何 cusp 上的 residue 为 (1144.17) 的单位。故 (1144.10) 的 residue map 是一维空间之间的非零同态，即 Galois 等变同构
$$
H^1(\overline{\mathcal M},
       \operatorname{Sym}^d\mathcal H(t))
 \xrightarrow{\ \sim\ }\mathbb F_p(t-1).
\tag{1144.19}
$$
该 Galois 角色由原 Tate q-line coinvariant 得出，不能换成 $\mu_p$ invariant line。

现在对 $\mathcal M/\mathbb Q$ 使用 Hochschild–Serre。在总次数 $2$，几何 $H^0$、$H^2$ 都为零，只有 $(1,1)$ 项；进入或离开它的 differential 的几何 $H^0$ 项也为零。因此得到完整同构
$$
\boxed{\quad
H^2(\mathcal M,\operatorname{Sym}^d\mathcal H(t))
 \xrightarrow{\ \sim\ }
H^1(\mathbb Q,\mathbb F_p(t-1)).
\quad}
\tag{1144.20}
$$
它就是限制到 punctured Tate disk 后的惯性 edge。没有遗漏 base $H^2$、Picard 商或另一 HS graded piece。相同论证对 $K$ 成立；而 $\mathbb Q\to K$ 的 restriction 在这些模 $p$ 群上单射，因为 $[K:\mathbb Q]=p-1$。

## 5. 三个 contraction 的完整 cup 计算

由 Weil pairing 定义
$$
\Pi_r(v^4\otimes w^8)
 =e_p(v,w)^r\,v^{4-r}w^{8-r},
 \qquad r=0,2,4.
\tag{1144.21}
$$
通过 polarization 唯一线性延拓；其目标是
$\operatorname{Sym}^{12-2r}\mathcal H(r)$。所有 factorial 均为单位，故这些是实际模 $p$ sheaf maps。写
$$
C_r=\Pi_r(\mathsf M_4\cup\mathsf M_8)
 \in H^2(\mathcal M,
       \operatorname{Sym}^{12-2r}\mathcal H(r+2)).
$$

### 5.1 两个 ramified cocycles 的 cup 真正为零

对 $C_p=\langle u\rangle$，两个 $1$-cocycles $f,g$ 的 cup 在标准 cyclic resolution 中由
$\sum_{i=0}^{p-1}f(u^i)\otimes u^ig(u)$ 表示。取 (1144.16) 的 ramified 部分，则
$$
f(u^i)=v_4\sum_{j=0}^{i-1}(e_1+je_2)^4,\qquad
u^ig(u)=v_8(e_1+ie_2)^8.
$$
前者各坐标是 $i$ 的次数至多 $5$ 的多项式；与后者相乘后的次数至多 $13<p-1$。所有 $i\in\mathbb F_p$ 的 power sums，包括常数项之和，均为零。故 cyclic-resolution 代表本身为零：
$$
\mathsf R_4\cup\mathsf R_8=0.
\tag{1144.22}
$$
这是 $C_p$ 的真 $H^2$ 消失式，经 inflation 仍为零；不只是惯性 residue 为零。如此保留了 (1144.15) 所付的完整 arithmetic 转移。

### 5.2 唯一留下的 cross term

采用 $\operatorname{res}\{\text{unit},q\}=+\kappa(\text{unit})$ 的 cup–residue convention。

两个 unramified 项的 cup 在惯性 edge 为零。对
$\mathsf U_4\cup\mathsf R_8$，$\Pi_r$ 后仍有 $e_2^{4-r}$，除非 $r=4$；其它情形在 coinvariant 中为零。$r=4$ 时，(1144.9) 的原 pairing 给正号。另一 cross
$\mathsf R_4\cup\mathsf U_8$ 在所有 $r\le4$ 后仍有 $e_2$，所以均消失。

定义
$$
\gamma_5\in H^1(\mathbb Q,\mathbb F_p(5)),
\qquad
\gamma_5|_K=\epsilon_4\otimes\zeta_p^{\otimes4}.
\tag{1144.23}
$$
它存在且唯一：$\epsilon_4$ 的 $\Delta$ 角色为 $\omega^{-4}$，乘上 $\zeta_p^{\otimes4}$ 后为 invariant，且 restriction–corestriction 的 degree 为 $p-1$。

因此原局部计算给
$$
\operatorname{res}C_0=\operatorname{res}C_2=0,\qquad
\operatorname{res}C_4=v_8\gamma_5.
\tag{1144.24}
$$
利用 (1144.20)，前两式成为全局的 $C_0=C_2=0$。同时
$$
\operatorname{res}(\mathsf M_4\cup\gamma_5)=-v_4\gamma_5:
$$
这里 ramified 类在第一槽，故有负号。再次用同一个完整 $H^2$ 同构，得到
$$
\boxed{\quad
C_0=C_2=0,\qquad
C_4=-\frac{v_8}{v_4}\mathsf M_4\cup\gamma_5
   =-\frac{21}{11}\mathsf M_4\cup\gamma_5.
\quad}
\tag{1144.25}
$$
这一步没有假设 $\gamma_5$ 非零，也没有使用 $B_{p-5}$。

## 6. 原 norm 的完整 polarization 与两次 factor 2

令 $v,w$ 为任意两个向量，$D=\det(v,w)$。R1140 的整 polynomial identity 为
$$
\begin{aligned}
N(v)^2N(w)^4
={}&\frac1{495}[z^4]N(zv+w)^6\\
&-\frac{4\delta D^2}{77}[z^2]N(zv+w)^4
 +\frac{16\delta^2D^4}{21}N(w)^2 .
\end{aligned}
\tag{1144.26}
$$
它可直接展开核验；所有分母的素因子仅为 $3,5,7,11$。按通常 normalized polarization，
第一项是 $\langle N^6,\Pi_0(v^4\otimes w^8)\rangle$；第二项因
$\binom82=28$ 而为 $-(16\delta/11)\langle N^4,\Pi_2(\cdot)\rangle$。于是
$$
N^2\otimes N^4
 =N^6\circ\Pi_0-\frac{16\delta}{11}N^4\circ\Pi_2
     +\frac{16\delta^2}{21}N^2\circ\Pi_4 .
\tag{1144.27}
$$
没有额外奇 contraction 被默默设零；本式已经是指定左侧的完整恒等式。

拉到原 full-level curve，代入 (1144.8)、(1144.25)，得
$$
\begin{aligned}
4A_1\cup A_2
 &=\frac{16\delta^2}{21}\langle N^2,C_4\rangle\\
 &=-\frac{16\delta^2}{11}\,
          \langle N^2,\mathsf M_4\rangle\cup\epsilon_4\\
 &=-\frac{32\delta^2}{11}\,A_1\cup\epsilon_4.
\end{aligned}
$$
除以 $4$ 即为 (1144.3) 在 open full-level curve 上的等式。

原 determinant-one normalizer quotient 的 degree 是 $p+1$，为 $p$ 单位；这是 R1136、R1138 的同一实际 $H$。先在 quotient stack 上作 restriction–corestriction，再用 elliptic stabilizers 阶数为 $2,3$、均 prime to $p$，即得到原 coarse open $Y_K\subset X_K$ 上的等式。整个过程中未反除 degree 含 $p$ 的映射，也未改变原 norm/Weil frame。

## 7. proper 与算术模型上的准确回填

### 7.1 不能只在函数域或 open 曲线上停步

两个原 $A_i$ 本来来自 $H^1(X_K,\mu_p)$，常数 $\epsilon_4$ 也可拉回，因此 (1144.3) 的两侧都有指定 proper lift。

设 $\Sigma=X_K\setminus Y_K$。纯度序列说明
$$
\ker\!\left(H^2(X_K,\mu_p^{\otimes2})
        \longrightarrow H^2(Y_K,\mu_p^{\otimes2})\right)
 \subseteq\operatorname{im}
 \bigoplus_{s\in\Sigma}H^0(s,\mu_p).
\tag{1144.28}
$$
全部原 cusps 定义于实圆分域 $\mathbb Q(\zeta_p)^+$，所以复共轭固定 cusp 标签而在 $\mu_p$ 上作用为 $-1$。右侧整个 image 为 odd。两杯积均在 even 角色
$\theta=\omega^{-6}$，故该角色的 kernel 为零。由此原 open 等式唯一回填为 (1144.3) 的 proper 等式；没有留下可能非零的 cusp Picard 类。

### 7.2 $S=\operatorname{Spec}\mathcal O_K[1/p]$ 上不需要新的 Bernoulli 门

R1067 的原模型论证使 $A_1,A_2$ 延拓为 $\mathscr X/S$ 上的 $\mu_p$-torsors；(1144.2) 是 $S$-unit 类。这里完整沿用同一原归一，而非只延拓某个有相同几何 divisor 的函数。

R1142 §4 的下列段落独立于该篇后续 $B_{p-5}$ / DVR 假设：
$$
H^2(\mathscr X,\mu_p^{\otimes2})_\theta
 \xrightarrow{\ \sim\ }
 H^1(S,\mathcal J[p])_{\omega^{-7}} .
\tag{1144.29}
$$
为避免范围混淆，重列其所用事实。固定 $\zeta_p$ 识别一个 Tate twist 后，角色为 $\xi=\omega^{-7}$；$R^1f_*\mu_p=\mathcal J[p]$，$R^2f_*\mu_p=\mathbb F_p$，所以 top 项在 $\xi$ 上为零。$K$ 无实位且只有一个 $p$ 位，故 $\operatorname{Br}(S)=0$。Herbrand 与恒为 $p$ 单位的 $B_8=-1/30$ 给
$H^2(S,\mu_p)_\xi=(\operatorname{Pic}S/p)_\xi=0$。原 cusp section 使 base pullback 在 $H^3$ 单射，故进入 base 项的 Leray differential 为零。这些条件只用 $p>37$。

有限 étale sheaf 的 torsor 若在泛点平凡，则其 section 由正规性唯一延拓，因此
$$
H^1(S,\mathcal J[p])\longrightarrow H^1(K,J[p])
\quad\text{单射}.
\tag{1144.30}
$$
(1144.29) 与泛点 Leray edge 相容。若算术 proper 类在 $X_K$ 上为零，其 edge 经 (1144.30) 为零，故原类为零。因此
$$
H^2(\mathscr X,\mu_p^{\otimes2})_\theta
 \longrightarrow H^2(X_K,\mu_p^{\otimes2})_\theta
\quad\text{单射}.
\tag{1144.31}
$$
(1144.3) 遂在 $\mathscr X$ 上成立。没有使用 $p\nmid B_{p-5}$、$p\nmid B_{16}$ 或 $p\nmid B_{p-15}$，也没有把 field 等式绕过 Picard 障碍直接提升。

## 8. 原 SV 端点的精确值及原 I₈ 余项

原 $A_1$ 的 usual Hecke 特征为
$$
T_\ell A_1=(\ell^{-2}+\ell^3)A_1
\quad(\ell>3,\ \ell\ne p).
\tag{1144.32}
$$
可直接由 R1138 (1138.13) 的 physical 单槽关系及
$\widetilde T_\ell=\sigma_\ell T_\ell$ 得到；$H^1(X_K,\mu_p)$ 到函数域 Kummer 群单射，所以这是 proper 类的同一等式。与常数类的 cup 按 projection formula 相容，故 (1144.3) 的整个原杯积也满足所有这些 away-$6p$ Hecke 等式。下文只消费这一已付范围，不另断言 $\ell=2,3$ 的关系。

消费 R1140 §7 的准确对象
$$
\beta=\frac4{m^2}\{F_1,F_2\},\qquad
S_n=\frac{16\delta^2}{21}\Psi_n(c_E),\qquad
S_n=V_n\beta,
$$
$$
V_n=n^4-n^{-4}T_n+n^{-11},\qquad
v_n=n^{-11}(n^5-1)(n^{10}-1).
\tag{1144.33}
$$
选 primitive residue prime $n_0>3$，则 $v_{n_0}$ 非零。在原一维端点线上定义
$$
\Psi_E(c_E)=v_{n_0}^{-1}\Psi_{n_0}(c_E).
$$
R1140 的 compatibility 保证它不依赖 $n_0$。这里仅定义这一指定 eigenline 的 normalized smoothed value；不冒称没有 Bernoulli 门时存在整个 compact source 的 unsmoothing map。

(1144.3)、(1144.32) 现在给
$$
\beta_8=\beta-v_{n_0}^{-1}S_{n_0}=0.
\tag{1144.34}
$$
这只消去 R1140 中**这一指定 pair** 的实际 $I_8$ common-kernel 余项，不是一般 $I_8$ 块消失定理。原两角色自身的完整计算已替代本 pair 的 F33 混合门。

由 (1144.33) 和主等式，
$$
\Psi_E(c_E)
 =-\frac{42}{11m^2}\{F_1,\epsilon_4\}.
\tag{1144.35}
$$
R1143 的实际整比较已无条件给
$c_E=-2016\delta^2P_{\chi_1}$。其系数是单位，故
$$
\boxed{\qquad
\Psi_E(P_{\chi_1})
 =\frac1{132\delta^2}\{F_{\chi_1},\epsilon_4\}
 \quad\text{in }K_2(K(X))/p.
\qquad}
\tag{1144.36}
$$
从 (1144.35) 到 (1144.36) 使用
$42/(11\cdot2016\,m^2)=1/132$，因 $m^2=1/4$ 于 $\mathbb F_p$。
正号保留了 R1143 的负 Abel 号与本篇 ramified-first cup 的负号。

本文先证明 proper étale 等式，再由函数域 norm-residue 同构读为 $K_2/p$ 等式。(1144.36) 声明的是原 SV field target 的准确值；没有把其任意 field representative 另行指定为一个未知的 proper Picard lift。需要 proper lift 时，使用 (1144.3)、(1144.33) 中已经指定的原 Kummer-cup lift。

## 9. 范围及后继接口

本篇无条件确定同一个原两角色杯积和端点值。常数修正仍为原 $\epsilon_4$，不是事后任选的局部常数；全部 source/target、ordered point 权、Galois twist、finite transfer 及两次 factor $2$ 均已付清。

在 $p\nmid B_{p-5}$ 的范围内，R1142 另证明
$A_1\cup\beta_{\chi_2}$ 的 proper 类非零且为 socle。因此本篇系数为单位时，原未修正杯积的 proper 类同样非零；其函数域像是否为零仍由 R1142 的实际 MW/Pic 二分控制。这与修正后 (1144.4) 的 proper 零杯积不同，不能互相混用。

(1144.4) 可供实际 central-extension obstruction 使用，但本文不代替下一步的 torsor 构造、算术下降和连接性证明，更不把两输入的 Heisenberg 情形称为四阶覆盖。一般 forced pairs、全部高 cochains、真正同点辅助排除及 Serre 一致性的主门仍未由本篇解决。

## 10. 原来源与纸面核查

- R1070、[R1138](R1138-original-integral-bare-cup-smoothing-comparison.md)：原 theta/division-polynomial all-vector 类、leading 归一、完整 finite norm 与两槽系数。本文有限矩仅使用其 $p$-整版本。
- [R1140](R1140-original-low-weight-Manin-source-reduction.md)：原 polarization、完整 compact source、same-Weil Hecke、原 $\epsilon_4$ 及 $v_4,v_8$ 规范；本篇另以 (1144.13)–(1144.17) 自证有限 residue。
- [R1142](R1142-original-proper-Eisenstein-cohomology-and-Picard-dichotomy.md) §4：原算术 proper Leray 同构中不依 $B_{p-5}$ 的部分。
- [R1143](R1143-original-Eisenstein-lattice-and-exact-cuspidal-endpoint.md)：同一 $c_E=-2016\delta^2P_{\chi_1}$，包括 BM 整格、原 cusp divisor 与负 Abel 号。
- R. Sharifi、A. Venkatesh，*Eisenstein cocycles in motivic cohomology*，Compositio Mathematica 160 (2024), 2407–2479，[作者全文](https://www.math.ucla.edu/~sharifi/publ/eisensymbol.pdf)，§6.3 的实际 theta 类；Lemma 7.2.5 的 level-$4$/prime-to-$6$ cohomological-dimension 论证。没有消费 §7.2.6 的 level-prime 假设，也未将有理 $1/p$ Siegel 公式约模 $p$。
- 几何 cohomology、有限 cyclic cup、全 HS、polarization、proper 及算术回填均在本文逐项证明。函数域最后一步使用 Merkurjev–Suslin 的 $K_2/p$ norm-residue 定理；未以 $K_2[p]$ 结论代替它。

没有数学程序执行。局部 Cor/arithmetic 项、cyclic sum、contraction 的符号及 $\mu_p$ 线共同 q 阶已由 o2_high_coefficient 独立纸核；全文全局比较与原尺度另交 root/o2 按同一文本核阅。
