# R486：完整 ruling 的三导平方、有限低阶余表与真实状态开域障碍

日期：2026-11-16。**完整纸面证明；没有执行符号程序、原根恢复、profile 求积、秩计算、人工检查或新的数值研究。**

本稿回答 R482/R484 留下的一个具体问题：如果从起点增加有限 $C^2$ profile 观察，能否把两条加速度行连同整个无加速度项一并清掉，从而允许原 R70 桥任意走？

答案必须分层。

1. 原完整 ruling 的高阶部分仍有一个真实三导平方。R296 的点态证明不依赖 Gaussian 芽；在原规范的真实零历史、零速度起点下，它适用于任意后续水平几何。加速度两行只在低阶余项中，不能替代这个平方。
2. 完整余项确实只有有限个连续 quartic $C^2$ profile 系数，可以从起点纳入同一个有限观察表；但“保留这些值”不等于“任意令其为零”。
3. 更强地，在 R480 同一个严格不交 rank-one 库中，两条完整第二历史行有相同的三导主项，却相差一个严格负的低阶量。它排除把完整无加速度项在真实十三状态的任何开放集合上恒清。
4. 这个开域结论**不排除**满足真实八矩 ODE 的较低维约束路径，也不能直接判定一个常 scalar 实现。常 scalar 的原矩阵与 physical 配对之间有一个必须保留的 rank-one 关联；它不是任意八矩。

因此下一正向机制仍可寻找真实约束状态族，但不能把“所有新增低阶观察从头匹配”理解成内部 ruling 已自由消失。本文不排可变 cap，不重用冻结母的非零结论去排全部库。

## 1. 对象、完整无加速度项及其二次历史系数

固定 R480 的同一个真实圆
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=\sum_i c_i(\theta)u_i,\qquad
c_i=a_i\cos\theta+b_i\sin\theta,
$$
$$
d_i(\theta)=a_i^2-c_i(\theta)^2,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
\tag{1}
$$
$u_i$ 为有限个非零实光滑紧 profiles，支撑严格不交，保原右锚及两个 collars。所有已付三矩与完整 $W$ outer 条件均在同一个库中：
$$
I_j\{\phi_\theta,\tau(\phi_\theta;D_\theta)\}=0
\quad(\tau\in W,\ j=0,1,2).
\tag{2}
$$

记当前几何与第二历史为
$$
S=(h,k,\omega),\quad z=x+\omega,\quad e=hz-k,\quad Q=1+e^2,
$$
$$
\gamma=h_s,\quad \upsilon=k_s,\quad e_s=\gamma z-\upsilon/2,\quad
A=\Phi_{\mathsf m},\qquad \mathsf m_s=M_{\rm raw}(S,\gamma,\upsilon).
\tag{3}
$$
$h>0$，共同物理支为 $z>0$。第二累计 $\mathsf m$ 是真实状态，不是任意可安装的瞬时控制。

原 physical 配对为
$$
\mathcal E_S(a,b)
=\frac1{4h}\int\{Q a''b''+2h^2a'b'\}
=\mathbf w(S)\cdot\mathbf I(a,b),
$$
$$
\mathbf w(S)=\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right).
\tag{4}
$$
涉及非紧单包输出时，始终使用原完整 Green／左尾规范；只有整体 $AD_\theta$ 由原三矩真正紧。

R482 已把完整 ruling 写为
$$
\mathscr K=\mathcal F(X;\theta)+\mathcal C_h(S;\theta)h_{ss}
+\mathcal C_k(S;\theta)k_{ss},
\quad X=(S,\mathsf m,\gamma,\upsilon).
\tag{5}
$$
$\mathcal F$ 包含全部局部恢复、变化-profile chain、真实端点势、一般固定 $w_\theta,\chi_\theta$ 和第二历史平方。直接从其完整式可读出：关于八个 $\mathsf m$ 变量的齐次二次部分准确为
$$
\boxed{
\mathcal Q_{A,\theta}(S)
=-\mathcal E_S(AD_\theta,AD_\theta)
+2\mathcal E_S\{\phi_\theta,A(\phi_\theta,AD_\theta)\}.
}
\tag{6}
$$
其余关于 $\mathsf m$ 的项至多一次。特别，(6)不含 $w_\theta,\chi_\theta$，也不含真实初端的固定势。这一点不需要把初端重置为零。

