# R314 — 原零质量线的最小倍点返回、全部迭代与完整 q=2 转置

日期：2026-11-13。**状态：以下原单位乘子、最小次数、统一整数导子格、全部倍点返回、实际 q=2 进位、完整中央转置和同一子格的 Smith 等距均已证明。** 倍点来源的中央零确实来自同一个原目标；它们的数量不被计作新的独立 Stokes 条件，也没有把乘回单位后的来源本身判成中央零。

## 1. 同一原来源中的纯 theta 单位

保留 R309 的全部规范：$b=17$，$t=-b/x^3$，
$$
X=7bS,\quad Y=H_3,\quad Z=H_5,\qquad
(X,Y,Z)=\rho(a(t),b_0(t),c(t)),
$$
其中三个四次多项式就是 R309(4)，
$$
\rho=\sigma^{34}x^{14}(x^3-8b),\quad \rho(0)=1,
\quad S=z^6+\cdots .
$$
所有来源次数仍按 $X,Y,Z$ 的原次数计。

这里有一个特别简单的**原线性**单位：
$$
\boxed{U=\frac{-48X+5Y+4Z}{9}
=\rho(1+8t)^3
=\Theta(z)\Theta(2z)^4,\qquad U(0)=1.}                 \tag{1}
$$
最后一式完全保留 theta 权：$\Theta=x\sigma^2$、
$\Theta(2z)=x(x^3-8b)\sigma^8$，两边均为
$\sigma^{34}x^5(x^3-8b)^4$，degree 为 $34$。
因此
$$
9U=-336bS+5H_3+4H_5.                                    \tag{2}
$$
(1) 同时给实际五因子测度表达；(2) 没有给参考斜率赋值。

真实倍点在角坐标和完整载体上为
$$
\boxed{\begin{aligned}
\tau(t)&=\frac{64t(1-t)^3}{(1+8t)^3},\\
\rho(2z)&=\rho(z)^4 R_2(t),\\
R_2(t)&=(1+8t)^{10}\bigl((1+8t)^3+512t(1-t)^3\bigr).
\end{aligned}}                                         \tag{3}
$$
特别 $\deg R_2=14$。证明是将
$\sigma(2z)=-2y\sigma^4$、
$x(2z)=x(x^3-8b)/(4(x^3+b))$ 代入完整的 $\rho$；
所有 $2$ 的幂和 $(x^3+b)$ 因子恰好抵消。没有只替换角参数而忽略 Gaussian。

## 2. 完整导子格的统一整数补充

令 $\mathcal R=\mathbf Z[1/(42b)]$，$\mathcal A,\mathcal B$ 和三个
conic $C_0,C_1,C_2$ 都按 R309；记
$$d(t)=t(t-1)(8t^2+20t-1)^2.$$
除了 R309 已给的五个三次代表 $dt^j$、$0\le j\le4$，本篇精确证书还给
$$dt^5=Q_5(a,b_0,c),\qquad dt^6=Q_6(a,b_0,c).             \tag{4}$$
其分母分别仅需 $2^{14}3^{11}$、$2^{15}3^{11}$。完整系数随证书保存。
结合 $C_j(a,b_0,c)=dt^j$ 以及 R309 的无基点 pencil 递推，得到对每个
$m\ge0$ 成立的整个整数包含：
$$
\boxed{C_0\mathcal B_m+C_1\mathcal B_m+C_2\mathcal B_m
=\rho^{m+2}d(t)\mathcal R[t]_{\le4m+2}
\ \subset\ \mathcal A_{m+2}.}                          \tag{5}
$$
等号表示实际归一化中的像。证明只须先核 $m=0,1$；$m=1$ 正好需要
(4) 的两个额外代表。其后用同一个四次 pencil 生成全部 $\mathcal B_m$。
于是对所有 $n\ge2$，$\rho^n d(t)\mathcal R[t]_{\le4n-6}$ 都整地属于
原 $\mathcal A_n$。没有按次数添加新的坏素数。

## 3. 原 S 的最小单位返回次数恰为二

