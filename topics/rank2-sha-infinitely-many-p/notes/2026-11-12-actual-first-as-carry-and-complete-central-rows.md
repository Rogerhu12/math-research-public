# 真实第一 AS 进位、第三层共同消元与完整中央行

日期：2026-11-12。**状态：本文全级数模 $p^2$ 比较、真实第一
AS 缺陷、第三层共同前缀消元和完整中央行接口均已证明。**
第三层是无条件的局部收益；本文另行保留原两个完整中央导数的
消失条件，没有将前者重复计算成 R159 的严格全局收益。

固定惰性素数 $p=4r-1\ge7$，置
$$
 R=r(p-1)=\frac{p^2-1}{4},\qquad w=z^4.
$$
沿用 R167–R177 的实际函数
$$
 a=\vartheta^4,\quad b=\sigma^4,\quad
 U(w)=\sum_{t\ge0}u_t w^{r+Rt},\qquad
 V(w)=w+\sum_{t\ge1}v_t w^{1+Rt}.
 \tag{1}
$$
这里 $U,V$ 是 R174 的同一整环境 Cartan 坐标，不能把它们沿
曲线的高阶系数也直接称为整。记
$$
 g_0=pu_0\in\mathbb Z_p^\times,\qquad
 \tau=\bar g_0,\qquad
 \mathfrak w_p=\frac{(p-1)!+1}{p}\bmod p.
 \tag{2}
$$
最后一个量是 Wilson 商的约化。

## 1. 原加法参数中的两条完整整级数

定义
$$
 \mathcal G(T)=\sum_{t\ge0}p^{1+pt}u_tT^t,\qquad
 \mathcal V(T)=1+\sum_{t\ge1}p^{pt}v_tT^t.
 \tag{3}
$$
于是作为形式恒等式，
$$
 U(w)=\frac{w^r}{p}\mathcal G(w^R/p^p),\qquad
 V(w)=w\mathcal V(w^R/p^p).
 \tag{4}
$$
本篇将直接证明
$$
 \mathcal G\in\mathbb Z_p[[T]],\qquad
 \mathcal V\in1+pT\mathbb Z_p[[T]].
 \tag{5}
$$

R177 中以 $v=V(w)$ 为输出的真实级数满足
$$
 U=\frac{v^r}{p}G(v^R/p^p),\qquad
 G\in\mathbb Z_p[[T]],\qquad
 \bar G+T\bar G^p=\tau.
$$
故准确有
$$
 \boxed{\quad
 \mathcal G(T)=\mathcal V(T)^r
            G\bigl(T\mathcal V(T)^R\bigr).
 \quad}
 \tag{6}
$$
特别是 $\bar{\mathcal G}=\bar G$。下文统一记这条约化为 $H(T)$。

换 $w$ 为 $v$ 保持真实前缀及其首个非零系数，但通常会改变某个
孤立的高阶中央系数。因此完整中央条件必须先写在 (4) 的原
$w=z^4$ 参数中；第 6 节没有省略这个修正。

## 2. 真实解析余项为何在第一进位中全部消失

取 R54 的准确首坏 sigma 常数 $c$，$v_p(c)=-1$，令
$$
 a_0=4c,\qquad \alpha=pa_0\in\mathbb Z_p^\times,\qquad
 \rho=p^{-1/(2p)}.
$$
R54 的参考截面 $S=(x^2+1)\sigma^4$ 及其闭 $\rho$ 盘估计给
$$
 a(w)-b(w)/3=e^{a_0w^r}A(w),\qquad
 b(w)/w=e^{a_0w^r}B(w),
 \tag{7}
$$
其中 $A(0)=B(0)=1$，两余项在该闭盘解析、Gauss 范数至多一。
具体地，原 $s=x^{-2}$ 参数给
$$
 \frac{a-b/3}{S}=\frac{1-s/3}{1+s}.
$$
此外 $a/S=x^2/(x^2+1)$ 是原点附近的整单位，而
$b/(wa)=1/(w x^2)$ 也是范数为一的整解析单位；乘去这些固定
单位正好由 R54 的 $S$ 得到 (7)。因此
$$
 v_p([w^m]A),\ v_p([w^m]B)
                  \ge-\left\lfloor\frac{2m}{p}\right\rfloor.
 \tag{8}
$$
这里使用的是 R54 已证明的较大余项盘，不只用首个 sigma 分母。

