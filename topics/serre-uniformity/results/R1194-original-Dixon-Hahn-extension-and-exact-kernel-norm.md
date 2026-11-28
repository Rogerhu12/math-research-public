# R1194：原 Dixon 零谱块的 Hahn 扩大与准确核范数

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126。

## 1. 结论与原对象

保持 [原 Dixon/Hesse 推导](../notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)
(J.19)–(J.37) 的曲线、导子、谱参数及边界。令
$$
p=6N+5>37,\qquad \ell=2N+1,\qquad M=4N+2=2\ell.
\tag{1194.1}
$$
本篇给出同一个零谱核向量的显式扩大：
$$
v_j={}_3F_2\left(\begin{matrix}-\ell,\ell+1,-j\\1,-M\end{matrix};1\right),
\qquad 0\le j\le M.
\tag{1194.2}
$$
这里是有限多项式；所有实际分母均为 $p$ 单位。
它在 $0\le j<\ell$ 恰为原来的 $q_j(0)$，并且
$$
\boxed{\quad
\sum_{j=0}^{\ell-1}q_j(0)^2
=-\frac{\ell!}{2(M+1)(M!)^2}\ne0\quad\text{in }\mathbf F_p.
\quad}
\tag{1194.3}
$$
这付清一个新的准确无权范数。原短谱导数则准确读
$$
\sum_{j=0}^{N-1}\frac{q_j(0)^2}{3j+2};
\tag{1194.4}
$$
§6 保留其全部权重和归一。因此本篇不把 (1194.3) 当作原 $K_4$ 单位，
也不据全块的零根简单性关闭原两个指定障碍。

## 2. 从原矩阵逐行得到扩大算子

置 $a_j=3j+2$。原 (J.35) 在 $(\lambda,w)=(0,0)$ 的三条对角线为
$$
\mathcal Q_{j,j}=-2a_j(a_j^2+1),\quad
\mathcal Q_{j,j-1}=a_j(a_j-1)(a_j-2),\quad
\mathcal Q_{j,j+1}=a_j(a_j+1)(a_j+2).
\tag{1194.5}
$$
原范围为 $0\le j<\ell$；其中 $a_j\ne0$。
把第 $j$ 行除以 $9a_j$，并使用
$$
M\equiv-\frac43\pmod p,
$$
得到
$$
\begin{aligned}
B_j&=(j+1)(j-M)=(j+1)(j+4/3),\\
D_j&=j(j-M-1)=j(j+1/3),\\
(\mathscr L f)(j)
&=B_j\{f(j+1)-f(j)\}+D_j\{f(j-1)-f(j)\},\\
\mathscr H&=\mathscr L+2/9.
\end{aligned}
\tag{1194.6}
$$
例如 $B_j+D_j=(2a_j^2+4)/9$，所以对角线确为
$-(B_j+D_j)+2/9=-2(a_j^2+1)/9$。
上下两条对角线也正是 (1194.5) 除以 $9a_j$。

现在把 (1194.6) 定义在全部 $j=0,\ldots,M$ 上。
$D_0=B_M=0$ 给出这次扩大的真实两个端点；不需要越界值。
而
$$
B_j=D_{j+1}\qquad(0\le j<M),
\tag{1194.7}
$$
所以 $\mathscr H$ 是标准坐标内的对称矩阵。
这只是原矩阵在零谱处的逐行归一和扩大；对一般 $\lambda$，
原行归一后的谱项是 $\lambda/(9a_j)$，并不是 $\lambda I$。
尤其不能据此把原幂零谱问题换成 $\mathscr H$ 的普通谱问题。

## 3. 扩大全块的零根恰为简单根

因 $M<p$，次数至多 $M$ 的多项式在 $0,\ldots,M$ 的评价是同构。
直接展开差分可见 $\mathscr L$ 保持次数过滤，且在次数 $n$ 的最高项上
作用为 $n(n+1)$。例如 $B_j-D_j=2j-M$；
二阶差分的最高项再贡献 $n(n-1)$，合为 $n(n+1)$。
故
$$
\det(zI-\mathscr H)
=\prod_{n=0}^M\{z-n(n+1)-2/9\}.
\tag{1194.8}
$$
零特征值要求 $(3n+1)(3n+2)=0$。
两个剩余类的最小非负代表分别是
$$
n=\ell=2N+1,\qquad n=M+1=4N+3.
$$
后者不在 $0\le n\le M$，前者恰出现一次。
因此零根的代数重数与几何重数均为一。
这里不要求其他特征值互异。

