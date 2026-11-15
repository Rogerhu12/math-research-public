# R710 — 原中央的全阶单位核、真实进位与首边界正则补项

日期：2026-11-15。**状态：已证明。主目标仍未完成。**

本篇保持 R663 的同一个原连接、原完整来源 $\mathcal B_m$ 和原算术值 $j_m$。
给出全部阶数的准确读数：第 $i$ 个原边界系数的权，恰为
$(-1)^ii!(mc)^{-i-1}$ 乘一个 $1+p\mathcal O$ 单位。
因此可以保留全部原高尾而作任意精度的有限计算，并把 $j_m=0$
写成一条明确的全阶进位递推。

同时，原首边界余数与正则补项可以准确分开。
正则补项从第二个 $p$ 进位就参与，而不是可以随高度界删除的尾。
在同一真实连接中，若只要求整 forcing 和零初值，
其首边界余数像恰为 $p\mathcal O\oplus\mathcal O^{p-2}$。
最后这个像结论仅标明解析条件的范围；
构造中的可变 forcing **不是**原固定 $\sigma^m\phi_m$ 来源。

## 1. 同一个原连接及定义域

保持
$$
p\equiv5\pmod6,\qquad e=p-1,\quad d=p+1,\quad q=p^2,
\qquad K=\mathbf Q_p(\omega),\quad\mathcal O=\mathcal O_K.
$$
对原 $m=34,72$ 取 R663 的原好素数门；
第三条 $m=136$ 另取 $p>136$，按 R707 第二增补的同源扩展。
以下始终 $p\nmid m$，$v_p$ 在 $K^\times$ 上为整数。

R663 的准确对象为
$$
r_E=p^{-1/e},\qquad Q(W)=W^e-p,\qquad
H(W)=\mathcal H_p(W^e),\qquad
c=[z^{p+1}]\log(\sigma/z),\quad v_p(c)=-1,
$$
$$
a(W)=c+\sum_{j\ge1}a_jW^j,\qquad
k(W)=1+dW\,H'(W)/H(W)=\sum_{t\ge0}k_tW^t.
\tag{1}
$$
尤其 $a_0-c=0$、$k_0=1$。
设
$$
L_m=\partial_W+ma(W),\qquad
\mathcal D_m=(mc)^{-1}\partial_W+(a-c)/c.
\tag{2}
$$

在每个 $p^{-1}<r<r_E$ 的闭盘上，R663 已付
$$
\|\mathcal D_m\|_r<1,\qquad
L_m^{-1}=(mc)^{-1}\sum_{n\ge0}(-\mathcal D_m)^n.
\tag{3}
$$
不同盘上的逆由唯一性相容。
对任意 $B\in\mathcal O[[W]]$ 定义
$$
\mathfrak J_m(B)=\left[L_m^{-1}(kB)\right]_{W=0}.
\tag{4}
$$
(4) 是用同一个原 $a,k$ 定义的辅助线性泛函。
其指定原输入仍为 R663 的 $\mathcal B_m$，准确有
$$
\boxed{j_m=\mathfrak J_m(\mathcal B_m).}
\tag{5}
$$
没有重新选择原 $j_m$，也没有把任意 $B$ 认作算术来源。

## 2. 边界范数如何给每个乘法系数的整数界

R663 的严格闭边界估计是
$$
\|a-c\|_{r_E}<p.
$$
因此每个 $j\ge1$ 满足
$$
v_p(a_j)+j/e>-1.
$$
因为系数估值为整数，
$$
\boxed{
v_p(a_j)\ge-\lceil j/e\rceil,\qquad
v_p(a_j/c)\ge1-\lceil j/e\rceil.
}
\tag{6}
$$
这里不能把严格不等式换成一个不正确的逐系数整性断言。
例如大 $j$ 的 $a_j$ 仍可有分母。

还需控制 $k$。
在每个闭 $r<r_E$ 盘上，$H$ 无零，$H(0)=1$，
且 $H,H^{-1}$ 都是 Tate 元。
Tate 单位的常数项严格主导，故
$$
\|H\|_r=\|H^{-1}\|_r=1,\qquad
\|WH'\|_r\le1,\qquad \|k\|_r\le1.
$$
也可由一变量 Newton 多边形的零点判据得到同一个单位结论。
让 $r$ 从内侧趋于 $r_E$，得
$$
\boxed{v_p(k_t)\ge-\lfloor t/e\rfloor\quad(t\ge0).}
\tag{7}
$$
本篇不假定 $k$ 在首边界无极。
事实上它仍有 R663 的全部 $Q$ 极；
(7) 正保留这些极对应的分母。

