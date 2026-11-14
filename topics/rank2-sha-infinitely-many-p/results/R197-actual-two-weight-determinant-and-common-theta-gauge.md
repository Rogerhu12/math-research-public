# R197. 原双权行列式的共同 theta 消去与真实模 p 公式

日期：2026-11-12。**状态：本篇的整行变换、有限域公式及实际
E34 的完整 Hecke 行已证明；没有证明目标行列式在无穷多个
素数处为单位。**

## 1. 保留两条原函数及所有尺度

使用 R162/R195 的共同 $E_0:y^2=x^3-x$、$\omega=dx/(2y)$
尺度，令
$$
 u=x^{-1/2},\qquad w=z^4,\qquad s=u(z)^4,\qquad
 \vartheta(z)=\sigma(z)/u(z).
$$
这里 $u=z+O(z^5)$、$\vartheta(0)=1$。本篇始终取实际
$$
 A(w)=A_2(z)=\vartheta(z)^{68}P(s),\qquad
 B(w)=B(z)=\vartheta(z)^{68}Q(s).                         \tag{1}
$$
为避免把两条有限字符或二处因子混同，全部多项式再列为
$$
\begin{aligned}
 J(s)&=\frac{s(1-2s+5s^2)(5-2s+s^2)}5,\\
 H_1(s)&=1+4s+70s^2+4s^3+s^4,\\
 H_2(s)&=1+20s-26s^2+20s^3+s^4,\\
 Q_8(s)&=1+364s^2-1088s^3+1190s^4-1088s^5+364s^6+s^8,\\
 P(s)&=J(s)(1-s)^2(1+s)H_1(s)H_2(s),\\
 Q(s)&=J(s)(1-s)(1+s)^2Q_8(s).
\end{aligned}                                                   \tag{2}
$$
故 $P,Q\in s\mathbb Z[1/5][s]$、次数十六、首项均为 $s$。
特别 $A=w+\cdots$、$B-A=-22w^2+\cdots$。

若改回实际曲线截面 $S_{17},S_{34}$，准确的矩尺度是
$$
\begin{aligned}
 H_{A,m}&=2^{m-4}17^{\,1-m/4}H_{S_{17},m},\\
 H_{B,m}&=34^{\,2-m/2}H_{S_{34},m},
 \qquad H_{F,m}=m![z^m]F,\quad 4\mid m .
\end{aligned}                                                   \tag{3}
$$
这些是 R51/R115 的实际截面及 R117 的 $[2]$ 拉回，不是
任意同次数 theta 函数。各因子在本篇目标素数处为单位，但
依赖 $m$，所以不能先删去它们再比较一个双权行列式。
以下直接在 (1) 的原 $A_2,B$ 上进行全部消去。

固定
$$
                 p=4r-1\ge7,\qquad p\text{ 为素数}.            \tag{4}
$$
本篇的公式包括 $p=11$；引用 R189 的平面坐标/中央判据时
仍保留那里排除 $11$ 的范围。

## 2. 前两权中恰有一个共同的非整指数系数

写
$$
 K(w)=\log\vartheta(z)=\sum_{n\ge1}k_nw^n .
$$
整数流 $L'=u^2,\ \vartheta'=L\vartheta$ 给
$$
 k_n=\frac{[z^{4n-2}]u(z)^2}{4n(4n-1)}.                       \tag{5}
$$
椭圆对数的反函数规范为
$$
 z=uF(u^4),\qquad
 F(s)=\sum_{n\ge0}
       \frac{\binom{2n}{n}}{4^n(4n+1)}s^n .                  \tag{6}
$$
对 $0\le n\le2r-1$，$4n+1$ 不是 $p$ 的倍数。因此 (6)
至 $u^{2p-1}$ 的系数均在 $\mathbb Z_p$，首系数为一；
逐项反演证明 $u(z)$ 至 $z^{2p-1}$ 亦整。由此：

- $s(w)$ 至 $w^{2r}$ 整，因为 $u^4$ 的该项只读 $u$ 至
  $z^{2p-1}$；
- (5) 的分子对 $1\le n\le2r-1$ 均整；
- 在这些 $n$ 中，分母 $4n(4n-1)$ 只有 $n=r$ 含 $p$，
  而且恰含一次。

