# R824 — 原四块首次提升的三条强制分支值与中央 Schur 余项

日期：2026-11-15。**状态：下列原四块首次提升恒等式、十三行边界的真实非零余核、三条分支必要值及中央代入公式已证明。**

本篇从 R821 的整个原矩阵出发，不先除去固定导子乘子。对已经属于原格的四次幂首核，首次修正沿同一个正规分支被迫具有系数 $28,-11,3$ 的三个非零值；后两项各有明确的额外读取条件。更直接地，若该首核只借十三行前缀通过第三个满块，则相应十三行带内有一个明确单位首 Bockstein，不能提升到 $p^2$。

这些结论没有假定修正保持 $F$ 的任何幂，也没有把四条中央零变成四次幂首核的存在定理。四中央在原首余核上的真正作用，最后写成同一个有限 Schur 值；重复倍点来源的原生缺陷也完整保留。

## 1. 固定的原格与完整物理修正

保持 R821 的
$$
p=6s-1>211,\qquad 1\le\ell<s-13,\qquad
\ell_0=\ell+13,\qquad a=a_p=p\kappa\in\mathcal O^\times .
\tag{1}
$$
还删去该篇固定四阶子式的有限坏集。置
$$
d=1+8t,\qquad h_7=7+4t+16t^2,\qquad
\rho=d\Theta^{17},\qquad
\mathcal E=\frac{\Theta}{17}\partial_\Theta .
$$
R335 的固定原导子为
$$
\boxed{
G_0=\rho^{40}
 \frac{P_{134}(t)t^{13}(t-1)^{15}h_7^{13}}{d^{17}},
\qquad \mathcal E G_0=40G_0 .
}
\tag{2}
$$
这里保留完整的一百三十四次多项式，且
$P_{134}(0)=-3^4\cdot3159421$；R335§4（依 R328）已证明3159421为分裂素数，故在当前惰性好素数它是单位。

具体的全 canonical 基由 R335(18) 给出：
$$
\frac{C_{n+1,j}}{G_0}
=\rho^n
 \frac{t^{\lfloor(n+1)/4\rfloor+j}
 (t-1)^{\lfloor(n+1)/3\rfloor}
 h_7^{\lfloor(n+1)/4\rfloor}}
 {d^{\lfloor n/2\rfloor}},
\qquad 0\le j\le e_{n+1}.
\tag{3}
$$
每个右端在原点整。对任意已选的有限完整次数范围，以及已逐列支付的混合来源，记相对格为 $\mathscr W_{\rm act}$，完整物理格为
$$
\mathscr L_{\rm act}=G_0\mathscr W_{\rm act}.
\tag{4}
$$
本篇对扩充列的要求就是 (4) 的真实成员性和原点整性；不把新 $V_{66}$ 裸来源免费加入旧格。R473 的返回须按其完整乘子和次数支付。

令 $\vartheta=(g/d)^{1/17}$ 为同一个原 regularized 轴，$t(w)=-w+\cdots$。在所读范围内，
$$
G_0(t(w),\vartheta(w))=w^{13}g_0(w),\qquad g_0(0)\in\mathcal O^\times.
\tag{5}
$$
因此 (4) 的每个完整来源及其所有 $\mathcal E$ 导数都含 $w^{13}$。

本稿 $F(t,\Theta)$ 是原来源方程在 $\rho=d(t)\Theta^{17}$ 后的实际 $\Theta$ 表达；$\mathcal E=(\Theta/17)\partial_\Theta$，$\psi(t)$ 始终指 $\Theta$ 坐标的正规分支。第1–6节只需这个分支简单，不先假全部 $\Theta$ 表达不可约；第7节的结式论证另加其显示的全局不可约条件，并使用该实际表达的双次数，不能混用代入前的 $Y$ 次数。

本篇用 $R$ 专指**完整物理首次修正**，并另用
$R_{\rm rel}=R/G_0$ 表示相对修正。二者从不混用。若给定一个实际相对来源约化
$$
\bar P=t^rF^4Q,\qquad r\ge0,\quad
F(0,1)=0,\quad
(\mathcal EF)(0,1)Q(0,1)\ne0,
\tag{6}
$$
选整系数提升 $\widetilde F,\widetilde Q$ 后，每个同一原系数类的实际提升准确写为
$$
\boxed{
\Phi^{(2)}=G_0t^r\widetilde F^4\widetilde Q+pR,\qquad
R=G_0R_{\rm rel}.
}
\tag{7}
$$
相对系数差被 $p$ 整除，所以 $R_{\rm rel}$ 在原点整。这也直接证明 $R$ 仍含整个 $G_0$，无需先消去非单位的 $t^{13}$。

