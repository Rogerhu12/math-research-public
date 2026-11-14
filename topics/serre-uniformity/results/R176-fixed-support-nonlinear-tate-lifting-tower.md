# R176：固定支撑的非线性 Tate 提升塔与 Robert 阻碍线

**状态：已证明。**

本文接续 R168、R171，研究**同一个全局首差类**的后阶提升。
带非零 Tate 惯性的首差类通常不能继续作线性上同调提升；
真实表示的乘法却含有二次交换子，这一项恰能抵消第一个局部缺陷。
局部抵消之后，保持同一个全局支撑及全部指定局部同构型，
仍有一个必须另外求值的全局阻碍。

在单素数情形 $\gamma_q=0,\lambda_q\ne0$，固定第一次模 $p^2$ 表示后，
每一级符合全部指定局部型的提升**至多有一个严格共轭类**；
每一级是否存在，由原始 Robert 单位线对偶的一个 $\mathbf F_p$ 标量决定。
本文确定这个标量的定义、独立性、对偶线和每一级的准确量词，
不把它宣称为已经算出的零或非零数值。

这里始终固定全部允许分歧的素数。
若实际分母还有更晚才出现的乘法素数，必须纳入新的局部问题；
本文的固定支撑阻碍不能直接用于排除这种变化支撑。
R171 的具体素数仍已被 Gaussian $5$ 条件排除，
只校验下面的表示论接口，不是实际椭圆曲线候选。

## 1. 设定与提升定理

令
$$
A:y^2=x^3-x,\qquad p>37,\quad p\equiv3\pmod4,
$$
$$
\mathcal M=\operatorname{ad}^0T_p(A)
=\mathbf Z_p(\eta)J\oplus\mathcal W,\qquad
M=\mathcal M/p=\mathbf F_p(\eta)J\oplus W,\qquad \eta=\chi_{-4}.
\tag{176.1}
$$
迹配对把 $M$ 与线性对偶识别；Tate 对偶为 $M(1)$。
固定
$$
R=\{q_1,\ldots,q_r\},\qquad q_i\equiv-1\pmod{4p},\qquad
S=\{2,p,\infty\}\cup R.
\tag{176.2}
$$

提升问题要求：

- 在 $S$ 外不分歧，行列式固定为 cyclotomic；
- 在 $p$、$2$ 处分别与 $T_p(A)$ 的完整局部表示同构；
- 每个 $q_i$ 处固定乘法符号 $\epsilon_i\in\{1,-1\}$，
  并固定一个惯性恰在 $p$ 深度开始的整 Tate 同构型。

因此每个 $q_i$ 的第一惯性系数非零；
全体允许的 Tate 支撑都已在模 $p^2$ 层出现。
没有把可能含有更深素数的“最小支撑”当成全部分母支撑。

使用 R168 的单位行 $\gamma$ 和矩阵 $C$：
严格 $p$ 条件的 $W$ 类具有奇异坐标 $b$ 当且仅当 $\gamma b=0$，
且其有限坐标为 $a=Cb$。记
$$
D_\epsilon=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_r),\qquad
\mathcal B=\begin{pmatrix}\gamma\\C\end{pmatrix}D_\epsilon,\qquad
h=\dim_{\mathbf F_p}\ker\mathcal B.
\tag{176.3}
$$

**定理 176.1。**
设 $m\ge2$，$\rho_m:G_{\mathbf Q,S}\to
\operatorname{GL}_2(\mathbf Z/p^m)$ 已满足以上行列式和全部局部同构型，
其模 $p$ 约化为 $A[p]$。则：

1. 不保留指定局部同构型时，$\rho_m$ 总有一个同支撑、
   同固定行列式的普通全局模 $p^{m+1}$ 提升。
2. 恢复全部指定局部同构型的阻碍落在一个维数为 $h+1$ 的
   $\mathbf F_p$ 商空间中。
