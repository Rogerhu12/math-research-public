# R211 — 原 theta 连接的两权正规式、固定与剩余 log 因子及真实残差

日期：2026-11-12。**状态：两权窗口内的连接正规式、原行列式分解及同一实际样本的剩余项已证明。没有证明无穷素数非零，也没有从裸有理迹单位推出原目标单位。**

本篇继续 [R207](R207-actual-dyadic-twist-trace-and-theta-branch-identity.md)
与 [R208](R208-original-theta-single-pole-faber-and-integral-log-comparison.md)。
始终保留 R197 的原 $A_2,B$、原 $P,Q$ 和唯一坏指数项的同一个 gauge。
新增的是：把实际 theta 的连接项写成一个明确的多项式部分、一个共同整 gauge 方向和一个线性的 $\log h_p$ 强迫项，再在原 Faber 配对中区分 $s=-1$ 与其余因子。

## 1. 原级数、有限窗与二项式多项式

令 $p=4r-1\ge7$ 为素数，$d=2r-1=(p-1)/2$。在原 $E_0$ 上使用
$$
s=x^{-2}=u^4,\qquad w=z^4,\qquad
z=uF(s),\qquad W(s)=sF(s)^4,
$$
其中
$$
F(s)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}s^j.
$$
记
$$
h(s)=\sum_{j=0}^{d}\frac{(-1)^j\binom dj}{4j+1}s^j\in\mathbf F_p[s],
\qquad
\kappa=\frac{\binom{2r-2}{r-1}}{4^{r-1}}\in\mathbf F_p^\times.
\tag{1}
$$
R202 的实际二项式参数给
$$
\deg h=d,\quad h(0)=1,\quad s^d h(1/s)=h(s),\qquad
4s h'(s)+h(s)=(1-s)^d.
\tag{2}
$$
在本篇所读窗口，$\overline F=h$。特别
$$
h(-1)=0,\qquad h'(-1)=-2^{d-2}\ne0.
\tag{3}
$$
所以可准确分解
$$
h(s)=(1+s)\,\widetilde h(s),\qquad
\widetilde h(0)=1,\quad \widetilde h(-1)\ne0.
\tag{4}
$$
$\log h,\log(1+s),\log\widetilde h$ 均指在 $s=0$、常数为零的有限形式对数，只读次数小于 $2r<p$。其中每个积分分母都是单位。

