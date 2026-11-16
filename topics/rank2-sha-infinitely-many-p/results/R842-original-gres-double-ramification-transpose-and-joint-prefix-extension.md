# R842 — 原 GRes 的二倍分歧转置与同前缀联合延拓

日期：2026-11-16。**状态：以下实际转置、十九角运输及联合延拓等价已证明；指定延拓是否可解仍未完成。**

本篇把 [R822](R822-original-cartier-residue-descent-and-actual-ramification-trace.md)
的指定分歧行代入
[R836](R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)、
[R840](R840-original-double-ramification-euler-image-and-unique-normal-tail.md)
的同一个实际值对。得到的两个有限向量由原 $F,q_{\rm src}$ 唯一确定，
不能自由增加第二法向值。
全局判据保同一个有限对偶向量和两个真正全局微分的共同边界条件；
没有认定该判据可解，也没有把它替换成维数判断。

## 1. 原来源、有限配对与同一高前缀

保持原十九角曲面和几何整 Cartier 曲线
$$
C=(F=0),\quad P=(0,1),\quad
N=\mathcal O_C(C),\quad
\kappa=C^2,\quad \chi=-K_XC>0,
$$
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
\mathcal E=Y\partial_Y,\quad e=\mathcal EF,\quad f_2=\mathcal E^2F,
\quad Z=(e|_C),\quad 2Z=(e^2|_C).
\tag{1}
$$
$P$ 光滑且 $e(P)$ 为单位。
取已经支付的真实返回
$q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D}$，
并保持 R836/R840 的 $3b<p$ 和
$$
h<T\le2h,\qquad T>2\kappa.
\tag{2}
$$
物理四块使用 $T=s-r-13$；
相对 $J_4$ 若另行使用则是 $T=s-r$。
原 $G_0/U_0/P_{134}$、charge 四十、全部十三行带和完整余因子逆，
均须先按 R836 支付，才使用下列相对数据。

记
$$
\mathscr V_T=H^0(C,N^3(-TP)),\quad
\mathscr Z=H^0(Z,N^3|_Z),\quad
\mathscr Z^{(2)}=H^0(2Z,N^3|_{2Z}).
$$
它们的真有限对偶为
$$
\mathscr Z^\vee=H^0(Z,\omega_C N^{-2}|_Z),\qquad
(\mathscr Z^{(2)})^\vee
=H^0(2Z,\omega_C N^{-1}|_{2Z}).
\tag{3}
$$
例如第二个配对是
$$
\langle V,\lambda\rangle_{2Z}
=\sum_{Q\in Z}\operatorname{Res}^C_Q(V\widetilde\lambda/e^2).
\tag{4}
$$
所有剩余域迹均包含在记号内。奇点处使用原 Gorenstein/Rosenlicht
配对、全部正规化分支及 conductor；不是普通 Artin 乘法迹。

原 $D_3$ 因子化为真正有限算子
$$
\mathfrak d:\mathscr Z^{(2)}\to\mathscr Z,
\qquad
D_3(V)=(\mathcal EG)|_Z=\mathfrak d(V|_{2Z}),
\quad G|_C=V.
\tag{5}
$$
改变 $G$ 的提升只添 $F\mathcal H_2$，其 Euler 值在 $Z$ 为零。
局部把 $V$ 改为 $V+e^2K$ 后，导数模 $e$ 也为零，
故 (5) 确实定义在整个 $2Z$ 上。
另记自然值限制为
$\iota:\mathscr Z^{(2)}\to\mathscr Z$。

## 2. 原有限转置及每个真框中的零阶项

先在原非固定有限图使用
$$
\Omega_{\log}=\frac{dt\wedge dY}{Y},\qquad
\mathcal L_{\mathcal E}\Omega_{\log}=0.
$$
以 $\mathcal R_{F,e}(B)$ 表示有序方程 $(F,e)$、
二形式 $\Omega_{\log}$ 的完整 Grothendieck 留数。
对局部正则 $H,V$ 有
$$
\boxed{
\mathcal R_{F,e}(H\,\mathcal EV)
=\mathcal R_{F,e^2}
 \bigl(V(Hf_2-e\,\mathcal EH)\bigr).
}
\tag{6}
$$

