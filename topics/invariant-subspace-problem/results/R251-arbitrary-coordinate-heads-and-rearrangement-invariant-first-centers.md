# R251：任意有限位集的真实进位预算与按幅度排序的 first 分支中心

日期：2026-11-12（UTC）。作者：kernel。
状态：以下结论已证明。本稿加强 R243 的正向多项式循环类；规范恒幅交替调和行仍不满足假设，不宣称普通 ISP 完成。

## 1. 新结论与准确的排序约定

沿用实际 Haar 模型
$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad a\in\ell^2,
\qquad V_j=(I-N_j)(I+N_j)^{-1}.
$$
全部无界算子及幂均取 R125/R176 的真实自然实现。内积对第一变量线性。

将非零 $|a_j|$ 按非增顺序排列，得到 $r_1\ge r_2\ge\cdots>0$；同模时按原位置递增打破并列。令 $\iota(k)$ 为对应的原位置，置
$$
A_n=\{\iota(1),\ldots,\iota(n)\},\qquad
\tau_n=a_*+\sum_{k=1}^n a_{\iota(k)}.
\tag{1.1}
$$
若只有有限个非零系数，以下按有限和另行处理。无限支撑时假设
$$
\boxed{n r_n\longrightarrow0.}
\tag{1.2}
$$
这只限制系数幅度的递减重排，不要求原位置上的 $|a_j|\le b/(j+1)$。

**定理 1.1。** 在 (1.2) 下，设 $M\ne0$ 是闭子空间，
$$
M\subseteq\operatorname{Dom}X,\qquad XM\subseteq M.
$$
闭图定理使 $B=X|_M$ 有界。

1. 若 $(\tau_n)$ 无界，则这样的 $M$ 不存在。
2. 每个有限聚点 $s$ 都属于 $\sigma(B)$。
3. 若 $\sigma(B)$ 有限，则 $(\tau_n)$ 必收敛于一个有限数 $s$，且
   $$
   \boxed{\sigma(B)=\{s\}.}
   \tag{1.3}
   $$

这里不需要先假定 $M$ 对 $A$ 不变。第 3 项的“有限谱”不能省略。

**推论 1.2。** 对同一 first
$$
u=a_*+\sum_j a_j\chi_j
$$
及任意复 $\ell^2$ first 指数 $w$，有：

- 若 $(\tau_n)$ 不收敛到有限复数，则每个非零多项式 $q$ 都使 $q(u)e^w$ 为实际 $A$ 的循环向量；
- 若 $\tau_n\to s$，则每个满足 $q(s)\ne0$ 的多项式 $q$ 都使 $q(u)e^w$ 循环。

这使用 R176/R147 已完成的实际 Bell 多项式及加权图循环接口，证明见 §7。没有声称任意不变限制的 first 值域由此都稠密。

核心改进是：有限头进位的四次成本依赖头中位数，而非最大位号；尾的指数次数权则只数未选中的位。

## 2. 任意有限位集的四次进位界

固定有限集 $F\subset\mathbb N_0$，记
$$
d=|F|,\qquad b_F=\sum_{j\in F}|a_j|,
\qquad H_F=\sum_{j\in F}a_j(V_j-I).
$$
实际关系为
$$
N_j^2=\eta_jN_{j+1},\qquad
\eta_j\le e^{-770\,16^j},\qquad
\|N_j\|\le1,\qquad \|(I+N_j)^{-1}\|\le3.
\tag{2.1}
$$

考虑一个总次数为 $k$ 的单项式 $\prod_{j\in F}N_j^{k_j}$。
从低到高按 (2.1) 进位，令 $c_j$ 为第 $j$ 位的进位次数，$\epsilon_j\in\{0,1\}$ 为最终余位。有限的非负整数递推给
$$
\prod_{j\in F}N_j^{k_j}
=\left(\prod_j\eta_j^{c_j}\right)\prod_jN_j^{\epsilon_j}.
\tag{2.2}
$$
进入某位的额外进位只会增大该位的次数，故
$$
c_j\ge\lfloor k_j/2\rfloor.
$$
因此
$$
C_{\rm car}:=\sum_jc_j
\ge\sum_{j\in F}\lfloor k_j/2\rfloor
\ge\frac{k-d}{2}.
\tag{2.3}
$$
尤其 $k\ge2d$ 时 $C_{\rm car}\ge k/4$。这一步没有出现 $\max F$。

