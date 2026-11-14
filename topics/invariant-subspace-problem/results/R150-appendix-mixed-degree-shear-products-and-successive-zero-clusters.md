# R150 附录：任意有限次数的剪切乘积、逐层零簇与完整 Bell 核

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf；多尺度零簇递推由根代理与 normal_resume_1cf 分别推导。

状态：完整证明；根代理与 kernel_resume_1cf 已独立核查宏观和局部预算、零簇真实整除以及全部实际深词域。接续[同次数不同最高簇的 Bell 分解](R150-appendix-distinct-leading-clusters-complete-bell-factorization-and-pointwise-products.md)。本文移除各个剪切中心必须具有相同次数的限制，仍对最初普通点态乘积的完整 Bell 图证明，不从各因子循环推出乘积循环。

## 1. 原函数和全部结论

原 $u,v$ 保持[全部高次剪切稿](R150-appendix-all-polynomial-shears-fixed-complex-line-and-higher-companion-parts.md)的范围：
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d^1_j+e^1_j)\chi_j,
\tag{1.1}
$$
其中
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,
$$
$d^\nu$ 在 $a=0$ 位为零、$\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty$，$e^\nu\in\ell^1(\mathbb C)$，其余常数与 $\psi$ 任意。

取有限多个标量多项式 $\Psi_i$，次数分别为
$$
k_i\ge2,\qquad
\Psi_i(x)=\kappa_i x^{k_i}+\text{低次项},\qquad\kappa_i\ne0.
$$
对每个 $i$，令 $G_i(x,s)$ 关于 $s$ 首一、次数 $m_i\ge1$，并满足
$$
\boxed{
p+(k_i-1)q\le(k_i-1)m_i
\quad([x^ps^q]G_i\ne0).
}
\tag{1.2}
$$
允许各 $k_i$ 不同，允许相同次数内有任意重复的最高系数，允许全部最高边碰撞。

置
$$
F(x,y)=\prod_{i=1}^{n}G_i(x,y-\Psi_i(x)).
\tag{1.3}
$$

**定理。** 对每个 $\lambda\in\mathbb C$、整数 $r\ge1$ 和任意复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.4}
$$

若两个因子的 $(k_i,\kappa_i)$ 相同，可先合并。选定其中一个 $\Psi$，其余 $\Psi-\Psi_i$ 的次数至多 $k_i-1$，所以
$G_i(x,s+\Psi-\Psi_i)$ 保持 (1.2)；乘积仍首一。以下因而假设所有对 $(k_i,\kappa_i)$ 不同。

## 2. 实际算子和已经证明的自然排核

取同一实际
$$
Z=X_{a+d^0}+\omega,\qquad
L=Z^{-1}\in\mathfrak C=A',\qquad
Y=e^{i\psi}X_b.
\tag{2.1}
$$
$L$ 有界、单射、拟幂零，$\mathfrak C$ 是交换的范数闭有界算子代数。

对每个 $k\ge2,\kappa\ne0$，令
$$
T_{k,\kappa}=(Y-\kappa Z^k)_{\rm can}L^{k-1}.
\tag{2.2}
$$
[同次数稿 §3](R150-appendix-distinct-leading-clusters-complete-bell-factorization-and-pointwise-products.md)已准确归约到全部高次剪切稿，给
$$
\boxed{
\ker\left(T_{k,\kappa}^{d}+\sum_{j<d}B_jT_{k,\kappa}^{j}\right)
=\{0\},\qquad B_j\in\mathfrak C,
}
\tag{2.3}
$$
定义域为真实自然 $\operatorname{Dom}T_{k,\kappa}^{d}$。全部有界系数都允许，不需要有限谱。

在共同深词域上，
$$
T_{k,\kappa}=YL^{k-1}-\kappa Z,\qquad
YL^k=\kappa I+LT_{k,\kappa}.
\tag{2.4}
$$
后面每次应用 (2.3) 都先支付这些自然幂的输入域。