所以
$$
 k_n\in\mathbb Z_p\quad(1\le n\le2r-1,\ n\ne r),\qquad
 \kappa_p:=p k_r\in\mathbb Z_p.                              \tag{7}
$$
实际唯一非整项也能完全确定其首层：
$$
 \boxed{\quad
 \bar\kappa_p=
 \frac{\binom{2r-2}{r-1}}{4^{r-1}}\in\mathbb F_p^\times .
 \quad}                                                       \tag{8}
$$
证明用 Lagrange 反演：
$$
 [z^{p-1}]u^2
 =\frac2{p-1}[s^{r-1}]F(s)^{-(p-1)} .
$$
在所需次数小于 $p$ 的范围，$F^p\equiv1\pmod{(p,s^p)}$，
故 $F^{-(p-1)}\equiv F$。又
$$
 \frac2{p-1}\equiv-2,\qquad
 [s^{r-1}]F=
 \frac{\binom{2r-2}{r-1}}{4^{r-1}(p-2)} .
$$
最后 $\kappa_p=[z^{p-1}]u^2/(p+1)$，即得 (8)。
所有二项式中的阶乘都小于 $p$，所以右端非零。

定义只用于本篇有限窗口的整指数
$$
 \widehat K_p(w)=
 \sum_{\substack{1\le n\le2r-1\\n\ne r}}k_nw^n,\qquad
 E_p(w)=\exp(68\widehat K_p(w)).
$$
因 $2r-1<p$，指数展开在此窗口内的阶乘均为单位。
准确地置
$$
 \widehat A_p=E_p(w)P(s(w)),\qquad
 \widehat B_p=E_p(w)Q(s(w))
                   \pmod{w^{2r+1}}.                          \tag{9}
$$
则两者在 $\mathbb Z_p[w]/(w^{2r+1})$ 中。未读出的
$k_{2r}$ 不影响 (9)：$P(s),Q(s)$ 均从 $w$ 开始。

## 3. 精确整行变换及原 Δ/p³

对 $F=A,B$，令 $\widehat F$ 表示 (9) 的对应函数。
共同指数准确给
$$
 \begin{aligned}
 [w^r]F&=[w^r]\widehat F,\\
 [w^{2r}]F&=[w^{2r}]\widehat F+
                     68k_r[w^r]\widehat F .
 \end{aligned}                                                \tag{10}
$$
没有 $k_r^2$ 项：该项必须乘 $\widehat F(0)=0$。
因此原有理 Taylor 行列式满足精确等式
$$
 \boxed{\quad
 \det\begin{pmatrix}
 [w^r]A &[w^r]B\\
 [w^{2r}]A &[w^{2r}]B
 \end{pmatrix}
 =
 \det\begin{pmatrix}
 [w^r]\widehat A_p &[w^r]\widehat B_p\\
 [w^{2r}]\widehat A_p &[w^{2r}]\widehat B_p
 \end{pmatrix}\in\mathbb Z_p .
 \quad}                                                       \tag{11}
$$
这是对两条原行的同一个下三角消去，不分别选择任意 theta
规范，也不把共同指数函数当成单位乘子后直接省略。

对原 Hurwitz 行，记
$$
 \eta_p=68k_r\frac{(2p+2)!}{(p+1)!}\in\mathbb Z_p^\times .
                                                                  \tag{12}
$$
精确的整格形式是
$$
\begin{aligned}
 \frac{H_{F,p+1}}p
    &=\frac{(p+1)!}p[w^r]\widehat F,\\
 \frac{H_{F,2p+2}-\eta_pH_{F,p+1}}{p^2}
    &=\frac{(2p+2)!}{p^2}[w^{2r}]\widehat F .
\end{aligned}                                                   \tag{13}
$$
两行右端都整；(8) 及 Wilson 定理给
$$
 \frac{(p+1)!}{p}\equiv-1,\qquad
 \frac{(2p+2)!}{p^2}\equiv4,\qquad
 \eta_p\equiv-272\bar\kappa_p\pmod p .                          \tag{14}
$$
第二个阶乘式保留了两个不同的因子 $p,2p$：
删去它们后，三个剩余分块的积模 $p$ 为
$(-1)(-1)2=2$，再乘 $2p/p=2$ 得 $4$。

