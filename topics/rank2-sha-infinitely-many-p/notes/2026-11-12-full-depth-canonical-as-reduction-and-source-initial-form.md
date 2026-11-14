# 全深度 canonical Artin–Schreier 约化与真实源的初始形式

日期：2026-11-12。**状态：以下全系数约化、正反向整级数、无限尖锐系数及实际源提升命题均已证明。**
它们保留 R170/R174 的原 theta 曲线。特征 $p$ 的多项式方程只描述明确缩放后的约化；本文没有把它提升成原特征零曲线的多项式方程，也没有把剩余源自动放回原前缀核。

固定惰性 $p=4r-1\ge7$，置 $R=r(p-1)=(p^2-1)/4$。
在实际 $E_0:y^2=x^3-x$ 上用
$$
s=u^4,\qquad a=\vartheta^4,\quad b=\sigma^4=sa,\quad
t(s)=\log a=\frac{W(s)}{17},\quad
 t_m=\frac1m\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
\tag{1}
$$
记 $\tau=p t_r\bmod p\in\mathbb F_p^\times$；R170/R174 已证明它也等于 $pu_0\bmod p$。

## 1. 对数的全系数界与唯一最低项

由 R163 的准确计数，
$$
v_p(t_m)=-v_p(m)+
 \sum_{h\ge1}(-1)^h
 \mathbf1_{\{p^h/4<(m\bmod p^h)<3p^h/4\}}.
\tag{2}
$$
因此对全部 $m\ge1$ 有
$$
\boxed{\quad v_p(t_m)\ge-\lfloor m/r\rfloor.\quad}
\tag{3}
$$
这里给出全范围的直接证明。若 $m<p$，(2) 只可能有 $h=1$ 的负项；$m<r$ 时它不存在，$m\ge r$ 时下界 $-1$ 足够。
若 $p^h\le m<p^{h+1}$、$h\ge1$，任何非零指标 $j$ 必须满足 $p^j<4m<p^{h+2}$，故 $j\le h+1$。
负项总数至多 $\lceil(h+1)/2\rceil$，另有 $v_p(m)\le h$。
而
$$
h+\lceil(h+1)/2\rceil\le2h+1
 \le3p^{h-1}\le\lfloor p^h/r\rfloor\le\lfloor m/r\rfloor.
$$
中间不等式在 $h=1$ 成立，随后由 $p\ge7$ 立即归纳。得到 (3)。在 $m=r$，准确有 $v_p(t_r)=-1$。