令
$$
E_{\rm car}=\sum_j16^jc_j.
$$
进位传播满足 $c_{j+\ell}\ge\lfloor c_j/2^\ell\rfloor$。若 $c_j\ge1$，
取 $\ell=\lfloor\log_2c_j\rfloor$，得到
$$
E_{\rm car}\ge16^{j+\ell},
\qquad c_j\le2E_{\rm car}^{1/4}2^{-j}.
$$
对 $j\ge0$ 求和，
$$
C_{\rm car}\le4E_{\rm car}^{1/4}.
$$
结合 (2.3)，对 $k\ge2d$，
$$
E_{\rm car}\ge(k/16)^4.
\tag{2.4}
$$

由于 $V_j-I=-2N_j(I+N_j)^{-1}$，全部分母相互交换，也与全部 $N_i$ 交换。
一个次数 $k$ 的多项式项只付 $3^k$ 的逆范数和 $2^k$ 的系数因子。由 (2.2)–(2.4)，再对多项式系数绝对值求和，得到
$$
\boxed{
\|H_F^k\|\le(6b_F)^k e^{-\gamma k^4},
\qquad k\ge\max(2d,16),\qquad
\gamma=\frac{770}{16^4}.
}
\tag{2.5}
$$
所有 $k$ 上另有粗界 $(6b_F)^k$。所用真实进位及分母预算与 R241 相同，只有 (2.3) 改用了任意支撑的计数。

### 2.1 小位数头的统一指数预算

记 $k_0=\max(2d,16)$，$x=6b_FR$，
$$
C_\gamma=\sum_{k\ge0}e^{-\gamma k^4/2},
\qquad
c_\gamma=\frac{3}{4(2\gamma)^{1/3}}.
$$
对 $|z|\le R$，由 (2.5)，丢掉有利的 $1/k!$ 后，用
$$
k\log(1+x)-\frac{\gamma}{2}k^4
\le c_\gamma[\log(1+x)]^{4/3}
$$
估计高幂和，可得
$$
\log\|e^{zH_F}\|
\le
\log(k_0+C_\gamma)
+k_0\log(1+6b_FR)
+c_\gamma[\log(1+6b_FR)]^{4/3}.
\tag{2.6}
$$
当 $d\le\sqrt R+1$ 时，$b_F\le\|a\|_2\sqrt d$，所以 (2.6) 的右侧是
$$
o(R)
\tag{2.7}
$$
并且这个结论一致于所有满足该位数限制的有限集 $F$，与其最大位号无关。空集给 $H_F=0$，同样适用。

## 3. 只数补集位的真实指数次数权

固定任意有限集 $F$，令 $J=F^c$，
$$
Z_J=X_{\sum_{j\in J}a_j\chi_j},\qquad
g_J=\left(\sum_{j\in J}|a_j|^2\right)^{1/2}.
$$
令 $\mathcal N_J$ 只数 Walsh 单项式中属于 $J$ 的位，置
$$
\mathcal H_{J,t}=\operatorname{Dom}e^{t\mathcal N_J},
\qquad \|f\|_{J,t}=\|e^{t\mathcal N_J}f\|,
\qquad 0\le t\le1.
$$
令 $Q_F$ 为 $\operatorname{span}\{\chi_E:E\subset F\}$ 上的正交投影。
因此 $Q_FH$ 恰是 $\mathcal N_J$ 的零次层；它保留整个 $2^{|F|}$ 维的选中头。

**引理 3.1。** 存在同一个有限模型常数 $C$，使
$$
\boxed{
\|Z_J:\mathcal H_{J,t}\to\mathcal H_{J,t-\delta}\|
\le Cg_J\delta^{-1/2}
\quad(0<\delta\le t\le1).
}
\tag{3.1}
$$
它是实际闭算子的限制，特别 $\mathcal H_{J,t}\subseteq\operatorname{Dom}Z_J$。

**证明。** 重做 R207 指数权附录 §A，但仅对 $J$ 的次数分层。
纯算子 $\sum_{j\in J}a_jS_j$ 的创建、删除、对角三个块仍分别有
$g_J\sqrt{q+1}$、$g_J\sqrt q$、$2g_J\sqrt q$ 的范数界。
选中头 $F$ 只是这些块的恒等放大，不产生头维数因子。
加上指数权后，三个块的范数总和仍至多
$16g_J\delta^{-1/2}$。

