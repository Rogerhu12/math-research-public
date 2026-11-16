# R921. 原惰性位的完整残余局部矩阵与整 Bockstein

日期：2026-11-16。**状态：下列局部复形、两条残余线、全矩阵及整提升判据已证明。** 本篇使用 R908 的同一原四角色、同一 tame 生成元和算术 Frobenius；尤其保留 $h=p^{v_p(q+1)}$、$u=(q+1)/h$，不把 u 改为1。

核心区别是：原整类的约化只占一条局部线；残余系数上还有一条由 $H^0$ 连接映射产生的线。后者经原 induced/Shapiro 映射为零，但它的整 Bockstein 完全非零。故新增惰性位的原几何局部零不能直接删掉 residual descent 中的这条线。本文没有证明任何原全局类非零、没有推出 ordinary p 位的局部化单射或 R893 的 $s=0$。

以下全为符号证明，没有数学程序执行。

## 1. 原对象、局部方向及系数

固定原普通 $p>211$ 和原最高角色格 $\mathcal T$。允许使用 R897 已固定的同一有界格 $p^{-c_p}T$，但全文不再改变这份格。原三组 $(j,k)$、finite Artin 标签、CM 符号、$q/q^4$ 端点、$X_1/X_0$ 倍率和 $C_5=-216$ 全保。

取新的惰性 q，满足
$$
q\nmid30\cdot34p,\qquad
h=p^e,\quad e=v_p(q+1)>0,\qquad
u=(q+1)/h\in\mathbf Z_p^\times .
\tag{1}
$$
在原 $K=\mathbf Q(\omega)$ 的 q 位，剩余域为 $\mathbf F_{q^2}$。
R908(5)–(6)已逐项核定原四个角色的算术 Frobenius 都为
$$
F|_{\mathcal T}=-q .
\tag{2}
$$
特别最高角色是 $\lambda/\mathbf N$，不是未作 Tate twist 的
$\lambda$。本文只选其一条原符号线写矩阵；原其它三槽在此位的
同一局部矩阵也成立，但其全局 Selmer/根数结论不因此相同。

令 $\tau$ 为原 tame pro-p 惯性生成元，取向使其在
$R\otimes\mathcal T$ 上作用为 $\sigma$。令 F 在原
$G_q=\langle\sigma\rangle=C_h$ 上的像为一。则
$$
F\tau F^{-1}=\tau^Q,\qquad Q=q^2,\qquad
\tau|_{\mathcal T}=1.
\tag{3}
$$
原 $K[q]_w/K_v$ 是全分歧 tame h 次扩张。所有旧、与 q 互素的
ring-class 层和反循环 wild 层在 q 完全分裂；下文最后恢复
这些全部上方素点。

置
$$
R=\mathcal O[C_h],\quad N=\sum_{i=0}^{h-1}\sigma^i,\quad
A=R/(N),\quad I=(\sigma-1)R,\quad j=\sigma-1,
$$
$$
d_R=\sum_{i=1}^{h-1}i\sigma^i,\qquad d_A=d_R\bmod N,\qquad
c=(Q-1)/h=(q-1)u .
\tag{4}
$$
整同构 $j:A\to I$ 是 R901/R908 的那一个，不是 A 上的 j
自乘。后者在模 p 后可能有核，前者模任何 $p^m$ 仍是同构。
两条准确恒等式为
$$
j d_R=h-N,\qquad j d_A=h,\qquad
N_Q:=\sum_{i=0}^{Q-1}\sigma^i=1+cN .
\tag{5}
$$

固定
$$
1\le m\le e,\qquad B=\mathcal O/p^m\mathcal O,\quad
R_B=R\otimes B,\quad A_B=A\otimes B .
\tag{6}
$$
即使 $\mathcal O/\mathbf Z_p$ 分歧，(6)仍按理性 p 的幂定义；
$h=0$ 于 B，u 始终为单位。为缩短记号，选择原 $\mathcal T$
的一个固定基，将张量 $\mathcal T/p^m$ 隐含在下面矩阵中。
更换该基只同时缩放全部坐标。

## 2. 完整 tame cochain 复形