把 (3) 代入 $X=\rho a(t)$。准确的归一化倍点角函数是
$$\frac{X(2z)}{\rho^4}=R_2(t)a(\tau(t)).                \tag{6}$$
它在 $t=-1/8$ 有真二阶极，在无穷处有十八阶极；约分后没有其他有限极。
这可由显示式直接约分，也可由原 $S$ 在 $x=0$、$x^3=8b$ 的确切零阶核定。

**定理 1。** 有
$$
\boxed{U^2X(2z)\in\mathcal A_6,\qquad
U^2(Z(2z)-Y(2z))\in\mathcal A_6.}                       \tag{7}
$$
对 $X(2z)$ 而言，原点为单位的原齐次乘子所需最小次数为二。

**证明。** $U^2$ 的角因子是 $(1+8t)^6$，所以 (6) 乘它后是次数二十四的
多项式。$a=t(t-1)(16t^2+4t+7)$，而
$\tau-1=-(8t^2+20t-1)^2/(1+8t)^3$。因此乘后多项式被 $d(t)$ 整除。
式 (5) 使它属于原 $\mathcal A_6$。$c-b_0$ 在 $t=0,1$ 同样消失，第二式
完全相同。证书另给两个完整的六次原多项式代表，分母只有 $2,3$。

若次数一的原乘子角函数为 $k(t)$，要清掉 (6) 的有限极，必须有
$(1+8t)^2\mid k$；要落在 $\mathcal A_5\subset\mathcal B_5$，还必须
$\deg k\le2$。原三维线性空间中，次数至多二的非零角函数仅有一条线：
$$
\frac{81}{52}(832t^2-104t+1).
$$
它在 $t=-1/8$ 不为零，故不存在这样的乘子。次数零显然也不行。
而 $U^2(0)=1$，证明最小值。$\square$

这个返回是零质量来源的特殊性质。设 $P\in\mathcal A_m$ 齐次，
$c=P(O)\ne0$。原节点两支的粘合是
$$P_{\rm ang}(1)=729^mP_{\rm ang}(0).$$
另一方面 $\tau(0)=\tau(1)=0$，且
$$R_2(0)=1,\qquad R_2(1)=9^{13}=9\cdot729^4.$$ 
若原次数 $n$ 的乘子 $K$ 在 $O$ 为单位，则
$KP(2z)$ 在节点两支的比，多出准确因子 $9^m$。特征零中 $9^m\ne1$，所以
$$
\boxed{P(O)\ne0\ \Longrightarrow\ 
\text{任何次数的原单位乘子都不能将 }P(2z)
\text{ 返回原齐次 }\mathcal A.}                         \tag{8}
$$
这里 $m\ge1$。模 $p^N$ 的相应必要节点条件则保留
$K(O)c(9^m-1)\in p^N\mathcal O$，不能将特征零障碍无证改成模 $p$ 单位。
特别 (7) 不能直接用于两个质量一参考的各自倍点。

## 4. 全部倍点迭代，且不增加固定坏集

记 $j\ge0$、$Q_j=4^j$，并置
$$
e_j=\frac{2(4^j-1)}3,\qquad
D_j=Q_j+e_j=\frac{5\cdot4^j-2}3.
$$
这些都是整数，$D_j=1,6,26,106,\ldots$。

**定理 2。** 对每个 $j$ 有真实 primitive 原来源
$$
\boxed{T_j=U^{e_j}S(2^jz)\in\mathcal A_{D_j},\qquad
T_j=2^{6j}z^6+\cdots .}                                 \tag{9}
$$
更一般，对每个齐次 $P\in\mathcal A_m$，若 $P(O)=0$，则
$$
\boxed{U^{e_jm}P(2^jz)\in\mathcal A_{D_jm}.}             \tag{10}
$$

**证明。** $j=0$ 是恒等式。设 $j\ge1$。原线性系的共同零除子在
$x=0$ 两点各有阶二、在 $x^3=8b$ 六点各有阶一；$\rho$ 在这两组点
的阶分别为十四、一。倍点把这两组点送到非零三挠点，故
$P(2^jz)$ 在它们的零阶至少都是 $2m$。

除以 $\rho^{Q_jm}$ 后，角函数的全部可能极只有无穷与 $t=-1/8$，
阶数至多为
$$
\frac{14Q_j-2}{3}m,\qquad (Q_j-2)m.                     \tag{11}
$$
三分之一来自 $t$ 在 $x=0$ 的三阶极。乘 $U^{e_jm}$ 的角部分
$(1+8t)^{3e_jm}$ 清掉有限极，并且
$$
\frac{14Q_j-2}{3}m+3e_jm=4D_jm.                        \tag{12}
$$
所以得到次数至多 $4D_jm$ 的真实角多项式。

