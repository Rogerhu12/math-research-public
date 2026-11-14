# 普通 CL reciprocity、实际 CM 伴随形式及线性次数

日期：2026-11-12。**已证明。** 本篇给 R134 原 Heegner 迹的一阶
CL reciprocity 模型、明确的权 $p-1$ CM 分子及 $O(p)$ 极点次数。
原受限环类轨道上的两矩无穷非零仍未证明。

## 1. 固定微分与两种 CM 域

固定
$$
 E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
 N=9248,\qquad F=\mathbb Q(\sqrt{-15}).
$$
取 R105–R134 的实际参数化 $\pi:X_0(N)\to E$，$\pi(\infty)=O$，
写
$$
 \omega_E=\frac{dx}{2y},\qquad
 \pi^*\omega_E=c_\pi f(q)\frac{dq}{q},\qquad
 f=\sum_{n\ge1}a_nq^n,\quad a_1=1.
 \tag{1}
$$
其中 $c_\pi\in\mathbb Q^\times$ 固定。删去其分子、分母及所有
固定模型坏素数。本文使用
$$
 \omega_0=c_\pi^{-1}\omega_E,\qquad
 \log_0=c_\pi^{-1}\log_E,\qquad z_0=c_\pi^{-1}z_Q.
 \tag{2}
$$
于是 $\pi^*\omega_0=f\,dq/q$，而 $\omega_0$ 是整不变微分的生成元。
Buium–Poonen 的 (4.8) 以所选微分写作 $dx/y$；其 $\delta$-character
及 reciprocity 函数均随微分线性缩放。我们从开始就选择 (2)，故
原式与 $dx/(2y)$ 间的因子 $2$ 已被明确吸收，不再藏在符号中。
恢复 R134 的原微分时，将本文所有原函数、迹和两矩乘以单位 $c_\pi$。

以下令 $p\ge13$ 在 **$F$ 和 $K$ 都分裂**，且排除上述固定有限集。
写
$$
 X^2-a_pX+p=(X-\alpha_p)(X-\beta_p),\qquad
 \alpha_p\in\mathbb Z_p^\times,\quad
 \beta_p=p/\alpha_p,\quad v_p(\beta_p)=1.
 \tag{3}
$$
置 $u_p=\alpha_p^{-1}$，所以 BP 的非单位根 $u_pp$ 正是 $\beta_p$。
这里 $u_p$ 不表示类群中阶为 $u=(\ell+1)/p$ 的子群。

目标 $E$ 在这些 $p$ 是 canonical lift（CL）：其 CM 阶为
$\mathbb Z[i]$，$p$ 在 $K$ 分裂。原源点 $x_\ell$ 的 CM 阶为
$\mathcal O_\ell\subset F$；$p$ 在 $F$ 分裂且 $p\ne\ell$，
故它及所有原共轭同样是 CL。两项分别应用 BP Theorem 4.4(1)(b)，
不能只由目标 ordinary 推出源点 ordinary。

取 $R=W(\overline{\mathbb F}_p)$，$\phi$ 为 Witt Frobenius。
原环类域在 $p$ 不分歧，所以选定嵌入后的全部源点都在 $R$ 中。
它们不在尖点，且 ordinary 约化的端环分式域是 $F$，因此其
$j$ 值不可能是端环分式域分别为 $\mathbb Q(\sqrt{-3})$、
$\mathbb Q(i)$ 的 ordinary $j=0,1728$。故这些实际点全落在
BP Theorem 3.17 的标准开集；没有删除轨道中未知的点。

BP 的一般 reciprocity 本身不要求目标 CL：目标非 CL 时，
Theorem 3.17(2) 给出的正是 R134 的 $f_{\rm pre}$，使用二阶
$\delta$-character。本篇新增的简单极点及 $O(p)$ **总次数**
才需要目标 CL；没有把该额外假设强加给 R134 的原比较。

## 2. 实际 CL 函数及原函数的准确因子

BP Lemma 4.7、(4.8) 给一阶整 $\delta$-character
$$
 \psi_0(P)=\frac{(\phi-\beta_p)\log_0(P)}p.
 \tag{4}