**证明。** 对同一个局部残数展开
$\mathcal L_{\mathcal E}(HV\Omega_{\log}/(Fe))$，其留数为零。
这给
$$
0=\mathcal R_{F,e}((\mathcal EH)V+H\mathcal EV)
-\operatorname{Res}\frac{HV\Omega_{\log}}{F^2}
-\mathcal R_{F,e^2}(HVf_2).
$$
中间只有 $F^2$ 的极，没有第二个余维一极；
也可写成 $\mathcal R_{F^2,e}(eHV)=0$。
余式正是 (6)。该形式留数论证在本特征中成立，
不要求 $Z$ 约化，也不要求 $F_t$ 在奇点为单位。证毕。

因此在这个原框中，
$$
\boxed{
\mathfrak d^\vee H=Hf_2-e\mathcal EH
 \pmod{(F,e^2)},\qquad
\iota^\vee H=eH\pmod{(F,e^2)}.
}
\tag{7}
$$
这是从 $Z$ 对偶到 $2Z$ 对偶的映射。
若把 $H$ 的提升改为 $H+eK$，第一式准确只改变
$-e^2\mathcal EK$，所以不依赖局部提升。

### 全十九角的实际框

不能将 (7) 的裸 $\mathcal E$ 原样抄入吹起后的系数框。
取一个真局部框，使原 $\mathcal O_X(mC)$ 上的算子为
$$
\mathcal E^{(m)}=D+ma,
$$
其中 $D$ 是原正则向量场的 lift。
取局部单位二形式 $\Omega_U$，记
$\mathcal L_D\Omega_U=c\,\Omega_U$。
在这个框中
$$
e=(D+a)F,\qquad f_2=(D+a)e,
$$
而 $\mathcal H_3$ 的实际 Euler 值为 $(D+3a)V$。
同一留数展开逐项给出
$$
\boxed{
\mathfrak d^\vee H
=Hf_2-e\bigl(DH+(c-a)H\bigr)
\pmod{(F,e^2)},\qquad
\iota^\vee H=eH.
}
\tag{8}
$$
这里 $c-a$ 不能丢。
具体地，
$$
\operatorname{Res}\mathcal L_D\frac{HV\Omega_U}{Fe}=0
$$
的分子先给 $(DH)V+HDV+cHV$，
再由 $DF=e-aF,\ De=f_2-ae$ 添上 $2aHV$。
将 $HDV$ 换为实际 $H(D+3a)V$，
余下正是 (8) 的 $c-a$。
提升 $H\mapsto H+eK$ 使 (8) 改变
$$
-e^2\bigl(DK+(c-2a)K\bigr),
$$
仍为零。若另改原曲线代表 $H\mapsto H+FL$，
(8) 模 $F$ 只改变 $-e^2L$，也为零。
因此它确实定义在原 $(F,e)$ 商上。

以下表把原十九角全部包括在内；$V_j$ 是原累计重数。

| 原图 | $D$ | $a$ | $c$，对局部单位坐标二形式 |
|---|---|---|---|
| 负链第 $j$ 图，$t-t_i=x^jz_j,\ x=Y^{-1}$ | $-x\partial_x+jz_j\partial_{z_j}$ | $b-V_j$ | $j-1$ |
| 有限正链第 $j$ 图，$t-t_i=x^jz_j,\ x=Y$ | $x\partial_x-jz_j\partial_{z_j}$ | $V_j$ | $1-j$ |
| 底无穷远正链，$T=1/t,\ Z=t^4Y$，再作同一正图 | $x\partial_x-jz_j\partial_{z_j}$ | $V_j$ | $1-j$ |

三个四步负链、一个三步负链、两个两步正链共十九次吹起，
均在表中；其余交叠图按同一算子和局部单位变换运输。
底无穷远的 $T^u$ 权为零。
若改用有零极的 $\Omega_{\log}$ 框，
它的系数满足 $D\log(\Omega_{\log}/\Omega_U)=-c$，
因此 (8) 与 (7) 严格一致。
这也说明 (8) 是真有限对偶的公式，不是任选一个 raw 多项式导数。

