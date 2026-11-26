# R953 — 原奇偶列块的首次 Bockstein 单射与完整整指数一

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列完整同 parity 首次提升排除及整Smith结论已证明。** 在原自然五块预算和固定短比 \(9/41<x<2/7\) 下，充分大时原每个奇偶列块没有 primitive 的 \(p^2\) 解；其全部Smith指数只为零或一。证明先支付全核最近支和合法原格提升，再用同一次真实 carry 给出四个非零系数 \(180,-162,90,-35\)，并由同一个修正的两点次数门得到矛盾。全矩阵至少半数整指数至多一，未把两个块的像相加，仍保跨 parity 修正与主目标。

保持 R952 的原十九角、\(B=B_D\)、\(\beta=B^2\)、\(N=s-13\)、同 parity 非零子核 \(K_\varepsilon\)。
其实际共同因子为 \(F^m\)，\(m\in\{5,6,7,8\}\)，\(C=(F)=\tau C\)。
记
\[
 d=B C,\quad \kappa=C^2,\quad b=\deg_YF,\quad
 \lambda=L_{\rm pole}C\le8b,\quad mb\le D.
\]
以下的商 \(Q=\widehat P/F^m\) 与待求整模修正 \(\mathcal R\) 是两个不同对象，不混写。

## 1. 全部非零成员都保同一个唯一最近支

R952 已付 \(H^0(B-(m+1)C)=0\)。
所以每个非零核向量均恰含 \(F^m\)，其 \(Q|_C\ne0\)。
parity 和两真实正规化点给
\[
 v(Q):=\operatorname{ord}_{Q_+}Q
 =\operatorname{ord}_{Q_-}Q
 \le v_{\max}:=\frac{d-m\kappa}{2}.
 \tag{1}
\]
先对 R952 选定的一般成员使用
\[
 N\le(m-3)h+mT+v(Q),\qquad
 2(h+7T)\le3\kappa+\lambda.
 \tag{2}
\]
这里 \(h\) 是 \(C\) 的唯一最近支的截止接触，\(T\) 为同 \(C\) 的其它远支接触和；两者由固定 \(C\) 决定。

从 (2) 消去 \(T\)，再用 (1)，得
\[
 h\ge\frac{14N-7d+4m\kappa-m\lambda}{2(6m-21)}.
\]
再减 \(v_{\max}\)，并用 R952 的
\((2m-9)\kappa\ge2N-d-(m-3)\lambda\)，得到完整有限式
\[
 \boxed{
 h-v_{\max}\ge A_m:=
 \frac{(m+3)N-\frac32(m-2)d
                   -\frac12m(m-2)\lambda}{2m-9}.}
 \tag{3}
\]
四个显示式为
\[
 \begin{aligned}
 A_5&=8N-\tfrac92d-\tfrac{15}{2}\lambda,\\
 A_6&=3N-2d-4\lambda,\\
 A_7&=2N-\tfrac32d-\tfrac72\lambda,\\
 A_8&=(11N-9d-24\lambda)/7.
 \end{aligned}
\]
在原自然短比 \(9/41<x<1/3\) 中，
\(2N/\beta\to\rho=1/(4+x)>3/13\)，且 \(d\le\beta/m\)、\(\lambda=O(D)\)。
四种 \(A_m/\beta\) 在最小极限 \(\rho=3/13\) 的下界分别为
\(3/130,1/78,3/182,15/728\)，全严格为正。

若某个特殊成员的 \(Q\) 在物理点另有一个接触至少 \(h\) 的根，
超度量不等式使 \(Q(t,\psi)\) 的零阶至少为 \(h\)。
局部 \(Q\) 是正规函数，垂直含量非负，其余根和单位不能抵消这份零阶。
这与 (1)、(3) 矛盾。
因此 \(A_m>0\) 时，固定 \(C\) 的这个根对**整个 \(K_\varepsilon\) 的每个非零成员**仍为唯一最近根。
特殊成员无需重新选一个最近因子。

## 2. 保全部远支的实际局部单位展开

对任一非零成员，在固定支 \(Y=\psi(t)\) 周围写 \(X=Y-\psi\)。
完整分解给
\[
 \widehat P(t,\psi+X)=a(t)X^m
       \left(1+\sum_{j\ge1}b_j(t)X^j\right),
 \quad
 a(t)=F_Y(t,\psi)^m Q(t,\psi),
 \quad \operatorname{ord}_t a=mT+v.
 \tag{4}
\]
所有固定标量和局部 frame 单位保在同一个 \(a(t)\) 中。
令 \(V\) 为除这个最近支外，全部其余根与 \(\psi\) 的最大正接触。
真实乘积展开和正规外单位给
\[
 V\le\max(T,v),\qquad v_t(b_j)\ge-jV.
 \tag{5}
\]
这里 \(Q\) 的垂直含量保在 \(v\) 中；若无远根取 \(V=0\)。
令 \(\eta=g-\psi\)、\(\delta=h-V>0\)。
对 \(0\le j\le4\)，普通与 Euler 导数的有限展开给
\[
 \frac{\mathcal E^j\widehat P(t,g)}
 {(m)_j g^j a(t)\eta^{m-j}}
 \equiv1\pmod{t^\delta}.
 \tag{6}
\]
对 \(j=0\) 取 \((m)_0=1\)。
证明中每一个远根修正至少多一份 \(h-V\)；
Euler 较低普通导数项至少多一份 \(h\)。
原 \(p>211\) 保这里全部整数分母与 \((m)_j\) 为单位。

