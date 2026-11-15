# R725 — 原整窗的共同平方模型与低极帽直接返回

日期：2026-11-15。**状态：以下两种原整窗插值、完整极帽、全部首 Cartier 返回及实际留数公式已证明。**  
两种模型均由同一原 sigma 的已付完整窗口唯一指定；没有增加可自由选择的来源列。

保持
$$
E:y^2=x^3+b,\quad b=17,\quad
p=6s-1>101,\quad q=p^2,\quad L=(q-1)/6,
\quad k=\mathbf F_{p^2}.
$$
第三来源 $m=136$ 仍要求 $p>136$。
原坐标、微分及规范为
$$
\omega_E=\frac{dx}{2y},\quad D=\frac d{\omega_E},\quad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
w=z^6,\quad \sigma^\circ=zU(w).
$$
只在 R717 已证明整的有限窗口中约化。
令 $\mathcal D_2$ 为三个非零二挠点的约化除子。
沿用 R721 的同一个
$$
\widehat Z=z+O(z^q),\qquad D\widehat Z=1,\qquad
(\widehat Z)_\infty=M_p\mathcal D_2,\qquad
M_p=p(2s-1)=p(p-2)/3.
\tag{1}
$$
记 $\mathcal Z=(\widehat Z)_0$。它由 $3M_p$ 个几何单零组成，包含 O。
原三个完整多项式来源记为 $\phi_m$，$m=34,72,136$；
在 O 的极阶准确为 $m-6$，其它点正则。
其原不变量为
$$
A_m^\circ=(\sigma^\circ)^m\phi_m
 =wU(w)^m\ell_m(w),\qquad \ell_m(0)\ne0.
\tag{2}
$$
全部原系数和共同 Gaussian 规范保持。

## 1. 原不变量坐标的单位三角返回

定义
$$
\xi=\frac b{y^2},\qquad B_2=\frac{x^2}{y^2},\qquad
X(w)=z^2x(z).
$$
于是有实际局部等式
$$
\xi=\frac{bw}{X(w)^3+bw}=bw+O(w^2),\qquad
B_2=z^2\,\frac{X(w)^2}{X(w)^3+bw}.
\tag{3}
$$
$\xi$ 是原 $\mu_6$ 不变量，$B_2$ 为型2。
$\xi$ 在 O 为六阶零，在每个二挠点为二阶极；
$B_2$ 在 O 为二阶零，在 $x=0$ 的两个点各为二阶零，
在每个二挠点为二阶极。

由于 $b$ 是单位，(3) 有唯一有限反级数
$$
w=w(\xi)\pmod{\xi^{L+1}}.
\tag{4}
$$
它只用 $X\bmod w^L$。每一步只除 $b$ 的幂。
等价地，$B_2\xi^j$ 的首项是
$b^jz^{2+6j}$，$\xi^j$ 的首项是 $b^jz^{6j}$；
两种返回矩阵都是单位三角矩阵。

这没有取任何高阶普通对数。
$U\bmod w^L$ 可用 R717 的实际 Artin–Hasse 坐标，
也可在 R723 的 $e_{\rm CM}(p)\ge s$ 范围内，
由两个固定 CM 来源和原 $X$ 的第一位恢复。
(3)–(4) 不要求额外原第二位。

## 2. 保持三个来源共有平方的模型

存在唯一
$$
P_2(\xi)\in k[\xi]_{<L}
$$
使
$$
\boxed{\quad
\mathcal S_2=B_2P_2(\xi)
       =(\sigma^\circ)^2+O(z^{q+1}).
\quad}
\tag{5}
$$
其准确定义为
$$
P_2(\xi)=
\left[
 \frac{U(w)^2\{X(w)^3+bw\}}{X(w)^2}
\right]_{w=w(\xi),\,\deg_\xi<L}.
\tag{6}
$$
$X(0)=U(0)=1$，故 $P_2(0)=1$。
(3) 的单位三角性证明存在和唯一；
保留的末行是 $z^{2+6(L-1)}=z^{q-5}$，
下一型2行是 $z^{q+1}$，给 (5)。

