# R612 — 原完整来源的带权物理核、真实单位子式与结点的固定出口

日期：2026-11-14。**状态：已证明。**

本篇把 R607 的同一个首 $p^2$ 有限整目标用于整个原
$G_0\mathcal W_D$，保留原固定乘子、全部十九角和次数帽。
其模 $p$ 核准确等于原多项式格在 $(t,Y)=(0,1)$ 的一个显示带权理想：
权为 $(6,1)$，阈值为 $p-78$，其中 $78$ 正是原 $w^{13}$ 的成本。
这不是把局部完成环当成来源。

由原各列的首 $t$ 阶还得到全 $\mathcal W_D$ 的实际单位方阵，
以及同一个完整真前缀的空区间。
对 R597 的 $r=1,\nu=2,c=3$ 结点，
进一步给出任意同格 $R,T$ 都不能改变的两条实际高行；
其中较早的一条恰在 $\ell=2$ 原目标之后。
本篇不将后一条误作新的非空饱和层，
也不由完整大目标中的饱和推断旧三块的 $d_2$。

## 1. 原来源和同一个完整有限目标

固定原好惰性范围
$$
p=6s-1>101,
$$
以及 R335/R434 的同一规范
$$
Y=\mathscr R,\qquad
\mathscr R(w)=g(w)\exp\!\left(\frac a p w^s\right),
\qquad a\in\mathcal O^\times,\quad g(0)=1.
\tag{1}
$$
保原 $t(w)=\tau_0w+O(w^2)$，$\tau_0\in\mathcal O^\times$；
在 R434 的单位尺度中 $\tau_0=-1$。
已付 $b=17$ 与共同模型的单位换参不改变下面任何带权理想或整性。

仍取
$$
\mathcal W_D=
\bigoplus_{n=0}^D Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,
$$
$$
f_n=\left\lfloor\frac{9n}{2}\right\rfloor+4,\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{2}
$$
完整实际来源是
$$
\Phi(P)=G_0P(t,\mathscr R),\qquad
G_0=Y^{40}h_0(t),
$$
且同一个原整单位分解为
$$
\boxed{
\Phi(P)=c_*w^{13}U_0(w)
 \exp(40a\epsilon)\,
 P(t(w),g(w)\exp(a\epsilon)),
\quad \epsilon=w^s/p.}
\tag{3}
$$
$h_0$、$c_*$、$U_0$ 全来自原 $P_{134}$，
$c_*U_0(0)$ 为单位；不替换其完整高尾。

使用 R607 的同一个实际物理窗口 $0\le j<ps$：
$$
\mathcal C_p
=\bigoplus_{0\le j<ps}\mathcal O\,
 p^{-\lfloor6j/p\rfloor}w^j.
\tag{4}
$$
其真实环表示为
$$
\mathcal C_p=
\mathcal O[w,\epsilon,\upsilon]/
(w^s-p\epsilon,\epsilon^6-w\upsilon,
 w^{s-1}\epsilon^5-p\upsilon,\upsilon^s).
\tag{5}
$$
以下记实际评价为
$$
\mathscr M^{\rm full}_{p,D}:\mathcal W_D\longrightarrow\mathcal C_p,
\qquad P\longmapsto\Phi(P)\bmod w^{ps}.
\tag{6}
$$
它和原三块 $M$ 使用同一来源及同一 $G_0$；
区别仅为这里读取一个更长的、已经付清的整目标。

### 1.1 全原 canonical 列确实在此整目标中

这一步不能仅从来源有限自由推断。
R588 的同一实际 sigma 给
$$
H_\sigma=\frac{\sigma}{z\exp(cz^{p+1})},\quad
H_\sigma^{\pm1},\quad z^2x,\quad -z^3y
\in\mathbf C_p\langle z/\rho\rangle,\qquad
\rho=p^{-1/(2p)},
\tag{7}
$$
所用单位的 Gauss 范数为一。
于是 $t/w$、$g$、固定 $U_0$ 及每个
$q_n(t)/t^{A_n}$ 都是在同一盘上的实际单位，范数为一。
固定 $h_0/t^{13}$ 的单位性和整数系数仍用原好素数范围。
因此每一基列去掉其 Gaussian 后的普通部分
$H(w)=\sum h_jw^j$ 满足
$$
v_p(h_j)\ge-\left\lfloor\frac{3j}{p}\right\rfloor.
\tag{8}
$$
这保所有角、固定乘子和任意 $D$，不是仅对 $S,T$ 的估计。