允许的 $R_{\rm rel}$ 是一个确定的真实仿射空间：若 $\Phi_b$ 是一个实际系数提升，令
$$
R_{{\rm rel},b}
=\frac{\Phi_b/G_0-t^r\widetilde F^4\widetilde Q}{p},
\qquad
\mathscr A_{\rm rel}=R_{{\rm rel},b}+\overline{\mathscr W}_{\rm act}.
\tag{8}
$$
以后所有修正都在此空间内。没有假定 $\widetilde F,\widetilde Q$ 或它们的积分别属于原格，也没有把 (8) 扩成全部双次数多项式。

## 2. 原四块、实际接触和首核窗口

令 $\Phi_i(w)=(\mathcal E^i\Phi)(t(w),\vartheta(w))$，
$\mathscr S$ 为准确的 $s$ 阶系数移位。对完整物理来源，原评价在
$$
\Gamma_{\rm phys}
=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^4,w^{\ell_0}\epsilon^3)
$$
中准确是
$$
\boxed{
\mathfrak M_4(\Phi)=
\begin{pmatrix}
[\Phi_0]_{<s}\\
[a\Phi_1+p\mathscr S\Phi_0]_{<s}\\
[\frac{a^2}{2}\Phi_2+pa\mathscr S\Phi_1+
 p^2\mathscr S^2\Phi_0]_{<s}\\
[\frac{a^3}{6}\Phi_3+\frac{pa^2}{2}\mathscr S\Phi_2+
 p^2a\mathscr S^2\Phi_1+p^3\mathscr S^3\Phi_0]_{<\ell_0}
\end{pmatrix}.
}
\tag{9}
$$
这是将 $\Phi(t,\vartheta e^{a\epsilon/17})$ 的整个指数展开后，再用 $w^s=p\epsilon$ 归并得到的原 $M$。它只采用 R335/R821 已固定的单位规范；(2) 的四十 charge、$P_{134}$、全部普通单位和三条十三行带都在 $\Phi$ 中。不能把 (9) 的 $\Phi$ 换成 $P=\Phi/G_0$ 而保持同一窗口。

设
$$
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w)),\qquad 1\le h<s,
\qquad r_0=r+13 .
$$
由 $\mathcal EF$、$Q$ 为单位，
$$
\operatorname{ord}_w\bar\Phi_i=r_0+(4-i)h,\qquad 0\le i\le3.
$$
故完整物理首核条件准确为
$$
\boxed{
\bar\Phi\in\ker\overline{\mathfrak M}_4
\quad\Longleftrightarrow\quad
r_0+2h\ge s,\qquad r_0+h\ge\ell_0 .
}
\tag{10}
$$
以下置
$$
k=r_0+2h-s\ge0 .
\tag{11}
$$
第4节的十三行边界只需 $k<\min(13,\ell_0)$。
第5节三个分支值使用更明确的窗口
$$
\boxed{k<\min(h,s-h,\ell_0).}
\tag{12}
$$
特别 $h+k<s$、$k<\ell_0$；它们分别保证第三、第四块的实际所读行存在。

## 3. 首次商的完整低行：先保留根修正

假设 (7) 满足 $\mathfrak M_4(\Phi^{(2)})\in p^2\Gamma_{\rm phys}$。写
$$
f=\widetilde F(t(w),\vartheta(w))=w^hu+p\xi,\qquad
\xi\in\mathcal O[w]_{<h},
$$
$$
e=(\mathcal E\widetilde F)(t(w),\vartheta(w)),\qquad
C=\frac{G_0(t(w),\vartheta(w))}{w^{13}}
 \left(\frac{t(w)}w\right)^r
 \widetilde Q(t(w),\vartheta(w)).
\tag{13}
$$
$C(0),u(0),e(0)$ 全为单位。$\xi$ 是实际低阶根修正，不能预先令其为零。

