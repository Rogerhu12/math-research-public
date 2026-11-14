# R239 附录：两组任意重数加一异常位的整个出生一全高度严格比较

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：完整有限模型定理。本文闭合此前全高度有界普通权比证明中剩余的 $\delta>0,B<0$ 区域；异常权和普通权比均不受限制。核心新步骤是实际可行域的 $K<2N/3$ 界，以及保留完整混合费用后的正二次式。本文证明的是下述整个 $K_1$，不外推到更高出生、一般多权或普通 ISP。

独立符号证书：[完整大权比符号证书](../notes/2026-11-14-birth-one-allheight-large-contrast-closure-check-0c.py)。它检查全部新有理恒等式和严格正括号；没有参数扫描、近似根或外部表。

## 1. 完整原空间定理

取 $q,L\ge1$ 个物理位的权分别为 $a,b$，另有一个物理位权为 $c$，三者均严格正。整体归一后写
$$z=a^2/b^2,\qquad w=c^2/b^2,\qquad
N_{\rm tot}=q+L,\qquad h=N_{\rm tot}-1.$$
总物理位数为 $N_{\rm tot}+1$。定义
$$F_j=\frac{D^j(D^*)^j}{(j!)^2}\bigg|_{\mathcal H_1},\qquad
K_1=\ker D\cap\mathcal H_1,\qquad
\Gamma_j=P_{K_1}F_j^{-1}|_{K_1}.$$
所有逆首先在完整物理层上取；不存在“先压缩原 Gram 再取逆”的替换。

**定理。** 对每个合法内部高度 $1\le n\le h-1$，在整个 $K_1$ 上严格有
$$\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1}.}\tag{1.1}$$
当 $h=1$ 时没有内部比较，陈述为空；其余所有合法边界均包括在内。

先处理已付范围。$\min(q,L)\le3$ 的所有高度由两异常权、三异常权及三位等权短串加一异常位的完整旧定理支付，准确来源与组交换方式列于 [第二边证明](R239-appendix-birth-one-two-group-singleton-second-and-penultimate-edges.md) §1。以下可取 $q,L\ge4$。

[任意正权第一边](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)、[第二与末第二边](R239-appendix-birth-one-two-group-singleton-second-and-penultimate-edges.md)、以及[第三与末第三边](R239-appendix-birth-one-two-group-singleton-third-and-antepenultimate-edges.md)（附可独立重建的完整整数证书），结合 [真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)，已经支付 $n\le3$ 或 $h-n\le3$。故新的内部证明只需
$$n\ge4,\qquad m=h-n\ge4.\tag{1.2}$$
特别 $h\le7$ 的全部边早已覆盖。以下的局部字母
$$M=m+1,\qquad N=n+1,\qquad H=M+N$$
与总位数 $N_{\rm tot}$ 不同；由 (1.2)，$M,N\ge5$。

## 2. 准确的三维全逆、二维压缩与实际三参数

两组内的标准子空间和三维群固定空间同时约化完整 $F_j$ 及其逆。压缩到 $K_1$ 后，得到同时约化全部 $\Gamma_j$ 的真实正交分解
$$K_1=V_{\rm short}\oplus V_{\rm pool}\oplus K_{\rm fix},\qquad\dim K_{\rm fix}=2.$$
固定二维块仍须先在原三维群固定空间取全逆后压缩；它本身不被声称约化原 $F_j$。

两个组内标准部分的 $F_j$ 标量分别为
$$e_j(z^{[q-2]},1^{[L]},w),\qquad e_j(z^{[q]},1^{[L-2]},w).$$
直接删位展开给这些值；严格 Newton 不等式支付其倒数的全部相邻严格 log 凸性。所以只剩同一个真实固定二维块。

用 [完整真空归约](R239-appendix-birth-one-two-group-singleton-vacuum-reduction.md) 和 [实际三正参数入口](R239-appendix-birth-one-actual-three-positive-parameter-normalization.md)。为明确这里用的是实际有限族，记
$$Z_j=[x^j](1+zx)^q(1+x)^L,\quad M_j=\Theta\log Z_j,\quad V_j=\Theta^2\log Z_j,\quad\Theta=z\partial_z.$$
先取 $z>1$。定义
$$p=\frac{q-M_n}{m+1},\quad r=\frac{M_{n+1}}{n+1},\quad
A=p(1-p),\quad B_0=r(1-r),\quad d=r-p,$$
$$\theta=\frac{V_{n+1}}{(n+1)B_0},\qquad
u=\frac{A(1-\theta)}{B_0\theta},\quad
\eta=\frac{d^2\theta}{A},\quad t=\frac\theta{1-\theta}.$$
这里的 $u$ 是既有规范四次式中的正参数，与异常物理权 $w$ 不同。实际入口给 $0<p<r<1,0<\theta<1$ 和
$$\alpha=n-u\eta>0,\qquad\beta=m-\eta>0,$$
$$J=u(m+2+\eta)-n>0,\qquad K=n+2-u(m-\eta)>0,$$
$$\delta=Mu-N,\qquad V=1+u+u\eta,\qquad J=V+\delta,\quad K=V-\delta.\tag{2.1}$$
其中 $K$ 是标量，不是原空间 $K_1$。

