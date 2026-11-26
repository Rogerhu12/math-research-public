# R1038：原 p≡5 mod12 双中心 Raynaud 块与完整首对数

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
o1_theta / root；实际双中心与 CM 域边界另经 global_route 核对。

**已证明：对全部 $p\ge41,\ p\equiv5\bmod12$，原
$P=(p-1)D_0$ 在真实 Raynaud 良好部分的像有准确第
$m=(p-1)/2$ 层形式点和完整对数；同一个整最低型投影保留
该完整首向量。**
这里处理实际双中心、两个无穷远点及非平凡环面，
不把本行的整个 Jacobian 称为好约化。

原首对数为
$\varepsilon\sum_s\theta_s(\lambda(s)+R_p(s))f_s$；
本篇证明其对本行所有素数非零，不依赖有限窗口。
实际非 CM 简单商的 Néron 格、指定 MW 消去横截值和有理点排除
仍须另证。

## 1. 原对象和实际 Raynaud 位置

设
$$
p=12g+5\ge41,\quad m=(p-1)/2=6g+2,\quad h=m/2=3g+1,
\quad n=p+1,\quad e_0=mn,
$$
$$
R=W(k)[\pi_0],\quad \pi_0^{e_0}=p,\quad
\varepsilon=\pi_0^m,\quad \varepsilon^{p+1}=p.
\tag{1038.1}
$$
必要的标记经有限非分歧扩张取得，之后可作完美剩余域扩张。
$\sigma(\pi_0)=\xi\pi_0$，$\xi$ 阶为 $e_0$。
仍用原 $X_1,J_1,c_0,c_1,\delta,N,D_0$：
$$
N=1+\delta+\delta^2,\qquad
D_0=(3-N)[c_1-c_0],\qquad P=2mD_0.
$$
原三次扭曲在 $\mathbf Q_p$ 上由唯一的 $\sqrt[3]4$
解开；未更换六标记、Cartan 或点差。

用 R906/R921 的实际 Raynaud 扩张和周期格
$$
0\longrightarrow T\longrightarrow G\longrightarrow B\longrightarrow0,
\qquad
0\longrightarrow\Lambda\longrightarrow G^{\rm an}
                  \longrightarrow J^{\rm an}\longrightarrow0.
\tag{1038.2}
$$
$B/R$ 是原良好阿贝尔部分。
由原形式完备化，
$$
\widehat G\simeq\widehat{\mathcal J^0},\qquad
0\to\omega_B\to\omega_G\simeq\omega_{\mathcal J}
                      \to\omega_T\to0
\tag{1038.3}
$$
整正合，第一箭头饱和。R921 §2 已将它整地识别到原正规
半稳定曲线的相对对偶化微分，保留原 Abel 映射及下降。
本篇不重新假定任一商映射的 Hodge 拉回饱和。

## 2. 本行新增的二次局部类型必须保留

原 $\mathbb T_p^s$ 仍取 R1029 的 split-Hecke 完备整代数。
目标仍为
$$
\tau_1=\widetilde\omega_2^{p-1}
           \oplus\widetilde\omega_2^{-(p-1)}.
\tag{1038.4}
$$
R1029 的主同余导子界和有限 $N_{\rm ns}$ character 平均
对本行同样适用：正则 PS 仅保偶参数 $a$，正则 cusp
仅保奇参数 $r$。但此时 $p\equiv1\bmod4$，所以其 §2.2
中被上一行排掉的二次 Steinberg 固定线现在确实存在。
完整新增谱为
$$
\begin{array}{c|c|c}
\text{类型}&\text{Weil 惯性}&N_{\rm WD}\\ \hline
{\rm St}\otimes\epsilon_{\rm quad}&
       \epsilon_{\rm quad}\oplus\epsilon_{\rm quad}&\ne0\\
\text{二次 PS}&
       \epsilon_{\rm quad}\oplus\epsilon_{\rm quad}&0
\end{array}
\tag{1038.5}
$$
其中
$\epsilon_{\rm quad}|_{I_p}=\widetilde\omega^{\,m}$。
这与小参数 $\varepsilon=\pi_0^m$ 是不同记号。
有限一维二次 determinant character 仍无正规化子固定向量；
二次 PS 的固定方向来自有限
${\rm St}\otimes\epsilon_{\rm quad}\det$ 部分。
原平凡球面旧型仍由 $S_2(H_6)=0$ 排除。

正则类型的 Savitt 剩余列表与碰撞核对沿用 R1029
(1029.8)–(1029.10)，额外可能参数仍是被奇偶性排除的
$r=2$、$a=1$ 或已处理的 $a=0$。
只须核 (1038.5) 不与 $\tau_1$ 剩余惯性相撞。