以下 $R_i=(\mathcal E^iR)(t(w),\bar\vartheta(w))$，
以及 $C,u,e,\xi,a$ 均已约化。在 (12) 的有限读取范围中，完整首次商给
$$
\boxed{
\begin{aligned}
R_0&\equiv0 &&\pmod{w^s},\\
R_1&\equiv-\frac1a w^{2h+k}Cu^4
 &&\pmod{w^s},\\
R_2&\equiv-24w^{r_0+h}Cu\xi e^2
 -\frac8a w^{h+k}Cu^3e
 &&\pmod{w^{h+k+1}},\\
R_3&\equiv-24w^{r_0}C\xi e^3
 -\frac{36}a w^kCu^2e^2
 &&\pmod{w^{k+1}}.
\end{aligned}
}
\tag{14}
$$
后两行的模阶就是显示的模阶，不声称它们已给完整第三、第四块。

证明必须包括总 Euler 对 $C$ 的作用。令 $C_i$ 为先作第 $i$ 次总 Euler 再评价的系数，并记 $e_j=\mathcal E^j\widetilde F$ 的实际评价。则
$$
\begin{aligned}
\Phi_1^{\rm base}/w^{r_0}
 &=4Cf^3e+C_1f^4,\\
\Phi_2^{\rm base}/w^{r_0}
 &=12Cf^2e^2+(4Ce_2+8C_1e)f^3+C_2f^4,\\
\Phi_3^{\rm base}/w^{r_0}
 &=24Cfe^3+(36Cee_2+36C_1e^2)f^2\\
 &\quad +(4Ce_3+12C_1e_2+12C_2e)f^3+C_3f^4 .
\end{aligned}
\tag{15}
$$
这些是完整来源式，非仅作用于 $F$ 的最高项。

第一块的 base 首次商从 $r_0+3h\ge s$ 起。第二块的 Gaussian 首次商从 $r_0+2h=s+k$ 起，低于 $s$ 不贡献；唯一留下的移位项为
$\mathscr S(w^{r_0+4h}Cu^4)=w^{2h+k}Cu^4$，得到 (14) 前两行。

第三块的 Gaussian 首次商最低项是
$12a^2w^{r_0+h}Cu\xi e^2$，而
$pa\mathscr S\bar\Phi_1^{\rm base}$ 最低项是
$4pa\,w^{h+k}Cu^3e$。含 $C_1,e_2$ 的其余 Gaussian 项从 $s+k$ 起，额外移位项从 $2h+k$ 起，均在所读末行之后。除以 $a^2/2$ 给第三行。

第四块的 Gaussian 首次商最低项为
$4a^3w^{r_0}C\xi e^3$；其余项从
$r_0+h\ge\ell_0$ 起。实际移位
$(pa^2/2)\mathscr S\bar\Phi_2^{\rm base}$
最低项为 $6pa^2w^kCu^2e^2$，其余从 $h+k$ 起。除以 $a^3/6$ 给末行。
(9) 中已有 $p^2,p^3$ 的项在首次商约化后才消失；没有预先删其更高精度作用。

特别，令 $q=\min(r_0,k)$，有
$$
\operatorname{ord}R_0\ge s,\quad
R_1\equiv-\frac1a w^{2h+k}Cu^4\pmod{w^s},\quad
\operatorname{ord}R_2\ge h+q,\quad
\operatorname{ord}R_3\ge q
\tag{16}
$$
在各自显示窗口内成立。

## 4. 原十三行带中的一个单位左配对

**定理1。** 若 (10) 成立且
$$
\boxed{0\le k<\min(13,\ell+13),}
\tag{17}
$$
则该实际首核不能在同一个完整原格中提升到 $p^2$。其原首 Bockstein 在目标行 $3s+k$ 上有单位配对。

这里不需要 (12) 的 $k<h$ 或 $k<s-h$。直接在 (9) 的末块读第 $k$ 行：因为 $R=G_0R_{\rm rel}$，
$$
[w^k]R_3=0,\qquad
[w^k]\big(w^{r_0}C\xi e^3\big)=0
\quad(k<13,\ r_0\ge13).
$$
而实际 carry 给
$$
\boxed{
[w^k]\overline{\mathfrak M_4(\Phi^{\rm base})_3/p}
=6a^2C(0)u(0)^2e(0)^2\in k^\times .
}
\tag{18}
$$
(15) 的其它项分别从 $r_0+h\ge\ell_0$ 或 $h+k>k$ 起，不进入该行。