令
$$
 \Delta_p=
 H_{A,p+1}H_{B,2p+2}-H_{B,p+1}H_{A,2p+2}.
$$
则无条件有
$$
 v_pH_{F,p+1}\ge1,\qquad v_pH_{F,2p+2}\ge1,\qquad
                         v_p\Delta_p\ge3,                    \tag{15}
$$
且本篇的目标公式为
$$
 \boxed{\quad
 \frac{\Delta_p}{p^3}\equiv
 -4\det\begin{pmatrix}
 [w^r]\widehat A_p &[w^r]\widehat B_p\\
 [w^{2r}]\widehat A_p &[w^{2r}]\widehat B_p
 \end{pmatrix}\pmod p .
 \quad}                                                       \tag{16}
$$
式 (13) 还明确说明，原第二个 Hurwitz 行只有一次普遍的
$p$ 因子；先减去已给出的原第一行倍数，才得到两次 $p$。
不能直接把原第二行除 $p^2$ 当成整行。

## 4. 完全在 Fp 上读取右端

令 $d=2r$，在 $\mathbb F_p[s]/(s^{d+1})$ 中取
$$
 \bar F(s)=\sum_{n=0}^{d-1}
       \frac{\binom{2n}{n}}{4^n(4n+1)}s^n,\qquad
 W(s)=s\bar F(s)^4 .
$$
$W$ 的首系数为一，令 $S(w)$ 是其反函数至 $w^d$。
置
$$
 U(w)=\bar F(S(w))^{-1},\qquad
 T_p(w)=
 \sum_{\substack{1\le n\le d-1\\n\ne r}}
       \frac{[w^{n-1}]U(w)^2}{4n(4n-1)}w^n .                 \tag{17}
$$
所有分母在 $\mathbb F_p$ 中可逆。由 (5)–(9)，(16)
右端的四项准确等于
$$
 [w^r],\ [w^{2r}]
 \quad\hbox{作用于}\quad
 e^{68T_p(w)}P(S(w)),\qquad e^{68T_p(w)}Q(S(w)).              \tag{18}
$$
指数只需至 $w^{d-1}$，故不出现 $p!$。
于是 (16) 不是需要先求一个未知 $p$-adic regulator 的公式：
它由原两个固定次数十六多项式和一个长度 $O(p)$ 的有限域
反演、乘法、指数递推计算。

同样，若记
$M_{j,k}=[w^{jr}]e^{68T_p(w)}S(w)^k$，则
$$
 \det\widehat R
 =\sum_{1\le k<l\le16}
       (P_kQ_l-Q_kP_l)
       (M_{1,k}M_{2,l}-M_{1,l}M_{2,k}).                       \tag{19}
$$
这保留原 $P,Q$ 的所有系数。它只把两个原列送到同一有限域
矩阵，没有声称该矩阵在每个 $p$ 上均有某个指定非零子式。

## 5. 与完整中央失败的准确比较

R195 已无条件证明 $\Delta_p\ne0$（用固定辅助位 $5$），但
那个结论不等于本目标位的 (16) 非零。
对 R189/R195 的范围 $p\ne11$，两个完整中央导数同时为零
仍迫使
$$
 H_{A,p+1},H_{B,p+1}\in p^2\mathbb Z_p,\qquad
                         \Delta_p\in p^5\mathbb Z_p .        \tag{20}
$$
经本篇原整行变换，这些必要条件变成
$$
 \widehat R_1\in p\mathbb Z_p^2,\qquad
 \det(\widehat R_1,\widehat R_2)\in p^2\mathbb Z_p .           \tag{21}
$$
当第一条已成立时，第二条等价于
$$
 \det(p^{-1}\widehat R_1,\widehat R_2)\equiv0\pmod p .         \tag{22}
$$
因此实际的后继检测保留了被除一次 $p$ 的原第一行。
只看 (16) 模 $p$，在 $\widehat R_1\equiv0$ 时当然自动为零；
不能把这一个模 $p$ 行列式当成两次深度的全部信息。
本篇没有证明 (21) 对无穷多个 $p$ 失败。

### 5.1. 与真实 Cartan 整轴的准确兼容