使用原规范
$$
z(gh)=z(g)+g z(h),\qquad
(\delta x)(g)=(g-1)x.
\tag{7}
$$
写 $a=z(\tau)$、$b=z(F)$，从(3)直接得
$$
(F-N_Q)a-(\sigma-1)b=0.
\tag{8}
$$
这些系数的 wild pro-q 及作用平凡的 prime-to-p 部分正阶上同调为零。
其余 tame inertia $\mathbf Z_p$ 和 unramified $\mathbf Z_p$
各用两项复形，再取 mapping cone，给
$$
C^0(M)=M,\qquad C^1(M)=M\oplus M,\qquad C^2(M)=M
\tag{9}
$$
以及
$$
d^0(x)=(jx,(-q-1)x),\qquad
d^1(a,b)=(-q-N_Q)a-jb .
\tag{10}
$$
此 mapping-cone描述也支付连续性：惯性与 unramified
$\mathbf Z_p$ 的有限连续商相容取极限，(8)正是半直积的唯一
兼容式。不是仅在两个抽象生成元上任选不连续函数。

在整 A 系数上，$N=0$，所以
$$
\boxed{
d_A^0(x)=(jx,-uhx),\qquad
d_A^1(a,b)=-uha-jb .
}
\tag{11}
$$
在整 R 系数上则必须保 cN：
$$
\boxed{
d_R^0(x)=(jx,-uhx),\qquad
d_R^1(a,b)=-uha-cNa-jb .
}
\tag{12}
$$
在原一维 $\mathcal T$ 上，$\tau=1$、$N_Q=Q$，故
$$
d_{\mathcal T}^0(x)=(0,-uhx),\qquad
d_{\mathcal T}^1(a,b)=-quh\,a .
\tag{13}
$$
(12)的 cN 项不能只因 $Q\equiv1\pmod{p^m}$ 而删除：
$N_Q$ 是群环和，不是整数 Q。这个项决定下面 singular 基的
准确 F 坐标。

## 3. 整类的唯一局部线及 H²

整 A 上 j 单射，且 $jd_A=h$。由(11)，所有整 cocycle
准确为
$$
(a,-ud_Aa),\qquad a\in A.
$$
coboundary对应 $a\in jA$。因此
$$
H^0(K_v,A\otimes\mathcal T)=0,\qquad
H^1(K_v,A\otimes\mathcal T)\simeq\mathcal O/(h),
$$
$$
H^2(K_v,A\otimes\mathcal T)
=A/(hA+jA)\simeq\mathcal O/(h).
\tag{14}
$$
两份同构都保原 $\mathcal T$ 基；H¹用 tame 值模 j，
H²用(9)末项模 j。因为 $h=jd_A$，末式没有额外商。

整 H¹ 的生成 cocycle为
$$
L_{\rm int}=(1,-ud_A).
\tag{15}
$$
R908 的原 $j:A\to I\subset R$ 把它送到 unramified
Shapiro 坐标 u：减去 $\delta1$ 后，
$$
(j,-u(h-N))-(j,-uh)=(0,uN).
\tag{16}
$$
这再次核定正号，且没有除 h。

## 4. A_B 的两条线：满生成与独立

约到(6)，(11)成为
$$
d^0(x)=(jx,0),\qquad d^1(a,b)=-jb .
\tag{17}
$$
有
$$
A_B/jA_B\simeq B,\qquad \ker(j:A_B\to A_B)=B\,d_A.
\tag{18}
$$
第一式由 $N$ 在 $\sigma=1$ 处为 $h=0$ 得到。
第二式可以逐系数核定：若 $jx=tN$ 于 $R_B$，
其系数满足 $x_{i-1}-x_i=t$，所以模 BN 后
$x=-t\,d_A$。反之(5)给 $jd_A=0$。
$d_A$ 的 B-倍数没有非零 annihilator：
在基 $1,\sigma,\ldots,\sigma^{h-2}$ 中消去
$\sigma^{h-1}$ 后，$d_A$ 有一个系数为−1。
这证明(18)的满生成与 B-自由性。

于是
$$
H^1(K_v,A_B\otimes\mathcal T)
 =\{(a,b):b\in Bd_A\}/\{(jx,0)\}
 \simeq B^2.
