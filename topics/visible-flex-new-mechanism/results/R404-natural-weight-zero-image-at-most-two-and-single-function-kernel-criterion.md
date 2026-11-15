# R404：原加速度平方零式把自然权零像缩至两维及单函数判据

日期：2026-11-15。**纸面原空间推论；没有执行新的原根恢复、profile 评价、积分、成员、消元、秩或人工检查。**

[R400](R400-weight-zero-natural-flux-kernel-and-three-static-function-criterion.md)
把增强联合核准确归于三个完整自然函数
$n_i(u)=\Lambda_u(C_i)$，$i=2,4,6$。
本稿再使用原完整加速度平方的零式，证明
$$
\boxed{\exists c_0\in\mathbb R:\quad
n_4=-c_0n_6,}
\tag{1}
$$
这个 $c_0$ 由下面原 $U_0/\mathcal R_0$ 的系数唯一指定，
不是声称在 $n_6=0$ 时仅凭函数式可以唯一辨认该数。

因此原自然权零像至多二维，R400 的实际相关核条件严格缩为
$$
\boxed{
\exists K\in U:\quad
E(K)=0,\quad \Lambda_\cdot(K)=0,\quad\lambda_+(K)=1
\quad\Longleftrightarrow\quad
n_2\in\operatorname{span}\{n_6\}.
}
\tag{2}
$$
本稿没有求出 $c_0,n_2,n_6$，也没有把(2)的右侧当作已成立。
结论来自已付的完整原函数商，而非只比较某个主符号或有限 profile 值。

## 1. 四个原记录及真实规范

沿用
$$
E=(\pi,\mathcal Q),\qquad
\mathcal Q(V)(u)=\frac14[x^2]_{\rm left}V(u^2,0),
\qquad
\mathcal N(V)(u)=\Lambda_u(V).
\tag{3}
$$
$\Lambda$ 始终是原 self 总通量、正式 pure 及有序 $2+2$ 三矩真尾的完整组合；它杀掉整个真实响应空间 $\mathcal R$。
它不是只读左二次尾的 $\mathcal Q$。

[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)
原二十二条 normal 记录中，本稿只需四条：

| 原记录 | 完整正规族 | 状态键 $(h,k,\omega,\log h)$ 的幂 |
|---|---|---|
| $C_2$ | $F_0$ | $(0,2,0,0)$ |
| $C_4$ | $F_0$ | $(0,4,0,0)$ |
| $C_6$ | $F_0$ | $(1,1,1,0)$ |
| $C_{20}$ | $\bar A_{hh}$ | $(-2,0,0,0)$ |

R196 表中将最后一族简称为 $A_{hh}$；它来自
[R134 的完整正规加速度平方](R134-acceleration-layer-from-complete-local-v4.md)，
即原 $A_{hh}-\beta_{hh}$，不是未经分部积分的单个 raw 加速度槽。
第三记录的状态键含 $\omega$，不含 $\log h$。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
已在所有真实状态、所有实紧 profile 上完整证明
$$
\Lambda_u(\bar A_{hh}(S))
=\Lambda_u(\bar A_{hk}(S))
=\Lambda_u(\bar A_{kk}(S))=0.
\tag{4}
$$
这个定理包含原加速度势、formal pure 与有序尾，不依赖后来已更正的旧 H 非零主张。
R134 的层次分离也表明原 $N_0,N_2,\Gamma$ 不会改变这三个正规加速度平方系数。

由于(4)是有限 Laurent/log 状态函数的全状态身份，
其真实系数分别为零，故
$$
\boxed{\mathcal N(C_{20})=0.}
\tag{5}
$$
这里没有由单一状态值外推系数，也没有把某个 raw self 为零替换成(5)。

## 2. 完整原商与两头的作用

R196 已付的是原完整函数身份
$$
U_0/\mathcal R_0
=\operatorname{span}\{[C_2],[C_4],[C_6]\},
\qquad \dim(U_0/\mathcal R_0)=3.
\tag{6}
$$
这三个商类是真基。
同一结果给
$$
(\mathcal R_0+NU_1)/\mathcal R_0
=\operatorname{span}\{[C_6]\}.
\tag{7}
$$
因此全部真实权零仿射字符形成二维空间。
按 R196 的原参数 $x,y$，四条记录的准确赋值是
$$
\lambda_{x,y}(C_2)=-x-y,\quad
\lambda_{x,y}(C_4)=y,\quad
\lambda_{x,y}(C_6)=0,\quad
\lambda_{x,y}(C_{20})=y.
\tag{8}
$$
每一个(8)都是已经过完整原函数关系和真实平移像检验的泛函；
本稿没有重新假设形式记录独立。

