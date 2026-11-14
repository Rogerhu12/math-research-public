# R236 附录：实际有限头的精确真空列和不可省的进位成本

日期：2026-11-13（UTC）。作者：normal_complex；有限头原像公式由 central_review 提供，本文与 central_review 分别核验；特殊进位列及全部低头系数预算经 central_review 独核。

状态：已证明；不另立一般核结论。它证明迟首二次行的完整 MP 列成本，并在 §4.3 扩至有限条可和局部行的固定多项式，保留有限非零形式首阶假设。它没有排除允许真空误差的原像、ridge 证书或原算子的单射性。

## 1. 真实头、方向及固定首阶

在原 Haar 模型的前 $p$ 位物理正交基中，置
$$
L=2^p,\qquad
\Omega_p=L^{-1/2}\sum_{k=0}^{L-1}e_k.
$$
删除越过前缀的最后一次进位，得到真正的局部头
$$
A_p e_k=\alpha_{v_2(k+1)}e_{k+1}\quad(0\le k<L-1),
\qquad A_pe_{L-1}=0.
\tag{1.1}
$$
这是前移方向。R249 的边界矩阵采用后移方向；本稿只引用其相同的实际正权积，不把两个无限表示的向量或权域认同。

令
$$
W_0=1,\qquad
W_k=\prod_{j\in\operatorname{bits}(k)}d_j,\qquad
D_p=\operatorname{diag}(W_0,\ldots,W_{L-1}),
$$
则
$$
A_p=D_pJ_LD_p^{-1},\qquad J_Le_k=e_{k+1},\quad J_Le_{L-1}=0.
\tag{1.2}
$$
[R249 §1](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 给准确式
$$
-\log\alpha_j
=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\tag{1.3}
$$
$$
-\log d_j
=100\,16^j-105\,8^j+(150j+25)2^j
\le100\,16^j.
\tag{1.4}
$$
特别，$0<W_k\le1$，且
$$
W_{2^m-1}=\frac{d_m}{\alpha_m},\qquad
W_{2^m+s}=d_mW_s\quad(0\le s<2^m).
\tag{1.5}
$$

固定 $a,c\in\ell^1(\mathbb C)$，使用同一实际二次行
$$
Q_j^{[p]}=-2\frac{A_p^{2^j}/d_j}{I+A_p^{2^j}/d_j},\qquad
X_p=\sum_{j<p}a_jQ_j^{[p]},\quad
Y_p=\sum_{j<p}c_jQ_j^{[p]},
$$
$$
T_p=X_p^2-\sum_{j<p}a_j^2(Q_j^{[p]})^2+Y_p.
\tag{1.6}
$$
每个逆都是有限矩阵的准确逆。对应标量有理函数为
$$
f_p(z)=
2\sum_{0\le i<j<p}a_ia_jq_i(z)q_j(z)
+\sum_{j<p}c_jq_j(z),\qquad
q_j(z)=-\frac{2z^{2^j}}{d_j+z^{2^j}}.
\tag{1.7}
$$
$T_p=f_p(A_p)$；在有限头上只取模 $z^L$ 的系数即可。

假设这些逐阶稳定的形式系数有固定的有限首阶 $r\ge1$ 和非零首系数 $t_r$。因此充分大 $p$ 时
$$
f_p(z)=z^rg_p(z),\qquad g_p(0)=t_r\ne0.
\tag{1.8}
$$
本稿不把无限慢形式级数声明为收敛芽。所用每个 $f_p$ 都只是一个有限有理函数。

迟首二次余族具有上述固定首阶。例如 $a$ 至少有两个非零位置，$j_0=\min\operatorname{supp}a$，且 $c_j=0$ 对 $j\le j_0$ 时，主行前两个非零位置产生的最低交叉次数，其二进赋值恰为 $j_0$；辅助行的所有次数均被 $2^{j_0+1}$ 整除，所以不可能把全部形式系数消掉。

## 2. 完整最小范数原像及加权卷积

固定整数幂 $q\ge1$，记
$$
d=rq<L,\qquad
g_p(z)^{-q}=\sum_{n\ge0}u_{p,q,n}z^n.
\tag{2.1}
$$
这里只需要有限多个系数。令
$$
\mathcal L_{p,q}
=D_pJ_L^{*d}g_p(J_L)^{-q}D_p^{-1}.
$$
全部函数 $J_L$ 的因子交换，所以准确地
$$
\mathcal L_{p,q}T_p^q
=D_pJ_L^{*d}J_L^dD_p^{-1}
=P_{[0,L-d)}.
\tag{2.2}
$$
于是
$$
(T_p^q)^*\mathcal L_{p,q}^*\Omega_p
=P_{[0,L-d)}\Omega_p.
\tag{2.3}
$$

又
$$
(T_p^q)^*
=D_p^{-1}g_p(J_L)^{*q}J_L^{*d}D_p,
$$
其中 $g_p(J_L)^{*q}$ 可逆，故
$$
\ker(T_p^q)^*=\operatorname{span}\{e_0,\ldots,e_{d-1}\}.
\tag{2.4}
$$
把 $\mathcal L_{p,q}^*\Omega_p$ 的底部 $d$ 个坐标置零，所得 $\xi_{p,q}$ 是 (2.3) 的唯一最小范数解，即完整 Moore–Penrose 解。

对 $d\le k<L$，逐项相乘得
$$
\boxed{
(\xi_{p,q})_k=
\frac1{\sqrt L\,W_k}
\sum_{n=0}^{L-1-k}
\overline{u_{p,q,n}}\,W_{k-d+n};
\qquad
(\xi_{p,q})_k=0\ (k<d).
}
\tag{2.5}
$$
复共轭只落在逆系数上，真实权 $W_k$ 为正实数。

目标残量与解的自由核是两个不同端点：
$$
\boxed{
\|\Omega_p-(T_p^q)^*\xi_{p,q}\|
=\sqrt{\frac{rq}{2^p}}.
}
\tag{2.6}
$$
(2.6) 是顶部 $d$ 个目标坐标；(2.4) 是底部 $d$ 个解坐标。两者不能互换。

## 3. 一条不丢长卷积的进位坐标

以下置
$$
m=p-1,\qquad rq=d\le2^m,\qquad
k_*=2^m+d-1.
$$
(1.5) 给
$$
W_{k_*}=d_mW_{d-1},\qquad
W_{k_*-d}=W_{2^m-1}=\frac{d_m}{\alpha_m}.
$$
对 $n\ge1$，(2.5) 涉及的其余权为
$$
W_{k_*-d+n}=W_{2^m-1+n}=d_mW_{n-1}.
$$
所以完整长卷积准确化为
$$
\boxed{
(\xi_{p,q})_{k_*}
=\frac1{\sqrt L\,W_{d-1}}
\left[
\frac{\overline{t_r^{-q}}}{\alpha_m}
+\sum_{n=1}^{2^m-d}\overline{u_{p,q,n}}W_{n-1}
\right].
}
\tag{3.1}
$$
未删除任何长卷积项。下一节估计整个和。

令 $f_m$ 是删除最高行 $j=m$ 的低头符号。最高辅助项的首项是 $-2c_mz^{2^m}/d_m$，所有含最高位的交叉项至少从 $2^m+1$ 次开始。因此
$$
f_p(z)-f_m(z)
=-\frac{2c_m}{d_m}z^{2^m}+O(z^{2^m+1}),
$$
$$
g_p(z)-g_m(z)
=-\frac{2c_m}{d_m}z^{2^m-r}+O(z^{2^m-r+1}).
\tag{3.2}
$$

若 $q\ge2$，则 $2^m-rq<2^m-r$。故 (3.1) 中用到的全部逆系数与 $g_m^{-q}$ 的对应系数相同。

若 $q=1$，唯一可能改变的是最后一个系数：
$$
[z^{2^m-r}]g_p^{-1}
=[z^{2^m-r}]g_m^{-1}
+\frac{2c_m}{d_mt_r^2}.
\tag{3.3}
$$
由二进制补集恒等式
$$
\frac{W_{2^m-r-1}}{W_{2^m-1}}=\frac1{W_r},
$$
最高行对 (3.1) 的整个主项只产生以下准确修正：
$$
\frac{\overline{t_r^{-1}}}{\alpha_m}
\left(1+\frac{2\overline{c_m}}{\overline{t_r}W_r}\right).
\tag{3.4}
$$
因为 $c_m\to0$，括号的模最终至少为 $3/4$。这里没有漏掉最高行，也未假设逆系数同号。

## 4. 低头系数圆及统一主项支配

取
$$
R_m=\exp(-400\,8^{m-1}).
\tag{4.1}
$$
对 $j<m$、$|z|=R_m$，由 (1.4)
$$
\left|\frac{z^{2^j}}{d_j}\right|
\le
\exp[-400\,8^{m-1}2^j+100\,16^j]
\le\exp[-300\,8^{m-1}2^j].
\tag{4.2}
$$
因此全部低位分母在此圆及其内部非零，且各归一化变量一致趋零。

进一步有
$$
\boxed{
\sup_{|z|\le R_m}
\left|\frac{g_m(z)}{t_r}-1\right|\longrightarrow0.
}
\tag{4.3}
$$
完整理由如下。先固定 $J$，使 $2^J>4r$ 且 $f_J$ 已具有首项 $t_rz^r$。固定有理函数 $f_J(z)/z^r=t_r+O(z)$，所以其余项在 $R_m$ 圆上趋零。对 $J\le j<m$，(4.2) 及分母下界给
$$
R_m^{-r}|q_j(z)|
\le4\exp[-300\,8^{m-1}2^j+400r\,8^{m-1}]
\le4e^{-200\,8^{m-1}2^j}.
$$
高位辅助和由 $4\|c\|_1e^{-200\,8^{m-1}2^J}$ 支配。含至少一个高位的交叉和同样由固定常数乘此指数支配：另一因子用 $|q_i(z)|\le4$，所有系数用 $\|a\|_1^2$。这付清 $f_m-f_J$ 除以 $z^r$ 的全部项。先在边界得 (4.3)，再用最大模原理延至整个圆盘。

故充分大 $m$ 时，$g_m$ 在此盘上无零，且
$$
|g_m(z)^{-q}|\le |t_r|^{-q}2^q
\quad(|z|\le R_m,\ q\ge1).
$$
Cauchy 给所有系数
$$
|[z^n]g_m(z)^{-q}|
\le |t_r|^{-q}2^q R_m^{-n}.
\tag{4.4}
$$
这个估计对所需全部 $q$ 一致。因为 $W_{n-1}\le1$，$q\le2^m/r$，
$$
\begin{aligned}
\sum_{n=1}^{2^m-rq}
|[z^n]g_m^{-q}|W_{n-1}
&\le |t_r|^{-q}2^q2^mR_m^{-2^m}\\
&=|t_r|^{-q}
\exp[50\,16^m+q\log2+m\log2]\\
&\le |t_r|^{-q}\exp[50\,16^m+O(2^m)].
\end{aligned}
\tag{4.5}
$$
空和也满足该界。$O(2^m)$ 的常数可固定，不依允许范围内的 $q$。

另一方面，(1.3) 给
$$
\alpha_m^{-1}
=\exp\left[\frac{280}{3}16^m+O(8^m)\right].
\tag{4.6}
$$
$280/3>50$，所以 (4.5) 相对 $|t_r|^{-q}/\alpha_m$ 一致趋零。结合 (3.1)—(3.4)，得到：

**命题。** 存在只依固定 $a,c,r,t_r$ 的 $p_0$，使所有 $p\ge p_0$ 及所有整数 $1\le rq\le2^{p-1}$ 均满足
$$
\boxed{
\|\xi_{p,q}\|
\ge |(\xi_{p,q})_{2^{p-1}+rq-1}|
\ge
\frac{|t_r|^{-q}}
{4\,2^{p/2}\alpha_{p-1}W_{rq-1}}.
}
\tag{4.7}
$$
这是同一个完整最小范数真空列的下界，不是把环境逆范数的下界强加到某一向量上。

由于 $W_{rq-1}\le1$，对该整个范围还有
$$
\log\|\xi_{p,q}\|
\ge
\frac{35}{6}16^p-\frac{45}{4}8^p
+150\,2^p-O(p+q+1).
\tag{4.8}
$$
因此，任意满足 $rq_p/2^p\to0$ 的整数幂序列都满足
$$
\boxed{
\liminf_{p\to\infty}
\frac{\log\|\xi_{p,q_p}\|}{16^p}\ge\frac{35}{6}.
}
\tag{4.9}
$$
此处先给完整列下界；§4.2 将保留共同权比并证明精确主指数。

### 4.1 完整列上界及真实低头 carry 的正向支付

上述下界不表示低头进位误差也无法支付。对所有充分大 $p$，把 (4.3)—(4.4) 的指标改成 $p$，在同一个实际全头符号 $g_p$ 上有
$$
|u_{p,q,n}|
\le |t_r|^{-q}2^q R_p^{-n},
\qquad R_p=e^{-400\,8^{p-1}}.
\tag{4.10}
$$
真实权沿整数链递减，因此 $W_k\ge W_{L-1}$。用 (2.5) 逐坐标相加，至多 $L$ 项、至多 $L$ 个坐标，得到保守但完整的上界
$$
\boxed{
\|\xi_{p,q}\|
\le
\frac{L\,2^q|t_r|^{-q}R_p^{-L}}{W_{L-1}}.
}
\tag{4.11}
$$
由 R249 的准确权积
$$
-\log W_{L-1}
=\frac{20}{3}16^p-15\,8^p+(150p-275)2^p+\frac{850}{3},
$$
以及 $L\log R_p^{-1}=50\,16^p$，可得
$$
\boxed{
\log\|\xi_{p,q}\|
\le\frac{170}{3}16^p+O(8^p+p2^p+q),
\qquad 1\le rq\le2^{p-1}.
}
\tag{4.12}
$$
常数只依固定系数行及首项，统一于所列整数幂。

现在回到全 Haar 空间，并定义真实低行
$$
X_{<p}=\sum_{j<p}a_jQ_j,\quad
Y_{<p}=\sum_{j<p}c_jQ_j,\quad
B_{<p}=\sum_{j<p}a_j^2Q_j^2,\quad
\widehat T_p=X_{<p}^2-B_{<p}+Y_{<p}.
$$
这里每个 $Q_j$ 都是完整实际算子；$\widehat T_p$ 不等于局部 $T_p\otimes I$。

保留精确进位参数，实际头比较为
$$
\|N_j-N_j^{[p]}\otimes I\|
=\alpha_p/\alpha_j\le\eta_{p-1}\quad(j<p).
$$
Cayley 逆差公式给对应 $Q_j$ 差至多固定常数乘此量。再对平方作有序望远镜，并使用
$\|a\|_1,\|c\|_1,\sum|a_j|^2<\infty$，得到固定 $C_T$：
$$
\|\widehat T_p-T_p\otimes I\|\le C_T\eta_{p-1}.
\tag{4.13}
$$
该式也正是前述真核 HS 稿中实际头与局部头的比较，此处只把原来的粗指数恢复成真实 $\eta$。取固定 $M\ge1$ 一致控制两个头的算子范数，则
$$
\|\widehat T_p^{\,q}-(T_p\otimes I)^q\|
\le C_TqM^{q-1}\eta_{p-1}.
\tag{4.14}
$$
不用两个不同头互相交换。

准确参数是
$$
-\log\eta_{p-1}
=\frac{175}{2}16^p-\frac{315}{4}8^p+150\,2^p.
$$
因此 (4.12)—(4.14) 给
$$
\boxed{
\|[\widehat T_p^{\,q}-(T_p\otimes I)^q]^*
(\xi_{p,q}\otimes\Omega_{\ge p})\|
\le
\exp\!\left[-\frac{185}{6}16^p+O(8^p+p2^p+q)\right].
}
\tag{4.15}
$$
这里 $185/6=175/2-170/3>0$。使用粗 $770\,16^{p-1}$ 会丢掉这个已付余量，故不能在此步提前粗化。

结合 (2.6)，真实低行确有以下全空间近真空原像：
$$
\boxed{
\|\Omega-(\widehat T_p^{\,q})^*
(\xi_{p,q}\otimes\Omega_{\ge p})\|
\le
\sqrt{\frac{rq}{2^p}}
+\exp\!\left[-\frac{185}{6}16^p+O(8^p+p2^p+q)\right].
}
\tag{4.16}
$$
当 $rq/2^p\to0$ 时右端趋零。全部低头真实进位已经支付；尚未支付的是把 $\widehat T_p$ 再换为含全部慢尾的原 $T$，其费用正由下一节单独比较。

### 4.2 保留完整权比后的精确 MP 型与更强真实 carry 余量

本节保留 §4.1 的完整粗界，并把同一完整真空列的上下主指数夹到一起。仍固定首阶 $r$ 和 $t_r\ne0$，令
$$
L=2^p,\qquad d=rq,\qquad 1\le d\le L/2.
$$
定义更接近临界值的系数圆
$$
\varepsilon_p=2^{-p/2},\qquad
\ell_p=(100+\varepsilon_p)8^{p-1},\qquad
\varrho_p=e^{-\ell_p}.
\tag{4.17}
$$

**第一步：全部早位与最高位的圈预算。** 对 $j\le p-2$，由准确权界 $\Lambda_j=-\log d_j\le100\,16^j$，
$$
\Lambda_j\le\frac{100}{8}\,8^{p-1}2^j.
$$
所以在 $|z|=\varrho_p$，
$$
\log|z^{2^j}/d_j|
\le-\left(\frac{175}{2}+\varepsilon_p\right)8^{p-1}2^j.
\tag{4.18}
$$
另对最高位 $j=p-1$，
$$
\begin{aligned}
\log|z^{2^{p-1}-r}/d_{p-1}|
&=-\ell_p(2^{p-1}-r)+\Lambda_{p-1}\\
&\le-\varepsilon_p16^{p-1}+O_r(8^p)
\longrightarrow-\infty.
\end{aligned}
\tag{4.19}
$$
因为 $\varepsilon_p16^{p-1}=2^{(7/2)p-4}$，它严格压住固定 $r$ 的 $O(8^p)$ 项。

为说明这里没有遗漏任何早位，先固定 $J$，使 $2^J>4r$ 且 $f_J$ 已有首项 $t_rz^r$。固定有理函数 $f_J/z^r=t_r+O(z)$ 在此圈上趋于 $t_r$。对 $J\le j\le p-2$，把 (4.18) 除以 $\varrho_p^r$；用 $\varepsilon_p\le1$ 和 $2^j>4r$，所得指数不超过
$$
-50\,8^{p-1}2^j.
$$
所有这些项的辅助系数和交叉系数分别由 $\|c\|_1$、$\|a\|_1^2$ 控制。各 Cayley 分母一致离零，另一交叉因子可统一有界处理。因此整个中间高位和趋零。含最高位的辅助项及交叉项由 (4.19) 同样趋零，且没有用最高行的符号。

所以最大模原理给
$$
\sup_{|z|\le\varrho_p}
\left|\frac{g_p(z)}{t_r}-1\right|\longrightarrow0.
\tag{4.20}
$$
充分大 $p$ 时，$g_p$ 在该盘上无零。对所有整数 $q\ge1$，同一个盘因此给
$$
\boxed{
|u_{p,q,n}|
\le |t_r|^{-q}2^q e^{\ell_p n}
\qquad(n\ge0).
}
\tag{4.21}
$$
(4.20) 不需要关于 $q$ 的更强趋零率；取逆的 $q$ 次幂产生的全部因子已明确保留为 $2^q$。

**第二步：把每一项的正缩放权一起估计。** 置
$$
\omega_k=-\log W_k,\qquad F_p(k)=\ell_pk-\omega_k\quad(0\le k<L).
$$
由于实际 bit 加性，
$$
F_p(k)=\sum_{j\in\operatorname{bits}(k)}
(\ell_p2^j-\Lambda_j).
$$
每个被加项均非负：$j<p$ 时
$\ell_p2^j\ge100\,8^{p-1}2^j\ge100\,16^j\ge\Lambda_j$。
故
$$
\boxed{0\le F_p(k)\le F_p(L-1).}
\tag{4.22}
$$
不需要 $F_p(k)$ 随整数 $k$ 单调。

对 (2.5) 中任意一项，令 $v=k-d+n$。所有实际指标均满足 $0\le v,k<L$，并且准确有
$$
\ell_p n+\omega_k-\omega_v
=F_p(v)-F_p(k)+d\ell_p
\le F_p(L-1)+d\ell_p.
$$
用 (4.21) 逐项相加，再对坐标取 Hilbert 范数，得到
$$
\boxed{
\|\xi_{p,q}\|
\le L\,2^q|t_r|^{-q}
\exp\!\left[F_p(L-1)+d\ell_p\right].
}
\tag{4.23}
$$
这里始终保留 $W_v/W_k$ 的真实共同位置；没有把 $W_v$ 与 $W_k^{-1}$ 独立取最坏界。

准确求和给
$$
\frac{F_p(L-1)}{L^4}\longrightarrow
\frac{100}{8}-\frac{20}{3}=\frac{35}{6},
\qquad
\frac{d\ell_p}{L^4}
=\left(\frac{25}{2}+\frac{\varepsilon_p}{8}\right)\frac dL.
$$
而 $q\le L/(2r)$，所以 (4.23) 中 $q\log(2/|t_r|)+\log L$ 除以 $L^4$ 一致趋零。因此在整个允许范围
$$
\boxed{
\frac{\log\|\xi_{p,q}\|}{16^p}
\le\frac{35}{6}+\frac{25}{2}\frac{rq}{2^p}+o(1),
}
\tag{4.24}
$$
其中 $o(1)$ 对所列整数幂一致。

结合 §4 已付的同一列下界 (4.7)—(4.9)，任意整数幂序列满足 $rq_p/2^p\to0$ 时，得到精确极限
$$
\boxed{
\lim_{p\to\infty}
\frac{\log\|\xi_{p,q_p}\|}{16^p}
=\frac{35}{6}.
}
\tag{4.25}
$$
所以这里确是完整精确投影真空 MP 列的主指数。没有把这个极限声明为允许目标误差的最优原像成本；§6 的实际 $A_p$ 校准仍然适用。

**第三步：真实低头的进位余量。** 继续使用 §4.1 的准确
$$
\|\widehat T_p-T_p\otimes I\|\le C_T\eta_{p-1},
\qquad
-\log\eta_{p-1}
=\frac{175}{2}16^p-\frac{315}{4}8^p+150\,2^p.
$$
在 $rq_p=o(2^p)$ 时，(4.25) 和有序幂望远镜给
$$
\boxed{
\|[\widehat T_p^{\,q_p}-(T_p\otimes I)^{q_p}]^*
(\xi_{p,q_p}\otimes\Omega_{\ge p})\|
\le
\exp\!\left[-\left(\frac{245}{3}+o(1)\right)16^p\right].
}
\tag{4.26}
$$
这里 $245/3=175/2-35/6$，额外的 $q_pM^{q_p-1}$ 只贡献 $O(q_p+\log q_p)=o(16^p)$。

因而在同一范围，真实低行的近真空式增强为
$$
\boxed{
\|\Omega-(\widehat T_p^{\,q_p})^*
(\xi_{p,q_p}\otimes\Omega_{\ge p})\|
\le
\sqrt{\frac{rq_p}{2^p}}
+\exp\!\left[-\left(\frac{245}{3}+o(1)\right)16^p\right].
}
\tag{4.27}
$$
若只要求统一 $rq\le2^{p-1}$，(4.24) 也给上主指数 $145/12$，从而真实 carry 仍有统一正余量 $905/12$。前者等于 $35/6+25/4$，后者等于 $175/2-145/12$。

本节优化的是已存在的完整 MP 列及真实低头比较。把 $\widehat T_p$ 换成包含全部慢尾的原 $T$，仍须支付 §5 的独立预算；本节没有取消那一步。


### 4.3 有限条可和局部行的固定多项式

本节只扩大同一完整 MP 列和真实低头 carry 估计的适用类；不附加任何新的慢尾速率。允许全部系数为复数。

固定有限个行，$1\le\nu\le s$：
$$
R_\nu=
\sum_{j\ge0}
\left(a_{\nu j}N_j+b_{\nu j}Q_j+e_{\nu j}Q_j^2\right),
\qquad
a_\nu,b_\nu,e_\nu\in\ell^1(\mathbb C).
\tag{4.28}
$$
取固定的复多项式 $P$，满足 $P(0,\ldots,0)=0$。定义
$$
T=P(R_1,\ldots,R_s).
$$
所有行及 $T$ 都是真实有界交换代数元素。平方局部项用于同时包含原稿的 $B_0$ 行；没有假设它能写成线性 $N_j,Q_j$ 行。

与原稿相同，局部 $p$ 头由 $j<p$ 的实际局部 $N_j^{[p]},Q_j^{[p]}$ 定义：
$$
R_{\nu,p}
=\sum_{j<p}
\left(a_{\nu j}N_j^{[p]}
+b_{\nu j}Q_j^{[p]}
+e_{\nu j}(Q_j^{[p]})^2\right),
\qquad
T_p=P(R_{1,p},\ldots,R_{s,p}).
\tag{4.29}
$$
其标量符号是
$$
r_{\nu,p}(z)
=\sum_{j<p}
\left(
a_{\nu j}\frac{z^{2^j}}{d_j}
+b_{\nu j}q_j(z)+e_{\nu j}q_j(z)^2
\right),
\qquad
f_p(z)=P(r_{1,p}(z),\ldots,r_{s,p}(z)).
\tag{4.30}
$$
每个 $r_{\nu,p}(0)=0$。逐个有限次数的系数最终稳定。明确假设其形式首项非零且有限：
$$
f_p(z)=t_rz^r+O(z^{r+1}),\qquad
t_r\ne0,\quad r\ge1
\tag{4.31}
$$
对全部充分大 $p$ 成立。本节不推断每个实际非零元素都必有这样的形式首阶，也不声明无限形式符号在零附近收敛。

固定整数幂 $q$，仍令 $d=rq<L=2^p$，并定义 $g_p=f_p/z^r$ 及原稿的完整 MP 列 $\xi_{p,q}$。

**低头圈与上界。** 在 §4 的粗圈或 §4.2 的锋利圈上，所有归一化变量 $z^{2^j}/d_j$ 一致趋零。局部三个函数
$$
u,\qquad -2u/(1+u),\qquad 4u^2/(1+u)^2
$$
均在该小盘上有固定界 $C|u|$。因此原稿中固定早位、全部中间高位及最高位的三段估计，对每个 $r_{\nu,p}$ 逐项成立。固定多项式的差可以写成有限个“一个行差乘其他有界行因子”的和。选定足够大、但与 $p$ 无关的 $J$ 后，$f_J/z^r=t_r+O(z)$；其余每一项至少含一个高位行差，除以 $z^r$ 后仍由原稿相同指数支配。

于是 §4.2 的准确结论保持：
$$
\sup_{|z|\le\varrho_p}|g_p(z)/t_r-1|\to0,\qquad
|[z^n]g_p(z)^{-q}|
\le |t_r|^{-q}2^q e^{\ell_p n}.
\tag{4.32}
$$
常数及充分大 $p$ 的门槛可以依固定 $P$ 与这些行，不能依所允许的整数幂 $q$。此后完整权比的 bit-$F_p$ 估计完全不变，故原稿的 MP 上界 (4.23)—(4.24) 保持。

**最高位首系数与下界。** 令 $m=p-1$。新增最高位在第 $\nu$ 行中的首项为
$$
r_{\nu,p}(z)-r_{\nu,m}(z)
=\frac{a_{\nu m}-2b_{\nu m}}{d_m}z^{2^m}
+O(z^{2^m+1}).
$$
$Q_m^2$ 最早从 $2^{m+1}$ 次出现，不影响这里的系数。由于全部旧行在零点为零，固定多项式的 Taylor 展开给
$$
f_p(z)-f_m(z)
=\frac{\widetilde d_m}{d_m}z^{2^m}
+O(z^{2^m+1}),
$$
$$
\boxed{
\widetilde d_m
=\sum_{\nu=1}^s
(\partial_\nu P)(0)\,(a_{\nu m}-2b_{\nu m})
\longrightarrow0.
}
\tag{4.33}
$$
若 $P$ 的全部一次偏导在零点为零，则 $\widetilde d_m=0$，此时最高位甚至不改变所需端点系数。

对 $q\ge2$，原 (3.1) 只读取次数不超过 $2^m-rq<2^m-r$ 的逆系数，所以最高位仍完全不进入。对 $q=1$，准确改变量变为
$$
[z^{2^m-r}]g_p^{-1}
=[z^{2^m-r}]g_m^{-1}
-\frac{\widetilde d_m}{d_mt_r^2}.
$$
因此特殊进位列的主项修正为
$$
\boxed{
\frac{\overline{t_r^{-1}}}{\alpha_m}
\left(1-\frac{\overline{\widetilde d_m}}
{\overline{t_r}W_r}\right).
}
\tag{4.34}
$$
其括号最终一致离零，因为 $\widetilde d_m\to0$。原粗低头余项仍由 $e^{50\,16^m+O(2^m)}$ 支配，严格低于 $\alpha_m^{-1}$ 的主指数。故 (4.7) 的统一列下界仍成立，至多调整固定门槛。

与 (4.32) 的锋利上界合并，得到同一个精确型：
$$
\boxed{
\lim_{p\to\infty}
\frac{\log\|\xi_{p,q_p}\|}{16^p}
=\frac{35}{6}
\quad\text{只要 }rq_p/2^p\to0.
}
\tag{4.35}
$$
原 (2.6) 的目标残量 $\sqrt{rq_p/2^p}$ 也保持，因为它只用固定首阶分解与真实加权链。

**真实低头比较。** 令
$$
\widehat R_{\nu,p}
=\sum_{j<p}
(a_{\nu j}N_j+b_{\nu j}Q_j+e_{\nu j}Q_j^2),
\qquad
\widehat T_p=P(\widehat R_{1,p},\ldots,\widehat R_{s,p}).
$$
这些是全空间的真实低行，不是局部矩阵。对 $j<p$，$N_j$ 的实际头差至多 $\eta_{p-1}$；Cayley 逆差至多 $18\eta_{p-1}$。可统一取 $\|Q_j\|,\|Q_j^{[p]}\|\le6$，所以平方差至多 $216\eta_{p-1}$。所有系数可和，故每行之差至多固定常数乘 $\eta_{p-1}$。

再对固定多项式按有序乘积望远镜，得到
$$
\|\widehat T_p-T_p\otimes I\|
\le C_P\eta_{p-1}.
\tag{4.36}
$$
全部行范数一致有界，故常数独立于 $p$。随后的幂望远镜及精确 $\eta$ 指数与 §4.2 完全相同。因此当 $rq_p=o(2^p)$ 时，真实 carry 仍由
$$
\exp[-(245/3+o(1))16^p]
$$
支付，且 (4.27) 的真实低行近真空式保持。

这里没有给原 $T-\widehat T_p$ 的新增速率。一般 $\ell^1$ 行只保证慢尾趋零；本节不把这种定性收敛与完整 MP 费用自动相乘，也不将 §5 的特定指数尾预算扩展到无速率的行。

### 4.4 固定非零有限柱目标与完整卷积

固定一个非零有限物理柱函数 $f$，其前缀长度为 $\ell$，并记
$$
D=2^\ell,\qquad
f_s=f(s)\ (0\le s<D),\qquad
M_f=\max_{s<D}|f_s|.
$$
$f$ 独立于 $p,q$。在 $p\ge\ell$ 的标准物理正交基中，准确向量归一为
$$
f_p=2^{-p/2}\sum_{k=0}^{2^p-1} f_{\,k\bmod D}\,e_k,
\qquad
\|f_p\|^2=\frac1D\sum_{s=0}^{D-1}|f_s|^2.
\tag{4.37}
$$
无限空间中 $f=f_p\otimes\Omega_{\ge p}$。不把柱函数的剩余类取值与其正交基系数混为一谈。

**固定目标的循环性。** [R88 §6](R88-riesz-basis-bounded-multipliers-strong-closure.md) 的准确实际公式为
$$
p_f(z)=\sum_{s<D}\frac{f_s}{W_s}z^s,\qquad
Z_\ell=\prod_{j<\ell}(I+N_j),\qquad
X_f=p_f(A)Z_\ell^{-1},\quad X_f\Omega=f.
$$
因为 $f\ne0$，$p_f$ 是非零多项式。写 $p_f(z)=z^su(z)$、$u(0)\ne0$，则 $X_f$ 为 $A^s$ 乘实际单位，所以单射且值域稠密。它与 $A$ 交换，$\Omega$ 对 $A$ 循环，因此 $f$ 对 $A$ 循环。$\mathcal Cf$ 也是非零有限柱，同样对 $A$ 循环；反酉关系给 $f$ 对 $A^*$ 循环，因而也对全部 $(A')^*$ 循环。这里只使用固定有限柱，未把这个结论延至任意变化目标。

**完整最小范数列。** 保持原稿固定首阶 $r,t_r$，令 $L=2^p$、$d=rq<L$。求
$$
(T_p^q)^*\xi_{p,q}^{\,f}=P_{[0,L-d)}f_p
$$
的最小范数解。与 §2 相同，$\ker(T_p^q)^*$ 恰为底部 $d$ 个物理坐标，故解在这 $d$ 个坐标上必须取零。其余坐标的完整式为
$$
\boxed{
(\xi_{p,q}^{\,f})_k
=\frac1{\sqrt L\,W_k}
\sum_{n=0}^{L-1-k}
\overline{u_{p,q,n}}\,W_{k-d+n}
 f_{\,(k-d+n)\bmod D}
\quad(d\le k<L).
}
\tag{4.38}
$$
目标的复取值没有取共轭；共轭仍只在逆级数系数上。顶部目标误差满足
$$
\boxed{
\|f_p-(T_p^q)^*\xi_{p,q}^{\,f}\|
\le M_f\sqrt{d/L}.
}
\tag{4.39}
$$

定义从前缀末端数起的第一个非零取值位置：
$$
t=\min\{0\le s<D:f_{D-1-s}\ne0\},\qquad
\theta=f_{D-1-t}\ne0.
\tag{4.40}
$$
以下明确加条件
$$
t+r<d=rq\le2^{p-1}.
\tag{4.41}
$$
它允许固定 $q$；并不要求 $q\to\infty$。任何增长的整数幂 $q_p\to\infty$ 最终满足左侧条件，但右侧仍须单独保持。

取 $m=p-1\ge\ell$ 及
$$
k_*=2^m+d-1-t.
$$
由 (4.41)，$d\le k_*<L$，且
$$
W_{k_*}=d_mW_{d-1-t},\qquad
W_{2^m-1-t}=\frac{d_m}{\alpha_mW_t}.
$$
在 (4.38) 中，$1\le n\le t$ 的目标取值全部为零，正是 (4.40) 的最小性。$n=0$ 的目标为 $\theta$；对 $n>t$，目标与权均进入进位后的低段。因此准确有
$$
\boxed{
(\xi_{p,q}^{\,f})_{k_*}
=\frac1{\sqrt L\,W_{d-1-t}}
\left[
\frac{\overline{t_r^{-q}}\theta}{\alpha_mW_t}
+
\sum_{n=t+1}^{2^m-d+t}
\overline{u_{p,q,n}}\,W_{n-1-t}
 f_{\,(n-1-t)\bmod D}
\right].
}
\tag{4.42}
$$
若上界小于下界，此和按零处理。这里保留了全部 $n>t$ 的长卷积。

(4.41) 给 $2^m-d+t<2^m-r$。因此 (4.42) 中读取的所有逆系数都来自低头 $g_m^{-q}$；最高位的新项完全不进入。用 §4 的粗低头圆
$R_m=e^{-400\,8^{m-1}}$，得到
$$
\begin{aligned}
\left|
\sum_{n=t+1}^{2^m-d+t}
\overline{u_{p,q,n}}W_{n-1-t}
 f_{\,(n-1-t)\bmod D}
\right|
&\le M_f|t_r|^{-q}2^q2^mR_m^{-2^m}\\
&\le M_f|t_r|^{-q}
e^{50\,16^m+O(2^m)}.
\end{aligned}
\tag{4.43}
$$
上式对 (4.41) 中全部整数幂一致。$M_fW_t/|\theta|$ 是固定常数，而
$-\log\alpha_m=(280/3)16^m+O(8^m)$。所以 (4.43) 相对 (4.42) 的唯一主项一致趋零。充分大 $p$ 时，
$$
\boxed{
\|\xi_{p,q}^{\,f}\|
\ge
\frac{|\theta|\,|t_r|^{-q}}
{4\sqrt L\,\alpha_{p-1}W_tW_{rq-1-t}}.
}
\tag{4.44}
$$
门槛可以依固定 $f$、$r,t_r$ 和固定系数行，但不依所允许的 $q$。

另一方面，在 §4.2 的 bit-$F_p$ 上界中只需额外乘上 $M_f$。因此
$$
\|\xi_{p,q}^{\,f}\|
\le M_f L\,2^q|t_r|^{-q}
e^{F_p(L-1)+rq\,\ell_p}.
\tag{4.45}
$$
(4.44)—(4.45) 给出：

对任意固定非零有限柱 $f$，若整数幂序列满足
$$
rq_p>t+r\quad\text{最终成立},\qquad rq_p/2^p\to0,
$$
则
$$
\boxed{
\lim_{p\to\infty}
\frac{\log\|\xi_{p,q_p}^{\,f}\|}{16^p}
=\frac{35}{6}.
}
\tag{4.46}
$$
这包括全部增长幂序列，也包括满足所列固定门槛的有界幂序列。原 §4.3 的有限多项式行类同样适用，因为此处只读取其最高位新项开始之前的系数。

真实低头比较的费用也只多固定因子 $M_f$。在上述序列范围，(4.26)—(4.27) 相应给
$$
\|f-(\widehat T_p^{\,q_p})^*
(\xi_{p,q_p}^{\,f}\otimes\Omega_{\ge p})\|
\le
M_f\sqrt{\frac{rq_p}{2^p}}
+\exp[-(245/3+o(1))16^p].
\tag{4.47}
$$
全部低头 carry 已付；原完整慢尾仍单独保留。

**范围。** 本节的单最高位证明要求 (4.41)，未过门槛的固定小幂由下节 §4.5 的完整多高位卷积补齐；仍不将 (4.46) 外推到随 $p$ 改变的目标。


### 4.5 固定幂数、任意固定有限柱目标的完整高位卷积

本节仍只考察有限头的 **exact projected-target** Moore–Penrose 原像。
允许目标随 $p$ 改变并保留小误差的 ridge 问题不在以下下界内。

先固定原近共振二次行
$$
\mathfrak t_p(z)
 =\left(\sum_{j<p}a_jQ_j(z)\right)^2
  -\sum_{j<p}a_j^2Q_j(z)^2+\sum_{j<p}c_jQ_j(z),
\qquad
Q_j(z)=-\frac{2z^{2^j}/d_j}{1+z^{2^j}/d_j}.
\tag{4.50}
$$
$a,c\in\ell^1$，且稳定形式首项为 $t_rz^r\ne0$。
这里用 $\mathfrak t_p$ 表示算子 $T_p$ 的标量函数，避免与目标向量 $f_p$ 混淆。
设
$$
\mathfrak t_p(z)=z^rg_p(z),\qquad
g_p(z)^{-q}=\sum_{n\ge0}u_{p,q,n}z^n.
$$
本节的 $q\ge1$ 是固定整数，不随 $p$ 改变。

固定 §4.4 的非零有限柱 $f$，前缀长度 $\ell$、$D=2^\ell$，并记
$$
t=\min\{s:0\le s<D,\ f_{D-1-s}\ne0\},\qquad
\theta=f_{D-1-t},\qquad d=rq.
\tag{4.51}
$$
所有 $f_s$ 都是柱函数取值；实际头向量含 $2^{-p/2}$ 归一因子。
$\xi^f_{p,q}$ 始终指
$$
(T_p^q)^*\xi^f_{p,q}=P_{[0,2^p-d)}f_p,\qquad
\xi^f_{p,q}\perp\ker (T_p^q)^*
$$
的最小范数解。因此其底部 $d$ 个坐标为零，删去的是目标顶部 $d$ 个坐标。

本节证明：

1. 若 $t<d$，只用 $a_j,c_j\to0$ 就有
   $$
   \lim_{p\to\infty}\frac{\log\|\xi^f_{p,q}\|}{16^p}
   =\frac{35}{6}.
   \tag{4.52}
   $$

2. 若 $t\ge d$，再假设 $c_j$ 最终非零，且
   $$
   \log\frac1{|c_j|}=o(16^j),
   \tag{4.53}
   $$
   则仍有严格正的四次型下界。准确地，令
   $$
   K=\left\lceil\frac{t+1}{r}\right\rceil,\qquad
   s=rK-t-1,\qquad k=d+s.
   \tag{4.54}
   $$
   此时 $K\ge q+1\ge2$、$0\le s<r$，$k$ 是与 $p$ 无关的合法源坐标。
   有
   $$
   \lim_{p\to\infty}
   \frac{\log|(\xi^f_{p,q})_k|}{16^{p-K+1}}
   =\frac{280}{3},
   \tag{4.55}
   $$
   因而
   $$
   \liminf_{p\to\infty}
   \frac{\log\|\xi^f_{p,q}\|}{16^p}
   \ge \frac{35}{6}\,16^{2-K}>0.
   \tag{4.56}
   $$

第二项没有声称整个源范数具有 (4.56) 的精确型。
原来的 $c_j=e^{-\kappa\beta j^\alpha}$（只在首个允许位置以后取值）
满足 (4.53)，所以这两项覆盖该行的每个固定 $q$ 与每个固定非零有限柱 $f$。

#### 4.5.1 $t<d$：最高新行的全部有限修正

令 $m=p-1$、$L=2^p$，选取
$$
k_p=2^m+d-1-t.
$$
当 $p$ 足够大时该坐标合法。§4.4 的完整公式给出
$$
\begin{aligned}
\sqrt L\,W_{d-1-t}(\xi^f_{p,q})_{k_p}
={}&\frac{\overline{t_r}^{-q}\theta}{\alpha_mW_t}\\
&+\sum_{n=t+1}^{2^m-d+t}
 \overline{u_{p,q,n}}W_{n-1-t}
 f_{(n-1-t)\bmod D}.
\end{aligned}
\tag{4.57}
$$
$n=1,\ldots,t$ 的项恰为零，来自 $t$ 的定义。
其余全部长卷积保留。

写
$$
X_{<m}(z)=\sum_{j<m}a_jQ_j(z),\qquad
V_m(z)=c_m+2a_mX_{<m}(z),\qquad
x_m=\frac{z^{2^m}}{d_m}.
$$
近共振平方的同位项已准确消去，所以
$$
\mathfrak t_p=\mathfrak t_m+Q_mV_m.
\tag{4.58}
$$
由于 (4.57) 只读取次数至 $2^m-d+t<2^m$，
最高新行在逆系数中至多出现一次。准确地，
$$
u_{p,q,n}=u_{m,q,n}
 +\frac1{d_m}e_{m,h}
 \quad\text{当 }n=2^m-r+h,
\qquad
e_{m,h}=2q[z^h]\bigl(V_mg_m^{-q-1}\bigr),
\tag{4.59}
$$
这里仅须 $0\le h\le r-d+t$；若 $r-d+t<0$，修正和为空。
在其余读取次数上 $u_{p,q,n}=u_{m,q,n}$。
式 (4.59) 是形式幂级数的准确截断，不是算子范数近似。

所需 $h$ 均不超过 $r-1$。这些有限阶低头 jet 最终稳定，
故固定 $q$ 下
$$
|e_{m,h}|\le C_{q,r}(|a_m|+|c_m|)\longrightarrow0.
\tag{4.60}
$$
在 (4.57) 的修正项中使用
$$
W_{2^m-1-(r+t-h)}
 =\frac{d_m}{\alpha_mW_{r+t-h}}
$$
得到准确恒等式
$$
\begin{aligned}
\sqrt L\,W_{d-1-t}(\xi^f_{p,q})_{k_p}
={}&\frac1{\alpha_m}
\left[
 \frac{\overline{t_r}^{-q}\theta}{W_t}
 +\sum_{h=0}^{r-d+t}
 \overline{e_{m,h}}\,
 \frac{f_{(D-1-t-r+h)\bmod D}}{W_{r+t-h}}
\right]+\mathcal E_m.
\end{aligned}
\tag{4.61}
$$
其中 $\mathcal E_m$ 是把全部 $u_{p,q,n}$ 换成低行
$u_{m,q,n}$ 后的完整 $n>t$ 和。

沿 §3 的低行圆 $|z|=\exp(-400\,8^{m-1})$，
$g_m/t_r$ 一致接近 $1$；系数 Cauchy 估计与 $W_j\le1$ 给出
$$
|\mathcal E_m|
 \le \exp\bigl(50\,16^m+O(2^m)\bigr).
\tag{4.62}
$$
固定 $q,f$ 的常数已吸入右侧。
(4.61) 的方括号趋于非零数 $\overline{t_r}^{-q}\theta/W_t$，
而
$$
\log\alpha_m^{-1}=\frac{280}{3}16^m+O(8^m).
$$
因此 (4.61) 的主项不能被完整余和抵消。
这给 (4.52) 的下界；§4.4 对任意固定 $f$ 的锐上界给相反方向。

#### 4.5.2 反向目标多项式与共轭位置

下文设 $t\ge d$。定义
$$
F_\ell(z)=\sum_{i=0}^{D-1}
 \frac{f_{D-1-i}}{W_i}z^i,\qquad
B_p^f(z)=\sum_{i=0}^{2^p-1}
 \frac{f_{(D-1-i)\bmod D}}{W_i}z^i.
$$
由二进位乘积权准确分解，
$$
B_p^f(z)=F_\ell(z)\prod_{j=\ell}^{p-1}
 \left(1+\frac{z^{2^j}}{d_j}\right),\qquad
F_\ell(z)=\frac{\theta}{W_t}z^t+O(z^{t+1}).
\tag{4.63}
$$
记 $\check{\mathfrak t}_p(z)=\overline{\mathfrak t_p(\bar z)}$，
即只共轭算子系数。目标取值 $f_s$ 不作共轭。

一般反向公式须先从 $B_p^f$ 删去次数 $<d$ 的项，
这正对应目标顶部 $d$ 个坐标被投影删去。
现在 $t\ge d$，这些项本来就全为零，所以完整 MP 公式等价于
$$
\sqrt L\,W_k(\xi^f_{p,q})_k
 =W_{L-1}[z^{L-1-k}]
   \left(\check{\mathfrak t}_p(z)^{-q}B_p^f(z)\right).
\tag{4.64}
$$
此式是 Laurent 系数提取。$k$ 取 (4.54) 的固定值。

#### 4.5.3 最高有限多位展开与严格截断

令
$$
h=K-1,\qquad n=p-h,\qquad H=2^h,\qquad L=H2^n.
$$
$n\to\infty$，但 $h,H,q,k,t$ 都固定。对最高 $h$ 位引入独立形式变量
$$
x_i=\frac{z^{2^{n+i}}}{d_{n+i}},\qquad 0\le i<h.
$$
设
$$
A(z)=\check{\mathfrak t}_n(z)
 =z^r(\overline{t_r}+O(z)),\qquad
Y(z)=\sum_{j<n}\overline{a_j}Q_j(z).
$$
则准确的多变量表达为
$$
\begin{aligned}
\check{\mathfrak t}_p
={}&A+
 \sum_{i<h}(\overline{c_{n+i}}+2\overline{a_{n+i}}Y)Q(x_i)\\
&+2\sum_{i<j<h}\overline{a_{n+i}a_{n+j}}Q(x_i)Q(x_j),
\qquad Q(x)=-\frac{2x}{1+x}.
\end{aligned}
\tag{4.65}
$$
将
$$
\left(\text{(4.65) 右侧}\right)^{-q}
 \prod_{i<h}(1+x_i)
 =\sum_{\nu\in\mathbb N_0^h}R_{\nu,n}(z)x^\nu
\tag{4.66}
$$
作形式展开。对 $v=|\nu|$，
$$
\operatorname{ord}_zR_{\nu,n}\ge-r(q+v).
\tag{4.67}
$$
因为产生 $x^\nu$ 至多使用 $v$ 个扰动因子，而 $Y(0)=0$。
达到这个最大极阶的项只能逐次使用线性的
$-2\overline{c_{n+i}}x_i$；交叉二次项、Cayley 高次项、
$\prod(1+x_i)$ 的非恒等项及 $Y$ 项都会降低该极阶。
因此准确首 Laurent 项是
$$
R_{\nu,n}(z)=
 \frac{(q)_v\,2^v\prod_{i<h}\overline{c_{n+i}}^{\,\nu_i}}
      {\prod_{i<h}\nu_i!}\,
 \overline{t_r}^{-q-v}z^{-r(q+v)}
 +O\!\left(z^{-r(q+v)+1}\right),
\tag{4.68}
$$
其中 $(q)_v=q(q+1)\cdots(q+v-1)$，$(q)_0=1$。
若所示系数为零，(4.68) 仍以极阶上界理解。

记
$$
s_\nu=\sum_{i<h}\nu_i2^i,\qquad S_\nu=2^ns_\nu.
$$
把 (4.66) 代回 (4.64)，每项准确为
$$
W_{L-1}\prod_{i<h}d_{n+i}^{-\nu_i}
 [z^{L-1-k-S_\nu}]\bigl(B_n^f(z)R_{\nu,n}(z)\bigr).
\tag{4.69}
$$

这里没有遗漏任意高的 $\nu$。由 (4.67)，该项总次数至少为
$$
S_\nu+t-r(q+|\nu|)
 \ge (2^n-r)|\nu|+t-rq.
$$
当 $2^n>r(H+1-K)$ 时，$|\nu|\ge H+1$ 的这个下界严格大于 $L-1-k$。这里已用 $t+k+1=r(q+K)$；该条件最终成立。
剩下 $|\nu|\le H$；若 $s_\nu\ge H+1$，又有
$$
S_\nu+t-r(q+|\nu|)
 \ge (H+1)2^n+t-r(q+H)>L-1-k.
$$
所以只有固定有限集合
$$
|\nu|\le H,\qquad s_\nu\le H
\tag{4.70}
$$
可以贡献。特别地，$S_\nu>L$ 的项全部严格为零。

若 $s_\nu=H$ 且 $|\nu|<K$，则
$$
\operatorname{ord}(B_n^fR_{\nu,n})
 \ge t-r(q+|\nu|)>-1-k,
$$
因为 $t+k+1=r(q+K)$。这些项也准确为零。

#### 4.5.4 总高位次数不足 $L$ 的全部长卷积

使用 §4.2 在低头长度 $n$ 上的锐圆
$$
\rho_n=e^{-\lambda_n},\qquad
\lambda_n=(100+2^{-n/2})8^{n-1}.
$$
已有的逐段圆估计给出
$$
|A(z)|\ge\frac{|t_r|}{2}|z|^r,\qquad
|B_n^f(z)|\le C_f|z|^t
\quad (|z|=\rho_n).
$$
$Y$ 在这些圆上一致有界，所有高行系数也一致有界。
对 (4.70) 的固定有限集合，形式展开 (4.66) 因而给
$$
|R_{\nu,n}(z)|\le C\,\rho_n^{-r(q+|\nu|)}.
\tag{4.71}
$$
常数可以依赖 $q,f,K$，但不依赖 $n$。

设 $s=s_\nu<H$。对 (4.69) 作 Cauchy 估计，并代入准确权渐近，
其对数上界除以 $16^n$ 等于
$$
100\sum_{i<h}\nu_i16^i
 -\frac{20}{3}H^4+\frac{25}{2}(H-s)+o(1).
\tag{4.72}
$$
系数读取中的固定次数偏移只增加 $O(8^n)=o(16^n)$。

以下有限整数优化保留了每个长卷积系数的总费用。
在 $\sum\nu_i2^i=s<H$ 时，将两个相同低位合并到下一位，
只会增大 $\sum\nu_i16^i$。最终得到 $s$ 的二进位展开，所以
$$
\sum\nu_i16^i\le\sum_{i\in\operatorname{bits}(s)}16^i.
$$
函数
$$
s\longmapsto \sum_{i\in\operatorname{bits}(s)}16^i-\frac{s}{8}
$$
在整数 $0\le s<H$ 上严格递增：进位至第 $j$ 位时，增量为
$$
16^j-\sum_{i<j}16^i-\frac18
 =\frac{14}{15}16^j+\frac1{15}-\frac18>0.
$$
故 (4.72) 在 $s=H-1$ 取最大上界
$$
100\left(-\frac1{15}+\frac18\right)
 =\frac{35}{6}.
\tag{4.73}
$$
因此全部 $S_\nu<L$ 项之和至多为
$\exp((35/6+o(1))16^n)$。
这里没有只估计某一个逆系数或把复系数当作正项。

#### 4.5.5 $S_\nu=L$ 的唯一最大权分拆

剩下 $s_\nu=H$、$|\nu|\ge K=h+1$。
把 $\nu$ 看成把 $H=2^h$ 分拆为 $|\nu|$ 个二进位正数，
每个数至多 $H/2$。在这些分拆中，
$$
\nu^*_0=2,\qquad \nu^*_i=1\quad(1\le i<h)
\tag{4.74}
$$
唯一最大化 $\sum\nu_i16^i$。

给出一个有限维证明。将各分拆的部分从大到小排列，并补零到相同长度。
对 $1\le l\le h$，任意前 $l$ 部分的和严格小于 $H$，
且其二进位非零位数不超过 $l$，所以该和至多
$H-2^{h-l}$。(4.74) 的前 $l$ 部分准确达到这个上界。
对 $l\ge h+1$，(4.74) 的部分和已经是 $H$。
因此 (4.74) 的部分和支配每个其他分拆；
严格凸函数 $x^4$ 给出所需最大值和唯一性。
这也可直接从
$\sum x_i^4=12\int_0^\infty t^2\sum_i(x_i-t)_+\,dt$
与上述部分和不等式得到。

准确最大值为
$$
\sum_i\nu_i^*16^i
 =2+\sum_{i=1}^{h-1}16^i
 =\frac{H^4+14}{15}.
\tag{4.75}
$$
其他分拆的这个整数值至少小 $1$。

$s_\nu=H$ 时读取的是固定 Laurent 次数 $-1-k$。
所需低头 jet 阶数固定；随着 $n$ 增长，这些 jet 最终稳定。
高行的 $a_j,c_j$ 有界，因此所有这些系数一致有界。
结合 (4.75)，除 $\nu^*$ 外的项至多为
$$
\exp\left(\left(\frac{280}{3}-100+o(1)\right)16^n\right)
 =\exp\left(\left(-\frac{20}{3}+o(1)\right)16^n\right).
\tag{4.76}
$$

对 $\nu^*$，其总次数恰为 $K$，
而 $t+k+1=r(q+K)$，所以 (4.68) 只读取准确首 Laurent 系数。
二进位乘积权又给
$$
\frac{W_{2^p-1}}
     {d_n^2\prod_{j=n+1}^{p-1}d_j}
 =\frac{W_{2^n-1}}{d_n}
 =\frac1{\alpha_n}.
\tag{4.77}
$$
于是得到包括全部其余卷积的准确主项分离：
$$
\begin{aligned}
\sqrt L\,W_k(\xi^f_{p,q})_k
={}&
 \frac{
  2^{K-1}(q)_K\,\theta\,
  \overline{c_n}^{\,2}
  \prod_{j=n+1}^{p-1}\overline{c_j}
 }{
  W_t\,\overline{t_r}^{\,q+K}\,\alpha_n
 }
 +\mathcal R_p,\\
|\mathcal R_p|
\le{}&\exp\left(\left(\frac{35}{6}+o(1)\right)16^n\right).
\end{aligned}
\tag{4.78}
$$
$n=p-K+1$。这里的 $o(1)$ 只在固定 $q,f$ 下取 $p\to\infty$。
主项只共轭 $c_j,t_r$，不共轭目标值 $\theta$。

条件 (4.53) 使有限个 $c_j$ 因子的对数损失为 $o(16^n)$。
又
$$
\log\alpha_n^{-1}=\frac{280}{3}16^n+O(8^n),
$$
所以 (4.78) 的主项严格压过全部余项，给出 (4.55)–(4.56)。

#### 4.5.6 本节关闭的预算与仍须保留的容错问题

原指数行中，每个固定 $q$ 的所选充分 HS 尾预算含
$e^{-C_qp^\alpha}$ 这一慢尺度。
(4.52) 或 (4.56) 表明，对每个固定非零有限柱目标，
精确 projected-target 最小原像仍有
$\exp(c_{q,f}16^p)$ 级费用，$c_{q,f}>0$。
因此该精确原像不能与前述固定幂数的充分 HS 预算相乘趋零。

这里比较的是此前选定的充分预算，未把它当成真实残量的下界。
本节也没有排除：

- $f_p$ 随 $p$ 改变并趋近某个固定循环向量；
- 以很小目标误差消去相关的高位主项；
- 双行、混合行或其他真见证专属的便宜原像。

特别地，§6 的 $A_p$ 容错校准仍说明：
精确原像的巨大费用不能自行推出 ridge 不可能。
下一步必须继续控制真实目标修正及其完整 Schur 残量。

#### 4.5.7 固定柱目标的全部允许幂数

以上结论还可与 §4.4 合并为对变化 $q$ 的统一下界。
固定同一个非零有限柱 $f$，令
$$
K_f=\left\lceil\frac{t+1}{r}\right\rceil,\qquad
c_f=\frac{35}{6}\,16^{\,2-\max\{2,K_f\}}>0.
\tag{4.79}
$$
保持 (4.53) 及其最终非零条件，则
$$
\liminf_{p\to\infty}\ 
\inf_{\substack{q\in\mathbb N\\1\le rq\le2^{p-1}}}
 \frac{\log\|\xi^f_{p,q}\|}{16^p}
 \ge c_f.
\tag{4.80}
$$

证明分三个准确范围。

当 $q\ge K_f+1$ 时，$rq>t+r$，所以 §4.4 的完整主项分离适用。
那里主项与余项共有 $|t_r|^{-q}$ 因子；
其余 $q$ 费用至多 $\exp(O(q))$。
在 $rq\le2^{p-1}$ 的整个范围，这些对数费用一致为 $o(16^p)$。
因此该范围统一给出 $35/6-o(1)$ 的下界。

当 $q=K_f$ 时，$t<rq$，由本节 §4.5.1 的固定有限 jet 证明得到
$35/6-o(1)$。

当 $1\le q<K_f$ 时，$t\ge rq$。
这是固定有限个 $q$；每个的 spine 都有相同的 $K=K_f$，
故 (4.56) 给出
$(35/6)16^{2-K_f}-o(1)$。
对有限个余量取最大即可一致化。
若 $K_f=1$，这个范围为空；若 $K_f=2$，所给常数仍为 $35/6$。
三段合并即 (4.80)。

原指数行使用的充分 HS 尾预算 $b_{p,q}$ 满足
$$
\log b_{p,q}\ge-\beta q p^\alpha-C_0q
$$
其中 $C_0\ge0$ 是固定常数。
由于 $q\le2^{p-1}/r$，
$$
q p^\alpha=o(16^p)
$$
在全部允许幂数上一致成立。
因此 (4.80) 还给
$$
\liminf_{p\to\infty}\ 
\inf_{\substack{q\in\mathbb N\\1\le rq\le2^{p-1}}}
 \frac{\log\bigl(b_{p,q}\|\xi^f_{p,q}\|\bigr)}{16^p}
 \ge c_f>0.
\tag{4.81}
$$
这排除任意允许幂数序列（包括有界、增长及不单调序列）
对同一固定有限柱目标所作的 exact projected-target 证书。

(4.81) 仍只是选定充分预算与该精确最小原像的比较，
不把充分预算升级成真实 HS 残量下界。
允许目标随 $p$ 改变并保留小误差的问题完全保留。


### 4.6 单层最高位掩膜：变化目标的完整原像上界

本节给出一个真正允许目标随 $p$ 改变的构造。
它把原像的四次型上界降低一个二进位层级，并同时给出趋零的目标误差。
它尚未支付原来的慢尾 HS 预算，也不把单层结论当成免费可迭代的估计。

保持 §4.5 的近共振二次行，令
$$
m=p-1,\qquad H=2^m,\qquad L=2H,\qquad d=rq,
$$
并假设
$$
d+r\le H.
\tag{4.82}
$$
$q$ 可以随 $p$ 变化。设 $\mathcal G_{p,q}$ 是 $(T_p^q)^*$ 的
Moore–Penrose 逆，包含目标投影 $P_{[0,L-d)}$。
在物理正交基中，它的完整矩阵为
$$
(\mathcal G_{p,q})_{k,v}
 =
 \begin{cases}
 \overline{u_{p,q,v-k+d}}\,W_v/W_k,
   &k\ge d,\ 0\le v\le L-d-1,\ v-k+d\ge0,\\
 0,&\text{其余情形}.
 \end{cases}
\tag{4.83}
$$
这里没有 $L^{-1/2}$ 因子；该因子属于真空向量的坐标。

令 $Q_{p,q}$ 是删去两个目标区间的正交坐标投影：
$$
[H-d,H),\qquad [L-d-r,L).
\tag{4.84}
$$
这些区间不交，长度分别为 $d$、$d+r$，且第二个区间包含原先必须删去的顶部 $d$ 个目标。
定义
$$
u_{p,q}=\mathcal G_{p,q}Q_{p,q}\Omega_p.
$$
则准确有
$$
(T_p^q)^*u_{p,q}=Q_{p,q}\Omega_p,\qquad
\|\Omega_p-(T_p^q)^*u_{p,q}\|
 =\sqrt{\frac{2d+r}{L}}.
\tag{4.85}
$$

用 §4.2 在低头 $m$ 上的记号
$$
\lambda_m=(100+2^{-m/2})8^{m-1},\qquad
\mathcal F_m(j)=\lambda_mj+\log W_j\quad(0\le j<H).
$$
存在与 $p,q$ 无关的常数 $C<\infty$、$\gamma\ge1$，使充分大 $p$ 下
$$
\boxed{
\|\mathcal G_{p,q}Q_{p,q}\|
 \le C(1+q)\gamma^{q+1}L
 \exp\!\left(\mathcal F_m(H-1)+(d+r)\lambda_m\right).
}
\tag{4.86}
$$
若 $d=o(H)$，则 (4.85) 的目标误差趋零，同时
$$
\limsup_{p\to\infty}
 \frac{\log\|u_{p,q}\|}{16^{p-1}}\le\frac{35}{6}.
\tag{4.87}
$$
这与同一固定柱目标的下界不矛盾：这里目标是准确的变化掩膜 $Q_{p,q}\Omega_p$。

#### 4.6.1 最高位展开中的全部项

记
$$
V_m(z)=c_m+2a_mX_{<m}(z),\qquad x=\frac{z^H}{d_m},
\qquad A(z)=\mathfrak t_m(z)=z^rg_m(z).
$$
由 (4.58)，
$$
\mathfrak t_p=\frac{A+x(A-2V_m)}{1+x}.
$$
因此
$$
g_p^{-q}
 =g_m^{-q}(1+x)^q
   \left(1+x\left(1-\frac{2V_m}{A}\right)\right)^{-q}.
\tag{4.88}
$$
将括号中 $x$ 的系数准确展开：
$$
[x^1]=\frac{2qV_m}{A},\qquad
[x^2]=-\frac{2qV_m}{A}
       +\frac{2q(q+1)V_m^2}{A^2}.
\tag{4.89}
$$
$x^j$ 系数的 $z$ 极阶至多为 $rj$，
所以 $x^j$ 的整个贡献次数至少为 $j(H-r)$。
由 (4.82)，当 $j\ge3$ 时这已不小于 $L-d$。
而 (4.83) 只读取 $n\le L-d-1$，故这些高次项全部准确为零。

$x^2$ 中的第一项起于次数 $L-r\ge L-d$，也不进入读取范围。
第二项起于 $L-2r$；当 $q\ge2$ 时，$d\ge2r$，所以仍被截去。
因此在所有需要的系数上，准确有
$$
\begin{aligned}
g_p^{-q}\equiv{}&
 g_m^{-q}
 +\frac{z^{H-r}}{d_m}\,\bigl(2qV_mg_m^{-q-1}\bigr)\\
&+\mathbf1_{\{q=1\}}\frac{4z^{L-2r}}{d_m^2}
 V_m^2g_m^{-3}
 \pmod {z^{L-d}}.
\end{aligned}
\tag{4.90}
$$
这保留了低头函数的完整 Taylor 级数，没有把任何长卷积换成有限 jet。

$q=1$ 的最后一项只能在 $n\ge L-2r$ 出现。
若其在 (4.83) 中非零，则
$$
v=n+k-d\ge L-2r
$$
因为 $k\ge d=r$。
它的全部目标坐标都落在 (4.84) 的第二个区间
$[L-2r,L)$，故乘上 $Q_{p,q}$ 后该项准确消失。

#### 4.6.2 四个高位矩阵块与掩膜的作用

写
$$
k=\alpha H+k_0,\qquad
v=\beta H+v_0,\qquad
\alpha,\beta\in\{0,1\},\quad 0\le k_0,v_0<H.
$$
准确权比是
$$
\frac{W_v}{W_k}
 =d_m^{\,\beta-\alpha}\frac{W_{v_0}}{W_{k_0}}.
\tag{4.91}
$$

先看 (4.90) 的基本项 $g_m^{-q}$。
其读取次数是
$$
n=(\beta-\alpha)H+v_0-k_0+d.
$$
若 $\beta-\alpha=-1$，非负次数要求
$v_0\ge H+k_0-d\ge H-d$。
此时目标在下半头，恰落在第一个删去区间。
所以剩下的基本项只有同半头块和
$\alpha=0,\beta=1$ 的上半目标至下半源块。

再看一次最高位项。令
$$
w_{m,q,j}=[z^j]\bigl(2qV_mg_m^{-q-1}\bigr).
$$
该项在 (4.83) 中读取的低次数为
$$
j=(\beta-\alpha-1)H+v_0-k_0+d+r,
\tag{4.92}
$$
并有额外因子 $d_m^{-1}$。

若 $\beta=\alpha=0$，有 $k_0=k\ge d$，
所以 $j\ge0$ 要求 $v_0\ge H-r$。
由于 $d\ge r$，这包含于第一个删去区间。

若 $\beta=\alpha=1$，则 $j\ge0$ 要求
$v_0\ge H-d-r$，即目标在 $[L-d-r,L)$，被第二个区间删去。

若 $\beta-\alpha=-1$，由 $d+r\le H$，
$$
j\le -2H+(H-1)+d+r\le-1,
$$
故根本没有这样的系数。

所以一次最高位项唯一剩下的矩阵块是
$\alpha=0,\beta=1$。在这个块中，(4.91) 的 $d_m$
与展开中的 $d_m^{-1}$ 准确抵消。
以上检查覆盖四个块；没有留下未经支付的逆 carry 因子。

#### 4.6.3 一次统一 Cauchy 估计

沿 §4.2 的低头圆 $|z|=e^{-\lambda_m}$，
$$
|g_m(z)|\ge |t_r|/2,\qquad |V_m(z)|\le C_V
$$
最终一致成立，$C_V$ 与 $p,q$ 无关。
取 $\gamma=\max\{1,2/|t_r|\}$，则完整 Taylor 系数满足
$$
|u_{m,q,n}|\le \gamma^q e^{\lambda_mn},
\qquad
|w_{m,q,j}|\le2qC_V\gamma^{q+1}e^{\lambda_mj}.
\tag{4.93}
$$
这些是对全部所读次数的同一 Cauchy 界。

令 $\Lambda_m=-\log d_m$。§4.2 的准确二进位权给出
$$
0\le\mathcal F_m(k_0)\le\mathcal F_m(H-1),
$$
且
$$
H\lambda_m-\Lambda_m
 =-\frac{175}{2}16^m+o(16^m)<0.
\tag{4.94}
$$

对基本项，代入 (4.91)、(4.93) 后的指数为
$$
\mathcal F_m(v_0)-\mathcal F_m(k_0)+d\lambda_m
 +(\beta-\alpha)(H\lambda_m-\Lambda_m).
\tag{4.95}
$$
已经证明剩下只有 $\beta-\alpha=0$ 或 $1$。
由 (4.94)，全部基本项因而不超过
$$
\gamma^q
 \exp\bigl(\mathcal F_m(H-1)+d\lambda_m\bigr).
$$

对唯一剩下的一次最高位块，$\beta-\alpha=1$，
其完整指数正好是
$$
\mathcal F_m(v_0)-\mathcal F_m(k_0)+(d+r)\lambda_m.
$$
所以每个矩阵元均受
$$
2qC_V\gamma^{q+1}
 \exp\bigl(\mathcal F_m(H-1)+(d+r)\lambda_m\bigr)
$$
控制。加上基本项，用 $L\times L$ 矩阵的
$\|\cdot\|\le L\max_{k,v}|\cdot_{k,v}|$，得到 (4.86)。

最后，
$$
\mathcal F_m(H-1)=\left(\frac{35}{6}+o(1)\right)16^m.
$$
当 $d=o(H)$ 时，$(d+r)\lambda_m=o(16^m)$，
且 $\log((1+q)\gamma^{q+1}L)=o(16^m)$。
这证明 (4.87)。

#### 4.6.4 实际低头提升与剩余费用

设 $\widehat T_p$ 是此前的实际低头算子，满足
$$
\|\widehat T_p-T_p\otimes I\|\le C\eta_{p-1}.
$$
仍取 $d=o(H)$，用同一实际算子范数上界 $M_0$ 和幂次望远镜，
$$
\begin{aligned}
&\|\Omega-(\widehat T_p^q)^*(u_{p,q}\otimes\Omega_{\ge p})\|\\
&\qquad\le
 \sqrt{\frac{2d+r}{L}}
 +qM_0^{q-1}C\eta_{p-1}\|u_{p,q}\|.
\end{aligned}
\tag{4.96}
$$
第二项已经支付，因为它的对数至多为
$$
-\left(\frac{175}{2}-\frac{35}{96}+o(1)\right)L^4.
\tag{4.97}
$$
这里仍只提升到准确的实际低头 $\widehat T_p$。
完整 $T-\widehat T_p$ 的慢尾尚未支付，
也没有声称 (4.86) 可以直接乘上旧 HS 尾预算趋零。

若继续削去更多高位，必须重新控制全部低头分子
$V_m$、高位交叉项与目标掩膜的共同作用。
逐层重复同一个算子范数上界，或仅按被删坐标的比例估计 Schur 残量，
都不能替代这项完整证明。


### 4.7 全部高位一次展开的多层掩膜与真实 ridge 预算

本节不迭代 §4.6 的算子范数。
它把全部高位放入一次形式展开，在同一低头圆上支付所有系数，
并用目标端的周期掩膜排除未抵消的最大 carry。
以下上界不需要 $c_j$ 最终非零，也不需要 §4.5 的慢对数下界。

保持近共振实际二次行 (4.50)，$a,c\in\ell^1$，
稳定形式首项 $t_rz^r\ne0$。
选整数
$$
1\le n\le p,\qquad H=2^n,\qquad h=p-n,\qquad L=2^p,
\qquad q\ge1,\quad d=rq.
$$
设
$$
w=d+r(h+1)<H.
\tag{4.98}
$$
令 $Q_{n,p,q}$ 是如下正交坐标投影：在每个长度为 $H$ 的物理块中，
删去最后 $w$ 个目标坐标。准确地，
$$
Q_{n,p,q}e_b
 =\mathbf1_{\{b\bmod H<H-w\}}e_b.
$$
全局顶部 $d$ 个目标已包含在被删坐标内。

令
$$
u_{n,p,q}=\mathcal G_{p,q}Q_{n,p,q}\Omega_p.
$$
则
$$
(T_p^q)^*u_{n,p,q}=Q_{n,p,q}\Omega_p,\qquad
\|\Omega_p-(T_p^q)^*u_{n,p,q}\|
 =\sqrt{\frac wH}.
\tag{4.99}
$$

存在只依赖固定行和 $r,t_r$ 的常数 $C\ge1$，使全部充分大的 $n$、
全部满足 (4.98) 的 $p,q$ 一致有
$$
\boxed{
\|\mathcal G_{p,q}Q_{n,p,q}\|
 \le C^{q+h}L(L+1)
 \exp\!\left(
  \mathcal F_n(H-1)+(d+rh)\lambda_n
 \right).
}
\tag{4.100}
$$
这里
$$
\lambda_n=(100+2^{-n/2})8^{n-1},\qquad
\mathcal F_n(j)=\lambda_nj+\log W_j,\quad 0\le j<H.
$$
因此若
$$
n\longrightarrow\infty,\qquad q+h=o(H),
\tag{4.101}
$$
则目标误差趋零，并且
$$
\limsup
 \frac{\log\|u_{n,p,q}\|}{16^n}\le\frac{35}{6}.
\tag{4.102}
$$
所有高位个数 $h$ 都可以增长。没有把固定 $h$ 的余量当成统一余量。

#### 4.7.1 高位系数的按次数统一主控

在低头圆 $|z|=\rho_n=e^{-\lambda_n}$ 上，
$$
A(z)=\mathfrak t_n(z)=z^rg_n(z),\qquad
|g_n(z)|\ge |t_r|/2,\qquad |X_{<n}(z)|\le C_X.
$$
对 $0\le i<h$ 引入独立变量
$$
x_i=\frac{z^{H2^i}}{d_{n+i}}.
$$
与 (4.65) 相同，但暂不共轭系数，写
$$
\begin{aligned}
\mathfrak t_p
={}&A+
 \sum_{i<h}(c_{n+i}+2a_{n+i}X_{<n})Q(x_i)\\
&+2\sum_{i<j<h}a_{n+i}a_{n+j}Q(x_i)Q(x_j).
\end{aligned}
\tag{4.103}
$$
令
$$
z^d\left(\text{(4.103) 右侧}\right)^{-q}
 =\sum_{\nu\in\mathbb N_0^h}U_{\nu,n,q}(z)x^\nu.
\tag{4.104}
$$
对 $v=|\nu|$，每项的 Laurent 极阶至多为 $rv$：
$$
\operatorname{ord}_zU_{\nu,n,q}\ge-rv.
\tag{4.105}
$$
这里 $z^d$ 已准确抵消基本逆的 $rq$ 阶极点。

需要的不是随 $h$ 增长的逐项粗常数。
以下给出按总次数的统一正主控。
把 $Q(x)=-2x/(1+x)$ 的系数取绝对值，
再用 $\sum|a_j|,\sum|c_j|<\infty$ 与圆上的 $C_X$，
高位扰动的全部绝对系数在共同形式半径 $t$ 上的和不超过
$$
B_0\frac{t}{(1-t)^2},
\tag{4.106}
$$
其中 $B_0$ 不依赖 $n,h,q$。
设 $\gamma=\max\{1,2/|t_r|\}$，选一个固定
$0<\delta<1/2$，使
$$
\gamma B_0\frac{\delta}{(1-\delta)^2}\le\frac12.
$$
在形式半径 $t=\delta\rho_n^r$ 上，
二项式逆展开的绝对系数主控至多为
$$
\gamma^q\left(
 1-\gamma\rho_n^{-r}B_0\frac{t}{(1-t)^2}
 \right)^{-q}\le(2\gamma)^q.
$$
这是 $z^d$ 已乘入后的估计。

因此可以对所有 $\nu$ 选取非负数 $M_\nu$，在整个低头圆上一致满足
$$
|U_{\nu,n,q}(z)|\le M_\nu,\qquad
\sum_{|\nu|=v}M_\nu
 \le C^{q+v}\rho_n^{-rv},
\tag{4.107}
$$
其中固定 $C\ge\max\{1,2\gamma,\delta^{-1}\}$。
这个主控来自逐系数的非负多变量级数；
没有交换未经控制的“上确界”和无限求和。
Cauchy 估计于是给
$$
\bigl|[z^j]U_{\nu,n,q}(z)\bigr|
 \le M_\nu e^{\lambda_nj}
\tag{4.108}
$$
，包括合法的负 Laurent 次数 $j$。

#### 4.7.2 必要次数条件与准确高位费用

考虑 (4.83) 中一个未被掩膜删去的目标坐标 $b$ 与源坐标 $k$。
因此
$$
k\ge d,\qquad b\bmod H\le H-w-1.
$$
记
$$
N=b-k+d,\qquad
S_\nu=H\sum_{i<h}\nu_i2^i,\qquad v=|\nu|.
$$
若 $N<0$，该矩阵元为零；否则 $u_{p,q,N}$ 的 $\nu$ 项是
$$
\prod_{i<h}d_{n+i}^{-\nu_i}
 [z^{N-S_\nu}]U_{\nu,n,q}(z).
\tag{4.109}
$$
由 (4.105)，一个非零项必须满足
$$
k+S_\nu-rv\le b+d.
\tag{4.110}
$$
又 $S_\nu\ge Hv$，所以
$$
(H-r)v\le N<L.
\tag{4.111}
$$
由于 (4.98) 保证 $H>2r$，全部所需总次数 $v$ 少于 $L+1$。
多变量项本身可能很多，但 (4.107) 已经控制同一次数上的总和。

写
$$
k=Hk_{\rm hi}+k_0,\qquad
b=Hb_{\rm hi}+b_0,\qquad 0\le k_0,b_0<H.
$$
令 $\kappa_i,\beta_i\in\{0,1\}$ 分别为
$k_{\rm hi},b_{\rm hi}$ 的二进位位。
定义
$$
J_i=-\log d_{n+i}-\lambda_nH2^i,\qquad
B=r\lambda_n+\log C,\qquad
\mu_i=J_i+B.
\tag{4.112}
$$
把 (4.108) 的低圆费用、精确权比及 $C^v$ 合并，
其指数恰为
$$
\mathcal F_n(b_0)-\mathcal F_n(k_0)+d\lambda_n
 +\sum_{i<h}(\nu_i+\kappa_i-\beta_i)J_i+Bv.
\tag{4.113}
$$
以下控制最后两个高位项，不逐层乘任何逆范数。

#### 4.7.3 统一的权比界

充分大的 $n$ 下，对所有 $i\ge0$ 一致有
$$
77\,16^n16^i\le J_i\le110\,16^n16^i,\qquad
0\le B\le16^n,\qquad
\mu_i\le111\,16^n16^i.
\tag{4.114}
$$
确实，准确权公式给
$90\,16^j\le-\log d_j\le110\,16^j$ 对全部充分大的 $j$ 成立；
而 $\lambda_nH\le13\,16^n$，
$2^i\le16^i$，且 $B=O_r(8^n)+O(1)=o(16^n)$。

置
$$
\vartheta_i=\frac{\mu_i}{H2^i-r}.
$$
由 $H>2r$ 与 (4.114)，
$$
\frac{\vartheta_{i+1}}{\vartheta_i}
 \ge\frac{16\cdot77}{111}\,
       \frac{H2^i-r}{2H2^i-r}
 \ge\frac{1232}{333}>1.
\tag{4.115}
$$
特别，$\vartheta_i$ 严格递增。对 $j\ge1$ 还有
$$
H2^{j+1}\vartheta_{j-1}
 \le8\mu_{j-1}
 \le\frac{111}{2}16^n16^j
 <J_j.
\tag{4.116}
$$
这些粗数常数只用于保证统一的严格间隔。

#### 4.7.4 最大未抵消高位的完整排除

记
$$
e_i=\nu_i+\kappa_i-\beta_i.
$$
若全部 $e_i=0$，则 $\nu_i=\beta_i-\kappa_i\in\{0,1\}$，
所以 $v\le h$，直接有
$$
\sum_i e_iJ_i+Bv\le Bh.
$$

否则取最大的 $j$ 使 $e_j\ne0$。
对 $i>j$，有 $\nu_i+\kappa_i=\beta_i\le1$，从而
$$
\nu_{>j}:=\sum_{i>j}\nu_i\le h-1-j.
\tag{4.117}
$$
在 (4.110) 中准确消去这些高位的普通二进位质量，
只留下右侧额外的 $r\nu_{>j}$。

先证 $e_j$ 不可能为正。

若 $\beta_j=0$，则 $\nu_j+\kappa_j\ge1$。
左侧第 $j$ 位的最小有效质量至少是 $H2^j-r$；
所有更低位的有效质量与 $k_0$ 非负。
右侧用 $b_0\le H-w-1$、$\beta_{<j}$ 的最大值及 (4.117)，至多为
$$
H2^j-w-1+d+r(h-1-j)
 =H2^j-r(j+2)-1,
$$
严格小于 $H2^j-r$，矛盾。

若 $\beta_j=1$，则 $\nu_j+\kappa_j\ge2$。
左侧最小有效质量至少为 $2H2^j-2r$；
右侧至多为
$$
H2^{j+1}-w-1+d+r(h-1-j)
 =H2^{j+1}-r(j+2)-1
 <2H2^j-2r,
$$
仍矛盾。

因此最高非零差只能是 $e_j=-1$，
并且必有
$$
\beta_j=1,\qquad \nu_j=\kappa_j=0.
\tag{4.118}
$$
此时 (4.110) 给全部更低位的有效质量
$$
\mathcal M_{<j}
 =\sum_{i<j}\nu_i(H2^i-r)+\sum_{i<j}\kappa_iH2^i
 <H2^{j+1}.
\tag{4.119}
$$
其中只丢弃了非负的 $k_0$；同一掩膜和 (4.117) 保证严格不等式。

忽略低位目标带来的负项，并把低位的 $B\nu_i$ 并入 $\mu_i$。
若 $j\ge1$，由 (4.115)–(4.116)，
$$
\begin{aligned}
\sum_i e_iJ_i+Bv
&\le B\nu_{>j}-J_j+
 \sum_{i<j}\nu_i\mu_i+\sum_{i<j}\kappa_iJ_i\\
&\le Bh-J_j+\vartheta_{j-1}\mathcal M_{<j}\\
&<Bh.
\end{aligned}
\tag{4.120}
$$
这里源位的比值
$J_i/(H2^i)$ 也不超过 $\vartheta_i$。
若 $j=0$，没有低位，(4.120) 直接由 $-J_0<0$ 得到。

所以对每一个真实可能贡献的多变量项，统一成立
$$
\boxed{\sum_i e_iJ_i+Bv\le Bh.}
\tag{4.121}
$$
它同时覆盖任意多的同位重复、全部高位交叉分子，
以及所有高位之间的二进位 carry。

#### 4.7.5 完整算子上界与实际提升

把 (4.121) 代入 (4.113)，并用
$0\le\mathcal F_n(k_0)\le\mathcal F_n(H-1)$。
对固定 $v$，置
$$
p_\nu=\frac{M_\nu}{C^{q+v}\rho_n^{-rv}},
\qquad \sum_{|\nu|=v}p_\nu\le1.
$$
每一项的上述指数估计仍乘有 $p_\nu$，所以可以先用 (4.121)，再对 $p_\nu$ 求和。
按总次数 $v$ 分组，(4.107) 表明每一组最多贡献
$$
C^q
 \exp\!\left(\mathcal F_n(H-1)+d\lambda_n+Bh\right).
$$
由 (4.111)，总次数组少于 $L+1$。
所以每个完整矩阵元不超过上述数乘 $L+1$。
再用 $\|\cdot\|\le L\max|\cdot_{k,b}|$，得到 (4.100)。

由 (4.101)，$w/H\to0$，
$(d+rh)\lambda_n=o(16^n)$，
并且 $p=n+h=o(H)$、$q+h=o(H)$。
故 $C^{q+h}L(L+1)$ 的对数也是 $o(16^n)$。
结合 $\mathcal F_n(H-1)=(35/6+o(1))16^n$，得到 (4.102)。

实际低头比较仍是此前已经支付的
$$
\|\widehat T_p-T_p\otimes I\|\le C_1\eta_{p-1}.
$$
对 $u=u_{n,p,q}\otimes\Omega_{\ge p}$，
同一幂次望远镜给
$$
\|\Omega-(\widehat T_p^q)^*u\|
 \le\sqrt{w/H}+qM_0^{q-1}C_1\eta_{p-1}\|u_{n,p,q}\|.
\tag{4.122}
$$
在 (4.101) 下，第二项为 $\exp(-c16^p)$ 级小量，
可取任意固定 $c<245/3$ 并让参数充分大。
这是因为 $n\le p$，源型至多为 $(35/6+o(1))16^p$，
而真实 carry 的负主型为 $(175/2)16^p$。
这里没有把 $T_p$ 当成实际交换子。

#### 4.7.6 慢尾预算的一个准确可付范围

以下是由本节构造直接得到的充分条件。
$\alpha>3$ 的核零和循环范围已经由
[既有快类范围核查](R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)
覆盖；这里新增的是明确的实际多层容错原像，不重新计为核范围扩展。

设同一实际行另满足尾范数界
$$
\|T-\widehat T_p\|\le C_2e^{-\beta p^\alpha},
\qquad \alpha>3,\quad\beta>0,
\tag{4.123}
$$
且 $T$ 与 $\widehat T_p$ 互相交换。
原 $a_j=e^{-\beta_0j^\alpha}$、
$c_j=e^{-\kappa\beta_0j^\alpha}$ 的迟首行在 $\kappa>1$ 时具有这种界，
允许把 $\beta$ 略缩小以吸收固定常数。

取
$$
q=p,\qquad
n=\left\lceil(1+\varepsilon)\log_2p\right\rceil,
\qquad
0<\varepsilon<\frac{\alpha-3}{4}.
\tag{4.124}
$$
则 $H\asymp p^{1+\varepsilon}$、$h=p-n$，
所以 (4.101) 成立，且
$$
\log\|u_{n,p,q}\|=O(p^{4+4\varepsilon})
 =o(p^{\alpha+1}).
\tag{4.125}
$$

若 $z\in\ker T$，令 $R_p=T-\widehat T_p$。
因全程是实际交换算子，
$$
\widehat T_p^qz=(-R_p)^qz.
$$
于是
$$
\|(T_p^q\otimes I)z\|
 \le\left[
 (C_2e^{-\beta p^\alpha})^q+
 qM_0^{q-1}C_1\eta_{p-1}
 \right]\|z\|.
\tag{4.126}
$$
(4.124)–(4.125) 使方括号与 $\|u_{n,p,q}\|$ 的乘积趋零。
结合准确的 (4.99)，得到
$$
|\langle z,\Omega\rangle|
 \le\|z\|\sqrt{w/H}
 +\|(T_p^q\otimes I)z\|\,
  \|u_{n,p,q}\|
 \longrightarrow0.
$$
所以 $\ker T\perp\Omega$。
$\ker T$ 对真实 $A'$ 不变，而 R88 已付 $\Omega$ 的 $A'^*$ 循环性，
故 $\ker T=\{0\}$。再由实际 $C$ 对称性，$T$ 的像稠密；
所有正整数幂也单射且像稠密。

这个证明没有使用纯模型的核零结论，
也没有从核残量小推断距核小。

#### 4.7.7 临界参数处仍缺什么

本构造给出真实的变化目标上界。在强目标误差趋零的条件 (4.101) 下，
当前估计的直接配平阈值仍为 $3$；下一节改用固定比例的 WOT 目标。
在 (4.101) 下，总有
$$
p=o(H),\qquad q=o(H).
$$
若 $\alpha\le3$，则
$$
\frac{qp^\alpha}{H^4}
 =\frac qH\left(\frac pH\right)^3p^{\alpha-3}
 \longrightarrow0.
\tag{4.127}
$$
因此把 (4.100) 的 $H^4$ 级上界直接代入
$e^{-\beta qp^\alpha}$ 的慢尾预算，不能得到所需的趋零乘积。

(4.127) 只说明这个已经证明的上界还不足以支付临界范围。
它不是实际最小原像的下界，也不排除更好的目标改动、
非坐标的正交投影、正密度专属修正或不同的完整 Schur 证书。


#### 4.7.8 固定比例掩膜的 WOT 证书与三次边界

不必始终要求 $w/H\to0$。假设
$$
n\to\infty,\qquad
\frac{w}{H}\longrightarrow\theta,\qquad 0<\theta<1.
\tag{4.128}
$$
把 $Q_{n,p,q}$ 视为 $\mathcal H=L^2(\mathbb Z_2)$ 上的真实有限柱乘法投影。
则
$$
Q_{n,p,q}\xrightarrow{\mathrm{WOT}}(1-\theta)I.
\tag{4.129}
$$
这里只作环境空间中的目标投影，没有声称 $Q$ 属于 $A'$ 或保未知核。

给出准确验证。若 $f,g$ 都只依赖前 $\ell$ 位，
则它们的物理取值乘积按周期 $2^\ell$ 重复。
当 $n\ge\ell$ 时，每个 $H$ 块保留前 $H-w$ 个取值。
完整周期贡献 $(1-w/H)\langle f,g\rangle$，
末尾不完整周期的误差至多
$$
\frac{2^{\ell+1}}H\|f\|_\infty\|g\|_\infty.
$$
故有限柱对的配对收敛到所述标量。
$\|Q\|\le1$ 与有限柱稠密性把它延拓为全空间 WOT 收敛。
这里没有用变化的无界归一投影来替代 (4.129)。

设 $b_{p,q}$ 是真实核比较中已经支付的上界，即
$$
\|(T_p^q\otimes I)z\|\le b_{p,q}\|z\|
\quad(z\in\ker T).
$$
若沿所选子列有
$$
b_{p,q}\|\mathcal G_{p,q}Q_{n,p,q}\|\longrightarrow0,
\tag{4.130}
$$
则 $\ker T=\{0\}$。
确实，对任意固定有限柱 $f$，当 $p$ 足够大时，
$$
u_p^f=(\mathcal G_{p,q}Q_{n,p,q}f_p)\otimes\Omega_{\ge p}
$$
满足
$$
(T_p^q\otimes I)^*u_p^f=Q_{n,p,q}f,\qquad
\|u_p^f\|\le\|\mathcal G_{p,q}Q_{n,p,q}\|\|f\|.
$$
对真核向量 $z$，
$$
|\langle z,Q_{n,p,q}f\rangle|
 =|\langle(T_p^q\otimes I)z,u_p^f\rangle|
 \le b_{p,q}\|\mathcal G_{p,q}Q_{n,p,q}\|\|z\|\|f\|
 \longrightarrow0.
$$
由 (4.129)，$(1-\theta)\langle z,f\rangle=0$。
有限柱稠密给 $z=0$。这个论证甚至不需要把未知核先投影到加权域。

作为常数核验，考虑
$$
\|T-\widehat T_p\|\le C_2e^{-\beta p^3}.
$$
取固定 $a>0$、$0<\theta<1$，置
$$
C_*=\frac{r(a+1)}{\theta}.
$$
必须按二进位子列选参数：
$$
H_n=2^n,\qquad
p_n=\left\lfloor\frac{H_n}{C_*}\right\rfloor,\qquad
q_n=\lfloor ap_n\rfloor,\qquad h_n=p_n-n.
\tag{4.131}
$$
充分大 $n$ 后所有参数合法，并且
$$
\frac{H_n}{p_n}\to C_*,\qquad
\frac{q_n}{p_n}\to a,\qquad
\frac{w_n}{H_n}\to\theta.
$$
没有对全部整数 $p$ 声称一个不合法的二进位比值极限。

(4.100) 给出
$$
\limsup
\frac{\log\|\mathcal G_{p_n,q_n}Q_{n,p_n,q_n}\|}{p_n^4}
\le C_*^4\left(\frac{35}{6}+\frac{25}{2}\theta\right).
\tag{4.132}
$$
因为 $\lambda_n=(25/2+o(1))H_n^3$，
而 $(d+rh)/H_n\to\theta$；$C^{q+h}L(L+1)$ 只增加 $O(p_n)$。

真实慢尾幂的负主型为 $-\beta a p_n^4$；
实际低头 carry 为 $\exp(-c16^{p_n})$，远小于此尺度。
所以如下严格不等式足以支付 (4.130)：
$$
\beta a>
\frac{r^4(a+1)^4}{\theta^4}
\left(\frac{35}{6}+\frac{25}{2}\theta\right).
\tag{4.133}
$$
利用
$$
\min_{a>0}\frac{(a+1)^4}{a}=\frac{256}{27}
\quad\text{在 }a=\frac13\text{ 取到},
$$
并让固定的 $\theta<1$ 充分接近 $1$，
本构造得到的一个显式充分条件是
$$
\beta>\frac{14080}{81}r^4.
\tag{4.134}
$$
每次使用的 $\theta$ 都固定小于 $1$，
所以 WOT 极限始终是非零标量；没有使用 $\theta=1$ 的退化极限。

这一大常数三次范围已被前述既有快类结论的
$\beta>80r^4/3$ 单射与限制稠密范围覆盖；
$\beta>400r^4$ 对应的是更强的标准范数理想结论。
本节不声称改善这些原有充分范围或常数。
(4.129)–(4.130) 的内容是一个新的可复核目标机制：
源算子有完整上界，目标只需保留固定的非零 WOT 锚，
且全部实际比较仍保真核条件。


#### 4.7.9 有限可和局部行之固定多项式的同一上界

(4.100)、目标误差及固定比例 WOT 机制还适用于 §4.3 的有限行族
$$
R_\nu=\sum_j(a_{\nu j}N_j+b_{\nu j}Q_j+e_{\nu j}Q_j^2),
\qquad a_\nu,b_\nu,e_\nu\in\ell^1,
$$
以及固定多项式 $P$、$P(0)=0$、$T=P(R_1,\ldots,R_\ell)$。
仍明确要求实际形式首阶有限非零，为 $t_rz^r$。
这里不推广 §4.5 使用特定 $c_j$ 主项的下界。

确实，将高位写成独立 $x_i$ 后，每个高行的非负绝对系数主控在共同形式半径 $t<1$ 上至多为
$$
C_\nu\frac{t}{(1-t)^2},
$$
因为 $N$、$Q$、$Q^2$ 分别给 $x$、$-2x/(1+x)$、
$4x^2/(1+x)^2$，且每条系数行可和。
低行在 §4.3 已付的低头圆上一致有界。
展开固定有限次数 $P$，其高位扰动因而有
$$
B_1\frac{t}{(1-t)^{D_1}}
$$
的正主控，$D_1$ 和 $B_1$ 固定，不随高位数或截断变化。
取足够小的固定 $\delta$，使
$$
\gamma B_1\frac{\delta}{(1-\delta)^{D_1}}\le\frac12,
$$
并仍使用 $t=\delta\rho_n^r$，就得到相同的 (4.107)。

每个非恒等高位扰动至少含一个 $x_i$，故产生总次数 $v$ 时最多取 $v$ 个逆展开扰动因子，仍有
$\operatorname{ord}U_\nu\ge-rv$。之后的必要次数、周期掩膜、最高未抵消位、精确权比和按 $v$ 求和证明完全相同。
因此 (4.100) 的全部常数仍可取成与 $n,p,q,h$ 无关的固定数。

§4.3 的 actual 低头比较已给 $C\eta_{p-1}$，有限多项式的有序幂差只增加前述 $qM_0^{q-1}$。
若另有 (4.123) 或其三次版本的真实完整尾界，§§4.7.6、4.7.8 的充分预算也相应成立。
一般仅可和行不因此获得新的慢尾速率；此处只扩上界与 WOT 机制的对象范围。


### 4.8 固定二进位目标乘子与真实正常湮灭理想

本节把 §4.7 的向量原像连接到实际 $A'$ 中的有界理想输出。
不再要求正密度支撑于 $\ker T$。
全部费用仍显式保留，且已被旧定理覆盖的 $\alpha,\beta$ 范围不重新计为成果。

#### 4.8.1 已付的有限头乘法字典

记 $\mathcal H_p$ 为前 $p$ 位柱向量空间，尾部是真空。
对 $w\in\mathcal H_p$，已有实际与局部 Walsh 乘子
$$
X_w=\sum_{F\subset[0,p)}\widehat w_F V_F\in\mathcal A\subset A',
\qquad
X_w^{[p]}\in\mathcal A_p,
\qquad
X_w\Omega=X_w^{[p]}\Omega=w.
$$
沿用
[规范源完整幂预算 §1](../notes/2026-11-13-canonical-positive-sources-mixed-power-residuals-and-polynomial-budgets-normal-complex.md)
的准确界
$$
\|X_w\|,\|X_w^{[p]}\|\le K_p\|w\|,
\qquad K_p=10^{p/2},
$$
$$
\|X_w-X_w^{[p]}\|\le D_p\|w\|,
\qquad D_p\le6p\eta_{p-1}K_p.
\tag{4.135}
$$
局部代数 $\mathcal A_p$ 交换，$\Omega_p$ 对它循环，
全部局部乘子共同 $C_p$ 对称。
实际 $C$ 保持 $\mathcal H_p$，其限制正是 $C_p$，
且 $C\Omega=\Omega$、$C\chi_F=(-1)^{|F|}\chi_F$。

若 $B\in\mathcal A_p$ 满足 $B\Omega_p=0$，
则对每个 $R\in\mathcal A_p$ 有 $BR\Omega_p=RB\Omega_p=0$；
由循环性 $B=0$。因此有限头中的乘法恒等式可以在真空上核验。
这一步只用于同一个有限头交换代数，不把未知限制上的循环性免费代入。

#### 4.8.2 固定 dyadic 掩膜给实际统一有界的非零 WOT 锚

固定
$$
\theta=\frac{b}{2^s},\qquad 0<b<2^s,
\tag{4.136}
$$
其中 $s,b$ 不随 $p,n,q$ 改变。
对 $n\ge s$，令 $Q_n^\theta$ 在每个长度 $H=2^n$ 的物理块中，
删去最后 $\theta H$ 个坐标。
假设参数满足
$$
d+r(h+1)\le\theta H<H,\qquad h=p-n.
\tag{4.137}
$$
这个掩膜是 §4.7 掩膜的进一步子投影，
故原算子上界仍适用：
$$
\|\mathcal G_{p,q}Q_n^\theta\|
 \le C^{q+h}L(L+1)
 \exp\bigl(\mathcal F_n(H-1)+(d+rh)\lambda_n\bigr).
\tag{4.138}
$$

置
$$
v_n=Q_n^\theta\Omega,\qquad
\Theta_n=X_{Cv_n}\in\mathcal A.
\tag{4.139}
$$
$v_n$ 是取值为 $0,1$ 的真实柱函数，只依赖
$$
B_n=\{n-s,\ldots,n-1\}
$$
这固定数量的远处位；$Cv_n$ 仍只依赖这些位。
其平均值始终为 $1-\theta$。

由 Walsh 展开和 $\|V_F\|\le3^{|F|}$，
$$
\|\Theta_n\|
 \le10^{s/2}\|Cv_n\|
 \le10^{s/2}.
\tag{4.140}
$$
这是只依赖固定 $s$ 的统一界，不是 $K_p$ 级界。

还准确有
$$
\boxed{\Theta_n\xrightarrow{\mathrm{WOT}}(1-\theta)I.}
\tag{4.141}
$$
说明其实际性：对 $F\subset B_n$，把实际 $V_j$ 与纯单个位
$V_j^0$ 比较，已付 carry 界给
$$
\|V_F-V_F^0\|
 \le C_s\max_{j\in B_n}\eta_j\longrightarrow0.
$$
固定数量因子的乘积望远镜在这里费用统一。
若 $F\ne\varnothing$，则对任意两个固定有限柱 $x,y$，
当 $B_n$ 已在它们支撑之后时，
$$
\langle V_F^0x,y\rangle
 =\langle x,y\rangle
  \langle V_F^0\Omega,\Omega\rangle=0,
$$
因为 $V_F^0\Omega=\chi_F$，其均值为零。
统一范数界把该结论延拓到所有 $x,y$。
于是只有 Walsh 常数项存留，得到 (4.141)。

这个证明只用有限纯位乘积和实际范数比较；
没有假设无限相位酉或无限 Haar 旋转存在。
(4.139) 的 $X_{Cv_n}$ 是实际乘子，不是把坐标投影 $Q_n^\theta$
误当成 $A'$ 元素。

#### 4.8.3 有限头 adjoint 原像变成准确乘法恒等式

取
$$
u_p=\mathcal G_{p,q}Q_n^\theta\Omega_p,
\qquad
(T_p^q)^*u_p=v_n.
\tag{4.142}
$$
目标顶部 $d$ 个坐标已经由 (4.137) 删去。
局部 $C_p$ 对称性给
$$
T_p^q(C_pu_p)=C_pv_n.
$$
在同一 $\mathcal A_p$ 中比较真空像，并用 §4.8.1 的忠实性，得到
$$
\boxed{
T_p^qX_{Cu_p}^{[p]}=X_{Cv_n}^{[p]}.
}
\tag{4.143}
$$
这里右侧目标取 $Cv_n$ 而不是 $v_n$；
该 $C$ 的位置来自 adjoint 方程，不能省略。

令
$$
U_p=X_{Cu_p}\in\mathcal A,\qquad
\epsilon_p=\|\widehat T_p-T_p\otimes I\|,
\qquad
M\ge1,\ \|\widehat T_p\|,\|T_p\|\le M.
$$
由 (4.135)、幂次望远镜及 (4.143)，
$$
\widehat T_p^qU_p=\Theta_n+E_p,
\tag{4.144}
$$
其中
$$
\boxed{
\|E_p\|
 \le
 \bigl(M^qD_p+qM^{q-1}\epsilon_pK_p\bigr)\|u_p\|
 +D_p\|v_n\|.
}
\tag{4.145}
$$
展开顺序为
$$
\begin{aligned}
\widehat T_p^qU_p-\Theta_n
={}&
 \widehat T_p^q(U_p-X_{Cu_p}^{[p]})\\
&+(\widehat T_p^q-T_p^q)X_{Cu_p}^{[p]}\\
&+(X_{Cv_n}^{[p]}-\Theta_n).
\end{aligned}
$$
中间的有限头乘法差由 (4.143) 准确为零。
这里无需局部 $T_p$ 与实际 $\widehat T_p$ 交换。

#### 4.8.4 全实际的余项理想恒等式

设
$$
R_p=T-\widehat T_p,\qquad r_p=\|R_p\|.
$$
$T,\widehat T_p,R_p,U_p$ 都是真实交换的 $\mathcal A$ 元素。
因此
$$
\widehat T_p^q-(-R_p)^q
 =
T\sum_{j=0}^{q-1}\widehat T_p^{q-1-j}(-R_p)^j.
$$
定义实际有界右因子
$$
F_p=
\left(\sum_{j=0}^{q-1}
 \widehat T_p^{q-1-j}(-R_p)^j\right)U_p\in\mathcal A.
\tag{4.146}
$$
每个 $F_p$ 都有界，但不声称它们的范数统一。
由 (4.144)，
$$
TF_p=\Theta_n+E_p-(-R_p)^qU_p.
\tag{4.147}
$$
所以
$$
\boxed{
\|TF_p-\Theta_n\|\le
r_p^qK_p\|u_p\|
+\bigl(M^qD_p+qM^{q-1}\epsilon_pK_p\bigr)\|u_p\|
+D_p\|v_n\|.
}
\tag{4.148}
$$

若 (4.148) 的右侧趋零，则 $TF_p$ 一致有界，且
$$
TF_p\xrightarrow{\mathrm{WOT}}(1-\theta)I.
\tag{4.149}
$$
这是一个实际主理想内的有界输出序列。
没有使用非实际纯比较算子作为右因子，也没有把大的 $F_p$ 范数隐藏起来；
它已通过 $K_p\|u_p\|$ 进入每一项预算。

特别地，若固定正正常泛函 $\varphi$ 满足
$$
\varphi(TR)=0\qquad(R\in A'),\qquad \varphi(I)>0,
$$
一致有界的 WOT 收敛蕴含对每个 trace-class 泛函收敛：先以有限秩泛函逼近，再用统一输出界控制余项。因此由 (4.149) 与正规性得到
$$
0=\lim_p\varphi(TF_p)=(1-\theta)\varphi(I)>0,
$$
矛盾。这一步不要求 $T\rho^{1/2}=0$，
也不需要规范源的未定 trace-tail 衰减速度。

同样，任意正规泛函在 $A'$ 上的非零限制都不可能湮灭 $TA'$：
对固定 $R\in A'$ 使用 $TF_pR$，即可得到 $\varphi(R)=0$。

先除以非零实数 $1-\theta$，再在主理想中作有限凸组合，可把 (4.149) 变为强算子单位。
对有限向量组，输出向量组在直和 Hilbert 空间中弱收敛；
有限凸组合可使其范数收敛，再对可数稠密向量组对角化。
统一输出范数保证全空间强收敛。
本模型 $A'$ 的共同 $C$ 对称性同时给 adjoint 强收敛。
因此得到有界的 strong* 主理想单位；不声称它是收缩单位。

#### 4.8.5 与已付多层预算的准确衔接

令 $\mathcal U_{p,q}=\|\mathcal G_{p,q}Q_n^\theta\|$。
因为 $\|u_p\|\le\mathcal U_{p,q}$、$\|v_n\|\le1$，
完整充分条件是
$$
\boxed{
K_pr_p^q\mathcal U_{p,q}
+\bigl(M^qD_p+qM^{q-1}\epsilon_pK_p\bigr)
 \mathcal U_{p,q}
+D_p\longrightarrow0.
}
\tag{4.150}
$$
$K_p=e^{O(p)}$ 不可删去。
在 §4.7 的 $q=O(p)$、$\log\mathcal U_{p,q}=O(p^4)$ 参数中，
它不改变已付慢尾主指数；真实 carry
$\epsilon_p=O(\eta_{p-1})$、$D_p\le6p\eta_{p-1}K_p$
仍远小于这些费用。

固定 dyadic $\theta$ 可选在任意给定的严格余量内，
并使 (4.137) 最终成立。
因此 §4.7 中已被旧快类覆盖的超三次及大常数三次参数，
也由这一明确字典得到真实正常湮灭者的排除。
这些核范围、限制稠密范围与强主理想范围均不重新计数；
本节的用途是保留可供新证书使用的实际源输出与非零锚。

#### 4.8.6 两条或有限多条真实湮灭行的联合接口

上述字典不局限于单行 MP 逆。
设同一个固定正常泛函湮灭
$$
Z_\nu A'\qquad(1\le\nu\le m_0),
$$
其中 $Z_\nu,\widehat L_{\nu,p},R_{\nu,p}\in\mathcal A$ 全部为实际交换元，且
$$
Z_\nu=\widehat L_{\nu,p}+R_{\nu,p},
\qquad
r_{\nu,p}=\|R_{\nu,p}\|,
$$
并有同一有限头中的局部算子 $L_{\nu,p}\in\mathcal A_p$，
$$
\epsilon_{\nu,p}=
 \|\widehat L_{\nu,p}-L_{\nu,p}\|.
$$
取正整数 $q_\nu$。若找到同一目标 $v_n=Q_n^\theta\Omega$
的完整有限头 row 原像
$$
\boxed{
\sum_{\nu=1}^{m_0}(L_{\nu,p}^{q_\nu})^*u_{\nu,p}
 =v_n,
}
\tag{4.151}
$$
则 $C$ 对称与有限头忠实性准确给
$$
\sum_\nu L_{\nu,p}^{q_\nu}X_{Cu_{\nu,p}}^{[p]}
 =X_{Cv_n}^{[p]}.
\tag{4.152}
$$
每行按 (4.145) 提升，目标 lift 只付一次。
若 $\|\widehat L_{\nu,p}\|,\|L_{\nu,p}\|\le M_\nu$，则全部误差与尾项受
$$
\boxed{
\begin{aligned}
\Delta_p\le{}&
D_p\|v_n\|\\
&+\sum_{\nu=1}^{m_0}
\left[
 K_pr_{\nu,p}^{q_\nu}
 +M_\nu^{q_\nu}D_p
 +q_\nu M_\nu^{q_\nu-1}\epsilon_{\nu,p}K_p
\right]\|u_{\nu,p}\|.
\end{aligned}
}
\tag{4.153}
$$
各行使用真实差幂恒等式，得到某些实际有界 $F_{\nu,p}\in\mathcal A$ 满足
$$
\left\|
\sum_\nu Z_\nu F_{\nu,p}-\Theta_n
\right\|\le\Delta_p.
\tag{4.154}
$$
故 $\Delta_p\to0$ 将以同一个非零 WOT 锚排除该同一正常湮灭者。

(4.151) 的 row 原像必须在完整有限头内求解，
并付清实际范数或真实 Gram 最小值；
不能用先压缩后取逆、不同见证、不同目标或未经控制的 Schur 残量代替。
本节没有证明临界余族中这样的便宜联合原像已经存在。
它给出的正是下一步需要接上的实际接口。

### 4.9 固定 gauge 双行的完整单层最小源与慢费用接口

本节只处理一次行 $T_p,\gamma_\zeta(T_p)$。
结论是完整有限头联合 row 的一个准确 Schur 最小化公式，
以及利用相位分离的全目标原像上界。
它没有把这一层自动迭代成临界余族的可付证书，
也不将局部逆的费用误作整个源的费用。

#### 4.9.1 同一个见证与完整最高位分块

沿用原迟首二次行
$$
T=X^2-B_0+Y,\qquad
X=\sum_j a_jQ_j,\quad Y=\sum_jc_jQ_j,\quad
B_0=\sum_j a_j^2Q_j^2.
$$
设稳定形式首项为 $t_rz^r$，$t_r\ne0$。
固定一个 dyadic $\zeta$，要求
$$
\zeta^r\ne1.
\tag{4.155}
$$
在同一见证的构造中，这个附加要求合法：
[迟首二次核与共同正态稿 §4](R236-appendix-late-support-quadratic-kernels-and-positive-joint-first-annihilators.md)
的有限排除群 $G_*$ 可以预先再包含全部满足 $\zeta^r=1$ 的
dyadic 根，然后作同一次 Fourier 非零配对选择。
仍然只取一个 $\zeta$ 和一个 $\rho$。

对该见证，
$\gamma_\zeta(T)-T=2D_\zeta S_\zeta$，
所以同一个正常泛函同时湮灭 $TA'$ 与 $\gamma_\zeta(T)A'$。
没有合并不同 $\zeta$ 的密度。

令 $p=m+1$、$H=2^m$，并取 $m$ 足够大，使
$\zeta^H=1$、$H>2r$，低头首项已稳定。
按最高物理位把 $\mathcal H_p$ 写为
$\mathcal H_m\oplus\mathcal H_m$。
准确地，
$$
N_m^{[p]}=E=
\begin{pmatrix}0&0\\I&0\end{pmatrix},\qquad E^2=0.
\tag{4.156}
$$
低行标量芽记为
$$
x_m(z)=\sum_{j<m}a_jq_j(z),\quad
f_m(z)=x_m(z)^2-\sum_{j<m}a_j^2q_j(z)^2
       +\sum_{j<m}c_jq_j(z)
       =z^rg_m(z),
$$
其中 $g_m(0)=t_r$。
记
$$
T_0=f_m(A_m),\quad T_1=f_m(\zeta A_m),\quad
X_m=x_m(A_m),\quad X_{m,\zeta}=x_m(\zeta A_m).
$$
最高行是精确的一次 $E$ 项：
$$
T_p=f_m(A_p)+E\bigl(-4a_mx_m(A_p)-2c_mI\bigr).
\tag{4.157}
$$
因此存在实际完整低头矩阵 $L_0,L_1$，使
$$
T_p=\begin{pmatrix}T_0&0\\L_0&T_0\end{pmatrix},
\qquad
\gamma_\zeta(T_p)=
\begin{pmatrix}T_1&0\\L_1&T_1\end{pmatrix}.
\tag{4.158}
$$
这里 $L_0,L_1$ 包含全部低行跨越最高边界的 carry。
以下没有将它们换成纯模型。

#### 4.9.2 低行比值与固定维相位单位

定义真正解析芽
$$
c_m^{\,0}(z)=\zeta^r\frac{g_m(\zeta z)}{g_m(z)}.
$$
这里上标 $0$ 用来与辅助系数 $c_m$ 区分。
在两个有限头上合法求值：
$$
C_m=c_m^{\,0}(A_m),\qquad
C_m^{[p]}=c_m^{\,0}(A_p)
 =\begin{pmatrix}C_m&0\\F_m&C_m\end{pmatrix}.
\tag{4.159}
$$
只使用 $g_m(0)\ne0$ 的有限幂零函数演算；
不把 $T_0$ 当作可逆算子。

由 $f_m(\zeta z)=c_m^{\,0}(z)f_m(z)$ 和 (4.157)，准确有
$$
\boxed{
\gamma_\zeta(T_p)-C_m^{[p]}T_p=E\,U_m,
}
\tag{4.160}
$$
其中右侧表示以低块 $U_m$ 为下左块，而
$$
U_m=
2c_m(C_m-I)+4a_m(C_mX_m-X_{m,\zeta}).
\tag{4.161}
$$
特别，
$$
T_1=C_mT_0,\qquad
L_1=C_mL_0+F_mT_0+U_m.
\tag{4.162}
$$
这些是保留完整 carry 后的恒等式。

置
$$
K=\ker T_0=\operatorname{span}\{e_{H-r},\ldots,e_{H-1}\},
\qquad P=P_K.
$$
$U_m$ 是 $A_m$ 的多项式，故保持 $K$。
若 $c_m\ne0$，则
$$
W_m=U_m|_K
$$
是一个真正的 $r\times r$ 单位，其全部对角元为
$$
2c_m(\zeta^r-1)\ne0.
\tag{4.163}
$$
当 $m$ 足够大时，$C_m,X_m,X_{m,\zeta}$ 的前 $r$ 个 Taylor
系数已与 $m$ 无关；末 $r$ 坐标中的 $A_m$ 权也稳定，
因为 $v_2(H-s)=v_2(s)$ 对固定 $0<s<r$ 成立。
所以存在只依固定低行、$r,\zeta$ 的常数 $C$，使
$$
\boxed{
\beta_m:=\|W_m^{-1}\|
 \le \frac{C}{|c_m|}
 \left(1+\frac{|a_m|}{|c_m|}\right)^{r-1}.
}
\tag{4.164}
$$
证明是有限 Neumann 和：
$W_m=2c_m(\zeta^r-1)I+V_m$，
$V_m^r=0$ 且 $\|V_m\|\le C(|a_m|+|c_m|)$。
整个逆只需 $r$ 项。

因而相位接口本身不付 $\alpha_m^{-1}$。
但不能只凭 (4.164) 声称联合原像便宜；
下一两节保留完整低头源和 Schur 度量。

有一个容易混淆的等价写法。
若先对完整 $f_p$ 取比值
$\zeta^rg_p(\zeta z)/g_p(z)$，
其低块已含最高行在 $z^{H-r},\ldots,z^{H-1}$ 的系数，
可能具有 $c_m/\alpha_m$ 级大小。
在那种写法中，相位改善被藏在巨大比值的低块里。
(4.159) 坚持使用低行 $f_m$，才把它准确分离为 (4.161)；
两种写法不能混用。

#### 4.9.3 完整联合 row 的准确最小源

定义
$$
\mathscr R(u,v)=T_0^*u+T_1^*v,\qquad
\mathscr D(u,v)=L_0^*u+L_1^*v.
$$
按上下半源重排后，完整联合 adjoint row 就是
$$
\mathscr L=
\begin{pmatrix}\mathscr R&\mathscr D\\0&\mathscr R\end{pmatrix}.
\tag{4.165}
$$
因此其未压缩 Gram 是
$$
\mathscr L\mathscr L^*=
\begin{pmatrix}
\mathscr R\mathscr R^*+\mathscr D\mathscr D^*
 &\mathscr D\mathscr R^*\\
\mathscr R\mathscr D^*&\mathscr R\mathscr R^*
\end{pmatrix}.
\tag{4.166}
$$
不能先把 (4.166) 的每一项压到某个猜测的好空间再取逆。

记
$$
J=\mathscr R^\dagger,\qquad
\mathcal N=\ker\mathscr R,\qquad
D_{\mathcal N}=\mathscr D|_{\mathcal N},\qquad
\mathcal E=P D_{\mathcal N}.
$$
$J$ 在 $K$ 上为零，在 $K^\perp=\operatorname{Ran}\mathscr R$
上为最小范数右逆。

$\mathcal E$ 满射到 $K$。确实，对 $v\in K$，
$$
n(v)=(-C_m^*v,v)\in\mathcal N,
$$
而 (4.162) 给
$$
\mathscr D n(v)=T_0^*F_m^*v+U_m^*v,\qquad
P\mathscr D n(v)=W_m^*v.
\tag{4.167}
$$
(4.163) 便给满射性。这一步没有给 $F_m$ 的范数付费，
因为它在该边界投影中被准确消去。

取任意目标 $y=(y_0,y_1)$，其中 $y_1\perp K$。
置
$$
z_0=Jy_1,\quad
a=P(y_0-\mathscr D z_0),\quad
b=(I-P)(y_0-\mathscr D z_0),
$$
$$
M_{\mathcal N}
=I_{\mathcal N}
 +D_{\mathcal N}^*J^*J D_{\mathcal N},\qquad
c=D_{\mathcal N}^*J^*Jb.
\tag{4.168}
$$
$M_{\mathcal N}$ 是严格正单位，且
$\mathcal E M_{\mathcal N}^{-1}\mathcal E^*$ 在 $K$ 上严格正。
准确最小化参数为
$$
\begin{aligned}
n_*={}&M_{\mathcal N}^{-1}c\\
&+M_{\mathcal N}^{-1}\mathcal E^*
(\mathcal E M_{\mathcal N}^{-1}\mathcal E^*)^{-1}
(a-\mathcal E M_{\mathcal N}^{-1}c).
\end{aligned}
\tag{4.169}
$$
相应的完整最小源为
$$
z_*=z_0+n_*,\qquad x_*=J(b-\mathscr D n_*).
\tag{4.170}
$$
其平方范数准确为
$$
\boxed{
\begin{aligned}
\|(x_*,z_*)\|^2={}&
\|z_0\|^2+\|Jb\|^2
-\langle M_{\mathcal N}^{-1}c,c\rangle\\
&+\left\langle
(\mathcal E M_{\mathcal N}^{-1}\mathcal E^*)^{-1}
(a-\mathcal E M_{\mathcal N}^{-1}c),
a-\mathcal E M_{\mathcal N}^{-1}c
\right\rangle.
\end{aligned}
}
\tag{4.171}
$$
说明：任何下半源为 $z_0+n$，$n\in\mathcal N$；
上半方程可解恰当且仅当 $\mathcal E n=a$。
其最小上半源为 $J(b-\mathscr D n)$。
因 $z_0\perp\mathcal N$，总费用是
$$
\|z_0\|^2+\|n\|^2+\|J(b-\mathscr D n)\|^2.
$$
配平方并在约束 $\mathcal E n=a$ 下作有限维正最小化，
即得 (4.169)--(4.171)。
这给完整 Gram 的费用，没有免费舍去任何 Schur 残量。

#### 4.9.4 一个显式全目标源及其准确预算

为了给出可直接估计的上界，令
$$
S_m=(T_0^*)^\dagger,\quad
j_m=\|S_m\|,\quad
b_m=\|\mathscr D\|,\quad
d_m^{\,C}=(1+\|C_m\|^2)^{1/2},
$$
$$
\ell_m=\|P L_0^*S_m\|.
\tag{4.172}
$$
这里 $d_m^{\,C}$ 不是原权 $d_m$。

对上述任意目标，取
$$
z_0=(S_my_1,0),\qquad
a=P(y_0-\mathscr D z_0),\qquad
v=(W_m^*)^{-1}a,
$$
$$
n=(-C_m^*v,v),\qquad z=z_0+n,\qquad
x=(S_m(y_0-\mathscr D z),0).
\tag{4.173}
$$
由 (4.167)，$P(y_0-\mathscr D z)=0$，故 (4.173) 合法，
并且准确有 $\mathscr L(x,z)=y$。
它未必是最小源，但整个源都已给出。

直接逐项估计得到
$$
\boxed{
\|(x,z)\|\le
\left\{
j_m+(1+b_mj_m)
\left[j_m+d_m^{\,C}\beta_m(1+\ell_m)\right]
\right\}\|y\|.
}
\tag{4.174}
$$
具体地，
$$
\|a\|\le\|y_0\|+\ell_m\|y_1\|,\qquad
\|n\|\le d_m^{\,C}\beta_m\|a\|,
$$
$$
\|z\|\le j_m\|y_1\|+
d_m^{\,C}\beta_m(\|y_0\|+\ell_m\|y_1\|),
$$
且 $\|x\|\le j_m(\|y_0\|+b_m\|z\|)$。
因此 (4.174) 支付的是最后实际源范数，
没有把完整 $C_m^{[p]}$ 的巨大范数额外当作必付右因子。

#### 4.9.5 低头 carry 与边界反馈的统一控制

最高分块中的低行 carry 满足
$$
L_0=-4a_mX_m-2c_mI+E_m,\qquad
\|E_m\|\le C\eta_{m-1}.
\tag{4.175}
$$
给出直接核验。对 $j<m$，$N_j^{[p]}$ 与
$\operatorname{diag}(N_j^{[m]},N_j^{[m]})$ 之差只在下左块，
其非零部分是常数权的坐标平移，范数准确为
$$
\delta_{j,m}
=\frac{d_m}{d_j^2\prod_{j<\nu<m}d_\nu}
=\prod_{\nu=j}^{m-1}\eta_\nu
\le\eta_{m-1}.
\tag{4.176}
$$
由 $N_j^2=\eta_jN_{j+1}$ 与 $\|N_j\|\le1$，
两个有限头中的 $(I+N_j)^{-1}$ 范数均不超过 $3$。
Cayley resolvent 恒等式给对应 $Q_j$ 差的范数不超过
$18\delta_{j,m}$，平方差不超过 $216\delta_{j,m}$。
对 $x_m^2$、辅助一次和及 $B_0$ 逐项求和，
得到 (4.175)，常数只依 $\|a\|_1,\|c\|_1$。
未假定低行矩阵是纯产生算子。

另外存在固定常数 $C_r$，使
$$
\|P S_m\|\le C_r.
\tag{4.177}
$$
由原完整 MP 公式，$S_m$ 的末 $r$ 行只读目标末 $2r$ 个坐标：
若 $k\ge H-r$，只有
$k-r\le b\le H-r-1$ 可以贡献，
故逆系数指标 $b-k+r$ 落在 $0,\ldots,r-1$。
这些系数已稳定；相应权比只穿过距末端小于 $2r$ 的固定低位。
于是有限矩阵的所有相关条目一致有界，得到 (4.177)。
这里保留了这些行中所有允许的逆系数，而不是只留零次项。

因 $X_m$ 保持 $K$，
$P X_m^*=P X_m^*P$。
故 (4.175)--(4.177) 给
$$
\boxed{
\ell_m\le
C_r\bigl(4|a_m|\|X_m\|+2|c_m|\bigr)
+C\eta_{m-1}j_m.
}
\tag{4.178}
$$
这说明下半目标反馈到上半边界的费用没有多乘一次
整个 $j_m$，除了已显式保留的 supercarry 项。
$b_m$ 由完整有限头 $T_p,\gamma_\zeta(T_p)$ 的统一范数控制。

#### 4.9.6 锋利低头圆给出的单层联合上界

沿用 §4.2 在低头 $H=2^m$ 的圆
$$
\rho_m=e^{-\lambda_m},\qquad
\mathcal F_m(k)=\lambda_m k+\log W_k.
$$
原证明已给
$$
|g_m(z)|\ge|t_r|/2,\qquad |g_m(z)|\le2|t_r|
\quad(|z|=\rho_m)
$$
以及
$$
0\le\mathcal F_m(k)\le\mathcal F_m(H-1),\qquad
\mathcal F_m(H-1)=(35/6+o(1))16^m.
$$
同一个圆上 $|c_m^{\,0}(z)|\le4$。
Cauchy 与准确权比因而给
$$
\|C_m\|\le4H e^{\mathcal F_m(H-1)},\qquad
j_m\le\frac{2H}{|t_r|}
 e^{\mathcal F_m(H-1)+r\lambda_m}.
\tag{4.179}
$$
第一界用矩阵条目
$[z^{b-k}]c_m^{\,0}(z)\,W_b/W_k$；
第二界正是原 $q=1$ 完整 MP 上界。
二者都只在真实低头求值。

由 $\eta_{m-1}\le e^{-770\,16^{m-1}}$，
(4.179) 推出 $\eta_{m-1}j_m\to0$。
若 $a,c\in\ell^1$，则 (4.178) 进一步给 $\ell_m\to0$。

若还假设最终 $c_m\ne0$ 且
$$
\log^+(|c_m|^{-1})=o(16^m),
\tag{4.180}
$$
则 (4.164) 给 $\log^+\beta_m=o(16^m)$。
记 $\mathcal J_p$ 为完整 row
$[T_p^*,\gamma_\zeta(T_p)^*]$ 在其像上的 MP 右逆。
由 (4.174)、(4.178)、(4.179)，准确得到上界
$$
\boxed{
\limsup_{p\to\infty}16^{-p}\log^+\|\mathcal J_p\|
 \le\frac{35}{48}.
}
\tag{4.181}
$$
因为 (4.174) 的最高指数为
$2\mathcal F_m(H-1)+2r\lambda_m+o(16^m)$，
而 $p=m+1$。
本式只是联合源上界，不是其精确型或下界。

这一 row 的像准确为
$$
\{(y_0,y_1):y_1\perp K\}
=\operatorname{span}\{e_0,\ldots,e_{2H-r-1}\}.
$$
所以对真空可以只删全头最后 $r$ 个目标坐标，
目标误差为 $\sqrt{r/(2H)}$。
与单行的最高 carry 主列相比，本节确实给出全目标联合源的改善；
不需要在中间边界另加一个坐标 mask。

(4.181) 乘上 §4.8 的 $K_p=e^{O(p)}$ 后，
真实局部提升 carry 仍可支付。
但原临界慢尾只有 $e^{-\beta p^\alpha}$ 量级，
当前 $q=1$ 上界本身不能证明 §4.8 的总误差趋零。
这既不是实际最小费用的下界，也没有排除更精细的 Schur 选择。

#### 4.9.7 后续递推所须保留的条件

(4.169)--(4.171) 给出可以继续分析的完整度量：
边界接口不是只看 $W_m^{-1}$，
而是
$\mathcal E M_{\mathcal N}^{-1}\mathcal E^*$。
若要把单层改善反复使用，须控制这个真实 Schur Gram，
或给出同样准确的完整源构造与相容费用。

本节只证明一次行。
对 $T_p^q,\gamma_\zeta(T_p)^q$，最高位 $E^2=0$，
高位一次系数带有低行的 $q-1$ 次幂；
不能直接把 (4.163) 的 $r$ 维单位改成 $rq$ 维单位。
同样，不能将低头比值 $C_m$ 的范数、局部相位逆费用、
最终联合源范数三者互相替代。

准确的新接口是：
同一个真实正常见证允许固定相位分离，
完整最高 carry 可以在联合 row 中通过 (4.160) 重组，
并有 (4.171) 的全 Gram 与 (4.174) 的全目标源。
临界联合费用与多层非坐标目标仍须继续求解。

## 5. 与已付真核 HS 残量的准确比较

[混合幂及真核 HS 工作注记 §7](../notes/2026-11-13-canonical-positive-sources-mixed-power-residuals-and-polynomial-budgets-normal-complex.md) 对原 $T\rho^{1/2}=0$ 已付
$$
\|T_p^q\rho^{1/2}\|_{\rm HS}
\le\sqrt{\tau}\,\mathfrak b_{p,q},
\qquad
\mathfrak b_{p,q}=\mathfrak r_p^q+qM^{q-1}\epsilon_p.
\tag{5.1}
$$
其中 $\mathfrak r_p$ 是真实尾差的选定上界，$\epsilon_p$ 是局部头比较的真实 carry；不是把整个 $T$ 的尾差称为纯尾算子。

在 $a_j=e^{-\beta j^\alpha}$、$\alpha>1$、$c_j=a_j^\kappa$ 的迟首正尾、$\kappa>1$ 中，可取
$$
\mathfrak r_p=C e^{-\beta p^\alpha},\qquad
\epsilon_p\le C'e^{-770\,16^{p-1}}
\tag{5.2}
$$
（充分大 $p$，固定 $C>0$）。本节只比较这一已经付清的上界预算。

若用完整 $\xi_{p,q_p}$ 实现真空 ridge 证书，需同时选择 $s_p>0$ 使
$$
\mathfrak b_{p,q_p}/s_p\to0,\qquad
s_p\|\xi_{p,q_p}\|\to0,\qquad rq_p/2^p\to0.
\tag{5.3}
$$
这不可能。确实，前两项要求乘积 $\mathfrak b_{p,q_p}\|\xi_{p,q_p}\|\to0$；但由 (4.8) 与 (5.1)—(5.2)
$$
\log(\mathfrak b_{p,q_p}\|\xi_{p,q_p}\|)
\ge
\frac{35}{6}16^p-\beta q_pp^\alpha-O(8^p+p+q_p).
\tag{5.4}
$$
$rq_p=o(2^p)$ 给 $q_pp^\alpha=o(16^p)$，故右端趋于正无穷。

(5.4) 没有把已知上界当成实际残量的下界。它只说明：使用这一明确的充分残量预算与精确投影真空 MP 列，两个付款条件无法兼容。它未排除更强的见证专属残量，也未排除换用允许误差的原像。

## 6. 为何这不排 ridge：同一真实 $A_p$ 的校准

完整列的一个巨大坐标仍可能由改变很小的目标质量来绕开。最简单的实际例子就是 $T_p=A_p$。

固定整数 $1\le\ell<p$，定义
$$
u_{p,\ell}
=L^{-1/2}
\sum_{\substack{1\le k<L\\v_2(k)<\ell}}
\alpha_{v_2(k)}^{-1}e_k.
$$
准确有
$$
A_p^*u_{p,\ell}
=L^{-1/2}
\sum_{\substack{1\le k<L\\v_2(k)<\ell}}e_{k-1}.
$$
目标遗漏由 $k$ 为 $2^\ell$ 的倍数及最后一个坐标组成，恰有 $L/2^\ell$ 个，所以
$$
\boxed{
\|\Omega_p-A_p^*u_{p,\ell}\|=2^{-\ell/2},
\qquad
\|u_{p,\ell}\|\le\alpha_{\ell-1}^{-1}.
}
\tag{6.1}
$$
相反，$A_p$ 的完整 MP 真空列已含
$2^{-p/2}\alpha_{p-1}^{-1}$。

例如给定 $s_p=e^{-\beta p^\alpha}$，取
$\ell_p=\lfloor\theta\log_2p\rfloor$，其中 $0<4\theta<\alpha$。则 (1.3) 与 (6.1) 给
$$
\|\Omega_p-A_p^*u_{p,\ell_p}\|\to0,\qquad
s_p\|u_{p,\ell_p}\|\to0.
\tag{6.2}
$$
这只是说明 exact MP 与允许误差的 primitive 的差别；不把 $A_p$ 的逐列剪除移植到 $T_p^q$。后者具有 (2.5) 的完整长卷积，删去进位目标坐标后，仍须重新控制全部跨列贡献。

## 7. 当前留下的正向目标

真正足够的目标仍是找到某个允许误差的 $u_p$、幂 $q_p$ 与阈值 $s_p$，使
$$
\|\Omega_p-(T_p^{q_p})^*u_p\|\to0,\qquad
s_p\|u_p\|\to0,\qquad
\mathfrak b_{p,q_p}/s_p\to0.
$$
或直接证明对应低奇异值投影作用于真空的范数趋零。

R249 及其最优相似附录已有环境单链相似的四次成本；本文的范围增量仅为这一个完整 MP 真空列、全部允许整数幂、以及与真核残量预算的直接比较。本文没有新的普通 ISP 完成声明。
