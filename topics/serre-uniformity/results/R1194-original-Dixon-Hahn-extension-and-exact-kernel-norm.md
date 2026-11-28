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


### 9.7. 原算子的半步因式分解与全格点多项式

以下仍在同一 $\mathbf F_p[a]$ 中，不更换 (HC.3) 的非齐次源。
对常数 $c$ 定义
$$
(T_cf)(a)=(a+c/2)f(a+3/2)-(a-c/2)f(a-3/2).
$$
直接乘开两次半步移位得到
$$
\boxed{\mathcal L=T_2T_1.}
\tag{HC.25}
$$
正、负整步项分别为 $(a+1)(a+2)$ 与 $(a-1)(a-2)$；
中央项为 $-(a+1)^2-(a-1)^2=-2(a^2+1)$，所以这里没有额外常数。

置
$$
Z(a)=\prod_{j=-N}^{N}(a-3j)
     =a\prod_{j=1}^{N}(a^2-9j^2),\qquad c_\ell=[a^\ell]v.
$$
由 $3N+3/2\equiv-1$，完整端点相消给
$$
\frac{Z(a+3/2)}{Z(a-3/2)}=\frac{a-1}{a+1}.
$$
故 $T_2Z=0$。算子 $T_c$ 保持奇偶及次数，在 $a^d$ 上的最高系数是 $3d+c$。
在奇次数 $d\le\ell$ 内，$T_2$ 只有 $d=\ell$ 的次数对角为零；
因此其核正是 $\mathbf F_pZ$。由 (HC.25) 及
$3\ell+1=p-1=-1$，得
$$
\boxed{\quad T_1v=-c_\ell Z,\qquad
z:=T_1w\ \Longrightarrow\ T_2z=-v/a.\quad}
\tag{HC.26}
$$
两个箭头都保留原边界，第二个源仍是 $-v/a$。例如
$T_1v(-1/2)=v(-2)=-1$，其归一由原 $v(2)=1$ 和奇性直接锁定；
不能由这个旁值非零推断 $w(-1/2)\ne0$。

(HC.10) 的全格点多项式还可以写成
$F(a)=\prod_{j=-\ell}^{\ell}(a-3j)$。
它满足 $T_1F=0$：这次端点比值为 $(a-1/2)/(a+1/2)$。
这给出全格点和短半格点的两个不同核，不能互换其长度。

(HC.19) 的同一 Newton 系数允许一个精确的全长延拓。令
$D=(4/3)_\ell(2/3)_\ell$，则
$$
\boxed{\quad
\sum_{r=0}^{\ell}p_rE_r
=\frac{(1+a/3)_\ell(1-a/3)_\ell}{D}
=-3^{-2\ell}\frac{F(a)}{aD}.
\quad}
\tag{HC.27}
$$
这里取有限 Pfaff--Saalschütz 恒等式的长度 $\ell$：
上参数为 $-\ell,1/3+a/3,1/3-a/3$，下参数为
$4/3,1/3-\ell$。模 $p$ 后 $-\ell=2/3$、
$1/3-\ell=1$，恰是显示的同一个有限和。
所有 $r!$、$(4/3)_r$ 在 $r\le\ell$ 都为单位。
右端乘积与 $F/a$ 的根和最高项逐一相同，给出最后的准确标量。

在原标记点 $a_0=-1/2=b_N$，(HC.27) 的普通空间导数是
$$
\boxed{\quad
\left.\frac{d}{da}\sum_{r=0}^{\ell}p_rE_r\right|_{a=-1/2}
=\frac{2(-1)^N N!(3N+2)!}{D}\ne0.
\quad}
\tag{HC.28}
$$
证明只需
$F'(b_N)=(-1)^N3^{2\ell}N!(3N+2)!$ 和 $a_0^{-1}=-2$。
(HC.27) 的下半段是 $v/(Ka)$，上半段在非零格点处给它的相反数。
(HC.28) 是两半段相加后的空间导数；它不是 (HC.5) 的谱导数，
因此本节不以它关闭 (HC.9)。

### 9.8. 取消参数的真实导数与完整调和余项

以下给原 $t_r$ 一个明确的参数导数来源，并把不能删去的余项写出。
对 $0\le r\le N$ 置 $m=N-r+1$，所以 $1\le m\le N+1$。
先在特征零的有限有理函数中定义
$$
\mathcal F_m(\epsilon)
={}_4F_3\!\left(\begin{matrix}-m,1,-1/3,\epsilon\\
 \epsilon+1/2-m,1/2,2/3\end{matrix};1\right).
