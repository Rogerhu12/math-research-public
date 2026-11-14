# R591 — 两个原惰性首 forcing 的同参数系数与准确首共振

日期：2026-11-14。**状态：已证明。**

本篇将 R586 的两个指定首系数同时化为一个固定级数的两个线性系数行。
变换保原 $b=17$、原加法坐标和首个 Gaussian 之前的整窗口。
共同级数的对数导数有显式一阶递推；其下一共振准确重现原 Gaussian 单位。
这个已知单位不等于两条目标系数，本篇没有由此声称联合非零。

## 1. 同一形式曲线上的四个固定级数

先在特征零取
$$
y^2=x^3+b,\qquad x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,
\quad D\zeta=-x,\quad \zeta=D\log\sigma .
$$
令
$$
u=x^{-1/2},\qquad t=bu^6,\qquad
y=-u^{-3}\sqrt{1+t},
$$
并准确定义
$$
\mathsf C(t)=(1+t)^{-1/2}=\sum_{n\ge0}C_nt^n,\qquad
\mathsf H(t)=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,
$$
$$
\mathsf J(t)=\sum_{n\ge0}\frac{C_n}{1-6n}t^n,\qquad
\mathsf K(t)=\left(\frac{\sigma(z(u))}{u}\right)^6 .
\tag{1}
$$
于是
$$
dz=\mathsf C(t)\,du,\qquad z=u\mathsf H(t),\qquad
\zeta(z(u))=u^{-1}\mathsf J(t).
\tag{2}
$$
第一式来自原椭圆微分。第三式的证明是
$$
D=\sqrt{1+t}\,\frac d{du},\qquad
6t\mathsf J'-\mathsf J=-\mathsf C ,
\tag{3}
$$
它与 $D\zeta=-u^{-2}$ 及原主部 $u^{-1}$ 等价。
不存在另选积分常数：型 $-1$ 与原主部已指定全部系数。