经过同一个源合同及逐高度的正几何因子后，实际三个相邻形式的高范数为
$$\left(\frac{m+2}{\alpha},\ 1,\ C,\ \frac{C(n+2)}\beta\right),\qquad C=N/M,$$
低范数为
$$\left(\frac1{uR},\ 1,\ u,\ \frac{u^2}T\right),$$
其中
$$\ell=\frac{nJ}{Mu\alpha},\quad k=\frac{mK}{N\beta},\qquad
R=\frac N{Mu}-\ell t,\quad T=\frac{Mu}N-\frac kt.$$
这些仍是同一实际有限多项式的范数，故 [两权全高度严格比较](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md) 给
$$\boxed{0<R<1,\qquad0<T<1,\qquad
JK<\frac{MNu\alpha\beta}{nm}.}\tag{2.2}$$
最后一式也直接由 $R,T>0$ 得到 $\ell k<1$。入口中的共同源合同与几何因子保留 (1.1)，没有逐层任意更换源。

## 3. 保留全部费用的四次式及已闭两个区域

在中心剪切消为零的同源坐标中，实际差为
$$\mathcal K=H_{n-1}-H_nH_{n+1}^{-1}H_n.$$
其首主子式严格正，来自高范数严格 log 凸与同正线性和的 Cauchy–Schwarz。完整行列式乘一个严格正分母后为异常权参数的四次多项式
$$\mathcal P(\omega)=\sum_{i=0}^4P_i\omega^i,\qquad\omega>0.$$
这里 $\omega$ 是入口中对 $w$ 的正重标；所有 shear 平方、交叉项和四次费用都保留。$P_0,P_4>0$ 来自真实高、低范数的严格相邻比较。

[规范中间系数定理](R239-appendix-birth-one-normalized-middle-quartic-positivity.md) 已证明 $P_2>0$ 对整个实际域成立。[有界普通权比全高度稿](R239-appendix-birth-one-bounded-ordinary-contrast-all-heights.md) §§3–5 的证明还给出如下不依赖权比的事实：

- $P_1>0$ 在 $\delta\le0$ 的整个域成立；
- 当 $n,m\ge3$ 时，$P_1>0$ 在 $B\ge0$ 的整个域成立，其中 $B$ 见下式；
- 规范倒数反射交换 $P_1,P_3$，且保持实际域。

为直接处理剩余域，写
$$H_+=H+N\eta,\qquad H_-=H+Mu\eta,$$
$$B=mH-N(M+1)\eta,\qquad G=2H+\eta(2N-K)>0,$$
$$D_1=\frac{\alpha\beta M^2N}{u}>0.$$
完整 $P_1$ 的准确 Laurent 身份为
$$\boxed{D_1RT P_1=uM\beta JH_+\,t-JKB-MN\delta G+
\frac{N(3m+2)KH_-}{t}.}\tag{3.1}$$
这来自通用完整四次式的逐系数身份，已在既有独立脚本核验。以下保留式中的所有项，不再以单独剪切费用的粗上界替换。

唯一剩余情形是
$$\delta>0,\qquad B<0,\qquad M,N\ge5.\tag{3.2}$$

## 4. 实际可行域的新严格上界 $K<2N/3$

从 (2.1) 得到准确重参数化
$$u=\frac{N+\delta}{M},\qquad u\beta=N+1-K,$$
$$M\alpha=N(M+1)-m\delta-MK,\qquad J=K+2\delta,$$
$$uH_+=NK+(N+1)\delta,\qquad H_-=MK+m\delta.\tag{4.1}$$
因为 $u,\beta>0$，有 $0<K<N+1$。把 (2.2) 的最后一式乘正因子，得到
$$F:=MN\alpha(N+1-K)-nmK(K+2\delta)>0.$$
准确展开为
$$F=F_0(K)-m\delta\{N(N+1)+(N-2)K\},\tag{4.2}$$
$$F_0(K)=(H-1)K^2-N(2MN+H)K+N^2(M+1)(N+1).$$
所以 $F_0(K)>0$。但 $F_0$ 是严格凸的二次式，并且
$$\boxed{F_0(2N/3)=-\frac{N^2}{9}
\{8(M-5)+8(N-5)+3(M-5)(N-5)\}\le0,}\tag{4.3}$$
$$F_0(N+1)=-nm(N+1)^2<0.$$
凸函数在这两个端点之间不超过连接端点的线段，因而在 $[2N/3,N+1]$ 非正。结合 $0<K<N+1$ 与 $F_0(K)>0$，严格得到
$$\boxed{K<2N/3.}\tag{4.4}$$
即使 $M=N=5$ 使 (4.3) 为零，严格的 $F_0(K)>0$ 仍排除等号。这里确实使用同一实际相位的正低范数约束，未把孤立的局部曲率 cap 当成充分条件。