\tag{19}
$$
定义准确的两条基线
$$
\boxed{
L=[(1,-ud_A)],\qquad C=[(1,0)] .
}
\tag{20}
$$
若按 $(a\bmod j,\ b/d_A)$ 写坐标，则 L、C 的矩阵是
$$
\begin{pmatrix}1&1\\-u&0\end{pmatrix},
\qquad\det=u\in B^\times.
\tag{21}
$$
所以两线独立并生成**全部**残余 H¹。
L 是(15)的整约化；C 还不能称为一个整类的约化。

H⁰、H²同时为
$$
H^0(K_v,A_B\otimes\mathcal T)=Bd_A,\qquad
H^2(K_v,A_B\otimes\mathcal T)=B .
\tag{22}
$$

## 5. 原 induced/Shapiro 群的 unramified 与 singular 基

约化(12)给
$$
d_R^0(x)=(jx,0),\qquad d_R^1(a,b)=-cNa-jb .
\tag{23}
$$
定义
$$
\boxed{
U=[(0,N)],\qquad S=[(1,c\,d_R)] .
}
\tag{24}
$$
由于 $jd_R=-N$ 于 $R_B$，S确为 cocycle。
任一 cycle可先用 coboundary将 a 改成其 augmentation
$a_0\in B$；随后(23)迫
$b-cd_Ra_0\in\ker j=BN$。
这证明(24)独立、满生成，因而
$$
H^1(K_v,R_B\otimes\mathcal T)=BU\oplus BS .
\tag{25}
$$

这些名字是实际局部 Shapiro 坐标。
identity coset上的 evaluation使
$$
U:\ z(\tau^h)=0,\ z(F)=1;
\qquad
S:\ z(\tau^h)=1,\ z(F)=0.
\tag{26}
$$
第二式用 $z(\tau^h)=Na$、N的identity系数1，
及 $d_R$ 的identity系数0。
因此 U是全分歧扩张上真正的 unramified 基，S是真正的
singular 基；没有用一个未校准的形式分解。

原 $\mathcal T/p^m$ 在 $K_v$ 上同样有
$$
U_0=[(0,1)],\qquad S_0=[(1,0)]
\tag{27}
$$
作为基，因为(13)约化后两个微分都为零。
两群的惯性生成元分别是 $\tau^h$ 与 $\tau$，不可先相认。

## 6. 全部映射的准确矩阵

考虑整短正合列及其约化
$$
0\longrightarrow A\otimes\mathcal T
 \xrightarrow{\,j\,}R\otimes\mathcal T
 \xrightarrow{\,\epsilon\,}\mathcal T
\longrightarrow0.
\tag{28}
$$
这里第一个箭头用 $A\simeq I$；商是 $\mathcal O$-free，
故约化后仍短正合。

### 6.1 j 与实际 corestriction

由(16)，$j_*L=uU$。
另一方面 $j_*C=[(j,0)]=[\delta1]=0$。
所以
$$
\boxed{
[j_*]_{(L,C)\to(U,S)}
=\begin{pmatrix}u&0\\0&0\end{pmatrix}.
}
\tag{29}
$$
augmentation 在 Shapiro 下正是原全分歧 h 次扩张的
corestriction；并非任选的一个素点投影。
由于
$$
\epsilon(N)=h=0,\qquad
\epsilon(d_R)=h(h-1)/2=0\quad\text{于 }B,
$$
有
$$
\epsilon_*U=0,\qquad \epsilon_*S=S_0,
$$
即
$$
\boxed{
[\epsilon_*]_{(U,S)\to(U_0,S_0)}
=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
}
\tag{30}
$$
在这里2为单位；h是奇数。式(30)把 unramified 上的 h 倍
与 singular 上的单位返回区别开来。

### 6.2 两个连接映射与 H⁰/H²

(28)的 H⁰连接满足
$$
\boxed{\partial_0(1)=C.}
\tag{31}
$$
证明是在 R_B 中以1提升 $\mathcal T/p^m$ 的不变元。
其 coboundary是 $(j,0)$，经 $j^{-1}:I_B\to A_B$ 得
$(1,0)$，正是 C。故这条线有明确来源；不能用原
整 $H^0=0$ 将残余的 $H^0(\mathcal T/p^m)=B$ 删除。

