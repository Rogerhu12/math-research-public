# R372：原 canonical 权的固定二挠边界、三挠单位行与真实双 Euler 拉回

日期：2026-11-14。**状态：已证明。** 对整个已付 canonical 来源，R369 的 finite theta frame 差在固定二挠点的加权留数可由两个固定超几何端点和一个明确 Laurent 多项式准确计算。所有 $P_{134}$ 和角因子保留。两个原次数二乘子还产生两条准确的固定三挠单位边界。最后给出原两接触尾经过乘法后的真实 double-Euler 拉回，包含 Gaussian 混合、两个十三行边界和全部新增末行；它不是简单乘同一个留数权。以下没有把这些边界或整三角矩阵解释成新增中央零。

## 1. 同一个原有理参数及合法降极规范

取 $p=6s-1>83$、$b=17$，在原剩余域 $k$ 上令
$$
E_b:y^2=x^3+b,\qquad Dx=2y,\quad Dy=3x^2,\quad
t=-b/x^3,\qquad DZ=1 .
$$
$Z=Z_p$ 始终是 R342/R346 的实际有理函数。
记
$$
\nu=(p-1)/2,\qquad M=(p^2-1)/2,\qquad
B(t)=B_p(-t),\qquad \deg B=\nu,\quad B(0)=1 .
$$
沿 R373 取一个合法的同时 Gaussian 重标，使
$$
H=H_\kappa=H_\sigma+2c_pZ^{p+1}.
$$
这是 $\Delta\equiv-68c_p\bmod p$ 对应的实际规范；完整来源仍同步保留
$e_2(Na_\kappa\epsilon)$，原矩阵及质量零的完整中央导数不变。
R373 已证明
$$
H=\frac{N_H(t)}{(1-t)^M},\qquad
N_H\in k[t],\qquad
N_H(0)=0,\quad N_H(1)=-1/3,\quad\deg N_H\le M-1.
\tag{1}
$$
特别是 $N_H(1)$ 是整单位。由 $u=1-t=y^2/x^3$ 换参数产生的因子
已经包含在 (1) 中。

置 $V=Z^2x$。原 R342 的有限除法多项式直接给
$$
\boxed{
V=\frac{B(t)^2}{(1-t)^p},\qquad
d\log Z=\frac{(1-t)^\nu}{6tB(t)}\,dt.
}
\tag{2}
$$
例如写 $N=(3p-1)/2$，则
$Z=x^NB(t)/(2Ny^p)$，而 $2N=-1$ 于 $k$；
平方后使用 $2N+1=3p$ 即得第一式。
第二式由 $DZ=1$、$Dt=-6ty/x$ 得出。

R371 的完整 frame 差因此准确下降为
$$
\boxed{
\chi\,dz
=\frac{(1-t)^\nu}{6tB(t)}\,dt
-\frac{B(t)^{p-1}}{6t(1-t)^{M+1}}\,dt.
}
\tag{3}
$$
这是真正的有理微分，包含所有移动测试极、二挠极和 $x=0$ 两点。
没有把它替成只在 $O$ 有相同 jet 的微分。

## 2. 整个原 canonical 权及二挠点的完整系数式

令 $m$ 是偶数、$0<m<p$，$F(t)\in k[t]$ 满足
$$
\deg F\le m/6 .
\tag{4}
$$
只在原来源已经给出这种 $m,F$ 时使用它。其有限 theta 代表为
$$
\mathcal S_{m,F}
=V^{m/2}F(t)E_{p-1}(mH),\qquad
E_{p-1}(u)=\sum_{j=0}^{p-1}\frac{u^j}{j!}.
\tag{5}
$$

这确实包括 R335/R361 的整个原 canonical 基：
令 $a\ge0$、$m=34(a+40)$，
$$
F_{a,j}
=P_{134}\,t^{13+\alpha+j}(t-1)^{15+\beta}
 h_7^{13+\alpha}(1+8t)^{23+a-\gamma},
