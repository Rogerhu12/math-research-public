# R290：完整负二 Gaussian 平方的三外矩与原有限观测固定的低阶余项

日期：2026-11-15。**完整纸面推导；未执行求积、符号程序、参数扫描、人工检查或研究计算。**

本稿从 [R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md) 的完整平方式计算 $E_{-2}^2$，保留不同外槽、真实右锚、全部 primitive 和 $I_2$ 的一阶导项。结果分为两层：

1. 对一般真实三矩圆，给出三个原外矩的准确公式；第二外矩中确实存在两个累计积分，不能删掉。
2. 在 R277—R287 已用的等平方背景、原 $\mathcal F$ 纤维与完整复制类中，证明所需低阶组合已经由**原来**的 Gaussian self 观测固定。一个额外 even 角项恰归为 R280 已付的三矩面积 $\mathcal A_{01}$，所以整个平方留下三个真实高阶标量门；本稿不预先宣布这三个门已经为零或独立。

有限观测归属的证明使用小参数非退化区间。必须在最初选择实际例外几何时，按 [R227 联合安装](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)及 [R241 共振范围](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)，同时选
$0<\kappa^2<1/100$。这是原允许的小非零参数中的一次初始选择，**不能**在任意已冻结 $\kappa$ 上事后替换几何。一般原式不需要这个额外小区间；其用途仅在§7的四个已存观测之线性代数。