定义这一个真实成员的
\[
 \rho_0=mT+v,\qquad
 k=\rho_0+(m-3)h-s.
 \tag{7}
\]
不能以纯垂直 \(r\) 代替 \(\rho_0\)。
原第三长行准确给 \(k\ge-13\)。

由 \(\delta\ge h-v-T\)、(1)、forcing 和 R952(10)，准确得到
\[
 \boxed{\delta-k\ge A_m+13.}
 \tag{8}
\]
一种直接核法是
\[
 \begin{aligned}
 \delta-k
 &\ge s-(m-4)h-(m+1)T-2v\\
 &\ge s-d+\frac{12-m}{2}\kappa
                -\frac{m-4}{2}\lambda+(6m-29)T,
 \end{aligned}
\]
再代入 \((2m-9)\kappa\ge2N-d-(m-3)\lambda\) 和 \(N=s-13\)。
\(6m-29>0\)，故可保留或向下舍去该正项。
自然预算中 (8) 有正的二次余量，统一至少为
\(\beta/78+o(\beta)\)。
因此 \(k\) 及其任何固定十三行平移之前，远支单位扰动确实未进入 (6) 的归一读数。
完整 \(a(t)\) 的单位系数并未消失，不能把 \(a(t)\) 替成其首常数。

还有
\[
 2h\le3\kappa+\lambda\le3\beta/m^2+O(D).
 \tag{9}
\]
所以 \(m=6,7,8\) 在自然窗口自动满足 \(2h<s\)。
\(m=5\) 不由 (9) 免费得到 \(2h<s\)；若某个具体 Taylor reader 需要此条件，必须另付或使用不同余项次数。

全部首因子变形的严格余项门也由同一预算支付：
\[
 \boxed{
 h+v\le\frac{\beta}{2m}+\frac{\lambda}{2},\qquad
 h+T+\max(T,v)\le\frac{\beta}{2m}+\frac{\lambda}{2}.}
 \tag{9a}
\]
第二式分成 \(V=T\)、\(V=v\) 两种：
\(h+2T\le3\kappa/2+\lambda/2\le3\beta/(2m^2)+\lambda/2\)，
\(h+T+v\le d/2-(m-3)\kappa/2+\lambda/2-6T\)。
因 \(m\ge5\)，两者都不超过显示右端。
对 \(m\ge6\) 还准确有
\[
 \boxed{2h+T\le3\beta/m^2+\lambda.}\tag{9b}
\]
自然 \(s/\beta\to\rho/2>3/26\)，(9a) 的主系数至多 \(1/10\)，
(9b) 的主系数至多 \(1/12\)，所以
\(s-h-v\)、\(s-h-T-\max(T,v)\)，以及 \(m\ge6\) 的
\(s-2h-T\)，都有严格正二次余量。
这正支付五重 \(Z^4\) 项有限 Taylor 相消之后和六至八重未相消项的不同余项门。
此外 \(h\le3\beta/(2m^2)+O(D)<s\)，故此范围的最近接触实际未碰 \(s\) 截断；不是继续依赖一个辅助位移后的伪根。

## 3. 同一原来源中的合法整因子提升

先在一个有限未分歧扩张的完整 DVR \(\mathcal O\) 上展开全部需要的剩余常数。
原十九角是 \(\mathbb F_{4,\mathcal O}\) 在相同固定中心的连续吹起，给一个光滑、射影 \(\mathcal O\)-模型 \(\mathscr X\)。
根 \(h_7\) 在当前好素数处分离，必要时经有限未分歧扩张 Hensel 提升；
全部 Pic 类由原 \(S_0,F_0,E_{\alpha,j}^*\) 明确提升。
\(\tau:Y\mapsto-Y\) 保全部中心，因而提升到此模型。