$$
在形式群外，(4) 先由群同态延拓；对 R134 的实际 $Q$，
也可用一个 $p$-单位整数将点送入形式群，所得对数一致。
其模 $p$ 核为
$$
 \psi_0^{-1}(pR)=E(R)_{\rm tors}+pE(R).
 \tag{5}
$$

记 $V(\sum b_nq^n)=\sum b_nq^{pn}$，并设
$$
 f^{(-1)}=\sum_{p\nmid n}\frac{a_n}{n}q^n,\qquad
 f_{[u_p]}^{(-1)}=\sum_{r\ge0}u_p^rV^rf^{(-1)}.
 \tag{6}
$$
BP Theorem 3.17(3) 给实际 CL reciprocity 函数 $\Phi^\dagger$，
其尖点展开及约化 $g_p=\overline{\Phi^\dagger}$ 满足
$$
 \Phi^\dagger_\infty=-u_pf_{[u_p]}^{(-1)},\qquad
 g_p^p-\bar a_pg_p=f_{\rm pre},\qquad
 f_{\rm pre}:=\overline{f^{(-1)}}
       =\frac{\Theta^{p-2}\bar f}{\mathrm{Ha}_p^p}.
 \tag{7}
$$
这里 $\Theta$ 为 Katz holomorphic theta，$\mathrm{Ha}_p$ 的
所有尖点展开均为 $1$。$g_p$ 在紧模曲线的 ordinary 部分
（包括尖点）正则。BP 证明中的 (4.77) 同时给真实取值等式
$$
                  \Phi^\dagger(x)=\psi_0(\pi(x))
                  \quad(x\text{ 为上述 CL 点}).
 \tag{8}
$$
因此 (7) 并非只有 q 展开的候选函数。

## 3. 固定曲线的明确 CM 伴随分子

令 $\psi_E$ 为 $E/K$ 的 Hecke 角色，导子
$\mathfrak f=2(1+i)17$、无穷型 $(1,0)$。定义经典 CM theta 形式
$$
 H_p(q)=
 \sum_{(\mathfrak a,\mathfrak f)=1}
              \psi_E(\mathfrak a)^{p-2}q^{N\mathfrak a}.
 \tag{9}
$$
Hecke–Shimura 定理（Schütt，Theorem 1.4）给它权 $p-1$。
其准确有限导子仍为 $\mathfrak f$：因为 $K$ 类数为 $1$，
可将角色在主理想上写成 $\epsilon(a)a$，有限部分值在
$\mu_4$ 中；$p-2\equiv3\pmod4$，这个幂是 $\mu_4$ 的自同构，
保留其全部局部核。因
$$
 \psi_E((n))=\chi_{-4}(n)n,\qquad
 \psi_E((n))^{p-2}/n^{p-2}=\chi_{-4}(n),
$$
模形式 nebentypus 为 $\chi_{-4}^2=1$，故准确 level 是
$4N\mathfrak f=9248$。共轭理想成对及 Gaussian 整性给
$H_p\in S_{p-1}(\Gamma_0(N),\mathbb Z)$。

现在逐项证明所需的模 $p$ 同余。固定与 (3) 相容的
$K\hookrightarrow\mathbb Q_p$。若 $(n,p)=1$，
$$
 \psi_E(\mathfrak a)^{p-2}
 \equiv\psi_E(\mathfrak a)^{-1}
 =\frac{\overline{\psi_E(\mathfrak a)}}{n}\pmod p
 \quad(N\mathfrak a=n).
$$
共轭置换求和理想，故 $[q^n]\bar H_p=\bar a_n/n$。
对 $n=p^rm$、$(m,p)=1$，在所有范数 $p^r$ 的理想中，
含有 $\psi_E$ 值为非单位根 $\beta_p$ 的项模 $p$ 为零，
仅单位根 $\alpha_p$ 的那一项保留。于是
$$
 [q^{p^rm}]\bar H_p=\bar\alpha_p^{-r}\frac{\bar a_m}{m},
 \qquad
 \bar H_p(q)=\overline{f_{[u_p]}^{(-1)}}(q).
 \tag{10}
$$
这也覆盖坏素数 $2,17$ 的系数：原角色和 (9) 均只对素于
$\mathfrak f$ 的理想求和，其对应系数同时为零。