3. 阻碍消失时，符合全部局部型的提升按全局严格共轭分类，
   构成维数为 $h$ 的仿射空间。

这些空间由同一个残余模 $M$、支撑 $R$、符号 $\epsilon$
和 R168 的矩阵决定，不需要为每一级换一个素数。

当 $r=1,\gamma_q=0,C=(\lambda_q)$ 且 $\lambda_q\ne0$ 时，$h=0$。
阻碍空间的 Tate 对偶恰好是原始 Robert 单位线 $\mathcal D_p$。
选其非零生成元 $d_0$；任一普通全局提升在 $p$ 处的偏差
$z_{p,m}\in H^1(\mathbf Q_p,M)$ 给出阻碍标量
$$
\Omega_m=\langle z_{p,m},\operatorname{loc}_p(d_0)\rangle_p\in\mathbf F_p.
\tag{176.4}
$$
其零性与所有选择无关。符合全部局部型的下一层存在当且仅当
$\Omega_m=0$，存在时严格共轭类唯一。

## 2. 线性奇异类的确切寿命

固定 $q\equiv-1\pmod{4p}$，令 $d=v_p(q+1)$。
完整 Frobenius 矩阵 $\varphi$ 满足 $\varphi^2=-qI$。
取 $r_q=\sqrt{-q}\in1+p\mathbf Z_p$，令
$F=\varphi/r_q$、$K_0=JF$。则
$$
F^2=K_0^2=I,\qquad J^2=-I,\qquad FJ=-JF,
$$
$$
\operatorname{Ad}(\varphi):
F\longmapsto F,\qquad J\longmapsto-J,\qquad K_0\longmapsto-K_0.
\tag{176.5}
$$

局部 tame 上同调给
$$
H^1_{\rm sing}(\mathbf Q_q,\mathcal M/p^k)
\simeq\ker\bigl(\operatorname{Ad}(\varphi)-q\bigr).
$$
由于 $q-1$ 是 $p$ 单位，
$$
H^1_{\rm sing}(\mathbf Q_q,\mathcal M/p^k)
=
\operatorname{Ann}_{\mathbf Z/p^k}(q+1)J
\oplus\operatorname{Ann}_{\mathbf Z/p^k}(q+1)K_0,
\tag{176.6}
$$
$$
\operatorname{Ann}_{\mathbf Z/p^k}(q+1)
=p^{\max(k-d,0)}\mathbf Z/p^k.
\tag{176.7}
$$
对 $\mathcal W$ 只保留 $K_0$ 项，对 $\eta J$ 只保留 $J$ 项。

所以一个模 $p$ 奇异坐标非零的线性类，只可能线性提升到 $k\le d$。
在 $k=d+1$ 时，所有奇异类约化到模 $p$ 都为零。
特别地，$d=1$ 时非零模 $p$ 奇异类没有线性的模 $p^2$ 提升。
整格中更有
$$
H^1_{\rm sing}(\mathbf Q_q,\mathcal M)=0,
\tag{176.8}
$$
因为非零整数 $q+1$ 不能杀死非零 $\mathbf Z_p$ 向量。
这不是关于真实椭圆曲线表示的排除：其高层相对首差不是线性 cocycle。

对偶目标的大小也精确可见。
Frobenius 在 $\mathcal W(1)$ 的 $F,K_0$ 上分别为 $q,-q$，故
$$
H^1_{\rm unr}(\mathbf Q_q,\mathcal W(1))
\simeq\mathbf Z_p/(q+1)\cdot K_0.
\tag{176.9}
$$
若 $d=1$，这个整局部目标已被 $p$ 杀死。
任一真正整对偶类若在此目标的模 $p$ 约化为零，其整未分歧定位便为零。
这不预设给定的模 $p$ 全局类有整提升；只确定线性局部目标的大小。

## 3. 真正的相对首差满足 BCH 乘法

