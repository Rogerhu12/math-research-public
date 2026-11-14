# R239 附录：三位等权短串加一异常位的出生一全高度，及四头特殊权型的全部 primitive

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的有限模型结论。** 对长度 $3,L,1$、$L\ge3$ 的三串，任意正权的相对出生一整个二维块，在全部高度 $h=L+2$ 上严格满足相邻系数一。结合已完成的相对出生二、三及一维分支，得到权型 $a,a,a,c$ 加任意大小等权池的整个 $K_s$、所有出生和高度的严格系数一。一般更长短串、更多独立权及普通 ISP 仍开。

可复算的有限整数证书：[内部及第三边](../notes/2026-11-13-three-short-weights-birth-one-interior-certificate-0c.py)、[次首边与两个小高度例外](../notes/2026-11-13-three-short-weights-birth-one-boundary-certificate-0c.py)。这些程序先准确除去下文列出的公共正因子，再逐一检查剩余多项式的全部系数；不使用数值采样或参数外推。

## 1. 完整二维 MP 与固定四次式

设短串长度三、长串长度 $L\ge3$，第三串长度一。权归一化为 $a,1,c>0$，写 $z=a^2,w=c^2$。相对出生 $t=1$，故 $\delta=2$、高度 $h=L+2$。在缺失普通头数 $r=0,1,2,3$ 及异常位缺失数 $\epsilon=0,1$ 下，完整二维源的最高多重仿射部分为
$$
f(r,\epsilon)=6\alpha\binom r3+2\beta\epsilon\binom r2.
$$
固定源坐标为 $(\alpha,\beta)$。由[全高度完整 MP 与剪切公式](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md) §§2–4，两个三次通道 $F_0,F_1$ 的最高系数同为 $\alpha$、二次系数之差为 $\beta$，其余系数全部自由，且
$$
H_n[\alpha,\beta]=\min_{F_0,F_1}\sum_{r=0}^3\binom3r z^r
\left\{\frac{|F_0(r)|^2}{\binom L{n+r-3}}
+w\frac{|F_1(r)|^2}{\binom L{n+r-2}}\right\}.
\tag{1.1}
$$
每个非法池占据都强制相应通道在该整数点为零。完整有限差分 MP 定理已经穷尽所有原像；组内平均保源及最小范数。因此保留的是完整层逆及整个二维 primitive，并没有固定某条试探原像。

令 $a_j$ 为权 $\binom3r z^r/\binom L{j+r-3}$ 下带全部强制根的首一三次最小范数，$b_{j-1}$ 为同权、同强制根的首二次最小范数。把三次最小多项式的二次系数记为 $-\mu_j$。仍有
$$
H_n=\begin{pmatrix}A_n+B_nk_n^2&-B_nk_n\\-B_nk_n&B_n\end{pmatrix},
\quad A_n=a_n+w a_{n+1},\quad k_n=\mu_n-\mu_{n+1},
\tag{1.2}
$$
$$
B_n=\frac{w b_{n-1}b_n}{b_{n-1}+w b_n}\quad(1\le n<h),
\qquad B_0=w b_0,\quad B_h=b_{h-1}.
$$
目标是在同一完整源坐标中证明
$$
\boxed{H_nH_{n+1}^{-1}H_n\prec H_{n-1},\qquad1\le n<h.}
\tag{1.3}
$$
$H_0$ 是真实源 Gram；共同合同后即为原 $\Gamma$ 比较。

对内点令 $K=H_{n-1}-H_nH_{n+1}^{-1}H_n$，并用共同剪切使中间 $k_n=0$。旧两值全高度比较给 $a_j$ 严格 log 凸，故
$$
K_{11}=A_- -A_0^2/A_++B_-x_s^2>0,
\quad x_s=\mu_{n-1}-2\mu_n+\mu_{n+1},
\quad y_s=-\mu_n+2\mu_{n+1}-\mu_{n+2}.
\tag{1.4}
$$
其余完整费用正是 $\det K$。记 $(a,b,c,d)=(a_{n-1},a_n,a_{n+1},a_{n+2})$、$(p,q,r,t)=(b_{n-2},b_{n-1},b_n,b_{n+1})$，则
$$
P=\det K\frac{(p+wq)(q+wr)^2(c+wd)t}{w}
$$
$$
=q\Lambda F-wpq^3r(c+wd)(r+wt)x_s^2
-wq^2r^2t(a+wb)(p+wq)y_s^2
-2wpq^2rt(b+wc)(q+wr)x_sy_s-w^2pq^3r^2t x_s^2y_s^2,
\tag{1.5}
$$
其中
$$
\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),
\quad F=pq(qt-r^2)+wqr(pt-qr)+w^2rt(pr-q^2).
$$
$P$ 是 $w$ 的四次式。两端 $P_0=pq^2(ac-b^2)(qt-r^2)$、$P_4=qrt(bd-c^2)(pr-q^2)$ 由旧高、低两值序列的严格 log 凸性为正。因此只须付三个中间系数。

