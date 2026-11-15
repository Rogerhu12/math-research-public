# R701 — 原两 charge 清极的充要矩条件、尖锐无穷远门与同 R 两块 cap

日期：2026-11-15。**状态：已证明。**

本篇继续 R697 的同一个整因子、同一个 $P_2=P^{\rm fact}+pR$ 和完整旧矩阵。得到一个有明确范围的实际改善：最高系数的两个无穷远矩满足显示等式，并且原立方来源具有四个无穷远赋值单位的余量时，保全部 $3C$ 的 forcing 返回可以只增加两个 charge；原第一修正的未付部分准确缩为最后两个 charge。两组十三行给出本文式 (25) 的实际联立条件，不能独立选择其原像。

这两个条件没有由原中央零推出。尤其，乘子有两 charge 成本不等于整个 forcing 已有这个成本；本文证明额外的无穷远门一般是尖锐的。尚未证明所指定的第二余类为零或非零，也没有给新的乘子来源附加中央零。

## 1. 同一原格和最高系数

沿 R697，$b=\deg_YF$，这里的 $b$ 是因子次数，不是固定椭圆曲线参数。取
$$
p=6s-1>101,\quad f_D<p,\quad
F=\sum_{i=0}^bf_i(t)Y^i,\quad 1\le b<p,\quad f_0f_b\ne0,
$$
$$
\mathcal E=Y\partial_Y,\quad \delta=t\partial_t,\quad
d=1+8t,\quad h_7=7+4t+16t^2,
$$
$$
A=6(1-t),\quad B=-(1+2t),\quad
\mathcal P=A\delta^2+B\delta,\quad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2}.
\tag{1}
$$
原 forcing $K_F$、实际立方来源及最高缺口仍是
$$
\begin{aligned}
K_F={}&e^3\mathcal R+A e^2\delta^2F
-2A e a_0\mathcal E\delta F+A a_0^2\mathcal E^2F+B e^2a_0,\\
&e=\mathcal EF,\qquad a_0=\delta F,\\
P^{\rm fact}={}&d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
D_0=3b+\deg_YQ\le D,\\
h_+={}&b-\max\{i<b:f_i\ne0\}.
\end{aligned}
\tag{2}
$$
一般首核仍不能无证写成 (2)。

保 R697 的实际固定角条件
$$
f:=f_b=c\,t^{a_0^*}(t-1)^{a_1}d^{a_d}
(t-\alpha_+)^{a_+}(t-\alpha_-)^{a_-},
\quad c\in\mathcal O^\times,\quad a_\bullet\in\mathbf Z_{\ge0},
\tag{3}
$$
其中
$$
\alpha_\pm=\frac{-1\pm3\sqrt{-3}}8.
$$
(3) 是同一整提升的等式。必要时在原有限非分歧扩张内拆开 $h_7$；不从模 $p$ 的角分解自动推它到下一位。

置
$$
a=\deg f,\qquad \sigma_j=\sum_\alpha a_\alpha\alpha^j\quad(j\ge1),
$$
这里 $\alpha$ 遍历 $0,1,-1/8,\alpha_+,\alpha_-$。R697 的唯一全三层最高项修正为
$$
c_F=b^2\{b\mathcal R+\mathcal P\log f\},\qquad
K_F^{[3]}=K_F-c_FF^3.
\tag{4}
$$
$\mathcal P\log f$ 只表示有理函数
$A(\delta^2f/f-(\delta f)^2/f^2)+B\delta f/f$，不引入正特征完整 log。
准确有
$$
\deg_YK_F^{[3]}\le3b-h_+,\qquad
K_F^{[3]}\equiv K_F\pmod{F^3}.
\tag{5}
$$
因此值和两个原 normal 导数都保持；不能只保曲线值。

## 2. 两个无穷远矩准确控制乘子成本

