# R286：完整负三—负二 Gaussian 乘积的三外矩与两个真实余门

日期：2026-11-15。**完整原式的纸面推导；没有执行新的求积、profile 采样、符号消元、人工检查或研究计算。**

[R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md) 给出了全部对称二层 history 的准确系数；[R284](R284-six-alternating-packets-pay-the-square-history-and-even-energies.md) 在原有限数据纤维内支付了整个 $E_{-3}^2$。本稿单独提取相邻的 $E_{-3}E_{-2}$，保完整 outer/inner 圆、原右锚以及第三槽的真实左尾。

结论有明确范围：在当前 even 微包、原同 $\mathcal F$ 纤维和完整 odd 包装的实际圆上，该乘积的零外矩随 $H_1=0$ 消失；其余两个外矩准确归入下述两个标量条件。它们尚未由 R284 的五量根支付。本稿不把两条方程的数量当作秩，也不从 principal 行共线推断完整方程相同。

## 1. 原系数及规范

固定共同右锚 r，

$$
Jw(x)=\int_x^r w(t)\,dt,\qquad (Jw)'=-w.
$$

沿用 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的三个实际外矩：

$$
I_0(u,v)=\int u''v'',\quad
I_1(u,v)=\int xu''v'',\quad
I_2(u,v)=\int(x^2u''v''+2u'v').
\tag{1}
$$

令

$$
P=\Phi_{r_0},\qquad R=\Phi_{r_1},\qquad S=\Phi_{s_0}.
$$

完整原二次算子是

$$
P(u,v)=J(u''v''),\quad
R(u,v)=u'v'+xJ(u''v''),\quad
S(u,v)=J(xu''v'').
\tag{2}
$$

当前共振参数 $\varepsilon=\kappa^2/4$、$\kappa\ne0$ 给

$$
B_{-3}=cP,\qquad B_{-2}=aR+bS,
$$

$$
a=-\frac{51\kappa^4+2\kappa^2+8}{64h_e^2},\quad
b=-\frac{17\kappa^4+4\kappa^2}{32h_e^2},\quad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}.
\tag{3}
$$

特别 $a<0,b<0,c\ne0$。这些是实际 Gaussian 常系数，不与下文各包方向 $a_i,b_i$ 混淆。

对整个圆取

$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u.
$$

定义 normalized mixed 外矩

$$
M_j(P,X)
=-I_j(PD,XD)
+I_j\{u,P(u,XD)+X(u,PD)\},
\quad X=R,S.
\tag{4}
$$

R282 的原二阶平方与第三 history 一起给

$$
[E_{-3}E_{-2}]\mathscr K_\theta
=
2c\left\{
\frac{1+j_\sigma^2}{4h}(aM_0(P,R)+bM_0(P,S))
+\frac{j_\sigma}{2}(aM_1(P,R)+bM_1(P,S))
+\frac h4(aM_2(P,R)+bM_2(P,S))
\right\}.
\tag{5}
$$

这里 $j_\sigma=2\varepsilon\kappa\sigma^2$，$h=h_e e^{\varepsilon\sigma^2}$。因子2属于不同字母的对称乘积，不是面积交换子的系数。由原 Gaussian 词独立性及 $e^{\varepsilon\sigma^2}$ 的超越性，(5)全 $\sigma$ 恒零准确等价于三个括号外矩分别为零。

## 2. 先保完整合法内槽，再进行局部化

记

$$
v=u',\quad r=u'',\quad F=(f'')^2,\quad
d=F-r^2,\quad e=(f')^2-v^2,\quad
\ell=e''-2d.
\tag{6}
$$

这里 d 是 $D^{[2,2]}$；e 只是本节的导数平方差，不是几何 R56 的同名量。令

$$
A=PD=Jd,\quad C_R=RD=e+xA,\quad C_S=SD=J(xd).
$$

整个圆已经付真实三矩，特别 $\int d=\int xd=0$。因此 $A,C_R,C_S$ 在两端 collar 真正为零。这个结论是对完整 D 而言，**不能逐个微包使用**。

原右积分直接给

$$
\begin{aligned}
A'&=-d,& A''&=-d',\\
C_R'&=e'+A-xd,& C_R''&=\ell-xd',\\
C_S'&=-xd,& C_S''&=-d-xd'.
\end{aligned}
\tag{7}
$$

外第三槽

$$
T_X=P(u,C_X)+X(u,A)
$$

可以有左常尾或线性尾。下列公式不要求其左尾为零：

$$
\begin{aligned}
T_S'&=rd+2xrd',\\
T_S''&=r'd+3rd'+2x(rd')',
\end{aligned}
\tag{8}
$$

$$
\begin{aligned}
T_R'&=-r\ell-rd-vd'-J(rd')+2xrd',\\
T_R''&=-(r\ell)'-r'd+rd'-vd''+2x(rd')'.
\end{aligned}
\tag{9}
$$

例如 $P(u,C_S)'=r(d+xd')$，$S(u,A)'=xrd'$；这两项之和有 $(rd)'$，不能把它误略为只含 $2(rd')$ 的表达式。