真实 carry 的局部级数为
$$
Z_J-\sum_{j\in J}a_jS_j
=\sum_{j\in J}\sum_{L\ge1}a_jB_{j,j+L},
\qquad
\|B_{j,j+L}\|\le18\eta_j\eta_*^{L-1}.
\tag{3.2}
$$
每项只作用 $[j,j+L]$ 的 $L+1$ 位。即使 $F$ 在该区间中有孔，
$\mathcal N_J$ 的局部最大最小值之差仍不超过 $L+1$，所以
$$
\|e^{t\mathcal N_J}B_{j,j+L}e^{-t\mathcal N_J}\|
\le e^{t(L+1)}\|B_{j,j+L}\|.
\tag{3.3}
$$
因此 carry 在每个 $0\le t\le1$ 的同权空间上有界，范数至多
$$
\frac{18e^2}{1-e\eta_*}\sum_{j\in J}|a_j|\eta_j
\le C_Kg_J,\qquad
C_K=\frac{18e^2\|\eta\|_2}{1-e\eta_*}.
\tag{3.4}
$$
可取 $C=16+C_K$；实际参数下也可沿 R241 附录取 $C=17$。

有限柱在每个 $\mathcal H_{J,t}$ 中稠密；用有限柱的加权逼近，
再用实际 $Z_J$ 与输出指数权的闭性延拓 (3.1)。
所以这里没有把散乱位上的形式和当成已识别的最大闭域。证毕。

把 $1\to0$ 分成 $p$ 个等步长，由 (3.1) 逐步付清自然域，
$$
\boxed{\|Z_J^pQ_F\|\le(Cg_J\sqrt p)^p\qquad(p\ge1).}
\tag{3.5}
$$
故
$$
\mathcal E_J(z)Q_F
=\sum_{p\ge0}\frac{z^p}{p!}Z_J^pQ_F
$$
是整个复平面上的算子范数整函数，并有
$$
\boxed{
\|\mathcal E_J(z)Q_F\|
\le\sqrt2\exp(e^2C^2g_J^2|z|^2).
}
\tag{3.6}
$$
例如由 $p!\ge(p/e)^p$，把级数支配为
$\sum(eCg_J|z|)^p/\sqrt{p!}$，再对权 $2^{-p/2}$ 用
Cauchy–Schwarz 即得 (3.6)。

## 4. 任意有限选中头的真实整轨道分解

置
$$
s_F=a_*+\sum_{j\in F}a_j.
$$
实际有
$$
X-s_FI=H_F+Z_{F^c}.
\tag{4.1}
$$
这里没有重新定义 $X$ 的常数项，也没有把任何条件收敛的无穷标量和拆成两份。
严格地，先在共同有限柱核心上使用
$$
X=a_*I+\sum_{j\in F}a_jV_j+X_{\sum_{j\notin F}a_j\chi_j}.
$$
右侧只从原 $\ell^2$ first 中减去有限个系数。有限头是有界算子，
而两个 first 的有限柱都是图核心，所以取闭包即给完整域等式 (4.1)。
例如在参考向量 $1$ 上，$Z_{F^c}1=\sum_{j\notin F}a_j\chi_j$ 始终按 $L^2$ 无条件收敛；
它不被替换成带有重排标量常数的另一个尾算子。
相应的 $-\sum_{j\in F}a_j$ 完整保留在 $H_F1$ 中。
因此后文的幅度排序中心是同一个实际 $X$ 的有限截断预算所逼出的谱约束，
不是给无界 $X$ 另赋一个全空间代数字符。

$H_F$ 有界，属于 $\mathcal A$，保持 $Z_{F^c}$ 的全部自然幂域并作域交换。
对有界交换扰动的逐阶归纳给
$$
\operatorname{Dom}(X-s_FI)^p
=\operatorname{Dom}Z_{F^c}^p.
\tag{4.2}
$$
反向归纳时把已经入域的低阶项从有限二项式中减去即可。
因而在 $Q_FH$ 上，
$$
\mathcal E_F(z)
:=\sum_{p\ge0}\frac{z^p}{p!}(X-s_FI)^pQ_F
=e^{zH_F}\mathcal E_{F^c}(z)Q_F.
\tag{4.3}
$$
(3.5) 和有界头的指数级数使等式两侧都按算子范数整收敛。
本式不把 $\mathcal E_F(z)$ 当成全空间上的有界 $e^{zX}$。