令 $R=r(p-1)$。R199 在同一原 $w$ 参数中证明
$$
 A=e^{17u_0w^r}f_A(w),\qquad
 B=e^{17u_0w^r}f_B(w)\pmod{w^{R+1}},
 \qquad f_A,f_B\in\mathbb Z_p[[w]] ,
$$
其中 $f_A=w+\cdots$，且 $2r\le R$。因此 (9)–(10) 与
这两个真实轴级数满足
$$
 f_A=e^{d_pw^r}\widehat A_p,\qquad
 f_B=e^{d_pw^r}\widehat B_p\pmod{w^{2r+1}},\qquad
 d_p=68k_r-17u_0 .
$$
两端均整；比较第一式的 $w^{r+1}$ 系数，利用
$[w]\widehat A_p=1$，得到
$$
 d_p=[w^{r+1}]f_A-[w^{r+1}]\widehat A_p\in\mathbb Z_p .
$$
故若 $\tau_p=pu_0$，则 $\bar\tau_p=4\bar\kappa_p$。记
$v_j=([w^{jr}]f_A,[w^{jr}]f_B)$，准确有
$$
 v_1=\widehat R_1,\qquad
 v_2=\widehat R_2+d_p\widehat R_1,\qquad
                 \det(v_1,v_2)=\det(\widehat R_1,\widehat R_2).
$$
所以 (16) 也给真正 Cartan 整轴前两行的模 $p$ 行列式。
这里是同一个整下三角行操作；并未免费把非整 $u_0$ 当成
整坐标变换。

## 6. 两条实际 full-weight-one 行的 Hecke 比较

R82 的 $57$ 个角色分量来自 E17 原 $256$ 点，不能直接充当
E34 的有限行。本节支付第二条实际轨道，并明确它给出的约束。

在 $\mathcal O_K/(68)$，写标签为 $(a,b)$，$a+bi$。
E34 的原导子是 $(68)$、起点为 $(1,0)/68$。
由 R112 的
$\psi_{34}=\psi_0(\chi_{136}\circ N)$，其实际 $512$ 点轨道为
$$
 \mathcal S_{34}=
 \left\{(a,b):
 \begin{array}{l}
 a\ \text{奇},\ b\ \text{偶},\quad17\nmid a^2+b^2,\\
 \chi_4(a)\chi_{17}(a^2+b^2)=1
 \end{array}\right\}.                                       \tag{23}
$$
证明如下。把 $\alpha=a+bi$ 在模 $(1+i)^3$ 的单位代表写成
$\varepsilon\in\mu_4$，则 $\psi_0$ 的有限部分为
$\varepsilon^{-1}$。若 $a$ 偶、$b$ 奇，该值为 $\pm i$，
乘二次扭曲后不可能成为一。若 $a$ 奇、$b$ 偶，则
$$
 \varepsilon^{-1}=\chi_4(a+b),\qquad
 \chi_8(a^2+b^2)=(-1)^{b/2}.
$$
二者乘积是 $\chi_4(a)$；余下十七处因子正是
$\chi_{17}(a^2+b^2)$。有限字符的核即 (23)。
原 CM 射线类作用的像是此核，大小为
$|(\mathcal O_K/(68))^\times|/4=512$，没有少取一个二处陪集。

从而实际带符号行准确为
$$
 w_{34}(a,b)=
 1_{\{a\ {\rm odd},\,b\ {\rm even}\}}\,
                   \chi_4(a)\chi_{17}(a^2+b^2),              \tag{24}
$$
其中 $\chi_{17}(0)=0$。它满足
$$
 w_{34}(ua,ub)=\chi_4(u)w_{34}(a,b)
             \quad(u\in(\mathbb Z/68)^\times).               \tag{25}
$$
定义真实 completed-zeta 全轨道和
$\mathcal G_{34}$，及
$$
 F_{34}^{(1)}(\tau)=\frac{\mathcal G_{34}(68\tau)}{2\pi i},
 \qquad
 C_{34}(d,e)=\sum_{a\bmod68}w_{34}(a,e)\zeta_{68}^{ad}.