把(7)—(9)代入(1)、(4)，所有 IBP 的端项含紧 u、d、e 或真正紧的 A。唯一需要特别保留、再由完整内槽消失的项是

$$
2\int dA=\left(\int d\right)^2=0.
\tag{10}
$$

它在 $M_2(P,R)$ 的 $-2\int A'C_R'$ 中出现。若先分成单包并对各包擅自删掉，结论会错误；本稿始终先用完整(10)，然后才按不交支持相加。

另一个含 history 的项按紧 u 准确变为

$$
\int vJ(rd')=\int urd'.
\tag{11}
$$

这里也没有把 $J(rd')$ 的左尾置零。完成(10)—(11)后，全部六个外矩只剩真实局部积分。

## 3. 两个一外矩的原积分式

先列最直接暴露低阶余项的两个 $I_1$。由(7)—(9)得到

$$
\boxed{
M_1(P,S)
=-\int x^2F'd'
-\frac32\int xr^2d'
-\frac12\int r^2d
+\frac12\int d^2.
}
\tag{12}
$$

并有

$$
\boxed{
\begin{aligned}
M_1(P,R)-M_1(P,S)
={}&\int x\{\ell(d'+rr')+vr'd'\}\\
&+\int\{r^2\ell+r^2d+rvd'-d^2/2\}.
\end{aligned}}
\tag{13}
$$

两个式子都包含实际低阶项；它们不是只给 $u'''$ principal。

作为(12)的核对，$-\int xA''C_S''$ 给
$-\int x^2(d')^2+\frac12\int d^2$。外槽项给
$-2\int x^2rr'd'-\frac32\int xr^2d'-\frac12\int r^2d$。
合并 $(d')^2+2rr'd'=F'd'$ 即得原式。

对 $I_2$ 必须同时保留 $-2\int A'C_X'$ 与 $2\int vT_X'$。例如 S 的完整式是

$$
\boxed{
\begin{aligned}
M_2(P,S)
={}&-\int x^3F'd'
-\frac72\int x^2r^2d'
-\int xr^2d-\int xd^2\\
&+2\int vrd+4\int xvrd'.
\end{aligned}}
\tag{14}
$$

后两项和 $-\int xd^2$ 均来自完整的一阶导配对；只用加权二导会丢掉它们。

## 4. 全合法圆局部化后的六条微包贡献

写实际不交表示

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\quad
c_i=a_i\cos\theta+b_i\sin\theta,\quad d_i=a_i^2-c_i^2.
$$

对每个实际实微包定义

$$
K_{m,i}=\int x^m\{((u_i'')^2)'\}^2,\qquad
J_{m,i}=\int x^m u_i'u_i''(u_i''')^2,
$$

$$
C_{m,i}=\int x^m(u_i'')^4,\qquad
N_i=\int u_i'(u_i'')^3.
\tag{15}
$$

由第2节完成整体端项处理后，$M_j$ 是下表各实际包贡献的和。表中简写 $A_i=a_i^2d_i$、$B_i=c_i^2d_i$、$D_i=d_i^2$。

| 外矩 | $M_j(P,S)$ 的第 i 包贡献 | $M_j(P,R)$ 的第 i 包贡献 |
|---|---|---|
| $j=0$ | $-A_iK_{1,i}$ | $-A_iK_{1,i}+4A_iJ_{0,i}$ |
| $j=1$ | $-A_iK_{2,i}+(B_i/4+D_i/2)C_{0,i}$ | $-A_iK_{2,i}+4A_iJ_{1,i}-B_iC_{0,i}/12$ |
| $j=2$ | $-A_iK_{3,i}-(B_i/6+D_i)C_{1,i}-2B_iN_i/3$ | $-A_iK_{3,i}+4A_iJ_{2,i}-5B_iC_{1,i}/6+(2B_i+4D_i)N_i-2D_iC_{1,i}$ |

**这些是完整合法圆局部化后的贡献，不是任意非legal 单包的原 self 表。** 特别(10)已经对全 D 使用一次，不再把每包的非零平方矩逐个删除。

几个决定低阶系数的实际 IBP 为，写 $w=u_i'$、$r_i=u_i''$、$t_i=u_i'''$：

$$
\int wr_i^2t_i=-C_{0,i}/3,\qquad
\int xwr_i^2t_i=-(N_i+C_{1,i})/3,
$$

$$
\int w^2r_it_i=-N_i,\qquad
\int u_ir_i^2t_i=-N_i/3,
$$

$$
\int x^2r_i^3t_i=-C_{1,i}/2.
\tag{16}
$$

在(13)中，首行局部化为 $4A_iJ_{1,i}$；第二行合为
$-B_iC_{0,i}/3-D_iC_{0,i}/2$。
因此从 S 行的 $B_i/4+D_i/2$ 得到 R 行的 $-B_i/12$，而不是删除所有 quartic 余项。

同样，把(14)代入 $d=d_i r_i^2$，两项
$\int x^2r^2d'$ 和 $\int xvrd'$ 分别给
$-B_iC_{1,i}$、$-2B_i(N_i+C_{1,i})/3$；
于是准确得到表中的 $-B_iC_{1,i}/6-2B_iN_i/3-D_iC_{1,i}$。
R 行还需保原(10)—(11)，最后得到表中列明的所有 $N_i$ 项。

## 5. 当前 even 同纤维圆中的完整角归约

R284 的实际母包及每个有限频率纠正均 even。若第 i 个包以 $\xi_i$ 为中心，则

$$
J_{0,i}=N_i=0,\qquad C_{1,i}=\xi_iC_{0,i},\qquad
J_{2,i}=2\xi_iJ_{1,i}.
\tag{17}
$$

这只是关于该包自身中心的奇偶性，不是把物理 x 改成零中心。

在每个完整等平方 block 中 $b_i^2=B_0$、$R_i=a_i^2-B_0$。原格点矩及同 $\mathcal F$ 纤维确实保持 $C_{0,i}$；其来源在 R282/R284 中已从真实非legal Gaussian self 表给出，不需要增强 $\mathcal F$。所以原零次、一次格点矩仍给

$$
\sum_iR_iC_{0,i}=0,\qquad
\sum_iR_iC_{1,i}=0.
\tag{18}
$$

在实际全部副本上使用原正四次权。不同完整 block 的共同幅度可以不同；(18)逐 block 成立，再按其正四次权相加。

令 $\langle\sum\rangle$ 表示这一真实加权和，定义

$$
\mathsf K_m=\left\langle\sum_i a_i^2R_iK_{m,i}\right\rangle,\qquad
\mathsf J_m=\left\langle\sum_i a_i^2R_iJ_{m,i}\right\rangle,
$$

$$
\mathsf C_m=\left\langle\sum_iR_i^2C_{m,i}\right\rangle.
\tag{19}
$$

因此 R282/R284 的平方门为

$$
H_0=\mathsf K_0,\qquad H_1=\mathsf K_1,\qquad
H_2=\mathsf K_2+2\mathsf C_0.
\tag{20}
$$

最后十二完整副本的符号/四次权差分仍清除所有 odd 角项：本节原量在共同平移下最高三次，而该包装已消次数至多10。不能只因 even 母包就跳过这个完整包装。

由

$$
R_i^2-4(a_ib_i)^2=(7B_0/2)R_i
$$

和(18)，准确有

$$
\left\langle\sum_i c_i^2d_iC_{m,i}\right\rangle=0,\qquad
\left\langle\sum_i d_i^2C_{m,i}\right\rangle
=\sin^2\theta\,\mathsf C_m,\quad m=0,1.
\tag{21}
$$

把(17)—(21)代入第4节，六条 whole-circle 原式变为

$$
\boxed{
\begin{array}{c|cc}
 &M_j(P,S)&M_j(P,R)\\ \hline
0&-\sin^2\theta\,\mathsf K_1&-\sin^2\theta\,\mathsf K_1\\
1&\sin^2\theta(-\mathsf K_2+\mathsf C_0/2)
 &\sin^2\theta(-\mathsf K_2+4\mathsf J_1)\\
2&\sin^2\theta(-\mathsf K_3-\mathsf C_1)
 &\sin^2\theta(-\mathsf K_3+4\mathsf J_2-2\mathsf C_1).
\end{array}}
\tag{22}
$$

这里只使用了当前已构造圆实际拥有的 even 性、同 F 与完整复制；不把该表推广成任意合法 f,g 圆的恒等。

## 6. 已付平方门之后准确剩下什么

现在取 R284 已得 $H_0=H_1=H_2=0$。由(22)，整个 $E_{-3}E_{-2}$ 的零外矩为

$$
aM_0(P,R)+bM_0(P,S)
=-(a+b)\sin^2\theta\,H_1=0.
\tag{23}
$$

另外两矩是

$$
\boxed{
\begin{aligned}
aM_1(P,R)+bM_1(P,S)
&=\sin^2\theta\left\{
4a\mathsf J_1+(2a+5b/2)\mathsf C_0
\right\},\\
aM_2(P,R)+bM_2(P,S)
&=\sin^2\theta\left\{
-(a+b)\mathsf K_3+4a\mathsf J_2-(2a+b)\mathsf C_1
\right\}.
\end{aligned}}
\tag{24}
$$

所以在这个准确范围内，whole-circle 乘积门的必要充分条件为

$$
\boxed{
4a\mathsf J_1+(2a+5b/2)\mathsf C_0=0,\qquad
-(a+b)\mathsf K_3+4a\mathsf J_2-(2a+b)\mathsf C_1=0.
}
\tag{25}
$$

这些是(5)全部三外矩的 iff，不是只检查某个 pure 或 $\theta=\pi/2$ 后猜其他相位。

低阶基线有确定符号：

$$
\mathsf C_0>0.
\tag{26}
$$

因为每个实际 $R_i$ 非零、各 $u_i$ 非零且所有最终四次混合权严格正。又 $a,b<0$，第一门要求

$$
\mathsf J_1
=-\left(\frac12+\frac{5b}{8a}\right)\mathsf C_0
<-\mathsf C_0/2.
\tag{27}
$$

$\mathsf J_1$ 本身带真实 $a_i^2R_i$ 正负权，所以(27)不是一个立即不可能的正性断言。它说明不能用已付 $H_2=0$ 把这一完整余门删去，也不能把原 $P/S$ 单独行在 $H_2=0$ 后的 $5\mathsf C_0/2$ 忽略。

本稿没有断言任意 R284 根已经违反(25)，也没有证明两门在全部允许圆上独立。其正确范围是：此前实际构造没有以这两个完整方程作为目标；现在已把它们准确提取，仍需真实兼容的后续控制或新的恒等。

## 7. 为什么只增加同一 cutoff 的位置不能当作任意余量控制

这个结论可以直接从 R284 的真实 perturbation 读出，无需新的求积或计算。对同一个 even 基点和同一个 even $\chi$，

$$
u_N'''=u_0'''+z\chi\sin Ny+O(N^{-1}).
$$

$\mathsf K_0$ 的单包 principal 系数为
$2\int (u_0'')^2\chi^2$。而 $\mathsf J_1$ 的单包 principal 系数为

$$
\frac12\int y u_0'u_0''\chi^2,
\tag{28}
$$

因为共同位置乘 $\int u_0'u_0''\chi^2=0$。全部真实副本的正权只共同乘这两个数。因此固定这一个 cutoff 后，

$$
\frac{\mathsf J_{1,\mathrm{principal}}}
{\mathsf K_{0,\mathrm{principal}}}
=
\frac14\,
\frac{\int y u_0'u_0''\chi^2}
{\int (u_0'')^2\chi^2},
\tag{29}
$$

与微包位置无关。

所以再添许多位置，不会自动把第一余门的 principal 与 $H_0$ 分开；其非零低阶基线必须保留。这是本次固定提案族的准确列关系，**不是**对所有真实 profile 的内在 $C^2$ 恒等，更不授整个 nonlinear 系统不相容。

若后续从一开始采用两个不同 even cutoff，(29)可以不同。例如在 R281 允许选择的 $u_0''(0)\ne0$ 下，$y u_0'/u_0''=y^2+O(y^4)$ 在中心邻域非恒定；取集中在不同小 $|y|$ 区域的两个 even cutoff即得严格不同的加权平均。若坚持解析端芽类别，可按 R281 用 $\psi Q$ 的 $C^2$ 逼近保留该严格差异。这个观察提供一个真实的新母方向接口，尚不代替七个完整量的正平衡、有限频率根或其余 Gaussian 乘积的支付。

## 8. 已付范围与下一问题

本稿完整保了原右锚、全 D 三矩、第三槽左尾以及 $I_2$ 的一阶导项。它把当前 $E_{-3}E_{-2}$ 的一个自动矩和两个待付矩分开，并展示了一个会阻止“单纯加位置即可任意控余项”的真实 principal 依赖。

其余 Gaussian 对称乘积、零/一层 history、canonical period、全路径 gauge 与整个非线性闭嵌入目标继续未付。下一步若使用两种 cutoff，必须在同一原 $\mathcal F$ 纤维、真实复制和有限参数系统中联立(25)，不能改变已付72面积或平方门来换取本门。