若整表示 $\rho_E\equiv\rho_A\pmod{p^n}$ 且行列式相同，写
$$
U(g)=\rho_E(g)\rho_A(g)^{-1}
=\exp(p^nX(g)),\qquad X(g)\in\mathcal M.
\tag{176.10}
$$
$p>3$ 保证矩阵对数、指数收敛；行列式 $1$ 给 $\operatorname{tr}X(g)=0$。
由 $U(gh)=U(g)\,gU(h)$，
$$
X(gh)=X(g)+gX(h)
+\frac{p^n}{2}[X(g),gX(h)]+O(p^{2n}).
\tag{176.11}
$$
所以 $X\bmod p^n$ 是线性 cocycle，
但下一层必须保留交换子。
当 $v_p(q+1)=n$ 时，线性奇异类第一次失败的层，
恰是这个非线性项开始起作用的层。

在深度 $n=1$，设 $c=X\bmod p$。
令 $\beta(c)$ 为
$$
0\longrightarrow M\longrightarrow\mathcal M/p^2
\longrightarrow M\longrightarrow0
$$
的 Bockstein，微分采用
$d\widetilde c(g,h)=g\widetilde c(h)-\widetilde c(gh)+\widetilde c(g)$。
普通二阶提升的阻碍为
$$
\operatorname{ob}(c)
=\beta(c)+\frac12[c\smile c]
\in H^2(G_{\mathbf Q,S},M),
\tag{176.12}
$$
括号杯积由 $[c(g),g c(h)]$ 表示。
此类为零当且仅当存在固定行列式的普通模 $p^3$ 提升。
指定局部型还需要后面的全局相容性。

在整分解 $\eta J\oplus\mathcal W$ 下，
$[J,J]=0$、$[J,\mathcal W]\subset\mathcal W$、
$[\mathcal W,\mathcal W]\subset\eta J$。
因此，$W$ 的自交换子可以补偿 $\eta$ 的 Bockstein，
交叉交换子又进入 $W$ 阻碍。
不能把反循环首差角色单独提升失败当成整个表示提升失败。

## 4. 完整 Tate 局部模型及 R168 的抵消式

在 (176.5) 的基中令
$$
N_\epsilon=J+\epsilon K_0,\qquad N_\epsilon^2=0,\qquad
\Phi_\epsilon=\epsilon\frac{q+1}{2}I+\frac{1-q}{2}F.
\tag{176.13}
$$
直接相乘得
$$
\det\Phi_\epsilon=q,\qquad
\Phi_\epsilon N_\epsilon\Phi_\epsilon^{-1}=qN_\epsilon.
\tag{176.14}
$$
取 tame 生成元的作用为
$$
\Theta=I+p\mu N_\epsilon,\qquad \mu\in\mathbf Z_p^\times,
\tag{176.15}
$$
便给出惯性深度恰为 $1$ 的整 Tate 局部同构型。
$q-1$ 为 $p$ 单位，Tate 参数的单位部分没有整 $p$-Kummer 贡献；
此模型也可由具有相应正整数赋值的 Tate 参数及整基变换实现。

设首差坐标为
$$
D=x(J+\epsilon K_0),\quad
c(\operatorname{Frob}_q)=aF\pmod{\text{coboundary}},\quad x\ne0,
\qquad u=(q+1)/p\bmod p.
$$
用 $[F,J+\epsilon K_0]=-2\epsilon(J+\epsilon K_0)$，
tame 关系模 $p^3$ 的负特征部分为
$$
\operatorname{pr}_{-}\!\left(
\rho(\operatorname{Frob}_q)\rho(\tau_q)
\rho(\operatorname{Frob}_q)^{-1}-\rho(\tau_q)^q\right)
=
p^2(2\epsilon a-u)D\pmod{p^3}.
\tag{176.16}
$$
因此抵消条件正是
$$
a=\epsilon\frac{q+1}{2p}\pmod p,
\tag{176.17}
$$
即 R168 的实际非齐次式。
反过来，(176.13)–(176.15) 给出匹配该首差的整局部目标；
这不只是形式上的必要条件。