若 $j=Qs+r$，$0\le r<s$，则 $Q\ge1$ 时
$$
3j=3Qs+3r<(6s-1)Q=pQ.
\tag{9}
$$
在 $H(w)\exp(\gamma w^s/p)$ 的第 $j$ 行，
Gaussian 项数均小于 $p$，其阶乘是单位。
对第 $L\le Q$ 项乘 $p^Q$ 后，
$Q-L\ge1$ 的普通剩余阶由 (8)–(9) 至少多一个 $p$；
$L=Q$ 时普通阶 $r<s$，系数整。
因此每条实际列先属于原
$\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p)$，
从而属于 (4)，并且模 $p$ 在旧目标中准确为
$$
\left(\sum_{r<s}\bar h_rw^r\right)
 \sum_{L=0}^{p-1}\frac{\bar\gamma^L}{L!}\epsilon^L .
\tag{10}
$$
进入 (4) 时，R607 的额外一阶缩放恰杀掉
$6r+L\ge p$ 的项，除此以外没有删尾。

## 2. 完整物理核是固定的带权消失条件

R607 已证明旧 $\overline{\mathcal A}_p$ 到
$\overline{\mathcal C}_p$ 的核是权 $6r+i\ge p$ 的单项式理想。
故其像是实际子环
$$
\mathcal B_\theta
=k[w,\epsilon]/I_p(w,\epsilon),\qquad
I_m(u,v):=\langle u^rv^i:6r+i\ge m\rangle.
\tag{11}
$$
本篇不重新证明该目标表示；新增的是它与原完整来源的准确识别。

令 $v=Y-1$。由 (10)，原评价在 (11) 中为
$$
t\longmapsto\bar t(w),\qquad
v\longmapsto
\bar g(w)\sum_{i=0}^{p-1}\frac{a^i\epsilon^i}{i!}-1.
\tag{12}
$$
其首带权项分别为 $\tau_0w$ 和 $a\epsilon$。
其余项的权分别严格大于六和一。
所以 (12) 是两个同一带权 Artin 环之间的同构：
$$
\boxed{
k[t,v]/I_p(t,v)\ \xrightarrow{\ \sim\ }\ \mathcal B_\theta.}
\tag{13}
$$
可逐带权阶用两个首项单位构造逆。
等价地，先以普通整逆解 $w=w(t)$，
再用次数小于 $p$ 的有限 $\log$ 解 $\epsilon$；
所用 $1,\ldots,p-1$ 均为单位。
这证明同构而非只比较维数。

原 $U_0e^{40a\epsilon}$ 是 (11) 中的单位。
$w^{13}$ 则不能删除：其乘法核准确为
$I_{p-78}/I_p$。同时 $t^{13}/w^{13}$ 是单位。
因此得到：

**定理 1（整个原来源的准确物理核）。**
令 $c_D=C_D$，则
$$
\boxed{
\ker\overline{\mathscr M}^{\rm full}_{p,D}
=
\left\{\bar P\in\overline{\mathcal W}_D:
d^{c_D}\bar P\in I_{p-78}(t,Y-1)\right\}.}
\tag{14}
$$
右边是原多项式格与显示理想的交，
所有十九角和原次数帽仍由 $d^{c_D}\overline{\mathcal W}_D$ 支付。
没有把满足局部条件的任意多项式加入来源。
$d(0)=1$，所以清除这个原共同分母不改变带权消失阶。

(14) 也给一个不含原 theta 高系数的准确有限算法：
在同一个清分母原基上读取
$$
[t^r(Y-1)^i]\,d^{c_D}P,\qquad 6r+i<p-78.
\tag{15}
$$
其核就是 (6) 的模 $p$ 核。
这是原物理评价后的核识别，不是来源端的自由性声明。
但它只针对 (6)，不把旧三块的核换成 (14)。

## 3. 全原格的显示单位方阵

置
$$
b_n=A_n+e_{n+1}
=f_n-2A_n-B_n+C_n,\qquad
N_D=\sum_{n=0}^D(e_{n+1}+1).
$$
对 $0\le r\le b_D$ 定义真实列集合
$$
\mathcal I_r=\{0\le n\le D:A_n\le r\le b_n\},
\qquad m_r=|\mathcal I_r|.
\tag{16}
$$
第 $r$ 组的列恰为
$Y^nq_nt^{r-A_n}$，$n\in\mathcal I_r$；
故 $\sum_rm_r=N_D$。