## 3. 非交换词的准确估值与 $i!$ 整除

令
$$
J_{m,i}=\mathfrak J_m(W^i)\qquad(i\ge0).
$$
展开 (3)，并在每个乘法项中展开 (1)。
一个可能贡献常数的词，先取 $k_tW^{i+t}$，
再使用 $s$ 个正次数乘法项
$$
(a_{j_1}/c)W^{j_1},\ldots,(a_{j_s}/c)W^{j_s},
\qquad j_\nu\ge1.
$$
设该词含 $r$ 个导数因子 $(mc)^{-1}\partial_W$。
次数守恒强制
$$
r=i+t+\sum_{\nu=1}^s j_\nu.
\tag{8}
$$
不满足 (8) 或中途被导数杀掉的词，常数贡献为零。

### 3.1 每个非零词都含 $i!$

暂时只保这个词中的 $\partial_W$ 与单项式乘法 $M_{W^j}$，
把所有标量系数提出。
用
$$
\partial_W M_{W^j}
 =M_{W^j}\partial_W+jM_{W^{j-1}}
$$
把它正规排序，得到整数线性组合
$$
\sum_{u,v\ge0}n_{u,v}W^u\partial_W^v,\qquad n_{u,v}\in\mathbf Z.
$$
作用于 $W^i$ 后取常数，只有 $u=0,v=i$ 能留下：
若 $v>i$，导数为零；若 $v\le i$，常数条件 $u+i-v=0$
迫 $u=0,v=i$。
所以每个原词的整数系数都被 $i!$ 整除。
这是对每一个非交换词的结论，不依赖不同词之间的相消。

### 3.2 保留全部乘法分母后的权重

由 (6)–(8)，包含外部 $(mc)^{-1}$ 后，该词估值至少为
$$
\begin{aligned}
&v_p(i!)+1+r+
 \sum_{\nu=1}^s(1-\lceil j_\nu/e\rceil)-\lfloor t/e\rfloor\\
&\qquad=i+1+v_p(i!)+
 \left(t-\lfloor t/e\rfloor\right)+
 \sum_{\nu=1}^s\left(j_\nu+1-\lceil j_\nu/e\rceil\right).
\end{aligned}
\tag{9}
$$
记最后两个和为 $\Delta$。
除 $t=0,s=0$ 外，$\Delta\ge1$。
而 $t=0,s=0$ 时，唯一能取常数的词是 $i$ 次导数，
其准确贡献为
$$
(-1)^ii!(mc)^{-i-1}.
\tag{10}
$$

### 3.3 无限词重排确实收敛

这一步不以形式正规排序替代分析收敛。
因为 $e\ge2$，
$$
t-\lfloor t/e\rfloor\ge t/2,
$$
$$
j+1-\lceil j/e\rceil\ge j/2,\qquad
j+1-\lceil j/e\rceil\ge1\quad(j\ge1).
$$
所以
$$
\Delta\ge\frac12\left(t+\sum_\nu j_\nu\right),
\qquad \Delta\ge s.
\tag{11}
$$
固定 $i$ 和估值门 $M$ 后，$\Delta<M$ 只允许
$$
t+\sum_\nu j_\nu\le2(M-1),\qquad s\le M-1,
$$
因而由 (8)，导数数目及总词长都有固定有限上界。
这些次数下只有有限个指标和有限种词次序。
所以每个估值门下只有有限项；
全部词构成可任意重排的 $p$ 进收敛族。
它与 (3) 的 Banach 逆展开给出同一个常数，
不是另外选了一个形式解。

## 4. 全部阶数的精确单位核

