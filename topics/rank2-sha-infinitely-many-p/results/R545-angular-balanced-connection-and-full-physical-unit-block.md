# R545 — 原角平衡连接、固定两 charge 返回与完整物理单位块

日期：2026-11-14。**状态：已证明。** R543 的额外极次数来自原
rational \(F\) 在 \(d=0\) 两条例外曲线上的零。
本篇用一个由实际角重数确定的整数 \(c\) 平衡这部分零极，
并把相应的**全部零阶修正**写成真实多项式算子。
该新算子仍只付固定两个 charge，十九个中间角全部保留。

对这个新返回，R543 的有效极次数降为准确的 \(\kappa=C^2\)。
因此在此前满主阶低 \(\ell\) 窗中，原 \(J\) 和整个原 \(M\)
上的限制已经全部为单位 Smith 因子。
其核是三个明确的真实来源列，
可作完整整 Schur 消元，保持所有后续 Bockstein 与原 carry。

这不是原 \(\mathcal V_F\) 的无条件强化：
新算子含不可删除的两个零阶/Euler 项。
它不向来源赋任何新的中央零，也不直接排除余下的原第二障碍。

## 1. 同一原因子与整数平衡区间

保 R495、R498、R502、R517、R543 的同一实际因子、整提升和曲面：
$$
d^{C_D}\bar P=t^rF^3Q,\qquad
F=\sum_{i=0}^b f_i(t)Y^i,\quad f_0\ne0,\quad
u=\max_i(\deg f_i-4i)\ge0.
$$
\(F(0,1)=0\)、\(F_Y(0,1)Q(0,1)\ne0\)，
\(Y=\mathscr R\)、\(d=1+8t\)，全部十九个固定吹起不变。
记 \(d\) 链、无穷远链第一重数分别为
\(\mu_{d,1}\)、\(\mu_{\infty,1}\)。

R495 的逐系数公式在 \(i=0\) 项给
$$
\mu_{d,1}\le\operatorname{ord}_{-1/8}f_0,\qquad
\mu_{\infty,1}\le u-\deg f_0.
$$
所以
$$
\boxed{\mu_{d,1}+\mu_{\infty,1}\le u.}
\tag{1}
$$
可以固定任一整数
$$
\boxed{\mu_{d,1}\le c\le u-\mu_{\infty,1};}
\tag{2}
$$
例如始终取 \(c=\mu_{d,1}\)。
这个 \(c\) 来自同一个实际因子，不是一个可自由调中央条件的参数。
角阶与次数保持的整提升保住 (1)、(2)。

继续记 R543 的边界除子
$$
\mathscr D=C-\operatorname{div}_X(F).
$$
定义计算用的有理函数和边界除子
$$
\boxed{
F_c=d^{-c}F,\qquad
\mathscr D_c=\mathscr D+c\,\operatorname{div}_X(d),\qquad
\operatorname{div}_X(F_c)=C-\mathscr D_c.
}
\tag{3}
$$

**引理 1。** \(\mathscr D_c\) 是有效除子，不经过 \(P=(0,1)\)，并且
$$
\boxed{\deg_C(\mathscr D_c|_C)=C^2=\kappa.}
\tag{4}
$$

**证明。** 原 \(F\) 在有限 \(Y=\infty\) 链和无穷远链的函数值均非正，
唯一可能的边界零在 \(d\) 两例外曲线上。
第一、第二步 \(d\) 值为
\(\mu_{d,1}\)、\(\mu_{d,1}+\mu_{d,2}\)。
普通相邻重数满足 \(\mu_{d,2}\le\mu_{d,1}\)，故 (2) 使
$$
c\ge v_{d,1}(F),\qquad 2c\ge v_{d,2}(F).
$$
除 \(d^c\) 后这两条函数值都非正。

在无穷远，原函数值为
$$
v_{\infty,1}(F)=\mu_{\infty,1}-u,\qquad
v_{\infty,2}(F)=\mu_{\infty,1}+\mu_{\infty,2}-2u.
$$
除 \(d^c\) 分别增加 \(c,2c\)。
由 \(\mu_{\infty,2}\le\mu_{\infty,1}\) 和 (2)，仍均非正。
原底无穷纤维的极次数由 \(u\) 变为 \(u-c\ge0\)；
原 \(d\) 纤维增加一个允许的 \(c\) 阶极。
其他有限角上 \(d\) 是单位，所有函数值不变。