还需要单个真实 Cayley 因子的预算。由
$$
a_j(V_j-I)=-2a_jN_j+2a_jN_j^2(I+N_j)^{-1}
$$
及 $N_j^2=\eta_jN_{j+1}$，偶、奇指数项分别估计得到
$$
\boxed{
\|e^{za_j(V_j-I)}\|
\le(1+2|z a_j|)
 \exp\!\left[|z a_j|(2\sqrt{\eta_j}+6\eta_j)\right].
}
\tag{4.4}
$$
两个有界指数因子交换。定义
$$
\kappa_J=\sum_{j\ge J}|a_j|(2\sqrt{\eta_j}+6\eta_j);
\qquad \kappa_J\longrightarrow0.
\tag{4.5}
$$
这里必须让低物理位的截断 $J$ 随尺度增长，不能把固定的小 $\eta_0$ 乘 $R$ 当成 $o(R)$。

## 5. 最大幅度集加物理前缀：全部普通有限柱最终被保留

现在假设 (1.2) 且支撑无限。取
$$
F_n=A_n\cup\{0,\ldots,n-1\},
\quad
g_n=\|a_{F_n^c}\|_2,
\quad
s_n=a_*+\sum_{j\in F_n}a_j.
\tag{5.1}
$$
这些集合递增，$|F_n|\le2n$，且 $Q_{F_n}\to I$ 强。
增加原物理前缀是为了同时保留零系数位，并保证真正逼近整个 $H$。

令 $G_n^2=\sum_{k>n}r_k^2$。由 (1.2)，
$$
G_n^2\le
\left(\sup_{k>n}kr_k\right)^2\sum_{k>n}k^{-2},
\qquad nG_n^2\longrightarrow0.
\tag{5.2}
$$
因此
$$
t_n:=ng_n^2\longrightarrow0,
\qquad
|s_n-\tau_n|\le\sqrt n\,G_n\longrightarrow0.
\tag{5.3}
$$
每个 $g_n>0$；若某个等于零，原支撑已经有限。

由 (1.2)，存在有限 $b$ 使 $r_k\le b/k$。
对任意至多 $2n$ 个系数和任意 $R>0$，
$$
\begin{aligned}
\sum_{j\in F}\log(1+2R|a_j|)
&\le\sum_{k=1}^{2n}\log(1+2bR/k)\\
&\le 2n\,I(bR/n)\\
&\le2n[\log(1+bR/n)+1],
\end{aligned}
\tag{5.4}
$$
其中
$$
I(v)=\int_0^1\log(1+v/x)\,dx
=(1+v)\log(1+v)-v\log v
\le\log(1+v)+1.
$$
第一步只用递减重排的定义，不能把它误写成原物理坐标上的幅度界。

取
$$
R_n=\frac{n}{\sqrt{t_n}},
\qquad
J_n=\lfloor\sqrt{R_n}\rfloor,
\qquad
F_n^{\rm low}=F_n\cap[0,J_n).
\tag{5.5}
$$
$R_n\to\infty$、$J_n\to\infty$。低物理部分的位数至多 $\sqrt{R_n}$，
故 §2.1 给一致的
$$
\sup_{|z|\le R_n}\log\|e^{zH_{F_n^{\rm low}}}\|=o(R_n).
\tag{5.6}
$$
对其余选中位，使用 (4.4)、(4.5)、(5.4)。
再由 (3.6)、(4.3)，存在显式非负上界 $\Lambda_n$，使
$$
\sup_{|z|\le R_n}\|\mathcal E_{F_n}(z)\|\le e^{\Lambda_n},
\tag{5.7}
$$
其中可取
$$
\Lambda_n=
F^{\rm low}_n
+2n[\log(1+bR_n/n)+1]
+R_n\kappa_{J_n}
+\tfrac12\log2+e^2C^2g_n^2R_n^2.
\tag{5.8}
$$
$F^{\rm low}_n$ 是把 $F_n^{\rm low},R_n$ 代入 (2.6) 的右侧。
分别除以 $R_n$：
$$
\frac{F^{\rm low}_n}{R_n}\to0,\quad
\frac{2n[\log(1+bR_n/n)+1]}{R_n}\to0,\quad
\kappa_{J_n}\to0,\quad
g_n^2R_n=\sqrt{t_n}\to0.
$$
因此
$$
\boxed{\Lambda_n/R_n\longrightarrow0.}
\tag{5.9}
$$