令 $\Gamma=\overline{\Gamma_p}\in\mathbf F_p[s]/(s^{2r})$ 为 R208 的**实际**共同 theta 代表，$\Gamma(0)=1$；写
$$
H=\frac{\Gamma'}{\Gamma}\pmod{s^{2r-1}}.
$$
$H$ 只读取原有限 jet。以下不把 $\Gamma$ 在别的点的值冒称原 theta 的全局值。

## 2. 原 logarithmic derivative 的准确强迫项

先在特征零中写
$$
L(s)=\log\vartheta(z(s))^{68},\qquad H_{\rm raw}=L'(s).
$$
R162 的原系数递推
$$
L(s)=\sum_{m\ge1}\frac{d_m}{m}s^m,\qquad
d_1=\frac{17}{3},\qquad
d_{m+1}=\frac{4m+1}{4m+3}d_m
$$
准确等价于
$$
4s(1-s)H_{\rm raw}'+(3-5s)H_{\rm raw}=17.
\tag{5}
$$
设 $c_p=68k_r$，保留 R197 的原 $k_r$。实际整 gauge 是
$$
H_{\rm corr}=H_{\rm raw}-c_p\frac{d}{ds}W(s)^r.
$$
因为 $W^r=z^{p+1}$，并且 $dz/ds=1/(4u^3\sqrt{1-s})$，直接微分给
$$
\begin{aligned}
\mathcal P H_{\rm corr}
&=17-\frac{c_p p(p+1)}4\,s^{r-1}F(s)^{p-1},\\
\mathcal P&=4s(1-s)\frac d{ds}+3-5s.
\end{aligned}
\tag{6}
$$
式 (6) 在特征零就成立。R197 的整性和 $p k_r\bmod p=\kappa$ 使其约化到所需窗口，得到
$$
\boxed{\quad
\mathcal P H
=17\left(1-\frac{\kappa s^{r-1}}{h(s)}\right)
\pmod{s^{2r-1}}.
\quad}
\tag{7}
$$
这里使用 $F^p\equiv1$ 到所需低次数；不是全局恒等式
$F^{p-1}=1/h$。如果全局保留 $h(s)^p$，极点和次数会变化，不能把
(7) 的局部 $\log h$ 项擅自解释为原 theta 在所有 $h$ 根处的全局 monodromy。

## 3. 显式多项式部分与唯一共同 gauge 方向

定义
$$
\lambda(s)=s^{r-1}(1-s)^d,
$$
以及完全明确的多项式
$$
\mathcal B_p(s)=
\frac{17}{4}(1-s)^d
\sum_{\substack{0\le j\le d\\j\ne r-1}}
  \frac{(-1)^j\binom dj}{j-r+1}s^j.
\tag{8}
$$
其中 $-r+1\le j-r+1\le r$，排除零后均是单位。
由 (2) 可直接核对
$$
\mathcal P\lambda=0,\qquad
\frac d{ds}\bigl(4s^r h(s)\bigr)=\lambda(s).
\tag{9}
$$
另令
$$
S(s)=
\sum_{\substack{0\le j\le d\\j\ne r-1}}
 \frac{(-1)^j\binom dj}{j-r+1}s^{j-r+1}.
$$
因为 $(-1)^{r-1}\binom d{r-1}=\kappa$，
$$
S'=s^{-r}(1-s)^d-\kappa/s.
$$
使用 (2)，逐项计算给
$$
\mathcal P\left(\mathcal B_p-17\kappa\lambda\log h\right)
=17(1-s^p)\left(1-\frac{\kappa s^{r-1}}h\right).
$$
$s^p$ 在当前窗口之外。因此存在一个由原 $\Gamma$ 确定的标量
$C_p\in\mathbf F_p$，使
$$
\boxed{\quad
H=\mathcal B_p-17\kappa\lambda\log h+C_p\lambda
\pmod{s^{2r-1}}.
\quad}
\tag{10}
$$
没有额外自由源：$C_p$ 就是
$[s^{r-1}](H-\mathcal B_p)$。唯一性也可直接从 $\mathcal P$ 的系数递推看到：
在 $0\le j\le2r-2$ 中，唯一的零对角 $4j+3$ 出现在 $j=r-1$；
其齐次解准确为 $\lambda$。

定义下面两个积分时，**只积到次数 $<2r$**：
$$
\mathcal V_p(s)=
\left[
 \int_0^s\mathcal B_p(t)\,dt+
 68\kappa\int_0^s t^r h'(t)\,dt
\right]_{<2r},
\qquad
\Gamma^\circ(s)=\exp\mathcal V_p(s)\pmod{s^{2r}}.
\tag{11}
$$
这两个有限积分的分母均小于 $p$。由 (9) 分部积分，
$$
\int\lambda\log h
=4s^r h\log h-4\int s^r h'.
$$
又 $W^r\equiv s^r h\pmod{s^{2r}}$，于是 (10) 的准确积分形式为
$$
\boxed{\quad
\Gamma
=\Gamma^\circ
 \exp(4C_p W^r)\,
 \bigl(1-68\kappa W^r\log h\bigr)
 \pmod{s^{2r}}.
\quad}
\tag{12}
$$
最后一个因子的非平凡项从 $s^{r+1}$ 开始，故其平方在窗口之外。
这说明真正的 $\log h$ 强迫在第二个原权只出现一次，在第一个原权完全不出现。

(11) 不是一个免费全局 primitive。事实上 $\deg\mathcal B_p=p-1$，其最高系数在 $\mathbf F_p$ 中为 $17\ne0$；若把同一显式多项式一直积分到次数 $p$，会遇到非单位分母 $p$。本篇仅使用已明确给出的两权窗口。

## 4. 原两行与固定、剩余 log 的准确分解

记原多项式向量 $\mathbf P=(P,Q)$，以及 R197/R208 的原行
$$
\widehat{\mathbf R}_j=[w^{jr}]\Gamma(s(w))\mathbf P(s(w)),
\qquad j=1,2.
$$
定义辅助行
$$
\mathbf R_j^\circ=[w^{jr}]\Gamma^\circ(s(w))\mathbf P(s(w)),
$$
并把 (4) 的两项分别放进**同一原** Faber 配对：
$$
\begin{aligned}
\mathbf L_{\rm fix}
 &=[w^r]\Gamma(s(w))\mathbf P(s(w))
                  \log(1+s(w)),\\
\mathbf L_{\rm rem}
 &=[w^r]\Gamma(s(w))\mathbf P(s(w))
                  \log\widetilde h(s(w)).
\end{aligned}
\tag{13}
$$
在 (13) 中把 $\Gamma$ 换成 $\Gamma^\circ$ 不改变结果，因为其差从
$s^r$ 开始，而 $\mathbf P$ 和这两个对数均从正次开始。

由 (12) 直接得到
$$
\boxed{\quad
\widehat{\mathbf R}_1=\mathbf R_1^\circ,\qquad
\widehat{\mathbf R}_2
=\mathbf R_2^\circ+4C_p\widehat{\mathbf R}_1
 -68\kappa(\mathbf L_{\rm fix}+\mathbf L_{\rm rem}).
\quad}
\tag{14}
$$
这是两条**实际**列的同一个行操作，未把原两列分别更换 gauge。
因此
$$
\boxed{\quad
\det\widehat{\mathbf R}
=\det(\mathbf R_1^\circ,\mathbf R_2^\circ)
 -68\kappa\det(\widehat{\mathbf R}_1,\mathbf L_{\rm fix})
 -68\kappa\det(\widehat{\mathbf R}_1,\mathbf L_{\rm rem}).
\quad}
\tag{15}
$$
共同 gauge 参数 $C_p$ 完全消去，但剩余 $\log\widetilde h$ 配对仍在。

每个 (13) 的分量还可用原单固定极点的有限式直接读：
$$
\begin{aligned}
L_g(F)
&=\frac1r[s^{r-1}]
   \bigl(\Gamma(s)P_F(s)\log g(s)\bigr)'h(s)^{-4r}\\
&=[s^r]\Gamma(s)P_F(s)\log g(s)
                 \frac{(1-s)^d}{h(s)^2},
\qquad g=1+s,\ \widetilde h.
\end{aligned}
\tag{16}
$$
第二式使用 $4r\equiv1$、$h^{-4r}\equiv h^{-1}$ 在当前窗口以及 (2)。
所以 (15) 的剩余项是一个明确的原有限系数，不是任意补上的未知常数。

## 5. 同一实际 p43 校准排除无条件丢掉剩余项

[精确脚本](../scripts/check-original-theta-fixed-moving-log.py)
从 R162 的原有理 theta 递推和原椭圆对数重新生成 R208 的
$\Gamma$，再独立计算 (8)–(16)；
[输出](../scripts/check-original-theta-fixed-moving-log.json) 与脚本一起保存。
这里只复用已经出现的 $p=43$，没有扩充素数扫描。

准确结果是
$$
\kappa=30,\quad C_p=13,\quad -68\kappa=24
\quad\text{于 }\mathbf F_{43}.
$$

| 实际行或配对 | A2 分量 | B 分量 |
| --- | ---: | ---: |
| 原第一行 $\widehat{\mathbf R}_1$ | 39 | 6 |
| 原第二行 $\widehat{\mathbf R}_2$ | 22 | 2 |
| 多项式连接行 $\mathbf R_2^\circ$ | 26 | 13 |
| 加同一 gauge 后、去掉 log 强迫的第二行 | 33 | 24 |
| 固定因子配对 $\mathbf L_{\rm fix}$ | 29 | 23 |
| 剩余因子配对 $\mathbf L_{\rm rem}$ | 1 | 37 |

相应子式为
$$
\det\widehat{\mathbf R}=32,\quad
\det(\mathbf R_1^\circ,\mathbf R_2^\circ)=7,\quad
\det(\widehat{\mathbf R}_1,\mathbf L_{\rm fix})=35,\quad
\det(\widehat{\mathbf R}_1,\mathbf L_{\rm rem})=18.
$$
特别
$$
32=7+24\cdot35+24\cdot18\pmod{43}.
\tag{17}
$$
最后一个真实剩余项贡献 $2$；若把它丢掉，原 minor 会从 $32$ 错算成 $30$。
这严格排除“在原两列的完整两权 minor 中，剩余因子无条件自动消掉”的说法。

同一素数的 R207 裸有理迹单位为 $21$。它与 (13) 的固定因子配对不是同一个对象；
(13) 仍含原 theta 有限 jet 和原 Faber 核。

此样本的原第一行不为零，所以它不排除一个**另需证明**的、只在
$\widehat{\mathbf R}_1\in pO^2$ 后才成立的更细恒等式。更不能据 (17) 认定首行失败后的 next-digit minor 自动为零或自动非零。

## 6. 与完整中央条件仍缺的比较

本篇支付了原 theta 连接项，而没有把它省略：

1. 第一个权仍是原 $\widehat{\mathbf R}_1$，看不到 $\log h$ 强迫；
2. 第二个权的强迫只线性出现，且可准确拆成固定 $s=-1$ 因子与剩余因子；
3. 共同 gauge 方向在整个 minor 中消去，剩余因子一般不消去；
4. 两个配对均由同一原 $\Gamma,P,Q$ 和同一 Faber 泛函给出。

若原第一行已经被 $p$ 整除，R197/R208 所需的下一位仍是
$$
\det(p^{-1}\widehat{\mathbf R}_1,\widehat{\mathbf R}_2)\bmod p.
$$
式 (15) 只有模 $p$ 的两权信息，不计算原第一行除 $p$ 后的值。
继续工作必须保留这个整提升，并真正控制 (16) 的剩余配对或把它与
原除 $p$ 行建立新的关系。不能以 $h(-1)=0$、R207 的固定留数单位、
$\log h\ne0$ 或同一个对数参考方向代替这项非零证明。