所以 \(F_c\) 在曲面上的整个零除子准确为 \(C\)，
其余边界均是极或零阶，即 \(\mathscr D_c\) 有效。
\(d(P)=1\)，所以不增加 \(P\) 处的边界。
\(\mathscr D_c\sim C\) 给 (4)。证毕。

本引理没有把 \(d^{-c}\) 免费加入原来源。
它只用于计算同一线性系的另一种 rational 平凡化：
$$
\boxed{
H\in\mathcal H_2
\longleftrightarrow
H_c=d^{-2c}H\in H^0(X,\mathcal O_X(2\mathscr D_c)).
}
\tag{5}
$$
相同地，\(\mathcal H_1\) 使用 \(d^{-c}\) 平凡化。

## 2. 新算子的完整多项式公式

仍置
$$
\delta=t\partial_t,\quad \mathcal E=Y\partial_Y,\quad
e=\mathcal EF,\quad
\mathcal V_F=e\delta-(\delta F)\mathcal E.
$$
定义
$$
\boxed{
\mathcal L_c(H)=d\,\mathcal V_FH
+c(\delta d)\bigl(F\mathcal EH-2eH\bigr),
\qquad \delta d=8t.
}
\tag{6}
$$
这是同一真实 \(\mathcal H_2\) 上的整多项式线性算子。
准确的计算身份为
$$
\boxed{
\mathcal L_c(H)
=d^{\,3c+1}\,
\mathcal V_{F_c}(H_c).
}
\tag{7}
$$

确实，
$$
\mathcal V_{F_c}
=d^{-c}\left(\mathcal V_F+
c\frac{\delta d}{d}F\mathcal E\right),
$$
而对 \(H_c=d^{-2c}H\) 使用同一个导子，
还产生 \(-2c(\delta d/d)eH\)；
相乘即得 (6)、(7)。

(6) 的两个附加项均不能删掉。
特别不能仅以 \(d\mathcal V_F\) 代替新算子，
也不能将 (5) 当成对原 \(\mathcal V_F\) 核的无成本换基。

由 \(\mathscr D_c\) 有效，\(1,F_c,F_c^2\) 都属于 (5) 的线性系。
运输回同一原来源，得到三个真实列
$$
\boxed{d^{2c},\qquad d^cF,\qquad F^2\in\mathcal H_2.}
\tag{8}
$$
逐式代入 (6) 也直接给
$$
\mathcal L_c(d^{2c})=\mathcal L_c(d^cF)
=\mathcal L_c(F^2)=0.
\tag{9}
$$
它们的 \(Y\) 次数为 \(0,b,2b\)，故在原剩余域上线性独立。
这三条关系在整提升上同样准确成立。

## 3. 固定两个 charge 的真实返回

仍用 R517 的原乘子
$$
\mathfrak m_2=Y^2t(t-1)^2h_7^2,\qquad
D_0=3b+\deg_YQ\le D.
$$
定义完整返回
$$
\boxed{
\mathcal T_c(H)
=d^{-C_D}t^rQ\,\mathfrak m_2\,\mathcal L_c(H).
}
\tag{10}
$$

**定理 1。** 同一整来源上，准确有
$$
\boxed{\mathcal T_c:\mathcal H_2\longrightarrow\mathcal W_{D_0+2}.}
\tag{11}
$$
若 \(D_0+2\le D\)，它就在旧 \(\mathcal W_D\)；
否则只在真正扩大的来源中使用它。
原 R517 缓冲返回并未由本篇自动扩大，亦未删除任何来源成本。

**证明。** 对 R517 的五类末端 Gauss 值，
\(\mathcal V_FH\) 相对 \(3v(F)\) 的下界是
\((0,-4,-3,-2,0)\)。
乘 \(d\) 后成为
\((0,-4,-3,0,-2)\)。
另因 \(\mathcal E\mathcal H_2\subset\mathcal H_2\)，
附加项
\((\delta d)(F\mathcal EH-2eH)\)
的下界为 \((4,0,0,0,-2)\)。
所以
$$
v(\mathcal L_cH)-3v(F)\ge(0,-4,-3,0,-2).
$$
原 \(\mathfrak m_2\) 的值为 \((2,6,4,2,4)\)，
相乘后五类余量至少是
$$
\boxed{(2,2,1,2,2).}
\tag{12}
$$
所有原 Gauss 界因而保持。