## 3. 指定原 GRes 的两个确定向量

现在专取 R822 的实际权
$$
W_s=t^{r+1-s}(1-t)^{3s},\qquad
c_s=\frac{3(-1)^s}{17},\qquad
H_s=c_sW_sF_t^2.
$$
在其非固定开集 $Z^\circ\subset Z$ 上，$Y$ 和 $W_s$ 都为单位，
原式 (16) 准确等于
$$
\mathfrak G_F(R)
=\sum_{Z^\circ}\mathcal R_{F,e}(H_s\mathcal E^2R).
\tag{9}
$$
这里
$\Omega_{\log}/(Fe)=dt\wedge dY/(Y^2FF_Y)$，
所以 (9) 保了原 $Y^{-2}$ 和有序方程的符号。

令
$$
\boxed{
A_s=H_sf_2-e\math EH_s
=c_sW_s\bigl(F_t^2f_2-2eF_t\,\math EF_t\bigr)
\pmod{(F,e^2)}.
}
\tag{10}
$$
这里 $A_s$ 先在原共同有理框中定义。
物理 $R$ 的来源线束可以不同于 $3C$；
只有与下文 $q_{\rm src}$ 及其导数合成后的向量，
才认作 (3) 的有限对偶，不单独把 $A_s$ 加入一个来源格。
在 (6) 中取 $V=\mathcal ER$，得到实际转置
$$
\boxed{
\mathfrak G_F(R)
=\sum_{Z^\circ}\mathcal R_{F,e^2}(A_s\,(\mathcal ER)|_C).
}
\tag{11}
$$
它读取同一 $R$ 的 $2Z^\circ$ 值；没有将二阶读取丢成一阶值。

对同一个真实来源
$$
R=q_{\rm src}t^rG,\quad G\in\mathcal H_3,\qquad
V_0=G|_C,\quad V_1=(\mathcal EG)|_C,
$$
有
$$
(\mathcal ER)|_C
=t^r\bigl(q_{\rm src}V_1+(\mathcal Eq_{\rm src})V_0\bigr).
$$
故存在两个完全确定的
$\lambda_0,\lambda_1\in(\mathscr Z^{(2)})^\vee$，满足
$$
\boxed{
\mathfrak G_F(q_{\rm src}t^rG)
=\langle V_0|_{2Z},\lambda_0\rangle_{2Z}
+\langle V_1|_{2Z},\lambda_1\rangle_{2Z}.
}
\tag{12}
$$
在 $2Z^\circ$ 的原有限框，它们准确由
$$
\lambda_0:\quad t^r(\mathcal Eq_{\rm src})A_s,\qquad
\lambda_1:\quad t^rq_{\rm src}A_s
\tag{13}
$$
乘同一残数密度
$$
\frac{dY}{YF_t e^2}=-\frac{dt}{e^3}
\tag{14}
$$
给出。
换句话说，在 (4) 中它们的局部微分系数为
$t^r(\mathcal Eq_{\rm src})A_s\,dY/(YF_t)$
和 $t^rq_{\rm src}A_s\,dY/(YF_t)$。
(14) 明确了与原 $dt/e$ 框的负号。

### 固定边界不是被删掉的自由数据

$\mathfrak G_F$ 按 R822 只求和于非固定分歧 $Z^\circ$。
因此 $\lambda_0,\lambda_1$ 在
$2(Z\setminus Z^\circ)$ 的所有局部因子上定义为零，
而不是将 (13) 的有理式强行限制到其极点。
有限概形的分解使这给出真正全局有限向量。
奇异因子仍采用完整局部对偶及全部剩余域迹。
R822 的其它边界残数 $\mathfrak B_F$ 没有在这一步消失。

### 余因子的第二导数并未遗漏

直接展开原 $\mathcal E^2(q_{\rm src}G)$ 会得到
$q_{\rm src}\mathcal E^2G+
2(\mathcal Eq_{\rm src})\mathcal EG+
(\mathcal E^2q_{\rm src})G$。
它给另一个等价向量对
$$
\lambda'_1=\mathfrak d^\vee(t^rq_{\rm src}H_s)
 +2\iota^\vee(t^r(\mathcal Eq_{\rm src})H_s),\qquad