将 (10) 与 (7) 用同权 q 展开原则比较，得到全局等式
$$
 \boxed{\quad
 h_p:=\frac{\bar H_p}{\mathrm{Ha}_p},\qquad
 g_p=-\bar a_p^{-1}h_p,\qquad
 f_{\rm pre}=h_p-\bar a_p^{-1}h_p^p.
 \quad}
 \tag{11}
$$
两边都是权零函数。特别地，$g_p$ 从 BP 所用 $X_1(N)$
下降到 $X_0(N)$；这里的下降由 (9) 的真实 trivial
nebentypus 给出，不是任意改变有限角色。

R105 的旧形式映射 $\Phi=\pi d_1+\pi d_3$ 对应
$f+3V_3f$，但原函数是 $G+V_3G$。因此其 reciprocity
约化为 $g_p+V_3g_p$，其伴随分子为
$\bar H_p+V_3\bar H_p$（在 level $3N$ 上除以 Hasse）。
尖点一次系数仍为 $1$。没有把微分里的 $3$ 错留在权零原函数中。

## 4. 简单超奇异极点、准确 filtration 及一次 AS 非平凡

在一个固定的素于 $p$ 的细模曲线 $X$ 上，Hasse 在超奇异点
是简单零，且在尖点是单位。由 (11)，$h_p$、$g_p$
只可能有简单超奇异极点。至少一处是真的：若全无极点，
则 $h_p$ 在紧曲线正则而为常数；但其 q 展开常数为零、
一次系数为 $1$，矛盾。等价地，$\bar H_p$ 不被 Hasse
整除，其 exact filtration 是 $p-1$。上述旧形式分子也有
相同结论。

设 $g_X$、$\nu_X$ 分别为固定 $X$ 的 genus 和尖点数。
由 $\omega^{\otimes2}\simeq\Omega_X^1(\mathrm{cusps})$，
$$
 \boxed{\quad
  \deg(g_p)\le
       \frac{2g_X-2+\nu_X}{2}(p-1)=O(p).
 \quad}
 \tag{12}
$$
这里 degree 是极点除子的次数，等于非恒定函数映射到
$\mathbb P^1$ 的次数。下降至 $X_0(N)$ 后次数不会增加。
此界也直接来自 BP Corollary 3.19 的证明：
在 CL 分支有准确 $p\deg(g_p)=\deg(f_{\rm pre})$，
而非只使用其兼容两分支的粗 $O(p^2)$ 界。

还有比 R134 更强的实际全局 AS 事实。令
$\operatorname{AS}(v)=v^p-v$，函数域取
$\overline{\mathbb F}_p(X)$。有理 $2$-挠点 $(0,0)$
使 $a_p$ 为偶数；$p\ge7$ 时 $p-1>2\sqrt p$，结合
Hasse 界得到 $\bar a_p\ne1$。由 (11)，
$$
 f_{\rm pre}-\operatorname{AS}(-\bar a_p^{-1}h_p)
             =(1-\bar a_p^{-1})h_p.
 \tag{13}
$$
右边在上述某处仍为简单极点。非恒定有理函数 $v$ 若有
$r$ 阶极点，则 $v^p-v$ 在该点有准确 $pr$ 阶极点；
常函数也不能产生简单极点。因此
$$
 h_p\notin\operatorname{AS}\bigl(\overline{\mathbb F}_p(X)\bigr),
 \qquad
 f_{\rm pre}\notin\operatorname{AS}
                       \bigl(\overline{\mathbb F}_p(X)\bigr).
 \tag{14}
$$
同时，**twisted** 方程 $y^p-\bar a_py=f_{\rm pre}$ 确有
有理解 $y=g_p$。其线性系数是 $\bar a_p\ne1$；
不能把它与 (14) 的 untwisted AS 方程混同。

## 5. 原完整环类迹与两个真实矩

保持 R134 的原点定义：
$$
 H=F[\ell],\quad
 \mathsf U=\operatorname{Gal}(H/L),\quad
 |\mathsf U|=2u,\quad u=(\ell+1)/p,\qquad
 Q=\operatorname{Tr}_{H/L}\pi(x_\ell).
 \tag{15}