$$
与 R47/R82 的同一 Kronecker 展开相比，本次必须保留 $b=0$
的 cotangent 项，准确得到
$$
 F_{34}^{(1)}
 =-8i-\sum_{n\ge1}\left(\sum_{de=n}C_{34}(d,e)\right)q^n .
                                                                  \tag{26}
$$
确实 $b\ne0,34$ 的标签按 $b\leftrightarrow68-b$ 配对，
常数相消；$b=34$ 的常数为零。在 $b=0$ 处，原轨道是
$a\equiv1\pmod4$ 的模 $68$ 单位，且
$$
 \sum_{\substack{a\bmod68\\a\equiv1(4),\,17\nmid a}}
       \cot(\pi a/68)
 =17\cot(\pi/4)-\cot(\pi/4)=16.
$$
除 $2i$ 即为 $-8i$，不是 R82 的常数 $4$。

由 (25)，R82 的有限核换元与标准 Hecke 计算现在分别适用于
两条**实际** full-weight-one 行：
$$
\begin{aligned}
 \langle p\rangle F_j^{(1)}
       &=\chi_4(p)\sigma_{p^2}F_j^{(1)},\\
 T_pF_j^{(1)}&=(1+\chi_4(p))\sigma_pF_j^{(1)},\\
 U_pF_j^{(1)}&=V_p\sigma_{p^2}F_j^{(1)},\qquad
 U_p^2F_j^{(1)}=\sigma_{p^2}F_j^{(1)}
                   \quad(p\equiv3\!\!\pmod4),
 \qquad j=17,34 .
\end{aligned}                                                   \tag{27}
$$
常数项在这里也相容，因为 $\sigma_{p^2}$ 固定 $i$。
这不是对原半权行或 $w$-Taylor 系数直接施加 cusp 的 $U_p$。

两条有限行仍有真实差别：$C_{34}$ 只在 $d$ 奇、$e$ 偶时
可能非零，且它在十七处 $a\mapsto-a$、二处不变的作用下固定。
第一条由 $a\mapsto a+34$ 的符号换元证明，第二条直接由
(24) 证明。因此当 $p^2\equiv-1\pmod{17}$ 时，
$$
                      \sigma_{p^2}F_{34}^{(1)}=F_{34}^{(1)}.  \tag{28}
$$
E17 的 R82 分解含非零的奇指数十七角色，并无这一普遍
不变性。即使在 (28) 的素数类中，(27) 仍是全部同源分支的
迹关系；本篇未将其变成 (16) 的非零式。
原中央 Borel 平方公式也不能把两个半权列的行列式无证换成
两个 full-weight-one 形式的普通线性行列式。

## 7. 复算与剩余实质问题

[精确脚本](../scripts/check-actual-two-weight-gauge-minor.py)
用原无分母 Hurwitz 流生成 (1)，独立用 (6)、(17)–(18) 在
$\mathbb F_p$ 上恢复四个系数，并核对 (8)、(10)–(16)。
只选已有的 $p=7,19$ 校准规范，不扩充数值素数列表来代替证明。
脚本另直接枚举 (23) 的原有限字符核和 (25)，保留二处标签。

所有外部识别均来自已证明的原对象：

- [R51](R51-explicit-theta-section-and-central-square-constant.md)、
  [R115](R115-e34-explicit-degree68-theta-section.md) 的实际截面；
  [R117 的共同尺度原证明](../notes/2026-11-12-two-rank-two-theta-linear-convolution.md)；
- [R57 的整数流](R57-global-hurwitz-integers-and-fixed-polynomial-flow.md)、
  [R162](R162-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md) 的原 $P,Q$；
- [R112](R112-e34-dyadic-theta-and-two-rank-two-rows.md) 的完整 CM
  字符与 dyadic 向量；[R82 的完整证明](../notes/2026-11-12-actual-weight-one-hecke-and-character-decomposition.md)，
  其权一 Hecke 规范的原始文献为 Dasgupta–Kakde **2021** §4
  与 Borisov–Gunnells **2001** §5.1；
- [R195](R195-fixed-five-adic-moments-and-first-two-central-rows.md)
  的统一前两行独立性与完整中央失败必要条件。

尚需真正的新输入，是证明 (21) 在无穷多个目标素数处不成立，
或把相应上界转成同一完整前缀的严格净算术收益。
本篇的原行变换和有限域式不预设该输入。