对任一非边界几何整素分量 \(C'\)，R680 给 \(K_XC'<0\)。
它是光滑曲面上的整 Cartier 曲线，Serre 对偶和伴随给
\[
 H^1(C',\mathcal O_{C'}(C'))^\vee
 =H^0(C',\mathcal O_{C'}(K_X))=0.
\]
从
\(0\to\mathcal O_X\to\mathcal O_X(C')\to
\mathcal O_{C'}(C')\to0\)
及 \(H^1(\mathcal O_X)=H^2(\mathcal O_X)=0\)，得
\[
 H^1(X,\mathcal O_X(C'))=0.
 \tag{10}
\]
此证明不要求 \(C'\) 光滑。

用原 Pic 基提升类 \(C'\)，得到 \(\mathscr L_{C'}\)。
proper coherent cohomology 有限生成；
由
\(0\to\mathscr L_{C'}\xrightarrow{p}\mathscr L_{C'}
\to\mathscr L_{C'}|_{X_k}\to0\)
可知 \(H^1(\mathscr X,\mathscr L_{C'})/p\) 注入 (10)。
Nakayama 因而给 \(H^1(\mathscr X,\mathscr L_{C'})=0\)，进而
\[
 H^0(\mathscr X,\mathscr L_{C'})\twoheadrightarrow
 H^0(X,\mathcal O_X(C')).
 \tag{11}
\]
这给真整截面，不仅形式提升。
边界严格例外、特殊及一般底纤维、两截面则有原几何定义的 canonical lift。

将给定 \(\widehat P\) 的完整有效除子按真实素分量和重数全部提升，再相乘。
所有 Pic 基系数和准确为 \(B\)，所以所得截面属于
\(H^0(\mathscr X,\mathcal O_{\mathscr X}(B))\)，约化为原 \(\widehat P\)。
无需逐系数 naive lift 一个未付角帽的多项式。

还须识别整格而非只识别特殊纤维。
R680(1) 的原格本来就是显示自由格
\[
 \mathcal W_{D,\mathcal O}
 =\bigoplus_{n=0}^D
 Y^n(th_7)^{A_n}(t-1)^{B_n}d^{-C_n}
       \mathcal O[t]_{\le e_{n+1}}.
\]
十九角的逐 charge Gauss 条件在 \(\mathcal O\) 上是同一个固定因子整除和次数帽计算；
中心互不相撞，所用常数在当前都是单位。
故逐字得到
\[
 H^0(\mathscr X,\mathcal O(B))
 =d^{C_D}\mathcal W_{D,\mathcal O}.
 \tag{12}
\]
没有通过特殊纤维同维推断整像饱和。

对实际共同 \(F^m\)，先用 (11) 提升 \(F\)，再投影偶特征：
\((\widetilde F+\tau\widetilde F)/2\) 仍约化为 \(F\)。
余商 \(Q\) 先按完整除子逐因子提升，之后投影到相应 parity。
于是
\[
 P^{\rm fact}=\widetilde F^m\widetilde Q
 \in d^{C_D}\mathcal W_{D,\mathcal O}^{\varepsilon},
 \qquad \overline{P^{\rm fact}}=\widehat P.
\]
若 \(P^{\rm given}\) 是给定的同 parity 整来源，
\[
 (P^{\rm given}-P^{\rm fact})/p
 \in d^{C_D}\mathcal W_{D,\mathcal O}^{\varepsilon}.
 \tag{13}
\]
所以选取这一合法提升只在原允许的同一个首修正来源中平移。
原 \(G_0/P_{134}\)、公共单位和 \(w^{13}\) 是随后实际 \(M\) 的固定乘子；此构造没有删去、重选或交换它们。

## 4. 所有两点次数门的有限支付

继续用同一原商 \(Q\) 的 \(h,T,v,k\)，并假设自然短比位于
\[
 9/41<x<2/7.
 \tag{14}
\]
这个范围包括 \(11/47\)、\(1/4\)、\(2/9\)。本稿保留全部 \(m=5,6,7,8\)：R952 的先行八重排除只在 \(x<4/15\) 自动，不能把它扩大为本节全部范围。

置 \(j_m=8-m\)，所以 \(m=5,6,7,8\) 分别对应 \(j_m=3,2,1,0\)。
定义最终需要的几何差
\[
 G_m=2(m-4)h-2(8-m)T-d+(8-m)\kappa.
\]
从 (1)–(2) 保远支消元，先得
\[
 2(6m-21)T\le d+(2m-9)\kappa+(m-3)\lambda-2N.
 \tag{15}
\]
再逐个代入相同长行，不丢 \(T\)，得到
\[
 \boxed{
 \begin{aligned}
 G_5&\ge12N-7d-11\lambda,\\
 G_6&\ge(16N-11d-18\lambda)/3,\\
 G_7&\ge4N-3d-5\lambda,\\
 G_8&\ge(24N-19d-32\lambda)/7.
 \end{aligned}}
 \tag{16}
\]
例如 \(m=6\)，先有
\(G_6\ge(32N-31d+72\kappa-18\lambda)/15\)，
再代 \(3\kappa\ge2N-d-3\lambda\) 得显示式。
\(m=5,7\) 分别先得
\((20N-19d+44\kappa-11\lambda)/9\)、
\((44N-43d+100\kappa-25\lambda)/21\)，
再代 R952(10) 得 (16)。
八重的第一步是
\(G_8\ge(56N-55d+128\kappa-32\lambda)/27\)，
代 \(7\kappa\ge2N-d-5\lambda\) 给同表第四行。

代入 \(d\le\beta/m\)，(16) 在 (14) 中均有严格正的二次主项：
\(m=5\) 的门准确要求 \(\rho>7/30\)，即 \(x<2/7\)；
\(m=6,7,8\) 已在整个 \(9/41<x<1/3\) 中成立。
在 \(x=11/47\) 时四者皆有固定正余量，足以支付任何已明确的固定十三行损失。

这些最终门也支付全部前序除法：
因为 \(d\ge m\kappa\)，\(G_m>0\) 迫 \(h>\kappa\)；
对每个 \(0\le j\le j_m\)，
\[
 2((4-j)h-jT)-d+j\kappa
 =G_m+(j_m-j)\{2(h+T)-\kappa\}>0.
 \tag{17}
\]
而每个 min 中的长窗分支由
\[
 2(N-jT)-d+j\kappa
 \ge2N-d-j\lambda/7>0
 \tag{18}
\]
统一支付：此处 \(2T\le(3\kappa+\lambda)/7\)，且
\(\rho>3/13>1/m\)。
原 \(k\ge-13\) 及任意确定的额外固定移位只在 (17)–(18) 中增加固定误差，严格二次余量保留。

读取范围也能由同一预算给出。
R952(10) 和 (15) 使
\[
 k\le\frac{3(m-3)}{2m^2}\beta-s+O(D)
 \le\frac18\beta-s+O(D).
\]
故自然窗口中 \(k<\ell-cD^2\)，其中 \(c>0\) 只依赖固定短比；
因为 \(\ell+s-\beta/8\) 的主项是
\(\frac32(1/4-\rho)\beta>0\)。
对最终非零 reader 的候选阶，
\[
 (4-j_m)h+k=(m-4)h+k
 \le\frac{d+(5m-21)\kappa+(2m-7)\lambda}{2}-s.
\]
\(m=5,6,7,8\) 时上式严格小于 \(N-c'D^2\)，
因为其两倍分子主系数至多
\(\max 3(2m-7)/m^2=3/7<2\rho\)。
所有这些先是原物理有限范围的几何余量；对应实际 carry 在§6完整证明。

## 5. 这些前置如何消费一个真实首修正 reader

假定完整原 \(M\) 的一次除 \(p\)、合法提升差及全部 fixed carrier 已经给出
\(\mathcal R\in H^0(B)^\varepsilon\) 的实际限制。
若对 \(0\le j<j_m\) 已证明
\[
 \operatorname{ord}_{Q_\pm}
  (\mathcal E^j\mathcal R)|_{\widetilde C}
 \ge\min\{N,(4-j)h+k\}-c_0,
 \tag{19}
\]
并对 \(j=j_m\) 给出非零限制及准确首阶
\[
 \operatorname{ord}_{Q_\pm}
  (\mathcal E^{j_m}\mathcal R)|_{\widetilde C}
 =(4-j_m)h+k+O(1),
 \tag{20}
\]
其中全部固定移位已明确且不随 \(D\) 增长，那么 (16)–(18) 真正排除该首修正。

证明是同一个原来源中的连续除法。
若 \(j_m=0\)，直接用 (20) 的两点零阶和超过 \(d\)，迫 \(F\mid\mathcal R\)，立即与该非零限制矛盾。
若 \(j_m\ge1\)，(19) 的 \(j=0\) 两点零阶和超过 \(d\)，迫
\(\mathcal R=F H_1\)，\(H_1\in H^0(B-C)\)。
若已知 \(\mathcal R=F^jH_j\)，则在整曲线泛点及其正规化上准确有
\[
 (\mathcal E^j\mathcal R)|_C=j!(\mathcal EF|_C)^j H_j|_C.
\]
这里 \(\operatorname{ord}_{Q_\pm}(\mathcal EF)=T\)，没有将其当单位。
相应两点深度须减 **\(jT\)**；(17)–(18) 仍严格大于
\((B-jC)C=d-j\kappa\)，迫 \(F\mid H_j\)。
到 \(j_m\) 时同样迫 \(F^{j_m+1}\mid\mathcal R\)，
这与 (20) 的非零限制矛盾。
奇支不妨碍此论证：对一个非零 \(H_j|_C\)，正规化拉回的总零阶仍不超过完整次数 \(d-j\kappa\)。

本节先证明 (19)–(20) 的完整几何消费者；§6随后从实际原矩阵证明这两个读数。
若实际 carry 只给环境 jet、丢了 \(G_0\)、使用不合法因子提升或未经支付的尾，则不能套用本节。
也不从这个条件消费者直接宣称更高 Smith 指数或原无穷中央非零。


## 6. 同一五块矩阵的完整首次 carry：把前置变成实际非零

以下使用实际算术轴 \(g=g_{A^*}\)，不将参考 \(g_\circ\) 或自由高轴代入。
所有 \(t\) 阶均可由原单位换参 \(t=t(w)\) 读为 \(w\) 阶。
固定一个非零首核向量 \(\widehat P=F^mQ\)，令
\[
 \eta=mT+v,\qquad k=\eta+(m-3)h-s,\qquad k_{\rm phys}=k+13.
 \tag{21}
\]
这里的 \(v=\operatorname{ord}_{Q_\pm}Q\) 保全部垂直含量和其它因子；
不是只取 \(\operatorname{ord}_t\widehat P\)。

### 6.1 实际整目标单位换基与全部52跨界行

R328/R324 的原单位在此物理长度内准确为
\[
 U_{0,A}=g_A^{40}u_*(w)e_4(40a_p\epsilon)\in
 \Gamma_{\rm phys}^{\times},
 \qquad
 u_*=\frac{G_0}{c_*w^{13}\rho^{40}},\quad u_*(0)=1.
\]
原固定 \(c_*\) 在当前好惰性素数是单位：其中3159421是
\(1\bmod6\) 的固定素数，其余固定小素数已排除。
因此 R943(68) 在**实际** \(A=A^*\) 下给
\[
 (c_*U_{0,A})^{-1}M_A^{\rm orig}
       =m_{13}J_{5,A}.
 \tag{22}
\]
这是原完整目标上的整自同构，保每一个 \(p^r\) 的核以及任何固定的
source parity。没有把 \(U_{0,\circ}\) 当作 \(U_{0,A}\)；
两者的实际 \(g_A^{40}\) 与 \(e^{40h_A}\) 比例都在这个原单位内。
\(P_{134}\)、总charge四十和全部原常数通过已证原单位身份保持。
这里始终**不逆** \(m_{13}\)。

为写出这个准确等价矩阵，对实际相对来源 \(P\in\mathcal W_{D,\mathcal O}\)
置
\[
 \Psi_j=w^{13}(\mathcal E^jP)(t(w),g(w)),\qquad
 \mathcal E=Y\partial_Y .
\]
若用清分母来源 \(\widehat P\)，则
\(\Psi_j=w^{13}d^{-C_D}\mathcal E^j\widehat P(t(w),g(w))\)；
\(d^{-C_D}\) 是同一原角单位且与 \(\mathcal E\) 交换。
全部五行恰为
\[
 \left[
 \sum_{i=0}^{r}\frac{a_p^i}{i!}p^{r-i}
                    \mathscr S^{r-i}\Psi_i
 \right]_{<m_r},
 \quad
 (m_0,m_1,m_2,m_3,m_4)=(s,s,s,s,\ell+13).
 \tag{23}
\]
这是先乘 \(w^{13}\) 后在原 \(w^s=p\epsilon\) 目标中完整归并，
所以四条十三行跨界带和最前十三个目标方向全部还在。
只对可逆公共单位换基，没有将52成本当成零。

### 6.2 合法因子提升的同一次首阶变形

假设原同 parity 来源存在 primitive 的 \(p^2\) 解。
依§3，选同一原来源格中的合法因子提升
\(\widehat P^{\rm fact}=\widetilde F^m\widetilde Q\)，并唯一写成
\[
 \widehat P^{(2)}=\widehat P^{\rm fact}+p\widehat{\mathcal R},
 \qquad
 \widehat{\mathcal R}\in H^0(\mathscr X,\mathcal O(B))^\varepsilon .
 \tag{24}
\]
以下 \(\mathcal R\) 表示这个修正的约化清分母截面。
它不是第1–4节的原商 \(Q\)。

取 \(\psi\) 的一个整形式提升 \(\widetilde\psi(w)\)；
前 \(h\) 个系数选成实际 \(g(w)\) 的同一系数。
这合法，因为 \(\psi\) 与 \(\bar g\) 在这些系数上相等。
于是
\[
 Z=\log(Y/\widetilde\psi),\qquad
 z=\log(g/\widetilde\psi)=w^hu(w),\quad u(0)\in\mathcal O^\times .
 \tag{25}
\]
\(\widetilde\psi\) 不被假定为 \(\widetilde F\) 的根。
其所有未消失的首 \(p\) 误差马上保留在同一个变形项中。

这些 log/exp 只在有限截断环中使用。
物理长度 \(L_{\rm phys}=4s+\ell+13<5s<p\)，
即使为四次导数多保留四个 \(Z\) 次数，也有
\(L_{\rm phys}+4<p\)。
因此所用 factorial 全是单位；更高 \(Z\) 项在代入
\(z\in w^h\mathcal O[[w]]\)、作至多四次导数之后，仍越过全部读取长度。
没有声称无限的 \(\exp Z\) 属于 \(\mathcal O[[Z]]\)。

在这个有限环中，
\[
 \bar F(t,\psi e^Z)=Z U(Z),\quad
 \bar Q(t,\psi e^Z)=Q(Z),
\]
且§2的完整远支展开给
\[
 \operatorname{ord}_w[Z^i]U\ge T-iV,\qquad
 \operatorname{ord}_w[Z^i]Q\ge v-iV.
 \tag{26}
\]
首系数准确阶分别为 \(T,v\)。
逐系数选择保持这些实际 \(w\) 阶的整提升 \(U_{\mathcal O},Q_{\mathcal O}\)。
这只是证明中分解实际局部表达，不改变全局合法
\(\widetilde F,\widetilde Q\) 或来源格。
于是实际提升在模 \(p^2\) 下可写成
\[
 \Psi^{\rm fact}(Z)
  =w^{13}\{Z^m A_{\mathcal O}(Z)+p\,\mathcal D(Z)\},
 \tag{27}
\]
其中原角单位 \(d^{-C_D}\) 全保在系数中，
\[
 \operatorname{ord}[Z^i]\bar A_{\mathcal O}\ge\eta-iV,
 \qquad \operatorname{ord}\bar A_{\mathcal O}(0)=\eta.
\]
首阶变形 \(\mathcal D\) 是同一个实际表达，分为两类：
\[
 \mathcal D=
 m(ZU)^{m-1}B_FQ\cdot(\text{原单位})
 +(ZU)^m B_Q\cdot(\text{原单位}).
 \tag{28}
\]
\(B_F,B_Q\) 的全部系数整，未假它们的值或导数为零。
原单位的首阶变化可并入第二类。
因而第一类的第 \(m-1+i\) 项系数阶至少为
\((m-1)T+v-iV\)，第二类的第 \(m+i\) 项至少为
\(mT-iV\)。特别
\(\mathcal D\in Z^{m-1}k[[w]][Z]\)。
这是保留 \(F_Y\) 的非单位阶 \(T\) 后的实际变形，
不是先在分式域沿一个未支付的整根作除法。

因为 \(h>V\)，(27) 第一项的第 \(j\) 个 Euler 值，
在整系数层面的 \(w\) 阶至少为
\(13+\eta+(m-j)h\)，其约化准确等于这个阶。
原首核条件使它在相应第 \(j\) 行的整个窗口内为零。
所以把 (23) 真正除一次 \(p\)，再逐行乘单位 \(j!/a_p^j\)，得到
\[
 X_j\equiv-w^{13}\mathcal D^{(j)}(z)
       -\frac{j}{a_p}\,
             \mathscr S\bigl(\bar\Psi_{j-1}^{\rm fact}\bigr)
              \pmod{w^{m_j}},\quad 0\le j\le4,
 \tag{29}
\]
其中 \(X_j=w^{13}d^{-C_D}
 (\mathcal E^j\mathcal R)(t(w),\bar g(w))\)，
\(j=0\) 时第二项为零。

每一个 \(j\ge1\) 所用的
\(\bar\Psi_{j-1}^{\rm fact}\) 都来自原四条长行，已消到 \(s\)。
所以在这些项上
\(\mathscr S=w^{-s}\) 是**实际完整 shift**，没有被删的低于 \(s\) 前缀。
不能在未乘原 \(w^{13}\) 的相对来源上裸用这个等式。

### 6.3 原十三行首先消去负 \(k\)

若 \(-13\le k<0\)，则 \(0\le k_{\rm phys}<13\)。
在 (29) 的第四行，\(X_4\) 与
\(w^{13}\mathcal D^{(4)}(z)\) 都含 \(w^{13}\)。
但其真实 carry 首项在 \(w^{k_{\rm phys}}\)，系数为
\[
 -\frac{4(m)_3}{a_p}\,
     [w^\eta]A_{\mathcal O}(0)\,u(0)^{m-3}\in k^\times .
\]
它在原短窗口内，因为 \(\ell+13>13\)。
于是同一原首余核已有非零前缀行，矛盾。
任何被假设的 \(p^2\) 提升都必须满足
\[
 \boxed{k\ge0.}\tag{30}
\]
此处没有另选来源调整最低行。

### 6.4 有限逆 Taylor 消去全部根提升误差

对 \(0\le a\le3\) 定义完整的有限线性组合
\[
 \mathcal T_a=\sum_{j=a}^{4}
          \frac{(-z)^{j-a}}{(j-a)!}(\text{第 }j\text{ 行}).
\]
对每个 \(Z^n\)、\(a<n\le4\)，
\[
 \sum_{j=a}^{n}
 \frac{(-z)^{j-a}}{(j-a)!}
 \left.\frac{d^jZ^n}{dZ^j}\right|_{Z=z}=0.
\]
这解释五重情形中为何必须消去 \(\mathcal D\) 的 \(Z^4\) 项。
它不是一个可直接判为高阶的项。

对 \(\mathcal D\) 剩下的全部项，(28) 给如下真实下界，
均还须加上公共13：
\[
\begin{array}{c|c|c}
 &\text{第一类变形}&\text{第二类变形}\\ \hline
 m=5&(5-a)h+4T+v-V&(5-a)h+5T\\
 m\ge6&(m-1-a)h+(m-1)T+v&(m-a)h+mT.
\end{array}
\tag{31}
\]
因为 \(h>V\)，更高的 \(Z\) 次数只增大这些下界。
欲读取的物理 carry 阶为
\[
 J_a^{\rm phys}=13+(4-a)h+k
              =13+\eta+(m+1-a)h-s .
\]
(31) 与它的差，第一类分别是
\[
 s-h-T-V\quad(m=5),\qquad s-2h-T\quad(m\ge6),
\]
第二类均为 \(s-h-v\)。
§2(9a)–(9b) 已给它们严格正的二次余量。
所以所有未知根提升和原商提升在实际 reader 中都被支付。
五重不需要假 \(2h<s\)。

同一个首修正的第五及更高 Taylor 项至少从
\(13+(5-a)h\) 起；它比目标高 \(h-k>0\)，由§2(8)支付。
长行未知尾的阶至少为 \(s+(j-a)h\)；
第四短行未知尾的阶为 \(\ell+13+(4-a)h\)，比目标高
\(\ell-k>0\)。
因而对任意 \(a\le3\) 可读至
\(\min(s,J_a^{\rm phys})\)；若 \(J_a^{\rm phys}<s\)，
还准确读到其非零首项。
全过程始终在同一组五行和同一个修正内，没有分别拼接四个 \(R\)。

### 6.5 实际四个首系数与完整低阶限制

令 \(A_0(w)=\bar A_{\mathcal O}(0)\)，其阶为 \(\eta\)。
(26) 的所有远支误差在 carry 的主项之后至少多 \(h-V>0\)。
把 (29) 的全部 carry 同时代入 \(\mathcal T_a\)，得到系数
\[
 c_{m,a}=-
 \sum_{j=\max(a,1)}^4
       \frac{(-1)^{j-a}j(m)_{j-1}}{(j-a)!}.
\]
完整相加是
\[
\begin{aligned}
 c_{m,3}&=m(m-1)(4m-11),\\
 c_{m,2}&=-m(2m-3)(m-3),\\
 c_{m,1}&=(m-2)(m-3)(4m-1)/6,\\
 c_{m,0}&=-\binom{m-1}{3}.
\end{aligned}
\tag{32}
\]
这些系数乘同一个
\(a_p^{-1}w^{-s}A_0(w)z^{m+1-a}\)；原角单位已经完整含在 \(A_0\) 中。
只在确定首阶时取它们的首常数；完整 \(A_0(w)\) 没有被替换掉。

现在才除去已明确共同的 \(w^{13}\) 并乘回 \(d^{C_D}\)，
在真实 \(\widetilde C\) 上得到
\[
 \boxed{
 \operatorname{ord}_{Q_\pm}(\mathcal E^a\mathcal R)|_{\widetilde C}
 \ge \min\{N,(4-a)h+k\},\quad 0\le a\le3.}
 \tag{33}
\]
这只是对已知含 \(w^{13}\) 的真实分支值减去阶13，
没有对原目标乘子 \(m_{13}\) 作整逆。

取 \(a=j_m=8-m\)。§4已逐项付清
\((4-j_m)h+k<N\) 和 \(k<\ell\)。
所需四个系数准确为
\[
 (c_{5,3},c_{6,2},c_{7,1},c_{8,0})
       =(180,-162,90,-35)\in(k^\times)^4.
\]
因此在这一个真实修正上，
\[
 \boxed{
 \operatorname{ord}_{Q_\pm}(\mathcal E^{j_m}\mathcal R)|_{\widetilde C}
       =(4-j_m)h+k,\qquad
 (\mathcal E^{j_m}\mathcal R)|_{\widetilde C}\ne0.}
 \tag{34}
\]
\(\tau F=F\)、同一 source parity，以及 \(\tau\) 将两条图轴
\(Y=g\)、\(Y=-g\) 和两条分支 \(Y=\psi\)、\(Y=-\psi\) 分别交换，
使两个正规化点具有相同阶，首系数最多差一个固定特征符号。
没有给第二点自由指定另一个修正或 forcing。

(33)–(34) 正是§5的条件 reader，此处已由完整实际 carry 证明；
其中 \(c_0=0\)，所有物理十三行平移均已准确消去而非写成未知误差。

## 7. 首 Bockstein 真单射与同一列块的整结论

固定
\[
 9/41<x<2/7,\qquad
 D\to\infty,\quad \ell/N\to x,\quad
 4N+\ell=n_D+o(D^2).
 \tag{35}
\]
沿同一原好惰性素数和实际来源序列，前述全部有限严格门对充分大的
\(D\) 同时成立。它们的余量由 \(\beta\asymp D^2\)、
\(\lambda\le8D/m\) 和§1–4的显示公式统一支付，
不依赖一个所挑选的核向量。

若存在 primitive 的 \(p^2\) 解，其非零约化属于 \(K_\varepsilon\)。
R952与§1保证这个**实际**向量具有同一固定 \(F^m\) 和最近支，
§3给同原格的合法因子提升，§6给同一个
\(\mathcal R\) 的 (30)、(33)、(34)。
由 \(k\ge0\)，§4的 \(G_m>0\) 和两个 min 分支不再有任何未付的
固定13损失。§5的逐次真实除 \(F\) 因而迫
\(F^{j_m+1}\mid\mathcal R\)，与 (34) 的非零限制矛盾；
\(m=8,j_m=0\) 时第一步就矛盾。

所以对每个 \(\varepsilon\)：
\[
 \boxed{
 M_A^{\rm orig}(P)\in p^2\Gamma_{\rm phys},\
 P\in\mathcal W_{D,\mathcal O}^{\varepsilon}
 \quad\Longrightarrow\quad
 P\in p\mathcal W_{D,\mathcal O}^{\varepsilon}.}
 \tag{36}
\]
若 \(K_\varepsilon=0\)，这一式直接由模 \(p\) 单射成立。
它不是声称所有 \(p\) 倍来源的像均自动属于 \(p^2\)。

等价地，这个**完整 parity 列块**的首次 Bockstein
\[
 \beta_{1,\varepsilon}:K_\varepsilon\longrightarrow
 \operatorname{coker}
   (\bar M_A^{\rm orig}|_{\mathcal W_D^\varepsilon})
\]
为单射。设 \(n_\varepsilon=\operatorname{rank}\mathcal W_D^\varepsilon\)。
由DVR上的Smith分解，(36)同时排除零列因子和所有指数至少二的因子：
\[
 \boxed{
 \operatorname{rank}_{\operatorname{Frac}\mathcal O}
       (M_A^{\rm orig}|_{\mathcal W_D^\varepsilon})=n_\varepsilon,
 \quad\text{全部Smith指数属于 }\{0,1\}.}
 \tag{37}
\]
指数一的个数准确是 \(\dim K_\varepsilon\)。
原真整因子/来源识别及全部物理窗口是 (37) 的前提，
不是由小型模 \(p\) 例子外推。

还可保守地返回到全矩阵。设其Smith指数按非降序记为 \(a_i\)，
秩之外记 \(+\infty\)。因为完整 parity 块真是其原列子集，
至少 \(n_\varepsilon\) 个 \(a_i\le1\)：
若少于 \(n_\varepsilon\)，在全矩阵的Smith行坐标中，
令该列块在所有 \(a_i\le1\) 的行上准确为零。
少于 \(n_\varepsilon\) 个线性方程有非零分式解，清分母并除去公共
\(p\) 得一个原始整向量；余下行全部被 \(p^2\) 整除，违反 (36)。
因此
\[
 \boxed{\#\{i:a_i\le1\}\ge
       \max(n_+,n_-)\ge\lceil n_D/2\rceil.}\tag{38}
\]
这选取一个较大的列块，没有相加两个交像。
按相同原子式的整除关系还有
\[
 \sum_{i=1}^{n_\varepsilon}a_i
       \le\dim K_\varepsilon.
 \tag{39}
\]
特别在 \(x=11/47\)，R952给右边与 \(n_D\) 之比的 \(\limsup\) 严格小于
\(1/1250\)，并保原全矩阵单位秩比例的 \(\liminf\) 严格大于 \(312/625\)。

## 8. 这一实际后页结论仍保的界限

本篇确实排除了完整同 parity 来源的全部 primitive \(p^2\) 解，
并给真实列块的整Smith结论；不是条件性的环境 jet 消费者。

全矩阵的一个提升若首项在 \(K_\varepsilon\)，但其下一修正允许另一
parity，那么它取商的是
\(\operatorname{coker}(\bar M|_{\mathcal W_D})\)，
不是 (37) 的单块余核。本文没有将两者混同，
也没有从 (38) 宣称全矩阵所有指数至多一。
剩余 \(q=1\) 混合核、跨 parity 首修正、实际高页与五中央的跨素数
联合非零仍需继续处理。通常全 \(\Sha\) 的无穷素数目标尚未完成。

本篇没有新增数值执行、素数扫描或可重算输出。


## 依据与同源定位

- [R952](R952-original-fixed-factor-residual-restriction-and-same-kernel-injection.md)：全parity核的共同因子、真正剩余限制、下一重数消失与原移动部；本文保全部奇支和远支。
- [R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)定理1及R491的原Gauss帽：同一完整来源的十九角识别与整显示基；§3把实际因子提升的全部边界和parity选择写全，没有新扩源。
- [R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)§10、R328/R324的实际单位身份：原五块、实际g、完整52跨界及同一物理窗口。
- R824 的同修正有限Taylor原则仅作前序定位；本篇§6独立保全新的四长一短及非单位T的实际读数，不把旧简单根公式直接外推。