## 2. 同一个有限生成式，含所有强制根

对四点非负权 $V$ 定义
$$
Z_k(V)=\sum_{\substack{I\subset\{0,1,2,3\}\\|I|=k}}
\prod_{u<v\in I}(v-u)^2\prod_{r\in I}V(r),\qquad Z_0=1.
\tag{2.1}
$$
这就是 Hankel Gram 行列式的 Cauchy–Binet 展开。对第 $i$ 个分布 $W_i$，令非法节点的强制根集合为 $E_i$，置
$$
V_i(r)=W_i(r)\prod_{u\in E_i}(r-u)^2,\quad
d_i=3-|E_i|,\quad \sigma_i=\sum_{u\in E_i}u,
$$
$$
C_i=Z_{d_i-1}(V_i),\quad B_i=Z_{d_i}(V_i),
\quad A_i=Z_{d_i+1}(V_i),\quad
M_i=z\partial_z B_i+\sigma_i B_i.
\tag{2.2}
$$
本稿用到的全部位置都有 $d_i\ge1$，且三个 Gram 行列式严格正。准确有
$$
a_i=A_i/B_i,\qquad b_i=B_i/C_i,\qquad \mu_i=M_i/B_i.
\tag{2.3}
$$
这里 $i=0,1,2,3$ 只标四个连续分布。式中 $\sigma_i$ 是强制根对次高系数的真实贡献，尤其高端根三不能遗漏。

采用[最高二维出生稿](R239-appendix-three-equal-short-weights-one-exceptional-saturated-two-dimensional-all-heights.md) §3 写明的三个固定多项式 $N_1,N_2,N_3$，按[相对出生二稿](R239-appendix-three-equal-short-weights-one-exceptional-birth-two-all-heights.md) (2.3) 代入
$$
(p,q,r,t)=(B_i/C_i)_{i=0}^3,\qquad
(A,B,C,D)=(A_i/C_i)_{i=0}^3,
$$
$$
X=\frac{M_0B_1B_2-2M_1B_0B_2+M_2B_0B_1}{C_0C_1C_2},
\quad Y=\frac{-M_1B_2B_3+2M_2B_1B_3-M_3B_1B_2}{C_1C_2C_3}.
\tag{2.4}
$$
于是 $X=pqr x_s,Y=qrt y_s$，并且
$$
P_1=N_1/(prt),\quad P_2=N_2/(pqr^2t),\quad P_3=N_3/(prt).
$$
定义
$$
\mathcal N_{1,3}=C_0^2C_1^3C_2^3C_3^2N_{1,3},\qquad
\mathcal N_2=C_0^2C_1^4C_2^4C_3^2N_2.
\tag{2.5}
$$
这是准确逐项清分母；某个 $C_i=Z_0=1$ 时也保持原式。所有多项式生成式在所引固定 $N_i$ 及 (2.1)–(2.5) 中完全明确，两个随稿程序也直接包含全部三个 $N_i$。

## 3. 内点的公共正因子与完整正系数

置
$$
x=n-4,\quad y=L-n-2,\quad L=x+y+6.
$$
当 $x,y\ge0$，所有分布有完整支撑；除去共有正因子 $x!y!/L!$ 后，真实四权为
$$
W_i(r)=\binom3r z^r(x+1)_{i+r}(y+1)_{6-i-r},\qquad 0\le i,r\le3.
\tag{3.1}
$$
此时 $C_i=Z_2,B_i=Z_3,A_i=Z_4,M_i=z\partial_zB_i$。

写
$$
G(e,f,k)=z^k\prod_{j=1}^5(x+j)^{e_j}(y+j)^{f_j}.
$$
由有限生成式准确分解
$$
\mathcal N_1=G(e_1,f_1,32)R_1,\quad
\mathcal N_2=G(e_2,e_2,38)R_2,\quad
\mathcal N_3=G(f_1,e_1,32)R_3,
\tag{3.2}
$$
其中
$$
e_1=(28,23,15,6,1),\quad f_1=(28,23,15,7,2),
\quad e_2=(34,28,18,8,2).
$$
所有公共因子均正于 $x,y\ge0,z>0$。整数程序先对每个小生成多项式精确因式分解，并回乘核对原式；在 (2.5) 的各单项之间逐个取公共因子后，再精确核对它等于 (3.2) 给出的 $G$。所以除因子没有丢掉任何项或假定未证正性。