对二次 PS，先去掉真实二次角色，得到 Hodge–Tate 权
$\{0,1\}$ 的 crystalline 表示。Fontaine–Laffaille 的
简单对象和惯性数字给两种半单化：
$\{1,\omega\}$ 或 $\{\psi,\psi^p\}$；
二次 twist 后因此为
$$
\{\omega^m,\omega^{m+1}\}
\quad\text{或}\quad
\{\psi^{e_0+1},\psi^{e_0+p}\},
\qquad \omega=\psi^{p+1}.
\tag{1038.6}
$$
允许任意稳定整格，因为剩余半单化不随格改变。
所用分类是 FL Proposition 4.4、Theorem 5.3 及 §§7–8
的 crystalline 比较在两维权 $0,1$ 的直接应用。

二次 Steinberg 去 twist 后 semistable 且非 crystalline。
其 rank-one $N_{\rm WD}$ 和 $N\varphi=p\varphi N$
使 Frobenius 两斜率为 $0,1$；行列式固定 cyclotomic。
$\ker N$ 的斜率为零，弱可容许性迫其 Hodge 权为零，
所以给未分歧一维子表示，商为 cyclotomic 乘未分歧角色。
故只产生 (1038.6) 的第一对，而无额外剩余类型。

目标的三种可能仍是
$$
\{1,\omega\},\quad
\{\psi^{2p-1},\psi^{2-p}\},\quad
\{\psi,\psi^p\}.
\tag{1038.7}
$$
第一对与 (1038.6) 的 ordinary 对显然不同。
其 niveau-two 对与 $\{\psi,\psi^p\}$ 相等会迫
$e_0\equiv0$ 或 $\pm(p-1)\bmod(p^2-1)$，不可能。
与另一对比较时，所有可能差除以 $p-1$ 分别为
$$
(p-3)/2,\ (p+3)/2,\ (p-1)/2,\ (p+5)/2;
$$
它们严格在 $0$ 与 $p+1$ 之间，均不是所需的零余数。
ordinary 与 niveau-two 也不能混同。

因此 R1029 §4 的真实 maximal-ideal 分离证明逐步适用：
split 本征值相同模剩余位给 $G_{\mathbf Q(\sqrt{-3})}$
剩余半单化相同，而 $I_p$ 包含其中；上述不相交排除一个
maximal factor 同时承载目标及补型。得到真正整幂等元
$$
\boxed{\quad e_1\in\mathbb T_p^s,\qquad e_1^2=e_1.\quad}
\tag{1038.8}
$$
没有把 (1038.5) 从原 canonical 谱中漏掉。

## 3. 双中心、图作用与真正良好 BT 因子

Edixhoven–Parent Theorem 3.3 的本行实际模型有两个
$\mathrm{Ig}(p)/C_4$ 中心 $I_+,I_-$。
原 fine Hasse 的简单零使 Igusa cover 的局部惯性达到全阶，
故这两个原中心各自连通；取同一 $H_6$ 商仍保持连通。
generic 尾与 CM 支持尾分别为
$$
D_s:\ Y^2=X(X^{(p+1)/2}+A_s),\quad \operatorname{genus}=h,
$$
$$
D_\xi:\ y^2=x(x^{(p+1)/6}+A_\xi),\quad
       \operatorname{genus}=g.
\tag{1038.9}
$$
本行两式均有两个无穷远点。
原 $\pi_0$ 底环上的节点厚度分别为 $2$、$6$，
与 EP Theorem 3.5 (26) 及原 $H_6$ 的实际稳定子相容。
$j=1728$ 在本行是 ordinary，不属于下文的 SS 根集；
$b=0$ 则仍是一个非支持的实际 SS 点。

R910 §2 在原 full-six 模型上已算出的完整惯性为
$$
(X,Y)\longmapsto(t^2X,tY),\qquad
t=\xi^m\in\mu_{p+1}.
\tag{1038.10}
$$
因 $(p+1)/2=2h+1$ 为奇数，
$Y/X^{h+1}$ 在完整生成元作用下改变符号。
故该元素交换两个无穷远点及两个中心，同时固定尾的标号。
图中的每条连接路径被反向，所有图 $H_1$ 的角色均为
$-1=\xi^{e_0/2}$。正规细分与收缩不改变此 $H_1$。

Raynaud 函子性把这个作用传到 $T,\Lambda$。
其二次 Weil 惯性与 $\tau_1$ 不同，所以 $e_1$ 在
$T_pT$ 和 $\Lambda\otimes\mathbf Z_p$ 上为零。
真实无挠格和 finite-flat 延伸使这些消失是整的。
在 fppf 正合列
$$
0\to T[p^a]\to G[p^a]\to B[p^a]\to0
$$
施以幂等元并取相容极限，得到
$$
\boxed{\quad
\mathcal G_1:=e_1G[p^\infty]\ \simeq\ e_1B[p^\infty].
\quad}
\tag{1038.11}
$$
它的 generic Tate 表示正是 $e_1V_pJ$，周期格没有遗漏。
这是实际良好 BT 直和因子，不要求 $e_1$ 是某个
$\mathbf Q$-简单商的有理投影。

