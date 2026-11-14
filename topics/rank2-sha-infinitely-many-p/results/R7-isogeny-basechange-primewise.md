# R7：同源、二次基变换与 CM 素理想分解的精确比较

**可信度：已证明。** 本结果给出实际的群同态及其逆，确定 R4 的二次下降能通过哪些映射传播、传播到哪里。它不证明无穷多个 $p$ 上的有限性，也不声称不存在尚未发现的跨素数方法。

固定
$$
E/\mathbb Q:\ y^2=x^3-17x,\qquad
E'/\mathbb Q:\ Y^2=X^3+68X,\qquad K=\mathbb Q(i).
$$
R4 已证明 $\operatorname{rank}E(\mathbb Q)=2$。记 $c$ 为 $K/\mathbb Q$ 的复共轭，$I=[i]$ 为 $E/K$ 的 CM 自同态
$$
I(x,y)=(-x,iy),\qquad I^2=[-1],\qquad cIc^{-1}=-I.
$$

## 1. 次数为 2 的同源在每个奇 $p$ 上无损

R4 中的同源 $\phi:E\to E'$ 及其对偶 $\psi:E'\to E$ 满足
$$
\psi\phi=[2]_E,\qquad \phi\psi=[2]_{E'}.
$$
因此，对任意特征为零的域 $F$、奇素数 $p$ 和整数 $n\ge1$，$\phi$ 诱导 Galois 模同构
$$
E[p^n]\xrightarrow{\sim}E'[p^n].
$$
若选整数 $a$ 满足 $2a\equiv1\pmod{p^n}$，则逆就是 $a\psi$。同理，它在 $E(F)/p^nE(F)$ 与 $E'(F)/p^nE'(F)$ 上给出同构，逆仍为 $a\psi$。

将上述同构放入全局和各局部的 Kummer 图，它们与边界映射交换；故在数域 $F$ 上有
$$
\operatorname{Sel}_{p^n}(E/F)\simeq\operatorname{Sel}_{p^n}(E'/F),
\qquad
\operatorname{Sel}_{p^\infty}(E/F)\simeq\operatorname{Sel}_{p^\infty}(E'/F).
$$
在 Weil–Châtelet 群及其处处局部平凡子群上，同源仍满足对偶复合等于 $[2]$。任何 $p$-初等群上乘 $2$ 是自同构，于是
$$
\phi_*:\Sha(E/F)[p^\infty]\xrightarrow{\sim}\Sha(E'/F)[p^\infty],
\qquad \phi_*^{-1}=\tfrac12\psi_*.
$$
这里核与余核均为零。结论是：同源确实允许把**同一个奇素数**的已知结论在 $E,E'$ 间搬运；它没有把 $2$-初等群变成 $p$-初等群。

在 $K$ 上，这一事实还可写得更具体。令 $u=1+i$，定义同构
$$
\tau:E\longrightarrow E',\qquad \tau(x,y)=(u^2x,u^3y).
$$
由于 $u^4=-4$，它确为同构，并且
$$
\phi=\tau\circ[1+i],\qquad
\psi=[1-i]\circ\tau^{-1}.
$$
例如第一式可由群律直接验证；也可比较两个次数 $2$ 的同态的核及微分：$\phi^*(dX/(2Y))=dx/(2y)$、$\tau^*(dX/(2Y))=u^{-1}dx/(2y)$，故 $\tau^{-1}\phi$ 的微分为 $u$。特征零时同态由其微分唯一确定。这说明 R4 的二次下降在 CM 环内对应的是唯一位于 $2$ 上的素理想 $(1+i)$。

## 2. $K/\mathbb Q$ 的限制与余限制

下面的论证同时适用于 $\Sha[p^\infty]$ 和 $\operatorname{Sel}_{p^\infty}$；先对 $\Sha$ 写出。

设
$$
A_p=\Sha(E/\mathbb Q)[p^\infty],\qquad
S_p=\Sha(E/K)[p^\infty],\qquad p\ne2.
$$
限制和余限制映射满足
$$
\operatorname{cor}\operatorname{res}=2,
\qquad
\operatorname{res}\operatorname{cor}=1+c.
$$
它们保持处处局部平凡条件：全局限制与各局部限制交换，余限制的局部化是相应局部余限制的和。因此这些映射确实定义在 $\Sha$ 上。

令
$$
S_p^+=\{s:c(s)=s\},\qquad S_p^-=\{s:c(s)=-s\}.
$$
由于 $2$ 在 $p$-初等群上可逆，投影 $e_\pm=(1\pm c)/2$ 给出
$$
S_p=S_p^+\oplus S_p^-.
$$
$\operatorname{res}:A_p\to S_p^+$ 是同构，其逆为 $\tfrac12\operatorname{cor}$：核由 $\operatorname{cor}\operatorname{res}=2$ 消去，满射由 $\operatorname{res}\operatorname{cor}=1+c$ 得到。

又因 $cIc^{-1}=-I$，$I$ 将 $S_p^+$ 同构到 $S_p^-$。所以有显式同构
$$
A_p\oplus A_p\xrightarrow{\sim}S_p,
\qquad (a,b)\longmapsto\operatorname{res}(a)+I\operatorname{res}(b).
$$
其逆为
$$
s\longmapsto
\left(\frac12\operatorname{cor}(s),\ -\frac12\operatorname{cor}(Is)\right).
$$
因此
$$
\Sha(E/K)[p^\infty]\simeq\Sha(E/\mathbb Q)[p^\infty]^2,
$$
特别地，两个有限性命题等价；基变换把余秩加倍，而不是把原来的未知部分消掉。

对 Selmer 群，同样的限制、余限制关系成立。其局部条件是 Kummer 像，而余限制在 Kummer 像上对应点的范数，所以保持这些条件。故
$$
\operatorname{Sel}_{p^\infty}(E/K)
\simeq\operatorname{Sel}_{p^\infty}(E/\mathbb Q)^2.
$$
有限层 $p^n$ 也成立。

## 3. 为什么二次扭转没有使这里降秩

对任意二次扩张 $F(\sqrt d)/F$，奇 $p$ 的上述 $+$ 分量来自 $E/F$，$-$ 分量来自二次扭转 $E^{(d)}/F$。这是由扭转同构将负 Galois 作用变成正作用直接得到的。

在当前例子中，标准二次扭转模型为
$$
E^{(d)}:\ y^2=x^3-17d^2x.
$$
取 $d=-1$ 时，$E^{(-1)}$ 的方程与 $E$ 相同；在 $K$ 上实现扭转的同构正是 $I$。因此两个分量各自都对应秩 $2$ 的原曲线。

同一分解适用于 $E(K)\otimes_\mathbb Z\mathbb Q$，给出
$$
\operatorname{rank}_\mathbb Z E(K)=4,
\qquad \operatorname{rank}_{\mathbb Z[i]}E(K)=2.
$$
更换一个二次扩张也不会去掉原来的 $+$ 分量；如果另一个扭转恰有低秩定理可用，它只控制另一个直和项。

## 4. 分裂素数的单个 CM 分量恰等于原来的 $p$-初等问题

设 $p\equiv1\pmod4$，并取
$$
p\mathbb Z[i]=\mathfrak p\bar{\mathfrak p},\qquad
\mathfrak p=(\pi),\qquad \pi\bar\pi=p.
$$
由中国剩余定理
$$
\mathbb Z[i]\otimes\mathbb Z_p\simeq\mathbb Z_p\oplus\mathbb Z_p
$$
得到幂等元 $e_{\mathfrak p},e_{\bar{\mathfrak p}}$，以及
$$
S_p=S_{\mathfrak p}\oplus S_{\bar{\mathfrak p}},
\qquad
S_{\mathfrak p}=\Sha(E/K)[\mathfrak p^\infty].
$$
复共轭交换两个直和项。此时有更强的显式同构
$$
r_{\mathfrak p}:A_p\xrightarrow{\sim}S_{\mathfrak p},
\qquad a\longmapsto e_{\mathfrak p}\operatorname{res}(a),
$$
其逆恰为 $\operatorname{cor}|_{S_{\mathfrak p}}$，无需另加 $2$ 的因子。

**验证。** 若 $x\in S_{\mathfrak p}$，则
$$
r_{\mathfrak p}(\operatorname{cor}x)
=e_{\mathfrak p}(x+cx)=x.
$$
若 $a\in A_p$，则
$$
\operatorname{res}(\operatorname{cor}(r_{\mathfrak p}a))
=r_{\mathfrak p}a+c(r_{\mathfrak p}a)
=(e_{\mathfrak p}+e_{\bar{\mathfrak p}})\operatorname{res}(a)
=\operatorname{res}(a).
$$
第 2 节已证明限制单射，故 $\operatorname{cor}(r_{\mathfrak p}a)=a$。$\square$

同样的证明对 Selmer 群成立：
$$
\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
\simeq\operatorname{Sel}_{\mathfrak p^\infty}(E/K).
$$
所以从二维 $p$-进 Tate 模改用一维 CM 特征确实简化了系数表示，但没有把 Selmer 的 Mordell–Weil 余秩从 $2$ 降为 $1$。

## 5. 每个分裂 $p$ 的 Kummer 列与精确缺项

对每个 $n\ge1$，乘 $\pi^n$ 的 Kummer 列给出
$$
0\longrightarrow E(K)/\pi^nE(K)
\longrightarrow\operatorname{Sel}_{\pi^n}(E/K)
\longrightarrow\Sha(E/K)[\pi^n]\longrightarrow0.
$$
这里有理点商恰为
$$
E(K)/\pi^nE(K)\simeq(\mathbb Z[i]/(\pi^n))^2
\simeq(\mathbb Z/p^n\mathbb Z)^2.
$$
理由是第 3 节给出 $\mathbb Z[i]$-秩为 $2$，而 $\mathbb Z[i]$ 是主理想环；另外这里没有奇分裂 $p$ 的有理挠点：$3$ 在 $K$ 中惰性，$E$ 在其上方素点好约化，且
$$
\#E(\mathbb F_9)=(3+1)^2-a_3^2=16,
\qquad a_3=3+1-\#E(\mathbb F_3)=0.
$$
任意 $p\equiv1\pmod4$ 都与 $3$ 不同，故该 $p$ 的挠点注入一个 $16$ 元群，必须为零。有限挠部分因此在模 $\pi^n$ 商中没有贡献。

传到无穷层，得到
$$
0\longrightarrow(\mathbb Q_p/\mathbb Z_p)^2
\longrightarrow\operatorname{Sel}_{\mathfrak p^\infty}(E/K)
\longrightarrow\Sha(E/K)[\mathfrak p^\infty]\longrightarrow0.
$$
结合第 4 节，所需的缺项就是
$$
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{\mathfrak p^\infty}(E/K)=2
$$
对无穷多个同一条曲线的分裂 $p$ 成立。一个更强的充分条件是
$$
\dim_{\mathbb F_p}\operatorname{Sel}_{\pi}(E/K)=2
$$
对无穷多个 $p$ 成立：由 Kummer 列它使 $\Sha[\pi]=0$，从而整个 $\pi$-初等部分为零。这个有限层充分条件**不是**有限性的必要条件；有限但非零的 $\Sha[\mathfrak p^\infty]$ 仍可能含 $\pi$-挠点。

## 6. 一个真正统一于 $p$ 的局部结论

### 6.1 除去 $5$ 后自动非异常

对任意好约化素数 $p\ge7$，点 $T=(0,0)$ 在 $E(\mathbb F_p)$ 中仍为非零二阶点，因此 $\#E(\mathbb F_p)$ 为偶数。Hasse 界给出
$$
0<p+1-2\sqrt p\le\#E(\mathbb F_p)\le p+1+2\sqrt p<2p.
$$
如果 $p$ 整除这个群的阶，它只能等于 $p$，与偶数性矛盾。因此
$$
p\nmid\#E(\mathbb F_p)\qquad(p\ge7,\ p\nmid34).
$$
这是一次性证明的无穷素数范围，未使用逐个计算。$p=5$ 的确不能并入：R4 给出 $\#E(\mathbb F_5)=10$。

### 6.2 分裂 $p$ 的两个有限层局部条件

现设 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$。由上一小节以及好约化形式群在 $\mathbb Q_p$ 上的无挠性，
$$
E(K_{\mathfrak p})[p]=E(K_{\bar{\mathfrak p}})[p]=0;
$$
两局部域都等于 $\mathbb Q_p$。这里形式群无挠可由形式对数在 $p\mathbb Z_p$ 上是群同构看出；任何局部 $p$ 挠点若约化为零，便落入该形式群，而非零约化又被 $p\nmid\#E(\mathbb F_p)$ 排除。

设 $V=E[\pi]$。Weil 配对给出其 Tate 对偶 $V^*(1)\simeq E[\bar\pi]$。因此在两个局部域上都有 $H^0(V)=H^0(V^*(1))=0$。局部 Tate 对偶与 Euler–Poincaré 公式于是给出
$$
\dim_{\mathbb F_p}H^1(K_{\mathfrak p},V)
=\dim_{\mathbb F_p}H^1(K_{\bar{\mathfrak p}},V)=1.
$$

乘 $\pi$ 在椭圆曲线局部李群的微分为 $\pi$。它在 $K_{\mathfrak p}$ 中的赋值为 $1$，在 $K_{\bar{\mathfrak p}}$ 中为 $0$。由形式对数，在足够小的开子群上，它分别对应 $\mathbb Z_p$ 上乘 $p$ 倍单位、乘单位。对有限剩余商使用核/余核的计数，并利用局部 $\pi$ 挠点为零，得到
$$
\#\bigl(E(K_{\mathfrak p})/\pi E(K_{\mathfrak p})\bigr)=p,
\qquad
E(K_{\bar{\mathfrak p}})/\pi E(K_{\bar{\mathfrak p}})=0.
$$
Kummer 映射是单射，所以在维数为 $1$ 的两局部上同调空间中，$\pi$-Selmer 条件分别为
$$
H^1_f(K_{\mathfrak p},E[\pi])=H^1(K_{\mathfrak p},E[\pi]),
\qquad
H^1_f(K_{\bar{\mathfrak p}},E[\pi])=0.
$$
这对上述全部 $p$ 同时成立。因而“局部非异常性是否有无穷多个 $p$”并不是当前 CM 候选的障碍；仍需控制的是全局类在严格的 $\bar{\mathfrak p}$ 局部条件下的核。

## 7. 固定四次扩张去掉扭转后，目标进入哪个分块

一种值得实际检查的路线是将 $E$ 在固定扩张上化成基本 CM 曲线
$$
E_1:\ y^2=x^3-x.
$$
令 $\delta^4=17$、$F=K(\delta)$。由于 $17$ 在高斯整数中任一上方素点的赋值都是 $1$，$X^4-17$ 在该素点 Eisenstein，故 $[F:K]=4$。$K$ 含四次单位根，所以扩张为循环 Galois 扩张，取
$$
\sigma(\delta)=i\delta,\qquad \operatorname{Gal}(F/K)=\langle\sigma\rangle.
$$
对 $k=0,1,2,3$，记
$$
E_{17^k}:\ y^2=x^3-17^kx,
\qquad
\theta_k:E_{17^k}/F\xrightarrow{\sim}E_1/F,
\quad \theta_k(x,y)=\left(\frac{x}{\delta^{2k}},\frac{y}{\delta^{3k}}\right).
$$
直接作用于系数，得到
$$
{}^\sigma\theta_k=I^k\theta_k.
$$
这里 $I$ 在 $E_1$ 上仍为 $(x,y)\mapsto(-x,iy)$，且与 $\sigma$ 交换。

固定任意奇素数 $p$，令 $S=\Sha(E_1/F)[p^\infty]$。在 $S$ 上定义
$$
e_k=\frac14\sum_{j=0}^3 I^{-kj}\sigma^j,
\qquad S_k=e_kS=\{s\in S:\sigma s=I^ks\}.
$$
由于 $I^2=-1$，有限几何级数直接给出 $e_k^2=e_k$、$e_ke_l=0$（$k\ne l$）、$\sum_ke_k=1$，因而
$$
S=\bigoplus_{k=0}^3S_k.
$$

限制映射给出
$$
\Sha(E_{17^k}/K)[p^\infty]
\xrightarrow{\sim}
\Sha(E_{17^k}/F)[p^\infty]^{\operatorname{Gal}(F/K)}.
$$
这仍是第 2 节的限制/余限制证明，只把次数 $2$ 换成 $4$；$4$ 在奇 $p$-初等群上可逆。将此同构与 $\theta_k$ 复合，并使用 $^\sigma\theta_k=I^k\theta_k$，恰得到
$$
\Sha(E_{17^k}/K)[p^\infty]\xrightarrow{\sim}S_k.
$$
局部平凡性在域扩张与曲线同构下保持；反向下降的局部平凡性由局部限制/余限制复合为局部次数（它整除 $4$）保证。完全相同的证明适用于有限层及无穷层 Selmer 群。

**因此目标位于 $k=1$ 分块，而基域基本曲线的结论只位于 $k=0$ 分块。** 更具体地，$\operatorname{res}:\Sha(E_1/K)[p^\infty]\to S$ 的像为 $S_0$；范数
$$
N=1+\sigma+\sigma^2+\sigma^3
$$
在 $S_0$ 上为 $4$，在 $S_1,S_2,S_3$ 上均为零。对目标块 $S_1$，这只是恒等式 $1+I+I^2+I^3=0$。所以即使基域 $\Sha(E_1/K)$ 的有限性已知，也不会通过这些映射给出 $S_1$ 的有限性。

必须区分两个余核：限制到**不变部分**的余核被扩张次数消灭；限制到整个 $S$ 的余核却包含全部非平凡分块，不被次数 $4$ 自动消灭。混淆两者会制造一个假的“固定次数基变换继承有限性”论证。

有理点层面同样如此：$\theta_1$ 将秩 $2$ 的 $\mathbb Z[i]$-模 $E(K)$ 送入 $E_1(F)$ 的目标分块。因此去扭转没有把目标分块的秩降为零。在 $\ell$-进表示层面，这也是 Weil 限制的分解
$$
\operatorname{Res}_{F/K}(E_1)\sim_K
E_1\times E_{17}\times E_{17^2}\times E_{17^3}
$$
所表达的事实：上述四个投影是以 $4$ 为公分母的有理同源投影。相应的 $L$ 函数乘积中仍然含有 $L(E_{17}/K,s)$ 因子，不能将 $E_1/\mathbb Q$ 的低秩结论直接应用到 $E_1/F$。

## 8. 不同素数之间究竟有什么映射

若 $A$ 是 $p$-初等挠群、$B$ 是 $q$-初等挠群且 $p\ne q$，则任何阿贝尔群同态 $A\to B$ 都为零。事实上，一个元素的像同时被某个 $p^n$ 和某个 $q^m$ 消灭，而两整数互素。

因此，同源诱导的同态、限制和余限制在上述定义下都保持同一个素数；不能由它们构造一个把 $\Sha[2^\infty]$ 的有限性直接搬到 $\Sha[p^\infty]$ 的非零群同态。对于 $p\ne2$，$[1+i]$ 本来就是 $p$-初等部分上的自同构；它不会检测该部分的大小或余秩。

这只排除了“沿现成这些群同态传递 $2$ 下降结论”的具体路线。仍可能存在利用共同整结构、特殊值或统一局部条件的跨素数定理；那需要额外的算术输入，而不是从本节推出逻辑上的不可能性。进一步尝试及可变分圆域的具体单位/类群项记录在 `notes/2026-11-12-prime-comparison-attempt.md`。

## 9. 变化 $p$ 的一个具体类群公式

仍设 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$，并令
$$
M_p=K(E[p]),\qquad \Delta_p=\operatorname{Gal}(M_p/K).
$$
CM 作用与 Galois 作用交换，故 $\Delta_p$ 嵌入
$$
(\mathbb Z[i]/p)^\times\simeq\mathbb F_p^\times\times\mathbb F_p^\times.
$$
特别地，$|\Delta_p|$ 与 $p$ 互素，其指数整除 $p-1$。记它在 $E[\pi]$、$E[\bar\pi]$ 上的特征分别为 $\chi_\pi,\chi_{\bar\pi}$。Weil 配对给出 $\mu_p\subset M_p$ 及
$$
\chi_{\rm cyc}=\chi_\pi\chi_{\bar\pi}.
$$
对 $\mathbb F_p[\Delta_p]$-模 $N$，用 $N^\chi$ 表示 $\delta n=\chi(\delta)n$ 的特征子空间。

令 $S$ 为 $M_p$ 中所有位于 $2,17,p$ 上的有限素点，并定义
$$
V_S=\{a\in M_p^\times/M_p^{\times p}:\ v_w(a)\equiv0\pmod p\text{ for every }w\notin S\}.
$$
标准单位–理想列在这里具体为
$$
0\longrightarrow\mathcal O_{M_p,S}^\times/\mathcal O_{M_p,S}^{\times p}
\longrightarrow V_S
\longrightarrow\operatorname{Cl}(\mathcal O_{M_p,S})[p]\longrightarrow0.\tag{9.1}
$$
其最后一个映射把 $(a)=\mathfrak a^p$（忽略 $S$ 内素因子）送到 $[\mathfrak a]$；任意 $p$-挠理想类都可这样取得，而核恰是 $S$-单位平方类的 $p$ 次版本。这也给出 (9.1) 的直接证明。

### 9.1 为什么是 $\chi_{\bar\pi}$ 分量

由于 $|\Delta_p|$ 与 $p$ 互素，限制给出
$$
H^1(K,E[\pi])\simeq H^1(M_p,E[\pi])^{\Delta_p}.
$$
在 $M_p$ 上应用 Kummer 理论，系数 $E[\pi]$ 相对 $\mu_p$ 的扭转特征为
$$
\chi_\pi\chi_{\rm cyc}^{-1}=\chi_{\bar\pi}^{-1}.
$$
因此，右边同构于 $(M_p^\times/M_p^{\times p})^{\chi_{\bar\pi}}$。限制在 $2,17,p$ 之外无分歧的类后，恰得到 $V_S^{\chi_{\bar\pi}}$。这里所有子群和特征都随同一个 $p$ 定义，没有把不同系数特征混同。

### 9.2 单位分量的维数恰为 $1$

首先，$\chi_{\bar\pi}$ 在 $S$ 中各素点的分解群上都非平凡。对位于 $p$ 上的点，这由第 6 节的 $E(K_v)[p]=0$ 得到。对位于 $2$ 上的点，形式群是 pro-$2$ 群，剩余域为 $\mathbb F_2$；若好约化，有限约化群的阶至多为 $5$，若加性约化，连通部分的阶为 $2$，几何分支群的阶至多为 $4$。故没有 $p\ge13$ 的挠点。对位于 $17$ 上的点，曲线为加性约化，连通部分的阶为 $17$，分支群的阶至多为 $4$，所以在 $p\ne17$ 时同样没有 $p$ 挠点。因此 $E[\bar\pi]$ 没有相应局部不变向量。

其次，Dirichlet 的实对数嵌入把通常单位群的无挠部分（张量 $\mathbb R$）识别为复素点置换表示中去掉常数的一项。$K$ 是虚二次域，$\Delta_p$ 在 $M_p$ 的复素点上正则作用，所以这个表示是正则表示减去平凡表示。加入 $S$-单位，对应再加上各有限素点轨道的置换表示 $\operatorname{Ind}_{D_v}^{\Delta_p}1$。由于 $\chi_{\bar\pi}|_{D_v}\ne1$，后面这些项对该特征的重数均为零。

$\chi_{\bar\pi}$ 非平凡，故无挠单位部分中它的重数恰为 $1$。这在模 $p$ 后仍成立：$p\nmid|\Delta_p|$，所有特征的阶都整除 $p-1$，可在 $\mathbb Z_p$ 中作 Teichmüller 提升并用整幂等元分解。单位群中 $p$-幂单位根的模 $p$ 特征为 $\chi_{\rm cyc}$，与 $\chi_{\bar\pi}$ 不同，因为 $\chi_\pi$ 非平凡。所以最终
$$
\dim_{\mathbb F_p}
\left(\mathcal O_{M_p,S}^\times/\mathcal O_{M_p,S}^{\times p}\right)^{\chi_{\bar\pi}}=1.\tag{9.2}
$$
这里计算的是抽象代数单位群的表示重数，**没有**使用 Leopoldt 猜想或 $p$-adic 单位调节子的非退化。

### 9.3 精确维数关系

令
$$
c_p=\dim_{\mathbb F_p}\operatorname{Cl}(\mathcal O_{M_p,S})[p]^{\chi_{\bar\pi}}.
$$
因为取特征分量是正合函子，(9.1)–(9.2) 给出
$$
\dim_{\mathbb F_p}V_S^{\chi_{\bar\pi}}=1+c_p.
$$
第 6 节说明 $\mathfrak p$ 处没有额外局部限制，而 $\bar{\mathfrak p}$ 处要求局部化为零。位于 $2,17$ 上的局部 $H^1(K_v,E[\pi])$ 本身为零：上一小节已排除 $E[\pi]$ 与其 Tate 对偶 $E[\bar\pi]$ 的局部不变向量，再用剩余特征不等于 $p$ 的局部 Euler 特征与对偶即可。其他素点的好约化 Kummer 条件恰是无分歧条件。

因此有正合列（不声称最右端满射）
$$
0\longrightarrow\operatorname{Sel}_\pi(E/K)
\longrightarrow V_S^{\chi_{\bar\pi}}
\xrightarrow{\operatorname{loc}_{\bar{\mathfrak p}}}
H^1(K_{\bar{\mathfrak p}},E[\pi]).
$$
记最后一个映射的秩为 $\varepsilon_p\in\{0,1\}$，便得到具体公式
$$
\boxed{\displaystyle
\dim_{\mathbb F_p}\operatorname{Sel}_\pi(E/K)=1+c_p-\varepsilon_p.}\tag{9.3}
$$
R4 与第 5 节给出的两个 Mordell–Weil 维数强迫
$$
c_p\ge1+\varepsilon_p.
$$
尤其 $c_p\ge1$；试图把此类群分量对几乎所有 $p$ 直接证明为零，与已知的秩 $2$ 就已矛盾。下面利用已经证明的奇偶定理，把足够条件放宽到 $c_p\le2$。

### 9.4 完整类群与 $S$-类群在目标分量上相同

从通常类群到 $S$-类群的自然满射的核，由 $S$ 内素理想的类生成。它是各素点轨道的自由置换模
$$
\bigoplus_{v\mid2\cdot17\cdot p}
\mathbb Z[\Delta_p/D_v]
$$
的商。第 9.2 节已经证明 $\chi_{\bar\pi}|_{D_v}\ne1$，故上述模张量 $\mathbb Z_p$ 后，其 $\chi_{\bar\pi}$ 的 Teichmüller 提升分量为零。由于 $p\nmid|\Delta_p|$，该整特征投影是正合的。因此通常类群和 $S$-类群的 $p$-初等目标分量同构，特别有
$$
c_p=
\dim_{\mathbb F_p}\operatorname{Cl}(M_p)[p]^{\chi_{\bar\pi}}.\tag{9.4}
$$
这一步使用的是局部分解群上非平凡这一事实；不能对任意特征不加检查地删去 $S$。

### 9.5 不预设 $\Sha$ 有限的奇偶提升

记
$$
s_p=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q).
$$
第 4 节的有限层同构给出
$$
\operatorname{Sel}_p(E/\mathbb Q)
\xrightarrow[e_\pi\operatorname{res}]{\ \sim\ }
\operatorname{Sel}_\pi(E/K),\tag{9.5}
$$
其逆是先将 $\pi$ 分量包含到 $\operatorname{Sel}_p(E/K)$，再作余限制。确实，对 $\pi$ 分量内的 $x$，
$e_\pi\operatorname{res}\operatorname{cor}(x)=e_\pi(x+cx)=x$；反向复合为恒等式则由限制的单射性得到。局部 Kummer 条件在限制、范数和 CRT 投影下相容，所以这里同构的是 Selmer 群本身，而非仅仅系数模或全局 $H^1$。这不需要假设任何 $\Sha$ 有限。

R4 给出 $E(\mathbb Q)_{\rm tors}=\mathbb Z/2\mathbb Z$，因此 $E(\mathbb Q)[p]=0$。把 $\Sha(E/\mathbb Q)[p^\infty]$ 的最大可除子群记为
$$
D_p\simeq(\mathbb Q_p/\mathbb Z_p)^{t_p}.
$$
因为 $p$-Selmer 群有限，$\Sha[p^\infty]$ 是余有限型 $\mathbb Z_p$-模；故其商 $B_p=\Sha[p^\infty]/D_p$ 有限。可除群是内射阿贝尔群，从而该扩张在抽象群层面分裂，给出
$$
\dim_{\mathbb F_p}\Sha[p]=t_p+\dim_{\mathbb F_p}B_p[p].
$$
Cassels–Tate 配对在 $B_p$ 上非退化且交错，因此 $B_p$ 是若干对相同循环 $p$-群的直和，$\dim B_p[p]$ 为偶数。这里只对有限商 $B_p$ 使用非退化配对，没有假设 $D_p=0$。

Dokchitser–Dokchitser 的 $p$-奇偶定理（2010 年论文 Theorem 1.4，亦为 Theorem 4.19）对所有 $E/\mathbb Q$、所有 $p$ 成立，给出
$$
(-1)^{\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)}
=(-1)^{2+t_p}=w(E/\mathbb Q).
$$
`notes/2026-11-12-cm-local-inputs.md` 已用局部根数公式证明本曲线 $w(E/\mathbb Q)=+1$。故 $t_p$ 偶，而 Kummer 正合列给出
$$
s_p=2+t_p+\dim_{\mathbb F_p}B_p[p]\equiv0\pmod2.\tag{9.6}
$$
把 (9.3)、(9.5)、(9.6) 合起来，由 $\varepsilon_p\in\{0,1\}$ 得到更精确的公式
$$
\boxed{\displaystyle
s_p=2\left\lceil\frac{c_p}{2}\right\rceil,
\qquad
\varepsilon_p=
\begin{cases}
0,&c_p\text{ 为奇数},\\
1,&c_p\text{ 为偶数}.
\end{cases}}\tag{9.7}
$$
尤其，在本节素数范围内，
$$
\boxed{\quad
c_p\in\{1,2\}
\quad\Longleftrightarrow\quad
\operatorname{Sel}_p(E/\mathbb Q)\text{ 的维数为 }2
\quad\Longleftrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.
\quad}\tag{9.8}
$$
最后一步用秩恰为 $2$ 和 $E(\mathbb Q)[p]=0$：有限层 Kummer 列先给出 $\Sha[p]=0$；若一个 $p$-初等挠群非零，任意非零有限阶元素的适当 $p$ 次幂都会产生非零 $p$-挠元素，所以整个 $\Sha[p^\infty]$ 也为零。反向蕴含同样直接来自 Kummer 列。

因此，“对无穷多个分裂 $p$ 证明 (9.4) 的具体类群分量维数至多 $2$”足以完成主目标，而且会证明更强的 $p$-初等部分为零。**R7 没有证明这个无穷性断言。** 主目标仅要求有限性，所以 (9.8) 给出的仍是一个充分路线；不能把它升级为主目标的必要条件。

## 标准背景

所用一般事实为 Kummer 正合列、Galois 上同调的限制/余限制恒等式、局部对偶、Mordell–Weil 定理和 Dirichlet 单位定理；群同态的逆、局部条件相容性、CM 分量以及所有指数因子均已在正文写出。可参看 J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., 2006，以及 J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., 2009。

奇偶提升另外使用下列已发表结果：

- T. Dokchitser and V. Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, **Annals of Mathematics 172** (2010), 567–596, Theorems 1.4 and 4.19；[期刊全文](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n1-p11-p.pdf)，[DOI](https://doi.org/10.4007/annals.2010.172.567)。其中定理无条件证明 $p^\infty$-Selmer 余秩的奇偶性，并非假设 $\Sha$ 有限后才能使用的 Mordell–Weil 奇偶表述。
- B. Poonen and M. Stoll, *The Cassels–Tate pairing on polarized abelian varieties*, **Annals of Mathematics 150** (1999), 1109–1149；[作者全文](https://math.mit.edu/~poonen/papers/sha.pdf)，[DOI](https://doi.org/10.2307/121064)。其引言说明商去最大可除子群后的非退化性，以及椭圆曲线情形的交错性。

R7 不以尚未证明的猜想或现代预印本的推测作为论证步骤。