令
$$
\mathsf Q=\mathsf J\mathsf C=\sum_{n\ge0}q_nt^n,\qquad
\mathsf K=\sum_{n\ge0}k_nt^n,\qquad q_0=k_0=1 .
$$
由 $d\log\sigma/du=\zeta\mathsf C$，准确有
$$
\boxed{t\frac{\mathsf K'}{\mathsf K}=\mathsf Q-1.}
\tag{4}
$$
利用 (3) 和 $\mathsf C'/\mathsf C=-1/(2(1+t))$，
$$
\boxed{6t(1+t)\mathsf Q'+(2t-1)\mathsf Q+1=0.}
\tag{5}
$$
因此整个固定级数可用三条明确递推计算：
$$
\boxed{
C_0=1,\quad C_n=-\frac{2n-1}{2n}C_{n-1},\qquad
q_n=-\frac{6n-4}{6n-1}q_{n-1},\qquad
n k_n=\sum_{j=1}^nq_jk_{n-j}.
}
\tag{6}
$$
等价地，$L=\log\mathsf K$ 满足
$$
\boxed{6t(1+t)L''+(5+8t)L'+2=0,\qquad L(0)=0.}
\tag{7}
$$
这是同一个原 sigma 的方程；没有把它替换为另一个有利的有理来源。

## 2. 原 p 前窗口的全部整性

现在取 $p=6s-1>71$、$b=17$、$N=s-1$。
(6) 中 $1\le n<s$ 的所有分母均为 $p$ 单位：
$$
n,\quad2n,\quad6n-1,\quad6n+1 .
$$
所有这些 $C_n,q_n$ 也为单位；例如
$2n-1$ 与 $6n-4$ 在该区间均非零模 $p$。
所以
$$
C_n,\quad \frac{C_n}{6n+1},\quad
\frac{C_n}{1-6n},\quad k_n\in\mathbf Z_{(p)}
\quad(0\le n<s).
\tag{8}
$$
这里没有说每个 $k_n$ 是单位。

R586 的两个原首 forcing 是
$$
c_{4,p}=[z^{p-1}](x\sigma^6),\qquad
c_{1,p}=[z^{p-4}](-xy\sigma^6).
\tag{9}
$$
它们需要的相对次数都只有 $N=s-1$，
所以 (8) 足以进行全部换元和约化。
高阶 $\mathsf J,\mathsf K$ 的坏分母不被提前约化进本窗口。

## 3. 两个目标的准确同参数系数

**定理。** 在原指定整模型的惰性处，
$$
\boxed{
\overline{c_{4,p}}
=b^{s-1}[t^{s-1}](\overline{\mathsf K}\,\overline{\mathsf C}),
\qquad
\overline{c_{1,p}}
=b^{s-1}[t^{s-1}](\overline{\mathsf K}\,\overline{\mathsf H}^{\,3}).
}
\tag{10}
$$
右边每个级数只需截断到 $t^{s-1}$；所有条目按 (8) 有意义。

证明。特征零中原来源在 $u$ 坐标的准确式是
$$
x\sigma^6=u^4\mathsf K,\qquad
-xy\sigma^6=u\sqrt{1+t}\,\mathsf K .
\tag{11}
$$
对第一个系数用形式留数换元，保全部 Jacobian：
$$
\begin{aligned}
c_{4,p}
&=\operatorname{Res}_{z=0}(x\sigma^6)z^{-p}\,dz\\
&=\operatorname{Res}_{u=0}
 u^{4-p}\mathsf K(t)\mathsf C(t)\mathsf H(t)^{-p}\,du\\
&=b^{s-1}[t^{s-1}]
 \mathsf K(t)\mathsf C(t)\mathsf H(t)^{-p}.
\end{aligned}
\tag{12}
$$
因 $N=s-1<p$，在这个整截断环内
$\overline{\mathsf H}^{\,p}=1\bmod t^p$。
故 (12) 约化后给第一式。

对第二个系数，同样有
$$
\begin{aligned}
c_{1,p}
&=\operatorname{Res}_{z=0}(-xy\sigma^6)z^{-(p-3)}\,dz\\
&=\operatorname{Res}_{u=0}
 u^{4-p}\mathsf K(t)\mathsf H(t)^{3-p}\,du\\
&=b^{s-1}[t^{s-1}]
 \mathsf K(t)\mathsf H(t)^{3-p}.
\end{aligned}
\tag{13}
$$
这里 $\sqrt{1+t}$ 与 $dz/du=\mathsf C$ 准确相消。
再去掉同一个模 $t^p$ 的 $\mathsf H^p$ 因子，
就得到 (10) 的第二式。证毕。

所以普通方向 R549 的截断 log 平方/五次不能照搬过来：
本惰性两行的实际因子是 $\mathsf C$ 和 $\mathsf H^3$，
由 (12)–(13) 的原指数决定。

两行还有一个完整的末两系数分解。
记
$$
A_N=\sum_{i=0}^{N-2}k_iC_{N-i},\qquad
B_N=\sum_{i=0}^{N-2}k_i[t^{N-i}]\mathsf H^3 .
$$
因为 $C_1=-1/2$、$[t]\mathsf H^3=-3/14$，
$$
\begin{pmatrix}
b^{-N}c_{4,p}\\ b^{-N}c_{1,p}
\end{pmatrix}
\equiv
\begin{pmatrix}1&-1/2\\1&-3/14\end{pmatrix}
\begin{pmatrix}k_N\\k_{N-1}\end{pmatrix}
+\begin{pmatrix}A_N\\B_N\end{pmatrix}
\pmod p .
\tag{14}
$$
矩阵行列式为 $2/7$，是单位。
这使“两行同时零”成为对这两个**实际**末系数的准确两条条件，
而不使它们成为可独立调整的自由变量；所有 $k_i$ 仍须满足 (6)。

## 4. 下一共振的单位与目标两行的区别

写
$$
h_p=\binom{3s-1}{2s-1},\qquad c_p=b^s h_p ,
$$
与 R356/R587 的 Cartier 常数一致。
由 (6)，换元 $l=s-j$，在 $\mathbf F_p$ 中给
$$
\overline{q_{s-1}}
=(-1)^{s-1}\prod_{l=1}^{s-1}\frac{2l+1}{2l}
=\frac{(-1)^{s-1}(2s-1)}{4^{s-1}}
 \binom{2s-2}{s-1}.
$$
再用同一剩余域中的等式
$h_p=(-1)^s4^{-s}\binom{2s}{s}$，
于 $\mathbf F_p$ 中得到
$$
\boxed{\overline{q_{s-1}}=-2s\,h_p=-h_p/3\ne0.}
\tag{15}
$$
下一项满足准确特征零式
$$
p q_s=-(p-3)q_{s-1}.
$$
由 (6) 的 $n=s$ 递推，除 $q_s$ 外其余乘积仍整，
且 $s$ 是单位，故
$$
\boxed{\overline{p k_s}
=\overline{p q_s/s}=18\,\overline{q_{s-1}}=-6h_p\ne0.}
\tag{16}
$$
这恰与 R586 的实际 Gaussian 单位
$a=6p[z^{p+1}]\log(\sigma/z)$ 相符：
$$
\overline{a/b^s}=-6h_p.
\tag{17}
$$
也可直接比较
$\log\mathsf K=6\log(\sigma/z)+6\log(z/u)$：
$t^s$ 处第二项整，因为 $6s+1=p+2$ 是单位，
首项给同一个首坏分母。

(15)–(17) 位于共同对数导数及 $k_s$ 的下一共振，
而 (10) 读取的是 $\mathsf K\mathsf C$、
$\mathsf K\mathsf H^3$ 的 $t^{s-1}$ 系数。
它们不能互换。尤其不能从 $q_{s-1}$ 或 $p k_s$ 为单位，
直接宣布 (10) 任一条或两条联合非零。

## 5. 可继续使用的原接口

(6)、(10)、(14) 在固定原来源上给完整、有限、无未定义分母的两行。
它们与 R589 的首共振整项相连时，
仍须保留 $b^{s-1}$、原 $w=z^6$ 与 $w^s=p\epsilon$ 的行尺度。
R587 的整个 Gaussian 曲率也没有替换上述指定系数。

尚须证明两行的适当联合非消失，或将其与原全部算术和饱和前缀接合。
本篇没有证明这些尚缺条件，也没有作新的素数非消失扫描。