(9)–(11) 立即给出本篇的全阶结论：
$$
\boxed{
J_{m,i}=(-1)^ii!(mc)^{-i-1}\,\varepsilon_{m,i},
\qquad
\varepsilon_{m,i}\in1+p\mathcal O,
\qquad i\ge0.
}
\tag{12}
$$
特别地，
$$
\boxed{v_p(J_{m,i})=i+1+v_p(i!).}
\tag{13}
$$
这不是只对 $i<p$ 的同余。
当 $i\ge p$ 时，正规排序所付的整个 $v_p(i!)$ 仍保留。

令
$$
\gamma_m=mpc\in\mathcal O^\times.
$$
对任意原整 $B=\sum b_iW^i$，由 (13) 可以重排输入级数与 (3)，得到
$$
\boxed{
\mathfrak J_m(B)=
 \sum_{i\ge0}(-1)^ii!\frac{p^{i+1}}{\gamma_m^{i+1}}
       \varepsilon_{m,i}b_i.
}
\tag{14}
$$
该和绝对 $p$ 进收敛。
尤其对指定的 $\mathcal B_m$，(14) 就是原 $j_m$ 的完整表达。

若截到 $0\le i<H$，则全部未取项满足
$$
\boxed{
\mathfrak J_m(B)-
 \sum_{i=0}^{H-1}b_iJ_{m,i}
 \in p^{H+1+v_p(H!)}\mathcal O
 \qquad(H\ge0).
}
\tag{15}
$$
这是真正的全 $H$ 量词；
没有把 R614 的有限 Gaussian 整窗免费延长。
这里使用的是 R663 已付的整 LT 来源及本篇的完整词权重。

(11) 还给出有限算法。
计算 $\varepsilon_{m,i}\bmod p^M$ 时，只需 $\Delta<M$ 的词，
即 $k_t,a_j$ 的指标不超过 $2(M-1)$，
总词长不超过 $i+3(M-1)$。
相应系数按 (6)–(7) 先作显示的 $p$ 幂整归一，
再取所需有限精度。
因此 (12) 不是依靠未指定无限尾的数值定义。

## 5. 原 $j_m=0$ 的准确全阶进位

以下 $b_i$ 始终为原固定 $\mathcal B_m$ 的准确系数。
设
$$
S_H=\sum_{i=0}^{H-1}b_iJ_{m,i},\qquad S_0=0,
$$
并定义实际商
$$
\mathcal C_H
 =-\frac{\gamma_m^{H+1}}{H!\,p^{H+1}}S_H,
\qquad H\ge0.
\tag{16}
$$
它们由原来源唯一确定；不允许为了使它整而修改低块。

由 (15)，
$$
\boxed{
j_m=0\quad\Longleftrightarrow\quad
\mathcal C_H\in\mathcal O\ \text{对全部 }H\ge0.
}
\tag{17}
$$
反向因为整性使 $S_H\to0$，而 (15) 又使 $S_H\to j_m$。

全部实际商满足准确递推
$$
\boxed{
\mathcal C_{H+1}
 =\frac{\gamma_m}{p(H+1)}
   \left(\mathcal C_H-(-1)^H\varepsilon_{m,H}b_H\right).
}
\tag{18}
$$
所以在原 $j_m=0$ 假设下，
$$
\boxed{
\mathcal C_H\equiv
 (-1)^H\varepsilon_{m,H}b_H
 \pmod{p^{\,1+v_p(H+1)}}.
}
\tag{19}
$$
例如 $H=p-1$ 的下一跳必须保两位。
(19) 没有令 $b_H$ 单独为零；
右侧所等的 $\mathcal C_H$ 是全部较低原块形成的真实商。

R663 的 $H(W)=1+O(W^e)$ 还使
$$
b_{m,i}=g^{\rm c}_{m,i+1}\qquad(0\le i<e)
\tag{20}
$$
准确成立，不仅模 $p$。
因此 R708 的短 prefix 正是这些原完整中央系数。
但 (17)–(19) 没有把它们变成逐行零。

## 6. 原首边界余数与正则 forcing 的准确分离

对指定 $\mathcal B_m$ 作 R663 的完整除法
$$
\mathcal B_m=R_m+Q\,C_m,\qquad
R_m=\sum_{i=0}^{e-1}r_{m,i}W^i,
\tag{21}
$$
其中为免与算术 $j_m$ 的正规解混淆，
本节 $R_m$ 只表示这个有限余数多项式。
全部系数准确为
$$
r_{m,i}=\sum_{k\ge0}p^k b_{m,i+ek},
\qquad
[W^n]C_m=\sum_{k\ge1}p^{k-1}b_{m,n+ek}.
\tag{22}
$$
两式保留原全部尾，且 $C_m\in\mathcal O[[W]]$。