先作一个有理恒等式：
$$
\boxed{\mathcal R=\mathcal P\log d+\frac{34}{3}t.}
\tag{6}
$$
它直接由
$$
\mathcal P\log d=\frac{8t(5-16t-16t^2)}{d^2}
$$
核定。因为
$$
\delta\log f=a+\frac{\sigma_1}{t}+\frac{\sigma_2}{t^2}+\cdots,
$$
可逐项得到
$$
\boxed{
\frac{c_F}{b^2}
=\left(\frac{28b}{3}-2a\right)t+
\left(-\frac{3b}{2}+4\sigma_1-a\right)
+\frac{33b/32+10\sigma_2-7\sigma_1}{t}
+O(t^{-2}).
}
\tag{7}
$$
所以
$$
\boxed{
c_F=O(t^{-1})\ \text{于 }\infty
\quad\Longleftrightarrow\quad
a=\frac{14b}{3},\qquad \sigma_1=\frac{37b}{24}.
}
\tag{8}
$$
这些是同一有理函数的准确等式；只在模 $p$ 中满足时，不能直接把以下整结论应用到模 $p^3$。

定义两个固定清极量
$$
\mathfrak m'_3=Y^3t(t-1)^2h_7^3d,\qquad
\mathfrak m_2=Y^2t(t-1)^2h_7^3d,
$$
以及
$$
\mu'_3=\mathfrak m'_3c_F,\qquad \mu_2=\mathfrak m_2c_F.
\tag{9}
$$
它们只允许原 $d$ 分母，不要求无分母的多项式：在 $d=0$ 至多余一个 $d^{-1}$，由原 $q_n$ 的分母帽支付。

**定理 1（实际乘子门）。**

1. 无须 (8)，$\mu'_3\mathcal W_N\subset\mathcal W_{N+3}$ 对每个 $N$ 整成立。
2. 对显示的 $\mathfrak m_2$，有准确充要条件
   $$
   \boxed{
   \mu_2\mathcal W_N\subset\mathcal W_{N+2}
   \text{ 对全部 }N\ge0
   \quad\Longleftrightarrow\quad (8).
   }
   \tag{10}
   $$

**证明。** R491/R514 的实际原格判据为
$$
\deg_Y P\le N,\quad
(v_0,v_{h_+},v_{h_-},v_1,v_d,v_\infty)
\ge(-2,-2,-2,-1,0,-8),
\tag{11}
$$
有限角权依次为 $(4,-1),(4,-1),(4,-1),(3,-1),(2,1)$，无穷远权为 $(-2,9)$。这里 $h_\pm$ 仅标记 $h_7$ 的两根，与 (2) 的最高缺口不同。

由 (3)，$c_F$ 的五类下界是
$$
(0,-8,-3,-4,-2).
$$
$\mathfrak m'_3$ 的对应值是 $(1,9,3,5,7)$，故其乘子总值至少
$(1,1,0,1,5)$。这证明第一项；R697 原 $\mathfrak m_3$ 在 $d$ 角多出的一个 $d$ 确实不是此处必要的。

在 (8) 下，$c_F$ 的无穷远值提高为至少 $2$。
$\mathfrak m_2$ 的值为
$$
(2,10,4,4,-2),
$$
所以
$$
\boxed{v(\mu_2)\ge(2,2,1,0,0).}
\tag{12}
$$
Gauss 乘法和 (11) 给全部 $N$ 的正向包含。反向，若 (8) 不成立，则 $v_\infty(c_F)<2$，故 $v_\infty(\mu_2)<0$。原真列 $t^4\in\mathcal W_0$ 的无穷远值恰为 $-8$，于是 $\mu_2t^4\notin\mathcal W_2$，已经在实际最小来源中失败。证毕。

(11) 是双向的原 $q_n\mathcal O[t]_{\le e_{n+1}}$ 条件，不是较大矩形：其取整分别给 $A_n,B_n,-C_n$ 和 $f_n$。因而 (10) 保全部原列帽及相应十九个中间角；没有以某个环境空间的满射代替来源包含。

### 一个更深的无穷远取消也不能无限继续