剩余三个多项式的全部非零系数均为正整数：

| 剩余分子 | 正项数 | 总次数 | $x=X_0-1$ 后正项数 | $X_0^0$ 层正项数 |
|---|---:|---:|---:|---:|
| $R_1$ | 6084 | 56 | 6080 | 455 |
| $R_2$ | 8822 | 66 | 8819 | 624 |
| $R_3$ | 6084 | 56 | 6080 | 455 |

平移后三个明确正锚分别为
$$
[X_0^0y^0z^{25}]R_1(X_0-1,y,z)=23837781756511459928930726707200,
$$
$$
[X_0^0y^0z^{31}]R_2(X_0-1,y,z)=199621251780066428746393433250201600,
$$
$$
[X_0^0y^0z^{25}]R_3(X_0-1,y,z)=4584188799329126909409755136000.
\tag{3.3}
$$
故 $R_i>0$ 对所有 $x,y\ge0,z>0$ 成立，含 $x=0$、$y=0$。由 (2.5) 给所有 $4\le n\le L-2$ 的完整严格比较。

## 4. 第三边 $n=3$ 的真实强制零根极限

令 $\varepsilon=x+1\downarrow0$、$y\ge0$ 固定。所有权除以 $\varepsilon$ 后，唯一发散质量为 $i=r=0$；其余有限极限为
$$
\binom3r z^r(i+r-1)!(y+1)_{6-i-r},\qquad i+r\ge1.
$$
令 $L=y+5$，这恰是 $n=3$ 的原四分布，除一个共同正常数。发散质量强制第一个三次及二次多项式都在零点有根；它们的剩余次数依次为二、一。所有实际 $a_i,b_i$ 除以 $\varepsilon$ 后均趋有限正常数。

未除以 $\varepsilon$ 前，$C_0=Z_2(W_0)$ 有准确一阶零，$C_1,C_2,C_3$ 各有二阶零。因此 (2.5) 的三个清分母因子依次有十八、二十二、十八阶零。式 (3.2) 则给三个分子准确的二十八、三十四、二十八阶零，且 (3.3) 证明相应首项严格正。

所以 $N_1,N_2,N_3$ 有十、十二、十阶零；再除 $prt,pqr^2t,prt$ 的三、五、三阶零，三个 $P_i$ 都有准确七阶零。式 (1.5) 对共同 Gram 缩放的齐次次数恰为七，故 $\varepsilon^{-7}P_i$ 的严格正极限就是实际归一化后第三边的系数。两端系数和 $K_{11}$ 由旧两值严格比较保留，得到所有 $L\ge5$ 的 $n=3$。

这个极限同时处理高、低两个次数的强制根，没有把发散节点直接删去，也没有把真实二次范数设为无穷。

## 5. 所有次首边与两个小高度例外

### 5.1 $L\ge4$ 的 $n=2$

置 $y=L-4\ge0$。把四分布同乘 $L!/(L-4)!$ 后，准确写为
$$
W_i(r)=\binom3r z^r k!(y+1)_{4-k},\qquad k=i+r-2,
$$
仅保合法 $0\le k\le4$。四个强制根集合为
$$
E_0=\{0,1\},\quad E_1=\{0\},\quad E_2=E_3=\varnothing.
$$
按 (2.2)，四个剩余高次分别是一、二、三、三；低次各少一。因此所有 $C_i,B_i,A_i$ 严格正，完整矩阵及四次式仍是 (1.2)、(1.5)，没有端点无穷量。

在 (2.5) 的分子中准确取出
$$
\mathcal N_{1,3}=z^{30}(y+1)^{21}(y+2)^{16}(y+3)^8(y+4)R_{1,3},
$$
$$
\mathcal N_2=z^{36}(y+1)^{26}(y+2)^{20}(y+3)^{10}(y+4)R_2.
\tag{5.1}
$$
所有公共因子严格正，剩余正系数数据为

| 分子 | 正项数 | 总次数 | 正 $y^0z^k$ 锚的 $k$ |
|---|---:|---:|---:|
| $R_1$ | 253 | 21 | 21 |
| $R_2$ | 351 | 25 | 25 |
| $R_3$ | 210 | 19 | 19 |