原 $\overline{\mathfrak M}_4$ 的每列末块都含 $w^{13}$，所以目标坐标
$\lambda_k=[\epsilon^3w^k]$ 在**整个原首像**上为零。式 (18) 因而不是某个较小修正空间的障碍，而是同一个完整 $C_1=\operatorname{coker}\overline{\mathfrak M}_4$ 中的真实非零左配对。

这个结论准确消去了该四次幂族借前缀得到的最初十三行宽限：在本范围若能提升，必须有 $k\ge13$，即
$$
r+2h\ge s .
\tag{19}
$$
仍不能从 (19) 推出已能提升。也不把本定理外推到未经证明共有 $G_0$ 的其它来源列。

## 5. 不预先保持因子的三条真实分支值

令 $\psi(t)$ 为 $F(t,\psi)=0$、$\psi(0)=1$ 的正规分支。$F_\Theta(0,1)\ne0$ 给其存在唯一性。以下所有分支式用同一个 $t(w)$ 参数化。

**定理2。** 在 (10)、(12) 中，每一个真实 (7) 必满足
$$
\boxed{
(\mathcal E^2R)(t(w),\psi(t(w)))
=\frac{28}{a}C(0)u(0)^3e(0)\,w^{h+k}
+O(w^{h+k+1}).
}
\tag{20}
$$
若再有 $2h+k<s$，则
$$
\boxed{
(\mathcal ER)(t(w),\psi(t(w)))
=-\frac{11}{a}C(0)u(0)^4\,w^{2h+k}
+O(w^{2h+k+1}).
}
\tag{21}
$$
若进一步 $3h+k<s$，则
$$
\boxed{
R(t(w),\psi(t(w)))
=\frac{3C(0)u(0)^5}{a e(0)}\,w^{3h+k}
+O(w^{3h+k+1}).
}
\tag{22}
$$
三个首系数在当前素数全为单位。特别，修正分别不可能属于 $F^3$、$F^2$、$F$ 理想。后两断言只在其显示的额外范围内成立。

**证明。** 用总 Euler 的流坐标，置
$$
v=17\log\frac{\bar\vartheta(w)}{\psi(t(w))}
=\frac{w^hu}{e}+O(w^{2h}).
\tag{23}
$$
这里只使用到所需有限阶的对数和 Taylor 多项式。因 $4h<4s<p$，所用分母均为单位；不在特征 $p$ 中使用一个未经定义的无限对数。对任一完整多项式，
$R(t,\psi)=e^{-v\mathcal E}R(t,\bar\vartheta)$ 在这些有限阶准确成立。

先读 $\mathcal E^2R$：
$$
(\mathcal E^2R)(\psi)
\equiv R_2-\frac{w^hu}{e}R_3
\pmod{w^{h+k+1}}.
\tag{24}
$$
二次 Taylor 余项从 $2h>h+k$ 起。$v-w^hu/e$ 乘 $R_3$ 的最低可能阶为 $2h+\min(r_0,k)$；若取 $r_0$，该阶为 $s+k$，若取 $k$，该阶为 $2h+k$，两者均严格大于 $h+k$。

代入 (14) 后，两条含 $\xi$ 的整段
$-24w^{r_0+h}Cu\xi e^2$ 与
$+24w^{r_0+h}Cu\xi e^2$ 精确相消。剩余系数是
$-8+36=28$，得到 (20)。即使 $r_0\le k$，也必须先作这个相消，不能把 $\xi$ 项单独判为高阶。

再设 $2h+k<s$。由 $s=r_0+2h-k$，准确等价于 $r_0>2k$，所以 $r_0>k$。完整二次 Taylor 给
$$
(\mathcal ER)(\psi)
\equiv R_1-\frac{w^hu}{e}R_2+
 \frac{w^{2h}u^2}{2e^2}R_3