R663 写
$$
H=(1-W^e/p)U,\qquad
k=k_{\rm reg}+\frac{de\,p}{Q},
\qquad
k_{\rm reg}=q+dW\,U'/U.
\tag{23}
$$
$U^{\pm1}$、$k_{\rm reg}$ 在某个闭 $r_+>r_E$ 盘 Tate。
因此完整 forcing 恰为
$$
\boxed{
k\mathcal B_m
 =F_{m,\rm reg}+
    de\,p\,\frac{R_m}{Q},\qquad
F_{m,\rm reg}=k_{\rm reg}\mathcal B_m+de\,p\,C_m.
}
\tag{24}
$$
$F_{m,\rm reg}$ 确在该外侧闭盘解析，
而不是把 $k$ 的极省掉之后任选的一个修正。

令
$$
Y_{m,\rm reg}=L_m^{-1}F_{m,\rm reg},\qquad
Z_{m,i}=L_m^{-1}(W^i/Q)
$$
分别在真实外侧盘和严格内侧盘取 R663 的同一逆。
于是原解和原初值严格分成
$$
\boxed{
Y_m=Y_{m,\rm reg}+de\,p\sum_{i<e}r_{m,i}Z_{m,i},
\qquad
j_m=Y_{m,\rm reg}(0)+de\,p\sum_{i<e}r_{m,i}Z_{m,i}(0).
}
\tag{25}
$$

$Z_{m,0},\ldots,Z_{m,e-1}$ 模外侧 Tate 函数线性独立：
若其线性组合延过边界，应用 $L_m$ 并乘 $Q$，
在 $Q$ 的每个根评价，就迫次数 $<e$ 的对应余数多项式为零。
所以 (25) 保留全部 $e$ 个真实边界缺陷；
求原点值不会自动杀掉它们。

### 第一个正则补项

令 $\ell_m(F)=[L_m^{-1}F]_0$。
不带 $k$ 时，第3节同样给
$$
\ell_m(W^i)=(-1)^ii!(mc)^{-i-1}(1+p\mathcal O).
$$
由 (23)–(24) 的低系数或 (22)、(25) 直接得到
$$
\boxed{
Y_{m,\rm reg}(0)
 \equiv-\frac{p^2}{\gamma_m}[W^0]C_m\pmod{p^3},
\qquad
[W^0]C_m\equiv b_{m,e}\pmod p.
}
\tag{26}
$$
证明时 $k_{\rm reg}$ 的常数是 $q=p^2$，
其其余项从 $W^e$ 起。
高项按 (7)、第3节的导数词估值至少在 $p^3$；
$de\,p\equiv-p\bmod p^3$，
只有 $C_m$ 的常数给 (26) 的最低项。

若 $j_m=0$，第一进位先给 $r_{m,0}\in p\mathcal O$。
此时 (25) 的下一位准确为
$$
\boxed{
\frac{r_{m,0}}p
 \equiv b_{m,e}+\frac{r_{m,1}}{\gamma_m}\pmod p.
}
\tag{27}
$$
这里 (26) 的正则项与首边界余数都真实参与。
没有将 $r_{m,0}/p$、$b_{m,e}$ 或 $r_{m,1}$ 预置为零。

## 7. $b_{m,e}$ 正是实际第一 Frobenius 交界

R663 的首 LT 对数系数为
$$
h_e=[W^e]H(W)=\frac1{p^q-p}.
$$
在同一原身份
$$
G_{m,{\rm c},0}(WH^d)=WH^m\mathcal B_m(W)
$$
比较 $W^{e+1}=W^p$，精确得到
$$
\boxed{
b_{m,e}
 =g^{\rm c}_{m,p}+(d-m)h_e\,a_{m,1},
\qquad
a_{m,1}=b_{m,0}=g^{\rm c}_{m,1}.
}
\tag{28}
$$
只用最高极或仅用 $a_{m,1}\bmod p$ 不能计算这个整系数。
其两项分别可能有 $p$ 分母，整性由原同一来源支付。
准确有 $h_e+1/p\in p^{q-2}\mathcal O$，所以 (28) 的补项为
$(m-d)a_{m,1}/p$，不是可以丢掉的高阶项。
R616/R619 的原坏带与 full $F_{\rm c}$ 剪切正应在这里共同使用。