因此对 $y\ge0,z,w>0$ 严格有 $P>0$，这付出全部 $L\ge4$ 的实际次首边。

### 5.2 $L=3$ 的 $n=2$

此时用真实权同乘 $3!$ 的形式
$$
W_i(r)=\binom3r z^r k!(3-k)!,\qquad k=i+r-2,
$$
非法点仍强制为根。集合依次为 $\{0,1\},\{0\},\varnothing,\{3\}$。最后一个高根的常数贡献由 (2.2) 的 $\sigma_3=3$ 保留。

三个分子准确分解为
$$
\mathcal N_{1,3}=z^{25}(z+1)^2(z^2+3z+1)^2R_{1,3},
\qquad
\mathcal N_2=z^{31}(z+1)^2(z^2+3z+1)^2R_2.
$$
$R_1,R_2,R_3$ 分别有 $15,19,13$ 个正整数系数，次数分别为 $14,18,12$。所有非零项严格正，所以对每个 $z,w>0$ 给出实际小高度比较。

### 5.3 $L=4$ 的中点 $n=3$

用同乘 $4!$ 的真实权
$$
W_i(r)=\binom3r z^r k!(4-k)!,\qquad k=i+r-1.
$$
四个强制根集合为 $\{0\},\varnothing,\varnothing,\{3\}$。此时
$$
\mathcal N_{1,3}=z^{27}R_{1,3},\qquad \mathcal N_2=z^{33}R_2.
$$
三个剩余多项式分别有 $25,31,25$ 个正整数系数，次数为 $24,30,24$，故该完整中点亦严格。这里没有用一般式的负参数外推，也没有将低、高强制根分开后遗失交叉费用。

## 6. 首尾、全部高度与整个有限权型

相对出生一的首边 $n=1$ 由已经证明的[R271 任意正权完整出生一首边](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)支付。它在整个物理 $K_1$ 上严格成立。当前群对称块同时约化 $D,D^*$、完整逆及 primitive Gram，所以限制到本二维块保持严格性和完整源，不把一个压缩逆误作逆压缩。

[全出生真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)给同一源合同下的 $n\leftrightarrow h-n$，保留整个矩阵与正权型。因此已证首边、次首边和第三边给另一端的三条边。$L\ge6$ 时 §3 补齐中间 $4\le n\le h-4$；$L=5$ 的两中间边由 §4 及对偶覆盖；$L=4$ 的唯一中点由 §5.3 覆盖；$L=3$ 的两个中间边由 §5.2 及对偶覆盖。由此 (1.3) 对 $L\ge3$ 全部合法高度成立。

**全部出生推论。** 考虑任意正 $a,b,c$、任意 $M\ge0$，权列表为
$$
\underbrace{a,a,a}_{3\text{ 位}},\quad c,\quad
\underbrace{b,\ldots,b}_{M\text{ 位}}.
$$
分别作两个共同权组的正交升降串分解。每个有效块为短串长度 $q\le3$、长串长度 $L\ge q$ 加一条长度一串。全部组内出生和表示重数原样保留。

当 $q=3$ 时，三个二维相对出生由本稿 $t=1$、[前稿 $t=2$](R239-appendix-three-equal-short-weights-one-exceptional-birth-two-all-heights.md)及[最高二维 $t=3$](R239-appendix-three-equal-short-weights-one-exceptional-saturated-two-dimensional-all-heights.md)分别覆盖；不存在相邻阶的高度零、一块无需比较。若 $q\le2$，该块属于已经完成的[三任意异权头加等权池](R239-appendix-three-exceptional-weights-full-primitive-gram-bound.md)或更小模型。

相对真空分支是一维，完整 Gram 为初等对称和的倒数，严格 Newton 给相邻系数一。最高一维出生 $t=q+1$ 则是 $q+1$ 个独立正权头的饱和固定线，由[任意头双侧常数](R239-appendix-saturated-primitive-two-sided-weight-count-constants.md)给严格小于一的相邻界。某普通串长度为零时直接是旧两权模型。

故对该完整有限权型的每个出生 $s$ 和全部合法 $1\le n<h$，在整个 $K_s$ 上严格有
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1}.}
$$
共同权 $a,b,c$ 可以相等，所有实际权始终有限且为正。该推论没有给任意四个独立异常头或一般三大权组；也没有给统一离一的谱隙、原高孔窄源的完整 Schur 返回费或普通 ISP 的完成证明。