在原节点的 $t=0,1$，倍点后的 $P$ 都因 $P(O)=0$ 消失；在两个原四挠
分支，第一次倍点送到原二挠点，后续倍点送到 $O$。原节点粘合及
$P(O)=0$ 使前者至少有两阶局部零，后者至少有六阶。因此整个角多项式
被 $d(t)$ 整除，(5) 给 (10)。

整数断言没有额外的解析假设：$\sigma(2^jz)/\sigma(z)^{4^j}$ 是原整数
除法多项式，原 $x(2^jz)$ 的分母在完整正 theta 截面中取消；(11) 清掉的
正好是剩下的两个载体极。所有系数在同一个 $\mathcal R$ 中，再用 (5)
返回。对 $S$，原点首项为 (9)，在每个好奇素数处是单位，故该原来源
primitive。$\square$

预算 $D$ 中可以容纳
$\lfloor\log_4((3D+2)/5)\rfloor+1$ 条显示的实际返回来源（包括 $j=0$）。
这是具体列数；尚不是这么多层的 Smith 增益。

这些代表的对数高度仍只有 $O(D_j)$，没有隐藏一个额外的 $jD_j$ 成本。
一种直接证明是在固定的复 $x$ 圆周上读取完整正 theta 截面：原 $S(2^jz)$
的最大值至多 $\exp(C4^j)$；除去在该紧集上无零的 $\sigma^{34\cdot4^j}$
后，仍是这个界。Cauchy 估计给其原椭圆多项式系数同样的指数界。
乘 $U^{e_j}$ 只增加 $O(e_j)$，最后使用 (5) 的固定 pencil 表示只增加
$O(D_j)$。同理，(10) 可取高度 $O(h(P)+D_jm)$ 的原代表。所有常数只依赖
固定曲线和固定来源；这一步保留了全局有限次数预算。

## 5. 同一个 q=2 目标中的完整尺度 carry

取 R309 的同一个惰性 $p=6s-1>7$、$p\ne17$，前缀长度
$L=2s+\ell$、$0\le\ell<s$，以及
$$
\kappa=34c_p,\quad a_p=p\kappa\in\mathcal O^\times,
\quad g(w)=e^{-\kappa w^s}\rho(w),\quad w=z^6.
$$
所有函数在本节都截到 $w^L$。令 $R_j(t)$ 由
$\rho(2^jz)=\rho^{Q_j}R_j(t)$ 定义；它可由 (3) 迭代得到，且在 $t=0$
为整单位。置
$$
\boxed{\Delta_j=\frac{2^{j(p+1)}-4^j}{p}\in\mathcal O.}   \tag{13}
$$
真实轴满足准确有限式
$$
\boxed{g(64^jw)=g(w)^{Q_j}R_j(t(w))
               \exp(-a_p\Delta_jw^s)\pmod{w^L}.}          \tag{14}
$$
这里指数只需到二次，$2$ 是单位。$\Delta_1=4(2^{p-1}-1)/p$；其实际值
及下一位均被保留，没有宣称它总是单位。

在原整数目标
$$
T_L=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,
                                      w^\ell\epsilon^2)
$$
中，物理倍点的作用是整自同构
$$
\boxed{\Sigma_j(w)=64^jw,\qquad
\Sigma_j(\epsilon)=2^{j(p+1)}\epsilon.}                  \tag{15}
$$
它在原基的第 $r$ 行正好乘 $64^{jr}$，所有因子都是单位。
式 (14) 的指数在该环中变成 $e_2(-pa_p\Delta_j\epsilon)$，从而
$$
e_2(-pa_p\Delta_j\epsilon)
e_2(a_p2^{j(p+1)}\epsilon)=e_2(a_pQ_j\epsilon).            \tag{16}
$$
因此 $\Sigma_j$ 与 (3) 的完整 source 替换准确相容，保全部三个整数块，
而不只在模 $p$ 的首核相容。实际 $U$ 的像
$$J(U)=g(w)(1+8t(w))^3e_2(a_p\epsilon)$$
也是同一个目标里的整数单位。