\pmod{w^{2h+k+1}}.
\tag{25}
$$
三次余项从 $3h>2h+k$ 起，(14) 的各输入精度足够。
含 $\xi$ 的合项从 $r_0+2h>2h+k$ 起；其余三个系数为
$-1+8-18=-11$，得到 (21)。

若 $3h+k<s$，则 $r_0>h+2k$。还可读完整三次 Taylor：
$$
R(\psi)\equiv
R_0-\frac{w^hu}{e}R_1+
 \frac{w^{2h}u^2}{2e^2}R_2-
 \frac{w^{3h}u^3}{6e^3}R_3
\pmod{w^{3h+k+1}}.
\tag{26}
$$
$R_0$ 的未知尾从 $s$ 起，四次 Taylor 余项从
$4h>3h+k$ 起，$\xi$ 合项从 $r_0+3h>3h+k$ 起。剩余系数是
$1-4+6=3$，得到 (22)。当 $2h+k=s$ 或 $3h+k=s$ 时，未读的整行能进入相应目标，不能把严格不等号改成非严格。$\square$

无论后两额外条件是否成立，同一个展开还给
$$
\boxed{
\begin{aligned}
\operatorname{ord}R(t,\psi)&\ge\min(s,3h+k),\\
\operatorname{ord}(\mathcal ER)(t,\psi)&\ge\min(s,2h+k).
\end{aligned}}
\tag{27}
$$
例如先由 (16) 得第一行下界 $\min(s,3h+q)$。
若 $q=r_0<k$，则 $3h+r_0=s+h+k>s$；因此它准确简化成 (27)。
第二行同理用 $2h+r_0=s+k\ge s$。这些下界没有从未知高 Euler 行补出额外零。

改变 $\widetilde F$ 的系数提升，只使 $R$ 的约化改变一个
$4G_0t^rF^3QB$；改变 $\widetilde Q$ 只增加 $G_0t^rF^4B$。
它们的前三个分支值 $R|_F,(\mathcal ER)|_F,(\mathcal E^2R)|_F$ 都为零。
所以 (20)–(22) 对提升选择不变，不是某种特选 $\xi$ 的结果。

## 6. 已保留 carry 后的相对修正与有限像条件

现在才使用真实成员性 $R=G_0R_{\rm rel}$。在真分支上写
$$
G_0(t(w),\psi(t(w)))=w^{13}g_F(w),\qquad
c_0=\frac{C(0)}{g_F(0)}\in k^\times.
$$
由 $\mathcal E G_0=40G_0$，
$$
\begin{aligned}
R/G_0&=R_{\rm rel},\\
(\mathcal ER)/G_0&=\mathcal ER_{\rm rel}+40R_{\rm rel},\\
(\mathcal E^2R)/G_0&=\mathcal E^2R_{\rm rel}
 +80\mathcal ER_{\rm rel}+1600R_{\rm rel}.
\end{aligned}
\tag{28}
$$
若实际提升存在，第4节已经迫 $k\ge13$。置
$$
m_0=\min(s,3h+k)-13,\quad
m_1=\min(s,2h+k)-13,\quad
m_2=h+k-13 .
\tag{29}
$$
则 $m_0\ge m_1>m_2\ge0$。式 (20)、(27)、(28) 准确给
$$
\boxed{
\begin{aligned}
\operatorname{ord}R_{\rm rel}|_F&\ge m_0,\\
\operatorname{ord}(\mathcal ER_{\rm rel})|_F&\ge m_1,\\
(\mathcal E^2R_{\rm rel})|_F
 &=\frac{28}{a}c_0u(0)^3e(0)\,w^{m_2}
  +O(w^{m_2+1}).
\end{aligned}}
\tag{30}
$$
若 $2h+k<s$，还得
$$
(\mathcal ER_{\rm rel})|_F
=-\frac{11}{a}c_0u(0)^4\,w^{2h+k-13}
+O(w^{2h+k-12});
\tag{31}
$$
若 $3h+k<s$，则
$$
R_{\rm rel}|_F
=\frac{3c_0u(0)^5}{a e(0)}\,w^{3h+k-13}
+O(w^{3h+k-12}).
\tag{32}
$$
这里的减十三发生在完整物理提升及全部实际读取条件已经证明之后。它没有把 (12) 换成较大的相对窗口，也没有消掉原三十九行的 Smith 成本。

