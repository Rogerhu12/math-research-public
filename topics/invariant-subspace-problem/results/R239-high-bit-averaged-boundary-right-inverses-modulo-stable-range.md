# R239：高位实际归一化幂平均：模稳定范围的右逆与缺陷形式原像的三次次数界

日期：2026-11-12（UTC）。独占作者：l2_moments；高位实际幂提升机制与 root 共同核验。

**状态：完整实际算子证明。** 本稿同时适用于负整数边界表示的两个慢符号
$$
T_N=\sum_{j\ge0}(j+1)^{-2}\mathsf N_j,\qquad
T_Y=\sum_{j\ge0}(j+1)^{-2}\mathsf Y_j.
$$
它解决的是 R234 右逆与规范有限三角原像之间的一个模稳定范围接口。
本稿使用新的高位平均右逆；没有宣称 R234 原右逆本身与规范逆之差已经落入稳定范围。
边界 $N=\overline{B\ker T}$ 是否等于 $\ker T$，以及原 Haar 不变子空间问题，仍未解决。

## 1. 空间、已有输入和主结论

在负整数边界空间
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0
$$
中，记
$$
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1}.
\tag{1.1}
$$
这里 $\|\mathsf N_j\|=1$，且 $d_j>0$。
整数 $n$ 的二进制 $1$ 的个数记为 $\nu(n)$。令
$$
\mathcal H_q=\overline{\operatorname{span}}\{e_n:\nu(n)=q\},
\qquad \mathsf P_q:\mathcal H_-\to\mathcal H_q.
\tag{1.2}
$$
这些是边界物理孔次数层，不是 Haar Walsh 次数层。
有限整数支撑向量在每个 $\mathcal H_q$ 中稠密。

固定 $T=T_N$ 或 $T=T_Y$，并记
$$
M=\ker T,\qquad N=\overline{BM},\qquad D=M\ominus N.
\tag{1.3}
$$
因 $T$ 与 $B$ 交换，$M$ 在 $B$ 下不变，所以 $N\subset M$。

以下三个已有输入均是这两个实际边界模型上的结论。

1. R234 给出 Banach 空间
   $$
   \mathscr X=
   \left\{v:\|v\|_{\mathscr X}
   =\sum_{p\ge0}e^{(p+1)^3}\|\mathsf P_pv\|<\infty\right\}
   $$
   和有界线性映射
   $$
   G:\mathscr X\longrightarrow\mathcal H_-,
   \qquad TG=I_{\mathscr X},\qquad \|G\|\le C_G<\infty.
   \tag{1.4}
   $$
   特别，$\|G|_{\mathcal H_p}\|\le C_Ge^{(p+1)^3}$。
   不要求、也不使用 $T:\mathscr X\to\mathscr X$ 有界。
2. R238 给出每层的有界规范右逆
   $$
   J_q:\mathcal H_q\longrightarrow\mathcal H_-,
   \qquad TJ_q=I_{\mathcal H_q}.
   \tag{1.5}
   $$
   对有限支撑 $v$，$J_qv$ 就是满足 $Tz=v$、$z_0=0$ 的唯一有限支撑解。
   对 $f_0=0$，唯一逐行形式解 $T^*h=f$ 满足
   $$
   \mathsf P_qh=J_q^*f.
   \tag{1.6}
   $$
   这里每个右侧都是真正的 Hilbert 向量；尚不要求 $h$ 全局平方可和。
3. R187 的实际有限头修复及其 R188 的 Cayley 版本证明
   $$
   e_0\in N.
   \tag{1.7}
   $$
   第 4 节会从这一事实重新证明本稿所需的
   $M\cap\operatorname{Ran}B^r\subset N$，无需假设 $N=M$。

**定理 1.1。** 给定 $q\ge0$、整数 $r\ge1$，以及任意要求的高位起点，
存在显式有界线性映射
$$
\widetilde G_{q,r}:\mathcal H_q\longrightarrow\mathcal H_-
$$
满足
$$
T\widetilde G_{q,r}=I_{\mathcal H_q},\qquad
\operatorname{Ran}\widetilde G_{q,r}\subset\operatorname{Ran}B^r,
\tag{1.8}
$$
$$
\|\widetilde G_{q,r}\|\le2C_Ge^{(q+2)^3},
\qquad
(\widetilde G_{q,r}-J_q)\mathcal H_q\subset N.
\tag{1.9}
$$
构造所用的所有位可以高于指定起点，而 (1.9) 的常数不依赖这些位或 $r$。