固定 $\lambda,r,w$，记
$$
d_i=r m_i,\qquad D=\sum_i d_i,\qquad K=\max_i k_i.
$$
先对原完整 $[F(x,y)-\lambda]^r$ 构造全部联合 Bell 项，再按真实域等式
$$
x_{\rm old}=Z+H,\qquad
y_{\rm old}=Y+RZ+K_0,\qquad H,R,K_0\in\mathfrak C
\tag{2.5}
$$
换到 $Z,Y$。记所得有限核心多项式为 $P(x,y)\in\mathfrak C[x,y]$。它关于 $y$ 首一、次数为 $D$，代表原规范 Bell 图 $\mathcal P$ 在共同自然深域上的作用。

这里 $K_0$ 是有界算子，区别于最高次数 $K$。原 Bell 系数、全部混合 cumulant 和原复倾斜均保留。

## 3. 两类有限 Newton 预算都对完整 Bell 保持

### 3.1 每个宏观次数的预算

对任意整数 $k\ge2$，定义
$$
M_k=\sum_i d_i\max(k_i,k).
\tag{3.1}
$$
先看一个原因子 $G_i(x,y-\Psi_i(x))$。赋权
$\operatorname{wt}x=1,\operatorname{wt}y=k$。由 (1.2)，每个单项式的权至多
$$
(k_i-1)m_i+
\bigl(\max(k_i,k)-k_i+1\bigr)q
\le m_i\max(k_i,k).
$$
所以原乘积的 $r$ 次幂及其常数移位的 $r$ 次幂权都不超过 $M_k$。

正阶 Bell 微分严格降低这个权；(2.5) 的有界 $x$ 平移和 $y\mapsto y+Rx+K_0$ 也不增加权。因此
$$
\boxed{
\widehat P_k(t,s)
=t^{M_k}P(t^{-1},t^{-k}s)\in\mathfrak C[t,s].
}
\tag{3.2}
$$
当 $k$ 取某个实际次数 $k_i$ 时，准确最高符号为
$$
\boxed{
\widehat P_k(0,s)
=C_{>k}\,
s^{D_{<k}}
\prod_{k_i=k}(s-\kappa_i)^{d_i},
}
\tag{3.3}
$$
其中
$$
C_{>k}=\prod_{k_i>k}(-\kappa_i)^{d_i}\ne0,
\qquad D_{<k}=\sum_{k_i<k}d_i.
$$
最高符号是准确标量乘 $I$。因为各最高微分和平移修正都严格降权，没有额外零字符高项被略去。

在最大次数 $K$，$M_K=KD$，且 $\widehat P_K$ 关于 $s$ 首一、次数为 $D$。在较低尺度 $\widehat P_k$ 通常不首一；不能直接把它当作新的首一规范算子。

### 3.2 每条曲线自身的局部预算

固定簇 $i$，令
$$
B_i=d_i(k_i-1)+\sum_{j\ne i}d_j\max(k_i,k_j)
=M_{k_i}-d_i.
\tag{3.4}
$$
在
$$
x=t^{-1},\qquad
y=\kappa_i t^{-k_i}+t^{-(k_i-1)}z
$$
处，自身因子由 (1.2) 只有负阶 $m_i(k_i-1)$。其他因子的负阶不超过
$m_j\max(k_i,k_j)$。相同 $(k,\kappa)$ 已合并，所以该数也与实际其余最高中心相容。

因此，对原 $[F-\lambda]^r$，
$$
t^{B_i}[F(t^{-1},
\kappa_i t^{-k_i}+t^{-(k_i-1)}z)-\lambda]^r
$$
是多项式。这里 $B_i=r[m_i(k_i-1)+\sum_{j\ne i}m_j\max(k_i,k_j)]$，常数 $\lambda$ 不破坏非负次幂。

这个局部解析性对全部原 Bell 及 (2.5) 仍成立。准确核查如下：对固定 $N=B_i,k=k_i,\kappa=\kappa_i$ 记
$$
\mathcal T_NJ
=t^N J(t^{-1},\kappa t^{-k}+t^{-(k-1)}z).
$$
则
$$
\mathcal T_N(\partial_xJ)
=\bigl[Nt-t^2\partial_t-((k-1)tz+k\kappa)\partial_z\bigr]\mathcal T_NJ,
$$
$$
\mathcal T_N(\partial_yJ)=t^{k-1}\partial_z\mathcal T_NJ.
\tag{3.5}
$$
右侧都保持真正的非负 $t$ 次数。对有界平移作有限 Taylor 展开，$y$ 平移项准确合成为
$$
(Rt^{k-2}+K_0t^{k-1})^q,
$$
也没有负幂。因此最终实际核心 $P$ 满足
$$
\boxed{
J_i(t,z):=
t^{B_i}P(t^{-1},
\kappa_i t^{-k_i}+t^{-(k_i-1)}z)
\in\mathfrak C[t,z].
}
\tag{3.6}
$$
结合 (3.2)、(3.4)，
$$
\boxed{
\widehat P_{k_i}(t,\kappa_i+t z)=t^{d_i}J_i(t,z).
}
\tag{3.7}
$$