## 5. 一个保留正补偿的二次式

先定义
$$S=2(3m+2)\beta H_--MmG.$$
用 (4.1) 精确展开：
$$\begin{aligned}
uS={}&K\{(4M^2-M+1)N+5M^2-M-(5M^2-M)K\}\\
&+m\delta\{(4M-2)(N+1)-(5M-1)K\}.
\end{aligned}\tag{5.1}$$
这里的 $u$ 即 §2 的正参数。由 (4.4)，第一个花括号严格大于
$$\frac{N(2M^2-M+3)}3+5M^2-M>0,$$
第二个花括号严格大于
$$\frac{(2M-4)N}3+4M-2>0.$$
所以
$$\boxed{S>0.}\tag{5.2}$$

现在使用实际条件 $0<T<1$。置
$$v=1-T\in(0,1),\qquad
 t=\frac{mK}{\beta(\delta+Nv)}.$$
该式直接来自 §2 的 $T$ 定义；$\delta+Nv>0$。将 (3.1) 乘这个正因子，恰得
$$\boxed{(\delta+Nv)D_1RT P_1=Q_0+Q_1v+Q_2v^2,}\tag{5.3}$$
其中
$$Q_2=\frac{N^3(3m+2)\beta H_-}{m}>0,$$
$$\boxed{Q_1=N\left[-JKB+\frac{N\delta}{m}S\right]>0.}\tag{5.4}$$
严格号分别使用 $B<0$、$J,K,\delta>0$ 和 (5.2)。被保留的 $-JKB$ 正补偿在此直接发挥作用。

常数项准确为
$$Q_0=uMmJH_+K-JKB\delta-MN\delta^2G+
\frac{N(3m+2)\beta H_-\delta^2}{m}.$$
它的正性不能从前式逐项读取，但有下列完整正分解：
$$\boxed{m(N+\delta)Q_0=C_0+C_1\delta+C_2\delta^2+C_3\delta^3,}\tag{5.5}$$
$$C_0=K^3MN^2m^2,$$
$$C_1=K^2MNm\{2MK+N(3M-5)-M-1\},$$
$$C_2=KMN\{(4M^2-8M+2)K+(3M^2-8M+7)N+2\},$$
$$C_3=MNm\{2K(M-2)+m(N+1)\}.$$
当 $M,N\ge5,K>0$ 时，四个系数均严格正。例如 $C_1$ 花括号不小于 $5(3M-5)-M-1=14M-26>0$；其余三个括号的各项显然严格正。因此 $Q_0>0$。

(5.3) 的三个系数全部严格正，故 $P_1>0$。这闭合 (3.2) 的整个剩余域；没有对 $t$ 或 $v$ 采样，也不需要再选择一个更窄的权比扇区。

## 6. 倒数反射、完整四次式和全空间拼接

规范反射为
$$(n,m,u,\eta,t,\omega)\longmapsto
(m,n,u^{-1},u\eta,t^{-1},\omega^{-1}).$$
它满足 $R'=T,T'=R$，并有完整系数身份
$$\mathcal P(\omega)=u^4C^2\omega^4\mathcal P'(\omega^{-1}),\qquad C=N/M.$$
所以新证明与 §3 已闭区域一起给 $P_1>0$ 的全域；应用同一事实于反射模型便得 $P_3>0$。所有五个系数因此严格正，对每个异常权 $w>0$ 都有 $\mathcal P(\omega)>0$。清分母因子严格正，故 $\det\mathcal K>0$。再用首主子式严格正，得到固定二维块的 (1.1)。两个组内标准部分已在 §2 支付，故整个 $K_1$ 严格成立。

$z=1$ 时，所有普通位合并成一个等权池，与异常位组成两权模型，直接由完整两权定理支付。$0<z<1$ 时交换普通组并统一缩放，参数成为 $(L,q,z^{-1},w/z)$；原物理置换、同一整体权缩放保持 (1.1)。小组大小及所有硬端已在 §1 的完整旧定理范围内，未用非法范数外推端点。

新符号证书逐一核 (4.1)–(4.3)、(5.1)、完整二次恒等式 (5.3) 和全部四系数 (5.5)，再以 $M=5+x,N=5+y$ 展开六个残余括号，核其全部非零系数严格正且常数项正。这是有限代数身份的核验；普遍性和严格性由上述解析域论证给出。

因此定理 1 完成。更高出生的一般二维族以及一般多种普通权仍是后续实际问题；本文不从这个有限出生一结论推出普通不变子空间问题。

## 独立复核记录

根代理全文核验了实际可行域、所有边界、完整三维逆与二维共同源拼接，并以[独立v二次恒等核验](../notes/2026-11-14-birth-one-allheight-independent-v-identity-check-0c.py)重建强K界、完整uS、Q0四系数和v二次身份，输出ALL_PASS。该核验与作者的六个严格正括号证书分别保留；普遍正性由正文的解析域证明给出。