因此，对 $f\in N^\perp$，其唯一形式原像 $T^*h=f$ 满足
$$
\boxed{
\mathsf P_qh=\widetilde G_{q,r}^*f,\qquad
\|\mathsf P_qh\|\le2C_Ge^{(q+2)^3}\|f\|.
}
\tag{1.10}
$$
这里 $f_0=0$ 自动由 (1.7) 成立。尤其 (1.10) 适用于未知缺陷向量 $f\in D$。

## 2. 实际高位幂与纯创建的精确乘积

令 $E_j$ 为第 $j$ 位的纯孔删除：
它把该位的 $1$ 送到 $0$，并杀掉该位为 $0$ 的向量。
令 $E_j^*$ 为纯孔创建，$P_{j,0}$ 为该位为空的正交投影。
于是
$$
E_jE_j^*=P_{j,0},\qquad (E_j^*)^2=0.
$$

在实际负整数表示中，保留全部更高位进位的精确递推是
$$
\mathsf N_j
=E_j+\eta_jE_j^*\mathsf N_{j+1},
\qquad \eta_j=\alpha_{j+1}/\alpha_j.
\tag{2.1}
$$
$\mathsf N_{j+1}$ 只作用于更高位，与 $E_j^*$ 交换。
所以右乘 $E_j^*$ 后，第二项严格为零：
$$
\boxed{\mathsf N_jE_j^*=P_{j,0}.}
\tag{2.2}
$$
这不是把实际 $\mathsf N_j$ 用纯矩阵 $E_j$ 近似所得的等式。
它没有 $\eta_j$ 误差，也不需要输入的高位尾有任何衰减。

此外，$E_j^*$ 把 $\mathcal H_q$ 送入 $\mathcal H_{q+1}$，范数不超过 $1$。
$T$ 是 $B$ 的范数收敛函数，因而
$$
T\mathsf N_j=\mathsf N_jT.
\tag{2.3}
$$
本稿只使用这一交换；不要求 $G$ 与 $\mathsf N_j$ 或 $E_j^*$ 交换。

## 3. 有限高位平均及真实值域控制

取任意有限位集 $F$，令 $n=|F|>q$。
在 $\mathcal H_q$ 上定义
$$
Q_F=\sum_{j\in F}P_{j,0}
=nI-\sum_{j\in F}E_j^*E_j.
\tag{3.1}
$$
一个恰有 $q$ 个孔的基向量，在 $F$ 内至多占据 $q$ 位。因此
$$
(n-q)I_{\mathcal H_q}\le Q_F\le nI_{\mathcal H_q}.
\tag{3.2}
$$
$Q_F$ 保持 $\mathcal H_q$，且其在这一层上的逆满足
$$
\|Q_F^{-1}\|\le(n-q)^{-1}.
\tag{3.3}
$$
这里的逆只定义在 $\mathcal H_q$ 上；无须在整个边界空间中可逆。

定义
$$
\boxed{
\widetilde G_{F,q}
=\sum_{j\in F}\mathsf N_j\,G\,E_j^*Q_F^{-1}
:\mathcal H_q\longrightarrow\mathcal H_-.
}
\tag{3.4}
$$
每个 $E_j^*Q_F^{-1}v$ 属于 $\mathcal H_{q+1}\subset\mathscr X$，
所以 (3.4) 的全部组合都是实际有定义的有界映射。

由 (1.4)、(3.3) 及 $\|\mathsf N_j\|=\|E_j^*\|=1$，
$$
\|\widetilde G_{F,q}\|
\le\frac{n}{n-q}C_Ge^{(q+2)^3}.
\tag{3.5}
$$
利用 (2.2)–(2.3)，
$$
\begin{aligned}
T\widetilde G_{F,q}
&=\sum_{j\in F}\mathsf N_jTG E_j^*Q_F^{-1}\\
&=\sum_{j\in F}\mathsf N_jE_j^*Q_F^{-1}\\
&=Q_FQ_F^{-1}=I_{\mathcal H_q}.
\end{aligned}
\tag{3.6}
$$
特别地，这是有限和给出的精确右逆，不是弱极限中的候选。

给定 $r\ge1$，再要求每个 $j\in F$ 都满足 $2^j\ge r$。
则
$$
\mathsf N_j
=B^r\left(B^{2^j-r}/d_j\right).
$$
因此
$$
\widetilde G_{F,q}
=B^r\left[
\sum_{j\in F}(B^{2^j-r}/d_j)\,G\,E_j^*Q_F^{-1}
\right].
\tag{3.7}
$$
括号是有限个有界映射之和，所以 (3.7) 证明真实的值域包含
$$
\operatorname{Ran}\widetilde G_{F,q}\subset\operatorname{Ran}B^r.
\tag{3.8}
$$
这一步没有以闭包代替值域。
括号的范数可能很大，但本稿不需要控制它；右逆本身的范数仍由 (3.5) 控制。