ambient 帽也没有增加第三个 charge：
\(\deg_Y\mathcal L_cH\le3b\)，
其第 \(i\) 个系数的 \(t\) 次数至多 \(3u+4i+1\)。
\(\mathfrak m_2\) 的 \(Y\) 次数二、\(t\) 次数七，
所以最终准确为
$$
\deg_Y(\mathfrak m_2\mathcal L_cH)\le3b+2,\qquad
\deg_t(\mathfrak m_2\mathcal L_cH)_i\le3u+4i.
\tag{13}
$$
结合原 R514/R517 双向判据与同一前缀 \(t^rQ/d^{C_D}\)，
得到 (11)。证毕。

### 全十九个中间角

不能仅用 (12) 的末端值代替中间例外条件。
对 \(G_c=\mathfrak m_2\mathcal L_cH\)，
按 (13) 的实际 ambient 平凡化，逐链准确有下界
$$
\begin{array}{c|c|c}
\text{原链}&j\text{ 范围}&V_j(G_c)-3V_j(F)\text{ 下界}\\ \hline
0,\ h_7\text{ 两根的 }Y=\infty&1,\ldots,4&j\\
1\text{ 的 }Y=\infty&1,\ldots,3&j\\
d=0,\ Y=0&1,2&2\\
t=\infty,\ Z=0&1,2&2.
\end{array}
\tag{14}
$$
对 \(d\,\mathfrak m_2\mathcal V_FH\)，
这是 R517 原表分别加上 \(d\) 的值 \(0,0,j,-j\)。
对附加项 \(\mathfrak m_2(\delta d)(F\mathcal EH-2eH)\)，
前三类有限 \(Y=\infty\) 链的余量至少 \(2j\)，
\(d\)、无穷远两链均至少二：
\(\delta d=8t\) 在 \(0\) 多给 \(j\)，在无穷远损 \(j\)，
均由 \(\mathfrak m_2\) 的实际余量支付。
两部分合并即为 (14)。

因此还有准确的比较空间成员性
$$
G_c\in H^0(X,\mathcal O_X(3C+2\pi^*S_\infty)).
\tag{15}
$$
这里仍是原拉回截面，所有中间角已一并支付。

## 4. 原全 Gamma 与第三精度的显示身份

令 \(\operatorname{ev}\) 为原完整评价，
\(\mathsf A_2:\mathcal H_2\to\Gamma\) 为其真实有限矩阵，
\(\mathcal E_2\) 为同一来源的整数 charge 对角矩阵。
继续使用 R517 的合法整导子
$$
\mathsf D=\nu\mathsf N,\qquad
\mathsf N(w)=w,\quad\mathsf N(\epsilon)=s\epsilon.
$$
它保 \(w^s=p\epsilon\) 及全部截断关系。
R517 的全链式身份代入 (6)，给
$$
\boxed{
\begin{aligned}
\operatorname{ev}(\mathcal L_cH)
={}&d\,\operatorname{ev}(e)\,
       \mathsf D\operatorname{ev}(H)\\
&+\bigl(c(\delta d)\operatorname{ev}(F)
       -d\,\mathsf D\operatorname{ev}(F)\bigr)
       \operatorname{ev}(\mathcal EH)\\
&-2c(\delta d)\operatorname{ev}(e)\operatorname{ev}(H).
\end{aligned}}
\tag{16}
$$
其中 \(d,\delta d\) 也是其同一实际代入。

令
\(\rho=\operatorname{ev}(d^{-C_D}t^rQ\mathfrak m_2)\)，
则完整矩阵式为
$$
\boxed{
\begin{aligned}
J\mathcal T_c={}&
\mathsf M_{\rho d\,\operatorname{ev}(e)}
       \mathsf D\mathsf A_2\\
&+\mathsf M_{\rho(c(\delta d)\operatorname{ev}(F)
              -d\,\mathsf D\operatorname{ev}(F))}
       \mathsf A_2\mathcal E_2\\
&-\mathsf M_{2c\rho(\delta d)\operatorname{ev}(e)}
       \mathsf A_2 .
\end{aligned}}
\tag{17}
$$
这在整个整 \(\Gamma\) 上成立，故保模 \(p^2,p^3\) 和原全部 carry；
没有把 \(\epsilon\) 当微分常量。

