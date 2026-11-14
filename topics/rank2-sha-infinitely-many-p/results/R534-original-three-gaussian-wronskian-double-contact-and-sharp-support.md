# R534 — 原三 Gaussian 行的双接触 Wronskian 与改进临界支持界

日期：2026-11-14。**状态：已证明。** 本篇使用同一原矩阵的三条 Gaussian 系数行，把 R525 只读第一低轴的支持界加强为
$$
k\ge\{(3/7)^{1/3}-o(1)\}N^{1/3}
$$
于同一真实二次临界序列中；常数不再含第三块比例的分母。
对同一来源的 primitive 模 $p^2$ 右核，有限不等式的左端准确为整个 $L=2s+\ell$。

关键不是把原 Theta ODE 延长到 $t^s$ 之后。先证明一个新的有限零估计：一个多项式及其清分母 ODE 导数若**同时**消到 $T\le3s$，则仍满足原次数界。再由三条实际 Gaussian 行证明 Wronskian 恰好满足这两个高接触条件。原 $t^s$ forcing 乘法向导数的一项被显式估计，未被删掉。

来源始终是显示的同一 $\mathcal B_{\le N}$ 物理矩阵，或同一已付 conductor·$\mathcal B_{\le N}$ 子格的矩阵。没有把任意 $\mathcal A=\mathcal O[S,T,U]$ 呈示中的 primitive 核搬到未经证明饱和的另一呈示。全部 $P_{134}/U_0$、Gaussian charge、两条进位和原首次修正范围均保留。结论仍是实际核的支持必要条件，不是原核不存在、物理像饱和或新的中央非零。

## 1. 同一原低轴和清分母导子

保 R525、R526 的
$$
p=6s-1>83,\qquad k_0=\mathcal O/p\text{ 完美},\qquad
\delta=t\partial_t,\qquad \theta=\overline{\Theta}_{\rm reg},\quad\theta(0)=1.
$$
只使用原低轴已付的
$$
x=\delta\theta/\theta,\qquad
D_0=6(1-t),\qquad
D_0\delta x-(1+2t)x=\frac23t\pmod{t^s}.
\tag{1}
$$
置
$$
c(t)=\frac{1+2t}{D_0},\qquad b(t)=\frac{2t}{3D_0},\qquad
\Delta=\delta x-cx-b\in t^s k_0[[t]],
\tag{2}
$$
以及多项式导子
$$
\mathcal V=D_0t\partial_t+
\left((1+2t)X+\frac23t\right)\partial_X.
\tag{3}
$$
这里可以任取原有限 $\theta\bmod t^s$ 的一个形式单位延拓，并用它定义 $x$。下文的必要接触条件对每个这样的延拓都成立。没有把该延拓认作原高轴，也没有令 $\Delta=0$。

R525 §1 已证明，对每个不可约正 $X$ 次数多项式 $F$，
$$
F\nmid\mathcal VF.
\tag{4}
$$
该证明使用原 $s$ 给出的非零残数及有限可分扩张上的 $D^p=0$，包括 $F_X=0$ 的情形，不需要 $\deg_XF<p$。R525 引理 1 同时给：若
$$
a_F=\deg_tF,\quad b_F=\deg_XF>0,\quad
B_F=b_F(2a_F+1)<s,
$$
则
$$
\operatorname{ord}_tF(t,x(t))\le B_F.
\tag{5}
$$
这是可见有限阶的严格结论：若实际阶至少为 $s$，先以 $T=s$ 应用该引理就矛盾。

## 2. 新的双接触零估计：不延长 ODE

**引理 1。** 设非零 $P(t,X)\in k_0[t,X]$，$\deg_tP=A$、$\deg_XP=B\ge1$。若
$$
1\le T\le3s,\qquad
P(t,x(t))=\mathcal VP(t,x(t))=0\pmod{t^T},
\tag{6}
$$
则
$$
\boxed{T\le2AB+B.}
\tag{7}
$$

**证明。** 反设 $\mathcal B_P=2AB+B<T$。分解
$$
P=q(t)\prod_iF_i^{r_i}
$$
为不同的正 $X$ 次数不可约因子和纯 $t$ 因子。记 $a_i,b_i,B_i=b_i(2a_i+1)$。