取 $n=2(q+1)$，便有 $n/(n-q)<2$。
可以把这 $n$ 个位全部移到任意高处，证明 (1.8) 及 (1.9) 的范数部分。

## 4. 核中的实际右移值域落入稳定范围

为完整说明模 $N$ 步骤，先给出一个一般有限旗论证。

记
$$
\mathcal E_r=\operatorname{span}\{e_0,\ldots,e_{r-1}\}
=\ker B^r.
$$
$T_N$ 与 $T_Y$ 的形式首阶都是 $1$，首系数为 $1/d_0\ne0$。
所以它们在有限头上的矩阵严格降低整数指标，并且每个第一超对角元素非零。
因此
$$
T\mathcal E_{r+1}=\mathcal E_r.
\tag{4.1}
$$

若 $x\in M\cap\operatorname{Ran}B^r$，选 $y\in\mathcal H_-$ 使 $x=B^ry$。
由 $Tx=0$ 与交换性，
$$
B^rTy=TB^ry=0,
$$
所以 $Ty\in\mathcal E_r$。由 (4.1) 可选 $z\in\mathcal E_{r+1}$，满足
$Tz=Ty$。于是 $y-z\in M$，且
$$
x=B^r(y-z)+B^rz.
\tag{4.2}
$$
第一项属于 $B^rM\subset BM\subset N$；第二项属于 $\mathbb Ce_0\subset N$。
故
$$
\boxed{M\cap\operatorname{Ran}B^r\subset N\qquad(r\ge1).}
\tag{4.3}
$$
这也给出 R200 所用的代数和
$M\cap\operatorname{Ran}B^r=B^rM+\mathbb Ce_0$。
本稿不需要这个和的唯一性，也不需要关于 $B|_M$ 的有界逆或满射结论。

## 5. 高位平均逆与规范逆在模 $N$ 下相同

固定 $q,r,F$ 如第 3 节。
先取有限支撑 $v\in\mathcal H_q$。
由 R238，$J_qv$ 仍有限支撑；由于所有 $B$ 的权都严格为正，
任何有限支撑向量都属于 $\operatorname{Ran}B^r$。
结合 (3.8)，
$$
\widetilde G_{F,q}v-J_qv\in\operatorname{Ran}B^r.
$$
(1.5)、(3.6) 又给
$$
T(\widetilde G_{F,q}v-J_qv)=0.
$$
由 (4.3)，
$$
\widetilde G_{F,q}v-J_qv\in N.
\tag{5.1}
$$

有限支撑向量在 $\mathcal H_q$ 中稠密。
$\widetilde G_{F,q}$ 和 $J_q$ 都是这一层上的真正有界算子，而 $N$ 闭，
故 (5.1) 延拓到完整的无限位输入层：
$$
\boxed{
(\widetilde G_{F,q}-J_q)\mathcal H_q\subset N.
}
\tag{5.2}
$$
延拓时不需要 $\operatorname{Ran}B^r$ 闭。
我们只把已经得到的 $N$ 包含关系取极限。

等价地，若 $\pi_N:\mathcal H_-\to\mathcal H_-/N$ 为 Hilbert 商映射，则
$$
\pi_N\widetilde G_{F,q}=\pi_NJ_q,\qquad
\|\pi_NJ_q\|\le2C_Ge^{(q+2)^3}.
\tag{5.3}
$$
因此这是规范右逆在商空间中的新范数估计，而非它在整个 $\mathcal H_-$ 中的范数估计。

## 6. 缺陷形式原像的三次次数增长

取 $f\in N^\perp$。
由于 $e_0\in N$，有 $f_0=0$，所以 R238 的逐行形式方程有唯一解 $h$。
由 (1.6) 与 (5.2)，
$$
\mathsf P_qh=J_q^*f=\widetilde G_{F,q}^*f.
\tag{6.1}
$$
这是对两个有界层算子取通常伴随的等式。
我们没有给未知形式序列 $h$ 直接取全空间伴随。

由 (3.5) 得
$$
\boxed{
\|\mathsf P_qh\|
\le2C_Ge^{(q+2)^3}\|f\|\qquad(q\ge0).
}
\tag{6.2}
$$
特别，若 $f\in D=M\ominus N$，则 (6.2) 与两条方程
$$
Tf=0,\qquad T^*h=f\quad\text{逐行}
\tag{6.3}
$$
同时成立。