$$
$$
\alpha=\lfloor(a+1)/4\rfloor,\qquad
\beta=\lfloor(a+1)/3\rfloor,\qquad
\gamma=\lfloor a/2\rfloor .
\tag{6}
$$
原来源是 $\Theta^{17(a+40)}F_{a,j}$；
其在 $x=0$ 的原全纯性给 (4)。这里没有换成任意全纯角格，
也没有把 $P_{134}$ 当单位删除。

对 $1\le n\le K\le s-2$，记
$$
\delta=m-6n,\qquad
f_{m,F,n}=\mathcal S_{m,F}Z^{-6n}
=(-b)^nt^{-n}B^\delta(1-t)^{-p\delta/2}
 F(t)E_{p-1}(mH).
\tag{7}
$$
定义下降后的两个固定边界
$$
\beta_2(m,F,n)=\operatorname{Res}_{t=1}(f_{m,F,n}\chi\,dz),
\qquad
\beta_3(m,F,n)=\operatorname{Res}_{t=\infty}(f_{m,F,n}\chi\,dz).
\tag{8}
$$
在原 $E_b$ 上，每个非零二挠点的残数是 $2\beta_2$，
每个 $x=0$ 点的残数是 $3\beta_3$：
这是 $t$ 商映射在这两类点的真实分歧指数。

(1)、(3) 给一个不省略任何高极部的有限系数式。
令 $u=1-t$，并写
$$
A_{F,n}(u)=(1-u)^{-n-1}F(1-u),\quad
B_u=B(1-u),\quad N_u=N_H(1-u).
$$
则
$$
\boxed{\begin{aligned}
\beta_2(m,F,n)
={(-b)^n\over6}\sum_{j=0}^{p-1}{m^j\over j!}
\bigg\{&
[u^{p\delta/2+M(j+1)}]\,
 A_{F,n}(u)B_u^{\delta+p-1}N_u^j\\
-&[u^{p\delta/2-\nu-1+Mj}]\,
 A_{F,n}(u)B_u^{\delta-1}N_u^j
\bigg\}.
\end{aligned}}
\tag{9}
$$
负的系数指标解释为零。
$B_u$、$N_u$ 在 $u=0$ 为单位，所有 $j!$ 也为单位，
故 (9) 是实际有限 étale 整局部格上的系数操作。
负的 $B_u$ 幂通过其真实整逆展开；没有大于等于 $p$ 的阶乘除法。

证明只须把 (7) 代入 (3)，再用
$H^j=N_u^ju^{-Mj}$、$dt=-du$ 逐项取 $u^{-1}du$。
以下将把 (9) 化为远短于其最高极阶的固定端点表达，
而不是把其中的项判零。

## 3. 移动测试极的完整偶阶多项式

在覆盖 $x=v^2,\ y^2=v^6+b$ 上，用形式变量 $g$，先令 $Dg=0$，
再用算子
$$
D-x\partial_g+mg .
$$
在真正的测试点 $Z=0$，这就是 R356 已付的 $G_\kappa(0)=0$、
$DG_\kappa=-x$ 的小于 $p$ 阶局部递推。

若 $N\ge0$ 为偶数且 $N<p$，定义
$$
\boxed{
C_N^{m,A}(\xi)
={v^{-A-N}\over N!}
\left.(D-x\partial_g+mg)^Nv^A\right|_{g=0},
\qquad \xi=b/v^6.
}
\tag{10}
$$
它属于 $k[\xi]$，且
$$
\deg C_N^{m,A}\le N/2,\qquad
C_N^{m,A}(0)=[u^N](1-u)^{m-A}e^{mu}.
\tag{11}
$$
包括 $N=0$ 和负 $A$。证明与 R369 的 filtration 递推相同：
令 $\theta=y/v^3,\gamma=g/v$，给 $\xi,\theta,\gamma$ 权 $2,1,1$，
每次导子至多增一；偶阶并令 $\gamma=0$ 后只剩 $\xi$。
在 $\xi=0$ 的实际局部解给 (11) 第二式。