还有一个不需范数公式的非零证明：若非零核向量 $v$ 满足
$v^{\mathsf t}v=0$，则由对称性
$v\in(\ker\mathscr H)^\perp=\operatorname{im}\mathscr H$。
于是有 $w$ 使 $\mathscr H w=v$，产生长度至少二的零特征 Jordan 链，
与上述代数重数一矛盾。以下进一步付清范数的准确值。

## 4. 有限多项式、反射及与原核的准确识别

对 $0\le i\le M$ 置
$$
\phi_i(j)=\frac{(-j)_i}{(-M)_i},\qquad \phi_0=1,
$$
其中 $(x)_i$ 是上升阶乘。逐项差分给
$$
\mathscr L\phi_i=i(i+1)\phi_i-i^2\phi_{i-1}
\quad(i\ge1),\qquad \mathscr L\phi_0=0.
\tag{1194.9}
$$
因此对任意整数 $0\le n\le M$，在特征零先定义
$$
V_n(j)=\sum_{i=0}^n
\frac{(-n)_i(n+1)_i}{(i!)^2}\,\phi_i(j).
\tag{1194.10}
$$
相邻系数之比为 $(i-n)(i+n+1)/(i+1)^2$；代入 (1194.9) 即得
$\mathscr L V_n=n(n+1)V_n$，并且 $V_n(0)=1$。
现在取 $n=\ell$ 并模 $p$：
$i!$、$(-M)_i$ 及 $(\ell+1)_\ell$ 所用整数均小于 $p$，
所以这一步合法，次数仍为 $\ell$，且 $v_j=V_\ell(j)$ 是 (1194.2) 的核。

反射 $j\mapsto M-j$ 交换 $B$ 与 $D$，因而与 $\mathscr H$ 交换。
核一维，$V_\ell(M-j)$ 的最高项是 $(-1)^\ell$ 倍；$\ell$ 为奇数，故
$$
v_{M-j}=-v_j,\qquad v_\ell=0.
\tag{1194.11}
$$
原 (J.20) 在 $\lambda=0$，正是
$(\mathscr Hq)(j)=0$ 的同一递推。
起点 $q_0=1=v_0$，左越界系数为零；
在 $0\le j<\ell$，用于递推到 $j+1$ 的 $B_j$ 全部非零。
因此
$$
v_j=q_j(0)\quad(0\le j\le\ell),\qquad q_\ell(0)=0.
\tag{1194.12}
$$
这同时核定了零谱识别和中点边界；没有更换原 $q_N$。

## 5. Rodrigues 与有限求和给出准确范数

为使公式自足，本节先在 $\mathbf Q$ 对整数 $0\le n\le M$ 证明。
用下降阶乘记
$$
R_n(j)=j^{\underline n}(j-M-1)^{\underline n},\qquad
\widetilde V_n(j)=\frac{\Delta^nR_n(j)}{n!(-M)_n},
\quad\Delta f(j)=f(j+1)-f(j).
\tag{1194.13}
$$
$R_n$ 在 $0,\ldots,n-1$ 和 $M+1,\ldots,M+n$ 全为零。
特别 $\Delta^nR_n(0)=R_n(n)=n!(-M)_n$，故
$\widetilde V_n(0)=1$。其次数为 $n$，最高系数为
$$
c_n=\frac{(2n)!}{(n!)^2(-M)_n}.
\tag{1194.14}
$$

展开差分并令 $k=j+i$，两端的零值精确消去全部边界，给出
$$
\sum_{j=0}^M P(j)\Delta^nR_n(j)
=(-1)^n\sum_{k=n}^M R_n(k)\nabla^nP(k),
\quad \nabla P(k)=P(k)-P(k-1).
\tag{1194.15}
$$
因此 $\widetilde V_n$ 与所有次数小于 $n$ 的多项式正交。
由 $\mathscr L$ 的对称性和次数过滤，
$(\mathscr L-n(n+1))\widetilde V_n$ 次数小于 $n$，
同时与全部该次数空间正交；在特征零的有限正定内积下它只能为零。
特征零的 $n(n+1)$ 在 $0,\ldots,M$ 中单重，
再用原点归一即得 $\widetilde V_n=V_n$。
本段的正定性仅用来证明一个特征零多项式身份，
没有对有限域中的原短范数使用正性。