先收集所有满足 $B_i<s$ 的因子。由 (5)，其实际阶 $n_i\le B_i<s$。准确的评价链式法则是
$$
(\mathcal VF_i)(t,x)
=D_0\delta\{F_i(t,x)\}-D_0\Delta(F_i)_X(t,x).
\tag{8}
$$
第一项至少有 $n_i$ 阶，第二项至少有 $s$ 阶。因此
$$
(\mathcal VF_i)(t,x)/F_i(t,x)\in k_0[[t]].
\tag{9}
$$
所有 $a_i=0$ 的因子也可以收集进去：若 $F_i(0)\ne0$，其评价为单位，(9) 立即成立，阶为零；若 $F_i(0)=0$，不可约性迫使 $F_i$ 是 $X$ 的非零常数倍，此时 $B_i=1<s$，已经在前一类中。纯 $t$ 因子同样满足
$$
\mathcal Vq/q=D_0\,\delta q/q\in k_0[[t]].
\tag{10}
$$

余下每个因子都有 $a_i\ge1$、$B_i\ge s$。它不能重复。否则 $r_i\ge2$ 给
$$
\begin{aligned}
\mathcal B_P
&\ge 2(r_i a_i)(r_i b_i)+r_i b_i\\
&\ge 2b_i(4a_i+1)
\ge\frac{10}{3}b_i(2a_i+1)
\ge\frac{10}{3}s
>3s\ge T,
\end{aligned}
\tag{11}
$$
与反设矛盾。倒数第二个比较只用 $a_i\ge1$。

于是可写 $P=QR$，其中 $Q$ 是上述已经收集的部分，$R$ 为余下不同因子的乘积。$Q(t,x)$ 的实际阶 $n_Q$ 有限，满足
$$
n_Q\le \deg q+\sum_{F_i\mid Q}r_iB_i\le\mathcal B_P<T,\qquad
(\mathcal VQ)(t,x)/Q(t,x)\in k_0[[t]].
\tag{12}
$$
若 $R=1$，(6) 已与 (12) 矛盾。否则令 $A_R=\deg_tR$、$B_R=\deg_XR$。由 (4) 及 $R$ 无重复因子，
$$
\gcd_{k_0(t)[X]}(R,\mathcal VR)=1.
$$
由 (6)、(12) 和
$$
\mathcal VP=(\mathcal VQ)R+Q\mathcal VR
$$
得到
$$
R(t,x),\ \mathcal VR(t,x)
\in t^{T-n_Q}k_0[[t]].
\tag{13}
$$
非零 resultant
$$
\operatorname{Res}_X(R,\mathcal VR)
$$
的次数至多 $2A_RB_R+B_R$；其多项式 Bézout 身份使它消到 $T-n_Q$。故
$$
T\le n_Q+2A_RB_R+B_R\le2AB+B.
\tag{14}
$$
最后一个比较由次数可加和
$$
\deg q+\sum r_i(2a_i b_i+b_i)+2A_RB_R+B_R
\le2AB+B
$$
直接得到，纯 $t$ 因子的次数也已计入。这又与反设矛盾，证毕。$\square$

此引理要求两个实际接触，不能只给 $P(t,x)$ 高阶零就使用。式 (11) 正是范围 $T\le3s$ 内可处理重复因子的原因，不需要假定 Wronskian 无重复因子。

## 3. 原多权 jet 与精确法向变分

保原规范化
$$
a(t)=t(t-1)(7+4t+16t^2),\qquad
c_m=\lceil m/68\rceil,\qquad
e_m=\lfloor11m/34\rfloor-4c_m.
\tag{15}
$$
取 $k\ge2$ 个不同非空权
$$
0\le m_1<\cdots<m_k\le N<p
$$
及非零 $f_i\in k_0[t]_{\le e_{m_i}}$。记
$$
A_i=a^{c_{m_i}}f_i=t^{v_i}B_i,\qquad B_i(0)\ne0,
$$
$$
v_i=c_{m_i}+\operatorname{ord}_0f_i,\qquad
\deg B_i=3c_{m_i}+\deg f_i-\operatorname{ord}_0f_i,
$$
$$
g_i=A_i\theta^{m_i},\qquad
F_r=\sum_i m_i^r g_i\quad(r\ge0),\qquad
q=\frac{k(k-1)}2,\qquad
A_\Sigma=\sum_i\deg B_i.
\tag{16}
$$
$B_i$ 在本节表示这些归一多项式，勿与引理 1 中的因子次数界混淆。