$$
取 $p$ 上素位的算术 Artin 元 $s\in\Gamma=\operatorname{Gal}(L/F)$。
由 (8)、$\psi_0$ 可加及其系数在 $\mathbb Z_p$，
$$
 \begin{aligned}
 B&:=\sum_{\gamma\in\mathsf U}
          \Phi^\dagger(x_\ell^\gamma)
       =\psi_0(Q)=(s-\beta_p)z_0,\\
 \eta_0&:=c_\pi^{-1}\eta_{p,\ell}
       =(s-\alpha_p)B
       =(p-a_ps+s^2)z_0.
 \end{aligned}
 \tag{16}
$$
这里 $z_0$ 是 R134 先延拓原点对数、再除唯一一层 $p$
得到的实际整元素。没有将整性无证分配给各个
$\log_0\pi(x_\ell^\gamma)/p$。CL 函数的各取值本身整，
是 (4)、(8) 的结论。

模 $p$ 后，在所有完成组成的真正半局部模中，
$$
 \bar B=s\bar z_0,\qquad
 C:=\sum_{\gamma\in\mathsf U}
                 h_p(\overline{x_\ell^\gamma})
      =-\bar a_p\,s\bar z_0,\qquad
 \bar\eta_0=\bar B^p-\bar a_p\bar B.
 \tag{17}
$$
对最后一式的 $p$ 次幂须逐完成理解为算术 Frobenius；
当分解完全分裂时仍保留完成间的 $\Gamma$ 置换。
使用阶 $u$ 的惯性子群与 $\Phi=\pi d_1+\pi d_3$ 时，原
类数 $2$ 的和已经在 $\Phi$ 内；再用 $\mathsf U$ 就会重复。
(15)–(17) 始终使用完整 $2u$ 项约定。

若 $s=\tau^h\ne1$，令 $k=\mathbb F_{p^p}$、
$\upsilon^p-\upsilon=h$、$\tau\upsilon=\upsilon+1$，
并对迹零元素 $z=\bar z_0$ 置
$$
 T_1(z)=\operatorname{Tr}_{k/\mathbb F_p}(\upsilon z),
 \qquad
 T_2(z)=\operatorname{Tr}_{k/\mathbb F_p}(\upsilon^2z).
$$
将 $s^{-1}\upsilon=\upsilon-h$ 代入有限域迹，直接得到
$$
 \begin{aligned}
 \binom{T_1(\bar B)}{T_2(\bar B)}
   &=\begin{pmatrix}1&0\\-2h&1\end{pmatrix}
                         \binom{T_1(z)}{T_2(z)},\\
 \binom{T_1(C)}{T_2(C)}
   &=-\bar a_p\begin{pmatrix}1&0\\-2h&1\end{pmatrix}
                         \binom{T_1(z)}{T_2(z)},\\
 \binom{T_1(\bar\eta_0)}{T_2(\bar\eta_0)}
   &=\begin{pmatrix}1-\bar a_p&0\\
                   -2h(2-\bar a_p)&1-\bar a_p\end{pmatrix}
                         \binom{T_1(z)}{T_2(z)}.
 \end{aligned}
 \tag{18}
$$
三矩阵均可逆。另一素位按 R134 的共轭规则同时变换，
没有删掉它。若 $s=1$，改用 R134 的实际完成置换矩
$A_1,A_2$，同式取 $h=0$ 成立；不将单个 $\mathbb F_p$
完成冒充次数 $p$ 的域扩张。

特别地，R130 的实际算子
$\mathcal D_2=\sum_{j=0}^{p-1}\binom j2\tau^j$ 满足
$$
 \mathcal D_2\bar z_0\ne0
 \ \Longleftrightarrow\
 \mathcal D_2 C\ne0.
 \tag{19}
$$
右边是原 $2pu$ 个 CM 项的准确加权和：
$$
 \sum_{j=0}^{p-1}\binom j2
       \sum_{\gamma\in\mathsf U}
           h_p(\overline{x_\ell^{\tau^j\gamma}}).
 \tag{20}