后一个连接映射准确为
$$
\boxed{\partial_1(U_0)=-1,\qquad\partial_1(S_0)=0}
\quad\text{于 }H^2(A_B\otimes\mathcal T)=B.
\tag{32}
$$
对 $U_0=(0,1)$，取 R_B提升后(23)给 $-j$；
用 $j^{-1}$得到−1。
对 $S_0=(1,0)$，得到 $-cN=j(c d_R)$，
而 $d_A\bmod j=h(h-1)/2=0$，故其 H² 类为0。

其余两端也全部核定：
$$
H^0(A_B)\ni d_A\xmapsto{j}-N\in H^0(R_B),\qquad
H^0(R_B)\xrightarrow[\ 0\ ]{\epsilon}H^0(B),
$$
$$
H^2(A_B)\xrightarrow[\ 0\ ]{j}H^2(R_B),\qquad
H^2(R_B)\xrightarrow{\epsilon}H^2(B)
\text{ 为 }1.
\tag{33}
$$
因此(29)–(33)确组成完整长正合列，而非只给几条兼容箭头。

## 7. 整 Bockstein 精确识别不可提升线

现在使用另一个短正合列
$$
0\longrightarrow A\otimes\mathcal T
 \xrightarrow{p^m}A\otimes\mathcal T
 \longrightarrow A_B\otimes\mathcal T
 \longrightarrow0 .
\tag{34}
$$
记其 Bockstein为
$$
\beta_m:H^1(A_B\otimes\mathcal T)
 \longrightarrow H^2(A\otimes\mathcal T)[p^m].
$$
因为 L有真正的整 cocycle提升(15)，
$$
\beta_m(L)=0.
$$
对 C的残余倍数 $x\in B$，取任一 $\widetilde x\in\mathcal O$
提升，使用 cochain $(\widetilde x,0)$。
由(11)，其差分是 $-uh\widetilde x$；除 $p^m$ 后得到
$$
\boxed{
\beta_m(xC)
=-u\,\frac{h}{p^m}\,\widetilde x
\pmod h.
}
\tag{35}
$$
由于 $m\le e$，该式整且与提升无关。
映射
$$
B\longrightarrow(\mathcal O/h)[p^m],\qquad
x\longmapsto -u p^{e-m}\widetilde x
$$
是同构，既非零也非仅有界误差。
因此
$$
\boxed{
\operatorname{im}\bigl(H^1(A\otimes\mathcal T)/p^m
       \longrightarrow H^1(A_B\otimes\mathcal T)\bigr)=BL,
\quad
\ker\beta_m=BL .
}
\tag{36}
$$
而(31)的连接线 BC经 Bockstein同构到全部
$H^2(A\otimes\mathcal T)[p^m]$。特别
$$
H^1(A_B\otimes\mathcal T)=BL\oplus BC
\tag{37}
$$
是保原规范的整提升线/连接线分解。
这不是把两条任意的一维向量空间称为“同一个局部类”。

## 8. 原全来源、全部素点与 ordinary p 条件

在 R908 的双新位 $q_1$ 上，张量其它 $A_i$、旧有限群环
及 finite wild 群环。它们均为 $\mathcal O$-free。
由于 $(q_1)$ 在这些旧 ring-class 层完全分裂，
这些因子在选定局部处是常系数。
因此(29)–(37)逐坐标张量恒等，保留每一个上方素点；
不取它们的 augmentation或不带 frame 的 trace。
取相容 wild逆极限时，矩阵仍逐系数成立于
$(\mathcal O/p^m)[[\Gamma]]$；没有改变原 u。

对原可整提升的
$\mathcal N^{\rm aug}_{12}$，其局部约化落在 BL。
所以 R908附A及 R913已经支付的几何局部零，
通过(29)的单位 u准确控制这条 L坐标。
若使用固定尺度 D或 $D_p$，只能在同一格中保留该尺度；
不能用(35)给另一个 residual class免费添一个整提升。