考虑 $U$ 的第 $t\ge1$ 个稀疏项，令
$K=1+(p-1)t$。指数只有 $w^{rh}$ 次项，所以相关余项必为
$[w^{rh}]A$，$0\le h\le K$。把它乘以 (3) 的归一化幂后，
其赋值至少为
$$
 h+t-v_p((K-h)!)
       -\left\lfloor\frac{(p+1)h}{2p}\right\rfloor.
 \tag{9}
$$
当 $h=1$ 时，$K-h=(p-1)t>0$，其 $p$ 进数位和至少为 $p-1$，
故 (9) 至少二。对 $h\ge2$，用
$v_p(n!)\le n/(p-1)$，(9) 严格大于一，因为
$$
 \frac{ph-1}{p-1}-\frac{(p+1)h}{2p}
 =\frac{(p^2+1)h-2p}{2p(p-1)}>1.
 \tag{10}
$$
赋值为整数，故也至少二。这已覆盖任意大的 $K,h$。

对 $\mathcal V$，同样取 $K=(p-1)t>0$，相应下界去掉 (10)
分子中的 $2p$。$h\ge2$ 时仍严格大于一；$h=1$ 时
$K-1\equiv-1\bmod p-1$ 的数位和至少 $p-2$，准确给二。
所以两条真实级数的全部正 $t$ 项，模 $p^2$ 都只保留 (7)
余项的常数一。

在 $t=0$ 的 $U$ 项还会保留 $p[w^r]A$；这项整，故
$g_0-\alpha\in p\mathbb Z_p$。它不能被误删，但可准确吸收到
下一节的参数 $g_0$ 中。

## 3. 普适径向指数与实际全级数比较

令 $\lambda^{p-1}=p$，置
$$
 u(\eta)=\sum_{n\equiv1\ (p-1)}\frac{\eta^n}{n!},
 \qquad f_\beta(X)=\lambda^{-1}u(\lambda\beta X)
          =X F_\beta(X^{p-1}).