在特征零的 (8) 下，$\sigma_1$ 的 $\sqrt{-3}$ 部分迫 $a_+=a_-=:A_h$。若还消去 (7) 的 $t^{-1}$ 项，则
$$
A_h=\frac{181b+45a_d}{180},\quad
a_1=\frac{1291b}{720}+\frac{3a_d}{16},\quad
a_0^*=\frac{69b}{80}-\frac{27a_d}{16},
$$
而下一项准确为
$$
\boxed{
[t^{-2}]\,c_F=\frac{b^2(3327b+675a_d)}{160}\ne0.
}
\tag{13}
$$
验证用
$\alpha_++\alpha_-=-1/4$、
$\alpha_+^2+\alpha_-^2=-13/16$、
$\alpha_+^3+\alpha_-^3=5/16$；
一般 $t^{-j}$ 项是
$b^2\{-(27j+6)(-1/8)^j/4+(6j+4)\sigma_{j+1}-(6j+1)\sigma_j\}$。
(13) 的非零由 $b>0,a_d\ge0$ 给出；模 $p$ 时还保明确条件
$p\nmid b(3327b+675a_d)$。在原 $f_D<p$ 且 $D=O(\sqrt p)$ 的大素数范围，分子是 $O(D)$，这个附加排除自动最终成立。

这只限制此固定角有理函数的衰减，不把它当原中央非零。

## 3. 完整 forcing 仍要支付四个无穷远单位

(10) **本身不证明** $\mathfrak m_2K_F^{[3]}$ 已有两 charge 成本。原 $K_F$ 的五类损失仍是
$$
v(K_F)-3v(F)\ge(0,-8,-3,-4,-2).
\tag{14}
$$
即使 $c_F$ 满足 (8)，$K_F^{[3]}$ 的一般无穷远损失也仍至多为二。

**定理 2（原整返回）。** 除 (8) 外，若同一个来源满足
$$
\boxed{v_\infty(P^{\rm fact})\ge-4,}
\tag{15}
$$
则
$$
\boxed{
\begin{aligned}
B_2^{\rm old}&=d^{-C_D}t^rQ\,\mathfrak m_2K_F
 \in\mathcal W_{D_0+2},\\
B_2^{[3]}&=d^{-C_D}t^rQ\,\mathfrak m_2K_F^{[3]}
 \in\mathcal W_{D_0+2-h_+},\\
B_2^{[3]}&=B_2^{\rm old}-\mu_2P^{\rm fact}.
\end{aligned}}
\tag{16}
$$
因此 $D_0+2-h_+\le D$ 时是同一预算返回；特别 $h_+\ge2$ 已足够。

**证明。** $\mathfrak m_2$ 与 (14) 相加，有限角总增益为
$(2,2,1,0)$，无穷远增益下界为 $-4$。
对 $c_FF^3$，(8) 还给更强的无穷远界，故对其差也保这个下界。
乘回同一 $d^{-C_D}t^rQ$ 后，有限角均不降低 $P^{\rm fact}$ 的原值，(15) 给无穷远至少 $-8$。唯一所余 $d^{-1}$ 亦已由 $v_d\ge0$ 支付。最后用 (5) 的实际 $Y$ 次数及 (11) 的双向判据，得到 (16)。证毕。

没有抽掉原 $Q$、$d^{-C_D}$ 或 $t^r$；也未要求后续 $R,T$ 具有额外因子。后续全部 $R,T$ 使用的是已完整成立的乘子包含 (10)。

### 无穷远门为何一般是尖锐的

在剩余域及其代数闭包上，令 $v=v_\infty(F)$，以
$t=\zeta^{-2},\ Y=\zeta^{9}Z$ 写原最低形式
$$
F=\zeta^vF_\infty(Z)+\text{更高 }\zeta\text{ 阶}.
$$
记 $e_\infty=Z\partial_ZF_\infty$、$f_{2,\infty}=(Z\partial_Z)^2F_\infty$。
保持 $Y$ 的原 $\delta$ 在该坐标中是
$-\zeta\partial_\zeta/2+9Z\partial_Z/2$。代入 (2) 得
$$
\boxed{
\operatorname{in}_{3v-2}(K_F)=
\frac13e_\infty^3+
vF_\infty e_\infty^2-
\frac32v^2F_\infty
(F_\infty f_{2,\infty}-e_\infty^2).
}
\tag{17}
$$
已抽掉共同的 $\zeta^{3v-2}$。