真左行的完整转置是将 (17) 三项同时转置，
特别最后一项不能因它是零阶项而删除。
原 \(M\) 的左行仍先按
$$
\lambda_J=m_{13}^{\,T}
\mathsf M_{c_*U_0}^{\,T}\lambda_M
$$
整拉回。全部 \(P_{134}/U_0\)、十三自由行、两条十三行 carry、
\(U_1/p\) 及第三精度均照原矩阵保持。

## 5. 真实物理核缩为三条已付列

继续 R543 的低 \(\ell\) 范围
$$
1\le\ell\le r<h,\quad k=2h+r-s,\quad 0\le k<\ell,\quad
S=s-r,\quad \eta^2=0\bmod t^S.
$$
对相对 \(J\)、整个原 \(M\) 分别使用准确长度
$$
T=T_J=s-r-1,\qquad T=T_M=s-r-14.
\tag{18}
$$
假定
$$
\boxed{T>2\kappa,\qquad h>\kappa.}
\tag{19}
$$

**定理 2。** 对 (10) 的同一真实返回，准确有
$$
\boxed{
\ker(\bar J\,\overline{\mathcal T_c})
\quad\text{或}\quad
\ker(\bar M\,\overline{\mathcal T_c})
=
k\,d^{2c}\oplus k\,d^cF\oplus k\,F^2,
}
\tag{20}
$$
使用对应 (18) 的条件。

**证明。** 对 \(H\) 处于所选物理核，
用 (7) 和原整单位 \(d(P)=1\)，
剥 (10) 的整个非 \(t\) 前缀后，得到
$$
\mathcal V_{F_c}H_c(t,g e^{a\epsilon})=0
\quad\text{于 }k[[t]][\epsilon]/(t^T,\epsilon^2).
\tag{21}
$$
这是对同一个实际 \(H\) 的计算；
\(H_c\) 只由 (5) 运输，不是另添来源。

原因子分支仍是同一个 \(Y=\psi(t)\)。
\(F_c\) 的分支 Euler 导数 \(d^{-c}e\) 在 \(P\) 为单位。
按 R543 的两 Gaussian 行推导，(21) 先给
$$
H_c|_C-H_c(P)\in
H^0(C,\mathcal O_C(2\mathscr D_c-TP)).
$$
此线束次数 \(2\kappa-T<0\)，故 \(H_c|_C\) 是常数。

\(\mathscr D_c\) 有效，常数一是这个线性系的真实截面。
扣掉该常数后，由同一限制核写成
$$
H_c=a_0+F_c H_{1,c},\qquad
H_{1,c}\in H^0(X,\mathcal O_X(\mathscr D_c)).
$$
再按同一个正镜轴，
\(\mathcal V_{F_c}H_{1,c}(t,\psi e^{2\eta})=0\bmod t^T\)，
从而
$$
H_{1,c}|_C-H_{1,c}(P)\in
H^0(C,\mathcal O_C(\mathscr D_c-\min(h,T)P)).
$$
(19) 使这条线束也负度。
因此 \(H_{1,c}=a_1+a_2F_c\)，
最后
$$
H=d^{2c}H_c=a_0d^{2c}+a_1d^cF+a_2F^2.
$$
反向由整身份 (9) 成立，证明 (20)。证毕。

本证明只读 \(T\le S<s<p\) 内的真实 jet，
以及全部已付的曲线线性系。
它不需要 R537 的不可分交数门 \(p>8b^2+4bu\)；
这里的物理强窗口已经直接排除所有额外来源或评价关系。
仍保其他使用中的原 \(f_D<p\) 或扩大预算后的相应门。

## 6. 来源与物理像同时饱和，准确整 Schur 消元

用第1节的角/次数保持提升，
(8) 的三列在整 \(\mathcal H_2\) 中存在并满足 (9)，
且其约化线性独立。
由 R495，
$$
\operatorname{rank}\mathcal H_2=1+2\kappa+\chi.
$$
因此 (20) 给真实约化秩
$$
\boxed{R_c=2\kappa+\chi-2.}
\tag{22}
$$
三个显示核向量本身生成饱和子格。

**定理 3。** 在对应 (19) 中：

1. \(\mathcal T_c\) 的整来源核准确由 (8) 生成；
   其来源返回像在所用真实 \(\mathcal W\) 中 \(p\) 饱和。
2. \(J\mathcal T_c\) 或 \(M\mathcal T_c\) 的全部
   \(R_c\) 个非零 Smith 因子都是单位。