在全局除子上，
$$
(\mathcal S_2)_\infty\le 2L\mathcal D_2.
\tag{7}
$$
所有 m 都是偶数，因此同一个 $\mathcal S_2$ 给
$$
\mathcal A_m^{\rm com}=\mathcal S_2^{m/2}\phi_m.
$$
由
$\mathcal S_2-(\sigma^\circ)^2=O(z^{q+1})$
和原 $\phi_m$ 的极阶 $m-6$，
$$
\boxed{\quad
\mathcal A_m^{\rm com}
   =A_m^\circ+O(z^{q+5}),\qquad
(\mathcal A_m^{\rm com})_\infty
   \le mL\mathcal D_2.
\quad}
\tag{8}
$$
第一式的误差阶是
$(q+1)+(m-2)-(m-6)=q+5$。
在 O 模型仍从 $z^6$ 起，故 O 没有极。
其余地方 $\phi_m$ 正则，(7) 给第二式。

(8) 保留三个来源的同一个平方模型及原完整 $\phi_m$，
而非分别挑选三种 sigma。
若使用全局连接，其准确式为
$D-(m/2)D\log\mathcal S_2$；
它是此有理模型的 gauge 连接。
它与原连接的比较只在已经支付的有限窗口成立，
不能把该 gauge 的全局恒等式直接赋给原完整特征零来源。

本篇没有证明 $P_2$ 的末系数非零；
所以 (7) 是上界，不宣称每个 p 都达到它。

## 3. 直接压缩完整不变量来源

还存在唯一
$$
Q_m(\xi)\in \xi k[\xi],\qquad \deg Q_m\le L,
$$
使
$$
\boxed{\quad
\mathcal A_m^{\rm dir}=Q_m(\xi)
 =A_m^\circ+O(z^{q+5}),\qquad
(\mathcal A_m^{\rm dir})_\infty\le2L\mathcal D_2.
\quad}
\tag{9}
$$
准确定义是
$$
Q_m(\xi)=
\left[
 wU(w)^m\ell_m(w)
\right]_{w=w(\xi),\,\deg_\xi\le L}.
\tag{10}
$$
(2) 的首因子 w 保证 (10) 只用
$U,\ell_m\bmod w^L$。
在曲线方程下，原完整 $\ell_m$ 只需相同 $X\bmod w^L$；
涉及 y 的单位因子由固定符号
$y=-z^{-3}(X^3+bw)^{1/2}$ 唯一展开，2 为单位。
$\xi$ 的 $L+1$ 次从 $z^{6(L+1)}=z^{q+5}$ 起，
故 (10) 给第一式；$\xi$ 的二挠极阶给第二式。
$q-1=6L$ 这一末条实际行仍被保留。

完整的全局来源类也可明确说明。
任何原 $\mu_6$ 不变、只在 $\mathcal D_2$ 有极、
在 O 正则的有理函数都属于 $k[\xi]$：
它属于不变量域 $k(x^3)=k(\xi)$，
而每一个有限 $\xi$ 值的原像都不允许极，
所以唯一允许的极是 $\xi=\infty$。
其中极帽 $2L\mathcal D_2$ 且在 O 为零的子空间，
恰为 $\xi k[\xi]_{\le L}$。
因此 (9) 是这个明确空间到全部 L 条原型0行的同构。

(9) 的极帽与 m 无关，比 (8) 更小。
不过三个 $Q_m$ 在全局未必来自一个共同平方；
共同关系保证到 $O(z^{q+5})$ 为止。
需要全局共有 $\mathcal S_2$ 时应使用 (8)，
不能把两种模型的各自优点拼成未证明的同一个模型。

## 4. 两种模型均准确读取所有原首 Cartier 行

本节的 $\mathcal A_m$ 可取 (8) 或 (9)。
对 $1\le h\le p-1$ 定义
$$
\Theta_{m,h}
 =\widehat Z^{-h-1}\mathcal A_m\omega_E,\qquad
\rho_{m,h}=\operatorname{Res}_O\Theta_{m,h},
$$
$$
B_{m,h}
 =\frac{\mathscr C(\Theta_{m,h})}{\omega_E}
      -\frac{\rho_{m,h}^{1/p}}{\widehat Z}.
\tag{11}
$$
在 O 输入的极阶至多 $(h-5)_+<p$；
Cartier 后只有实际留数所给的可能简单极，
所以 $B_{m,h}$ 在 O 正则。

