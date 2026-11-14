# R237 — 原负号群环的规范 Delta 商与全部精度观测

日期：2026-11-13。**状态：已证明的原对象比较。** 本篇补出 R232、R234 的负号观测在所有有限精度的整除法，保留完整环类迹。没有证明原第一个 Bockstein 非零，也没有把模 $p$ 的升层比较擅自提升成模 $p^n$ 的自守比较。

关键区别是：在整个 $(\mathbb Z/p^n)[C_p]$ 中除以 $\Delta$ 有一个额外的反对称零化方向；在原负号对应的对称部分中，除法的目标准确是 $\mathcal O^+/p^n$。这个目标只有模 $p$ 的规范中心评价，不能把增加观测精度解释为已经构造了一个 $\mathbb Z_p$ 值的中心提升。

## 1. 原对象与本篇结论

使用 R150、R153、R156、R230 的同一合法输入
$$
 E:y^2+y=x^3+x^2-2x,\quad F,\quad p,\quad \ell,\quad L/F,
 \qquad Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell].
$$
设 $\Gamma=\langle\tau\rangle$ 的阶为奇素数 $p\ge7$，并记
$$
 R=\mathbb Z_p[\Gamma],\quad g=(p-1)/2,\quad
 \delta=\tau^g(\tau-1),\quad
 \Delta=\delta^2=\tau+\tau^{-1}-2,\quad
 N=\sum_{j=0}^{p-1}\tau^j.
$$
星号表示 $\tau\mapsto\tau^{-1}$。仍令
$$
 B=E(L)\otimes\mathbb Z_p,\quad B_0=E(F)\otimes\mathbb Z_p,\quad
 A_0=\ker(N:B\to B_0)=\mathcal O w,\quad
 \mathcal O=\mathbb Z_p[\zeta_p].
$$
已删除原固定有限挠点例外。取平衡标签使 $cQ=-Q$，并写
$Q=\delta^a\varepsilon w$。

本篇处理 $a$ 奇的分支。R232 在这一分支已经证明真正的点格等式
$$
 B=RX\oplus B_0^+,\qquad cX=-X,\qquad NX=P_-,
 \qquad Q=\Delta f(\Delta)X,
 \qquad a=1+2v_\Delta(f).
 \tag{1}
$$
这里 $P_-$ 是固定负秩一格的生成元，$f\in\mathcal O^+$，且 $\mathcal O^+$ 是 $\mathcal O$ 的星号不变子环。

新增的完整结论是：

1. 对每个 $n\ge1$，可以选择正密度的真实辅助素数 $q$，使全部 $p$ 个完成给出的负号观测在 $RX/p^nRX$ 上是整同构，核准确为 $B_0^+/p^nB_0^+$。
2. 从原 $Q$ 的完整观测作对称 $\Delta$ 除法，得到 $\mathcal O^+/p^n$ 中的元素，其生成理想准确为 $(f)$ 的像。无需知道 $X$ 的局部坐标或再除一个饱和指数。
3. 第一个中心值仍只是 R232 的
$\lambda_Q=f(0)\bmod p$。它是一个实际范数除法的边界类；全部高精度观测没有免费证明 $\lambda_Q\ne0$。

## 2. 对称群环的准确整模型

置 $U=\Delta$。Chebyshev 递推给
$$
 R^+=\mathbb Z_p[U]/(U\Psi_p(U)),\qquad N=\Psi_p(U),
 \qquad
 \mathcal O^+=\mathbb Z_p[U]/(\Psi_p(U)),
 \tag{2}
$$
其中 $\Psi_p$ 首一，次数为 $g$，常数项为 $p$，并满足
$\Psi_p(U)\equiv U^g\pmod p$。

为完整核对 (2)，$1,\tau^j+\tau^{-j}$（$1\le j\le g$）是 $R^+$ 的 $\mathbb Z_p$ 基。由
$$
 \tau^{j+1}+\tau^{-j-1}
 =(\Delta+2)(\tau^j+\tau^{-j})
  -(\tau^{j-1}+\tau^{-j+1}),
$$
得到 $1,\Delta,\ldots,\Delta^g$ 为另一组整基，且
$N=\Psi_p(\Delta)$ 是首一的 $g$ 次多项式。显然 $\Delta N=0$。
上式给出的首一关系次数为 $g+1$，故基的比较证明第一同构。
把 $\tau$ 送到 $\zeta_p$，其核由 $N$ 生成；对星号取不变量是整正合的，因为 $2$ 可逆。这证明第三个同构。
最后，模 $p$ 令 $T=\tau-1$，则
$$
 N=T^{p-1},\qquad \Delta=\frac{T^2}{1+T},\qquad
 N=\Delta^g
 \quad\text{于 }\mathbb F_p[T]/(T^p).