若要将 (14) 改写成 R309(32) 的 $q=x^{-3}$ 坐标，必须写
$$w^s=q^s h(-bq)^{p+1},$$
其中 $h$ 是 R305 的原椭圆对数。于是指数仍有完整因子
$h^{p+1}$；其 $h^p$ 的下一位不能删除。

## 6. 全部返回列的原完整中央条件

先在普通处取 R295、R300 的同一个原 Amice 周期。R302 的 $\Theta$ 是原整
测度来源，而 (1) 给
$$
\nu_U=\nu_\Theta*([2]_*\nu_\Theta)^{*4},\qquad
\nu_U(\mathbf Z_p)=1.                                   \tag{17}
$$
由于它的 Amice 常数是单位，卷积逆 $\nu_U^{*-e_j}$ 确实是有界整测度。
因此 (9) 的准确普通转置是
$$
\boxed{\nu_U^{*-e_j}*\nu_{T_j}=[2^j]_*\nu_S.}            \tag{18}
$$
单位 Mellin 在左边必须读完整加法卷积及 $x+y\in\mathbf Z_p^\times$ 的区域；
不能将它写成两个乘法 Mellin 的商。右边则直接给
$$
M_{U^{-e_j}T_j}(u)=\langle2\rangle^{j(p-1)u}M_S(u).
\tag{19}
$$
这是原 $S$ 的真实物理缩放，并保留了 $p$-depletion、全部环带和质量。

惰性处将 $S_j=S(2^jz)$ 按自己的 charge $Q_j$ 定义
$$
\widehat S_j=e^{-Q_j\kappa w^s}S_j,\qquad
J_j(u)=\sum_{h\ge0}[w^{hs}]\widehat S_j
                         (Q_j\kappa)^{-h}(u)_h.
$$
置 $\lambda_j=2^{j(p-1)}\in1+p\mathcal O$。实际尺度及每个非负整数的有限
系数卷积给
$$
\boxed{J_j(u)=\lambda_j^uJ_S(u).}                         \tag{20}
$$
两边均在 R301 的同一较大圆盘解析，且整数点在 $p$ 进意义下有聚点，故
该等式由整数权扩展到整个中心邻域。也可由下一节的 Newton 系数恒等式
直接证明。

由于 $S(0)=0$，(19)、(20) 都准确保留
$$
\boxed{M_S'(0)=0\Rightarrow M_{U^{-e_j}T_j}'(0)=0,
\qquad J_S'(0)=0\Rightarrow J_j'(0)=0.}                   \tag{21}
$$
这里没有声称 $M_{T_j}'(0)$ 或其自身 charge 下的 $J_{T_j}'(0)$ 为零。
惰性处的完整乘法转置使用
$$
e^{-Q_j\kappa w^s}U^{-e_j}T_j
 =\widehat U^{-e_j}\widehat T_j,\quad
\widehat U=e^{-\kappa w^s}U,\quad
\widehat T_j=e^{-D_j\kappa w^s}T_j.                       \tag{22}
$$
所以中央系数读取的是 (22) 的全部卷积。$\widehat U$ 及其逆在 R301 的
半径上范数一；原 $S_j$ 的余项仍有 $R^6$ 界。这支付了所有高尾，没有丢掉
返回乘子。

## 7. 有限中央精度中的准确依赖

写 $J_S(u)=\sum_{h\ge0}a_h(u)_h$，$a_0=0$。乘 $\lambda^u$ 的整个 Newton
系数变换是
$$
\boxed{a_h^{(\lambda)}
=\sum_{i=0}^h\lambda^i\frac{(\lambda-1)^{h-i}}{(h-i)!}a_i.}
\tag{23}
$$
证明用
$\lambda^u\binom ui=\lambda^i\sum_{h\ge i}
\binom hi(\lambda-1)^{h-i}\binom uh$。
对 $\lambda\in1+p\mathcal O$，所有项与 R301 的估计相容：
$$
v_p(a_h^{(\lambda)})\ge
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil\quad(h\ge1).
$$
确实，额外 $m=h-i$ 的指数项赋值至少
$m-v_p(m!)\ge m(p-2)/(p-1)\ge m(p-1)/(2p)$。