$$
则
$$
 F_\beta(T)=\sum_{t\ge0}
  \frac{p^t\beta^{1+(p-1)t}}{(1+(p-1)t)!}T^t,\qquad
 V_\beta(T)=\frac{f_\beta'(X)}{\beta}
 =\sum_{t\ge0}\frac{p^t\beta^{(p-1)t}}{((p-1)t)!}T^t.
 \tag{11}
$$
对 $n\equiv1\bmod p-1$，前一系数的赋值为
$(s_p(n)-1)/(p-1)$；后一正系数的赋值为
$s_p(n)/(p-1)\ge1$。所以 $F_\beta$ 整，$V_\beta\in1+pT\mathbb Z_p[[T]]$。

由第 2 节，$\mathcal G$ 的正系数模 $p^2$ 等于 $F_\alpha$ 的
正系数，$\mathcal V\equiv V_\alpha\bmod p^2$。
若 $n>1$、$n\equiv1\bmod p-1$，则
$$
 v_p\!\left(n\,\frac{p^{(n-1)/(p-1)}}{n!}\right)\ge1:
$$
若 $p\mid n$ 由 $n$ 支付；否则 $s_p(n)\ge p$。
所以这些正系数对 $\beta$ 的导数都被 $p$ 除。
$V_\beta$ 的正系数也有此性质。因此以
$g_0\equiv\alpha\bmod p$ 替换参数，得到完整恒等比较
$$
 \boxed{\quad
 \mathcal G\equiv F_{g_0}\pmod{p^2},\qquad
 \mathcal V\equiv V_{g_0}\pmod{p^2}.
 \quad}
 \tag{12}
$$
第一式的常数项也完全相等。特别，(5) 已由原 theta 系数证明，
不是从自由选择一个 Artin–Schreier 提升得到。

### 3.1 径向 $[p]$ 的两项与 Wilson 商

级数
$$
 \upsilon(x)=u(\log(1+x))
 =\frac1{p-1}\sum_{\zeta\in\mu_{p-1}}
       \zeta^{-1}\bigl((1+x)^\zeta-1\bigr)
$$
属于 $x+x^2\mathbb Z_p[[x]]$，有整形式逆。因此
$$
 [p]_u(U)=u(pu^{-1}(U))
   =pU+c_1U^p+c_2U^{2p-1}+\cdots
                     \in\mathbb Z_p[[U]].
 \tag{13}
$$
有限角色使支撑恰在 $1\bmod p-1$。直接反演到 $2p-1$ 给
$$
 c_1=\frac{p^p-p}{p!},\qquad
 c_2=\frac{p^2-p^{p+1}}{(p!)^2}
       +\frac{p^{2p-1}-p}{(2p-1)!}.
 \tag{14}
$$
Wilson 定理逐余数块给
$$
 c_1\equiv1\pmod p,\qquad
 \frac{c_1-1}{p}\equiv\mathfrak w_p\pmod p,\qquad
 c_2\equiv0\pmod p.
 \tag{15}
$$
最后一式中两项最低层分别是 $1$、$-1$，确实相消。

把 $U=\lambda f_\beta(X)$ 代入 (13)，除以 $p\lambda$：
$$
 f_\beta+c_1 f_\beta^p
       +p c_2 f_\beta^{2p-1}+\cdots=f_\beta(pX)/p.
$$
所有更高项至少含 $p^2$；右侧模 $p^2$ 准确为 $\beta X$。
故
$$
 \frac{f_\beta+f_\beta^p-\beta X}{p}
       \equiv-\mathfrak w_p\bar f_\beta^p\pmod p.
 \tag{16}
$$
对上一模 $p^2$ 等式微分，还得到
$$
 \frac{f_\beta'/\beta-1}{p}
                         \equiv-\bar f_\beta^{p-1}\pmod p.
 \tag{17}
$$
所有微分均对整系数形式级数逐系数进行，不会损失模数。

## 4. 两个实际缺陷的全 $T$ 闭式

定义
$$
 \mathcal W=(\mathcal V-1)/p,\qquad
 \mathcal E=\frac{\mathcal G+T\mathcal G^p-g_0}{p},\qquad
 E=\frac{G+TG^p-g_0}{p}.
 \tag{18}
$$
由 (12)、(16)、(17)，
$$
 \boxed{\quad
 \bar{\mathcal W}=-T H^{p-1},\qquad
 \bar{\mathcal E}=-\mathfrak w_p T H^p.
 \quad}
 \tag{19}
$$
原输出和 Cartan 输出的两个缺陷不同。将 (6) 展开到模 $p^2$，
并用 $R\equiv-r\bmod p$，得到
$$
 \bar{\mathcal E}=\bar E
       +r\bar{\mathcal W}(H-TH').
$$
微分 $H+TH^p=\tau$ 给 $H'=-H^p$，所以 $H-TH'=\tau$。
于是 R179 的真实缺陷准确为
$$
 \boxed{\quad
 \bar E=-\mathfrak w_p T H^p+r\tau T H^{p-1}
       =(\tau-H)\left(\frac{r\tau}{H}-\mathfrak w_p\right).
 \quad}
 \tag{20}
$$
这些是全部系数的等式。尤其不能只检查 $[T]E$ 后，把其他项
视为任意或零。也没有假设 Wilson 商非零。

## 5. 第三个真正的共同前缀层

在 R179 的原有限源上，固定 $(\alpha_1,j)$，
$1\le\alpha_1\le p-1$、$0\le j<r$，记
$$
 k=r\{\alpha_1+(p-1)t\}+j,\quad
 e=\alpha_1+pt,\quad
 \mathcal B_t=p^e[v^k]P(\gamma_v).
$$
所有 $L_{i,l}$ 都来自同一个原源的整 Cartan 逆。
置 $q=T G^{p-1}$，它是首项单位的整参数。
R179 的全深共同式准确给
$$
 \frac{\sum_{t\ge0}\mathcal B_tT^t}{G^{\alpha_1}}
 =\sum_{\substack{b,s\ge0\\i=\alpha_1+(p-1)b-s\ge0}}
           p^{b+s}q^bG^{-s}L_{i,j+rs}.
 \tag{21}
$$
若 $i=0$，原系数条件仍自动保留；(21) 在任意固定模 $p^N$
下只用 $b+s<N$ 的有限项。

记 $\mathfrak w_p$ 在 $\mathbb Z_p$ 中任取提升。由 (20)，
$$
 G^{-1}\equiv g_0^{-1}(1+q)
      -p\tau^{-1}q(r-\mathfrak w_p+rq)\pmod{p^2}.
 \tag{22}
$$
其中乘 $p$ 的系数只须在剩余域解释。保留 (21) 的
$b+s\le2$ 后，分别是
$$
 L_{\alpha_1,j}
 +p\{G^{-1}L_{\alpha_1-1,j+r}
                         +qL_{\alpha_1+p-1,j}\}
$$
以及
$$
 p^2\{G^{-2}L_{\alpha_1-2,j+2r}
     +qG^{-1}L_{\alpha_1+p-2,j+r}
     +q^2L_{\alpha_1+2p-2,j}\}.
 \tag{23}
$$
负的第一个指标约定该项为零。代入 (22)，整个式子模 $p^3$
是 $q$ 的次数至多二的多项式。

若原 $P$ 在目标 $k$ 以前的全部真实 jet 为零，且 $t\ge3$，
则同余数的 $t=0,1,2$ 三行当然准确为零。
除去共同整单位 $G^{\alpha_1}$、再用整参数 $q$，其前三系数
仍为零。因此 (23) 的全部多项式系数都被 $p^3$ 除，
进而原 $\mathcal B_t(P)\in p^3\mathbb Z_p$。结合 R179：
$$
 \boxed{\quad
 v_p([v^k]P(\gamma_v))\ge-e+\min(t,3).
 \quad}
 \tag{24}
$$
这使用全部原列和同一个准确前缀，没有逐列调整参数。
因为首系数在 $v(w)=w+\cdots$ 下不变，(24) 也是真实 $w$ jet
的前缀范数界。

即使类似的收益增长为 $O(t)$，其量级仍是 $O(k/p^2)$；
跨素数求和只产生 $O(k)$ 项。因此 (24) 本身不能改变
R159 的 $k\log k$ 主系数，更不能冒充原两个中央条件已经支付。

## 6. 原 $w$ 系数的完整共同矩阵

由 (4)，原 $w$ 的归一化行是
$$
 \begin{aligned}
 \mathcal B^w_{t,\alpha_1,j}
 ={}&\sum_{b=0}^{t}
       \sum_{s=0}^{\alpha_1+(p-1)b}
 p^{b+s}[T^{t-b}]
   \mathcal G^{\alpha_1+(p-1)b-s}
   \mathcal V^{j+rs}
   L_{\alpha_1+(p-1)b-s,j+rs}\\
 &+\mathbf1_{\alpha_1=p-1}\,
       p^{-1}[T^{t+1}]\mathcal V^j\,L_{0,j}.
 \end{aligned}
 \tag{25}
$$
第二行是必要端点：它对应重标中的 $b=-1,i=s=0$。
它因 (5) 而整，在中央余数 $j=0$ 时准确为零。
除此之外，对固定精度仍只用同一个有限 $L$ 集合。
不能将 $i=0$ 的 $\mathcal V^l$ 当成常数；R179 在 $v$ 参数中
没有这个问题，而单个高中央系数必须使用 (25)。

## 7. 两个完整中央导数给所有深度的准确条件

现在只取实际两个线性坐标
$$
 F=\mathcal A=A_2\quad\hbox{或}\quad F=\mathcal B=B.
$$
它们具有同一 theta 次数 $68$，且在原加法参数中从 $z^4$
开始。令 $a_*=68c$。与 R54 相同的整前因子及闭 $\rho$ 盘
证明给
$$
 F=e^{a_*z^{p+1}}F_{\rm res},\qquad
 \|F_{\rm res}\|_\rho\le\rho^4,
$$
以及真正解析函数
$$
 J_F(k)=k!a_*^{-k}[w^{rk}]F\quad(k\in\mathbb Z_{\ge0}),
 \qquad
 J_F-J_F'(0)u\in p^2u^2\mathbb Z_p\langle u\rangle.
 \tag{26}
$$
这里 $J_F(0)=0$。例如 $\mathcal A=A_1(2z)/16$ 时，
$J_{\mathcal A}(u)=16^{-1}(2^{p-1})^uJ_{A_1}(u)$，
所以其完整导数只是原导数的单位倍；没有改动目标的零性。
$\mathcal B$ 直接使用相同次数 $68$ 的已认证截面。

置
$$
 t_n=\frac{p^n-1}{p-1},\qquad
 e_n=1+pt_n=p^n+v_p((p^n)!).
$$
两截面使用同一个明确单位
$$
 \epsilon_{p,n}
       =\frac{p^{e_n}a_*^{p^n}}{(p^n)!}\in\mathbb Z_p^\times.
$$
准确插值为
$$
 \boxed{\quad
 \mathcal B^w_{t_n,1,0}(F)
   =p^{e_n}[w^{rp^n}]F
   =\epsilon_{p,n}J_F(p^n).
 \quad}
 \tag{27}
$$
从而
$$
 \boxed{\quad
 J_F'(0)=0
 \quad\Longleftrightarrow\quad
 \mathcal B^w_{t_n,1,0}(F)\in p^{2n+2}\mathbb Z_p
                         \quad\hbox{对全部 }n\ge0.
 \quad}
 \tag{28}
$$
正向由 (26)；反向将 (27) 除以 $p^n$ 并令 $n\to\infty$。
这保留了原完整导数条件，而非仅其首权必要条件。
同一式适用于两个线性坐标的任意整线性组合；
本文没有把它作用于高次乘积列。

## 8. 下一中央条件的真实轴形式

对质量为零、$ab$ 齐次次数 $d\in\mathbb Z_p^\times$ 的原 $F$，
置
$$
 c_F=L_{0,r}(F)=[w^r]F,\qquad d_F=L_{0,2r}(F).
$$
假设 $c_F\in p\mathbb Z_p$。R175 的两条完整轴式准确给
$$
 L_{p-1,r}
       =\frac{d^{p-1}-r}{(p-1)!}\,c_F,\qquad
 L_{p-2,2r}
       =\frac{d^{p-2}d_F+r\kappa_pc_F}{(p-2)!}.
 \tag{29}
$$
在 (25) 取 $t=\alpha_1=1,j=0$。所有 $L_{h,0}$ 为零，
所以模 $p^4$ 只剩
$$
 p\,r[T]\mathcal V\,c_F
 +p^2g_0^{p-1}L_{p-1,r}
 +p^3g_0^{p-2}L_{p-2,2r}.
 \tag{30}
$$
由 (19)，$[T]\mathcal V/p\equiv-1$；再用
$(p-1)!\equiv-1$、$(p-2)!\equiv1$，得到
$$
 \boxed{\quad
 \frac{\mathcal B^w_{1,1,0}(F)}{p^3}
       \equiv-\frac{c_F}{p}+\frac{d_F}{d\tau}\pmod p.
 \quad}
 \tag{31}
$$
左边整性也由 (30) 同时给出。

因此原两个完整中央导数同时消失，确实在两个原线性坐标上给
$$
 \boxed{\qquad
 c_F\in p\mathbb Z_p,\qquad
 d_F\equiv17\tau\,c_F/p\pmod p
 \qquad(F=A_2,B).
 \qquad}
 \tag{32}
$$
这里 $d_F=[w^{2r}]F-17u_0[w^r]F$ 是真实 Cartan 轴系数。
它整，不能把右边两项分别假定为整后消去共同首极。
(32) 是从完整深度 $n=0,1$ 得到的额外约束；并没有说
$[w^{2r}]F$ 或高次乘积的中央值自动为零。

## 9. 精度、范围及有限校准

本篇的无条件第三层 (24)，与有条件的全深 (28)/(32)，是不同
输入。下一步若要获得 R159 的严格预算，仍须把 (28) 在原两个
线性坐标上的全部稀疏条件转成同一个有限次数源的充分累计收益；
本篇没有证明这项全阶结论。

尤其，以低总阶 Euler 式构造第二个合流 Vandermonde 门时，
其自然范围 $2D\le p-1$、目标前缀 $2rD$ 可能已经没有非零原核。
不能把空核上的模数改善计作新的中央收益。本文保留 (31)–(32)
这个真实非空线性数据接口，不据此宣称已经得到另一段严格预算。

[独立有限证书](../scripts/check-actual-first-as-carry.py)
使用真正 $t(s)$、第一类周期 $w=s\mathcal L^4$、
Cartan 角色投影和实际逆级数，不用 (19)–(20) 构造测试数据。
它只复用 R177 已有的 $p=7,t\le8$、$p=11,t\le3$ 范围，
另检查 (31) 的一个真实线性组合及所述两个临界前缀的秩。
全部检查通过。$p=7$ 的组合 $B-3A_2$ 与 $p=11$ 的组合
$B-A_2$ 都满足首个 $c_F\in p$ 条件，但 (31) 的值分别为
$5\bmod7$、$9\bmod11$，表明下一轴条件并非首条件的形式重述。
两个临界前缀则分别在行 $9$、$20$ 已满秩，目标 $12$、$30$
处确实没有非零核。
一般等式的依据是上面的全系数估计和整形式群计算。

## 依赖

- [R54 的较大余项盘](2026-11-12-inert-half-factor-first-layer.md)；
  [R54 结果与完整半因子](../results/R54-inert-analytic-half-factor-and-central-slope.md)。
- [R174：真实整 Cartan](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)。
- [R175：完整径向轴及第二带](2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
- [R177：全深 AS 约化](2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)。
- [R179：完整共同核及两层消元](2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R159：实际次数敏感的全局门槛](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)。
