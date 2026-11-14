# R239 附录：合并约束的两参数递推、局部松弛反例与外一层必要条件

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

状态：已证明的代数重建、精确非实际反例与实际外层必要条件。本文不证明一般高度的完整相邻比较，普通 ISP 仍开放。完整 Fraction 证书见[独立脚本](../notes/2026-11-13-casimir-globalmean-relax-certificate-0c.py)。

## 1. 同一个实际源与局部归一

使用[完整 MP/shear](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)、[实际 Pearson](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)、[固定合并源方向](R239-appendix-fixed-merger-directions-and-actual-casimir-identities.md)。短组长为 $q_0=t+D-1$，长组长为 $L=t+N-D-1$，其中 $t\ge1$、$1\le D\le N/2$、$N=h+1$。两大组相对权为 $z>1$，异常位为 $w>0$。本稿先取
$$2\le n\le h-2,\qquad m=h-n\ge2,\qquad J=L+1=t+N-D.$$

将本地四个 $a$ 和四个 $b$ 同时除以同一正数 $b_{n-1}$，记
$$
(a_{n-1},a_n,a_{n+1},a_{n+2})=\beta(A,1,\alpha,B),\qquad
(b_{n-2},b_{n-1},b_n,b_{n+1})=(P^{-1},1,R,RT).
\tag{1.1}
$$
这是共同标量归一，不换源基。实际族满足
$$0<P<R<T,\quad P<\alpha<T,\quad A\alpha>1,\quad B>\alpha^2.$$
令 $\mu=-k_n$、$x=k_{n-1}-k_n$、$y=k_{n+1}-k_n$。Pearson 身份准确给
$$
A=\frac1R+\frac{z(m+1)}n(\alpha-P),\qquad
B=\alpha R+\frac{n+1}{zm}(1-\alpha/T),
\tag{1.2}
$$
$$
x=\frac{(z-1)\beta(P-\alpha)}n<0,\qquad
y=\frac{(z-1)\beta(1-\alpha/T)}{zmR}>0.
\tag{1.3}
$$
完整同源矩阵仍为
$$
H_j(w)=B_j(w)\begin{pmatrix}Q_j(w)+\mu_j^2&\mu_j\\\mu_j&1\end{pmatrix},
\quad
Q_j(w)=\frac{(a_j+wa_{j+1})(b_{j-1}+wb_j)}{wb_{j-1}b_j}.
$$
各个逆均先在完整物理层上取。

## 2. 实际相邻高度的两参数重建

固定方向身份为
$$
Q_j(1)=\mu_j(J-\mu_j),\qquad
Q_j(z)=(D+\mu_j)(t-\mu_j),\qquad 0<\mu_j<t.
\tag{2.1}
$$
在中心令
$$
u=\mu(J-\mu),\quad v=(D+\mu)(t-\mu),\quad E=u(1+zR)-v(1+R).
$$
两条中心身份是
$$\beta(1+\alpha)(1+R)/R=u,\qquad \beta(1+z\alpha)(1+zR)/(zR)=v.$$
解这两个线性方程得到
$$
\boxed{\beta=\frac{zRE}{(z-1)(1+R)(1+zR)},\qquad
\alpha=\frac{zv(1+R)-u(1+zR)}{zE}.}
\tag{2.2}
$$
实际 $\beta>0$，故 $E>0$。

令 $\sigma=J-2\mu$。因为 $\mu_{n-1}=\mu-x$、$\mu_{n+1}=\mu-y$，
$$
Q_n(1)-Q_{n-1}(1)=x\sigma+x^2,\qquad
Q_n(1)-Q_{n+1}(1)=y\sigma+y^2.
$$
将 (1.1)–(1.3) 代入并约去严格非零的 $x,y$，得
$$
\boxed{
P=\alpha+\frac{(z-1)\sigma-z(m+1)(1+\alpha)+n(1+1/R)}
{z(m+1)-\beta(z-1)^2/n}.
}
\tag{2.3}
$$
以及
$$
\boxed{
V:=1-\alpha/T=
\frac{(z-1)\sigma-zm(1+R)+(n+1)(1+\alpha)/\alpha}
{(n+1)/\alpha-\beta(z-1)^2/(zmR)},\qquad
T=\frac{\alpha}{1-V}.
}
\tag{2.4}
$$