置整数
$$
p_n=\left\lceil\sqrt{R_n(1+\Lambda_n)}\right\rceil.
\tag{5.10}
$$
则 $p_n\to\infty$、$p_n/R_n\to0$、$\Lambda_n/p_n\to0$。
对 (5.7) 用算子值 Cauchy 估计以及 $p_n!\le p_n^{p_n}$，得到
$$
\|(X-s_nI)^{p_n}Q_{F_n}\|^{1/p_n}
\le \frac{p_n}{R_n}\exp(\Lambda_n/p_n)
=:\epsilon_n\longrightarrow0.
\tag{5.11}
$$

实际共轭 $C$ 保持每个 $Q_F$，且 $X^*=CXC$；对自然幂逐次使用该等式，便得到
$$
\boxed{
\|(X^*-\overline{s_n}I)^{p_n}Q_{F_n}\|^{1/p_n}
\le\epsilon_n\longrightarrow0.
}
\tag{5.12}
$$
没有从一次通常伴随同域直接跳到所有高次伴随域；这里的具体 $Q_F$ 向量先由 §3–4 逐次入域，再由共轭运输。

## 6. 同一个未知闭分支上的谱结论

设 $M,B$ 如定理 1.1。对 $v\in\operatorname{Dom}X^*$，真实伴随定义给
$$
P_Mv\in\operatorname{Dom}B^*=M,\qquad
P_MX^*v=B^*P_Mv.
\tag{6.1}
$$
它只用 $M\subseteq\operatorname{Dom}X$、$XM\subset M$；不要求 $M$ 由 $C$ 保持。

当 $s_n\in\rho(B)$ 时，对 (5.12) 的已付清域逐幂迭代 (6.1)，得到
$$
\boxed{
\|P_MQ_{F_n}\|
\le\left[\|(B-s_nI)^{-1}\|\epsilon_n\right]^{p_n}.
}
\tag{6.2}
$$

如果 $(\tau_n)$ 无界，由 (5.3) 可选子列 $|s_n|\to\infty$。
这时预解式范数至多 $(|s_n|-\|B\|)^{-1}$，(6.2) 右侧趋零。
但 $Q_{F_n}\to I$ 强，迫 $P_M=0$，矛盾。

如果 $\tau_{n_\nu}\to s$ 而 $s\notin\sigma(B)$，
则 $s_{n_\nu}$ 的预解式范数一致有界，(6.2) 同样给矛盾。
故每个有限聚点必须属于 $\sigma(B)$。

最后假设 $\sigma(B)$ 有限。前一段已排除 $(\tau_n)$ 无界，故它至少有一个有限聚点 $s$。
对每个 $\lambda\in\sigma(B)$，取 $B$ 的 Riesz 谱子空间 $M_\lambda$。
它是原 $H$ 中的非零闭 $X$ 不变空间，$X|_{M_\lambda}$ 的谱只有 $\lambda$。
对这个真实闭子空间重新使用前一段，即得 $\lambda=s$。
所以 $\sigma(B)=\{s\}$；任何另一个聚点也必须等于 $s$。
有界复数序列只有一个聚点时必收敛，定理 1.1 得证。

若 $a$ 有限支撑，$X\in\mathcal A$ 且 $X-sI$ 拟幂零，
其中 $s=a_*+\sum_j a_j$。它在任何非零 $X$ 不变闭空间上的限制仍拟幂零，
直接得到相同的有限和谱结论。

## 7. 实际多项式与任意 first 指数权

R176 的自然多项式定理给以下已经付清的接口。
对 $q(u)e^w$，R147/R176 将其表示为
$$
B_*P(X)\xi,
$$
其中 $B_*\in\mathcal A$ 为有界单位，$\xi$ 是所有所需自然幂域中的循环向量，
$P$ 是最高系数为单位的有限次多项式，所有系数属于 $\mathcal A$，字符多项式为 $q$。
$P(X)$ 闭、$C$ 自伴；其核若非零，则是闭 $A$ 不变空间，
并且整个核都在 $\operatorname{Dom}X$ 中，$X$ 在该核上有界，且
$$
\sigma(X|_{\ker P(X)})\subseteq\{z:q(z)=0\}.
\tag{7.1}
$$
这是有限谱分支。图循环性还给
$$
[P(X)\xi]_A=\overline{\operatorname{Ran}P(X)}.
$$