若 $F_\infty$ 不是单项式，它在代数闭包有一个非零根，重数
$1\le m\le b<p$。在此根处，(17) 的第一项阶为 $3m-3$，后两项至少为 $3m-2$；第一首系数为单位 $m^3Z_0^3/3$ 乘单位。因此 (17) 非零。
若 $F_\infty=cZ^i$，(17) 准确为
$c^3i^2(i/3+v)Z^{3i}$。
所以除单项式 $i=0$ 或 $i+3v=0$ 的显示共振外，准确有
$$
v_\infty(K_F)=3v_\infty(F)-2.
$$
在 (8) 下，$c_FF^3$ 的值至少 $3v+2$，不能取消这一首项。于是
$$
\boxed{
v_\infty(B_2^{[3]})=v_\infty(P^{\rm fact})-4
}
\tag{18}
$$
在上述非共振范围成立。若 $v_\infty(P^{\rm fact})<-4$，它确实违反原来源帽。这里的失败发生在原格，不是仅仅某个粗估计不够。

## 4. 条件有实际来源，但不冒充原首核

为说明 (8)、(15) 的来源范围并非空集，取任意 $b=24m$、$D=3b$、$r=1$ 或 $2$，以及
$$
\begin{aligned}
f_b&=t^{7b/8}(t-1)^{43b/24}h_7^b,\\
F&=d^{b/2}
+\frac{(t-1)h_7d^{b/2}}7Y+f_bY^b,\\
P^{\rm fact}&=d^{-3b/2}t^rF^3.
\end{aligned}
\tag{19}
$$
同一整多项式满足
$F(0,1)=0,\ \mathcal EF(0,1)=-1$。
它的五类 Gauss 值准确为
$$
(-1,0,0,b,-b),
$$
故 $P^{\rm fact}$ 的对应值为
$(4r-3,0,0,0,-2r)$，准确属于原 $\mathcal W_D$，且满足 (15)。
最高系数的次数为 $14b/3$，第一矩为 $37b/24$，也满足 (8)；
$h_+=b-1$。

(19) 只是一个全参数的真实来源族。没有声称它与原 $g$ 有所需高接触、属于 $\ker\bar M$ 或命中原算术候选。下面凡使用首核或第二核均另作明确假设。

## 5. 同一个 P2：未付部分缩为最后两个 charge

以下固定 (3)、(8)、(15) 以及 $D_0+2-h_+\le D$。令
$$
M^{(N)}:\mathcal W_N\to Y_{\rm old}
$$
扩大来源而保持同一个旧目标、$P_{134}/U_0$、charge40、$g,t,a_p$ 和全部 carry；$M=M^{(D)}$。实际目标乘子记 $\mu_{\rm phys}$。
由真正整乘法，完整有
$$
M^{(N+2)}(\mu_2H)=\mu_{\rm phys}M^{(N)}H.
\tag{20}
$$
若 $\bar P^{\rm fact}\in K_1(M)$，(16) 于是给
$\overline{M^{(D+2)}B_2^{\rm old}}\in\operatorname{im}\bar M$。

现在固定同一个
$$
P_2=P^{\rm fact}+pR,\qquad MP_2\in p^2Y_{\rm old}.
$$
写 $\mu_2=Y^2\mu_{20}(t)$ 及 $R=\sum_{n=0}^DY^nR_n(t)$，定义
$$
\boxed{
C_R^{(2)}=\Pi_{>D}(\mu_2R)
=\sum_{n=\max(0,D-1)}^DY^{n+2}\mu_{20}(t)R_n(t).
}
\tag{21}
$$
这是原 $R$ 的最后两个 charge，含其全部原角系数，不是两条自由目标列。其来源秩上界是
$\sum_{n=\max(0,D-1)}^D(e_{n+1}+1)$；没有从这个上界宣称物理秩。