R171 给
$$
x=-1,\quad b=-\epsilon,\quad a=27\epsilon,\quad u=11,
$$
于是 $2\epsilon a-u=54-11=0\pmod{43}$。
非零奇异类没有线性的模 $43^2$ 提升，
但非线性 tame 缺陷确被抵消。
这仍未证明全局固定局部型的提升存在。

## 5. 普通全局 $H^2$ 障碍由局部完全检测

首先，
$$
H^1(G_{\mathbf Q,S},\eta(1))=0.
\tag{176.18}
$$
用 $\mathbf Q(i)$ 的 Kummer 序列即可证明：
$\mathbf Z[i]$ 类数为 $1$，单位没有奇数 $p$ 挠；
$p$、全部 $q_i$ 惰性，$2$ 只有一个分歧素理想。
$S$-单位由这些有理素数、$1+i$、四次单位根生成。
共轭把 $1+i$ 变成 $-i(1+i)$，
四次单位根模 $p$ 次幂为零，故所有 $S$-单位类都在正部分。
这里确实使用 $\eta=\chi_{-4}$ 和全部新增素数惰性的假设。

其次，
$$
H^1(G_{\mathbf Q,S},W(1))=\mathcal D_{p,R}.
\tag{176.19}
$$
其中一个类若全部局部定位为零，其 $R$ 奇异坐标为零，
由 R168 的正合列落在 $\mathcal D_p$；
再由 R161 的 $p$ 定位注入，它为零。因此
$$
\Sha^1_S(\eta(1))=\Sha^1_S(W(1))=0.
\tag{176.20}
$$
Poitou–Tate 对偶给 $\Sha^2_S(M)=0$。
还须保留正合列末端：
$$
H^0(G_{\mathbf Q,S},M(1))
=H^0(\eta(1))\oplus H^0(W(1))=0.
\tag{176.21}
$$
前者有非平凡 cyclotomic 惯性，后者由 R161 的 Cartan 字符为零。
所以不是仅有单射，而是同构
$$
H^2(G_{\mathbf Q,S},M)\xrightarrow{\sim}
\bigoplus_{v\in S}H^2(\mathbf Q_v,M)
=\bigoplus_{q\in R}H^2(\mathbf Q_q,M).
\tag{176.22}
$$
$p$ 处 $H^0(M(1))=0$；
$2$ 处 $Q_8$ 惯性没有相应不变量；
实处奇数 $p$ 的 $H^2$ 为零。
每个 $q$ 处 $H^0(M(1))$ 维数为 $2$，故全局 $H^2$ 维数为 $2r$。

给定任一层 $\rho_m$，任取保持行列式的矩阵提升。
其乘法误差在 $I+p^mM$ 中给出普通 $H^2(G_{\mathbf Q,S},M)$ 类。
各局部都来自指定的整局部目标，所以该类在所有局部为零。
由 (176.22)，普通全局提升存在。
这个证明对每个 $m\ge2$ 都成立。

## 6. 下一层的局部比较线

普通全局提升未必保持全部局部目标。
在 $p$ 处，局部残余绝对不可约给
$$
\operatorname{End}_{G_{\mathbf Q_p}}(A[p^m])=\mathbf Z/p^m;
\tag{176.23}
$$
证明是逐级减去标量再除以 $p$。
因此保持完整 $p$ 处同构型的差异子空间为 $L_p=0$。
$2$ 处 $H^1(M)=0$ 也不给差异参数。