\tag{HC.29}
$$
和严格终止在 $j=m$，且 $\mathcal F_m(0)=1$。
对每一项求导，使用
$\left.\partial_\epsilon(\epsilon)_j\right|_0=(j-1)!$，
再令 $j=d+1$，直接得到
$$
\boxed{\quad
t_r=\frac{2m-1}{24m}\mathcal F_m'(0).
\quad}
\tag{HC.30}
$$
详细地，$-m$、$-1/3$、$1/2-m$、$1/2$、$2/3$ 的首个因子
全部提出以后，右侧是
$$
-\frac1{12}\sum_{d=0}^{m-1}
\frac{(1-m)_d\,d!\,(2/3)_d}
     {(3/2-m)_d(3/2)_d(5/3)_d}.
$$
由于 $m-1=N-r$、$3/2-m\equiv r+4/3$，这恰为原 (HC.21)，
没有将一个点值恒等式微分。

为完整计算 (HC.30) 中实际导数，使用有限 balanced Whipple 变换
$$
{}_4F_3\!\left(\begin{matrix}x,y,z,-m\\u,v,w\end{matrix};1\right)
=\frac{(v-z)_m(w-z)_m}{(v)_m(w)_m}
{}_4F_3\!\left(\begin{matrix}-m,u-x,u-y,z\\
u,1+z-v-m,1+z-w-m\end{matrix};1\right),
$$
其中 $u+v+w=x+y+z+1-m$。
这是有限和的有理函数身份；可由有限 Saalschütz 后交换两次有限求和证明。
本节仅用它的如下具体代入：
$x=-1/3,\ y=\epsilon,\ z=1,\ u=\epsilon+1/2-m,\ v=1/2,\ w=2/3$。
于是
$$
\mathcal F_m(\epsilon)
=\frac1{(2m-1)(3m-1)}
{}_4F_3\!\left(\begin{matrix}
-m,\epsilon+5/6-m,1/2-m,1\\
\epsilon+1/2-m,3/2-m,4/3-m
\end{matrix};1\right).
\tag{HC.31}
$$
两首尾比
$(-1/2)_m/(1/2)_m=-1/(2m-1)$、
$(-1/3)_m/(2/3)_m=-1/(3m-1)$
给出这个不依赖 $\epsilon$ 的完整因子。
所用有限变换也见 M. Rahman,
[A non-negative representation of the linearization coefficients of the product of Jacobi polynomials](https://doi.org/10.4153/CJM-1981-072-9),
Canad. J. Math. 33 (1981), 印刷页 920（PDF 第 6 页）, §2, (2.4)--(2.5)；
这里只消费该有限恒等式，不消费任何正性或无限级数结论。

记
$$
\mathsf H_j(x)=\sum_{i=0}^{j-1}\frac1{x+i},\qquad \mathsf H_0=0,
\quad
T_{m,j}=\frac{(-m)_j(5/6-m)_j}
                  {(3/2-m)_j(4/3-m)_j}.
$$
在 $\epsilon=0$ 时，(HC.31) 中的一对参数相消。
有限 Saalschütz 给
$$
\sum_{j=0}^{m}T_{m,j}=(2m-1)(3m-1).
\tag{HC.32}
$$
但其导数中这对参数不能预先相消。准确结果为
$$
\boxed{\quad
\mathcal F_m'(0)
=-\frac{9m}{3m-1}
+\frac{\displaystyle\sum_{j=0}^{m}T_{m,j}
 \{\mathsf H_j(4/3-m)-\mathsf H_j(1/2-m)\}}
 {(2m-1)(3m-1)}.
\quad}
\tag{HC.33}
$$

为核定 (HC.33) 的全部余项，置
$b=5/6-m,\ c=3/2-m,\ d=4/3-m,\ a_*=1/2-m$。
(HC.31) 的逐项导数是 $T_{m,j}\{\mathsf H_j(b)-\mathsf H_j(a_*)\}$。
沿仍然 balanced 的 Saalschütz 路径把 $b,d$ 同时改成 $b+\epsilon,d+\epsilon$，
则其逐项导数为 $T_{m,j}\{\mathsf H_j(b)-\mathsf H_j(d)\}$，
而其完整乘积是
$$
\frac{(2/3-\epsilon)_m(1/2-m)_m}
     {(3/2-m)_m(-1/3-\epsilon)_m}.
$$
这个乘积在零处的对数导数准确是
$\mathsf H_m(-1/3)-\mathsf H_m(2/3)=-9m/(3m-1)$。
剩下的两条路径差正是 (HC.33) 显示的
$\mathsf H_j(d)-\mathsf H_j(a_*)$；没有丢掉取消参数的导数。

安全范围是逐项的：$m\le N+1$，$j\le m$；
$2m-1,3m-1$ 和 $m!$ 均非零模 $p$。
上述半整数分母的两倍、三分之一参数分母的三倍，
在所读范围内绝对值小于 $p$ 且非零；
$5/6-m+i$ 的六倍也在 $(-p,p)$ 内且非零。
因此 (HC.29)--(HC.33) 的有限导数及所有调和分母都可直接约化，
不需要任何 $p$ 次除法或未说明的正则化。

### 9.9. 原标记值的有限三角源与尚需比较的差额

写
$$
u_r=p_r(1/6)_r(1/2)_r
=\frac{(2/3)_r(1/6)_r(1/2)_r}{(4/3)_r(r!)^2}.
$$
原两槽仍严格是
$$
\boxed{\quad
v(-1/2)=-\frac K2\sum_{r=0}^N u_r,\qquad
w(-1/2)=\frac K{24}\sum_{r=0}^N
 u_r\frac{2m_r-1}{m_r}\mathcal F_{m_r}'(0),
\quad m_r=N-r+1.
\quad}
\tag{HC.34}
$$
所以 (HC.33) 的调和余项是原谱导数内的真实项，
不是只影响另一个辅助族的误差。

也可不引入参数微分，直接在 (HC.21) 的有限三角形中换序：
$$
\frac{w(-1/2)}K
=-\frac1{12}\sum_{\substack{r,s\ge0\\r+s\le N}}
\frac{(-N)_{r+s}}{(4/3)_{r+s}}\,
\frac{(2/3)_r(1/6)_r(1/2)_r}{(-N)_r(r!)^2}\,
\frac{s!\,(2/3)_s}{(3/2)_s(5/3)_s}.
\tag{HC.35}
$$
这是用 $(-N+r)_s=(-N)_{r+s}/(-N)_r$ 以及
$(r+4/3)_s=(4/3)_{r+s}/(4/3)_r$ 的直接有限相消；
所有 $r+s\le N$，特别没有越过 $(-N)_{N+1}=0$ 的边界。

R1061 §15 的原已证单位是
$4D_N'(1)+(4/3)D_N(1)$，其中导数是该 Dixon 多项式的变量导数。
本节已把实际 $w$ 的来源付成 (HC.33)--(HC.35)，
但尚未将显示的全部调和余项和三角边界运输到那个单位组合。
同样，(HC.28) 的全格点空间导数没有被认作谱导数。
因此本节保存新的完整源、有限变换和端点，
原 $e=K_4=0$ 的排除仍是待证结论。


### 9.10. 原两槽的共同有限权重、点值桥与完整伴随余项

本节沿用 (HC.34)–(HC.35) 的同一原输入，不更换谱参数，不把点值恒等式微分。

#### 原点值桥与归一常数

沿 R1194 的原规范，$p=6N+5\ge41$、$\ell=2N+1$，
$v(a)$ 是原奇 Hahn 核，$v(2)=1$，而偶 companion 满足
$\mathcal Lw=-v/a$。记
$$
p_r=\frac{(2/3)_r}{(4/3)_r(r!)^2},\qquad
u_r=\frac{(2/3)_r(1/6)_r(1/2)_r}{(4/3)_r(r!)^2}.
$$
R1194 (HC.19)、(HC.34) 给
$$
\frac{v(a)}a=K\sum_{r=0}^Np_r(1/3+a/3)_r(1/3-a/3)_r,
\quad
v(-1/2)=-\frac K2\sum u_r,\quad
w(-1/2)=K\sum u_rt_r.
\tag{HA.1}
$$
全部求和未注明时均从 $0$ 到 $N$。

归一常数也可完全写出。R1194 (1194.2) 的 $j^\ell$ 最高系数是
$-1/\ell!$：因为 $M=2\ell$、$\ell$ 为奇数，
$$
\frac{(2\ell)!}{(\ell!)^2(-2\ell)_\ell}=-\frac1{\ell!}.
$$
换成 $a=3j+2$，再与 (HA.1) 的最高项比较，得到
$$
K=\frac{(-1)^{N+1}(4/3)_N(N!)^2}
        {3\ell!(2/3)_N}.
\tag{HA.2}
$$
这里每一因子都是 $p$ 单位。

令 $v_0$ 表示原椭圆曲线的常数，$\Gamma=(2v_0)^{2N+2}$。
由 R1194 (HC.8) 及 R1061 (1061.34)–(1061.36)，同一个原 $e$ 分别为
$$
e=\frac{\delta\Gamma K}{4v_0}\sum u_r
=-\frac{\delta v_0}{3}\,
 \frac{(-v_0^2)^N N!(4/3)_N}{(5/3)_N(7/6)_N}\,D_N(1),
$$
其中
$$
D_N(z)=\sum_{r=0}^N
\frac{(2/3)_r^2(1/6)_r}{(r!)^2(3/2)_r}z^r.
$$
用 $(2N+1)!=4^NN!(3/2)_N$ 消去单位，严格得到
$$
\boxed{\quad
\sum u_r=
\frac{(3/2)_N(2/3)_N}{(5/3)_N(7/6)_N}\,D_N(1).
\quad}
\tag{HA.3}
$$
这是两个已经识别为同一 $e$ 的实际来源的比较。它不把点值身份微分，不支付谱导数到 $D_N'(1)$ 的箭头。

#### 一个保留全部终止边界的简单分母式

R1194 (HC.29) 的真实有限参数族是
$$
\mathcal F_m(\epsilon)
={}_4F_3\left(\begin{matrix}-m,1,-1/3,\epsilon\\
\epsilon+1/2-m,1/2,2/3\end{matrix};1\right),
\qquad 1\le m=N-r+1\le N+1.
$$
另一次有限 balanced Whipple 变换给
$$
\mathcal F_m(\epsilon)=
-\frac{\epsilon-m-1/2}{(3m-1)(\epsilon-1/2)}
{}_4F_3\left(\begin{matrix}
-m,5/6,1/2-\epsilon,1\\
1/2,3/2-\epsilon,4/3-m
\end{matrix};1\right).
\tag{HA.4}
$$
这里直接对 (HC.29) 使用 (HC.31) 所列的有限变换，取
$x=-1/3,y=\epsilon,z=1,u=1/2,v=\epsilon+1/2-m,w=2/3$。
首个 Pochhammer 比为 $(\epsilon-m-1/2)/(\epsilon-1/2)$，另一个为 $-1/(3m-1)$；所有和仍终止在 $m$。
令
$$
S_m=\sum_{j=0}^m
\frac{(-m)_j(5/6)_j}
     {(3/2)_j(4/3-m)_j(2j+1)}.
$$
在零处无 $1/(2j+1)$ 的那条有限 Saalschütz 和等于
$-(3m-1)/(2m+1)$。逐项微分 $(1/2-\epsilon)_j/(3/2-\epsilon)_j$，
连同 (HA.4) 的完整 prefactor，得到
$$
\mathcal F_m'(0)=
-\frac2{2m+1}-\frac{2(2m+1)}{3m-1}S_m,
$$
$$
\boxed{\quad
t_r=-\frac{2m-1}{12m(2m+1)}
-\frac{(2m-1)(2m+1)}{12m(3m-1)}S_m.
\quad}
\tag{HA.5}
$$
这里 $t_r=(2m-1)\mathcal F_m'(0)/(24m)$，正是原 (HC.30)。

若要改变外层终止范围，必须先把 $j=0$ 合并，并在每个 $j\ge1$ 项中消去 $(-m)_j/m$。
准确的安全形式为
$$
\begin{aligned}
t_r={}&-\frac{(2m-1)(4m+7)}
 {12(2m+1)(3m-1)}\\
&+\frac{5(2m-1)(2m+1)}
 {324(3m-1)(4/3-m)}
 \sum_{d=0}^{m-1}
 \frac{(1-m)_d(11/6)_d(3/2)_d}
 {(7/3-m)_d(5/2)_d^2}.
\end{aligned}
\tag{HA.6}
$$
这是提出 $j=d+1$ 的首因子得到，原范围内每个分母非零模 $p$。
第一行在形式 $m=0$ 的值为 $-7/12$；但它不是一个已经定义的 $t_{N+1}$。
第二行原本只在 $m\ge1$ 的三角形内求和，不能用负长度和的擅自延拓删掉它。
以下改从原 (HC.35) 换序，从始至终不需要引入 $m=0$。

#### 两个原读数成为同一有限权重下的配对

定义
$$
C_N=\frac{(2/3)_N}{N!},\qquad
c_n=\frac{(-N)_n(5/6)_n(2/3)_n}
           {(4/3)_n(7/6)_n n!},\qquad
a_n=\frac{(1/6)_n}{n!},
$$
$$
b_j=\frac{(j!)^2}{(3/2)_j(5/3)_j},
\qquad
h_n=\sum_{j=0}^n b_j a_{n-j}.
\tag{HA.7}
$$
本段实际指标全部在 $0,\ldots,N$。因此 $c_n$ 和所显示的全部分母在此范围是单位；这不表示它们的和为单位。

完整有限恒等式是
$$
\boxed{\quad
\sum_{r=0}^N u_r=C_N\sum_{n=0}^Nc_na_n,\qquad
\sum_{r=0}^N u_rt_r=-\frac{C_N}{12}\sum_{n=0}^Nc_nh_n.
\quad}
\tag{HA.8}
$$

直接固定原三角形 (HC.35) 中的 $s$，置 $L=N-s$。其内层和是
$$
J_s={}_4F_3\left(\begin{matrix}-L,2/3,1/6,1/2\\
-N,4/3+s,1\end{matrix};1\right).
$$
这在有理数上已经 balanced。在 (HC.31) 所用的同一有限 Whipple 恒等式中取
$$
x=2/3,\quad y=1/2,\quad z=1/6,\quad
u=4/3+s,\quad v=-N,\quad w=1.
$$
变换后的上参数是
$-L,2/3+s,5/6+s,1/6$；下参数是
$4/3+s,7/6+s,1/6-N+s$.
完整首因子是
$$
\frac{(-N-1/6)_L(5/6)_L}{(-N)_L L!}
\equiv\frac{(2/3)_L}{L!}\pmod p.
$$
因 $N=-5/6$ 于 $\mathbf F_p$，最后一个下参数约化为 $1+s$。又有
$$
\frac{(2/3)_{N-s}}{(N-s)!}
=C_N\frac{(-N)_s}{(1/3-N)_s}
\equiv C_N\frac{(5/6)_s}{(7/6)_s}.
$$
所以原外因子变成 $C_Nc_sb_s$，而变换后内层指标 $r$ 的系数准确为 $(c_{r+s}/c_s)a_r$。
置 $n=r+s$ 得 (HA.8) 第二式，包含 $s=0,N$ 两端。
取 $s=0$ 时，原 $J_0$ 的两个 $(-N)$ 参数在 $0,\ldots,N$ 内安全相消，正给第一式。
所有分母 $(-N)_j$ 均满足 $j\le N$，没有反除 $N+1$ 处的终止零。

#### 同一 $h$ 的非齐次 Gauss 方程

以下方程直接由同一系数推出。置
$$
A(z)=\sum_{j\ge0}b_jz^j
={}_3F_2(1,1,1;3/2,5/3;z),\qquad \theta=z\,d/dz.
$$
系数比给
$$
[(\theta+1/2)(\theta+2/3)-z(\theta+1)^2]A=\frac13.
$$
由 $h(z)=(1-z)^{-1/6}A(z)$，直接共轭得到
$$
\boxed{\quad
[(\theta+1/2)(\theta+2/3)-z(\theta+7/6)^2]h
=\frac13(1-z)^{-1/6}.
\quad}
\tag{HA.9}
$$
因此 $h_0=1$，且 $n\ge1$ 时
$$
\boxed{\quad
(n+1/2)(n+2/3)h_n-(n+1/6)^2h_{n-1}=a_n/3.
\quad}
\tag{HA.10}
$$
(HA.8) 只读取 $n\le N$，该范围全部反除因子为单位。

#### 完整有限伴随与仍然存在的两个移位矩

在特征 $p$ 中，$c_{N+1}=0$，且对 $0\le n<N$ 有
$$
\frac{c_{n+1}}{c_n}
=\frac{(n+5/6)^2(n+2/3)}
 {(n+4/3)(n+7/6)(n+1)}.
$$
右式在 $n=N$ 给零，所以连同此端点仍成立，且其分母全部非零。
令 $h_{-1}=0$，将 (HA.10) 乘 $c_n$ 后从零加到 $N$，再平移第二个和。
$c_nh_n$ 的准确系数为
$$
\begin{aligned}
R_n&=(n+1/2)(n+2/3)
-\frac{(n+7/6)(n+5/6)^2(n+2/3)}
 {(n+4/3)(n+1)}\\
&=-\frac1{216}
 \left(30-\frac1{n+1}-\frac{18}{n+4/3}\right).
\end{aligned}
$$
上端余项准确为 $c_{N+1}(N+7/6)^2h_N=0$。因此
$$
\boxed{\quad
\sum_{n=0}^N\frac{c_nh_n}{n+1}
+18\sum_{n=0}^N\frac{c_nh_n}{n+4/3}
-30\sum_{n=0}^Nc_nh_n
=72\sum_{n=0}^Nc_na_n.
\quad}
\tag{HA.11}
$$
在原共同零假设下，最后两个和由 (HA.8) 为零，准确剩下前两个移位矩的和。
本节没有证明其中任一个分别为零，也没有将它们的另一线性组合认作已付单位 $4D_N'(1)+(4/3)D_N(1)$。

#### 实际三角形以外的首次共振边界

下面仅记录同一有理 $h$ 的准确安全范围，不给 (HA.11) 添加额外输入。
$b_j$ 的分母首次含 $p$ 因子发生于 $j=\ell=2N+1$，因为
$$
5/3+\ell-1=p/3.
$$
此前全部 $b_j$ 整，且 $a_n$ 的分母在此范围不含 $p$。所以 $p h_\ell\bmod p$ 只有 $b_\ell a_0$ 贡献，得到
$$
\boxed{\quad
p h_\ell\equiv
\frac{3(\ell!)^2}{(3/2)_\ell(5/3)_{\ell-1}}\ne0\pmod p.
\quad}
\tag{HA.12}
$$
这个共振在 $N$ 以外，而 (HA.7) 的实际 $c_n$ 严格终止于 $N$；不能通过延长有限和把 (HA.12) 插入原配对。
后继若用参数导数移去终止因子，必须同时运输此边界和完整原谱源。

因此当前准确差额仍是 (HA.11) 的两个移位矩。(HA.8) 与 (HA.3) 已保留原 $e,K_4$ 和 Dixon 的全部归一，尚未排除共同零。

本节为纸面证明，无数学程序执行。o2 已亲读原 (HC.35) 与本节全文，独核 (HA.8) 的全部 Whipple 参数、两个三角端点，以及 (HA.9)–(HA.11) 的系数与上端余项。


### 9.11. 两个 contiguous 单位、完整有理伴随与原 Beta 配对

本节仍在 $p=6N+5\ge41$、$k=N+1$ 下使用 (HA.7) 的同一 $c_n,a_n,h_n$ 和 (HC.34) 的同一 $u_j$。所有有限和未注明时从 $0$ 到 $N$。记
$$
U=\sum c_na_n,\quad H=\sum c_nh_n,\quad
A_q=\sum\frac{c_na_n}{n+q},\quad
H_q=\sum\frac{c_nh_n}{n+q},\quad
\mathcal U=\sum u_j=C_NU.
\tag{HA.13}
$$
以下 $q=1,4/3,2,7/3$ 的分母均为单位。本节证明新的完整来源，不把 $A_q$ 的单位性当成 $H$ 的单位性。

#### 两个原 $a$-moment 的单位及原 Dixon 单位的准确箭头

有
$$
\boxed{\quad
\sum\frac{6n+1}{n+1}c_na_n=6C_N,\qquad
\sum\frac{6n+1}{n+4/3}c_na_n=\frac{C_N}{3}.
\quad}
\tag{HA.14}
$$
第一式的左端是
$\,{}_3F_2(-N,5/6,2/3;4/3,2;1)$。
为在约化前应用有限 Saalschütz，第二下参数取真正 balanced 的 $7/6-N$，它模 $p$ 为 $2$。
右积为
$(1/2)_N(2/3)_N/((4/3)_N(-1/6)_N)$。
反序
$(1/2)_N=(-1)^N(4/3)_N$、
$(-1/6)_N=(-1)^N(N+1)!$
给 $C_N/(N+1)=6C_N$。

第二式的左端是
$(3/4){}_3F_2(-N,5/6,2/3;7/3,1;1)$。
真正 balanced 的第二下参数是 $1/6-N\equiv1$，故其右积为
$$
\frac34\,\frac{(3/2)_N(5/3)_N}{(7/3)_N(5/6)_N}.
$$
用
$(3/2)_N/(1/2)_N=-2/3$、
$(5/3)_N/(2/3)_N=-1/4$、
$(7/3)_N/(4/3)_N=3/8$，
再用 $(5/6)_N=(-1)^NN!$，即得 $C_N/3$。
这些有限变换中没有终止因子被越界相消。

原 R1061 §15 的单位也可准确送到第一式：
$$
\boxed{\quad
4D_N'(1)+\frac43D_N(1)
=\frac{N!}{12(4/3)_N}
  \sum\frac{6n+1}{n+1}c_na_n
=\frac{(2/3)_N}{2(4/3)_N}.
\quad}
\tag{HA.15}
$$
这里的导数仍是原 Dixon 变量导数。直接证明是对原 $d_j$ 使用有限 Dougall：
加入 $(-N)_j/(5/3+N)_j$，它在所用范围内模 $p$ 为 $1$，则
$$
\sum(3j+1)d_j
=\frac{(5/3)_N(5/6)_N}{N!(3/2)_N}
=\frac38\frac{(2/3)_N}{(4/3)_N}.
$$
乘 $4/3$ 就是 (HA.15)，没有微分 (HA.3) 的点值身份。

特别在原 $e=0$，即 $U=0$ 时，
$$
A_1=-\frac65C_N,\qquad A_{4/3}=-\frac1{21}C_N.
$$
但相应的完整 $h$ 伴随仍为
$$
\boxed{\begin{aligned}
72A_1&=216H+37H_1+27H_{4/3}-490H_2,\\
96A_{4/3}&=288H+H_1+184H_{4/3}-945H_{7/3}.
\end{aligned}}
\tag{HA.16}
$$
这由 (HA.10) 分别乘 $c_n/(n+1)$、$c_n/(n+4/3)$ 后有限分部求和得到。
例如第二式的实际伴随系数是
$$
1+\frac1{288(n+1)}
+\frac{23}{36(n+4/3)}
-\frac{105}{32(n+7/3)}.
$$
上端仍由 $c_{N+1}=0$ 消掉，分母在该端无极。
因此在 $U=H=0$ 下，连同 (HA.11)，只能得到
$$
639H_{4/3}+490H_2=\frac{432}{5}C_N,\qquad
166H_{4/3}-945H_{7/3}=-\frac{32}{7}C_N.
$$
显示的两个移位矩没有被删去。

#### 一个完全显式、极点都在原窗口外的有理伴随

令
$$
D(n)=(n+1/2)(n+2/3),\qquad
B(n)=\frac{(n+7/6)(n+5/6)^2(n+2/3)}
           {(n+4/3)(n+1)},
\qquad
\mathcal A f(n)=D(n)f(n)-B(n)f(n+1).
$$
这正是 (HA.10) 在原 $c_n$ 下的有限伴随。
置
$$
\boxed{\quad
\eta_j=(2j+1)(6j+1)u_j,\qquad
f(n)=\sum_{j=0}^N\frac{\eta_j}{n-k-j},
\qquad g(n)=f(n)-f(0).
\quad}
\tag{HA.17}
$$
$f$ 只有 $k,\ldots,2k-1$ 这些简单极，全部避开实际输入 $0,\ldots,N$。
其留数递推准确为
$$
\frac{\eta_{j+1}}{\eta_j}
=\frac{(j+2/3)(j+3/2)(j+7/6)}
       {(j+4/3)(j+1)^2}
=\frac{D(k+j)}{B(k+j)}.
$$
所以 $\mathcal A f$ 的相邻极部完全相消。
右端最后一个极由 $D(2k-1)=0$ 消去；
左端 $n=N$ 虽然 $f(n+1)$ 有简单极，$B(n)$ 却有二重零，故完整乘积 $B(n)f(n+1)$ 在该点正则且为零。
这里没有给有极的 $f(N+1)$ 单独赋值，也没有删去未计算的 $0\cdot\infty$。

其余可能的极只有 $n=-1,-4/3$。直接读取两个留数及无穷远常数，得到
$$
\boxed{\quad
\mathcal A f(n)=
\sum\eta_j+\frac{f(0)}{216(n+1)}
             +\frac{f(-1/3)}{12(n+4/3)}.
\quad}
\tag{HA.18}
$$
事实上 $B$ 在这两点的留数分别为 $-1/216,-1/12$。
而
$$
f(0)=-6\sum(2j+1)u_j,\qquad
f(-1/3)=-2\sum(6j+1)u_j,\qquad
f(-1/3)-f(0)=4\mathcal U.
$$

为准确锁定 (HA.18) 的常数，设 $\mathcal U(z)=\sum u_jz^j$。
原截断 $\,{}_3F_2$ 的完整方程是
$$
\bigl[\theta^2(\theta+1/3)
-z(\theta+2/3)(\theta+1/6)(\theta+1/2)\bigr]\mathcal U(z)
=\frac{u_N}{27}z^{N+1},
\qquad \theta=z\,d/dz.
$$
右端来自
$-(N+2/3)(N+1/6)(N+1/2)u_N=u_N/27$，不能当成齐次方程。
在 $z=1$，
$$
-\theta^2\mathcal U(1)-\frac{19}{36}\theta\mathcal U(1)
-\frac1{18}\mathcal U(1)=\frac{u_N}{27}.
$$
连同 (HA.18) 和
$\mathcal A1=-5/36+1/(216(n+1))+1/(12(n+4/3))$，
严格给
$$
\boxed{\quad
\mathcal A g(n)=
-\frac49u_N-\frac12\mathcal U
+\frac{\mathcal U}{3(n+4/3)}.
\quad}
\tag{HA.19}
$$
尤其 $e=0$ 时 $\mathcal A g=-4u_N/9$ 是单位，且
$g(0)=g(-1/3)=0$。这是原窗口外允许简单极的实际有理逆；它没有声称原 $H$ 已非零。

#### 原 $K_4$ 的准确有限 Beta 配对

(HA.17) 的极点不在实际求和区间内，且 (HA.19) 已整体处理上端，故有限伴随给
$$
\left(-\frac49u_N-\frac12\mathcal U\right)H
+\frac{\mathcal U}{3}H_{4/3}
=\frac13\left(\sum c_na_nf(n)-f(0)U\right).
\tag{HA.20}
$$
在 $e=0$ 分支，这准确化为
$H=-3\sum c_na_nf(n)/(4u_N)$。

令
$$
M(z)=\sum_{n=0}^Nc_na_nz^n,\qquad
Z(z)=\sum_{j=0}^N\zeta_jz^j,\quad
\zeta_j=\eta_{N-j},\qquad
\mathcal I\left(\sum_r F_rz^r\right)
=\sum_r\frac{F_r}{r+2/3}.
$$
本节只对次数不超过 $2N$ 的多项式使用 $\mathcal I$；所有分母均为单位，
因为 $2\le3r+2\le p-3$。
反序 (HA.17) 中的 $j$，利用 $2N+1=-2/3$，得
$$
\boxed{\quad
\sum c_na_nf(n)
=\sum_{n,j=0}^N\frac{c_na_n\zeta_j}{n+j+2/3}
=\mathcal I(MZ).
\quad}
\tag{HA.21}
$$
这可记作形式 Beta 配对 $\int_0^1z^{-1/3}M(z)Z(z)\,dz$；
含义就是上面的安全有限分母式，不诉诸有限域正性。

沿原 (HC.8)、(HA.1) 和 (HA.8) 的全部尺度，在 $e=0$ 时
$$
\boxed{\quad
w(-1/2)=\frac{K C_N}{16u_N}\,\mathcal I(MZ),
\qquad
K_4=-\frac{3\delta^2\Gamma K C_N}{32v_0^2u_N}\,
          \mathcal I(MZ).
\quad}
\tag{HA.22}
$$
此处所有外部因子均为原已付单位。因而共同零的剩余命题准确是：
在 $M(1)=0$ 时，能否排除这个指定的 $\mathcal I(MZ)=0$。

最后，新的 $Z$ 也有完整、自足的低阶来源：
$$
\zeta_0=\frac83u_N,\qquad
\frac{\zeta_j}{\zeta_0}
=\frac{(1/2)_j(5/6)_j^2}
       {(1/3)_j(2/3)_j(7/6)_j},
$$
$$
\boxed{\quad
\bigl[(\theta-2/3)(\theta-1/3)(\theta+1/6)
-z(\theta+1/2)(\theta+5/6)^2\bigr]Z
=\frac{\zeta_0}{27}.
\quad}
\tag{HA.23}
$$
系数递推直接证明此式；最高端的 $(N+5/6)^2$ 为零，所以没有遗漏的高端强迫。
$\zeta_0/27$ 为单位，但未被当成 (HA.22) 的配对单位。

原 $M$ 的完整多项式算子则是
$$
L_M=\bigl[\theta^2(\theta+1/3)
-z(\theta+5/6)^2(\theta+2/3)\bigr](\theta+1/6).
$$
在权 $z^{-1/3}dz$ 下，形式上 $\theta^*=-\theta-2/3$，所以
$$
L_M^*=(\theta+2/3)^2(\theta+1/3)(\theta+1/2)
-z(\theta+5/6)^2(\theta+1)(\theta+3/2).
\tag{HA.24}
$$
它并不等于 (HA.23) 的三阶算子。
此外，若后继 Green 运算产生次数 $2N+1$，则 $2N+1+2/3=p/3=0$；
该首次共振不在 (HA.21) 的安全积分范围内，不能在分母为零处延长 $\mathcal I$。
后续仍须支付准确的 contiguous/Green 余项和这个边界。
本节没有把两个 $a$-moment、伴随常数或 $Z$ 的强迫单位移作原 $w$ 的非零证明。

本节全为纸面推导，无数学程序执行。O2 已独核 (HA.14) 与第一条 (HA.16)；
其余显示来源由本节逐式给出，未将尚未完成的配对排除写成结论。