置
$$
Z_2^0=B_2^{[3]}-p\Pi_{\le D}(\mu_2R),\qquad
F_2^{\rm old}=M^{(D+2)}B_2^{\rm old}.
$$
整准确有
$$
MZ_2^0=F_2^{\rm old}-\mu_{\rm phys}MP_2
+pM^{(D+2)}C_R^{(2)}.
\tag{22}
$$
因而固定首来源类 $\overline{B_2^{[3]}}$ 时，第一提升可解当且仅当
$[\overline{M^{(D+2)}C_R^{(2)}}]=0$ 于 $C_1(M)$。
若允许更换首类，则需按 R697 保首次 Bockstein 像，而非删去它。

通过这一门后，固定一个同预算 $S$，使
$$
M^{(D+2)}C_R^{(2)}+MS\in pY_{\rm old}.
$$
完整第二代表是
$$
\boxed{
\Omega=
\overline{\frac{M^{(D+2)}C_R^{(2)}+MS}{p}
-\mu_{\rm phys}\frac{MP_2}{p^2}}.
}
\tag{23}
$$
固定 $Z_2=Z_2^0+pS$ 时，下一位可解当且仅当 (23) 在 $C_1(M)$ 为零；
固定首类而允许改变第一修正时，准确在 $C_2(M)$ 读取。
$R$ 或 $S$ 的自由度、以及第三提升的同一个 $T$，均按 R697 的完整整等式运输。特别第三位仍有
$pM^{(D+2)}C_R^{(2)}+p^2M^{(D+2)}C_T^{(2)}$，
不能分别删掉。

## 6. 原低 r 角帽把乘子锁为恰一次零

再假设 (2) 中的 $t^r$ 已抽尽，$F,Q$ 在 $t$ 上 primitive。
原 $v_0(P^{\rm fact})\ge-2$，而 $v_0(Q)\le0$，且
$v_0(F)\le4a_0^*-b$。因此
$$
\boxed{12a_0^*-3b+4r\ge-2.}
\tag{24}
$$
若 $b>(4r+2)/3$，则 $a_0^*>0$。原来源总次数帽给
$a_0^*\le\deg f\le(f_D+C_D)/3<p$，所以
$c_F(0)=-b^2a_0^*$ 是单位。

令 $\tau_1=[w]t(w)\in\mathcal O^\times$，保原实际尺度。此时
$\mu_{\rm phys}=w\,U$，其中 $U$ 是完整旧 $\Gamma$ 的整单位，
$U(0)=-343b^2a_0^*\tau_1$。
对 $r\le13$ 的高 $b$ 候选，(24) 因而排除了把 $\mu$ 设成任意深零来消掉第二余项的做法。

在 $\Gamma_T$、$T=2s+\ell+13<3s$ 的标准基
$e_j=w^j/p^{\lfloor j/s\rfloor}$ 上，乘 $\mu_{\rm phys}$ 的 Smith 因子准确为
$T-3$ 个单位、两个 $p$、一个零。
模 $p$ 的核为
$\langle e_{s-1},e_{2s-1},e_{T-1}\rangle$。
证明只用它等于乘 $w$ 再乘整单位；乘 $w$ 在两次过界处给 $p$，末列给零。单位乘法保持这些消灭理想。这里不由目标算子的 Smith 形推出原 $M$ 余核上的单射。

## 7. 两组十三行：同一 cap 与同一 d2 的准确联立

本节在第六节的一次零范围工作。仅用原整目标单位作共轭，
写
$$
\widehat M=(c_*U_0)^{-1}M=w^{13}J,\qquad n_0=s-13.
$$
没有换来源、Gaussian 或 $t/w/\epsilon$ 规范。
对任意原来源 $X$，记其完整 $J$ 三块为 $J_i(X)$，定义真实尾
$$
\mathfrak b_i(X)=\sum_{j=0}^{12}
[w^{n_0+j}]J_i(X)\,w^j,\qquad i=0,1.
$$
$\widehat MP_2\in p^2$ 使
$B_i=\overline{\mathfrak b_i(P_2)/p}$ 整定义。
置同一个
$N=C_R^{(2)}+S$；
$\widehat M^{(D+2)}N\in p$ 已由第五节支付。以下对 $N$ 的 $J$ 和评价始终用这个扩大来源、目标不变的原映射。