在
$$
k_0[t,(1-t)^{-1},X,Y,Y^{-1}]
$$
上定义
$$
E=Y\partial_Y,\qquad
\widehat\delta
=t\partial_t+(cX+b)\partial_X+XE.
\tag{17}
$$
$E$ 与 $\widehat\delta$ 对易，而
$$
[\partial_X,\widehat\delta]=E+c\partial_X.
\tag{18}
$$
对每个与 $X$ 无关的 $F(t,Y)$，由归纳有
$$
\boxed{
\partial_X\widehat\delta^{\,j}F
=\sum_{0\le l<j}\lambda_{j,l}(t)\,
 \widehat\delta^{\,l}(EF),
}
\tag{19}
$$
其中所有 $\lambda_{j,l}\in k_0[t,(1-t)^{-1}]$ 在原点正规。准确递推为
$$
\lambda_{1,0}=1,\qquad
\lambda_{j+1,l}
=\delta\lambda_{j,l}+c\lambda_{j,l}
+\lambda_{j,l-1}+\mathbf1_{l=j},
\tag{20}
$$
缺失指标取零。这里 $\lambda_{j,j-1}=j$；证明无需除以 $j$。

把前 $k$ 个 jet 按 $j=0,\ldots,k-1$ 排成列。令
$$
G_i=\left(
\left.\widehat\delta^{\,j}(A_iY^{m_i})\right|_{X=x,Y=\theta}
\right)_j,\qquad
C_r=\sum_i m_i^rG_i .
\tag{21}
$$
令 $\mathsf L=(\lambda_{j,l})_{j,l}$，它是原点正规的严格下三角矩阵。式 (19) 准确给
$$
\boxed{\partial_XG_i=m_i\mathsf L G_i,\qquad
\partial_X C_r=\mathsf L C_{r+1},}
\tag{22}
$$
其中 $\partial_X$ 在评价之前作用，评价时把 $Y$ 独立固定。它不是对 $\theta(t)$ 作新的来源操作。

因为实际 $\delta x$ 与 (17) 相差 $\Delta\in t^s$，同一归纳给
$$
G_i-(\delta^jg_i)_j\in
t^{s+v_i}k_0[[t]]^k.
\tag{23}
$$
这正是 R525 (16) 的未除 $t^{v_i}$ 版本。特别，若 $F_r=0\bmod t^{h_r}$ 且 $h_r\le s$，则 $C_r$ 的每个分量也消到 $h_r$。不需要知道任何单列到 $t^s$ 后的 ODE 身份。

## 4. 两条、三条 moment 行支付两个高接触

由 R525 的同一多项式递推，
$$
\det(G_1,\ldots,G_k)
=\theta^{\sum m_i}t^{\sum v_i}D_0^{-q}\,
\mathscr W(t,x),
\tag{24}
$$
这是按 (17) 定义的 formal jet 行列式的**准确代数身份**。同一个 $\mathscr W$ 满足
$$
\deg_X\mathscr W=q,\qquad
\deg_t\mathscr W\le A_\Sigma+q,
\tag{25}
$$
$$
[X^q]\mathscr W
=D_0^q\left(\prod_iB_i\right)
 \prod_{i<j}(m_j-m_i)\ne0.
\tag{26}
$$
式 (24) 不声称真实微分 Wronskian 与其在全长相等；两者只按 (23) 比较。

把 $v_i$ 按非降序记为 $v_{(1)},\ldots,v_{(k)}$，并设
$$
F_0,F_1=0\pmod{t^H},\qquad 0\le H\le s.
\tag{27}
$$
若使用第三条，再设
$$
F_2=0\pmod{t^K},\qquad 0\le K\le s.
\tag{28}
$$
$K=0$ 表示没有第三阶消失要求。

选择 $v_i$ 最小的两列或三列，以 $C_0,C_1$ 或 $C_0,C_1,C_2$ 替换，保其余原列。列变换的行列式是这些选中 $m_i$ 的 Vandermonde，因此为非零常数。这里用到 $N<p$，没有借用一般位置。

### 4.1 两条长行

设 $k\ge2$。由 (23)、(27)，新列各消到 $H$，其余列 $G_i$ 各消到 $v_i$。故
$$
\operatorname{ord}\mathscr W(t,x)
\ge T_2:=2H-v_{(1)}-v_{(2)}.
\tag{29}
$$
对这个已经变换的行列式作 $\partial_X$。由 (22)，第一条新列的导数为 $\mathsf L C_1$，仍至少 $H$ 阶；第二条新列的导数为 $\mathsf L C_2$，至少 $v_{\min}$ 阶；未选中列的导数不降低其 $v_i$ 阶。因此
$$
\operatorname{ord}\mathscr W_X(t,x)
\ge H+\min(H,v_{\min})-v_{(1)}-v_{(2)}.
\tag{30}
$$
由 $H\le s$、$\operatorname{ord}\Delta\ge s$ 得
$$
\operatorname{ord}(\Delta\mathscr W_X)(t,x)\ge T_2.
\tag{31}
$$
链式法则
$$
(\mathcal V\mathscr W)(t,x)
=D_0\delta\{\mathscr W(t,x)\}
 -D_0\Delta\mathscr W_X(t,x)