$$
所以 $\Psi_p\equiv U^g\pmod p$。它是 Eisenstein 多项式，故
$\mathcal O^+$ 是离散赋值环，$U$ 为素元且
$$
 v_U(p)=g.
 \tag{3}
$$

令
$$
 R_n=(\mathbb Z/p^n)[\Gamma],\qquad
 S_n=R_n^+=(\mathbb Z/p^n)[U]/(U\Psi_p(U)),\qquad
 A_n=(\mathbb Z/p^n)[U]/(\Psi_p(U)).
$$
这里先取不变量再约化，与先约化再取不变量相同。
多项式环中乘 $U$ 总是单射，即使系数环有零因子。因此
$$
 \operatorname{Ann}_{S_n}(U)=(\Psi_p(U)),
 \qquad
 \boxed{\quad
 d_n:US_n\xrightarrow{\ \sim\ }A_n,\quad
 Uh\longmapsto h\bmod\Psi_p
 \quad}
 \tag{4}
$$
是规范的模同构。它对 $n$ 的约化相容；这不是在 $S_n$ 中逆一个零因子。

### 2.1 整个群环确实多一个零化方向

令
$$
 D=\sum_{j=0}^{p-1}j\tau^j,\qquad T=\tau-1.
$$
逐项计算给
$$
 TD=p-N,\qquad D^*=p(N-1)-D.
 \tag{5}
$$
因为 $\Delta=T^2\tau^{-1}$，$\operatorname{Ann}(\Delta)=\operatorname{Ann}(T^2)$。
若 $T^2z=0$，则 $Tz=bN$；施加增广得 $pb=0$，故
$b=p^{n-1}b_0$。由 (5)，$T(z+p^{n-1}b_0D)=0$，而
$\operatorname{Ann}(T)=(\mathbb Z/p^n)N$。因此
$$
 \boxed{\quad
 \operatorname{Ann}_{R_n}(\Delta)
 =(\mathbb Z/p^n)N+\mathbb F_p\,p^{n-1}D.
 \quad}
 \tag{6}
$$
两项直和为加法群：$D$ 的常数系数为零、$\tau$ 系数为一。
第二项在星号下反对称，第一项对称。因此 (6) 限制到原对称部分，恰回到 (4) 的核。
这给出必须先保留原符号再作除法的一个整理由。

### 2.2 规范中心只有模 p 评价

由 $\Psi_p(0)=p$，有规范满射
$$
 A_n\longrightarrow\mathbb F_p,\qquad U\longmapsto0.
 \tag{7}
$$
当 $n\ge2$ 时，不存在将 $U$ 送到零、并在系数环上为恒等的
$A_n\to\mathbb Z/p^n$ 环同态，因为关系 $\Psi_p(U)=0$ 会把非零的
$p\in\mathbb Z/p^n$ 送成零。
取次数小于 $g$ 的多项式代表当然可以读出一个常数系数，但那不是这样的环同态，也不在任意换基后保持不变。

## 3. 任意精度的真实负号观测素数

固定 $n\ge1$ 和 $v\in(\mathbb Z/p^n)^\times$，使
$v\bmod p\notin\{1,-1\}$。选择有理素数 $q$，要求
$$
\begin{gathered}
 q\nmid p\ell389\operatorname{disc}F,\qquad q\text{ 在 }F\text{ 惰性},\\
 q\equiv v\pmod{p^n},\qquad
 \rho_{E,p^n}(\operatorname{Frob}_q)
       \sim\operatorname{diag}(-1,-v),\\
 \operatorname{red}(P_-)\ne0
       \quad\text{于 }E(\mathbb F_{q^2})/pE(\mathbb F_{q^2}).
\end{gathered}
\tag{8}
$$
可同时避开任何已指定的有限素数集。这些要求给正 Dirichlet 密度的素数族。