在 (1194.15) 中取 $P=V_n$，有 $\nabla^nV_n=n!c_n$。
另一方面
$$
R_n(k)=(-1)^n(n!)^2
\binom{k}{n}\binom{M+n-k}{n},
$$
而 Vandermonde 求和给
$$
\sum_{k=n}^M\binom{k}{n}\binom{M+n-k}{n}
=\binom{M+n+1}{2n+1}.
$$
后一个身份也可逐个选择大小为 $2n+1$ 的子集，按其中第 $n+1$ 个元素划分，
所以包含了全部两个端点。
代回并使用 $(-M)_n=(-1)^nM!/(M-n)!$，得到
$$
\boxed{\quad
\sum_{j=0}^M V_n(j)^2
=\frac{(M+n+1)!(M-n)!}{(2n+1)(M!)^2}.
\quad}
\tag{1194.16}
$$
现在只在 $n=\ell,\ M=2\ell$ 这一安全位置约化。
因为 $M+n+1=p-1$、$M-n=\ell$，(1194.16) 的所有分母为 $p$ 单位。
Wilson 给
$$
\sum_{j=0}^M v_j^2
=-\frac{\ell!}{(M+1)(M!)^2}\ne0.
\tag{1194.17}
$$
由 (1194.11)，左右两半范数相同，中点贡献零；除以二即为 (1194.3)。
没有把 (1194.16) 在分母或分子越过 $p$ 的其他位置无条件约化。

## 6. 原短谱导数的权重不能删去

假设原第一障碍 $e=0$。由原 (J.26)，这等价于 $q_N(0)=0$。
记原 $N$ 阶左主块为 $Q_N(\lambda)$，
$$
\mathbf q(\lambda)=(q_0(\lambda),\ldots,q_{N-1}(\lambda))^{\mathsf t},
\quad A_N=\operatorname{diag}(3j+2)_{j=0}^{N-1}.
$$
其末行的真实越界项为
$u_{N-1}q_N(\lambda)$，其中
$u_{N-1}=(3N-1)(3N)(3N+1)$；所以
$$
Q_N(\lambda)\mathbf q(\lambda)
=-u_{N-1}q_N(\lambda)e_{N-1}.
\tag{1194.18}
$$
矩阵 $A_N^{-1}Q_N(0)$ 对称，
故 $\mathbf q(0)^{\mathsf t}A_N^{-1}$ 是左核向量。
对 (1194.18) 在零处求导，再乘这个左核向量，得到准确身份
$$
\boxed{\quad
\sum_{j=0}^{N-1}\frac{q_j(0)^2}{3j+2}
=-(3N)(3N+1)q_{N-1}(0)q_N'(0).
\quad}
\tag{1194.19}
$$
$q_{N-1}(0)\ne0$：否则与 $q_N(0)=0$ 一起沿非零三项系数反推，
会给 $q_0(0)=0$。其余显示因子也全是单位。
因此在 $e=0$ 下，原第二障碍的消失准确等价于 (1194.19) 左边为零。
与原符号的连接仍是 (J.27)：
$$
q_N'(0)=\frac{\delta}{6\Gamma}\nu_k,
\quad k=N+1,\quad\Gamma=(2v)^{2k},
\quad K_4=-\frac{\delta^3}{4v^2}\nu_k.
\tag{1194.20}
$$
这里 $v$ 是原 Weierstrass 常数；不与本篇带指标的 $v_j$ 混同。

(1194.3) 的无权和有 $\ell$ 项，(1194.19) 的带权和只有 $N$ 项。
原完整 Hesse 正常导数又另含 $A_N^2$，见 (J.37)。
三者各有实际来源，当前没有证明它们可相互替代。

## 7. 第一障碍下的四段与明确剩余问题