\tag{32}
$$
遂给 $\mathcal V\mathscr W(t,x)$ 也消到 $T_2$。

若 $T_2>0$，其长度至多 $2s$，引理 1 可用；若 $T_2\le0$，以下不等式立即成立。得到
$$
\boxed{
2H\le v_{(1)}+v_{(2)}
+q(2A_\Sigma+2q+1).
}
\tag{33}
$$

### 4.2 三条完整 Gaussian 行

设 $k\ge3$。同理得
$$
\operatorname{ord}\mathscr W(t,x)
\ge T_3:=2H+K-v_{(1)}-v_{(2)}-v_{(3)}.
\tag{34}
$$
对三条新列逐一作法向导数，(22) 的三种实际代价分别为
$$
C_0\longmapsto\mathsf LC_1,\qquad
C_1\longmapsto\mathsf LC_2,\qquad
C_2\longmapsto\mathsf LC_3.
$$
其消失阶至少为 $H,K,v_{\min}$。因此
$$
\operatorname{ord}\mathscr W_X(t,x)\ge
\min(2H+K,\ H+2K,\ 2H+v_{\min})
-\sum_{j=1}^3v_{(j)}.
\tag{35}
$$
第一种不损阶；第二种至多损 $H-K\le s$；第三种至多损 $K-v_{\min}\le s$。故
$$
\boxed{
\operatorname{ord}(\Delta\mathscr W_X)(t,x)\ge T_3.
}
\tag{36}
$$
由 (32)，$\mathscr W$ 与 $\mathcal V\mathscr W$ 同时消到 $T_3$。由于 $T_3\le3s$，引理 1 得
$$
\boxed{
2H+K\le v_{(1)}+v_{(2)}+v_{(3)}
+q(2A_\Sigma+2q+1).
}
\tag{37}
$$

式 (36) 是跨 $s$ 所需的新项。只用 R525 (20) 的模 $t^s$ 行列式身份，只能读取 $\min(T_3,s)$；那样不能得到 (37)。本节同时支付高接触和 forcing 乘法向导数的高接触，因而没有这个精度跳步。

## 5. 同一原 M 的三条行确实给 (27)–(28)

只在 R486、R530 已付的原整窗口和固定坏素数排除下工作。保
$$
\Gamma_+=\mathcal O[t,\epsilon_t]/
(t^s-p\epsilon_t,\epsilon_t^3,t^{\ell_+}\epsilon_t^2),
\qquad0<\ell_+<s.
\tag{38}
$$
不用 conductor 时取 $r_c=C=0$；使用 R473/R486 的已付返回时取
$$
C=10980,\quad r_c=\operatorname{ord}_0q_{\mathfrak c},\quad
d_0=13+r_c.
$$
保 $d_0<s$、$\ell_+>d_0$，并置
$$
H=s-d_0,\qquad K=\ell_+-d_0.
\tag{39}
$$
在通常的原映射 $\Gamma_\ell\to\Gamma_{\ell+d_0}$ 中，准确有 $K=\ell$。如果使用别的已经固定的原目标，则必须按显示的 $\ell_+$ 读取 (39)，不能另添目标行。

对同一
$$
P=\sum_m X_{\rm alg}^m a^{c_m}f_m
$$
，R530 的全列身份为
$$
M(P)=U_*\,t^{d_0}
\sum_m X^m a^{c_m}f_m,
\tag{40}
$$
$$
U_*=c_*U_0(w/t)^{13}X^C q_{\mathfrak c}/t^{r_c},
\qquad
X=\Theta_{\rm reg}\exp(a_0\epsilon/17).
$$
$U_*$ 是整个原三块目标中的共同整单位，保原 $P_{134}$、charge $40$ 及 conductor 的 $C/17$ charge。这里只在该目标取其逆，不在整个角曲线或来源环中除它。

