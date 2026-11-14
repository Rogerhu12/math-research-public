# R91：准确 Hermite 中央行与全部深度的邻点 jets

日期：2026-11-12。状态：留数、必要性、整格及输入精度已根端独审。
证明见[真实邻点的 Hermite 中央行](../notes/2026-11-12-hermite-central-trace-and-full-depth-neighbor-jets.md)。

令 $d=p+1$，$\mathscr P_p=t^d+pA_p$ 是真实一级邻点 $r$ 的
Eisenstein 最小多项式。置
$$
m=M_e/t^4,\quad q=d-4,\quad
R_p=\left[K^d/(sJ^{d+1})\right]_{\le q}\in\mathbb Z_p[t].
$$
则 $C_d=[t^q](R_pm)$，$\Gamma_{i,p}=C_d/p\in\mathbb Z_p$。

## 1. 首层中心系数的真实邻点公式

取唯一整余式 $m_2=m\bmod\mathscr P_p^2$，$\deg m_2<2d$。
因为 $q<d$，$C_d\equiv[t^q](R_pm_2)\pmod{p^2}$。
实际有 $m_2(r)=m(r)$、$m_2'(r)=m'(r)$。
令
$$
W_p=\left(\mathscr P_p^2R_p/t^{q+1}\right)_+.
$$
无穷远展开与全部二阶极点留数给
$$
C_d\equiv\operatorname{Tr}_{B(r)/B}
\left\{
\frac{(W_pm)'(r)}{\mathscr P_p'(r)^2}
-\frac{W_p(r)m(r)\mathscr P_p''(r)}{\mathscr P_p'(r)^3}
\right\}\pmod{p^2}.
$$
完整迹除 $p$ 再模 $p$，准确得到 $\Gamma_{i,p}$。
整性来自完整留数与整多项式余式，不能逐项丢弃不同理想分母。

## 2. 点值确实丢失中央方向

取 $\Delta M=t^d\mathscr P_p(t)$。它在全部邻点为零，保留首项和已证整性，
但 $\Delta\Gamma_{i,p}=\mathscr P_p(0)/p$ 为单位。
所以仅乘邻点值的任何迹权，都不能在这个整函数空间上普遍恢复中央行。
第一导数恰检测这个核方向。扰动未保留实际 Hecke 特征，不是对原曲线的反例。

## 3. Hermite 格的准确代价

Hasse jets 映射
$$
\mathcal O_B[t]/\mathscr P_p^e\longrightarrow\mathcal O_{B(r)}^e,\qquad
f\longmapsto(f(r),f^{[1]}(r),\ldots,f^{[e-1]}(r))
$$
的余核长度准确为 $\binom e2(d-1)$。
采用 $\mathscr P_p^kt^a$ 基，对角块为乘 $\mathscr P_p'(r)^k$，
再用驯分歧不同理想即得。首层 $e=2$ 的长度为 $p$。
相容整数据满足
$b(r)=(m'(r)-a_0'(r))/\mathscr P_p'(r)\in\mathcal O_{B(r)}$，
并有 $m_2=a_0+\mathscr P_pb_0$。
在同一固定整基或相容有限环中，模 $p^3$ 的数据足够恢复 $\Gamma\bmod p$。

## 4. 完整证书所需的模函数输入

整除法给 $t^{d(e+N-1)}\in(\mathscr P_p^e,p^N)$；
当 $e\ge N+\lfloor D'/d\rfloor$ 时，该余类决定原点到次数 $D'$ 的模 $p^N$ jet。
对 R81 取
$$
N_n=4n+3,\quad D_n=\min\{dp^n,2dN_n+4\},\quad
e_n=N_n+\lfloor(D_n-4)/d\rfloor\le3N_n.
$$
原 $m$ 在同一真实邻点轨道上的 $e_n-1$ 阶 jets，
连同已核定的整格精度，决定完整证书的全部 $M_e$ 输入。
真实 GM 矩阵输入及高权系数提取仍保持 R81 的要求。
准确中央比较已得到；跨素数非零仍须实际 Hecke 或其他全局约束。