令 $t=\widehat Z$。由 $dt=\omega_E$，
若 $\mathcal A_m=\sum a_nt^n$，
则局部 Cartier 选择输入的指数
$n-h-1\equiv-1\bmod p$。
输出的 $t^{h-1}dt$ 项正是 $a_{h(p+1)}^{1/p}$。
(8) 或 (9) 与 (1) 保证
$$
a_{h(p+1)}=[z^{h(p+1)}]A_m^\circ,\qquad
h(p+1)\le q-1.
$$
坐标差 $t-z=O(z^q)$ 乘原来源的首阶6，
只会从 $z^{q+5}$ 起影响它。
故全部原指定条目仍准确为
$$
\boxed{\quad
\bar g_{m,h}
 =\left(\frac{D^{h-1}B_{m,h}(O)}{(h-1)!}\right)^p,
 \qquad 1\le h\le p-1.
\quad}
\tag{12}
$$
全部阶乘是单位，留数是同一 $\Theta_{m,h}$ 的实际留数。

## 5. 新模型必须保留其它零点的极

本篇的 $\mathcal S_2$ 或 $Q_m(\xi)$
未必在 $\widehat Z$ 的其它零点为零。
所以 R721 中由
$\widehat\Sigma=\widehat ZU(\widehat Z^6)$
得到的 $(h+1-m)_+$ 零点节省，不能沿用。

写
$$
C_m=
 \begin{cases}
 mL,&\mathcal A_m=\mathcal A_m^{\rm com},\\
 2L,&\mathcal A_m=\mathcal A_m^{\rm dir}.
 \end{cases}
$$
完整新极帽是
$$
\boxed{\quad
(\Theta_{m,h})_\infty
 \le(h-5)_+O
  +(C_m-(h+1)M_p)_+\mathcal D_2
  +(h+1)(\mathcal Z-O).
\quad}
\tag{13}
$$
在二挠点，$\widehat Z^{-h-1}$ 有
$(h+1)M_p$ 阶零；在其它 $\widehat Z$ 零点，
$\mathcal A_m$ 正则但不预设零；在 O 用原首阶6。
这逐点证明 (13)。

对直接模型，当前 p 范围内
$$
2L=(p^2-1)/3<2M_p\le(h+1)M_p.
$$
所以 (13) 的二挠极项完全消失。
所有余下输入极阶至多 $h+1\le p$。
Cartier 因而至多在 $\mathcal Z$ 有简单极，
减去实际留数项亦不增加极支持。于是
$$
\boxed{\quad
B_{m,h}\in H^0(E,\mathcal O_E(\mathcal Z)),
\qquad
(B_{m,h})_\infty\le\mathcal Z,\quad
B_{m,h}\text{ 在 O 正则}.
\quad}
\tag{14}
$$
$\deg\mathcal Z=3M_p=p(p-2)$。
(14) 的大小仍随 p 二次增长；不是原旧预算 $D$ 的免费来源。

更明确地，对任一 $P\in\mathcal Z$，
以同一个局部参数 $t=\widehat Z$ 写
$$
\rho_{m,h}(P)
 =[t^h]\mathcal A_m(P+t)
 =\frac{D^h\mathcal A_m(P)}{h!}.
\tag{15}
$$
符号 $P+t$ 仅表示该点的 t 局部展开，不是另选群坐标。
(15) 的 h 小于 p，合法使用普通阶乘。
Cartier 在该点的留数是
$\rho_{m,h}(P)^{1/p}$。
这些实际残余不能以“其它点都是额外的”或
“原首行只有 O”删除。

## 6. 直接模型的统一有理分子

仍只取直接模型。定义同一实际有理函数
$$
N_{m,h}
 =\widehat Z\,
      \frac{\mathscr C(\Theta_{m,h})}{\omega_E}.
\tag{16}
$$
由第5节，所有 $\mathcal Z$ 简单极被准确消去；
二挠点处 Cartier 输出正则。
因此
$$
\boxed{\quad
N_{m,h}\in
 H^0(E,\mathcal O_E(M_p\mathcal D_2)).
\quad}
\tag{17}
$$
$\widehat Z$ 是 $k(E)/k(E)^p$ 的 p-基。
在该基上写任何 f 为
$f=\sum_{j=0}^{p-1}f_j^p\widehat Z^j$，
则
$\mathscr C(f\omega_E)=f_{p-1}\omega_E$
且 $D^{p-1}f=-f_{p-1}^p$。
所以 (16) 有无需额外选择的准确定义
$$
\boxed{\quad
N_{m,h}^{\,p}
 =-\widehat Z^pD^{p-1}
          \bigl(\widehat Z^{-h-1}Q_m(\xi)\bigr).
\quad}
\tag{18}
$$
右侧为真实 p 次幂，根在 $k(E)$ 中唯一。
这不是在一个自由 Riemann–Roch 空间重新挑解。