完整 Hodge 权可从 (1038.10) 和 R910 §3 直接读取：
$$
m(2j+1)\ (0\le j<h),\qquad
3m(2j+1)\ (0\le j<g),
\tag{1038.12}
$$
分别来自 generic 和 CM 尾。
Igusa 权为 $p+1$ 的倍数，且没有零权：双中心并的
全惯性商是 $\mathbf P^1_b$，其 $H^1(O)$ 为零。
若保留整个 $G$，环面另给权 $e_0/2$。
于是所有实际形式权均满足
$$
m\le w_i<e_0-m=pm,
$$
权 $m$ 恰来自全部 generic SS 尾的最低一对，
权 $-m$ 不在 Hodge 空间。

在先取得 (1038.11) 后作实际 crystalline-descent 比较，
便与 R1029 §5 一样得到
$$
(e_1\omega_B)\otimes k=(\omega_B\otimes k)_{w=m}.
\tag{1038.13}
$$
块内同权提升模 $p$ 唯一：
取权 $m$ 整基后，同特殊纤维提升的差系数为惯性不变量，
属于 $W(k)$ 且模 $\pi_0$ 为零，因此属于 $pW(k)$。
两次 PD 的 R1035 比较也适用于这个实际良好 BT，
但不据此称整个 $J$ 良好。

## 4. 原 $P$ 的 multidegree、bounded lift 与准确形式首层

在三个原 CM 支持标号 $\xi=1,\zeta,\zeta^2$ 上写
$$
a_1=2,\qquad a_\zeta=a_{\zeta^2}=-1.
$$
每个中心到原 $\mathbf P^1_b$ 的次数为 $h=m/2$，
且原 ordinary forgetful map 为 $a=b^p$；
$[p]$ 对六标记的共同 $-I$ 已在原 $H_6$ 中处理。
每个支持点在两个中心上都唯一且全分歧：
原 Hasse 简单零及 $\gcd(h,3)=1$ 给该结论。
置
$$
G(b)=\frac{(b-1)^2}{b^2+b+1}.
$$
于是
$$
\operatorname{div}_{I_\pm}G
    =h\sum_\xi a_\xi s_{\xi,\pm}.
\tag{1038.14}
$$

在原厚度六的支持尾上取 vertical twister 系数
$6ma_\xi$，两个中心系数零，其余尾系数零；
正规细分链的系数以整数步长 $ma_\xi$ 插入。
因为
$$
\operatorname{div}_{D_\xi}x
   =2Q_\xi-\infty_+-\infty_-,
$$
经此原 twister 调整后，$P=2mD_0$ 的分量除子为
$$
ma_\xi(2Q_\xi-\infty_+-\infty_-)
\quad\text{在 }D_\xi,
\qquad
m\sum_\xi a_\xi s_{\xi,\pm}
\quad\text{在 }I_\pm.
\tag{1038.15}
$$
它们分别由 $x^{ma_\xi}$、$G^2$ 主化；
其余分量为零，且中心总度为零。
故 $P\in\mathcal J^0(R)$，它在特殊 $B_k$ 中的像为零。
双中心图可能留下环面 clutching，本篇没有把该点直接宣布
为整个 $J$ 的形式零点。

由 (1038.3)，$P$ 有唯一 bounded lift
$P_G\in G(R)$。亦可先在严格非分歧底域构造；
周期格的 tropical monodromy 配对正定，使
$\Lambda\cap G(R)=0$，因此唯一性使它下降。
其 $B$ 像 $P_B$ 是实际形式点，约化为零。

$\overline{P_G}$ 位于 $T_k(k)$，且所有数据定义于有限剩余域，
故它的阶 $r_0$ 素于 $p$。
取 $T(R)[r_0]$ 中唯一具有该约化的 Teichmüller 点 $\tau$，
则
$$
\widetilde P=P_G-\tau\in\widehat G_0(R),\qquad
\pi_B(\widetilde P)=P_B.
\tag{1038.16}
$$
唯一性保留原下降，且 $\log\tau=0$。
**不定义 $e_1\tau$**：$p$-进完备 Hecke 幂等元无需
作用于这个素于 $p$ 阶挠点。
只在减去它后的实际形式点及 $B[p^\infty]$ 上施以 $e_1$。
其在形式环面上的作用为零，故所得只依赖 $P_B$。