把 $V_\ell(j)$ 写成变量 $a=3j+2$ 的多项式 $P(a)$。
反射 (1194.11) 成为 $P(-a)=-P(a)$，故 $P$ 为奇多项式。
而 $j=N$ 对应 $a=(p-1)/2=-1/2$。
因此
$$
e=0\quad\Longrightarrow\quad a(a^2-1/4)\mid P(a).
\tag{1194.21}
$$
扩大核在 $j=N,\ell,3N+2$ 三处为零，余下四段各有 $N$ 个点：
$$
[0,N-1],\quad[N+1,2N],\quad[2N+2,3N+1],\quad[3N+3,4N+2].
$$
反射只把外两段、内两段分别配对；它保持平方而把 $a$ 变成 $-a$。
故不能利用该反射删掉 (1194.19) 的 $1/a$ 权重。
当前可继续的精确问题是：在同一原多项式、真实切点和完整递推下，
能否把 (1194.19) 的消失送到与 (1194.3) 冲突的等式，
或由同一实际来源给出另一项横截单位。
原 $e,K_4$ 共同非零和课题主要完成标准均仍开放。

## 8. 核定与范围

所有矩阵、分母、两端差分、范数和短谱归一均在文中证明。
o1_theta 独立纸核了逐行扩大、反射、唯一零根与 Rodrigues 范数常数；
root 按原 (J.20)、(J.35)–(J.37) 核对了对象和谱权重。
没有运行数学程序、增加素数窗口或重做已登记的 Hesse 全行列式。
本篇新增的是原零谱核的 Hahn 扩大与准确无权范数，
不是有限域上的一般正交多项式简单根论断。


## 9. 原谱导数的偶 companion 与完整差分行列式

日期：2026-11-28；o1_theta / root。本节继续同一个原零谱核。以下原来源恒等式已逐式证明；它们不证明原 $e,K_4$ 不同时为零。

### 9.1. 同一个零谱核及其偶 companion

置
$$
p=6k-1\ge41,\qquad N=k-1,\qquad \ell=2N+1=2k-1,
\qquad M=2\ell,
$$
并在 $\mathbf F_p[a]$ 上定义
$$
\mathcal L h(a)
=(a+1)(a+2)h(a+3)+(a-1)(a-2)h(a-3)
 -2(a^2+1)h(a).
\tag{HC.1}
$$
R1194 的准确 Hahn 核记为 $v(a)$，归一为 $v(2)=1$。它是次数恰为 $\ell$ 的奇多项式，并满足 $\mathcal L v=0$。在 $a_j=3j+2$ 上，原 Dixon 短谱递推恰为
$$
\lambda q_j(\lambda)+a_j\mathcal L q(\lambda)(a_j)=0,
\qquad q_{-1}=0,\quad q_0=1;
\qquad v(a_j)=q_j(0).
\tag{HC.2}
$$
这里 $\mathcal L$ 在序列上的含义是 (HC.1) 的相邻三项；不假设一般 $q_j(\lambda)$ 已来自一个低次 $a$ 多项式。

算子 $\mathcal L$ 保持奇偶与次数，且在 $a^d$ 上的最高系数为
$$
9d(d+1)+2=(3d+1)(3d+2).
$$
对偶数 $0\le d\le\ell-1$，两个正整数 $3d+1,3d+2$ 均小于 $p$。因此存在唯一偶多项式
$$
\boxed{\quad
w\in\mathbf F_p[a]_{\le\ell-1},\qquad
\mathcal Lw=-\frac{v(a)}a.
\quad}
\tag{HC.3}
$$
右侧确为多项式，因为 $v$ 为奇函数。若 $c_\ell=[a^\ell]v$，则
$$
\deg w=\ell-1,\qquad [a^{\ell-1}]w=-c_\ell/12.
\tag{HC.4}
$$
这是因为最后的次数对角是
$(3\ell-2)(3\ell-1)=(p-4)(p-3)=12$。

对 (HC.2) 作真正的谱参数微分，得
$\mathcal Lq'(0)(a_j)=-v(a_j)/a_j$。原 $j=0$ 行的下邻系数为零，其上邻系数非零；对 $0\le j<\ell$ 的上邻系数也均非零。因此初值及逐行递推准确锁定
$$
\boxed{\quad
q_j'(0)=w(a_j)-w(2)v(a_j),\qquad 0\le j\le\ell.
\quad}
\tag{HC.5}
$$
本式不把正常参数导数换为谱导数。最高 $j=\ell$ 由最后一条实际递推得到，未丢弃端点。