这里的 $p$ 条件**强于普通有限平坦条件**。
R19 的实际曲线在 $p$ 好超奇异；由 $p>3$ 的 Hasse 界，
$a_p(E)=a_p(A)=0$。R157 §2 的晶体唯一性、稳定格唯一性和
有限层标量对齐，才使它满足这里的完整局部型。
R161 的有限平坦切线是一维 $W$ 方向；固定完整局部型把这条方向也杀掉。
因此最小 $R=T$ 或一般 level raising 给出的有限平坦模形式，
不能自动消去下文的 $\Omega_m$：其 $a_p$ 可以变化，
并不固定这里的晶体对象。
在 $2$ 处，实际曲线满足指定型则由 R114 §2.2：
共同 $Q_8$ 惯性核先对齐完整惯性，Frobenius 之比为标量；
固定行列式及模 $p$ 同余迫该标量为 $1$。

在 $q$ 处，Tate Frobenius 的两个特征值之差为 $p$ 单位，
故模 $p^m$ 自同构必须对角。
与 $I+p\mu N_\epsilon$ 交换又迫两个对角项之差被 $p^{m-1}$ 整除。
除去标量，其自同构恰为
$$
I+p^{m-1}zF\pmod{p^m}.
\tag{176.24}
$$
提升到下一层时 Frobenius 不变，惯性变化为
$$
p^m z\mu[F,N_\epsilon]\pmod{p^{m+1}}.
$$
$\mu\ne0\bmod p$ 保证得到且只得到整条奇异线
$$
L_q=\mathbf F_p(J+\epsilon K_0)\subset H^1(\mathbf Q_q,M),
\tag{176.25}
$$
其有限 $F$ 坐标为零。
这个计算对每个 $m\ge2$ 相同。

**这是已经固定非零首惯性项的 $\rho_m$ 之上的局部比较线，
不是未分歧残余点处整个 special 变形环的切空间。**
原始首差通常有非零有限坐标，所以本身不在 $L_q$；
后面的差异 Selmer 为零不与首差存在矛盾。

全局残余绝对不可约也使模 $p^m$ 全局自同构只有标量。
普通全局提升按严格共轭分类后，是
$H^1(G_{\mathbf Q,S},M)$ 的仿射空间，没有额外非标量全局自同构商。

## 7. 固定局部型的阻碍商

令
$$
\mathcal V=
H^1(\mathbf Q_p,M)\oplus
\bigoplus_{q\in R}H^1(\mathbf Q_q,M)/L_q,
$$
$$
\operatorname{res}:H^1(G_{\mathbf Q,S},M)\longrightarrow\mathcal V.
\tag{176.26}
$$
选一个普通全局提升并逐处与整局部目标比较。
其偏差在 $\mathcal V$ 中的像，模去 $\operatorname{im}(\operatorname{res})$，为
$$
\operatorname{Obs}_m(\rho_m)\in\operatorname{coker}(\operatorname{res}).
\tag{176.27}
$$
改变普通全局提升增加全局 $H^1$ 类；
改变局部比较同构增加 $L_q$。
故这个仿射阻碍良定义，为零当且仅当能同时保留所有局部型；
为零时解集的差异空间为
$$
H^1_L(G_{\mathbf Q,S},M)=\ker(\operatorname{res}).
\tag{176.28}
$$

维数逐项为
$$
\dim H^1(\mathbf Q_p,M)=3,\qquad
\dim H^1(\mathbf Q_q,M)=3,\qquad \dim L_q=1,
$$
$$
\dim\mathcal V=3+2r.
\tag{176.29}
$$
第一式也可拆成 $\eta$ 的 $1$ 维和 $W$ 的 $2$ 维。
$q$ 处 $H^0(M)$ 维数为 $1$、$H^0(M(1))$ 维数为 $2$。
全局 $H^0(M)=0$、$H^2$ 维数为 $2r$，
复共轭在 $M$ 上的负特征维数为 $2$。
Euler–Poincaré 公式给
$$
\dim H^1(G_{\mathbf Q,S},M)=2r+2.
\tag{176.30}
$$