因此下一项明确有限对象是
$$
\boxed{
R_{\rm rel}\in\mathscr A_{\rm rel}
\quad\text{同时实现 (30) 及在可读范围内的 (31)、(32)。}
}
\tag{33}
$$
每个条件都是同一分支上的有限多项式行。例如
$[(\mathcal E^2R_{\rm rel})(t,\psi)]_{\le m_2}$ 必须等于
显示的一个非零末项单项式，所有较低系数同时为零。
允许列只能是 (8) 的原列。若一个真实左行杀掉这些列的像，却对仿射目标取非零值，就得到原首次提升障碍；单看维数或把修正空间换成较大的矩形不能代替这个条件。

(33) 是必要条件，不是完整提升的充分条件。(9) 的未被这几个分支读法使用的所有行仍须满足。

## 7. 不扩大修正空间的三个次数排除

本节给 (33) 的一个直接可用充分排除标准，不声称原预算自动满足它。
设 $F$ 在 $k[t,\Theta]$ 中不可约，双次数为 $(a_F,b_F)$。
若原实际仿射修正经过已经支付的共同角单位清分母后，全部满足
$$
\deg_tR_{\rm rel}\le M,\qquad
\deg_\Theta R_{\rm rel}\le N,
$$
置
$$
B_j=b_FM+a_FN-2j\,a_Fb_F,\qquad j=0,1,2.
\tag{34}
$$
清分母只乘同一个在原点为单位、与 $\mathcal E$ 交换的角多项式，
须将其次数计入 $M$；它不增加来源列或删除任何 carry。

若
$$
\boxed{m_0>B_0,\qquad m_1>B_1,\qquad m_2>B_2,}
\tag{35}
$$
则实际 $p^2$ 提升不存在。

证明用无分母 Sylvester 恒等式。若 $F\nmid R_{\rm rel}$，
非零 $\operatorname{Res}_\Theta(F,R_{\rm rel})$ 的次数至多 $B_0$，
但 (30) 令其在 $t=0$ 有至少 $m_0$ 阶零，矛盾。
故 $R_{\rm rel}=FR_1$。真分支上
$\mathcal ER_{\rm rel}=(\mathcal EF)R_1$，第二个不等式同理迫
$R_1=FR_2$。再由
$\mathcal E^2R_{\rm rel}|_F=2(\mathcal EF)^2R_2|_F$
和第三个不等式迫 $F\mid R_2$，与 (30) 的单位首项矛盾。

还有三个更窄的必要条件，不需要先假设修正保持因子：
$$
\begin{array}{c|c}
\text{实际已付的读取／次数条件}&\text{存在提升所必需}\\ \hline
3h+k<s &3h+k-13\le B_0\\
m_0>B_0,\quad2h+k<s&2h+k-13\le B_1\\
m_0>B_0,\quad m_1>B_1&h+k-13\le B_2 .
\end{array}
\tag{36}
$$
各行分别使用 (32)、(31)、(30) 的准确非零阶。
$M,N$ 必须来自 (8) 的整个原仿射空间；只在较小的试验列中成立的界不能用于 (35)–(36)。特别，新 degree66 来源若经固定导子返回，其全部额外次数仍须计入。

## 8. 四原中央实际代入的是哪一条 Schur 行

本节不再取条件性的四次幂形状，回到同一个完整原矩阵的任意真实首核向量。沿用 R821 的四坐标 $\mathbf u=(u_0,u_1,u_2,u_3)$，完整四中央整多项式为
$\mathbf F=(F_S,F_T,F_U,F_V)^t$，并置
$$
\mathbf b=\overline{\mathbf F(0)},\qquad
B_4=
\big([w^4]\nu,[w^3]\nu,[w^2]\nu,[w]\nu\big)_{\nu=S,T,U,V}.
$$
其固定行列式为
$$
\det B_4=-\frac{33226598045199130624}{173559375}.
\tag{37}
$$
四条原完整中央同时零，严格给
$$
\overline{\mathbf u^*}=-B_4^{-1}\mathbf b .
\tag{38}
$$
这里 $\mathbf b$ 是同一原参考的完整聚合基准，不是四个自由常数。