两分母的正性已经支付。写 $\kappa=z/(z-1)^2$、$\lambda=\beta/\kappa$，实际单 Schur Toda 身份给
$$\lambda<n(m+1),\qquad \lambda\alpha/R<(n+1)m.$$
它们恰保证 (2.3)、(2.4) 的分母严格正；实际 $T>0$ 又给 $V<1$。

因此固定 $n,m,D,t,z$ 后，局部数据由 $(R,\mu)$ 唯一重建。向下一高度的实际状态准确为
$$
\boxed{(R_{n+1},\mu_{n+1})=(T,\mu-y),\qquad \beta_{n+1}=\beta\alpha/R.}
\tag{2.5}
$$
反向为 $(P,\mu-x)$、$\beta_{n-1}=\beta AP$。该结论不宣称任意初始 $(R,\mu)$ 都能正延拓到全部高度。

## 3. 任意异常权的精确表达

从 $Q_n(w)=a_n/(wb_n)+a_n/b_{n-1}+a_{n+1}/b_n+wa_{n+1}/b_{n-1}$，按 $1,z$ 两点插值：
$$
\boxed{
Q_n(w)=\mu(J-\mu)+\frac{w-1}{z-1}(Dt-N\mu)
+\frac{a_n}{b_n}\frac{(w-1)(w-z)}{wz}.
}
\tag{3.1}
$$
故 $H_{11}/B_n=Q_n(w)+\mu^2$ 中的 $\mu^2$ 消去。第三项在 $1<w<z$ 上为负；这不是未经证明的正矩阵分解。

## 4. 三点 Casimir、四 cap 和全部一阶均值仍不充分

取完全有理的参数
$$
n=12,\quad m=13,\quad N=26,\quad D=12,\quad t=5000,\quad z=403/400,
$$
$$
R=1213636691/10^9,\qquad \mu=1130318015927/500000000.
$$
按 (2.2)–(2.4) 准确有理重建其余数据。仅为识别方便，近似值为
$$
P\simeq0.6742560891,\quad T\simeq1.2138866910,\quad
\alpha\simeq0.9090961172,\quad \beta\simeq1787511.4357.
$$

[完整 Fraction 证书](../notes/2026-11-13-casimir-globalmean-relax-certificate-0c.py) 证明：

- 两个方向的 Pearson、合并第三耦合以及相邻三层的两条 (2.1) 全部准确成立；
- 本地四个 $a$ 和四个 $b$ 的全部相邻标量比较严格成立，且 $x<0<y$、$0<\mu-y<\mu<\mu-x<t$；
- 四个真实矩形 cap 严格成立：
  $$0<(a/p,b/q,c/r,d/s)_j<\kappa\frac{t\min(j,D)(N-\max(j,D))}{t+|j-D|},\quad j=n-1,\ldots,n+2;$$
- 全部 $0\le j\le N$ 的一阶均值端点、积分区间和内部严格离散凹性均可同时满足，并保局部三条 Pearson 均值差。

最后一项有明确全局补全。置
$$
f_n=(z-1)\beta\alpha+n\mu,\quad
f_{n-1}=f_n-(\mu-x),\quad f_{n+1}=f_n+\mu,\quad f_{n+2}=f_{n+1}+\mu-y.
$$
令 $l=n-1=11$、$r=n+2=14$，其余值为
$$f_j=(j/l)f_l+j(l-j)\quad(0\le j<l),$$
$$f_j=f_r+\frac{j-r}{N-r}(tD-f_r)+(j-r)(N-j)\quad(r<j\le N).$$
逐项有理运算给每个内部 $j$
$$
\max\left\{\frac{jtD}{N},\
t\min(j,D)-\frac{t\min(j,D)(N-\max(j,D))}{(z-1)(t+|j-D|)}
\right\}<f_j<t\min(j,D),
$$
$$2f_j>f_{j-1}+f_{j+1},\qquad f_0=0,\quad f_N=tD.$$
这些只是拟定的一阶导数数值，并非一组实际 Schur 参数函数。

尽管以上条件同时成立，完整四次分子仍准确满足
$$\boxed{\mathcal P(1/8000)<-20000.}\tag{4.1}$$
准确值为 $-408998164115217067902872842357129933851658966494435143477437585300863635916376902680343853099512996439349869928033516702634955851462229552805486421902582570409952150981783927289$ 除以正整数 $19850782162956856235706568960322338313033649834037197817478296231839384925151847832718102288404097280000000000000000000000000000000000000000000000000000000000000000000000000$。脚本直接从有理输入重算此值，并核分母与首末系数为正；不依赖浮点判断。