相反，由模 $p^m$ 的导数、除 h或 descent构造的残余类，
一般未给出整 H¹提升。对这样一个**实际已构造**的全局类
$x\in H^1(K,A\otimes\mathcal T/p^m)$，写
$$
\operatorname{loc}_q x=\ell_qL+c_qC.
$$
自然性给准确关系
$$
\boxed{
\operatorname{loc}_q\bigl(\beta_m^{\rm glob}(x)\bigr)
=-u p^{e-m}c_q
\quad\text{于 }\mathcal O/h .
}
\tag{38}
$$
这是 c坐标的真实全局控制门。若原全局 class有整提升，
或其指定全局 Bockstein在该处为零，则由(35)可推出
$c_q=0$；仅知它经 induced/Shapiro的局部像为零，
按(29)只能推出 $\ell_q=0$，对 $c_q$没有这个推论。
本文不把一般残余类代成原 Euler 类，也没有给任何原导数类
赋予未证明的 $c_q\ne0$。

在两个 ordinary p 位，情况不同。原最高角色的惯性模 p
分别含 $\overline\varepsilon_{\rm cyc}^{\,2}$ 和
$\overline\varepsilon_{\rm cyc}^{\,-1}$。
p>211时二者均非平凡；q群环因子在 p不分歧。
可取惯性元素，使原一维格的残余 scalar不为1。
若同时保 finite wild群环，它的额外惯性像是有限 p群，
模剩余特征只给 unipotent作用；非1 scalar乘这个作用后减1
仍可逆。因此同一算子在全部这些整有限 free格上减1为单位，故
$$
H^0(K_{\mathfrak p},M/p^m)=
H^0(K_{\bar{\mathfrak p}},M/p^m)=0
\tag{39}
$$
对这里全部 $M=A\otimes\mathcal T,\ R\otimes\mathcal T,\ \mathcal T$
及原其它常系数因子成立。
所以(28)在这两个 p 位没有(31)那条 H⁰连接线。
尤其 $\bar{\mathfrak p}$ 的原零条件若在 R像中为零，
其 A原像亦为零；$\mathfrak p$仍保原 full条件。
这不提供 $\mathfrak p$局部化单射，只是准确保持原
balanced条件，不能用 q位的二维矩阵改写它。

## 9. 对主增广门的准确范围

本篇的新信息是完整矩阵(29)–(35)，以及原 residual class的
全局 Bockstein坐标式(38)。
它具体解释了为什么不能把“所有新增惰性 raw局部像为零”
和基域 Selmer秩一直接作 Nakayama下降：
原局部残余控制中存在 BC，其像被(29)杀掉，
而这条线的大小随 $p^m$准确增长，不能并入一个与 m无关的
固定有限误差。

另一方面，(36)也说明对**已给出的整原类约化**不能任意加上 C。
两种情形必须分开；这避免把一个形式 residual障碍误算成
原类已有的非零信息。

R893的 ordinary函数及其增广阶 s仍须读取同一个原
$\mathfrak p$定位。R897 的全系统除 T条件与 R913 的合法
T除法局部稳定性均保持。本篇的 p-Bockstein不是那条 T除法，
(35)没有给 $s=0$，也没有排除原 $c_1=0$。

## 依据

- [R908](R908-original-inert-augmentation-specialization-and-point-shadow.md)，
  §§1–5：原四角色、$F=-q$、全分歧 h层、整 j同构及正u读取。
- [R901](R901-original-inert-endpoint-test-matrix-and-local-period.md)，
  附B：原整 augmentation格与全来源提升。
- [R897](R897-original-endpoint-complete-wild-tame-system-and-specialization.md)：
  同一 fixed格、完整 tame/wild来源与原 ordinary条件。
- [R885](R885-original-endpoint-bounded-anticyclotomic-lift-and-unit-specialization.md)：
  最高角色在两个 p位的真实 Tate指数2和−1。
- 本篇(9)–(38)直接由原 tame relation(3)、群环恒等式(5)
  及连续 cocycle规范(7)逐项证明；未借用普通 canonical
  Mazur–Rubin定理替代本题 paired/conjugate-self-dual系统。