3. 可在同一个实际原矩阵中整分裂并消去这 \(R_c\) 个单位因子；
   剩余矩阵保原全部非单位 Smith 因子及 Bockstein 问题。

**证明。** 三列整关系使特征零秩至多 \(R_c\)，
(20) 的约化秩使它至少 \(R_c\)。
故物理整矩阵没有额外特征零核，且其全部非零 Smith 因子为单位。
来源返回矩阵的秩不小于这个物理秩，
也不超过 \(R_c\)，所以它同样全部非零因子为单位。
这同时证明第1、2项，未从来源饱和跳到物理饱和。

令 \(\mathcal U_c=\operatorname{im}\mathcal T_c\subset\mathcal W\)，
它是来源中的自由直和项。
其物理像也是原目标中的自由直和项；
选整基后，整个原矩阵有块形
$$
\begin{pmatrix}I_{R_c}&A\\0&B\end{pmatrix}.
$$
按同一个来源作整列消元即得
\(\operatorname{diag}(I_{R_c},B)\)。
此为完整整等价，故所有精度的非单位 Smith 因子、
可提升左右核及 Bockstein 均准确运输到 \(B\)。证毕。

若用原 \(M\)，第2、3项须使用
$$
\boxed{s-r-14>2\kappa,\qquad h>\kappa.}
\tag{23}
$$
若只付相对 \(J\) 的 \(s-r-1>2\kappa\)，
不能据此消去原 \(M\) 的全部相应因子。
整 Schur 过程保实际低行高尾及整个 \(U_0\)；
它不是删除原二十六条 carry。

## 7. 此前低 ell 二次临界窗确实满足物理强门

逐个考虑已经存在的真实候选，并保
$$
D=3b,\quad
\kappa=\frac{47}{12}b^2+O(b),\quad \chi=O(b),\quad
r,\ell,k=O(b),
$$
$$
2s+\ell=\dim\mathcal W_{3b}+O(b),\qquad
\dim\mathcal W_{3b}=\frac{141}{8}b^2+O(b).
\tag{24}
$$
原 \(k=2h+r-s\) 给
$$
h=\frac{141}{32}b^2+O(b),\qquad
T_M=\frac{141}{16}b^2+O(b).
$$
因此两个严格余量是
$$
\boxed{
h-\kappa=\frac{47}{96}b^2+O(b),\qquad
T_M-2\kappa=\frac{47}{48}b^2+O(b).
}
\tag{25}
$$
两者最终均正，故整个原 \(M\) 已适用定理2、3。
相对 \(J\) 也随之适用。

若需要扩大固定两个 charge 才能容纳 (10)，
来源维数和复型成本都按该真实扩大读取；
这个固定增加只改变 (24) 的 \(O(b)\) 项。
旧矩阵的左行没有因此自动被赋新列条件。

与 R543 不同，这里无须
\(\mu_{d,1}^2+\mu_{d,2}^2\) 的主阶假设。
原有效极余量被 (6) 的真实平衡项支付，
所以 \(\kappa\) 取代了 \(K_+\)。
相应单位块大小为
$$
\boxed{R_c=\frac{47}{6}b^2+O(b).}
\tag{26}
$$
这没有宣称整个原矩阵满秩；
实际剩余来源和目标仍须保留。

## 8. 与原 forcing 及完整中央的边界

新返回的全部公式始终使用同一个 \(F,Q,t,g\)、同一 \(\mathcal H_2\)
和同一个实际角整数 \(c\)。
在源格中写的是 (6)、(10)，不是免费使用
\(d^{-c}\)、\(d^{-2c}\) 的新全局列。
(17) 保全部 Gaussian、零阶项与三精度。

定理3给一个可用于后续真实余核计算的整消元块。
R502 的完整 \(\xi\)、活 \(V_1\)、原低行高尾及 R479/R481 的同一修正
必须经过这同一个 Schur 过程。
只有余下的实际 forcing 类被证明非零，才会给原提升障碍；
(25) 的严格余量本身不是那条非零结论。

三条原完整中央仍只控制原 \(S,T,U\)。
它们没有被传播到 \(\mathcal T_c(H)\)，
物理单位块也没有自动改变 R418 的全部饱和前缀预算。
下一步是将这个已付整块用于真正剩余矩阵与 forcing，
而不是再将连接容量等同于中央缺陷。