R821 已证明 $\bar M_{\mathbf u}=\bar M_\circ$。因此使用同一个
$$
K_1=\ker\bar M_\circ,\qquad C_1=\operatorname{coker}\bar M_\circ
$$
和同一个真实首 Bockstein。令 $L_j:K_1\to C_1$ 为该篇 (41) 中 $u_j$ 的系数，则
$$
\beta_1^{\mathbf u}=\beta_1^\circ+\sum_{j=0}^3\bar u_jL_j .
\tag{39}
$$
为使这个接口完全明确，对同一个源向量 $v\in K_1$，设
$W_i(v)=\sum_\Phi v_\Phi Q_\Phi^iA_\Phi(w)$；$Q_\Phi$ 是总 charge，$A_\Phi$ 保所有原单位。定义
$$
d_{j,i}=[w^{s-13+i}]W_j\ (j=1,2),\qquad
d_{3,i}=[w^{\ell+i}]W_3,\quad0\le i\le3,
$$
并令负下标为零。那么
$$
\boxed{
L_j(v)=\left[
\sum_{i=0}^3d_{1,i-j}\epsilon w^{s-4+i}
+a\sum_{i=0}^3d_{2,i-j}\epsilon^2w^{s-4+i}
+\frac{a^2}{2}\sum_{i=0}^3d_{3,i-j}\epsilon^3w^{\ell+9+i}
\right].
}
\tag{40}
$$
方括号商去整个 $\operatorname{im}\bar M_\circ$。十二条尾系数全属于同一个 $v$。

因此，对任何实际左行 $\lambda\in C_1^\vee$，
$$
\boxed{
\lambda\beta_1^{\mathbf u^*}(v)
=\lambda\beta_1^\circ(v)
-\big(\lambda L_0(v),\ldots,\lambda L_3(v)\big)B_4^{-1}\mathbf b .
}
\tag{41}
$$
这才是四中央与真实首次提升的有限共同对象。子式 (37) 为单位，只允许作这一个整代入；它不决定 (41) 为零或非零。

给定一个实际首单位块，可等价地对完整矩阵作
$$
M=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad \mathcal S(\mathbf u)=D-CA^{-1}B .
\tag{42}
$$
$\mathcal S/p\bmod p$ 表示 (39)。要付 $p^3,p^4$ 的提升，必须继续在这个真实 Schur 块上逐次整消元，并代入 (38) 的后续 Hensel 位。R821 的末端项
$$
\frac{p^3\epsilon^3}{24}w^{s-3}P_3^4
 J_{4,\circ}\mathcal E_{\rm tot}^{\,4}
$$
及整个 $U_{0,\circ}$ 继续保留；本篇只在首次商约化时暂不读取它们。

尤其，原 $M\bmod p^4$ 只读 $\mathbf u^*\bmod p^3$，而完整中央必要系统给到模 $p^4$。不能把矩阵没有读取的最后一位自动认作一个已得到的深核或非零左配对。

## 9. 重复倍点也可进入必要系统：准确缺陷与失去免费推论之处

这里明确说明，重复来源并非“禁止输入”；它们可以合法进入同一必要系统，但不能按形式 Jacobian 的行数重复计算算术条件。

令 $m$ 为固定正整数、$p\nmid m$，
$$
A_m(z)=m^{-6}S(mz).
$$
保全部 Gaussian 重标后，R812/R821 的完整身份为
$$
J_{A_m}(v)=m^{-6}(m^{p-1})^vJ_S(v),\qquad
J_{A_m}'(0)=m^{-6}J_S'(0).
\tag{43}
$$
共同的整归一是 $(a_p/p)J'$, 所以实际原点上
$$
F_{A_m}(\mathbf u^*)=m^{-6}F_S(\mathbf u^*)\pmod{p^4}.
\tag{44}
$$
例如四个不同整数 $m_i$ 的共同角族仍可有单位四阶 Jacobian。其模 $p$ 行准确是
$$
B_{m_i}=
\big(m_i^{18}S_4,\ m_i^{12}S_3,\ m_i^6S_2,\ 1\big),
\qquad S_j=[w^j]S .
\tag{45}
$$
R821 的 $S_2,S_3,S_4$ 全非零；以四个不同的 $m_i^6$ 作 Vandermonde，
在删去一个固定有限坏集后，这个矩阵可逆。与此同时，(44) 的四个原中央仍只有同一个 $J'_S(0)$。