在 (1038.12) 的整 character 参数中，
$\sigma(\widetilde P)=\widetilde P$ 迫各坐标估值至少为对应
正权 $w_i$。因此
$$
P_B\in F^mB(R),\qquad e_1P_B\in F^m\mathcal G_1(R).
\tag{1038.17}
$$
这里 $F^j$ 表示原形式参数在 $\pi_0^jR$ 的点。

### 4.1 两节点的原 quotient-Hasse 单位相同

在非支持 SS 尾 $s$ 上，保原 trace-zero
$Q_{\rm level}=\sqrt{-3}P_{\rm level}$。
记 $s_0=\sqrt{-3}\in\mathbf F_{p^2}$，
$\alpha=T(P_{\rm level})/\varpi$、
$\beta=T(Q_{\rm level})/\varpi$，$\varpi^2=\pi_0$。

两个 ordinary charts 分别对应
$E/\langle Q_{\rm level}\rangle$ 与
$E/\langle P_{\rm level}\rangle$。
原同源的 norm derivative 与 Hasse 简单零给其实际参数
$$
b_{{\rm lift},+}-s=\varepsilon\theta_s\beta^{p-1}+\cdots ,
\qquad
b_{{\rm lift},-}-s=\varepsilon\theta_s\alpha^{p-1}+\cdots ,
\tag{1038.18}
$$
其中是**同一个**原 $\theta_s\in k^\times$。

核这一次同号而不任意归一：在原 Cartan eigenvariables
$A_0=\beta+s_0\alpha,\ B_0=\beta-s_0\alpha$ 中，
惯性取 $u=s_0$ 的 norm 为 $3$，在本行是非平方，
故交换两个中心。原完整作用给
$$
(A_0,B_0)\mapsto(-A_0,B_0),\qquad
(\alpha,\beta)\mapsto(-\beta/s_0,-s_0\alpha).
$$
同时 $\varepsilon\mapsto-\varepsilon$，
$\beta^{p-1}\mapsto-\alpha^{p-1}$，
故两负号消去。两个实际同源方向互换，六标记相同，
从而原 quotient-Hasse 单位相同。
在中心稳定子的精度 $0<j\le m<p+1$ 内，
非零修正需 $(p+1)\mid j$，所以没有遗漏另一同阶中心项。
尾在 $0<j<m$ 亦无允许惯性层；第 $m$ 层的 regular
frame 改动仅改变 Čech coboundary。

### 4.2 真正的双节点类及残数

设 generic 尾 $D_s$ 的
$$
M=(p+1)/2=2h+1,\qquad A_s=(a^*)^2,
$$
$$
A_0^{p+1}-B_0^{p+1}=2a^*,\quad
U=A_0^{p+1}-a^*,\quad V=A_0B_0,\quad
X=V^2,\quad Y=UV.
$$
在两个无穷远点取 $z=X^{-1}$，则
$$
Y=\pm z^{-h-1}S(z),\qquad S(z)^2=1+A_sz^M,\qquad S(0)=1.
$$
(1038.18) 的原 descended germs
$\psi_+=\beta^{p-1}$、$\psi_-=\alpha^{p-1}$
的负主部准确为
$$
\psi_\pm=\pm z^{-h}S(z)^{-1}
       \quad\text{模各节点的 regular 函数}.
\tag{1038.19}
$$

为核不是错误的分数幂替代，置 $W=V^{-1}$、$z=W^2$、
$w=W^M$。在 $A_0/B_0=R_+$ 接近 $1$ 的节点，
$R_+^M=S+a^*w$，而 $R_+^p\equiv1\bmod w^p$。
故 $R_+=(S+a^*w)^2+O(w^p)$，
$$
\frac{1-R_+}{1+R_+}
       =-\frac{a^*w}{S}+O(w^p),\qquad
\beta^{p-1}
       =\frac{U+a^*(1-R_+)/(1+R_+)}{V}.
$$
这给 (1038.19) 的正号。
另一个节点置 $R_-=-A_0/B_0$ 接近 $1$；
由于 $M$ 为奇数，$R_-^M=S-a^*w$。
同一有限计算及 $s_0^{p-1}=-1$ 给负号。
误差阶至少 $W^{Mp-2h}>0$，因此不改变负主部。
只取所需有限精度，没有在特征 $p$ 中定义任意无限二项级数。

令 $f_s$ 为这个**双节点 pair** 的 Čech 类。
对尾的全部 holomorphic basis
$\omega_{s,j}=X^j\,dX/Y$、$0\le j<h$，两端分别为
$$
\omega_{s,j}=\mp z^{h-j-1}S(z)^{-1}dz.
$$
(1038.19) 与它相乘，在每端的残数是
$-1$ 当 $j=0$，否则为零，因为 $j<h<M$。
故原 Serre 配对为
$$
\langle f_s,\omega_{s,0}\rangle=-2,\qquad
\langle f_s,\omega_{s,j}\rangle=0\ (j>0).
\tag{1038.20}
$$
这是一个非零原底 gap；不是将两个独立类相加后再乘二。