R238 的真实下界
$$
\|J_q\|\ge d_0/\alpha_q
$$
不受影响。该最坏全空间成本的对数有 $16^q$ 量级。
(6.2) 利用了 $f\perp N$，只控制 $J_q^*|_{N^\perp}$。
不能把它改写成 $\|J_q\|\le2C_Ge^{(q+2)^3}$。

本结论也没有证明 R234 原来的 $Gv-J_qv$ 总属于 $N$。
本稿使用的是 (3.4) 的另一个、对每个固定层有界的实际右逆。

## 7. 可合法使用的形式配对及长 carry 求和

定义稍强的次数测试空间
$$
\mathscr Y=
\left\{v:\|v\|_{\mathscr Y}
=\sum_{q\ge0}e^{(q+2)^3}\|\mathsf P_qv\|<\infty\right\}.
\tag{7.1}
$$
由 (6.2)，按孔层定义的配对
$$
\langle h,v\rangle
=\sum_{q\ge0}\langle\mathsf P_qh,\mathsf P_qv\rangle
$$
绝对收敛，且
$$
|\langle h,v\rangle|
\le2C_G\|f\|\,\|v\|_{\mathscr Y}.
\tag{7.2}
$$
这里的通常内积取第一变量线性；(7.2) 也只是在一个更强测试空间上的连续配对。

为后续能量分析记录一个真正的映射性质。
R234 的局部差分解为
$$
T=T^{[1]}+\sum_{L\ge1}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}},
\tag{7.3}
$$
其中 $K_L$ 只作用在前 $L+1$ 位，$T^{[1]}$ 是有限头加纯删除尾。
对固定 $p$，$T^{[1]}$ 将 $\mathcal H_{\le p}$ 送入某个固定有限次数空间；
粗略可取 $\mathcal H_{\le p+1}$。
而
$$
K_L\mathcal H_{\le p}\subset\mathcal H_{\le p+L+1}.
$$
对次数不超过 $b$ 的向量，
$$
\|v\|_{\mathscr Y}
\le\sqrt{b+1}\,e^{(b+2)^3}\|v\|.
$$
因此
$$
\sum_{L\ge1}\|K_L\|_{\mathcal H_{\le p}\to\mathscr Y}
\le
52\sum_{L\ge1}
\sqrt{p+L+2}\,
\exp\!\left((p+L+3)^3-770\,16^{L-1}\right)
<\infty.
\tag{7.4}
$$
这证明
$$
T:\mathcal H_{\le p}\longrightarrow\mathscr Y
\quad\text{有界，对每个固定 }p.
\tag{7.5}
$$
它并不证明 $T:\mathscr X\to\mathscr X$ 或 $T:\mathscr Y\to\mathscr Y$ 有界。

对有限整数支撑 $v$，$Tv$ 仍有限支撑，逐行方程给
$\langle h,Tv\rangle=\langle f,v\rangle$。
在 $\mathcal H_{\le p}$ 中取有限整数头逼近，并使用 (7.2)、(7.5)，得到合法延拓
$$
\boxed{
\langle h,Tv\rangle=\langle f,v\rangle
\qquad(v\in\mathcal H_{\le p},\ p<\infty).
}
\tag{7.6}
$$
因此新的次数界确实可以支付固定低输出层所涉及的长 carry，
也可用于有限次数测试的实际积分分部。
(7.6) 中的右边是普通 Hilbert 配对，左边是 (7.2) 的连续形式配对。

## 8. 尚不能作的能量推断

(6.2) 不意味着
$$
\sum_q\|\mathsf P_qh\|^2<\infty.
$$
因此，在尚未证明额外收敛前，不能把 $v=f$ 直接代入 (7.6)，
也不能从 $Tf=0$ 形式写成
$\langle h,Tf\rangle=\langle f,f\rangle$ 来推出 $f=0$。

长 carry 的次数下降可由 (7.4) 的超快误差支付。
但纯尾主项只在相邻孔次数之间传递；其截断边界项不带同样的超快系数。
此外，固定低位 carry 的算子范数虽小，却不能在所有次数上免费压过
$e^{(q+2)^3}$ 的增长。
进一步需要真正控制这种相邻次数通量，或构造在上述配对中可用的核内逼近。

本稿的确定结论是：**存在任意远高位构造的、落在每个指定 $\operatorname{Ran}B^r$
且模 $N$ 等于规范逆的逐层真实右逆；因此缺陷形式原像有统一的三次次数增长界。**