模 $p$，实际乘子是
$$
\bar\mu_{\rm phys}=w\,u(w)e_2(2\bar a_p\epsilon),
\qquad u(0)\ne0.
$$
其中 $u$ 是真实 $g^2\mu_{20}(t)/w$ 的低轴；高 ordinary 整系数经
$w^s=p\epsilon$ 在此约化中消失，并未把高位目标改成自由量。

令 $\widehat\Omega=(c_*U_0)^{-1}\Omega$。它的两组十三行准确为
$$
\boxed{
\begin{aligned}
\operatorname{carry}_0(\widehat\Omega)
&=\overline{\mathfrak b_0(N)}
-\pi_{13}\bigl(wu\,B_0\bigr),\\
\operatorname{carry}_1(\widehat\Omega)
&=\overline{\mathfrak b_1(N)}
-\pi_{13}\bigl(wu\,(B_1+2\bar a_pB_0)\bigr).
\end{aligned}}
\tag{25}
$$
两行全来自同一个 $R,S$；$2\bar a_pB_0$ 是 charge 二乘子的实际交叉项。

**证明。** 乘 $w^{13}$ 把 $J_0$ 的末十三行变成第二块前十三行乘 $p$，把 $J_1$ 的末十三行变成第三块前十三行乘 $p$。所以
$\widehat MN/p$ 的这两带是
$\overline{\mathfrak b_0(N)},\overline{\mathfrak b_1(N)}$。
$\widehat MP_2/p^2$ 的同两带为 $B_0,B_1$；其第一块前十三行仍为零。
再乘上 $wu e_2(2\bar a_p\epsilon)$，直接给 (25)。
其余低行和高尾仍在完整 (23) 中。特别，$B_i$ 的最后系数乘 $w$ 后移到相邻普通行，并没有从整个目标消失。证毕。

因为 $\operatorname{im}\bar{\widehat M}$ 的这两组 carry 恒零，(25) 全部为零是固定 $\Omega$ 落首像的必要条件。在 $C_2$ 中判定时仍要保来源首次提升能改变的实际 carry 像，不能无证令其自由。即使两组都通过，还必须检验 (23) 在其余原目标行的像成员性；本篇没有将必要条件冒充充分非零判断。

## 8. 实际改善与仍未支付的输入

本篇的两 charge 返回具有三道明确门：同一固定角最高系数 (3)、两个准确无穷远矩 (8)、以及同一原来源的四单位缓冲 (15)。它把 R697 的最后三个 charge 降为最后两个，而且把所省的成本和仍存的两组十三行全部落在同一个 $P_2,R,S$ 上。

(17)–(18) 说明不能只改乘子再省略完整 forcing 的无穷远主项；(24) 则说明原低 $r$ 高 $b$ 区域的乘子通常就是一次零，不能从它的乘积反推原 $d_2$ 消失。

原实际候选是否满足 (8)、(15)，以及 (21)、(23)、(25) 在全部原列中的指定类，均未在本文判为零或非零。一般首核和原 $\mathcal D_\psi$ 的完整同修正问题继续开放。没有以 (19) 的普通来源族冒充实际缺陷纤维，也没有由任何返回来源增加一个原中央零。

依赖：[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)、[R514](R514-cubic-forcing-return-and-actual-mirror-tail-normal-form.md)、[R689](R689-original-integral-top-charge-reduction-and-complete-forcing-return.md)、[R697](R697-full-third-normal-top-reduction-and-same-correction-cap.md)；原完整矩阵与同修正约定沿 R479、R481、R651、R687。

本文是全参数有理函数、原赋值格和有限矩阵证明，不新增扫描或可重算数据文件。