用 (1038.15) 的实际 frame，两个中心均由 $G^{-2}$ 主化，
非支持尾取相应常数 frame。
去掉 (1038.16) 的常数 clutching 后，按 R1018 的原
transition 方向展开 $G^2$，得到
$$
P_B\equiv
 \varepsilon\sum_{s\in S}\theta_s\lambda(s)f_s
       \pmod{F^{m+1}},\qquad
\lambda=2G'/G=-\frac{6(b+1)}{1-b^3}.
\tag{1038.21}
$$
在真实 $s=0$ 分量上系数为 $-6\theta_0\ne0$；
其他尾或环面不能抵消 $B_k$ 的这个直积分量。
所以 (1038.17) 的形式深度准确为 $m$，
且 $e_1$ 保留该层。
本篇接着计算完整 log，未把 (1038.21) 当作 log。

## 5. 全非约化节点与双端的同一次 Frobenius 消去

R1021 的 full-$p$ affine 模型与刚性本来对所有
$p\equiv2\bmod3$ 有效，故仍在整个 $R/(p)$ 中适用。
在实际同源变形环，取真实微分乘子 $v,w$，满足 $vw=p$；
原 target eigenparameter 仍有准确形状
$$
u'=vA(p,v^{p+1})+w^pB(p,w^{p+1}),
\qquad A(0,0)\in W^\times.
\tag{1038.22}
$$

本行原节点为 $R[[z,w_I]]/(zw_I-\rho\pi_0^2)$。
它是正常 Krull 环，通常不是 UFD，不能照搬上一行的 UFD 句子。
实际 $v$ 无水平零，尾上阶 $m$、中心上阶零；
而 $w_I$ 的 Weil 除子为尾的二倍。
因此
$$
\operatorname{div}(v)=mD,\qquad
\operatorname{div}(w_I)=2D,\qquad
v/w_I^h\in R[[z,w_I]]^\times .
$$
最后一步用正常环为 height-one DVR 的交：
该比值及其逆均无任何 height-one 极点。
只对这个单位开 Hensel $h$ 次根，再把原 $\rho$ 吸收到
节点坐标，得到
$$
v=W^h,\qquad ZW=\pi_0^2,\qquad v/\varepsilon=Z^{-h}.
\tag{1038.23}
$$
实际单位保存在 (1038.18) 的原参数比较中，并未设 $\theta_s=1$。
(1038.22) 的后续项在所需 Laurent 精度中均含 $p$，
因为 $v^{p+1}/\varepsilon^{p+1}=Z^{-h(p+1)}$，
且 $w^p/\varepsilon=p^{p-1}Z^{hp}$。
结合原 affine 刚性，可取原类的整 cocycle 规范为
$$
t_{s,\pm}=c_s\varepsilon\psi_\pm\pmod p
\tag{1038.24}
$$
于两个实际 Laurent 重叠。

两端的 Frobenius 使用**同一个** affine 0-cochain。
在原 full-$p$ 图上置
$$
C_s=\alpha^p\beta-\alpha\beta^p,\qquad
\mathcal D_s=
\frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}{C_s}.
$$
真实线性化多项式恒等式
$$
\prod_{a,b\in\mathbf F_p}(T-a\alpha-b\beta)
 =T^{p^2}-\mathcal D_sT^p+C_s^{p-1}T
$$
分别代 $T=\beta,\alpha$，给
$$
\psi_+^p=\mathcal D_s-C_s^{p-1}/\psi_+,\qquad
\psi_-^p=\mathcal D_s-C_s^{p-1}/\psi_- .
\tag{1038.25}
$$
$\mathcal D_s$ 与 $C_s^{p-1}$ 都是实际 level 群不变量；
前者是 quotient affine 尾的全局 regular 函数。
因此 $f_s^p$ 的两个 annular cochains 同时减掉单个
$\mathcal D_s$，不留下两个不同消去函数之间的图常数。

写实际参数变换 $b=B_s(t)=s+a_st+b_{2s}t^2+b_{3s}t^3+\cdots$，
$\theta_s=c_sa_s$。
两个中心均以同一个
$$
R_s^*(b)=\frac{C_s^{p-1}\theta_s}{b-s}
$$
消去主部。返回任一目标尾的两端恰组成同一个 $f_t$；
故原 $2m$ 层矩阵是
$$
K_{ts}=-\frac{C_s^{p-1}\theta_s\theta_t}{(t-s)^2}\quad(t\ne s),
\qquad
K_{ss}=\frac{C_s^{p-1}\theta_s^2}{6}
                 \frac{s(s^3+7)}{2(1-s^3)^2}.