下面先从原 R156 的剩余满像支付全部高精度满像，而不增加假设。
令 $H=\rho_{E,p^\infty}(G_F)$。其闭交换子群 $H'$ 位于
$\mathrm{SL}_2(\mathbb Z_p)$，且模 $p$ 的像为 $\mathrm{SL}_2(\mathbb F_p)$。
取 $U\in H'$ 提升 $I+E_{12}$。当 $p\ge5$ 时，展开乘积给
$U^p\equiv I+pE_{12}\pmod{p^2}$：提升误差是次数至多二的 $j$ 多项式之和，
$\sum_{j=0}^{p-1}1,\sum j,\sum j^2$ 在模 $p$ 下全为零。
共轭的 $E_{12}$ 张成 $\mathfrak{sl}_2(\mathbb F_p)$，故 $H'$ 含第一主同余层的全部商。
再用 $(I+p^mV)^p\equiv I+p^{m+1}V\pmod{p^{m+2}}$ 逐层提升，
闭性给 $H'=\mathrm{SL}_2(\mathbb Z_p)$。
原 $p$ 在 $F$ 不分歧，二次域 $F$ 不可能含于只在 $p$ 分歧的 $p$ 圆分塔，
所以圆分行列式在 $G_F$ 上满射。于是 $H=\mathrm{GL}_2(\mathbb Z_p)$，特别地
$\rho_{E,p^n}(G_F)=\mathrm{GL}_2(\mathbb Z/p^n)$。
$L/F$ 在 $\ell$ 分歧，而 $F(E[p^n])/F$ 在该好位不分歧，所以二者交为 $F$。
于是可指定同一个 Galois 元素在 $L/\mathbb Q$ 上为反射、在 $E[p^n]$ 上为 (8) 的矩阵。

令 $M=E[p]$。固定负点的非零 Kummer 类在
$H^1(\mathbb Q,M\otimes\chi_F)$ 中。它限制到
$G_{LF(E[p^n])}$ 后仍非零：在
$\operatorname{Gal}(LF(E[p^n])/F)$ 中，中心元 $(-I,1)$ 在 $M$ 上作用为 $-1$，
Sah 引理给这个商群的 $H^1$ 为零，再用 inflation--restriction。
其限制像受满剩余像作用稳定，因而为整个 $M$。

在保持已指定的 $E[p^n]$ 矩阵和 $L$ 分量时，改变提升会使该 cocycle 的剩余平移遍历 $M$。
记矩阵的模 $p$ 约化为 $A=\operatorname{diag}(-1,-\bar v)$。
负扭曲 cocycle 在平方处的值为 $(1-A)z$；在有限局部商
$M/(A^2-1)M$ 的唯一一维线上，该因子准确为 $2$。
因此局部值为零只是一个比例 $1/p$ 的仿射超平面。
选择其补集，再在所得有限 Galois 扩张中应用 Chebotarev，得到 (8)。
这里仅借助有限层 Kummer 类，没有假设固定点在 $p$ 处的对数为单位。

每个这样的 $q$ 都在 $L/F$ 分裂：二面体群中反射平方为一。
全部 $p$ 个完成的剩余域均为 $k_q=\mathbb F_{q^2}$。
置
$$
 W_{q,n}=E(k_q)/p^nE(k_q),\qquad \rho_{q,n}=\operatorname{red}(P_-).
$$
由于 $A^2$ 的模 $p$ 特征值为 $1,\bar v^2$，且前者在模 $p^n$ 仍为 $1$，
这个群是自由秩一的 $\mathbb Z/p^n$ 模；其 $q$ 次 Frobenius 作用为 $-1$。
(8) 的最后一个条件使 $\rho_{q,n}$ 为生成元。

## 4. 全部完成的整同构与原坐标理想

选一个由 $c$ 固定的素位 $\mathfrak q_0$。对 $Y\in B$ 定义
$$
 \Phi_{q,n}(Y)=\sum_{j=0}^{p-1}
      \operatorname{red}_{\mathfrak q_0}(\tau^{-j}Y)\tau^j
      \in R_n\otimes W_{q,n}.
 \tag{9}
$$
它对 $p$ 完备点格有定义，$R$ 等变，增广为 $\operatorname{red}(NY)$，
并满足
$$
 \Phi_{q,n}(cY)=-\Phi_{q,n}(Y)^*.
 \tag{10}
$$
由 $cX=-X$ 和 $NX=P_-$，准确可写
$$
 \Phi_{q,n}(X)=u_{q,n}(U)\rho_{q,n},
 \qquad u_{q,n}\in S_n,\qquad u_{q,n}(0)=1.
 \tag{11}
$$
$R_n$ 是局部环，其极大理想为 $(p,T)$，故 $u_{q,n}$ 为单位。
同样，$S_n$ 的极大理想为 $(p,U)$，它在那里也为单位。
任意正号基层点的约化同时被 $c$ 固定且被 $c$ 取负，因 $2$ 可逆而为零。
结合 (1)，这证明
$$
 \boxed{\quad
 B/p^nB\longrightarrow R_n\otimes W_{q,n}
 \text{ 满射，核恰为 }B_0^+/p^nB_0^+.
 \quad}
 \tag{12}
$$
特别在原 $RX$ 块上没有任何额外有限精度损失。

对原 $Q$，(1) 和 (11) 给
$$
 \rho_{q,n}^{-1}\Phi_{q,n}(Q)=U f(U)u_{q,n}(U)\in US_n.