原完整块已经支付 $q_\ell(\lambda)=u\lambda^\ell$，其中 $u\ne0$；又 $a_\ell=p=0$、$v(0)=0$、$\ell>1$。在 (HC.5) 中代入 $j=\ell$，得到
$$
\boxed{w(0)=0.}
\tag{HC.6}
$$
故可唯一写成
$$
v(a)=aP(a^2),\qquad w(a)=a^2Q(a^2),
\qquad \deg P=N,\quad\deg Q=N-1.
\tag{HC.7}
$$
两者最高系数均为单位。

### 9.2. 原 $e,K_4$ 的完整读取

保持原 $E:V^2=U^3+v_0^2$ 的常数 $v_0$、$\delta$，并记
$\Gamma=(2v_0)^{2k}$。本节把椭圆常数写成 $v_0$，以免与上面的 Hahn 多项式 $v(a)$ 混同。

原 Dixon/Jordan J.26 与原 Fermat 六次 G4.87 已支付
$$
e=-\frac{\delta\Gamma}{2v_0}q_N(0),\qquad
K_4=-\frac{3\delta^2\Gamma}{2v_0^2}q_N'(0).
$$
第二式是 G4.87 前已付的无条件第四层身份，不需要预先假设 $e=0$。由于 $a_N=3N+2=-1/2$，(HC.5) 给
$$
\boxed{\begin{aligned}
e&=-\frac{\delta\Gamma}{2v_0}v(-1/2),\\
K_4&=-\frac{3\delta^2\Gamma}{2v_0^2}
       \{w(-1/2)-w(2)v(-1/2)\}.
\end{aligned}}
\tag{HC.8}
$$
全部外因子为原来源的单位。特别
$$
\boxed{\quad e=K_4=0
\iff v(-1/2)=w(-1/2)=0
\iff P(1/4)=Q(1/4)=0.\quad}
\tag{HC.9}
$$
这是同一个原谱导数的多项式实现；尚未证明 $P,Q$ 在该点没有共同零。

### 9.3. 普通第二类 Hahn 多项式的准确源