\tag{1038.26}
$$
对角项来自同一个 $B_s$ 的完整 Schwarzian：
$b_{2s}^2/a_s^2-b_{3s}/a_s
=a_s^2\operatorname{Schwarzian}(t;b)(s)/6$。
原 GM 三阶比较仍只除 $1,2,3$，详见 R1023 §4。
没有把两个中心返回矩阵相加。

精度不超过 $2m$ 时，Igusa cohomology 的同阶角色只可能
要求中心零权，而它已在 §3 排除。
图角色 $e_0/2$、支持尾角色与高 gap 同样不能进入这一层。
整 cocycle 提升差的 Frobenius 至少含
$\pi_0^p=\pi_0^{2m+1}$；
目标高阶基变换乘已在第 $2m$ 层的矩阵，也不改其首层。
所以 (1038.26) 是完整非约化 $R/(p)$ 上所需矩阵的准确首层，
不止特殊点矩阵。

## 6. 完整首 log：所有分母与唯一 degree-$p$ 返回

在实际 $B$ 的整形式参数中，formal log 的次数 $j$ 项
分母至多 $p^{v_p(j)}$：对该项沿每个参数微分，得到整不变微分；
所有次数指数的共同 $p$-因子至多为 $p^{v_p(j)}$。
先用线性部恒等的整 character 变换消去次数
$2,\ldots,p-1$，不改 (1038.21)。

写次数 $p$ 的 log 与 $[p]$ 部分为 $B_p,M_p$。
同一原形式群中比较 $L([p]Z)=pL(Z)$，准确得到
$$
M_p=(p-p^p)B_p,\qquad
pB_p=M_p/(1-p^{p-1}).
\tag{1038.27}
$$
次数 $p$ 的 mixed 单项式在 $M_p\bmod p$ 中为零，
因为 $[p]=V\circ\operatorname{Fr}$；故其 log 系数整，
代入原点后至少为第 $pm>m$ 层。
下面的单输入权预算只针对 pure- $p$ 次项。

整个非约化 $R/(p)$ 上，Picard 的 $[p]$ 由 line-bundle
transitions 的 $p$ 次幂和相对 Frobenius 给出；
投到实际 $B$ 后仍为同一诱导映射。
故 $M_p\bmod p$ 的纯 $p$ 次项就是上述真实 Hasse–Witt
矩阵，不是另取特殊点的任意提升。

次数 $j>p$ 的项在原点至少为
$$
jm-e_0v_p(j)>m.
$$
当 $v_p(j)=1$ 用 $j\ge2p$；
当 $v_p(j)=a\ge2$ 用 $p^a-a(p+1)>1$；
无分母时直接成立。
degree-$p$ 的输出权 $w_i$、输入权 $w_j$ 的系数角色
为 $w_i-pw_j\bmod e_0$。
因 $m\le w_i<pm$，除 $p$ 后每项至少位于第 $w_i$ 层；
若输出 $m$ 而输入 $>m$，则
$pw_j>e_0+m$，不能进入第 $m$ 层。

因此只有底到自身的
$\varepsilon^2K+O(\pi_0^{2m+1})$ 与线性项同阶，
并且 $\varepsilon^{p+1}=p$ 给准确首向量
$$
\log_B(P_B)\equiv\varepsilon(v+Kv^{(p)})
                       \pmod{\pi_0^{m+1}},
\qquad v_s=\theta_s\lambda(s).
\tag{1038.28}
$$
这一预算也解释为什么第一形式层非零不直接等于完整 log 非零。

## 7. 原 Hasse 因子、真实尺度与完整 rational remainder

仍保原 auxiliary family 和微分
$$
E_b:\ y^2=x^3+3brx+r(1-2b^3),\qquad
r=1-b^3,\qquad \omega=dx/(2y).
$$
其真实 Hasse 为
$$
h_p(b)=[x^{p-1}]
 \bigl(x^3+3brx+r(1-2b^3)\bigr)^m
       =r^{2g+1}A_p(b),
$$
$$
A_p=bQ_p(b^3),\quad A_p,Q_p\text{ 单首},\quad
\deg A_p=6g+1=(p-3)/2,\quad \deg Q_p=2g.
\tag{1038.29}
$$
直接在原展开中，三项指数满足
$$
3g+1\le i\le4g+1,\quad
j=12g+4-3i,\quad k=2i-6g-2.
$$
最小 $r$ 次数 $2g+1$ 只在
$(i,j,k)=(4g+1,1,2g)$ 出现，系数非零。
最高 $b$ 系数由
$(X-1)^{p-1}(X+2)^m$ 的 $X^{p-1}$ 系数给出，
为 $3^m=-1$，恰与 $r^{2g+1}$ 的最高系数相同；
所以 (1038.29) 保留准确的 monic 规范。