在 $P\in\mathcal Z$，
$$
N_{m,h}(P)=\rho_{m,h}(P)^{1/p}.
\tag{19}
$$
且 (11) 等于
$B_{m,h}=(N_{m,h}-\rho_{m,h}^{1/p})/\widehat Z$。
因此 (12) 也可写成
$$
\boxed{\quad
\bar g_{m,h}
 =\left(\frac{D^hN_{m,h}(O)}{h!}\right)^p.
\quad}
\tag{20}
$$
这给所有 m 共用同一个极帽 $M_p\mathcal D_2$ 的真实分子。

只保 (19) 的有限点值仍不足以替代 (18)：
在 (17) 的空间中，零于全部 $\mathcal Z$ 的函数
恰为 $k\widehat Z$，
因为 $\operatorname{div}(\widehat Z)=\mathcal Z-M_p\mathcal D_2$。
故点值最多确定 $N_{m,h}$ 到 $c\widehat Z$。
这个歧义对应 Cartier 微分的全局正则部分 $c\omega_E$；
本篇始终用 (18) 保留它。
特别 h=1 时它确实影响 (20)，不能以总留数为零删除。

## 7. 当前收益与未付联系

R721 的完整 sigma 代入上界为
$m(q-6)M_p\mathcal D_2$。
(8) 在保共同平方与原 $\phi_m$ 的同时，
将它压到 $mL\mathcal D_2$；
(9) 保全部指定原窗口，把每个完整不变量压到
$2L\mathcal D_2$。
第5、6节同时支付因换模型而重新出现的所有零点留数、
全局正则部分及真实 Cartier 分子。

在 R723 的密度一素数集合上，
两种模型均由原固定 CM/AH 输入唯一恢复。
它们没有给 $\bar g_{m,h}$ 非零，
没有把原 $j_m=0$ 推成 R708 的逐行前缀零，
也没有删去 R710 的原中央 carry。
全 $\Sha[p^\infty]$ 的固定曲线无穷 p 目标继续。

依赖：
[R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)；
[R714](R714-original-height-two-rational-parameter-and-full-first-cartier-window.md)；
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)；
[R721](R721-minimal-two-torsion-poles-for-original-height-two-parameter.md)；
[R723](R723-fixed-cm-and-artin-hasse-full-height-two-reconstruction.md)。


## 8. 只读前 K 条原行时的线性极帽

上文使用整个 $q$ 窗口。若当前只需前 K 条指定 Cartier 行，
不必保留整个参数的二次极帽。令
$$
1\le K\le p-1,\qquad
J_K=\left\lfloor\frac{K+1}{6}\right\rfloor,\qquad
L_K=sK,\qquad M_K=p(2J_K+1).
\tag{21}
$$
R721 的系数 $a_j$ 保持不变，置
$$
h_{[J_K]}=\frac{x^2}{y}\sum_{j=1}^{J_K}a_j\xi^j,
\qquad
Z_{[K]}=Z+c_p^{-1}h_{[J_K]}^p.
\tag{22}
$$
空和为零。因为 $J_K\le s-1$，
全部系数仍由同一个单位递推给定。

R721 的原比较逐行给
$$
H-h_{[J_K]}=O(z^{6J_K+5}).
$$
当 $J_K=s-1$ 时这恰是原 $O(z^p)$，
没有把下一条共振系数当作已知单位。
结合原 $Z_1=z+O(z^q)$，得到
$$
\boxed{\quad
DZ_{[K]}=1,\qquad
Z_{[K]}=z+O(z^{p(6J_K+5)}),\qquad
(Z_{[K]})_\infty=M_K\mathcal D_2 .
\quad}
\tag{23}
$$
$J_K=0$ 时最后一式是 R636 的原 Z 在每个二挠点的准确 p 阶极。
$J_K\ge1$ 时，$h_{[J_K]}$ 的末项系数是单位，
在每个二挠点有准确 $2J_K+1$ 阶极；
其 p 次幂的阶严格大于原 Z 的 p 阶，不能相消。
这同时证明 (23) 的完整极支持。

由于
$$
6J_K+5\ge K+1,\qquad
p(6J_K+5)+5>K(p+1),
\tag{24}
$$
这个较短参数仍保前 K 条原对角所需的全部坐标精度。
第二个不等式使用 $K\le p-1$，不是仅作主阶比较。

按 (10) 只截到 $\xi^{L_K}$，定义同一个原输入的
$$
Q_{m,K}(\xi)
 =\left[wU(w)^m\ell_m(w)\right]_{
          w=w(\xi),\,\deg_\xi\le L_K}.