(28) 是原输入的恒等，不允许将 $g^{\rm c}_{m,p}$ 换成任选提升。
它将 (26) 中最先出现的正则补项直接标回原 Frobenius 块。

## 8. 形式余数满像：精确说明解析条件的边界

本节固定同一个原 $a,k,m$，只考察 (4) 在整 forcing 上的作用。
它不增加原算术来源，不修改指定的 $\mathcal B_m$。

由 (12)，
$$
v_p\mathfrak J_m(1)=1,\qquad
v_p\mathfrak J_m(W^e)=e+1=p.
$$
因此
$$
\boxed{
\mathfrak J_m(Q)
 =J_{m,e}-pJ_{m,0}\in p^2\mathcal O^\times.
}
\tag{29}
$$
对任何 $B\in\mathcal O[[W]]$，
$\mathfrak J_m(B)=0$ 由 (14) 模 $p^2$ 迫 $b_0\in p\mathcal O$；
其 $Q$ 余数的常数 $r_0\equiv b_0\bmod p$ 也在 $p\mathcal O$。

反之，给任意
$$
R(W)=\sum_{i<e}r_iW^i,\qquad
r_0\in p\mathcal O,\quad r_i\in\mathcal O\ (i>0),
$$
有 $\mathfrak J_m(R)\in p^2\mathcal O$。
定义
$$
B_R(W)=R(W)-
 \frac{\mathfrak J_m(R)}{\mathfrak J_m(Q)}\,Q(W).
\tag{30}
$$
(29) 支付该比例整，所以 $B_R\in\mathcal O[W]$；
同时
$$
\mathfrak J_m(B_R)=0,\qquad B_R\bmod Q=R.
$$
故准确的整余数像是
$$
\boxed{
\operatorname{rem}_Q
  \bigl(\ker\mathfrak J_m\cap\mathcal O[[W]]\bigr)
 =p\mathcal O\oplus\mathcal O^{e-1}.
}
\tag{31}
$$

(30) 的比例是同连接的真实 $p$ 进值，
但并未证明它是某个固定全局 theta 截面的系数。
本节尤其没有说原 $\phi_m$ 可以这样变动，
也没有给 $B_R$ 原 R696/R707 的全局代数迹及高度。
(31) 的准确含义仅为：
**原连接、整性和零初值本身不足以推出 R708 的逐系数 prefix 消失。**
若要得到该消失，必须另外使用原固定 $\sigma^m\phi_m$
及其实际算术或全局性质。

## 9. 三条原来源的范围及后续接口

对 $m=34,72$，(5)、(12)–(28) 都是原两条来源的同一规范。
对 $m=136$，用 R707 第二增补的原 $P_U$、极130、$p>136$，
同一个 $a,k,H$ 及 $m$ 为单位已经完整支付；
全部公式因此同样适用。

但每个 $m$ 的 (17)–(19)、(27) 都只在其自己的实际 $j_m=0$
假设下使用。原 $j_{34}=j_{72}=0$ 不额外加入 $j_{136}=0$。

本篇的新增内容是全阶单位核、全部原进位和正则补项的准确定位。
它没有把这些进位重命名为独立中央零；
原两条 $j$ 到边界短 prefix 的算术联系仍未完成。

## 依赖

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原 LT 整坐标、同一个完整 $a,k$、严格闭边界范数及真实逆。
- [R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)：
  三条指定原来源、前五块和实际低位商。
- R616：
  原第一坏带；正文 (28) 的证明不依赖该文件的低精度截断。
- R619：原第二坏带及同一 Gaussian/源规范。
- [R707](R707-original-theta-average-and-three-quarter-trace-height.md)：
  原全局迹的高度与第三来源的完整扩展。
- R708：同一原边界的范数判据和真实短 prefix。

本篇为一般证明；无数值检查、素数扫描或新增数据文件。