若 $6n<m$，置 $L_{m,F,n}=0$。
若 $6n\ge m$，写 $F(t)=\sum_d f_dt^d$，定义
$$
\boxed{
L_{m,F,n}(t)
=(-b)^n\sum_d f_dt^{d-n}
 C_{6n-m}^{m,m-6d}(-t).
}
\tag{12}
$$
这是明确的 Laurent 多项式。若 $e=\operatorname{ord}_0F$、
$d_F=\deg F$，则其指数范围是
$$
e-n\le\deg_{\rm monomial}L_{m,F,n}
\le 2n-m/2+d_F .
\tag{13}
$$

**命题1。** 在每个真正的非原点测试点，$t=\alpha$ 为 $B$ 的根时，
$$
\boxed{
\operatorname{Res}_{P}(f_{m,F,n}\chi\,dz)=L_{m,F,n}(\alpha).
}
\tag{14}
$$

证明中 $\chi=Z^{-1}+O(Z^{p-1})$，而
$E_{p-1}(mH)$ 的小于 $p$ jets 是 R369 的正规局部指数。
故残数准确读取第 $6n-m$ 阶导数。
若该数为负便是零；否则它小于 $p$，
(10) 逐项给 (12)。所有 $(m-6d)$ 幂和角零都保留，
没有在 $F(\alpha)=0$ 时除以它。
$p$ 阶以上的 $\chi$ 和指数尾在这里均不能贡献留数。

## 4. 固定的两个端点与全部二挠边界

定义两个固定级数
$$
h_0(t)=\sum_{j\ge0}{(1/2)_j\over j!(6j+1)}t^j,\qquad
h_3(u)=\sum_{j\ge0}{(1/2)_j\over j!(3j+1)}u^j.
\tag{15}
$$
原 $B$ 的两端系数准确为
$$
B(t)\equiv h_0(t)\pmod{t^{\nu+1}},\qquad
{u^\nu B(1/u)\over B_{\rm top}}
\equiv h_3(u)\pmod{u^{\nu+1}},
\quad B_{\rm top}={(-1)^{\nu+1}\over2}.
\tag{16}
$$
这里均指模 $p$ 后显示有限范围；不把无限级数当全局函数。
它们直接来自
$\binom{\nu}{j}=(-1)^j(1/2)_j/j!$、
$N/(N-3j)=1/(6j+1)$，及反序后的分母 $3j+1$。

对 Laurent 多项式 $L=\sum L_jt^j$，定义
$$
\boxed{
\mathfrak T(L)=
-\frac12 L_0
-\sum_{j\ge1}j[t^j]\log h_0(t)\,L_{-j}
-\sum_{j\ge1}j[u^j]\log h_3(u)\,L_j .
}
\tag{17}
$$
当指数范围如 (13) 时，所需两端长度均严格小于 $\nu$，
且所有显示系数均为 $p$ 整：
负端最多 $K$，正端至多 $2K$，而 $K\le s-2$。
因此 Newton 和式准确给
$$
\boxed{\sum_{B(\alpha)=0}L(\alpha)=\mathfrak T(L).}
\tag{18}
$$
例如负幂用 $-\!j[t^j]\log B$，正幂用反序多项式；
常数项使用 $\nu=-1/2$ 于 $k$。这包括全部测试根，不删除任何
$P_{134}$ 或其他原角零所在分量。