$$
它非零便给 $a\le1$，由 R127 的整 Selmer 推论得到
$\Sha(E/\mathbb Q)[p^\infty]=0$。这只是一条真实充分证书；
本篇没有把 (20) 的无穷非零当作已得结论。

## 6. 线性次数尚未自动支付的量词

BP Theorem 1.3 / Corollary 3.19 的计数控制的是落在一个
指定子群 $\Lambda\le E(R)$ 内的**个别** CM 像点，其中
$$
 r=\dim_{\mathbb F_p}
 \frac{\Lambda}{\Lambda\cap(E(R)_{\rm tors}+pE(R))}.
 \tag{21}
$$
CL 分支的常数可用 (12)，所以形状是 $O(p)\,p^r$。
(20) 消失却只是一条带全部迹权重的关系，不能推出每个
$\pi(x_\ell^{\tau^j\gamma})$ 属于同一个小 $r$ 子群。
BP Theorem 3.24 的 uniqueness 假设对所有 CL 点及全部相应
Hecke 关系成立，也不是当前指定 $C_p$ 商上一个关系的反命题。

即使只考虑次数和 Frobenius 轨道，仍有准确反例说明缺少的输入：
在 $k=\mathbb F_{p^p}$、$p\ge7$ 中，取上述 $\upsilon$。
迹配对非退化且 $1,\upsilon,\upsilon^2$ 线性独立，故
三个迹同时为零的空间维数是 $p-3$。它含 $\mathbb F_p$，
因为 $\operatorname{Tr}(\upsilon^j)=0$ 对 $0\le j\le2$。
可取 $b\notin\mathbb F_p$ 在这个核内；$b$ 的次数准确为 $p$。
于是 $\mathbb P^1$ 上次数 $1$ 的函数 $x$ 在这条完整
Frobenius 轨道上同样有前三矩零。此例不是原模曲线的反例，
只严格说明 (12) 加轨道长度本身不能推出 (20) 非零。

原轨道的无权总迹本来为零：
$N_\Gamma Q=0$ 及 (17) 给 $N_\Gamma C=N_\Gamma\bar\eta_0=0$。
这与 (14) 的实际全局 AS 非平凡同时成立；所以需要利用
该指定环类轨道的额外结构，而非把它换成任意闭点。

最后区分两个已证素数选择：R123 的密度一选择可以限制到
$p$ 在 $F,K$ 同时分裂的正密度子集，为本篇提供无穷合法输入；
它没有同时给 $u<\sqrt p$。R126 给 $u^2=o(p)$ 的无穷输入，
但没有控制这些 $p$ 在 $F,K$ 的分裂类型。本篇逐个适用于
其中满足分裂条件的 $p$，未证明该交集无穷。

## 一手来源与使用范围

- A. Buium, B. Poonen, *Independence of points on elliptic curves
  arising from special points on modular and Shimura curves, II:
  local results*, Compositio Math. **145** (2009), 566–602，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)。
  作者版 2008-10-20，Theorems 3.5、3.17、3.24、Corollary 3.19
  及其证明（印页 6–11），Theorem 4.4、Lemma 4.7、
  (4.8)（印页 15–17），(4.77)。本篇仅用这些已出版的
  CL reciprocity 与次数结论，不将有限群计数改成受限迹非零定理。
- M. Schütt, *CM newforms with rational coefficients*，2008 年
  最终作者版，§1 Theorem 1.4，印页 3，
  [原文](https://arxiv.org/pdf/math/0511228)。
  这里使用其中准确陈述的经典 Hecke–Shimura theta 模形式
  定理；未使用该文涉及 ERH 的分类断言。(9)–(11) 的原曲线
  导子、角色及模 $p$ 系数比较均在本文直接证明。
- N. Katz, *A result on modular forms in characteristic p*，
  LNM **601** (1977), 53–61，
  [作者全文](https://web.math.princeton.edu/~nmk/old/modformcharp.pdf)，
  §II Theorem (1)–(2)、Corollaries，及印页 60 的 Hasse 简单零。
- R105、R123、R127、R130、R134：原完整迹、整数指数与
  全半局部两矩。本文保留这些实际对象；只将原函数明确化为
  (11)，并给其线性次数、一次 AS 类和 (16)–(20) 的完整比较。