## 2. 原主平方适用于任意真实路径：哪里用了起点条件

本节先取 canonical $w=\chi=0$。采用整个实际词的原共同起点，假设该处真实
$$
\mathsf m_0=0,\qquad T_0=0,\qquad
\gamma_0=\upsilon_0=0.
\tag{7}
$$
常 scalar 初芽满足(7)；零速度的原起点也足够。**不能在后来切出的每个子桥重新施加(7)。**

对单包写
$$
u'=p,\qquad u''=r,\qquad u'''=t.
$$
任一原八矩算子 $X$ 有
$$
\Phi_X(u,u)''=\alpha_X[u]\,t+\beta_X^{(2)}[u],
$$
$$
\boxed{
\alpha_X=A_{1,X}u+2A_{2,X}p-2C_Xr,\qquad
C_X=B_{0,X}+xB_{1,X}+x^2B_{2,X}.
}
\tag{8}
$$
$\beta_X^{(2)}$ 保真实 $C^2$ primitives；上标只是导数阶说明，不与下面的局部 $\beta$ 混同。

从 R221 原 $\eta$ 定义
$$
\boxed{
\beta_S[u]=\frac Q{8h^3}(\gamma p-e_sr),\qquad
L_{S,\mathsf m,\gamma,\upsilon}[u]=\frac{\alpha_A[u]}2+\beta_S[u].
}
\tag{9}
$$
R296§§4–6 的证明中，以下三个关键身份都是 R56/R73 的**点态原式**：
$$
\partial_r^{\rm loc}\Phi_X(u,\Phi_Y(u,u))
=\frac{\alpha_X\alpha_Y}{2},
\tag{10}
$$
$$
\partial_r^{\rm loc}\mathscr C_s(u;u,u)
=\partial_s(\beta_S[u]^2),
\tag{11}
$$
$$
\partial_r^{\rm loc}T_s(u;u,u)
=\beta_S[u]^2-\frac{\alpha_A[u]^2}{4}.
\tag{12}
$$
其中 $\mathscr C_s$ 是 R73 的完整局部第三密度，已经扣除真实变化-profile 的 $\Psi$。$\partial_r^{\rm loc}$ 采用 R285/R296 的固定降阶呈示：对 local $r$ 微分，真实低阶 primitive 变量保留。

(10)由原六项式及右积分中的一次 $t$ 降阶得到；(11)用的就是原 $M_{\rm raw}$ 与真实水平关系 $\omega_s=k_s/(2h)$。两者没有使用 Gaussian 的 $\sigma$ 依赖。只有从(11)积分到(12)时用了(7)与 $\beta_0=0$。因此不能因为 R296 最初把它应用于 Gaussian 芽，就把(10)(11)误限于那种几何；也不能反向丢掉它们的初值要求。

为保清真实前缀，任一中间切点 $s_0$ 的准确版本是
$$
\begin{aligned}
\partial_r^{\rm loc}T_s
={}&\beta_s^2-\frac{\alpha_{A_s}^2}{4}\\
&+\left(
\partial_r^{\rm loc}T_{s_0}
-\beta_{s_0}^2+\frac{\alpha_{A_{s_0}}^2}{4}
\right).
\end{aligned}
\tag{13}
$$
若它是从同一满足(7)的全词起点真实走来的切点，括号确实为零，但必须由该真实入值判断。任意给定非零初端第三或速度时，括号必须原样加入，不能把它叫作无关常数删掉。

## 3. 完整 ruling 的高阶部分及全部尾项范围