严格 $p$ 的 $\eta J$ 类由奇异坐标
$x\in\mathbf F_p^r$ 唯一确定：
$\mathbf Q(i)$ 类数为 $1$，各惰性射线素数给一个独立 $p$ 角色。
对 $W$，R161、R168 给精确条件
$\gamma b=0$、$a=Cb$。
落在 (176.25) 内恰要求 $b=D_\epsilon x$、$a=0$，所以
$$
H^1_L(G_{\mathbf Q,S},M)
\simeq
\ker\left(\begin{pmatrix}\gamma\\C\end{pmatrix}D_\epsilon\right).
\tag{176.31}
$$
其维数为 $h$，合并维数即得
$$
\boxed{\dim\operatorname{coker}(\operatorname{res})=h+1.}
\tag{176.32}
$$
改变 $q$-单位基 $d_j\mapsto d_j+t_jd_0$ 只给 $C$ 增加
由 $\gamma$ 生成的行；保留 $\gamma$ 后，核、秩和阻碍维数均不变。

## 8. 对偶空间与 Robert 标量

写 $M$ 的有限坐标为 $aF$、奇异坐标为 $xJ+bK_0$；
$M(1)$ 的有限坐标为 $c_\eta J+c_WK_0$、奇异坐标为 $dF$。
R168 的杯积及
$\operatorname{tr}J^2=-2$、
$\operatorname{tr}F^2=\operatorname{tr}K_0^2=2$ 给配对
$$
2(ad+xc_\eta-bc_W).
\tag{176.33}
$$
因此 $L_q^\perp$ 要求 $c_\eta=\epsilon c_W$。
(176.18) 已使全局 $\eta(1)$ 类为零，
所以全局对偶条件恰是每个 $q$ 的 $W(1)$ 有限坐标为零。

在 R168 的基 $d_0,d_1,\ldots,d_r$ 中，系数 $t_0,v$ 的有限坐标为
$\gamma^{\mathsf t}t_0+C^{\mathsf t}v$。
Poitou–Tate 因而识别
$$
\boxed{
\operatorname{coker}(\operatorname{res})^\vee
\simeq
\ker\begin{pmatrix}\gamma^{\mathsf t}&C^{\mathsf t}\end{pmatrix}
\subset\mathcal D_{p,R}.}
\tag{176.34}
$$
其维数为 $h+1$，也核对了 (176.32)。

单素数 $\gamma_q=0,\lambda_q\ne0$ 时，(176.34) 迫 $v=0$，
只余原始 Robert 线 $\mathbf F_pd_0$。
$d_0(q)=0$、$d_0(p)\ne0$，全局配对只剩
$$
\Omega_m=\langle z_{p,m},\operatorname{loc}_p(d_0)\rangle_p.
\tag{176.35}
$$
更换普通全局提升产生全局 $H^1$ 偏差；
全局互反及 $d_0(q)=0$ 说明该数值不变。
更换 $d_0$ 的非零生成元仅乘一个非零常数，零性不变。

这给出一个真正的后阶计算目标：
计算同一个全局提升在 $p$ 处的非线性偏差，
并与已经原始生成的 Robert 单位配对。
仅知生成性、$d_0(q)=0$ 或 $\lambda_q\ne0$，
都不能推出这个新标量为零。

## 9. 唯一提升塔与固定 $q$ 的同源类限制

当 $\gamma_q=0,\lambda_q\ne0$，
初始模 $p^2$ 类固定后，每一级必须检验同一个全局对象的 $\Omega_m$。
若非零，则不存在符合全部固定局部型的下一层；
若为零，则下一层严格共轭类唯一。
只有在同一个固定素数上全部标量都消失，才能得到完整整表示。

如果全塔存在，唯一的相容共轭类可以逐级选成相容矩阵，
逆极限给连续 $\mathbf Z_p$ 表示。
各处与固定整局部目标的同构由紧致性取极限，
因此 $p$ 处表示和 Tate 类型确实保留。
这不是把每个有限层分别选出的不同素数拼成整对象。