取 Eisenstein 扩张
$$
K_p'=\mathbb Q_p(\varpi),\quad \varpi^R=p,
\qquad \lambda=\varpi^r,\quad\mu=\varpi^p.
\tag{4}
$$
它的剩余域仍为 $\mathbb F_p$，且
$$
\lambda^{p-1}=p,\qquad\mu^r=p\lambda=\lambda^p,
\qquad\mu^R=p^p.
$$
以下先在 $\mathcal O_{K_p'}/(\varpi)$ 中约化。
令 $s=\mu y_0$。写 $m=rn+e$、$0\le e<r$，(3) 给
$$
v_\varpi\left(\frac{t_m\mu^m}{\lambda}\right)
 \ge rn+pe-r.
\tag{5}
$$
当 $m\ge r$，右边只在 $m=r$ 时可为零；当 $1\le m<r$，原整性给 $mp-r>0$。
所以整个形式级数满足
$$
\frac{t(\mu y_0)}{\lambda}\in\mathcal O_{K_p'}[[y_0]],
\qquad
\overline{t(\mu y_0)/\lambda}=\tau y_0^r.
\tag{6}
$$
(5) 还随 $m$ 趋于无穷，故这里没有把一个有限截断的常数外推到全深度。

## 2. 指数的全部 p 次幂项与准确 AS 图

置 $H(y_0)=t(\mu y_0)/\lambda$。指数展开给
$$
\frac{a(\mu y_0)-1}{\lambda}
 =\sum_{n\ge1}\frac{\lambda^{n-1}}{n!}H(y_0)^n.
\tag{7}
$$
$H(0)=0$，故每个系数只涉及有限个 $n$。
Legendre 计数给
$$
v_p\left(\frac{\lambda^{n-1}}{n!}\right)
 =\frac{s_p(n)-1}{p-1}\ge0,
\tag{8}
$$
其中 $s_p(n)$ 是 $p$ 进数位和。单位恰发生于 $n=p^j$。
令
$$
u_j=\frac{(p^j)!}{p^{(p^j-1)/(p-1)}}\in\mathbb Z_p^\times.
$$
将阶乘中的 $p$ 倍数剥离，每一层的其余因子按长度 $p$ 的余数块分组，Wilson 定理给 $u_j\equiv-u_{j-1}$，$u_0=1$。
因此
$$
\frac{\lambda^{p^j-1}}{(p^j)!}=u_j^{-1}\equiv(-1)^j\pmod\varpi.
$$
结合 (6)，(7) 的完整约化为
$$
\overline{(a-1)/\lambda}
 =\tau\sum_{j\ge0}(-1)^j y_0^{rp^j}.
\tag{9}
$$

因为 $b=s a$，变量 $y=b/\mu=y_0a(\mu y_0)$ 是一个首项一的整形式变量，且 $y\equiv y_0\pmod\varpi$；其整逆存在。
记原真图为 $a=f(b)$，则
$$
x(y)=\frac{f(\mu y)-1}{\lambda}\in\mathcal O_{K_p'}[[y]],
\qquad
\boxed{\quad \bar x+\bar x^p=\tau y^r.\quad}
\tag{10}
$$
这条方程的零常数形式解唯一，准确由 (9) 给出。
它是原整图在指定尺度上的约化，而非另选的比较曲线。

## 3. 真 Cartan 稀疏图的全深正反向形式

R174 给整坐标
$$
U=(a-1)-b/3+O((a-1,b)^2),\qquad V=b\cdot e(a-1,b),\quad e(0,0)=1.
$$
由于 $v_\varpi(\mu)=p>r=v_\varpi(\lambda)$，这些环境误差在除去各自尺度后都进极大理想。
所以 $U/\lambda$、$V/\mu$ 是同一 (10) 的整图及输出，约化分别为 $\bar x,y$。

完整 Teich 角色给
$$
U=v^r g(v^R),\qquad v=V(w),\qquad g(0)=u_0.
$$
定义
$$
\boxed{\quad G(T)=p\,g(p^pT).\quad}
\tag{11}
$$
把 $v=\mu y$ 代入，准确得到
$$
U/\lambda=y^rG(y^R).
$$
左侧全部系数整，而右侧系数在 $\mathbb Q_p$ 中；由
$\mathbb Q_p\cap\mathcal O_{K_p'}=\mathbb Z_p$，得
$$
G\in\mathbb Z_p[[T]],\quad G(0)\in\mathbb Z_p^\times,
\qquad
\boxed{\quad \bar G+T\bar G^p=\tau\quad\text{于 }\mathbb F_p[[T]].\quad}
\tag{12}
$$
最后一步是先用 (10) 模 $\varpi$，再因这些系数位于 $\mathbb Z_p$ 而降成模 $p$。
不能对一般 $K_p'$ 系数直接将这两个模数混用。

写
$$
t_j=\frac{p^j-1}{p-1}\quad(j\ge0).
$$
方程 (12) 的唯一解为
$$
\boxed{\quad
\bar G(T)=\tau\sum_{j\ge0}(-1)^jT^{t_j}.
\quad}
\tag{13}
$$
故 $p^{1+pt}[v^{r+tR}]U$ 总是整；它模 $p$ 非零恰好在 $t=t_j$，值为 $\tau(-1)^j$。
特别，原 $g_1$ 准确满足
$$
p^{p+1}g_1\equiv-\tau\pmod p,
\qquad v_p(g_1)=-(p+1).
\tag{14}
$$

反向也有一个完整整级数。令 $S=T G(T)^{p-1}$，它首项为单位，可整反演 $T=T(S)$；置
$$
C(S)=G(T(S))^{-1}\in\mathbb Z_p[[S]].
$$
原曲线准确满足
$$
\boxed{\quad
V^r=pU\,C\left(U^{p-1}/p\right),
\qquad \bar C(S)=\tau^{-1}(1+S).
\quad}
\tag{15}
$$
确实 $U^{p-1}/p=T G(T)^{p-1}$；模 $p$ 时 (12) 就是 $G(1+S)=\tau$。
因此若 $V^r=\Psi(U)$，其支撑只有 $n=1+h(p-1)$。
线性系数是原 $\pi_0=u_0^{-1}$；$U^p$ 系数是单位、模 $p$ 为 $\tau^{-1}$。
$h\ge2$ 的系数至少有估值 $2-h$，但本文不声称它们全部整。
尤其 $V^r/p$ 的 $U^p$ 项真有一个 $p$ 分母，R176 的首带余式格不能不加修正就用于全深度。

## 4. 原图包络在无限多个系数上尖锐

(9)–(10) 同样直接计算原 $f(b)=1+\sum c_kb^k$，不只计算换坐标后的 $U$。
对 $k_j=rp^j$，有
$$
\frac{\mu^{k_j}}\lambda
 =p^{(p^{j+1}-1)/(p-1)}.
$$
于是
$$
\boxed{\quad
p^{(p^{j+1}-1)/(p-1)}c_{rp^j}
 \equiv\tau(-1)^j\pmod p,
\qquad
v_p(c_{rp^j})=-\frac{p^{j+1}-1}{p-1}.
\quad}
\tag{16}
$$
这精确达到 R173 的 $e_p(rp^j)$，同时包含首共振及第二共振。
它解释全深度包络中的无限进位，但仍是指定坐标的系数结论。
这些坐标没有自动位于高阶原前缀核，因此 (16) 不提供任一饱和 jet 的范数下界。

## 5. AS 曲线与原有限次数源的全深必要条件

以下源是闭合平面的原
$$
E_D=\mathbb Z_p[X,Y]_{\le D},\qquad X=a-1,\quad Y=b.
$$
对非零 $P=\sum c_{ij}X^iY^j$ 定义
$$
\omega(P)=\min_{c_{ij}\ne0}\{R v_p(c_{ij})+ri+pj\}.
\tag{17}
$$
其实际初始多项式为
$$
H_P(x,y)=\overline{\varpi^{-\omega(P)}P(\lambda x,\mu y)}
 \in\mathbb F_p[x,y]\setminus\{0\}.
$$
它总次数至多 $D$；每个出现的单项权 $ri+pj$ 至多 $\omega(P)$，且同余于 $\omega(P)\pmod R$。

先核准所用曲线几何。多项式
$$
F=x^p+x-\tau y^r
$$
在代数闭常数域上不可约：将 $x$ 乘一个常数即可变为标准 $z^p-z=h(y)$，而 $h$ 在无穷处有与 $p$ 互素的极点阶 $r$；任何有理 $g$ 的 $g^p-g$ 若有极点，其阶均被 $p$ 除。因此没有有理根，阶 $p$ 的 Artin–Schreier 多项式不可约。
曲线仿射部分光滑，因为对 $x$ 的导数是一。在无穷处，若其在 $\mathbb P^1_y$ 上的分歧指数为 $e$，方程的极点阶给 $p\operatorname{ord}_\infty(x)=-er$，故 $p\mid e$。
扩张次数是 $p$，于是只有一个无穷点，且
$$
\operatorname{pole}_\infty(y)=p,\qquad
\operatorname{pole}_\infty(x)=r.
$$
原点处 $y$ 是局部参数。因此非零的 $H_P$ 在该曲线上的函数若不恒零，其原点零阶至多其唯一极点阶，也就至多 $\omega(P)$。

由 (10)，若真实完整前缀满足
$$
\operatorname{ord}_b P(f(b)-1,b)\ge k>\omega(P),
$$
那么 $H_P$ 在 AS 曲线上必须恒零，即
$$
\boxed{\quad F\mid H_P.\quad}
\tag{18}
$$
该结论无 $k<pr$ 限制。
若 $D<p$，因 $\deg F=p$ 而 $H_P\ne0$，(18) 不可能。
将 $P$ 除去共同 $p$ 因子后 $\omega(P)\le pD$，从而得全深度零阶上界
$$
\boxed{\quad 0\ne P\in E_D,\ D<p
 \ \Longrightarrow\ \operatorname{ord}_bP(f(b)-1,b)\le pD.\quad}
\tag{19}
$$

## 6. 初始关系能在同一实际次数格中提升

取 $\widetilde\tau\in\mathbb Z_p^\times$ 为 $\tau$ 的任意提升，定义真正的源多项式
$$
\mathcal H_p=X^p+pX-\widetilde\tau Y^r\in E_p.
\tag{20}
$$
假设 (18)，写 $H_P=FG$。对权 $(r,p)$，$F$ 的最高权部分是 $x^p-\tau y^r$，权 $pr$；多项式环无零因子，故
$$
\deg_{(r,p)}G\le\omega(P)-pr,\qquad
\deg G\le D-p.
$$
同时按 $\mathbb Z/R$ 分次，$H_P$ 齐次、$F$ 齐次且乘法单射，故 $G$ 只含权同余 $\omega(P)-pr\pmod R$ 的单项。
对 $G=\sum g_{ij}x^iy^j$ 逐项选整数提升，令
$$
Q=\sum\widetilde g_{ij}
 p^{(\omega(P)-pr-ri-pj)/R}X^iY^j.
\tag{21}
$$
每个指数都是非负整数，且 $Q\in E_{D-p}$。按同一缩放直接比较初始项，得到
$$
\boxed{\quad \omega(P-\mathcal H_pQ)>\omega(P).\quad}
\tag{22}
$$
这是原实际多项式空间中的明确整提升。
但 $\mathcal H_p$ 沿原曲线一般不为零；(22) 的余项不自动保原前缀。
若继续迭代，必须把 $\mathcal H_p$ 的真实缺陷与 $Q$ 一同搬入新的共同源格，不能分别消去两项的前缀。

原 $A_2,B$ 源只经固定 degree $17$ 映射嵌入这个 $ab$ 源；本文没有把 (20) 自动称为 $\mathbb Z_p[A_2,B]$ 中的源多项式。
严格总预算仍要支付此源区别、全精度缺陷及全部先前零行。

## 7. 有限独立校准

[实际 sigma 逆级数脚本](../scripts/check-canonical-as-reduction.py) 从固定 $t(s)$、真正第一类周期 $w=s\mathcal L(s)^4$ 计算 $a(w),b(w)$，再作 R174 的准确字符投影和真正 $V$ 反演。
它不从 (12) 生成测试系数；只校准 $p=7$ 的 $0\le t\le8$ 和 $p=11$ 的 $0\le t\le3$。
例如 $p=7$ 的归一化 $G_t\bmod7$ 仅在 $t=0,1,8$ 非零，值依次为 $2,5,2$；$p=11$ 的 $t=0,1$ 为 $7,4$。
一般结论来自上面的全系数证明，不由这些有限值外推。

## 依赖

- [R163 全部系数的精确赋值](2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)：(2) 的原整数乘积计数。
- [R173 全深度包络](2026-11-12-full-depth-cm-carry-envelope-and-true-jets.md)：(16) 与既有真实前缀上界的准确关系。
- [R174 实际整 Cartan 坐标](2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)：整变换、完整角色支撑及真实有限源。
- [R176 首带除幂源格](2026-11-12-actual-divided-source-lattices-and-prefix-saturation.md)：(15)、(20) 提供其越过首带时必须同时保留的真实新项。