原第二场最高 profile jet 为
$$
(V_Z')_{\rm prin}=(1,0,e)L[u]\,t .
$$
真正第三局部场的三导项、原累计 $T$ 的(12)与第二能量，在共同因子 $Qt^2/h$ 下分别给
$$
-d_i^2L_i^2,\qquad
-2c_i^2d_i\beta_iL_i,\qquad
c_i^2d_i\left(-\frac{\alpha_{A,i}^2}{4}+\beta_i^2\right).
$$
三项准确相加为 $-a_i^2d_iL_i^2$。所以
$$
\boxed{
\mathscr K_s^0(\theta)\equiv_2
-\sum_i a_i^2d_i(\theta)
\int\frac Qh\,L[u_i]^2(u_i''')^2 .
}
\tag{14}
$$

$\equiv_2$ 指差是一个**完整、连续 quartic $C^2$ polynomial 泛函**，保所有右 primitives、左常值、有序 cross 与 Green 边项；不是高频渐近号，也不表示差为零。

这里不能仅从 $|V_Z'|^2$ 猜(14)。如果漏掉 $\Psi$、$T$ 的原初值或第三局部场，所得平方的交叉系数会错。两加速度 $h_{ss},k_{ss}$ 的真实系数已经由 R482 证明为 $C^2$，所以它们全在余项中；(14)只依赖当前 $S,\mathsf m,\gamma,\upsilon$。

跨包不能凭支撑不交直接删除。原右方包在当前包上的第二左尾是实际仿射分子；代 R56 后相应第三局部项没有 local $r$ 导。其余带一次 $t$ 的 cross 项按同一个真实 primitive 公式降到 $C^2$。因此没有额外的跨包 $t_i t_j$ 主项；那些低阶尾本身仍存在。

在(14)中取后来子桥的真实 $\mathsf m$，已经保留原前缀。若全词起点不满足(7)，须先使用(13)补回初端第三项的真实贡献，再谈同样分解；本文不给那种初端一个免费的零值。

## 4. 哪些部分确属有限低阶观察，哪些不是

将(9)平方展开：
$$
L^2=\frac{\alpha_A^2}{4}+\alpha_A\beta+\beta^2.
\tag{15}
$$
这精确区分三类高阶来源：

| 原几何／历史次数 | 完整三导主项 | 是否可直接列作 $C^2$ 观察 |
|---|---|---|
| 第二累计二次 | $\alpha_A^2/4$ | 一般不能 |
| 第二累计乘真实速度 | $\alpha_A\beta$ | 一般不能 |
| 真实速度二次 | $\beta^2$ | 一般不能 |
| 两加速度行 | 无三导平方 | 可以，按 R482 原式 |
| 扣除(14)后的完整余项 | 无剩余三导平方 | 可以，须保原尾及基线 |

“可以”只表示具有原初选有限低阶纤维方法要求的正则性；不意味着可任意赋值或已经由当前库支付。

### 4.1 高阶表也是有限的，但不能改名为低阶表

(8)(9)中 $u,p,r$ 的 $x$ 系数次数分别至多 $2,3,4$。乘上原 $Q$ 后，全部主项落在下列已明确的有限生成表：
$$
\begin{array}{c|c}
\text{jet 单项式，另乘 }(u''')^2&x\text{ 次数}\\ \hline
r^2&0,\ldots,10\\
pr&0,\ldots,9\\
ur&0,\ldots,8\\
p^2&0,\ldots,8\\
up&0,\ldots,7\\
u^2&0,\ldots,6
\end{array}
\tag{16}
$$
共有五十四个生成量。这沿用 R296 的真实次数界，**不是新的实际秩**，也不是当前二十目标已经覆盖全部任意状态系数的结论。已有偶母普遍关系与特定几何关系必须按原范围保留。

### 4.2 确定的非 $C^2$ 例子

取 $P=\Phi_{r_0}$。由 $\alpha_P=-2r$，其能量含
$$
\int Q\,r^2t^2 .
\tag{17}
$$
它在任何含有非零实紧母的自然 $C^2$ 邻域中都没有连续 $C^2$ 延拓。纸面证明可以在一个 $u_0''\ne0$ 的内小区间取平滑 cutoff $\chi$，令
$$
u_N=u_0+N^{-5/2}\chi(x)\cos(Nx).
$$
则 $\|u_N-u_0\|_{C^2}\to0$，三导扰动却为 $O(N^{1/2})$。在该小区间上(17)的平方主项随 $N$ 发散，而低阶项保持有界。两端与外 cap 完全没有移动。

这只是正则性的纸面见证，没有执行高频求值，也不声称这条扰动本来保当前所有纤维条件。它已经足够说明：不能把(17)作为一个连续 $C^2$ 观察直接塞入原低阶 IFT，或认为普通 IBP 会消掉它。

### 4.3 有限低阶余表的准确含义

从 R482 的有限原式、R73 的八算子和 R77/R79 的固定有限第三端点空间出发，扣去(14)，再逐个将线性三导按 R285 的 local primitive 降阶，得到有限的真实 quartic $C^2$ 系数表。几何系数保有限 Laurent/log 表达，第二累计至多二次；不再有一个随路径任意增长的第三 history 字表。

可以从起点把**所需这些完整低阶系数**加入同一个 $F^\star$。在做微包 self 呈示时，必须像 R294/R299 一样保真实有序核和校正边界；未经该处理的非紧单包值不等于完整圈的低阶余项。对完整 canonical block 的共同平移，R245 原恢复仍给至多十次的整体次数界。

以上给的是有限数据接口，不是把“有限”升级成“全可控”。保持新 $F^\star$ 只保持其初始基线。若余表存在一个严格正的完整关系，该关系不会因把每一项都列入 $F^\star$ 而消失。下一节给出这样的准确关系。

## 5. 全 $W$ outer 已经固定一个严格正的四次幅和

设
$$
C_i=\int(u_i'')^4>0,\qquad
\lambda_i(\theta)=-a_i^2d_i(\theta).
$$
$C_i>0$ 只使用实性、非零性和双零 collar。

取 $P=\Phi_{r_0}$、$L=\Phi_{p_0}$。R259/R267/R304 的完整同锚表给
$$
2I_0\{u,[P,L](u;u^2)\}=C(u)/6
$$
且该外矩的有序跨包核准确为零。因此(2)包含
$$
\boxed{
\mathcal A_\theta:=\sum_i c_i(\theta)^2d_i(\theta)C_i=0
\quad\text{对全部 }\theta.
}
\tag{18}
$$
这不是新增未付门，也不要求单包的三矩为零。

因为 $a_i^2=d_i+c_i^2$，
$$
\boxed{\sum_i\lambda_i C_i=-\sum_i d_i^2C_i.}
\tag{19}
$$
置
$$
A_4=\sum_i a_i^4C_i,\quad
C_{22}=\sum_i a_i^2b_i^2C_i,\quad
E_4=\sum_i b_i^4C_i=\int(g'')^4.
$$
在 $\theta=\pi/2$ 用(18)，再取其完整相位平均，准确给
$$
E_4=C_{22},\qquad A_4=5C_{22}.
$$
故
$$
\boxed{
\sum_i d_i(\pi/2)^2C_i=4E_4>0.
}
\tag{20}
$$
非退化真实圆有 $g\ne0$。这些身份不依赖等背景、母形相同、包序或某个冻结 cap。

## 6. 两条完整平方行的严格负差

按原规范定义 directed 行
$$
\mathscr H^{Y\to X}_{j,\theta}
=-I_j(YD_\theta,XD_\theta)
+2I_j\{\phi_\theta,Y(\phi_\theta,XD_\theta)\}.
\tag{21}
$$
所有 $\Phi$ 记号在此按原算子省写；不把这些算子复合当作八矩矩阵乘法。

取 $S=\Phi_{s_0}$。R304§3 的两个完整表项为
$$
\begin{array}{c|c|c}
\text{行}&\text{有序跨包核}&
I_j(Yu^2,Xu^2)+2I_j\{u,Y(u,Xu^2)\}\\ \hline
P\to P,\ j=2&0&4C/3\\
S\to P,\ j=1&0&C/2
\end{array}
\tag{22}
$$
这保留 $P(u,u)=J(r^2)$ 与 $S(u,u)=J(xr^2)$ 的真左常尾。两条 self 还可由
$
P(u,Pu^2)=2r^3/3,\qquad
S(u,Pu^2)=2\{xr^3+J(r^3)\}/3
$
直接用原 $I_2,I_1$ 核回(22)；后式的 $J(r^3)$ 没有擅置左值为零。用(18)，两条 self 补偿准确消去，故
$$
\mathscr H^{P\to P}_{2,\theta}
=\sum_i\lambda_i I_2(Pu_i^2,Pu_i^2),
$$
$$
\mathscr H^{S\to P}_{1,\theta}
=\sum_i\lambda_i I_1(Su_i^2,Pu_i^2).
\tag{23}
$$

为核主项和低阶差，置
$$
H_{a,i}=\int x^2(u_i'')^2(u_i''')^2.
$$
直接用
$$
(Pu^2)'=-r^2,\quad (Pu^2)''=-2rt,\quad
(Su^2)''=-r^2-2xrt
$$
及真实紧端 IBP $\int xr^3t=-C/4$，得到
$$
I_2(Pu^2,Pu^2)=4H_a+2C,\qquad
I_1(Su^2,Pu^2)=4H_a-C/2.
\tag{24}
$$
第一式的 $2C$ 来自原 $I_2$ 的 $2(P')^2$，不能删掉。

由(19)(23)(24)，
$$
\boxed{
\mathscr H^{P\to P}_{2,\theta}
-\mathscr H^{S\to P}_{1,\theta}
=-\frac52\sum_i d_i(\theta)^2C_i.
}
\tag{25}
$$
特别
$$
\boxed{
\mathscr H^{P\to P}_{2,\pi/2}
-\mathscr H^{S\to P}_{1,\pi/2}
=-10\int(g'')^4<0.
}
\tag{26}
$$

两条行具有相同的三导能量主项，但它们的**完整**差不能为零。这正是“principal 全付后仍须保低阶基线”的一个具体实例。本文只是消费已发表的两条原表并完成新的用途，没有重新求旧整体秩。

## 7. 完整无加速度项不可能在真实状态开域恒零

**开域障碍定理。** 对满足(1)(2)且 $g\ne0$ 的真实库，固定任何合法的同一个 $w_\theta,\chi_\theta$ 与真实初端类，R482 的 $\mathcal F(X;\theta)$ 不可能在十三状态域的某个非空开放集合上、对全部 $\theta$ 恒为零。

证明分三步。

第一步，开放集合包含一个状态乘积小盒。固定其 $S,\gamma,\upsilon$，把 $\mathcal F$ 看作八个 $\mathsf m$ 的至多二次多项式。若它在 $\mathsf m$ 的开盒恒零，其齐次二次部分(6)必须对每一个八矩 $A$ 为零：
$$
\mathcal Q_{A,\theta}(S)=0.
\tag{27}
$$
这里是多项式身份推出任意 $A$，不是声称实际路径能独立访问这些 $\mathsf m$。

第二步，$S$ 也在开盒变化。令 $d=h\omega-k$。对固定 $A,\theta$，(27)为
$$
\frac{1+d^2}{4h}H_0+\frac d2H_1+\frac h4H_2=0,
\quad H_j=\mathscr H^{A\to A}_{j,\theta}.
$$
乘 $4h$ 后得到
$$
(1+d^2)H_0+2hdH_1+h^2H_2=0
$$
于一个真实 $(h,d)$ 开集，故三个常系数全零。因此
$$
\mathscr H^{A\to A}_{j,\theta}=0
\quad\text{对每个 }A,\ j=0,1,2.
\tag{28}
$$
这保原 $I_2$，没有将 physical 配对替成只有二导的伪度量。

第三步，对(28)作真实算子极化，得到
$$
\mathscr H^{X\to Y}_{j,\theta}
+\mathscr H^{Y\to X}_{j,\theta}=0.
$$
另一方面，两者的差为
$$
2I_j\{\phi_\theta,[X,Y](\phi_\theta;D_\theta)\},
$$
由已付(2)为零。所以每个 directed 行本身都为零。特别(25)左边为零，与(26)矛盾。证毕。

本定理同样适用于打算从起点另增有限低阶观察、仍保严格 rank-one 及完整(2)的库；(26)是这些原条件本身迫出的身份。不能通过“把差也放进 $F^\star$”将严格非零值改成零。

但本定理没有排除较低维的允许状态族。真实 $\mathsf m_s=M_{\rm raw}$ 只沿一条路径走；它不需要在八矩开盒中自由变化。如果 $\mathcal C$ 非零，真实反馈也可能用两个加速度支付 $\mathcal F$，受 R484 的锁定与奇点边界限制。这里排除的是**将 $\mathcal F$ 在整个状态开域清零以获得无约束桥**的那条方案。

## 8. 常 scalar 的真实 rank-one 关联，不能混同开域结论

对某个具体常 scalar $S_c=(h,k,\omega)$，令 $\gamma=\upsilon=0$。原 R73 给
$$
K_0=kx^2+a_1x+a_0,\qquad
a_1=2k\omega-\frac{k^2+1}{h},\quad
a_0=k\omega^2-\frac{k^2+1}{h}\omega,
$$
$$
d=h\omega-k,\qquad
b=\begin{pmatrix}1+d^2\\2hd\\h^2\end{pmatrix}.
$$
将原八坐标逐列收集，真实矩阵恰为
$$
\boxed{
M_c=
b\begin{pmatrix}
-\dfrac{k}{2h}&\dfrac{a_1}{4h}&-\dfrac{a_0}{2h}
\end{pmatrix}.
}
\tag{29}
$$
原 trace 恒等是
$$
-\frac{k(1+d^2)}h+d\,a_1-h\,a_0=0.
$$
所以作为 $3\times3$ 矩阵，
$$
\boxed{\operatorname{rank}M_c=1,\qquad M_c^2=0.}
\tag{30}
$$
非零性也真实：若 $k\ne0$，第一列非零；若 $k=0$，$a_1=-1/h\ne0$，第二列非零。

同时 physical 权向量准确为
$$
\boxed{\mathbf w(S_c)=b/(4h).}
\tag{31}
$$
因此一个常态实现的 $M_c$ 与它用于(6)的三矩权之间有固定关联。它不是任意 $A$ 配任意三矩权。

尤其(30)不能替换成
$\Phi_{M_c}(\phi,\Phi_{M_c}D)=0$。后者是原二次算子复合，不是矩阵乘法；R482(39)正须保它。第7节的“任意八矩与开 scalar 域分离”不能直接用于这个受约束关联族。

## 9. 当前常态平方门的明确主项及剩余完整接口

静态 R73 系数给
$$
A_{1,M_c}=-\frac{kQ}{2h},\qquad
A_{2,M_c}=\frac{K_{0,x}Q}{8h},\qquad
C_{M_c}=\frac{K_0Q}{8h}.
$$
因此
$$
\boxed{
\alpha_{M_c}[u]
=\frac Q{4h}\{-2ku+K_{0,x}u'-K_0u''\}.
}
\tag{32}
$$

在实际常段 $A(t)=A_*+t\Phi_{M_c}$ 上，R482 的 $t^2$ 系数正是(6)。从完整平方(14)取其 $t^2$ 系数，得到
$$
\boxed{
\mathcal Q_{M_c,\theta}(S_c)\equiv_2
-\sum_i a_i^2d_i
\int\frac{Q^3}{64h^3}
\{-2ku_i+K_{0,x}u_i'-K_0u_i''\}^2
(u_i''')^2 .
}
\tag{33}
$$
这个公式保真实静态 $M_c$，不把它换成一个任意平方方向。

例如在合法 $k=\omega=0$ 的常态（此时共同物理区间须 $x>0$），
$$
\Phi_{M_c}=-\frac{R}{8h^2}-\frac{T}{8},\qquad
R=\Phi_{r_1},\quad T=\Phi_{t_1},
$$
而单包能量化为
$$
\int\frac{(1+h^2x^2)^3}{64h^5}
(u'-xu'')^2(u''')^2.
\tag{34}
$$
对任何非零实紧 $u$，(34)严格正。若其为零，令 $v=u'-xu''$，则 $vu'''=0$ 且 $v'=-xu'''$，故 $(v^2)'=0$。双 collar 迫 $v=0$；在 $x>0$ 上再解 $u'=xu''$，得 $u$ 为二次多项式，双 collar 迫 $u=0$，矛盾。

**这仍不是(33)的整个相位聚合定号。** 系数 $-a_i^2d_i(\theta)$ 有符号，而且(33)还有真实 $C^2$ 余项。不能把单包正能量、矩阵 rank-one 或第7节的开域障碍直接变成某个实际常段已被排除。

### 9.1 一个不丢尾的有限完整检查对象

要判真正的(6)，应保完整 directed 张量
$$
H_{XY,j}(\theta)=\mathscr H^{Y\to X}_{j,\theta},
\qquad X,Y\in E_8,\quad j=0,1,2 .
$$
由(2)，这个张量在 $X,Y$ 上对称。若 $M_c=\sum_Xm_X(S_c)X$，准确有
$$
\boxed{
\mathcal Q_{M_c,\theta}(S_c)
=\sum_{j=0}^2w_j(S_c)
\sum_{X,Y}m_X(S_c)m_Y(S_c)H_{XY,j}(\theta).
}
\tag{35}
$$
对称呈示最多是一百零八个生成项，非 rank 声明。每项由 R259 的原 adjoint／真实尾表、原二导与全角槽定义；不需要重新恢复第四 forcing，也不能只用其(16)主表替代。

在单个固定 $S_c$，(35)是原相位次数至多四的准确多项式；种子 $D_0=0$ 去掉纯 $\cos^4\theta$ 项，保另外四个实际槽。若使用已证明的完整十二副本 odd 消去，可按那个原范围再缩减，但不凭四个采样值猜恒等。

最后，一个正长度常态段还须连同 R482 的入口常数和一次项为零：
$$
\mathscr K(0;\theta)=0,\qquad
-2\mathcal E(q_*,M_cD)
+4\mathcal E\{\phi,M_c(\phi,q_*)\}=0,\qquad
\mathcal Q_{M_c,\theta}=0,
$$
$q_*=A_*D+w$。后两处 $M_c$ 均指原 $\Phi_{M_c}$。完整第三入值、初端势与该段新增 $V$ 不因此删除。

## 10. 后续真正可走的分支

本稿给两种不能混同的约束：

- 在任意状态模型中，完整 $\mathcal F$ 不能借有限低阶观察变成一个无约束开域的零函数；(25)(26)给出明确完整障碍。
- 对实际常态，只允许(29)(31)这个关联族。必须判断(35)及真实入口两项，不能把它扩大成第7节的任意状态假设。

因此下一项实际构造可以沿两条准确路线推进：一是在(29)关联族上直接判断完整平方门；二是在 R482 的真实动力学中找到一个较低维、对向量场相切的允许状态族，连同 R484 真降秩出口接到下一段。这两条都保实际八矩 ODE，不把 $\mathsf m$ 当可逐点指定的参数。

若还需从起点增加低阶资料，只能加入第4节明确的完整 $C^2$ 余系数，并同时保原三矩、完整 $W$、共同 cap、二十目标和相位种子。高阶表(16)仍需按它自己的真实主关系与完整基线处理；已知的某一有限主控制结果不能无条件升级为任意状态的全部五十四生成量。

整个最终词的 $M$、$T$、$V$、两 period、同一十三规范及全部其余 $s$ 段仍继续。本文没有以末成本可控代替内部 ruling，也没有把加速度两行消失称为完整 $K_0$ 完成。

### 来源与独立窄核范围

- [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)：原恢复、真实密度、chain 与 physical 配对；
- [R245](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)：同锚有限呈示与降阶；
- [R296](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)、[R299](R299-complete-centered-ruling-angular-reduction-by-corrected-pure-self-fibers.md)：完整点态三项相消、低阶余项及边界校正；
- [R304](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md) §§2–4：本文两条完整原表及正四次幅身份；本文不搬用其 Gaussian 几何不可能结论；
- [R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md)、[R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)、[R484](R484-rational-germ-continuation-locking-and-finite-acceleration-discriminant.md)：当前同一库、完整状态方程与延拓边界。

mechanism 只独立窄核了在给定原表后的(19)(25)(26)消元、符号与因子；没有因此授完整状态开域分离、静态矩阵关联或新科学执行。本文所有新增结论均由以上显示原式纸面推出。