其他来源：[R259 原算子与非紧 self](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R268](R268-full-sine-four-area-obstruction-for-centered-microcells.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R275](R275-first-moment-obstruction-for-the-small-width-two-slope-family.md)、[R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、[R286](R286-complete-mixed-minus-three-minus-two-Gaussian-moments.md)及 [R287](R287-two-even-oscillation-shapes-pay-the-complete-mixed-Gaussian-product.md)。

## 1. 原方向、完整槽与规范

仍取同一个正右积分 $Jv(x)=\int_x^{r_*}v(t)\,dt$。记

$$
P(u,v)=J(u''v''),\quad
R(u,v)=u'v'+xJ(u''v''),\quad
S(u,v)=J(xu''v'').
$$

共振参数 $\varepsilon=\kappa^2/4$ 的原负二方向为

$$
X=B_{-2}=aR+bS,\qquad h_{ab}=a+b,
$$

$$
a=-\frac{51\kappa^4+2\kappa^2+8}{64h_e^2},\qquad
b=-\frac{17\kappa^4+4\kappa^2}{32h_e^2}.
\tag{1}
$$

$h_{ab}$ 只是本稿的常系数简写，不是几何函数 $h$。

固定 $\theta$，置

$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u.
$$

三外矩为原 $I_0,I_1,I_2$，特别
$I_2(v,w)=\int(x^2v''w''+2v'w')$。定义

$$
q_j=-I_j(XD,XD)+2I_j\{u,X(u,XD)\},\quad j=0,1,2.
\tag{2}
$$

$X$ 已含真实 $a,b$，因此(2)无需再乘一个 Gaussian 标量。完整 history 系数是

$$
\mathscr Q_{-2,-2,\theta}
=\frac{1+j_s^2}{4h}q_0+\frac{j_s}{2}q_1+\frac h4q_2,
\qquad j_s=2\varepsilon\kappa\sigma^2.
\tag{3}
$$

这是平方规范，不混用两个不同 Gaussian 字母的 cross 因子2。

## 2. 原函数的导数及端条件

写

$$
v=u',\quad r=u'',\quad t=u''',\quad
F=(f'')^2,\quad d=F-r^2,\quad e=(f')^2-v^2,
$$

$$
A=Jd,\qquad \ell=e''-2d,\qquad
w=av-h_{ab}xr,\qquad C=XD.
$$

$d=D^{[2,2]}$，不是先点乘 $D$ 后作四次导数。原式直接给

$$
\begin{aligned}
C&=ae+axA+bJ(xd),\\
C'&=ae'+aA-h_{ab}xd,\\
C''&=a\ell-bd-h_{ab}xd'.
\end{aligned}
\tag{4}
$$

三矩使 $A$ 与 $C$ 在两侧 collar 真正为零。令 $B=X(u,C)$；同一右积分给

$$
\boxed{
B'=arC'+wC''+aJ(rC''),\qquad
B''=atC'+(wC'')'.
}
\tag{5}
$$

$B$ 仍可有左多项式尾。本稿的分部积分只用紧的 $u,d,e,A,C$；从未令 $B$ 的左尾为零。

## 3. 一般三矩圆的三个完整外矩

由(4)—(5)，对 $j=0,1$，

$$
\boxed{
\begin{aligned}
q_j={}&-\int x^j\{(C'')^2+2wtC''+ar^2C''\}\\
&-2j\int x^{j-1}rwC''
-aj\int x^{j-1}r^2C'.
\end{aligned}}
\tag{6}
$$

证明中的两步是
$2a\int x^jrtC'=-a\int x^jr^2C''-aj\int x^{j-1}r^2C'$
及 $2\int x^jr(wC'')'=-2\int(x^jt+jx^{j-1}r)wC''$。

第二外矩还含原一阶导项，完整结果为

$$
\boxed{
\begin{aligned}
q_2={}&-\int x^2\{(C'')^2+2wtC''+ar^2C''\}\\
&+4\int(v-xr)wC''
+2a\int r(2v-xr)C'\\
&-2\int(C')^2+4a\int urC''.
\end{aligned}}
\tag{7}
$$

最后一项来自 $\int vJ(rC'')=\int urC''$，只使用紧 $u$。把 $I_2$ 错写成 $\int x^2u''v''$ 会丢掉(7)整整第二、三行的部分贡献。

(6)—(7)保留全部原历史，对一般合法 $f,g$ 成立。

## 4. 真不交微包上的完整公式

令

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
$$

实紧 $u_i$ 的支持严格不交。记

$$
c_i=a_i\cos\theta+b_i\sin\theta,\quad
d_i=a_i^2-c_i^2,\quad
A_i=a_i^2d_i,\ B_i=c_i^2d_i,\ D_i=d_i^2,
$$

并在单包内写 $v_i=u_i',r_i=u_i'',t_i=u_i'''$、
$w_i=av_i-h_{ab}xr_i$。用

$$
C_{j,i}=\int x^j r_i^4,\quad
N_{j,i}=\int x^jv_ir_i^3,\quad
V_i=\int v_i^2r_i^2,\quad U_i=\int u_ir_i^3.
\tag{8}
$$

注意 $A_i=B_i+D_i$。由(4)，包内

$$
C''=d_i(2w_it_i-br_i^2).
\tag{9}
$$

把(9)代入(6)—(7)，只在已经成为 local 的部分按包相加，可得

$$
\boxed{
q_0=-4\sum_i A_i\int w_i^2t_i^2
+\frac{a^2+2ab+3b^2}{6}\sum_i B_iC_{0,i}
-\frac{ab}{3}\sum_i D_iC_{0,i},
}
\tag{10}
$$

$$
\boxed{
\begin{aligned}
q_1={}&-4\sum_i A_i\int xw_i^2t_i^2
+\left(\frac{2ab}{3}+b^2\right)\sum_i A_iC_{1,i}\\
&-\frac{4ab}{3}\sum_i A_iN_{0,i}
-a^2\int u''{}^2A .
\end{aligned}}
\tag{11}
$$

第二外矩为

$$
\boxed{
\begin{aligned}
q_2={}&-4\sum_i A_i\int x^2w_i^2t_i^2
+\sum_i B_iL_B(u_i)+\sum_i D_iL_D(u_i)\\
&+2ab\int A^2-2a^2\int xu''{}^2A,
\end{aligned}}
\tag{12}
$$

其中

$$
\boxed{
\begin{aligned}
L_B(u)={}&
\frac{-5a^2-2ab+5b^2}{6}C_2
+\left(4a^2-\frac{4b^2}{3}\right)N_1\\
&+(-6a^2+4ab)V-\frac{4a(a+b)}3U,
\\
L_D(u)={}&
\left(-2a^2-\frac{7ab}{3}\right)C_2
+\left(8a^2+\frac{16ab}{3}\right)N_1-12a^2V.
\end{aligned}}
\tag{13}
$$

### 4.1 可逐项核对的分部积分与原 primitive

例如

$$
\int w_i r_i^2t_i=\frac{-a+3b}{12}C_{0,i},
$$

$$
\int xw_i r_i^2t_i
=-\frac a3N_{0,i}+\frac{a+3b}{6}C_{1,i},
$$

$$
\int x^2w_i r_i^2t_i
=-\frac{2a}{3}N_{1,i}+\frac{5a+9b}{12}C_{2,i}.
\tag{14}
$$

这些三式给(10)、(11)和(13)中的相应系数。(12)的两个累计积分并非额外自造项。确切地，$C'=ae'-h_{ab}xd+aA$ 中所有 $A$ 项，在(7)中先合并为

$$
2ab\int A^2-2a^2\int xr^2A
+2a^2\sum_iB_iV_i-4a^2\sum_iD_iV_i.
\tag{15}
$$

这里用了完整的
$\int e'A=\int ed$、
$\int xdA=\frac12\int A^2$、
$\int vrA=\frac12\int v^2d$。
第二式要求**全体** $\int d=0$ 使 $A$ 紧；不能在每个 $d_iJ(r_i^2)$ 上单独如此操作。

(15)的后两项已经收入(13)。因此(12)没有丢单包自项、包间 history 或左端常数。一个直接对照是 $a=0,b=1$ 时

$$
q_2=-\sum_iA_i\int x^4((r_i^2)')^2
+\frac56\sum_iB_iC_{2,i}-\frac43\sum_iB_iN_{1,i},
$$

仍保留了不只 principal 的两个低阶项。

## 5. 原等平方背景及完整包装

以下进入 R277/R280 已用的类。先在一个基本布局内写

$$
b_i^2=B_0>0,\quad R_i=a_i^2-B_0\in\{-B_0/2,8B_0\},
\quad T_i=a_ib_i,
$$

$$
R_i^2-4T_i^2=\frac{7B_0}{2}R_i.
\tag{16}
$$

真实格点矩与 $\mathcal F$ 纤维保原三矩、所有 Gaussian self 的平移系数及其真实次序。各实际母包保持 even；共同偶母包不是指不同位置的整个函数关于全局原点偶。

原八/十二副本与最后完整 block 的正四次权都必须带入。以下公式可先在一个基本布局计算，再以这些真实权相加；不要求最终所有副本有共同一个背景 $B_0$。原十二复制清掉所需 odd 角项，其多项式平移次数仍不超过已付界。

在一个布局内，$\mathcal F$ 保 $C_{0,i}$ 为同一原母值；其准确来源已由 R282§5 从 $S_{B_{-1},B_{-3},0}$ 给出，未新增观测。格点矩与(16)给

$$
\sum_iB_iC_{j,i}=0,\quad
\sum_iD_iC_{j,i}=\sin^2\theta\sum_iR_i^2C_{j,i}
\quad(j=0,1).
\tag{17}
$$

even 母包还给 $N_{0,i}=0$。定义包含全部实际四次权的

$$
\begin{aligned}
\mathcal K_j&=\sum_i a_i^2R_i
 \int x^j((u_i''{}^2)')^2,\\
\mathcal J_j&=\sum_i a_i^2R_i
 \int x^ju_i'u_i''(u_i''')^2,\\
\mathcal W_j&=\sum_i a_i^2R_i
 \int x^j(u_i')^2(u_i''')^2,\qquad
\mathcal C_j=\sum_iR_i^2C_{j,i}.
\end{aligned}
\tag{18}
$$

这些是实际函数积分，不是可独立指定的坐标。

(11)中剩余的零阶 primitive 在该类也准确消去。令
$F=f''{}^2,G=g''{}^2,T=f''g''$，
$A_R=J(F-G),A_T=JT$。三矩使两者真紧。消 odd 后

$$
\int u''{}^2A=\sin^2\theta\int G A_R.
$$

每包原 $I_0=m$ 相同，因此

$$
\int G A_R=B_0m^2\sum_jR_j(j+\tfrac12)=0.
\tag{19}
$$

这里是等距格点的零/一次矩；母包内部 self 的系数 $1/2$ 已保留。不同完整 block 的 inner 原矩零使其 cross 为零。

于是

$$
\boxed{
q_0=\sin^2\theta\left[
-h_{ab}^2\mathcal K_2+8ah_{ab}\mathcal J_1
-4a^2\mathcal W_0-\frac{ab}{3}\mathcal C_0
\right],
}
\tag{20}
$$

$$
\boxed{
q_1=\sin^2\theta\left[
-h_{ab}^2\mathcal K_3+8ah_{ab}\mathcal J_2
-4a^2\mathcal W_1+
\left(\frac{2ab}{3}+b^2\right)\mathcal C_1
\right].
}
\tag{21}
$$

## 6. 第二矩的额外 even 项：先保全，再判来源

在一个完整基本布局中置

$$
\mathcal R=\int A_R^2,\qquad
\mathcal T=\int A_T^2,\qquad
\mathcal L=\int xG A_R.
$$

这些是真实累计积分。直接展开 $A=\sin^2\theta A_R-2\cos\theta\sin\theta A_T$，在完整 odd 消去后，

$$
\int A^2=\sin^2\theta\,\mathcal R+
\cos^2\theta\sin^2\theta(4\mathcal T-\mathcal R),
$$

$$
\int xu''{}^2A=\sin^2\theta\,\mathcal L+
\cos^2\theta\sin^2\theta(\mathcal R/2-2\mathcal T).
\tag{22}
$$

第二式用了 $\int x(F-G)A_R=\mathcal R/2$ 和
$\int xT A_T=\mathcal T/2$，边项由各完整 primitive 的紧性消掉。

所以(12)准确为

$$
q_2=\sin^2\theta\,\mathcal A_2+
\cos^2\theta\sin^2\theta\,\Xi,
\tag{23}
$$

其中

$$
\begin{aligned}
\mathcal A_2={}&
-h_{ab}^2\mathcal K_4+8ah_{ab}\mathcal J_3-4a^2\mathcal W_2\\
&+B_0\sum_iR_iL_B(u_i)+\sum_iR_i^2L_D(u_i)
+2ab\mathcal R-2a^2\mathcal L,
\end{aligned}
\tag{24}
$$

$$
\boxed{
\Xi=\frac{7B_0}{2}\sum_iR_i(L_B-L_D)(u_i)
-a(a+2b)(\mathcal R-4\mathcal T).
}
\tag{25}
$$

目前不能把(25)当零，也不能只因两项都是 $C^2$ 连续便声称它们被原 $\mathcal F$ 固定。下一节给出所需的准确原观测归属。

## 7. 四个已存 Gaussian self 给出的原有限维子空间

对任意实紧 $u$，记

$$
\Delta(u)=\iint|x-y|u''(x)^2u''(y)^2\,dx\,dy.
$$

考察五元向量 $(C_2,N_1,V,U,\Delta)$。原 $\mathcal F$ 已含下列四行；已知原二次矩乘积作为固定常数剥去，不添加新观测：

$$
\begin{aligned}
A_*={}&-C_2+\frac83N_1-V-\frac43U+\frac{\Delta}{4},\\
B_*={}&-\frac{5(d_-+7e_-)}6C_2+
 \frac{4(d_-+11e_-)}3N_1-8e_-V-\frac{8e_-}{3}U,\\
D_*={}&\frac{5(d_--5e_-)}4C_2-
 4(d_--4e_-)N_1+(d_--3e_-)(3V+U),\\
C_*={}&\left\{\frac{d_-(a+b)}6+\frac{e_-(11a+5b)}{12}\right\}C_2\\
&-\frac{d_-(a+b)+e_-(8a+2b)}3N_1
+\frac{a(4e_--d_-)}2V+\frac{d_-(a+b)}3U
-\frac{k_*}{4}\Delta,
\end{aligned}
\tag{26}
$$

其中

$$
d_-=\frac{6\kappa^3}{h_e},\quad
e_-=-\frac{\kappa(15\kappa^2+1)}{4h_e},\quad
k_*=\frac{d_-b}{2}-e_-a.
$$

四行的原来源分别是：

- **$A_*$：** R268(5)的 nonlegal $S_{P,Y,0}$。准确
  $S_{P,Y,0}=A_*-\mu_0\mu_1/2$；
  原 Gaussian 行 $S_{B_1,B_{-3},0}=-\zeta cS_{P,Y,0}$，且 $\zeta c\ne0$。
- **$B_*$：** R267(6)—(7)的
  $d_-S_{P,p_0,2}+e_-S_{P,s_1,2}$；
  原 Gaussian 行只另乘非零 $-c$。
- **$D_*$：** R270(4)—(5)的
  $d_-S_{p_0,Y,0}+e_-S_{s_1,Y,0}$ 在共同平移参数中的**二次系数**。原 Gaussian 行另乘非零 $-\zeta$。这里使用完整 self 的平移系数，未只取某个 leading 母包极限。
- **$C_*$：** R275(6)四个第一外矩的原组合
  $d_-aS_{p_0,R,1}+d_-bS_{p_0,S,1}
   +e_-aS_{s_1,R,1}+e_-bS_{s_1,S,1}$。
  用真实 $H_{\rm self}=\mu_0\mu_1-\Delta/2$ 后，该组合为
  $C_*-k_*\mu_0\mu_1/2$。

因此(26)确来自四个**实际 Gaussian pair**的原 self 数据及其平移系数。没有把六个基本 $\Phi$ 的任意 self 全部偷偷加进 $\mathcal F$。

### 7.1 原四行的准确核

令

$$
\Lambda_*=3ad_--bd_-+2ae_-.
$$

若 $d_-^2-e_-^2\ne0$ 且 $\Lambda_*\ne0$，(26)四行的共同核恰为

$$
\boxed{\operatorname{span}(8,5,2,4,8).}
\tag{27}
$$

手算如下。先置 $W=3V+U$。$B_*,D_*$ 对 $(C_2,W)$ 的系数行列式是
$-5(d_-^2-e_-^2)/6$，故核内先有
$C_2=8N_1/5,\ W=2N_1$。
$A_*=0$ 再给 $\Delta=32N_1/5-12V$。
最后 $C_*=0$ 准确变成
$\Lambda_*(N_1/5-V/2)=0$，得到(27)。

原参数代入给

$$
d_-^2-e_-^2=
\frac{\kappa^2(9\kappa^2-1)(39\kappa^2+1)}{16h_e^2},
$$

$$
\Lambda_*=
\frac{\kappa(8-166t+105t^2-663t^3)}{128h_e^3},
\qquad t=\kappa^2.
\tag{28}
$$

从最初选择 $0<t<1/100$ 时，两者非零。没有把一个未必可安装的特殊 $\kappa$ 当作构造参数，也没有改变任何已固定的几何；若处理该区间之外的既有 $\kappa$，必须直接核(28)，否则只保(25)而不使用本节结论。

(13)给

$$
L_B\cdot(8,5,2,4,8)=-4a^2,\qquad
L_D\cdot(8,5,2,4,8)=8ab.
$$

于是下列两个完整量准确属于(26)的行空间：

$$
\boxed{
I_B=L_B+\frac{a^2}{2}\Delta,\qquad
I_D=L_D-ab\Delta.
}
\tag{29}
$$

这是原 $\mathcal F$ 的可验证线性组合。它**不**声称 $\Delta,L_B,L_D$ 各自都固定；沿(27)它们单独可以改变。

## 8. 有序 primitive 的准确合并与额外角项消去

定义实际单包三矩中的 $\mu_{0,i},\mu_{1,i}$，以及

$$
O_{RR}=\sum_{i<j}R_iR_j
(\mu_{0,i}\mu_{1,j}-\mu_{1,i}\mu_{0,j}),
$$

$$
\mathcal A_{01}=\sum_{i<j}(R_iR_j-4T_iT_j)
(\mu_{0,i}\mu_{1,j}-\mu_{1,i}\mu_{0,j}).
\tag{30}
$$

这是 R280 的反对称三矩面积规范，未除以2。

零总矩的真实 primitive 恒等式给

$$
\mathcal R=-O_{RR}-\frac12\sum_iR_i^2\Delta_i,
$$

$$
\boxed{
\mathcal R-4\mathcal T
=-\mathcal A_{01}-\frac{7B_0}{4}\sum_iR_i\Delta_i.
}
\tag{31}
$$

例如第一式来自
$\int(J\rho)^2=-\frac12\iint|x-y|\rho(x)\rho(y)$，
先用全体 $\int\rho=0$，再按真实包次序展开；包内的 $\Delta_i$ 一直保留。

将(31)代入(25)，得到

$$
\Xi=a(a+2b)\mathcal A_{01}
+\frac{7B_0}{2}\sum_iR_i(I_B-I_D)(u_i).
\tag{32}
$$

$I_B-I_D$ 已由(29)固定，且对母包共同平移是次数至多2的准确多项式。原格点十矩因此给
$\sum_iR_i(I_B-I_D)(u_i)=0$。
所有实际完整副本与最后 block 按原正四次权相加，且 R280 已支付相同规范的总 $\mathcal A_{01}=0$。故

$$
\boxed{\Xi_{\rm total}=0.}
\tag{33}
$$

这不是逐基本布局先断言 $\mathcal A_{01}=0$；它可能在单个正/负布局非零，是最终完整组合才支付的总量。

第二矩的整条低阶基线也被同一原数据固定。准确有

$$
\mathcal L
=B_0\sum_iR_i\left(\frac{\mu_{0,i}\mu_{1,i}}2-\frac{\Delta_i}{4}\right)
+B_0\sum_{i<j}R_j\mu_{1,i}\mu_{0,j}.
\tag{34}
$$

把(29)、(31)、(34)代入(24)，其低阶部分为

$$
\boxed{
\begin{aligned}
\mathcal B_2={}&
B_0\sum_iR_iI_B(u_i)+\sum_iR_i^2I_D(u_i)-2abO_{RR}\\
&-a^2B_0\sum_iR_i\mu_{0,i}\mu_{1,i}
-2a^2B_0\sum_{i<j}R_j\mu_{1,i}\mu_{0,j}.
\end{aligned}}
\tag{35}
$$

原三矩、真实左右次序和(29)固定每项。特别，虽然 $\int A^2$ 与 $\int xr^2A$ 单独含非局部数据，**它们在原平方中的实际组合**没有遗漏一个新、未存的低阶量。

## 9. 在已付七个标量以后，真正还欠什么

R287 已准确支付 $H_0,H_1,H_2,L_c,M_c$ 以及 R286 的两个 mixed 条件。相关身份是

$$
\mathcal K_2=-2\mathcal C_0,\qquad
4a\mathcal J_1=-(2a+\tfrac52b)\mathcal C_0,
$$

$$
-h_{ab}\mathcal K_3+4a\mathcal J_2-(2a+b)\mathcal C_1=0.
\tag{36}
$$

因此(20)—(21)还可写成

$$
\boxed{
q_0=-\sin^2\theta
\left[4a^2\mathcal W_0+
(2a^2+\tfrac{16}3ab+3b^2)\mathcal C_0\right],
}
\tag{37}
$$

$$
\boxed{
q_1=\sin^2\theta
\left[4ah_{ab}\mathcal J_2-4a^2\mathcal W_1+
(2a^2+\tfrac{11}3ab+2b^2)\mathcal C_1\right].
}
\tag{38}
$$

结合(23)、(33)、(35)，

$$
\boxed{
q_2=\sin^2\theta
\left[-h_{ab}^2\mathcal K_4+
8ah_{ab}\mathcal J_3-4a^2\mathcal W_2+\mathcal B_2\right].
}
\tag{39}
$$

(37)—(39)给这个完整平方的三个准确剩余标量。它们的低阶基线由原 $\mathcal F$、原有序矩与已付面积固定；三阶导积分仍须在同一个实际圆上支付。

$\mathcal W_j,\mathcal J_j$ 带真实有符号 $a_i^2R_i$，不能因其单包 integrand 为平方就赋给总量错误的固定号。本稿没有证明这三个式子自动为零，也没有仅从条目数声称三条独立。它们可交给 R285/R289 的 principal 与真实有限频率构造继续分析，但必须连同(35)、(36)的完整基线同时处理。

所有 odd 消去、原三矩、完整第三与72面积均沿原包装和原纤维使用。没有新增计算，没有重算旧科学，也没有把已证明的有限必要层等同于完整第四 ruling、canonical period、平台/flux或最终非线性几何的解。