原 GM 和 Hasse 方程是这个固定 family 的恒等式：
$$
\nabla\omega=\frac{b^2}{2r}\omega+\frac1{2r}\eta,\qquad
\nabla\eta=\frac b2\omega-\frac{b^2}{2r}\eta,\qquad \eta=x\omega,
$$
$$
h_p''-\frac{3b^2}{r}h_p'
 -\frac{b(5-4b^3)}{4r^2}h_p=0.
\tag{1038.30}
$$
因 $2g+1=(p+1)/6\equiv1/6\bmod p$，代入得
$$
rA_p''-4b^2A_p'-\frac94bA_p=0,
$$
$$
x(1-x)Q_p''+\frac43(1-2x)Q_p'-\frac{25}{36}Q_p=0.
\tag{1038.31}
$$
次数小于 $p$ 的合法 Taylor 递推排除 $r\ne0$ 处共同根
$A_p=A_p'=0$。因此 $S=\{A_p=0\}$ 正是全部非支持的
原简单 SS 点，且 $S\cap\{r=0\}=\varnothing$。
同一递推和单首系数给
$$
Q_p(0)Q_p(1)\ne0,\qquad Q_p(1-x)=Q_p(x).
\tag{1038.32}
$$
这里是偶次数的正号；后面只用反射平方不变。

