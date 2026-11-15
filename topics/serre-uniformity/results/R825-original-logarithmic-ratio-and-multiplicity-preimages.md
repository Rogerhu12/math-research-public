# R825：用原对数导数比与有限多项式前像提取三重数

日期：2026-11-15。状态：**完整证明与实际消费者契约；尚未计算原 $P/Q$、新的极理想层或 $D$。**
本篇接 [R814](R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md) 的原导子，
使用 [R805](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) 的
$E=\mathcal B+3D$ 及 [R820](R820-original-cusp-finite-algebra-and-two-chart-Hermite-ideals.md)
的真实约化 cusp 理想。
它把此次三重数消费者中的一般整理想商，换成固定两个乘法矩阵的完整多项式前像。
原局部高度、刚性化、第二类周期与 $\eta$ 尚未因此得到。

## 1. 原输入与适用范围

保留原 $L=\mathbf Q(b,\zeta)$、$s=1+2\zeta$、$Y_L$，
原铅笔 $\langle\tau,\sigma\rangle$ 和正规基
$$
z=\sigma/\tau,\qquad
\beta_a=d_a/\tau^{\epsilon_a},\qquad
\epsilon=(0,1^{144},2^{127}),\qquad N=272 .
\tag{825.1}
$$
第二图写 $t=1/z$、$\beta^\sigma_a=t^{\epsilon_a}\beta_a$。
同一个函数的坐标从第一图到第二图乘
$$
D(t)=\operatorname{diag}(t^{-\epsilon_a}).
\tag{825.2}
$$
这里的 $\mathcal R_\tau=\bigoplus_a L[z]\beta_a$ 和
$\mathcal R_\sigma=\bigoplus_aL[t]\beta^\sigma_a$ 都是完整正规环。

令 $f$ 为本课题的非零原整数 Hom 映射，$y=y_f$ 为其原目标 $y$ 函数，
$E=(y)_\infty$。R805 已证明
$$
E=\mathcal B+3D_f,\qquad
\mathcal B=\mathcal D_{\rm cusp}+P_0,\qquad
D_f\ge0,\qquad
\deg D_f=(\deg f-21)/3 .
\tag{825.3}
$$
原 R793 的单轨道与不可约 Hom 模论证又给每个 cusp 的实际局部次数为1，
故 $D_f$ 不含 cusp。
因此非cusp极点的重数只可能为 $3d$ 或 $3d+1$；
后一种非零余数只在原 $P_0=\phi(c_0)$ 出现。
原 $P_1=\phi(c_1)$ 不加入 $\mathcal B$。

**后面的取整公式只针对这些原重数。**
不能把它推广为任意有效除子的三分之一：
对一般重数 $m$，相同逆递推实际给
$\lfloor(m+1)/3\rfloor$；例如 $m=5$ 会给2而不是1。

首个目标是原 $f_4$：
$$
\deg f_4=1206,\qquad \deg D_{f_4}=395 .
\tag{825.4}
$$
这只是既有原次数的理论上界。
它不提供新的极理想矩阵、重数分布、层数或矩阵秩。

需要的原输入是：

- 已完整认证的两图 $I_0=I_E$，在原正规基中的满秩多项式列基；
- 原实际导子矩阵 $M_{g,\tau},\Gamma_\tau$ 及第二图对应矩阵；
- 原实际两图 $A/B$ regular-multiplier 对，其中 $A=yB$、$B\ne0$；
- R820 的两图完整 cusp 理想 $\mathcal C$。

R824 的齐次模若先返回，仍须按其准确原权逐列运输到(825.1)后，才是这里的多项式输入。
一组尚未换基的齐次截面不直接冒充 $I_0$ 的 normal 矩阵。

## 2. 原导数层保持 cusp，逐一降低其他重数