## 4. 逐层分簇的解析不变量

把实际不同次数按严格降序写成
$$
K=k^{(1)}>k^{(2)}>\cdots>k^{(s)}\ge2.
$$
以下所有解析式都在某个足够小的原点圆盘上成立。层数有限，可每次缩小圆盘，最后取一个共同圆盘。

对当前层 $k$，将构造
$$
\boxed{
\widehat P_k(t,s)=U_{>k}(t,s)\,Q_k(t,s),
}
\tag{4.1}
$$
满足：

- $Q_k$ 是解析 $\mathfrak C$ 系数的首一 $s$ 多项式，次数
  $D_{\le k}=\sum_{k_i\le k}d_i$；
- $U_{>k}$ 也是有限 $s$ 多项式、其系数关于 $t$ 解析，并且
  $$U_{>k}(0,s)=C_{>k}I;$$
- 准确有
  $$
  Q_k(0,s)=s^{D_{<k}}\prod_{k_i=k}(s-\kappa_i)^{d_i}.
  \tag{4.2}
  $$

最高层取
$$
Q_K=\widehat P_K,\qquad U_{>K}=I,
$$
故 (4.1)—(4.2) 起初成立。

使用同次数稿 §5 的有限系数固定点分解，将 (4.2) 中的各不同根分开：
$$
\boxed{
Q_k(t,s)=
\left(\prod_{k_i=k}P_i(t,s)\right)R_k(t,s),
}
\tag{4.3}
$$
其中
$$
P_i(0,s)=(s-\kappa_i)^{d_i},\quad \deg_sP_i=d_i,
$$
而在 $D_{<k}>0$ 时，
$$
R_k(0,s)=s^{D_{<k}},\quad \deg_sR_k=D_{<k}.
$$
所有因子首一；若 $D_{<k}=0$，约定 $R_k=1$。

这个代数分解允许一个根为0：固定点构造只用不同标量根之间的互素，不要求每个根非零。自然排核 (2.3) 则仍只用于各非零 $\kappa_i$。

### 4.1 非零簇的局部首一式

将 (4.1)、(4.3) 代入 $s=\kappa_i+t z$。$U_{>k}$ 在 $t=0$ 为非零标量；其他同层因子及 $R_k$ 在该点也都是非零标量单位。由 (3.7)，在形式环 $\mathfrak C[z][[t]]$ 中，
$$
t^{d_i}\mid P_i(t,\kappa_i+t z).
$$
于是
$$
\boxed{
q_i(t,z)=t^{-d_i}P_i(t,\kappa_i+t z)
}
\tag{4.4}
$$
是解析系数首一 $z$ 多项式，次数 $d_i$。所有除法已在解析系数中完成。

### 4.2 零簇到下一次数的准确归一