全部 $s\in S$ 仍在 $\mathbf F_{p^2}$：
取 Frobenius 平方为 $-p$ 的原 SS 模型，
$-p\equiv1\bmod6$ 保 full-six 标记，
而三次扭曲在 $\mathbf F_p$ 已解开。
真实 source/target 同源尺度照 R1023 §5 保留。
若特殊形式同源及 dual 的首项为 $k_sT^p,g_sT^p$，则
$$
C_s^{p-1}=\frac1{g_sk_s^p},\quad
U_{\rm target}=k_sg_s^p,\quad
\theta_s=-\frac{k_sg_s}{h_p'(s)}.
\tag{1038.33}
$$
原 crystalline 水平性、determinant 和
$c_{\rm GM}=1/(2r)$ 给
$U_{\rm target}=-(h_p'/c_{\rm GM})^{p-1}$。
合并后得到
$$
\boxed{\quad
q_s:=C_s^{p-1}\theta_s^{p+1}
 =-\frac{c_{\rm GM}(s)^{1-p}}{h_p'(s)^2}
 =-\frac{r_s^{8g+2}}{A_p'(s)^2}.
\quad}
\tag{1038.34}
$$
没有将未知 source、target 或 norm 单位设为一。

定义原有理函数及其唯一部分分式
$$
\mathscr F_p(b)
=\frac{6(b^p+1)}{r^{4g+3}A_p(b)^2}
=\sum_{s\in S}\frac{d_s}{(b-s)^2}+R_p(b),
$$
$$
d_s=\frac{6(s^p+1)}
           {r_s^{4g+3}A_p'(s)^2}
    =q_s\lambda(s)^p.
\tag{1038.35}
$$
由 (1038.30) 作三阶 Taylor 展开，
所有 $S$ 上的一阶极部均为零，扣掉自身双极部的常数为
$$
d_s\,\frac{s(s^3+7)}{12(1-s^3)^2}.
$$
因此 $R_p$ 仅在三个 $r=0$ 支持点有极点，
且在无穷远消失。
将所有交叉项及这个准确对角项代入 (1038.28)，得到
$$
\boxed{\quad
\log_B(P_B)\equiv
\varepsilon\sum_{s\in S}\theta_s
                \bigl(\lambda(s)+R_p(s)\bigr)f_s
                         \pmod{\pi_0^{m+1}} .
\quad}
\tag{1038.36}
$$
$e_1$ 在该完整首向量上为恒等；环面、两个中心、
支持尾及其可能的 degree-$p$ 输入已在 §§5–6 处理。

## 8. 同一实际向量对本行全部素数非零

置
$$
\ell=(p+1)/3=4g+2,\qquad d_Q=(p-5)/6=2g,\qquad
y=1-b^3,\qquad q(y)=Q_p(y).
$$
有 $\ell=2d_Q+2,\ p=3\ell-1$，且 (1038.32) 保证
$q^2$ 的反射不变。定义
$$
P_1=T_{\le\ell}\frac1{(1-y)q^2},\qquad
P_2=T_{\le\ell}\frac{(1-y)^{\ell-1}}{q^2}.
$$
按 (1038.35) 的三个实际支持极部展开，准确得到
$$
\lambda+R_p=
\frac6{y^{\ell+1}}
 \{b(P_1-y^\ell)+(P_2-y^\ell)\}.
\tag{1038.37}
$$
因此完整首向量全零当且仅当
$$
q\mid P_1-y^\ell,\qquad q\mid P_2-y^\ell,\qquad P_2(1)=1.
\tag{1038.38}
$$
最后一条件仍来自原 $b=0$ 尾，不可删除。

R1024 §§2–5 的有限代数证明只使用
$\ell=2d_Q+2,\ p=3\ell-1$、同一个 (1038.31) 的 ODE、
$q^2$ 反射及 $\ell>5$，没有使用 $d_Q$ 为奇数。
将本行参数代入它的两条截断一阶方程后，仍迫一个
次数至多二的多项式及该文 (1024.7)：
$$
\mathcal G(y)(a y+b y^2)
 \equiv(1-y)^{2/3}-1+c y\pmod{y^\ell},
\qquad
\mathcal G=(1-y)^{5/3}(q/q(0))^4.
$$
故 (1038.38) 同时要求该文已逐项纸面核准的两个残差为零：
$$
\frac{108439}{39844224}=0,\qquad
\frac{11227003}{2762532864}=0
                    \quad\text{于 }\mathbf F_p.
$$
所用分母只含 $2,3,5,7,13,61$；
没有一个属于本行 $p\ge41,\ p\equiv5\bmod12$。
而已登记的完整整数恒等式
$$
1290641\cdot108439-12466\cdot11227003=1
$$
排除两个分子同时为零。这是消费既有纸面证明，不重跑旧计算。

从而本行有
$$
\boxed{\begin{aligned}
P_B&\in F^mB(R)\setminus F^{m+1}B(R),\\
\log_B(P_B)&\in
 \pi_0^m\operatorname{Lie}B
          \setminus\pi_0^{m+1}\operatorname{Lie}B,\\
e_1\log_B(P_B)&\in
 \pi_0^m\operatorname{Lie}\mathcal G_1
          \setminus\pi_0^{m+1}\operatorname{Lie}\mathcal G_1.
\end{aligned}}
\tag{1038.39}
$$
形式点与完整对数的准确深度都是 $m$，对应 $p$-赋值
$1/(p+1)$；两者的非零是分别证明的。

## 9. 来源、已核边界与接续

- [R906](R906-original-period-lattice-and-integral-CM-Tate-image.md)、
  [R910](R910-original-normalizer-inertia-and-one-sided-CM-gluing.md)
  §§2–3、[R921](R921-original-Igusa-node-and-first-Drinfeld-normal-differential.md)
  §§2–3：实际 Raynaud、完整惯性、Igusa kernel、饱和 Hodge
  比较及本行节点厚度。只消费这些原范围，不搬其特定 CM 商结论。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)
  §§2–5：真实 regular 局部型、Savitt 列表及整 Hecke 分离；
  本篇 §2 单独补完本行新增二次型。
- Fontaine–Laffaille，
  [*Construction de représentations p-adiques*](https://www.imo.universite-paris-saclay.fr/~fontaine/laffaille.pdf)，
  Proposition 4.4、Theorem 5.3、§§7–8；
  root/o1 亲读其简单对象、惯性数字和 crystalline 比较。
- Edixhoven–Parent，
  [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)，
  §2.2.4、Theorem 3.3、Theorem 3.5 (26)；
  root/o1 核双中心和原底环上的厚度 $2,6$，
  未忽略该文对 Igusa 连通性的 caveat。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)、
  [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：
  同一个原 quotient-Hasse 比较及 full-$p$ affine 刚性；
  双节点的共同单位、完整主部与 Krull 节点步骤在本篇另付清。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)
  §§2–6：同 family 的 GM、真实 source/target 尺度和完整
  degree-$p$ 分母预算；本篇显式给出本行变更后的所有指数。
- [R1024](R1024-original-complete-first-log-uniform-nonvanishing.md)
  §§2–5：与次数奇偶无关的原两整除加中心矛盾。
  [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)
  的一般 BT 比较可施于 (1038.11)，不能施于整个半稳定 $J$。

o1 与 root 分别纸核所有新增二次型、两个中心和 graph 角色、
原 $2mD_0$ 的 twister、素于 $p$ 挠点的处理、
两端共同 Dickson 消去、全部 $p$ 分母、原 Hasse 指数及
R1024 的参数范围。global 独核实际 bounded lift 和 CM 域边界。
没有数学程序执行，也没有重跑已登记素数窗。

(1038.39) 不宣称任何预先选定简单商上的 Néron 单位。
本行额外可能的 CM 域、完整 MW 消去和指定 CM jet
必须在后继中按实际最低型分别核准。
**Serre 主目标仍 OPEN；O0 的其余全局分支没有由本篇排除。**