R814 的正则导子为
$$
\delta_\tau=\tau^{-1}D_0,\qquad
D_0=\frac{q_Y}{82}\frac d{dq_Y},\qquad
\operatorname{div}\delta_\tau=\mathcal D_{\rm cusp}-H_\tau .
\tag{825.5}
$$
在 $U_\tau$ 内，它只在 cusp 有一阶零。
第二图必须使用 $\delta_\sigma=t\delta_\tau$，不是在全图硬用第一图导子。

对任一已经准确认证的非零整理想 $I\subset\mathcal R_\tau$，定义
$$
\mathcal N(I)=I+\delta_\tau(I).
\tag{825.6}
$$
这里右侧取加法子群；R814 的 Leibniz 论证已经证明它本身是完整 $\mathcal R_\tau$ 理想。
如果 $I=H_IL[z]^N$，则准确有
$$
\mathcal N(I)=\operatorname{im}_{L[z]}
 [\,H_I,\ \Gamma_\tau H_I+M_{g,\tau}H_I'\,] .
\tag{825.7}
$$
没有额外的原 $N$ 个基元素乘法闭包。

令
$$
I_{\ell+1}=\mathcal N(I_\ell),\qquad I_0=I_E .
\tag{825.8}
$$
在一个闭点的完成 DVR 中写
$I_0=(u^m)$、$\delta=a(u)\partial_u$。
特征零保证 $m>0$ 时导数首系数 $m$ 不消失。
因此在非cusp极点，
$$
v_P(I_\ell)=\max(m-\ell,0),
\tag{825.9}
$$
在 cusp，原 $m=1$ 且 $v(a)=1$，故每层一直有
$$
v_P(I_\ell)=1 .
\tag{825.10}
$$
在 $E$ 外，各层都是单位理想。
这些论证可在忠实标量扩张后验证，再下降；实际算法不拆分闭点。

于是两图的层最终同时等于原 $\mathcal C$。
R820 已真实给出两图的完整 $\mathcal C$：
run43721747750，source
7890fde180ffabee056de2ce8dd241b189a893a2；
原certificate SHA256为
a2e629d05d561e1144e6989612213b33990075400a21f7c1c2f0c2eb825152b4。
两图各有实际余长度20，不重新计算这个理想。

如果首次实际得到两图 $I_{\ell_*}=\mathcal C$，
则 $\ell_*$ 是非cusp最大极点重数；可以取
$$
K=\left\lceil\frac{\ell_*-1}{3}\right\rceil
=\max_{P\notin\mathcal D_{\rm cusp}}v_P(D_f).
\tag{825.11}
$$
这里用到了(825.3)的重数同余。
在尚未取得这些真实层时，可直接用安全理论界
$K=\deg D_f$。
不能从安全界反填实际 $\ell_*$ 或实际最大重数。

### 2.1 原C的稀疏坐标只用于底环换基

R820 的真实两图 Hermite 度数都是
$$
(d_0,\ldots,d_{271})=(0,\ldots,0,20).
$$
因此在各自原底变量中，其列形为
$$
C_j=e_j-q_j(z)e_{271}\quad(j<271),\qquad
C_{271}=P_{20}(z)e_{271},
\tag{825.11a}
$$
$P_{20}$首一；这些$q_j,P_{20}$直接读取原完成stage，不重新求值或求核。
对一个已知属于C的多项式列$v$，准确的C基坐标为
$$
(C^{-1}v)_j=v_j\ (j<271),\qquad
(C^{-1}v)_{271}
=\frac{v_{271}+\sum_{j<271}q_jv_j}{P_{20}} .
\tag{825.11b}
$$
最后一次除法必须在原字段中实际整除。

这是$L[z]$自由模的坐标变换，**不是**整理想商$I:\mathcal C$，
也不是把C的线丛平凡化为原环。
各$I_\ell\subset C$，所以可用(825.11b)检验$I_\ell=C$：
恰当的条件是变换后整个列像为单位模，而不是某个模点满秩。

还可先保原生成列，无需每一步立即转成Hermite基。
令
$$
F_0=H_E,\qquad F_{j+1}=\Gamma F_j+M_gF_j'.
$$
则完整列像恒为
$$
I_\ell=\operatorname{im}_{L[z]}[\,F_0,F_1,\ldots,F_\ell\,].
\tag{825.11c}
$$
归纳证明中，$\delta(F_jc)=F_{j+1}c+M_gF_jc'$；
第二项属于已证为环理想的旧层，故没有漏掉系数导数或额外乘法闭包。

例如实际找到多项式矩阵$X$并完整认证
$$
[\,C^{-1}F_0,\ldots,C^{-1}F_\ell\,]X=I_{272}
\tag{825.11d}
$$
即可得到$I_\ell=C$。
这是一条准确的底环Bézout证书；单个模素数的rank272不能替代它。
如果只证明某个$\ell$终止而未证明它最早，
$\lceil(\ell-1)/3\rceil$仅登记为安全上界，不登记为实际最大重数。
需要较窄的逆步骤时，再对所消费的$I_{3k+1}$求完整基。
若直接保矩形生成列，(825.26)必须使用它的全部列，
相应核秩也按真实列数计算，不硬套544。

## 3. 一个原有理函数在所有相关点给所需的一阶量

令
$$
r_\tau=\frac{y}{\delta_\tau y}\in L(Y)^\times .
\tag{825.12}
$$
$y$ 非常数，$L(Y)$ 在 $L$ 上可分且常数域为 $L$；
非零导子 $\delta_\tau$ 的核是常数，所以 $\delta_\tau y\ne0$。
同样 $y$ 不是零函数。

在一个 $y$ 的极点，写
$y=c\,u^{-m}+\text{高阶项}$、$c\ne0$。
若导子零阶为 $c_\delta=0$ 或1，则
$$
v_P(\delta_\tau y)=-m-1+c_\delta,\qquad
v_P(r_\tau)=1-c_\delta .
\tag{825.13}
$$
因此 $r_\tau$ 在每个非cusp极点恰有一阶零，在每个 cusp 是单位。
在 $E$ 以外，$r_\tau$ 可能有别的零和极点；
下文的整理想交环步骤专门保留这些情况，不能假设它在全图正则。

第二图有
$$
r_\sigma=\frac{y}{\delta_\sigma y}=t^{-1}r_\tau .
\tag{825.14}
$$
在两图重叠处 $t$ 为单位；对理想乘以该单位不会改变理想。

## 4. 完整逆递推，避免一般理想商和点分解

取任何满足 $K\ge\max_P v_P(D_f)$ 的整数。
定义两图中的整理想
$$
J_K=\mathcal R,\qquad
J_k=\mathcal R\cap\bigl(I_{3k+1}+rJ_{k+1}\bigr),
\qquad k=K-1,K-2,\ldots,0 .
\tag{825.15}
$$
$r$ 始终是所在图的(825.12)或(825.14)。
中间的和是分式理想；最外面的 $\mathcal R\cap$ 不可删除。

**定理825.1。** 在本篇原输入下，两图中的
$$
\boxed{J_0=I_{D_f}.}
\tag{825.16}
$$

**证明。**
先在非cusp极点写 $m=3d$ 或 $3d+1$。
由(825.9)、(825.13)，若 $j_k=v_P(J_k)$，则
$$
j_K=0,\qquad
j_k=\min\{\max(m-3k-1,0),\,1+j_{k+1}\}.
\tag{825.17}
$$
两项均非负，所以此处交环不再改变指数。
展开逆递推，$j_0$ 是
$$
K,\qquad
k+\max(m-3k-1,0)\quad(0\le k<K)
\tag{825.18}
$$
这些整数的最小值。
当 $k<d$ 时，后者至少 $d+1$；
当 $k\ge d$ 时至少为 $d$；
而 $k=d$（若 $d<K$）给 $d$，$d=K$ 时首项给 $d$。
故 $j_0=d$。

在 cusp，(825.10)和$r$为单位给
$j_k=\min(1,j_{k+1})$，从$j_K=0$得到$j_0=0$。
这一步自动去掉了所有 cusp，不需要再计算 $(J:\mathcal C)$。

在 $E$ 外，$I_{3k+1}=\mathcal R$。
因此无论$r$有何零极，每一步
$\mathcal R\cap(\mathcal R+rJ_{k+1})=\mathcal R$。
不会引入任何来自$\delta y$零点的新支撑。

整理想由所有闭点的非负指数唯一确定，得到(825.16)。
两图的$I_\ell$在重叠处相等，(825.14)只乘一个单位，
所以每个$J_k$也在重叠处相等，定义同一个原全局有效除子。证毕。

一般$m=3d+2$时，(825.18)的最小值是$d+1$。
本定理刻意使用原(825.3)，不把它误称为任意有效除子的三重根算法。

## 5. 原 $P,Q$ 乘法矩阵：不能把导子当作乘法矩阵

从本节起固定首个实际消费者 $f_4$ 及其原 $A,B\in V_5$；
其他原映射的重数定理仍成立，但若用别的同次表示，下面的10、11须按该实际次数改写。
在第一图令
$$
a=A/\tau^5,\qquad b_0=B/\tau^5,\qquad y=a/b_0 ,
$$
以$b_0$区别目标模型参数$b$。
由原已认证的$M_a,M_{b_0},\Gamma,M_g$，准确有
$$
M_{\delta a}=\Gamma M_a-M_a\Gamma+M_gM_a',\qquad
M_{\delta b_0}=\Gamma M_{b_0}-M_{b_0}\Gamma+M_gM_{b_0}' .
\tag{825.19}
$$
这里导数只作用于底变量多项式系数。
证明是把$\delta(av)=a\delta v+(\delta a)v$代入原坐标式；
未知列$v'$的项因真正的乘法矩阵$M_g,M_a$交换而消去。

定义
$$
\mathsf P=M_aM_{b_0},\qquad
\mathsf Q=M_{\delta a}M_{b_0}-M_aM_{\delta b_0}.
\tag{825.20}
$$
它们分别是原函数
$$
p=ab_0,\qquad q=(\delta a)b_0-a(\delta b_0)
$$
的乘法矩阵，且
$$
\boxed{\quad r=p/q,\qquad \mathsf Q\text{ 在 }L(z)\text{ 上可逆}.\quad}
\tag{825.21}
$$
因为$q=b_0^2\delta y\ne0$。
不能仅凭矩阵外形把一个尚未认证的对易子宣布为原乘法矩阵；
(825.19)依赖实际的原导子和实际的原函数乘法输入。

原$A,B$来自同一同次截面关系；
所有共同尺度、$b,s,82$因子都沿原输入保留。
对$\mathsf P,\mathsf Q$不能各自重选不同的首项常数。
本篇也没有用$y$的新立方根来构造$x$或改变原CM方向。

## 6. 第二图的 $t^{10}$ 与 $t^{11}$，以及真实最高项消去

原同次截面在第二图为
$$
a_\sigma=t^5a_\tau,\qquad b_{0,\sigma}=t^5b_{0,\tau},
\qquad \delta_\sigma=t\delta_\tau .
$$
因而
$$
p_\sigma=t^{10}p_\tau .
\tag{825.22}
$$
对$q$逐项使用Leibniz：
两个导数中含$\delta_\tau(t^5)$的项完全抵消，余下
$$
q_\sigma=t^{11}q_\tau .
\tag{825.23}
$$
所以原正规坐标矩阵必须满足
$$
\mathsf P_\sigma(t)=t^{10}D(t)\mathsf P_\tau(1/t)D(t)^{-1},
$$
$$
\mathsf Q_\sigma(t)=t^{11}D(t)\mathsf Q_\tau(1/t)D(t)^{-1}.
\tag{825.24}
$$
两图都正则，故$\mathsf P_\tau$的第$(i,j)$项次数至多
$10+\epsilon_j-\epsilon_i$，$\mathsf Q_\tau$至多
$11+\epsilon_j-\epsilon_i$。
直接按(825.19)计算的朴素$q$界会是$12+\epsilon_j-\epsilon_i$；
那一层最高系数必须在实际原字段中逐项为零，并作为证书保存，
不能只按预期界截掉。
同理第二图必须认证非负次数和完整(825.24)，而不是只验几个模点。

(825.22)–(825.24)精确保留$r_\sigma=t^{-1}r_\tau$。
它不是把两图的导子或$r$强行当成同一个全局正则函数。

## 7. 每个逆步骤只是已知矩阵的完整多项式核

设原图内
$I_{3k+1}=H_I L[z]^N$、$J_{k+1}=H_J L[z]^N$。
对坐标列$x\in L[z]^N$，由$\mathsf Q$在分式域可逆，
$$
\beta x\in\mathcal R\cap(I_{3k+1}+rJ_{k+1})
$$
等价于存在$u,v\in L[z]^N$使
$$
\mathsf Qx-\mathsf QH_Iu-\mathsf PH_Jv=0 .
\tag{825.25}
$$
因此精确地
$$
J_k=\operatorname{pr}_x
 \ker_{L[z]}[\,\mathsf Q,\ -\mathsf QH_I,\ -\mathsf PH_J\,].
\tag{825.26}
$$
源矩阵是$272\times816$，分式域行秩272；
完整多项式核自由秩544。
必须先取得这个完整核，再对全部544个投影列取完整列像。

**投影在这里一般不单射。**
两个辅助表示$u,v$可以不同；
不能套用R811原两个块情形的“核投影同构”。
投影像包含非零理想$I_{3k+1}$，所以秩272；
对全部投影列做准确列Hermite化，才得到$H_{J_k}$。

所有运算只用已有$\Gamma,M_g,\mathsf P,\mathsf Q$与当前理想矩阵。
不要求272个$\beta_a$的全部乘法矩阵，不用ambient场迹配对，
也不把$L[z,w]$当成完整正规环。

## 8. 实际证书、断点和未完成量

一次完整消费者应保：

1. 原$I_E$、原$A/B$、原导子、原C四条实际来源链和相同正规基；
2. $\mathsf P/\mathsf Q$两图、完整原字段公式与$t^{10}/t^{11}$运输，
   $\mathsf Q$最高层真实消去与非零来源；
3. 每个实际$I_\ell$的完整列像证书、与C的真实终止比较；
4. 每步(825.26)的完整核、全部投影和完整列像证书；
5. 最终两图重叠、有效性和实际全局次数
   $\deg D_{f_4}=395$，以及其他目标各自的原次数检查。

理论395是安全界与最终比较，不是预填的矩阵次数。
$\mathsf P,\mathsf Q$的稠密乘法、原字段系数高度、544列投影、
多项式Euclid/Hermite过程和可能的许多层，都是尚需实际完成的成本。
可按固定原矩阵表达分块供给$\mathsf P/\mathsf Q$的列，
或保其已经认证的乘法组合；不能把未物化的表达式称为已计算矩阵。

前向层只在真实需要处保留供逆递推消费的$I_{3k+1}$，
但每一个被删大工作文件都要先有已成源绑定证书和可续接的小历史。
现存完成输入不重做；新算术只在公开Actions。
当前没有原$I_E$的新输出，也没有本篇的$P/Q$或$D$数值。
原$u_g/v_g$主函数、三同源Norm修正、刚性化和高度仍按R805/R804原规范继续。

## 来源

- 本仓库 R793、R805、R814、R820（2026）：原全Hom的cusp不分歧、
  固定21点重数同余、两图正规基、原导子与完整约化cusp理想。
- R811、R813、R815、R817（2026）：原regular乘法、Wronskian导子、
  两图矩阵及必须使用的准确列约定。
- R822、R824（2026）：完整原极理想的来源条件与按需normal运输。
  本篇的逆重数公式和固定多项式前像已在正文逐点证明。