$b_n$ 严格递增。由其 floor 公式，单步差至少一。
若 $\mathcal I_r$ 非空，
$$
m_r-1\le b_D-r.
\tag{17}
$$
确实从最小的允许 $n$ 到 $D$ 的个数，
被严格递增的 $b_n$ 所控制。

现假定
$$
\boxed{p>6(b_D+13).}
\tag{18}
$$
原行取
$$
j(r,h)=hs+13+r,\qquad
0\le r\le b_D,\quad0\le h<m_r,
$$
$$
\boxed{\Lambda_{r,h}=p^h h!\,[w^{j(r,h)}].}
\tag{19}
$$
由 (17)，
$$
6(13+r)+h\le6(b_D+13)<p.
$$
故 $13+r<s$、$h<p$，所有行互不重复，
均在 $0\le j<ps$，而且 (4) 的缩放指数恰为 $h$。
所以 (19) 是整个实际目标上的整泛函。

按 $r$ 排列行列。
列首普通阶大于 $13+r$ 时，(10) 给该块严格为零。
在同一个 $r$ 对角块中，第 $n$ 列首系数为单位
$$
\eta_{n,r}=c_*U_0(0)\tau_0^r
             7^{A_n}(-1)^{B_n}.
$$
总 Gaussian charge 仍是 $n+40$，
因此其第 $h$ 个原行模 $p$ 准确为
$$
\eta_{n,r}\{a(n+40)\}^{h}.
\tag{20}
$$
对角块是原不同整数 $n$ 的 Vandermonde。
(18) 保 $D<p$；节点即便有一个为零也不影响差的单位性。
整个方阵 $\mathcal V_D$ 的行列式为
$$
\boxed{
\det\mathcal V_D\equiv
\prod_{r:m_r>0}
\left[
\left(\prod_{n\in\mathcal I_r}\eta_{n,r}\right)
a^{\binom{m_r}{2}}
\prod_{\substack{n<n'\\n,n'\in\mathcal I_r}}(n'-n)
\right]\not\equiv0\pmod p.}
\tag{21}
$$

**定理 2。**
在 (18) 下，(6) 是像为 $p$ 饱和的整单射，
且 $\mathcal V_D\in{\rm GL}_{N_D}(\mathcal O)$。
对任意原系数向量 $c=(c_{n,k})$，
$$
\boxed{
\max_{n,k}|c_{n,k}|_p
=\max_{r,h}|\Lambda_{r,h}(\Phi(P))|_p.}
\tag{22}
$$
证明是 (21) 的实际单位逆；并非从来源自由推评价饱和。
原 $P_{134}/U_0$、十三行及 charge 四十全在 (19)–(21) 中。

若去掉 (19) 的行缩放，
所选方阵的行列式赋值准确为
$$
-\sum_r\binom{m_r}{2}.
\tag{23}
$$
(23) 不是连续饱和旗标的成本，见下一节。

## 4. 真前缀的准确空界与特征零接触

令
$$
K^{\rm can}_{D,k}
=\{P\in\mathcal W_D:
[w^j]\Phi(P)=0\ \text{对所有 }0\le j<k\},
$$
$$
J_D(p)=\max_{r:m_r>0}\{s(m_r-1)+13+r\}.
\tag{24}
$$
这是原全部连续行，不是仅选 (19) 的替代核。
(21) 立即给
$$
\boxed{K^{\rm can}_{D,J_D(p)+1}=0.}
\tag{25}
$$
更一般，其秩至多是 $N_D$ 减去
$j(r,h)<k$ 的实际选定行数。

取辅助好惰性素数 $p_D>6(b_D+13)$，
则上述有理矩阵在特征零也非奇异。
沿用 R604 已付的固定模六素数定理选择，
可令 $p_D=(25+o(1))D$。因为
$$
b_D=\frac{25}{6}D+O(1),\qquad
\max_rm_r=\frac{47}{50}D+O(1),
$$
所以整个原 canonical 格的最大非零接触满足
$$
\boxed{
N_D+12\ \le\
\max_{0\ne P}\operatorname{ord}_{w=0}\Phi(P)
\ \le\ \left(\frac{47}{12}+o(1)\right)D^2,
\quad N_D=\frac{47}{24}D^2+O(D).}
\tag{26}
$$
左边是全部列共有 $w^{13}$ 后的维数论；
右边来自同一真正非奇异物理方阵。
$\max m_r$ 的主项直接由
$\frac{6r}{25}+O(1)\le n\le\min(D,4r+O(1))$
得到，峰值在 $r=D/4+O(1)$。

本节仅将非连续单位行用于证明真前缀为空。
不把 (23) 替换成连续旗标的范数成本，
也不把整个九来源格赋成 (26) 的二次接触。
R604 的 $D=1$ 反例继续说明这两类成本不能互换。

## 5. 原帽内的 charge 返回及完整边界

在 (11) 上，裸 $\partial_\epsilon$ 不保持截断理想；
而
$$
\boxed{\mathscr L=\frac{\bar t(w)}a\,\partial_\epsilon}
\tag{27}
$$
保持它，因为每项至少把带权次数提高五。
有限 exponential 的末项准确满足
$$
\partial_\epsilon e_{an}
=an\,e_{an}+(an)^p\epsilon^{p-1}.
$$
乘 $t$ 后末项为零，
因为 $6+(p-1)\ge p$。
因此在整个实际纯 theta 子环上
$$
\boxed{
\mathscr L\,\overline{\mathscr M}^{\rm full}(P)
=
\overline{\mathscr M}^{\rm full}\bigl(t(\mathcal E+40)P\bigr).}
\tag{28}
$$
这里右边必须确实属于所用来源。

具体地，对 $n=0,\ldots,D$ 各系数帽减一，
得到同一原格的余维 $D+1$ 子格
$\mathcal W_D^-$。有真正整来源返回
$$
t(\mathcal E+40):\mathcal W_D^-\longrightarrow\mathcal W_D.
\tag{29}
$$
不增加 theta charge，也不新增角；
代价是显示的原系数帽损失，不是零成本。

对整个 $\mathcal W_D$，写
$P=\sum Y^nq_n f_n$、
$c_n=[t^{e_{n+1}}]f_n$。
准确边界为
$$
\mathcal T_DP=
t(\mathcal E+40)P-
\sum_{n=0}^D(n+40)c_nY^nq_nt^{e_{n+1}+1}
\in\mathcal W_D.
\tag{30}
$$
所以 (28) 的源像缺口由这 $D+1$ 个指定外边界列完全表示，
每个系数均由同一个 $P$ 的实际顶项给出。
这些外边界列没有被加入来源。
相应边界算子秩至多 $D+1$，
不声称它们在实际目标中独立或能任意支付 forcing。

同样，(14) 的实际核只在满足 (29) 的来源上具有该返回稳定性。
没有由 (27) 宣称原整个有限来源像稳定。

## 6. 投回旧三块时不能删除的边界

原目标是 (5) 的真正商：
$$
\mathcal C_p\longrightarrow
\Gamma_{L+13}
=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2),
\qquad \upsilon\longmapsto0.
\tag{31}
$$
(6) 经此商恰为原 $M=c_*U_0m_{13}J$。
同一 $P+pR+p^2T$ 在两目标间保持，
没有换另一份修正或取消两条十三行。