\lambda'_0=\iota^\vee(t^r(\mathcal E^2q_{\rm src})H_s).
$$
设 $\nu_q=t^r(\mathcal Eq_{\rm src})H_s$，也按上述固定边界补零。
原框中逐项恒等为
$$
\boxed{
(\lambda'_0-\lambda_0,\lambda'_1-\lambda_1)
=(-\mathfrak d^\vee\nu_q,\ \iota^\vee\nu_q).
}
\tag{15}
$$
因为同一兼容对满足 $D_3V_0=V_1|_Z$，(15) 在它上面为零。
所以 (13) 是用这一个已付兼容关系合并了第二导数项，
不是删除它或另选一个 $R$。

(8) 负责把 (10)–(15) 运到每一个真框；
$q_{\rm src}$ 和 $G$ 的相反框权、各自 Euler 零阶项均随之运输。
它们的乘积仍为同一个物理 $R$。
不会因换框而新增一个可自由选择的有限向量。

## 4. 真前缀的完整对偶正合列

令
$$
j_T:\mathscr V_T\longrightarrow\mathscr Z^{(2)}
$$
为原限制。因为 $T>\kappa$，其核
$H^0(C,N(-TP))$ 为零。
从同一个精确序列
$$
0\to N(-TP)\xrightarrow{\,e^2\,}N^3(-TP)
\to N^3|_{2Z}\to0
$$
及 Serre 对偶得到完整正合列
$$
\boxed{
0\to H^0(C,\omega_CN^{-3}(TP))
\to\mathcal Q_T^{(2)}
\xrightarrow{\ \mathrm{res}_{2Z}\ }
(\mathscr Z^{(2)})^\vee
\xrightarrow{\ j_T^\vee\ }
\mathscr V_T^\vee\to0,
}
\tag{16}
$$
其中
$$
\mathcal Q_T^{(2)}=H^0(C,\omega_CN^{-1}(TP)).
$$
特别
$$
\ker j_T^\vee=\operatorname{im}(\mathrm{res}_{2Z}).
\tag{17}
$$
这里没有假定 $H^1(C,N^3(-TP))=0$：
它的完整对偶正是 (16) 最左边的项。
全局延拓的非唯一性只能来自该项，不能任意改各个局部主部。

## 5. 对同一兼容高前缀对的精确联合延拓判据

定义真正的高前缀对空间
$$
\mathscr P_T=
\{(V_0,V_1)\in\mathscr V_T^2:
D_3V_0=V_1|_Z\}.
$$
它是实际映射
$$
\mathcal A_T:\mathscr V_T^2\to\mathscr Z,\qquad
\mathcal A_T(V_0,V_1)
=\mathfrak d\,j_T(V_0)-\iota\,j_T(V_1)
\tag{18}
$$
的核。这里不假定 $\mathcal A_T$ 满射。

**定理。** 原指定行 (12) 在整个 $\mathscr P_T$ 上恒零，
当且仅当存在同一个
$$
\nu\in\mathscr Z^\vee
$$
和两个真正全局截面
$$
\omega_0,\omega_1\in\mathcal Q_T^{(2)}
$$
满足
$$
\boxed{
\lambda_0-\mathfrak d^\vee\nu
 =\mathrm{res}_{2Z}\omega_0,\qquad
\lambda_1+\iota^\vee\nu
 =\mathrm{res}_{2Z}\omega_1.
}
\tag{19}
$$

**证明。** 在有限维原空间上，
$\operatorname{Ann}(\ker\mathcal A_T)=
\operatorname{im}\mathcal A_T^\vee$，无需映射满射。
具体的对偶正合列为
$$
0\to(\operatorname{coker}\mathcal A_T)^\vee
\to\mathscr Z^\vee
\xrightarrow{\mathcal A_T^\vee}
(\mathscr V_T^\vee)^2
\to\mathscr P_T^\vee\to0.
$$
故原行恒零当且仅当某个同一 $\nu$ 使
$$
j_T^\vee(\lambda_0-\mathfrak d^\vee\nu)=0,\qquad
j_T^\vee(\lambda_1+\iota^\vee\nu)=0.
$$
逐项用 (16)–(17)，恰为 (19)。
$\nu$ 的非唯一性是上列显示的核；
$\omega_i$ 的非唯一性是 (16) 最左项。
没有增加环境来源，也没有把两个相同来源条件拆开。证毕。