$$
于是
$$
Q_{m,K}(\xi)=A_m^\circ+O(z^{K(p+1)+6}),\qquad
(Q_{m,K})_\infty\le2sK\mathcal D_2.
\tag{25}
$$
只用原 $U,X\bmod w^{sK}$，无新的自由系数。
所有 $h\le K$ 的原 $\bar g_{m,h}$ 由
$$
\Theta^{[K]}_{m,h}
 =Z_{[K]}^{-h-1}Q_{m,K}(\xi)\omega_E
\tag{26}
$$
按 (11)–(12) 同样准确读取；(24) 保证坐标误差严格晚于每个目标行。

实际二挠极也全部消失。确切地，
$K\le6J_K+4$ 给
$$
(p+1)K<6p(2J_K+1),
$$
因为右侧减去 $(p+1)(6J_K+4)$ 为
$6J_K(p-1)+2p-4>0$。
因此
$$
2sK<2M_K\le(h+1)M_K\qquad(h\ge1).
\tag{27}
$$
令 $\mathcal Z_K=(Z_{[K]})_0$；
它仍全为单零，度为 $3M_K$。
(26) 仅在 $\mathcal Z_K$ 有阶至多 $h+1\le p$ 的极。
所以实际有限部及分子满足
$$
\boxed{\quad
(B^{[K]}_{m,h})_\infty\le\mathcal Z_K,\qquad
N^{[K]}_{m,h}
 :=Z_{[K]}\frac{\mathscr C(\Theta^{[K]}_{m,h})}{\omega_E}
 \in H^0(E,\mathcal O_E(M_K\mathcal D_2)).
\quad}
\tag{28}
$$
全部留数仍按 (15)、(19) 保留，且
$$
\boxed{\quad
\bar g_{m,h}
 =\left(\frac{D^hN^{[K]}_{m,h}(O)}{h!}\right)^p
 \qquad(1\le h\le K).
\quad}
\tag{29}
$$

固定 K 时，(28) 的分子极帽为 $O_K(p)$；
K 随 p 增长时为 $O(pK)$。
例如前四条原行都可使用原 Z 和 $M_K=p$；
第五至第十条用 $J_K=1$ 和 $M_K=3p$。
这是准确的有限窗口代价，不把 K 条原行缩成一条中央，
也不向旧 $\mathcal W_D$ 免费增加这些随 p 变化的来源。

## 9. 分子实际上是同一来源的完整 p-基系数

固定上一节的 K，记 $t=Z_{[K]}$ 和
$A=Q_{m,K}(\xi)$。唯一的 p-基分解为
$$
\boxed{\quad
A=\sum_{h=0}^{p-1}\mathcal N_h^p t^h,
\qquad \mathcal N_h\in k(E).
\quad}
\tag{30}
$$
对每个 $0\le h\le p-1$，
$$
\boxed{\quad
\mathcal N_h
 =t\,\frac{\mathscr C(t^{-h-1}A\omega_E)}{\omega_E},
\qquad
\mathcal N_h^p=-t^pD^{p-1}(t^{-h-1}A).
\quad}
\tag{31}
$$
证明只须对 (30) 的每项使用局部 Cartier：
$t^{r-h-1}\omega_E$ 在 $0\le r,h<p$ 内
只有 $r=h$ 能留下，其 Cartier 为 $t^{-1}\omega_E$。
p 次系数按半线性提出，得到第一式；
第二式由第6节的同一 p-基导数公式成立。
所以对 $1\le h\le K$，
$\mathcal N_h=N^{[K]}_{m,h}$。
所有分子来自同一个 A，不能分别选择其全局正则项。

(27) 还使 $1\le h<p$ 的全部 $\mathcal N_h$
都有 $M_K\mathcal D_2$ 极帽；
不过 $h>K$ 的条目是截断模型的系数，
没有被认作原未支付的高行。

$h=0$ 的输入则必须另算。
由 $K\le6J_K+4$、$J_K\le s-1$，
$$
2sK-M_K
 \le p/3+2J_K+4/3
 \le(2p-1)/3<p.
$$
所以它在二挠点的 Cartier 输出最多有简单极，
从而只有完整上界
$$
(\mathcal N_0)_\infty\le(M_K+1)\mathcal D_2.
\tag{32}
$$
不能把 (28) 的较小帽未经检查赋给零号分子。
(30)–(32) 给准确的一体化呈示，
保留零号项和所有 p 次系数；没有产生新的非零结论。