然而 (27) 不能在 (31) 上下降：
它把被杀的 $w^{\ell+13}\epsilon^2$
送到
$2t\,w^{\ell+13}\epsilon/a$，
在 $\ell+14<s$ 时仍是原第二块中的非零向量。
在边界 $\ell+14=s$ 时，
$\epsilon^3$ 的像 $3t\epsilon^2/a$ 仍是第三块非零向量。
对本线 $\ell\le2$、$p>101$，
至少上述一个具体边界保留；
较大的 $p$ 下第一个直接非零。

剥单位和原 $m_{13}$ 后，相对三块也有同一问题：
$w^\ell\epsilon^2$ 的像是
$2t\,w^\ell\epsilon/a\ne0$。
因此完整大目标中的核识别、列饱和和 (28)，
均不能代替 R597 的两个同源像条件。
特别不能先投旧三块，再以裸 charge 导数证明首核或第二余类稳定。

## 7. 同一结点的固定高行与真正出口

现在取 R597/R603 的同一
$r=1,\nu=2,c=3$ 原候选及整临界基准。
仍记
$$
P=P^{\rm crit},\quad
B=(\mathcal E^2P)|_{\psi_+}=w^2b,\quad b_*=b(0)\in\mathcal O^\times,
$$
$$
C=(\mathcal E^3P)|_{\psi_+}=c_1w+O(w^2),
\quad c_1\in\mathcal O^\times.
\tag{32}
$$
$\bar P=t\bar f$，$\bar f(0,1+v)$ 在 $v=0$ 恰有三重根。
所以在 (14) 的带权坐标中
$$
\operatorname{ord}_{(6,1)}\bar P=9,
\qquad
\operatorname{ord}_{(6,1)}
 \overline{\mathscr M}^{\rm full}(P)=87.