令 $L_H^{(\lambda)}=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_h^{(\lambda)}$，
并用 R301 的实际尾界
$$M_{p,H}=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!).$$
因为完整导数在 $a_0=0$ 时不变，得到
$$
\boxed{L_H^{(\lambda)}\equiv L_H^{(1)}\pmod{p^{M_{p,H}}}.} \tag{24}
$$
所以在这份同精度证书中，全部 $j$ 的有限中央失败条件确实等价。
对它们作 Vandermonde 消元不能凭空获得 $\log D$ 个独立精度。
(23) 也精确保留了首项下一位；例如
$$
a_1^{(\lambda)}=\lambda a_1,\quad
a_2^{(\lambda)}=\lambda^2a_2+\lambda(\lambda-1)a_1,
$$
$$
a_3^{(\lambda)}=\lambda^3a_3+
\lambda^2(\lambda-1)a_2+\lambda(\lambda-1)^2a_1/2.         \tag{25}
$$
不能只保留这里的对角缩放再把不同 $j$ 当成独立中央行。

## 8. 同一原有限 q=2 核的真实等距及尚待取得的联合收益

令
$$
\mathcal I_D=\bigoplus_{1\le m\le D}
\ker\{\mathcal A_m\longrightarrow\mathcal R, P\mapsto P(O)\}.
$$
这是要求**每个**齐次部分质量为零的原直和子格，不只是所有质量之和为零。
在 $D\ge2$ 时，它在 $\mathcal A_{\le D}$ 的余维为 $D+1$；不能在一个给定
深核向量上无证地投影到这个子格。

式 (10) 给原整线性映射
$$
\mathcal T_{j,D}:\mathcal I_D\longrightarrow\mathcal A_{\le D_jD},
\qquad P\longmapsto U^{e_jD}P(2^jz).                    \tag{26}
$$
各齐次部分先用 (10)，再乘剩余的 $U$ 幂即可。它模每个好素数仍单射：
在真实函数域中，$t\mapsto t(2^jz)$、$\rho\mapsto\rho(2^jz)$ 给 dominant
替换，且乘子 $U$ 非零。因此 (26) 的像在原系数格中是 primitive；其来源
范数没有被一个隐藏的公共 $p$ 因子改变。

在第 5 节**同一个** $T_L$ 上，有完整恒等式
$$
\boxed{J\mathcal T_{j,D}
=J(U)^{e_jD}\,\Sigma_j J\big|_{\mathcal I_D}.}            \tag{27}
$$
右边两个目标算子都整可逆。因此对任意精度 $N$，该显示子格上的全部
Smith 指数、模 $p^N$ 核长度及 primitive 深关系，准确与原
$J|_{\mathcal I_D}$ 相同。它可合法运输一个已构造的深关系；单独迭代不会使
其深度再增加一次 $p$。

(9)、(21)、(26) 现在给一个明确的后续原输入：把这些 primitive 非线性
返回列放进 R309(32) 的同一个有限源，并计算不同返回像之间的真实交集或
Hensel 障碍。若这些不同像发生新的整消去，仍可能产生所需深 Smith。
本篇没有从源列数、固定节点因子或 (27) 的单份等距推断这个交集已经变大。
原 $S$ 的跨素数完整中央非零仍未证明。

## 9. 精确证书

- [check-jzero-original-doubling-return-and-q2-transport.py](../scripts/check-jzero-original-doubling-return-and-q2-transport.py)
- [check-jzero-original-doubling-return-and-q2-transport.json](../scripts/check-jzero-original-doubling-return-and-q2-transport.json)

证书的 **35 项精确检查全部通过**，重建实际倍点载体、原线性 $U$、两个额外整数导子代表、最小次数排除、
两个完整六次返回、多次迭代的准确极阶、完整指数 carry 和 Newton 三角变换。
没有扫描任何目标素数。全部无界次数和全精度断言由上述原整数格证明给出。

直接依赖：R295/R300 的原普通测度；R301/R303 的惰性完整半因子与尾界；
R302 的真实 $\Theta$ 来源；R307 的三个原多项式；R309 的完整四次像、
节点/tacnode、整数 pencil 与同一 q=2 目标。