对原问题还有一个固定支撑推论。
假设实际曲线唯一的新增乘法素数为 $q$、惯性深度为 $1$，
且 $\gamma_q=0,\lambda_q\ne0$。
始终使用 R168 的同一个 $A[p]$ 标架、$J=[i]$、
Frobenius 正特征线及 $\zeta=e(v,Jv)$ 的 tame 规范。
这里准确的最大同余深度为 $1$，不能混入首差在更高层才出现的曲线。
R168 已唯一确定
$$
x_q=\frac{q+1}{2p\lambda_q}\pmod p.
\tag{176.36}
$$
固定乘法符号 $\epsilon$ 后，严格 $p$ 的 $\eta$、$W$ 类
由各自奇异坐标唯一确定，故模 $p^2$ 首差类唯一。
实际惯性非零还迫 $v_p(q+1)=1$；否则 (176.36) 的右端为零。

这里没有隐藏的 $\mu$ 或残余同构参数。
两个深度为 $1$ 的 Tate 模型的系数都为 $p$ 乘单位；
用对角整单位基变换缩放 $N_\epsilon$，可使两个模型完全同构。
实际残余全局同构 $E[p]\simeq A[p]$ 只差标量，
其作用于首差的共轭为恒等；改变整提升只增加 coboundary。
Weil 乘数的平方类仍须满足 R168 的实际平方条件，
但不额外改变这里按 $\operatorname{GL}_2$ 同构分类的表示：
本文没有要求两条曲线的同构为指定的辛同构。
随后所有高层至多唯一。因此：

> 对固定 $p,q,\epsilon$，满足这些条件的实际曲线，
> 至多属于一个 $\mathbf Q$-同源类。

两条这样的曲线具有同构的完整 $p$-adic Tate 表示，
Faltings 同源定理给结论。
这不是“至多一条有理同构类”的结论，不声称同源类存在，
也不产生变化 $q,p$ 的绝对界。
R171 给 $x_q=-1$，但 Gaussian $5$ 已使该实例的实际同源类集合为空；
本文没有为这个已排实例计算无关的无限塔。

## 10. 变化支撑边界与尚未求出的量

定理的 $S$ 是整个允许分歧集合。
若分母有更高惯性深度的素数，它在模 $p^2$ 可以尚未显现，
却在后面带来新的全局 $H^1$ 调整方向和新的 Tate 比较条件。
此时不能沿用旧的 $\mathcal V$、$\mathcal B$ 或一维阻碍商。

若新增素数在 $\mathbf Q(i)$ 中分裂，
(176.18) 的 $S$-单位负部也可能非零，
维数与对偶生成元必须重算。惰性假设不是记号上的方便。

本文没有给出任一个 $\Omega_m$ 的新数值。
已证明的是：在指定的固定支撑分支，真实后阶问题落在一个准确、
每级相同的全局阻碍空间；单素数且斜率非零时，
这条空间由原始 Robert 单位直接对偶。
O6 仍需把这些阻碍与真正全支撑、原始整数方程及更深惯性素数联立。

## 11. 来源定位

- R157：超奇异处整局部同构与有限层标量对齐；
  R161：严格 $p$ Selmer、$\mathcal D_p$ 定位注入及局部维数；
  R163：原始 Robert 全 $p$ 生成性；
  R168：$q$-单位矩阵、杯积和整数 $q+1$ 非齐次式；
  R171：$\gamma_q=0,\lambda_q=16$ 的精确证书。
- J. S. Milne，Arithmetic Duality Theorems，第二版（2006），
  I Theorem 4.10（正文页 57）、I Theorem 5.1（正文页 67），
  [全文](https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf)。
  特别保留 $H^0(M(1))=0$ 的末端条件，才得到 (176.22) 的满射。
- G. Faltings，Endlichkeitssätze für abelsche Varietäten über Zahlkörpern，
  Invent. Math. 73 (1983), 349–366，§5 Theorems 3、4（正文页 360–361），
  [原刊扫描](https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)。
  对两曲线的积应用该定理，给出完整 Tate 表示同构推出有理同源。