因此所列必要条件的合取仍不充分。此反例不是实际有限权族，亦不否定原相邻 Gram 猜想。

## 5. 实际族的外一层必要条件

设 $P_-=b_{n-2}/b_{n-3}$。在 (2.3) 中换成前一层：
$$
n\mapsto n-1,\quad m\mapsto m+1,\quad R\mapsto P,\quad
\alpha\mapsto1/A,\quad \beta\mapsto\beta AP,\quad \sigma\mapsto\sigma+2x.
$$
再用中心的 (2.3)，直接展开得到
$$
\boxed{
\mathcal E_-=z(1+P)+1+\frac nR-\frac{n-1}{P}
-z\lambda\left[\frac{P(AP-1)}{n-1}+\frac{P-\alpha}{n}\right]
=z\left(m+2-\frac{\lambda AP}{n-1}\right)(P-P_-).
}
\tag{5.1}
$$
真正前一层的曲率界为 $\lambda AP<(n-1)(m+2)$，所以右侧乘子严格正。实际完整下范数序列的严格标量比较又给 $P_-<P$，从而
$$\boxed{\mathcal E_->0.}\tag{5.2}$$
$n=2$ 时按实际缺失低层 $b_{-1}=\infty$ 读取 $P_-=0$；式中只除原 $P>0$。

右侧对应条件由[完整倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)得到，在 (5.1) 左式中作
$$
(n,m,z,P,R,T,\alpha,\lambda,A,B)
\mapsto(m,n,z^{-1},T^{-1},R^{-1},P^{-1},\alpha^{-1},\lambda\alpha/R,B/\alpha,A/\alpha).
$$
它是另一正乘子乘 $T^{-1}-T_+^{-1}$，其中 $T_+=b_{n+2}/b_{n+1}>T$。$m=2$ 时 $T_+=\infty$，读取倒数为零。

§4 的准确数据却满足 $\mathcal E_-<-1/10$，故其前一层必有 $P_->P$；近似为
$$P_-\simeq0.6958656409>P\simeq0.6742560891.$$
这给出了具体的非实际性原因，并显示为何必须保留继续延拓的信息。

## 6. 首个中间系数的一元二次归约

令 $U=\alpha-P$、$V=1-\alpha/T$。完整四次分子的 $w$ 系数除以正数 $\beta^2R/P$ 后准确为
$$
\mathcal F_1=R(A\alpha-1)(T-P)+(AB-\alpha)(T-R)
-\lambda\left[\frac{zR\alpha U^2}{n^2}+\frac{ATV^2}{zm^2}-\frac{2TUV}{nm}\right].
\tag{6.1}
$$
第三合并耦合给
$$
\lambda=mn\frac{cT-(n+1)}{dT-e},\quad
c=z[mR-(m+1)P]+n/R-(z+1),\quad d=mzU+n/R,\quad e=n\alpha/R.
$$
$U>0,T>\alpha$ 保证 $dT-e>0$。

置 $\gamma=(n+1)/(zm)$，定义
$$a_1=R(A\alpha-1)+A(\alpha R+\gamma)-\alpha,$$
$$a_0=-RP(A\alpha-1)-R[A(\alpha R+\gamma)-\alpha]-A\gamma\alpha,\qquad a_{-1}=A\gamma\alpha R,$$
$$j_1=A/(zm^2)-2U/(nm),$$
$$j_0=zR\alpha U^2/n^2-2A\alpha/(zm^2)+2U\alpha/(nm),\qquad j_{-1}=A\alpha^2/(zm^2).$$
直接展开得
$$
\boxed{\mathcal F_1=\frac{c_2T^2+c_1T+c_0}{dT-e},}
\tag{6.2}
$$
其中
$$c_2=da_1-mncj_1,$$
$$c_1=da_0-ea_1-mncj_0+mn(n+1)j_1,$$
$$c_0=da_{-1}-ea_0-mncj_{-1}+mn(n+1)j_0.$$
潜在的 $1/T$ 项严格消失，因为 $ea_{-1}=mn(n+1)j_{-1}$。同时 $(dT-e)\mathcal E_-$ 关于 $T$ 仅为一次式。

这是一条降低代数复杂度的准确身份，并未证明二次式的正号。剩余任务是用真实外层约束或更长递推支付它的符号，同时控制另外两个中间系数及所有硬端。有限扫描不替代这一证明。