(19) 在固定边界上也要逐项成立。
因为那里的 $\lambda_i$ 是零，它准确要求
$$
\mathrm{res}\,\omega_0=-\mathfrak d^\vee\nu,\qquad
\mathrm{res}\,\omega_1=\iota^\vee\nu
\quad\text{于 }2(Z\setminus Z^\circ).
\tag{20}
$$
不能在非固定点解 (19) 后丢掉 (20)，
也不能分别把两个 $\omega_i$ 或 $\nu$ 的固定边界值设为零。

原真全局框条件可照原十九角 canonical 除子直接检验：
$$
\operatorname{div}\Omega_{\log}
=-H_--H_+-2f_\infty
+\sum_{\text{有限链}}\sum_j(j-1)E_{i,j}
-\sum_{j=1}^2(j+1)E_{\infty,j}.
\tag{21}
$$
因 $\omega_CN^{-1}=K_X|_C$，
(19) 的每个 $\omega_i$ 必须在这个原线束中正则，
只允许 $TP$ 的极。
在奇点，正规化各支上的阶条件仍不够；
系数模 conductor 必须从原 $\mathcal O_C$ 下降。
因此 (19) 是原边界及前缀的实际成员性问题，
不是任意有限向量都可延拓的断言。

## 6. 同一仿射 forcing 能读取的确切值

考虑非空的真正仿射兼容纤维
$$
[V_0]_{<T}=j_0,\qquad [V_1]_{<T}=j_1,\qquad
D_3V_0=V_1|_Z.
\tag{22}
$$
R840 的原 forcing 给
$j_0=f_0-\eta f_1,\ j_1=f_1-\eta f_2$，
各个 $f_i$ 均须先通过原物理低行和单位逆。

若 (19) 可解，(12) 在 (22) 上是一个固定值，准确为
$$
\boxed{
\mathfrak G_F(q_{\rm src}t^rG)
=-\operatorname{Res}_P^C
\frac{j_0\omega_0+j_1\omega_1}{e^2}.
}
\tag{23}
$$
证明是将 (19) 代入 (12)，先用同一个兼容关系消去 $\nu$ 两项，
再对两个真正全局微分
$V_i\omega_i/e^2$ 使用全局留数。
除 $2Z$ 和 $P$ 外，它们在原 $\omega_C$ 中正则；
其它奇点的所有 conductor 分支残数和为零。
在 $P$，$e$ 是单位而 $\omega_i$ 的极阶至多 $T$，
所以只需已读的 $<T$ 前缀。
这没有延长原窗口，也没有把 raw 有理候选的其它边界极删除。

反过来，若原行在整个仿射纤维 (22) 上恒定，
它在其差空间 $\mathscr P_T$ 上为零，故仍须满足 (19)。
若 (22) 为空，不作这项反推。

## 7. 仍须判定的实际接口

本篇已经把指定原行化为明确的 $(\lambda_0,\lambda_1)$、
明确的有限算子 (8) 和同一个全局延拓系统 (19)。
目前未证明这个系统可解或不可解。
更没有把 $\mathfrak G_F$ 与原其余边界补偿
$\mathfrak B_F$ 分别认成零。

R840 的实际三长核还须满足唯一 $V_2$、同一个 $cF^3$ 的第三长尾
及第四短尾；它是 $\mathscr P_T$ 的真实受限子空间。
所以 (19) 对该更小核给一个充分的消去条件，
但不能在未支付其余条件的情况下宣称也是必要条件。
完整 $\mathcal W_D$ 的其它列仍比本篇返回子格更大。

原同一个 $R$、余因子的全部 Euler 项、低行右逆高尾、
$P_{134}/U_0$、两条／三条十三行带和下一精度均保持。
没有新增中央零、自由 $2Z$ 来源或已证主目标非零。