若还有下一层 $k'<k$，它们之间没有新的实际次数。令
$$
h=k-k',\qquad D_0=D_{<k}=D_{\le k'}>0.
$$
由 (3.1) 准确有
$$
M_k-M_{k'}=hD_0.
\tag{4.5}
$$
因此
$$
\widehat P_k(t,t^h u)=t^{hD_0}\widehat P_{k'}(t,u).
\tag{4.6}
$$
另一方面，(4.1)、(4.3) 给
$$
\widehat P_k(t,t^h u)
=
U_{>k}(t,t^h u)
\left(\prod_{k_i=k}P_i(t,t^h u)\right)
R_k(t,t^h u).
\tag{4.7}
$$
(4.7) 的前两个因子之积在 $t=0$ 为
$$
C_{>k}\prod_{k_i=k}(-\kappa_i)^{d_i}I
=C_{>k'}I,
$$
它是与 $u$ 无关的非零标量。因此它在形式环
$\mathfrak C[u][[t]]$ 中有逆。(4.6) 迫
$$
t^{hD_0}\mid R_k(t,t^h u).
$$
由于 $R_k$ 关于 $s$ 只有有限次数，各个 $u$ 系数均为解析函数且具有上述有限零阶，所以
$$
\boxed{
Q_{k'}(t,u)=t^{-hD_0}R_k(t,t^h u)
}
\tag{4.8}
$$
确为解析系数多项式。$R_k$ 首一、次数 $D_0$，其最高项变为
$t^{hD_0}u^{D_0}$；所以 $Q_{k'}$ 仍首一、次数恰为 $D_0$。

置
$$
U_{>k'}(t,u)
=U_{>k}(t,t^h u)\prod_{k_i=k}P_i(t,t^h u).
\tag{4.9}
$$
由 (4.6)—(4.8) 得到新的 (4.1)。在 $t=0$ 用 (3.3) 与
$U_{>k'}(0,u)=C_{>k'}I$，得到新的 (4.2)。归纳不变量完整成立。

注意：这里用到的形式单位只用于证明有限系数的消失阶。后面绝不要求未知无界 $U_{>k}[L](YL^k)$ 有逆，也不会在实际核上消去它。

## 5. 有界系数代入及有限 Bézout 分核

所有解析系数都只代入有界拟幂零 $L$。若
$$
C(t)=\sum_{n\ge0}C_nt^n,\qquad C_n\in\mathfrak C,
$$
则
$$
C[L]=\sum_{n\ge0}C_nL^n
$$
在算子范数中绝对收敛。它是代数同态，且极限仍属于 $\mathfrak C$，保持每个真实 first 和全部有限混合词域。完整论证见同次数稿 §6。

对每一层 (4.3)，有限 Sylvester 矩阵在 $t=0$ 为标量单位，故有解析有限 Bézout 系数。包括 $R_k$ 时，令 $\mathcal F_k$ 为全部 $P_i$ 与 $R_k$ 的集合；没有低层时只含 $P_i$。可取
$$
\deg_sE_F<\deg_sF
$$
使
$$
\boxed{
\sum_{F\in\mathcal F_k}
E_F(t,s)\prod_{\substack{G\in\mathcal F_k\\G\ne F}}G(t,s)=1.
}
\tag{5.1}
$$
每个分核多项式的总 $s$ 次数至多 $D_{\le k}-1\le D-1$。

代入 $t=L$ 后仍是有限 $\mathfrak C[s]$ 恒等式。特别，(4.4)、(4.8) 给
$$
\boxed{
P_i[L](\kappa_i I+Lz)=L^{d_i}q_i[L](z),
}
\tag{5.2}
$$
$$
\boxed{
R_k[L](L^h u)=L^{hD_0}Q_{k'}[L](u).
}
\tag{5.3}
$$
没有任何负次 $L$。

## 6. 原规范核的真实逐层运输

假设原规范最大 Bell 算子有
$$
0\ne f\in\ker\mathcal P.
$$
把全部原倾斜 first 以及 $Z,Y$ 同时纳入一个有限族，取同一个 R186 单射共同正则器
$\mathcal R\in\mathfrak C$。选一个充分大的有限
$$
N\ge K(3D+2),
$$
必要时按原有限族的具体展开再增加固定深度，使
$$
v_0=\mathcal R^Nf\ne0
\tag{6.1}
$$
进入全部所需长度不超过 $N$ 的真实混合词域。原图交换性给
$$
P(Z,Y)v_0=\mathcal Pv_0=0.
$$

在深域中记
$$
S_k=YL^k.
$$
最高层准确有
$$
Q_K[L](S_K)v_0
=\widehat P_K[L](S_K)v_0
=L^{KD}P(Z,Y)v_0=0.
\tag{6.2}
$$

下面证明：若在某层
$$
Q_k[L](S_k)v_0=0,
\tag{6.3}
$$
则所有该层非零中心的分量为零；如有低层，则同一个原向量 $v_0$ 满足下一层的核方程。

把 (5.1) 在 $S_k$ 上作用于 $v_0$，得到有限分解
$$
v_0=\sum_{F\in\mathcal F_k}v_F,\qquad
v_F=E_F[L](S_k)
\prod_{\substack{G\in\mathcal F_k\\G\ne F}}G[L](S_k)v_0,
\tag{6.4}
$$
以及
$$
F[L](S_k)v_F=0.
\tag{6.5}
$$
所有这些运算均为有限 $S_k$ 多项式，度数界见 §5。

对非零中心因子 $F=P_i$，(2.4)、(5.2) 在已付域上给
$$
0=P_i[L](S_k)v_{P_i}
=L^{d_i}q_i[L](T_{k_i,\kappa_i})v_{P_i}.
$$
$L$ 单射且 $q_i[L]$ 首一，因此自然排核 (2.3) 给
$$
v_{P_i}=0.
\tag{6.6}
$$

若没有低层，(6.4) 已给 $v_0=0$，与 (6.1) 矛盾。若有低层，则 (6.4)、(6.6) 给
$$
v_0=v_{R_k},\qquad R_k[L](S_k)v_0=0.
\tag{6.7}
$$
注意这里剩下的向量准确还是最初 $v_0$，所以它继续保有 (6.1) 的全部原深域，而不是只知道某个较浅分量的域。

因为 $S_k=L^hS_{k'}$，(5.3)、(6.7) 给
$$
0=L^{hD_0}Q_{k'}[L](S_{k'})v_0.
$$
$L$ 单射，故
$$
\boxed{
Q_{k'}[L](S_{k'})v_0=0.
}
\tag{6.8}
$$
这就是准确的下一层核方程。此处只消去了有界单射 $L^{hD_0}$，没有消去未知 $U_{>k}$，也没有假设零中心存在任何 Riesz 谱向量。

### 6.1 全部自然域的统一检查

每层 (6.4) 的多项式次数至多 $D-1$。每次 $S_k=YL^k$ 只消耗一个 first 词长度；全部解析得到的有界系数保持剩余词域。

(6.5) 的有限恒等式至多需要 $2D-1$ 次 $Y$ 作用。对分量再作用
$T_{k_i,\kappa_i}^{d_i}$，总词长度不超过
$$
(D-1)+k_i d_i\le(D-1)+KD.
$$
原 $P(Z,Y)$ 的词长度至多 $KD$。因此 (6.1) 一次选择的 $N$ 足以覆盖所有层。

逐次 $T$ 作用先用有界 $L^{k_i-1}$ 保持词域，再用规范
$(Y-\kappa_iZ^{k_i})_{\rm can}$ 在该共同自然域上的准确作用。这逐层支付
$v_{P_i}\in\operatorname{Dom}T_{k_i,\kappa_i}^{d_i}$，没有把整个规范 Bell 域认作自然 $T$ 幂域。

由 (6.7)，每次递推继续使用原向量 $v_0$，所以不会随层数累积一个未经支付的域损失。

## 7. 终止、原循环性及范围

实际次数层数有限，且最小次数仍至少为2。在最后一层没有剩余零簇，因此 §§6—6.1 迫 $v_0=0$，与真实单射正则化矛盾。

故原规范最大 Bell 核为零。原空间上完整 $C$ 自伴性给像稠密，R186 的循环指数图核心给
$$
[\mathcal Pe^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
$\mathcal Pe^w$ 正是原普通点态向量 (1.4)，定理得证。

例如取
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=i\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
\quad 1/2<\sigma\le1.
$$
则对任意复 $\beta,\lambda$、$r\ge1$ 和复权 $w$，
$$
\boxed{
\left[
\bigl((v-u^2)^2-4u^2\bigr)
\bigl((v-u^3)^2-\beta u^4\bigr)-\lambda
\right]^r e^w
\text{ 循环。}
}
$$
包括 $\beta=9$ 时两个不同次数内分别出现的旧真实碰撞。

最高次数归一中的零根在本文中是一个有指定较低次数结构的暂时余簇。它通过 (4.8)、(5.3) 的实际系数整除逐层处理；并非一般零最高簇均已排除。

次数1或没有已知下一非零多项式中心的零簇不由本文覆盖。超过各因子 (1.2) 权界的余项，以及一般不落在固定复直线的复杂辅助骨架，也仍保留。原真正常见证聚合预算、一般慢主理想和普通复 Hilbert ISP 没有因此完成。