\tag{33}
$$
这份准确首权不是由新的局部来源代替原 $P$ 得到的。

对任意同一原格中的
$$
Q=P+pR+p^2T
$$
乃至任意更高整提升，
(6) 的整性使其模 $p$ 像仍是同一个 $\bar P$。
由 R597 的约化普通读数
$\bar P|_{\bar g}=0\bmod w^s$、
$(\mathcal E\bar P)|_{\bar g}=0\bmod w^s$，
以及 $g/\psi_+=\exp(\eta_0)$、$\operatorname{ord}\eta_0\ge s-2$，
有两条准确实际行：
$$
\boxed{
p^2[w^{2s+15}]\Phi(Q)
\equiv c_*U_0(0)\frac{a^2b_*}{2}\not\equiv0\pmod p,}
\tag{34}
$$
$$
\boxed{
p^3[w^{3s+14}]\Phi(Q)
\equiv c_*U_0(0)\frac{a^3c_1}{6}\not\equiv0\pmod p.}
\tag{35}
$$
两行分别有带权 $92$、$87$，均小于 $p$。
因此其 R607 缩放指数正是二、三。
原总 charge 四十在 (34) 的额外
$80P_1+1600P_0$ 中、在 (35) 的额外
$120P_2+4800P_1+64000P_0$ 中：
所读径向阶分别为二和一，
这些额外项全由原消失阶严格杀掉。
$U_0$ 的非恒定部分同样不能降低这些准确首阶。
这逐项支付了 (34)–(35)，而非删除原共同乘子后读取环境行。

(35) 中的三次系数还可直接由 (33) 的
$t v^3$ 单位项读出。
任意 $pR,p^2T$ 在 (4) 的正规化行中均多一个 $p$，
所以不能改变这两个模 $p$ 值。

较早的是 (34)，因为 $s>1$。
因此这整个原余类中不存在达到
$2s+16$ 的真正全前缀：
$$
\boxed{
Q\equiv\bar P\pmod p
\quad\Longrightarrow\quad
Q\notin K^{\rm can}_{D,\,2s+16}.}
\tag{36}
$$
若该余类有真正前缀达到 $2s+15$，
其下一原行就准确有赋值 $-2$；
这只是对存在的真前缀的条件性 sharp 读数，
不另外宣称这种前缀已经存在。

当 $\ell=2$ 时，原 $M$ 的物理窗口
长 $L+13=2s+15$，最后读取 $2s+14$。
所以 (34) 恰在它之后。
当 $\ell=1$ 时它比窗口长再多一行。
这解释为什么上述确定单位与
R597 的截止内 $p^3$ 可提升性不矛盾：
它们没有落在那个旧目标中。

尤其 (35) 不可再算作新的非空饱和层，
因为 (34) 已使该余类的更长真前缀为空。
本篇没有从“最终必有一条高行单位”推出原中央导数非零，
也没有把两条高行当成当前 $d_2$ 的左证书。

## 8. 已付结论与仍需支付的全长 forcing

本篇给出的新实际约束是 (14) 的全来源物理核、
(21) 的原列单位子式、(28)–(30) 的精确帽边界，
以及同一结点任意整修正都保留的 (34)–(36)。
这些全部使用原 $G_0\mathcal W_D$，没有增加来源。

旧三块中的首强迫、两条十三行和第二代表仍须用
R593/R597 的同一个 $R$ 与其真正余核。
完整大目标的源像饱和不保证其商 (31) 中的像饱和。
特别，(34) 已位于旧窗口之外，
不能用它替代尚未付的截止内非零判定。

三条原完整算术中央及原 $\Sha[p^\infty]$ 主目标继续保持；
本篇不赋任意乘积、角函数或新比较列以中央零。

## 依赖

- R335/R434：原 canonical 格、全部固定乘子、charge 四十和整换参。
- R588 §1：同一实际 regularized sigma 与椭圆单位的完整 Tate 范数。
- R607：同一无扭有限目标、纯 theta 子环和全部真实行缩放。
- R604：仅使用其固定模数素数选择及非连续行与真旗标的区别；
  本篇的单位方阵是原 $\mathcal W_D$ 全列，未重复其纯 $S/T$ 子格。
- R593/R597/R603：同一结点、全部原低行、完整 carry 和真正第二像判据。

全篇为全参数证明，无新增素数扫描或未经付清的实际候选。