两件事为何相容，可以在完整来源上准确看见。围绕实际对象作共同角变动 $\delta h$，正确的倍点 family 是
$$
m^{-6}S(mz)e^{\delta h(mz)};
$$
共同 charge $m^2$ 的计算 family 则是
$$
m^{-6}S(mz)e^{m^2\delta h(z)}.
$$
它们的准确比值为
$$
\boxed{\exp\{m^2\delta h(z)-\delta h(mz)\}.}
\tag{46}
$$
正确 pullback family 的整中央始终成比例；较大的形式 Jacobian 读取的是 (46) 的原生缺陷。

更具体地，在同一共同角参考下写
$$
F_{A_m}(\mathbf u)\equiv b_m+B_m\mathbf u,\qquad
F_S(\mathbf u)\equiv b_S+B_S\mathbf u\pmod p .
$$
由真实来源身份 (44)，无条件有
$$
\boxed{
b_m-m^{-6}b_S
=-(B_m-m^{-6}B_S)\overline{\mathbf u^*}.
}
\tag{47}
$$
这并未使用 $J'_S(0)=0$。所以不能把新增的 $b_m$ 当独立基准、同时丢掉 (46)–(47)，再把增加的形式秩改称新增算术零。

若假设原 $J'_S(0)=0$，全部复制行确实为零；它们的形式必要系统仍然有效。由它求出的坐标应继续完整代入 (41)–(42)，包括所有原生缺陷和同一个来源格。这一步没有自动使 Schur 值为零、构造四次幂候选，或证明某个指定左行非零。准确尚缺的是这些实际 Schur 值与完整原修正像的相容性，而不是一句未定义的“中央独立性”。

新 $E_{-11}$ 来源有十一处真实 ramified 角色，R821 已排除它是旧 $S,T,U$ 的 CM 标量 pullback。但这一算术区别也不替代 (41) 或 (33) 的实际非零比较。

## 10. 已付结论与继续的同源有限问题

本篇已经给出三个可以直接用于原问题的结果。

1. 对 R821 同一个完整原格，满足 (10)、(17) 的四次幂首核有明确单位左配对 (18)，不能提升到 $p^2$。这是真正原三十九行带内的排除。
2. 其余满足 (12) 的可读范围内，任何提升都必须在同一真实仿射修正空间实现 (30)–(33)；三个首常数分别是 $28,-11,3$，全部根修正、总 charge、完整 $G_0$ 和十三行成本已支付。式 (35)–(36) 给同源的可检验排除条件。
3. 四条原中央的首位只通过 (41) 进入真实首余核；更高位继续通过 (42) 的完整整消元。重复倍点的恒等式 (43)–(47) 精确说明了为何形式低 jet 秩不能替代这一步。

仍未证明原全部首核都具有 (6) 的四次幂形状，也未证明原全局预算必产生这样一个可提升的类。新增 degree66 来源的完整中央仍由 R816/R820 支付，其乘积、导子返回和任意修正列没有被赋新的中央零。

本篇所有新增等式均由完整来源、有限 Taylor 和实际目标逐式推导；不使用目标素数扫描或新的数值样本。固定中央数据沿用 R821 已登记的公开运行及全部有限坏集。

## 依赖

- [R821：第四原来源、四高轴与完整四块](R821-original-four-central-axes-and-complete-four-block-carries.md)。
- [R335：整个原导子的准确整基及固定乘子](R335-full-integral-canonical-conductor-and-exact-relative-source.md)，尤其 (18)、(21)–(23)。
- [R459：不先保持因子的真实三次首修正](R459-actual-angular-content-and-padded-cubic-first-lift.md)；本篇使用原四块并把十三前缀保在物理修正中。
- [R425：完整中央与原 Schur 逐级消元](R425-complete-two-central-hensel-parameters-and-four-row-schur-interface.md)。
- [R812：倍点 Gaussian 和中央的准确分布关系](R812-original-same-charge-cancellation-and-complete-source-budget.md)。
- [R473：同一归一化与固定整导子](R473-three-source-function-field-normalization-and-integral-conductor.md)。