由(6)，存在唯一实数 $a,b,c_0$ 和一个真实 $R_*\in\mathcal R_0$，
使
$$
C_{20}=aC_2+bC_4+c_0C_6+R_*.
\tag{9}
$$
将(8)代入(9)，对所有 $x,y$ 得
$$
y=-ax+(-a+b)y.
$$
所以 $a=0,b=1$，从而
$$
\boxed{C_{20}=C_4+c_0C_6+R_*,\qquad R_*\in\mathcal R_0.}
\tag{10}
$$
系数 $c_0$ 的唯一性来自(6)的三类独立；
(8)单独看不到这个系数，本稿也未为它指定猜测值。

现在对(10)施原完整自然映射，使用(5)及
$\mathcal N(\mathcal R)=0$，准确得到(1)。
这一步不需要 $C_{20}$ 的响应展开系数，也不需要重做旧完整核。

## 3. 权零增强像与新联合核方向

[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)
及 R400 已付
$$
E(U_0)=E(\mathcal R_0),
$$
并给实际线性代表 $H_*,J_4,J_6$ 满足
$$
\begin{gathered}
E(H_*)=E(J_4)=E(J_6)=0,\\
\mathcal N(H_*)=n_2,\quad
\mathcal N(J_4)=n_4,\quad
\mathcal N(J_6)=n_6,\\
\lambda_+(H_*)=1,\qquad
\lambda_+(J_4)=\lambda_+(J_6)=0.
\end{gathered}
\tag{11}
$$
因此(1)给一个原完整联合核方向
$$
\boxed{
J_4+c_0J_6\in\ker(E,\mathcal N),\qquad
\lambda_+(J_4+c_0J_6)=0.
}
\tag{12}
$$
(12)是线性空间里的真实成员，不是已构造一条成本为此值的正时长闭路径。

更具体地，
$$
\boxed{
\begin{aligned}
\mathcal N(U_0)&=\operatorname{span}\{n_2,n_6\},\\
(E,\mathcal N)(U_0)
&=E(U_0)\oplus\operatorname{span}\{n_2,n_6\},\\
(E,\mathcal N)(U_0)/(E,\mathcal N)(\mathcal R_0)
&\simeq\operatorname{span}\{n_2,n_6\}.
\end{aligned}}
\tag{13}
$$
所以该新函数商的维数至多为二。
本稿不把“两条尚未求值函数”称为已证秩二；
$n_6$ 可以为零，$n_2$ 也可能与之相关。

## 4. 消去原正字符的准确单函数条件

R400 已证明全自然函数核与 $E$ 核都对真实正仿射作用稳定。
利用原 $U$ 的有限真权分解，
若有
$$
E(K)=\mathcal N(K)=0,\qquad\lambda_+(K)=1,
$$
则其真实权零投影具有同样性质。
这一步使用所有实紧输入上的函数身份，
不能用两个固定 profiles 的零值替代。

在权零中，(6)(11)使任意候选唯一写成
$$
K=H_*+bJ_4+cJ_6+R,\qquad
R\in\mathcal R_0\cap\ker E.
\tag{14}
$$
施 $\mathcal N$，再用(1)，得
$$
\mathcal N(K)=n_2+(c-bc_0)n_6.
\tag{15}
$$
于是存在这样的 $K$ 当且仅当 $n_2$ 是 $n_6$ 的实常数倍，证明(2)。

若 $n_6=0$，条件准确退化为 $n_2=0$；
不能因(1)给 $n_4=0$ 就漏掉 $n_2$。
若有已证明的全函数式 $n_2=a n_6$，
则 $H_*-aJ_6$ 是一个明确的联合核代表。
当前尚未得到这个全函数式。

等价地，原 $\lambda_+$ 能经过增强映射 $(E,\mathcal N)$ 下降，
当且仅当
$$
n_2\notin\operatorname{span}\{n_6\}.
\tag{16}
$$
这里只是良定义线性泛函的因子化条件。
即使未来证明(2)，也仍须保留实际成本半群的完整基准、真桥与有限联合构造；
不能把一个线性核代表等同于实际截面。

## 5. 与新的静态原式及下一最小观察

[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)
给另一个完整静态系数
$$
\Lambda_u([h^{-4}]F_0(h,0,0))
=\frac3{32}\int(u'-xu'')^4u'''.
$$
它具有自然真权 $-4$。
本稿的 $C_2,C_6$ 却是真权零的原正常记录，
所以这条已求值身份不能代替(2)的右侧。

下一真正需要求的完整函数已从三个缩为两个：
$$
u\longmapsto\Lambda_u(C_2),\qquad
u\longmapsto\Lambda_u(C_6).
$$
若消费已有原根，应只新增这两个完整自然收缩或其已付 pure-zero 代表的总通量，
保原 $N_0,\Gamma$、全部 mixed 输出和真实锚；
不得把已付的 pure/self 成员结果作为新总通量值。

本稿未执行任何新消费，也没有授权重做旧核、旧成员或旧秩。
(10)(13)是已闭的完整函数结论，
而 $c_0$ 的原数值、(2)的真假、全部低层自然像与实际 whole 联合控制仍未付。