还需完整给出固定三挠边界。令
$$
J_3(u)=\sum_{j\ge0}{(1/2)_j\over j!(3j+2)}u^j,\qquad
H_3(u)=\frac1{12}\int_0^u{J_3(v)\over\sqrt{1-v}}\,dv.
\tag{19}
$$
这些也是固定级数。$H_3=u/24+\cdots$。
在 $x=0$ 的任一原分支，$u=1/t=-x^3/b$，
直接积分 $dz=dx/(2y)$ 及 $DG=-x$ 给
$$
V=-\frac u4 h_3(u)^2+\cdots,\qquad
H=H_3(u)+O(u^{2s}),\qquad
\chi\,dz=\left(\frac13+u\frac{h_3'}{h_3}\right)\frac{du}{u}
+O(u^{p-1})\,du .
\tag{20}
$$
第一式在所需小于 $p$ 的范围成立；其完整 Frobenius 修正是
$(1-u)^{-p}$，从 $u^p$ 起。
第二式的第一次积分共振恰在 $u^{2s}$；
这里所有所需系数指标都小于 $2s$，故没有跨过它。
合法 Gaussian 的改变也只从这个共振阶参与。

写 $F^*(u)=u^{d_F}F(1/u)$ 及
$d_\infty=2n-m/2+d_F$。若 $d_\infty<0$，$\beta_3=0$；
否则
$$
\boxed{\begin{aligned}
\beta_3(m,F,n)
={}&(-b)^n(-1/4)^{m/2-3n}\\
&\cdot[u^{d_\infty}]
F^*(u)h_3(u)^{m-6n}e^{mH_3(u)}
\left(\frac13+u\frac{h_3'}{h_3}\right).
\end{aligned}}
\tag{21}
$$
由 (4)，$d_\infty\le2K-m/3<2s$。
所以 (19)–(21) 中所有积分、指数、阶乘和真正的三挠局部规范都已支付。

**定理1（整个原权的固定边界）。**
对 (5) 中每一条真实来源，
$$
\boxed{
\beta_2(m,F,n)
=-\mathfrak T(L_{m,F,n})-\beta_3(m,F,n).
}
\tag{22}
$$
因此 (9) 的全部高阶二挠极部只需两个固定端点的短系数来计算。

**证明。** 微分 $f_{m,F,n}\chi\,dz$ 在原点的阶至少为
$6(p+\operatorname{ord}_0F-n)-1>-1$，故原点残数为零。
它在 $t$ 线上除 $B$ 的全部根、$1$ 和 $\infty$ 外没有其他极点：
(1)–(7) 中有限指数是多项式，未引入它的零点分母。
分别应用 (14)、(18)、(21) 及全局残数定理即得 (22)。

若在原 $E_b$ 上计算，同一等式是全体测试极的六重轨道、
三个二挠点的二重分歧、两个 $x=0$ 点的三重分歧共同除以六；
该数为单位。因而没有丢掉某个原分支或错误平均三挠残数。
$\square$

(22) 可以线性作用于同一混合次数来源和同一 forcing。
它没有逐次数添加零条件。特别是固定边界由指定端点计算，
并不因原点 finite jet 看不见 $\chi$ 而消失。

## 5. 两个原次数二乘子的准确单位边界

取 R366 的原两乘子，$m=68$，
$$
F_0=128t^5-80t^4+12t^3-53t^2-7t,\qquad F_1=tF_0 .
\tag{23}
$$
它们符合 (4)，且完整保留真实 $Z^{68}$。
对同一 $q_1,\ldots,q_K$，令
$\beta_{j,i}(q)=\sum_nq_n\beta_j(68,F_i,n)$。

由 (21)，$\beta_3(68,F_i,n)=0$ 当 $2n+i-29<0$。
原首两条非零行准确为
$$
\boxed{
\beta_3(68,F_1,14)=\frac{2^{23}b^{14}}3,\qquad
\beta_3(68,F_0,15)=-\frac{2^{28}b^{15}}9.
}
\tag{24}
$$
证明只需
$$
h_3=1+u/8+\cdots,\qquad H_3=u/24+\cdots,\qquad
F_i^*=128-80u+12u^2-53u^3-7u^4.
$$
对于第一式 $d_\infty=0$，读取常数。
第二式 $d_\infty=1$；$h_3^{-22}e^{68H_3}$ 的一次项为 $1/12$，
再乘最后的 $1/3+u/8+\cdots$，得到系数 $-64/9$；
外因子为 $4^{11}b^{15}$，即为所列值。

所以当 $K\ge15$ 时，这两个固定三挠边界在列 $q_{14},q_{15}$
上有一个真实二阶单位三角子式。
这是原边界的非零性，不是原中央导数的非零性。
在原 $x=0$ 点，(24) 另乘已付分歧指数三，仍为单位。

对 $n\le11$，(14) 的测试极残数全为零，
(21) 的三挠边界也为零；(22) 因而精确迫使
$\beta_2(68,F_i,n)=0$。
这一取消包含 (9) 的全部大极部，并非只检查首极项。
对其余 $n$，(22) 给实际的完整边界值，不能再把它置零。

## 6. 原 two-contact 的真正 double-Euler 拉回

现在回到 R338/R342 的同一个原有限目标。
保留 $K=s-14$ 和 R366 的
$$
T,\ T+1,\ T+2<3s,\qquad
T=2s+\ell+13,\quad1\le\ell<s-15.
$$
取真正 $P_2\in K_2(M)$，以及相应大目标上的真正模 $p^2$ 整左核
$\lambda_2$；其约化属于正确 $C_2$ 对偶。
物理 Laurent 对偶始终是
$$
\sum_r\lambda_r p^{\lfloor r/s\rfloor}w^{-r-1}\,dw.
\tag{25}
$$
以下先按这个整对偶完成除 $p$，再使用其模 $p$ 系数。
没有从任意模 $p$ 行开始。

写同一 $P$ 的两条尾为 $D_1,D_2$。
两个乘子 charge 都是二，所以共同 Gaussian 混合先给
$$
\widetilde D_2=D_2+2\bar a_\kappa D_1 .
\tag{26}
$$
令 $\ell_+$ 是所用真实大目标的第三相对块长度
（可以是 $\ell+1$ 或 $\ell+2$），定义
$$
S_r=
\sum_{j=r}^{K}\lambda_{1,j+13}[w^{j-r}]D_1
+\sum_{j=r}^{\ell_+-1}
 \lambda_{2,j+13}[w^{j-r}]\widetilde D_2,\qquad
q_r^{\rm mix}=S_r/d_r,\quad d_r=6r(6r+1).
\tag{27}
$$
空和为零。两个 $+13$、第一个上界 $K$，
以及第二和中 $j=\ell_+-1$ 的新增末行全部保留。
它们正是 R342 的除幂转置；(26) 对两个乘子相同。

令 $v_i(w)$ 为原 $Q_i$ 的 ordinary regularized 乘子，
完整物理乘子是 $v_i e_2(2a_\kappa\epsilon)$。
于是
$$
v_0=7bw+\cdots,\qquad v_1=t(w)v_0=-7b^2w^2+\cdots.
\tag{28}
$$
真正拉回后的 forcing 是
$$
\boxed{
(q_i)_n
=\frac1{d_n}\sum_{k\ge0}(v_i)_k d_{n+k}q_{n+k}^{\rm mix},
\quad1\le n\le K,
}
\tag{29}
$$
越过 $K$ 的项为零。

证明是直接将 $v_iD_1,v_i\widetilde D_2$ 代入 (27)：
先交换有限的 $j,k$ 两和，再令 $r=n+k$，便得到 (29)。
正次数乘法保证所需 $v_i$ 只有已经给出的前缀；
不需要未知目标尾。新增末行已经在 (27) 中，不能先删去。

令
$$
\mathsf E=6w\partial_w,\quad
\mathcal L=\mathsf E(\mathsf E-1),\qquad
q(w)=\sum_{n=1}^Kq_nw^{-n}.
$$
负 Laurent 格上 $\mathcal L(w^{-n})=d_nw^{-n}$，所有 $d_n$ 为单位。
若 $\operatorname{pp}$ 保留严格负幂，(29) 等价于
$$
\boxed{
\mathcal T(v)q=\mathcal L^{-1}\operatorname{pp}(v\mathcal Lq).
}
\tag{30}
$$
它的完整交换差为
$$
\boxed{
\mathcal T(v)q=\operatorname{pp}(vq)-
\mathcal L^{-1}\operatorname{pp}
\left(2(\mathsf Ev)\mathsf Eq+
(\mathsf E^2v-\mathsf Ev)q\right).
}
\tag{31}
$$
这说明从原接触恒等式
$\mathcal D(PQ_i)=Q_{i,\rm phys}\mathcal D(P)$
不能直接把两个拉回认作 $v_iq$。

## 7. 真实拉回的整原始性及与局部 theta 权的区别

**定理2。** 在整个长度 $K$ 的负 Laurent 整格上，
$$
\boxed{\mathcal T(v)\mathcal T(u)=\mathcal T(vu).}
\tag{32}
$$
若 $v=w^eh$，$h(0)$ 为单位，则
$\mathcal T(v)$ 的核准确是前 $e$ 条列，秩为 $K-e$，
且有一个 $K-e$ 阶单位子式。

证明中 $\mathcal L$ 是整对角同构。
正幂级数乘以一个在原点正规的舍弃项，仍不会产生负幂，
故两次取 $\operatorname{pp}$ 可以合并，得到 (32)。
而 $\operatorname{pp}(v\,\cdot)$ 在负 Laurent 基中是上三角行移，
第一非零对角为 $h(0)$。与 $\mathcal L$ 共轭保留核和单位子式。

由 (28)，原联合拉回
$$
q^{\rm mix}\longmapsto(q_0,q_1)
$$
的核准确为 $\langle w^{-1}\rangle$，其整像是 $p$-饱和的；
已有第一块的 $K-1$ 阶单位子式。
第二块核为 $\langle w^{-1},w^{-2}\rangle$。
与 R346 已付的未扭整留数映射复合，仍有这同一个
$K-1$ 阶单位子式，不丢新的 $p$ 精度。

这个结论作用于真正的 forcing 拉回矩阵。
它不把受同一 $P,\lambda$ 限制的实际双线性像说成整个 forcing 格；
也不从矩阵原始性推断这些留数已被原中央条件判零。

R369 的另一矩阵则是在完整 finite theta 权
$\mathcal Q_i$ 乘一个指定共同 $\omega_q$ 后计算的局部留数，
它确实带 $Z^{68}$ 并有前十一条零列。
(30)、(31) 明确给出两种计算之间尚须保留的步骤：
原点主部投影、double-Euler 交换差及完整 Gaussian 混合。
本篇第2–5节又将该全局 frame 差的固定二挠／三挠边界算清。
二者不能用一个免费的行单位同构互换。

R363 的模 $p^2$ 第一商、R365 的总 charge、公共 $U_0$、
$P_{134}$、$Z^{-78}$ 以及原两条十三行仍留在实际 $C_2$ 配对中。
尤其本篇在特征 $p$ 的合法降极，不免除整 lift 中的 $p$ 倍极部。
原完整中央失败依旧只给
$a_\kappa c_1-pc_2=0\bmod p^2$ 的聚合。
下一步可以把 (9)、(22)、(27)–(31) 直接代入该指定配对；
本篇没有提前新增逐权、逐次数或逐测试极的零。

## 依赖

- R335、R338、R342：整个 canonical 来源、正确第二余核和原 double-Euler 系数。
- R346：真实测试代数与未扭留数的整原始性。
- R351、R363、R365：可提升整左核、完整第一商、总 charge 和所有公共因子。
- [R366](R366-original-two-degree-two-multipliers-and-joint-local-residue-primitivity.md)、
  [R369](R369-original-finite-theta-frame-and-shifted-joint-residue-primitivity.md)：
  两个真乘法图和完整 finite theta 局部模型。
- [R371](R371-original-frame-defect-cartier-logarithm-and-weighted-exact-term.md)、
  [R373](R373-original-theta-log-cartier-chain-and-gaussian-pole-reduction.md)：
  实际 $\chi$、全部 exact 项及合法 Gaussian 降极。

本篇为全参数证明，无目标素数扫描。通过已授权 GitHub API 保存；
核心索引和同步记录由根代理维护。