$$
现在使用 (4) 定义
$$
 \mathcal B_{q,n}(Q)
 =d_n\bigl(\rho_{q,n}^{-1}\Phi_{q,n}(Q)\bigr)\in A_n.
 \tag{13}
$$
该定义只需要原 $Q$ 的全部完成、固定负点以及对称群环，不需要显式找出 $X$。
由于 $u_{q,n}$ 的像仍是单位，
$$
 \boxed{\qquad
  \bigl(\mathcal B_{q,n}(Q)\bigr)=(f)\,A_n.
 \qquad}
 \tag{14}
$$
这是原坐标的完整理想等式，不只是一个低阶值的比较。
写 $h=v_U(f)$，则从 (13) 读出的截断赋值准确为
$$
 \min(h,ng).
 \tag{15}
$$
当 $ng>h$ 时，它恢复原 $a=1+2h$。原已经知道的半层范围甚至使 $n=1$ 足够读出该指数。
(14) 说明提高精度不会造成新观测饱和；它不说明 $h=0$。

在 $n=1$，R234 的同一个单位比较还给
$$
 \Theta_{q,\ell}=c_q(\operatorname{id}\otimes\iota_q)\Phi_{q,1}(Q).
$$
因此对原真正的 definite 群环作对称 $\Delta$ 除法，仍得到 (14)。
当 $n>1$ 时，本篇只断言 (9)—(15) 的实际点格比较；没有在缺少对应整升层定理时宣称存在同精度的 definite 本征函数。

## 5. 第一个 Bockstein 的完整范数正合列

在实际点格中有规范正合列
$$
 \boxed{\quad
 0\longrightarrow \Delta A_0
 \longrightarrow \Delta B
 \xrightarrow{\ \beta\ } NB/pB_0
 \longrightarrow0,
 \qquad
 \beta(\Delta Z)=NZ\bmod pB_0.
 \quad}
 \tag{16}
$$
证明如下。$\ker(\Delta:B\to B)=B_0$：在 $A_0\otimes\mathbb Q_p$ 的非平凡角色上 $\Delta$ 非零，在基层块上为零。
改变除点 $Z$ 因而只使其范数改变 $pB_0$，故映射良定义。
若 $NZ=pY$，则 $Z-Y\in A_0$，于是 $\Delta Z=\Delta(Z-Y)$；
这证明核准确为 $\Delta A_0$。满射由定义给出。

在 (1) 的奇数分支，
$$
 NB=\mathbb Z_pP_-+pB_0,\qquad
 NB/pB_0=\mathbb F_pP_-.
$$
对 $Q$ 使用 (16)，得到
$$
 \beta(Q)=\lambda_QP_-,\qquad
 \lambda_Q=f(0)\bmod p,\qquad
 \lambda_Q\ne0\iff a=1.
 \tag{17}
$$
(13) 经 (7) 评价，准确也得到 $\lambda_Q$，因为 $u_{q,n}(0)=1$。
当 $n=1$ 时 $U=T^2/(1+T)$，故这一值就是原第二矩除以固定负点的局部生成元。

任何实际 $\Delta$-除点都可以加上 $Y\in B_0$；它的范数随即加上 $pY$。
因此 (16) 自然落在 $B_0/pB_0$，与 §2.2 的有限群环事实一致。
既没有一个未经选择的更高中心值，也没有理由因为负点本身非零就认定 $\beta(Q)\ne0$。

## 6. 对当前主目标的准确用途

本篇给出原负号群环的完整整除法与任意精度的无损观测。
后续若要从原 definite 群环的高精度性质逼出 $a=1$，现在可以直接在同一 $\mathcal O^+$ 理想 $(f)$ 上进行，不必再支付局部比较成本。

仍欠的算术断言是：对 R156/R230 的同一联合无穷输入，$\beta(Q)$ 不总为零，或存在另一条不要求 $a=1$ 的初级有限性证明。
改变 $q$、增加 $n$ 和单位归一都不改变 (14) 的原理想。
本篇没有把这些可选择观测当作跨素数的非零证明。

### 依赖与来源

- R232：原负秩一输入后的真正 regular 点格、范数坐标和 $a$ 的奇数分支；本篇不改变 $Q$ 或原 Kolyvagin 首项。
- R234：原满像及域交条件、同符号 Chebotarev 定位、模 $p$ 的完整 definite 群环比较。
- Wei Zhang, *Selmer groups and the indivisibility of Heegner points*, Cambridge Journal of Mathematics **2** (2014), 191–253，§4.2，式 (4.7)–(4.9)。本篇仅在 $n=1$ 使用这一已发表比较。
  [发表版](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf)。
- §2 的所有有限群环断言、§3 的高精度选择及 §§4–5 的点格比较均已在本文给出证明。