采用 $\epsilon_t=(t/w)^s\epsilon$，令
$$
\gamma(t)=\overline{(a_0/17)(w/t)^s}\in k_0[[t]]^\times.
$$
原三块模 $p$ 的完整表达准确为
$$
\overline{U_*}^{-1}\bar M(P)
=t^{d_0}
\left(F_0+\gamma\epsilon_t F_1
+\frac{\gamma^2}{2}\epsilon_t^2F_2\right).
\tag{41}
$$
$\gamma$ 在三块所需长度均为单位。故同一原首核给
$$
\boxed{
\bar M(P)=0
\ \Longrightarrow\
F_0,F_1=0\bmod t^{s-d_0},\qquad
F_2=0\bmod t^{\ell_+-d_0}.
}
\tag{42}
$$
这不是从第一低轴猜出的额外条件，而是三块全部 Gaussian 系数的实际读法。完整单位必须先共同取逆；如果把它拆开后只留某个低项，(41) 不成立。

令
$$
C_N=\lceil N/68\rceil,\qquad
E_N=\max_{m\le N,\ e_m\ge0}e_m.
$$
若 $N=68u+r$、$0\le r<68$，
$$
E_N=18u+\max(0,\lfloor11r/34\rfloor-4).
\tag{43}
$$
原系数帽给
$$
v_i\le C_N+E_N,\qquad
A_\Sigma\le k(3C_N+E_N).
\tag{44}
$$
因此每个有 $k\ge3$ 个非零约化权的真实首核都满足
$$
\boxed{
2(s-d_0)+(\ell_+-d_0)
\le 3(C_N+E_N)+
q\{2k(3C_N+E_N)+2q+1\}.
}
\tag{45}
$$
通常目标 $\ell_+=\ell+d_0$ 时，左端为 $2s+\ell-2d_0$。

相应的两行界为
$$
2(s-d_0)\le2(C_N+E_N)+
q\{2k(3C_N+E_N)+2q+1\}.
\tag{46}
$$
若 $k=1$，首行要求 $H\le C_N+E_N$。若 $k=2$，$F_0,F_1$ 的 $2\times2$ Vandermonde 直接使每个 $g_i$ 消到 $H$，所以也要求 $H\le C_N+E_N$。在本篇临界范围最终 $H>C_N+E_N$，因而 (45) 的 $k\ge3$ 范围自动满足。

另一个有限推论是：若 $H>4E_N+C_N+7$，任取一个非零权 $m_a$，$F_1-m_aF_0$ 有 $k-1$ 个非零权且消到 $H$。R526 的两权排除迫 $k\ge4$。此处只取一条真实已知为零的函数组合，不声称 $(E-m_a)P$ 是完整原核。

## 6. 原模 p² 提升去掉两条 d₀ carry 的损失

在同一实际分解
$$
M=U_*\,m_{d_0}J:
\mathcal B_{\le N}\longrightarrow\Gamma_{\ell+d_0},
\qquad J:\mathcal B_{\le N}\longrightarrow\Gamma_\ell
\tag{47}
$$
中，$m_{d_0}$ 是原整乘 $t^{d_0}$，不是其非整逆。保 $0<d_0<s$、$\ell+d_0<s$。

给 $\Gamma_\ell$ 的合法基按 $n=j+is$ 编号，
$$
e_n=t^j\epsilon_t^i,\qquad
0\le n<2s+\ell .
$$
乘法准确为
$$
m_{d_0}(e_n)
=p^{\lfloor(n+d_0)/s\rfloor-\lfloor n/s\rfloor}
e_{n+d_0}.
\tag{48}
$$
目标下标仍在原 $\Gamma_{\ell+d_0}$ 内。显示的指数只有 $0$ 或 $1$；指数一恰出现于两条原长度 $d_0$ 的进位带。其余是单位因子，外加 $d_0$ 条自由目标行。

若同一来源的 $P_2$ 满足
$$
M(P_2)=0\bmod p^2,
$$
则取完整单位逆后，由 (48) 逐坐标得到
$$
J(P_2)\in p\Gamma_\ell.
$$
所以
$$
\boxed{
\bar P_2\in K_2^{\rm red}(M)
\ \Longrightarrow\ \bar J(\bar P_2)=0.
}
\tag{49}
$$
这里 $K_2^{\rm red}(M)$ 指这份真实矩阵的模 $p^2$ 右核约化；只有其非零、即显示来源中的 primitive 情形才应用支持界。没有把完整第一次提升的充分条件改写为 (49)。