若 $\tau_n$ 不收敛到有限数，定理 1.1 排除 (7.1) 的非零核。
若 $\tau_n\to s$ 且 $q(s)\ne0$，(1.3) 同样排除该核。
$C$ 自伴性随后给值域稠密，图循环性和外单位 $B_*$ 给 $q(u)e^w$ 循环。
这完成推论 1.2；没有把“全空间无核”误写成“任意限制上像稠密”。

## 8. 任意置换的慢趋零交替调和行全部保留危险平方循环性

取
$$
\varepsilon_0=1,\qquad
\varepsilon_k>0,\qquad
\varepsilon_k\downarrow0,\qquad
\sum_{k\ge0}\frac{\varepsilon_k}{k+1}=\infty,
$$
并令
$$
c_k=\frac{(-1)^k\varepsilon_k}{k+1}.
\tag{8.1}
$$
幅度 $|c_k|$ 严格递减，且其交替和
$$
s_\varepsilon=\sum_{k\ge0}c_k
$$
满足 $0<s_\varepsilon<1$。

令 $\pi$ 为任意排列 $\mathbb N_0$ 的置换，要求 $\pi(0)=0$，定义
$$
a_j=c_{\pi(j)},\qquad
a_*=0,\qquad u_\pi=\sum_j a_j\chi_j.
\tag{8.2}
$$
这里保留 $a_0=1$，故危险平方的点态应用符合 R208 §7 的前提。
幅度递减排序重新读出的恰是 $c_0,c_1,\ldots$，所以
$$
nr_n\to0,\qquad \tau_n\to s_\varepsilon\in(0,1).
$$
取 $q(z)=z^2-1$，推论给
$$
\boxed{(u_\pi^2-1)e^w\text{ 对每个复 }\ell^2\text{ first }w\text{ 都循环。}}
\tag{8.3}
$$

这允许任意严重的物理位置稀疏化。比如将选定的第 $2^k$ 个原系数放到
远大于 $2^{2^k}$ 的指定位置，其余位置按原顺序填入剩余系数。
原坐标上的 $(j+1)|a_j|$ 可以无界，$m\|a_{\ge m}\|_2^2$ 也可沿子列无界，
而 (8.3) 完全不受影响。

### 8.1 物理顺序的系数和可以恰为碰撞根 1

还有一个更直接的例子。可取
$$
\varepsilon_k=\frac1{\log(k+e)}.
$$
从 $a_0=c_0=1$ 开始，在剩余正项池 $c_2,c_4,\ldots$ 与负项池
$c_1,c_3,\ldots$ 中分别保持原顺序，反复执行：

1. 依次取尚未使用的正项，直到当前部分和严格大于 $1$；
2. 依次取尚未使用的负项，直到当前部分和严格小于 $1$。

两个符号子列都不可和，所以每个有限块都能结束；每轮至少用一项正项及一项负项，
因而全部原项最终都会被用到。最后一项的幅度趋零，故每次越界的过冲趋零，
而块内部分和在相邻越界端点之间单调。因此这确实给一项排列，并满足
$$
\sum_{j=0}^\infty a_j=1
\quad\text{按原物理顺序收敛。}
\tag{8.4}
$$
尽管 (8.4) 恰等于 $q(z)=z^2-1$ 的活动根，幅度排序中心仍为
$s_\varepsilon\in(0,1)$，所以 (8.3) 仍成立。
这说明未经尾预算保证的物理顺序和不能被当作有界分支必取的唯一谱中心。

正、负两类系数都不可和，按 R138 的原谱分类，这些 first 仍属全平面连续谱类。
本稿提供的是新的多项式循环结论，并非把它们改归到空谱 first。

## 9. 仍未覆盖的规范临界行

若 $\varepsilon_k\equiv1$，则 $r_n=1/n$，$nr_n=1$，且
$n\sum_{k>n}r_k^2\to1$。所以本稿的 $t_n\to0$ 机制失效。
任意位集进位预算并未把这个临界量自动变成零。

特别，规范 $a_j=(-1)^j/(j+1)$ 的原 $u^2-1$ 的活动根 $+1$，
仍须接续 R246/R233/R236 的实际未知核与中央零阶逆问题。
这里不由排序不变的次临界结果向 $\varepsilon\equiv1$ 免费取参数极限。

依赖：R125；R161；R176；R207 指数次数权附录 §§A–B；R241 及其常数附录；
R243 指数头附录；R147 的实际加权多项式和图循环接口。