令 $b_j=3j+2$，$0\le j\le M$，以及
$$
F(a)=\prod_{j=0}^M(a-b_j),\qquad
S(a)=\frac{F'(a)}{F(a)},\qquad
W(a)=\sum_{j=0}^M\frac{v(a)-v(b_j)}{a-b_j}.
\tag{HC.10}
$$
$W$ 是实际多项式。两个端点在 $\mathbf F_p$ 中是 $b_0=2$、$b_M=-2$，所以
$$
\frac{F(a+3)}{F(a)}=\frac{a+1}{a+2},\qquad
S(a+3)-S(a)=\frac1{(a+1)(a+2)},
$$
$$
S(a-3)-S(a)=-\frac1{(a-1)(a-2)}.
\tag{HC.11}
$$
对核 $K(a,b)=1/(a-b)$，直接通分给
$\mathcal L_aK=\mathcal L_bK$：两正移位系数之差分别是
$(a+b)(a-b+3)$ 和 $(a+b)(a-b-3)$，恰消去中央项。
格点矩阵真对称，因为
$(b_j+1)(b_j+2)=(b_{j+1}-1)(b_{j+1}-2)$；两外端项均为零。
故对 $T(a)=\sum_jv(b_j)/(a-b_j)$，完整有限分部求和给 $\mathcal LT=0$。
再以 $W=vS-T$ 及 (HC.11) 计算，得到
$$
\boxed{\quad \mathcal LW=v(a+3)-v(a-3).\quad}
\tag{HC.12}
$$
所以普通第二类多项式的方程与 (HC.3) 不同；不能把它与 $v$ 的经典互素性用于原 $w$。

### 9.4. 实际 companion 的差分行列式

定义
$$
\mathscr C(a)=v(a)w(a+3)-w(a)v(a+3).
$$
由 $\mathcal Lv=0$、$\mathcal Lw=-v/a$ 直接相减，得
$$
\boxed{\quad
(a+1)(a+2)\mathscr C(a)
 -(a-1)(a-2)\mathscr C(a-3)
=-\frac{v(a)^2}{a}.
\quad}
\tag{HC.13}
$$
奇偶性与 (HC.4) 还给
$$
\mathscr C(-a-3)=\mathscr C(a),\quad
\deg\mathscr C=2\ell-2,\quad
[a^{2\ell-2}]\mathscr C=c_\ell^2/4,\quad
\mathscr C(2)=-1/24.
\tag{HC.14}
$$
最后一式是 (HC.13) 的实际左端点，使用 $v(2)=1$；没有把全无权 Hahn 范数换成原短谱范数。

若原共同零成立，则 $a^2-1/4$ 同时整除 $v,w$，因而
$$
(a^2-1/4)((a+3)^2-1/4)\mid\mathscr C(a).
\tag{HC.15}
$$
反之，在 $v(-1/2)=0$ 的分支，原不可约三项递推迫
$v(5/2)\ne0$（否则两个相邻零将递推回 $v(2)=0$）。所以
$\mathscr C(-1/2)=0$ 精确等价于 $w(-1/2)=0$。

还可保留一个完全多项式的写法。由 (HC.14) 存在唯一
$R$ 使 $\mathscr C(a)=R((a+3/2)^2)$；置
$S_0(z)=(z-1/4)R(z)$。则
$$
S_0((a+3/2)^2)-S_0((a-3/2)^2)
=-aP(a^2)^2,
\tag{HC.16}
$$
且
$$
\deg S_0=\ell,\quad S_0(1/4)=0,\quad S_0(49/4)=-1/2.
$$
原共同零进一步给 $S_0(1)=S_0(4)=0$。现有次数容许这些零点，故本式不自行产生矛盾。

### 9.5. 同一 Wilson–Newton 基的有限逆方程

以下仅是 (HC.1) 的直接展开，不引用一般 Wilson 多项式识别。令
$$
z=a/3,\qquad E_r=(1/3+z)_r(1/3-z)_r.
$$
将两次移位的 Pochhammer 比代入并通分，可逐项得到
$$
\mathcal LE_r
=(6r+1)(6r+2)E_r
 -36r^2(r-2/3)(r-1/6)E_{r-1}.
\tag{HC.17}
$$
在奇 sector 写 $\mathcal L(af)=a\mathcal L_{\rm odd}f$，则
$$
\mathcal L_{\rm odd}E_r
=(6r+4)(6r+5)E_r
 -36r^2(r+1/3)(r-1/6)E_{r-1}.
\tag{HC.18}
$$
因 $N=(p-5)/6$，(HC.18) 的最后一个次数对角为零。递推给唯一标量 $K\ne0$ 使
$$
\frac{v(a)}a
=K\sum_{r=0}^N p_rE_r,\qquad
p_r=\frac{(2/3)_r}{(4/3)_r(r!)^2}.
\tag{HC.19}
$$
此有限式的每个 $p_r$ 均为单位。若
$w=K\sum_{r=0}^Np_rt_rE_r$，(HC.3) 准确等价于
$$
\boxed{\quad
(r+1/6)t_r
-\frac{(r+5/6)(r+2/3)}{r+4/3}t_{r+1}
=-\frac1{36(r+1/3)},\qquad
t_N=-\frac1{12}.
\quad}
\tag{HC.20}
$$
递推实际在 $r=N-1,\ldots,0$ 向下使用；所有所除因子均为单位。
在原标记点 $a=-1/2$，$E_r=(1/6)_r(1/2)_r$，因此 (HC.19)–(HC.20) 仍准确读取原两槽。
这里保留了真实非齐次逆方程，没有把它未经证明认作某一个齐次 Wilson 参数移位。

以上没有数学程序执行，也没有旧素数窗口重跑。偶 companion 的唯一性、最高项和原两个谱 jet 已由 o2_high_coefficient 独立纸核；其余显示式在本文自足推导。下一缺口仍是 (HC.9) 的指定共同零排除，而不是全无权范数或普通第二类多项式的互素性。


root 全文逐式核对 HC.1–20，并重读原 G4.86–87 核准无条件 K4 尺度；原核、差分端点、Casoratian 和非齐次 Wilson–Newton 方程均按显示式保留。


### 9.6. 原逆系数的终止 balanced 四阶和：自足有限证明

继续 (HC.19)–(HC.20)，对 $0\le r\le N$ 置
$$
n=N-r,\qquad \alpha=r+4/3.
$$
在 $\mathbf F_p$ 中准确有 $\alpha+n=1/2$。原唯一逆系数可以写成
$$
\boxed{\quad
t_r=-\frac1{12}\sum_{d=0}^{n}
 \frac{(-n)_d(1)_d(1)_d(2/3)_d}
      {(\alpha)_d(3/2)_d(5/3)_d\,d!}
=-\frac1{12}\,{}_4F_3
 \!\left(\begin{matrix}-n,1,1,2/3\\
                  r+4/3,3/2,5/3\end{matrix};1\right).
\quad}
\tag{HC.21}
$$
本式表示终止在 $d=n$ 的有限和。上下参数之和的差为一；若要在特征零先写 balanced 身份，可取 $\alpha=1/2-n$ 再约化，这与显示的 $r+4/3$ 同余。

下面直接验证原非齐次递推，不引用无限级数或一般 Whipple 正常性。
令
$$
h_{r,d}=\frac{(-n)_d\,d!\,(2/3)_d}
                  {(\alpha)_d(3/2)_d(5/3)_d},
\qquad H_r=\sum_{d=0}^{n}h_{r,d}.
$$
在 $r<N$ 时，下一行的 $n$ 减一、$\alpha$ 加一，所以
$$
\frac{h_{r+1,d}}{h_{r,d}}
=\frac{\alpha(n-d)}{n(\alpha+d)}.
$$
这一式也准确使下一行的 $d=n$ 项为零。由于
$r+1/6=\alpha-7/6$、$r+5/6=-n$、
$r+2/3=\alpha-2/3$，逐项相减得到
$$
\begin{aligned}
&(r+1/6)H_r
 -\frac{(r+5/6)(r+2/3)}{r+4/3}H_{r+1}\\
&\qquad=-\frac1{3\alpha}
 \sum_{d=0}^{n}\frac{(-n)_d\,d!}
                         {(\alpha+1)_d(3/2)_d}.
\end{aligned}
\tag{HC.22}
$$
这里用的唯一简化是
$(2/3)_d/(5/3)_d=(2/3)/(d+2/3)$；对应的 $d+2/3$ 因子在逐项差中恰好抵消。

最后的有限和有一个显式望远镜证明。写
$$
u_d=\frac{(-n)_d\,d!}{(\alpha+1)_d(3/2)_d},
\qquad
R(d)=-\frac{4(d+\alpha)(d+1/2)}{2n+1}.
$$
由 $\alpha=1/2-n$，直接展开两个二次多项式即得
$$
R(d+1)u_{d+1}-R(d)u_d=u_d.
$$
由于 $u_{n+1}=0$、$u_0=1$，完整求和给
$$
\boxed{\quad
\sum_{d=0}^{n}u_d
=-R(0)=\frac{2\alpha}{2n+1}
=-\frac{\alpha}{\alpha-1}.
\quad}
\tag{HC.23}
$$
代回 (HC.22)，再乘 $-1/12$，正好是 (HC.20) 的右侧
$-1/[36(r+1/3)]$。在 $r=N$，(HC.21) 只有常数项，给 $t_N=-1/12$。
由 (HC.20) 的唯一性，(HC.21) 遂与原 companion 完全一致。

也可把向下迭代 (HC.20) 的结果保留为另一条 balanced 有限式：
$$
\boxed{\quad
t_r=-\frac{1}{36(r+1/3)(r+1/6)}
{}_4F_3\!\left(\begin{matrix}
 -n,r+2/3,r+1/3,1\\
 r+4/3,r+4/3,r+7/6
\end{matrix};1\right).
\quad}
\tag{HC.24}
$$
这次只需把逐步乘积写成 Pochhammer，并将末项的两个一次分母吸收到相邻参数中。它与 (HC.21) 的相等已经由上面的同一有限递推和同一末端值证明，不需要另加变换定理。

全部范围是安全的：$0\le d\le n\le N<p$，$2n+1\le2N+1=\ell<p$；$\alpha,\alpha+1,\alpha-1$ 在所读有限段可取半整数 $1/2-n,3/2-n,-1/2-n$，其两倍绝对值小于 $p$ 且为奇数。另 $(3/2)_d,(5/3)_d$ 及 (HC.24) 中的所有下参数均不遇 $p$。因此望远镜、反除及两条四阶和都在原 $\mathbf F_p$ 中成立。

这支付原 $w$ 的明确有限 hypergeometric 来源，仍没有证明 (HC.9) 的共同零不可能。特别不能以终止和的各因子为单位、或以 (HC.23) 的另一条和为单位，替代 (HC.21) 在原标记点组合后的非零。


root 逐项核 HC.22 的相邻行消元、HC.23 的完整望远镜端点及全部有限分母；本节与原 HC.20 的非齐次源和末端值一致。