对 (49) 直接用原内层三块，得到 $H=s$、$K=\ell$。因此每个有 $k\ge3$ 个非零约化权的 primitive 模 $p^2$ 右核满足
$$
\boxed{
L=2s+\ell
\le v_{(1)}+v_{(2)}+v_{(3)}
+q(2A_\Sigma+2q+1)
}
\tag{50}
$$
以及
$$
\boxed{
2s+\ell
\le3(C_N+E_N)+
q\{2k(3C_N+E_N)+2q+1\}.
}
\tag{51}
$$
模 $p^3$ 的同一 primitive 右核也须满足 (50)–(51)。原首次修正、低行全部高尾、两条 carry 的进一步同格兼容以及 R481 的第二障碍仍需另行满足。本节只使用了全部进位的必要约化，未删掉这些条件。

## 7. 同一二次临界的加强常数

考虑真实候选序列，$N\to\infty$，固定 conductor 不随 $N,p$ 变化，
$$
\frac{\ell}{s}\longrightarrow\tau\in[0,1],\qquad
2s+\ell=\frac9{68}N^2+o(N^2).
\tag{52}
$$
这里是 R525 的同一个真实来源维数量级，不从维数制造核。保原目标 $\ell+d_0<s$。由 (43)，
$$
C_N+E_N=\frac{19}{68}N+O(1),\qquad
3C_N+E_N=\frac{21}{68}N+O(1).
$$
无论用首核的 (45)，还是实际提升的 (51)，左端均为
$$
\frac9{68}N^2+o(N^2).
$$
若反设 $k\le(c-\varepsilon)N^{1/3}$，其中 $c^3=3/7$，则右端至多
$$
\frac{21}{68}k^3N+o(N^2),
$$
因为 $q=k(k-1)/2$，其余 $O(k^4+k^2N+k^3+N)$ 项均为 $o(N^2)$。常数严格矛盾，故
$$
\boxed{
\liminf\frac{k}{N^{1/3}}\ge(3/7)^{1/3}.
}
\tag{53}
$$
由 $p=6s-1$，等价地
$$
\boxed{
k\ge
\left\{\left(\frac{34(2+\tau)}{147}\right)^{1/6}-o(1)\right\}p^{1/6}.
}
\tag{54}
$$
特别低第三块 $\ell/s\to0$ 时，
$$
\boxed{
k\ge\{(68/147)^{1/6}-o(1)\}p^{1/6}.
}
\tag{55}
$$

式 (53) 中消掉 $2+\tau$ 的分母，是三条真实 Gaussian 行同时进入同一双接触零估计的结果；没有改来源范数、目标长度、conductor 返回或原算术预算。

## 8. 精确范围和未付接口

1. (33)、(37) 保留每条原系数的真实次数和 $t$ 阶；(45)、(51) 只是其累计上界。没有把单个普通行的接触直接数三次。
2. 原 ODE 仅到 $t^s$。跨该长度的证明依赖显示的 $\Delta\mathscr W_X$ 估计和引理 1，两个步骤缺一不可。
3. 所有微分和 formal jet 用于必要零估计，不被冒称同预算的来源连接操作。没有假定 $\mathcal V(\operatorname{im}J)$ 稳定。
4. 规范化来源仍最多有 $O(N)$ 个可用权，(53) 只迫 $N^{1/3}$ 个非零权。它仍未排除全支持真实核，也未直接给非零原 $C_2$、中央导数或无限素数结论。
5. 三个原完整中央条件若要进一步限制这些密支持核，仍须接同一个实际整格及 R479/R481 的完整同一修正。本篇未给任意乘积、微分来源或新观察赋中央零。

依赖：

- [R525：原低轴、多权 Wronskian 及无不变因子证明](R525-original-multiweight-wronskian-and-growing-kernel-support.md)。
- [R526：原 Theta ODE、两权接触界及完整第一块范围](R526-original-theta-logarithmic-zero-bound-and-two-weight-kernel-exclusion.md)。
- [R486：同一分级来源、真实 conductor 与全部物理进位](R486-graded-integral-connection-and-actual-homogeneous-third-kernels.md)。
- [R530：原目标整坐标及同一完整单位共轭](R530-divided-graded-connection-full-integral-gauge-and-mixed-second-precision.md)。
- [R479：原完整 M carry 与同一修正](R479-original-carry-graph-and-two-normal-jets.md)。
- [R481：原第三精度与实际第二障碍](R481-full-third-precision-normal-form-and-common-correction.md)。

本篇是全参数证明；没有新增有限素数扫描，也没有用未执行的代码冒充证书。
